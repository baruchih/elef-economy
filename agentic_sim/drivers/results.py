"""Keeping results.

Two kinds, both under `agentic_sim/results/`:

  results/tests/<commit>[-dirty].txt   what `run_tests.py` printed, with the commit, date and
                                        Python version at the top. One file per commit; a rerun on
                                        the same commit overwrites it.
  results/runs/<run-id>/                one directory per run: `manifest.json` (what was run, on
                                        which engine, with which parameters and permitted
                                        operations, and how it ended), `metrics.csv` (the per-tick
                                        series the run chose to log), `fingerprint.json` (the
                                        History head and the readable consequences, as
                                        tests/test_perf_equivalence.py defines them).

The record on disk from record mode (gigabytes) is not kept here; the manifest names where it was
written and the History head commits to it. Results are written by the code and read by people;
the suite and the engine stay the authority.
"""
from __future__ import annotations
from dataclasses import asdict
import csv
import datetime as _dt
import json
import os
import platform
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
RESULTS = os.path.join(os.path.dirname(HERE), "results")


def git_commit() -> str:
    """Short hash of HEAD, with `-dirty` if the tree differs from it; `unknown` outside git."""
    try:
        root = os.path.dirname(HERE)
        h = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=root, capture_output=True,
                           text=True, check=True).stdout.strip()
        # results written by the code are not a change to the code
        dirty = subprocess.run(["git", "status", "--porcelain", "--", ".", ":!results"],
                               cwd=root, capture_output=True, text=True, check=True).stdout.strip()
        return h + ("-dirty" if dirty else "")
    except Exception:  # noqa: BLE001
        return "unknown"


def now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def environment() -> dict:
    return {"engine_commit": git_commit(), "python": platform.python_version(),
            "platform": platform.platform(), "argv": sys.argv}


def fingerprint(w) -> dict:
    """The History head and the readable consequences — the same fields the equivalence tests use,
    minus the per-wallet and per-case tuples, which the head already commits to."""
    states: dict[str, int] = {}
    for c in w.cases.values():
        states[c.state] = states.get(c.state, 0) + 1
    return {"head": w.history.head, "entries": len(w.history.entries), "events": len(w.ledger.events),
            "M": round(w.ledger.M, 6), "Res": round(w.ledger.Res, 6), "t": w.t,
            "cases": len(w.cases), "reviews": len(w.reviews), "states": dict(sorted(states.items()))}


class RunRecorder:
    """Writes one run's directory. Create it before the run with what is declared; call `tick`
    for each metrics row; `finish` with the world and whatever the run concluded."""

    def __init__(self, name: str, *, kind: str, params, declared: dict, root: str = RESULTS):
        stamp = _dt.datetime.now().strftime("%Y%m%d-%H%M%S")
        self.run_id = f"{stamp}-{name}"
        self.dir = os.path.join(root, "runs", self.run_id)
        env = environment()                       # before this run's own directory exists
        os.makedirs(self.dir, exist_ok=False)
        self._t0 = time.time()
        self.manifest = {
            "run_id": self.run_id, "name": name, "kind": kind, "started": now(),
            "environment": env,
            "params": asdict(params) if hasattr(params, "__dataclass_fields__") else dict(params),
            "declared": declared,          # actors, ticks, seed, permitted operations, what is not in the run
            "status": "running",
        }
        self._write_manifest()
        self._metrics_path = os.path.join(self.dir, "metrics.csv")
        self._metrics = None
        self._writer = None

    def _write_manifest(self):
        with open(os.path.join(self.dir, "manifest.json"), "w") as f:
            json.dump(self.manifest, f, indent=2, sort_keys=False, default=str)
            f.write("\n")

    def tick(self, row: dict):
        if self._writer is None:
            self._metrics = open(self._metrics_path, "w", newline="")
            self._writer = csv.DictWriter(self._metrics, fieldnames=list(row))
            self._writer.writeheader()
        self._writer.writerow(row)
        self._metrics.flush()

    def note(self, key: str, value):
        self.manifest[key] = value
        self._write_manifest()

    def finish(self, w, status: str = "completed", **conclusions):
        if self._metrics is not None:
            self._metrics.close()
        fp = fingerprint(w)
        with open(os.path.join(self.dir, "fingerprint.json"), "w") as f:
            json.dump(fp, f, indent=2)
            f.write("\n")
        self.manifest.update({"status": status, "finished": now(),
                              "elapsed_s": round(time.time() - self._t0, 1), "head": fp["head"], **conclusions})
        self._write_manifest()
        return self.dir

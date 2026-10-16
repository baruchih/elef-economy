"""A throughput run: how much of the loop the engine turns per second, and in how much memory.

There are no economics in it. Every reviewer stamps F at zero cost, every actor is funded far
beyond what it can lose, every task is accepted by protocol default — the simplest permitted
path, posted → awarded → submitted → reviewed F → window → vested, repeated. It measures the
engine, not the rules, and its results say nothing about strategies.

    python3 -m drivers.load_run --actors 200 --ticks 10000 --on-duty 40 --tasks 30 --record-dir /path

Results go to results/runs/<run-id>/ (drivers/results.py).
"""
from __future__ import annotations
import argparse
import os
import resource
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sim import Params, World, check_all          # noqa: E402
from sim.engine import F                          # noqa: E402
from drivers.results import RunRecorder, fingerprint  # noqa: E402

PERMITTED = ["post_root (human H, beta 20)", "award (price 18, tau 1, chosen round-robin by availability)",
             "submit", "assign_initial (first free on-duty reviewer)", "complete_review F cost 0", "advance"]
NOT_IN_RUN = ["bids", "N/P/⊥ verdicts", "responses", "appeals", "disputes", "audits", "rulings", "overrides",
              "delegation", "cancellation", "resource spend", "human reactions", "any policy"]


def rss_mb() -> float:
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2 ** 20


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--actors", type=int, default=20)
    ap.add_argument("--ticks", type=int, default=1000)
    ap.add_argument("--on-duty", type=int, default=4)
    ap.add_argument("--tasks", type=int, default=3, help="new root tasks per tick, at most")
    ap.add_argument("--record-dir", default=None, help="record mode: write the record here")
    ap.add_argument("--log-every", type=int, default=100)
    ap.add_argument("--full-check-every", type=int, default=0)
    ap.add_argument("--name", default=None)
    a = ap.parse_args(argv)

    actors = [f"a{i:03d}" for i in range(a.actors)]
    p = Params(Res0=1e9, X=a.on_duty, float_per_actor=5000.0, record_dir=a.record_dir,
               full_check_every=a.full_check_every)
    name = a.name or f"load-{a.actors}x{a.ticks}" + ("-record" if a.record_dir else "-memory")
    rec = RunRecorder(name, kind="load run — engine throughput and memory; no economics, no policies",
                      params=p,
                      declared={"actors": a.actors, "on_duty": a.on_duty, "tasks_per_tick": a.tasks, "ticks": a.ticks,
                                "humans": {"H": 5e8}, "seed": None, "randomness": "none: deterministic drive",
                                "permitted_operations": PERMITTED, "not_in_run": NOT_IN_RUN,
                                "record_dir": a.record_dir,
                                "checks": {"per_tick": "check_tick after every tick — always; not configurable",
                                           "full_audit_every_n_ticks": a.full_check_every or "not scheduled",
                                           "final_full_audit": "check_all after the last tick; outcome in full_audit"}})
    w = World(p, actors, humans={"H": 5e8}, on_duty=actors[:a.on_duty])
    t0 = time.time()
    last_t, last_time = 0, t0
    for t in range(1, a.ticks + 1):
        posted = 0
        for aid in actors:
            act = w.actors[aid]
            if posted < a.tasks and not act.on_duty and act.committed is None and act.open_review is None \
                    and w.ledger.wallet(aid).U >= 9:
                q = w.post_root("H", 20)
                w.award(q, aid, 18, 1)
                posted += 1
        for c in list(w._live_cases.values()):
            if c.state == "COMMITTED" and t >= c.t_award + 1:
                w.submit(c.id)
            if c.state == "SUBMITTED":
                rv = [x for x in actors if w.actors[x].on_duty and w.actors[x].open_review is None
                      and w.ledger.wallet(x).U >= 5]
                if rv:
                    w.complete_review(w.assign_initial(c.id, rv[0]), F, 0)
        w.advance(t)
        if t % a.log_every == 0 or t == a.ticks:
            nowt = time.time()
            row = {"t": t, "ticks_per_s": round((t - last_t) / max(nowt - last_time, 1e-9), 1),
                   "cases": len(w.cases), "live_cases": len(w._live_cases), "reviews": len(w.reviews),
                   "events": len(w.ledger.events), "entries": len(w.history.entries),
                   "M": round(w.ledger.M, 3), "Res": round(w.ledger.Res, 3), "maxrss_mb": round(rss_mb(), 1)}
            if a.record_dir:
                row["resident_cases"] = len(w.cases.resident_items())
                row["resident_reviews"] = len(w.reviews.resident_items())
            rec.tick(row)
            print(f"t={t} {row['ticks_per_s']} ticks/s cases={row['cases']} live={row['live_cases']} "
                  f"maxrss={row['maxrss_mb']} MB", flush=True)
            last_t, last_time = t, nowt
    run_s = time.time() - t0
    print(f"run: {run_s:.1f}s, {a.ticks / run_s:.0f} ticks/s, maxrss {rss_mb():.0f} MB; full audit…", flush=True)
    t1 = time.time()
    try:
        check_all(w)
        audit = {"full_audit": "passed", "full_audit_s": round(time.time() - t1, 1)}
    except AssertionError as e:                      # InvariantError is an AssertionError
        audit = {"full_audit": f"FAILED: {e}", "full_audit_s": round(time.time() - t1, 1)}
    fp = fingerprint(w)                              # before close: in record mode it reads the archive
    on_disk = None
    if a.record_dir:
        w.close()
        on_disk = {f: os.path.getsize(os.path.join(a.record_dir, f)) for f in sorted(os.listdir(a.record_dir))}
    out = rec.finish(fp=fp, status="completed" if audit["full_audit"] == "passed" else "audit failed",
                     run_s=round(run_s, 1), ticks_per_s=round(a.ticks / run_s, 1), maxrss_mb=round(rss_mb(), 1),
                     record_bytes=on_disk, **audit)
    print(f"{audit['full_audit']} in {audit['full_audit_s']}s; results in {os.path.relpath(out)}")
    return 0 if audit["full_audit"] == "passed" else 1


if __name__ == "__main__":
    sys.exit(main())

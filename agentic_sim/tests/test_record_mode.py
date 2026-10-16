"""Record mode: the record on disk, the working set in memory, the same engine.

Through the performance pass the engine kept every History entry, ledger event, case and
review in RAM for the whole run — about sixteen kilobytes per case — so a long run was bounded
by memory before time. With `Params.record_dir` set (sim/record.py) the History and the event
copy are written through to files, settled cases and reviews are paged out to archives, and
RAM holds the working set. This is an engineering change under spec §19: it moves where the
record lives, never what the engine does. This file is that claim in test form:

  1. The seeded random scenario of test_perf_equivalence, run in record mode with the full
     audit after every tick, ends in the identical fingerprint to the in-memory run and to the
     v1.0.1 engine's golden; only the live cases are resident at the end.
  2. The record on disk is complete and independently verifiable: the chain re-hashes from
     genesis from the file alone, and ends at the engine's head.
  3. A paged-out case comes back when the engine touches it, with its History positions, and
     the full audit still holds; an engine-caused violation on a paged-out case is caught by
     both checks, as in memory.
  4. The working set and the resident set stay bounded while the record grows.
  5. The Journal behaves as the list it replaces across its in-memory tail boundary.
"""
import hashlib
import json
import os
import shutil
import sys
import tempfile

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
try:
    import pytest
except ImportError:
    sys.path.insert(0, os.path.dirname(__file__))
    from _mini_pytest import pytest

from sim import Params, World, InvariantError, check_all, check_tick
from sim.engine import F, N
from sim.record import Journal
from test_perf_equivalence import ACTORS, GOLDEN, scenario, fingerprint, _states


def _tmp():
    return tempfile.mkdtemp(prefix="agentic_record_")


def _verify_file(path: str) -> tuple[str, int]:
    """Re-hash the chain from the file alone; return (head, entries)."""
    prev = hashlib.sha256(b"genesis").hexdigest()
    n = 0
    with open(path, "rb") as f:
        for n, line in enumerate(f, 1):
            e = json.loads(line)
            body = json.dumps({"seq": e["seq"], "kind": e["kind"], "payload": e["payload"], "prev": prev},
                              sort_keys=True, default=str)
            assert e["seq"] == n - 1 and e["prev"] == prev
            assert hashlib.sha256(body.encode()).hexdigest() == e["hash"]
            prev = e["hash"]
    return prev, n


@pytest.mark.parametrize("seed", [1, 2])
def test_record_mode_reproduces_the_in_memory_run_and_the_golden(seed):
    rd = _tmp()
    try:
        w = scenario(seed, 200, audit_every=1, record_dir=rd)     # check_all after every tick, on the files
        fp = fingerprint(w)
        assert fp == fingerprint(scenario(seed, 200))                # the in-memory engine, whole fingerprint
        g = GOLDEN[seed]                                            # the v1.0.1 engine
        assert fp["head"] == g["head"] and fp["entries"] == g["entries"]
        assert fp["M"] == g["M"] and fp["Res"] == g["Res"] and _states(w) == g["states"]
        # paging happened, and what is resident is exactly the working set
        resident = {cid for cid, _ in w.cases.resident_items()}
        assert resident == set(w._live_cases) and len(resident) < len(w.cases)
        assert all(w.cases.is_resident(r.case) for _, r in w.reviews.resident_items())
        head, entries = w.history.head, len(w.history.entries)
        w.close()
        # the record on disk is the whole chain, verifiable without the engine
        assert _verify_file(os.path.join(rd, "history.jsonl")) == (head, entries)
        with open(os.path.join(rd, "events.jsonl"), "rb") as f:
            assert sum(1 for _ in f) == fp["events"]
    finally:
        shutil.rmtree(rd, ignore_errors=True)


def _vest_one(w):
    q = w.post_root("H", 20)
    w.award(q, "a05", 18, 3)
    w.advance(1)
    w.submit(q)
    r = w.assign_initial(q, "a00")
    w.complete_review(r, F, 0)
    w.advance(w.t + w.p.W + 1)
    assert w.cases[q].state == "VESTED"
    w.advance(w.t + 1)                                              # settled: leaves the working set
    return q, r


def test_paged_out_case_comes_back_when_touched():
    rd = _tmp()
    try:
        w = World(Params(record_dir=rd), ACTORS, humans={"H": 1000.0}, on_duty=ACTORS[:4])
        q, r = _vest_one(w)
        assert q not in w._live_cases and not w.cases.is_resident(q) and not w.reviews.is_resident(r)
        assert q in w.cases and r in w.reviews and q not in w._case_entries
        copy = w.cases.peek(q)                                      # an audit's read: a copy, still not resident
        assert copy.state == "VESTED" and len(copy.log) > 0 and not w.cases.is_resident(q)
        before = fingerprint(w)
        w.override(q, "H", N)                                       # a human corrects the settled outcome
        assert w.cases.is_resident(q)
        assert w._case_entries[q] == [entry[2] for entry in w.cases[q].log]
        w.advance(w.t + 1)
        check_all(w)
        after = fingerprint(w)
        assert after["head"] != before["head"] and after["entries"] > before["entries"]
        # the same actions in memory give the same world
        m = World(Params(), ACTORS, humans={"H": 1000.0}, on_duty=ACTORS[:4])
        _vest_one(m)
        m.override(q, "H", N)
        m.advance(m.t + 1)
        assert fingerprint(m) == after
        w.close()
    finally:
        shutil.rmtree(rd, ignore_errors=True)


def test_violation_on_a_paged_out_case_is_caught_by_both_checks():
    rd = _tmp()
    try:
        w = World(Params(record_dir=rd), ACTORS, humans={"H": 1000.0}, on_duty=ACTORS[:4])
        q, _ = _vest_one(w)
        assert not w.cases.is_resident(q)
        w.ledger.transfer("H", "a05", 1.0, case=q, note="late payment")   # money on account of a vested case (I10)
        with pytest.raises(InvariantError):
            check_all(w)
        with pytest.raises(InvariantError):
            check_tick(w)
        w.close()
    finally:
        shutil.rmtree(rd, ignore_errors=True)


def test_resident_set_stays_bounded_while_the_record_grows():
    rd = _tmp()
    try:
        w = World(Params(Res0=1e6, record_dir=rd), ACTORS, humans={"H": 5e5}, on_duty=ACTORS[:4])
        sizes = []
        for t in range(1, 301):
            for a in ACTORS:
                act = w.actors[a]
                if not act.on_duty and act.committed is None and act.open_review is None and w.ledger.wallet(a).U >= 9:
                    q = w.post_root("H", 20)
                    w.award(q, a, 18, 1)
            for c in list(w._live_cases.values()):
                if c.state == "COMMITTED" and t >= c.t_award + 1:
                    w.submit(c.id)
                if c.state == "SUBMITTED":
                    rv = [a for a in ACTORS if w.actors[a].on_duty and w.actors[a].open_review is None
                          and w.ledger.wallet(a).U >= 5]
                    if rv:
                        w.complete_review(w.assign_initial(c.id, rv[0]), F, 0)
            w.advance(t)
            sizes.append((len(w._live_cases), len(w.cases.resident_items()), len(w.reviews.resident_items())))
        assert len(w.cases) > 1000
        assert max(s[1] for s in sizes[150:]) <= max(s[1] for s in sizes[:150]) + 5
        assert all(res <= live + 5 for live, res, _ in sizes)
        assert len(w.ledger.pools) <= len(w.cases.resident_items()) + 5      # empty pools left with their cases
        check_all(w)
        w.close()
        assert os.path.getsize(os.path.join(rd, "cases.pickle")) > 0
    finally:
        shutil.rmtree(rd, ignore_errors=True)


def test_journal_reads_like_the_list_it_replaces():
    rd = _tmp()
    try:
        j = Journal(os.path.join(rd, "j.txt"), encode=str, decode=int, tail=3)
        for i in range(10):
            j.append(i)
        assert len(j) == 10 and list(j) == list(range(10)) and list(j.iter_from(5)) == [5, 6, 7, 8, 9]
        assert j[0] == 0 and j[9] == 9 and j[-1] == 9 and j[-10] == 0
        assert j[2:7] == [2, 3, 4, 5, 6] and j[8:] == [8, 9] and j[7:100] == [7, 8, 9] and j[::4] == [0, 4, 8]
        with pytest.raises(IndexError):
            j[10]
        j.append(10)                                                 # across a tail trim
        assert j[-1] == 10 and j[3] == 3 and len(j) == 11
        j.close()
    finally:
        shutil.rmtree(rd, ignore_errors=True)

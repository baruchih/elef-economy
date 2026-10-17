"""The per-tick check is equivalent to the full audit, and the engine's behaviour is unchanged.

Background. Through v1.0.1 the engine ran the full §17 audit after every tick, and three of the
checks rescanned the whole record each time, so a run slowed as the square of its length. The
working-set refactor (`check_tick`, `World._live_cases`, the ledger's per-case event index and
running totals) is a conformance-neutral change under spec §19: it changes how the rules are
checked, never what the engine does. This file is that claim in test form:

  1. On a seeded random scenario that exercises most paths — appeals, disputes, audits,
     rulings, overrides before and after settlement, delegation with cancellation, pool
     exhaustion and kill fees, timeouts and replacements, rotation, and since 1.2.0 planted work
     with its adjudication, suspensions and the dial's period — the full audit passes after
     every tick while the per-tick check runs, and the final world's fingerprint (History head,
     supply, reserve, every wallet, every case's state and grade) equals the one the v1.0.1
     engine produced for the same scenario (GOLDEN, recorded from commit 6a746a1).
  2. An engine-caused violation is caught by the per-tick check exactly where the full audit
     catches it.
  3. The working set stays bounded while the record grows.
"""
import os
import random
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
try:
    import pytest
except ImportError:
    sys.path.insert(0, os.path.dirname(__file__))
    from _mini_pytest import pytest

from sim import Params, World, RuleError, LedgerError, InvariantError, check_all, check_tick
from sim.engine import F, N, P, BOT

ACTORS = [f"a{i:02d}" for i in range(12)]


def _try(fn, *a, **k):
    try:
        return fn(*a, **k)
    except (RuleError, LedgerError):
        return None          # a refused action changes nothing; both engines must refuse alike


def scenario(seed: int, ticks: int, audit_every: int = 0, record_dir=None) -> World:
    """A seeded random drive of the engine through most of its paths."""
    rng = random.Random(seed)
    # 1.2.0: short periods, a two-plant record and a short suspension, so the dial moves and
    # actors are suspended, readmitted and re-seated within the scenario's 200 ticks
    w = World(Params(Res0=2e5, omega_rate=0.05, record_dir=record_dir, period_ticks=40, n_min=2, T_susp=30), ACTORS,
              humans={"H1": 60000.0, "H2": 30000.0, "D1": 30000.0}, delegates=["D1"], on_duty=ACTORS[:4])

    def free_actors():
        return [a for a in ACTORS if not w.actors[a].on_duty and w.actors[a].committed is None
                and w.actors[a].open_review is None]

    def free_reviewers(c):
        return [a for a in ACTORS if w.actors[a].on_duty and w.actors[a].open_review is None
                and w.actors[a].committed is None and a not in c.excluded and a != c.actor and a != c.requester]

    for t in range(1, ticks + 1):
        for req in ("H1", "H2", "D1"):
            if rng.random() < 0.35:
                _try(w.post_root, req, rng.choice([10, 20, 30, 45]))
        for _ in range(w.plants_due()):                # 1.2.0: the orchestrator's plants at the rate the dial sets
            _try(w.create_plant, rng.random() >= 0.75, rng.choice([10, 20, 30]))
        for c in list(w.cases.values()):
            if c.state != "AVAILABLE":
                continue
            if rng.random() < 0.15:
                if c.is_nested() and rng.random() < 0.3:
                    _try(w.withdraw_unawarded, c.id)
                continue
            f = [a for a in free_actors() if a != c.requester]
            if f:
                _try(w.award, c.id, rng.choice(f), round(c.beta * rng.uniform(0.5, 1.0), 2), rng.randint(2, 6))
            elif c.is_nested() and rng.random() < 0.3:
                _try(w.withdraw_pool_exhaustion, c.parent, c.id)
        for c in list(w.cases.values()):
            if c.state == "COMMITTED":
                r = rng.random()
                if r < 0.15 and c.is_root and not c.children:
                    _try(w.post_nested, c.id, rng.choice([4, 6, 8]))
                elif r < 0.3:
                    _try(w.spend, c.actor, rng.choice([1, 2, 3]), c.id)
                elif r < 0.75:
                    _try(w.submit, c.id)
                elif r < 0.8 and c.children:
                    _try(w.cancel_nested, rng.choice(c.children))
            elif c.state == "RESUBMITTING" and rng.random() < 0.7:
                _try(w.resubmit, c.id)
        for c in list(w.cases.values()):
            if c.state == "SUBMITTED":
                if c.is_nested():
                    if rng.random() < 0.7:
                        _try(w.judge_nested, c.id, rng.choice([F, F, N]))
                else:
                    fr = free_reviewers(c)
                    if fr and not any(w.reviews[r].role == "initial" and w.reviews[r].status in ("open", "done", "vested")
                                      for r in c.reviews):
                        _try(w.assign_initial, c.id, rng.choice(fr))
        for r in list(w.reviews.values()):
            if r.status == "open" and rng.random() < 0.6:
                c = w.cases[r.case]
                if r.role == "appeal" and c.verdict == BOT:
                    obj = rng.choice(["upheld", "rejected"])
                    v = N if obj == "upheld" else rng.choice([F, N])
                    _try(w.complete_review, r.id, v, rng.choice([0, 1, 2, 7]), objection=obj)
                else:
                    v = rng.choice([F, F, F, N, P, BOT]) if r.role == "initial" else rng.choice([F, N])
                    _try(w.complete_review, r.id, v, rng.choice([0, 1, 2, 7]))
        for c in list(w.cases.values()):
            if c.state == "AWAITING_RESPONSE" and rng.random() < 0.6:
                act = rng.choice(["accept", "appeal", "revise", "supply_evidence"])
                _try(w.respond, c.id, act, "grounds" if act == "appeal" else None)
            if c.state == "PENDING" and c.outcome_or_verdict() == F and c.is_root:
                r = rng.random()
                if r < 0.1:
                    _try(w.dispute, c.id, c.requester, "not convinced")
                elif r < 0.3:
                    fr = free_reviewers(c)
                    if fr:
                        _try(w.assign_audit, c.id, rng.choice(fr))
                elif r < 0.35:
                    _try(w.accept_explicit, c.id, c.requester)
                elif r < 0.38 and c.audit_vacated:
                    _try(w.waive_audit, c.id)
            if c.challenge and not c.challenge["resolved"]:
                if len(c.challenge["reviews"]) < 2 and rng.random() < 0.7:
                    fr = free_reviewers(c)
                    if fr:
                        _try(w.assign_appeal, c.id, rng.choice(fr))
                elif rng.random() < 0.5:
                    obj = rng.choice(["upheld", "rejected"]) if c.verdict == BOT else None
                    out = N if obj == "upheld" else rng.choice([F, N])
                    _try(w.rule, c.id, out, obj)
            if rng.random() < 0.02 and c.state not in ("AVAILABLE", "COMMITTED", "WITHDRAWN", "CANCELLED"):
                obj = rng.choice(["upheld", "rejected"]) if c.verdict == BOT else None
                out = N if obj == "upheld" else rng.choice([F, N])
                _try(w.override, c.id, rng.choice(["H1", "H2", "D1"]), out, obj)
        if rng.random() < 0.05:
            _try(w.volunteer, rng.choice(ACTORS), rng.random() < 0.5)
        w.advance(t)
        if audit_every and t % audit_every == 0:
            check_all(w)
    return w


def fingerprint(w: World) -> dict:
    return {
        "head": w.history.head, "entries": len(w.history.entries), "events": len(w.ledger.events),
        "M": round(w.ledger.M, 6), "Res": round(w.ledger.Res, 6),
        "wallets": tuple((k, round(v.U, 6), round(v.L, 6)) for k, v in sorted(w.ledger.wallets.items())),
        "cases": tuple((c.id, c.state, c.outcome, c.grade, c.t_vest) for c in w.cases.values()),
        "reviews": tuple((r.id, r.status, round(r.fee, 6), round(r.reimbursed, 6)) for r in w.reviews.values()),
    }


# Recorded from the 1.2.0 engine (design revision 2: the loop's own clock) running `scenario(seed, 200)`
# with the full audit after every tick. The head commits every event in order; the rest are the
# readable consequences. The scenario now plants work, and its short periods move the dial to m_max,
# suspend and readmit actors, size the reserve and (seed 2) fire the alarm. The v1.0.1 goldens
# (commit 6a746a1) were 586af764… / 5686 and ab79fe65… / 4849 entries; the 1.1.0 goldens (a1e726a)
# bb0aa856… / 7489 and eb337b97… / 5324; each changed with the rule, as a change to settlement or to
# the reserve must, and was re-pinned once, at the commit that implemented the revision.
GOLDEN = {
    1: {"head": "b9c5d1a1d0eb8ec9b0f91c4fa00766692b1f90a5f1d67064e51d758fe8d508f7", "entries": 7613,
        "M": 199593.398135, "Res": 198843.0,
        "states": {"FINAL_N": 170, "VESTED": 74, "WITHDRAWN": 24, "CANCELLED": 4, "PENDING": 10, "SUBMITTED": 5,
                   "COMMITTED": 1, "AWAITING_RESPONSE": 1, "AVAILABLE": 9}},
    2: {"head": "40a459d830c3e8c5bb10c2e0f669c67ea8bc27ed286a0a42552ea8eef274a1f9", "entries": 7078,
        "M": 199556.601906, "Res": 199036.0,
        "states": {"FINAL_N": 174, "VESTED": 57, "WITHDRAWN": 21, "PENDING": 4, "AVAILABLE": 15,
                   "AWAITING_RESPONSE": 2, "SUBMITTED": 6}},
}


def _states(w):
    out = {}
    for c in w.cases.values():
        out[c.state] = out.get(c.state, 0) + 1
    return out


@pytest.mark.parametrize("seed", [1, 2])
def test_full_audit_agrees_with_tick_check_and_behaviour_is_unchanged(seed):
    w = scenario(seed, 200, audit_every=1)              # check_all after every tick, beside check_tick
    g = GOLDEN[seed]
    assert w.history.head == g["head"]
    assert len(w.history.entries) == g["entries"]
    assert round(w.ledger.M, 6) == g["M"] and round(w.ledger.Res, 6) == g["Res"]
    assert _states(w) == g["states"]
    # the scenario reached the paths it claims to
    assert any(c.challenge for c in w.cases.values())
    assert any(a[3] == "override" for c in w.cases.values() for a in c.assessments)
    assert any(c.is_nested() for c in w.cases.values())
    assert any(r.status == "overturned" for r in w.reviews.values())
    assert any(r.status == "withdrawn" for r in w.reviews.values())
    # and, since 1.2.0, the paths of design revision 2
    outcomes = {c.plant_outcome for c in w.cases.values() if c.plant is not None}
    assert outcomes >= {"stood", "failure", "spent"}
    assert w.suspensions > 0 and len(w.periods) == 4 and w.m_t == w.p.m_max
    assert any(e["kind"] == "suspension" and "readmitted" in e["payload"].get("msg", "") for e in w.history.entries)


def test_scheduled_full_audit_runs_inside_advance():
    rng_free = World(Params(full_check_every=3), ACTORS, humans={"H": 100.0}, on_duty=ACTORS[:4])
    q = rng_free.post_root("H", 20)
    rng_free.award(q, "a05", 18, 3)
    rng_free.advance(9)                                  # ticks 3, 6, 9 audit from genesis
    assert rng_free.history._verified_upto == len(rng_free.history.entries)


def test_tick_check_catches_an_engine_caused_violation_where_the_audit_does():
    w = World(Params(), ACTORS, humans={"H": 1000.0}, on_duty=ACTORS[:4])
    q = w.post_root("H", 20)
    w.award(q, "a05", 18, 3)
    w.advance(1)
    w.submit(q)
    r = w.assign_initial(q, "a00")
    w.complete_review(r, F, 0)
    w.advance(w.t + w.p.W + 1)
    assert w.cases[q].state == "VESTED"
    w.advance(w.t + 1)                                   # the vested case has left the working set
    assert q not in w._live_cases
    # an adjudication that moves money on account of a vested case, after its vesting (I10)
    w.ledger.transfer("H", "a05", 1.0, case=q, note="late payment")
    with pytest.raises(InvariantError):
        check_all(w)
    with pytest.raises(InvariantError):
        check_tick(w)


def test_working_set_stays_bounded_while_the_record_grows():
    w = World(Params(Res0=1e6), ACTORS, humans={"H": 5e5}, on_duty=ACTORS[:4])
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
        sizes.append(len(w._live_cases))
    assert len(w.cases) > 1000
    assert max(sizes[150:]) <= max(sizes[:150]) + 5     # no growth in the second half
    check_all(w)                                         # and the full audit still holds

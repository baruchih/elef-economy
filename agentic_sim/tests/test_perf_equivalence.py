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
     engine produced for the same scenario (GOLDEN, recorded from commit 6a746a1; re-pinned once at each design
     revision's implementing commit — last for 2.1.0, the bank: the summons is a loan repaid from its return, the index is
     published once a period, a plant's pots are minted and destroyed, and the wall binds in this random drive, whose state
     deliveries fail far above a fifth, so the state retracts and 24 requests wait at the end of seed 1; and once more for 2.2.0, the rebate from income: the claims
     are paid at the period's close from the fee pool, which is a lock on Ω, so the summonses between arrive at different
     ticks and a few more loans are made; and once more for 2.3.0, the supply side: a nested request carries its own pots posted
     by the parent and settles them at its node's closure).
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
            truth, _B = rng.random() >= 0.75, rng.choice([10, 20, 30])
            _try(w.post_plant, truth)                   # 2.6.0: the plant goes through the market (its ceiling the engine's draw)
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
                    cost = 0 if w.is_troop(r.reviewer) else rng.choice([0, 1, 2, 7])   # 1.4.0: a troop's cost was purchased at summons
                    _try(w.complete_review, r.id, v, cost)
        for c in list(w.cases.values()):
            if c.state == "AWAITING_RESPONSE" and rng.random() < 0.6:
                act = rng.choice(["accept", "appeal", "revise", "supply_evidence"])
                _try(w.respond, c.id, act, "grounds" if act == "appeal" else None)
            if c.state == "PENDING" and c.outcome_or_verdict() == F and c.is_root:
                r = rng.random()
                if r < 0.1:
                    _try(w.dispute, c.id, c.requester, "not convinced")
                elif r < 0.3:
                    if not c.audit_obligation and not c.audit_vacated:
                        _try(w.roll_audit, c.id)                  # 1.4.0: the roll is an obligation; seated when a reviewer is free
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


# Recorded from the 1.6.0 engine (design revision 6: auto-scale) running `scenario(seed, 200)`
# with the full audit after every tick. The head commits every event in order; the rest are the readable
# consequences. The scenario plants work, moves the dial to m_max, suspends actors from the market, puts them
# on probation, pays the dial's raised tax out of the duty fund and (seed 2) fires the alarm. Earlier goldens:
# v1.0.1 (6a746a1) 586af764… / 5686 and ab79fe65… / 4849 entries; 1.1.0 (a1e726a) bb0aa856… / 7489 and
# eb337b97… / 5324; 1.2.0 (d40cde2) b9c5d1a1… / 7613 and 40a459d8… / 7078; 1.4.0 (f0779ac) 2b23701b… / 8220 and
# 1f5bf324… / 7876 (the 1.3.0 figures were re-pinned at 1.4.0 since the roll became an obligation and troops are
# summoned; at 1.5.0 the reserve counts refused demand, so the uplift paid — and the period record — change; 1.5.0
# (01b75e2) 89a9b62d… / 8172 and 9462aea8… / 7876; at 1.6.0 the clock pays rebates from Ω, Ω backs the fund above a
# plant reserve, the reserve seats the queue and panels need a determined record, so the scenario's path changes; 1.6.0
# (195896a) a49c2c9e… / 8154 and 1d052569… / 6159; at 1.7.0 the troop account pays its surplus to Ω instead of the reviewers'
# uplift and the members' cap is two thirds, so the scenario's seating and settlement change; 1.7.0 (003a238) cb1ea471… / 7817
# and 1a568fcd… / 4309; at 1.7.1 the award summons is read per request — the requests past w_A beyond the free fundable
# members are the state's — a conformance correction, so the scenario summons where one free member used to block; 1.7.1
# (8d9b866) 51a3ac39… / 7164 and 2f47e98b… / 4027; at 2.0.0 the price of work — no backing (M is the floats, Ω and the
# requesters' wallets, Res 0), every nominal indexed by the price level the scenario's awards set, the pay-in locked at
# posting, Ω creating for its summonses and rebates and retiring from its inflows, the state at cost, N_T — so the whole
# path changes; 2.0.0 (…) ef0b9ac5… / 8650 and b1ab78fa… / 9267 carried through 2.1.0–2.3.0 as those revisions re-pinned in turn; at 2.4.0 the
# award pass gathers only requests at or above the state's price — the 1.7.1 conformance correction made at acceptance — so the
# scenario's below-market requests no longer hold a member's slot and the summonses fall differently (the floor itself never binds
# here: B̄ is 13–21 throughout, no summons declined for it)). Each
# changed with the rule, as a change to settlement, the reserve or membership must, and was re-pinned once, at the
# implementing commit.
GOLDEN = {
    # re-pinned once at 2.6.0 (design revision 14, the plant's disguise): the scenario's plants go through the market — posted, bid on,
    # awarded on the report, submitted at a drawn tick — so every fingerprint moves; the previous pins (2.4.0) are in the History of this file
    # seed 1 re-pinned with the Appendix S ruling after run 21 (the same day, the same revision): the p_T path follows the summons pass's
    # refusals, and this scenario refuses nineteen plants for credit; seed 2 meets no refusal and is unchanged
    1: {"head": "9e3fbbd157e3016205a533466d37531f0d506bd92f7fd0095bcea9388b393507", "entries": 8979,
        "M": 120321.776243, "Res": 0.0,
        "states": {"FINAL_N": 178, "VESTED": 55, "WITHDRAWN": 10, "PENDING": 3, "SUBMITTED": 4, "AVAILABLE": 5}},
    2: {"head": "843ad30458e29c2ba90ac194e6aa86084f8b1d73868c4a85a44c7939206264c8", "entries": 9756,
        "M": 120027.852558, "Res": 0.0,
        "states": {"FINAL_N": 200, "VESTED": 61, "WITHDRAWN": 17, "PENDING": 4, "AVAILABLE": 5, "AWAITING_RESPONSE": 1, "SUBMITTED": 1, "COMMITTED": 3}},
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
    assert w.suspensions > 0 and len(w.periods) == 4 and w.m_t >= 3.0        # the dial rose (both seeds end at 4.0 under 2.0.0)
    # 1.3.0/1.4.0: the troops' wallet's flows reconcile (I23); 1.7.0: that wallet is the troop account, and the uplift fund
    # is the raised tax received less the uplift paid
    # 2.0.0: the troops' wallet is Ω itself and the reserves are retired; Ω created for its summonses and rebates (I28)
    assert w.fund_in > 0 and w.p.floating and w.troop_wallet == w.ledger.OMEGA and w.R_T == 0
    # and, since 2.1.0, the bank's: loans made and repaid, debt from the drive's failed state deliveries, the wall reached in this
    # random drive (its state deliveries fail far above a fifth), the index published at the boundaries, a plant's pots minted
    assert w.bank_on and w.deficit_created == 0 and w.bank_minted["loan"] >= w.bank_destroyed["repayment"] >= 0
    assert w.debt_created >= 0 and w.troop_refused_credit_seats == 0
    assert w.bank_minted["mint_plant"] > 0 and w.bank_destroyed["retire_plant"] > 0 and w._P_published_at is not None
    assert w.pool_on and w.rebates_paid > 0 and not w.omega_liabilities and w.liabilities_accrued == 0     # 2.2.0: the pool, no stock
    assert w.supply_on and w.parent_pots and any(c.own_pots for c in w.cases.values()) and any(c.node_closed for c in w.cases.values())   # 2.3.0
    assert abs(w.ledger.wallet("DUTY-FUND").W - (w.fund_in - w.fund_out)) < 1e-6
    assert w.ledger.wallet(w.troop_wallet).W + w.troop_surplus_paid > 0          # the troops earned, and it is the state's


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

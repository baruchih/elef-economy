"""Design revision 10 — the rebate from income (2.2.0): §2.1 the claim recorded at the stop, the measure of lateness, r_s indexed
when stated (the conformance correction); §2.2 Ω's fee income after the debt pooled as a lock on Ω — fee events only, never the
returns of capital — untouched until the close, where the period's claims are paid pro rata and the rest is forgone and read, the
remainder released to Ω; no liability stock, nothing owed across a close; I32, I30 and I26 amended, I10's note.
"""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
try:
    import pytest
except ImportError:  # plain `python3 run_tests.py`
    sys.path.insert(0, os.path.dirname(__file__))
    from _mini_pytest import pytest

from sim import Params, World, Ledger, check_all
from sim.engine import F, N
from sim.invariants import InvariantError

ACTORS = ["A", "B", "C", "D", "E", "F"]
DUTY = ["C", "D", "E", "F"]


def make_world(budget=1000.0, actors=ACTORS, duty=DUTY, **over):
    # 2.2.0 defaults (the bank and the pool on); no emission, the service fee on, no plants, long turns, a short service target
    kw = dict(E0=0.0, H=1e9, omega_rate=0.05, Omega0=0.0, duty_turn_reviews=10_000, duty_turn_ticks=100_000,
              r_s=1.0, T_s=2, pi0=0.0, period_ticks=12)
    kw.update(over)
    return World(Params(**kw), actors, humans={"H": budget}, on_duty=duty)


def post_and_award(w, actor, B, beta=None, tau=500):
    q = w.post_root("H", beta if beta is not None else B)
    w.award(q, actor, B, tau)
    return q


def two_awards_then_a_summons(w, beta=30):
    """Two members awarded at 10 for two ticks (they lapse at tick 2), then a request nobody is free for at tick 1's seating."""
    post_and_award(w, "A", 10, tau=2)
    post_and_award(w, "B", 10, tau=2)
    q = w.post_root("H", beta)
    w.advance(w.t + 2)
    return q


def pool_lock(w):
    return w.ledger.lock_record(Ledger.OMEGA, f"pool:{w.pool_index}")


def test_fees_are_pooled_as_a_lock_on_Omega_and_the_returns_of_capital_are_not():
    w = make_world(T_s=10_000, period_ticks=50)      # no close inside the test
    L = w.ledger
    post_and_award(w, "A", 10, tau=2)                 # the base fee 0.5 is income: pooled, locked
    assert w.omega_pool == pytest.approx(0.5) and pool_lock(w) == pytest.approx(0.5)
    assert L.wallet(Ledger.OMEGA).U == pytest.approx(0.0) and L.wallet(Ledger.OMEGA).L == pytest.approx(0.5)
    post_and_award(w, "B", 10, tau=2)
    q = w.post_root("H", 30)
    w.advance(w.t + 2)                                # a summons: Ω's unlocked balance is zero, so the bank lends cost + G in full
    c = w.cases[q]
    assert w.is_troop(c.actor) and w.loans[c.actor]["amount"] == pytest.approx(7.0 + 5.0)
    assert w.omega_pool == pytest.approx(1.5)         # the summons's own fee joined the pool
    w.submit(q)
    r = w.assign_initial(q, "C")
    w.complete_review(r, F, 0)
    w.advance(w.cases[q].window_end + 1)
    assert w.cases[q].state == "VESTED" and w.loans == {}
    # the price 10 and the guarantee 5 came back: 12 repaid the loan, 3 — the delivery's surplus — is Ω's unlocked, not the pool's
    assert L.wallet(Ledger.OMEGA).U == pytest.approx(3.0) and w.omega_pool == pytest.approx(1.5)
    assert all(e.kind != "creation" for e in L.events) and w.omega_liabilities == []
    check_all(w)


def test_a_claim_is_recorded_at_the_stop_and_paid_at_the_close_from_the_pool_only():
    w = make_world()
    L = w.ledger
    q = two_awards_then_a_summons(w)                  # the state's delivery; Ω's fees 1.5 in the pool
    c = w.cases[q]
    w.advance(c.deadline + 1)                         # nobody submits: final N at tick 3 with no verdict — the clock stops, 1 tick late
    assert c.state == "FINAL_N" and c.late_ticks == 1 and c.rebate_owed == pytest.approx(1.0)
    assert c.rebate_paid == 0 and w.rebates_paid == 0 and w.omega_liabilities == [] and w.liabilities_accrued == 0
    assert w.period["claims"] == [(q, "H", pytest.approx(1.0))] and w.period["claims_total"] == pytest.approx(1.0)
    assert w.debt == pytest.approx(12.0) and L.wallet(Ledger.OMEGA).U == pytest.approx(0.0)   # the loan became debt; the pool is locked, not Ω's
    assert w.omega_pool == pytest.approx(1.5) and pool_lock(w) == pytest.approx(1.5)
    check_all(w)
    h_before = L.wallet("H").U
    w.advance(13)                                     # the boundary (the tick numbered 12): the close
    rec = w.periods[-1]
    assert c.rebate_paid == pytest.approx(1.0) and c.rebate_forgone == pytest.approx(0.0) and c.rebate_settled_at == 12
    assert L.wallet("H").U == pytest.approx(h_before + 1.0)
    assert any(e.kind == "transfer" and e.note == "rebate (settled at the period's close)" and e.case == q for e in L.events)
    assert rec["claims"] == pytest.approx(1.0) and rec["pool"] == pytest.approx(1.5) and rec["rebates_paid"] == pytest.approx(1.0)
    assert rec["rebates_forgone"] == 0 and rec["forgone_share"] == 0 and rec["omega_retained_period"] == pytest.approx(0.5)
    assert w.omega_pool == 0 and pool_lock(w) == 0 and w.pool_index == 1
    assert w.debt == pytest.approx(11.5)              # the remainder 0.5 was an inflow like any other: the debt first
    check_all(w)


def test_claims_above_the_pool_are_paid_pro_rata_and_the_rest_forgone_never_carried():
    w = make_world(T_s=1)
    L = w.ledger
    # two member deliveries that lapse at their deadlines: two claims, each capped at B = 10 (deadline 4 → late 3 at r_s 1 → 3 each)
    qa = post_and_award(w, "A", 10, tau=4)
    qb = post_and_award(w, "B", 10, tau=4)
    w.advance(5)
    ca, cb = w.cases[qa], w.cases[qb]
    assert ca.state == cb.state == "FINAL_N" and ca.rebate_owed == pytest.approx(3.0) and cb.rebate_owed == pytest.approx(3.0)
    assert w.period["claims_total"] == pytest.approx(6.0) and w.omega_pool == pytest.approx(1.0)   # two fees of 0.5
    w.advance(13)                                     # the close: a pool of 1.0 against claims of 6.0 — a sixth each
    rec = w.periods[-1]
    assert ca.rebate_paid == pytest.approx(0.5) and cb.rebate_paid == pytest.approx(0.5)
    assert ca.rebate_forgone == pytest.approx(2.5) and cb.rebate_forgone == pytest.approx(2.5)
    assert rec["rebates_paid"] == pytest.approx(1.0) and rec["rebates_forgone"] == pytest.approx(5.0)
    assert rec["forgone_share"] == pytest.approx(5.0 / 6.0) and rec["omega_retained_period"] == pytest.approx(0.0)
    assert w.rebates_forgone == pytest.approx(5.0) and w.omega_liabilities == [] and w.liabilities_accrued == 0
    assert w.rebates_owed == pytest.approx(w.rebates_paid + w.rebates_forgone)         # nothing owed across the close
    assert all(e.kind not in ("creation", "loan") or e.note != "loan: rebate" for e in L.events)
    check_all(w)
    # the next period starts clean: no claim, no pool, the forgone part is never revisited
    assert w.period["claims"] == [] and w.omega_pool == 0
    w.advance(25)
    assert w.periods[-1]["claims"] == 0 and ca.rebate_paid == pytest.approx(0.5)
    check_all(w)


def test_the_pool_is_not_Omegas_unlocked_balance_and_funds_no_summons():
    w = make_world(T_s=10_000, period_ticks=50)      # no close inside the test
    L = w.ledger
    for _ in range(6):                                # six awards' fees, 3.0, all in the pool
        post_and_award(w, "A", 10, tau=1)
        w.advance(w.t + 2)
    assert w.omega_pool == pytest.approx(3.0) and L.wallet(Ledger.OMEGA).U == pytest.approx(0.0)
    post_and_award(w, "A", 10, tau=500)
    post_and_award(w, "B", 10, tau=500)
    q = w.post_root("H", 30)
    w.advance(w.t + 2)
    c = w.cases[q]
    assert w.is_troop(c.actor) and w.loans[c.actor]["amount"] == pytest.approx(12.0)   # the whole need: the pool funded none of it
    assert w.omega_pool == pytest.approx(3.0 + 1.0 + 0.5)
    check_all(w)


def test_r_s_is_indexed_at_the_cases_first_lock_when_stated():
    w = make_world(period_ticks=6, T_s=1)
    L = w.ledger
    post_and_award(w, "A", 10, tau=2)
    post_and_award(w, "B", 40, tau=2)                 # the first period's awards: mean 25, published at the boundary
    w.advance(7)
    assert L.index() == pytest.approx(1.25)
    q = post_and_award(w, "A", 40, tau=4)             # posted at index 1.25: r_s = 1.25 a tick late
    w.advance(w.cases[q].deadline + 1)
    c = w.cases[q]
    assert c.state == "FINAL_N" and c.index_at_lock == pytest.approx(1.25)
    assert c.rebate_owed == pytest.approx(min(1.25 * c.late_ticks, 40.0)) and c.late_ticks == 3
    check_all(w)
    # the default r_s = 0 means ω₀B, which scales with the price on its own
    w2 = make_world(r_s=0.0, T_s=1)
    q2 = post_and_award(w2, "A", 10, tau=4)
    w2.advance(5)
    assert w2.cases[q2].rebate_owed == pytest.approx(min(0.05 * 10 * 3, 10.0))
    check_all(w2)


def test_debt_takes_the_fee_before_the_pool_does():
    w = make_world(T_s=10_000)
    L = w.ledger
    q = two_awards_then_a_summons(w)
    w.advance(w.cases[q].deadline + 1)                # a failed state delivery: debt 12; the pool holds 1.5 from before the debt
    assert w.debt == pytest.approx(12.0) and w.omega_pool == pytest.approx(1.5)
    post_and_award(w, "A", 10, tau=2)                 # a fee of 0.5 arrives with debt standing: the debt first, nothing to the pool
    assert w.debt == pytest.approx(11.5) and w.omega_pool == pytest.approx(1.5)
    check_all(w)


def test_I32_catches_a_pool_that_does_not_match_its_lock_and_a_liability_under_the_pool():
    w = make_world(T_s=10_000)
    post_and_award(w, "A", 10, tau=2)
    check_all(w)
    w.omega_pool += 1.0
    with pytest.raises(InvariantError):
        check_all(w)
    w.omega_pool -= 1.0
    w.omega_liabilities.append({"requester": "H", "amount": 1.0, "t": 0, "case": "q1"})
    with pytest.raises(InvariantError):
        check_all(w)


def test_the_six_actor_quiet_period_and_flooded_period_of_section_6():
    # the quiet period: the fees cover the claims — paid in full, the rest retained
    w = make_world(T_s=1)
    for _ in range(4):
        post_and_award(w, "A", 10, tau=1)             # on time: the fee 0.5 each, no claim
        w.advance(w.t + 2)
    q = post_and_award(w, "B", 10, tau=3)             # one late by 2: a claim of 2 against a pool of 2.5
    w.advance(13)
    rec = w.periods[-1]
    assert rec["claims"] == pytest.approx(2.0) and rec["rebates_paid"] == pytest.approx(2.0) and rec["forgone_share"] == 0
    assert rec["omega_retained_period"] == pytest.approx(0.5) and w.cases[q].rebate_forgone == 0
    check_all(w)
    # the flooded period: claims far above the fees — a small fraction each, the rest forgone, Ω retains nothing
    w2 = make_world(T_s=1)
    qs = [post_and_award(w2, a, 10, tau=10) for a in ("A", "B")]
    w2.advance(11)                                    # both lapse at tick 10, nine ticks late: claims of 9 each (under the cap of B = 10), 18 in all; the pool 1.0
    w2.advance(13)
    rec2 = w2.periods[-1]
    assert rec2["claims"] == pytest.approx(18.0) and rec2["rebates_paid"] == pytest.approx(1.0)
    assert rec2["forgone_share"] == pytest.approx(17.0 / 18.0) and rec2["omega_retained_period"] == pytest.approx(0.0)
    assert all(w2.cases[q].rebate_paid == pytest.approx(0.5) and w2.cases[q].rebate_forgone == pytest.approx(8.5) for q in qs)
    check_all(w2)


def test_rebate_pool_off_is_the_210_engine():
    w = make_world(rebate_pool=False)
    q = two_awards_then_a_summons(w)
    w.advance(w.cases[q].deadline + 1)
    c = w.cases[q]
    assert c.rebate_owed == pytest.approx(1.0) and len(w.omega_liabilities) == 1 and w.omega_pool == 0 and pool_lock(w) == 0
    assert w.ledger.wallet(Ledger.OMEGA).L == pytest.approx(0.0)
    check_all(w)

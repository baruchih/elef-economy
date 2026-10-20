"""Design revision 9 — the bank (2.1.0): §2.1 a second account that alone creates and destroys; §2.2 the state burns its expected
cost c^D_T = (1 − b_T) B̄ − b_T G, floored, and delivers at B̄; §2.3 issuance, emission and a plant's pots minted by rule, the plant's
sweep destroyed; §2.4 the loan tied to a summons and repaid from its own return, the debt from settled summonses, every inflow to
Ω ordered at once (Appendix N's ruling: debt → liabilities → Ω), a rebate never created, the wall on deliveries and never on
seats; §2.5 P_t published once a period; §2.6 every refusal marked and told. I28 rewritten, I30, I31.
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
from sim.engine import LedgerError, RuleError, F, N, PLANT_REQ, PLANT_ACT
from sim.invariants import InvariantError

ACTORS = ["A", "B", "C", "D", "E", "F"]
DUTY = ["C", "D", "E", "F"]
ACTORS7 = ACTORS + ["G"]            # a seventh member for the wall test's seat


def make_world(budget=1000.0, actors=ACTORS, duty=DUTY, **over):
    # 2.1.0 defaults (bank on); no emission, the service fee on, no plants, the service target far off, long turns
    # 2.2.0 (design revision 10) moved the rebate to the period's pool; these tests pin the 2.1.0 engine (rebate_pool=False)
    kw = dict(plant_market=False,   # 2.6.0: these tests build plants submitted — the 1.2.0 construction, the control
              E0=0.0, H=1e9, omega_rate=0.05, Omega0=0.0, duty_turn_reviews=10_000, duty_turn_ticks=100_000,
              r_s=1.0, T_s=10_000, pi0=0.0, rebate_pool=False)
    kw.update(over)
    return World(Params(**kw), actors, humans={"H": budget}, on_duty=duty)


def post_and_award(w, actor, B, beta=None, tau=500):
    q = w.post_root("H", beta if beta is not None else B)
    w.award(q, actor, B, tau)
    return q


def two_awards_then_a_summons(w, beta=30):
    """Two members awarded at 10 (B̄ = 10, G = 5) for two ticks — nobody submits, so they lapse at tick 2 and the two are free
    again — then a request nobody is free for at the seating of tick 1: the state's after w_A."""
    post_and_award(w, "A", 10, tau=2)
    post_and_award(w, "B", 10, tau=2)
    q = w.post_root("H", beta)
    t = w.t
    w.advance(t + 2)
    return q


def kinds(w):
    return {e.kind for e in w.ledger.events}


def test_a_summons_is_lent_for_the_shortfall_at_the_expected_cost_and_its_return_repays_before_Omega_keeps():
    w = make_world()
    L = w.ledger
    q = two_awards_then_a_summons(w)
    c = w.cases[q]
    assert c.state == "COMMITTED" and w.is_troop(c.actor)
    # §2.2: the burn is (1 − 0.2) × 10 − 0.2 × 5 = 7, not 10; the price stays B̄ = 10
    assert c.c_d_t == pytest.approx(7.0) and c.b_t_at_summons == pytest.approx(0.2) and c.B == pytest.approx(10.0)
    assert w.troops[c.actor]["cost"] == pytest.approx(7.0) and w.troops[c.actor]["lock"] == pytest.approx(5.0)
    # §2.4: Ω held the two fees (1.0); the bank lent the shortfall of 7 + 5 over it, tied to the summons
    assert w.loans == {c.actor: {"amount": pytest.approx(11.0), "kind": "delivery", "case": q, "t": w.troops[c.actor]["t_summons"]}}
    assert w.bank_minted["loan"] == pytest.approx(11.0) and w.loans_outstanding == pytest.approx(11.0) and w.debt == 0
    assert any(e.kind == "loan" and e.note == "loan: delivery" and e.case == q for e in L.events)
    assert "creation" not in kinds(w) and w.deficit == 0
    assert L.wallet(Ledger.OMEGA).U == pytest.approx(0.5)      # this summons's own fee; nothing of the loan is left unspent
    check_all(w)
    # the delivery vests: the price and the guarantee come home, 11 repays the loan first, 4 reach Ω — with the fees, 4.5
    w.submit(q)
    r = w.assign_initial(q, "C")
    w.complete_review(r, F, 0)
    w.advance(w.cases[q].window_end + 1)
    assert w.cases[q].state == "VESTED" and w.loans == {} and w.debt == 0
    assert w.bank_destroyed["repayment"] == pytest.approx(11.0)
    assert any(e.kind == "repayment" and e.note == f"repayment: delivery {c.actor}" for e in L.events)
    assert L.wallet(Ledger.OMEGA).U == pytest.approx(4.5)      # b_T (B̄ + G) = 3 on the delivery, plus three fees of 0.5
    check_all(w)


def test_a_failed_delivery_leaves_its_loan_as_debt_and_the_next_inflow_repays_it_at_once():
    w = make_world()
    L = w.ledger
    q = two_awards_then_a_summons(w)
    tid = w.cases[q].actor
    w.advance(w.cases[q].deadline + 1)                # nobody submits for the troop: final N at the deadline
    c = w.cases[q]
    assert c.state == "FINAL_N" and w.loans == {}
    # §2.4: nothing returned — the loan of 11 is the state's debt; Ω's own 0.5 went to it the moment the debt was made
    assert w.debt == pytest.approx(10.5) and w.debt_created == pytest.approx(11.0) and w.debt_since == c.t_closed or w.debt_since is not None
    assert L.wallet(Ledger.OMEGA).U == pytest.approx(0.0)      # I30: nothing kept while the debt stands
    assert L.wallet("H").U > 0 and any(e.kind == "forfeit_to" and e.dst == "H" for e in L.events)   # G to the requester
    assert w.bank_minted["loan"] - w.bank_destroyed["repayment"] == pytest.approx(w.loans_outstanding + w.debt)
    check_all(w)
    # Appendix N's ruling: an inflow is ordered the moment it arrives — the next award's fee repays debt inside the award
    before = w.debt
    post_and_award(w, "A", 10)
    assert w.debt == pytest.approx(before - 0.5) and L.wallet(Ledger.OMEGA).U == pytest.approx(0.0)
    assert any(e.kind == "repayment" and e.note == "repayment: debt" for e in L.events)
    check_all(w)


def test_the_order_of_Omegas_income_is_debt_then_liabilities_oldest_first_then_Omega():
    w = make_world(T_s=2, r_s=1.0)
    L = w.ledger
    q = two_awards_then_a_summons(w)
    w.advance(w.cases[q].deadline + 1)                # a failed state delivery, late: its rebate took Ω's 0.5 at the stop, the
    c = w.cases[q]                                    # rest is a liability; then the loan closed as debt — 11
    assert w.debt == pytest.approx(11.0) and c.rebate_owed > 0.5 and c.rebate_paid == pytest.approx(0.5)
    assert len(w.omega_liabilities) == 1 and L.wallet(Ledger.OMEGA).U == pytest.approx(0.0)
    # a late member request: the rebate owed cannot be paid (Ω is empty while the debt stands) — a liability, never created
    q2 = post_and_award(w, "A", 10, tau=6)
    w.advance(w.t + 6)
    w.submit(q2)
    r = w.assign_initial(q2, "C")
    w.complete_review(r, F, 0)
    c2 = w.cases[q2]
    assert c2.late_ticks > 0 and c2.rebate_owed > 0
    assert c2.rebate_paid == pytest.approx(0.0) and len(w.omega_liabilities) == 2
    assert "creation" not in kinds(w) and w.bank_minted["loan"] == pytest.approx(11.0)   # nothing lent for the rebates
    assert w.debt == pytest.approx(11.0 - 0.5)        # the award's fee repaid debt the moment it arrived
    check_all(w)
    # an inflow large enough for all: the debt first, then the liabilities oldest first, then Ω keeps the rest
    owed = sum(l["amount"] for l in w.omega_liabilities)
    debt = w.debt
    L.transfer("H", Ledger.OMEGA, debt + owed + 2.0, note="test: an inflow to Ω")
    assert w.debt == pytest.approx(0.0) and w.omega_liabilities == [] and w.cases[q2].rebate_paid == pytest.approx(c2.rebate_owed)
    assert w.cases[q].rebate_paid == pytest.approx(w.cases[q].rebate_owed)
    assert L.wallet(Ledger.OMEGA).U == pytest.approx(2.0)
    check_all(w)


def test_the_wall_refuses_a_delivery_marks_it_told_and_never_refuses_a_seat():
    # one closed period of fee income is the wall; a period of 4 ticks with one award closes with a fee of 0.5
    w = make_world(period_ticks=4, debt_bound_periods=1, actors=ACTORS7)
    L = w.ledger
    post_and_award(w, "A", 10, tau=2)
    w.advance(5)                                      # the boundary (processed at the tick numbered 4): the wall is the closed period's fees, 0.5
    assert w.periods and w._debt_bound() == pytest.approx(0.5)
    # the state's delivery fails: the debt (about 10) is above the wall. G is committed through the refusal and free again after
    qA = post_and_award(w, "A", 10, tau=500)
    qB = post_and_award(w, "B", 10, tau=500)
    post_and_award(w, "G", 10, tau=6)
    q = w.post_root("H", 30)
    w.advance(w.t + 2)
    tid = w.cases[q].actor
    assert w.is_troop(tid)
    w.advance(w.cases[q].deadline + 1)
    assert w.cases[q].state == "FINAL_N" and w.debt > w._debt_bound()
    # the next request past w_A is refused for credit — marked, told, the clock running
    q2 = w.post_root("H", 30)
    t = w.t
    w.advance(t + 2)
    c2 = w.cases[q2]
    assert c2.state == "AVAILABLE" and c2.refused == "credit" and c2.refused_credit >= 1 and c2.refused_at == t + 1 and c2.capacity_told
    assert w.troop_refused_credit_awards >= 1 and w.troop_refused_credit_seats == 0
    assert any("refused for credit" in m for _, m, _ in c2.log)
    assert c2.clock_ticks >= 2
    # a seat is lent for regardless: C and D are reviewing, E and F cannot fund a bond, so G's submitted delivery waits w_R
    # for its inspection and a troop takes the seat on the bank's loan, the debt still above the wall
    w.advance(w.cases[q].deadline + 4)                # G's own award has lapsed by now; G is free
    w.submit(qA)
    w.submit(qB)
    w.assign_initial(qA, "C")
    w.assign_initial(qB, "D")
    for a in ("E", "F"):
        L.transfer(a, "H", L.wallet(a).U, note="test: the bond cannot be funded")
    q3 = post_and_award(w, "G", 10, tau=2)
    w.advance(w.t + 2)
    w.submit(q3)
    w.advance(w.t + 3)
    c3 = w.cases[q3]
    assert w.debt > w._debt_bound()
    assert any(w.is_troop(w.reviews[r].reviewer) for r in c3.reviews), "the seat was lent for above the wall"
    assert w.troop_refused_credit_seats == 0 and any(e.kind == "loan" and e.note == "loan: review" for e in L.events)
    check_all(w)


def test_the_wall_unbounded_is_the_control_and_the_state_does_not_retract():
    w = make_world(period_ticks=4, debt_bound_periods=0)
    post_and_award(w, "A", 10, tau=2)
    w.advance(5)
    post_and_award(w, "A", 10, tau=500)
    post_and_award(w, "B", 10, tau=500)
    q = w.post_root("H", 30)
    w.advance(w.t + 2)
    w.advance(w.cases[q].deadline + 1)
    assert w.cases[q].state == "FINAL_N" and w.debt > 0 and w._debt_bound() == float("inf")
    q2 = w.post_root("H", 30)
    w.advance(w.t + 2)
    assert w.cases[q2].state == "COMMITTED" and w.is_troop(w.cases[q2].actor) and w.troop_refused_credit_awards == 0
    check_all(w)


def test_the_burn_is_floored_at_zero_and_follows_the_states_own_record():
    w = make_world(b_t_prior=0.8)                     # above two thirds: (1 − 0.8) × 10 − 0.8 × 5 < 0 → 0
    q = two_awards_then_a_summons(w)
    assert w.cases[q].c_d_t == pytest.approx(0.0) and w.troops[w.cases[q].actor]["cost"] == pytest.approx(0.0)
    check_all(w)
    # the state's own record: with fewer than b_t_min_n closed the prior holds; with enough the rate is its own
    w2 = make_world(period_ticks=3, b_t_min_n=1, debt_bound_periods=0)
    q = two_awards_then_a_summons(w2)
    w2.advance(w2.cases[q].deadline + 1)              # one state delivery closed, failed
    w2.advance(w2.t + 4)                              # a boundary: the record is (1 closed, 1 failed)
    assert any(h == (1, 1) for h in w2.state_delivery_history) and w2._state_fail_rate() == pytest.approx(1.0)
    post_and_award(w2, "A", 10, tau=500)              # nobody free again
    post_and_award(w2, "B", 10, tau=500)
    q3 = w2.post_root("H", 30)
    w2.advance(w2.t + 2)
    assert w2.cases[q3].c_d_t == pytest.approx(0.0) and w2.cases[q3].b_t_at_summons == pytest.approx(1.0)
    w3 = make_world(period_ticks=3, b_t_min_n=10, debt_bound_periods=0)
    q = two_awards_then_a_summons(w3)
    w3.advance(w3.cases[q].deadline + 1)
    w3.advance(w3.t + 4)
    assert w3._state_fail_rate() == pytest.approx(0.2)   # one closed, ten needed: the prior
    check_all(w3)


def test_the_control_modes_at_cost_and_half():
    w = make_world(c_d_t_mode="at_cost")
    q = two_awards_then_a_summons(w)
    assert w.cases[q].c_d_t == pytest.approx(10.0)
    w2 = make_world(c_d_t_mode="half")
    q2 = two_awards_then_a_summons(w2)
    assert w2.cases[q2].c_d_t == pytest.approx(10.0)  # c_D_T × P_t/P_0 = 10 × 1 in the first period
    check_all(w2)


def test_P_t_is_published_at_the_period_boundary_and_does_not_move_within_a_period():
    w = make_world(period_ticks=10)
    L = w.ledger
    post_and_award(w, "A", 10, tau=2)                 # the two lapse at tick 2 and the actors are free again
    post_and_award(w, "B", 40, tau=2)
    assert L.P_t == pytest.approx(20.0) and L.index() == pytest.approx(1.0) and w.price_level() == pytest.approx(20.0)
    q = w.post_root("H", 30)                          # posted in the first period: indexed at 1
    assert w.cases[q].index_at_lock == pytest.approx(1.0) and w.cases[q].phi_E == pytest.approx(10.0)
    w.advance(11)                                     # the boundary (the tick numbered 10): the closed period's mean, (10 + 40) / 2
    assert L.P_t == pytest.approx(25.0) and w.price_level() == pytest.approx(25.0) and w._P_published_at == 10
    assert w.periods[-1]["P_level"] == pytest.approx(25.0)
    q2 = w.post_root("H", 30)
    assert w.cases[q2].index_at_lock == pytest.approx(1.25) and w.cases[q2].phi_E == pytest.approx(12.5)
    post_and_award(w, "A", 10)                        # awards within the period move B̄, never P_t
    assert L.P_t == pytest.approx(25.0) and w.mean_awarded_price() == pytest.approx(10.0)
    w.advance(21)                                     # a period with one award at 10
    assert L.P_t == pytest.approx(10.0)
    w.advance(31)                                     # a period with none: carried
    assert L.P_t == pytest.approx(10.0)
    check_all(w)


def test_a_plants_pots_are_minted_and_its_whole_sweep_destroyed_with_Omega_untouched():
    w = make_world(pi0=0.1)
    L = w.ledger
    om0 = L.wallet(Ledger.OMEGA).U
    q = w.create_plant(True, 20.0)
    c = w.cases[q]
    assert any(e.kind == "mint_plant" and e.dst == PLANT_REQ and e.amount == pytest.approx(15.0) for e in L.events)
    assert w.bank_minted["mint_plant"] == pytest.approx(15.0) and L.wallet(Ledger.OMEGA).U == pytest.approx(om0)
    assert L.pools[q].escrow == 0 and L.lock_record(PLANT_ACT, f"G:{q}") == 0        # netted since 1.3.0
    r = w.assign_initial(q, "C")
    w.complete_review(r, F, 1)
    w.advance(w.cases[q].window_end + 1)
    assert w.cases[q].tree_closed
    assert any(e.kind == "retire_plant" and e.src == PLANT_REQ for e in L.events)
    assert L.wallet(PLANT_REQ).U == pytest.approx(0.0) and L.wallet(PLANT_ACT).U == pytest.approx(0.0)
    cost_of_truth = w.bank_minted["mint_plant"] - w.bank_destroyed["retire_plant"]
    assert cost_of_truth == pytest.approx(1.0 + 2.0)   # the reviewer's cost 1 reimbursed and its fee 2: what the pots paid out
    assert L.wallet(Ledger.OMEGA).U == pytest.approx(om0)   # nothing minted for the plant reached Ω
    check_all(w)


def test_the_scenario_is_the_banks_declared_operation_and_Omega_never_creates():
    w = make_world()
    w.scenario_create(50.0)
    assert w.ledger.wallet("H").U == pytest.approx(1050.0) and w.scenario_created == 50.0
    assert w.bank_minted["mint_scenario"] == pytest.approx(50.0) and "creation" not in kinds(w) and w.deficit == 0
    check_all(w)
    # a creation asked of Ω under the bank is caught
    w._omega_ensure(10.0, None, "summons")
    with pytest.raises(InvariantError):
        check_all(w)


def test_a_refusal_for_capacity_marks_the_request_and_the_mark_comes_off_when_served():
    w = make_world(N_T=3)
    post_and_award(w, "A", 10)
    post_and_award(w, "B", 10)
    q3 = w.post_root("H", 30)
    q4 = w.post_root("H", 30)
    t = w.t
    w.advance(t + 2)
    c3, c4 = w.cases[q3], w.cases[q4]
    assert c3.state == "COMMITTED" and c3.refused is None
    assert c4.refused == "capacity" and c4.refused_at == t + 1 and c4.refused_last == t + 1 and c4.capacity_told
    w.submit(q3)
    w.assign_initial(q3, "C")
    w.advance(w.t + 1)
    assert w.cases[q4].state == "COMMITTED" and w.cases[q4].refused is None and w.cases[q4].refused_at == t + 1
    check_all(w)


def test_the_period_record_carries_the_banks_books():
    w = make_world(period_ticks=6)
    q = two_awards_then_a_summons(w)
    w.advance(7)
    rec = w.periods[-1]
    b = rec["bank"]
    assert b is not None and b["minted"]["loan"] == pytest.approx(11.0) and b["loans_period"] == pytest.approx(11.0)
    assert b["wall"] is None and rec["omega_fee_total"] == pytest.approx(1.5) and b["b_T"] == pytest.approx(0.2)
    assert b["omega_net"] == pytest.approx(b["omega_retained"] - b["debt"] - b["liabilities"])
    assert rec["P_level"] == pytest.approx(10.0)      # the closed period's mean awarded price (three at 10), published
    check_all(w)


def test_bank_off_is_the_200_engine():
    w = make_world(bank=False)
    q = two_awards_then_a_summons(w)
    assert any(e.kind == "creation" and e.note == "creation: summons" for e in w.ledger.events)
    assert w.deficit > 0 and w.loans == {} and w.cases[q].c_d_t == pytest.approx(10.0) and w.cases[q].b_t_at_summons is None
    assert w.ledger.P_t == pytest.approx(10.0)        # the live window
    check_all(w)

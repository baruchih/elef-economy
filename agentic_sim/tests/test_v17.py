"""Design revision 7 — specification 1.7.0: the state's earnings.

§2.1 Two accounts again: the duty fund is 1.3.0's uplift fund — the raised tax in, its whole balance out as uplift at
every settlement batch, no reserve, no lock — and the troops' wallet is a separate troop account: Ω's advances and every
troop's earnings in; costs, locks, forfeits, burns and repayments out; at each batch its unlocked balance above R_T flows
to Ω. R_T is the two-period peak of the capital troops held; a refusal no longer raises it. 1.4.0's "nothing a troop
earns reaches Ω except by repayment" is withdrawn. §2.3 The members' duty cap is ⌈2E_t/3⌉, floored at V_max + 1. Ω's
record carries its two incomes (base fee, troop surplus), its own money's flows (advances made, repaid) and its outflows.
"""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
try:
    import pytest
except ImportError:  # plain `python3 run_tests.py`
    sys.path.insert(0, os.path.dirname(__file__))
    from _mini_pytest import pytest

from sim import Params, World, InvariantError, Ledger, check_all
from sim.invariants import I23_load_and_fund
from sim.engine import F, DUTY_FUND, TROOP_ACCT

ACTORS = ["A", "B", "C", "D", "E", "F"]
DUTY = ["C", "D", "E", "F"]
DELIVERY = 10.0 + 10.0    # a troop delivery's capital at B = 20: cost 10 purchased, guarantee 10 locked
SEAT = 3.0 + 5.0          # a troop review seat's: cost 3, bond 5


def make_world(budget=1000.0, actors=ACTORS, duty=DUTY, **over):
    # 1.7.0 defaults (the troop account, the two-thirds cap); no emission, no service fee unless a test asks, no plants
    # (so the plant reserve is 0), the service target far off (so no rebate moves Ω in these figures), Ω 100, long turns
    kw = dict(E0=0.0, H=1e9, omega_rate=0.0, Omega0=100.0, duty_turn_reviews=10_000, duty_turn_ticks=100_000,
              r_s=1.0, T_s=10_000, pi0=0.0)
    kw.update(over)
    return World(Params(**kw), actors, humans={"H": budget}, on_duty=duty)


def omega_set(w, amount):
    """Set Ω's unlocked balance exactly, through the sponsor (a test's hand, not a rule)."""
    om = w.ledger.wallet(Ledger.OMEGA).U
    if amount > om:
        w.ledger.transfer("SPONSOR", Ledger.OMEGA, amount - om, note="test: Ω set")
    elif om > amount:
        w.ledger.transfer(Ledger.OMEGA, "SPONSOR", om - amount, note="test: Ω set")


def commit_free_members(w, tau=500):
    """A and B take tasks: no free member off duty remains, so the next request waits for a troop."""
    for actor in ("A", "B"):
        q = w.post_root("H", 20)
        w.award(q, actor, 20, tau)


def troop_delivery(w, reviewer="C"):
    """A request no member is free for; after w_A a troop delivers it at the market price, a member reviews it, and the
    case vests. Returns the case id and the troop's id."""
    q = w.post_root("H", 20)
    t_post = w.t
    w.advance(t_post + 2)                            # waited w_A = 2: summoned
    c = w.cases[q]
    assert c.state == "COMMITTED" and w.is_troop(c.actor), c.state
    tid = c.actor
    w.advance(c.deadline)
    w.submit(q)
    r = w.assign_initial(q, reviewer)
    w.advance(w.t + 1)
    w.complete_review(r, F, 0)
    w.advance(c.window_end + 1)
    assert c.state == "VESTED"
    return q, tid


def busy_all_duty(w):
    rids = []
    for aid in [a.id for a in w.actors.values() if a.on_duty and a.open_review is None]:
        qp = w.create_plant(True, 20.0)
        rids.append(w.assign_initial(qp, aid))
    return rids


def pending_case(w, actor="A", reviewer="C"):
    q = w.post_root("H", 20)
    w.award(q, actor, 20, 1)
    w.advance(w.t + 1)
    w.submit(q)
    r = w.assign_initial(q, reviewer)
    w.advance(w.t + 1)
    w.complete_review(r, F, 0)
    return q, r


# ------------------------------------------------------------ §2.1 two accounts
def test_a_troop_deliverys_earnings_are_the_states_and_the_uplift_fund_sees_none_of_them():
    w = make_world()
    commit_free_members(w)
    om0 = w.W(Ledger.OMEGA)
    assert w.W(DUTY_FUND) == 0.0 and w.W(TROOP_ACCT) == 0.0
    q, tid = troop_delivery(w)
    assert w.ledger.aliases[tid] == TROOP_ACCT
    # price 20 earned against cost 10 purchased: +10, realised in the troop account; Ω advanced 20 and was repaid 20
    assert w.advances_made == pytest.approx(20.0) and w.advances_repaid == pytest.approx(20.0) and w.advance_outstanding == 0.0
    assert w.W(TROOP_ACCT) + w.troop_surplus_paid == pytest.approx(10.0)
    assert w.W(DUTY_FUND) == 0.0 and w.fund_out == 0.0 and w.fund_in == 0.0      # the uplift fund saw none of it
    assert w.reviews[w.cases[q].reviews[0]].uplift == 0.0
    assert w.W(Ledger.OMEGA) == pytest.approx(om0 + w.troop_surplus_paid)        # what reached Ω is the surplus, nothing else
    check_all(w)
    # the 1.6.0 control (the merged fund): the same +10 lands in the duty fund and is paid out as uplift above R_T
    w2 = make_world(troop_account=False, duty_cap_frac=0.5)
    commit_free_members(w2)
    fund0 = w2.W(DUTY_FUND)
    troop_delivery(w2)
    assert w2.W(TROOP_ACCT) == 0.0 and w2.troop_surplus_paid == 0.0
    assert w2.W(DUTY_FUND) + w2.fund_out == pytest.approx(fund0 + 10.0)
    check_all(w2)


def test_the_surplus_flows_to_Omega_only_from_above_the_reserve_and_the_reserve_is_the_capital_held():
    w = make_world(period_ticks=6, period_plants=10_000)
    commit_free_members(w, tau=4)                     # A and B busy through the summons; final N at 4, then free again
    om0 = w.W(Ledger.OMEGA)
    q, tid = troop_delivery(w)
    # R_T is the peak capital held — one delivery's 20 — so the 10 earned sits below it and nothing flows yet
    assert w.R_T == pytest.approx(DELIVERY) and w.W(TROOP_ACCT) == pytest.approx(10.0) and w.troop_surplus_paid == 0.0
    assert w.W(Ledger.OMEGA) == pytest.approx(om0)
    # two periods later with no troop in the field the peak has rolled off; the next batch pays the account's balance to Ω
    w.advance(w.t + 13)
    assert w.R_T == 0.0
    q2, r2 = pending_case(w, actor="A", reviewer="D")
    w.advance(w.cases[q2].window_end + 1)             # the batch: surplus above R_T = 0 is the whole balance
    assert w.W(TROOP_ACCT) == pytest.approx(0.0) and w.troop_surplus_paid == pytest.approx(10.0)
    assert w.W(Ledger.OMEGA) == pytest.approx(om0 + 10.0)
    check_all(w)


def test_a_refusal_for_funds_no_longer_raises_the_reserve():
    w = make_world()
    commit_free_members(w)
    omega_set(w, 0.0)                                 # Ω cannot advance: the summons is refused for funds
    q = w.post_root("H", 20)
    w.advance(w.t + 2)
    assert w.cases[q].state == "AVAILABLE" and w.troop_shortfall_awards >= 1
    assert w.troop_demand_refused > 0 and w.R_T == 0.0          # 1.5.0's reading is recorded; the reserve ignores it
    omega_set(w, 100.0)
    w.advance(w.t + 1)
    assert w.is_troop(w.cases[q].actor) and w.R_T == pytest.approx(DELIVERY)
    check_all(w)


def test_the_uplift_fund_pays_its_whole_balance_while_the_troop_account_keeps_its_reserve():
    def world(**over):
        w = make_world(omega_rate=0.05, period_plants=2, period_ticks=10_000, Omega0=1000.0, **over)
        for aid in ("C", "E"):                        # the dial to m = 2: two bad plants approved
            qp = w.create_plant(False, 20.0)
            rp = w.assign_initial(qp, aid)
            w.advance(w.t + 1)
            w.complete_review(rp, F, 0)
        w.advance(w.t + 1)
        assert w.m_t == 2.0
        q, r = pending_case(w, actor="A", reviewer="D")
        busy_all_duty(w)
        w.roll_audit(q)
        w.advance(w.t + 2)                            # a troop takes the audit seat: R_T ≈ 8
        assert len(w.troops) == 1 and abs(w.R_T - SEAT) < 0.05
        tr = next(w.reviews[x] for x in w.cases[q].reviews if w.is_troop(w.reviews[x].reviewer))
        w.complete_review(tr.id, F, 0)
        q2 = w.post_root("H", 20)
        w.award(q2, "B", 20, 1)                       # at m = 2 each award's raised tax, 1, is the uplift fund's: 2 so far
        return w, q, r, tr
    w, q, r, tr = world()
    assert w.W(DUTY_FUND) == pytest.approx(2.0) and w.fund_in == pytest.approx(2.0)
    w.advance(w.cases[q].window_end + 1)              # q vests: the batch pays the fund's whole balance, R_T ≈ 8 notwithstanding
    assert w.fund_out == pytest.approx(2.0) and w.W(DUTY_FUND) == pytest.approx(0.0)
    assert w.reviews[r].uplift > 0 and tr.uplift == 0.0
    check_all(w)
    # the merged fund of 1.6.0 pays nothing while its balance is at or below the troops' reserve
    w2, q2_, r2, tr2 = world(troop_account=False, duty_cap_frac=0.5)
    w2.advance(w2.cases[q2_].window_end + 1)
    assert w2.fund_out == 0.0
    check_all(w2)


def test_a_troop_review_seat_nets_the_state_its_fee_since_its_cost_is_reimbursed_from_the_allowance():
    # Found at implementation (Appendix L): rc.2 §1.5, §2.1 and §6 say a troop review seat "nets nothing — fee 2 or 3
    # against a cost of 3", on the implementer's own rc.1 figure. The engine, as 1.4.0 §6 and test_v14 have it since
    # f0779ac, reimburses a troop reviewer's cost from the requester's allowance like any reviewer's: the seat nets the
    # fee — +3 for an audit, +2 for an ordinary review — and it is the state's. The text's figure is wrong; no rule is.
    w = make_world()
    q, r = pending_case(w)
    busy_all_duty(w)
    om0 = w.W(Ledger.OMEGA)
    w.roll_audit(q)
    w.advance(w.t + 2)                                # the audit seat waited w_R: a troop takes it, Ω advances 8
    tr = next(w.reviews[x] for x in w.cases[q].reviews if w.is_troop(w.reviews[x].reviewer))
    assert w.advances_made == pytest.approx(SEAT) and tr.cost == pytest.approx(3.0)
    w.complete_review(tr.id, F, 0)
    w.advance(w.cases[q].window_end + 1)
    assert tr.status == "vested" and tr.fee == pytest.approx(3.0) and tr.reimbursed == pytest.approx(3.0)
    assert w.advances_repaid == pytest.approx(SEAT) and w.W(Ledger.OMEGA) == pytest.approx(om0)
    # +3 realised in the troop account, held below R_T = 8 for now; Ω's once the peak rolls off (the test above)
    assert w.W(TROOP_ACCT) == pytest.approx(3.0) and w.troop_surplus_paid == 0.0 and w.R_T == pytest.approx(SEAT)
    check_all(w)


def test_Omegas_record_carries_its_two_incomes_and_its_own_moneys_flows():
    w = make_world(omega_rate=0.05)
    commit_free_members(w)                            # two member awards: the base fee 1 each is Ω's income
    assert w.omega_fee_income == pytest.approx(2.0) and w.period["omega_fee"] == pytest.approx(2.0)
    troop_delivery(w)                                 # a troop award pays the same base fee
    assert w.omega_fee_income == pytest.approx(3.0)
    assert w.period["advances_made"] == pytest.approx(DELIVERY) and w.advances_made == pytest.approx(DELIVERY)
    assert w.period["advances_repaid"] == pytest.approx(DELIVERY)
    assert w.period["troop_surplus"] == pytest.approx(w.troop_surplus_paid)
    w.advance(w.p.period_ticks + 1)                   # the period record carries them
    rec = w.periods[-1]
    assert rec["omega_income"]["fee"] == pytest.approx(3.0) and "troop_surplus" in rec["omega_income"]
    assert rec["omega_advances"]["made"] == pytest.approx(DELIVERY) and rec["omega_advances"]["repaid"] == pytest.approx(DELIVERY)
    assert set(rec["omega_out"]) == {"rebates_paid", "liabilities_paid", "plant_out", "plant_back"} and "uplift_fund" in rec
    check_all(w)


def test_I23_catches_an_uplift_fund_that_does_not_reconcile_or_holds_a_lock():
    w = make_world()
    w.ledger.transfer("SPONSOR", DUTY_FUND, 5.0, note="test: money the raised tax did not bring")
    with pytest.raises(InvariantError, match="I23 uplift fund"):
        check_all(w)
    w2 = make_world()
    w2.ledger.transfer("SPONSOR", DUTY_FUND, 5.0, note="test: seeded")
    w2.fund_in += 5.0                                 # reconciled by hand ...
    check_all(w2)
    w2.ledger.lock(DUTY_FUND, 5.0, key="test", note="test: a lock the fund may not hold")
    with pytest.raises(InvariantError, match="I23 the uplift fund holds a lock"):
        I23_load_and_fund(w2)                         # (the full audit's I15 would object first, to the same lock)


# ------------------------------------------------------------ §2.3 the cap
def test_the_members_duty_cap_is_two_thirds_floored_at_the_reserve_floor():
    w = make_world()
    assert [w._member_cap(E) for E in (4, 6, 7, 9, 10, 12, 20)] == [4, 4, 5, 6, 7, 8, 14]
    w2 = make_world(duty_cap_frac=0.5)                # the 1.6.0 control
    assert [w2._member_cap(E) for E in (6, 9, 10, 20)] == [4, 5, 5, 10]

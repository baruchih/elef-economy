"""Design revision 5 — specification 1.5.0: the reserve is sized to the need.

The duty fund's troop reserve R_T is the peak, over the current period, of the troop demand D_s at each
seating: the capital live troops hold plus the cost of the summonses the fund could not carry at that seating
(§2.1). A refusal for funds raises the reserve by the amount the carry check refused, once per seating; a
request priced below the market or that the requester cannot pay in for adds nothing; a challenge short of
both panel seats adds two; a refused summons carried at the next seating raises the peak once (the stock
moves from refused to held); no uplift is paid while the unlocked balance is at or below the reserve; the
peak holds within the period and restarts at the standing demand at the boundary, so rest returns it to
zero. `reserve_demand=False` is the 1.4.0 reading, kept as a declared control. I23 catches a reserve below
the capital held or the last demand.
"""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
try:
    import pytest
except ImportError:  # plain `python3 run_tests.py`
    sys.path.insert(0, os.path.dirname(__file__))
    from _mini_pytest import pytest

from sim import Params, World, InvariantError, check_all
from sim.engine import F, N, DUTY_FUND

ACTORS = ["A", "B", "C", "D", "E", "F"]
DUTY = ["C", "D", "E", "F"]
SEAT = 3.0 + 5.0          # a troop review seat's need at v = 1: c_T 3 purchased plus the bond G^V 5 locked


def make_world(budget=1000.0, actors=ACTORS, duty=DUTY, **over):
    # no emission, no service fee, Ω 100, long turns; A_T = 0 so that an empty fund refuses (Ω advances nothing)
    kw = dict(E0=0.0, H=1e9, omega_rate=0.0, Omega0=100.0, duty_turn_reviews=10_000, duty_turn_ticks=100_000, A_T=0.0,
              service_clock=False, omega_backs_fund=False, seat_the_queue=False, panel_determined=False, reserve_periods=1,
              troop_account=False, duty_cap_frac=0.5)      # 1.7.0: the merged fund and the half cap of this revision
    kw.update(over)
    return World(Params(**kw), actors, humans={"H": budget}, on_duty=duty)


def seed_fund(w, amt):
    w.ledger.transfer("SPONSOR", DUTY_FUND, amt, note="test: fund seeded")


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


def refused_audit(w):
    """A pinned-style audit nobody is free to take, that an empty fund cannot carry: refused at its window."""
    q, r = pending_case(w)
    busy_all_duty(w)
    w.roll_audit(q)
    w.advance(w.t + 2)                               # waited w_R = 2 seating steps: the summons is attempted and refused
    return q


# ------------------------------------------------------------ §2.1 a refusal is demand
def test_a_refusal_for_funds_raises_the_reserve_by_the_refused_cost_once_per_seating():
    w = make_world()
    q = refused_audit(w)
    assert not w.troops and w.troop_shortfall_seats == 1 and w.cases[q].audit_obligation
    assert w.troop_demand_held == 0.0 and w.troop_demand_refused == pytest.approx(SEAT)
    assert w.R_T == pytest.approx(SEAT)              # the reserve rose by exactly what the carry check refused
    w.advance(w.t + 1)                               # refused again at the next seating ...
    assert w.troop_shortfall_seats == 2
    assert w.R_T == pytest.approx(SEAT)              # ... the stock is the same case once more, not twice
    check_all(w)
    # the 1.4.0 reading, kept as a declared control: the peak capital carried, which a refusal does not move
    w4 = make_world(reserve_demand=False)
    refused_audit(w4)
    assert w4.troop_shortfall_seats == 1 and w4.troop_demand_refused == pytest.approx(SEAT) and w4.R_T == 0.0
    check_all(w4)


def test_a_request_priced_below_the_market_or_that_cannot_pay_in_adds_no_demand():
    # priced below B̄: the rule's own exclusion, not a shortage
    w = make_world(omega_rate=0.05)
    for actor in ("A", "B"):
        q0 = w.post_root("H", 20)
        w.award(q0, actor, 20, 500)                  # both off-duty members committed for a long time; B̄ = 20
    q = w.post_root("H", 10)
    w.advance(w.t + 3)                               # past w_A with no free fundable member
    assert w.cases[q].state == "AVAILABLE" and not w.troops
    assert w.troop_shortfall_awards == 0 and w.troop_demand_now == 0.0 and w.R_T == 0.0
    check_all(w)
    # the requester cannot pay in: the market's refusal, not the fund's
    w2 = make_world(omega_rate=0.05, budget=36.0 + 36.0 + 10.0)
    for actor in ("A", "B"):
        q0 = w2.post_root("H", 20)
        w2.award(q0, actor, 20, 500)                 # 20 + 10 + 5 + 1 each: 10 is left, less than an award's pay-in
    q2 = w2.post_root("H", 20)
    w2.advance(w2.t + 3)
    assert w2.cases[q2].state == "AVAILABLE" and not w2.troops
    assert w2.troop_shortfall_awards == 0 and w2.troop_demand_now == 0.0 and w2.R_T == 0.0
    check_all(w2)


def test_a_challenge_short_of_both_panel_seats_adds_two_seats_of_demand():
    w = make_world()
    q = w.post_root("H", 20)
    w.award(q, "A", 20, 1)
    w.advance(w.t + 1)
    w.submit(q)
    r = w.assign_initial(q, "C")
    w.advance(w.t + 1)
    w.complete_review(r, N, 0)
    w.respond(q, "appeal")                           # a panel of two is required; C is excluded, the rest are busy
    busy_all_duty(w)
    w.advance(w.t + 2)                               # the seats waited w_R: the first summons is refused, the loop stops
    assert not w.troops and w.troop_shortfall_seats == 1
    assert w.troop_demand_refused == pytest.approx(2 * SEAT)    # the case's demand is its unfilled seats — both
    assert w.R_T == pytest.approx(2 * SEAT)
    check_all(w)


def test_a_refused_summons_carried_at_the_next_seating_raises_the_peak_once():
    w = make_world()
    q = refused_audit(w)
    assert w.R_T == pytest.approx(SEAT) and w.troop_demand_refused == pytest.approx(SEAT)
    seed_fund(w, SEAT)
    w.advance(w.t + 1)                               # carried: the stock moves from refused to held
    assert len(w.troops) == 1 and not w.cases[q].audit_obligation
    assert w.troop_demand_held == pytest.approx(SEAT) and w.troop_demand_refused == 0.0
    assert w.R_T == pytest.approx(SEAT)              # the maximum does not double
    assert w.troop_shortfall_seats == 1
    check_all(w)


# ------------------------------------------------------------ §2.1 the uplift waits on the reserve
def test_no_uplift_is_paid_while_the_unlocked_balance_is_at_or_below_the_reserve():
    w = make_world()
    q, r = pending_case(w, "A", "C")
    q2, r2 = pending_case(w, "B", "D")               # a pending case that will vest and settle D's review
    plants = busy_all_duty(w)
    w.roll_audit(q)
    w.advance(w.t + 2)                               # refused: R_T = 8
    assert w.R_T == pytest.approx(SEAT)
    seed_fund(w, 5.0)                                # unlocked 5 ≤ R_T 8
    w.advance(w.cases[q2].window_end + 1)
    assert w.cases[q2].state == "VESTED" and w.reviews[r2].status == "vested"
    assert w.fund_out == 0.0 and w.reviews[r2].uplift == 0.0          # nothing above the reserve: no uplift
    # the plant reviews complete, members are free again: the audit is the market's to take, the peak holds
    for rid in plants:
        if w.reviews[rid].status == "open":
            w.complete_review(rid, F, 0)
    w.advance(w.t + 1)
    assert w.R_T == pytest.approx(SEAT) and w.cases[q].audit_obligation
    seed_fund(w, 15.0)                               # unlocked 20 > 8: the balance above the reserve is the uplift
    q3, r3 = pending_case(w, "A", "E")
    out_before = w.fund_out
    w.advance(w.cases[q3].window_end + 1)
    assert w.cases[q3].state == "VESTED"
    assert w.fund_out - out_before == pytest.approx(20.0 - SEAT) and w.reviews[r3].uplift > 0
    assert w.W(DUTY_FUND) == pytest.approx(SEAT)     # the fund is drained to its reserve, not below
    check_all(w)


# ------------------------------------------------------------ §2.1 a peak holds, then restarts at the standing demand
def test_the_peak_holds_within_the_period_and_restarts_at_the_standing_demand_at_the_boundary():
    w = make_world(period_ticks=8, period_plants=10_000)     # the first period ends at tick 8
    q = refused_audit(w)                             # tick 4: R_T = 8
    assert w.t == 4 and w.R_T == pytest.approx(SEAT) and len(w.periods) == 0
    seed_fund(w, SEAT)
    w.advance(w.t + 1)                               # carried
    tr = next(w.reviews[x] for x in w.cases[q].reviews if w.is_troop(w.reviews[x].reviewer))
    w.complete_review(tr.id, F, 0)                   # released: nothing held, nothing refused ...
    w.advance(7)
    assert w.troop_demand_now == 0.0 and w.R_T == pytest.approx(SEAT) and len(w.periods) == 0   # ... the peak holds
    w.advance(9)                                     # the boundary: the peak restarts at the standing demand, zero
    assert len(w.periods) == 1 and w.R_T == 0.0 and w.troop_demand_now == 0.0
    assert w.periods[0]["demand_peak"] == pytest.approx(SEAT) and w.periods[0]["demand_peak_refused"] == pytest.approx(SEAT)
    assert w.periods[0]["demand_last"] == 0.0
    check_all(w)
    # a troop still in the field at the boundary keeps the reserve at its capital: nothing drops while troops are carried
    w2 = make_world(period_ticks=8, period_plants=10_000)
    q2 = refused_audit(w2)
    seed_fund(w2, SEAT)
    w2.advance(w2.t + 1)                             # carried at tick 5; the seat's deadline is tick 10
    assert len(w2.troops) == 1 and w2.R_T == pytest.approx(SEAT)
    w2.advance(9)                                    # the boundary at tick 8, the troop's seat still open
    tr2 = next(w2.reviews[x] for x in w2.cases[q2].reviews if w2.is_troop(w2.reviews[x].reviewer))
    assert tr2.status == "open" and len(w2.periods) == 1
    assert w2.R_T == pytest.approx(SEAT) and w2.periods[0]["demand_last"] == pytest.approx(SEAT)
    check_all(w2)


# ------------------------------------------------------------ I23 catches
def test_I23_catches_a_reserve_below_the_capital_held_or_the_last_demand():
    w = make_world()
    refused_audit(w)
    check_all(w)
    w.troop_demand_peak = 0.0                        # the engine would never do this: the reserve below the last demand
    with pytest.raises(InvariantError, match="I23 reserve"):
        check_all(w)
    w2 = make_world()
    q2 = refused_audit(w2)
    seed_fund(w2, SEAT)
    w2.advance(w2.t + 1)                             # a troop holds 8
    check_all(w2)
    w2.troop_demand_peak, w2.troop_demand_held, w2.troop_demand_refused = 0.0, 0.0, 0.0
    with pytest.raises(InvariantError, match="I23 reserve"):
        check_all(w2)

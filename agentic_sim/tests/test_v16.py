"""Design revision 6 — specification 1.6.0: auto-scale.

§2.1 Every root request carries a service clock from posting to its first verdict — or to a final without one —
running only while its ceiling admits the market price; past T_s the orchestrator owes the requester r_s a tick,
capped at B, paid from Ω when the clock stops or carried as Ω's liability, serviced oldest first; a request
withdrawn before award is owed nothing. §2.2 Ω backs the fund above a plant reserve (no A_T); liabilities older than
a period are paid before any advance; review-seat summonses precede deliveries in a pass; a delivery is summoned only
when the fund plus Ω's available advance can carry its own capital and two review seats, and the advance drawn is its
own shortfall. §2.3 The reserve is at least the reviews waiting. §2.4 Once the world's first plant is adjudicated, a
panel seat needs a determined record. §2.5 R_T is the peak demand over this and the previous period. I26 catches.
"""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
try:
    import pytest
except ImportError:  # plain `python3 run_tests.py`
    sys.path.insert(0, os.path.dirname(__file__))
    from _mini_pytest import pytest

from sim import Params, World, RuleError, InvariantError, Ledger, check_all
from sim.engine import F, N, DUTY_FUND

ACTORS = ["A", "B", "C", "D", "E", "F"]
DUTY = ["C", "D", "E", "F"]
SEAT = 3.0 + 5.0          # a troop review seat's need at v = 1
DELIVERY = 10.0 + 10.0    # a troop delivery's own capital at B = 20
CHECK = DELIVERY + 2 * SEAT   # §2.2: a delivery carries its inspection — 36


def make_world(budget=1000.0, actors=ACTORS, duty=DUTY, **over):
    # no emission, no service fee (r_s set explicitly to 1 a tick late), no plants unless a test asks (so the plant
    # reserve is 0 and Ω's balance is the state's reach), Ω 100, long turns
    kw = dict(plant_market=False,   # 2.6.0: these tests build plants submitted — the 1.2.0 construction, the control
              E0=0.0, H=1e9, omega_rate=0.0, Omega0=100.0, duty_turn_reviews=10_000, duty_turn_ticks=100_000,
              r_s=1.0, pi0=0.0, troop_account=False, duty_cap_frac=0.5)   # 1.7.0: the merged fund and the half cap
    kw.update(over)
    kw.setdefault("floating", False)   # 2.0.0: these are 1.x behaviours and figures — the backing, the reserves, the pay-in at award
    return World(Params(**kw), actors, humans={"H": budget}, on_duty=duty)


def omega_set(w, amount):
    """Set Ω's unlocked balance exactly, through the sponsor (a test's hand, not a rule)."""
    om = w.ledger.wallet(Ledger.OMEGA).U
    if amount > om:
        w.ledger.transfer("SPONSOR", Ledger.OMEGA, amount - om, note="test: Ω set")
    elif om > amount:
        w.ledger.transfer(Ledger.OMEGA, "SPONSOR", om - amount, note="test: Ω set")


def seed_fund(w, amt):
    w.ledger.transfer("SPONSOR", DUTY_FUND, amt, note="test: fund seeded")


def busy_all_duty(w):
    rids = []
    for aid in [a.id for a in w.actors.values() if a.on_duty and a.open_review is None]:
        qp = w.create_plant(True, 20.0)
        rids.append(w.assign_initial(qp, aid))
    return rids


def pending_case(w, actor="A", reviewer="C", wait=0):
    q = w.post_root("H", 20)
    w.award(q, actor, 20, 1 + wait)
    w.advance(w.t + 1 + wait)
    w.submit(q)
    r = w.assign_initial(q, reviewer)
    w.advance(w.t + 1)
    w.complete_review(r, F, 0)
    return q, r


# ------------------------------------------------------------ §2.1 the clock
def test_the_clock_runs_from_posting_to_the_first_verdict_and_an_on_time_request_owes_nothing():
    w = make_world()
    H0 = w.W("H")
    t0 = w.t
    q, r = pending_case(w)                           # posted at t0, verdict at t0 + 2
    c = w.cases[q]
    assert c.first_verdict_at == t0 + 2 and c.clock_stopped_at == t0 + 2 and c.clock_ticks == 2
    assert c.late_ticks == 0 and c.rebate_owed == 0.0 and w.on_time_n == 1 and w.late_n == 0
    assert w.W("H") == pytest.approx(H0 - 35.0)       # the pay-in (20 + 10 + 5; ω = 0 here) and no rebate
    w.advance(w.t + 3)
    assert c.clock_ticks == 2                        # a stopped clock does not run
    check_all(w)


def test_a_late_request_is_owed_r_s_a_tick_past_T_s_from_Omega_capped_at_B():
    w = make_world(T_s=3)
    om0, H0 = w.W(Ledger.OMEGA), w.W("H")
    q, r = pending_case(w, wait=8)                   # posted at t0, verdict at t0 + 10: 7 ticks late
    c = w.cases[q]
    assert c.clock_ticks == 10 and c.late_ticks == 7 and c.rebate_owed == pytest.approx(7.0) and c.rebate_paid == pytest.approx(7.0)
    assert w.W(Ledger.OMEGA) == pytest.approx(om0 - 7.0) and w.W("H") == pytest.approx(H0 - 35.0 + 7.0)
    assert w.late_n == 1 and w.lateness_sum == 7 and w.rebates_paid == pytest.approx(7.0) and not w.omega_liabilities
    # the cap: more than B / r_s = 20 ticks late owes B and no more
    w2 = make_world(T_s=3)
    q2, r2 = pending_case(w2, wait=40)
    assert w2.cases[q2].late_ticks == 39 and w2.cases[q2].rebate_owed == pytest.approx(20.0)
    check_all(w); check_all(w2)


def test_the_clock_does_not_run_for_a_request_priced_below_the_market_and_stops_at_a_final_without_a_verdict():
    w = make_world(omega_rate=0.05)
    for actor in ("A", "B"):
        q0 = w.post_root("H", 20)
        w.award(q0, actor, 20, 500)                  # the market price is 20
    low = w.post_root("H", 10)
    fair = w.post_root("H", 20)
    w.advance(w.t + 3)
    assert w.cases[low].clock_ticks == 0 and w.cases[fair].clock_ticks == 3
    # a delivery that misses its deadline is final N with no review: the clock stops there
    w2 = make_world(T_s=1)
    q = w2.post_root("H", 20)
    w2.award(q, "A", 20, 3)                         # deadline at t + 3; never submitted
    w2.advance(w2.t + 4)
    c = w2.cases[q]
    assert c.state == "FINAL_N" and c.first_verdict_at is None and c.clock_stopped_at is not None
    assert c.clock_ticks == 3 and c.late_ticks == 2 and c.rebate_owed == pytest.approx(2.0) and c.rebate_paid == pytest.approx(2.0)
    check_all(w); check_all(w2)


def test_a_request_withdrawn_before_award_is_owed_nothing():
    w = make_world(T_s=2)
    H0 = w.W("H")
    q = w.post_root("H", 20)
    w.advance(w.t + 12)                              # twelve ticks on the clock, ten past T_s
    assert w.cases[q].clock_ticks == 12
    w.withdraw_unawarded(q)
    c = w.cases[q]
    assert c.state == "WITHDRAWN" and c.rebate_owed == 0.0 and c.clock_stopped_at is None and w.W("H") == H0
    w.advance(w.t + 2)
    assert c.clock_ticks == 12                       # final: the clock no longer runs
    check_all(w)


def test_a_rebate_Omega_cannot_pay_is_its_liability_serviced_oldest_first_when_it_can():
    w = make_world(T_s=1, Omega0=0.0)
    q1, _ = pending_case(w, "A", "C", wait=4)       # 6 ticks on the clock, 5 late: owed 5, Ω empty
    q2, _ = pending_case(w, "B", "D", wait=4)
    c1, c2 = w.cases[q1], w.cases[q2]
    assert c1.rebate_owed == pytest.approx(5.0) and c1.rebate_paid == 0.0 and c2.rebate_owed == pytest.approx(5.0)
    assert len(w.omega_liabilities) == 2 and w.liabilities_accrued == pytest.approx(10.0)
    omega_set(w, 5.0)                                # enough for one: the older is paid first, after the pass
    w.advance(w.t + 1)
    assert c1.rebate_paid == pytest.approx(5.0) and c2.rebate_paid == 0.0 and len(w.omega_liabilities) == 1
    omega_set(w, 100.0)
    w.advance(w.t + 1)
    assert c2.rebate_paid == pytest.approx(5.0) and not w.omega_liabilities and w.liabilities_paid == pytest.approx(10.0)
    check_all(w)


# ------------------------------------------------------------ §2.2 Ω's order
def test_Omega_advances_only_above_the_plant_reserve_so_the_honesty_clock_is_never_starved():
    w = make_world(pi0=0.3, Omega0=1000.0)          # a plant rate high enough that the reserve exceeds one plant's capital
    for actor, reviewer in (("A", "C"), ("B", "D"), ("A", "F")):
        pending_case(w, actor, reviewer)             # initial reviews this period: the plant rate is π_t × their rate
    q, r = pending_case(w, "B", "E")
    busy_all_duty(w)                                 # the duty plants are Ω's to fund first (and count as initial reviews)
    w.roll_audit(q)
    w.advance(w.t + 1)                               # waited 1 < w_R: nothing yet
    R = w._plant_reserve()
    assert R >= 15.0                                 # a plant's life of plants: more than one plant's capital
    omega_set(w, R + 5.0)                            # five above the reserve: not a review seat's eight
    w.advance(w.t + 1)                               # waited w_R: the summons is attempted
    assert not w.troops and w.troop_shortfall_seats >= 1          # refused for Ω's money, not policy
    assert w.W(Ledger.OMEGA) + 1e-6 >= w._plant_reserve()         # what sat above the reserve was advanced; the reserve was not
    qp = w.create_plant(True, 20.0)                  # the clock still has its capital
    assert w.cases[qp].plant is True
    omega_set(w, 1000.0)
    w.advance(w.t + 1)
    assert len(w.troops) == 1                        # with Ω above the reserve by enough, the seat is carried
    check_all(w)


def test_review_seats_are_summoned_before_deliveries_and_a_delivery_carries_its_inspection():
    w = make_world()
    q1, r1 = pending_case(w, "B", "C")               # a member's pending approval: its audit will need a seat
    for actor in ("A", "B"):
        q0 = w.post_root("H", 20)
        w.award(q0, actor, 20, 500)                  # no free member: an award will need a troop
    qa = w.post_root("H", 20)                        # unawarded: waits w_A
    busy_all_duty(w)                                 # every duty actor mid-review: the audit seat will need a troop
    w.roll_audit(q1)
    omega_set(w, SEAT)                               # Ω can carry exactly one review seat; the fund is empty
    assert w.W(DUTY_FUND) == 0.0
    w.advance(w.t + 2)                               # both have waited their windows at this seating
    troop_reviews = [t for t in w.troops.values() if t["kind"] == "review"]
    assert len(troop_reviews) == 1 and not w.cases[q1].audit_obligation      # the audit seat came first and was carried
    assert w.cases[qa].state == "AVAILABLE" and w.troop_shortfall_awards >= 1 # the delivery was refused (36 > 0 left)
    check_all(w)
    # the delivery check: fund 10 and Ω 30 carry 36, and the advance drawn is the delivery's own ten
    w2 = make_world()
    for actor in ("A", "B"):
        q0 = w2.post_root("H", 20)
        w2.award(q0, actor, 20, 500)
    seed_fund(w2, 10.0)
    omega_set(w2, 30.0)
    qd = w2.post_root("H", 20)
    w2.advance(w2.t + 2)
    c = w2.cases[qd]
    assert c.state == "COMMITTED" and w2.is_troop(c.actor)
    assert w2.advance_outstanding == pytest.approx(10.0) and w2.W(Ledger.OMEGA) == pytest.approx(20.0)
    assert w2.troop_demand_held == pytest.approx(DELIVERY)       # the demand stock keeps the delivery's own 20
    # fund 10 and Ω 20 is 30 < 36: refused although the delivery's own 20 could be carried
    w3 = make_world()
    for actor in ("A", "B"):
        q0 = w3.post_root("H", 20)
        w3.award(q0, actor, 20, 500)
    seed_fund(w3, 10.0)
    omega_set(w3, 20.0)
    qd3 = w3.post_root("H", 20)
    w3.advance(w3.t + 2)
    assert w3.cases[qd3].state == "AVAILABLE" and not w3.troops and w3.troop_shortfall_awards >= 1
    check_all(w2); check_all(w3)


# ------------------------------------------------------------ §2.3 seat the queue
def test_the_reserve_seats_the_reviews_waiting():
    w = make_world(duty_cap_frac=1.0)                # six members; the cap would otherwise hold the seats at four
    for _ in range(6):
        w.create_plant(True, 20.0)                   # six submissions waiting for an initial reviewer
    w.advance(w.t + 1)
    assert w._waiting_initial == 6 and w._x_target >= 6
    assert sum(1 for a in w.actors.values() if a.on_duty) == 6      # A and B seated for the queue
    w2 = make_world(duty_cap_frac=1.0, seat_the_queue=False)
    for _ in range(6):
        w2.create_plant(True, 20.0)
    w2.advance(w2.t + 1)
    assert sum(1 for a in w2.actors.values() if a.on_duty) == 4     # the period's sizing alone
    check_all(w); check_all(w2)


# ------------------------------------------------------------ §2.4 a panel seat requires a determined record
def test_a_panel_seat_requires_a_determined_record_once_the_first_plant_is_adjudicated():
    w = make_world(pi0=0.1)
    q, r = pending_case(w, "A", "C")
    w.roll_audit(q)
    ra = w.assign_audit(q, "D")                      # dormant: no plant adjudicated yet, D undetermined
    w.advance(w.t + 1)
    w.complete_review(ra, F, 0)
    assert w.first_plant_adjudicated_at is None
    qp = w.create_plant(True, 20.0)
    rp = w.assign_initial(qp, "E")
    w.advance(w.t + 1)
    w.complete_review(rp, F, 0)                      # the first adjudication: §2.4 is live
    assert w.first_plant_adjudicated_at == w.t
    assert not w.actors["F"].panel_eligible and w.actors["F"].duty_eligible    # undetermined: initial seats only
    for _ in range(w.p.n_min):                       # D judges four bad plants rightly: determined and passing
        qb = w.create_plant(False, 20.0)
        rb = w.assign_initial(qb, "D")
        w.advance(w.t + 1)
        w.complete_review(rb, N, 0)
    assert len(w.actors["D"].plant_bad) == w.p.n_min and w.actors["D"].panel_eligible
    q2, r2 = pending_case(w, "B", "C")
    w.roll_audit(q2)
    with pytest.raises(RuleError, match="panel"):
        w.assign_audit(q2, "F")                      # undetermined
    ra2 = w.assign_audit(q2, "D")
    assert w.reviews[ra2].reviewer == "D"
    check_all(w)
    # the control: with the rule off an undetermined member sits on a panel after a plant, as under 1.5.0
    w2 = make_world(pi0=0.1, panel_determined=False)
    qp = w2.create_plant(True, 20.0)
    rp = w2.assign_initial(qp, "E")
    w2.advance(w2.t + 1)
    w2.complete_review(rp, F, 0)
    q3, r3 = pending_case(w2, "A", "C")
    w2.roll_audit(q3)
    assert w2.reviews[w2.assign_audit(q3, "F")].reviewer == "F"
    check_all(w2)


# ------------------------------------------------------------ §2.5 the reserve over two periods
def test_the_reserve_is_the_peak_demand_over_this_and_the_previous_period():
    w = make_world(period_ticks=8, period_plants=10_000)
    q, r = pending_case(w)
    busy_all_duty(w)
    omega_set(w, 0.0)                                # Ω empty: an empty fund refuses
    w.roll_audit(q)
    w.advance(w.t + 2)                               # refused at tick 4: R_T = 8
    assert w.R_T == pytest.approx(SEAT)
    seed_fund(w, SEAT)
    w.advance(w.t + 1)                               # carried
    tr = next(w.reviews[x] for x in w.cases[q].reviews if w.is_troop(w.reviews[x].reviewer))
    w.complete_review(tr.id, F, 0)                   # released
    w.advance(9)                                     # the first boundary: the previous period's peak still counts
    assert len(w.periods) == 1 and w.R_T == pytest.approx(SEAT) and w.troop_demand_now == 0.0
    w.advance(17)                                    # the second: gone
    assert len(w.periods) == 2 and w.R_T == 0.0
    check_all(w)


# ------------------------------------------------------------ I26 catches
def test_I26_catches_a_rebate_that_does_not_match_the_lateness():
    w = make_world(T_s=3)
    q, r = pending_case(w, wait=8)
    check_all(w)
    w.cases[q].rebate_owed = 1.0                     # the engine would never do this
    with pytest.raises(InvariantError, match="I26"):
        check_all(w)

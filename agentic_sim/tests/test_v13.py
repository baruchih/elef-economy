"""Design revision 3 — specification 1.3.0: inspection is membership.

Suspension from duty suspends market membership (§2.1): no new award, the held commitment finished.
Probation is the way back (§2.2): initial reviews only, audit odds pinned at 1, re-suspended by any plant
failure, readmitted when the one trailing record passes θ_duty with n_min new outcomes judged. The
members' duty cap with probationers filling the initial seats (§2.3), the duty fund paying the dial's
raised tax to the reviewers as an uplift (§2.4), plant capital counted on the pots alone (§2.5), the
newcomer pin, I22 and I23. The §6 figures are reproduced where the engine's six-actor world admits them.

One implementer's reading is in the engine and flagged in the text: the members' cap never falls below
the reserve's floor V_max + 1 (`World._member_cap`), because ⌈E_t/2⌉ at six actors is 3, below the X₀ = 4
of Appendix A and §20 — the baseline's own worlds would violate the revision at tick 0.
"""
import copy
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
try:
    import pytest
except ImportError:  # plain `python3 run_tests.py`
    sys.path.insert(0, os.path.dirname(__file__))
    from _mini_pytest import pytest

from sim import Params, World, RuleError, LedgerError, InvariantError, Ledger, check_all
from sim.engine import F, N, PLANT_REQ, PLANT_ACT, DUTY_FUND

ACTORS = ["A", "B", "C", "D", "E", "F"]
DUTY = ["C", "D", "E", "F"]


def make_world(budget=1000.0, actors=ACTORS, duty=DUTY, **over):
    kw = dict(plant_market=False,   # 2.6.0: these tests build plants submitted — the 1.2.0 construction, the control
              E0=0.0, H=1e9, omega_rate=0.0, Omega0=100.0, duty_turn_reviews=10_000, duty_turn_ticks=100_000,
              service_clock=False, omega_backs_fund=False, seat_the_queue=False, panel_determined=False, reserve_periods=1,
              troop_account=False, duty_cap_frac=0.5)      # 1.7.0: the merged fund and the half cap of this revision
    kw.update(over)
    kw.setdefault("floating", False)   # 2.0.0: these are 1.x behaviours and figures — the backing, the reserves, the pay-in at award
    return World(Params(**kw), actors, humans={"H": budget}, on_duty=duty)


def plant_to(w, reviewer, truth, verdict, cost=0.0, B=20.0):
    q = w.create_plant(truth, B)
    r = w.assign_initial(q, reviewer)
    w.advance(w.t + 1)
    w.complete_review(r, verdict, cost)
    return q, r


def stamp_out(w, aid, n=4):
    """`n` approved bad plants: the record crosses θ_duty on the fourth (n_min = 4)."""
    for _ in range(n):
        plant_to(w, aid, False, F)


def omega_total(w):
    L = w.ledger
    pools = sum(L.pools[c.id].total for c in w.cases.values() if c.plant is not None and c.id in L.pools)
    return L.wallet(Ledger.OMEGA).W + L.wallet(PLANT_REQ).W + L.wallet(PLANT_ACT).W + pools


# ------------------------------------------------------------ §2.1 membership is gated
def test_a_suspended_actor_wins_no_award_but_finishes_what_it_holds():
    w = make_world()
    stamp_out(w, "C")
    C = w.actors["C"]
    assert C.suspended_until is not None and not C.is_member and not C.on_duty
    q = w.post_root("H", 20)
    before = (copy.deepcopy(w.ledger.wallets), copy.deepcopy(w.ledger.locks), w.history.head, w.cases[q].state)
    with pytest.raises(RuleError, match="not a member"):
        w.award(q, "C", 20, 3)                       # refused whole
    assert (copy.deepcopy(w.ledger.wallets), copy.deepcopy(w.ledger.locks), w.history.head, w.cases[q].state) == before
    w.award(q, "B", 20, 3)                           # a member wins it
    assert w.cases[q].member_at_award
    # a pending actor on duty, suspended while its case is pending: the case settles by the ordinary rules
    w2 = make_world()
    qa = w2.post_root("H", 20)
    w2.award(qa, "A", 20, 1)
    w2.advance(1)
    w2.submit(qa)
    ra = w2.assign_initial(qa, "D")
    w2.advance(2)
    w2.complete_review(ra, F, 0)                     # A pending, capacity released
    w2.volunteer("A")
    w2.actors["A"].on_duty, w2.actors["A"].duty_since = True, w2.t
    stamp_out(w2, "A")                               # A suspended from the market while its case is pending
    assert not w2.actors["A"].is_member
    w2.advance(w2.cases[qa].window_end + 1)
    assert w2.cases[qa].state == "VESTED" and abs(w2.W("A") - (50 + 20 - 4 * 5)) < 0.1   # paid B; four bonds lost (v drifts a little with the burns)
    check_all(w)
    check_all(w2)


def test_membership_off_is_the_1_2_1_engine():
    w = make_world(membership=False)
    stamp_out(w, "C")
    assert w.actors["C"].suspended_until is not None
    q = w.post_root("H", 20)
    w.award(q, "C", 20, 3)                           # 1.2.1: suspension from duty only
    assert w.cases[q].actor == "C"
    check_all(w)


# ------------------------------------------------------------ §2.2 probation
def test_probation_pins_the_odds_allows_initial_reviews_only_and_any_failure_resuspends():
    w = make_world(T_susp=5)
    stamp_out(w, "C")
    C = w.actors["C"]
    until = C.suspended_until
    w.advance(until + 1)
    assert C.suspended_until is None and C.probation and not C.is_member
    assert C.p_eff == 1.0 and C.pinned and C.duty_eligible and not C.panel_eligible
    msgs = [e["payload"].get("msg", "") for e in w.history.entries if e["kind"] == "suspension"]
    assert "probation begins" in msgs
    # seated as a probationer (initial seats), it may take an initial review but no panel seat
    w.advance(w.t + 1)
    assert C.on_duty
    q = w.post_root("H", 20)
    w.award(q, "A", 20, 1)
    w.advance(w.t + 1)
    w.submit(q)
    r = w.assign_initial(q, "D")
    w.advance(w.t + 1)
    w.complete_review(r, F, 0)
    with pytest.raises(RuleError, match="challenge panel"):
        w.assign_audit(q, "C")
    with pytest.raises(RuleError, match="not a member"):
        w.award(w.post_root("H", 20), "C", 20, 3)
    # any plant failure re-suspends at once, clock restarted
    plant_to(w, "C", False, F)
    assert C.suspended_until == w.t + 5 and not C.probation and C.since_susp == 0
    check_all(w)


def test_readmission_needs_n_min_new_outcomes_and_a_passing_trailing_record_and_panel_seats_come_later():
    """§6, the reformed path: after four approvals the record is 5/6; four rejected bad plants bring it to
    (4+1)/(8+2) = 0.5 ≤ θ_duty with four new outcomes judged — readmitted — but 0.5 > θ_panel: no panel
    seat until the four approvals roll out of the window of twenty."""
    w = make_world(T_susp=5)
    stamp_out(w, "C")
    C = w.actors["C"]
    t_susp = w.t
    w.advance(C.suspended_until + 1)
    w.advance(w.t + 1)
    assert C.probation and C.on_duty
    for i in range(3):
        plant_to(w, "C", False, N, cost=1)           # three rejected: 5/9 = 0.56 > 0.5, and only 3 new
        assert C.probation and not C.is_member
    plant_to(w, "C", False, N, cost=1)               # the fourth: 5/10 = 0.5, four new outcomes
    assert not C.probation and C.is_member and C.a_hat == pytest.approx(0.5)
    assert C.readmitted_at == w.t and w.readmissions == 1 and w.readmission_ticks_sum == w.t - t_susp
    assert C.duty_eligible and not C.panel_eligible   # 0.5 > θ_panel = 0.2
    assert C.p_audit == w.p.p_start and not C.pinned  # §8.3 applies from 1.0 once readmitted (record determined)
    w.actors["C"].on_duty = False                    # off duty (the rotation refills the seat): awards return
    q = w.post_root("H", 20)
    w.award(q, "C", 20, 3)                           # a member again
    w.advance(w.t + 1)                               # the rotation refills C's seat
    # a passing record alone does not readmit: a slipped careful reviewer needs its four new outcomes too
    w2 = make_world(T_susp=5, n_min=2)
    plant_to(w2, "D", False, F)
    plant_to(w2, "D", False, F)                      # 3/4: suspended (n_min = 2)
    D = w2.actors["D"]
    w2.advance(D.suspended_until + 1)
    w2.advance(w2.t + 1)
    plant_to(w2, "D", False, N, cost=1)              # 3/5 = 0.6 > 0.5: one new outcome, record failing — stays
    assert D.probation
    plant_to(w2, "D", False, N, cost=1)              # 3/6 = 0.5 ≤ 0.5 with two new: readmitted
    assert D.is_member and not D.probation
    check_all(w)
    check_all(w2)


def test_newcomer_odds_are_pinned_until_the_bad_plant_record_is_determined():
    w = make_world()
    C = w.actors["C"]
    assert C.pinned and C.p_eff == 1.0
    # five stood approvals do not taper the odds while pinned
    for i in range(5):
        q = w.post_root("H", 20)
        w.award(q, ["A", "B"][i % 2], 20, 1)
        w.advance(w.t + 1)
        w.submit(q)
        r = w.assign_initial(q, "C")
        w.advance(w.t + 1)
        w.complete_review(r, F, 0)
        w.advance(w.cases[q].window_end + 1)
        assert w.reviews[r].status == "vested"
    assert C.streak == 5 and C.p_audit == 1.0 and C.p_eff == 1.0
    # four bad plants judged: the record is determined, the adaptive rule applies from 1.0
    for _ in range(4):
        plant_to(w, "C", False, N, cost=1)
    assert not C.pinned and C.p_eff == 1.0 and C.is_member
    for i in range(5):                               # five more stood: halves once
        q = w.post_root("H", 20)
        w.award(q, ["A", "B"][i % 2], 20, 1)
        w.advance(w.t + 1)
        w.submit(q)
        r = w.assign_initial(q, "C")
        w.advance(w.t + 1)
        w.complete_review(r, F, 0)
        w.advance(w.cases[q].window_end + 1)
    assert C.p_audit == pytest.approx(0.5)
    check_all(w)


# ------------------------------------------------------------ §2.3 the cap and the fill order
def test_members_cap_binds_above_the_reserve_floor_and_probationers_take_the_initial_seats():
    actors = [f"a{i:02d}" for i in range(20)]
    w = make_world(actors=actors, duty=actors[:4], n_min=1, T_susp=25, duty_turn_ticks=3)
    suspended = []
    while len(suspended) < 8:                        # eight stampers, one bad plant each (n_min = 1); the fill seats the next member
        on = next(a for a in sorted(w.actors.values(), key=lambda a: a.id) if a.on_duty and a.is_member)
        plant_to(w, on.id, False, F)
        w.advance(w.t + 1)
        suspended = [a.id for a in w.actors.values() if a.suspended_until is not None]
    E_t = sum(1 for a in w.actors.values() if a.is_member)
    assert E_t == 12 and w._member_cap(E_t) == 6
    w.X_t, w.member_seats = 10, 2                    # a sized-up reserve with two member seats
    w.advance(w.t + 1)
    on_m = [a for a in w.actors.values() if a.on_duty and a.is_member]
    assert len(on_m) == 6 and w.reserve_shortfall_now == 4       # members to the cap, no probationer yet
    w.advance(max(a.suspended_until for a in w.actors.values() if a.suspended_until) + 1)
    assert sum(1 for a in w.actors.values() if a.probation) == 8  # suspensions have run out: probationers
    w.X_t, w.member_seats = 10, 2                    # (a period end may have re-sized them meanwhile)
    w.advance(w.t + 1)                               # probationers take the initial seats; members keep the member seats
    on_m = [a for a in w.actors.values() if a.on_duty and a.is_member]
    on_p = [a for a in w.actors.values() if a.on_duty and a.probation]
    assert len(on_m) == 2 and len(on_p) == 8 and w.reserve_shortfall_now == 0
    assert all(not a.panel_eligible for a in on_p) and all(a.p_eff == 1.0 for a in on_p)
    check_all(w)


def test_the_cap_never_falls_below_the_reserve_floor_and_the_panel_floor_is_bounded_by_availability():
    w = make_world()                                  # six members: the literal cap would be 3 < X₀ = 4
    assert w._member_cap(6) == 4
    w.advance(5)
    assert sum(1 for a in w.actors.values() if a.on_duty) == 4
    w2 = make_world(n_min=1, T_susp=1000)
    for aid in ["C", "D", "E", "F"]:                 # four suspended, A and B members; B committed to a task
        plant_to(w2, aid, False, F)
        w2.advance(w2.t + 1)
    assert sum(1 for a in w2.actors.values() if a.is_member) == 2
    on = [a.id for a in w2.actors.values() if a.on_duty]
    assert sorted(on) == ["A", "B"]                   # the floor min(V_max − 1, 2) = 2: both seated, nobody free
    check_all(w2)


# ------------------------------------------------------------ §2.4 the duty fund
def test_the_dials_raised_tax_goes_to_the_fund_and_is_paid_out_by_role_weight():
    w = make_world(period_plants=2, period_ticks=10_000, omega_rate=0.05, Omega0=1000.0)
    plant_to(w, "C", False, F)
    plant_to(w, "E", False, F)                        # F̂ = 1 → m: 1 → 2
    w.advance(w.t + 1)
    assert w.m_t == 2.0
    om = w.W(Ledger.OMEGA)
    q = w.post_root("H", 20)
    w.award(q, "A", 20, 1)
    assert w.cases[q].omega == pytest.approx(2.0)                            # ω_t = 0.1 B
    assert w.W(Ledger.OMEGA) - om == pytest.approx(1.0) and w.W(DUTY_FUND) == pytest.approx(1.0)
    assert w.fund_in == pytest.approx(1.0)
    w.advance(w.t + 1)
    w.submit(q)
    r = w.assign_initial(q, "D")
    w.advance(w.t + 1)
    w.complete_review(r, F, 0)
    a = w.assign_audit(q, "F")                        # weights 1 and 1.5 settle together: 0.4 and 0.6 of the fund
    w.advance(w.t + 1)
    w.complete_review(a, F, 0)
    w.advance(w.cases[q].window_end + 1)
    assert w.reviews[r].uplift == pytest.approx(0.4) and w.reviews[a].uplift == pytest.approx(0.6)
    # the fixed fees are a hair under 2 and 3 (the pot was frozen at the index after two bond burns); the uplift is on top
    assert w.reviews[r].fee == pytest.approx(w.reviews[r].fee_fixed + 0.4) and w.reviews[a].fee == pytest.approx(w.reviews[a].fee_fixed + 0.6)
    assert w.W(DUTY_FUND) == pytest.approx(0.0) and w.fund_out == pytest.approx(1.0)
    # with the fund off the whole ω stays with Ω
    w2 = make_world(period_plants=2, period_ticks=10_000, omega_rate=0.05, Omega0=1000.0, duty_fund=False)
    plant_to(w2, "C", False, F)
    plant_to(w2, "E", False, F)
    w2.advance(w2.t + 1)
    om = w2.W(Ledger.OMEGA)
    q2 = w2.post_root("H", 20)
    w2.award(q2, "A", 20, 1)
    assert w2.W(Ledger.OMEGA) - om == pytest.approx(2.0) and w2.W(DUTY_FUND) == 0.0
    check_all(w)
    check_all(w2)


# ------------------------------------------------------------ §2.5 plant capital
def test_a_plant_ties_up_the_pots_only_and_its_price_and_guarantee_are_notional():
    w = make_world(Omega0=14.0)
    before = (copy.deepcopy(w.ledger.wallets), len(w.cases), w.history.head)
    with pytest.raises(LedgerError, match="cannot fund"):
        w.create_plant(True, 20.0)                    # needs φ^E + φ^F = 15
    assert (copy.deepcopy(w.ledger.wallets), len(w.cases), w.history.head) == before
    w = make_world(Omega0=15.0)
    q = w.create_plant(True, 20.0)
    c = w.cases[q]
    assert w.W(Ledger.OMEGA) == pytest.approx(0) and w.ledger.pool(q).escrow == 0.0
    assert w.ledger.lock_record(PLANT_ACT, f"G:{q}") == 0.0 and c.B == 20 and c.G == 10   # nominal terms
    r = w.assign_initial(q, "D")
    w.advance(w.t + 1)
    w.complete_review(r, F, 2)                        # a good plant, approved: pending, then vests
    w.advance(c.window_end + 1)
    assert c.state == "VESTED" and w.W(PLANT_ACT) == 0.0                     # no price paid to the plant actor
    assert omega_total(w) == pytest.approx(15 - 2 - 2)                        # the inspection's expense and fee
    w2 = make_world(Omega0=15.0)
    plant_to(w2, "C", False, F)                       # a bad plant stamped: Ω's net cost 0
    assert omega_total(w2) == pytest.approx(15) and w2.W(Ledger.OMEGA) == pytest.approx(15)
    check_all(w)
    check_all(w2)


# ------------------------------------------------------------ I22 and I23 catch
def test_I22_catches_an_award_to_a_non_member_and_a_probationer_on_a_panel():
    w = make_world(T_susp=5)
    q0 = w.post_root("H", 20)
    w.award(q0, "A", 20, 300)
    w.cases[q0].member_at_award = False
    with pytest.raises(InvariantError, match="I22"):
        check_all(w)
    w.cases[q0].member_at_award = True
    check_all(w)
    stamp_out(w, "C")
    w.advance(w.actors["C"].suspended_until + 1)
    w.advance(w.t + 1)
    assert w.actors["C"].probation and w.actors["C"].on_duty
    q = w.post_root("H", 20)
    w.award(q, "B", 20, 1)
    w.advance(w.t + 1)
    w.submit(q)
    r = w.assign_initial(q, "D")
    w.advance(w.t + 1)
    w.complete_review(r, F, 0)
    a = w.assign_audit(q, "E")
    w.reviews[a].reviewer, w.actors["E"].open_review, w.actors["C"].open_review = "C", None, a   # a seat moved by hand
    with pytest.raises(InvariantError):
        check_all(w)


def test_I23_catches_a_fund_that_does_not_reconcile_and_idle_members_above_the_cap():
    w = make_world(omega_rate=0.05)
    w.fund_flow = 5.0                                  # the fund's recorded flows no longer match its wallet
    with pytest.raises(InvariantError, match="I23"):
        check_all(w)
    w.fund_flow = 0.0
    check_all(w)
    actors = [f"a{i:02d}" for i in range(20)]
    w2 = make_world(actors=actors, duty=actors[:4])
    w2.advance(1)
    for aid in actors[4:12]:                          # twelve members on duty, idle, cap 10 (= ⌈20/2⌉)
        w2.actors[aid].on_duty = True
    with pytest.raises(InvariantError, match="I23"):
        check_all(w2)

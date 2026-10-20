"""Design revision 14 — the plant's disguise (2.6.0): §2.1 a plant goes through the market — posted as a root under a fresh plant-requester
name with a ceiling drawn from the trailing real roots', available to the free members, awarded to a fresh plant-actor name at the price and
work ticks the market's selection reports (the award as the report; past w_A at p_T, counted apart), submitted at a draw within (0, τ];
fresh names alias the two plant wallets; no fee, no clock, not in B̄ or P_t, marked as any root, counted among the available roots; the dial's
plant counts published at the close; §2.3 opaque identifiers on the public surface; I39, I40; plant_market off = 2.5.0 (create_plant).
"""
import os
import re
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
try:
    import pytest
except ImportError:  # plain `python3 run_tests.py`
    sys.path.insert(0, os.path.dirname(__file__))
    from _mini_pytest import pytest

from sim import Params, World, check_all
from sim.engine import RuleError, F, N, PLANT_REQ, PLANT_ACT
from sim.invariants import InvariantError, I39_the_plants_disguise, I40_opaque_identifiers, I21_plant_capital, public_id
from drivers.view import Public

ACTORS = ["A", "B", "C", "D", "E", "F"]
DUTY = ["C", "D", "E", "F"]


def make_world(budget=1000.0, actors=ACTORS, duty=DUTY, **over):
    kw = dict(E0=0.0, H=1e9, omega_rate=0.05, Omega0=100.0, duty_turn_reviews=10_000, duty_turn_ticks=100_000,
              r_s=1.0, T_s=10_000, pi0=0.0, period_ticks=60)
    kw.update(over)
    return World(Params(**kw), actors, humans={"H": budget}, on_duty=duty)


# ---------------------------------------------------------------- §2.1 the plant's life

def test_a_plant_is_posted_as_a_root_in_sequence_under_a_fresh_name_with_the_pots_minted_and_the_marker_sealed():
    w = make_world()
    q1 = w.post_root("H", 45)
    p = w.post_plant(False)
    q2 = w.post_root("H", 40)
    assert [int(x[1:]) for x in (q1, p, q2)] == [1, 2, 3]       # the id minted at the posting, in sequence with the roots around it
    c = w.cases[p]
    assert c.state == "AVAILABLE" and c.is_root and c.plant is False and c.plant_market and c.t_post == 0 and c.actor is None
    assert c.requester.startswith("plant_req:") and w.ledger.resolve(c.requester) == PLANT_REQ
    assert c.beta == pytest.approx(w.price_level())              # before the first closed period: the drivers' default, P_t
    assert c.posting_lock == pytest.approx(c.beta + c.phi_E + c.phi_F)     # the all-in without a fee: a plant pays none
    assert w.ledger.lock_record(c.requester, f"post:{p}") == pytest.approx(c.posting_lock)
    assert any(e.kind == "mint_plant" and e.dst == PLANT_REQ and e.amount == pytest.approx(c.posting_lock) for e in w.ledger.events)
    assert w.history.matches(c.plant_hseq, "plant_created", {"t": 0, "case": p, "commit": c.plant_commit})
    assert w.plants_posted == 1 and w.period["plants_posted"] == 1
    check_all(w)


def test_the_award_is_the_markets_report_the_plant_actor_takes_it_and_the_member_is_not_committed():
    w = make_world()
    p = w.post_plant(False)
    a_before = (w.ledger.wallet("A").U, w.ledger.wallet("A").L)
    n_before, price_n_before = w.period["award_n"], w.period["price_n"]
    fee_before = w.omega_fee_income
    w.award(p, "A", 15, 4)                                        # the driver's selection reports A at 15 for 4 ticks
    c = w.cases[p]
    assert c.state == "COMMITTED" and c.actor.startswith("plant_act:") and w.ledger.resolve(c.actor) == PLANT_ACT
    assert c.plant_report_by == "A" and not c.plant_at_floor
    assert w.actors["A"].committed is None and (w.ledger.wallet("A").U, w.ledger.wallet("A").L) == a_before   # A learns nothing more
    assert c.B == 15 and c.tau == 4 and c.deadline == 4 and c.t_award == 0   # the price and the work ticks come with the report
    assert c.G == 8 and w.ledger.lock_record(c.actor, f"G:{p}") == pytest.approx(8.0)   # ⌈0.5 × 15⌉, minted and locked
    assert w.ledger.pools[p].escrow == pytest.approx(15.0)
    assert 0 < c.plant_submit_at <= c.deadline
    assert (w.period["award_n"], w.period["price_n"]) == (n_before, price_n_before)   # neither B̄ nor P_t
    assert w.omega_fee_income == fee_before and c.omega == 0.0                        # no fee
    assert w.plant_bids_lost == 1 and w.plants_awarded == 1
    with pytest.raises(RuleError):
        w.submit(p)                                               # nobody submits for the plant actor
    check_all(w)


def test_the_plant_actor_submits_at_its_drawn_tick_and_the_plant_is_adjudicated_and_destroyed_as_before():
    w = make_world()
    p = w.post_plant(False)
    w.award(p, "A", 15, 4)
    c = w.cases[p]
    w.advance(c.plant_submit_at)
    assert c.state == "COMMITTED"
    w.advance(c.plant_submit_at + 1)
    assert c.state == "SUBMITTED" and c.t_submit == c.plant_submit_at
    rid = w.assign_initial(p, "C")
    w.complete_review(rid, F, 0.0)                                # a stamp on a bad plant
    assert c.plant_outcome == "failure" and c.state == "FINAL_N" and w.actors["C"].plant_bad[-1][1] is True
    w.advance(w.t + 40)
    assert c.tree_closed
    assert w.ledger.wallet(PLANT_REQ).W == pytest.approx(0.0) and w.ledger.wallet(PLANT_ACT).W == pytest.approx(0.0)   # destroyed
    assert any(e.kind == "retire_plant" for e in w.ledger.events)
    assert w.ledger.wallet(w.ledger.OMEGA).W == pytest.approx(100.0)   # nothing minted for the plant reached Ω
    check_all(w)


def test_a_good_plant_vests_its_price_to_the_plant_actor_and_everything_is_destroyed_at_closure():
    w = make_world()
    p = w.post_plant(True)
    w.award(p, "B", 12, 3)
    c = w.cases[p]
    w.advance(c.plant_submit_at + 1)
    rid = w.assign_initial(p, "D")
    w.complete_review(rid, F, 2.0)                                # right: stood
    assert c.plant_outcome == "stood" and c.state == "PENDING"
    w.advance(c.window_end + 2)
    assert c.state == "VESTED" and c.tree_closed
    assert w.ledger.wallet(PLANT_ACT).W == pytest.approx(0.0) and w.ledger.wallet(PLANT_REQ).W == pytest.approx(0.0)
    check_all(w)


def test_a_plant_unbid_by_w_A_goes_to_its_actor_at_the_states_price_counted_apart_from_the_troops():
    w = make_world(w_A=3)
    p = w.post_plant(True)
    w.advance(6)
    c = w.cases[p]
    assert c.actor.startswith("plant_act:") and c.plant_at_floor and c.B == pytest.approx(w._state_price(c.beta))
    assert c.tau == w.p.tau_T and c.plant_report_by is None
    assert w.troop_summons_deliveries == 0 and w.plants_awarded_at_floor == 1 and not c.troop_award
    check_all(w)


def test_fresh_names_per_plant_alias_the_two_wallets_and_no_two_plants_share_one():
    w = make_world()
    ps = [w.post_plant(i % 2 == 0) for i in range(4)]
    for i, p in enumerate(ps):
        w.award(p, ACTORS[i % 2], 10, 3)
    reqs = [w.cases[p].requester for p in ps]
    acts = [w.cases[p].actor for p in ps]
    assert len(set(reqs)) == 4 and len(set(acts)) == 4
    assert {w.ledger.resolve(r) for r in reqs} == {PLANT_REQ} and {w.ledger.resolve(a) for a in acts} == {PLANT_ACT}
    assert len(w.plant_names) == 8
    I39_the_plants_disguise(w)
    check_all(w)


def test_a_plant_is_a_root_in_every_other_respect_marked_below_the_reservation_and_counted_as_available():
    w = make_world(state_reservation=30.0)                        # the floor above P_t: the drawn ceiling (20) lands below it
    pub = Public(w)
    before = pub.market()["available_roots"]
    p = w.post_plant(False)
    c = w.cases[p]
    assert c.below_reservation and c.below_reservation_since == 0  # the mark is the engine's reading of a ceiling, not of who posted
    assert pub.market()["available_roots"] == before + 1
    assert not w._clock_runs(c)                                   # no customer: no clock
    check_all(w)


def test_the_draws_read_the_trailing_real_roots_after_a_closed_period():
    w = make_world(period_ticks=10, period_plants=10_000)
    q = w.post_root("H", 24)
    w.award(q, "A", 20, 9)
    w.advance(3)
    w.submit(q)                                                   # a real delivery three ticks after its award
    w.advance(12)                                                 # the period closes: the trailing window holds β 24, τ 9, delivery 3
    assert w._trailing and w._trailing[-1]["betas"] == [24.0] and w._trailing[-1]["taus"] == [9] and w._trailing[-1]["deliv"] == [3]
    p = w.post_plant(True)
    assert w.cases[p].beta == pytest.approx(24.0)                 # the ceiling drawn from the real roots'
    w.award(p, "B", 18, 9)
    assert w.cases[p].plant_submit_at == w.t + 3                  # the plant actor's time to submission, the real deliveries'


# ---------------------------------------------------------------- §2.3 opaque identifiers, the view

def test_the_public_surface_translates_identifiers_both_ways_and_they_carry_no_order():
    w = make_world()
    pub = Public(w)
    ids = [pub.post_root("H", 10 + i) for i in range(14)]
    assert all(re.fullmatch(r"c[0-9a-f]{10}", x) for x in ids) and len(set(ids)) == 14
    assert sorted(ids) != ids                                     # not in creation order
    c0 = pub.case(ids[3])
    assert c0.id == ids[3] and c0.root == ids[3] and c0.beta == 13 and w.cases["q4"].id == "q4"   # the engine on the counter
    pub.award(ids[3], "A", 10, 4)
    assert w.cases["q4"].actor == "A" and pub.case(ids[3]).actor == "A"
    evs = pub.events_since(0)
    assert any(e.case == ids[3] for e in evs) and not any(re.fullmatch(r"q\d+", e.case or "") for e in evs)   # the record on the public surface
    with pytest.raises(RuleError):
        pub.case("c0000000000")
    I40_opaque_identifiers(w)
    assert public_id("q1") != public_id("q2")


def test_the_dials_plant_counts_are_published_at_the_periods_close():
    w = make_world(period_ticks=10, period_plants=10_000)
    pub = Public(w)
    p = w.post_plant(False)
    w.award(p, "A", 15, 4)
    assert not w.periods                                          # no closed period yet: nothing published
    w.advance(12)
    assert w.periods[-1]["plants_posted"] == 1 and w.periods[-1]["plants_awarded"] == 1
    assert pub.dial()["periods"][-1]["plants_posted"] == 1


# ---------------------------------------------------------------- I39, the control

def test_i39_catches_a_fee_paid_a_shared_name_and_a_submission_off_its_tick():
    w = make_world()
    p = w.post_plant(False)
    w.award(p, "A", 15, 4)
    c = w.cases[p]
    c.omega = 1.0
    with pytest.raises(InvariantError):
        I39_the_plants_disguise(w)
    c.omega = 0.0
    p2 = w.post_plant(True)
    w.award(p2, "B", 15, 4)
    saved, w.cases[p2].actor = w.cases[p2].actor, c.actor      # two plants, one actor name
    with pytest.raises(InvariantError):
        I39_the_plants_disguise(w)
    w.cases[p2].actor = saved
    c.plant_submit_at = c.deadline + 1
    with pytest.raises(InvariantError):
        I39_the_plants_disguise(w)


def test_plant_market_off_is_2_5_0_create_plant_built_submitted_and_post_plant_refused():
    w = make_world(plant_market=False)
    with pytest.raises(RuleError):
        w.post_plant(True)
    p = w.create_plant(False, 20)
    assert w.cases[p].state == "SUBMITTED" and w.cases[p].requester == PLANT_REQ and not w.cases[p].plant_market
    I21_plant_capital(w)                                          # the 1.2.0 construction: notional award and guarantee
    I39_the_plants_disguise(w)                                    # silent under the flag
    check_all(w)
    w2 = make_world()
    with pytest.raises(RuleError):
        w2.create_plant(False, 20)                                # under 2.6.0 a plant goes through the market


# ---------------------------------------------------------------- Appendix S, the ruling after run 21: the p_T path follows the summons pass

def test_a_plant_unbid_by_w_A_is_refused_for_capacity_as_a_root_would_be_and_takes_no_place_in_N_T():
    w = make_world(w_A=3, N_T=1)                                  # a delivery needs two places: the state refuses every award
    p = w.post_plant(True)
    w.advance(8)
    c = w.cases[p]
    assert c.state == "AVAILABLE" and c.actor is None
    assert c.refused == "capacity" and c.refused_capacity >= 1 and c.capacity_told and c.refused_at is not None
    assert w._places_held() == 0 and w.plants_refused_capacity >= 1 and w.plants_awarded_at_floor == 0 and not w.troops
    I39_the_plants_disguise(w)
    check_all(w)


def test_a_plant_unbid_by_w_A_is_refused_for_credit_above_the_wall_and_served_once_the_debt_is_within_it():
    w = make_world(w_A=3, period_ticks=10, period_plants=10_000, debt_bound_periods=1)
    w.advance(12)                                                 # a period closed: the wall is that period's fee income
    assert w._debt_bound() < float("inf")
    p = w.post_plant(False)
    w._debt_bound = lambda: -1.0                                  # the wall below the debt (0): the pass refuses every delivery for credit
    w.advance(w.t + 4)
    c = w.cases[p]
    assert c.state == "AVAILABLE" and c.refused == "credit" and c.refused_credit >= 1 and w.plants_refused_credit >= 1
    del w._debt_bound                                             # the wall back where the rule puts it
    w.advance(w.t + 1)
    assert c.state == "COMMITTED" and c.plant_at_floor and c.refused is None   # served at p_T, the mark off
    check_all(w)


def test_the_submission_draw_can_be_pinned_for_the_lag_cell():
    w = make_world(plant_submit_fixed=2)
    p = w.post_plant(True)
    w.award(p, "A", 15, 5)
    assert w.cases[p].plant_submit_at == w.cases[p].t_award + 2
    w2 = make_world(plant_submit_fixed=9)                         # never past the deadline
    p2 = w2.post_plant(True)
    w2.award(p2, "A", 15, 4)
    assert w2.cases[p2].plant_submit_at == w2.cases[p2].deadline


# ---------------------------------------------------------------- the Q2 probe's correction: the plant's submission in the members' step

def test_the_orchestrators_instrument_submits_for_the_plant_actor_at_its_tick_and_not_before():
    w = make_world(plant_submit_fixed=3)
    p = w.post_plant(False)
    w.award(p, "A", 15, 5)
    c = w.cases[p]
    assert c.plant_submit_at == 3
    with pytest.raises(RuleError):
        w.submit_plant(p)                                             # before the drawn tick
    q = w.post_root("H", 30); w.award(q, "B", 20, 4)
    with pytest.raises(RuleError):
        w.submit_plant(q)                                             # not a plant
    w.advance(3)
    w.submit_plant(p)                                                 # at the tick, in the members' submission step
    assert c.state == "SUBMITTED" and c.t_submit == 3 and c.seat_since == 3
    with pytest.raises(RuleError):
        w.submit_plant(p)                                             # not twice
    I39_the_plants_disguise(w)
    w.advance(4)                                                      # the engine's step finds nothing left to do
    assert c.state == "SUBMITTED" and c.t_submit == 3
    check_all(w)

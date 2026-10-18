"""Patch 1.7.1 — the award summons is per request, not per tick (1.4.0 §2.3, §12.3; a conformance correction).

A root request that no eligible member has been awarded within w_A ticks is awarded to a troop. A free member takes the
oldest request it can; the others, unawarded past their window with nobody offering for them, are the state's. So at the
seating step the requests that have waited w_A and exceed the free fundable members are summoned for, oldest first, after
the members have taken theirs. Members first is unchanged: a troop never takes an award a member offered for. 1.4.0–1.7.0
read the rule per tick — one free member blocked every award summons that tick, however long the queue — which run 9 showed
as the 50/50 collapse (79% of ticks stalled with 289 requests waiting and two members free).
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

ACTORS = ["A", "B", "C", "D", "E", "F"]
DUTY = ["C", "D", "E", "F"]


def make_world(budget=1000.0, actors=ACTORS, duty=DUTY, **over):
    # 1.7.0 defaults; no emission, no service fee, no plants, the service target far off, Ω 100, long turns
    kw = dict(E0=0.0, H=1e9, omega_rate=0.0, Omega0=100.0, duty_turn_reviews=10_000, duty_turn_ticks=100_000,
              r_s=1.0, T_s=10_000, pi0=0.0)
    kw.update(over)
    return World(Params(**kw), actors, humans={"H": budget}, on_duty=duty)


def market_price(w, actor="A", tau=500):
    """One award to a member at 20 sets B̄ = 20 and commits the member for a long time."""
    q = w.post_root("H", 20)
    w.award(q, actor, 20, tau)
    return q


def test_requests_beyond_the_free_members_are_summoned_for_oldest_first_and_the_oldest_are_left_to_the_members():
    w = make_world()
    market_price(w, "A")                              # A committed; B is the one free fundable member
    q1 = w.post_root("H", 20)
    q2 = w.post_root("H", 20)
    q3 = w.post_root("H", 20)
    t_post = w.t
    w.advance(t_post + 1)                             # waited 1 < w_A: nothing is summoned, nothing is counted
    assert all(w.cases[q].state == "AVAILABLE" for q in (q1, q2, q3))
    assert w.troop_summons_deliveries == 0 and w.awards_left_to_members == 0
    w.advance(t_post + 2)                             # waited w_A = 2: three wait, one member is free
    assert w.awards_waiting_now == 3 and w.members_free_now == 1
    assert w.awards_left_to_members == 1 and w.period["awards_left_to_members"] == 1
    assert w.cases[q1].state == "AVAILABLE" and w.cases[q1].actor is None       # the oldest is the market's
    for q in (q2, q3):                                                            # the rest are the state's, oldest first
        c = w.cases[q]
        assert c.state == "COMMITTED" and w.is_troop(c.actor) and c.troop_award and c.B == pytest.approx(20)
    assert w.troop_summons_deliveries == 2 and w.troop_shortfall_awards == 0
    assert w.troops[w.cases[q2].actor]["case"] == q2 and int(w.cases[q2].actor[1:]) < int(w.cases[q3].actor[1:])
    # members first, unchanged: the free member takes the request left to it
    w.award(q1, "B", 20, 5)
    assert w.cases[q1].state == "COMMITTED" and w.cases[q1].actor == "B" and not w.cases[q1].troop_award
    check_all(w)


def test_free_members_enough_for_the_queue_mean_no_summons_and_the_count_accrues_per_seating():
    w = make_world()
    q1 = w.post_root("H", 20)
    q2 = w.post_root("H", 20)                         # two wait; A and B are free and fundable
    t_post = w.t
    w.advance(t_post + 4)                             # three seatings past the window (t+2, t+3, t+4)
    assert all(w.cases[q].state == "AVAILABLE" for q in (q1, q2))
    assert w.troop_summons_deliveries == 0 and w.troop_shortfall_awards == 0
    assert w.awards_waiting_now == 2 and w.members_free_now == 2
    assert w.awards_left_to_members == 3 * 2          # both requests left to the members at each of the three seatings
    # the 1.4.0 case — one request, one free member: still no summons however long it waits
    market_price(w, "A")
    w.advance(w.t + 5)
    assert all(w.cases[q].state == "AVAILABLE" for q in (q1, q2)) or w.troop_summons_deliveries == 1
    # one free member (B) for two waiting requests: exactly the younger one is summoned for
    assert w.troop_summons_deliveries == 1 and w.cases[q1].state == "AVAILABLE" and w.is_troop(w.cases[q2].actor)
    check_all(w)


def test_a_long_queue_with_two_members_free_is_served_two_short_of_its_length_not_stalled():
    """Run 9's 50/50 shape in six actors: the queue beyond the free members is the state's at once, bounded by funds."""
    w = make_world(Omega0=200.0)
    qs = [w.post_root("H", 20) for _ in range(5)]     # five wait; A and B are free and fundable; B̄ = β = 20
    t_post = w.t
    w.advance(t_post + 2)
    assert w.awards_waiting_now == 5 and w.members_free_now == 2 and w.awards_left_to_members == 2
    assert [w.cases[q].state for q in qs] == ["AVAILABLE", "AVAILABLE", "COMMITTED", "COMMITTED", "COMMITTED"]
    assert all(w.is_troop(w.cases[q].actor) for q in qs[2:]) and w.troop_summons_deliveries == 3
    # Ω advanced each delivery's own shortfall (cost 10 + G 10, the troop account empty) and nothing was refused
    assert w.advances_made == pytest.approx(60.0) and w.troop_shortfall_awards == 0
    assert w.W(Ledger.OMEGA) == pytest.approx(200.0 - 60.0)
    # no request waited: the clocks of the three summoned stopped at the award's first verdict later; the two left are the market's
    w.award(qs[0], "A", 20, 2)
    w.award(qs[1], "B", 20, 2)
    w.advance(w.t + 1)
    assert w.awards_waiting_now == 0 and w.members_free_now is None
    check_all(w)


def test_the_period_record_carries_the_members_share():
    w = make_world(period_ticks=6)
    market_price(w, "A")
    q1 = w.post_root("H", 20)
    w.advance(w.t + 7)                                # the first period has ended
    assert w.cases[q1].state == "AVAILABLE"           # one request, one free member: the market's at every seating
    assert w.periods and w.periods[-1]["awards_left_to_members"] >= 1 and w.troop_summons_deliveries == 0
    check_all(w)

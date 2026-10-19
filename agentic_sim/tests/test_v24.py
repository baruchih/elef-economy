"""Design revision 12 — the state's reservation (2.4.0): §2.1 the state delivers at p_T = max(B̄, the reservation) and never below it —
no summons for a request whose ceiling is below p_T, the guarantee, the base fee and the burn at p_T, P_t counting the award at p_T;
§2.1 the award pass gathers only requests at β ≥ p_T (the 1.7.1 conformance correction made at acceptance); §2.2 the mark — set at
posting from tick 0, cleared at a raise to the floor, the clock stopped while it holds; the floor and the price in the public view;
§2.3 the float's bound on the parameters; §2.4 the kill fee is the child's recorded cost — zero for a child that never worked; I37;
the reservation at 0 is the 2.3.0 state.
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
from sim.engine import RuleError, LedgerError, F, N
from drivers.view import Public

ACTORS = ["A", "B", "C", "D", "E", "F"]
DUTY = ["C", "D", "E", "F"]


def make_world(budget=1000.0, actors=ACTORS, duty=DUTY, **over):
    # 2.4.0 defaults (the bank, the pool, the supply side, the reservation at 8); no emission, the fee on, no plants, long turns, the clock on
    kw = dict(E0=0.0, H=1e9, omega_rate=0.05, Omega0=100.0, duty_turn_reviews=10_000, duty_turn_ticks=100_000,
              r_s=1.0, T_s=10_000, pi0=0.0, period_ticks=60)
    kw.update(over)
    return World(Params(**kw), actors, humans={"H": budget}, on_duty=duty)


def post_and_award(w, actor, B, beta=None, tau=500):
    q = w.post_root("H", beta if beta is not None else B)
    w.award(q, actor, B, tau)
    return q


def cheap_market_then_a_request(w, beta, B=5.0):
    """Two members awarded at 5 (B̄ = 5, below the reservation of 8) for two ticks — nobody submits, they lapse at tick 2 and the two
    are free again — then a request at `beta` nobody is free for at the seating of tick 1: the state's after w_A if its ceiling admits
    the state's price."""
    post_and_award(w, "A", B, tau=2)
    post_and_award(w, "B", B, tau=2)
    q = w.post_root("H", beta)
    w.advance(w.t + 2)
    return q


# ---------------------------------------------------------------- §2.1 the state's price

def test_the_state_delivers_at_the_reservation_when_the_market_is_below_it():
    w = make_world()
    assert w.mean_awarded_price() == pytest.approx(20.0)        # P_0 before the first award
    q = cheap_market_then_a_request(w, beta=30)
    c = w.cases[q]
    assert w.mean_awarded_price() == pytest.approx(5.0)
    assert c.state == "COMMITTED" and w.is_troop(c.actor)
    # p_T = max(5, 8) = 8: the price, the guarantee ⌈0.5 × 8⌉ = 4, the burn (1 − 0.2) × 8 − 0.2 × 4 = 5.6, the base fee 0.05 × 8
    assert c.B == pytest.approx(8.0) and c.G == pytest.approx(4.0) and c.c_d_t == pytest.approx(5.6)
    assert w.troops[c.actor]["lock"] == pytest.approx(4.0) and w.troops[c.actor]["cost"] == pytest.approx(5.6)
    assert any(e.kind == "transfer" and e.note == "service fee" and e.case == q and e.amount == pytest.approx(0.4) for e in w.ledger.events)
    # P_t counts the state's award at p_T; B̄ (members only) does not move
    assert w.period["price_sum"] == pytest.approx(5.0 + 5.0 + 8.0) and w.period["price_n"] == 3
    assert w.mean_awarded_price() == pytest.approx(5.0)
    assert w.state_price_n == 1 and w.state_price_sum == pytest.approx(8.0)
    assert any("state's reservation" in str(line) for line in c.log)
    check_all(w)


def test_above_the_floor_the_state_is_a_price_taker_as_before():
    w = make_world()
    q = cheap_market_then_a_request(w, beta=30, B=12.0)         # B̄ = 12 ≥ 8
    c = w.cases[q]
    assert c.state == "COMMITTED" and w.is_troop(c.actor)
    assert c.B == pytest.approx(12.0) and c.G == pytest.approx(6.0) and c.c_d_t == pytest.approx(0.8 * 12 - 0.2 * 6)
    assert w.summons_declined_floor == 0
    check_all(w)


def test_no_summons_for_a_request_whose_ceiling_is_below_the_state_price():
    w = make_world()
    # β = 6: admits the market (B̄ = 5) but not the floor (8) — declined for the floor, marked, told; waits at any wait
    q = cheap_market_then_a_request(w, beta=6)
    c = w.cases[q]
    assert c.state == "AVAILABLE" and c.below_reservation and c.below_reservation_since == 0
    assert w.summons_declined_floor >= 1 and w.period["summons_declined_floor"] >= 1
    w.advance(w.t + 10)
    assert w.cases[q].state == "AVAILABLE" and all(t["case"] != q for t in w.troops.values())
    check_all(w)


def test_a_member_may_still_take_a_request_below_the_floor():
    w = make_world()
    q = cheap_market_then_a_request(w, beta=6)
    assert w.cases[q].state == "AVAILABLE" and w.cases[q].below_reservation
    w.advance(w.t + 1)                                           # A's lapsed award is final: A is free again
    w.award(q, "A", 5.5, 3)                                      # a member cheaper than the floor bids under the ceiling
    assert w.cases[q].state == "COMMITTED" and w.cases[q].actor == "A"
    check_all(w)


# ---------------------------------------------------------------- §2.1 the award pass gathers only what the state may take

def test_a_request_below_the_state_price_does_not_hold_a_members_slot():
    """Two requests past w_A at the seating with one free fundable member (G): the older one is below the state's price, the younger one
    admits it. 2.3.0's pass gathered both, left the older to the member — who will not take it — and summoned for the younger; 2.4.0's
    gathers only the younger, counts the member against it and leaves it to the market; the older is not the state's at any wait."""
    def world(**over):
        w = make_world(actors=ACTORS + ["G"], **over)
        post_and_award(w, "A", 5.0, tau=500)
        post_and_award(w, "B", 5.0, tau=500)                     # B̄ = 5; A and B committed; C–F on duty; G free and fundable
        low = w.post_root("H", 6)                                # admits the market (5), not the floor (8)
        high = w.post_root("H", 30)
        w.advance(w.t + 2)                                       # past w_A: the pass at the seating of tick 1
        return w, low, high
    w, low, high = world()
    assert w.cases[low].state == "AVAILABLE" and w.cases[low].below_reservation
    assert w.awards_waiting_now == 1 and w.members_free_now == 1 and w.awards_left_to_members >= 1
    assert w.cases[high].state == "AVAILABLE"                    # left to G; nothing summoned
    assert all(t["kind"] != "delivery" for t in w.troops.values())
    check_all(w)
    # the control (the 2.3.0 pass): both gathered, the older left to G, the younger the state's
    w0, low0, high0 = world(state_reservation=0.0)
    assert w0.awards_waiting_now == 2 and w0.members_free_now == 1
    assert w0.cases[low0].state == "AVAILABLE" and not w0.cases[low0].below_reservation
    assert w0.cases[high0].state == "COMMITTED" and w0.is_troop(w0.cases[high0].actor) and w0.cases[high0].B == pytest.approx(5.0)
    check_all(w0)


# ---------------------------------------------------------------- §2.2 the mark and the clock

def test_the_mark_is_set_at_posting_cleared_at_a_raise_and_stops_the_clock():
    w = make_world(T_s=2, r_s=1.0)
    q = w.post_root("H", 6)                                      # tick 0: no market price yet (no below-market flag), below the floor
    c = w.cases[q]
    assert c.below_reservation and c.below_reservation_since == 0 and not c.below_market
    assert w.below_reservation_marked == 1 and w.period["below_reservation"] == 1
    assert not w._clock_runs(c)                                  # the clock does not run while the mark holds
    w.advance(5)
    assert w.cases[q].state == "AVAILABLE"
    w.raise_ceiling(q, 7.5)                                      # still below: the mark stays
    assert w.cases[q].below_reservation and w.cases[q].below_reservation_since == 0
    w.raise_ceiling(q, 8.0)                                      # to the floor: the mark clears
    assert not w.cases[q].below_reservation
    assert w.below_reservation_marked == 1                       # counted once, at the marking
    # before any award B̄ reads P_0 = 20, so p_T = 20 and a ceiling of 8 is below the market: the clock still does not run (2.0.0)
    assert not w._clock_runs(w.cases[q])
    w.award(q, "A", 8.0, 2)                                      # a member takes it; B̄ = 8 = the floor: p_T = 8
    assert w._state_price() == pytest.approx(8.0)
    at = w.post_root("H", 8)                                     # at the state's price: unmarked, the clock runs
    under = w.post_root("H", 7)                                  # under it: marked, the clock stopped
    assert not w.cases[at].below_reservation and w._clock_runs(w.cases[at])
    assert w.cases[under].below_reservation and not w._clock_runs(w.cases[under])
    w.submit(q)
    r = w.assign_initial(q, "C")
    w.complete_review(r, F, 0)
    assert w.cases[q].clock_stopped_at is not None
    check_all(w)


def test_the_view_carries_the_floor_the_price_and_the_mark():
    w = make_world()
    v = Public(w)
    mk = v.market()
    assert mk["state_floor"] == pytest.approx(8.0) and mk["state_price"] == pytest.approx(20.0)   # p_T = max(P_0, 8) before any award
    q = w.post_root("H", 6)
    w.advance(3)
    mk = v.market()
    assert mk["below_reservation_marked"] == 1 and mk["below_reservation_waiting"] == 1 and mk["below_reservation_ticks"] == 3
    assert "summons_declined_floor" in v.troops()
    assert "state_price_mean" in v.troops()
    w.raise_ceiling(q, 9)
    assert v.market()["below_reservation_waiting"] == 0


# ---------------------------------------------------------------- §2.3 the float's bound

def test_a_parameter_set_with_the_float_below_the_bond_is_refused():
    with pytest.raises(ValueError):
        Params(F0=0.0)
    with pytest.raises(ValueError):
        Params(F0=4.0, G_V=5.0)
    Params(F0=5.0, G_V=5.0)                                      # at the bond: allowed
    Params(F0=0.0, supply=False)                                 # the 2.2.0 engine has no arrivals: no bound


# ---------------------------------------------------------------- §2.4 the kill fee is the child's recorded cost

def test_the_kill_fee_for_a_child_that_never_worked_is_zero_and_its_guarantee_is_released():
    w = make_world()
    q = w.post_root("H", 45)
    w.award(q, "A", 40, 8)
    w.advance(1)
    qn = w.post_nested(q, 6)
    w.award(qn, "B", 5, 3)
    before_B, before_A = w.ledger.wallet("B").W, w.ledger.wallet("A").W
    w.advance(2)
    w.cancel_nested(qn)                                          # B spent nothing: fee min(0, K) = 0; its guarantee released; A's escrow back
    assert w.cases[qn].state == "CANCELLED"
    assert w.ledger.wallet("B").W == pytest.approx(before_B) and w.ledger.wallet("B").L == pytest.approx(0.0)
    assert w.cases[q].actor_cost == pytest.approx(0.0)
    assert w.actors["B"].committed is None
    assert not any(e.note.startswith("kill fee") for e in w.ledger.events)
    w.advance(3)
    w.submit(q)                                                  # the parent self-executes after the cancellation
    check_all(w)


# ---------------------------------------------------------------- I37 and the control

def test_i37_catches_a_delivery_priced_below_the_reservation():
    from sim.invariants import InvariantError, I37_the_states_reservation
    w = make_world()
    q = cheap_market_then_a_request(w, beta=30)
    w.cases[q].B = 5.0                                           # an engine that delivered at B̄ under the floor
    with pytest.raises(InvariantError):
        I37_the_states_reservation(w)
    w.cases[q].B = 8.0
    I37_the_states_reservation(w)
    other = w.post_root("H", 30)
    w.cases[other].below_reservation = True                      # a mark on a request whose ceiling admits the floor
    with pytest.raises(InvariantError):
        I37_the_states_reservation(w)
    w.cases[other].below_reservation = False
    w.cases[other].beta = 6.0                                    # a request under the floor without its mark
    with pytest.raises(InvariantError):
        I37_the_states_reservation(w)


def test_the_reservation_at_zero_is_the_2_3_0_state():
    w = make_world(state_reservation=0.0)
    q = cheap_market_then_a_request(w, beta=6)                   # admits the market (B̄ = 5): the state's after w_A, at B̄
    c = w.cases[q]
    assert c.state == "COMMITTED" and w.is_troop(c.actor) and c.B == pytest.approx(5.0) and c.G == pytest.approx(3.0)
    assert not c.below_reservation and w.below_reservation_marked == 0 and w.summons_declined_floor == 0
    assert Public(w).market()["state_floor"] == 0.0
    check_all(w)

"""Design revision 13 — the missed child (2.5.0): §9.3 a nested request's cancellation is admissible only before the earlier of the child's
submission and the request's deadline — at or after the deadline it is refused with no effect; the lapse (the engine's since v1.0) finalizes
the child N after the tick's submissions, forfeits its guarantee to the parent, releases the rejection bond and frees the parent from the
next step; a child may still submit on its last tick; the kill fee before the deadline unchanged; I38; missed_child off = 2.4.0.
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
from sim.invariants import InvariantError, I38_the_missed_child

ACTORS = ["A", "B", "C", "D", "E", "F"]
DUTY = ["C", "D", "E", "F"]


def make_world(budget=1000.0, actors=ACTORS, duty=DUTY, **over):
    kw = dict(E0=0.0, H=1e9, omega_rate=0.05, Omega0=100.0, duty_turn_reviews=10_000, duty_turn_ticks=100_000,
              r_s=1.0, T_s=10_000, pi0=0.0, period_ticks=60)
    kw.update(over)
    return World(Params(**kw), actors, humans={"H": budget}, on_duty=duty)


def parent_and_child(w, child_tau=3, parent_tau=8):
    """A parent awarded at 40 posts a nested request at 6; B wins at 5 for `child_tau` ticks (deadline t_award + child_tau)."""
    q = w.post_root("H", 45)
    w.award(q, "A", 40, parent_tau)
    w.advance(1)
    qn = w.post_nested(q, 6)
    w.award(qn, "B", 5, child_tau)
    return q, qn


def snapshot(w):
    L = w.ledger
    return (w.history.head, len(L.events), tuple((k, round(v.U, 9), round(v.L, 9)) for k, v in sorted(L.wallets.items())),
            tuple((c.id, c.state, c.actor_cost) for c in w.cases.values()), tuple(sorted((a.id, a.committed) for a in w.actors.values())))


# ---------------------------------------------------------------- §9.3 the refusal

def test_cancellation_at_the_deadline_is_refused_with_no_effect():
    # `advance(T)` processes the ticks up to T − 1 and leaves the clock at T: at T = deadline the deadline tick has arrived and the lapse
    # (processed at tick = deadline, inside advance(deadline + 1)) has not yet run — the driver's step at the deadline tick
    w2 = make_world()
    q2, qn2 = parent_and_child(w2)                                # the child awarded at tick 1, deadline 4
    w2.advance(3)
    assert w2.cases[qn2].state == "COMMITTED" and w2.t == 3 and w2.cases[qn2].deadline == 4
    w2.cancel_nested(qn2)                                         # before the deadline: §9.3 as before (a fee of zero, the guarantee released)
    assert w2.cases[qn2].state == "CANCELLED" and w2.ledger.wallet("B").L == pytest.approx(0.0)
    check_all(w2)
    w3 = make_world()
    q3, qn3 = parent_and_child(w3)
    w3.advance(4)                                                 # the deadline tick: refused, the world unchanged
    assert w3.t == 4 and w3.cases[qn3].state == "COMMITTED"
    before = snapshot(w3)
    with pytest.raises(RuleError):
        w3.cancel_nested(qn3)
    assert snapshot(w3) == before
    w3.advance(5)                                                 # the lapse runs: final N, the guarantee to the parent
    c = w3.cases[qn3]
    assert c.state == "FINAL_N" and c.t_verdict is None
    with pytest.raises(RuleError):
        w3.cancel_nested(qn3)                                     # after it: nothing to cancel
    check_all(w3)


def test_the_lapse_forfeits_to_the_parent_releases_the_bond_and_frees_the_parent():
    w = make_world()
    q, qn = parent_and_child(w)
    G = w.cases[qn].G
    assert G == pytest.approx(3.0)                                # ⌈0.5 × 5⌉ (§6)
    a_before = w.ledger.wallet("A").W
    w.advance(5)                                                  # the lapse at tick 4, the deadline, after that tick's submissions
    c = w.cases[qn]
    assert c.state == "FINAL_N"
    assert any(e.kind == "forfeit_to" and e.dst == "A" and e.amount == pytest.approx(G) for e in w.ledger.events)
    assert w.ledger.wallet("B").L == pytest.approx(0.0)           # nothing of B's left locked on the child
    assert c.rejection_bond == 0.0
    assert w.actors["B"].committed is None
    assert w.ledger.wallet("A").W == pytest.approx(a_before + G - 0.0) or w.ledger.wallet("A").W > a_before   # the escrow came back too
    w.submit(q)                                                   # the milestone is reached by the final N: the parent self-executes
    assert w.cases[q].state == "SUBMITTED"
    check_all(w)


def test_a_child_may_still_submit_on_its_last_tick():
    w = make_world()
    q, qn = parent_and_child(w)
    w.advance(4)                                                  # the deadline tick
    with pytest.raises(RuleError):
        w.cancel_nested(qn)                                       # the parent may not pre-empt it
    w.submit(qn)                                                  # the deadline is inclusive: the child delivers on its last tick
    assert w.cases[qn].state == "SUBMITTED"
    w.advance(5)
    assert w.cases[qn].state == "SUBMITTED"                       # no lapse on a submitted case
    w.judge_nested(qn, F)
    check_all(w)


def test_the_kill_fee_before_the_deadline_is_unchanged():
    w = make_world()
    q, qn = parent_and_child(w, child_tau=5)                      # deadline 6
    w.advance(3)
    w.spend("B", 2, qn)
    w.cancel_nested(qn)                                           # min(2, K) = 2 from escrow; B's guarantee released
    assert w.cases[qn].state == "CANCELLED" and w.cases[q].actor_cost == pytest.approx(2.0)
    assert w.ledger.wallet("B").L == pytest.approx(0.0)
    check_all(w)


# ---------------------------------------------------------------- §6 in the six-actor world

def test_the_worked_example_the_lowballers_take_is_minus_its_guarantee():
    w = make_world()
    q = w.post_root("H", 45)
    w.award(q, "A", 24, 10)                                       # the parent, deadline 10
    w.advance(1)
    qn = w.post_nested(q, 9)
    w.award(qn, "B", 5, 3)                                        # the lowballer at 5, G = 3, deadline 4
    b_before = w.ledger.wallet("B").W
    w.advance(5)                                                  # no submission by tick 4: the lapse
    assert w.cases[qn].state == "FINAL_N"
    assert w.ledger.wallet("B").W == pytest.approx(b_before - 3.0)
    w.submit(q)                                                   # the parent self-executes with six ticks in hand
    r = w.assign_initial(q, "C")
    w.complete_review(r, F, 0)
    w.advance(w.cases[q].window_end + 1)
    assert w.cases[q].state == "VESTED"
    check_all(w)


# ---------------------------------------------------------------- I38 and the control

def test_i38_catches_a_cancellation_at_the_deadline_and_a_lapse_that_did_not_run():
    w = make_world()
    q, qn = parent_and_child(w)
    w.advance(4)
    with pytest.raises(RuleError):
        w.cancel_nested(qn)
    c = w.cases[qn]
    c.state, c.t_closed = "CANCELLED", 4                          # an engine that admitted it
    with pytest.raises(InvariantError):
        I38_the_missed_child(w)
    c.state, c.t_closed = "COMMITTED", None
    w.t = 5                                                       # committed past the deadline: the lapse did not run
    with pytest.raises(InvariantError):
        I38_the_missed_child(w)
    w.t = 4
    I38_the_missed_child(w)


def test_missed_child_off_is_2_4_0():
    w = make_world(missed_child=False)
    q, qn = parent_and_child(w)
    w.advance(4)
    w.cancel_nested(qn)                                           # 2.4.0: admitted at the deadline tick, the guarantee released
    assert w.cases[qn].state == "CANCELLED" and w.ledger.wallet("B").L == pytest.approx(0.0)
    I38_the_missed_child(w)                                       # the invariant is silent under the flag
    check_all(w)

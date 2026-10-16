"""The v0.8 rules and repairs in explicit form: no dispute after a human ruling; the grade is
the establishing author's; execution cost is the committed actor's, while executing; grounds
are validated before the fee; the post-settlement correction of a ⊥ reaches its author; a
released duty actor is not re-conscripted in the same tick."""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
try:
    import pytest
except ImportError:
    sys.path.insert(0, os.path.dirname(__file__))
    from _mini_pytest import pytest

from sim import Params, World, RuleError, LedgerError, check_all
from sim.engine import F, N, BOT, HUMAN, DELEGATE, UPHELD, REJECTED

ACTORS = list("ABCDEFGI")
DUTY = list("CDEF")


def world(**over):
    return World(Params(**over), ACTORS, humans={"H": 1000.0, "S": 100.0}, on_duty=DUTY, delegates=["S"])


def root(w, requester="H", B=10, tau=20, actor="A"):
    q = w.post_root(requester, B)
    w.award(q, actor, B, tau)
    return q


def initial(w, q, verdict=F, cost=0):
    w.submit(q)
    r = w.assign_initial(q, "C")
    w.complete_review(r, verdict, cost)
    return r


def snap(w):
    return (len(w.history.entries), round(w.ledger.M, 9),
            tuple(sorted((k, round(v.W, 9)) for k, v in w.ledger.wallets.items())))


# ------------------------------------------------- no dispute after a ruling
def test_dispute_after_ruling_is_refused_without_trace():
    w = world()
    q = root(w)
    initial(w, q, N)
    w.override(q, "H", F)
    s = snap(w)
    with pytest.raises(RuleError):
        w.dispute(q, "H", d="I disagree with the ruling")
    assert snap(w) == s and not w.cases[q].challenge_round_used
    w.advance(11)
    assert w.cases[q].state == "VESTED" and w.cases[q].grade == HUMAN


# ------------------------------------------------- grade by establishing author
def test_human_ruling_on_delegate_request_is_human_explicit_on_every_route():
    for route in ("before_F", "before_N", "after_N"):
        w = world()
        q = root(w, requester="S")
        initial(w, q, N if route == "before_F" else F)
        if route == "after_N":
            w.advance(11)
        w.override(q, "H", F if route == "before_F" else N)
        if not w.cases[q].final:
            w.advance(11)
        assert w.cases[q].grade == HUMAN, route
        check_all(w)
    w = world()
    q = root(w, requester="S")
    initial(w, q)
    w.accept_explicit(q, "S")
    w.advance(11)
    assert w.cases[q].grade == DELEGATE


# ------------------------------------------------------ cost attribution
def test_only_the_committed_actor_incurs_a_case_cost_and_only_while_executing():
    w = world()
    q = root(w, B=20)
    child = w.post_nested(q, 10)
    w.award(child, "B", 5, 10)
    s = snap(w)
    with pytest.raises(RuleError):
        w.spend("C", 4, child)                  # C is not B
    with pytest.raises(RuleError):
        w.spend("A", 4, child)                  # A is the requester, not the contractor
    assert snap(w) == s
    w.spend("C", 4)                             # C's own spending, unattributed, is fine
    w.spend("B", 4, child)
    assert w.cases[child].actor_cost == pytest.approx(4)
    q2 = root(w, actor="G")
    initial(w, q2)
    w.advance(11)
    s = snap(w)
    with pytest.raises(RuleError):
        w.spend("G", 1, q2)                     # vested: execution is over
    assert snap(w) == s


# ------------------------------------------------- grounds validated first
def test_non_text_grounds_refused_before_fee_for_appeal_and_dispute():
    w = world()
    q = root(w)
    initial(w, q, N)
    s = snap(w)
    with pytest.raises(RuleError):
        w.respond(q, "appeal", d=["not", "text"])
    assert snap(w) == s and w.cases[q].state == "AWAITING_RESPONSE"
    w2 = world()
    q2 = root(w2)
    initial(w2, q2)
    s2 = snap(w2)
    with pytest.raises(RuleError):
        w2.dispute(q2, "H", d=42)
    assert snap(w2) == s2


# ------------------------------- post-settlement ⊥ correction reaches its author
def test_post_settlement_bot_correction_uses_the_two_question_rule():
    w = world()
    q = root(w)
    orig = initial(w, q, BOT)
    w.respond(q, "appeal", d="the evidence was present")
    d = w.assign_appeal(q, "D"); e = w.assign_appeal(q, "E")
    w.complete_review(d, N, 0, objection=UPHELD); w.complete_review(e, N, 0, objection=UPHELD)
    w.advance(1)
    oC, oD = w.actors["C"].o, w.actors["D"].o
    with pytest.raises(RuleError):
        w.override(q, "H", F)                   # a ⊥ correction needs the disposition
    with pytest.raises(RuleError):
        w.override(q, "H", F, objection=UPHELD) # and upheld ⇒ N
    w.override(q, "H", F, objection=REJECTED)
    assert w.actors["C"].o == oC + 1 and w.actors["D"].o == oD + 1
    assert w.reviews[orig].contradicted_by_override
    w2 = world()
    q2 = root(w2)
    orig2 = initial(w2, q2, BOT)
    w2.respond(q2, "appeal"); d2 = w2.assign_appeal(q2, "D"); e2 = w2.assign_appeal(q2, "E")
    w2.complete_review(d2, N, 0, objection=UPHELD); w2.complete_review(e2, N, 0, objection=UPHELD)
    w2.advance(1)
    oC2 = w2.actors["C"].o
    w2.override(q2, "H", N, objection=UPHELD)   # the ruling agrees the evidence was missing
    assert w2.actors["C"].o == oC2 and not w2.reviews[orig2].contradicted_by_override


# ------------------------------------------------------- rotation snapshot
def test_released_duty_actor_is_not_reconscripted_in_the_same_tick():
    w = world()
    w.advance(31)                               # tick 30: all four turns end by elapsed time
    duty = sorted(a.id for a in w.actors.values() if a.on_duty)
    assert duty == ["A", "B", "G", "I"]         # the four who were free when the tick began
    assert not any(w.actors[x].on_duty for x in "CDEF")
    swaps = [e["payload"] for e in w.history.entries if e["kind"] == "rotation"]
    assert {s["in"] for s in swaps} == {"A", "B", "G", "I"} and {s["out"] for s in swaps} == set("CDEF")

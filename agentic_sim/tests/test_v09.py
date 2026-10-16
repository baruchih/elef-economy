"""The v0.9 rules and repairs in explicit form: delegates hold no ruling authority; a
post-settlement correction uses each appeal reviewer's complete two-question answer; and a
correction between a case's finality and its reviews' payout reaches those reviews as a
ruling. The v0.9 audit-reopening rule was withdrawn in v0.10; the fulfillment contract is
now stated by the view, and the tests below assert that form."""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
try:
    import pytest
except ImportError:
    sys.path.insert(0, os.path.dirname(__file__))
    from _mini_pytest import pytest

from sim import Params, World, RuleError, check_all
from sim.engine import F, N, P, BOT, UPHELD, REJECTED, HUMAN, DELEGATE

ACTORS = list("ABCDEFGI")
DUTY = list("CDEF")


def world(**over):
    return World(Params(**over), ACTORS, humans={"H": 1000.0, "S": 100.0}, on_duty=DUTY, delegates=["S"])


def root(w, requester="H", B=10, tau=20, actor="A"):
    q = w.post_root(requester, B)
    w.award(q, actor, B, tau)
    return q


def initial(w, q, verdict=F, cost=0, reviewer="C"):
    w.submit(q)
    r = w.assign_initial(q, reviewer)
    w.complete_review(r, verdict, cost)
    return r


# ------------------------------------------------------------ D: authority
def test_delegate_may_request_accept_and_dispute_but_not_rule():
    w = world()
    q = root(w, requester="S")
    initial(w, q)
    with pytest.raises(RuleError):
        w.override(q, "S", N)
    w.dispute(q, "S", d="not what I asked for")          # the delegate's own path
    assert w.cases[q].challenge["challenger"] == "S"
    w2 = world()
    q2 = root(w2, requester="S")
    initial(w2, q2)
    w2.accept_explicit(q2, "S")
    w2.advance(11)
    assert w2.cases[q2].grade == DELEGATE
    assert "S" not in w2.humans and "S" in w2.requesters


# ------------------------------------- A: complete two-question correction
def test_correction_of_the_objection_alone_contradicts_appeal_reviewers():
    w = world()
    q = root(w)
    orig = initial(w, q, BOT)
    w.respond(q, "appeal", d="the evidence was there")
    d = w.assign_appeal(q, "D"); e = w.assign_appeal(q, "E")
    w.complete_review(d, N, 0, objection=UPHELD); w.complete_review(e, N, 0, objection=UPHELD)
    w.advance(1)
    before = {a: w.actors[a].o for a in "CDE"}
    w.override(q, "H", N, objection=REJECTED)           # evidence was present; still not fulfilled
    assert w.actors["C"].o == before["C"] + 1            # the ⊥ was wrong
    assert w.actors["D"].o == before["D"] + 1 and w.actors["E"].o == before["E"] + 1
    assert w.reviews[d].contradicted_by_override and w.reviews[e].contradicted_by_override
    assert w.cases[q].challenge["objection"] == REJECTED


# ------------------------------------------- B: the payout boundary
def test_ruling_between_finality_and_payout_overturns_the_review():
    w = world(E0=0.0, omega_rate=0.0)
    q = root(w)
    r = initial(w, q, N)
    w.respond(q, "accept")                                # final N; C is done, not vested
    assert w.cases[q].state == "FINAL_N" and w.reviews[r].status == "done"
    bond_before = w.ledger.wallet("C").L
    w.override(q, "H", F)
    assert w.reviews[r].status == "overturned"            # a ruling before payout is a ruling
    assert w.ledger.wallet("C").L == pytest.approx(bond_before - 5)   # bond burned, not released
    w.advance(1)
    assert w.reviews[r].fee == 0 and w.actors["C"].o == 1
    # H: −10 price −10 deposit, +10 price back at final N, +5 A's guarantee, +10 unused deposit
    # once the only review is overturned and no reviewer is entitled to it
    assert w.W("H") == pytest.approx(1000 - 10 - 10 + 10 + 5 + 10)


# ----------------------------------- C (as withdrawn in v0.10): the contract is in the view
def test_identical_views_identical_admissibility_for_all_four_verdicts():
    """An initial review and an audit give identical views; the view states whether P/⊥ are
    available, and the engine admits exactly what the view says — for both roles alike."""
    for verdict in (F, N, P, BOT):
        wi = world()
        qi = root(wi)
        wi.submit(qi)
        ri = wi.assign_initial(qi, "C")
        wa = world()
        qa = root(wa)
        initial(wa, qa, F, reviewer="D")
        ra = wa.assign_audit(qa, "C")
        vi, va = wi.observe("C", ri), wa.observe("C", ra)
        assert vi.question == va.question == "fulfillment"
        assert vi.responses_available is True and va.responses_available is False
        wi.complete_review(ri, verdict, 0)                 # the first review of a submission: all four
        if va.responses_available or verdict in (F, N):
            wa.complete_review(ra, verdict, 0)
        else:
            with pytest.raises(RuleError):
                wa.complete_review(ra, verdict, 0)         # the view said no; the engine says no
        check_all(wi); check_all(wa)


def test_a_resumed_initial_review_states_that_responses_are_closed():
    w = world()
    q = root(w)
    r = initial(w, q, P)
    assert w.observe("C", r).responses_available is False  # once answered, the position is spent
    w.respond(q, "revise")
    w.resubmit(q)
    assert w.observe("C", r).resumed and not w.observe("C", r).responses_available
    with pytest.raises(RuleError):
        w.complete_review(r, P, 0)

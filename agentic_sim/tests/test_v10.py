"""v0.10: the audit-reopening rule of v0.9 is withdrawn. An audit reviews a finished verdict
after the actor's window has closed, so it is answered F or N; P and ⊥ are responses to a
submission and are available on its first review only. The view states which answers a
review may give, so identical views admit identical answers and no refusal reveals a role.
These tests assert the withdrawal directly and that each path the eighth review found is
now closed rather than repaired."""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
try:
    import pytest
except ImportError:
    sys.path.insert(0, os.path.dirname(__file__))
    from _mini_pytest import pytest

from sim import Params, World, RuleError, check_all
from sim.engine import F, N, P, BOT

ACTORS = list("ABCDEFGI")
DUTY = list("CDEF")


def world():
    return World(Params(), ACTORS, humans={"H": 1000.0, "S": 100.0}, on_duty=DUTY, delegates=["S"])


def root(w, actor="A", tau=20):
    q = w.post_root("H", 10)
    w.award(q, actor, 10, tau)
    return q


def initial(w, q, verdict=F, reviewer="C"):
    w.submit(q)
    r = w.assign_initial(q, reviewer)
    w.complete_review(r, verdict, 0)
    return r


def snapshot(w):
    return (len(w.history.entries), round(w.ledger.M, 9),
            tuple(sorted((k, round(v.W, 9)) for k, v in w.ledger.wallets.items())),
            tuple((c.id, c.state, c.verdict, c.t_verdict) for c in w.cases.values()))


def test_an_audit_is_answered_F_or_N_and_the_view_says_so():
    for verdict in (P, BOT):
        w = world()
        q = root(w)
        initial(w, q)
        w.advance(1)
        a = w.assign_audit(q, "D")
        assert w.observe("D", a).responses_available is False
        w.advance(2)
        s = snapshot(w)
        with pytest.raises(RuleError):
            w.complete_review(a, verdict, 0)              # refused whole: no reopening, nothing moved
        assert snapshot(w) == s and w.cases[q].t_verdict == 0 and w.cases[q].state == "PENDING"
        w.complete_review(a, F, 0)                        # the audit answers the question it was asked
        check_all(w)


def test_the_first_review_of_a_submission_may_answer_all_four_and_the_view_says_so():
    for verdict in (F, N, P, BOT):
        w = world()
        q = root(w)
        w.submit(q)
        r = w.assign_initial(q, "C")
        assert w.observe("C", r).responses_available is True
        w.complete_review(r, verdict, 0)
        check_all(w)


def test_no_review_may_answer_P_or_bot_after_a_resubmission_whoever_holds_it():
    w = world()
    q = root(w)
    r = initial(w, q, BOT)
    w.respond(q, "supply_evidence")
    w.resubmit(q)
    w.advance(6)                                          # C times out on the resumed review
    d = w.assign_initial(q, "D")
    assert w.observe("D", d).responses_available is False
    with pytest.raises(RuleError):
        w.complete_review(d, BOT, 0)
    w.complete_review(d, N, 0)
    check_all(w)


def test_appeals_and_disputes_are_answered_F_or_N():
    w = world()
    q = root(w)
    initial(w, q)
    w.dispute(q, "H", d="not as requested")
    e = w.assign_appeal(q, "E")
    assert w.observe("E", e).responses_available is False
    with pytest.raises(RuleError):
        w.complete_review(e, P, 0)


def test_the_paths_the_eighth_review_found_are_closed_not_repaired():
    """Each of the five findings began with an auditor's P/⊥ being admitted. None can begin."""
    # A. elapsed-time audit; C. appeal of an auditor's ⊥; D. busy actor; E. merged dispute
    w = world()
    q = root(w)
    initial(w, q)
    other = root(w, actor="A", tau=40)                    # A has taken new work while q is pending
    a = w.assign_audit(q, "D")
    w.dispute(q, "H", d="please examine")                 # the audit is merged into a dispute
    with pytest.raises(RuleError):
        w.complete_review(a, BOT, 0)
    assert w.actors["A"].committed == other and w.cases[q].challenge["kind"] == "dispute"
    w.complete_review(a, F, 0)
    e = w.assign_appeal(q, "E")
    w.complete_review(e, F, 0)
    check_all(w)
    # B. a nested child whose parent has submitted; the child's milestone is never erased
    w2 = world()
    parent = root(w2, tau=40)
    child = w2.post_nested(parent, 5)
    w2.award(child, "B", 5, 20); w2.submit(child); w2.judge_nested(child, F)
    w2.submit(parent)
    w2.advance(1)
    c = w2.assign_audit(child, "C")
    with pytest.raises(RuleError):
        w2.complete_review(c, BOT, 0)
    assert w2.cases[child].t_verdict == 0
    w2.complete_review(c, F, 0)
    check_all(w2)

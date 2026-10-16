"""The v0.7 rules and repairs in explicit form: no audit after a human ruling; a terminal
child is a milestone; the resubmission stage lives on the case; a refused dispute leaves the
vacated-audit obligation; acceptance by ruling ends the rejection obligation; the appeal's
grounds are committed; working copies are complete and ordered."""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
try:
    import pytest
except ImportError:
    sys.path.insert(0, os.path.dirname(__file__))
    from _mini_pytest import pytest

from sim import Params, World, RuleError, LedgerError, InvariantError, check_all
from sim.engine import F, N, P, BOT, HUMAN, PROCEDURAL

ACTORS = list("ABCDEFGI")
DUTY = list("CDEF")


def world(budget=1000, **over):
    kw = dict(E0=0.0, omega_rate=0.0)
    kw.update(over)
    return World(Params(**kw), ACTORS, humans={"H": budget}, on_duty=DUTY)


def root(w, B=10, tau=20, actor="A"):
    q = w.post_root("H", B)
    w.award(q, actor, B, tau)
    return q


def initial(w, q, verdict=F, reviewer="C", cost=0):
    w.submit(q)
    r = w.assign_initial(q, reviewer)
    w.complete_review(r, verdict, cost)
    return r


# ------------------------------------------------ no audit after a human ruling
def test_audit_after_override_is_refused_and_vesting_proceeds():
    w = world()
    q = root(w)
    initial(w, q, N)
    w.override(q, "H", F)
    with pytest.raises(RuleError):
        w.assign_audit(q, "D")
    w.advance(11)
    c = w.cases[q]
    assert c.state == "VESTED" and c.outcome == F and c.grade == HUMAN


def test_audit_agreement_is_judged_against_the_live_assessment():
    """An audit assigned before a ruling but completed after it compares to the ruling."""
    w = world()
    q = root(w)
    initial(w, q, F)
    a = w.assign_audit(q, "D")
    w.override(q, "H", F)                    # the open audit is voided by the ruling
    assert w.reviews[a].status == "withdrawn" and w.ledger.wallet("D").L == 0
    w.advance(11)
    assert w.cases[q].state == "VESTED"


# ------------------------------------------------------- terminal child milestone
def test_child_that_missed_delivery_does_not_block_the_parent():
    w = world()
    parent = root(w, B=20)
    child = w.post_nested(parent, 5)
    w.award(child, "B", 5, 1)
    w.advance(2)                             # B misses: final N, no verdict; B's guarantee to A
    assert w.cases[child].state == "FINAL_N" and w.cases[child].t_verdict is None
    w.submit(parent)                         # A carries the failure as its own risk
    r = w.assign_initial(parent, "C")
    w.complete_review(r, F, 0)
    w.advance(13)
    assert w.cases[parent].state == "VESTED"


def test_unjudged_submitted_child_still_blocks_the_parent():
    w = world()
    parent = root(w, B=20)
    child = w.post_nested(parent, 5)
    w.award(child, "B", 5, 5)
    w.submit(child)
    with pytest.raises(RuleError):
        w.submit(parent)


# --------------------------------------------- resubmission stage on the case
def test_replacement_reviewer_inherits_the_resubmitted_stage():
    w = world()
    q = root(w)
    r = initial(w, q, P)
    w.respond(q, "revise")
    w.resubmit(q)
    w.advance(6)                             # C times out on the resumed review
    assert w.reviews[r].status == "withdrawn"
    d = w.assign_initial(q, "D")
    assert w.observe("D", d).resumed
    with pytest.raises(RuleError):
        w.complete_review(d, P, 0)
    with pytest.raises(RuleError):
        w.complete_review(d, BOT, 0)
    w.complete_review(d, F, 0)
    assert w.cases[q].state == "PENDING"


# ------------------------------------- refused dispute keeps the obligation
def test_unfunded_dispute_is_refused_whole_under_full_defaults():
    w = World(Params(), ACTORS, humans={"H": 20.5}, on_duty=DUTY)
    q = w.post_root("H", 10)
    w.award(q, "A", 10, 20)                  # 10 + 10 deposit + 0.5 ω: H has 0
    initial(w, q)
    w.assign_audit(q, "D")
    w.advance(6)
    c = w.cases[q]
    assert c.audit_vacated and c.open_items == 1
    with pytest.raises(LedgerError):
        w.dispute(q, "H")
    assert c.audit_vacated and c.open_items == 1 and c.challenge is None and not c.challenge_round_used
    w.advance(12)
    assert c.state == "PENDING"              # still held
    w.waive_audit(q)
    w.advance(13)
    assert c.state == "VESTED"


# ------------------------------- acceptance by ruling ends the rejection obligation
def test_human_accepts_submitted_child_before_parent_judges():
    w = world()
    parent = root(w, B=20)
    child = w.post_nested(parent, 5)
    w.award(child, "B", 5, 10)
    w.submit(child)
    w.override(child, "H", F)
    assert w.cases[child].rejection_bond == 0 and w.ledger.lock_record("A", f"rej:{child}") == 0
    assert w.actors["A"].o == 0              # A had not judged: nothing to overturn
    w.advance(11)
    assert w.cases[child].state == "VESTED" and w.cases[child].grade == PROCEDURAL
    w.submit(parent)                         # the child's milestone is its (human) verdict


# ------------------------------------------- the appeal's grounds are committed
def test_appeal_grounds_change_the_history_head():
    heads = []
    for d in ("the log is attached", "no log was ever requested"):
        w = world()
        q = root(w)
        initial(w, q, N)
        w.respond(q, "appeal", d=d)
        heads.append(w.history.head)
        assert any(e["kind"] == "challenge" and e["payload"]["d"] == d for e in w.history.entries)
    assert heads[0] != heads[1]


# --------------------------------------- working copies: complete and ordered
def test_omitted_or_reordered_copy_entries_are_detected():
    w = world()
    q = root(w)
    initial(w, q)
    check_all(w)
    saved = list(w.ledger.events)
    w.ledger.events[:] = [e for e in w.ledger.events if e.kind != "transfer"]
    with pytest.raises(InvariantError):
        check_all(w)
    w.ledger.events[:] = saved
    check_all(w)
    w.ledger.events[0], w.ledger.events[1] = w.ledger.events[1], w.ledger.events[0]
    with pytest.raises(InvariantError):
        check_all(w)
    w.ledger.events[0], w.ledger.events[1] = w.ledger.events[1], w.ledger.events[0]
    check_all(w)
    w.cases[q].log.pop()
    with pytest.raises(InvariantError):
        check_all(w)

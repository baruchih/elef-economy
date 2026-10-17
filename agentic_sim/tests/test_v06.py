"""The v0.6 repairs in explicit form: boundary-wide atomicity, the unified override path,
the vacated-audit obligation and its waiver, cost debts without survivors, claims that keep
their review, the appeal view, and the authoritative history."""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
try:
    import pytest
except ImportError:
    sys.path.insert(0, os.path.dirname(__file__))
    from _mini_pytest import pytest

from sim import Params, World, RuleError, LedgerError, InvariantError, check_all
from sim.engine import F, N, P, BOT, UPHELD, REJECTED, HUMAN, PROCEDURAL

ACTORS = ["A", "B", "C", "D", "E", "F", "G"]
DUTY = ["C", "D", "E", "F"]


def world(**over):
    kw = dict(E0=0.0, omega_rate=0.0)
    kw.update(over)
    return World(Params(**kw), ACTORS, humans={"H": 1000.0}, on_duty=DUTY)


def root(w, actor="A", B=10, tau=100):
    q = w.post_root("H", B)
    w.award(q, actor, B, tau)
    return q


def initial(w, q, reviewer="C", verdict=F, cost=0):
    w.submit(q)
    r = w.assign_initial(q, reviewer)
    w.complete_review(r, verdict, cost)
    return r


def snapshot(w):
    return (round(w.ledger.M, 9), round(w.ledger.Res, 9), len(w.ledger.events), len(w.history.entries),
            tuple(sorted((k, round(v.W, 9)) for k, v in w.ledger.wallets.items())))


# ------------------------------------------------------------------ atomicity
def test_refused_actions_leave_no_trace():
    w = world()
    q = w.post_root("H", 10)
    snap = snapshot(w)
    for call in (lambda: w.spend("A", 3, "nope"),
                 lambda: w.override(q, "H", F),
                 lambda: w.award(q, "C", 10, 5),                  # on duty
                 lambda: w.award(q, "A", 10, -1)):
        with pytest.raises((RuleError, LedgerError)):
            call()
        assert snapshot(w) == snap
        assert w.cases[q].assessments == []
    w.award(q, "A", 10, 10)
    initial(w, q, verdict=P)
    snap = snapshot(w)
    with pytest.raises(RuleError):
        w.respond(q, "appeal")                                  # a P is not appealable
    assert snapshot(w) == snap and not w.cases[q].challenge_round_used


# ------------------------------------------------------- vacated audit obligation
def test_vacated_audit_holds_the_case_until_refilled_or_waived():
    w = world()
    q = root(w)
    initial(w, q)
    w.advance(9)
    a = w.assign_audit(q, "D")
    w.advance(15)                                               # D times out at 14, after the window
    c = w.cases[q]
    assert w.reviews[a].status == "withdrawn" and c.state == "PENDING" and c.audit_vacated
    w2 = world()
    q2 = root(w2)
    initial(w2, q2)
    w2.advance(9)
    w2.assign_audit(q2, "D")
    w2.advance(15)
    w2.waive_audit(q2)                                          # the orchestrator abandons the audit instead
    w2.advance(16)
    assert w2.cases[q2].state == "VESTED"
    with pytest.raises(RuleError):
        w2.waive_audit(q2)


def test_dispute_folds_in_a_vacated_audit():
    w = world()
    q = root(w)
    initial(w, q)
    w.advance(3)
    w.assign_audit(q, "D")
    w.advance(9)                                                # D times out at 8: obligation stands
    w.dispute(q, "H")                                           # the dispute takes over the obligation
    assert w.cases[q].open_items == 1 and not w.cases[q].audit_vacated
    rE = w.assign_appeal(q, "E"); rF = w.assign_appeal(q, "F")
    w.complete_review(rE, F, 0); w.complete_review(rF, F, 0)
    w.advance(11)                                               # window ends at 10
    assert w.cases[q].state == "VESTED"


# ----------------------------------------------------------- unified override
def test_override_with_open_challenge_voids_open_reviews_and_rules_once():
    w = world()
    q = root(w)
    r = initial(w, q, verdict=BOT)
    w.respond(q, "appeal", d="the trace is attached")
    rd = w.assign_appeal(q, "D")
    w.complete_review(rd, N, 0, objection=UPHELD)
    re = w.assign_appeal(q, "E")                                # still open
    with pytest.raises(RuleError):
        w.override(q, "H", F, objection=UPHELD)                 # upheld entails N
    w.override(q, "H", F, objection=REJECTED)                   # the human: evidence was present, and it fulfils
    c = w.cases[q]
    assert c.challenge["resolved"] and c.challenge["by"].startswith("human")
    assert w.reviews[re].status == "withdrawn" and w.ledger.wallet("E").L == 0 and w.actors["E"].o == 0
    assert w.reviews[rd].status == "overturned"                 # D's "upheld" contradicts the ruling
    assert w.reviews[r].status == "overturned" and c.court_fee_reimbursed == pytest.approx(2)
    assert c.state == "PENDING" and c.outcome == F


def test_override_contradicting_a_nested_rejection_forfeits_the_rejection_bond():
    w = world()
    qp = root(w, B=40)
    qn = w.post_nested(qp, 5); w.award(qn, "B", 5, 10)
    w.submit(qn); w.judge_nested(qn, N)
    assert w.ledger.lock_record("A", f"rej:{qn}") == pytest.approx(5)
    w.override(qn, "H", F)
    assert w.ledger.lock_record("A", f"rej:{qn}") == 0 and w.cases[qn].rejection_bond == 0
    assert w.actors["A"].o == 1
    w.advance(11)
    assert w.cases[qn].state == "VESTED" and w.cases[qn].grade == PROCEDURAL


def test_override_confirming_a_nested_rejection_releases_the_bond():
    w = world()
    qp = root(w, B=40)
    qn = w.post_nested(qp, 5); w.award(qn, "B", 5, 10)
    w.submit(qn); w.judge_nested(qn, N)
    w.override(qn, "H", N)
    assert w.ledger.lock_record("A", f"rej:{qn}") == 0 and w.actors["A"].o == 0
    assert w.cases[qn].state == "FINAL_N"


# -------------------------------------------------- debts without survivors
def test_cost_debts_are_paid_from_the_deposit_before_it_is_returned():
    w = world(Omega0=0.0)
    q = root(w, B=40)                                           # deposit 10
    r = initial(w, q, cost=12)                                  # cap 5: reimbursed 5 from the deposit
    assert w.ledger.pool(q).deposit == pytest.approx(5)
    before_H = w.W("H")
    w.override(q, "H", N)                                       # C overturned; no survivor
    assert w.W("H") - before_H == pytest.approx(40 + 20 + 5 + 5)    # escrow, guarantee, unused allowance and fee pot
    assert w.reviews[r].reimbursed == pytest.approx(5) and w.omega_claims == []


# ------------------------------------------------------- claims keep identity
def test_claims_carry_their_review_and_print_as_pairs():
    w = world(Omega0=0.0, omega_rate=0.05)
    q = root(w, B=10)
    initial(w, q, cost=5)
    w.dispute(q, "H")
    re = w.assign_appeal(q, "E"); rf = w.assign_appeal(q, "F")
    w.complete_review(re, F, 5); w.complete_review(rf, F, 5)
    w.advance(11)
    assert w.omega_claims == [("F", 2.5)]
    assert w.omega_claims[0].review == rf and w.omega_claims[0].reviewer == "F"


# ------------------------------------------------------------- appeal view
def test_appeal_and_dispute_views_state_their_question():
    w = world()
    q = root(w)
    initial(w, q, verdict=BOT)
    w.respond(q, "appeal", d="see the attached log")
    rd = w.assign_appeal(q, "D")
    v = w.observe("D", rd)
    assert v.question == "appeal" and v.appealed_assessment == BOT and v.objection_text == "see the attached log"
    w2 = world()
    q2 = root(w2)
    initial(w2, q2)
    w2.dispute(q2, "H", d="it does not run")
    re = w2.assign_appeal(q2, "E")
    v2 = w2.observe("E", re)
    assert v2.question == "dispute" and v2.appealed_assessment == F
    w3 = world()                                                # an audit's view is a plain fulfillment question
    q3 = root(w3)
    initial(w3, q3)
    au = w3.assign_audit(q3, "D")
    assert w3.observe("D", au).question == "fulfillment"


# ------------------------------------------------- the history is the record
def test_every_participant_action_is_committed_and_copies_are_checked():
    w = world()
    q = root(w)
    n = len(w.history.entries)
    initial(w, q)
    w.accept_explicit(q, "H")
    w.volunteer("C")
    assert len(w.history.entries) > n
    assert any(e["kind"] == "case" and "accepts" in e["payload"]["msg"] for e in w.history.entries)
    check_all(w)
    w.ledger.events[0].amount += 1
    with pytest.raises(InvariantError):
        check_all(w)

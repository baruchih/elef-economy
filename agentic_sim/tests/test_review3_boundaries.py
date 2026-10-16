"""Independent v0.6 conformance checks (not strategy or incentive experiments).

These use the uploaded implementation unmodified. Zero emission and zero service
fee make accounting differences legible unless a test says otherwise. The
ordinary reserve, challenge window, review deadlines, cap and bonds remain the
supplied defaults. Tests do not require a production evaluator or external head.

Tests that exercise a not-fully-specified follow-on action accept an atomic
refusal OR a consistent supported transition. They do not choose a new policy.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'agentic_sim'))

import pytest
from sim import Params, World, RuleError, LedgerError, InvariantError, check_all
from sim.engine import F, N, P, BOT

ACTORS = list('ABCDEFGI')
DUTY = list('CDEF')


def make_world(budget=1000, **overrides):
    p = dict(E0=0.0, omega_rate=0.0)
    p.update(overrides)
    return World(Params(**p), ACTORS, humans={'H': budget}, on_duty=DUTY)


def root(w, B=10, tau=20, actor='A'):
    q = w.post_root('H', B)
    w.award(q, actor, B, tau)
    return q


def initial(w, q, verdict=F, reviewer='C', cost=0):
    w.submit(q)
    r = w.assign_initial(q, reviewer)
    w.complete_review(r, verdict, cost)
    return r


def test_r5_a_unfunded_dispute_keeps_vacated_audit_obligation():
    """A refused filing must not silently waive the audit that it hoped to replace."""
    w = make_world(budget=20)
    q = root(w)  # 10 delivery + 10 verification deposit, H has zero left
    initial(w, q)
    w.assign_audit(q, 'D')
    w.advance(6)  # audit timed out at 5, original window ends at 10
    c = w.cases[q]
    assert c.audit_vacated and c.open_items == 1
    check_all(w)
    with pytest.raises(LedgerError):
        w.dispute(q, 'H', d='I cannot fund this filing')
    assert c.audit_vacated and c.open_items == 1, (
        'The refused filing cleared the uncompleted audit obligation')
    assert c.challenge is None and not c.challenge_round_used
    w.advance(11)
    assert not c.final


def test_r5_b_direct_nested_acceptance_override_releases_rejection_bond():
    """The human judges an actual submitted child before its requester-actor does."""
    w = make_world()
    parent = root(w, B=20)
    child = w.post_nested(parent, 5)
    w.award(child, 'B', 5, 10)
    w.submit(child)
    w.override(child, 'H', F)
    assert w.cases[child].rejection_bond == pytest.approx(0), (
        'Acceptance by override leaves the requester rejection bond locked')
    assert w.ledger.lock_record('A', f'rej:{child}') == pytest.approx(0)
    w.advance(1)
    check_all(w)


@pytest.mark.parametrize('audit_verdict', [N, F])
def test_r5_c_follow_on_audit_uses_live_ruling_or_is_refused(audit_verdict):
    """Do not compare a permitted follow-on audit to an already-overturned verdict.

Refusing the follow-on audit is an acceptable policy repair. If admitted, the
review must not be paid as supporting F while saying N, or crash while agreeing
with F because the original N reviewer is no longer available to overturn.
"""
    w = make_world()
    q = root(w)
    initial(w, q, N)
    w.override(q, 'H', F)
    c = w.cases[q]
    assert c.outcome == F and w.reviews[c.reviews[0]].status == 'overturned'
    try:
        audit = w.assign_audit(q, 'D')
    except RuleError:
        check_all(w)
        return
    w.complete_review(audit, audit_verdict, 0)
    if audit_verdict == N:
        # A contrary review could open a challenge or be overruled by the human
        # ruling; it cannot simply vest as if it supported that ruling.
        if c.challenge and not c.challenge['resolved']:
            return
        w.advance(11)
        assert not (c.outcome == F and w.reviews[audit].status == 'vested'), (
            'The audit said N but was rewarded as surviving the human F ruling')
    else:
        # Some implementations may use further review to settle this. Exercise
        # that admitted route rather than assuming a specific policy.
        if c.challenge and not c.challenge['resolved']:
            other = w.assign_appeal(q, 'E')
            w.complete_review(other, F, 0)
        w.advance(11)
        assert c.state == 'VESTED' and c.outcome == F
        check_all(w)


@pytest.mark.parametrize('first_verdict,response', [(P, 'revise'), (BOT, 'supply_evidence')])
def test_r5_d_replacement_retains_resubmitted_result_constraints(first_verdict, response):
    """Replacing the reviewer does not make the already-resubmitted result new."""
    w = make_world()
    q = root(w)
    r = initial(w, q, first_verdict)
    w.respond(q, response)
    w.resubmit(q)
    w.advance(6)  # the resumed reviewer times out at 5
    assert w.reviews[r].status == 'withdrawn'
    replacement = w.assign_initial(q, 'D')
    with pytest.raises(RuleError):
        w.complete_review(replacement, first_verdict, 0)


def test_r5_e_parent_submission_after_child_timeout_is_consistent_or_refused():
    """Final-N child without a submitted result needs an explicit milestone rule.

The test does not choose that rule: refusal must be atomic, while acceptance
must leave the supplied invariant suite satisfied.
"""
    w = make_world()
    parent = root(w, B=20)
    child = w.post_nested(parent, 5)
    w.award(child, 'B', 5, 1)
    w.advance(2)
    assert w.cases[child].state == 'FINAL_N'
    check_all(w)
    try:
        w.submit(parent)
    except RuleError:
        assert w.cases[parent].state == 'COMMITTED'
    check_all(w)


def test_r5_f_challenger_explanation_is_bound_to_history():
    """Two materially different admitted appeal explanations need different commitments."""
    worlds = []
    for explanation in ('The required log is attached.', 'The log was never requested.'):
        w = make_world()
        q = root(w)
        initial(w, q, N)
        w.respond(q, 'appeal', d=explanation)
        reviewer = w.assign_appeal(q, 'D')
        view = w.observe('D', reviewer)
        assert view.objection_text == explanation
        check_all(w)
        worlds.append(w)
    assert worlds[0].history.head != worlds[1].history.head, (
        'Different admitted appeal grounds produce exactly the same history head')


@pytest.mark.parametrize('copy_kind', ['case_log', 'ledger_transfers'])
def test_r5_g_working_copy_omissions_are_detected(copy_kind):
    """Optional record-hardening regression, not a claim that canonical history is lost.

I16 checks remaining copy entries but currently cannot establish complete copies.
The canonical history and its head are deliberately left unchanged here.
"""
    w = make_world()
    q = root(w)
    initial(w, q)
    original_head = w.history.head
    if copy_kind == 'case_log':
        w.cases[q].log.clear()
    else:
        w.ledger.events[:] = [e for e in w.ledger.events if e.kind != 'transfer']
    assert w.history.head == original_head and w.history.verify()
    with pytest.raises(InvariantError):
        check_all(w)


# Positive controls: neighboring ordinary/specified paths, included for scope.
def test_r5_control_funded_dispute_replaces_a_vacated_audit():
    w = make_world()
    q = root(w)
    initial(w, q)
    w.assign_audit(q, 'D')
    w.advance(6)
    w.dispute(q, 'H', d='Please reassess')
    c = w.cases[q]
    assert not c.audit_vacated and c.open_items == 1
    for who in ('E', 'F'):
        r = w.assign_appeal(q, who)
        w.complete_review(r, F, 0)
    w.advance(11)
    assert c.state == 'VESTED'
    check_all(w)


def test_r5_control_judged_nested_rejection_override_releases_bond():
    w = make_world()
    parent = root(w, B=20)
    child = w.post_nested(parent, 5)
    w.award(child, 'B', 5, 10)
    w.submit(child)
    w.judge_nested(child, N)
    w.override(child, 'H', F)
    assert w.cases[child].rejection_bond == 0
    w.advance(11)
    check_all(w)


def test_r5_control_new_review_on_original_submission_can_report_partial():
    w = make_world()
    q = root(w)
    r = initial(w, q, P)
    assert w.reviews[r].verdict == P
    check_all(w)


def test_r5_control_editing_existing_committed_copy_is_detected():
    w = make_world()
    q = root(w)
    initial(w, q)
    w.ledger.events[0].note = 'changed note'
    with pytest.raises(InvariantError):
        check_all(w)

"""Independent v0.9 conformance checks: auditor reopening versus existing case rules.

All Params are defaults; only identities, budgets and the initial duty roster are set.
No source changes, state edits, or replacement implementations. The cases use public
World actions; assertions inspect the resulting state and run the supplied invariants.
These are targeted interaction checks, not strategies or incentive measurements.

Run: python -m pytest independent_tests/test_v09_audit_reopening.py -q --tb=short
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
try:
    import pytest
except ImportError:
    sys.path.insert(0, str(ROOT / 'tests'))
    from _mini_pytest import pytest

from sim import World, Params, RuleError, LedgerError, check_all
from sim.engine import F, N, P, BOT, UPHELD, REJECTED


def world():
    return World(Params(), list('ABCDEFGI'), humans={'H': 1000., 'S': 100.},
                 on_duty=list('CDEF'), delegates=['S'])


def root(w, actor='A', tau=20):
    q = w.post_root('H', 10)
    w.award(q, actor, 10, tau)
    return q


def initial(w, q, verdict=F, reviewer='C'):
    w.submit(q)
    r = w.assign_initial(q, reviewer)
    w.complete_review(r, verdict, 0)
    check_all(w)
    return r


def reopened(w, q, verdict=BOT, reviewer='D'):
    audit = w.assign_audit(q, reviewer)
    w.complete_review(audit, verdict, 0)
    check_all(w)
    return audit


def child(w):
    parent = root(w, tau=40)
    q = w.post_nested(parent, 5)
    w.award(q, 'B', 5, 20)
    w.submit(q)
    w.judge_nested(q, F)
    check_all(w)
    return parent, q


# A. Historical audit authorization and child milestones must remain true when
# a later assessment is accepted. F/N controls use the identical elapsed-time path.
@pytest.mark.parametrize('verdict', [F, N, P, BOT])
def test_later_audit_answer_preserves_its_prior_authorization(verdict):
    w = world(); q = root(w); initial(w, q)
    w.advance(1); audit = w.assign_audit(q, 'D')
    w.advance(2)
    w.complete_review(audit, verdict, 0)
    check_all(w)


@pytest.mark.parametrize('verdict', [F, N])
def test_later_resumed_audit_preserves_its_prior_authorization(verdict):
    w = world(); q = root(w); initial(w, q)
    audit = reopened(w, q)
    w.respond(q, 'supply_evidence')
    w.advance(1); w.resubmit(q)
    w.complete_review(audit, verdict, 0)
    check_all(w)


def test_later_child_audit_does_not_erase_the_parents_valid_milestone():
    w = world(); parent, q = child(w)
    w.submit(parent)                         # legal: the child already had its initial F
    check_all(w)
    w.advance(1)
    audit = w.assign_audit(q, 'C')
    w.complete_review(audit, BOT, 0)         # later provisional assessment is legal too
    check_all(w)


# B. A resumed auditor can time out. Its position must be replaceable; a waiver
# either is refused atomically or must not decrement a nonexistent open item.
@pytest.mark.parametrize('verdict,action', [(P, 'revise'), (BOT, 'supply_evidence')])
def test_reopened_audit_timeout_has_a_replacement_path(verdict, action):
    w = world(); q = root(w); initial(w, q)
    audit = reopened(w, q, verdict)
    w.respond(q, action); w.resubmit(q)
    w.advance(6)
    assert w.reviews[audit].status == 'withdrawn'
    replacement = None
    errors = []
    for assign in (w.assign_audit, w.assign_initial):
        try:
            replacement = assign(q, 'E')
            break
        except (RuleError, LedgerError) as exc:
            errors.append(str(exc))
    assert replacement is not None, 'Eligible replacement denied by both APIs: ' + '; '.join(errors)
    assert w.observe('E', replacement).resumed, 'A replacement inherits the resubmitted stage.'
    w.complete_review(replacement, F, 0)
    check_all(w)
    w.advance(w.cases[q].window_end + 1)
    assert w.cases[q].state == 'VESTED'


def test_waiver_after_reopened_audit_timeout_cannot_make_obligation_count_negative():
    w = world(); q = root(w); initial(w, q)
    reopened(w, q)
    w.respond(q, 'supply_evidence'); w.resubmit(q); w.advance(6)
    before = w.history.head
    try:
        w.waive_audit(q)
    except (RuleError, LedgerError):
        assert w.history.head == before, 'A refused waiver must not be recorded as admitted.'
    assert w.cases[q].open_items >= 0, 'The waiver decremented zero open items to -1.'
    check_all(w)


def test_control_unreopened_audit_timeout_can_be_replaced():
    w = world(); q = root(w); initial(w, q)
    a = w.assign_audit(q, 'D'); w.advance(6)
    assert w.reviews[a].status == 'withdrawn'
    b = w.assign_audit(q, 'E'); w.complete_review(b, F, 0)
    w.advance(11); check_all(w)
    assert w.cases[q].state == 'VESTED'


# C. The adjudication target is the auditor who reopened the case, not necessarily
# the first-ever reviewer or the parent requester. V_max counts the current path.
def test_upheld_reopening_audit_appeal_stays_within_the_path_bound():
    w = world(); q = root(w); original = initial(w, q)
    audit = reopened(w, q)
    w.respond(q, 'appeal', d='The named evidence was present.')
    e = w.assign_appeal(q, 'E'); f = w.assign_appeal(q, 'F')
    w.complete_review(e, N, 0, objection=UPHELD)
    w.complete_review(f, N, 0, objection=UPHELD)
    assert w.cases[q].state == 'FINAL_N'
    assert w.reviews[original].status == 'overturned'
    check_all(w)
    assert w.positions(q) <= w.p.V_max
    w.advance(1); check_all(w)


@pytest.mark.parametrize('verdict', [F, N])
def test_nested_audit_appeal_charges_the_auditor_not_the_requester(verdict):
    w = world(); parent, q = child(w)
    audit = reopened(w, q, reviewer='C')
    assert w.cases[q].rejection_bond == 0, 'The parent already accepted and released its rejection bond.'
    w.respond(q, 'appeal', d='The evidence the auditor requested was in the submission.')
    d = w.assign_appeal(q, 'D'); e = w.assign_appeal(q, 'E')
    w.complete_review(d, verdict, 0, objection=REJECTED)
    w.complete_review(e, verdict, 0, objection=REJECTED)
    assert w.reviews[audit].status == 'overturned'
    assert w.cases[q].court_fee_reimbursed == pytest.approx(w.cases[q].D)
    transfers = [ev for ev in w.ledger.events
                 if ev.case == q and ev.kind == 'forfeit_to' and 'court fee' in ev.note]
    assert len(transfers) == 1 and transfers[0].src == 'C' and transfers[0].dst == 'B'
    check_all(w)


def test_nested_abandoned_audit_records_the_premature_requester_approval():
    w = world(); parent, q = child(w)
    before = w.actors['A'].o
    reopened(w, q, reviewer='C')
    w.respond(q, 'accept')
    check_all(w)
    assert w.actors['A'].o == before + 1, (
        'The parent is the nested initial assessor: final N after abandoning the '
        'reopening audit must record its premature approval, without a second bond.')


@pytest.mark.parametrize('verdict', [F, N])
def test_control_root_reopening_audit_rejected_appeal_settles(verdict):
    w = world(); q = root(w); initial(w, q); a = reopened(w, q)
    w.respond(q, 'appeal', d='The evidence was present.')
    e = w.assign_appeal(q, 'E'); f = w.assign_appeal(q, 'F')
    w.complete_review(e, verdict, 0, objection=REJECTED)
    w.complete_review(f, verdict, 0, objection=REJECTED)
    assert w.reviews[a].status == 'overturned'
    assert w.cases[q].court_fee_reimbursed == pytest.approx(2)
    check_all(w)
    w.advance((w.cases[q].window_end + 1) if verdict == F else 1)
    check_all(w)


def test_control_original_nested_rejection_appeal_uses_requester_bond():
    w = world(); parent = root(w, tau=40)
    q = w.post_nested(parent, 5); w.award(q, 'B', 5, 20); w.submit(q); w.judge_nested(q, N)
    w.respond(q, 'appeal', d='I fulfilled the request.')
    d = w.assign_appeal(q, 'D'); e = w.assign_appeal(q, 'E')
    w.complete_review(d, F, 0); w.complete_review(e, F, 0)
    assert w.cases[q].rejection_bond == 0 and w.cases[q].court_fee_reimbursed == pytest.approx(2)
    check_all(w)


# D. An actor may have taken other work during PENDING. Reopening cannot silently
# create a second executing commitment or an ordinary commitment plus an open review.
def test_reopening_cannot_create_a_second_untracked_execution():
    w = world(); q = root(w); initial(w, q)
    other = root(w, actor='A', tau=40)       # explicitly permitted while q is pending
    audit = w.assign_audit(q, 'D'); w.complete_review(audit, BOT, 0)
    w.respond(q, 'supply_evidence'); w.resubmit(q)
    w.spend('A', 1, q); w.spend('A', 1, other)
    active = [c.id for c in w.cases.values() if c.actor == 'A' and c.state in w.EXECUTING]
    assert len(active) <= 1, 'Two cases execute under one actor: ' + repr(active)
    check_all(w)


def test_reopening_while_actor_reviews_preserves_one_active_assignment():
    w = world(); q = root(w, tau=40)
    w.advance(29); initial(w, q)
    w.advance(31)                           # normal rotation puts A on duty, releases D
    other = root(w, actor='D'); w.submit(other)
    review = w.assign_initial(other, 'A')
    assert w.actors['A'].open_review == review
    audit = w.assign_audit(q, 'B'); w.complete_review(audit, BOT, 0)
    check_all(w)


def test_control_idle_actor_can_resume_a_reopened_audit():
    w = world(); q = root(w); initial(w, q); a = reopened(w, q)
    w.respond(q, 'supply_evidence'); w.resubmit(q); w.complete_review(a, F, 0)
    w.advance(11); check_all(w)
    assert w.cases[q].state == 'VESTED'


# E. Merging an in-progress audit into a paid requester dispute must not lose the
# challenge's obligation when that audit uses the newly allowed P/BOT response.
@pytest.mark.parametrize('verdict', [P, BOT])
def test_merged_audit_reopening_keeps_the_dispute_answerable(verdict):
    w = world(); q = root(w); initial(w, q)
    a = w.assign_audit(q, 'D')
    w.dispute(q, 'H', d='The accepted result does not meet the request.')
    e = w.assign_appeal(q, 'E')
    assert w.cases[q].open_items == 1 and w.cases[q].challenge['kind'] == 'dispute'
    w.complete_review(a, verdict, 0)
    check_all(w)
    view = w.observe('E', e)
    assert view.question == 'dispute'
    # The documented dispute interface still requires F/N and objection=None.
    w.complete_review(e, N, 0)
    if not w.cases[q].challenge['resolved']:
        w.rule(q, N)
    assert w.cases[q].open_items >= 0, 'The admitted dispute ruling left -1 outstanding items.'
    check_all(w)


@pytest.mark.parametrize('verdict', [F, N])
def test_control_merged_audit_definitive_answer_settles(verdict):
    w = world(); q = root(w); initial(w, q)
    a = w.assign_audit(q, 'D'); w.dispute(q, 'H', d='Please examine this result.')
    e = w.assign_appeal(q, 'E')
    w.complete_review(a, verdict, 0); w.complete_review(e, verdict, 0)
    check_all(w)
    assert w.cases[q].challenge['resolved'] and w.cases[q].open_items == 0
    w.advance(11 if verdict == F else 1); check_all(w)

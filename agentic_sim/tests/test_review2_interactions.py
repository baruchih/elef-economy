"""Additional v0.5 conformance checks; supplied implementation is unmodified.

These test protocol properties, not strategy optimality or real-world usefulness.
Several tests intentionally assert behavior not implemented yet; see REVIEW.md.
"""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'agentic_sim'))

import pytest
from sim import Params, World, RuleError, LedgerError, InvariantError, check_all
from sim.engine import F, N, P, BOT, UPHELD, REJECTED, HUMAN, DEFAULT

ACTORS = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
DUTY = ['C', 'D', 'E', 'F']

def world(**options):
    defaults = dict(E0=0.0, omega_rate=0.0)
    defaults.update(options)
    return World(Params(**defaults), ACTORS, humans={'H': 1000.0}, on_duty=DUTY)

def root(w, actor='A', price=10, duration=100):
    q = w.post_root('H', max(1, price))
    w.award(q, actor, price, duration)
    return q

def initial(w, q, reviewer='C', verdict=F, cost=0):
    w.submit(q)
    r = w.assign_initial(q, reviewer)
    w.complete_review(r, verdict, cost)
    return r


def test_r4_01_unknown_case_spend_is_atomic():
    w = world()
    before = (w.W('A'), w.ledger.Res, w.ledger.M, len(w.ledger.events))
    with pytest.raises(RuleError):
        w.spend('A', 3, 'not-a-case')
    after = (w.W('A'), w.ledger.Res, w.ledger.M, len(w.ledger.events))
    assert after == before, f'Refused spend changed money: {before} -> {after}'


def test_r4_02_unfundable_fee_pool_payment_is_atomic():
    w = world()
    q = root(w)
    before = (w.ledger.pool(q).deposit, w.W('C'), w.ledger.total_credits())
    with pytest.raises(LedgerError):
        w.ledger.pay_from_fee_pool(q, 'C', 11)
    after = (w.ledger.pool(q).deposit, w.W('C'), w.ledger.total_credits())
    assert after == before, f'Refused payout changed balances: {before} -> {after}'


def test_r4_03_refused_override_cannot_supply_later_human_provenance():
    w = world()
    q = w.post_root('H', 10)
    with pytest.raises(RuleError):
        w.override(q, 'H', F)  # AVAILABLE: no result exists, so rightly rejected
    w.award(q, 'A', 10, 10)
    initial(w, q)
    w.advance(11)
    assert w.cases[q].grade == DEFAULT, (
        f'Refused override became provenance: grade={w.cases[q].grade}; '
        f'assessments={w.cases[q].assessments}'
    )


def test_r4_04_override_during_open_appeal_voids_unfinished_reviewers():
    w = world()
    q = root(w)
    initial(w, q, verdict=N)
    w.respond(q, 'appeal')
    rd = w.assign_appeal(q, 'D')
    re = w.assign_appeal(q, 'E')
    w.override(q, 'H', F)
    assert all(w.actors[a].open_review is None for a in ('D', 'E')), (
        'Human resolved the appeal but its reviewers remain assigned'
    )
    assert all(w.ledger.lock_record(a, f'bond:{r}') == 0 for a, r in [('D', rd), ('E', re)])
    w.advance(6)
    assert w.actors['D'].o == w.actors['E'].o == 0


def test_r4_05_bot_override_cannot_uphold_missing_evidence_and_fulfill():
    w = world()
    q = root(w)
    initial(w, q, verdict=BOT)
    w.respond(q, 'appeal')
    rd = w.assign_appeal(q, 'D'); re = w.assign_appeal(q, 'E')
    w.complete_review(rd, N, 0, objection=UPHELD)
    w.complete_review(re, F, 0, objection=REJECTED)
    assert not w.cases[q].challenge['resolved']
    with pytest.raises(RuleError):
        w.override(q, 'H', F, objection=UPHELD)


def test_r4_06_audit_timeout_after_window_does_not_skip_replacement():
    w = world()
    q = root(w)
    initial(w, q)
    w.advance(9)
    old = w.assign_audit(q, 'D')  # window ends 10; this review's deadline is 14
    w.advance(15)
    assert w.reviews[old].status == 'withdrawn'
    assert w.cases[q].state == 'PENDING', (
        f'Case became {w.cases[q].state} before timely audit position could be replaced'
    )
    fresh = w.assign_audit(q, 'E')
    w.complete_review(fresh, F, 0)
    w.advance(16)
    assert w.cases[q].state == 'VESTED'


def test_r4_07_all_overturned_reviews_still_have_their_cost_claims():
    # Keep the standard ten-credit root deposit; child reviews exhaust it.
    # Zero initial Omega float deliberately exercises the promised shortfall path.
    w = world(Omega0=0.0, omega_rate=0.05)
    q = root(w, price=40)
    child = w.post_nested(q, 5); w.award(child, 'B', 5, 10)
    w.submit(child); w.judge_nested(child, N); w.respond(child, 'appeal')
    re = w.assign_appeal(child, 'E'); rf = w.assign_appeal(child, 'F')
    w.complete_review(re, F, 5); w.complete_review(rf, F, 5)
    assert w.ledger.pool(q).deposit == 0
    r = initial(w, q, cost=5)
    debt = w.reviews[r].deferred
    assert debt > 0
    w.override(q, 'H', N)
    w.advance(1)
    assert w.reviews[r].status == 'overturned'
    assert w.omega_claims == [('C', pytest.approx(debt))], (
        f'Closed case lost claim: queue={w.omega_claims}, deferred={w.reviews[r].deferred}'
    )


def test_r4_08_fifo_repayment_updates_the_correct_review():
    # Standard deposit and service-fee rate; zero initial Omega float.
    w = world(Omega0=0.0, omega_rate=0.05)
    q1 = root(w, 'A')
    initial(w, q1, reviewer='D', cost=5)
    w.dispute(q1, 'H')
    e1 = w.assign_appeal(q1, 'E'); r1 = w.assign_appeal(q1, 'C')
    w.complete_review(e1, N, 5); w.complete_review(r1, F, 3)
    # Split: q1 waits for a ruling; C is free to review another case.
    assert not w.cases[q1].challenge['resolved']
    assert w.reviews[r1].deferred == pytest.approx(0.5)
    w.advance(1)
    q2 = root(w, 'B')
    initial(w, q2, reviewer='D', cost=5)
    w.dispute(q2, 'H')
    e2 = w.assign_appeal(q2, 'E'); r2 = w.assign_appeal(q2, 'C')
    w.complete_review(e2, F, 5); w.complete_review(r2, F, 5)
    assert w.reviews[r2].deferred == pytest.approx(2.5)
    w.advance(12)
    assert w.omega_claims == [('C', pytest.approx(2.5))]
    w.advance(14); w.rule(q1, F); w.advance(15)
    assert w.omega_claims == [('C', pytest.approx(2.5)), ('C', pytest.approx(0.5))]
    root(w, 'B', price=60)  # service fee 3 repays the queue
    assert w.omega_claims == []
    actual = (w.reviews[r1].reimbursed, w.reviews[r1].reimbursed_pending,
              w.reviews[r2].reimbursed, w.reviews[r2].reimbursed_pending)
    assert actual == pytest.approx((3, 0, 5, 0)), f'Claims attributed to wrong reviews: {actual}'


def test_r4_09_partial_fulfillment_cannot_open_an_appeal():
    w = world()
    q = root(w)
    initial(w, q, verdict=P)
    with pytest.raises(RuleError):
        w.respond(q, 'appeal')  # §6.1 offers revise or accept N for P


def test_r4_10_explicit_acceptance_is_in_the_committed_history():
    w = world()
    q = root(w)
    initial(w, q)
    before = w.history.head
    w.accept_explicit(q, 'H')
    assert w.history.head != before, 'Explicit acceptance changed provenance without a history commitment'


@pytest.mark.parametrize('record', ['ledger_event', 'case_log'])
def test_r4_11_tampering_with_a_record_copy_is_detected(record):
    w = world()
    q = root(w)
    check_all(w)
    if record == 'ledger_event':
        e = next(e for e in w.ledger.events if e.kind == 'escrow_in' and e.case == q)
        e.dst = 'not-the-recorded-recipient'
    else:
        w.cases[q].log[-1] = (w.t, 'a replacement for the recorded award')
    # The central chain itself has NOT been rewritten or re-hashed.
    with pytest.raises(InvariantError):
        check_all(w)


def test_r4_12_appeal_view_exposes_the_required_objection_task():
    wa = world(); qa = root(wa)
    initial(wa, qa, verdict=BOT)
    wa.respond(qa, 'appeal')
    appeal = wa.assign_appeal(qa, 'D')
    va = wa.observe('D', appeal)
    wb = world(); qb = root(wb)
    initial(wb, qb, verdict=F)
    audit = wb.assign_audit(qb, 'D')
    vb = wb.observe('D', audit)
    # These identical views demand mutually exclusive valid response formats:
    # a BOT appeal requires a disposition; an audit forbids one. Audit vs initial
    # blindness need not hide what issue an appeal reviewer is asked to resolve.
    assert va != vb, f'Different required questions have indistinguishable policy inputs: {va}'


def test_r4_13_nested_override_resolves_rejection_collateral():
    w = world()
    qp = root(w, price=40)
    qn = w.post_nested(qp, 5); w.award(qn, 'B', 5, 10)
    w.submit(qn); w.judge_nested(qn, N)
    w.override(qn, 'H', F)
    w.advance(11)
    assert w.cases[qn].state == 'VESTED'
    assert w.ledger.lock_record('A', f'rej:{qn}') == 0, (
        'Nested case vested successfully but its rejection bond is still locked'
    )

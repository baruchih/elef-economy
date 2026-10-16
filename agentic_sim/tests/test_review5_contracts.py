"""Independent v0.8 protocol/decision-interface checks, not economic strategy runs.

Uses the supplied package without modifications. All Params are the default values;
only actor/requester identities, initial budgets and the explicit initial duty roster
are set. Counterexamples operate through World actions, without mutating case state.

Run from the project root:
    python -m pytest independent_tests/test_v08_review_contracts.py -q --tb=short
"""
from pathlib import Path
import hashlib
import pickle
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import pytest
from sim import Params, World, RuleError, LedgerError, check_all
from sim.engine import F, N, P, BOT, UPHELD, REJECTED, HUMAN, DELEGATE

ACTORS = list('ABCDEFGI')
DUTY = list('CDEF')


def world():
    return World(Params(), ACTORS, humans={'H': 1000.0, 'S': 100.0},
                 on_duty=DUTY, delegates=['S'])


def root(w, requester='H', actor='A', B=10, tau=20):
    q = w.post_root(requester, B)
    w.award(q, actor, B, tau)
    return q


def initial(w, q, verdict=F, cost=0):
    w.submit(q)
    r = w.assign_initial(q, 'C')
    w.complete_review(r, verdict, cost)
    check_all(w)
    return r


def fingerprint(w):
    return hashlib.sha256(pickle.dumps(w, protocol=4)).hexdigest()


def money(w):
    return (w.ledger.M, w.ledger.Res,
            tuple((k, v.U, v.L) for k, v in sorted(w.ledger.wallets.items())),
            tuple((k, v.escrow, v.deposit, v.minted)
                  for k, v in sorted(w.ledger.pools.items())))


def bot_appeal(w, q, disposition):
    original = initial(w, q, BOT)
    w.respond(q, 'appeal', d='The named evidence was available in the submitted result.')
    d = w.assign_appeal(q, 'D')
    e = w.assign_appeal(q, 'E')
    w.complete_review(d, N, 0, objection=disposition)
    w.complete_review(e, N, 0, objection=disposition)
    check_all(w)
    return original, d, e


# A: A correction must account for BOTH parts of an appeal assessment. In the
# failing cases only the objection changes: the reviewer is still contradicted.
@pytest.mark.parametrize('old,new,outcome', [
    (UPHELD, REJECTED, N),   # fail: same fulfillment, objection explicitly rejected
    (REJECTED, UPHELD, N),   # fail: same fulfillment, reverse objection correction
    (UPHELD, REJECTED, F),   # control: both fulfillment and objection change
    (UPHELD, UPHELD, N),     # control: no contradiction
])
def test_post_settlement_correction_uses_both_appeal_answers(old, new, outcome):
    w = world(); q = root(w)
    original, d, e = bot_appeal(w, q, old)
    w.advance(1)
    before_money = money(w)
    before = {a: w.actors[a].o for a in ('D', 'E')}
    w.override(q, 'H', outcome, objection=new)
    check_all(w)
    assert money(w) == before_money, 'A post-settlement correction must not move money.'
    contradicted = (old != new) or (new == REJECTED and outcome != N)
    for rid in (d, e):
        r = w.reviews[rid]
        assert w.actors[r.reviewer].o == before[r.reviewer] + int(contradicted), (
            'The final fulfillment may stay N, but changing the objection still '
            'contradicts this appeal reviewer: ' + r.reviewer)
        assert r.contradicted_by_override == contradicted


# B: Case financial finality can precede the review settlement batch. An admitted
# human correction must not disappear from reviewer reliability at that boundary.
# These tests deliberately do NOT choose whether unsettled fees/bonds should change;
# the existing correction at minimum must reach the completed reviewer in the record.
@pytest.mark.parametrize('kind', ['ordinary_N', 'bot_upheld'])
@pytest.mark.parametrize('after_batch', [False, True])
def test_correction_reaches_completed_review_on_both_sides_of_batch(kind, after_batch):
    w = world(); q = root(w)
    if kind == 'ordinary_N':
        original = initial(w, q, N)
        w.respond(q, 'accept')
        kwargs = {}
    else:
        original, _, _ = bot_appeal(w, q, UPHELD)
        kwargs = {'objection': REJECTED}
    assert w.cases[q].state == 'FINAL_N'
    assert w.reviews[original].status == 'done'
    if after_batch:
        w.advance(1)
        assert w.reviews[original].status == 'vested'
    before_o = w.actors['C'].o
    w.override(q, 'H', F, **kwargs)
    check_all(w)
    if not after_batch:
        w.advance(1)
    check_all(w)
    assert w.actors['C'].o == before_o + 1, (
        'The correction was accepted, but a completed reviewer was skipped only '
        'because its review had not reached the payout batch yet.')


def identical_fulfillment_views():
    # World 1: r2/q2 is an ordinary initial review; r1 occupies a different case.
    w = world()
    other = root(w, actor='B'); w.submit(other); w.assign_initial(other, 'D')
    q = root(w); w.submit(q); r = w.assign_initial(q, 'C')
    # World 2: r2/q2 is a surprise audit. r1 is the initial review on q2.
    x = world(); x.post_root('H', 10)
    qx = root(x); x.submit(qx)
    first = x.assign_initial(qx, 'D'); x.complete_review(first, F, 0)
    audit = x.assign_audit(qx, 'C')
    assert w.observe('C', r) == x.observe('C', audit)
    assert w.observe('C', r).question == 'fulfillment'
    assert not w.observe('C', r).resumed
    check_all(w); check_all(x)
    return (w, r), (x, audit)


# C: The current documented fulfillment interface promises F/N/P/BOT without
# disclosing initial-versus-audit. Identical visible inputs must have a coherent
# admissibility contract. The test does not dictate which hidden rule to revise.
@pytest.mark.parametrize('verdict', [F, N, P, BOT])
def test_identical_fulfillment_views_have_same_response_admissibility(verdict):
    left, right = identical_fulfillment_views()
    admitted = []
    for w, rid in (left, right):
        before = fingerprint(w)
        try:
            w.complete_review(rid, verdict, 0)
        except (RuleError, LedgerError):
            assert fingerprint(w) == before
            admitted.append(False)
        else:
            admitted.append(True)
        check_all(w)
    assert admitted[0] == admitted[1], (
        f'Identical ReviewViews accept {verdict!r} for initial={admitted[0]}, '
        f'audit={admitted[1]}; the policy cannot identify the required output contract.')


# D: Delegated requesters may accept and dispute. The spec brackets which HUMAN
# can rule over which request; it does not explicitly grant that power to a
# requester explicitly identified as a delegate.
def test_delegate_budget_does_not_itself_grant_human_override_power():
    w = world(); q = root(w, requester='H'); initial(w, q, F)
    assert 'S' in w.delegates
    before = fingerprint(w)
    with pytest.raises((RuleError, LedgerError)):
        w.override(q, 'S', N)
    assert fingerprint(w) == before
    check_all(w)


def test_control_actual_human_can_override_delegate_request():
    w = world(); q = root(w, requester='S'); initial(w, q, F)
    w.override(q, 'H', N)
    check_all(w)
    assert w.cases[q].grade == HUMAN and w.cases[q].state == 'FINAL_N'


def test_control_v08_ruling_blocks_dispute_atomically():
    w = world(); q = root(w); initial(w, q, N); w.override(q, 'H', F)
    before = fingerprint(w)
    with pytest.raises(RuleError):
        w.dispute(q, 'H', d='This belongs to human review, not another model round.')
    assert fingerprint(w) == before
    w.advance(11); check_all(w)
    assert w.cases[q].state == 'VESTED'


def test_control_v08_rotation_releases_entire_original_roster():
    w = world(); w.advance(31); check_all(w)
    assert sorted(a.id for a in w.actors.values() if a.on_duty) == list('ABGI')


def test_control_fulfilled_task_cost_and_delivery_payment():
    w = world(); q = root(w); w.spend('A', 2, q); initial(w, q, F, 1)
    w.advance(11); check_all(w)
    assert w.cases[q].state == 'VESTED'
    assert w.W('A') == pytest.approx(58.0)

"""Independent v0.7 conformance checks, not strategy experiments.

Use the submitted source unchanged. Where the specification does not fully settle
whether an action is admissible, either an atomic refusal OR coherent completion
is accepted. The tests do not prescribe a new post-ruling dispute policy.
"""
from pathlib import Path
import hashlib
import pickle
import sys
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'agentic_sim'))
from sim import Params, World, RuleError, LedgerError, check_all
from sim.engine import F, N, P, BOT, HUMAN, DELEGATE

ACTORS = list('ABCDEFGI')
DUTY = list('CDEF')


def world():
    # All economic/time parameters are the supplied defaults.
    return World(Params(), ACTORS, humans={'H': 1000.0, 'S': 100.0},
                 on_duty=DUTY, delegates=['S'])


def root(w, requester='H', B=10, tau=20, actor='A'):
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
    """Compare entire in-memory state without modifying or copying source files."""
    return hashlib.sha256(pickle.dumps(w, protocol=4)).hexdigest()


def balances(w):
    return {k: (v.U, v.L) for k, v in w.ledger.wallets.items()}


# A: No-audit-after-ruling works, but another admitted challenge still uses the old verdict.
def test_requester_dispute_after_ruling_is_refused_whole_or_settles():
    w = world(); q = root(w)
    initial(w, q, N)
    w.override(q, 'H', F)           # C's original rejection is now overruled.
    before = fingerprint(w)
    try:
        w.dispute(q, 'H', d='I challenge whether the submitted result fulfills my request.')
    except (RuleError, LedgerError):
        assert fingerprint(w) == before
        return                    # Explicit atomic refusal is an acceptable rule choice.
    r1 = w.assign_appeal(q, 'D'); r2 = w.assign_appeal(q, 'E')
    w.complete_review(r1, F, 1)
    w.complete_review(r2, F, 1)    # Must not re-overturn C or strand open_items.
    check_all(w)
    w.advance(11)
    assert w.cases[q].state == 'VESTED' and w.cases[q].open_items == 0


# B: The outcome grade must identify the adjudicating source, or authority must be refused first.
@pytest.mark.parametrize('route', ['before_F', 'before_N', 'after_N'])
def test_actual_human_override_of_delegate_request_is_consistent(route):
    w = world(); q = root(w, requester='S')
    initial(w, q, N if route == 'before_F' else F)
    if route == 'after_N':
        w.advance(11)
    outcome = F if route == 'before_F' else N
    before = fingerprint(w)
    try:
        w.override(q, 'H', outcome)
    except (RuleError, LedgerError):
        assert fingerprint(w) == before
        return
    check_all(w)
    if not w.cases[q].final:
        w.advance(11)
    # Do not choose ownership-based versus actual-author-based grading here.
    # The action and I13 must at least agree; the report identifies the ambiguity.
    assert w.cases[q].grade in (HUMAN, DELEGATE)
    check_all(w)


# C: A real expenditure is not automatically an expenditure by the contractor.
def test_other_actor_cost_cannot_become_contractor_kill_fee():
    w = world(); q = root(w, B=20)
    child = w.post_nested(q, 10); w.award(child, 'B', 5, 10)
    before = fingerprint(w)
    try:
        w.spend('C', 4, child)
    except (RuleError, LedgerError):
        assert fingerprint(w) == before
        return
    # Alternatively, separately recorded third-party funding must not become B's own cost.
    B_before = w.W('B')
    w.cancel_nested(child)
    check_all(w)
    assert w.W('B') == pytest.approx(B_before), 'B spent nothing, but was reimbursed C\'s cost.'


def test_spend_on_vested_case_is_rejected_whole_or_invariant_consistent():
    w = world(); q = root(w)
    initial(w, q, F); w.advance(11)
    before = fingerprint(w)
    try:
        w.spend('A', w.ledger.v, q)  # Exactly one credit, despite emission-driven exchange rate.
    except (RuleError, LedgerError):
        assert fingerprint(w) == before
        return
    # Admission and I10 must agree, even if the chosen policy permits later expenditure.
    check_all(w)


# D: Lower-priority malformed-input test, not a claim about valid text appeals.
def test_non_text_grounds_cannot_partially_admit_an_appeal():
    w = world(); q = root(w)
    initial(w, q, N)
    before = fingerprint(w)
    with pytest.raises((RuleError, LedgerError, TypeError, ValueError)):
        w.respond(q, 'appeal', d={0: 'mixed', 'key': 'types'})
    assert fingerprint(w) == before, 'Refused payload collected the fee and opened a challenge.'


# E: A completed missing-evidence assessment is also subject to later non-financial correction.
def test_post_settlement_bot_correction_reaches_the_original_reviewer():
    w = world(); q = root(w)
    original = initial(w, q, BOT)
    w.respond(q, 'appeal', d='The requested evidence was present.')
    d = w.assign_appeal(q, 'D'); e = w.assign_appeal(q, 'E')
    w.complete_review(d, N, 0, objection='upheld')
    w.complete_review(e, N, 0, objection='upheld')
    w.advance(1)                   # Costs, fees and all bonds have settled.
    assert w.reviews[original].status == 'vested'
    before_money = balances(w)
    before_o = w.actors['C'].o
    w.override(q, 'H', F, objection='rejected')
    check_all(w)
    assert balances(w) == before_money       # No clawback: keep this decision.
    assert w.actors['C'].o == before_o + 1, 'The expressly contradicted BOT was left as a survival.'


# Passing controls: demonstrate neighboring paths still work.
def test_control_fulfilled_root_under_full_defaults():
    w = world(); q = root(w)
    w.spend('A', 2, q)
    initial(w, q, F, cost=1)
    w.advance(11)
    assert w.cases[q].state == 'VESTED'
    assert w.W('A') == pytest.approx(58)
    check_all(w)


def test_control_requester_dispute_without_prior_ruling():
    w = world(); q = root(w)
    initial(w, q, F)
    w.dispute(q, 'H', d='Please reconsider.')
    d = w.assign_appeal(q, 'D'); e = w.assign_appeal(q, 'E')
    w.complete_review(d, F, 1); w.complete_review(e, F, 1)
    w.advance(11)
    assert w.cases[q].state == 'VESTED'
    check_all(w)


def test_control_delegate_acceptance_keeps_delegate_grade():
    w = world(); q = root(w, requester='S')
    initial(w, q, F)
    w.accept_explicit(q, 'S'); w.advance(11)
    assert w.cases[q].grade == DELEGATE
    check_all(w)


def test_control_contractor_own_cost_enters_kill_fee():
    w = world(); q = root(w, B=20)
    child = w.post_nested(q, 10); w.award(child, 'B', 5, 10)
    w.spend('B', 4, child)
    before = w.W('B'); w.cancel_nested(child)
    assert w.W('B') - before == pytest.approx(4)
    check_all(w)


def test_control_post_vesting_F_correction_reaches_reviewers_without_clawback():
    w = world(); q = root(w)
    initial(w, q, F); w.advance(11)
    before_money = balances(w); before_o = w.actors['C'].o
    w.override(q, 'H', N)
    assert balances(w) == before_money and w.actors['C'].o == before_o + 1
    check_all(w)

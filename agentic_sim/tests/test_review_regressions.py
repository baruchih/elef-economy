"""Independent v0.4 review regressions. Production/source files are unchanged.

These are assertions of the stated protocol (not of the engine's current bugs).
A failure is a reproducible counterexample, not an incentive-simulation result.
See REVIEW.md for scope, sources, and qualifications.
"""
import pytest
from sim import Params, World, RuleError, LedgerError, check_all
from sim.engine import F, N, P, BOT, PROCEDURAL

ACTORS = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
DUTY = ['C', 'D', 'E', 'F']

def world(**over):
    opts = dict(E0=0.0, omega_rate=0.0)
    opts.update(over)
    return World(Params(**opts), ACTORS, humans={'H': 1000.0},
                 on_duty=DUTY, enforce_reserve=True)

def root(w, actor='A', B=10, tau=100):
    q = w.post_root('H', B)
    w.award(q, actor, B, tau)
    return q

def initial(w, q, reviewer='C', verdict=F, cost=0):
    w.submit(q)
    r = w.assign_initial(q, reviewer)
    w.complete_review(r, verdict, cost)
    return r


def test_review_01_busy_reviewer_cannot_accept_another_review():
    w = world()
    q1, q2 = root(w, 'A'), root(w, 'B')
    w.submit(q1); w.submit(q2)
    w.assign_initial(q1, 'C')
    # C has an unfinished review, not merely a lingering financial liability.
    with pytest.raises(RuleError):
        w.assign_initial(q2, 'C')


def test_review_02_timed_out_appeal_position_can_be_reassigned():
    w = world()
    q = root(w)
    initial(w, q, verdict=N)
    w.respond(q, 'appeal')
    r1 = w.assign_appeal(q, 'D')
    r2 = w.assign_appeal(q, 'E')
    w.advance(1); w.complete_review(r1, F, 0)
    w.advance(6)
    assert w.reviews[r2].status == 'withdrawn'
    replacement = w.assign_appeal(q, 'F')
    w.complete_review(replacement, F, 0)
    assert w.cases[q].challenge['resolved']


def test_review_03_timed_out_audit_position_can_be_reassigned():
    w = world()
    q = root(w)
    initial(w, q)
    old = w.assign_audit(q, 'D')
    w.advance(6)
    assert w.reviews[old].status == 'withdrawn'
    replacement = w.assign_audit(q, 'E')
    w.complete_review(replacement, F, 0)
    w.advance(11)
    assert w.cases[q].state == 'VESTED'


def test_review_04_reimbursement_uses_spent_credits_not_real_cost():
    # A normally completed first case creates dilution through the engine.
    w = world(E0=10000.0, H=1e9)
    q1 = root(w, 'A', B=1)
    initial(w, q1, cost=0)
    w.advance(11)
    assert w.ledger.v < .51
    q2 = root(w, 'B', B=10)
    w.submit(q2)
    r = w.assign_initial(q2, 'D')
    spent_credits = 3 / w.ledger.v
    w.complete_review(r, F, 3)
    assert w.reviews[r].reimbursed == pytest.approx(min(spent_credits, w.cases[q2].K))


def test_review_05_unawarded_nested_bond_is_reconciled_at_award():
    w = world(E0=10000.0, H=1e9)
    qp = root(w, 'A', B=40)
    qn = w.post_nested(qp, 5)          # locks rejection bond at pre-dilution value
    qa = root(w, 'B', B=1)
    initial(w, qa, cost=0)
    w.advance(11)                    # a different case vests; value changes
    w.award(qn, 'G', 5, 10)
    c = w.cases[qn]
    assert c.rejection_bond == pytest.approx(c.G_V)


def test_review_06_future_service_fee_pays_fifo_reimbursement_claim():
    w = world(Omega0=0.0, omega_rate=.05)
    q = root(w, B=10)
    initial(w, q, cost=5)             # deposit 5, Omega .5
    w.dispute(q, 'H')                 # Omega 2.5
    re = w.assign_appeal(q, 'E'); rf = w.assign_appeal(q, 'F')
    w.complete_review(re, F, 5)       # deposit 0
    w.complete_review(rf, F, 5)       # Omega 0, defer 2.5
    w.advance(11)
    assert w.omega_claims == [('F', 2.5)]
    before = w.W('F')
    root(w, 'B', B=60)               # service fee 3, enough for the existing claim
    w.advance(12)
    assert w.W('F') - before == pytest.approx(2.5)
    assert w.omega_claims == []


def test_review_07_overturned_review_keeps_eligible_reimbursement_claim():
    w = world(Omega0=0.0, omega_rate=.05)
    q = root(w, B=10)
    initial(w, q, cost=5)
    w.dispute(q, 'H')
    re = w.assign_appeal(q, 'E'); rf = w.assign_appeal(q, 'F')
    w.complete_review(re, F, 5)
    w.complete_review(rf, N, 5)       # 2.5 paid, 2.5 deferred
    w.rule(q, F)                     # F loses its bond, not its cost reimbursement
    w.advance(11)
    paid = w.reviews[rf].reimbursed
    owed = sum(amount for who, amount in w.omega_claims if who == 'F')
    assert paid + owed == pytest.approx(5)


def test_review_08_prevesting_override_reconciles_original_review():
    w = world()
    q = root(w)
    r = initial(w, q, cost=3)
    w.advance(1)
    w.override(q, 'H', N)
    w.advance(2)
    assert w.cases[q].outcome == N
    assert w.reviews[r].status == 'overturned'
    assert w.reviews[r].fee == 0
    assert w.actors['C'].o == 1


def test_review_09_postvesting_override_updates_affected_reviewer():
    w = world()
    q = root(w)
    initial(w, q, cost=0)
    w.advance(11)
    before = w.W('C')
    w.override(q, 'H', N)
    # No money clawback, but the inherited human-override rule adjusts involved reviewers.
    assert w.W('C') == before
    assert w.actors['C'].o == 1


def test_review_10_nested_override_keeps_nested_grade_procedural():
    w = world()
    qp = root(w, B=40)
    qn = w.post_nested(qp, 5)
    w.award(qn, 'B', 5, 5)
    w.submit(qn); w.judge_nested(qn, F)
    w.advance(11)
    w.override(qn, 'H', N)
    assert w.cases[qn].grade == PROCEDURAL
    check_all(w)


def test_review_11_only_one_partial_revision_is_permitted():
    w = world()
    q = root(w)
    r = initial(w, q, verdict=P)
    w.respond(q, 'revise')
    with pytest.raises(RuleError):
        w.complete_review(r, P, 0)   # the re-review must be F or N, not another P


def test_review_12_appeal_can_uphold_a_cannot_assess_claim():
    w = world()
    q = root(w)
    r = initial(w, q, verdict=BOT)
    w.respond(q, 'appeal')
    rd = w.assign_appeal(q, 'D'); re = w.assign_appeal(q, 'E')
    # Intended case: missing evidence was indeed missing; final outcome is N.
    # The API has no separate way to specify that the original BOT claim was upheld.
    w.complete_review(rd, N, 0); w.complete_review(re, N, 0)
    assert w.cases[q].outcome == N
    assert w.cases[q].court_fee_reimbursed == 0
    assert w.reviews[r].status != 'overturned'


def test_review_13_pool_exhaustion_withdraws_all_unawarded_children():
    w = world()
    qp = root(w, B=40, tau=20)
    qn1 = w.post_nested(qp, 1)
    qn2 = w.post_nested(qp, 1)
    w.advance(5)
    w.withdraw_pool_exhaustion(qp, qn1)
    assert w.cases[qp].state == 'FINAL_N'
    assert w.cases[qn2].state == 'WITHDRAWN'
    assert w.wallet('A').L == pytest.approx(0)


def test_review_14_failed_award_has_no_partial_financial_effects():
    w = World(Params(E0=0, omega_rate=0), ACTORS, humans={'H': 42},
              on_duty=DUTY, enforce_reserve=True)
    q = w.post_root('H', 40)
    before = (w.W('H'), w.wallet('A').U, w.wallet('A').L,
              w.ledger.pool(q).escrow, w.ledger.pool(q).deposit, w.ledger.M)
    with pytest.raises(LedgerError):
        w.award(q, 'A', 40, 10)       # enough for B, but not B+phi
    after = (w.W('H'), w.wallet('A').U, w.wallet('A').L,
             w.ledger.pool(q).escrow, w.ledger.pool(q).deposit, w.ledger.M)
    unchanged = (after == before)
    assert unchanged, "rejected award locked the actor guarantee and debited requester escrow"


def test_review_15_failed_appeal_does_not_consume_challenge_round():
    w = world()
    q = root(w)
    initial(w, q, verdict=N)
    w.spend('A', w.wallet('A').U)     # all unlocked balance; bond remains intact
    with pytest.raises(LedgerError):
        w.respond(q, 'appeal')
    assert not w.cases[q].challenge_round_used
    assert w.cases[q].challenge is None


@pytest.mark.parametrize('cost', [-10.0, float('nan')])
def test_review_16_invalid_resource_cost_is_rejected(cost):
    w = world()
    with pytest.raises((RuleError, LedgerError, ValueError)):
        w.spend('A', cost)


def test_review_17_kill_fee_includes_completed_subcontract_costs():
    w = world()
    qp = root(w, B=40)
    qn = w.post_nested(qp, 10)
    w.award(qn, 'B', 10, 50)
    qg = w.post_nested(qn, 2)
    w.award(qg, 'G', 2, 5)
    w.submit(qg); w.judge_nested(qg, F)
    w.advance(11)                     # B has paid G two credits for completed work
    assert w.W('B') == pytest.approx(48)
    w.cancel_nested(qn)               # B has not yet submitted to A
    assert w.W('B') == pytest.approx(50)  # capped eligible cost 2 reimbursed, no profit


def test_review_18_unused_deposit_returned_when_no_review_entitled():
    w = world()
    q = root(w)
    w.submit(q)
    w.override(q, 'H', F)            # explicit acceptance with no paid reviews
    w.advance(1)
    assert w.cases[q].state == 'VESTED'
    assert w.W('H') == pytest.approx(990)  # delivery price 10, deposit returned
    assert w.W('OMEGA') == pytest.approx(20)


def test_review_19_duty_credit_uses_trailing_100_ticks():
    w = world()
    q = root(w)
    initial(w, q)
    w.advance(11)
    assert w.actors['C'].kappa == 1
    w.advance(112)
    assert w.actors['C'].kappa == 0

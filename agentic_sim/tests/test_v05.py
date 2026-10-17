"""The v0.5 rules in their explicit form: the three rule decisions of the third review
(denomination at first lock, the kill-fee cost basis, the two-question appeal of ⊥), the
override-as-ruling semantics, Ω claim servicing, occupancy, rotation, the filtered
reviewer view, and the hash-chained record."""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
try:
    import pytest
except ImportError:
    sys.path.insert(0, os.path.dirname(__file__))
    from _mini_pytest import pytest

from sim import Params, World, RuleError, LedgerError, InvariantError, Ledger, check_all
from sim.engine import F, N, P, BOT, UPHELD, REJECTED, HUMAN, DEFAULT, PROCEDURAL

ACTORS = ["A", "B", "C", "D", "E", "F", "G"]
DUTY = ["C", "D", "E", "F"]


def world(**over):
    kw = dict(E0=0.0, omega_rate=0.0)
    kw.update(over)
    return World(Params(**kw), ACTORS, humans={"H": 1000.0}, on_duty=DUTY, enforce_reserve=True)


def root(w, actor="A", B=10, tau=100):
    q = w.post_root("H", B)
    w.award(q, actor, B, tau)
    return q


def initial(w, q, reviewer="C", verdict=F, cost=0):
    w.submit(q)
    r = w.assign_initial(q, reviewer)
    w.complete_review(r, verdict, cost)
    return r


# ----------------------------------------------------------- appeal of ⊥, explicit
def test_bot_appeal_upheld_original_stands_actor_bears_fee():
    w = world()
    q = root(w)
    r = initial(w, q, verdict=BOT, cost=2)
    w.respond(q, "appeal")                     # A pays D=2
    rd = w.assign_appeal(q, "D"); re = w.assign_appeal(q, "E")
    w.complete_review(rd, N, 0, objection=UPHELD)   # the evidence really was missing
    w.complete_review(re, N, 0, objection=UPHELD)
    c = w.cases[q]
    assert c.state == "FINAL_N" and c.outcome == N
    assert c.court_fee_reimbursed == 0                      # the actor loses the fee
    assert w.reviews[r].status == "done"                   # the ⊥ was right: no overturn
    assert w.ledger.wallet("C").L == pytest.approx(5)      # bond still held until settlement
    w.advance(1)
    assert w.reviews[r].status == "vested"                 # and paid like any correct verdict
    assert w.actors["C"].o == 0 and w.actors["A"].o == 1


def test_bot_appeal_rejected_original_overturned_and_fulfillment_decides():
    w = world()
    q = root(w)
    r = initial(w, q, verdict=BOT, cost=2)
    w.respond(q, "appeal")
    rd = w.assign_appeal(q, "D"); re = w.assign_appeal(q, "E")
    w.complete_review(rd, F, 0, objection=REJECTED)  # the evidence was there, and it fulfils
    w.complete_review(re, F, 0, objection=REJECTED)
    c = w.cases[q]
    assert c.outcome == F and c.state == "PENDING"
    assert w.reviews[r].status == "overturned"
    assert c.court_fee_reimbursed == pytest.approx(2)      # from C's bond
    assert w.actors["C"].o == 1


def test_bot_appeal_objection_must_be_stated_and_consistent():
    w = world()
    q = root(w)
    initial(w, q, verdict=BOT, cost=0)
    w.respond(q, "appeal")
    rd = w.assign_appeal(q, "D")
    with pytest.raises(RuleError):
        w.complete_review(rd, N, 0)                        # no disposition: not expressible, so refused
    with pytest.raises(RuleError):
        w.complete_review(rd, F, 0, objection=UPHELD)      # missing evidence cannot be F
    w.complete_review(rd, N, 0, objection=UPHELD)
    re = w.assign_appeal(q, "E")
    w.complete_review(re, F, 0, objection=REJECTED)        # split on the objection
    assert not w.cases[q].challenge["resolved"]
    with pytest.raises(RuleError):
        w.rule(q, F)                                       # a ⊥ ruling states both answers
    w.rule(q, N, objection=UPHELD)
    c = w.cases[q]
    assert c.outcome == N and w.reviews[re].status == "overturned" and w.reviews[rd].status == "done"


# ------------------------------------------------- denomination at first lock (§4.5)
def test_nested_case_is_denominated_at_posting():
    w = world(E0=10000.0, H=1e9)
    qp = root(w, "A", B=40)
    qn = w.post_nested(qp, 5)
    frozen = (w.cases[qn].D, w.cases[qn].K, w.cases[qn].G_V)
    qa = root(w, "B", B=1)
    initial(w, qa, cost=0)
    w.advance(11)                                           # dilution through a normal vesting
    assert w.ledger.v < 0.51
    w.award(qn, "G", 5, 10)
    c = w.cases[qn]
    assert (c.D, c.K, c.G_V) == frozen and c.rejection_bond == pytest.approx(c.G_V)
    q2 = root(w, "B", B=10)                                 # a root awarded now is indexed now
    assert w.cases[q2].D == pytest.approx(2 / w.ledger.v)


# ------------------------------------------------------------- kill-fee cost basis
def test_kill_fee_counts_completed_subcontract_payments_and_resource_spend():
    w = world()
    qp = root(w, B=40)
    qn = w.post_nested(qp, 10); w.award(qn, "B", 10, 50)
    qg = w.post_nested(qn, 2); w.award(qg, "G", 2, 5)
    w.submit(qg); w.judge_nested(qg, F)
    w.spend("B", 1, qn)
    w.advance(11)                                           # qg vests: B has paid G 2
    assert w.cases[qn].actor_cost == pytest.approx(3)
    before = w.W("B")
    w.cancel_nested(qn)
    assert w.W("B") - before == pytest.approx(3)            # min(3, K=5)


# ------------------------------------------------------------------- atomicity
def test_unfundable_award_and_unpaid_filing_change_nothing():
    w = World(Params(E0=0, omega_rate=0), ACTORS, humans={"H": 42}, on_duty=DUTY)
    q = w.post_root("H", 40)
    snap = (w.W("H"), w.wallet("A").U, w.wallet("A").L, w.ledger.M, len(w.ledger.events))
    with pytest.raises(LedgerError):
        w.award(q, "A", 40, 10)
    assert snap == (w.W("H"), w.wallet("A").U, w.wallet("A").L, w.ledger.M, len(w.ledger.events))
    assert w.cases[q].state == "AVAILABLE" and w.actors["A"].committed is None
    with pytest.raises(LedgerError):
        w.spend("A", float("inf"))
    with pytest.raises(RuleError):
        w.award(q, "A", 10, 0)                              # tau must be a positive tick count


# ------------------------------------------------------------------ occupancy
def test_one_active_assignment_including_attached_reviewer_after_bot():
    w = world()
    q1, q2 = root(w, "A"), root(w, "B")
    r1 = initial(w, q1, verdict=BOT)                        # C stays attached to q1
    w.submit(q2)
    with pytest.raises(RuleError):
        w.assign_initial(q2, "C")
    w.respond(q1, "accept")                                 # actor gives up: C is released
    assert w.actors["C"].open_review is None
    w.assign_initial(q2, "C")


# ---------------------------------------------------------- override as a ruling
def test_prevesting_override_overturns_contradicting_reviews_and_voids_open_ones():
    w = world()
    q = root(w)
    r = initial(w, q, cost=3)                               # C: F
    a = w.assign_audit(q, "D")                              # open audit
    w.override(q, "H", N)
    assert w.reviews[r].status == "overturned" and w.reviews[a].status == "withdrawn"
    assert w.cases[q].state == "FINAL_N" and w.cases[q].grade == HUMAN
    assert w.ledger.wallet("D").L == 0                      # voided assignment: bond released, no burn
    assert w.actors["D"].o == 0 and w.actors["C"].o == 1


# ------------------------------------------------------------- Ω claim servicing
def test_omega_claims_are_serviced_fifo_from_any_inflow():
    w = world(Omega0=0.0, omega_rate=0.05)
    q = root(w, B=10)
    initial(w, q, cost=5)
    w.dispute(q, "H")
    re = w.assign_appeal(q, "E"); rf = w.assign_appeal(q, "F")
    w.complete_review(re, F, 5); w.complete_review(rf, F, 5)
    w.advance(11)
    assert w.omega_claims == [("F", 2.5)]
    before = w.W("F")
    q2 = root(w, "B", B=10)                                 # ω = 0.5: a partial payment
    assert w.W("F") - before == pytest.approx(0.5) and w.omega_claims == [("F", 2.0)]
    initial(w, q2, reviewer="D", verdict=N)
    w.respond(q2, "appeal")                                 # court fee 2 lands in Ω: the rest is paid
    assert w.omega_claims == [] and w.W("F") - before == pytest.approx(2.5)


# ------------------------------------------------------------------ rotation
def test_rotation_swaps_replacement_before_release_with_lowest_kappa_incoming():
    w = world()
    q = root(w, "A")
    initial(w, q, reviewer="C")                             # C: one vested review by t=10
    w.advance(11)
    assert w.actors["C"].kappa == 1
    w.advance(31)                                           # tick 30: turns end by elapsed time
    duty = sorted(a.id for a in w.actors.values() if a.on_duty)
    assert len(duty) == 4                                   # never below X during handover
    assert "C" not in duty and "A" in duty                  # A (free, kappa 0) came in before C left
    assert any(e["kind"] == "rotation" for e in w.history.entries)


def test_volunteer_is_not_rotated_out():
    w = world()
    w.volunteer("C")
    w.advance(31)
    assert w.actors["C"].on_duty


# ------------------------------------------------------- filtered reviewer view
def test_observe_hides_verdicts_identities_and_role():
    w = world()
    q = root(w)
    r = initial(w, q, reviewer="C")
    a = w.assign_audit(q, "D")
    view = w.observe("D", a)
    assert view.case_id == q
    assert not hasattr(view, "actor")       # 1.2.0 §14: the reviewer judges the work, not the worker
    assert not hasattr(view, "role") and not hasattr(view, "verdict") and not hasattr(view, "reviews")
    with pytest.raises(RuleError):
        w.observe("E", a)


# --------------------------------------------------------- hash-chained record
def test_history_chain_detects_tampering():
    w = world()
    root(w)
    w.advance(2)
    assert w.history.verify()
    w.history.entries[0]["payload"]["amount"] = 1.0
    assert not w.history.verify()
    with pytest.raises(InvariantError):
        check_all(w)


# ------------------------------------------- revision and evidence windows
def test_revision_window_and_binary_re_review():
    w = world()
    q = root(w)
    r = initial(w, q, verdict=P)
    w.respond(q, "revise")
    assert w.cases[q].state == "RESUBMITTING"
    w.advance(2)
    w.resubmit(q)
    with pytest.raises(RuleError):
        w.complete_review(r, P, 0)                          # after a revision: F or N only
    w.complete_review(r, F, 0)
    assert w.cases[q].state == "PENDING"
    w2 = world()
    q2 = root(w2)
    initial(w2, q2, verdict=P)
    w2.respond(q2, "revise")
    w2.advance(6)                                           # T_rev = 5 missed at tick 5
    assert w2.cases[q2].state == "FINAL_N"


# ------------------------------------------------------- deferred cost survives
def test_overturned_reviewer_keeps_cost_claim_but_not_fee_or_bond():
    w = world(Omega0=0.0)
    q = root(w, B=10)
    initial(w, q, cost=5)
    w.dispute(q, "H")
    re = w.assign_appeal(q, "E"); rf = w.assign_appeal(q, "F")
    w.complete_review(re, F, 5); w.complete_review(rf, N, 5)
    w.rule(q, F)
    w.advance(11)
    rv = w.reviews[rf]
    assert rv.status == "overturned" and rv.fee == 0
    assert rv.reimbursed + rv.reimbursed_pending == pytest.approx(5)
    assert ("F", 5 - rv.reimbursed) in w.omega_claims

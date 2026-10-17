"""Design revision 1 — specification 1.1.0: the verification deposit is two pots (§4.3).

The worked example of §20 re-settled under 1.1.0 and the properties the revision introduces:
fixed fees by role from the fee pot, expenses from the allowance alone, the cross-pot step and
the refund only at tree closure, nested cases drawing on the root's pots, and invariant I19.
Every figure here is the one §6 of the revision states; the engine reproduces it.

Also re-asserted here, at the 1.1.0 pay-in, is the principle of the fifth review's test
`test_r5_a_unfunded_dispute_keeps_vacated_audit_obligation`, which pinned the v1.0.1 deposit
through the human's budget and is listed as an expected failure for that reason.
"""
import os
import sys
import tempfile

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
try:
    import pytest
except ImportError:  # plain `python3 run_tests.py`
    sys.path.insert(0, os.path.dirname(__file__))
    from _mini_pytest import pytest

from sim import Params, World, LedgerError, InvariantError, Ledger, check_all
from sim.engine import F, N

ACTORS = ["A", "B", "C", "D", "E", "F"]
DUTY = ["C", "D", "E", "F"]


def make_world(budget=100.0, **over):
    kw = dict(E0=5.0, H=1e9, omega_rate=0.0)
    kw.update(over)
    return World(Params(**kw), ACTORS, humans={"H": budget}, on_duty=DUTY)


def nets(w, start=50.0):
    return {a: w.W(a) - start for a in ACTORS}


def worked_example(w):
    """§20 through the audit's agreement at t=8 (as test_spec.run_main_path)."""
    q = w.post_root("H", 45)
    w.award(q, "A", 40, 8)                 # H pays 40 + 10 + 5 = 55
    w.advance(1)
    qn = w.post_nested(q, 6)
    w.award(qn, "B", 5, 3)
    w.spend("B", 3, qn)
    w.advance(3)
    w.submit(qn)
    w.judge_nested(qn, F)
    w.spend("A", 12, q)
    w.advance(4)
    w.submit(q)
    r1 = w.assign_initial(q, "C")
    w.advance(6)
    w.complete_review(r1, F, 3)            # reimbursed 3 from φ^E (7 left)
    r2 = w.assign_audit(q, "D")
    w.advance(8)
    w.complete_review(r2, F, 3)            # reimbursed 3 from φ^E (4 left); agrees
    return q, qn, r1, r2


# ------------------------------------------------------------- §6: the worked example re-settled
def test_worked_example_resettled_under_1_1_0():
    w = make_world()
    q, qn, r1, r2 = worked_example(w)
    assert w.W("H") == 100 - 55                      # pay-in = B + φ^E + φ^F; nothing back before closure
    w.advance(17)
    c = w.cases[q]
    assert c.state == "VESTED" and c.t_vest == 16 and w.cases[qn].t_vest == 13
    n = nets(w)
    assert n["A"] == pytest.approx(23) and n["B"] == pytest.approx(2)
    assert n["C"] == pytest.approx(4)                # -3 + 3 + f 2 + emission 2
    assert n["D"] == pytest.approx(6)                # -3 + 3 + f 3 + emission 3  (was +5 under v1.0.1)
    assert w.W("H") - 100 == pytest.approx(-51)      # 55 in, the unused allowance 4 back  (was -50)
    assert w.W(Ledger.OMEGA) == pytest.approx(20)
    # fees: Owed = 2 + 3 = 5 = φ^F, paid in full; emission in full
    assert (w.reviews[r1].fee_owed, w.reviews[r1].fee_fixed, w.reviews[r1].fee) == (2, 2, pytest.approx(4))
    assert (w.reviews[r2].fee_owed, w.reviews[r2].fee_fixed, w.reviews[r2].fee) == (3, 3, pytest.approx(6))
    # escrow: in 55 = 40 + 6 + 5 + 4 out; the tree closed at the root's vest, the last settlement in it
    assert c.tree_closed and c.t_closed == 16
    assert c.fees_from_pot == pytest.approx(5) and c.expenses_from_pot == 0
    assert c.allowance_refunded == pytest.approx(4) and c.pot_refunded == 0
    pool = w.ledger.pool(q)
    assert pool.total == pytest.approx(0)


def test_default_under_consideration_K3_gives_identical_nets():
    """§2.6: K = 3, φ^E = 6, φ^F = 5 — H pays 51, both reimbursements exhaust the allowance, no refund."""
    w = make_world(K=3.0, phi_E_root=6.0)
    q, qn, r1, r2 = worked_example(w)
    assert w.W("H") == 100 - 51
    w.advance(17)
    n = nets(w)
    assert (n["A"], n["B"], n["C"], n["D"]) == (pytest.approx(23), pytest.approx(2), pytest.approx(4), pytest.approx(6))
    assert w.W("H") - 100 == pytest.approx(-51)
    c = w.cases[q]
    assert c.tree_closed and c.allowance_refunded == 0 and c.pot_refunded == 0
    assert w.ledger.pool(q).deposit == 0


def test_appeal_variant_scales_two_challenge_fees_to_the_pot():
    """§6 variant: C overturned (bond 2 to A, 3 burned, costs reimbursed, no fee); E and F each owed 3,
    Owed 6 > φ^F 5, paid 2.5 each plus emission."""
    w = make_world()
    q = w.post_root("H", 45)
    w.award(q, "A", 40, 8)
    w.advance(1)
    w.spend("A", 12, q)
    w.advance(4)
    w.submit(q)
    r1 = w.assign_initial(q, "C")
    w.advance(6)
    w.complete_review(r1, N, 3)
    w.advance(7)
    w.respond(q, "appeal")
    rE, rF = w.assign_appeal(q, "E"), w.assign_appeal(q, "F")
    w.advance(10)
    w.complete_review(rE, F, 3)
    w.complete_review(rF, F, 3)
    w.advance(17)
    c = w.cases[q]
    assert c.state == "VESTED" and w.reviews[r1].status == "overturned"
    assert w.reviews[r1].fee == 0 and w.reviews[r1].reimbursed == pytest.approx(3)
    for r in (rE, rF):
        assert w.reviews[r].fee_owed == pytest.approx(3) and w.reviews[r].fee_fixed == pytest.approx(2.5)
        assert w.reviews[r].fee == pytest.approx(2.5 + 2.5)          # emission 5 over weight 3 -> 2.5 each
    assert nets(w)["C"] == pytest.approx(-5) and nets(w)["A"] == pytest.approx(40 - 12)
    assert c.fees_from_pot == pytest.approx(5) and c.allowance_refunded == pytest.approx(1) and c.pot_refunded == 0


# -------------------------------------------------------- §2.3 step 3 / §2.4: the refund waits for the tree
def test_refund_waits_for_tree_closure_and_a_nested_settlement_draws_on_the_vested_roots_pots():
    """The root vests at 15 while its nested case waits for a ruling; the pots stay open, the nested
    settlement at 17 takes its fee from the root's pot after the root vested, and only then does the
    unused allowance return — the two I10 exceptions of the revision, and no violation."""
    w = make_world()
    q = w.post_root("H", 45)
    w.award(q, "A", 40, 8)
    w.advance(1)
    qn = w.post_nested(q, 6)
    w.award(qn, "B", 5, 3)
    w.advance(3)
    w.submit(qn)
    w.judge_nested(qn, N)                  # A rejects; the milestone is reached
    w.advance(4)
    w.respond(qn, "appeal")                # B appeals, pays D = 2
    rE, rF = w.assign_appeal(qn, "E"), w.assign_appeal(qn, "F")
    w.spend("A", 12, q)
    w.submit(q)
    r1 = w.assign_initial(q, "C")
    w.advance(5)
    w.complete_review(r1, F, 3)            # root pending, window to 15
    w.advance(6)
    w.complete_review(rE, F, 3)
    w.complete_review(rF, N, 3)            # split: the nested case waits for the orchestrator
    w.advance(16)
    c, cn = w.cases[q], w.cases[qn]
    assert c.state == "VESTED" and c.t_vest == 15
    assert not c.tree_closed and not cn.final
    pool = w.ledger.pool(q)
    assert pool.deposit == pytest.approx(10 - 3 - 3 - 3) and pool.fee_pot == pytest.approx(5 - 2)
    assert w.W("H") == pytest.approx(100 - 55)       # nothing has come back yet
    w.rule(qn, F)                                     # t = 16: B's work accepted; F's N is overturned
    w.advance(17)
    assert cn.state == "VESTED" and w.reviews[rF].status == "overturned"
    assert w.reviews[rE].fee_fixed == pytest.approx(3)        # paid from the root's pot after the root vested
    assert c.tree_closed and c.t_closed == cn.t_vest and c.t_closed > c.t_vest
    assert c.allowance_refunded == pytest.approx(1) and c.pot_refunded == 0
    assert w.W("H") == pytest.approx(100 - 55 + 1)
    check_all(w)                                      # I10 admits exactly these movements; I19 holds


def test_root_overridden_while_its_child_is_pending_keeps_the_claim_until_closure():
    """The r4_07 shape under 1.1.0 (why the cross-pot step waits for closure): the root is ruled N
    while its nested case is pending, its reviewer's deferred cost becomes a claim on Ω — the fee
    pot is not touched, because the nested appeal reviewers are still owed from it — and at the
    child's vest those fees take the pot whole, so the claim outlives closure."""
    w = make_world(E0=0.0, Omega0=0.0, omega_rate=0.05)
    q = w.post_root("H", 40)
    w.award(q, "A", 40, 20)                # H pays 40 + 10 + 5 + 2
    child = w.post_nested(q, 5)
    w.award(child, "B", 5, 10)
    w.submit(child)
    w.judge_nested(child, N)
    w.respond(child, "appeal")             # D = 2 -> Ω (Ω now 2 + 0.25 + 2 = 4.25)
    rE, rF = w.assign_appeal(child, "E"), w.assign_appeal(child, "F")
    w.complete_review(rE, F, 5)            # allowance 10 -> 5
    w.complete_review(rF, F, 5)            # allowance 5 -> 0
    w.submit(q)
    r = w.assign_initial(q, "C")
    w.complete_review(r, F, 5)             # Ω advances its 4.25; the rest is deferred
    # (the rejection bond burned at the appeal raised v a little, so the 5 real units are a few
    # thousandths less than 5 credits; the figures below follow the credits)
    debt = w.reviews[r].deferred
    assert debt == pytest.approx(w.reviews[r].cost - 4.25) and w.cases[q].omega_advance == pytest.approx(4.25)
    w.override(q, "H", N)                  # C overturned; the root is final with no surviving review
    c = w.cases[q]
    assert c.state == "FINAL_N" and not c.tree_closed
    assert w.omega_claims == [("C", pytest.approx(debt))]
    assert w.ledger.pool(q).fee_pot == pytest.approx(5)       # untouched: the child's reviewers are owed from it
    w.advance(11)                          # the child's window closes; E and F vest
    assert w.cases[child].state == "VESTED"
    assert w.reviews[rE].fee_fixed == pytest.approx(2.5) and w.reviews[rF].fee_fixed == pytest.approx(2.5)
    assert c.tree_closed and w.ledger.pool(q).total == pytest.approx(0)
    assert w.omega_claims == [("C", pytest.approx(debt))]     # nothing was left for it; Ω's inflows will serve it
    assert c.omega_advance == pytest.approx(4.25)             # unrecovered, borne by Ω
    check_all(w)


def test_fee_pot_remainder_pays_the_trees_claim_at_closure():
    """Ω has no float; the allowance (5) is spent by the initial review; the audit's cost is deferred
    and becomes a claim at settlement. With a pot of 8 and fees owed 5, the remainder 3 pays the
    claimant directly at closure and retires that much of the claim from Ω's queue."""
    w = make_world(E0=0.0, Omega0=0.0, phi_E_root=5.0, phi_F_root=8.0)
    q = w.post_root("H", 45)
    w.award(q, "A", 40, 8)
    w.advance(1)
    w.submit(q)
    r1 = w.assign_initial(q, "C")
    w.advance(2)
    w.complete_review(r1, F, 5)            # allowance 5 -> 0
    r2 = w.assign_audit(q, "D")
    w.advance(3)
    w.complete_review(r2, F, 5)            # nothing to advance: 5 deferred
    assert w.reviews[r2].deferred == pytest.approx(5)
    w.advance(13)
    c = w.cases[q]
    assert c.state == "VESTED" and c.tree_closed
    assert w.reviews[r1].fee_fixed == pytest.approx(2) and w.reviews[r2].fee_fixed == pytest.approx(3)
    assert c.expenses_from_pot == pytest.approx(3) and c.pot_refunded == 0
    assert w.reviews[r2].reimbursed == pytest.approx(3) and w.reviews[r2].reimbursed_pending == pytest.approx(2)
    assert w.omega_claims == [("D", pytest.approx(2))]
    check_all(w)


def test_fee_pot_remainder_repays_an_unrecovered_advance_at_closure():
    w = make_world(E0=0.0, phi_E_root=5.0, phi_F_root=8.0)      # Ω float 20
    q = w.post_root("H", 45)
    w.award(q, "A", 40, 8)
    w.advance(1)
    w.submit(q)
    r1 = w.assign_initial(q, "C")
    w.advance(2)
    w.complete_review(r1, F, 5)            # allowance 5 -> 0
    r2 = w.assign_audit(q, "D")
    w.advance(3)
    w.complete_review(r2, F, 5)            # Ω advances 5
    assert w.cases[q].omega_advance == pytest.approx(5) and w.W(Ledger.OMEGA) == pytest.approx(15)
    w.advance(13)
    c = w.cases[q]
    assert c.tree_closed and c.omega_advance == pytest.approx(2)         # 3 repaid from the pot's remainder
    assert c.expenses_from_pot == pytest.approx(3) and w.W(Ledger.OMEGA) == pytest.approx(18)
    assert w.omega_claims == []
    check_all(w)


def test_nested_reviews_draw_on_the_roots_pot_first_come_first_served():
    """§2.6: the nested case settles first and takes its fees first; the root's own review is then
    scaled to what is left — here nothing."""
    w = make_world(E0=0.0)
    q = w.post_root("H", 45)
    w.award(q, "A", 40, 20)
    w.advance(1)
    qn = w.post_nested(q, 6)
    w.award(qn, "B", 5, 3)
    w.advance(3)
    w.submit(qn)
    w.judge_nested(qn, N)
    w.advance(4)
    w.respond(qn, "appeal")
    rE, rF = w.assign_appeal(qn, "E"), w.assign_appeal(qn, "F")
    w.advance(7)
    w.complete_review(rE, F, 1)
    w.complete_review(rF, F, 1)            # B wins; A's rejection overturned
    w.submit(q)
    r1 = w.assign_initial(q, "C")
    w.advance(8)
    w.complete_review(r1, F, 1)
    w.advance(14)
    assert w.cases[qn].state == "VESTED"
    assert w.reviews[rE].fee_fixed == pytest.approx(2.5) and w.reviews[rF].fee_fixed == pytest.approx(2.5)
    assert w.ledger.pool(q).fee_pot == pytest.approx(0) and w.ledger.pool(qn).fee_pot == 0
    w.advance(19)
    c = w.cases[q]
    assert c.state == "VESTED" and w.reviews[r1].fee_owed == pytest.approx(2) and w.reviews[r1].fee_fixed == 0
    assert c.fees_from_pot == pytest.approx(5) and c.tree_closed
    reimbursed = sum(w.reviews[r].reimbursed for r in (rE, rF, r1))     # ≈ 3: credits per real unit moved at the burn
    assert c.allowance_refunded == pytest.approx(10 - reimbursed) and c.pot_refunded == 0


# ------------------------------------------------------------------------------- I19 and the pay-in
def test_pay_in_requires_both_pots_and_is_refused_whole():
    w = make_world(budget=54.0)            # one short of 40 + 10 + 5
    q = w.post_root("H", 45)
    before = (w.W("H"), w.W("A"), w.ledger.total_credits(), len(w.ledger.events))
    with pytest.raises(LedgerError):
        w.award(q, "A", 40, 8)
    assert (w.W("H"), w.W("A"), w.ledger.total_credits(), len(w.ledger.events)) == before
    assert w.cases[q].state == "AVAILABLE"


def test_unfunded_dispute_keeps_the_vacated_audit_obligation_at_the_1_1_0_pay_in():
    """The fifth review's r5_a, at a budget of exactly B + φ^E + φ^F: a refused filing waives nothing."""
    w = World(Params(E0=0.0, omega_rate=0.0), ACTORS, humans={"H": 25.0}, on_duty=DUTY)
    q = w.post_root("H", 10)
    w.award(q, "A", 10, 20)                # 10 + 10 + 5: H has zero left
    assert w.W("H") == 0
    w.submit(q)
    r = w.assign_initial(q, "C")
    w.complete_review(r, F, 0)
    w.assign_audit(q, "D")
    w.advance(6)                           # the audit timed out at 5
    c = w.cases[q]
    assert c.audit_vacated and c.open_items == 1
    check_all(w)
    with pytest.raises(LedgerError):
        w.dispute(q, "H", d="I cannot fund this filing")
    assert c.audit_vacated and c.open_items == 1
    assert c.challenge is None and not c.challenge_round_used
    w.advance(11)
    assert not c.final


def test_I19_catches_a_fee_from_the_allowance_and_an_expense_from_the_pot():
    for note, pay in (("review fee", "pay_from_deposit"), ("reimburse r1", "pay_from_fee_pot")):
        w = make_world()
        q = w.post_root("H", 45)
        w.award(q, "A", 40, 8)
        getattr(w.ledger, pay)(q, "C", 1.0, note=note)       # an engine bug would look like this
        with pytest.raises(InvariantError, match="I19"):
            w.advance(1)
        w2 = make_world()
        q2 = w2.post_root("H", 45)
        w2.award(q2, "A", 40, 8)
        getattr(w2.ledger, pay)(q2, "C", 1.0, note=note)
        with pytest.raises(InvariantError, match="I19"):
            check_all(w2)


def test_I19_catches_a_tree_closed_too_early_or_a_refund_before_closure():
    w = make_world()
    q = w.post_root("H", 45)
    w.award(q, "A", 40, 8)
    w.advance(1)
    qn = w.post_nested(q, 6)
    w.award(qn, "B", 5, 3)
    w.cases[q].tree_closed = True                         # the child is still committed
    with pytest.raises(InvariantError, match="I19"):
        check_all(w)
    w.cases[q].tree_closed = False
    w.cases[q].pot_refunded = 1.0                          # money said to have come back before closure
    with pytest.raises(InvariantError, match="I19"):
        check_all(w)


def test_record_mode_keeps_a_root_with_open_pots_resident_until_closure():
    with tempfile.TemporaryDirectory() as d:
        w = make_world(record_dir=d)
        q = w.post_root("H", 45)
        w.award(q, "A", 40, 8)
        w.advance(1)
        qn = w.post_nested(q, 6)
        w.award(qn, "B", 5, 3)
        w.advance(3)
        w.submit(qn)
        w.judge_nested(qn, N)
        w.advance(4)
        w.respond(qn, "appeal")
        rE, rF = w.assign_appeal(qn, "E"), w.assign_appeal(qn, "F")
        w.spend("A", 12, q)
        w.submit(q)
        r1 = w.assign_initial(q, "C")
        w.advance(5)
        w.complete_review(r1, F, 3)
        w.advance(6)
        w.complete_review(rE, F, 3)
        w.complete_review(rF, N, 3)
        w.advance(18)                                      # the root vested at 15; the child waits for a ruling
        c = w.cases.peek(q)
        assert c.state == "VESTED" and not c.tree_closed
        assert w.cases.is_resident(q) and q in w._live_cases
        w.rule(qn, F)
        w.advance(21)
        assert w.cases.peek(q).tree_closed
        assert not w.cases.is_resident(q) and q not in w._live_cases
        check_all(w)
        w.close()

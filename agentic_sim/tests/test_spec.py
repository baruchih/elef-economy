"""Replays spec v0.4 §16 (the worked example and its variants) and every exceptional
path raised by the two external reviews, through the engine, with invariants
checked after every tick.

Numbers are nets (final W minus starting W), which do not depend on the cold-start
float. The example states emission "works out to 2 credits per unit of role weight"
at the vesting tick and omits ω; the fixture sets a flat emission of 5 per tick and
ω = 0 to reproduce it exactly. A separate test turns ω back on.
"""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
try:
    import pytest
except ImportError:  # plain `python3 run_tests.py`
    sys.path.insert(0, os.path.dirname(__file__))
    from _mini_pytest import pytest

from sim import Params, World, RuleError, InvariantError, Ledger, check_all
from sim.engine import F, N, P, BOT, HUMAN, DELEGATE, DEFAULT, PROCEDURAL

ACTORS = ["A", "B", "C", "D", "E", "F"]
DUTY = ["C", "D", "E", "F"]


def make_world(**over):
    kw = dict(E0=5.0, H=1e9, omega_rate=0.0, floating=False)   # 2.0.0: the 1.0.1 money — the backing and index 1
    kw.update(over)
    p = Params(**kw)
    return World(p, ACTORS, humans={"H": 100.0}, on_duty=DUTY)


def nets(w, start=50.0):
    return {a: w.W(a) - start for a in ACTORS}


# ---------------------------------------------------------------- §16 main path
def setup_through_submit(w, tau=8):
    q = w.post_root("H", 45)
    w.award(q, "A", 40, tau)               # t=0: H pays 40 + 10; A locks 20; due by tau
    w.advance(1)
    qn = w.post_nested(q, 6)               # t=1: A locks 6 + 5 (rejection bond)
    w.award(qn, "B", 5, 3)                 # escrow 5 from A's lock, 1 released; B locks 3; due by 4
    w.spend("B", 3, qn)
    w.advance(3)
    w.submit(qn)                           # t=3
    w.judge_nested(qn, F)                  # A accepts: rejection bond released; qn window to 13
    w.spend("A", 12, q)
    w.advance(4)
    w.submit(q)                            # t=4
    r1 = w.assign_initial(q, "C")          # C locks 5; review deadline 9
    w.advance(6)
    return q, qn, r1


def run_main_path(w):
    q, qn, r1 = setup_through_submit(w)
    w.complete_review(r1, F, 3)            # t=6: reimbursed 3 from deposit; q pending, window to 16
    r2 = w.assign_audit(q, "D")            # blind audit; vesting suspended
    w.advance(8)
    w.complete_review(r2, F, 3)            # t=8: agrees; suspension lifted
    return q, qn, r1, r2


def test_main_path_nets_and_escrow():
    w = make_world()
    q, qn, r1, r2 = run_main_path(w)
    w.advance(14)
    assert w.cases[qn].state == "VESTED" and w.cases[qn].t_vest == 13
    w.advance(17)
    c = w.cases[q]
    assert c.state == "VESTED" and c.t_vest == 16
    n = nets(w)
    assert n["A"] == pytest.approx(23)     # 40 - (12 + 5)
    assert n["B"] == pytest.approx(2)      # 5 - 3
    assert n["C"] == pytest.approx(4)      # -3 cost +3 reimbursed + fixed fee 2 + emission 2x1.0
    assert n["D"] == pytest.approx(6)      # -3 +3 + fixed fee 3 (audit weight 1.5) + emission 2x1.5
    assert w.W("H") - 100 == pytest.approx(-51)         # paid 40 + 10 + 5; the unused allowance 4 came back
    assert w.W(Ledger.OMEGA) == pytest.approx(300)      # Ω untouched (Ω₀ = 300 since 1.2.0)
    pool = w.ledger.pool(q)
    assert pool.escrow == pytest.approx(0) and pool.deposit == pytest.approx(0) and pool.fee_pot == pytest.approx(0)
    # escrow in 55 = 40 (A) + 6 (reimbursements) + 5 (fixed fees: Owed = 2 + 3 = φ^F) + 4 (allowance returned)
    assert c.reimb_total == pytest.approx(6)
    assert c.tree_closed and c.allowance_refunded == pytest.approx(4) and c.pot_refunded == pytest.approx(0)
    assert w.reviews[r1].fee + w.reviews[r2].fee == pytest.approx(5 + 5)   # 5 fixed + 5 emission
    assert (w.reviews[r1].fee_fixed, w.reviews[r2].fee_fixed) == (pytest.approx(2), pytest.approx(3))
    assert c.grade == PROCEDURAL            # an audit occurred: the outcome was established by procedure
    assert w.cases[qn].grade == PROCEDURAL
    assert w.actors["C"].kappa == 1 and w.actors["D"].kappa == 1


def test_main_path_with_service_fee():
    w = make_world(omega_rate=0.05)
    q, qn, r1, r2 = run_main_path(w)
    w.advance(17)
    assert w.W(Ledger.OMEGA) == pytest.approx(300 + 2 + 0.25)   # ω on root (5% of 40) and nested (5% of 5)
    assert w.W("H") - 100 == pytest.approx(-53)         # -51 and the service fee 2
    assert nets(w)["A"] == pytest.approx(23 - 0.25)


def test_silence_without_audit_is_protocol_default_and_explicit_accept_is_human():
    for explicit in (False, True):
        w = make_world()
        q = w.post_root("H", 45)
        w.award(q, "A", 40, 8)
        w.advance(1)
        w.submit(q)
        r1 = w.assign_initial(q, "C")
        w.advance(2)
        w.complete_review(r1, F, 3)
        if explicit:
            w.accept_explicit(q, "H")
        w.advance(13)
        assert w.cases[q].state == "VESTED"
        assert w.cases[q].grade == (HUMAN if explicit else DEFAULT)


def test_delegate_root_requester_grade():
    p = Params(E0=5.0, H=1e9, omega_rate=0.0)
    w = World(p, ACTORS, humans={"S": 100.0}, on_duty=DUTY, delegates=["S"])
    q = w.post_root("S", 45)
    w.award(q, "A", 40, 8)
    w.advance(1)
    w.submit(q)
    r1 = w.assign_initial(q, "C")
    w.advance(2)
    w.complete_review(r1, F, 3)
    w.accept_explicit(q, "S")
    w.advance(13)
    assert w.cases[q].grade == DELEGATE


# ------------------------------------------------------- §16 variant: appeal
def test_appeal_variant():
    w = make_world()
    q, qn, r1 = setup_through_submit(w)
    w.complete_review(r1, N, 3)             # t=6: C rejects
    assert w.cases[q].state == "AWAITING_RESPONSE"
    w.advance(7)
    w.respond(q, "appeal")                  # A pays D=2 -> Ω
    assert w.actors["A"].committed is None  # capacity released at response
    rE = w.assign_appeal(q, "E")
    rF = w.assign_appeal(q, "F")
    w.advance(10)
    w.complete_review(rE, F, 3)
    w.complete_review(rF, F, 3)             # matching: settled without the orchestrator
    c = w.cases[q]
    assert c.challenge["resolved"] and c.challenge["by"] == "appeal reviewers"
    assert w.reviews[r1].status == "overturned"
    w.advance(17)
    assert c.state == "VESTED" and c.t_vest == 16
    n = nets(w)
    assert n["A"] == pytest.approx(23)      # court fee reimbursed from C's bond
    assert n["C"] == pytest.approx(-5)      # bond: 2 to A, 3 burned; costs reimbursed; no fee
    assert w.W(Ledger.OMEGA) == pytest.approx(302)       # the court fee is Ω's income; the loser bore it
    assert c.court_fee_reimbursed == pytest.approx(2)
    # E and F: emission 5 over weights 3 -> 2.5 each; fixed fees 3 each, Owed 6 > φ^F 5 -> scaled to 2.5 each
    assert w.reviews[rE].fee == pytest.approx(5.0) and w.reviews[rF].fee == pytest.approx(5.0)
    assert w.reviews[rE].fee_fixed == pytest.approx(2.5) and w.reviews[rE].fee_owed == pytest.approx(3)
    assert c.tree_closed and c.allowance_refunded == pytest.approx(1)   # 10 - 3 - 3 - 3
    assert w.W("H") - 100 == pytest.approx(-54)
    assert c.grade == PROCEDURAL
    assert w.actors["C"].p_audit == pytest.approx(1.0)   # p_start 1.0 doubled on the overturn, capped at p_cap = 1.0 (1.2.0 §2.4)


# ---------------------------------------------- §16 variant: pool exhaustion
def test_pool_exhaustion_withdrawal_before_deadline():
    w = make_world()
    q = w.post_root("H", 45)
    w.award(q, "A", 40, 8)
    w.advance(1)
    qn = w.post_nested(q, 6)                # nobody takes it
    w.spend("A", 12, q)
    w.advance(6)                             # T_wait = 5 elapsed at t=6, before the deadline at 8
    w.withdraw_pool_exhaustion(q, qn)
    c = w.cases[q]
    assert c.state == "FINAL_N" and c.I_pool and not c.I_N
    assert nets(w)["A"] == pytest.approx(-17)            # -12 spent, -5 (0.25 x 20) forfeited
    assert w.W("H") - 100 == pytest.approx(+5)           # escrow and unused deposit returned, plus the forfeiture
    assert w.cases[qn].state == "WITHDRAWN"
    assert w.ledger.wallet("A").L == pytest.approx(0)


def test_pool_exhaustion_unreachable_when_deadline_comes_first():
    w = make_world()
    q = w.post_root("H", 45)
    w.award(q, "A", 40, 4)                  # tau = 4: deadline at 4 < t_post(1) + T_wait(5)
    w.advance(1)
    qn = w.post_nested(q, 6)
    w.advance(5)                             # tick 4 processed: deadline missed -> ordinary final N
    c = w.cases[q]
    assert c.state == "FINAL_N" and c.I_N and not c.I_pool
    assert nets(w)["A"] == pytest.approx(-20)            # full forfeiture
    assert w.cases[qn].state == "WITHDRAWN"              # unawarded child withdrawn with the parent
    with pytest.raises(RuleError):
        w.withdraw_pool_exhaustion(q, qn)


# -------------------------------------------------- §16 variant: cancellation
def test_cancellation_before_submission_pays_kill_fee():
    w = make_world()
    q = w.post_root("H", 45)
    w.award(q, "A", 40, 8)
    w.advance(1)
    qn = w.post_nested(q, 6)
    w.award(qn, "B", 5, 3)
    w.advance(2)
    w.spend("B", 2, qn)
    w.cancel_nested(qn)                      # kill fee min(2, K=5) = 2 from escrow; 3 returned to A
    assert w.cases[qn].state == "CANCELLED"
    assert nets(w)["B"] == pytest.approx(0)
    assert w.actors["B"].committed is None
    assert w.ledger.wallet("A").L == pytest.approx(20)   # only the root guarantee remains locked
    assert w.cases[q].actor_cost == pytest.approx(2)     # the kill fee counts in A's cost
    w.advance(3)
    w.submit(q)                              # a cancelled child does not block the parent


def test_cancellation_unavailable_after_submission():
    w = make_world()
    q = w.post_root("H", 45)
    w.award(q, "A", 40, 8)
    w.advance(1)
    qn = w.post_nested(q, 6)
    w.award(qn, "B", 5, 3)
    w.advance(3)
    w.submit(qn)
    with pytest.raises(RuleError):
        w.cancel_nested(qn)


def test_kill_fee_exceeding_escrow_comes_from_unlocked_and_must_be_fundable():
    w = make_world()
    q = w.post_root("H", 45)
    w.award(q, "A", 40, 8)
    w.advance(1)
    qn = w.post_nested(q, 1)                 # beta' = 1
    w.award(qn, "B", 1, 3)                   # escrow 1
    w.advance(2)
    w.spend("B", 3, qn)                      # B overran: reimbursable cost 3 > escrow 1
    before_B = w.W("B")
    w.cancel_nested(qn)
    assert w.W("B") - before_B == pytest.approx(3)       # 1 from escrow + 2 from A's unlocked
    # affordability
    w2 = make_world()
    q2 = w2.post_root("H", 45)
    w2.award(q2, "A", 40, 8)
    w2.advance(1)
    qn2 = w2.post_nested(q2, 1)
    w2.award(qn2, "B", 1, 3)
    w2.advance(2)
    w2.spend("B", 3, qn2)
    w2.spend("A", w2.ledger.wallet("A").U - 0.5, q2)     # leave A with 0.5 unlocked
    with pytest.raises(RuleError):
        w2.cancel_nested(qn2)


# ------------------------------------- review 2, §2: nested rejection appeal
def test_nested_rejection_is_bonded_and_reimburses_the_appellant():
    w = make_world()
    q = w.post_root("H", 45)
    w.award(q, "A", 40, 20)                  # long root deadline: this test follows the nested case only
    w.advance(1)
    qn = w.post_nested(q, 6)
    w.award(qn, "B", 5, 3)
    w.spend("B", 3, qn)
    w.advance(3)
    w.submit(qn)
    w.judge_nested(qn, N)                    # A rejects; its rejection bond (5) stays locked
    assert w.ledger.wallet("A").L == pytest.approx(20 + 5)
    w.advance(4)
    w.respond(qn, "appeal")                  # B pays D=2
    rE = w.assign_appeal(qn, "E")
    rF = w.assign_appeal(qn, "F")
    w.advance(7)
    w.complete_review(rE, F, 3)
    w.complete_review(rF, F, 3)              # B wins: A's rejection overturned
    c = w.cases[qn]
    assert c.court_fee_reimbursed == pytest.approx(2)
    assert c.rejection_bond == 0 and w.ledger.wallet("A").L == pytest.approx(20)
    w.advance(14)
    assert c.state == "VESTED" and c.t_vest == 13
    assert nets(w)["B"] == pytest.approx(2)  # exactly as if accepted: 5 - 3, fee reimbursed
    assert w.W("A") == pytest.approx(50 - 5 - 5)         # paid B's price (5) and lost the bond (5)
    assert w.W(Ledger.OMEGA) == pytest.approx(302)
    assert w.actors["A"].o == 1
    # E and F were reimbursed from the ROOT's deposit (nested φ = 0)
    assert w.ledger.pool(q).deposit == pytest.approx(10 - 6)


# ------------------------------------- review 2, §1: shortfall and haircut
def test_shortfall_haircut_single_payout_rule():
    w = make_world(E0=6.0)                   # flat 6 so three surviving reviews (weight 4) get 1.5 per unit
    q = w.post_root("H", 45)
    w.award(q, "A", 40, 8)
    w.advance(1)
    w.submit(q)
    r1 = w.assign_initial(q, "C")
    w.advance(2)
    w.complete_review(r1, F, 5)              # deposit 10 -> 5
    w.advance(3)
    w.dispute(q, "H")                        # H pays D=2 -> Ω (now 22)
    rE = w.assign_appeal(q, "E")
    rF = w.assign_appeal(q, "F")
    w.advance(5)
    w.complete_review(rE, F, 5)              # deposit 5 -> 0
    w.complete_review(rF, F, 5)              # deposit empty: Ω advances 5 (22 -> 17)
    c = w.cases[q]
    assert c.omega_advance == pytest.approx(5)
    assert w.W(Ledger.OMEGA) == pytest.approx(297)
    assert c.challenge["resolved"] and c.outcome == F   # dispute rejected; all three verdicts stand
    w.advance(13)
    assert c.state == "VESTED" and c.t_vest == 12
    # 1.1.0: the allowance is spent, so Ω's advance cannot be repaid from it; the fee pot (5) pays
    # the fixed fees Owed = 2 + 3 + 3 = 8 scaled by 5/8 and has nothing left at closure, so the
    # advance stays unrecovered, borne by Ω; emission 6 over weight 4 is paid in full
    fees = {w.reviews[r].reviewer: w.reviews[r].fee for r in (r1, rE, rF)}
    assert fees["C"] == pytest.approx(2 * 5 / 8 + 1.5)
    assert fees["E"] == pytest.approx(3 * 5 / 8 + 2.25)
    assert fees["F"] == pytest.approx(3 * 5 / 8 + 2.25)
    assert sum(fees.values()) == pytest.approx(5 + 6)
    assert c.tree_closed and c.omega_advance == pytest.approx(5) and c.pot_refunded == 0
    assert w.W(Ledger.OMEGA) == pytest.approx(297)       # advance unrecovered; court fee kept
    assert c.grade == PROCEDURAL                         # the human disputed and lost
    assert any(a[1] == "H" and a[2] == N for a in c.assessments)
    assert w.W("H") - 100 == pytest.approx(-57)          # 40 + 10 + 5 paid in, the court fee 2, nothing came back


# ---------------------------------- review 2, §3: nominals frozen at award
def test_nominals_frozen_at_award_under_dilution():
    w = make_world(E0=10000.0)               # a huge flat emission so one vesting dilutes the credit
    q1 = w.post_root("H", 45)
    w.award(q1, "A", 40, 8)
    assert w.cases[q1].D == pytest.approx(2) and w.cases[q1].G_V == pytest.approx(5)
    w.advance(1)
    w.submit(q1)
    r1 = w.assign_initial(q1, "C")
    w.advance(2)
    w.complete_review(r1, F, 1)
    w.advance(13)                            # vests at 12, minting 10000 credits of emission
    v = w.ledger.v
    assert v < 0.6
    q2 = w.post_root("H", 25)
    w.award(q2, "B", 20, 8)                  # H's remaining 50 covers 20 + the indexed deposit
    c1, c2 = w.cases[q1], w.cases[q2]
    assert c1.D == pytest.approx(2) and c1.G_V == pytest.approx(5)     # unchanged after award
    assert c2.D == pytest.approx(2 / v) and c2.G_V == pytest.approx(5 / v)
    assert c2.G_V >= c2.D


# ------------------------- review 2, §4: timeouts, positions vs distinct actors
def test_timeout_replacement_positions_vs_distinct_reviewers():
    w = make_world()
    q = w.post_root("H", 45)
    w.award(q, "A", 40, 8)
    w.advance(1)
    w.submit(q)
    r1 = w.assign_initial(q, "C")            # deadline 6; C never completes
    w.advance(7)
    assert w.reviews[r1].status == "withdrawn"
    assert nets(w)["C"] == pytest.approx(-2.5)           # half the bond burned, no reimbursement
    assert "C" in w.cases[q].excluded
    r2 = w.assign_initial(q, "D")            # replacement: position vacated by C is reused
    w.advance(8)
    w.complete_review(r2, F, 2)
    w.advance(9)
    r3 = w.assign_audit(q, "E")
    w.advance(10)
    w.complete_review(r3, N, 2)              # audit disagrees: it stands as one appeal review
    r4 = w.assign_appeal(q, "F")
    w.advance(11)
    w.complete_review(r4, F, 2)              # split
    w.rule(q, F)
    c = w.cases[q]
    assert w.positions(q) == 3                           # positions on the challenge path
    assert w.distinct_reviewers(q) == 4                  # distinct actors over the case's lifetime
    assert w.reviews[r3].status == "overturned"
    w.advance(19)
    assert c.state == "VESTED" and c.t_vest == 18
    assert c.challenge["by"] == "orchestrator"


# ----------------------------------- review 2, §4: finality and suspension
def test_dispute_at_window_end_suspends_vesting_and_override_after_vesting_moves_no_money():
    w = make_world()
    q = w.post_root("H", 45)
    w.award(q, "A", 40, 8)
    w.advance(1)
    w.submit(q)
    r1 = w.assign_initial(q, "C")
    w.advance(2)
    w.complete_review(r1, F, 3)              # window to 12
    w.advance(12)
    w.dispute(q, "H")                        # filed at the window's last tick: admitted
    rE = w.assign_appeal(q, "E")
    rF = w.assign_appeal(q, "F")
    w.advance(13)
    assert w.cases[q].state == "PENDING" and w.cases[q].open_items == 1   # not vested at 12
    w.advance(14)
    w.complete_review(rE, F, 3)
    w.complete_review(rF, F, 3)
    w.advance(15)
    c = w.cases[q]
    assert c.state == "VESTED" and c.t_vest == 14        # max(window_end, resolution)
    wA = w.W("A")
    w.advance(20)
    w.override(q, "H", N)                    # after vesting
    assert c.outcome == N and c.grade == HUMAN
    assert c.corrective_obligation is not None
    assert w.W("A") == pytest.approx(wA)                 # no clawback
    w.advance(21)                            # invariants (I10) still hold


def test_override_before_vesting_is_the_ruling():
    w = make_world()
    q = w.post_root("H", 45)
    w.award(q, "A", 40, 8)
    w.advance(1)
    w.submit(q)
    r1 = w.assign_initial(q, "C")
    w.advance(2)
    w.complete_review(r1, F, 3)
    w.advance(5)
    w.override(q, "H", N)
    c = w.cases[q]
    assert c.state == "FINAL_N" and c.grade == HUMAN
    assert nets(w)["A"] == pytest.approx(-20)            # guarantee forfeited to H


def test_late_challenge_is_not_admitted():
    w = make_world()
    q = w.post_root("H", 45)
    w.award(q, "A", 40, 8)
    w.advance(1)
    w.submit(q)
    r1 = w.assign_initial(q, "C")
    w.advance(2)
    w.complete_review(r1, F, 3)
    w.advance(13)
    assert w.cases[q].state == "VESTED"
    with pytest.raises(RuleError):
        w.dispute(q, "H")


# ----------------------------------------- review 2, §5: money and the halt
def test_resource_purchase_is_value_neutral_and_emission_dilutes():
    w = make_world()
    v0 = w.ledger.v
    w.spend("A", 20)
    assert w.ledger.v == pytest.approx(v0)               # v' = v
    q = w.post_root("H", 45)
    w.award(q, "A", 40, 8)
    w.advance(1)
    w.submit(q)
    r1 = w.assign_initial(q, "C")
    w.advance(2)
    w.complete_review(r1, F, 1)
    w.advance(13)                            # emission minted at vesting
    assert w.ledger.v < v0


def test_reserve_exhaustion_is_a_halt_state_not_a_price():
    L = Ledger(Res0=100.0, v0=1.0)           # 100 backed credits in SPONSOR
    L.mint_emission_to_pool("x", 50.0)       # 50 unbacked credits: v falls to 2/3
    L.pay_from_fee_pool("x", "SPONSOR", 50.0)
    assert L.v == pytest.approx(100 / 150)
    prices = []
    while L.Res > 0:
        prices.append(1.0 / L.v)             # credit price of one real unit
        L.purchase("SPONSOR", min(L.Res, 10.0))
    assert len(set(round(p, 6) for p in prices)) == 1    # purchases never moved the price
    # the reserve and the supply exhaust together: dilution was spread over every holder
    assert L.halted and L.v == 0.0 and L.M == pytest.approx(0.0, abs=1e-6)
    L.mint_emission_to_pool("y", 10.0)       # emission after exhaustion: unbacked, worthless
    assert L.M == pytest.approx(10.0) and L.v == 0.0
    with pytest.raises(Exception):
        L.purchase("SPONSOR", 1.0)


# ------------------------------------------- review 2, table: initialization
def test_initialization_validity():
    p = Params()
    with pytest.raises(RuleError):
        World(p, [f"a{i}" for i in range(195)])          # 195 x 50 + 300 > 10000 (Ω₀ = 300 since 1.2.0)
    World(p, [f"a{i}" for i in range(194)])              # 194 x 50 + 300 = 10000 ok


def test_reserve_invariant_enforced_when_enabled():
    """1.2.0 §2.2: the reserve holds min(X_t, eligible). Started one short with free eligible actors,
    the first rotation seats the lowest-κ free actor and I9 holds; a reserve short of X_t while an
    eligible actor is free is what I9 fails on (asserted directly in test_v12)."""
    p = Params(E0=5.0, H=1e9, omega_rate=0.0)
    w = World(p, ACTORS, humans={"H": 100.0}, on_duty=["C", "D", "E"], enforce_reserve=True)
    w.advance(1)
    assert sum(1 for a in w.actors.values() if a.on_duty) == 4 and w.reserve_shortfall_now == 0
    next(a for a in w.actors.values() if a.on_duty).on_duty = False    # a reserve left short by hand, with a free actor
    with pytest.raises(InvariantError):
        check_all(w)


# ------------------------------------------- rule guards worth pinning down
def test_guards():
    w = make_world()
    q = w.post_root("H", 45)
    with pytest.raises(RuleError):
        w.award(q, "A", 46, 8)               # bid above beta
    with pytest.raises(RuleError):
        w.award(q, "C", 40, 8)               # on duty
    w.award(q, "A", 40, 8)
    with pytest.raises(RuleError):
        w.award(w.post_root("H", 10), "A", 10, 3)        # already committed
    w.advance(1)
    qn = w.post_nested(q, 6)
    w.award(qn, "B", 5, 3)
    with pytest.raises(RuleError):
        w.submit(q)                          # nested child has not reached its initial verdict
    w.advance(9)                             # A's deadline (8) missed at tick 8
    assert w.cases[q].state == "FINAL_N"
    with pytest.raises(RuleError):
        w.submit(q)


def test_bot_is_a_claim_evidence_resumes_same_reviewer():
    w = make_world()
    q = w.post_root("H", 45)
    w.award(q, "A", 40, 8)
    w.advance(1)
    w.submit(q)
    r1 = w.assign_initial(q, "C")
    w.advance(2)
    w.complete_review(r1, BOT, 2)
    assert w.cases[q].state == "AWAITING_RESPONSE"
    assert w.actors["C"].open_review == r1          # a ⊥ keeps the reviewer attached
    w.advance(3)
    w.respond(q, "supply_evidence")                  # window T_evid to resubmit
    assert w.cases[q].state == "RESUBMITTING"
    w.resubmit(q)
    assert w.reviews[r1].status == "open" and w.cases[q].state == "SUBMITTED"
    w.advance(4)
    w.complete_review(r1, F, 1)              # same assignment: one reimbursement cap
    assert w.reviews[r1].reimbursed == pytest.approx(3)  # 2 + 1 within K = 5
    assert w.actors["C"].open_review is None
    w.advance(15)
    assert w.cases[q].state == "VESTED"

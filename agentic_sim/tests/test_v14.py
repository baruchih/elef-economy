"""Design revision 4 — specification 1.4.0: the orchestrator's troops.

A rolled audit is an obligation of the case (§2.2): the driver rolls, the engine records, and the case
does not vest until an audit completes. A seat unfilled for w_R ticks, or a root request unawarded for
w_A ticks with no free fundable member, is taken by a troop summoned by the engine when the duty fund can
carry its cost and bond (§2.2, §2.3); the fund is the troop's wallet (§2.4) and pays uplift only from above
its reserve; a troop claims no emission or uplift, keeps no record, accepts every verdict on its own work at
the verdict, never touches a plant, and never audits the state's own work (§2.1, §2.3). I24, I25, and the
§6 figures: an audit seat nets the fund +3, a delivery +10 realised.
"""
import copy
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
try:
    import pytest
except ImportError:  # plain `python3 run_tests.py`
    sys.path.insert(0, os.path.dirname(__file__))
    from _mini_pytest import pytest

from sim import Params, World, RuleError, LedgerError, InvariantError, Ledger, check_all
from sim.engine import F, N, P, DUTY_FUND

ACTORS = ["A", "B", "C", "D", "E", "F"]
DUTY = ["C", "D", "E", "F"]


def make_world(budget=1000.0, actors=ACTORS, duty=DUTY, **over):
    # no emission, no service fee (the fund is seeded by hand where a test needs it), Ω 100, long turns
    kw = dict(E0=0.0, H=1e9, omega_rate=0.0, Omega0=100.0, duty_turn_reviews=10_000, duty_turn_ticks=100_000,
              service_clock=False, omega_backs_fund=False, seat_the_queue=False, panel_determined=False, reserve_periods=1,
              troop_account=False, duty_cap_frac=0.5)      # 1.7.0: the merged fund and the half cap of this revision
    kw.update(over)
    kw.setdefault("floating", False)   # 2.0.0: these are 1.x behaviours and figures — the backing, the reserves, the pay-in at award
    return World(Params(**kw), actors, humans={"H": budget}, on_duty=duty)


def seed_fund(w, amt):
    """The fund is fed by the raised tax at m > 1; a test seeds it directly from the sponsor."""
    w.ledger.transfer("SPONSOR", DUTY_FUND, amt, note="test: fund seeded")   # the engine's hook records the flow


def busy_all_duty(w):
    """Every duty actor holds an open review — of a good plant, which needs no awardee and which no troop
    ever touches: no market seat can be filled until these complete."""
    rids = []
    for aid in [a.id for a in w.actors.values() if a.on_duty and a.open_review is None]:
        qp = w.create_plant(True, 20.0)
        rids.append(w.assign_initial(qp, aid))
    return rids


def pending_case(w, actor="A", reviewer="C"):
    q = w.post_root("H", 20)
    w.award(q, actor, 20, 1)
    w.advance(w.t + 1)
    w.submit(q)
    r = w.assign_initial(q, reviewer)
    w.advance(w.t + 1)
    w.complete_review(r, F, 0)
    return q, r


# ------------------------------------------------------------ §2.2 the obligation
def test_a_rolled_audit_holds_the_case_until_an_audit_completes_and_is_admitted_after_the_window():
    w = make_world(troops=False)
    q, r = pending_case(w)
    before = w.cases[q].open_items
    w.roll_audit(q)
    c = w.cases[q]
    assert c.audit_obligation and c.audit_rolled_at == w.t and c.open_items == before + 1
    with pytest.raises(RuleError, match="already rolled"):
        w.roll_audit(q)
    w.advance(c.window_end + 3)                      # the window has closed: the case does not vest
    assert c.state == "PENDING" and not c.final
    a = w.assign_audit(q, "D")                       # admitted after the window for an obligation
    assert not c.audit_obligation and c.open_items == before + 1
    w.advance(w.t + 1)
    w.complete_review(a, F, 0)
    w.advance(w.t + 1)
    assert c.state == "VESTED"
    # refusals: on a plant, outside a pending F, after a human ruling
    qp = w.create_plant(True, 20.0)
    with pytest.raises(RuleError):
        w.roll_audit(qp)
    check_all(w)


def test_I25_catches_a_vested_case_with_an_obligation_outstanding():
    w = make_world(troops=False)
    q, r = pending_case(w)
    w.roll_audit(q)
    w.advance(w.cases[q].window_end + 1)
    c = w.cases[q]
    c.state, c.final, c.open_items, c.grade = "VESTED", True, 0, "protocol-default"   # vested by hand, obligation standing
    with pytest.raises(InvariantError, match="I25"):
        check_all(w)


# ------------------------------------------------------------ §2.2 summons for a seat
def test_an_audit_seat_unfilled_for_w_R_ticks_is_taken_by_a_troop_and_the_seat_nets_the_fund_three():
    w = make_world()
    seed_fund(w, 50.0)
    q, r = pending_case(w)                           # C approved; D, E, F free members
    busy_all_duty(w)                                 # ... now every duty actor holds a review
    w.roll_audit(q)
    t_roll = w.t
    w.advance(t_roll + 1)                            # waited 1 < w_R = 2: nothing yet
    assert not any(w.is_troop(w.reviews[x].reviewer) for x in w.cases[q].reviews)
    fund_before = w.W(DUTY_FUND)
    w.advance(t_roll + 2)                            # waited w_R: summoned at the seating step
    c = w.cases[q]
    troop_reviews = [w.reviews[x] for x in c.reviews if w.is_troop(w.reviews[x].reviewer)]
    assert len(troop_reviews) == 1 and troop_reviews[0].role == "audit" and not c.audit_obligation
    tr = troop_reviews[0]
    tid = tr.reviewer
    assert tid in w.troops and w.troops[tid]["kind"] == "review" and w.troops[tid]["t_release"] is None
    assert tr.cost == pytest.approx(3.0) and w.ledger.lock_record(tid, f"bond:{tr.id}") == pytest.approx(5.0)
    assert w.W(DUTY_FUND) == pytest.approx(fund_before - 3.0)     # the cost purchased; the bond is a lock
    with pytest.raises(RuleError, match="purchased from the fund at summons"):
        w.complete_review(tr.id, F, 2)               # a troop reports no further cost
    w.complete_review(tr.id, F, 0)                   # agrees: the audit stands
    assert w.troops[tid]["t_release"] == w.t
    out_before = w.fund_out
    w.advance(c.window_end + 1)
    assert c.state == "VESTED" and tr.status == "vested"
    assert tr.fee == pytest.approx(3.0) and tr.uplift == 0.0           # audit fee 1.5 f; no emission, no uplift
    # §6: the seat nets the fund +3 (−3 cost, +3 reimbursed, +3 fee); what the batch then paid out as uplift to the
    # market's reviewers — everything above the troops' reserve — is the fund doing its 1.3.0 job
    assert w.W(DUTY_FUND) + (w.fund_out - out_before) == pytest.approx(fund_before + 3.0)
    assert w.troop_summons_reviews == 1 and w.troop_ticks_reviews >= 1
    check_all(w)


def test_summons_refusals_are_whole_window_member_free_fund_short_and_the_states_own_audit():
    # a free eligible member: no summons however long the seat waits
    w = make_world()
    seed_fund(w, 50.0)
    q, r = pending_case(w)
    w.roll_audit(q)
    w.advance(w.t + 5)
    assert not w.troops and w.cases[q].audit_obligation
    # the fund cannot carry it, Ω's advance exhausted: counted, retried, nothing moved
    w2 = make_world(A_T=0.0)                         # the fund is empty and Ω advances nothing
    q2, r2 = pending_case(w2)
    busy_all_duty(w2)
    w2.roll_audit(q2)
    w2.advance(w2.t + 3)
    assert not w2.troops and w2.troop_shortfall_seats >= 1 and w2.troop_held_ticks >= 1 and w2.cases[q2].audit_obligation
    check_all(w2)
    # Ω's advance carries it when the fund is empty, and is repaid before any uplift
    w3 = make_world(A_T=100.0)
    q3, r3 = pending_case(w3)
    busy_all_duty(w3)
    w3.roll_audit(q3)
    w3.advance(w3.t + 2)
    assert len(w3.troops) == 1 and w3.advance_outstanding == pytest.approx(8.0)   # cost 3 + bond 5 advanced
    tr = next(w3.reviews[x] for x in w3.cases[q3].reviews if w3.is_troop(w3.reviews[x].reviewer))
    w3.complete_review(tr.id, F, 0)
    out_before = w3.fund_out
    w3.advance(w3.cases[q3].window_end + 1)
    assert w3.advance_outstanding < 1e-9                                # the advance was repaid before any uplift ...
    assert w3.W(DUTY_FUND) + (w3.fund_out - out_before) == pytest.approx(3.0)   # ... and the seat's +3 remained
    check_all(w3)


def test_troops_never_touch_a_plant_and_a_troop_cannot_be_assigned_by_hand():
    w = make_world()
    seed_fund(w, 50.0)
    busy_all_duty(w)
    qp = w.create_plant(False, 20.0)                 # a plant whose initial seat nobody is free to take
    w.advance(w.t + 4)
    assert not w.troops and w.cases[qp].state == "SUBMITTED"
    w2 = make_world()
    seed_fund(w2, 50.0)
    q, r = pending_case(w2)
    busy_all_duty(w2)
    w2.roll_audit(q)
    w2.advance(w2.t + 2)
    tid = next(iter(w2.troops))
    q3 = w2.post_root("H", 20)
    with pytest.raises(RuleError, match="troop"):
        w2.award(q3, tid, 20, 1)
    check_all(w2)


# ------------------------------------------------------------ §2.3 summons for an award
def test_a_request_unawarded_for_w_A_with_no_free_member_is_delivered_by_a_troop_at_the_market_price():
    w = make_world(omega_rate=0.05)
    seed_fund(w, 50.0)
    # a market price: one award to a member at 20
    q0 = w.post_root("H", 20)
    w.award(q0, "A", 20, 500)                        # A committed for a long time
    q1 = w.post_root("H", 20)
    w.award(q1, "B", 20, 500)                        # B too: no free member off duty remains
    q = w.post_root("H", 20)                         # nobody free to take it
    t_post = w.t
    w.advance(t_post + 1)
    assert w.cases[q].state == "AVAILABLE"
    fund_before = w.W(DUTY_FUND)
    w.advance(t_post + 2)                            # waited w_A = 2: summoned
    c = w.cases[q]
    assert c.state == "COMMITTED" and w.is_troop(c.actor) and c.troop_award and c.B == pytest.approx(20)
    tid = c.actor
    assert w.troops[tid]["kind"] == "delivery" and w.ledger.lock_record(tid, f"G:{q}") == pytest.approx(10)
    assert w.W(DUTY_FUND) == pytest.approx(fund_before - 10.0)         # c^D_T purchased; G is a lock
    assert w.ledger.pool(q).escrow == pytest.approx(20)                 # the requester paid in as for any award
    with pytest.raises(RuleError, match="never delegates"):
        w.post_nested(q, 5)
    w.advance(c.deadline)
    w.submit(q)
    r = w.assign_initial(q, "C")                     # a market reviewer; not the state's own audit
    w.advance(w.t + 1)
    w.complete_review(r, F, 0)
    assert not c.market_audit_only and w.audit_odds(q) == w.actors["C"].p_eff
    out_before = w.fund_out
    w.advance(c.window_end + 1)
    assert c.state == "VESTED" and w.troops[tid]["t_release"] == c.t_vest
    assert w.W(DUTY_FUND) + (w.fund_out - out_before) == pytest.approx(fund_before + 10.0)   # §6: price 20 − cost 10; m = 1: the tax is Ω's
    check_all(w)


def test_a_troop_accepts_every_verdict_at_the_verdict_and_a_request_below_the_market_waits():
    w = make_world()
    seed_fund(w, 50.0)
    q0 = w.post_root("H", 20)
    w.award(q0, "A", 20, 500)
    q1 = w.post_root("H", 20)
    w.award(q1, "B", 20, 500)
    q = w.post_root("H", 20)
    w.advance(w.t + 2)
    c = w.cases[q]
    tid = c.actor
    assert w.is_troop(tid)
    w.advance(c.deadline)
    w.submit(q)
    r = w.assign_initial(q, "C")
    w.advance(w.t + 1)
    w.complete_review(r, P, 0)                       # a P: the troop accepts N at the verdict, not the deadline
    assert c.state == "FINAL_N" and c.final and w.troops[tid]["t_release"] == w.t
    assert w.ledger.lock_record(tid, f"G:{q}") == 0.0                   # G forfeited to H; escrow returned
    with pytest.raises(RuleError):
        w.respond(q, "appeal", "x")
    # priced below the market: not a shortage — waits
    w.advance(w.t + 1)
    q2 = w.post_root("H", 10)
    w.advance(w.t + 5)
    assert w.cases[q2].state == "AVAILABLE" and w.cases[q2].actor is None
    check_all(w)


def test_the_states_own_work_is_audited_by_a_member_only_and_the_held_case_is_counted():
    w = make_world()
    seed_fund(w, 100.0)
    q0 = w.post_root("H", 20)
    w.award(q0, "A", 20, 500)
    q1 = w.post_root("H", 20)
    w.award(q1, "B", 20, 500)
    q = w.post_root("H", 20)
    w.advance(w.t + 2)                               # troop delivery summoned
    c = w.cases[q]
    assert w.is_troop(c.actor)
    w.advance(c.deadline)
    w.submit(q)
    rids = busy_all_duty(w)                          # no market reviewer free: the initial seat waits w_R
    w.advance(w.t + 2)
    tr = next(w.reviews[x] for x in c.reviews if w.is_troop(w.reviews[x].reviewer))
    assert tr.role == "initial"
    w.complete_review(tr.id, F, 0)                   # a troop approves the state's own work
    assert c.market_audit_only and c.audit_obligation and w.audit_odds(q) == 1.0
    w.advance(w.t + 4)                               # the members are still busy: no troop takes this seat
    assert not any(w.reviews[x].role == "audit" for x in c.reviews)
    assert w.held_market_audit_now == 1 and w.held_market_audit_max_age >= 2
    w.advance(w.t + 4)                               # the members' plant reviews time out: members come free
    member = next(a.id for a in w.actors.values() if a.on_duty and a.open_review is None and a.panel_eligible)
    a = w.assign_audit(q, member)
    w.advance(w.t + 1)
    w.complete_review(a, F, 0)
    w.advance(c.window_end + 1)
    assert c.state == "VESTED" and w.held_market_audit_now == 0
    check_all(w)


# ------------------------------------------------------------ §2.4 the fund's order
def test_uplift_is_paid_only_from_above_the_troops_reserve():
    w = make_world(omega_rate=0.05, period_plants=2, period_ticks=10_000, Omega0=1000.0)
    # the dial to m = 2: two bad plants approved
    for aid in ("C", "E"):
        qp = w.create_plant(False, 20.0)
        rp = w.assign_initial(qp, aid)
        w.advance(w.t + 1)
        w.complete_review(rp, F, 0)
    w.advance(w.t + 1)
    assert w.m_t == 2.0
    # a troop seat raises the reserve R_T to its capital (cost 3 + bond 5 = 8)
    q, r = pending_case(w, actor="A", reviewer="D")
    busy_all_duty(w)
    w.roll_audit(q)
    w.advance(w.t + 2)
    assert len(w.troops) == 1 and abs(w.R_T - 8.0) < 0.05               # cost 3 + the indexed bond ≈ 5
    tr = next(w.reviews[x] for x in w.cases[q].reviews if w.is_troop(w.reviews[x].reviewer))
    w.complete_review(tr.id, F, 0)
    # an award at m = 2 feeds the fund 1; the batch's uplift comes only from what sits above R_T
    q2 = w.post_root("H", 20)
    w.award(q2, "A", 20, 1)
    fund_before_batch = w.W(DUTY_FUND)
    w.advance(w.cases[q].window_end + 1)             # q vests: its surviving reviews settle; the troop's weight is excluded
    paid = w.fund_out
    assert paid <= max(0.0, fund_before_batch + 3.0 - w.R_T) + 1e-6   # +3 is the seat's own inflow that tick
    assert w.reviews[r].uplift >= 0.0 and tr.uplift == 0.0
    check_all(w)


# ------------------------------------------------------------ I24 catches
def test_I24_catches_a_troop_that_is_an_actor_or_holds_two_seats():
    w = make_world()
    seed_fund(w, 50.0)
    q, r = pending_case(w)
    busy_all_duty(w)
    w.roll_audit(q)
    w.advance(w.t + 2)
    tid = next(iter(w.troops))
    rec = w.troops[tid]
    saved = rec["case"]
    rec["case"] = w.create_plant(True, 20.0)         # recorded on a plant
    with pytest.raises(InvariantError, match="I24"):
        check_all(w)
    rec["case"] = saved
    check_all(w)

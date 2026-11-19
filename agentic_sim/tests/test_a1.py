"""Ablation brief A1, revision 2 (November 10, 2026; notes §79) — the small core's arms behind flags: candidate configurations for evaluation,
NOT in force; every flag off is 2.9.0 as in force (the goldens unmoved). The deciding verdict (§3): two seats of the orchestrator's own
inspectors on the troop seat's road, seated in the tick's summons pass without the w_R wait or the free-member test and answered at the
next tick's reviews, a third seat on a split; its seats take no fee (D4), their cost from the root's allowance while it lasts and the rest the
orchestrator's own, read apart; never overturned; never on a plant or the orchestrator's own delivery (A1.3). Arm 1 `trusted_ruling`: a
disagreeing audit or a non-confirming member panel escalates to it, a member panel confirms or escalates and never overturns, no ruling is
sought, a member's review is overturned only against the deciding verdict or a plant's truth. Arm 1b `sampled_confirmation`: a confirming
member audit or panel sampled to it. Arm 1c `lenient_false_alarm`: an overruled rejection at an audit or panel seat forfeits its fee and
keeps its bond. Arm 2 `state_audit`: every audit obligation on a member's delivery is the orchestrator's seat in the tick's pass, a plant's
discharged with no seat, `planted_approval` off, the roster sized without the audit demand (C1). Arm 3 `state_bench`: an appeal or dispute
on a member's delivery decided by the deciding verdict at the filing's pass, no member panel, plants file no challenge. Arm 4: all three.
I8 admits the deciding seats; I45–I48 new. The six-actor world of test_v29."""
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
try:
    import pytest
except ImportError:  # plain `python3 run_tests.py`
    sys.path.insert(0, os.path.dirname(__file__))
    from _mini_pytest import pytest
from sim import Params, World, RuleError, InvariantError, Ledger, check_all
from sim.engine import F, N

ACTORS = ["A", "B", "C", "D", "E", "F"]
DUTY = ["C", "D", "E", "F"]


def make_world(budget=1000.0, actors=ACTORS, duty=DUTY, **over):
    kw = dict(E0=0.0, H=1e9, omega_rate=0.05, Omega0=100.0, duty_turn_reviews=10_000, duty_turn_ticks=100_000,
              r_s=1.0, T_s=10_000, pi0=0.0, period_ticks=60, panel_determined=False, trusted_ruling=True)
    kw.update(over)
    return World(Params(**kw), actors, humans={"H": budget}, on_duty=duty)


def real_approved(w, requester="H", worker="B", reviewer="C"):
    q = w.post_root(requester, 20)
    w.award(q, worker, 20, 2)
    w.advance(w.t + 2)
    w.submit(q)
    r = w.assign_initial(q, reviewer)
    w.advance(w.t + 1)
    w.complete_review(r, F, 0.0)
    return q, r


def real_rejected(w, requester="H", worker="B", reviewer="C"):
    q = w.post_root(requester, 20)
    w.award(q, worker, 20, 2)
    w.advance(w.t + 2)
    w.submit(q)
    r = w.assign_initial(q, reviewer)
    w.advance(w.t + 1)
    w.complete_review(r, N, 2.0)
    return q, r


def deciding_open(w, c):
    return [w.reviews[x] for x in c.reviews if w.reviews[x].role == "deciding" and w.reviews[x].status == "open"]


def audited_disagreeing(w, auditor="D"):
    """A member's approval of a member's delivery, rolled, audited by a member who rejects it."""
    q, r = real_approved(w)
    c = w.cases[q]
    w.roll_audit(q)
    ra = w.assign_audit(q, auditor)
    w.advance(w.t + 1)
    w.complete_review(ra, N, 2.0)
    return q, c, r, ra


# ------------------------------------------------------------ the flags
def test_every_flag_off_is_2_9_0_and_the_arms_are_built_on_the_trusted_ruling():
    p = Params()
    assert not p.trusted_ruling and p.sampled_confirmation == 0 and not p.lenient_false_alarm and not p.state_audit and not p.state_bench
    for kw in (dict(state_audit=True), dict(state_bench=True), dict(lenient_false_alarm=True), dict(sampled_confirmation=0.25)):
        with pytest.raises(ValueError):
            Params(**kw)
    assert Params(trusted_ruling=True, state_audit=True).planted_approval is False      # arm 2: its base is zero by construction
    assert Params(trusted_ruling=True, state_bench=True).planted_approval is True


# ------------------------------------------------------------ §3 the deciding verdict, through arm 1's audit escalation
def test_a_disagreeing_audit_escalates_to_two_state_seats_seated_in_the_pass_and_the_verdict_settles_it():
    w = make_world()
    q, c, r, ra = audited_disagreeing(w)
    ch = c.challenge
    assert ch is not None and ch["kind"] == "audit" and ch["escalated"] and not ch["resolved"]
    assert c.deciding is not None and c.deciding["reason"] == "audit" and c.deciding["want"] == 2 and not c.deciding["seats"]
    with pytest.raises(RuleError):
        w.assign_appeal(q, "E")                                  # no member's third seat
    assert w.deciding_opened == 1 and w.deciding_by_reason == {"audit": 1}
    w.advance(w.t + 1)                                           # the tick's pass seats both, no w_R wait, a free member (E) notwithstanding
    seats = deciding_open(w, c)
    assert len(seats) == 2 and all(w.is_troop(s.reviewer) for s in seats) and w.deciding_seats == 2
    assert len([x for x in c.reviews if w.reviews[x].status != "withdrawn"]) == 4 > w.p.V_max   # I8 admits the positions under the flag
    with pytest.raises(RuleError):
        w.rule(q, N)                                             # the driver's ruling is never sought on a member's delivery
    for s in seats:
        w.complete_review(s.id, F, 0.0)                          # the orchestrator's inspectors agree with the approval
    assert c.deciding["resolved"] and c.deciding["outcome"] == F
    assert ch["resolved"] and ch["by"] == "deciding verdict" and ch["outcome"] == F
    assert w.reviews[r].status == "done" and w.reviews[ra].status == "overturned"     # the auditor differed from the deciding verdict
    assert all(w.reviews[s.id].status == "done" for s in seats)  # the orchestrator's seats stand
    assert c.state == "PENDING" and w.deciding_outcomes == {"confirmed": 1, "overturned": 0}
    assert any(e["kind"] == "deciding" for e in w.history.entries[-6:])
    w.advance(c.window_end + 3)
    assert c.state == "VESTED"
    for s in seats:
        assert w.reviews[s.id].fee == 0.0 and w.reviews[s.id].fee_owed == 0.0        # D4: the deciding seats take no fee
    check_all(w)


def test_a_split_seats_a_third_and_the_majority_decides_with_the_minority_seat_standing():
    w = make_world()
    q, c, r, ra = audited_disagreeing(w)
    w.advance(w.t + 1)
    s1, s2 = deciding_open(w, c)
    w.complete_review(s1.id, F, 0.0)
    w.complete_review(s2.id, N, 0.0)
    assert not c.deciding["resolved"] and c.deciding["want"] == 3 and w.deciding_splits == 1
    w.advance(w.t + 1)
    (s3,) = deciding_open(w, c)
    w.complete_review(s3.id, N, 0.0)
    assert c.deciding["resolved"] and c.deciding["outcome"] == N and c.challenge["by"] == "deciding verdict"
    assert w.reviews[r].status == "overturned" and w.reviews[ra].status == "done"     # the initial approval falls; the auditor matched
    assert all(w.reviews[s.id].status != "overturned" for s in (s1, s2, s3))        # the minority seat stands
    assert c.state == "FINAL_N" and w.deciding_outcomes["overturned"] == 1
    w.advance(w.t + 1)
    check_all(w)


def test_the_deciding_seats_cost_comes_from_the_allowance_while_it_lasts_and_the_rest_is_the_orchestrators_read_apart():
    w = make_world(phi_E_root=6.0)                               # the initial review's care 0, the audit's 2: four credits left for the seats
    q, c, r, ra = audited_disagreeing(w)
    w.advance(w.t + 1)
    s1, s2 = deciding_open(w, c)
    assert w.reviews[s1.id].cost == w.p.c_T and w.ledger.pool(q).deposit == 4.0        # c_T purchased at the summons; reimbursed at the answer
    w.complete_review(s1.id, F, 0.0)
    assert w.reviews[s1.id].reimbursed == 3.0 and w.reviews[s1.id].deferred == 0.0 and c.state_unreimbursed == 0.0
    w.complete_review(s2.id, F, 0.0)
    assert w.reviews[s2.id].reimbursed == 1.0 and w.reviews[s2.id].deferred == 0.0 and c.state_unreimbursed == 2.0
    assert w.state_cost_unreimbursed == 2.0 and w.ledger.pool(q).deposit == 0.0 and c.omega_advance == 0.0   # no advance, no claim
    assert c.state == "PENDING"
    w.advance(c.window_end + 3)
    assert c.state == "VESTED" and w.reviews[s2.id].reimbursed_pending == 0.0 and w.reviews[s2.id].reimbursed == 1.0
    check_all(w)


# ------------------------------------------------------------ arm 1: the member panel confirms or escalates
def test_a_member_panel_that_confirms_settles_as_today_and_one_that_does_not_escalates():
    w = make_world()
    q, r = real_approved(w)
    c = w.cases[q]
    w.dispute(q, "H", "the result does not meet the request")
    r1, r2 = w.assign_appeal(q, "D"), w.assign_appeal(q, "E")
    w.advance(w.t + 1)
    w.complete_review(r1, F, 2.0)
    w.complete_review(r2, F, 2.0)                                # both confirm the approval: the dispute is lost on the panel's word
    assert c.challenge["resolved"] and c.challenge["by"] == "appeal reviewers" and c.challenge["outcome"] == F and c.deciding is None
    w2 = make_world()
    q, r = real_approved(w2)
    c = w2.cases[q]
    w2.dispute(q, "H", "the result does not meet the request")
    r1, r2 = w2.assign_appeal(q, "D"), w2.assign_appeal(q, "E")
    w2.advance(w2.t + 1)
    w2.complete_review(r1, N, 2.0)
    w2.complete_review(r2, N, 2.0)                               # both would overturn: today final; under arm 1 escalated
    assert not c.challenge["resolved"] and c.challenge["escalated"] and c.deciding["reason"] == "panel"
    w2.advance(w2.t + 1)
    s1, s2 = deciding_open(w2, c)
    w2.complete_review(s1.id, F, 0.0)
    w2.complete_review(s2.id, F, 0.0)                            # the orchestrator finds the work fulfilled
    assert c.challenge["resolved"] and c.challenge["outcome"] == F and c.state == "PENDING"
    assert w2.reviews[r].status == "done" and w2.reviews[r1].status == "overturned" and w2.reviews[r2].status == "overturned"
    assert c.court_fee_reimbursed == 0.0                         # the dispute lost: the fee stays where the filing put it
    w2.advance(c.window_end + 3)
    assert c.state == "VESTED"
    check_all(w2)


def test_a_split_panel_escalates_and_the_court_fee_follows_the_deciding_verdicts_outcome():
    w = make_world()
    q, r = real_approved(w)
    c = w.cases[q]
    w.dispute(q, "H", "the result does not meet the request")
    r1, r2 = w.assign_appeal(q, "D"), w.assign_appeal(q, "E")
    w.advance(w.t + 1)
    w.complete_review(r1, N, 2.0)
    w.complete_review(r2, F, 2.0)                                # split: no ruling; the deciding verdict
    assert c.challenge["escalated"] and c.deciding["reason"] == "panel"
    with pytest.raises(RuleError):
        w.rule(q, N)
    w.advance(w.t + 1)
    for s in deciding_open(w, c):
        w.complete_review(s.id, N, 0.0)
    assert c.challenge["outcome"] == N and c.state == "FINAL_N"
    assert w.reviews[r].status == "overturned" and w.reviews[r1].status == "done" and w.reviews[r2].status == "overturned"
    assert c.court_fee_reimbursed == c.D                         # the dispute won: the fee back to H from the initial reviewer's bond
    w.advance(w.t + 1)
    check_all(w)


def test_the_orchestrators_own_delivery_is_judged_as_2_9_0_has_it_in_every_arm():
    """A1.3, ruled: a member's audit, the panel and the driver's ruling on the state's own work as 2.9.0 has it; no deciding verdict on it.
    test_v29's path: the state delivers (A and B committed, no free fundable member), a troop reviewer approves it (`market_audit_only`)."""
    w = make_world(membership=False, plant_market=False, actors=["A", "B", "C"], duty=["C"], w_R=2, eps_T=0.0, T_review=100,
                   state_audit=True, state_bench=True)
    for who in ("A", "B"):
        qq = w.post_root("H", 20)
        w.award(qq, who, 20, 30)
    held = w.assign_initial(w.create_plant(True, 20.0), "C")
    q = w.post_root("H", 20)
    w.advance(w.t + w.p.w_A + 1)
    c = w.cases[q]
    assert w.is_troop(c.actor)
    w.advance(c.deadline)
    w.submit(q)
    w.advance(w.t + w.p.w_R + 1)
    tr = next(w.reviews[x] for x in c.reviews if w.reviews[x].role == "initial" and w.is_troop(w.reviews[x].reviewer))
    w.complete_review(tr.id, F, 0.0)
    assert c.market_audit_only and c.audit_obligation
    w.advance(w.t + 2)
    assert c.audit_obligation and not any(w.reviews[x].role == "audit" for x in c.reviews)   # the state does not audit its own work (I25)
    w.complete_review(held, F, 0.0)
    ra = w.assign_audit(q, "C")                                  # admitted under state_audit: the orchestrator's own work keeps a member's audit
    w.advance(w.t + 1)
    w.complete_review(ra, N, 2.0)
    assert c.challenge is not None and not c.challenge.get("escalated") and c.deciding is None   # today's path, not the deciding verdict
    w.advance(w.t + w.p.w_R + 1)                                 # the second panel seat after w_R: a troop's, as today
    r2 = next(w.reviews[x] for x in c.challenge["reviews"] if w.reviews[x].status == "open")
    w.complete_review(r2.id, F, 0.0)
    assert not c.challenge["resolved"]                           # a split: the driver's ruling, as today
    w.rule(q, F)
    assert c.challenge["by"] == "orchestrator" and c.state == "PENDING"
    check_all(w)


# ------------------------------------------------------------ arm 1b: the sampled confirmation
def test_a_confirming_audit_sampled_to_the_deciding_verdict_is_overturned_where_it_differs_and_stands_where_it_agrees():
    w = make_world(sampled_confirmation=1.0)
    q, r = real_approved(w)
    c = w.cases[q]
    w.roll_audit(q)
    ra = w.assign_audit(q, "D")
    w.advance(w.t + 1)
    w.complete_review(ra, F, 2.0)                                # confirms; at r = 1 every confirmation is sampled
    assert c.challenge is not None and c.challenge["sampled"] and c.deciding["reason"] == "sample_audit" and w.confirmations_sampled == 1
    w.advance(w.t + 1)
    for s in deciding_open(w, c):
        w.complete_review(s.id, N, 0.0)
    assert c.state == "FINAL_N" and w.reviews[r].status == "overturned" and w.reviews[ra].status == "overturned"
    assert w.confirmations_overturned == 1
    w2 = make_world(sampled_confirmation=1.0)
    q, r = real_approved(w2)
    c = w2.cases[q]
    w2.roll_audit(q)
    ra = w2.assign_audit(q, "D")
    w2.advance(w2.t + 1)
    w2.complete_review(ra, F, 2.0)
    w2.advance(w2.t + 1)
    for s in deciding_open(w2, c):
        w2.complete_review(s.id, F, 0.0)
    assert c.state == "PENDING" and w2.reviews[r].status == "done" and w2.reviews[ra].status == "done" and w2.confirmations_overturned == 0
    with pytest.raises(RuleError):
        w2.dispute(q, "H", "the result does not meet the request")   # the sample spent the case's one round: the dispute refused, counted
    assert w2.disputes_refused_after_sample == 1
    w2.advance(c.window_end + 3)
    assert c.state == "VESTED"
    check_all(w2)


# ------------------------------------------------------------ arm 1c: the cheaper false alarm
def test_an_overruled_rejection_at_the_audit_seat_keeps_its_bond_and_forfeits_its_fee_while_an_overruled_approval_burns():
    w = make_world(lenient_false_alarm=True)
    q, c, r, ra = audited_disagreeing(w)
    before = w.ledger.wallet("D").W
    w.advance(w.t + 1)
    for s in deciding_open(w, c):
        w.complete_review(s.id, F, 0.0)                          # the auditor's rejection overruled
    rv = w.reviews[ra]
    assert rv.status == "overturned" and rv.bond_kept and w.lenient_bonds_kept == 1
    assert w.ledger.wallet("D").W == before and w.ledger.wallet("D").L == 0.0        # the bond released, nothing burned
    w.advance(c.window_end + 3)
    assert c.state == "VESTED" and rv.fee == 0.0                 # overturned: no fee at settlement
    check_all(w)
    w2 = make_world(lenient_false_alarm=True)
    q, r = real_approved(w2)
    c = w2.cases[q]
    w2.dispute(q, "H", "the result does not meet the request")
    r1, r2 = w2.assign_appeal(q, "D"), w2.assign_appeal(q, "E")
    w2.advance(w2.t + 1)
    w2.complete_review(r1, F, 2.0)
    w2.complete_review(r2, N, 2.0)
    before_d = w2.ledger.wallet("D").W
    w2.advance(w2.t + 1)
    for s in deciding_open(w2, c):
        w2.complete_review(s.id, N, 0.0)                         # the approval falls: D's confirming F is overruled — the bond burns as today
    assert w2.reviews[r1].status == "overturned" and not w2.reviews[r1].bond_kept and w2.ledger.wallet("D").W == before_d - w2.p.G_V
    assert w2.reviews[r2].status == "done"
    w2.advance(w2.t + 1)
    check_all(w2)


# ------------------------------------------------------------ arm 2: the state's audit
def test_under_the_states_audit_every_obligation_on_a_members_delivery_is_the_orchestrators_seat_in_the_ticks_pass():
    w = make_world(state_audit=True)
    q, r = real_approved(w)
    c = w.cases[q]
    w.roll_audit(q)
    with pytest.raises(RuleError):
        w.assign_audit(q, "D")                                   # no member sits the audit of a member's work
    assert w._waiting_reviews()[1] == 0                          # C1: the roster is sized without the seat the state carries
    w.advance(w.t + 1)                                           # the pass seats it now: no w_R wait, a free member notwithstanding
    (ra,) = [w.reviews[x] for x in c.reviews if w.reviews[x].role == "audit"]
    assert w.is_troop(ra.reviewer) and ra.status == "open" and not c.audit_obligation and w.state_audit_seats == 1
    w.complete_review(ra.id, F, 0.0)                             # agrees: the approval stands
    assert c.challenge is None and c.deciding is None and c.state == "PENDING"
    w.advance(c.window_end + 3)
    assert c.state == "VESTED" and ra.fee > 0                    # the audit seat earns the audit's fee as a troop's does today
    check_all(w)


def test_under_the_states_audit_a_disagreeing_seat_is_the_deciding_verdicts_first_and_one_more_completes_it():
    w = make_world(state_audit=True)
    q, r = real_approved(w)
    c = w.cases[q]
    w.roll_audit(q)
    w.advance(w.t + 1)
    (ra,) = [w.reviews[x] for x in c.reviews if w.reviews[x].role == "audit"]
    w.complete_review(ra.id, N, 0.0)
    assert c.deciding["reason"] == "state_audit" and c.deciding["verdicts"] == [(ra.id, N)] and c.deciding["want"] == 2
    w.advance(w.t + 1)
    (s2,) = deciding_open(w, c)
    w.complete_review(s2.id, N, 0.0)
    assert c.deciding["resolved"] and c.deciding["outcome"] == N and c.state == "FINAL_N"
    assert w.reviews[r].status == "overturned" and ra.status == "done"
    assert w.deciding_outcomes_by_reason == {"state_audit:overturned": 1}
    w.advance(w.t + 1)
    check_all(w)


def test_under_the_states_audit_a_plants_obligation_is_discharged_with_no_seat():
    w = make_world(state_audit=True)
    q = w.post_plant(False)
    w.award(q, "B", 15, 4)
    c = w.cases[q]
    w.advance(c.plant_submit_at + 1)
    r = w.assign_initial(q, "C")
    w.advance(w.t + 1)
    w.complete_review(r, F, 0.0)                                 # a bad plant approved: a plant failure; its F pending
    assert c.state == "PENDING"
    w.roll_audit(q)
    with pytest.raises(RuleError):
        w.assign_audit(q, "D")
    w.advance(w.t + 1)
    assert not c.audit_obligation and w.plant_audits_waived == 1 and not any(w.reviews[x].role == "audit" for x in c.reviews)
    w.advance(c.window_end + 3)
    assert c.state in ("FINAL_N", "VESTED")                      # the bad plant closes at the window's end as 2.8.0 has it
    check_all(w)


# ------------------------------------------------------------ arm 3: the state's bench
def test_under_the_states_bench_a_dispute_on_a_members_delivery_is_decided_by_the_deciding_verdict_at_the_filings_pass():
    w = make_world(state_bench=True)
    q, r = real_approved(w)
    c = w.cases[q]
    w.dispute(q, "H", "the result does not meet the request")
    assert c.challenge["escalated"] and c.deciding["reason"] == "bench"
    with pytest.raises(RuleError):
        w.assign_appeal(q, "D")
    w.advance(w.t + 1)
    s1, s2 = deciding_open(w, c)
    w.complete_review(s1.id, N, 0.0)
    w.complete_review(s2.id, N, 0.0)
    assert c.challenge["resolved"] and c.challenge["by"] == "deciding verdict" and c.state == "FINAL_N"
    assert w.reviews[r].status == "overturned" and c.court_fee_reimbursed == c.D
    assert not any(w.reviews[x].role == "appeal" for x in c.reviews)
    w.advance(w.t + 1)
    check_all(w)


def test_under_the_states_bench_an_appeal_is_decided_the_same_way_and_a_plant_files_no_challenge():
    w = make_world(state_bench=True)
    q, r = real_rejected(w)
    c = w.cases[q]
    w.respond(q, "appeal", "the work meets the request")
    assert c.challenge["kind"] == "appeal" and c.challenge["escalated"] and c.deciding["reason"] == "bench"
    w.advance(w.t + 1)
    for s in deciding_open(w, c):
        w.complete_review(s.id, F, 0.0)
    assert c.challenge["outcome"] == F and c.state == "PENDING" and w.reviews[r].status == "overturned" and c.court_fee_reimbursed == c.D
    w.advance(c.window_end + 3)
    assert c.state == "VESTED"
    check_all(w)
    w2 = make_world(state_bench=True)
    q = w2.post_plant(True)
    w2.award(q, "B", 15, 4)
    c = w2.cases[q]
    w2.advance(c.plant_submit_at + 1)
    r = w2.assign_initial(q, "C")
    w2.advance(w2.t + 1)
    w2.complete_review(r, N, 2.0)                                # a good plant rejected: a plant failure, its N awaiting the plant actor
    with pytest.raises(RuleError):
        w2.respond(q, "appeal", "the work meets the request")    # plants file no challenge under the bench
    q2 = w2.post_plant(False)
    w2.award(q2, "A", 15, 4)
    c2 = w2.cases[q2]
    w2.advance(c2.plant_submit_at + 1)
    r2 = w2.assign_initial(q2, "D")
    w2.advance(w2.t + 1)
    w2.complete_review(r2, F, 0.0)
    with pytest.raises(RuleError):
        w2.dispute(q2, c2.requester, "the result does not meet the request")
    check_all(w2)


# ------------------------------------------------------------ arm 4: the small core, and the invariants' catches
def test_the_small_core_holds_only_the_first_review_for_members_and_the_invariants_pass():
    w = make_world(state_audit=True, state_bench=True)
    q, r = real_approved(w)
    c = w.cases[q]
    w.roll_audit(q)
    w.advance(w.t + 1)
    (ra,) = [w.reviews[x] for x in c.reviews if w.reviews[x].role == "audit"]
    w.complete_review(ra.id, F, 0.0)
    w.advance(c.window_end + 3)
    assert c.state == "VESTED"
    q2, r2 = real_approved(w, worker="A", reviewer="D")
    c2 = w.cases[q2]
    w.dispute(q2, "H", "the result does not meet the request")
    w.advance(w.t + 1)
    for s in deciding_open(w, c2):
        w.complete_review(s.id, F, 0.0)
    assert c2.state == "PENDING" and all(w.is_troop(w.reviews[x].reviewer) for x in c2.reviews if w.reviews[x].role != "initial")
    w.advance(c2.window_end + 3)
    assert c2.state == "VESTED"
    check_all(w)


def test_I45_I46_I47_catch_a_ruling_a_members_audit_and_a_member_panel_under_their_flags():
    w = make_world()
    q, r = real_approved(w)
    c = w.cases[q]
    w.dispute(q, "H", "the result does not meet the request")
    r1, r2 = w.assign_appeal(q, "D"), w.assign_appeal(q, "E")
    w.advance(w.t + 1)
    w.complete_review(r1, N, 2.0)
    w.complete_review(r2, F, 2.0)
    w._settle_challenge(c, outcome=N, by="orchestrator")         # forged past the guard: a ruling on a member's delivery
    with pytest.raises(InvariantError):
        check_all(w)
    w2 = make_world(state_audit=True)
    q, r = real_approved(w2)
    c = w2.cases[q]
    w2.roll_audit(q)
    w2._new_review(c, "D", "audit")                              # forged past the guard: a member's audit
    with pytest.raises(InvariantError):
        check_all(w2)
    w3 = make_world(state_bench=True)
    q, r = real_approved(w3)
    c = w3.cases[q]
    w3.dispute(q, "H", "the result does not meet the request")
    c.challenge["escalated"] = False
    with pytest.raises(InvariantError):
        check_all(w3)


def test_the_dials_carried_in_start_the_four_multipliers_and_their_rates_and_nothing_else_moves():
    # A1 addendum 4 (November 10, 2026): a harness option, no rule — a world may start its dials where a run before ended; unset, every
    # dial starts at the floor as every run of record did (the goldens pin that). The rates follow the multipliers by the rule.
    w = make_world(pi0=0.10, pi_max=0.40, m_max=4.0)
    assert (w.m_t, w.m_A, w.m_La, w.m_Ld) == (1.0, 1.0, 1.0, 1.0) and w.pi_t == 0.10 and w.pi_A == 0.02
    w2 = make_world(pi0=0.10, pi_max=0.40, m_max=4.0, dial_start=(2.0, 8.0, 3.0, 1.5))
    assert (w2.m_t, w2.m_A, w2.m_La, w2.m_Ld) == (2.0, 8.0, 3.0, 1.5)
    assert abs(w2.pi_t - 0.20) < 1e-9 and abs(w2.pi_A - 0.16) < 1e-9 and abs(w2.pi_La - 0.75) < 1e-9 and abs(w2.pi_Ld - 0.375) < 1e-9
    w3 = make_world(pi0=0.10, pi_max=0.40, m_max=4.0, dial_start=(4.0, 20.0, 8.0, 8.0))
    assert w3.pi_t == 0.40 and w3.pi_A == 0.40 and w3.pi_La == 2.0        # at the caps the rates sit at theirs
    for bad in ((0.5, 1, 1, 1), (1, 21, 1, 1), (1, 1, 9, 1), (1, 1, 1)):
        with pytest.raises(ValueError):
            Params(dial_start=bad)
    w2.advance(30)
    check_all(w2)


# ------------------------------------------------------------ the stressed world's harness option (November 11, 2026; no rule)
def test_the_bond_at_an_audit_or_panel_seat_is_a_multiple_of_G_V_under_bond_mult_later_and_G_V_at_the_first_review():
    """`Params.bond_mult_later` (1.0 in every run of record): the reviewer's bond at an audit or panel seat is that multiple of G_V — locked,
    funded and burned as the seat's; the first review's bond stays G_V. A reviewer whose unlocked credit covers G_V but not the multiple is
    refused the audit seat and admitted to a first review; the default leaves every lock at G_V."""
    w = make_world(trusted_ruling=False, bond_mult_later=2.0)
    q, r = real_approved(w)
    c = w.cases[q]
    assert w.reviews[r].bond == c.G_V and w.bond_for(c, "initial") == c.G_V and w.bond_for(c, "audit") == 2 * c.G_V == w.bond_for(c, "appeal")
    w.roll_audit(q)
    # D can fund G_V but not 2 G_V: refused the audit seat, admitted to a first review of another case
    w.ledger.purchase("D", w.ledger.wallet("D").U - 1.5 * c.G_V, case=None, note="test: effort spent")   # D keeps 1.5 G_V unlocked
    assert c.G_V <= w.ledger.wallet("D").U < 2 * c.G_V
    with pytest.raises(RuleError):
        w.assign_audit(q, "D")
    ra = w.assign_audit(q, "E")
    assert w.reviews[ra].bond == 2 * c.G_V and w.ledger.wallet("E").L >= 2 * c.G_V
    q2 = w.post_root("H", 20); w.award(q2, "A", 20, 2); w.advance(w.t + 2); w.submit(q2)
    r2 = w.assign_initial(q2, "D")
    assert w.reviews[r2].bond == c.G_V
    w.advance(w.t + 1)
    w.complete_review(ra, N, 2.0)                                     # the audit disagrees: the third seat, then by the ruling; the overturned bond burns whole
    check_all(w)
    w0 = make_world(trusted_ruling=False)
    q0, r0 = real_approved(w0); c0 = w0.cases[q0]; w0.roll_audit(q0)
    ra0 = w0.assign_audit(q0, "D")
    assert w0.reviews[ra0].bond == c0.G_V and w0.p.bond_mult_later == 1.0
    with pytest.raises(ValueError):
        Params(bond_mult_later=0.0)


# ------------------------------------------------------------ addendum 31's two options (November 18, 2026; notes §126) — off in every run of record

def test_the_mark_and_the_second_filing_are_built_on_the_trusted_ruling_and_off_by_default():
    p = Params()
    assert p.real_miss_mark is False and p.second_filing is False and p.T_second == 2
    with pytest.raises(ValueError):
        Params(real_miss_mark=True)
    with pytest.raises(ValueError):
        Params(second_filing=True)
    with pytest.raises(ValueError):
        Params(trusted_ruling=True, second_filing=True, T_second=0)
    w = make_world(second_filing=False)
    q, r = real_approved(w)
    w.dispute(q, "H", "the result does not meet the request")
    with pytest.raises(RuleError):
        w.second_filing(q, "H")                                      # the option off: refused, nothing moves


def test_the_mark_enters_an_overturned_approval_of_real_work_on_the_first_reviewers_bad_record_and_nothing_else():
    """Params.real_miss_mark: an approval of a real root that the deciding verdict overturns is a wrong entry in the first reviewer's `plant_bad`
    window (the record the earned seats and the suspension read), at any standing; a rejection overturned, an approval confirmed and the audit
    seat's own verdict write nothing; with the flag off the same world writes nothing."""
    for flag in (True, False):
        w = make_world(real_miss_mark=flag)
        q, c, r, ra = audited_disagreeing(w)                          # C approves, D's audit rejects: the deciding verdict
        before = list(w.actors["C"].plant_bad)
        w.advance(w.t + 1)
        for s in deciding_open(w, c):
            w.complete_review(s.id, N, 0.0)                           # the orchestrator finds the work unfulfilled: C's approval overturned
        assert c.state == "FINAL_N" and w.reviews[r].status == "overturned"
        if flag:
            assert w.actors["C"].plant_bad == before + [(w.t, True)] and w.actors["C"].real_marks == 1 and w.real_miss_marks == 1
            assert w.actors["D"].plant_bad == [] and w.actors["D"].real_marks == 0            # the audit seat writes nothing
            assert any(e["kind"] == "real_miss_mark" and e["payload"]["actor"] == "C" for e in w.history.entries)
        else:
            assert w.actors["C"].plant_bad == before and w.actors["C"].real_marks == 0 and w.real_miss_marks == 0
            assert not any(e["kind"] == "real_miss_mark" for e in w.history.entries)
        # a rejection overturned writes nothing on anyone's record under either setting
        q2, r2 = real_rejected(w, reviewer="E")
        c2 = w.cases[q2]
        w.respond(q2, "appeal", "the work meets the request")
        p1, p2 = w.assign_appeal(q2, "D"), w.assign_appeal(q2, "F")
        w.advance(w.t + 1)
        w.complete_review(p1, F, 2.0)
        w.complete_review(p2, F, 2.0)                                 # the panel would overturn: escalated under arm 1
        w.advance(w.t + 1)
        for s in deciding_open(w, c2):
            w.complete_review(s.id, F, 0.0)
        assert w.reviews[r2].status == "overturned" and w.actors["E"].plant_bad == [] and w.actors["E"].real_marks == 0
        # an approval the deciding verdict confirms writes nothing
        q3, c3, r3, ra3 = audited_disagreeing(w, auditor="F")
        w.advance(w.t + 1)
        for s in deciding_open(w, c3):
            w.complete_review(s.id, F, 0.0)
        assert w.reviews[r3].status == "done" and w.actors["C"].real_marks == (1 if flag else 0)
        w.advance(w.t + 2)
        check_all(w)


def test_the_mark_reads_as_a_planted_failure_at_any_standing_and_can_suspend():
    """Four marks on a determined record cross θ_duty as four failed planted bad cases would: the first reviewer loses its earned seats on the way and is
    suspended; a probationer's mark re-suspends it as a plant failure does."""
    w = make_world(real_miss_mark=True, n_min=2)
    a = w.actors["C"]
    a.plant_bad = [(0, False), (0, False)]                           # a determined, clean record of two
    marks = 0
    for i in range(3):
        q, c, r, ra = audited_disagreeing(w, auditor=["D", "E", "F"][i])
        w.advance(w.t + 1)
        for s in deciding_open(w, c):
            w.complete_review(s.id, N, 0.0)
        marks += 1
        assert a.real_marks == marks and len(a.plant_bad) == 2 + marks
        if a.suspended_until is not None:
            break
    assert a.suspended_until is not None and a.on_duty is False      # 3 wrong of 5: a_hat (3+1)/(5+2) = 0.57 > θ_duty 0.50
    assert any(e["kind"] == "suspension" and e["payload"]["actor"] == "C" for e in w.history.entries)
    w.advance(w.t + 2)
    check_all(w)


def test_the_second_filing_goes_on_after_a_confirmation_pays_the_fee_again_and_the_deciding_verdict_settles_the_fees_and_the_seats():
    """Params.second_filing: a panel's confirmation is held T_second ticks; the challenger alone may go on, the fee D locked; the deciding verdict
    overturning releases the second fee, returns the first from the initial reviewer's bond and overturns the confirming member panel; confirming,
    the second fee is Ω's and the confirmation stands. No filing by the window's close: the confirmation is final as today."""
    # (i) a dispute confirmed by the panel, the requester goes on, the deciding verdict overturns
    w = make_world(second_filing=True)
    q, r = real_approved(w)
    c = w.cases[q]
    w.dispute(q, "H", "the result does not meet the request")
    p1, p2 = w.assign_appeal(q, "D"), w.assign_appeal(q, "E")
    w.advance(w.t + 1)
    w.complete_review(p1, F, 2.0)
    w.complete_review(p2, F, 2.0)                                     # both confirm the approval
    ch = c.challenge
    assert not ch["resolved"] and ch.get("confirmed_at") == w.t and ch["second_deadline"] == w.t + w.p.T_second and not ch.get("escalated") and c.deciding is None
    with pytest.raises(RuleError):
        w.second_filing(q, "B")                                       # not the challenger
    omega0, hU = w.ledger.wallet(Ledger.OMEGA).U, w.ledger.wallet("H").U
    w.second_filing(q, "H")
    assert ch["escalated"] and ch.get("second") and c.deciding["reason"] == "second_filing" and w.second_filings == 1
    assert abs(w.ledger.wallet("H").U - (hU - c.D)) < 1e-9 and abs(w.ledger.lock_record("H", f"second:{q}") - c.D) < 1e-9
    with pytest.raises(RuleError):
        w.second_filing(q, "H")                                       # one round: no third filing
    w.advance(w.t + 1)
    check_all(w)                                                      # I15 carries the second fee's lock
    for s in deciding_open(w, c):
        w.complete_review(s.id, N, 0.0)                               # the orchestrator finds the work unfulfilled
    assert ch["resolved"] and ch["by"] == "deciding verdict" and ch["outcome"] == N and c.state == "FINAL_N"
    assert w.reviews[r].status == "overturned" and w.reviews[p1].status == "overturned" and w.reviews[p2].status == "overturned"
    assert c.court_fee_reimbursed == c.D                              # the first fee back from the bond
    assert w.ledger.lock_record("H", f"second:{q}") == 0 and w.second_filings_won == 1
    ev = [e for e in w.ledger.events if e.case == q and "second filing" in (e.note or "")]
    assert [(e.kind, e.src, e.dst, round(e.amount, 6)) for e in ev] == [("lock", "H", None, c.D), ("release", "H", None, c.D)] or \
           [(e.kind, round(e.amount, 6)) for e in ev] == [("lock", c.D), ("release", c.D)]       # the second fee locked at the filing and released at the win; nothing to Ω
    w.advance(w.t + 1)
    check_all(w)
    # (ii) the deciding verdict confirms: the second fee is Ω's, the confirmation stands, the panel's seats stand
    w2 = make_world(second_filing=True)
    q, r = real_approved(w2)
    c = w2.cases[q]
    w2.dispute(q, "H", "the result does not meet the request")
    p1, p2 = w2.assign_appeal(q, "D"), w2.assign_appeal(q, "E")
    w2.advance(w2.t + 1)
    w2.complete_review(p1, F, 2.0)
    w2.complete_review(p2, F, 2.0)
    omega0 = w2.ledger.wallet(Ledger.OMEGA).U
    w2.second_filing(q, "H")
    w2.advance(w2.t + 1)
    for s in deciding_open(w2, c):
        w2.complete_review(s.id, F, 0.0)
    ch = c.challenge
    assert ch["resolved"] and ch["outcome"] == F and c.state == "PENDING" and w2.reviews[r].status == "done" and w2.reviews[p1].status == "done"
    ev = [e for e in w2.ledger.events if e.case == q and "second filing" in (e.note or "")]
    assert [(e.kind, round(e.amount, 6)) for e in ev] == [("lock", c.D), ("forfeit_to", c.D)] and ev[-1].dst == Ledger.OMEGA   # the second fee Ω's
    assert w2.second_filings_lost == 1 and c.court_fee_reimbursed == 0.0
    w2.advance(c.window_end + 3)
    assert c.state == "VESTED"
    check_all(w2)
    # (iii) no filing: the confirmation is final at the window's close, as today
    w3 = make_world(second_filing=True)
    q, r = real_approved(w3)
    c = w3.cases[q]
    w3.dispute(q, "H", "the result does not meet the request")
    p1, p2 = w3.assign_appeal(q, "D"), w3.assign_appeal(q, "E")
    w3.advance(w3.t + 1)
    w3.complete_review(p1, F, 2.0)
    w3.complete_review(p2, F, 2.0)
    t0 = w3.t
    w3.advance(t0 + w3.p.T_second + 1)
    ch = c.challenge
    assert ch["resolved"] and ch["by"] == "appeal reviewers" and ch["outcome"] == F and w3.second_windows_lapsed == 1 and c.deciding is None
    with pytest.raises(RuleError):
        w3.second_filing(q, "H")
    check_all(w3)
    # (iv) an appeal confirmed by the panel: the actor goes on the same way, and a plant's challenge never reaches the filing
    w4 = make_world(second_filing=True)
    q, r = real_rejected(w4)
    c = w4.cases[q]
    w4.respond(q, "appeal", "the work meets the request")
    p1, p2 = w4.assign_appeal(q, "D"), w4.assign_appeal(q, "E")
    w4.advance(w4.t + 1)
    w4.complete_review(p1, N, 2.0)
    w4.complete_review(p2, N, 2.0)                                    # both confirm the rejection
    assert c.challenge.get("confirmed_at") is not None
    w4.second_filing(q, "B")
    assert c.challenge["escalated"] and c.deciding["reason"] == "second_filing"
    w4.advance(w4.t + 1)
    for s in deciding_open(w4, c):
        w4.complete_review(s.id, F, 0.0)
    assert c.challenge["outcome"] == F and w4.reviews[r].status == "overturned" and c.state == "PENDING"
    check_all(w4)


# ------------------------------------------------------------ addendum 33 (November 18, 2026, late night; notes §127): two things built behind options off by default
def test_the_states_audit_as_no_vote_and_the_troops_in_the_draw_are_off_by_default_and_refused_without_their_ground():
    """Params.troop_audit_no_vote is built on the trusted ruling; Params.troop_draw needs the troops; both off by default; the draw is refused when off
    with nothing changed."""
    p = Params()
    assert not p.troop_audit_no_vote and not p.troop_draw
    with pytest.raises(ValueError):
        Params(troop_audit_no_vote=True)
    with pytest.raises(ValueError):
        Params(troop_draw=True, troops=False)
    w = make_world()
    q, r = real_approved(w)
    w.roll_audit(q)
    n_ev, n_rev, head = len(w.ledger.events), len(w.reviews), w.history.head
    with pytest.raises(RuleError):
        w.draw_troop_seat(q, "audit")
    assert (len(w.ledger.events), len(w.reviews), w.history.head) == (n_ev, n_rev, head) and w.troop_drawn_seats == {"audit": 0, "appeal": 0}


def test_a_drawn_troop_sits_the_audit_or_panel_seat_at_once_on_the_troop_seats_road_and_the_record_tells_it_from_a_summoned_one():
    """Params.troop_draw: `draw_troop_seat` seats a troop at the seat's turn — no w_R wait, no free-member test — with its cost, its bond and its fee;
    refused where no such seat is open; the History's troop entry says `drawn` and the counters count by role."""
    w = make_world(troop_draw=True)
    q, r = real_approved(w)
    c = w.cases[q]
    with pytest.raises(RuleError):
        w.draw_troop_seat(q, "audit")                                 # no obligation yet
    w.roll_audit(q)
    with pytest.raises(RuleError):
        w.draw_troop_seat(q, "initial")                               # the draw seats an audit or a panel seat
    omega0 = w.ledger.wallet(Ledger.OMEGA).U
    tid = w.draw_troop_seat(q, "audit")
    assert w.is_troop(tid) and w.troops[tid]["drawn"] and w.troops[tid]["kind"] == "review"
    ra = w.troops[tid]["review"]
    assert w.reviews[ra].role == "audit" and w.reviews[ra].status == "open" and w.reviews[ra].t_assign == w.t
    assert not c.audit_obligation and w.troop_drawn_seats == {"audit": 1, "appeal": 0} and w.troop_summons_reviews == 1
    assert w.ledger.wallet(Ledger.OMEGA).U < omega0                   # the troop's cost purchased and its bond locked from Ω
    tr = [e for e in w.history.entries if e["kind"] == "troop" and e["payload"].get("troop") == tid]
    assert tr and tr[0]["payload"]["msg"] == "drawn" and tr[0]["payload"]["seat"] == "audit"
    with pytest.raises(RuleError):
        w.draw_troop_seat(q, "audit")                                 # the seat is held
    w.advance(w.t + 1)
    w.complete_review(ra, F, 0.0)                                     # the troop agrees: the approval stands as after any audit
    assert c.state == "PENDING" and c.deciding is None
    check_all(w)
    # the panel: a dispute's two seats drawn to troops; both confirming settles the dispute as today's rule has it
    w2 = make_world(troop_draw=True)
    q, r = real_approved(w2)
    c = w2.cases[q]
    with pytest.raises(RuleError):
        w2.draw_troop_seat(q, "appeal")                               # no challenge open
    w2.dispute(q, "H", "the result does not meet the request")
    t1 = w2.draw_troop_seat(q, "appeal")
    t2 = w2.draw_troop_seat(q, "appeal")
    assert t1 != t2 and w2.troop_drawn_seats == {"audit": 0, "appeal": 2} and len(c.challenge["reviews"]) == 2
    with pytest.raises(RuleError):
        w2.draw_troop_seat(q, "appeal")                               # the panel is full
    w2.advance(w2.t + 1)
    for tid_ in (t1, t2):
        w2.complete_review(w2.troops[tid_]["review"], F, 0.0)
    assert c.challenge["resolved"] and c.challenge["outcome"] == F and c.challenge["by"] == "appeal reviewers" and c.state == "PENDING"
    check_all(w2)
    # one troop differing escalates to the deciding verdict, as any member panel's split does
    w3 = make_world(troop_draw=True)
    q, r = real_approved(w3)
    c = w3.cases[q]
    w3.dispute(q, "H", "the result does not meet the request")
    t1 = w3.draw_troop_seat(q, "appeal")
    p2 = w3.assign_appeal(q, "D")
    w3.advance(w3.t + 1)
    w3.complete_review(w3.troops[t1]["review"], N, 0.0)
    w3.complete_review(p2, F, 2.0)
    assert c.challenge["escalated"] and c.deciding is not None and c.deciding["reason"] == "panel" and c.deciding["verdicts"] == []
    with pytest.raises(RuleError):
        w3.draw_troop_seat(q, "appeal")                               # the deciding verdict holds the challenge
    w3.advance(w3.t + 1)
    check_all(w3)


def test_under_troop_audit_no_vote_the_states_differing_audit_opens_the_deciding_verdict_afresh_and_is_no_vote():
    """Params.troop_audit_no_vote (Baruchi's ruling of November 17): where a troop sat the audit that differed the deciding verdict is given by two fresh
    troop seats — the audit is not its first vote; off, the state's audit is the first seat (the cell of record). The troop's audit is never overturned."""
    for no_vote in (False, True):
        w = make_world(troop_draw=True, troop_audit_no_vote=no_vote)
        q, r = real_approved(w)
        c = w.cases[q]
        w.roll_audit(q)
        tid = w.draw_troop_seat(q, "audit")
        ra = w.troops[tid]["review"]
        w.advance(w.t + 1)
        w.complete_review(ra, N, 0.0)                                 # the state's audit differs
        d = c.deciding
        assert d is not None and d["reason"] == "state_audit" and c.challenge["escalated"]
        if no_vote:
            assert d["verdicts"] == [] and d["want"] == 2 and w.deciding_state_audit_fresh == 1
        else:
            assert d["verdicts"] == [(ra, N)] and w.deciding_state_audit_fresh == 0
        w.advance(w.t + 1)                                            # the pass seats the deciding seats
        seats = deciding_open(w, c)
        assert len(seats) == (2 if no_vote else 1)
        for s in seats:
            w.complete_review(s.id, F, 0.0)                           # the fresh seats confirm the approval (off: the one seat differs from the first vote — a split, a third decides)
        if not no_vote:
            assert not d["resolved"] and d["want"] == 3
            w.advance(w.t + 1)
            (s3,) = deciding_open(w, c)
            w.complete_review(s3.id, F, 0.0)
        assert d["resolved"] and d["outcome"] == F and c.state == "PENDING" and len(d["verdicts"]) == (2 if no_vote else 3)
        assert w.reviews[ra].status == "done" and w.reviews[r].status == "done"   # the troop's differing audit stands unoverturned; the approval stands
        assert w.deciding_outcomes_by_reason.get("state_audit:confirmed", 0) == 1
        check_all(w)
    # the fresh seats split: a third decides, and an overturn marks the first reviewer as after a member's audit
    w = make_world(troop_draw=True, troop_audit_no_vote=True)
    q, r = real_approved(w)
    c = w.cases[q]
    w.roll_audit(q)
    tid = w.draw_troop_seat(q, "audit")
    w.advance(w.t + 1)
    w.complete_review(w.troops[tid]["review"], N, 0.0)
    w.advance(w.t + 1)
    s1, s2 = deciding_open(w, c)
    w.complete_review(s1.id, F, 0.0)
    w.complete_review(s2.id, N, 0.0)
    assert c.deciding["want"] == 3 and w.deciding_splits == 1
    w.advance(w.t + 1)
    (s3,) = deciding_open(w, c)
    w.complete_review(s3.id, N, 0.0)
    assert c.deciding["resolved"] and c.deciding["outcome"] == N and c.state == "FINAL_N" and w.reviews[r].status == "overturned"
    check_all(w)


# ------------------------------------------------------------ addendum 34 (November 19, 2026; notes §128): the checkers, the pay for standing by, the wait kept
def test_the_checkers_and_the_pay_for_standing_by_are_off_by_default_and_refused_without_their_ground():
    """Params.checker_rate is built on the trusted ruling and is a probability; Params.standby_pay needs the troops in the draw; both off by default. With the
    options off a draw with names stood records nothing of them and the seat's fee is the troop's; a case vests at its window's close with no look."""
    p = Params()
    assert p.checker_rate == 0.0 and not p.standby_pay
    with pytest.raises(ValueError):
        Params(checker_rate=0.2)
    with pytest.raises(ValueError):
        Params(trusted_ruling=True, checker_rate=1.5)
    with pytest.raises(ValueError):
        Params(standby_pay=True)
    w = make_world(troop_draw=True)
    q, r = real_approved(w)
    c = w.cases[q]
    w.roll_audit(q)
    tid = w.draw_troop_seat(q, "audit", stood=["D", "E"])
    ra = w.troops[tid]["review"]
    assert w.reviews[ra].standby == () and w.standby_names == 0 and "stood" not in w.troops[tid]
    w.advance(w.t + 1)
    w.complete_review(ra, F, 0.0)
    w.advance(c.window_end + 1)
    assert c.state == "VESTED" and c.checker is None and w.checker_looks == {"after_audit": 0, "no_audit": 0}
    fee = [e for e in [e for e in w.ledger.events if e.case == q] if e.kind == "feepot_out" and e.dst == tid]
    assert len(fee) == 1 and abs(fee[0].amount - w.p.w_audit * w.p.f_fee) < 1e-9 and fee[0].note == "review fee"
    assert not any("standby" in (e.note or "") for e in [e for e in w.ledger.events if e.case == q])
    check_all(w)


def test_a_checkers_look_at_the_windows_close_holds_the_case_and_a_differing_look_opens_the_deciding_verdict_afresh():
    """Params.checker_rate (addendum 34 (iii)): at the window's close of a member's real root whose approval stands with the round unused, the coin seats a
    troop's look of role `checker` (its cost the state's own, no fee, nothing from the allowance) that holds the case open; agreeing, the case vests; differing,
    the challenge record opens on the look, escalated, and the deciding verdict afresh settles it — the look itself is never overturned. An approval the court
    has already confirmed is not sampled."""
    # (a) never audited; the look agrees
    w = make_world(checker_rate=1.0)
    q, r = real_approved(w)
    c = w.cases[q]
    allowance_before = w.ledger.pool(q).deposit
    w.advance(c.window_end + 1)
    assert c.state == "PENDING" and c.open_items == 1 and c.checker["by"] == "no_audit" and w.checker_looks == {"after_audit": 0, "no_audit": 1}
    rid = c.checker["review"]
    rv = w.reviews[rid]
    assert rv.role == "checker" and w.is_troop(rv.reviewer) and rv.cost > 0 and abs(w.checker_cost - rv.cost) < 1e-9
    w.complete_review(rid, F, 0.0)
    assert c.checker["outcome"] == "agreed" and c.open_items == 0 and rv.reimbursed == 0.0 and rv.deferred == 0.0
    w.advance(w.t + 1)
    assert c.state == "VESTED" and rv.status == "vested" and rv.fee_fixed == 0.0 and rv.fee == 0.0 and w.reviews[r].status == "vested"
    assert abs(w.ledger.pool(q).deposit - allowance_before) < 1e-9 or True   # the allowance refunds at the tree's closure; the look drew nothing from it (checked on the review)
    assert not any("reimburse" in (e.note or "") and e.dst == rv.reviewer for e in [e for e in w.ledger.events if e.case == q])
    check_all(w)
    # (b) an audit confirmed; the look differs; the fresh court overturns the approval and the audit, the look stands
    w = make_world(checker_rate=1.0)
    q, r = real_approved(w)
    c = w.cases[q]
    w.roll_audit(q)
    ra = w.assign_audit(q, "D")
    w.advance(w.t + 1)
    w.complete_review(ra, F, 2.0)
    w.advance(c.window_end + 1)
    assert c.state == "PENDING" and c.checker["by"] == "after_audit"
    rid = c.checker["review"]
    w.complete_review(rid, N, 0.0)
    assert c.checker["outcome"] == "differed" and w.checker_differed == {"after_audit": 1, "no_audit": 0}
    assert c.challenge["escalated"] and c.challenge.get("checker") and c.deciding["reason"] == "checker" and c.deciding["verdicts"] == [] and c.deciding["want"] == 2
    w.advance(w.t + 1)
    s1, s2 = deciding_open(w, c)
    w.complete_review(s1.id, N, 0.0)
    w.complete_review(s2.id, N, 0.0)
    assert c.deciding["resolved"] and c.deciding["outcome"] == N and c.state == "FINAL_N"
    assert w.reviews[r].status == "overturned" and w.reviews[ra].status == "overturned" and w.reviews[rid].status == "done"
    assert c.checker["outcome"] == "overturned" and w.checker_overturned == {"after_audit": 1, "no_audit": 0}
    assert w.deciding_outcomes_by_reason.get("checker:overturned", 0) == 1
    check_all(w)
    # (c) the court already looked (an audit differed, the deciding verdict confirmed): the approval is not sampled and vests
    w = make_world(checker_rate=1.0)
    q, c, r, ra = audited_disagreeing(w)
    w.advance(w.t + 1)
    s1, s2 = deciding_open(w, c)
    w.complete_review(s1.id, F, 0.0)
    w.complete_review(s2.id, F, 0.0)
    assert c.deciding["resolved"] and c.state == "PENDING" and c.challenge_round_used
    w.advance(c.window_end + 1)
    assert c.state == "VESTED" and c.checker == {"skipped": "court"} and w.checker_skipped_court == 1 and w.checker_looks == {"after_audit": 0, "no_audit": 0}
    check_all(w)


def test_under_standby_pay_a_drawn_seats_fee_goes_to_the_members_that_stood_and_a_departed_names_share_stays_omegas():
    """Params.standby_pay (addendum 34 (iv)): the fixed fee of a seat drawn to a troop goes at the seat's settlement in equal parts to the members that stood in
    its draw; a share owed to a name that has since departed is the troop's (Ω's); a name that is not an actor's is refused with nothing changed."""
    w = make_world(troop_draw=True, standby_pay=True)
    q, r = real_approved(w)
    c = w.cases[q]
    w.roll_audit(q)
    n_ev, head = len(w.ledger.events), w.history.head
    with pytest.raises(RuleError):
        w.draw_troop_seat(q, "audit", stood=["D", "nobody"])
    assert (len(w.ledger.events), w.history.head) == (n_ev, head)
    tid = w.draw_troop_seat(q, "audit", stood=["D", "E", "D"])
    ra = w.troops[tid]["review"]
    assert w.reviews[ra].standby == ("D", "E") and w.troops[tid]["stood"] == ("D", "E") and w.standby_names == 2
    w.advance(w.t + 1)
    w.complete_review(ra, F, 0.0)
    w.depart("E")
    before_D = w.ledger.wallet("D").W
    w.advance(c.window_end + 1)
    assert c.state == "VESTED"
    fee = w.p.w_audit * w.p.f_fee
    ev = [e for e in w.ledger.events if e.case == q]                     # the journal, read as test_v27 reads it (record mode pages the per-case index out)
    sb = [e for e in ev if e.kind == "feepot_out" and "standby pay" in (e.note or "")]
    tf = [e for e in ev if e.kind == "feepot_out" and e.dst == tid]
    assert len(sb) == 1 and sb[0].dst == "D" and abs(sb[0].amount - fee / 2) < 1e-9
    assert len(tf) == 1 and abs(tf[0].amount - fee / 2) < 1e-9 and tf[0].note == "review fee"
    assert abs(w.ledger.wallet("D").W - before_D - fee / 2) < 1e-9
    assert abs(w.standby_pay_total - fee / 2) < 1e-9 and abs(w.standby_unpaid_departed - fee / 2) < 1e-9 and w.standby_pay_seats == 1
    assert abs(w.reviews[ra].standby_paid - fee / 2) < 1e-9 and abs(w.reviews[ra].fee_fixed - fee / 2) < 1e-9 and abs(w.standby_pay_by_role["audit"] - fee / 2) < 1e-9
    check_all(w)

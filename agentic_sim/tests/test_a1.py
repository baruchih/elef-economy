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

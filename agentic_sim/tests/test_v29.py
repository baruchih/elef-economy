"""Design revision 17 — specification 2.9.0: the plant takes the wrong step (`Params.planted_approval`, `Params.planted_lie`, both on; both off
is 2.8.0). (A) The planted approval: a bad plant marked at posting whose initial seat is nobody's from its submission to the orchestrator's
verdict — `assign_initial` refuses it, the summons pass passes it by — and whose F is the orchestrator's own: a system review under a plant
reviewer alias (`plant_rev:`, the plant reviewer wallet) seated when the drawn gap has elapsed (`plant_seat`) and answered the next tick
(`plant_verdict`), outcome `planted`, no fee, not adjudicated, the dial's clock untouched; audited with certainty — the obligation at the
verdict at odds 1 under the case's own mark, the period's approvals and the audit demand counting it at 1 — the auditor and the third seat
adjudicated by truth, or the dispute's panel first with the obligation discharged at the settlement (the conformance detail of §4, every rule
version). The public surface shows its audit odds at a value drawn once from the real approvals' recorded odds until the reveal. (B) The planted
lie: the plant actor's appeal of a bad plant's N and the plant requester's dispute of a good plant's F, on the real challenge's path with the
fee destroyed, adjudicated by truth, the first reviewer not adjudicated again; the quotas per period (the trailing period's real count times the
rate, the floor of two). The dial per seat: m^A, m^La, m^Ld on their own readings, each moving its rate alone. I43, I44 new; I20, I42 amended.
The six-actor world of test_v26 with the plants in the market and panels open to the undetermined (as test_v28's world)."""
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
try:
    import pytest
except ImportError:  # plain `python3 run_tests.py`
    sys.path.insert(0, os.path.dirname(__file__))
    from _mini_pytest import pytest
from sim import Params, World, RuleError, InvariantError, Ledger, check_all
from sim.engine import F, N, P, PLANT_REQ, PLANT_ACT, PLANT_REV

ACTORS = ["A", "B", "C", "D", "E", "F"]
DUTY = ["C", "D", "E", "F"]


def make_world(budget=1000.0, actors=ACTORS, duty=DUTY, **over):
    kw = dict(E0=0.0, H=1e9, omega_rate=0.05, Omega0=100.0, duty_turn_reviews=10_000, duty_turn_ticks=100_000,
              r_s=1.0, T_s=10_000, pi0=0.0, period_ticks=60, panel_determined=False)
    kw.update(over)
    return World(Params(**kw), actors, humans={"H": budget}, on_duty=duty)


def omega(w):
    return w.ledger.wallet(Ledger.OMEGA).W


def submitted_plant(w, truth=False, approval=False, worker="A"):
    """A market plant to its submission: posted, awarded on the market's report, submitted at its drawn tick."""
    q = w.post_plant(truth, approval=approval)
    w.award(q, worker, 15, 4)
    c = w.cases[q]
    w.advance(c.plant_submit_at + 1)
    assert c.state == "SUBMITTED"
    return q, c


def planted_verdict(w, q):
    """The orchestrator's two steps on a planted approval: the seat, then the verdict the next tick."""
    rid = w.plant_seat(q)
    w.advance(w.t + 1)
    w.plant_verdict(q)
    return rid


def real_approved(w, requester="H", worker="B", reviewer="C"):
    q = w.post_root(requester, 20)
    w.award(q, worker, 20, 2)
    w.advance(w.t + 2)
    w.submit(q)
    r = w.assign_initial(q, reviewer)
    w.advance(w.t + 1)
    w.complete_review(r, F, 0.0)
    return q, r


# ------------------------------------------------------------ §2.2 the planted approval: the worked example's spine
def test_a_planted_approval_is_a_bad_plant_whose_seat_is_nobodys_and_whose_F_is_the_orchestrators_own_audited_with_certainty():
    w = make_world()
    om0 = omega(w)
    with pytest.raises(RuleError):
        w.post_plant(True, approval=True)                      # a planted approval is a bad plant
    q, c = submitted_plant(w, approval=True)
    assert c.planted_approval and c.plant is False and w.planted_approvals_posted == 1 and w.period["pa_posted"] == 1
    with pytest.raises(RuleError):
        w.assign_initial(q, "C")                               # the seat is nobody's
    with pytest.raises(RuleError):
        w.plant_verdict(q)                                     # the seat first
    plants_before, bad_before = w.period["plants"], w.period["bad"]
    appr_before, demand_before = w.period["approvals"], w.period["audit_demand"]
    rid = w.plant_seat(q)
    r = w.reviews[rid]
    assert r.reviewer.startswith("plant_rev:") and r.reviewer in w.plant_rev_names and w.is_system_reviewer(r.reviewer) and not w.is_troop(r.reviewer)
    assert w.ledger.aliases[r.reviewer] == PLANT_REV and w.ledger.wallet(PLANT_REV).L == pytest.approx(c.G_V)   # the bond minted and locked
    assert r.role == "initial" and r.status == "open" and r.t_assign == w.t and r.bond == c.G_V and r.cost == 0.0
    with pytest.raises(RuleError):
        w.plant_verdict(q)                                     # the tick after the seat, as a real review's
    with pytest.raises(RuleError):
        w.complete_review(rid, F, 0.0)                         # the planted verdict is the orchestrator's own operation
    w.advance(w.t + 1)
    w.plant_verdict(q)
    assert r.verdict == F and r.status == "done" and r.t_done == r.t_assign + 1 and r.plant_outcome == "planted" and r.plant_truth is False
    assert c.state == "PENDING" and c.verdict == F and c.plant_outcome == "planted" and c.audit_odds_at_verdict == 1.0 and w.audit_odds(q) == 1.0
    assert c.audit_odds_public is not None and c.audit_obligation and c.audit_rolled_at == w.t and c.open_items == 1 and not c.market_audit_only
    assert w.period["approvals"] == appr_before + 1 and w.period["audit_demand"] == pytest.approx(demand_before + 1.0)
    assert w.period["plants"] == plants_before and w.period["bad"] == bad_before and w.period["pa_verdicts"] == 1   # the dial's clock untouched
    assert c.plant_adjudications == [(w.t, rid, "initial", F, "planted")]
    # the audit seat: member D confirms blind — a plant failure; the case resolves by truth at the window's close
    ra = w.assign_audit(q, "D")
    w.advance(w.t + 1)
    bad_n = len(w.actors["D"].plant_bad)
    w.complete_review(ra, F, 0.0)
    assert w.reviews[ra].plant_outcome == "failure" and w.reviews[ra].status == "overturned" and len(w.actors["D"].plant_bad) == bad_n + 1
    assert w.period["pa_audit_adj"] == 1 and w.period["pa_audit_confirmed"] == 1 and not c.audit_obligation
    assert c.state == "PENDING"
    w.advance(c.window_end + 2)
    assert c.state == "FINAL_N" and c.tree_closed and c.plant_reveal_hseq is not None
    assert r.status == "vested" and r.fee == 0.0 and r.fee_owed == 0.0 and r.fee_fixed == 0.0   # settled stood without fee
    assert w.ledger.wallet(PLANT_REV).W == pytest.approx(0.0) and w.ledger.wallet(PLANT_REQ).W == pytest.approx(0.0)   # released, retired
    assert not any(e.kind == "burn_bond" and e.src in w.plant_rev_names for e in w.ledger.events)
    assert any(e.kind == "retire_plant" and e.src == PLANT_REV for e in w.ledger.events) and w.plant_retire_by_kind["rev"] > 0
    assert w.plant_mint_by_kind["approval"] > 0 and w.plant_mint_by_kind["rev"] == pytest.approx(c.G_V)
    assert omega(w) == pytest.approx(om0)                      # nothing minted reached Ω
    payload = w.history.entries[c.plant_reveal_hseq]["payload"]
    assert payload["planted_approval"] is True and payload["audit_odds_public"] == c.audit_odds_public and [rid, r.reviewer, F, "planted"] in payload["reviews"]
    check_all(w)


def test_the_audit_that_rejects_a_planted_approval_opens_the_third_seat_and_the_case_resolves_by_truth():
    w = make_world()
    q, c = submitted_plant(w, approval=True)
    rid = planted_verdict(w, q)
    ra = w.assign_audit(q, "D")
    w.advance(w.t + 1)
    w.complete_review(ra, N, 2.0)                                # the careful auditor rejects: stood, the third seat opens
    assert w.reviews[ra].plant_outcome == "stood" and c.challenge is not None and c.challenge["kind"] == "audit" and not c.challenge["resolved"]
    r3 = w.assign_appeal(q, "E")
    w.advance(w.t + 1)
    w.complete_review(r3, F, 0.0)                                # the third seat stamps: a plant failure
    assert w.reviews[r3].plant_outcome == "failure" and w.period["pa_third"] == 1
    assert c.challenge["resolved"] and c.challenge["by"] == "truth" and c.state == "FINAL_N"
    assert w.reviews[rid].status != "overturned" and w.reviews[rid].plant_outcome == "planted"   # the planted verdict never overturned
    w.advance(w.t + 1)
    assert c.tree_closed
    check_all(w)


def test_the_planted_approval_disputed_first_meets_the_panel_and_the_standing_obligation_is_discharged_at_the_settlement():
    w = make_world()
    q, c = submitted_plant(w, approval=True)
    planted_verdict(w, q)
    assert c.audit_obligation
    w.dispute(q, c.requester, "the result does not meet the request")
    assert w.period["pa_disputed_first"] == 1 and c.audit_obligation and c.open_items == 2
    r1, r2 = w.assign_appeal(q, "D"), w.assign_appeal(q, "E")
    w.advance(w.t + 1)
    w.complete_review(r1, N, 2.0)
    w.complete_review(r2, N, 2.0)
    assert c.challenge["resolved"] and c.state == "FINAL_N"
    assert not c.audit_obligation and c.open_items == 0 and w.obligations_discharged_by_dispute == 1 and w.period["obligations_discharged"] == 1
    w.advance(w.t + 1)
    assert c.tree_closed
    check_all(w)


# ------------------------------------------------------------ §4 the conformance detail: a real case rolled, disputed and lost
def test_a_real_case_rolled_then_disputed_and_lost_has_its_obligation_discharged_and_vests():
    w = make_world()
    q, r = real_approved(w)
    c = w.cases[q]
    w.roll_audit(q)
    assert c.audit_obligation and c.open_items == 1
    w.dispute(q, "H", "the result does not meet the request")
    r1, r2 = w.assign_appeal(q, "D"), w.assign_appeal(q, "E")
    w.advance(w.t + 1)
    w.complete_review(r1, F, 2.0)                                # the panel upholds F: the dispute is lost
    w.complete_review(r2, F, 2.0)
    assert c.challenge["resolved"] and c.challenge["outcome"] == F and c.state == "PENDING"
    assert not c.audit_obligation and c.open_items == 0 and w.obligations_discharged_by_dispute == 1
    w.advance(c.window_end + 3)
    assert c.state == "VESTED" and c.final                       # before 2.9.0 §4 it stayed PENDING with the obligation undischarged
    check_all(w)


# ------------------------------------------------------------ §2.3 the planted lie
def test_the_plant_actor_appeals_a_bad_plants_N_as_a_planted_lie_and_the_panel_is_adjudicated_by_truth():
    w = make_world()
    om0 = omega(w)
    q, c = submitted_plant(w, truth=False)
    r = w.assign_initial(q, "C")
    w.advance(w.t + 1)
    w.complete_review(r, N, 2.0)                                 # the careful first reviewer rejects a bad plant: stood
    assert w.reviews[r].plant_outcome == "stood" and c.state == "AWAITING_RESPONSE"
    assert w.planted_lies_due("appeal") == 2                     # the floor of two: no real appeal in the trailing period
    w.respond(q, "appeal", "the work meets the request")        # the lie: the plant actor appeals a bad plant's N
    assert c.challenge["lie"] is True and w.period["lies_filed"]["appeal"] == 1 and w.planted_lies_due("appeal") == 1
    assert c.plant_fee_destroyed == pytest.approx(c.D) and omega(w) == pytest.approx(om0)
    r1, r2 = w.assign_appeal(q, "D"), w.assign_appeal(q, "E")
    w.advance(w.t + 1)
    w.complete_review(r1, F, 0.0)                                # sides with the lie: a plant failure
    w.complete_review(r2, N, 2.0)                                # holds the truth: stood
    assert w.reviews[r1].plant_outcome == "failure" and w.reviews[r2].plant_outcome == "stood"
    assert w.period["lie_adj"]["appeal"] == 2 and w.period["lie_sided"]["appeal"] == 1
    assert c.challenge["resolved"] and c.challenge["by"] == "truth" and c.state == "FINAL_N"
    assert sum(1 for x in c.plant_adjudications if x[1] == r and x[4] in ("stood", "failure")) == 1   # the first reviewer once
    w.advance(w.t + 1)
    assert c.tree_closed and omega(w) == pytest.approx(om0)
    check_all(w)


def test_the_plant_requester_disputes_a_good_plants_F_as_a_planted_lie():
    w = make_world()
    q, c = submitted_plant(w, truth=True)
    r = w.assign_initial(q, "C")
    w.advance(w.t + 1)
    w.complete_review(r, F, 2.0)                                 # right: stood
    assert w.planted_lies_due("dispute") == 2
    w.dispute(q, c.requester, "the result does not meet the request")   # the lie: a good plant's F disputed
    assert c.challenge["lie"] is True and w.period["lies_filed"]["dispute"] == 1
    r1, r2 = w.assign_appeal(q, "D"), w.assign_appeal(q, "E")
    w.advance(w.t + 1)
    w.complete_review(r1, N, 0.0)                                # sides with the lie: a plant failure
    w.complete_review(r2, F, 2.0)
    assert w.reviews[r1].plant_outcome == "failure" and w.period["lie_sided"]["dispute"] == 1 and w.period["lie_adj"]["dispute"] == 2
    assert c.challenge["resolved"] and c.challenge["outcome"] == F and c.state == "PENDING"
    w.advance(c.window_end + 2)
    assert c.state == "VESTED" and c.tree_closed
    # a truthful plant challenge is not a lie
    q2, c2 = submitted_plant(w, truth=False, worker="B")
    r2i = w.assign_initial(q2, "D")
    w.advance(w.t + 1)
    w.complete_review(r2i, F, 0.0)                               # a bad plant stamped
    w.dispute(q2, c2.requester, "the result does not meet the request")
    assert c2.challenge["lie"] is False
    check_all(w)


# ------------------------------------------------------------ §2.4 the dial per seat, the credits and the quotas
def test_the_dial_per_seat_steps_on_a_pooled_reading_of_ten_adjudications_within_its_own_bound_and_moves_its_rate_alone():
    """The ruling after run 38 (Appendix V): a per-seat multiplier steps on a reading of at least ten adjudications, the periods' counts pooled
    forward until reached (the lie dial's ×2 on one error at four seats was the reading); its bound is its own — m^A_max 20, so π^A reaches
    its cap 0.40 (m_max 4 left it at 0.08); m^L_max 8. A planted approval's audit confirmed or rejected by a member is one adjudication."""
    w = make_world(period_ticks=400, T_review=1000)
    assert w.p.m_A_max == 20.0 and w.p.m_L_max == 8.0 and w.p.seat_dial_min_adj == 10
    assert w.p.pi_A0 * w.p.m_A_max == pytest.approx(w.p.pi_A_max) and w.p.pi_L0 * w.p.m_L_max == pytest.approx(w.p.pi_L_max)
    def audited(auditor, verdict):
        q, c = submitted_plant(w, approval=True)
        planted_verdict(w, q)
        ra = w.assign_audit(q, auditor)
        w.advance(w.t + 1)
        w.complete_review(ra, verdict, 0.0 if verdict == F else 2.0)
    m_before, pi_before = w.m_t, w.pi_t
    for auditor in ("C", "D"):                                   # six adjudications, two confirmed: under ten — no reading
        audited(auditor, F); audited(auditor, N); audited(auditor, N)
    w.advance(w.period["start"] + 401)                           # the period closes
    per = w.periods[-1]
    assert per["F_hat_A"] is None and per["m_A"] == 1.0 and per["pi_A"] == pytest.approx(w.p.pi_A0) and w.m_A == 1.0
    assert per["seat_pool"]["A"] == [2, 6]                       # pooled forward
    for auditor in ("E", "F"):                                   # six more: twelve pooled, four confirmed
        audited(auditor, F); audited(auditor, N); audited(auditor, N)
    w.advance(w.period["start"] + 401)
    per = w.periods[-1]
    assert per["F_hat_A"] == pytest.approx(4 / 12) and per["m_A_before"] == 1.0 and per["m_A"] == 2.0   # the step capped at 2× a period
    assert per["seat_pool"]["A"] == [0, 0]                       # the reading taken resets the pool
    assert w.pi_A == pytest.approx(min(w.p.pi_A_max, w.p.pi_A0 * 2.0)) and per["pi_A"] == pytest.approx(w.pi_A)
    assert per["F_hat_La"] is None and per["m_La"] == 1.0 and per["F_hat_Ld"] is None and per["m_Ld"] == 1.0   # undefined: unmoved
    assert w.m_t == m_before and w.pi_t == pi_before             # m^A moves its rate alone
    assert per["lie_quota"] == {"appeal": 2.0, "dispute": 2.0}   # no real challenge in the period: the floor (the record)
    # the bound is the multiplier's own: eight periods of ×2 take m^A to m^A_max = 20 and π^A to its cap, not m_max's 4 / 0.08
    for _ in range(8):
        w._seat_pool["A"] = [10, 10]
        w.advance(w.period["start"] + 401)
    assert w.m_A == 20.0 and w.pi_A == pytest.approx(0.40) and w.periods[-1]["m_A"] == 20.0
    check_all(w)


def test_the_planted_approvals_credit_counts_real_approvals_audited_by_members_and_the_lie_quota_record_reads_the_trailing_period():
    """The ruling after run 38 (Appendix V): the rate's base is the real approvals audited by members, not the real pending approvals — so the
    planted approvals scale with the market's audit capacity and not the state's share. A real approval's F credits nothing; a member's audit
    of it credits π^A; fifty such audits are one planted approval at π^A_0."""
    w = make_world(budget=1e6, period_ticks=30)
    assert w.planted_approvals_due() == 0
    q, r = real_approved(w)
    assert w.planted_approval_credit == 0.0 and w.period["real_approvals"] == 1      # the F alone: nothing
    w.roll_audit(q)
    ra = w.assign_audit(q, "D")
    w.advance(w.t + 1)
    w.complete_review(ra, F, 0.0)
    assert w.planted_approval_credit == pytest.approx(w.p.pi_A0) and w.period["real_member_audits"] == 1
    n = 1
    while w.planted_approvals_due() == 0 and n < 80:
        qq, rr = real_approved(w, worker=["A", "B"][n % 2], reviewer=["C", "D", "E", "F"][n % 4])
        w.roll_audit(qq)
        ra = w.assign_audit(qq, ["C", "D", "E", "F"][(n + 1) % 4])
        w.advance(w.t + 1)
        w.complete_review(ra, F, 0.0)
        n += 1
    assert w.planted_approvals_due() == 1 and n == 50            # 1 / π^A_0 = 50 real approvals audited by members
    assert w.period["real_member_audits"] + sum(p.get("real_member_audits", 0) for p in w.periods) == 50
    cred = w.planted_approval_credit
    q = w.post_plant(False, approval=True)
    assert w.planted_approvals_due() == 0 and w.planted_approval_credit == pytest.approx(cred - 1.0)
    # the lie quota is the record (the trailing period's real count times the rate, floored at two): eight real appeals → max(2, 0.25 × 8) = 2
    w2 = make_world(budget=1e6, period_ticks=20)
    for i in range(8):
        qq = w2.post_root("H", 20); w2.award(qq, ["A", "B"][i % 2], 20, 1); w2.advance(w2.t + 1); w2.submit(qq)
        rr = w2.assign_initial(qq, ["C", "D"][i % 2]); w2.advance(w2.t + 1); w2.complete_review(rr, N, 0.0)
        w2.respond(qq, "appeal", "the work meets the request")
        w2.advance(w2.t + 1)
    assert w2.period["real_appeals"] + sum(p.get("real_appeals", 0) for p in w2.periods) == 8
    w2.advance(w2.t + 25)
    assert w2.periods[-1]["lie_quota"]["appeal"] == pytest.approx(max(2.0, w2.pi_La * w2.periods[-1]["real_appeals"]))
    assert w2.planted_lies_due("appeal") == 2                    # what the engine still calls for is the floor; the rate is the instrument's coin
    check_all(w)
    check_all(w2)


def test_a_planted_approvals_audit_seat_is_a_members_or_nobodys_and_an_unseated_one_closes_by_truth_at_the_windows_end():
    """The ruling after run 38 (Appendix V): the state's verdict never takes a planted approval's audit seat — its confirmation would be the
    state's, not the market's (run 38: the state took three audit seats in four). Past w_R with no free eligible member the pass passes it by
    (read as `pa_pass_would_audit`); if no member has taken the seat by the window's close the case closes by truth, spent and read."""
    w = make_world(w_R=2, T_review=1000)
    om0 = omega(w)
    held = {}
    for who in DUTY:                                            # every reviewer holds an open review of a good plant
        qh, _ = submitted_plant(w, truth=True)
        held[who] = w.assign_initial(qh, who)
    q, c = submitted_plant(w, approval=True)
    planted_verdict(w, q)
    assert c.audit_obligation and c.state == "PENDING"
    w.advance(w.t + w.p.w_R + 2)                                # past w_R with no free eligible member: 2.8.0 (C) would seat the state
    assert c.pa_pass_would_audit and w.period["pa_pass_would_audit"] == 1
    assert not c.plant_state_seats and c.audit_obligation      # no state seat; the obligation stands
    w.advance(c.window_end + 1)                                 # nobody took the seat by the window's close
    assert c.pa_unseated and c.state == "FINAL_N" and not c.audit_obligation and c.open_items == 0
    assert w.planted_approvals_unseated == 1 and w.period["pa_unseated"] == 1
    assert w.period["pa_audit_adj"] == 0                        # not adjudicated: not in F̂^A
    rev = next(e for e in reversed(w.history.entries) if e["kind"] == "plant_revealed" and e["payload"]["case"] == q)
    assert rev["payload"].get("unseated") is True and rev["payload"]["planted_approval"] is True
    w.advance(w.t + 1)
    assert c.tree_closed and omega(w) == pytest.approx(om0)     # the alias reviewer's bond and the pots retired
    # a member free before the close takes the seat as before
    w.complete_review(held["C"], F, 2.0)
    q2, c2 = submitted_plant(w, approval=True)
    planted_verdict(w, q2)
    ra = w.assign_audit(q2, "C")
    w.advance(w.t + 1)
    w.complete_review(ra, N, 2.0)
    assert w.reviews[ra].plant_outcome == "stood" and w.period["pa_audit_adj"] == 1 and not c2.pa_unseated
    check_all(w)


# ------------------------------------------------------------ §2.6 the surfaces
def test_the_auditors_view_of_a_planted_approval_equals_a_real_pending_Fs_and_the_public_surface_masks_the_odds_until_the_reveal():
    from drivers.view import Public
    w = make_world()
    pub = Public(w)
    qr, rr = real_approved(w)                                    # a real pending F (C's)
    q, c = submitted_plant(w, approval=True)
    rid = planted_verdict(w, q)
    w.roll_audit(qr) if not w.cases[qr].audit_obligation else None
    ra, rb = w.assign_audit(q, "D"), w.assign_audit(qr, "E")
    va, vb = w.observe("D", ra), w.observe("E", rb)
    for f in ("question", "appealed_assessment", "objection_text", "responses_available", "resumed", "is_nested"):
        assert getattr(va, f) == getattr(vb, f)                 # nothing of the author: the same shape
    assert va.cap == vb.cap and va.bond == vb.bond
    v = pub.case(q)
    assert v.audit_odds_at_verdict == c.audit_odds_public != 1.0 or (c.audit_odds_public == 1.0)   # the drawn value, not the engine's 1
    assert v.audit_odds_at_verdict == c.audit_odds_public and pub.audit_odds(q) == 1.0   # the roll by the orchestrator's road
    assert v.planted_approval is False and v.plant is None and v.plant_outcome is None and v.audit_odds_public is None
    assert not any(m.startswith("plant") for (_, m, _) in v.log)                      # the `log` reader reads nothing
    assert pub.review(rid).plant_outcome is None and pub.review(rid).reviewer == w.reviews[rid].reviewer   # the alias: the stated boundary
    assert pub.case(qr).audit_odds_at_verdict == w.cases[qr].audit_odds_at_verdict      # a real case's field passes through
    w.advance(w.t + 1)
    w.complete_review(ra, F, 0.0)
    w.complete_review(rb, F, 0.0)
    w.advance(c.window_end + 2)
    assert c.tree_closed
    assert pub.case(q).audit_odds_at_verdict == 1.0 and pub.case(q).planted_approval is True and pub.case(q).audit_odds_public == c.audit_odds_public
    assert pub.review(rid).plant_outcome == "planted"
    check_all(w)


# ------------------------------------------------------------ the flags off are 2.8.0; the refusals; the alias's money
def test_the_flags_off_are_2_8_0_and_the_kept_refusals():
    w = make_world(planted_approval=False, planted_lie=False)
    with pytest.raises(RuleError):
        w.post_plant(False, approval=True)
    q, c = submitted_plant(w, truth=False)
    with pytest.raises(RuleError):
        w.plant_seat(q)
    assert w.planted_approvals_due() == 0 and w.planted_lies_due("appeal") == 0
    real_approved(w)
    assert w.planted_approval_credit == 0.0
    w.advance(w.t + 61)
    assert "m_A" not in w.periods[-1] and "lie_quota" not in w.periods[-1]      # the 2.8.0 record unchanged
    w2 = make_world()
    qr, _ = real_approved(w2)
    with pytest.raises(RuleError):
        w2.plant_seat(qr)                                        # a real case
    q2, c2 = submitted_plant(w2, truth=False)
    with pytest.raises(RuleError):
        w2.plant_seat(q2)                                        # a dial's plant, not a planted approval
    check_all(w)
    check_all(w2)


def test_the_planted_verdicts_review_is_paid_nothing_and_a_members_review_on_the_same_batch_is():
    w = make_world()
    q, c = submitted_plant(w, approval=True)
    rid = planted_verdict(w, q)
    ra = w.assign_audit(q, "D")
    w.advance(w.t + 1)
    w.complete_review(ra, N, 2.0)                                # D rejects: stood; the third seat
    r3 = w.assign_appeal(q, "E")
    w.advance(w.t + 1)
    w.complete_review(r3, N, 2.0)                                # E holds the truth: stood; final N by truth
    w.advance(w.t + 2)
    assert c.tree_closed
    assert w.reviews[rid].fee == 0.0 and w.reviews[rid].fee_fixed == 0.0 and w.reviews[rid].status == "vested"
    assert w.reviews[ra].fee_fixed > 0 and w.reviews[r3].fee_fixed > 0   # the members' seats paid from the plant's pots
    assert w.ledger.wallet(PLANT_REV).W == pytest.approx(0.0)
    check_all(w)


# ------------------------------------------------------------ I43, I44 and I42's extension catch
def test_I43_I44_and_I42_catch_the_state_on_the_seat_a_fee_on_the_alias_a_lie_without_its_fee_and_a_burned_bond():
    w = make_world()
    q, c = submitted_plant(w, approval=True)
    rid = planted_verdict(w, q)
    check_all(w)
    c.plant_state_seats.append((w.t, "initial", N))
    with pytest.raises(InvariantError, match="I43"):
        check_all(w)
    c.plant_state_seats.pop()
    w.reviews[rid].fee_owed = 1.0
    with pytest.raises(InvariantError, match="I43"):
        check_all(w)
    w.reviews[rid].fee_owed = 0.0
    saved = w.reviews[rid].status
    w.reviews[rid].status = "overturned"
    with pytest.raises(InvariantError, match="I20|I42"):      # the planted verdict overturned: I20's planted clause catches it first, I42 behind
        check_all(w)
    w.reviews[rid].status = saved
    c.market_audit_only = True
    with pytest.raises(InvariantError, match="I43"):
        check_all(w)
    c.market_audit_only = False
    check_all(w)
    # a planted lie without its fee
    q2, c2 = submitted_plant(w, truth=False, worker="B")
    r2 = w.assign_initial(q2, "C")
    w.advance(w.t + 1)
    w.complete_review(r2, N, 2.0)
    w.respond(q2, "appeal", "the work meets the request")
    check_all(w)
    c2.plant_fee_destroyed = 0.0
    with pytest.raises(InvariantError, match="I42|I44"):     # I42's fee clause catches it first, I44's behind
        check_all(w)
    c2.plant_fee_destroyed = c2.D
    check_all(w)


# ------------------------------------------------------------ the discharge and the state's own work (2.9.0 §4 against 1.4.0 §2.2, I25)
def _states_own_work_approved_by_a_troop_and_disputed(hold_c=True):
    """The path §8.2's liar cell found: the state delivers (A and B committed, no free fundable member), a troop reviewer approves it
    (`market_audit_only`: the audit held for a member, 1.4.0 §2.2, I25) and the requester disputes the approval."""
    w = make_world(membership=False, plant_market=False, actors=["A", "B", "C"], duty=["C"], w_R=2, eps_T=0.0, T_review=100)
    for who in ("A", "B"):
        qq = w.post_root("H", 20)
        w.award(qq, who, 20, 30)
    held = w.assign_initial(w.create_plant(True, 20.0), "C")   # C, the one reviewer, holds an open review of a good plant
    q = w.post_root("H", 20)
    w.advance(w.t + w.p.w_A + 1)                             # unawarded for w_A with no free fundable member: the state delivers
    c = w.cases[q]
    assert w.is_troop(c.actor), c.state
    w.advance(c.deadline)
    w.submit(q)
    w.advance(w.t + w.p.w_R + 1)                             # the initial seat waits w_R with C busy: a troop reviewer takes it
    tr = next(w.reviews[x] for x in c.reviews if w.reviews[x].role == "initial" and w.is_troop(w.reviews[x].reviewer))
    w.complete_review(tr.id, F, 0.0)                         # a troop approves the state's own work
    assert c.market_audit_only and c.audit_obligation and w.audit_odds(q) == 1.0 and c.state == "PENDING"
    if not hold_c:
        w.complete_review(held, F, 0.0)                      # C comes free before the panel is seated
    w.dispute(q, "H", "the result does not meet the request")   # the requester disputes the state's approved work
    return w, q, c, held


def test_the_states_own_work_disputed_before_a_panel_of_the_states_alone_keeps_its_audit_seat_after_the_dispute():
    """Appendix V's second reading, ruled after run 39: where the dispute's panel on the state's own work was the state's alone, the audit
    seat is admitted after the dispute — the one challenge round (1.0.1 §8) yields to I25's purpose, the round existing to limit a
    participant's exposure and the state being none; a case is never left standing (before the ruling the engine held the obligation and
    the round refused the seat, the case pending with it — the eighteen liar-cell episodes the regression)."""
    w, q, c, held = _states_own_work_approved_by_a_troop_and_disputed(hold_c=True)
    w.advance(w.t + w.p.w_R + 1)                             # the panel seats wait w_R: two troop panelists
    panel = [w.reviews[x] for x in c.reviews if w.reviews[x].role == "appeal" and w.reviews[x].status == "open"]
    assert len(panel) == 2 and all(w.is_troop(r.reviewer) for r in panel)
    for r in panel:
        w.complete_review(r.id, F, 0.0)                      # the panel finds for the approval — the state's judgment alone
    assert c.challenge["resolved"] and c.state == "PENDING"
    assert c.audit_obligation and c.audit_after_dispute and w.state_work_audit_after_dispute == 1
    assert w.obligations_discharged_by_dispute == 0 and w.state_work_discharged_by_panel == 0
    assert any("the audit seat admitted after the dispute" in m for (_, m, _) in c.log)
    w.advance(c.window_end + 2)
    assert c.state == "PENDING" and c.audit_obligation and w.held_market_audit_now == 1   # I25: held for a member
    w.complete_review(held, F, 0.0)                          # C comes free: the one round yields for the state's own work
    ra = w.assign_audit(q, "C")
    w.advance(w.t + 1)
    w.complete_review(ra, F, 2.0)                            # the market's audit confirms
    assert not c.audit_obligation
    w.advance(w.t + 2)
    assert c.state == "VESTED"                               # vested after a member's audit, as I25 requires
    check_all(w)


def test_the_states_own_work_disputed_before_a_panel_with_a_member_on_it_is_discharged_as_a_members_audit_would():
    """Appendix V's second reading, ruled after run 39: a dispute's panel on the state's own work is the market's judgment where a member sat
    on it, and discharges I25's obligation as a member's audit would; the case vests at the window's close with no audit seat."""
    w, q, c, held = _states_own_work_approved_by_a_troop_and_disputed(hold_c=False)
    rc = w.assign_appeal(q, "C")                             # a member takes one panel seat
    w.advance(w.t + w.p.w_R + 1)                             # the other waits w_R: a troop
    panel = [w.reviews[x] for x in c.reviews if w.reviews[x].role == "appeal" and w.reviews[x].status == "open"]
    assert len(panel) == 2 and sum(1 for r in panel if w.is_troop(r.reviewer)) == 1
    for r in panel:
        w.complete_review(r.id, F, 2.0 if r.id == rc else 0.0)
    assert c.challenge["resolved"] and c.state == "PENDING"
    assert not c.audit_obligation and not c.audit_after_dispute and c.open_items == 0
    assert w.state_work_discharged_by_panel == 1 and w.obligations_discharged_by_dispute == 1 and w.period["obligations_discharged"] == 1
    assert any("a member sat on the dispute's panel" in m for (_, m, _) in c.log)
    with pytest.raises(RuleError):
        w.assign_audit(q, "C")                               # the round is spent as for any case: no audit seat
    w.advance(c.window_end + 3)
    assert c.state == "VESTED" and not any(w.reviews[x].role == "audit" for x in c.reviews)
    check_all(w)                                             # I25 accepts the panel with a member on it


def test_I21_reads_the_record_s_six_decimal_rounding_on_a_per_seat_step_and_still_catches_a_step_beyond_its_bound():
    """The half cell on the corrected engine (run 41, seed 36 under the direct policy): m^A stepped ×2 from 7.2727… to 14.5454… — exact in the
    engine — and I21, reading the period record's values rounded to six decimals (7.272727 → 14.545455) with a tolerance of 1e-6, failed the
    run. The step's bounds are read with a tolerance covering the rounding at both ends; a step beyond ×2 or under ×0.9 is still caught, as is
    the dial's own step on the same record (I21 called on a copy of the record — the record itself is hashed into the History at the close)."""
    from sim.invariants import I21_dial_and_reserve
    w = make_world(period_ticks=400, T_review=1000)
    w.m_A = 8.0 / 1.1                                             # 7.272727…, whose doubling rounds up at the sixth decimal
    w._seat_pool["A"] = [10, 10]                                  # a reading of 1.0 at the close: the step clamps at ×2
    w.advance(w.period["start"] + 401)
    per = w.periods[-1]
    assert per["m_A_before"] == 7.272727 and per["m_A"] == 14.545455 and w.m_A == pytest.approx(16.0 / 1.1)
    assert per["m_A"] > 2.0 * per["m_A_before"] + 1e-6           # the rounded pair reads over the bound at 1e-6
    check_all(w)                                                  # and I21 reads it within the record's rounding
    def fails(**over):
        w.periods[-1] = dict(per, **over)
        try:
            with pytest.raises(InvariantError, match="I21 (m_A|dial) step"):
                I21_dial_and_reserve(w)
        finally:
            w.periods[-1] = per
    fails(m_A=round(2.0 * per["m_A_before"] + 1e-4, 6))           # a step beyond ×2 on the record is still a failure
    fails(m_A=round(0.9 * per["m_A_before"] - 1e-4, 6))           # and under ×0.9
    w.periods[-1] = dict(per, m_before=1.818182, m=3.636364)      # the dial's own record on the same shape (3.6363… = 2 × 1.8181…)
    I21_dial_and_reserve(w)
    w.periods[-1] = per
    fails(m_before=1.818182, m=3.636464)
    check_all(w)

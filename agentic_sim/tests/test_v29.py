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
def test_the_dial_per_seat_steps_on_its_own_reading_and_moves_its_rate_alone():
    w = make_world(period_ticks=30)
    q, c = submitted_plant(w, approval=True)
    planted_verdict(w, q)
    ra = w.assign_audit(q, "D")
    w.advance(w.t + 1)
    w.complete_review(ra, F, 0.0)                                # F̂^A = 1 in this period
    m_before, pi_before, X_before = w.m_t, w.pi_t, w.X_t
    w.advance(w.t + 31)                                          # the period closes
    per = w.periods[-1]
    assert per["F_hat_A"] == 1.0 and per["m_A_before"] == 1.0 and per["m_A"] == 2.0   # the step capped at 2× a period
    assert w.pi_A == pytest.approx(min(w.p.pi_A_max, w.p.pi_A0 * 2.0)) and per["pi_A"] == pytest.approx(w.pi_A)
    assert per["F_hat_La"] is None and per["m_La"] == 1.0 and per["F_hat_Ld"] is None and per["m_Ld"] == 1.0   # undefined: unmoved
    assert w.m_t == m_before and w.pi_t == pi_before             # m^A moves its rate alone
    assert per["lie_quota"] == {"appeal": 2.0, "dispute": 2.0}   # no real challenge in the period: the floor
    check_all(w)


def test_the_planted_approvals_credit_counts_real_approvals_and_the_lie_quota_reads_the_trailing_period():
    w = make_world(budget=1e6, period_ticks=30)
    assert w.planted_approvals_due() == 0
    n = 0
    while w.planted_approvals_due() == 0:
        real_approved(w, worker=["A", "B"][n % 2], reviewer=["C", "D", "E", "F"][n % 4])
        n += 1
        for cc in list(w.cases.values()):                        # keep the workers free: let the approvals vest
            pass
        if n > 80:
            break
    assert w.planted_approvals_due() == 1 and n == 50            # 1 / π^A_0 = 50 real approvals
    assert w.period["real_approvals"] + sum(p.get("real_approvals", 0) for p in w.periods) == 50
    cred = w.planted_approval_credit
    q = w.post_plant(False, approval=True)
    assert w.planted_approvals_due() == 0 and w.planted_approval_credit == pytest.approx(cred - 1.0)
    # a real appeal in this period: the next period's lying-appeal quota is max(2, 0.25 × 1) = 2; eight real appeals → 2
    w2 = make_world(budget=1e6, period_ticks=20)
    for i in range(8):
        qq = w2.post_root("H", 20); w2.award(qq, ["A", "B"][i % 2], 20, 1); w2.advance(w2.t + 1); w2.submit(qq)
        rr = w2.assign_initial(qq, ["C", "D"][i % 2]); w2.advance(w2.t + 1); w2.complete_review(rr, N, 0.0)
        w2.respond(qq, "appeal", "the work meets the request")
        w2.advance(w2.t + 1)
    assert w2.period["real_appeals"] + sum(p.get("real_appeals", 0) for p in w2.periods) == 8
    w2.advance(w2.t + 25)
    assert w2.periods[-1]["lie_quota"]["appeal"] == pytest.approx(max(2.0, w2.pi_La * w2.periods[-1]["real_appeals"]))
    check_all(w)
    check_all(w2)


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

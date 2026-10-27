"""Design revision 16 — specification 2.8.0: the plants reach every seat (`Params.plants_every_seat`, on; off is 2.7.0).
A planted case lives the whole life of a real one past its initial verdict: its pending F is audited at the odds its reviewer
carried at the verdict (D), its actor appeals and its requester disputes (the instrument's filings; here by hand), it is
revised through `revise_plant` with the resubmitted truth sealed as a second marker (B), every verdict on it at every seat is
adjudicated by its truth the moment it is given — each reviewer once — and the case resolves by truth with no second overturn,
no court fee moving and no ruling; the markers are revealed at closure. The money (A): the court fee is destroyed at filing, the
pots are topped up to the seat's need (nothing until the third seat on the defaults), nothing minted for a plant reaches Ω. The
seat nobody is free to take (C): the orchestrator's own verdict at the troop's step, no fee, counted apart. I20 rewritten per
seat, I42 new. The six-actor world of test_v23 (the bank, the pool and the supply side on), plants built submitted (the 1.2.0
construction — the flag governs both constructions)."""
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
try:
    import pytest
except ImportError:  # plain `python3 run_tests.py`
    sys.path.insert(0, os.path.dirname(__file__))
    from _mini_pytest import pytest
from sim import Params, World, RuleError, InvariantError, Ledger, check_all
from sim.engine import F, N, P, BOT, PLANT, PLANT_REQ, PLANT_ACT

ACTORS = ["A", "B", "C", "D", "E", "F"]
DUTY = ["C", "D", "E", "F"]


def make_world(budget=1000.0, actors=ACTORS, duty=DUTY, **over):
    kw = dict(plant_market=False, E0=0.0, H=1e9, omega_rate=0.05, Omega0=100.0, duty_turn_reviews=10_000, duty_turn_ticks=100_000,
              r_s=1.0, T_s=10_000, pi0=0.0, period_ticks=60,
              panel_determined=False)   # 1.6.0 §2.4 off: six actors with no plant record may sit on panels here (as test_v12's world)
    kw.update(over)
    return World(Params(**kw), actors, humans={"H": budget}, on_duty=duty)


def omega(w):
    return w.ledger.wallet(Ledger.OMEGA).W


def plant_to(w, reviewer, truth, verdict, cost=0.0, B=20.0):
    """One plant to its initial verdict: created, assigned to `reviewer`, answered the next tick."""
    q = w.create_plant(truth, B)
    r = w.assign_initial(q, reviewer)
    w.advance(w.t + 1)
    w.complete_review(r, verdict, cost)
    return q, r


def events(w, cid):
    return [e for e in w.ledger.events if e.case == cid]


# ------------------------------------------------------------ the audit seat (§2.1, D)
def test_a_bad_plant_approved_stays_pending_and_is_audited_at_the_odds_of_the_verdict():
    w = make_world(membership=False, p_start=0.5)          # odds unpinned so that the doubling is visible
    om0 = omega(w)
    assert w.actors["C"].p_eff == pytest.approx(0.5)
    q, r = plant_to(w, "C", False, F)                       # a stamp on a bad plant
    c = w.cases[q]
    assert c.plant_outcome == "failure" and w.reviews[r].status == "overturned" and w.reviews[r].plant_outcome == "failure"
    assert c.state == "PENDING" and c.window_end == c.t_verdict + w.p.W   # 2.8.0: pending with its window, not final N at once (1.2.0)
    assert c.plant_reveal_hseq is None                       # the marker sealed until closure
    assert w.actors["C"].p_eff == pytest.approx(1.0)        # the adjudication doubled C's odds ...
    assert c.audit_odds_at_verdict == pytest.approx(0.5) and w.audit_odds(q) == pytest.approx(0.5)   # ... the roll reads the odds at the verdict (D)
    assert w.period["approvals"] == 1 and w.period["audit_demand"] == pytest.approx(0.5)   # the reserve's demand counts the plant's pending F (§5)
    w.roll_audit(q)                                          # admitted (1.2.0 refused it)
    assert c.audit_obligation
    ra = w.assign_audit(q, "D")
    w.advance(w.t + 1)
    w.complete_review(ra, F, 0.0)                            # the auditor stamps too: a plant failure at the audit seat — the seat priced
    assert w.reviews[ra].plant_outcome == "failure" and w.reviews[ra].status == "overturned"
    assert w.actors["D"].plant_bad[-1][1] is True and c.plant_outcome == "failure"   # C adjudicated once; D for its own verdict
    assert c.state == "PENDING" and not c.audit_obligation and c.challenge is None   # the audit agreed: held to the window
    assert w.period["plants"] == 1 and w.period["plant_seats"]["initial"] == 1 and w.period["plant_seats"]["audit"] == 1   # the dial's clock: initial only
    assert w.period["plant_seat_failures"]["audit"] == 1
    w.advance(c.window_end + 1)
    assert c.state == "FINAL_N" and c.final and c.grade == PLANT          # the vesting step finalizes a bad plant N by truth
    assert c.plant_reveal_hseq is not None                                 # revealed at closure
    reveal = w.history.entries[c.plant_reveal_hseq]
    assert reveal["kind"] == "plant_revealed" and reveal["payload"]["truth"] == "bad" and len(reveal["payload"]["reviews"]) == 2
    w.advance(w.t + 1)
    assert c.tree_closed and omega(w) == pytest.approx(om0)               # nothing minted for the plant reached Ω
    assert w.ledger.wallet(PLANT_REQ).W == pytest.approx(0.0) and w.ledger.wallet(PLANT_ACT).W == pytest.approx(0.0)
    check_all(w)


def test_every_case_rolls_at_the_odds_its_reviewer_carried_at_the_verdict():
    w = make_world(membership=False, p_start=0.5)
    q = w.post_root("H", 20)
    w.award(q, "A", 20, 1)
    w.advance(1)
    w.submit(q)
    r = w.assign_initial(q, "C")
    w.advance(2)
    w.complete_review(r, F, 0.0)                             # a real approval at odds 0.5
    assert w.cases[q].audit_odds_at_verdict == pytest.approx(0.5)
    qp = w.create_plant(False, 20.0)
    rp = w.assign_initial(qp, "C")
    w.advance(3)
    w.complete_review(rp, F, 0.0)                            # C overturned on a plant in the same tick: live odds doubled
    assert w.actors["C"].p_eff == pytest.approx(1.0)
    assert w.audit_odds(q) == pytest.approx(0.5)             # the real case rolls at the verdict's odds — one number, one path (the ruling at acceptance)
    w2 = make_world(membership=False, p_start=0.5, plants_every_seat=False)
    q2 = w2.post_root("H", 20); w2.award(q2, "A", 20, 1); w2.advance(1); w2.submit(q2); r2 = w2.assign_initial(q2, "C"); w2.advance(2)
    w2.complete_review(r2, F, 0.0)
    w2.actors["C"].p_audit = 1.0
    assert w2.audit_odds(q2) == pytest.approx(1.0)           # the flag off: 2.7.0's live read
    check_all(w)


# ------------------------------------------------------------ the third seat, by truth (§2.2)
def test_an_audit_that_disagrees_seats_a_third_reviewer_and_the_case_resolves_by_truth_with_no_ruling():
    w = make_world()
    om0 = omega(w)
    q, r = plant_to(w, "C", False, F)                       # a bad plant stamped
    c = w.cases[q]
    w.roll_audit(q)
    ra = w.assign_audit(q, "D")
    w.advance(w.t + 1)
    w.complete_review(ra, N, 2.0)                            # the careful auditor rejects: stood, and the audit disagrees
    assert w.reviews[ra].plant_outcome == "stood" and w.reviews[ra].status == "done"
    assert c.challenge is not None and c.challenge["kind"] == "audit" and not c.challenge["resolved"]   # the real path's seat-opening
    assert c.court_fee_paid_by is None                       # no challenger, no fee (an audit's disagreement)
    r3 = w.assign_appeal(q, "E")
    w.advance(w.t + 1)
    w.complete_review(r3, F, 0.0)                            # the third seat stamps: a plant failure
    assert w.reviews[r3].plant_outcome == "failure" and w.reviews[r3].status == "overturned"
    assert c.challenge["resolved"] and c.challenge["by"] == "truth" and c.challenge["outcome"] == N
    assert c.state == "FINAL_N"                              # resolved by truth: a bad plant is final N
    assert w.reviews[r].status == "overturned" and len(w.actors["C"].plant_bad) == 1   # the initial reviewer adjudicated once, not again
    with pytest.raises(RuleError):
        w.rule(q, N)                                         # no ruling is sought on a plant
    assert w.period["plant_seats"] == {"initial": 1, "audit": 1, "third": 1, "appeal": 0, "dispute": 0, "resumed": 0, "state": 0}
    assert w.plant_seat_adjudications["third"] == {"stood": 0, "failure": 1}
    w.advance(w.t + 1)
    assert c.tree_closed and omega(w) == pytest.approx(om0) and c.omega_advance == 0.0
    check_all(w)


# ------------------------------------------------------------ the appeal and the dispute (§2.1, A)
def test_the_plant_actor_appeals_a_good_plants_rejection_with_the_fee_destroyed_and_nothing_reaching_omega():
    w = make_world()
    om0 = omega(w)
    q, r = plant_to(w, "C", True, N)                         # a careful reviewer misreads a good plant: a plant failure (1.2.0's mirror)
    c = w.cases[q]
    minted0, destroyed0 = w.bank_minted["mint_plant"], w.bank_destroyed["retire_plant"]
    assert c.plant_outcome == "failure" and c.state == "AWAITING_RESPONSE"   # the plant actor may appeal, as a real actor may
    assert w.ledger.wallet(c.actor).U == pytest.approx(0.0)  # the plant actor's alias holds nothing unlocked ...
    w.respond(q, "appeal", "the work meets the request")     # ... and the bank funds the fee, destroyed at filing
    assert w.bank_minted["mint_plant"] - minted0 == pytest.approx(c.D) and w.bank_destroyed["retire_plant"] - destroyed0 == pytest.approx(c.D)
    assert c.court_fee_paid_by == c.actor and c.court_fee_reimbursed == 0.0 and omega(w) == pytest.approx(om0)
    fee = [e for e in events(w, q) if e.kind == "retire_plant" and "court fee" in e.note]
    assert len(fee) == 1 and fee[0].amount == pytest.approx(c.D)
    assert c.state == "PENDING" and c.challenge["kind"] == "appeal" and c.challenge["challenger"] == c.actor
    r1, r2 = w.assign_appeal(q, "D"), w.assign_appeal(q, "E")
    w.advance(w.t + 1)
    w.complete_review(r1, F, 2.0)                            # D approves: stood
    w.complete_review(r2, N, 0.0)                            # E stamps-rejects: a plant failure
    assert w.reviews[r1].plant_outcome == "stood" and w.reviews[r2].plant_outcome == "failure"
    assert c.challenge["resolved"] and c.challenge["by"] == "truth" and c.challenge["outcome"] == F and c.state == "PENDING"
    assert c.court_fee_reimbursed == 0.0                     # no bond pays D back to a plant's challenger
    w.advance(c.window_end + 2)
    assert c.state == "VESTED" and c.tree_closed             # a good plant vests by truth
    assert omega(w) == pytest.approx(om0)                    # nothing minted for the plant reached Ω
    assert w.reviews[r1].status == "vested" and w.reviews[r1].fee > 0   # the stood panelist paid from the pots
    check_all(w)


def test_the_plant_requester_disputes_a_bad_plants_approval_and_the_panel_is_adjudicated_by_truth():
    w = make_world()
    om0 = omega(w)
    q, r = plant_to(w, "C", False, F)
    c = w.cases[q]
    with pytest.raises(RuleError):
        w.dispute(q, "H", "x")                               # only the case's requester — the plant requester's fresh name
    w.dispute(q, c.requester, "the result does not meet the request")
    assert c.challenge["kind"] == "dispute" and c.court_fee_paid_by == c.requester and omega(w) == pytest.approx(om0)
    r1, r2 = w.assign_appeal(q, "D"), w.assign_appeal(q, "E")
    w.advance(w.t + 1)
    w.complete_review(r1, N, 2.0)                            # stood
    w.complete_review(r2, F, 0.0)                            # a plant failure at the dispute panel — the seat priced
    assert w.reviews[r2].plant_outcome == "failure" and c.state == "FINAL_N" and c.challenge["by"] == "truth"
    assert w.period["plant_seats"]["dispute"] == 2 and w.period["plant_seat_failures"]["dispute"] == 1
    w.advance(w.t + 1)
    assert c.tree_closed and omega(w) == pytest.approx(om0)
    check_all(w)


def test_the_pots_are_topped_up_to_the_seats_need_and_only_at_the_third_seat_on_the_defaults():
    w = make_world()
    q, r = plant_to(w, "C", False, F)                       # the initial seat: no top-up
    c = w.cases[q]
    minted0 = w.bank_minted["mint_plant"]
    w.roll_audit(q)
    ra = w.assign_audit(q, "D")                              # the second seat: φ^E = 2K and φ^F = f(1 + 1.5) already pay for it
    assert w.bank_minted["mint_plant"] == pytest.approx(minted0)
    w.advance(w.t + 1)
    w.complete_review(ra, N, 3.0)                            # careful, cost 3 from the allowance
    r3 = w.assign_appeal(q, "E")                             # the third seat: the fee pot's shortfall is minted (owed 2 + 3 + 3 = 8 against 5)
    assert w.bank_minted["mint_plant"] - minted0 == pytest.approx(3.0)
    assert w.ledger.pool(q).fee_pot == pytest.approx(8.0) and w.period["plant_top_ups"] == pytest.approx(3.0)
    w.advance(w.t + 1)
    w.complete_review(r3, N, 3.0)                            # the third careful seat is reimbursed from the allowance, never Ω's advance
    assert c.omega_advance == 0.0 and not any("Ω advance" in e.note for e in events(w, q))
    assert w.reviews[r3].reimbursed == pytest.approx(3.0)
    w.advance(w.t + 2)
    assert c.tree_closed and w.ledger.pool(q).deposit == pytest.approx(0.0) and w.ledger.pool(q).fee_pot == pytest.approx(0.0)   # the remainder destroyed
    check_all(w)


# ------------------------------------------------------------ the resubmission seat (§2.1, B)
def test_a_P_on_a_plant_is_spent_unless_revised_and_a_revision_seals_a_second_marker():
    w = make_world()
    q, r = plant_to(w, "C", False, P)
    c = w.cases[q]
    assert c.plant_outcome is None and c.state == "AWAITING_RESPONSE" and w.actors["C"].open_review == r   # the reviewer attached (§6)
    with pytest.raises(RuleError):
        w.revise_plant(q, "good")                            # the truth is a bool
    w.respond(q, "accept")                                   # the instrument's window of real revisions is empty: spent, as 1.2.0 had it
    assert c.plant_outcome == "spent" and c.state == "FINAL_N" and w.actors["C"].plant_bad == [] and w.actors["C"].open_review is None
    w.advance(w.t + 1)
    assert w.reviews[r].status == "vested"                  # the review stands and is paid
    # a revision: the resubmitted truth drawn by the instrument, sealed as the second marker; the same reviewer resumes against it
    q2, r2 = plant_to(w, "D", False, P)
    c2 = w.cases[q2]
    n_hist = len(w.history.entries)
    w.revise_plant(q2, True)                                 # the instrument's draw: the revision is good
    assert c2.plant_revised is True and c2.plant_revised_commit is not None and c2.resubmitted and c2.state == "SUBMITTED"
    assert w.history.entries[c2.plant_revised_hseq]["kind"] == "plant_revised" and c2.plant_revised_hseq >= n_hist
    assert "good" not in str(w.history.entries[c2.plant_revised_hseq]["payload"])   # sealed: the commitment, not the truth
    assert w.reviews[r2].status == "open" and w.reviews[r2].resumed
    with pytest.raises(RuleError):
        w.revise_plant(q2, False)                            # one revision only
    with pytest.raises(RuleError):
        w.complete_review(r2, P, 0.0)                        # a resumed review answers F or N
    w.advance(w.t + 1)
    w.complete_review(r2, F, 0.0)                            # D stamps the resumed review: right against the revised truth
    assert w.reviews[r2].plant_outcome == "stood" and w.reviews[r2].plant_truth is True and c2.plant_outcome == "stood"
    assert w.actors["D"].plant_good[-1][1] is False and w.period["plant_seats"]["resumed"] == 1 and w.period["plants"] == 1
    w.advance(c2.window_end + 2)
    assert c2.state == "VESTED" and c2.tree_closed
    payload = w.history.entries[c2.plant_reveal_hseq]["payload"]
    assert payload["revised"]["truth"] == "good" and payload["revised"]["commit"] == c2.plant_revised_commit and payload["truth"] == "bad"
    with pytest.raises(RuleError):
        w.revise_plant(q2, True)                             # not after a verdict
    check_all(w)


# ------------------------------------------------------------ the seat the state takes (§2.1, C)
def test_the_orchestrators_own_verdict_takes_a_plants_seat_past_w_R_with_no_fee_and_no_troop():
    w = make_world(membership=False, actors=["A", "B", "C"], duty=["C"], w_R=2, eps_T=0.0)
    for who in ("A", "B"):                                   # A and B committed on long deliveries: nobody but C can take a seat
        qq = w.post_root("H", 20)
        w.award(qq, who, 20, 30)
    om0 = omega(w)                                           # after the real awards' fees
    q, r = plant_to(w, "C", False, F)                       # C, the one reviewer free, stamps a bad plant
    c = w.cases[q]
    w.roll_audit(q)                                          # nobody free and eligible: C is excluded from its own case
    t0 = w.t
    w.advance(t0 + w.p.w_R)                                  # the seat has waited w_R seating steps at the seating of t0 + w_R − 1
    assert c.plant_state_seats and c.plant_state_seats[0][1] == "audit" and c.plant_state_seats[0][2] == N   # the truth (ε_T 0)
    assert not c.audit_obligation and c.challenge is not None and c.challenge["kind"] == "audit" and c.challenge["state_verdicts"]
    assert len(w.troops) == 0 and w.plant_seats_at_state == 1   # no troop, no fee, no loan, no place; counted apart
    w.advance(w.t + w.p.w_R)
    assert len(c.plant_state_seats) == 2 and c.plant_state_seats[1][1] == "appeal"   # the third seat the same
    assert c.challenge["resolved"] and c.challenge["by"] == "truth" and c.state == "FINAL_N"
    assert w.plant_seats_at_state == 2 and w.period["plant_seats"]["state"] == 2 and len(w.troops) == 0
    w.advance(w.t + 1)
    assert c.tree_closed and omega(w) == pytest.approx(om0)
    check_all(w)


# ------------------------------------------------------------ the flag off is 2.7.0; the refusals kept
def test_the_flag_off_is_2_7_0_and_the_kept_refusals():
    w = make_world(plants_every_seat=False)
    q, r = plant_to(w, "C", False, F)
    c = w.cases[q]
    assert c.state == "FINAL_N" and c.plant_outcome == "failure" and c.plant_reveal_hseq is not None   # 1.2.0: final N at the verdict, revealed then
    for op in (lambda: w.roll_audit(q), lambda: w.assign_audit(q, "D"), lambda: w.dispute(q, c.requester, "x"), lambda: w.revise_plant(q, True)):
        with pytest.raises(RuleError):
            op()
    w2 = make_world()
    q2, r2 = plant_to(w2, "C", False, F)
    c2 = w2.cases[q2]
    for op in (lambda: w2.override(q2, "H", N), lambda: w2.accept_explicit(q2, c2.requester), lambda: w2.rule(q2, N)):
        with pytest.raises(RuleError):
            op()                                             # a human's override and an explicit acceptance stay outside the construction
    check_all(w); check_all(w2)


# ------------------------------------------------------------ I20 and I42 catch
def test_I20_and_I42_catch_a_reveal_before_closure_a_reimbursed_fee_and_an_advance_on_a_plant():
    w = make_world()
    q, r = plant_to(w, "C", False, F)
    c = w.cases[q]
    check_all(w)
    c.court_fee_reimbursed, c.court_fee_paid_by = 1.0, c.requester
    with pytest.raises(InvariantError, match="I20"):
        check_all(w)
    c.court_fee_reimbursed, c.court_fee_paid_by = 0.0, None
    saved = w.reviews[r].plant_outcome
    w.reviews[r].plant_outcome = None
    with pytest.raises(InvariantError, match="I20"):
        check_all(w)
    w.reviews[r].plant_outcome = saved
    c.plant_reveal_hseq = 0
    with pytest.raises(InvariantError, match="I20"):
        check_all(w)
    c.plant_reveal_hseq = None
    c.omega_advance = 1.0
    with pytest.raises(InvariantError, match="I42"):
        check_all(w)
    c.omega_advance = 0.0
    saved_odds = c.audit_odds_at_verdict
    c.audit_odds_at_verdict = None
    with pytest.raises(InvariantError, match="I42"):
        check_all(w)
    c.audit_odds_at_verdict = saved_odds
    check_all(w)


# ------------------------------------------------------------ the public view: no plant entry before the reveal (the ruling after run 37)
def test_the_public_view_of_a_plants_log_carries_no_plant_entry_until_its_closure():
    """2.8.0 §2.1: the markers are revealed at closure and not before. The `log` tell-reader (§8.7, by hand) read the engine's `plant:`
    entries from a plant's earlier seat through the Public view's case(cid).log and so read every plant at every later seat — a
    conformance item of the view, ruled after run 37. The History keeps every entry (I16 unchanged); the view carries none of a plant's
    plant entries until the reveal. The reader (the driver's predicate, verbatim) reads nothing at every seat — the audit, the third,
    the appeal, the dispute, the resumed, the state's — and equals the same reader with no tell; a real root's log is untouched; at
    closure the whole log is shown."""
    from drivers.view import Public

    def log_tell(pub, cid):                                  # drivers/stamping.py read_tells, the `log` tell
        return any(msg.startswith("plant") for (_, msg, _) in pub.case(cid).log)

    def no_tell(pub, cid):                                   # the same reader with no tell: every case read as real
        return False

    def plant_free(pub, cid):                                # nothing of the plant in the view's log, by any of the engine's wordings
        return not any(m.startswith(("plant", "the orchestrator's own verdict", "the state's audit verdict")) for (_, m, _) in pub.case(cid).log)

    def engine_has_plant_entry(w, cid):
        return any(m.startswith("plant") for (_, m, _) in w.cases[cid].log)

    # the audit seat and the third seat: a bad plant stamped, rolled, audited; the audit disagrees; the third seat resolves by truth
    w = make_world()
    pub = Public(w)
    real = w.post_root("H", 20)
    w.award(real, "A", 20, 3)
    q, r = plant_to(w, "C", False, F)
    c = w.cases[q]
    assert engine_has_plant_entry(w, q) and not log_tell(pub, q) and plant_free(pub, q)      # the first verdict's adjudication: in the History, not the view
    assert len(pub.case(q).log) < len(c.log) and [e[2] for e in pub.case(q).log] == [e[2] for e in c.log if not e[1].startswith("plant")]
    assert list(pub.case(real).log) == list(w.cases[real].log)                                # a real root's log untouched
    w.roll_audit(q)
    ra = w.assign_audit(q, "D")
    w.advance(w.t + 1)
    assert log_tell(pub, q) == no_tell(pub, q) == False and plant_free(pub, q)                # the audit seat
    w.complete_review(ra, N, 2.0)
    r3 = w.assign_appeal(q, "E")
    w.advance(w.t + 1)
    assert log_tell(pub, q) == no_tell(pub, q) == False and plant_free(pub, q)                # the third seat
    w.complete_review(r3, F, 0.0)
    assert c.state == "FINAL_N" and c.plant_reveal_hseq is not None                           # resolved by truth: final N, the markers revealed
    assert list(pub.case(q).log) == list(c.log) and log_tell(pub, q)                          # revealed at closure: the whole log
    w.advance(w.t + 1)
    assert c.tree_closed and list(pub.case(q).log) == list(c.log)
    check_all(w)                                                                             # I16: the History holds every entry

    # the appeal seat: a good plant rejected, the plant actor appeals
    w = make_world()
    pub = Public(w)
    q, r = plant_to(w, "C", True, N)
    w.respond(q, "appeal", "the work meets the request")
    r1, r2 = w.assign_appeal(q, "D"), w.assign_appeal(q, "E")
    w.advance(w.t + 1)
    assert engine_has_plant_entry(w, q) and log_tell(pub, q) == no_tell(pub, q) == False and plant_free(pub, q)
    w.complete_review(r1, F, 2.0)
    w.complete_review(r2, N, 0.0)
    assert plant_free(pub, q)
    check_all(w)

    # the dispute seat: a bad plant approved, the plant requester disputes
    w = make_world()
    pub = Public(w)
    q, r = plant_to(w, "C", False, F)
    w.dispute(q, w.cases[q].requester, "the result does not meet the request")
    r1, r2 = w.assign_appeal(q, "D"), w.assign_appeal(q, "E")
    w.advance(w.t + 1)
    assert engine_has_plant_entry(w, q) and log_tell(pub, q) == no_tell(pub, q) == False and plant_free(pub, q)
    w.complete_review(r1, N, 2.0)
    w.complete_review(r2, F, 0.0)
    w.advance(w.t + 1)
    assert w.cases[q].tree_closed and list(pub.case(q).log) == list(w.cases[q].log)
    check_all(w)

    # the resumed seat: a P on a plant, revised through revise_plant; the same reviewer resumes
    w = make_world()
    pub = Public(w)
    q, r = plant_to(w, "D", False, P)
    w.revise_plant(q, True)
    assert any(m.startswith("plant revised") for (_, m, _) in w.cases[q].log)
    w.advance(w.t + 1)
    assert log_tell(pub, q) == no_tell(pub, q) == False and plant_free(pub, q)
    w.complete_review(r, F, 0.0)
    check_all(w)

    # the state's seat: nobody free for the audit; the orchestrator's own verdict, its note in the History alone
    w = make_world(membership=False, actors=["A", "B", "C"], duty=["C"], w_R=2, eps_T=0.0)
    pub = Public(w)
    for who in ("A", "B"):
        qq = w.post_root("H", 20)
        w.award(qq, who, 20, 30)
    q, r = plant_to(w, "C", False, F)
    w.roll_audit(q)
    w.advance(w.t + w.p.w_R)
    c = w.cases[q]
    assert c.plant_state_seats and any(m.startswith("the orchestrator's own verdict") for (_, m, _) in c.log)
    assert log_tell(pub, q) == no_tell(pub, q) == False and plant_free(pub, q)
    w.advance(w.t + w.p.w_R + 1)
    assert c.tree_closed and list(pub.case(q).log) == list(c.log)
    check_all(w)


# ------------------------------------------------------------ the public view shows a plant as a real case until the reveal (the conformance pass after run 37)
def test_the_public_surface_carries_nothing_the_engine_writes_about_a_plant_before_its_reveal():
    """The ruling after run 37's second part: `_public_log`'s principle at every public accessor. Before the reveal a plant's case shows a
    real root's values on every plant field, its reviews show no plant outcome, the ledger copy's plant writes carry no case and no note
    (the money and the positions kept), while the engine holds all of it and the orchestrator's road (`plant_record`) reads it whole; at
    the reveal everything is shown. The alias names stay (the disguise's stated boundary); `review(rid).reviewer` stays (the harness's)."""
    from drivers.view import Public, _PLANT_FIELD_DEFAULTS
    w = make_world()
    pub = Public(w)
    real = w.post_root("H", 20)
    w.award(real, "A", 20, 3)
    q, r = plant_to(w, "C", False, F)                       # a bad plant stamped: adjudicated, PENDING, unrevealed
    c = w.cases[q]
    assert c.plant is False and c.plant_outcome == "failure" and c.plant_commit and c.plant_adjudications and c.plant_reveal_hseq is None
    v = pub.case(q)
    for name, default in _PLANT_FIELD_DEFAULTS.items():
        got = getattr(v, name)
        assert got == (list(default) if isinstance(default, tuple) else default), (name, got)
        assert getattr(pub.case(real), name) == getattr(w.cases[real], name)    # a real root's fields pass through
    assert v.plant is None and v.grade is None and v.plant_adjudications == [] and v.plant_outcome is None
    assert v.requester == c.requester and v.actor == c.actor                    # the aliases stay: the stated boundary
    assert pub.review(r).plant_outcome is None and pub.review(r).plant_truth is None and w.reviews[r].plant_outcome == "failure"
    assert pub.review(r).reviewer == "C" and pub.review(r).verdict == F         # the harness's reviewer field stays
    pr = pub.plant_record(q)                                                     # the orchestrator's road: whole, before the reveal
    assert pr.plant is False and pr.plant_outcome == "failure" and pr.plant_commit == c.plant_commit and len(pr.plant_adjudications) == 1
    with pytest.raises(RuleError):
        pub.plant_record(real)
    evs, raw = pub.events_since(0), w.ledger.events
    assert len(evs) == len(raw) and all(k.seq == e.seq and k.amount == e.amount and k.kind == e.kind for k, e in zip(evs, raw))
    writes = [(k, e) for k, e in zip(evs, raw) if e.case == q and (e.kind in ("mint_plant", "retire_plant") or e.note.startswith("plant"))]
    assert writes and all(k.case is None and k.note == "" for k, e in writes)   # the money, not the case
    others = [(k, e) for k, e in zip(evs, raw) if e.case == q and not (e.kind in ("mint_plant", "retire_plant") or e.note.startswith("plant"))]
    assert others and all(k.case == pub.case(q).id and k.note == e.note for k, e in others)   # a plant's ordinary events as a real case's
    assert all(k.case == pub.case(real).id and k.note == e.note for k, e in zip(evs, raw) if e.case == real)
    # the plant's dispute, its panel: the review proxies of the later seats masked too
    w.dispute(q, c.requester, "the result does not meet the request")
    r1, r2 = w.assign_appeal(q, "D"), w.assign_appeal(q, "E")
    w.advance(w.t + 1)
    w.complete_review(r1, N, 2.0)
    w.complete_review(r2, F, 0.0)
    assert c.state == "FINAL_N" and c.plant_reveal_hseq is not None            # resolved by truth: revealed
    v = pub.case(q)
    assert v.plant is False and v.plant_outcome == "failure" and v.grade == c.grade and list(v.plant_adjudications) == list(c.plant_adjudications)
    assert pub.review(r2).plant_outcome == "failure" and pub.review(r1).plant_outcome == "stood"
    evs = pub.events_since(0)
    assert all(k.case == pub.case(q).id and k.note == e.note for k, e in zip(evs, w.ledger.events) if e.case == q)   # shown at the reveal
    check_all(w)

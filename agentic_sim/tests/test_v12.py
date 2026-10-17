"""Design revision 2 — specification 1.2.0: the loop's own clock (asserted on the 1.2.1 engine: `Params`
with membership, the duty fund and netted plant capital off — design revision 3's additions are `test_v13`).

The worked example of §6 of the revision and the properties it introduces: planted work
adjudicated by its known truth (§2.1), the plant record with its two eligibility tiers and the
suspension that persists through its record (§2.2), the effort dial with its clamps, the reserve
sized to demand and allowed to run short, the capital cap and the alarm (§2.3), the newcomer
defaults (§2.4), the reviewer's view without the actor (§14 amended), the plant grade, and
invariants I20 and I21. Every figure here is the one §6 states; the engine reproduces it.

The one implementer's reading is documented at `World._rotate`: a record that still fails at the
end of a suspension cannot have changed (a suspended actor judges no plants), so the actor is
readmitted on probation until its next plant re-checks the record, rather than suspended for ever.
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
from sim.engine import F, N, P, BOT, PLANT, PLANT_REQ, PLANT_ACT

ACTORS = ["A", "B", "C", "D", "E", "F"]
DUTY = ["C", "D", "E", "F"]


def make_world(budget=1000.0, **over):
    # no emission, no service fee, Ω holds 100 as §6 has it; duty turns long enough that only the
    # revision's own rules move actors on and off duty
    # The 1.2.1 engine: membership, the duty fund and netted plant capital are design revision 3 (1.3.0,
    # `test_v13`); here they are off, as `drivers.stamping --rules 1.2.0` runs them for a control.
    kw = dict(E0=0.0, H=1e9, omega_rate=0.0, Omega0=100.0, duty_turn_reviews=10_000, duty_turn_ticks=100_000,
              membership=False, duty_fund=False, net_plant_capital=False)
    kw.update(over)
    return World(Params(**kw), ACTORS, humans={"H": budget}, on_duty=DUTY)


def omega_total(w):
    """Ω's money wherever it sits: its wallet, the two system wallets, and any plant's pools."""
    L = w.ledger
    pools = sum(L.pools[c.id].total for c in w.cases.values() if c.plant is not None and c.id in L.pools)
    return L.wallet(Ledger.OMEGA).W + L.wallet(PLANT_REQ).W + L.wallet(PLANT_ACT).W + pools


def plant_to(w, reviewer, truth, verdict, cost=0.0, B=20.0):
    """One plant through its adjudication: created, assigned to `reviewer`, answered next tick."""
    q = w.create_plant(truth, B)
    r = w.assign_initial(q, reviewer)
    w.advance(w.t + 1)
    w.complete_review(r, verdict, cost)
    return q, r


# ------------------------------------------------------------------ §6 worked example
def test_a_bad_plant_to_a_stamper_costs_omega_nothing_and_burns_the_bond():
    w = make_world()
    assert w.W(Ledger.OMEGA) == pytest.approx(100)
    q, r = plant_to(w, "C", False, F)              # C stamps a bad plant
    c = w.cases[q]
    assert c.plant is False and c.plant_outcome == "failure" and w.reviews[r].status == "overturned"
    assert w.W("C") == pytest.approx(45)           # bond 5 burned
    assert w.actors["C"].o == 1 and w.actors["C"].plant_bad == [(1, True)]
    assert w.actors["C"].a_hat == pytest.approx(2 / 3) and w.actors["C"].duty_eligible   # undetermined: n < n_min
    assert c.state == "FINAL_N" and c.grade == PLANT and c.tree_closed
    assert omega_total(w) == pytest.approx(100) and w.W(Ledger.OMEGA) == pytest.approx(100)   # net cost 0; swept back
    assert w.ledger.M == pytest.approx(w.p.M0 - 5)                                           # supply fell by the bond
    check_all(w)


def test_a_bad_plant_to_a_careful_reviewer_costs_omega_the_inspection():
    w = make_world()
    q, r = plant_to(w, "D", False, N, cost=3)      # D inspects (3) and rejects: stood
    c = w.cases[q]
    assert c.plant_outcome == "stood" and w.actors["D"].plant_bad == [(1, False)]
    assert w.W("D") == pytest.approx(50)           # cost 3 reimbursed from the allowance at completion
    w.advance(w.t + 1)                             # the N review settles in the next tick's batch
    assert w.reviews[r].status == "vested" and w.reviews[r].fee_fixed == pytest.approx(2)
    assert w.W("D") == pytest.approx(52)           # fee 2 (E0 = 0: no emission share here)
    assert c.allowance_refunded == pytest.approx(7) and c.pot_refunded == pytest.approx(3)
    assert omega_total(w) == pytest.approx(95)     # Ω's net cost: 3 + 2
    assert w.W(Ledger.OMEGA) == pytest.approx(95)  # and all of it swept back to Ω's wallet at closure
    check_all(w)


def test_four_bad_plants_later_the_stamper_is_suspended_and_the_careful_reviewer_keeps_both_tiers():
    w = make_world()
    for _ in range(3):
        plant_to(w, "C", False, F)
        plant_to(w, "D", False, N, cost=3)
    assert w.actors["C"].duty_eligible                                 # three of a kind: still undetermined
    plant_to(w, "C", False, F)                                          # the fourth
    C = w.actors["C"]
    assert C.a_hat == pytest.approx(5 / 6) and not C.duty_eligible and not C.panel_eligible
    assert C.suspended_until == w.t + w.p.T_susp and not C.on_duty    # left duty as the review completed
    w.advance(w.t + 1)
    on_duty = sorted(a.id for a in w.actors.values() if a.on_duty)
    assert len(on_duty) == 4 and "C" not in on_duty and "A" in on_duty   # the free actor with the lowest κ seated
    plant_to(w, "D", False, N, cost=3)
    D = w.actors["D"]
    assert D.a_hat == pytest.approx(1 / 6) and D.duty_eligible and D.panel_eligible
    # had D slipped once in four: 2/6 = 0.33 — on duty, off panels
    w2 = make_world()
    for v in (N, N, N, F):
        plant_to(w2, "D", False, v, cost=3)
    D2 = w2.actors["D"]
    assert D2.a_hat == pytest.approx(2 / 6) and D2.duty_eligible and not D2.panel_eligible
    check_all(w)
    check_all(w2)


def test_the_dial_doubles_at_most_and_moves_the_plant_rate_the_audit_odds_and_the_service_fee():
    """A period of four adjudicated plants, three bad, two approved: F̂ = 0.67 against F* = 0.10,
    ratio 6.7, clamped to ×2. Then π_t = 0.2, p_eff doubles, ω_t = 10% of B; the dial eases 10% a
    period while F̂ is below target and never goes below 1."""
    w = make_world(period_plants=4, period_ticks=10_000, omega_rate=0.05, Omega0=1000.0)
    plant_to(w, "C", False, F)
    plant_to(w, "D", False, N, cost=3)
    plant_to(w, "C", False, F)
    plant_to(w, "E", True, F)
    assert w.m_t == 1.0 and w.periods == []
    w.advance(w.t + 1)                             # the period closes at the tick's end
    per = w.periods[-1]
    assert per["plants"] == 4 and per["bad"] == 3 and per["bad_approved"] == 2
    assert per["F_hat"] == pytest.approx(2 / 3) and per["m_before"] == 1.0 and per["m"] == 2.0 and w.m_t == 2.0
    assert w.pi_t == pytest.approx(0.2)
    w.actors["F"].p_audit = 0.25
    assert w.actors["F"].p_eff == pytest.approx(0.5) and w.actors["D"].p_eff == 1.0   # min(1, m p)
    q = w.post_root("H", 20)
    w.award(q, "A", 20, 3)
    assert w.cases[q].omega == pytest.approx(0.05 * 2 * 20)                           # ω_t = ω_0 m_t
    # an honest period: F̂ = 0 → eases 10%; and another with no bad plant adjudicated holds
    for _ in range(4):
        plant_to(w, "D", False, N, cost=3)
    w.advance(w.t + 1)
    assert w.m_t == pytest.approx(1.8) and w.pi_t == pytest.approx(0.18)
    for _ in range(4):
        plant_to(w, "E", True, F)
    w.advance(w.t + 1)
    assert w.m_t == pytest.approx(1.8) and w.periods[-1]["F_hat"] is None
    check_all(w)


def test_the_dial_is_bounded_by_m_max_and_floored_at_one():
    w = make_world(period_plants=2, period_ticks=10_000, m_max=4.0)
    for _ in range(4):                               # four periods of pure negligence: 1 → 2 → 4 → 4 → 4
        plant_to(w, "C", False, F) if w.actors["C"].duty_eligible else None
        plant_to(w, "E", False, F) if w.actors["E"].duty_eligible else None
        w.advance(w.t + 1)
    assert w.m_t == 4.0 and w.pi_t == pytest.approx(0.4)
    w2 = make_world(period_plants=1, period_ticks=10_000)
    for _ in range(3):                               # three honest periods from m = 1 stay at 1
        plant_to(w2, "D", False, N, cost=2)
        w2.advance(w2.t + 1)
    assert w2.m_t == 1.0 and all(per["m"] == 1.0 for per in w2.periods)
    check_all(w)
    check_all(w2)


# ------------------------------------------------------------- the plant record (§2.2)
def busy(w, aid, cid_beta=20.0, tau=500):
    """Commit an actor to a long task so it cannot be conscripted: the reserve then runs short when
    a duty actor leaves, and a returning actor is seated by the fill."""
    q = w.post_root("H", cid_beta)
    w.award(q, aid, cid_beta, tau)
    return q


def test_suspension_persists_through_its_record_and_probation_ends_at_the_next_plant():
    w = make_world(n_min=2, T_susp=5)
    busy(w, "A")
    busy(w, "B")
    plant_to(w, "C", False, F)
    plant_to(w, "C", False, F)                       # a_hat = 3/4 > θ_duty: suspended for T_susp
    C = w.actors["C"]
    until = C.suspended_until
    assert until == w.t + 5 and not C.on_duty and w.reserve_shortfall_now == 0   # leaves at completion
    w.advance(w.t + 1)
    assert w.reserve_shortfall_now == 1 and w._pool_exhausted                  # nobody eligible is free
    w.advance(until + 1)                             # the suspension has run its course: the record still fails
    assert C.suspended_until is None and C.probation and C.duty_eligible and not C.panel_eligible
    assert C.p_audit == w.p.p_start and C.streak == 0           # a newcomer for the audit odds (§2.4)
    assert C.on_duty and w.reserve_shortfall_now == 0            # seated by the fill, on probation
    msgs = [e["payload"].get("msg", "") for e in w.history.entries if e["kind"] == "suspension"]
    assert any(m.startswith("readmitted on probation") for m in msgs)
    plant_to(w, "C", False, F)                       # still a stamper: the record still fails
    assert not C.probation and C.suspended_until == w.t + 5 and not C.on_duty
    # a reviewer whose record recovers is readmitted clean
    w2 = make_world(n_min=2, T_susp=5)
    busy(w2, "A")
    busy(w2, "B")
    plant_to(w2, "D", False, F)
    plant_to(w2, "D", False, F)                      # 3/4: suspended
    D = w2.actors["D"]
    w2.advance(D.suspended_until + 1)
    assert D.probation and D.on_duty
    plant_to(w2, "D", False, N, cost=2)              # 3/5 = 0.6 > 0.5: suspended again
    assert D.suspended_until is not None and not D.on_duty
    w2.advance(D.suspended_until + 1)
    assert D.probation and D.on_duty
    plant_to(w2, "D", False, N, cost=2)              # 3/6 = 0.5 ≤ θ_duty: passes; probation over, stays
    assert D.suspended_until is None and not D.probation and D.duty_eligible and not D.panel_eligible and D.on_duty
    check_all(w)
    check_all(w2)


def test_panel_tier_refuses_a_seat_and_duty_tier_refuses_any_review_whole():
    w = make_world(n_min=2)
    plant_to(w, "D", False, N, cost=2)
    plant_to(w, "D", False, F)                       # a_hat = 2/4 = 0.5: on duty, off panels (θ_panel 0.2)
    D = w.actors["D"]
    assert D.duty_eligible and not D.panel_eligible
    q = w.post_root("H", 20)
    w.award(q, "A", 20, 2)
    w.advance(w.t + 2)
    w.submit(q)
    r = w.assign_initial(q, "C")
    w.advance(w.t + 1)
    w.complete_review(r, F, 0)
    before = copy.deepcopy((w.ledger.wallets, w.ledger.locks, len(w.history.entries)))
    with pytest.raises(RuleError, match="challenge panel"):
        w.assign_audit(q, "D")
    assert copy.deepcopy((w.ledger.wallets, w.ledger.locks, len(w.history.entries))) == before
    a2 = w.assign_audit(q, "E")                      # E's record is undetermined: eligible for both tiers
    assert w.reviews[a2].panel_ok
    plant_to(w, "F", False, F)
    plant_to(w, "F", False, F)                       # F: 3/4 > θ_duty — suspended
    q2 = w.post_root("H", 20)
    w.award(q2, "B", 20, 1)
    w.advance(w.t + 1)
    w.submit(q2)
    with pytest.raises(RuleError, match="not on verification duty|plant record"):
        w.assign_initial(q2, "F")
    check_all(w)


def test_the_reserve_runs_short_rather_than_seat_the_negligent_and_the_shortfall_is_counted():
    """Every actor stamps; one bad plant each (n_min = 1) suspends them in turn. The reserve
    falls to zero, no eligible actor is free, I9 holds in its 1.2.0 form, and the gap is counted
    per tick; a reserve left short while an eligible actor is free is what I9 fails on."""
    w = make_world(n_min=1, T_susp=1000)
    for aid in ["C", "D", "E", "F"]:
        plant_to(w, aid, False, F)
        w.advance(w.t + 1)
    on_duty = sorted(a.id for a in w.actors.values() if a.on_duty)
    assert on_duty == ["A", "B"] and w.reserve_shortfall_now == 2 and w._pool_exhausted
    assert w.eligibility_shortfall > 0
    for aid in ["A", "B"]:
        plant_to(w, aid, False, F)
        w.advance(w.t + 1)
    assert not any(a.on_duty for a in w.actors.values()) and w.reserve_shortfall_now == 4
    q = w.post_root("H", 20)
    w.award(q, "A", 20, 1)                           # a suspended actor may still execute work (§2.2)
    assert w.cases[q].actor == "A"
    check_all(w)
    # left short by hand with an eligible actor free: I9 fails
    w2 = make_world()
    w2.advance(1)
    w2.actors["C"].on_duty = False
    with pytest.raises(InvariantError, match="I9"):
        check_all(w2)


# ---------------------------------------------- the dial's capital cap and the alarm (§2.3)
def test_a_plant_omega_cannot_fund_is_refused_whole():
    w = make_world(Omega0=44.0)                      # a plant at B = 20 ties up 20 + 10 + 5 + 10 = 45
    before = (copy.deepcopy(w.ledger.wallets), len(w.cases), w.history.head, w.ledger.M)
    with pytest.raises(LedgerError, match="cannot fund"):
        w.create_plant(False, 20.0)
    assert (copy.deepcopy(w.ledger.wallets), len(w.cases), w.history.head, w.ledger.M) == before
    q = w.create_plant(False, 19.0)                  # 19 + 10 + 5 + 10 = 44: funded exactly
    assert w.cases[q].plant is False and w.W(Ledger.OMEGA) == pytest.approx(0)
    check_all(w)


def test_plants_due_follows_the_rate_and_the_shortfall_is_the_periods_unfunded_plants():
    w = make_world(Omega0=0.0, pi0=0.5, pi_max=0.5, period_ticks=50)
    for i in range(4):                               # four real initial reviews → 2.0 plants due at π = 0.5
        q = w.post_root("H", 20)
        w.award(q, ["A", "B", "A", "B"][i], 20, 1)
        w.advance(w.t + 1)
        w.submit(q)
        w.assign_initial(q, DUTY[i])
        w.advance(w.t + 1)
        for rid in list(w.cases[q].reviews):
            if w.reviews[rid].status == "open":
                w.complete_review(rid, F, 0)
    assert w.plants_due() == 2
    with pytest.raises(LedgerError):
        w.create_plant(False, 20.0)                  # Ω holds nothing
    w.advance(60)                                    # the period closes at tick 50
    assert w.plant_shortfall == 2 and w.periods[-1]["plant_shortfall"] == 2 and w.plants_due() == 0
    check_all(w)


def test_the_alarm_fires_after_two_periods_at_m_max_and_reseats_by_plant_record():
    """m_max = 2, one plant per period. Period 1 (F̂ = 1): m 1 → 2. Period 2 at m_max with
    F̂ > F*: streak 1. Period 3: streak 2 — the alarm is committed and the reserve is re-seated
    from the actors with the lowest bad-plant approval rate."""
    w = make_world(period_plants=1, period_ticks=10_000, m_max=2.0, n_min=10)
    plant_to(w, "D", False, N, cost=2)              # D's record: 1 rejected
    w.advance(w.t + 1)                               # period 1: F̂ = 0 → m stays 1
    for i, stamper in enumerate(["C", "E", "F"]):
        plant_to(w, stamper, False, F)
        w.advance(w.t + 1)
    assert w.m_t == 2.0 and w.alarms == 1 and w.alarm_streak == 2
    alarm = [e for e in w.history.entries if e["kind"] == "capture_alarm"]
    assert len(alarm) == 1 and alarm[0]["payload"]["seated"]
    on_duty = sorted(a.id for a in w.actors.values() if a.on_duty)
    by_record = sorted(w.actors.values(), key=lambda a: (round(a.a_hat, 9), round(a.r_hat, 9), -a.kappa, a.id))
    assert on_duty == sorted(a.id for a in by_record[: w.X_t])
    assert "D" in on_duty                            # the one actor with a clean record holds a seat
    check_all(w)


# --------------------------------------------------------------- the view (§14 amended)
def test_a_plants_view_equals_a_matched_ordinary_cases_view_field_for_field():
    w = make_world()
    q = w.post_root("H", 20)
    w.award(q, "A", 20, 1)
    w.advance(1)
    w.submit(q)
    qp = w.create_plant(False, 20.0)                 # same price, submitted the same tick
    r, rp = w.assign_initial(q, "C"), w.assign_initial(qp, "D")
    v, vp = w.observe("C", r), w.observe("D", rp)
    strip = lambda view: {k: val for k, val in view.__dict__.items() if k not in ("review_id", "case_id")}
    assert strip(v) == strip(vp)
    assert not hasattr(v, "actor") and "plant" not in repr(vp)
    check_all(w)


def test_no_challenge_is_admitted_on_a_plant():
    w = make_world()
    qp = w.create_plant(True, 20.0)                  # a good plant, approved: pending F
    rp = w.assign_initial(qp, "C")
    w.advance(1)
    w.complete_review(rp, F, 0)
    c = w.cases[qp]
    assert c.state == "PENDING" and c.plant_outcome == "stood"
    for op in (lambda: w.assign_audit(qp, "D"), lambda: w.dispute(qp, PLANT_REQ, "x"),
               lambda: w.override(qp, "H", N), lambda: w.accept_explicit(qp, PLANT_REQ),
               lambda: w.respond(qp, "appeal", "x")):
        with pytest.raises(RuleError):
            op()
    w.advance(c.window_end + 1)
    assert c.state == "VESTED" and c.grade == PLANT and w.reviews[rp].status == "vested"
    assert omega_total(w) == pytest.approx(100 - 2)               # the stood review's fee
    # a good plant rejected: the mirror — a plant failure with no appeal needed
    qg = w.create_plant(True, 20.0)
    rg = w.assign_initial(qg, "E")
    w.advance(w.t + 1)
    w.complete_review(rg, N, 0)
    assert w.cases[qg].plant_outcome == "failure" and w.reviews[rg].status == "overturned"
    assert w.actors["E"].plant_good == [(w.t, True)] and w.W("E") == pytest.approx(45)
    w.advance(w.cases[qg].window_end + 1)
    assert w.cases[qg].state == "VESTED"                           # a good plant settles F by its truth
    # P or ⊥ on a plant: spent, no plant outcome for the reviewer, the review stands
    qs = w.create_plant(False, 20.0)
    rs = w.assign_initial(qs, "F")
    w.advance(w.t + 1)
    w.complete_review(rs, P, 0)
    assert w.cases[qs].plant_outcome == "spent" and w.actors["F"].plant_bad == [] and w.cases[qs].state == "FINAL_N"
    w.advance(w.t + 1)
    assert w.reviews[rs].status == "vested"
    check_all(w)


# ------------------------------------------------------------------ I20 and I21 catch
def test_I20_catches_a_challenge_on_a_plant_and_a_tampered_reveal():
    w = make_world()
    qp, rp = plant_to(w, "C", True, F)
    c = w.cases[qp]
    good = copy.deepcopy(c.challenge_round_used)
    c.challenge_round_used = True
    with pytest.raises(InvariantError, match="I20"):
        check_all(w)
    c.challenge_round_used = good
    c.plant = False                                  # a truth that does not hash to the sealed commitment
    with pytest.raises(InvariantError, match="I20"):
        check_all(w)
    c.plant = True
    check_all(w)


def test_I21_catches_a_dial_out_of_bounds_and_an_ineligible_actor_kept_on_duty():
    w = make_world(n_min=1)
    w.m_t = 5.0
    with pytest.raises(InvariantError, match="I21"):
        check_all(w)
    w.m_t = 1.0
    plant_to(w, "C", False, F)                       # C suspended, left duty
    w.actors["C"].on_duty = True                     # put back by hand
    with pytest.raises(InvariantError, match="I21"):
        check_all(w)
    w.actors["C"].on_duty = False
    check_all(w)


# ---------------------------------------------------------------- newcomers (§2.4)
def test_newcomer_audit_odds_start_at_one_and_the_cap_is_one():
    w = make_world()
    assert all(a.p_audit == 1.0 for a in w.actors.values()) and w.p.p_cap == 1.0
    q = w.post_root("H", 20)
    w.award(q, "A", 20, 1)
    w.advance(1)
    w.submit(q)
    r = w.assign_initial(q, "C")
    w.advance(2)
    w.complete_review(r, F, 0)
    w.actors["C"].p_audit = 0.2
    a = w.assign_audit(q, "D")
    w.advance(3)
    w.complete_review(a, N, 0)                       # disagreement: the audit stands as one appeal review
    b = w.assign_appeal(q, "E")
    w.advance(4)
    w.complete_review(b, N, 0)                       # C's F overturned
    assert w.reviews[r].status == "overturned" and w.actors["C"].p_audit == pytest.approx(0.4)
    w.actors["C"].p_audit = 0.8
    w2 = make_world()
    assert w2.actors["C"].p_eff == 1.0               # min(1, m · 1.0)
    check_all(w)

"""Design revision 11 — the supply side (2.3.0): §2.1 arrive — a probationer with a bank-minted float, no award root or nested, no
panel seat, admitted on n_min bad plants with a passing record; §2.2 depart — refused while any obligation is live, the wallet out as
departure, the identity never reused; §2.4 the parent posts the nested pots, the child's reviews draw on them, the root's deposit
untouched, the node's closure refunds the parent (the ruling); the summons never delivers a nested request; §2.6 the reviewer advance
from the rebate pool, the close net of it; I33–I36; supply off = 2.2.0.
"""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
try:
    import pytest
except ImportError:  # plain `python3 run_tests.py`
    sys.path.insert(0, os.path.dirname(__file__))
    from _mini_pytest import pytest

from sim import Params, World, Ledger, check_all
from sim.engine import RuleError, LedgerError, F, N
from sim.invariants import InvariantError

ACTORS = ["A", "B", "C", "D", "E", "F"]
DUTY = ["C", "D", "E", "F"]


def make_world(budget=1000.0, actors=ACTORS, duty=DUTY, **over):
    # 2.3.0 defaults (the bank, the pool and the supply side on); no emission, the fee on, no plants unless asked, long turns
    kw = dict(E0=0.0, H=1e9, omega_rate=0.05, Omega0=100.0, duty_turn_reviews=10_000, duty_turn_ticks=100_000,
              r_s=1.0, T_s=10_000, pi0=0.0, period_ticks=60)
    kw.update(over)
    return World(Params(**kw), actors, humans={"H": budget}, on_duty=duty)


def post_and_award(w, actor, B, beta=None, tau=500):
    q = w.post_root("H", beta if beta is not None else B)
    w.award(q, actor, B, tau)
    return q


def test_an_arrival_is_a_probationer_with_a_float_the_bank_mints_once_and_wins_no_award():
    w = make_world()
    L = w.ledger
    M0 = L.M
    w.arrive("G")
    g = w.actors["G"]
    assert g.probation and not g.is_member and g.pinned and g.arrived_at == 0 and g.admitted_at is None and g.suspended_until is None
    assert L.wallet("G").U == pytest.approx(50.0) and L.M == pytest.approx(M0 + 50.0)
    assert sum(1 for e in L.events if e.kind == "arrival") == 1 and w.bank_minted["arrival"] == pytest.approx(50.0) and w.arrivals == 1
    q = w.post_root("H", 30)
    with pytest.raises(RuleError):
        w.award(q, "G", 10, 5)                         # no root award before admission
    w.award(q, "A", 20, 50)
    qn = w.post_nested(q, 6)
    with pytest.raises(RuleError):
        w.award(qn, "G", 5, 3)                         # no nested award either (rc.2's correction)
    with pytest.raises(RuleError):
        w.arrive("G")                                  # an identity that exists is refused
    with pytest.raises(RuleError):
        w.arrive("H")                                  # a requester's name too
    check_all(w)


def test_an_arrivals_float_is_indexed_at_the_arrival_tick():
    w = make_world(period_ticks=6)
    post_and_award(w, "A", 10, tau=2)
    post_and_award(w, "B", 40, tau=2)
    w.advance(7)                                      # the boundary: P_t = 25, the index 1.25
    w.arrive("G")
    assert w.ledger.wallet("G").U == pytest.approx(50.0 * 1.25)
    check_all(w)


def test_an_arrival_is_admitted_on_n_min_bad_plants_with_a_passing_record_and_counted_apart_from_readmissions():
    w = make_world(pi0=0.1, n_min=2)
    w.arrive("G")
    g = w.actors["G"]
    # seat G on duty by rotation: make it the only free eligible initial reviewer by giving it duty through the plants it reviews
    w.actors["G"].on_duty = True                      # the rotation would seat a probationer first for initial seats (1.3.0 §2.3)
    for i in range(2):
        p = w.create_plant(False, 20.0)               # a bad plant: G rejects it — the record +1 each time
        r = w.assign_initial(p, "G")
        w.complete_review(r, N, 0)
        assert g.admitted_at is None or i == 1
    assert g.admitted_at is not None and not g.probation and g.is_member
    assert w.admissions == 1 and w.readmissions == 0 and w.admission_ticks_sum == g.admitted_at - g.arrived_at
    assert w.period["admissions"] == 1
    check_all(w)
    # a good plant does not count toward admission: two good plants leave another arrival a probationer
    w2 = make_world(pi0=0.1, n_min=2)
    w2.arrive("G")
    w2.actors["G"].on_duty = True
    for _ in range(2):
        p = w2.create_plant(True, 20.0)
        r = w2.assign_initial(p, "G")
        w2.complete_review(r, F, 0)
    assert w2.actors["G"].admitted_at is None and w2.actors["G"].probation
    check_all(w2)


def test_a_plant_failure_suspends_an_arrival_and_it_is_still_not_a_member():
    w = make_world(pi0=0.1, n_min=2, T_susp=5)
    w.arrive("G")
    w.actors["G"].on_duty = True
    p = w.create_plant(False, 20.0)
    r = w.assign_initial(p, "G")
    w.complete_review(r, F, 0)                        # approves a bad plant: suspended
    g = w.actors["G"]
    assert g.suspended_until is not None and not g.is_member and g.admitted_at is None
    check_all(w)                                      # I33: not a member before admission, suspended or not
    w.advance(7)
    assert g.suspended_until is None and g.probation and not g.is_member
    check_all(w)


def test_depart_is_refused_while_any_obligation_is_live_and_then_takes_the_wallet_out():
    w = make_world()
    L = w.ledger
    q = post_and_award(w, "A", 10, tau=4)
    with pytest.raises(RuleError):
        w.depart("A")                                 # a commitment
    w.submit(q)
    r = w.assign_initial(q, "C")
    with pytest.raises(RuleError):
        w.depart("C")                                 # an open review
    w.complete_review(r, F, 2)
    with pytest.raises(RuleError):
        w.depart("C")                                 # a completed review awaiting its settlement
    w.advance(w.cases[q].window_end + 1)
    assert w.cases[q].state == "VESTED"
    qb = w.post_root("H", 20)
    qn_parent = post_and_award(w, "B", 10, tau=50)
    qn = w.post_nested(qn_parent, 4)                  # B holds the nested lock and the rejection bond
    with pytest.raises(RuleError):
        w.depart("B")                                 # a lock (and a commitment)
    # a claim on Ω: a reviewer whose cost the allowance could not cover and Ω could not advance
    assert w.omega_claims == []
    # C is free of everything now: it departs, off duty, its wallet leaving M
    M0, u = L.M, L.wallet("C").U
    assert w.actors["C"].on_duty
    w.depart("C")
    assert "C" not in w.actors and "C" in w.departed_actors and not w.departed_actors["C"].on_duty
    assert L.M == pytest.approx(M0 - u) and L.wallet("C").U == 0 and w.actor_departures == 1 and w.actor_departed_credits == pytest.approx(u)
    assert any(e.kind == "departure" and e.src == "C" and e.amount == pytest.approx(u) for e in L.events)
    with pytest.raises(RuleError):
        w.arrive("C")                                 # the identity never reappears
    with pytest.raises(RuleError):
        w.depart("C")
    check_all(w)


def test_depart_is_refused_for_a_claim_on_Omega():
    w = make_world(Omega0=0.0, phi_E_root=0.0, phi_F_root=2.0)
    q = post_and_award(w, "A", 10, tau=4)             # no allowance, a fee pot of exactly the fee: C's cost is deferred and becomes a claim on Ω
    w.submit(q)
    r = w.assign_initial(q, "C")
    w.complete_review(r, F, 3)
    w.advance(w.cases[q].window_end + 1)
    assert any(cl.reviewer == "C" for cl in w.omega_claims)
    with pytest.raises(RuleError):
        w.depart("C")
    check_all(w)


def test_the_parent_posts_the_pots_the_child_draws_on_them_and_the_root_deposit_is_untouched():
    w = make_world()
    L = w.ledger
    q = post_and_award(w, "A", 20, tau=60)
    a_u0 = L.wallet("A").U
    qn = w.post_nested(q, 6)
    c = w.cases[qn]
    idx = L.index()
    assert c.own_pots and c.phi_E == pytest.approx(10.0 * idx) and c.phi_F == pytest.approx(5.0 * idx) and c.index_at_lock == pytest.approx(idx)
    all_in = 6 + 15 * idx + 0.05 * w.m_t * 6
    assert c.posting_lock == pytest.approx(all_in) and L.lock_record("A", f"beta:{qn}") == pytest.approx(all_in)
    assert L.lock_record("A", f"rej:{qn}") == pytest.approx(5.0 * idx)
    assert L.wallet("A").U == pytest.approx(a_u0 - all_in - 5.0 * idx)
    check_all(w)                                      # I15: the nested lock is the all-in; I36
    w.award(qn, "B", 5, 3)
    assert L.pools[qn].escrow == pytest.approx(5.0) and L.pools[qn].deposit == pytest.approx(10.0) and L.pools[qn].fee_pot == pytest.approx(5.0)
    assert L.lock_record("A", f"beta:{qn}") == 0       # released whole; the pay-in drawn from it
    root_pool = (L.pools[q].deposit, L.pools[q].fee_pot)
    w.advance(w.t + 3)
    w.submit(qn)
    w.judge_nested(qn, F)                             # the parent's judgment is the initial verdict; the child is audited as any case
    assert w.cases[qn].state == "PENDING"
    w.advance(w.cases[qn].window_end + 1)
    assert w.cases[qn].state == "VESTED" and w.cases[qn].node_closed
    assert (L.pools[q].deposit, L.pools[q].fee_pot) == root_pool      # the root's deposit untouched (I36)
    assert w.cases[qn].allowance_refunded == pytest.approx(10.0) and w.cases[qn].pot_refunded == pytest.approx(5.0)   # nothing drawn: no review
    assert L.pools[qn].deposit == 0 and L.pools[qn].fee_pot == 0
    assert any(e.kind == "feepot_out" and e.note == "node closure: unused fee pot returned" and e.dst == "A" for e in L.events)
    check_all(w)                                      # I19 per case: the node closed with empty pots; I10's note


def test_a_childs_audit_draws_on_the_childs_pots_and_the_node_closes_after_its_review_settles():
    w = make_world()
    L = w.ledger
    q = post_and_award(w, "A", 20, tau=80)
    qn = w.post_nested(q, 6)
    w.award(qn, "B", 5, 3)
    w.advance(w.t + 3)
    w.submit(qn)
    w.judge_nested(qn, F)
    w.roll_audit(qn)                                  # the market audits the child's work: paid from the child's pots
    r = w.assign_audit(qn, "C")
    w.complete_review(r, F, 3)
    assert w.reviews[r].reimbursed == pytest.approx(3.0) and L.pools[qn].deposit == pytest.approx(7.0)
    assert L.pools[q].deposit == pytest.approx(10.0)  # the root's allowance untouched
    w.advance(w.cases[qn].window_end + 1)
    c = w.cases[qn]
    assert c.state == "VESTED" and c.node_closed and c.fees_from_pot == pytest.approx(3.0)      # the audit's fee 1.5 f
    assert c.allowance_refunded == pytest.approx(7.0) and c.pot_refunded == pytest.approx(2.0)
    assert w.cases[q].fees_from_pot == 0 and not w.cases[q].tree_closed
    check_all(w)


def test_the_root_reading_is_the_control_and_the_children_draw_on_the_roots_pots():
    w = make_world(nested_pots="root")
    L = w.ledger
    q = post_and_award(w, "A", 20, tau=80)
    qn = w.post_nested(q, 6)
    c = w.cases[qn]
    assert not c.own_pots and c.phi_E == 0 and L.lock_record("A", f"beta:{qn}") == pytest.approx(6.0)
    w.award(qn, "B", 5, 3)
    w.advance(w.t + 3)
    w.submit(qn)
    w.judge_nested(qn, F)
    w.roll_audit(qn)
    r = w.assign_audit(qn, "C")
    w.complete_review(r, F, 3)
    assert L.pools[q].deposit == pytest.approx(7.0)   # the 1.1.0 reading: the root's allowance paid the child's audit
    check_all(w)


def test_no_troop_delivers_a_nested_request_but_a_seat_on_it_may_be_a_troops():
    w = make_world()
    post_and_award(w, "A", 10, tau=2)
    post_and_award(w, "B", 10, tau=2)
    q = post_and_award(w, "A", 20, tau=80) if False else None
    # A and B are committed; the only free members are none: a nested request waits past w_A and is not the state's
    w2 = make_world()
    qr = w2.post_root("H", 30)
    w2.award(qr, "A", 20, 80)
    post_and_award(w2, "B", 10, tau=80)
    qn = w2.post_nested(qr, 6)
    w2.advance(w2.t + 4)
    assert w2.cases[qn].state == "AVAILABLE" and not any(t["kind"] == "delivery" and t["case"] == qn for t in w2.troops.values())
    assert w2.troop_summons_deliveries == 0
    check_all(w2)                                     # I35


def test_a_reviewer_advance_draws_on_the_rebate_pool_and_the_close_is_net_of_it():
    w = make_world(Omega0=0.0, phi_E_root=1.0, phi_F_root=5.0, T_s=1, period_ticks=20)
    L = w.ledger
    post_and_award(w, "A", 10, tau=2)                 # fees into the pool: 0.5
    post_and_award(w, "B", 10, tau=2)                 # 1.0 pooled
    w.advance(3)                                      # both lapse late: claims 2 × min(1 × 1, 10) = 2
    assert w.omega_pool == pytest.approx(1.0) and w.period["claims_total"] == pytest.approx(2.0)
    q = post_and_award(w, "A", 10, tau=4)             # 1.5 pooled
    w.submit(q)
    r = w.assign_initial(q, "C")
    w.complete_review(r, F, 3)                        # the allowance of 1 covers 1; Ω's unlocked is 0; the pool advances up to 1.5
    rv = w.reviews[r]
    assert rv.reimbursed == pytest.approx(1.0 + 1.5) and rv.deferred == pytest.approx(0.5)
    assert w.omega_pool == pytest.approx(0.0) and w.pool_advances == pytest.approx(1.5) and w.cases[q].omega_advance == pytest.approx(1.5)
    assert any(e.note.startswith("Ω advance") and e.note.endswith("(from the pool)") for e in L.events)
    check_all(w)                                      # I32: the lock equals the pool, net of the advance
    w.advance(21)                                     # the close: the pool is what the advances left — nothing; the claims are forgone
    rec = w.periods[-1]
    assert rec["pool_advances"] == pytest.approx(1.5) and rec["rebates_paid"] == pytest.approx(0.0) and rec["forgone_share"] == pytest.approx(1.0)
    check_all(w)


def test_the_period_record_and_the_view_carry_the_supply_side():
    w = make_world(period_ticks=6)
    w.arrive("G")
    w.advance(7)
    rec = w.periods[-1]
    assert rec["arrivals"] == 1 and rec["admissions"] == 0 and rec["time_to_membership"] is None and rec["actors"] == 7 and rec["probationers"] == 1
    from drivers.view import Public
    v = Public(w)
    mk = v.market()
    assert mk["actors"] == 7 and mk["probationers"] == 1 and mk["members_total"] == 6 and mk["arrivals"] == 1 and mk["time_to_membership"] is None
    assert "G" not in str(sorted(k for k in mk if "cost" in k))      # nothing per actor
    check_all(w)


def test_supply_off_is_the_220_engine():
    w = make_world(supply=False)
    with pytest.raises(RuleError):
        w.arrive("G")
    with pytest.raises(RuleError):
        w.depart("A")
    q = post_and_award(w, "A", 20, tau=60)
    qn = w.post_nested(q, 6)
    assert not w.cases[qn].own_pots and w.ledger.lock_record("A", f"beta:{qn}") == pytest.approx(6.0)
    check_all(w)

"""Design revision 8 — the price of work (2.0.0): §2.1 the pay-in locked at posting and the ceiling raised; §2.2 the state
at the members' price; §2.3 the price level P_t indexing every nominal, frozen at a case's first lock, the cost API in
credits; §2.4 sources and sinks with no backing; §2.5 creation, retirement and the deficit; §2.6 the state at cost and the
capacity case; §2.8 the below-market flag; Appendix M's two rulings (two places until the inspection is seated; departure).
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
from sim.engine import LedgerError, RuleError, F, N
from sim.invariants import InvariantError

ACTORS = ["A", "B", "C", "D", "E", "F"]
DUTY = ["C", "D", "E", "F"]


def make_world(budget=1000.0, actors=ACTORS, duty=DUTY, **over):
    # 2.0.0 defaults; no emission, the service fee on, no plants, the service target far off, long turns
    # 2.1.0 (design revision 9) replaced Ω's creation and retirement with the bank; these tests pin the 2.0.0 engine (bank=False)
    kw = dict(E0=0.0, H=1e9, omega_rate=0.05, Omega0=100.0, duty_turn_reviews=10_000, duty_turn_ticks=100_000,
              r_s=1.0, T_s=10_000, pi0=0.0, bank=False)
    kw.update(over)
    return World(Params(**kw), actors, humans={"H": budget}, on_duty=duty)


def post_and_award(w, actor, B, beta=None, tau=500):
    q = w.post_root("H", beta if beta is not None else B)
    w.award(q, actor, B, tau)
    return q


def money(w):
    L = w.ledger
    return (round(L.M, 9), tuple((k, round(v.U, 9), round(v.L, 9)) for k, v in sorted(L.wallets.items())),
            len(L.events), len(w.cases))


def test_the_genesis_is_issuance_and_conservation_holds_over_every_source_and_sink():
    w = make_world(budget=200.0)
    L = w.ledger
    M0 = 6 * 50 + 100 + 200
    assert L.M == pytest.approx(M0) and L.Res == 0 and L.v == 1.0 and L.index() == 1.0
    kinds = {e.kind for e in L.events}
    assert "issuance" in kinds and "mint_backed" not in kinds
    w.scenario_create(30.0)                           # creation, paid to the requester
    w.add_requester("C1", 40.0)                       # issuance to an arriving requester
    w.remove_requester("C1")                          # departure
    w.advance(1)                                      # retirement runs at the tick's end
    kinds = {e.kind for e in L.events}
    assert {"creation", "departure"} <= kinds
    assert L.M == pytest.approx(M0 + 30 - w.deficit_retired) and w.deficit_retired == pytest.approx(30.0)
    check_all(w)                                      # I1 over every kind


def test_a_root_locks_its_all_in_maximum_at_posting_and_an_unaffordable_post_is_refused_whole():
    w = make_world(budget=60.0)
    L = w.ledger
    before = money(w)
    with pytest.raises(LedgerError, match="refused at posting"):
        w.post_root("H", 50)                          # all-in 50 + 15 + 2.5 = 67.5 > 60
    assert money(w) == before
    q = w.post_root("H", 40)                          # all-in 40 + 15 + 2 = 57
    c = w.cases[q]
    assert L.lock_record("H", f"post:{q}") == pytest.approx(57.0) and c.posting_lock == pytest.approx(57.0)
    assert c.index_at_lock == 1.0 and c.m_post == 1.0 and (c.D, c.K, c.G_V, c.phi_E, c.phi_F) == (2.0, 5.0, 5.0, 10.0, 5.0)
    assert L.wallet("H").U == pytest.approx(3.0)
    check_all(w)                                      # I29: the lock equals the all-in maximum
    w.award(q, "A", 10, 5)                            # the pay-in is drawn from the released lock: β − B and the unspent fee stay
    assert L.lock_record("H", f"post:{q}") == 0 and L.wallet("H").U == pytest.approx(60 - (10 + 15 + 0.5))
    assert L.pool(q).escrow == pytest.approx(10) and L.pool(q).deposit == pytest.approx(10) and L.pool(q).fee_pot == pytest.approx(5)
    check_all(w)


def test_a_withdrawn_request_releases_its_posting_lock():
    w = make_world(budget=100.0)
    q = w.post_root("H", 20)
    assert w.ledger.lock_record("H", f"post:{q}") == pytest.approx(36.0)
    w.withdraw_unawarded(q)
    assert w.ledger.lock_record("H", f"post:{q}") == 0 and w.ledger.wallet("H").U == pytest.approx(100.0)
    check_all(w)


def test_the_price_level_is_the_trailing_mean_of_every_award_and_indexes_the_next_case_frozen():
    w = make_world()
    L = w.ledger
    assert w.price_level() == 20.0                    # P_0 before the first award
    q1 = post_and_award(w, "A", 10)
    assert w.price_level() == pytest.approx(10.0) and L.index() == pytest.approx(0.5) and L.v == pytest.approx(2.0)
    q2 = w.post_root("H", 30)                         # priced at the index of its posting: 0.5
    c2 = w.cases[q2]
    assert (c2.D, c2.K, c2.G_V, c2.phi_E, c2.phi_F) == (1.0, 2.5, 2.5, 5.0, 2.5) and c2.index_at_lock == pytest.approx(0.5)
    w.award(q2, "B", 30, 5)
    assert w.price_level() == pytest.approx(20.0) and L.index() == pytest.approx(1.0)
    assert (c2.D, c2.K, c2.G_V, c2.phi_E, c2.phi_F) == (1.0, 2.5, 2.5, 5.0, 2.5)   # frozen (§4.5, I27)
    assert (w.cases[q1].D, w.cases[q1].phi_E) == (2.0, 10.0)                       # the first case was priced at P_0
    check_all(w)


def test_B_bar_counts_members_awards_only_and_P_t_counts_the_troops_too():
    w = make_world(Omega0=200.0)
    post_and_award(w, "A", 10)                        # B̄ = 10, P_t = 10
    post_and_award(w, "B", 10)                        # both free members committed
    q3 = w.post_root("H", 30)
    t = w.t
    w.advance(t + 2)                                  # waited w_A: the state's, at B̄ = 10
    c3 = w.cases[q3]
    assert c3.state == "COMMITTED" and w.is_troop(c3.actor) and c3.B == pytest.approx(10.0)
    assert w.period["award_n"] == 2 and w.period["price_n"] == 3
    assert w.mean_awarded_price() == pytest.approx(10.0) and w.price_level() == pytest.approx(10.0)
    assert w.troops[c3.actor]["cost"] == pytest.approx(10.0)      # §2.6: at cost — c^D_T = B̄
    check_all(w)


def test_the_state_at_cost_Omega_creates_the_shortfall_and_retires_it_from_the_next_inflow():
    w = make_world(Omega0=0.0)
    L = w.ledger
    post_and_award(w, "A", 10)
    post_and_award(w, "B", 10)                        # Ω holds the two fees, 1.0
    q3 = w.post_root("H", 30)
    t = w.t
    w.advance(t + 2)
    c3 = w.cases[q3]
    assert c3.state == "COMMITTED" and w.is_troop(c3.actor)
    # the summons needed cost 10 + G 5 against Ω's 1.0 (+ the fee ω of this award, drawn from the lock after the creation)
    assert w.deficit_created == pytest.approx(15.0 - 1.0) and w.deficit > 0
    assert L.wallet(Ledger.OMEGA).U == pytest.approx(0.0)         # I28: nothing kept while the deficit stands
    assert L.wallet(Ledger.OMEGA).L == pytest.approx(5.0)         # the troop's guarantee sits on Ω
    assert w.omega_liabilities == [] and w.advance_outstanding == 0 and w.R_T == 0
    check_all(w)
    # the delivery vests: the price and the guarantee come home to Ω and retire the deficit
    w.submit(q3)
    r = w.assign_initial(q3, "C")
    w.complete_review(r, F, 0)
    w.advance(w.cases[q3].window_end + 1)
    assert w.cases[q3].state == "VESTED"
    assert w.deficit == pytest.approx(0.0) and w.deficit_retired == pytest.approx(w.deficit_created)
    assert L.wallet(Ledger.OMEGA).U > 0 and w.deficit_since is None
    assert any(e.kind == "retirement" for e in L.events) and any(e.kind == "creation" and e.note == "creation: summons" for e in L.events)
    check_all(w)


def test_a_rebate_is_paid_at_the_stop_creating_if_short_and_no_liability_is_made():
    w = make_world(Omega0=0.0, T_s=2, r_s=1.0)
    q = post_and_award(w, "A", 10, tau=6)             # the clock runs from posting (ticks 0–5); first verdict at t = 6: 4 late
    w.advance(6)
    w.submit(q)
    r = w.assign_initial(q, "C")
    w.complete_review(r, F, 0)
    c = w.cases[q]
    assert c.clock_ticks == 6 and c.late_ticks == 4 and c.rebate_owed == pytest.approx(4.0) and c.rebate_paid == pytest.approx(4.0)
    assert w.omega_liabilities == [] and w.liabilities_accrued == 0
    assert w.deficit_created == pytest.approx(4.0 - 0.5)         # Ω held the fee 0.5 and created the rest
    assert any(e.kind == "creation" and e.note == "creation: rebate" for e in w.ledger.events)
    check_all(w)


def test_N_T_refuses_for_capacity_and_a_delivery_holds_two_places_until_its_inspection_is_seated():
    w = make_world(Omega0=500.0, N_T=3)
    post_and_award(w, "A", 10)
    post_and_award(w, "B", 10)
    q3 = w.post_root("H", 30)
    q4 = w.post_root("H", 30)
    t = w.t
    w.advance(t + 2)
    c3, c4 = w.cases[q3], w.cases[q4]
    assert c3.state == "COMMITTED" and w.is_troop(c3.actor) and w.troops[c3.actor]["places"] == 2
    assert c4.state == "AVAILABLE" and c4.refused_capacity == 1 and c4.capacity_told and c4.capacity_wait_max == 2
    assert w.troop_refused_capacity_awards == 1 and w._places_held() == 2
    assert w.deficit_created == 0                     # Ω carried the summons
    check_all(w)                                      # I24: places held ≤ N_T, the clock of q4 runs
    assert c4.clock_ticks == 2
    w.submit(q3)
    w.assign_initial(q3, "C")                         # the inspection is seated by a market reviewer: one place released
    assert w.troops[c3.actor]["places"] == 1 and w._places_held() == 1
    w.advance(w.t + 1)                                # q4 now fits: two places of three
    assert w.cases[q4].state == "COMMITTED" and w.is_troop(w.cases[q4].actor) and w._places_held() == 3
    check_all(w)


def test_unbounded_N_T_never_refuses_and_the_control_margin_is_half_the_price_level():
    w = make_world(Omega0=500.0, N_T=0, troop_cost_at_price=False)
    post_and_award(w, "A", 10)
    post_and_award(w, "B", 10)
    qs = [w.post_root("H", 30) for _ in range(5)]
    t = w.t
    w.advance(t + 2)
    assert all(w.is_troop(w.cases[q].actor) for q in qs) and w.troop_refused_capacity_awards == 0
    assert all(w.troops[w.cases[q].actor]["cost"] == pytest.approx(5.0) for q in qs)   # c_D_T × P_t/P_0 = 10 × 0.5
    check_all(w)


def test_a_request_below_the_market_is_flagged_its_clock_stopped_and_raising_the_ceiling_locks_the_difference():
    w = make_world()
    post_and_award(w, "A", 10)                        # B̄ = 10
    q = w.post_root("H", 6)
    c = w.cases[q]
    assert c.below_market and w.below_market_flagged == 1
    lock0 = w.ledger.lock_record("H", f"post:{q}")
    assert lock0 == pytest.approx(6 * 1.05 + 7.5)      # at index 0.5: φ 7.5
    w.advance(w.t + 3)
    assert c.clock_ticks == 0 and c.state == "AVAILABLE"            # not the state's to answer for, and no troop
    with pytest.raises(RuleError):
        w.raise_ceiling(q, 6)
    w.raise_ceiling(q, 12)
    assert not c.below_market and c.beta == 12 and w.ceilings_raised == 1
    assert w.ledger.lock_record("H", f"post:{q}") == pytest.approx(lock0 + 6 * 1.05)
    check_all(w)                                      # I29 at the raised lock
    w.advance(w.t + 1)
    assert c.clock_ticks == 1                         # the clock runs again


def test_a_crowd_requester_arrives_as_issuance_and_leaves_with_its_wallet_as_departure():
    w = make_world()
    M0 = w.ledger.M
    w.add_requester("C1", 100.0)
    assert w.ledger.M == pytest.approx(M0 + 100) and "C1" in w.humans
    q = w.post_root("C1", 20)
    with pytest.raises(RuleError, match="open requests"):
        w.remove_requester("C1")
    w.withdraw_unawarded(q)
    w.remove_requester("C1")
    assert w.ledger.M == pytest.approx(M0) and w.departed == pytest.approx(100.0) and "C1" not in w.requesters
    assert any(e.kind == "departure" for e in w.ledger.events)
    with pytest.raises(RuleError):
        w.post_root("C1", 10)
    check_all(w)


def test_issuance_credits_each_requester_at_the_ticks_start():
    w = make_world(budget=10.0, issuance=5.0)
    w.advance(3)
    assert w.ledger.wallet("H").U == pytest.approx(10 + 15) and w.issued == pytest.approx(6 * 50 + 100 + 10 + 15)
    assert w.period["issued"] == pytest.approx(15.0)
    check_all(w)


def test_the_scenario_operation_is_the_only_discretionary_creation_I28_recognises():
    w = make_world(Omega0=0.0, budget=100.0)
    w.scenario_create(50.0)
    assert w.ledger.wallet("H").U == pytest.approx(150.0) and w.deficit == pytest.approx(50.0) and w.scenario_created == 50.0
    assert w.ledger.wallet(Ledger.OMEGA).U == 0
    w.advance(1)
    check_all(w)
    # a creation for anything but a required payment is caught
    w._omega_ensure(5.0, None, "bonus")
    with pytest.raises(InvariantError, match="I28"):
        check_all(w)


def test_the_cost_api_is_in_credits_and_effort_is_not_indexed():
    w = make_world()
    q = post_and_award(w, "A", 10)                    # index 0.5 from here
    a0 = w.ledger.wallet("A").U
    burned = w.spend("A", 8.0, q)
    assert burned == pytest.approx(8.0) and w.ledger.wallet("A").U == pytest.approx(a0 - 8.0)   # 8 credits, not 8 / v
    q2 = post_and_award(w, "B", 10)                   # K = 2.5 at index 0.5
    w.submit(q2)
    r = w.assign_initial(q2, "C")
    c0 = w.ledger.wallet("C").U
    w.complete_review(r, F, 3.0)
    assert w.reviews[r].cost == pytest.approx(3.0) and w.reviews[r].reimbursed == pytest.approx(2.5)   # min(3, K)
    assert w.ledger.wallet("C").U == pytest.approx(c0 - 3.0 + 2.5)
    check_all(w)


def test_the_period_record_carries_the_price_level_the_deficit_and_the_capacity_case():
    w = make_world(Omega0=0.0, N_T=3, period_ticks=6)
    post_and_award(w, "A", 10)
    post_and_award(w, "B", 10)
    w.post_root("H", 30)
    w.post_root("H", 30)
    w.advance(7)                                      # the first troop misses its deadline (nobody submits for it) and the second is summoned
    rec = w.periods[-1]
    assert rec["P_level"] == pytest.approx(10.0) and rec["price_n"] >= 3
    assert rec["created"] > 0 and rec["deficit_peak"] > 0 and rec["refused_capacity"][1] >= 1 and "places_held" in rec
    assert rec["omega_net"] == pytest.approx(-rec["deficit"]) and rec["M"] == pytest.approx(w.ledger.M)
    check_all(w)


def test_floating_off_is_the_171_engine():
    w = make_world(floating=False)
    L = w.ledger
    assert L.Res == pytest.approx(10000.0) and L.v == pytest.approx(L.Res / L.M) and w.R_T == 0
    q = w.post_root("H", 40)
    assert L.lock_record("H", f"post:{q}") == 0 and w.cases[q].index_at_lock is None
    with pytest.raises(RuleError):
        w.raise_ceiling(q, 50)
    w.award(q, "A", 10, 5)
    assert L.index() == pytest.approx(L.v0 / L.v) and w.price_level() == pytest.approx(10.0)   # the reading exists, indexes nothing
    check_all(w)

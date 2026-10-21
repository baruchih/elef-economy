"""Design revision 15 — the arrival loan (2.7.0): §2.1 `arrive` lends the float (the loan carried on the name, the bank's names line);
every inflow of income — §2.1's table, fixed against the engine's events — repays the loan first, the moment it arrives, and a return
passes untouched; `depart` is admissible as 2.3.0 has it, recovers the loan from the unlocked wallet first and lets the remainder out as
`departure`, the shortfall the bank's default, read; I41 every tick; the §6 arrival, cycler and leaver reproduced; the flag off is 2.6.1's
grant; a world with no arrivals keeps 2.6.1's record to the hash (the goldens).
"""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
try:
    import pytest
except ImportError:  # plain `python3 run_tests.py`
    sys.path.insert(0, os.path.dirname(__file__))
    from _mini_pytest import pytest

from sim import Params, World, Ledger, check_all, check_tick
from sim.engine import RuleError, F, N
from sim.invariants import InvariantError

ACTORS = ["A", "B", "C", "D", "E", "F"]
DUTY = ["C", "D", "E", "F"]


def make_world(budget=1000.0, actors=ACTORS, duty=DUTY, **over):
    # 2.3.0's six-actor world (test_v23): the bank, the pool and the supply side on; plants built submitted (the 1.2.0 construction);
    # no emission unless asked, the fee on, long turns
    kw = dict(plant_market=False, E0=0.0, H=1e9, omega_rate=0.05, Omega0=100.0, duty_turn_reviews=10_000, duty_turn_ticks=100_000,
              r_s=1.0, T_s=10_000, pi0=0.0, period_ticks=60)
    kw.update(over)
    return World(Params(**kw), actors, humans={"H": budget}, on_duty=duty)


def post_and_award(w, actor, B, beta=None, tau=500):
    q = w.post_root("H", beta if beta is not None else B)
    w.award(q, actor, B, tau)
    return q


def snapshot(w):
    L = w.ledger
    return (w.history.head, len(L.events), tuple((k, round(v.U, 9), round(v.L, 9)) for k, v in sorted(L.wallets.items())),
            tuple((c.id, c.state, c.actor_cost) for c in w.cases.values()), tuple(sorted((a.id, a.committed) for a in w.actors.values())),
            dict(w.arrival_loan), w.names_lent, w.names_repaid, w.names_recovered, w.names_defaulted)


def admit(w, name):
    """An arrival admitted on two bad plants it rejects (n_min 2), then taken off duty so that it may be awarded."""
    w.actors[name].on_duty = True
    for _ in range(2):
        p = w.create_plant(False, 20.0)
        r = w.assign_initial(p, name)
        w.complete_review(r, N, 0)
    a = w.actors[name]
    assert a.admitted_at is not None and a.is_member
    w.advance(w.t + 12)                               # the plant reviews settle: their fees repaid, the loan 46
    a.on_duty = False


def events_to(w, name):
    return [e for e in w.ledger.events if e.dst == name]


def repaid_next(w, e):
    """Whether the event right after `e` is the name's repayment from income (False when `e` is the record's last event)."""
    L = w.ledger
    if e.seq + 1 >= len(L.events):
        return False
    n = L.events[e.seq + 1]
    return n.kind == "arrival_repayment" and n.src == e.dst and n.note.startswith("arrival loan repaid")


def on_duty_reviewer(w, exclude=()):
    return next(a for a in DUTY if w.actors[a].on_duty and a not in exclude)


def repayments_from_income(w, name):
    return [e for e in w.ledger.events if e.kind == "arrival_repayment" and e.src == name and e.note.startswith("arrival loan repaid")]


# ---------------------------------------------------------------- §2.1 arrive lends

def test_arrive_lends_the_float_and_the_loan_is_carried_on_the_name():
    w = make_world()
    L = w.ledger
    M0 = L.M
    w.arrive("G")
    assert L.wallet("G").U == pytest.approx(50.0) and L.M == pytest.approx(M0 + 50.0)   # the float is in the wallet, as before
    assert w.arrival_loan["G"] == pytest.approx(50.0) and w.names_outstanding == pytest.approx(50.0)
    assert w.names_lent == pytest.approx(50.0) and w.names_lent_n == 1 and w.names_repaid == 0 and w.names_recovered == 0 and w.names_defaulted == 0
    assert w.names_outstanding_peak == pytest.approx(50.0)
    assert w.bank_minted["arrival"] == pytest.approx(50.0)                                 # `arrival` a source, as it was
    e = [x for x in L.events if x.kind == "arrival"][0]
    assert "loan" in e.note
    entry = [h for h in w.history.entries if h["kind"] == "entry" and h["payload"].get("actor") == "G"][0]["payload"]
    assert entry["float"] == pytest.approx(50.0) and entry["loan"] == pytest.approx(50.0)
    # a genesis name carries no loan
    assert all(n not in w.arrival_loan for n in ACTORS)
    check_all(w)


def test_the_loan_is_indexed_at_the_arrival_tick_as_the_float_is():
    w = make_world(period_ticks=6)
    post_and_award(w, "A", 10, tau=2)
    post_and_award(w, "B", 40, tau=2)
    w.advance(7)                                      # the boundary: P_t = 25, the index 1.25
    w.arrive("G")
    assert w.ledger.wallet("G").U == pytest.approx(62.5) and w.arrival_loan["G"] == pytest.approx(62.5)
    check_all(w)


# ---------------------------------------------------------------- §2.1 repaid from income first — the table, event by event

def test_a_review_fee_repays_the_loan_and_the_reimbursement_and_the_bond_release_pass_untouched():
    w = make_world()
    L = w.ledger
    w.arrive("G")
    w.actors["G"].on_duty = True
    q = post_and_award(w, "A", 10, tau=4)
    w.submit(q)
    r = w.assign_initial(q, "G")                      # the bond G_V = 5 locked from the float
    assert L.wallet("G").L == pytest.approx(5.0) and L.wallet("G").U == pytest.approx(45.0)
    w.complete_review(r, F, 3)                        # its cost 3 spent (a burn) and reimbursed from the allowance — a return: the loan untouched
    assert L.wallet("G").U == pytest.approx(45.0) and w.arrival_loan["G"] == pytest.approx(50.0)
    reimb = [e for e in events_to(w, "G") if e.kind == "deposit_out"]
    assert len(reimb) == 1 and reimb[0].note.startswith("reimburse") and not w._is_income_event(reimb[0])
    assert not repaid_next(w, reimb[0])
    w.advance(w.cases[q].window_end + 1)              # vests: the fee 2 to G, repaid at once; the bond released, kept
    assert w.cases[q].state == "VESTED"
    fee = [e for e in events_to(w, "G") if e.kind == "feepot_out"]
    assert len(fee) == 1 and fee[0].note.endswith("review fee") and fee[0].amount == pytest.approx(2.0) and w._is_income_event(fee[0])
    rep = L.events[fee[0].seq + 1]
    assert rep.kind == "arrival_repayment" and rep.src == "G" and rep.amount == pytest.approx(2.0) and rep.note.startswith("arrival loan repaid")
    assert w.arrival_loan["G"] == pytest.approx(48.0) and w.names_repaid == pytest.approx(2.0) and w.name_repaid["G"] == pytest.approx(2.0)
    assert L.wallet("G").U == pytest.approx(50.0) and L.wallet("G").L == 0                # the fee netted, the bond back
    rel = [e for e in events_to(w, "G") if e.kind == "release"]
    assert rel and not any(repaid_next(w, e) for e in rel)
    assert w.names_lent == pytest.approx(w.names_repaid + w.names_recovered + w.names_outstanding + w.names_defaulted)
    check_all(w)


def test_the_delivery_price_repays_and_a_court_fee_coming_back_passes_untouched():
    w = make_world(pi0=0.1, n_min=2, panel_determined=False)   # the genesis reviewers may sit on the appeal panel without a plant record
    L = w.ledger
    w.arrive("G")
    admit(w, "G")                                     # two plant reviews: their fees repaid already
    loan0 = w.arrival_loan["G"]
    assert 0 < loan0 < 50.0 and loan0 == pytest.approx(50.0 - sum(e.amount for e in repayments_from_income(w, "G")))
    q = post_and_award(w, "G", 10, tau=4)             # admitted: awarded a root
    w.submit(q)
    c_rev = on_duty_reviewer(w)
    r = w.assign_initial(q, c_rev)
    w.complete_review(r, N, 0)                        # a false rejection
    u_before = L.wallet("G").U
    w.respond(q, "appeal", d="the work meets the specification")   # G pays the court fee D = 2 to Ω: an outflow
    assert L.wallet("G").U == pytest.approx(u_before - 2.0)
    for a in DUTY:                                    # two appeal reviewers: the challenge settles on two agreeing answers (§8.4)
        w.actors[a].on_duty = True
    panel = [a for a in DUTY if a != c_rev][:2]
    for a in panel:
        w.complete_review(w.assign_appeal(q, a), F, 0)
    assert w.cases[q].challenge["resolved"]           # the rejection overturned: the reviewer's bond pays G's fee back, the rest burned
    back = [e for e in events_to(w, "G") if e.kind == "forfeit_to" and "court fee" in e.note]
    assert len(back) == 1 and back[0].amount == pytest.approx(2.0) and not w._is_income_event(back[0])
    assert not repaid_next(w, back[0])
    assert w.arrival_loan["G"] == pytest.approx(loan0) and L.wallet("G").U == pytest.approx(u_before)
    w.advance(w.cases[q].window_end + 1)              # vests: the price 10 to G — income; the guarantee released — a return
    assert w.cases[q].state == "VESTED"
    price = [e for e in events_to(w, "G") if e.kind == "escrow_out" and e.note == "delivery price"]
    assert len(price) == 1 and price[0].amount == pytest.approx(10.0)
    rep = L.events[price[0].seq + 1]
    assert rep.kind == "arrival_repayment" and rep.src == "G" and rep.amount == pytest.approx(min(10.0, loan0))
    assert w.arrival_loan["G"] == pytest.approx(loan0 - min(10.0, loan0))
    check_all(w)


def test_a_kill_fee_and_a_childs_guarantee_forfeited_to_the_parent_are_income():
    # the kill fee: G an admitted arrival, the child of A's root; it spends, A cancels, the fee reaches G and repays
    w = make_world(pi0=0.1, n_min=2)
    L = w.ledger
    w.arrive("G")
    admit(w, "G")
    loan0 = w.arrival_loan["G"]
    q = post_and_award(w, "A", 40, beta=45, tau=50)
    w.advance(w.t + 1)
    qn = w.post_nested(q, 6)
    w.award(qn, "G", 5, 10)
    spent = w.spend("G", 3.0, qn)                     # a burn: not an inflow, the loan untouched
    assert w.arrival_loan["G"] == pytest.approx(loan0)
    w.advance(w.t + 2)
    w.cancel_nested(qn)
    kill = [e for e in events_to(w, "G") if e.note.startswith("kill fee")]
    assert kill and sum(e.amount for e in kill) == pytest.approx(min(spent, w.p.K))
    for e in kill:
        rep = L.events[e.seq + 1]
        assert rep.kind == "arrival_repayment" and rep.src == "G" and rep.amount == pytest.approx(min(e.amount, loan0))
    assert w.arrival_loan["G"] == pytest.approx(loan0 - sum(e.amount for e in kill))
    check_all(w)
    # the forfeited guarantee: G a parent, its child B misses the deadline; the lapse forfeits B's guarantee to G — income
    w2 = make_world(pi0=0.1, n_min=2)
    L2 = w2.ledger
    w2.arrive("G")
    admit(w2, "G")
    loan0 = w2.arrival_loan["G"]
    q = post_and_award(w2, "G", 40, beta=45, tau=50)
    w2.advance(w2.t + 1)
    qn = w2.post_nested(q, 6)
    w2.award(qn, "B", 5, 2)                           # G_child = ceil(0.5 × 5) = 3
    w2.advance(w2.cases[qn].deadline + 1)             # the lapse: final N, the guarantee to the parent
    assert w2.cases[qn].state == "FINAL_N"
    forf = [e for e in events_to(w2, "G") if e.kind == "forfeit_to" and "forfeit:" in e.note]
    assert len(forf) == 1 and forf[0].amount > 0 and w2._is_income_event(forf[0])
    rep = L2.events[forf[0].seq + 1]
    assert rep.kind == "arrival_repayment" and rep.src == "G" and rep.amount == pytest.approx(min(forf[0].amount, loan0))
    assert w2.arrival_loan["G"] == pytest.approx(loan0 - min(forf[0].amount, loan0))
    check_all(w2)


def test_every_inflow_to_a_name_with_a_loan_is_classified_by_the_table_and_the_record_holds_both_legs():
    # a long world with emission: every income event to the arrival is followed by its repayment while the loan stands, no return is
    w = make_world(pi0=0.1, n_min=2, E0=10.0)
    L = w.ledger
    w.arrive("G")
    admit(w, "G")
    w.actors["G"].on_duty = True
    for i in range(6):
        q = post_and_award(w, "A", 10, tau=3)
        w.submit(q)
        r = w.assign_initial(q, "G")
        w.complete_review(r, F, 2)
        w.advance(w.cases[q].window_end + 1)
    kinds_seen = set()
    for e in events_to(w, "G"):
        nxt = L.events[e.seq + 1] if e.seq + 1 < len(L.events) else None
        followed = nxt is not None and nxt.kind == "arrival_repayment" and nxt.src == "G" and nxt.note.startswith("arrival loan repaid")
        if w._is_income_event(e):
            kinds_seen.add((e.kind, e.note.split(" ")[-1] if e.kind != "fee_out" else e.note))
            assert followed or w.arrival_loan["G"] <= 1e-9 or nxt is None, (e.kind, e.note)
        else:
            assert not followed, (e.kind, e.note)
    assert ("feepot_out", "fee") in kinds_seen and any(k[0] == "fee_out" for k in kinds_seen)   # the fee and the emission share
    assert w.names_repaid == pytest.approx(sum(e.amount for e in repayments_from_income(w, "G")))
    check_all(w)


# ---------------------------------------------------------------- §2.1 recovered at departure

def test_depart_is_admissible_with_a_loan_outstanding_recovers_it_first_and_the_refusals_change_nothing():
    w = make_world()
    L = w.ledger
    w.arrive("G")
    # the four refusals, with a loan outstanding: nothing moves — the loan and the names line included
    w.actors["G"].on_duty = True
    q = post_and_award(w, "A", 10, tau=4)
    w.submit(q)
    r = w.assign_initial(q, "G")
    before = snapshot(w)
    with pytest.raises(RuleError):
        w.depart("G")                                 # an open review
    assert snapshot(w) == before
    w.complete_review(r, F, 0)
    before = snapshot(w)
    with pytest.raises(RuleError):
        w.depart("G")                                 # a review awaiting settlement (and the bond's lock)
    assert snapshot(w) == before
    w.advance(w.cases[q].window_end + 1)              # settles: the fee 2 repaid; the loan 48 still stands
    assert w.arrival_loan["G"] == pytest.approx(48.0) and L.wallet("G").U == pytest.approx(50.0) and L.wallet("G").L == 0
    # admissible with the loan outstanding: the wallet repays first, the remainder leaves
    M0 = L.M
    out = w.depart("G")
    assert out == pytest.approx(2.0)                                                  # 50 held, 48 recovered: its earnings leave
    assert "G" not in w.actors and "G" in w.departed_actors and "G" not in w.arrival_loan and "G" not in w.name_repaid
    assert L.M == pytest.approx(M0 - 50.0) and L.wallet("G").U == 0
    rec = [e for e in L.events if e.kind == "arrival_repayment" and e.src == "G" and e.note.startswith("departure")]
    dep = [e for e in L.events if e.kind == "departure" and e.src == "G"]
    assert len(rec) == 1 and rec[0].amount == pytest.approx(48.0) and len(dep) == 1 and dep[0].amount == pytest.approx(2.0)
    assert w.names_recovered == pytest.approx(48.0) and w.names_defaulted == 0 and w.names_outstanding == 0
    assert w.names_lent == pytest.approx(w.names_repaid + w.names_recovered + w.names_outstanding + w.names_defaulted)
    assert w.actor_departed_credits == pytest.approx(2.0) and w.departed == pytest.approx(2.0) and w.period["departed"] == pytest.approx(2.0)
    entry = [h for h in w.history.entries if h["kind"] == "entry" and h["payload"].get("msg") == "departed"][-1]["payload"]
    assert entry["wallet"] == pytest.approx(2.0) and entry["recovered"] == pytest.approx(48.0) and entry["defaulted"] == 0
    with pytest.raises(RuleError):
        w.arrive("G")
    check_all(w)


def test_the_six_cycler_carries_out_nothing_and_the_shortfall_is_the_banks_default():
    # §6: a stamper arrives, earns a fee, forfeits its bond on a bad plant it approves, is suspended and departs at once — the exit open
    w = make_world(pi0=0.1, n_min=2, T_susp=5)
    L = w.ledger
    w.arrive("G")
    w.actors["G"].on_duty = True
    q = post_and_award(w, "A", 10, tau=4)
    w.submit(q)
    r = w.assign_initial(q, "G")
    w.complete_review(r, F, 0)
    w.advance(w.cases[q].window_end + 1)              # the fee 2 repaid: L = 48, the wallet 50
    assert w.arrival_loan["G"] == pytest.approx(48.0)
    p = w.create_plant(False, 20.0)
    rp = w.assign_initial(p, "G")
    w.complete_review(rp, F, 0)                       # approves a bad plant: the bond 5 burned, suspended
    g = w.actors["G"]
    assert g.suspended_until is not None and L.wallet("G").U == pytest.approx(45.0) and L.wallet("G").L == 0
    M0 = L.M
    out = w.depart("G")                               # a suspension discharges every obligation: it leaves — with nothing
    assert out == 0 and L.M == pytest.approx(M0 - 45.0)
    assert w.names_recovered == pytest.approx(45.0) and w.names_defaulted == pytest.approx(3.0)   # the bond burned less the fee repaid
    assert not any(e.kind == "departure" and e.src == "G" for e in L.events)
    assert w.actor_departed_credits == 0
    check_all(w)


def test_the_six_leaver_takes_out_its_earnings_and_a_repaid_loan_recovers_nothing():
    # §6: a name with 40 of its loan outstanding and 95 in its wallet departs: 40 recovered, 55 out — its earnings to that tick
    w = make_world(F0=95.0, f_fee=55.0, phi_F_root=55.0)
    L = w.ledger
    w.arrive("G")
    w.actors["G"].on_duty = True
    q = post_and_award(w, "A", 10, tau=4)
    w.submit(q)
    r = w.assign_initial(q, "G")
    w.complete_review(r, F, 0)
    w.advance(w.cases[q].window_end + 1)              # one fee of 55: the loan 95 → 40, the wallet 95
    assert w.arrival_loan["G"] == pytest.approx(40.0) and L.wallet("G").U == pytest.approx(95.0)
    out = w.depart("G")
    assert out == pytest.approx(55.0) and w.names_recovered == pytest.approx(40.0) and w.names_defaulted == 0
    # a long-repaid loan: the wallet leaves whole, nothing recovered
    w2 = make_world(f_fee=30.0, phi_F_root=30.0)
    L2 = w2.ledger
    w2.arrive("G")
    w2.actors["G"].on_duty = True
    for i in range(3):                                # fees 30, 30, 30: the loan 50 → 20 → 0 (10 kept) → 30 kept
        q = post_and_award(w2, "A", 10, tau=4)
        w2.submit(q)
        r = w2.assign_initial(q, "G")
        w2.complete_review(r, F, 0)
        w2.advance(w2.cases[q].window_end + 1)
    assert w2.arrival_loan["G"] == 0 and L2.wallet("G").U == pytest.approx(90.0)        # §6: its wallet is its earnings
    assert w2.name_repaid["G"] == pytest.approx(50.0)
    out = w2.depart("G")
    assert out == pytest.approx(90.0) and w2.names_recovered == 0 and w2.names_defaulted == 0
    check_all(w)
    check_all(w2)


# ---------------------------------------------------------------- I41, the record, the control

def test_I41_holds_every_tick_and_catches_a_kept_income_or_a_broken_identity():
    w = make_world()
    w.arrive("G")
    w.advance(3)
    check_tick(w)
    check_all(w)
    w.names_lent += 1.0                               # the identity broken
    with pytest.raises(InvariantError):
        check_all(w)
    w.names_lent -= 1.0
    w.arrival_loan["A"] = 1.0                         # a loan on a genesis name
    with pytest.raises(InvariantError):
        check_all(w)
    del w.arrival_loan["A"]
    check_all(w)
    # an income kept with a loan outstanding: a fee credited to G without its repayment — I41 reads the record
    w2 = make_world()
    w2.arrive("G")
    w2._repaying = True                               # the hook silenced: the next fee is kept
    w2.actors["G"].on_duty = True
    q = post_and_award(w2, "A", 10, tau=4)
    w2.submit(q)
    r = w2.assign_initial(q, "G")
    w2.complete_review(r, F, 0)
    with pytest.raises(InvariantError):
        w2.advance(w2.cases[q].window_end + 1)


def test_the_period_record_and_the_view_carry_the_names_line_only_once_a_name_was_lent_to():
    w = make_world(period_ticks=5)
    w.advance(6)
    assert w.periods and "names" not in w.periods[-1]["bank"] and "arrival_repayment" not in w.periods[-1]["bank"]["destroyed"]
    w.arrive("G")
    w.advance(11)
    nm = w.periods[-1]["bank"]["names"]
    assert nm["lent"] == pytest.approx(50.0) and nm["lent_n"] == 1 and nm["outstanding"] == pytest.approx(50.0) and nm["lent_total"] == pytest.approx(50.0)
    assert w.periods[-1]["bank"]["destroyed"]["arrival_repayment"] == 0
    from drivers.view import Public
    v = Public(w)
    bk = v.bank()
    assert bk["loan_on"] and bk["names_lent"] == pytest.approx(50.0) and bk["names_outstanding"] == pytest.approx(50.0) and bk["destroyed"]["arrival_repayment"] == 0
    assert v.loan_outstanding("G") == pytest.approx(50.0) and v.loan_repaid("G") == 0 and v.loan_outstanding("A") == 0
    assert v.depart("G") == 0                         # the view returns the wallet out
    assert v.bank()["names_recovered"] == pytest.approx(50.0) and v.bank()["departed_net"] == 0
    check_all(w)


def test_arrival_loan_off_is_the_261_grant():
    w = make_world(arrival_loan=False)
    L = w.ledger
    assert not w.loan_on
    w.arrive("G")
    assert w.arrival_loan == {} and w.names_lent == 0 and "loan" not in [e for e in L.events if e.kind == "arrival"][0].note
    w.actors["G"].on_duty = True
    q = post_and_award(w, "A", 10, tau=4)
    w.submit(q)
    r = w.assign_initial(q, "G")
    w.complete_review(r, F, 0)
    w.advance(w.cases[q].window_end + 1)
    assert L.wallet("G").U == pytest.approx(52.0)      # the fee kept
    assert not any(e.kind == "arrival_repayment" for e in L.events)
    M0 = L.M
    out = w.depart("G")
    assert out == pytest.approx(52.0) and L.M == pytest.approx(M0 - 52.0)   # the grant carried out, as 2.3.0 had it
    assert any(e.kind == "departure" and e.src == "G" and e.amount == pytest.approx(52.0) for e in L.events)
    from drivers.view import Public
    assert not Public(w).bank()["loan_on"]
    check_all(w)

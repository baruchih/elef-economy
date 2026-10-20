"""Spec §17 invariants (twenty-five since 1.4.0). Each is a function of the whole world.

A failing invariant is a bug in the engine or a contradiction in the spec; it is never a
property of a strategy. Each check states what it actually establishes.

Two entry points, one set of predicates:

  check_all(w)   the full audit — every case, review and event, the record re-hashed from
                 genesis. What the tests call, and what `Params.full_check_every` schedules.
                 It is the only check that notices an edit to an entry it has already seen.
  check_tick(w)  what the engine runs after every tick — the same predicates over the
                 working set: cases and reviews that can still change, cases touched since
                 the last tick, and the events and record entries added since then. For a
                 world that is only ever changed through the engine's own operations, every
                 fact the full audit would establish, this establishes; its cost is what the
                 tick did, not what the run did.
"""
from __future__ import annotations
from itertools import islice
import hashlib
import math
from .ledger import Ledger, _i10_exempt, _i19_event_ok
PANEL_ROLES = ("appeal", "audit")              # the challenge-panel seats (1.2.0 §2.2)          # as the engine defines them (not imported: no cycle)
DUTY_FUND = "DUTY-FUND"

EPS = 1e-6

ALLOWED_EVENT_KINDS = {
    "lock", "release", "transfer", "forfeit_to", "burn_bond", "purchase",
    "mint_backed", "mint_emission", "issuance", "creation", "retirement", "departure", "escrow_in", "deposit_in", "feepot_in", "escrow_out",
    "deposit_out", "feepot_out", "fee_out",
    "mint_plant", "loan", "mint_scenario", "repayment", "retire_plant",     # 2.1.0: the bank's kinds
    "arrival",                                                              # 2.3.0: an arrival's float
}
GRADES = {"human-explicit", "delegate-explicit", "protocol-default", "procedural", "plant"}


class InvariantError(AssertionError):
    pass


def _fail(msg):
    raise InvariantError(msg)


def _fin(x):
    return isinstance(x, (int, float)) and math.isfinite(x)


def _tol(M: float) -> float:
    """Conservation tolerance. M is kept as a running sum while the balances are recomputed;
    the two drift apart by rounding in proportion to the supply, so the tolerance scales with
    it: one millionth of a credit per ten thousand credits in circulation."""
    return EPS * max(1.0, abs(M) / 1e4)


def _cases(w, cases):
    return w.cases.values() if cases is None else cases


def _reviews(w, reviews):
    return w.reviews.values() if reviews is None else reviews


def _peek(store, key):
    """Read a case or review without claiming it: in record mode a paged-out object comes back
    as a copy and the archive is not pulled into memory; in memory it is the object itself."""
    pk = getattr(store, "peek", None)
    return store[key] if pk is None else pk(key)


def _chunks(it, n):
    it = iter(it)
    while True:
        chunk = list(islice(it, n))
        if not chunk:
            return
        yield chunk


def I1_conservation(w, running: bool = False):
    """Every credit is in a wallet, a case pool, or Ω; their sum is M; and M equals the
    money minted minus the money burned according to the event log."""
    L = w.ledger
    tot = L.total_credits_running() if running else L.total_credits()
    if not _fin(tot) or not _fin(L.M) or abs(tot - L.M) > _tol(L.M):
        _fail(f"I1 conservation: wallets+pools={tot} != M={L.M}")
    recon = L.reconstruct_M_running() if running else L.reconstruct_M()
    if abs(recon - L.M) > _tol(L.M):
        _fail(f"I1 reconstruction: mints-burns={recon} != M={L.M}")


def I2_no_negative_or_nonfinite_balances(w, cases=None):
    for wl in w.ledger.wallets.values():
        if not _fin(wl.U) or not _fin(wl.L) or wl.U < -EPS or wl.L < -EPS:
            _fail(f"I2 bad balance in {wl.id}: U={wl.U} L={wl.L}")
    if cases is None:
        pools = w.ledger.pools.items()
    else:
        pools = [(c.id, w.ledger.pools[c.id]) for c in cases if c.id in w.ledger.pools]
    for cid, p in pools:
        for name, val in (("escrow", p.escrow), ("allowance", p.deposit), ("fee pot", p.fee_pot), ("minted", p.minted)):
            if not _fin(val) or val < -EPS:
                _fail(f"I2 bad {name} pool for {cid}: {val}")
    if not _fin(w.ledger.Res) or w.ledger.Res < -EPS:
        _fail("I2 bad reserve")


def I3_mints_and_burns(w, events=None):
    """Only known event kinds, with finite non-negative amounts; the only unbacked mint is
    emission; the only burns are bond forfeiture and resource purchase."""
    for e in (w.ledger.events if events is None else events):
        _I3_one(e)


def _I3_one(e):
    if e.kind not in ALLOWED_EVENT_KINDS:
        _fail(f"I3 unknown ledger event kind {e.kind}")
    if not _fin(e.amount) or e.amount < -EPS:
        _fail(f"I3 bad amount in {e.kind}: {e.amount}")


def I4_court_fee_once_and_within_bond(w, cases=None, reimb=None):
    """`reimb`, when given, is the court-fee reimbursement count per case from one pass over
    every event (`_audit_events`); otherwise the count is taken from the per-case event index."""
    by_case = w.ledger.events_by_case
    for c in _cases(w, cases):
        if c.court_fee_reimbursed > c.D + EPS:
            _fail(f"I4 {c.id}: court fee reimbursed {c.court_fee_reimbursed} > D {c.D}")
        if c.court_fee_reimbursed > EPS and c.court_fee_paid_by is None:
            _fail(f"I4 {c.id}: reimbursement without a paid fee")
        if c.nominals is not None and c.G_V + EPS < c.D:
            _fail(f"I4 {c.id}: bond {c.G_V} < court fee {c.D} (§7.2)")
        if reimb is not None:
            n_reimb = reimb.get(c.id, 0)
        else:
            n_reimb = sum(1 for e in by_case.get(c.id, ()) if e.kind == "forfeit_to" and "court fee" in e.note)
        if n_reimb > 1:
            _fail(f"I4 {c.id}: court fee reimbursed {n_reimb} times")


def I5_no_vest_with_open_items(w, cases=None):
    for c in _cases(w, cases):
        if c.state == "VESTED":
            if c.open_items != 0:
                _fail(f"I5 {c.id} vested with {c.open_items} open items")
            if c.challenge and not c.challenge["resolved"]:
                _fail(f"I5 {c.id} vested with an unresolved challenge")
            if c.t_vest is not None and c.window_end is not None and c.t_vest < c.window_end:
                _fail(f"I5 {c.id} vested before its window closed")
            if any(_peek(w.reviews, r).status == "open" for r in c.reviews):
                _fail(f"I5 {c.id} vested with an open review")


def I6_commit_before_audit(w, cases=None):
    for c in _cases(w, cases):
        for rid in c.reviews:
            r = _peek(w.reviews, rid)
            if r.role == "audit" and (c.t_verdict is None or r.t_assign < c.t_verdict):
                _fail(f"I6 {c.id}: audit assigned at {r.t_assign} before the verdict at {c.t_verdict}")


def I7_child_milestone_before_parent_submit(w, cases=None):
    """A parent submits only after every nested request reached its milestone (§9.1): an
    initial verdict, or a terminal state — the same definition the submit guard uses."""
    for c in _cases(w, cases):
        if c.t_submit is None:
            continue
        for ch in c.children:
            child = _peek(w.cases, ch)
            if child.t_post > c.t_submit:
                continue                              # posted after this submission (a resubmission)
            if child.t_verdict is not None and child.t_verdict <= c.t_submit:
                continue
            if child.state in ("WITHDRAWN", "CANCELLED", "FINAL_N") and child.t_verdict is None:
                continue
            _fail(f"I7 {c.id} submitted at {c.t_submit} before nested {ch} reached its milestone")


def I8_positions_bound(w, cases=None):
    for c in _cases(w, cases):
        # the engine's `_positions`, read without claiming the case or its reviews
        n = sum(1 for rid in c.reviews if _peek(w.reviews, rid).status != "withdrawn")
        if n > w.p.V_max:
            _fail(f"I8 {c.id} holds {n} review positions > V_max")


def I9_reserve(w):
    """The reserve holds min(X_t, eligible) (1.2.0 §2.2, amending the 1.1.0 'holds X'): a reserve
    short of X_t is admissible only when the last rotation found no eligible free actor to seat,
    and the gap is then counted as the eligibility shortfall."""
    if not w.enforce_reserve:
        return
    n = sum(1 for a in w.actors.values() if a.on_duty)
    X = max(w.X_t, w._x_target) if w.p.seat_the_queue else w.X_t     # 1.6.0 §2.3: at least the reviews waiting
    if n < X and not w._pool_exhausted and not w._reserve_dirty:
        _fail(f"I9 reserve {n} < target {X} (X_t={w.X_t}) while eligible actors were free to seat")
    if n < X and not w._reserve_dirty and w.reserve_shortfall_now != X - n:
        _fail(f"I9 reserve short by {X - n} but the shortfall counted is {w.reserve_shortfall_now}")


def _I10_event(e, c):
    if c.t_vest is not None and e.t > c.t_vest and not _i10_exempt(e.note):
        _fail(f"I10 {c.id}: {e.kind} {e.amount} at t={e.t} after vesting at {c.t_vest}")


def I10_no_post_vesting_adjudication_moves_money(w, cases=None, events=True):
    """After vesting, no adjudication moves money on account of the case (§6). Obligations
    established before vesting — deferred reimbursements, Ω claims — may still be paid; and, since
    1.1.0 (§4.3), a nested case may draw on its root's pots and the tree's closure returns the
    root's unused deposit — exactly those exceptions, recognised by the event's note.
    With `events` false the per-event half has been done by one pass over every event
    (`_audit_events`); otherwise it is taken from the per-case event index."""
    by_case = w.ledger.events_by_case
    for c in _cases(w, cases):
        if c.t_vest is None:
            continue
        if events:
            for e in by_case.get(c.id, ()):
                _I10_event(e, c)
        if c.post_vesting_funds_moved > EPS:
            _fail(f"I10 {c.id}: override moved funds after vesting")


def I11_exclusive_failure_indicators(w, cases=None):
    for c in _cases(w, cases):
        if c.I_N and c.I_pool:
            _fail(f"I11 {c.id}: I_N and I_pool both set")


def I12_frozen_nominals(w, cases=None):
    """Nominals are fixed at the case's first lock (§4.5) and G at award; neither changes after.
    Both pots are nominals: frozen with the case."""
    for c in _cases(w, cases):
        if c.nominals is not None and (c.D, c.K, c.G_V, c.phi_E, c.phi_F) != c.nominals:
            _fail(f"I12 {c.id}: nominals changed after they were frozen")
        if c.G_award is not None and c.G != c.G_award:
            _fail(f"I12 {c.id}: G changed after award")
        if c.is_nested() and c.nominals is not None and c.state == "AVAILABLE":
            if abs(c.rejection_bond - c.G_V) > EPS:
                _fail(f"I12 {c.id}: rejection bond {c.rejection_bond} != frozen G_V {c.G_V}")


def I13_grade_provenance(w, cases=None):
    """Every settled case carries exactly one grade, and the grade is justified by the record:
    human/delegate-explicit needs a matching explicit root judgment; procedural needs a
    challenge, an audit, or a nested case; protocol-default needs none of these."""
    for c in _cases(w, cases):
        settled = c.final and c.state in ("VESTED", "FINAL_N")
        if not settled:
            if c.grade is not None:
                _fail(f"I13 {c.id} graded before settlement")
            continue
        if c.grade not in GRADES:
            _fail(f"I13 {c.id} final without a valid grade: {c.grade}")
        if (c.grade == "plant") != (c.plant is not None):
            _fail(f"I13 {c.id}: the plant grade belongs to plants and only to them (graded {c.grade})")
        if c.plant is not None:
            continue
        if c.is_nested():
            if c.grade != "procedural":
                _fail(f"I13 nested {c.id} graded {c.grade}")
            continue
        matching = [a for a in c.assessments if a[2] == c.outcome and a[3] in ("accept", "dispute", "override")]
        explicit = bool(matching)
        audited = any(_peek(w.reviews, r).role == "audit" and _peek(w.reviews, r).status != "withdrawn"
                      for r in c.reviews)
        if c.grade in ("human-explicit", "delegate-explicit"):
            if not explicit:
                _fail(f"I13 {c.id} graded {c.grade} without a matching explicit root judgment")
            author = matching[-1][1]                   # the grade is the establishing event's author's
            want = "delegate-explicit" if author in w.delegates else "human-explicit"
            if c.grade != want:
                _fail(f"I13 {c.id} graded {c.grade}, but the establishing judgment was by {author}")
        elif c.grade == "procedural":
            if explicit:
                _fail(f"I13 {c.id} graded procedural despite a matching explicit judgment")
            if not (c.challenge_round_used or audited):
                _fail(f"I13 {c.id} graded procedural with no challenge or audit")
        else:
            if explicit or c.challenge_round_used or audited:
                _fail(f"I13 {c.id} graded protocol-default despite record events")


def I14_one_active_assignment(w, reviews=None):
    """One active assignment per actor: at most one ordinary commitment, at most one open
    review, and never both (§2.2)."""
    open_by = {}
    _I14_reviews(_reviews(w, reviews), open_by)
    _I14_actors(w, open_by)


def _I14_reviews(reviews, open_by):
    for r in reviews:
        if r.status == "open":
            if r.reviewer in open_by:
                _fail(f"I14 {r.reviewer} holds two open reviews")
            open_by[r.reviewer] = r.id


def _I14_actors(w, open_by):
    seen = {}
    for a in w.actors.values():
        if a.committed:
            if a.committed in seen:
                _fail(f"I14 case {a.committed} committed to two actors")
            seen[a.committed] = a.id
            st = _peek(w.cases, a.committed).state
            if st not in ("COMMITTED", "SUBMITTED", "AWAITING_RESPONSE", "RESUBMITTING"):
                _fail(f"I14 {a.id} committed to {a.committed} in state {st}")
            if a.id in open_by:
                _fail(f"I14 {a.id} is committed and holds an open review")
        if a.open_review and a.open_review not in w.reviews:
            _fail(f"I14 {a.id} open_review points nowhere")
        if a.open_review and _peek(w.reviews, a.open_review).status not in ("open", "done"):
            _fail(f"I14 {a.id} attached to a review that is {_peek(w.reviews, a.open_review).status}")


def I15_locks_reconcile(w, cases=None, reviews=None):
    """Every wallet's L equals the sum of its lock records, and every live obligation in the
    engine has a lock record of exactly its size: guarantees, bonds, nested ceilings,
    rejection bonds. No record exists for an obligation that has ended."""
    _I15_wallets(w)
    expected = {}
    _I15_expected_cases(_cases(w, cases), expected, w.p.net_plant_capital, w.ledger.resolve)
    _I15_expected_reviews(_reviews(w, reviews), expected, w.ledger.resolve)
    _I15_expected_world(w, expected)
    _I15_compare(w, expected)


def _I15_wallets(w):
    L = w.ledger
    for wid, wl in L.wallets.items():
        recs = sum(L.locks.get(wid, {}).values())
        if abs(recs - wl.L) > EPS:
            _fail(f"I15 {wid}: L={wl.L} but lock records sum to {recs}")


def _I15_expected_cases(cases, expected, netted_plants: bool = True, resolve=lambda x: x):
    for c in cases:
        market_plant = c.plant is not None and getattr(c, "plant_market", False)   # 2.6.0: a market plant's money is real
        if c.actor and c.state in ("COMMITTED", "SUBMITTED", "AWAITING_RESPONSE", "RESUBMITTING", "PENDING") \
                and not (netted_plants and c.plant is not None and not market_plant):   # 1.3.0 §2.5: a plant's guarantee binds nothing
            expected[(resolve(c.actor), f"G:{c.id}")] = c.G          # a troop's lock sits on the fund (1.4.0); a plant actor's on its wallet
        if c.is_nested() and c.state == "AVAILABLE":
            expected[(c.requester, f"beta:{c.id}")] = c.posting_lock if c.own_pots else c.beta   # 2.3.0: the all-in with the pots
        if c.is_root and c.state == "AVAILABLE" and (c.plant is None or market_plant) and c.index_at_lock is not None:
            expected[(resolve(c.requester), f"post:{c.id}")] = c.posting_lock    # 2.0.0 §2.1 / I29: the posting lock
        if c.is_nested() and c.rejection_bond > EPS:
            expected[(c.requester, f"rej:{c.id}")] = c.rejection_bond


def _I15_expected_world(w, expected):
    """2.2.0 §2.2: the rebate pool is a lock on Ω of exactly the fee income accrued this period after the debt."""
    if getattr(w, "pool_on", False) and w.omega_pool > EPS:
        expected[(w.ledger.OMEGA, f"pool:{w.pool_index}")] = w.omega_pool


def _I15_expected_reviews(reviews, expected, resolve=lambda x: x):
    for r in reviews:
        if r.status in ("open", "done"):
            expected[(resolve(r.reviewer), f"bond:{r.id}")] = r.bond


def _I15_compare(w, expected):
    L = w.ledger
    actual = {(wid, key): amt for wid, d in L.locks.items() for key, amt in d.items() if amt > EPS}
    for k, amt in expected.items():
        if abs(actual.get(k, 0.0) - amt) > EPS:
            _fail(f"I15 obligation {k} expects lock {amt}, record holds {actual.get(k, 0.0)}")
    for k in actual:
        if k not in expected:
            _fail(f"I15 lock record {k} has no live obligation")


def _log_pos(c, entry) -> int:
    """A case log entry is (t, msg, committed position); anything else is a tampered copy."""
    if not isinstance(entry, (tuple, list)) or len(entry) != 3 or isinstance(entry[2], bool) \
            or not isinstance(entry[2], int):
        _fail(f"I16 case log of {c.id} holds a malformed entry: {entry!r}")
    return entry[2]


def _check_case_log(w, c, want):
    if len(c.log) != len(want):
        _fail(f"I16 case log of {c.id} holds {len(c.log)} entries; the record holds {len(want)}")
    for entry, hseq in zip(c.log, want):
        if len(entry) != 3 or entry[2] != hseq or \
                not w.history.matches(hseq, "case", {"t": entry[0], "case": c.id, "msg": entry[1]}):
            _fail(f"I16 case log of {c.id} differs from its committed entry: {entry!r}")


def I16_history_is_authoritative(w):
    """The History chain verifies, and every working copy is a complete, ordered, faithful
    projection of it: the ledger's event list holds exactly the committed ledger entries in
    order, and each case log holds exactly that case's committed entries in order. The
    History is the record; the copies are checked against it, never the other way round.

    Established in two passes that stream the record rather than index it. Over the record:
    the ledger entries are paired one-to-one, in order, with the event copy, and each case
    entry is found in its case's log at the position the log claims. Over the cases: each log
    is strictly increasing in committed position, and the logs together hold exactly as many
    entries as the record holds case entries. A log entry names one position and one case, so
    the entries matched are distinct; equal counts make the match a bijection, and the
    increasing positions make it order-preserving — the same fact the v1.0.1 engine
    established by listing every case's positions."""
    if not w.history.verify():
        _fail("I16 history chain does not verify")
    events = iter(w.ledger.events)
    n_ledger = n_case = matched = 0
    for i, e in enumerate(w.history.entries):
        if e["kind"] == "ledger":
            n_ledger += 1
            ev = next(events, None)
            if ev is None:
                _fail(f"I16 ledger copy holds {n_ledger - 1} events; the record holds more")
            if ev.hseq != i or not w.history.matches(i, "ledger", ev.payload()):
                _fail(f"I16 ledger event #{ev.seq} ({ev.kind}) differs from its committed entry")
        elif e["kind"] == "case":
            n_case += 1
            cid = e["payload"]["case"]
            c = _peek(w.cases, cid) if cid in w.cases else None
            log = c.log if c is not None else []
            lo, hi = 0, len(log)                 # first log entry at a committed position >= i
            while lo < hi:
                mid = (lo + hi) // 2
                if _log_pos(c, log[mid]) < i:
                    lo = mid + 1
                else:
                    hi = mid
            k = lo
            if k >= len(log) or _log_pos(c, log[k]) != i or \
                    (log[k][0], cid, log[k][1]) != (e["payload"]["t"], e["payload"]["case"], e["payload"]["msg"]):
                _fail(f"I16 committed case entry #{i} for {cid} is not in its case log")
            matched += 1
    if next(events, None) is not None:
        _fail(f"I16 ledger copy holds {len(w.ledger.events)} events; the record holds {n_ledger}")
    total = 0
    for c in w.cases.values():
        last = -1
        for entry in c.log:
            if _log_pos(c, entry) <= last:
                _fail(f"I16 case log of {c.id} is not in committed order: {entry!r}")
            last = entry[2]
        total += len(c.log)
    if total != matched or total != n_case:
        _fail(f"I16 case logs hold {total} entries; the record holds {n_case}")


def I16_tick(w, cases, new_events, hist_from: int):
    """The per-tick form of I16: the chain is verified from where it was last verified; the
    ledger events appended since then are checked against their committed entries, one copy
    per committed ledger entry, in order; the logs of the cases in scope are checked whole
    against the positions the engine committed them at."""
    if not w.history.verify_new():
        _fail("I16 history chain does not verify")
    committed_ledger = [i for i, e in enumerate(w.history._iter_from(hist_from), hist_from)
                        if e["kind"] == "ledger"]
    if len(new_events) != len(committed_ledger):
        _fail(f"I16 ledger copy gained {len(new_events)} events; the record gained {len(committed_ledger)}")
    for e, hseq in zip(new_events, committed_ledger):
        if e.hseq != hseq or not w.history.matches(hseq, "ledger", e.payload()):
            _fail(f"I16 ledger event #{e.seq} ({e.kind}) differs from its committed entry")
    for c in cases:
        _check_case_log(w, c, w._case_entries.get(c.id, []))


def I17_debts_and_claims_reconcile(w, cases=None, reviews=None):
    """Deferred and pending reimbursements are non-negative; every Ω claim names a review whose
    pending field covers it; the pending fields sum to the claims; no ended nested obligation
    still carries a rejection bond."""
    pending = {}
    _I17_reviews(w, _reviews(w, reviews), pending)
    _I17_claims(w, pending)
    _I17_cases(_cases(w, cases))


def _I17_reviews(w, reviews, pending):
    for r in reviews:
        if r.deferred < -EPS or r.reimbursed_pending < -EPS or r.reimbursed < -EPS:
            _fail(f"I17 review {r.id} has a negative reimbursement field")
        if r.reimbursed + r.reimbursed_pending + r.deferred > min(r.cost, _peek(w.cases, r.case).K) + EPS:
            _fail(f"I17 review {r.id} reimbursed beyond its capped cost")
        if r.reimbursed_pending > EPS:
            pending[r.id] = r.reimbursed_pending


def _I17_claims(w, pending):
    claimed = {}
    for cl in w.omega_claims:
        if cl.amount <= EPS or cl.review not in w.reviews:
            _fail(f"I17 malformed Ω claim {cl!r}")
        if _peek(w.reviews, cl.review).reviewer != cl.reviewer:
            _fail(f"I17 Ω claim {cl!r} names the wrong reviewer")
        claimed[cl.review] = claimed.get(cl.review, 0.0) + cl.amount
    for rid in set(pending) | set(claimed):
        if abs(pending.get(rid, 0.0) - claimed.get(rid, 0.0)) > EPS:
            _fail(f"I17 review {rid}: pending {pending.get(rid, 0.0)} != claims {claimed.get(rid, 0.0)}")


def _I17_cases(cases):
    for c in cases:
        if c.is_nested() and c.state in ("VESTED", "FINAL_N", "CANCELLED", "WITHDRAWN") and c.rejection_bond > EPS:
            _fail(f"I17 nested {c.id} is {c.state} but still carries a rejection bond")


def I18_no_audit_outlives_a_ruling(w, cases=None):
    """Once a human has ruled on a case, no audit of it is open or assigned afterwards: an
    audit open at the ruling was voided by it, and none is admitted after it."""
    for c in _cases(w, cases):
        ruled = [a for a in c.assessments if a[3] == "override"]
        if not ruled:
            continue
        t_rule = min(a[0] for a in ruled)
        for rid in c.reviews:
            r = _peek(w.reviews, rid)
            if r.role != "audit":
                continue
            if r.t_assign > t_rule:
                _fail(f"I18 {c.id}: audit {rid} assigned after a human ruling")
            if r.status == "open":
                _fail(f"I18 {c.id}: audit {rid} still open after a human ruling")


CHECKS = [I1_conservation, I2_no_negative_or_nonfinite_balances, I3_mints_and_burns,
          I4_court_fee_once_and_within_bond, I5_no_vest_with_open_items, I6_commit_before_audit,
          I7_child_milestone_before_parent_submit, I8_positions_bound, I9_reserve,
          I10_no_post_vesting_adjudication_moves_money, I11_exclusive_failure_indicators,
          I12_frozen_nominals, I13_grade_provenance, I14_one_active_assignment,
          I15_locks_reconcile, I16_history_is_authoritative, I17_debts_and_claims_reconcile,
          I18_no_audit_outlives_a_ruling]


def I19_the_pots(w, cases=None, events=None):
    """1.1.0 §4.3: the expense allowance and the fee pot are accounted separately. For every root
    (the pots are the root's): fees paid from the pot never exceed φ^F; fee money went to expenses
    only at tree closure and only up to what was left after every fee in the tree; nothing came
    back to the requester before the tree closed; a closed tree has every case final and both pots
    empty. The event half: no fee is paid from the allowance; the fee pot pays fixed fees, and at
    closure the tree's expense debts and the refund, nothing else."""
    for e in ([] if events is None else events):
        if not _i19_event_ok(e):
            _fail(f"I19 {e.case}: {e.kind} {e.amount} '{e.note}' crosses the pots")
    for c in _cases(w, cases):
        if c.nominals is None or not (c.is_root or c.own_pots):
            continue
        if c.fees_from_pot > c.phi_F + EPS:
            _fail(f"I19 {c.id}: fees {c.fees_from_pot} paid from a pot of {c.phi_F}")
        if c.expenses_from_pot > c.phi_F - c.fees_from_pot + EPS:
            _fail(f"I19 {c.id}: expenses {c.expenses_from_pot} from the pot exceed what fees left of {c.phi_F}")
        moved_back = c.expenses_from_pot > EPS or c.pot_refunded > EPS or c.allowance_refunded > EPS
        closed = c.node_closed if c.own_pots else c.tree_closed      # 2.3.0 (the ruling): 'for every case' — a node closes itself
        if moved_back and not closed:
            _fail(f"I19 {c.id}: fee money reached expenses or the requester before the {'node' if c.own_pots else 'tree'} closed")
        if c.own_pots and c.node_closed:
            pl = w.ledger.pools.get(c.id)
            if pl is not None and (pl.deposit > EPS or pl.fee_pot > EPS):
                _fail(f"I19 {c.id}: node closed with {pl.deposit} allowance and {pl.fee_pot} fee pot left")
            if not c.final:
                _fail(f"I19 {c.id}: node closed while {c.state}")
            continue
        if c.tree_closed:
            pl = w.ledger.pools.get(c.id)
            if pl is not None and (pl.deposit > EPS or pl.fee_pot > EPS):
                _fail(f"I19 {c.id}: tree closed with {pl.deposit} allowance and {pl.fee_pot} fee pot left")
            stack = list(c.children)
            while stack:
                ch = _peek(w.cases, stack.pop())
                if not ch.final or ch.needs_review_settlement:
                    _fail(f"I19 {c.id}: tree closed while {ch.id} is {ch.state}")
                stack.extend(ch.children)


def I20_plants_self_adjudicated(w, cases=None):
    """1.2.0 §2.1: a plant's outcome is set only by its known truth; no audit, appeal, dispute or
    ruling is ever opened on it; its marker is in the History at creation, sealed, and revealed
    only at adjudication — the reveal names the truth and nonce that hash to the commitment.
    (That a plant's view is indistinguishable is a property of the view function, asserted by a
    test, not a per-tick predicate.)"""
    for c in _cases(w, cases):
        if c.plant is None:
            continue
        if c.challenge is not None or c.challenge_round_used:
            _fail(f"I20 {c.id}: a challenge was opened on a plant")
        if any(a[3] in ("override", "dispute", "accept") for a in c.assessments):
            _fail(f"I20 {c.id}: a root judgment or ruling was recorded on a plant")
        if c.plant_commit is None or c.plant_hseq is None or \
                not w.history.matches(c.plant_hseq, "plant_created", {"t": c.t_post, "case": c.id, "commit": c.plant_commit}):
            _fail(f"I20 {c.id}: the plant marker is not committed at creation")
        initial = [_peek(w.reviews, rid) for rid in c.reviews]
        if any(r.role != "initial" for r in initial):
            _fail(f"I20 {c.id}: a plant carries a non-initial review")
        done = [r for r in initial if r.status in ("done", "vested", "overturned")]
        if c.plant_outcome is None:
            if done or c.plant_reveal_hseq is not None:
                _fail(f"I20 {c.id}: a plant review completed without adjudication")
            continue
        if len(done) != 1 or c.plant_reveal_hseq is None:
            _fail(f"I20 {c.id}: adjudicated plant without exactly one completed review and a reveal")
        r = done[0]
        truth = "good" if c.plant else "bad"
        if hashlib.sha256(f"{c.id}|{truth}|{c.plant_nonce}".encode()).hexdigest() != c.plant_commit:
            _fail(f"I20 {c.id}: the revealed truth does not hash to the sealed commitment")
        if not w.history.matches(c.plant_reveal_hseq, "plant_revealed",
                                 {"t": r.t_done, "case": c.id, "truth": truth, "nonce": c.plant_nonce, "commit": c.plant_commit,
                                  "review": r.id, "reviewer": r.reviewer, "verdict": r.verdict, "outcome": c.plant_outcome}):
            _fail(f"I20 {c.id}: the reveal is not the committed one")
        right = (r.verdict == "F") == c.plant
        if c.plant_outcome == "stood" and not (right and r.status in ("done", "vested")):
            _fail(f"I20 {c.id}: plant 'stood' but the review was {r.verdict} on a {truth} plant / {r.status}")
        if c.plant_outcome == "failure" and not (r.verdict in ("F", "N") and not right and r.status == "overturned"):
            _fail(f"I20 {c.id}: plant 'failure' but the review was {r.verdict} on a {truth} plant / {r.status}")
        if c.plant_outcome == "spent" and r.verdict not in ("P", "⊥"):
            _fail(f"I20 {c.id}: plant 'spent' by a {r.verdict} verdict")
        if c.final and c.plant and c.state not in ("PENDING", "VESTED") and c.plant_outcome != "spent":
            _fail(f"I20 {c.id}: a good plant settled {c.state}")
        if c.final and not c.plant and c.state != "FINAL_N":
            _fail(f"I20 {c.id}: a bad plant settled {c.state}")


def I21_dial_and_reserve(w, reviews=None):
    """1.2.0 §2.3: 1 ≤ m_t ≤ m_max and each step within [0.9, 2]; π_t ≤ π_max; X_t ≥ V_max + 1; no
    assignment was made to an actor ineligible for its tier at the time; no actor remains on duty
    past the completion of its active review once duty-ineligible; the shortfalls are counted."""
    p = w.p
    if not (1.0 - EPS <= w.m_t <= p.m_max + EPS):
        _fail(f"I21 m_t={w.m_t} outside [1, {p.m_max}]")
    if w.pi_t > p.pi_max + EPS or w.pi_t < -EPS:
        _fail(f"I21 π_t={w.pi_t} outside [0, {p.pi_max}]")
    if w.X_t < p.V_max + 1:
        _fail(f"I21 X_t={w.X_t} below V_max + 1")
    for per in w.periods[-1:]:
        lo, hi = 0.9 * per["m_before"] - EPS, 2.0 * per["m_before"] + EPS
        if not (max(lo, 1.0 - EPS) <= per["m"] <= min(hi, p.m_max + EPS)) and per["m"] != per["m_before"]:
            _fail(f"I21 dial step {per['m_before']} → {per['m']} outside its bounds")
    for a in w.actors.values():
        if a.on_duty and not a.duty_eligible and a.open_review is None:
            _fail(f"I21 {a.id} remains on duty, duty-ineligible, with no active review")
    for r in _reviews(w, reviews):
        if not r.panel_ok:
            _fail(f"I21 review {r.id} was assigned to an actor ineligible for its tier")
    if w.plant_shortfall < 0 or w.eligibility_shortfall < 0:
        _fail("I21 a shortfall count is negative")


def I21_plant_capital(w, cases=None):
    """I21 amended (1.3.0 §2.5): a plant's award and guarantee tie up no balance — no escrow in its pool,
    no guarantee lock on the plant actor; B and G stay frozen nominals that bind nothing."""
    if not w.p.net_plant_capital:
        return
    L = w.ledger
    for c in _cases(w, cases):
        if c.plant is None or getattr(c, "plant_market", False):      # 2.6.0: a market plant's award and guarantee are real
            continue
        pl = L.pools.get(c.id)
        if pl is not None and pl.escrow > EPS:
            _fail(f"I21 plant {c.id} holds {pl.escrow} in escrow; its award is notional")
        if L.lock_record(c.actor, f"G:{c.id}") > EPS:
            _fail(f"I21 plant {c.id} has a guarantee lock; its guarantee is notional")


def I22_membership(w, reviews=None):
    """1.3.0 §2.1–2.2: no award is made to an actor that is suspended or on probation; no probationer
    holds an audit, appeal or dispute seat; every probationer's applied audit odds are 1; a readmission
    happens only with a passing trailing record and at least n_min outcomes since the suspension began."""
    if not w.p.membership:
        return
    for a in w.actors.values():
        if a.probation and a.p_eff != 1.0:
            _fail(f"I22 probationer {a.id} has applied audit odds {a.p_eff} ≠ 1")
        if a.probation and a.suspended_until is not None:
            _fail(f"I22 {a.id} is both suspended and on probation")
        if a.readmitted_at == w.t and (a.since_susp < w.p.n_min or not a.record_passes(w.p.theta_duty)):
            _fail(f"I22 {a.id} readmitted with {a.since_susp} outcomes since suspension / record failing")
    for r in _reviews(w, reviews):
        if r.status == "open" and r.role in ("appeal", "audit") and r.reviewer in w.actors and w.actors[r.reviewer].probation:
            _fail(f"I22 probationer {r.reviewer} holds a panel seat ({r.role} {r.id})")
        # 1.6.0 §2.4: once the world's first plant is adjudicated, no undetermined member holds a panel seat
        if r.status == "open" and r.role in ("appeal", "audit") and r.reviewer in w.actors and w.p.panel_determined \
                and w.first_plant_adjudicated_at is not None and r.t_assign >= w.first_plant_adjudicated_at \
                and len(w.actors[r.reviewer].plant_bad) < w.p.n_min:
            _fail(f"I22 undetermined member {r.reviewer} holds a panel seat ({r.role} {r.id}) after the first plant")


def _I22_cases(w, cases):
    for c in cases:
        if not c.member_at_award:
            _fail(f"I22 {c.id} was awarded to a non-member")
        if w.is_troop(c.actor) != c.troop_award:
            _fail(f"I22 {c.id}: a troop holds an award without a summons, or a summons without a troop (1.4.0 §2.3)")


def I23_load_and_fund(w):
    """1.3.0 §2.3–2.4: no member is seated while on-duty members ≥ ⌈E_t/2⌉ — a member above the cap holds
    no assignment past the completion of its active review; on-duty members ≥ min(V_max − 1, E_t)
    whenever that many free, fundable members exist to seat; the duty fund equals the raised tax collected
    less the uplifts paid, and holds no lock."""
    p = w.p
    if p.membership:
        E_t = sum(1 for a in w.actors.values() if a.is_member and a.record_passes(p.theta_duty))
        cap = w._member_cap(E_t)
        floor = min(p.V_max - 1, E_t)
        on_m = [a for a in w.actors.values() if a.on_duty and a.is_member]
        idle_above = [a for a in on_m if a.open_review is None and not a.volunteer]
        if len(on_m) > max(cap, floor) and idle_above and not w._reserve_dirty:
            # above the cap only members mid-review (or volunteers) may remain; the idle ones must have left
            _fail(f"I23 {len(on_m)} members on duty above the cap {cap} with {len(idle_above)} idle")
        if len(on_m) < floor and not w._member_pool_exhausted and not w._reserve_dirty:
            _fail(f"I23 {len(on_m)} members on duty below the panel floor {floor} while members were free to seat")
        # 1.6.0 §2.3: member seats at least the panel seats waiting, within the cap, while members were free to seat
        if p.seat_the_queue and len(on_m) < min(cap, w._waiting_panel) and not w._member_pool_exhausted and not w._reserve_dirty:
            _fail(f"I23 {len(on_m)} members on duty with {w._waiting_panel} panel seats waiting under the cap {cap}")
    if p.duty_fund and p.floating:
        # 2.0.0: the uplift fund is 1.3.0's (the raised tax in, uplift out, no lock); the troops' wallet is Ω and the
        # reserves, the advance and the order are retired (I28 holds the deficit)
        u = w.ledger.wallet(DUTY_FUND)
        if abs(u.W - (w.fund_in - w.fund_out)) > _tol(w.ledger.M):
            _fail(f"I23 uplift fund {u.W} ≠ the raised tax received {w.fund_in} less the uplift paid {w.fund_out}")
        if u.L > EPS:
            _fail(f"I23 the uplift fund holds a lock {u.L}")
        if w._uplift_violation:
            _fail(f"I23 {w._uplift_violation}")
    elif p.duty_fund:
        f = w.ledger.wallet(w.troop_wallet)       # 1.7.0 §2.1: the troop account; before it, the merged duty fund
        if p.troop_account:
            # the uplift fund is 1.3.0's again: the raised tax in, uplift out, no reserve, no lock, no other flow
            u = w.ledger.wallet(DUTY_FUND)
            if abs(u.W - (w.fund_in - w.fund_out)) > _tol(w.ledger.M):
                _fail(f"I23 uplift fund {u.W} ≠ the raised tax received {w.fund_in} less the uplift paid {w.fund_out}")
            if u.L > EPS:
                _fail(f"I23 the uplift fund holds a lock {u.L}")
        # 1.4.0: the fund's locks are troops' bonds and guarantees and nothing else (I15 reconciles them)
        troop_locks = 0.0
        for t in w.troops.values():
            if t["kind"] == "review":
                r = _peek(w.reviews, t["review"]) if t["review"] else None
                if r is not None and r.status in ("open", "done"):
                    troop_locks += r.bond
            else:
                c = _peek(w.cases, t["case"])
                if c.state in ("COMMITTED", "SUBMITTED", "AWAITING_RESPONSE", "RESUBMITTING", "PENDING"):
                    troop_locks += c.G
        if abs(f.L - troop_locks) > EPS:
            _fail(f"I23 the duty fund holds locks {f.L} beyond the troops' {troop_locks}")
        # conservation: the wallet equals every event into it less every event out of it (tax, troop earnings
        # and advances in; costs purchased, uplifts, bond burns, forfeits and repayments out)
        if abs(f.W - w.fund_flow) > _tol(w.ledger.M):
            _fail(f"I23 duty fund {f.W} ≠ its recorded flows {w.fund_flow}")
        if not p.omega_backs_fund and (w.advance_outstanding > p.A_T + EPS or w.advance_outstanding < -EPS):
            _fail(f"I23 Ω's advance outstanding {w.advance_outstanding} outside [0, A_T={p.A_T}]")
        if w.advance_outstanding < -EPS:
            _fail(f"I23 Ω's advance outstanding {w.advance_outstanding} negative")
        if p.reserve_demand or p.troop_account:  # 1.5.0 §2.1 / 1.7.0 §2.1: the reserve is at least the capital held ...
            held = sum(t["cost"] + t["lock"] for t in w.troops.values() if t["t_release"] is None)
            if w.R_T + EPS < held:
                _fail(f"I23 reserve {w.R_T} below the capital troops hold {held}")
        if p.reserve_demand and not p.troop_account:   # ... and under the demand reserve the last demand too
            if w.R_T + EPS < w.troop_demand_now:
                _fail(f"I23 reserve {w.R_T} below the demand at the last seating {w.troop_demand_now}")
        if w._uplift_violation:
            _fail(f"I23 {w._uplift_violation}")


def I26_service(w, cases=None):
    """1.6.0 §2.1: every root request's clock stops once, at its first verdict or at its final without one; the rebate
    owed is min(r_s · ticks late, B), paid or carried as Ω's liability — paid plus outstanding equals owed, a bookkeeping
    identity over the counter; waiting items are served oldest-first in every summons pass (a younger case summoned after
    an older one of the same kind was refused for funds is the violation)."""
    if not w.p.service_clock:
        return
    if w._priority_violation:
        _fail(f"I26 {w._priority_violation}")
    outstanding = sum(l["amount"] for l in w.omega_liabilities)
    if getattr(w, "pool_on", False):
        # 2.2.0: a claim is paid at the close or forgone; the identity is over claims, paid, forgone and this period's pending claims
        pending = w.period["claims_total"]
        if abs(w.rebates_owed - (w.rebates_paid + w.rebates_forgone + pending)) > _tol(w.ledger.M):
            _fail(f"I26 claims {w.rebates_owed} ≠ paid {w.rebates_paid} + forgone {w.rebates_forgone} + pending {pending}")
    elif abs(w.rebates_owed - (w.rebates_paid + w.liabilities_accrued)) > EPS:
        _fail(f"I26 rebates owed {w.rebates_owed} ≠ paid {w.rebates_paid} + liabilities accrued {w.liabilities_accrued}")
    if abs(outstanding - (w.liabilities_accrued - w.liabilities_paid)) > EPS:
        _fail(f"I26 liabilities outstanding {outstanding} ≠ accrued {w.liabilities_accrued} − paid {w.liabilities_paid}")
    for c in _cases(w, cases):
        if not c.is_root or c.plant is not None:
            continue
        if c.clock_stopped_at is not None:
            B = c.B if c.B else 0.0
            if w.p.r_s > 0:                     # §4.5: r_s indexed at the case's first lock (2.2.0's conformance correction)
                idx = (c.index_at_lock if c.index_at_lock is not None else w.ledger.index()) if w.p.floating else 1.0
                r_s = w.p.r_s * idx
            else:
                r_s = w.p.omega_rate * B
            owed = min(r_s * c.late_ticks, B) if B > 0 else 0.0
            if abs(c.rebate_owed - owed) > EPS:
                _fail(f"I26 {c.id} rebate owed {c.rebate_owed} ≠ min(r_s·late, B) = {owed}")
            if c.rebate_paid > c.rebate_owed + EPS:
                _fail(f"I26 {c.id} rebate paid {c.rebate_paid} above what was owed {c.rebate_owed}")
            if c.late_ticks != max(0, c.clock_ticks - w.p.T_s):
                _fail(f"I26 {c.id} lateness {c.late_ticks} ≠ clock {c.clock_ticks} − T_s {w.p.T_s}")
        elif c.first_verdict_at is not None or (c.final and c.state in ("FINAL_N", "VESTED")):
            if w.p.service_clock and c.B:
                _fail(f"I26 {c.id} reached a verdict or a final without its clock stopping")
        if c.state == "WITHDRAWN" and c.rebate_owed > EPS:
            _fail(f"I26 {c.id} withdrawn before award yet owed a rebate")


def I24_troops(w, cases=None):
    """1.4.0 §2.1–2.3: a troop holds exactly one seat from summons to release and no seat thereafter; it
    is not an actor (no ρ, κ, membership state or plant record); no troop reviews a plant or acts in one;
    a troop review carries no emission and no uplift; no troop takes the audit of a troop reviewer's
    approval of a troop's delivery; a troop's delivery is at B̄ where β ≥ B̄."""
    for tid, t in w.troops.items():
        if tid in w.actors:
            _fail(f"I24 troop {tid} is an actor")
        c = _peek(w.cases, t["case"])
        if c.plant is not None:
            _fail(f"I24 troop {tid} on plant {c.id}")
        if t["kind"] == "review":
            r = _peek(w.reviews, t["review"])
            if r.reviewer != tid or r.case != c.id:
                _fail(f"I24 troop {tid}'s seat {t['review']} is not its own")
            if (r.status == "open") == (t["t_release"] is not None):
                _fail(f"I24 troop {tid}: seat {r.status} but release {t['t_release']}")
            if r.role == "audit" and c.market_audit_only:
                _fail(f"I24 troop {tid} audits the state's own work on {c.id}")
            if r.uplift > EPS:
                _fail(f"I24 troop {tid} drew uplift {r.uplift}")
        else:
            if c.actor != tid or not c.troop_award:
                _fail(f"I24 troop {tid}'s delivery {c.id} is not its own award")
            if c.beta + EPS < c.B:
                _fail(f"I24 troop {tid} delivered {c.id} above its ceiling")
            if (c.final) != (t["t_release"] is not None):
                _fail(f"I24 troop {tid}: case {c.state} but release {t['t_release']}")
    if w.p.floating:
        # 2.0.0 §2.6 (Appendix M): a seat holds one place, a delivery two until its initial review is assigned, then one;
        # the places held never exceed N_T
        held = 0
        for tid, t in w.troops.items():
            if t["t_release"] is not None:
                continue
            pl = t.get("places", 1)
            held += pl
            if t["kind"] == "review" and pl != 1:
                _fail(f"I24 troop seat {tid} holds {pl} places")
            if t["kind"] == "delivery":
                c = _peek(w.cases, t["case"])
                seated = any(_peek(w.reviews, r).role == "initial" for r in c.reviews)
                if pl not in (1, 2) or (seated and pl != 1):
                    _fail(f"I24 troop delivery {tid} holds {pl} places with its inspection {'seated' if seated else 'unseated'}")
        if w.p.N_T > 0 and held > w.p.N_T:
            _fail(f"I24 {held} places held above N_T = {w.p.N_T}")
    seats = {}
    for tid, t in w.troops.items():
        key = ("r", t["review"]) if t["kind"] == "review" else ("c", t["case"])
        if key in seats:
            _fail(f"I24 troops {seats[key]} and {tid} hold the same seat")
        seats[key] = tid


def I25_the_obligation(w, cases=None):
    """1.4.0 §2.2: a case with a rolled audit outstanding does not vest — without exception; a troop
    reviewer's approval of a troop's delivery carries audit odds 1 (the engine records that obligation at
    the verdict) and vests only after a member's audit completed. A pinned reviewer's approval is audited
    because the orchestrator rolls at odds 1 and records the roll — that is the driver's conformance under
    §18.2, which the engine then holds; it is not a predicate the engine can check on a world whose
    orchestrator never rolls."""
    for c in _cases(w, cases):
        if c.state != "VESTED":
            continue
        if c.audit_obligation or c.audit_vacated:
            _fail(f"I25 {c.id} vested with an audit obligation outstanding")
        if c.market_audit_only:
            audits = [_peek(w.reviews, r) for r in c.reviews if _peek(w.reviews, r).role == "audit"]
            audited = any(r.status in ("done", "vested", "overturned") for r in audits)
            ruled = any(a[3] == "override" for a in c.assessments)
            if not audited and not ruled:
                _fail(f"I25 {c.id}: the state's own work vested without the market's audit")
            if any(w.is_troop(r.reviewer) for r in audits):
                _fail(f"I25 {c.id}: a troop audited the state's own work")


def I27_price_and_indexing(w, cases=None):
    """2.0.0 §2.3: P_t is the trailing mean awarded price on B̄'s window (P_0 before the first award) and the ledger
    indexes by it; every nominal of a case priced under 2.0.0 equals its base times the index at the case's first lock
    (§4.5, frozen); B̄ counts members' awards only (the summons never passes through `award`, so the period's award
    count is at most its price count)."""
    if not w.p.floating:
        return
    if abs(w.ledger.P_t - w.price_level()) > EPS:
        _fail(f"I27 the ledger's P_t {w.ledger.P_t} ≠ the price level {w.price_level()}")
    if abs(w.ledger.index() - w.price_level() / w.p.P0) > EPS:
        _fail(f"I27 index {w.ledger.index()} ≠ P_t/P_0")
    if w.period["award_n"] > w.period["price_n"]:
        _fail(f"I27 B̄ counts {w.period['award_n']} awards against {w.period['price_n']} prices")
    p = w.p
    for c in _cases(w, cases):
        if c.index_at_lock is None or c.plant is not None or not c.is_root:
            continue
        idx = c.index_at_lock
        for name, have, base in (("D", c.D, p.D), ("K", c.K, p.K), ("G_V", c.G_V, p.G_V),
                                 ("phi_E", c.phi_E, p.phi_E_root), ("phi_F", c.phi_F, p.phi_F_root)):
            if abs(have - base * idx) > EPS:
                _fail(f"I27 {c.id} {name} = {have} ≠ {base} × {idx} frozen at its first lock")


def I28_the_deficit(w):
    """2.0.0 §2.5: Ω creates only for a payment the rules require (or the declared scenario operation) and only when its
    unlocked balance cannot meet it; while the deficit stands Ω's unlocked balance is zero at the tick's end; deficit
    outstanding = created − retired ≥ 0. 2.1.0 (rewritten) — the bank: Ω never creates; the bank creates only by the three
    mintings and the loans; a loan is tied to a summons and repaid from its own return; what is lent is outstanding, repaid
    or debt, and nothing else; nothing is created for a rebate; nothing minted for a plant reaches Ω."""
    if not w.p.floating:
        return
    if w._creation_violation:
        _fail(f"I28 {w._creation_violation}")
    if w.bank_on:
        if w.deficit_created > EPS or w.deficit_retired > EPS:
            _fail(f"I28 Ω created {w.deficit_created} under the bank")
        lent, repaid = w.bank_minted["loan"], w.bank_destroyed["repayment"]
        if abs(lent - repaid - w.loans_outstanding - w.debt) > _tol(w.ledger.M):
            _fail(f"I28 lent {lent} ≠ repaid {repaid} + outstanding {w.loans_outstanding} + debt {w.debt}")
        if w.debt < -EPS or (w.debt > EPS and w.debt_since is None):
            _fail(f"I28 debt {w.debt} with age {w.debt_since}")
        for tid, ln in w.loans.items():
            t = w.troops.get(tid)
            if t is None or ln["amount"] < -EPS:
                _fail(f"I28 loan {ln} on no summons")
            if t["kind"] == "delivery" and t["t_release"] is not None:
                _fail(f"I28 loan on the released delivery troop {tid} still open")
            if t["kind"] == "review" and t["review"] is not None and _peek(w.reviews, t["review"]).status in ("vested", "overturned", "withdrawn"):
                _fail(f"I28 loan on the settled seat {tid} still open")
        return
    if w.deficit_created + EPS < w.deficit_retired:
        _fail(f"I28 retired {w.deficit_retired} more than created {w.deficit_created}")
    if w.deficit > EPS and w.ledger.wallet(w.ledger.OMEGA).U > EPS:
        _fail(f"I28 Ω holds {w.ledger.wallet(w.ledger.OMEGA).U} unlocked while its deficit is {w.deficit}")
    if w.deficit > EPS and w.deficit_since is None:
        _fail("I28 the deficit's age is not recorded")


_CREATION_NOTES = {"creation: summons", "creation: plant", "creation: rebate", "creation: scenario: deficit shock"}
_LOAN_NOTES = {"loan: delivery", "loan: review"}
_PLANT_WALLETS = {"OMEGA-REQ", "OMEGA-ACT"}             # engine.PLANT_REQ / PLANT_ACT (not imported: no cycle)


def I30_the_bank(w):
    """2.1.0 §2.4, I30: the bank's identity — while debt or liabilities stand Ω's unlocked balance is zero at the start of the
    summons pass and at the tick's end; a delivery is lent for only within the wall; a seat is never refused for credit; the
    loans outstanding are open summonses' (I28 holds the lent = repaid + outstanding + debt identity)."""
    if not getattr(w, "bank_on", False):
        return
    if w._wall_violation:
        _fail(f"I30 {w._wall_violation}")
    if w._order_violation:
        _fail(f"I30 {w._order_violation}")
    om = w.ledger.wallet(w.ledger.OMEGA).U
    if (w.debt > EPS or (w.omega_liabilities and not getattr(w, "pool_on", False))) and om > EPS:
        _fail(f"I30 Ω holds {om} unlocked at the tick's end with debt {w.debt} and {len(w.omega_liabilities)} liabilities")
    if w.troop_refused_credit_seats:
        _fail(f"I30 {w.troop_refused_credit_seats} review seats refused for credit")
    if w.debt_peak + EPS < w.debt or w.loans_peak + EPS < w.loans_outstanding:
        _fail("I30 a peak below its current value")


def I32_the_pool(w):
    """2.2.0 §2.2: the pool is a lock on Ω of the fee income accrued after the debt this period, untouched until the close; no
    liability stock exists and nothing is owed across a close; every claim settled is paid or forgone, never carried."""
    if not getattr(w, "pool_on", False):
        return
    if w._pool_violation:
        _fail(f"I32 {w._pool_violation}")
    rec = w.ledger.lock_record(w.ledger.OMEGA, f"pool:{w.pool_index}")
    if abs(rec - w.omega_pool) > EPS or w.omega_pool < -EPS:
        _fail(f"I32 the pool lock {rec} ≠ the pool {w.omega_pool}")
    if w.omega_pool > w.period["pool"] + EPS:
        _fail(f"I32 the pool {w.omega_pool} above the period's fee income {w.period['pool']}")
    if w.omega_liabilities:
        _fail(f"I32 a liability stock of {len(w.omega_liabilities)} under the pool")
    if w.liabilities_accrued > EPS:
        _fail(f"I32 liabilities accrued {w.liabilities_accrued} under the pool")
    if abs(w.rebates_owed - (w.rebates_paid + w.rebates_forgone + w.period["claims_total"])) > _tol(w.ledger.M):
        _fail(f"I32 claims {w.rebates_owed} ≠ paid {w.rebates_paid} + forgone {w.rebates_forgone} + this period's {w.period['claims_total']}")


def I33_entry_through_inspection(w, cases=None):
    """2.3.0 §2.1: an arrival holds no award — root or nested — and no panel seat until admitted on n_min bad plants with a passing
    record; its odds read 1 until then; its float was minted once, at arrival."""
    if not getattr(w, "supply_on", False):
        return
    if w._supply_violation:
        _fail(f"I33 {w._supply_violation}")
    arrivals = {a.id: a for a in w.actors.values() if a.arrived_at is not None}
    if not arrivals:
        return
    for a in arrivals.values():
        if a.admitted_at is None:
            if a.is_member:                         # a probationer, or suspended after a plant failure — never a member
                _fail(f"I33 arrival {a.id} is a member before admission")
            if a.suspended_until is None and abs(a.p_eff - 1.0) > EPS:
                _fail(f"I33 arrival {a.id} odds {a.p_eff} before admission")
        elif len(a.plant_bad) < w.p.n_min and a.admitted_at is not None and a.suspended_until is None:
            pass                                    # the record window may have rolled; admission itself needed n_min at the time
    for c in _cases(w, cases):
        a = arrivals.get(c.actor) if c.actor else None
        if a is not None and c.t_award is not None and (a.admitted_at is None or c.t_award < a.admitted_at) and c.plant is None:
            _fail(f"I33 arrival {a.id} awarded {c.id} at {c.t_award} before admission {a.admitted_at}")
    for r in w._live_reviews.values():
        a = arrivals.get(r.reviewer)
        if a is not None and a.admitted_at is None and r.role in PANEL_ROLES and r.status in ("open", "done"):
            _fail(f"I33 arrival {a.id} holds the panel seat {r.id} before admission")


def I34_a_clean_departure(w):
    """2.3.0 §2.2: a departed identity is gone — not an actor, holding no balance or lock, never readmitted."""
    if not getattr(w, "supply_on", False):
        return
    for name, a in w.departed_actors.items():
        if name in w.actors:
            _fail(f"I34 departed {name} is an actor again")
        wl = w.ledger.wallets.get(name)
        if wl is not None and (wl.U > EPS or wl.L > EPS):
            _fail(f"I34 departed {name} still holds {wl.U} / {wl.L}")
        if a.committed is not None or a.open_review is not None:
            _fail(f"I34 departed {name} left with an obligation")


def I35_the_summons_is_for_roots(w):
    """2.3.0 §2.4: no troop delivers a nested request."""
    for tid, t in w.troops.items():
        if t["kind"] == "delivery":
            c = _peek(w.cases, t["case"])
            if not c.is_root:
                _fail(f"I35 troop {tid} delivers the nested request {c.id}")


def I36_the_pots_grow_with_the_tree(w, cases=None):
    """2.3.0 §2.4 (I36): under the parent's pots every awarded nested case carries its own two pots, posted by the parent at its posting
    index, and its reviews never draw on the root's deposit."""
    if not getattr(w, "parent_pots", False):
        return
    for c in _cases(w, cases):
        if not c.is_nested() or c.t_award is None:
            continue
        if not c.own_pots:
            _fail(f"I36 nested {c.id} awarded without its own pots")
        if c.index_at_lock is None or abs(c.phi_E - w.p.phi_E_root * c.index_at_lock) > EPS or abs(c.phi_F - w.p.phi_F_root * c.index_at_lock) > EPS:
            _fail(f"I36 nested {c.id} pots {c.phi_E} / {c.phi_F} are not the defaults at its posting index {c.index_at_lock}")


def I37_the_states_reservation(w, cases=None):
    """2.4.0 §2.1–2.2 (I37): the state's price is p_T = max(B̄, the reservation); no troop delivers a request whose ceiling is below
    the reservation, and every troop delivery is priced at or above it; a live root request with β below the reservation carries the
    mark (and one at or above it does not); its clock does not run while it holds the mark; the reservation is nominal (a parameter)."""
    if not getattr(w.p, "floating", False):
        return
    floor = w.p.state_reservation
    for tid, t in w.troops.items():
        if t["kind"] != "delivery":
            continue
        c = _peek(w.cases, t["case"])
        if c.beta + 1e-9 < floor:
            _fail(f"I37 troop {tid} delivers {c.id} whose ceiling {c.beta} is below the state's reservation {floor}")
        if c.B is not None and c.B + 1e-9 < floor:
            _fail(f"I37 troop {tid} delivers {c.id} at {c.B}, below the state's reservation {floor}")
    for c in _cases(w, cases):
        if not c.is_root or (c.plant is not None and not getattr(c, "plant_market", False)) or c.final or c.state != "AVAILABLE":
            continue
        below = c.beta + 1e-9 < floor
        if below != c.below_reservation:
            _fail(f"I37 {c.id} β {c.beta} against the reservation {floor}: marked {c.below_reservation}")
        if below and c.below_reservation_since is None:
            _fail(f"I37 {c.id} marked without its tick")
        if below and w.p.service_clock and w._clock_runs(c):
            _fail(f"I37 the clock of {c.id} runs while it is below the state's reservation")


def I38_the_missed_child(w, cases=None):
    """2.5.0 §9.3 (I38): no cancelled nested case closed at or after its deadline; every committed nested case past its deadline is final N
    with its guarantee forfeited to the parent (the lapse's own check, stated); the parent may submit from the next step."""
    if not getattr(w.p, "missed_child", False):
        return
    for c in _cases(w, cases):
        if not c.is_nested() or c.deadline is None:
            continue
        if c.state == "CANCELLED" and c.t_closed is not None and c.t_closed >= c.deadline:
            _fail(f"I38 nested {c.id} cancelled at {c.t_closed}, at or after its deadline {c.deadline}")
        if c.state == "COMMITTED" and w.t > c.deadline:
            _fail(f"I38 nested {c.id} committed past its deadline {c.deadline} at tick {w.t}: the lapse did not run")


def I31_the_index_per_period(w):
    """2.1.0 §2.5: P_t is what the bank published at the last period boundary and does not move within a period."""
    if not getattr(w, "bank_on", False):
        return
    if abs(w.ledger.P_t - w._P_published) > EPS:
        _fail(f"I31 the ledger's P_t {w.ledger.P_t} ≠ the published {w._P_published}")
    if w._P_published_at is not None and w._P_published_at != w.period["start"]:
        _fail(f"I31 P_t published at {w._P_published_at}, not at the period boundary {w.period['start']}")
    if w._P_published_at is None and abs(w._P_published - w.p.P0) > EPS:
        _fail(f"I31 P_t {w._P_published} before any boundary")


def I29_the_posting_lock(w, cases=None):
    """2.0.0 §2.1: a root request holds, from posting to award, a lock of its all-in maximum at its posting index
    (raised with its ceiling); after the award or withdrawal nothing of it remains."""
    if not w.p.floating:
        return
    for c in _cases(w, cases):
        market_plant = c.plant is not None and getattr(c, "plant_market", False)
        if not c.is_root or (c.plant is not None and not market_plant) or c.index_at_lock is None:
            continue
        held = w.ledger.lock_record(c.requester, f"post:{c.id}")
        if c.state == "AVAILABLE":
            # 2.6.0: a plant's all-in carries no fee — it pays none (nothing minted for it reaches Ω)
            want = c.beta * (1.0 + (0.0 if market_plant else w.p.omega_rate * c.m_post)) + c.phi_E + c.phi_F
            if abs(held - want) > EPS or abs(c.posting_lock - want) > EPS:
                _fail(f"I29 {c.id} holds {held} against its all-in maximum {want} (recorded {c.posting_lock})")
        elif held > EPS:
            _fail(f"I29 {c.id} is {c.state} and still holds a posting lock {held}")


CHUNK = 2048


def _audit_events(w) -> dict:
    """One pass over every ledger event, for the full audit: I3 on each; the court-fee
    reimbursement count per case (I4); and no movement on account of a vested case after its
    vesting (I10). Returns the counts."""
    reimb: dict[str, int] = {}
    for e in w.ledger.events:
        _I3_one(e)
        if e.kind == "creation" and e.note not in _CREATION_NOTES:
            _fail(f"I28 creation '{e.note}' is not a payment the rules require")
        if e.kind == "creation" and getattr(w, "bank_on", False):
            _fail("I28 Ω created under the bank")
        if e.kind == "loan" and (e.note not in _LOAN_NOTES or e.case is None):
            _fail(f"I28 loan '{e.note}' on {e.case} is not a summons's")
        if e.kind == "mint_plant" and e.dst not in _PLANT_WALLETS:
            _fail(f"I28 mint_plant to {e.dst}")
        if e.kind == "mint_scenario" and e.note != "mint_scenario: deficit shock":
            _fail(f"I28 mint_scenario '{e.note}'")
        if e.kind == "retire_plant" and e.src not in _PLANT_WALLETS:
            _fail(f"I28 retire_plant from {e.src}")
        if e.kind == "repayment" and e.src != w.ledger.OMEGA:
            _fail(f"I28 repayment from {e.src}")
        if not _i19_event_ok(e):
            _fail(f"I19 {e.case}: {e.kind} {e.amount} '{e.note}' crosses the pots")
        cid = e.case
        if cid is None:
            continue
        if e.kind == "forfeit_to" and "court fee" in e.note:
            reimb[cid] = reimb.get(cid, 0) + 1
        if cid in w.cases:
            _I10_event(e, _peek(w.cases, cid))
    return reimb


def I39_the_plants_disguise(w, cases=None):
    """2.6.0 §2.1 (I39): a plant lives a root's life — posted (its id minted then, in sequence with the roots around it), available,
    awarded to a fresh plant-actor name on the market's report or at p_T past w_A, submitted at its drawn tick within (t_award, deadline];
    its requester and actor names are fresh per plant and alias the two plant wallets; it pays no fee, its clock never runs, it is never
    a troop's; a market plant is never built submitted."""
    if not getattr(w.p, "plant_market", False):
        return
    L = w.ledger
    by_req, by_act = {}, {}
    for c in _cases(w, cases):
        if c.plant is None:
            continue
        if not getattr(c, "plant_market", False):
            _fail(f"I39 {c.id}: a plant built submitted under plant_market")
        if not c.requester.startswith("plant_req:") or L.resolve(c.requester) != "OMEGA-REQ":
            _fail(f"I39 {c.id}: the plant requester {c.requester} is not a fresh alias of the plant wallet")
        if by_req.setdefault(c.requester, c.id) != c.id:
            _fail(f"I39 {c.id}: two plants share the requester name {c.requester}")
        if c.actor is not None:
            if not c.actor.startswith("plant_act:") or L.resolve(c.actor) != "OMEGA-ACT":
                _fail(f"I39 {c.id}: the plant actor {c.actor} is not a fresh alias of the plant wallet")
            if by_act.setdefault(c.actor, c.id) != c.id:
                _fail(f"I39 {c.id}: two plants share the actor name {c.actor}")
            if c.t_award is None or c.t_award < c.t_post or c.deadline != c.t_award + c.tau:
                _fail(f"I39 {c.id}: award {c.t_award}, posting {c.t_post}, deadline {c.deadline}, tau {c.tau}")
            if c.plant_submit_at is None or not (c.t_award < c.plant_submit_at <= c.deadline):
                _fail(f"I39 {c.id}: the submission tick {c.plant_submit_at} is not within (t_award, deadline]")
            if c.state == "COMMITTED" and w.t > c.plant_submit_at:
                _fail(f"I39 {c.id}: committed past its submission tick {c.plant_submit_at} at {w.t}")
            if c.t_submit is not None and c.t_submit != c.plant_submit_at:
                _fail(f"I39 {c.id}: submitted at {c.t_submit}, drawn {c.plant_submit_at}")
        if c.omega > EPS:
            _fail(f"I39 {c.id}: a plant paid a fee {c.omega}")
        if c.troop_award:
            _fail(f"I39 {c.id}: a plant delivered by a troop")
        if c.actor is not None and c.actor in w.troops:
            _fail(f"I39 {c.id}: a plant's actor holds a place in N_T")
        if c.refused not in (None, "capacity", "credit"):
            _fail(f"I39 {c.id}: an unknown mark {c.refused}")
        if w.p.service_clock and w._clock_runs(c):
            _fail(f"I39 {c.id}: a plant's clock runs")
        if c.state == "AVAILABLE" and c.t_award is not None:
            _fail(f"I39 {c.id}: available with an award")


def public_id(cid: str) -> str:
    """2.6.0 §2.3 (I40): a case's identifier on the public surface — a hash of the engine's id; order carries nothing. Translated both
    ways by `drivers.view.Public`; the engine, the record and the History's chain run on the creation counter."""
    return "c" + hashlib.sha256(f"elef-public|{cid}".encode()).hexdigest()[:10]


def I40_opaque_identifiers(w, cases=None):
    """2.6.0 §2.3 (I40): the public identifiers are a bijection on the cases and carry no order — among the live cases the public ids
    are distinct and, once there are a few, not in creation order."""
    if not getattr(w.p, "plant_market", False):
        return
    seen, ids = {}, []
    for c in _cases(w, cases):
        pid = public_id(c.id)
        if pid in seen and seen[pid] != c.id:
            _fail(f"I40 public id {pid} names both {seen[pid]} and {c.id}")
        seen[pid] = c.id
        ids.append((int(c.id[1:]), pid))
    ids.sort()
    if len(ids) >= 12 and all(ids[i][1] < ids[i + 1][1] for i in range(len(ids) - 1)):
        _fail("I40 the public identifiers follow the creation order")


def check_all(w):
    """The full audit: every predicate over everything, the record re-hashed from genesis.
    The record is streamed — one pass over the events, one over the reviews, one over the
    cases in chunks, two for I16 — so that in record mode nothing paged out is pulled back
    into memory whole. The facts established are those of the predicates above, which is
    what `check_tick` runs over the working set."""
    I1_conservation(w)
    reimb = _audit_events(w)                                 # I3; the per-event halves of I4 and I10
    I9_reserve(w)
    open_by, expected, pending = {}, {}, {}
    _I14_reviews(w.reviews.values(), open_by)
    _I15_expected_reviews(w.reviews.values(), expected, w.ledger.resolve)
    _I17_reviews(w, w.reviews.values(), pending)
    _I14_actors(w, open_by)
    _I17_claims(w, pending)
    I2_no_negative_or_nonfinite_balances(w, [])              # the wallets and the reserve
    for chunk in _chunks(w.cases.values(), CHUNK):
        I2_no_negative_or_nonfinite_balances(w, chunk)       # the chunk's pools
        I4_court_fee_once_and_within_bond(w, chunk, reimb=reimb)
        I5_no_vest_with_open_items(w, chunk)
        I6_commit_before_audit(w, chunk)
        I7_child_milestone_before_parent_submit(w, chunk)
        I8_positions_bound(w, chunk)
        I10_no_post_vesting_adjudication_moves_money(w, chunk, events=False)
        I11_exclusive_failure_indicators(w, chunk)
        I12_frozen_nominals(w, chunk)
        I13_grade_provenance(w, chunk)
        _I15_expected_cases(chunk, expected, w.p.net_plant_capital, w.ledger.resolve)
        _I17_cases(chunk)
        I18_no_audit_outlives_a_ruling(w, chunk)
        I19_the_pots(w, chunk)                               # the event half was done in _audit_events
        I20_plants_self_adjudicated(w, chunk)
        I21_plant_capital(w, chunk)
        if w.p.membership:
            _I22_cases(w, chunk)
        I25_the_obligation(w, chunk)
    _I15_wallets(w)
    _I15_expected_world(w, expected)
    _I15_compare(w, expected)
    I21_dial_and_reserve(w)
    I22_membership(w)
    I23_load_and_fund(w)
    I24_troops(w)
    I26_service(w)
    I27_price_and_indexing(w)
    I28_the_deficit(w)
    I29_the_posting_lock(w)
    I30_the_bank(w)
    I31_the_index_per_period(w)
    I32_the_pool(w)
    I33_entry_through_inspection(w)
    I34_a_clean_departure(w)
    I35_the_summons_is_for_roots(w)
    I36_the_pots_grow_with_the_tree(w)
    I37_the_states_reservation(w)
    I38_the_missed_child(w)
    I39_the_plants_disguise(w)
    I40_opaque_identifiers(w)
    I16_history_is_authoritative(w)


def check_tick(w):
    """The per-tick check over the working set. See the module docstring."""
    if w._violations:                       # I4/I10 facts established as the events were recorded
        _fail(w._violations[0])
    cases = list(w._live_cases.values())
    in_scope = set(w._live_cases)
    for cid in w._dirty_cases:
        if cid not in in_scope and cid in w.cases:
            cases.append(w.cases[cid])
            in_scope.add(cid)
    # a child's change can only bear on its parent's I7; bring parents in once
    with_parents = list(cases)
    for c in cases:
        if c.parent is not None and c.parent not in in_scope:
            with_parents.append(w.cases[c.parent])
            in_scope.add(c.parent)
    reviews = dict(w._live_reviews)
    for c in cases:
        for rid in c.reviews:
            if rid not in reviews:
                reviews[rid] = w.reviews[rid]
    reviews = list(reviews.values())
    new_events = w.ledger.events[w._events_checked:]
    hist_from = w.history._verified_upto

    I1_conservation(w, running=True)
    I2_no_negative_or_nonfinite_balances(w, cases)
    I3_mints_and_burns(w, new_events)
    I4_court_fee_once_and_within_bond(w, cases)
    I5_no_vest_with_open_items(w, cases)
    I6_commit_before_audit(w, cases)
    I7_child_milestone_before_parent_submit(w, with_parents)
    I8_positions_bound(w, cases)
    I9_reserve(w)
    I10_no_post_vesting_adjudication_moves_money(w, cases)
    I11_exclusive_failure_indicators(w, cases)
    I12_frozen_nominals(w, cases)
    I13_grade_provenance(w, cases)
    I14_one_active_assignment(w, reviews)
    I15_locks_reconcile(w, cases, reviews)
    I16_tick(w, cases, new_events, hist_from)
    I17_debts_and_claims_reconcile(w, cases, reviews)
    I18_no_audit_outlives_a_ruling(w, cases)
    I19_the_pots(w, cases, new_events)
    I20_plants_self_adjudicated(w, cases)
    I21_dial_and_reserve(w, reviews)
    I21_plant_capital(w, cases)
    I22_membership(w, reviews)
    if w.p.membership:
        _I22_cases(w, cases)
    I23_load_and_fund(w)
    I24_troops(w)
    I25_the_obligation(w, cases)
    I26_service(w, cases)
    I27_price_and_indexing(w, cases)
    I28_the_deficit(w)
    I29_the_posting_lock(w, cases)
    I30_the_bank(w)
    I31_the_index_per_period(w)
    I32_the_pool(w)
    I33_entry_through_inspection(w, cases)
    I34_a_clean_departure(w)
    I35_the_summons_is_for_roots(w)
    I36_the_pots_grow_with_the_tree(w, cases)
    I37_the_states_reservation(w, cases)
    I38_the_missed_child(w, cases)
    I39_the_plants_disguise(w, cases)
    I40_opaque_identifiers(w, cases)

    w._events_checked = len(w.ledger.events)
    w._prune_working_set()

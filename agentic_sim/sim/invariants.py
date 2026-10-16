"""Spec §17 invariants. Each is a function of the whole world.

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
import math
from .ledger import Ledger

EPS = 1e-6

ALLOWED_EVENT_KINDS = {
    "lock", "release", "transfer", "forfeit_to", "burn_bond", "purchase",
    "mint_backed", "mint_emission", "escrow_in", "deposit_in", "escrow_out",
    "deposit_out", "fee_out",
}
GRADES = {"human-explicit", "delegate-explicit", "protocol-default", "procedural"}


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
        for name, val in (("escrow", p.escrow), ("deposit", p.deposit), ("minted", p.minted)):
            if not _fin(val) or val < -EPS:
                _fail(f"I2 bad {name} pool for {cid}: {val}")
    if not _fin(w.ledger.Res) or w.ledger.Res < -EPS:
        _fail("I2 bad reserve")


def I3_mints_and_burns(w, events=None):
    """Only known event kinds, with finite non-negative amounts; the only unbacked mint is
    emission; the only burns are bond forfeiture and resource purchase."""
    for e in (w.ledger.events if events is None else events):
        if e.kind not in ALLOWED_EVENT_KINDS:
            _fail(f"I3 unknown ledger event kind {e.kind}")
        if not _fin(e.amount) or e.amount < -EPS:
            _fail(f"I3 bad amount in {e.kind}: {e.amount}")


def I4_court_fee_once_and_within_bond(w, cases=None):
    by_case = w.ledger.events_by_case
    for c in _cases(w, cases):
        if c.court_fee_reimbursed > c.D + EPS:
            _fail(f"I4 {c.id}: court fee reimbursed {c.court_fee_reimbursed} > D {c.D}")
        if c.court_fee_reimbursed > EPS and c.court_fee_paid_by is None:
            _fail(f"I4 {c.id}: reimbursement without a paid fee")
        if c.nominals is not None and c.G_V + EPS < c.D:
            _fail(f"I4 {c.id}: bond {c.G_V} < court fee {c.D} (§7.2)")
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
            if any(w.reviews[r].status == "open" for r in c.reviews):
                _fail(f"I5 {c.id} vested with an open review")


def I6_commit_before_audit(w, cases=None):
    for c in _cases(w, cases):
        for rid in c.reviews:
            r = w.reviews[rid]
            if r.role == "audit" and (c.t_verdict is None or r.t_assign < c.t_verdict):
                _fail(f"I6 {c.id}: audit assigned at {r.t_assign} before the verdict at {c.t_verdict}")


def I7_child_milestone_before_parent_submit(w, cases=None):
    """A parent submits only after every nested request reached its milestone (§9.1): an
    initial verdict, or a terminal state — the same definition the submit guard uses."""
    for c in _cases(w, cases):
        if c.t_submit is None:
            continue
        for ch in c.children:
            child = w.cases[ch]
            if child.t_post > c.t_submit:
                continue                              # posted after this submission (a resubmission)
            if child.t_verdict is not None and child.t_verdict <= c.t_submit:
                continue
            if child.state in ("WITHDRAWN", "CANCELLED", "FINAL_N") and child.t_verdict is None:
                continue
            _fail(f"I7 {c.id} submitted at {c.t_submit} before nested {ch} reached its milestone")


def I8_positions_bound(w, cases=None):
    for c in _cases(w, cases):
        if w.positions(c.id) > w.p.V_max:
            _fail(f"I8 {c.id} holds {w.positions(c.id)} review positions > V_max")


def I9_reserve(w):
    if not w.enforce_reserve:
        return
    n = sum(1 for a in w.actors.values() if a.on_duty)
    if n < w.p.X:
        _fail(f"I9 reserve {n} < X={w.p.X}")


def I10_no_post_vesting_adjudication_moves_money(w, cases=None):
    """After vesting, no adjudication moves money on account of the case (§6). Obligations
    established before vesting — deferred reimbursements, Ω claims — may still be paid."""
    by_case = w.ledger.events_by_case
    for c in _cases(w, cases):
        if c.t_vest is None:
            continue
        for e in by_case.get(c.id, ()):
            if e.t > c.t_vest and "deferred" not in e.note and "Ω claim" not in e.note:
                _fail(f"I10 {c.id}: {e.kind} {e.amount} at t={e.t} after vesting at {c.t_vest}")
        if c.post_vesting_funds_moved > EPS:
            _fail(f"I10 {c.id}: override moved funds after vesting")


def I11_exclusive_failure_indicators(w, cases=None):
    for c in _cases(w, cases):
        if c.I_N and c.I_pool:
            _fail(f"I11 {c.id}: I_N and I_pool both set")


def I12_frozen_nominals(w, cases=None):
    """Nominals are fixed at the case's first lock (§4.5) and G at award; neither changes after."""
    for c in _cases(w, cases):
        if c.nominals is not None and (c.D, c.K, c.G_V, c.phi) != c.nominals:
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
        if c.is_nested():
            if c.grade != "procedural":
                _fail(f"I13 nested {c.id} graded {c.grade}")
            continue
        matching = [a for a in c.assessments if a[2] == c.outcome and a[3] in ("accept", "dispute", "override")]
        explicit = bool(matching)
        audited = any(w.reviews[r].role == "audit" and w.reviews[r].status != "withdrawn" for r in c.reviews)
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
    for r in _reviews(w, reviews):
        if r.status == "open":
            if r.reviewer in open_by:
                _fail(f"I14 {r.reviewer} holds two open reviews")
            open_by[r.reviewer] = r.id
    seen = {}
    for a in w.actors.values():
        if a.committed:
            if a.committed in seen:
                _fail(f"I14 case {a.committed} committed to two actors")
            seen[a.committed] = a.id
            st = w.cases[a.committed].state
            if st not in ("COMMITTED", "SUBMITTED", "AWAITING_RESPONSE", "RESUBMITTING"):
                _fail(f"I14 {a.id} committed to {a.committed} in state {st}")
            if a.id in open_by:
                _fail(f"I14 {a.id} is committed and holds an open review")
        if a.open_review and a.open_review not in w.reviews:
            _fail(f"I14 {a.id} open_review points nowhere")
        if a.open_review and w.reviews[a.open_review].status not in ("open", "done"):
            _fail(f"I14 {a.id} attached to a review that is {w.reviews[a.open_review].status}")


def I15_locks_reconcile(w, cases=None, reviews=None):
    """Every wallet's L equals the sum of its lock records, and every live obligation in the
    engine has a lock record of exactly its size: guarantees, bonds, nested ceilings,
    rejection bonds. No record exists for an obligation that has ended."""
    L = w.ledger
    for wid, wl in L.wallets.items():
        recs = sum(L.locks.get(wid, {}).values())
        if abs(recs - wl.L) > EPS:
            _fail(f"I15 {wid}: L={wl.L} but lock records sum to {recs}")
    expected = {}
    for c in _cases(w, cases):
        if c.actor and c.state in ("COMMITTED", "SUBMITTED", "AWAITING_RESPONSE", "RESUBMITTING", "PENDING"):
            expected[(c.actor, f"G:{c.id}")] = c.G
        if c.is_nested() and c.state == "AVAILABLE":
            expected[(c.requester, f"beta:{c.id}")] = c.beta
        if c.is_nested() and c.rejection_bond > EPS:
            expected[(c.requester, f"rej:{c.id}")] = c.rejection_bond
    for r in _reviews(w, reviews):
        if r.status in ("open", "done"):
            expected[(r.reviewer, f"bond:{r.id}")] = r.bond
    actual = {(wid, key): amt for wid, d in L.locks.items() for key, amt in d.items() if amt > EPS}
    for k, amt in expected.items():
        if abs(actual.get(k, 0.0) - amt) > EPS:
            _fail(f"I15 obligation {k} expects lock {amt}, record holds {actual.get(k, 0.0)}")
    for k in actual:
        if k not in expected:
            _fail(f"I15 lock record {k} has no live obligation")


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
    History is the record; the copies are checked against it, never the other way round."""
    if not w.history.verify():
        _fail("I16 history chain does not verify")
    committed_ledger = [i for i, e in enumerate(w.history.entries) if e["kind"] == "ledger"]
    if len(w.ledger.events) != len(committed_ledger):
        _fail(f"I16 ledger copy holds {len(w.ledger.events)} events; the record holds {len(committed_ledger)}")
    for e, hseq in zip(w.ledger.events, committed_ledger):
        if e.hseq != hseq or not w.history.matches(hseq, "ledger", e.payload()):
            _fail(f"I16 ledger event #{e.seq} ({e.kind}) differs from its committed entry")
    committed_case: dict[str, list[int]] = {}
    for i, e in enumerate(w.history.entries):
        if e["kind"] == "case":
            committed_case.setdefault(e["payload"]["case"], []).append(i)
    for c in w.cases.values():
        _check_case_log(w, c, committed_case.get(c.id, []))


def I16_tick(w, cases, new_events, hist_from: int):
    """The per-tick form of I16: the chain is verified from where it was last verified; the
    ledger events appended since then are checked against their committed entries, one copy
    per committed ledger entry, in order; the logs of the cases in scope are checked whole
    against the positions the engine committed them at."""
    if not w.history.verify_new():
        _fail("I16 history chain does not verify")
    committed_ledger = [i for i in range(hist_from, len(w.history.entries))
                        if w.history.entries[i]["kind"] == "ledger"]
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
    for r in _reviews(w, reviews):
        if r.deferred < -EPS or r.reimbursed_pending < -EPS or r.reimbursed < -EPS:
            _fail(f"I17 review {r.id} has a negative reimbursement field")
        if r.reimbursed + r.reimbursed_pending + r.deferred > min(r.cost, w.cases[r.case].K) + EPS:
            _fail(f"I17 review {r.id} reimbursed beyond its capped cost")
        if r.reimbursed_pending > EPS:
            pending[r.id] = r.reimbursed_pending
    claimed = {}
    for cl in w.omega_claims:
        if cl.amount <= EPS or cl.review not in w.reviews:
            _fail(f"I17 malformed Ω claim {cl!r}")
        if w.reviews[cl.review].reviewer != cl.reviewer:
            _fail(f"I17 Ω claim {cl!r} names the wrong reviewer")
        claimed[cl.review] = claimed.get(cl.review, 0.0) + cl.amount
    for rid in set(pending) | set(claimed):
        if abs(pending.get(rid, 0.0) - claimed.get(rid, 0.0)) > EPS:
            _fail(f"I17 review {rid}: pending {pending.get(rid, 0.0)} != claims {claimed.get(rid, 0.0)}")
    for c in _cases(w, cases):
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
            r = w.reviews[rid]
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


def check_all(world):
    """The full audit: every predicate over everything, the record re-hashed from genesis."""
    for chk in CHECKS:
        chk(world)


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

    w._events_checked = len(w.ledger.events)
    w._prune_working_set()

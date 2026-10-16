"""Spec §17 invariants, checked after every tick. Each is a function of the whole world.

A failing invariant is a bug in the engine or a contradiction in the spec; it is never a
property of a strategy. Each check states what it actually establishes.
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


def I1_conservation(w):
    """Every credit is in a wallet, a case pool, or Ω; their sum is M; and M equals the
    money minted minus the money burned according to the event log."""
    L = w.ledger
    tot = L.total_credits()
    if not _fin(tot) or not _fin(L.M) or abs(tot - L.M) > EPS:
        _fail(f"I1 conservation: wallets+pools={tot} != M={L.M}")
    recon = L.reconstruct_M()
    if abs(recon - L.M) > EPS:
        _fail(f"I1 reconstruction: mints-burns={recon} != M={L.M}")


def I2_no_negative_or_nonfinite_balances(w):
    for wl in w.ledger.wallets.values():
        if not _fin(wl.U) or not _fin(wl.L) or wl.U < -EPS or wl.L < -EPS:
            _fail(f"I2 bad balance in {wl.id}: U={wl.U} L={wl.L}")
    for cid, p in w.ledger.pools.items():
        for name, val in (("escrow", p.escrow), ("deposit", p.deposit), ("minted", p.minted)):
            if not _fin(val) or val < -EPS:
                _fail(f"I2 bad {name} pool for {cid}: {val}")
    if not _fin(w.ledger.Res) or w.ledger.Res < -EPS:
        _fail("I2 bad reserve")


def I3_mints_and_burns(w):
    """Only known event kinds, with finite non-negative amounts; the only unbacked mint is
    emission; the only burns are bond forfeiture and resource purchase."""
    for e in w.ledger.events:
        if e.kind not in ALLOWED_EVENT_KINDS:
            _fail(f"I3 unknown ledger event kind {e.kind}")
        if not _fin(e.amount) or e.amount < -EPS:
            _fail(f"I3 bad amount in {e.kind}: {e.amount}")


def I4_court_fee_once_and_within_bond(w):
    for c in w.cases.values():
        if c.court_fee_reimbursed > c.D + EPS:
            _fail(f"I4 {c.id}: court fee reimbursed {c.court_fee_reimbursed} > D {c.D}")
        if c.court_fee_reimbursed > EPS and c.court_fee_paid_by is None:
            _fail(f"I4 {c.id}: reimbursement without a paid fee")
        if c.nominals is not None and c.G_V + EPS < c.D:
            _fail(f"I4 {c.id}: bond {c.G_V} < court fee {c.D} (§7.2)")
        n_reimb = sum(1 for e in w.ledger.events if e.case == c.id and e.kind == "forfeit_to" and "court fee" in e.note)
        if n_reimb > 1:
            _fail(f"I4 {c.id}: court fee reimbursed {n_reimb} times")


def I5_no_vest_with_open_items(w):
    for c in w.cases.values():
        if c.state == "VESTED":
            if c.open_items != 0:
                _fail(f"I5 {c.id} vested with {c.open_items} open items")
            if c.challenge and not c.challenge["resolved"]:
                _fail(f"I5 {c.id} vested with an unresolved challenge")
            if c.t_vest is not None and c.window_end is not None and c.t_vest < c.window_end:
                _fail(f"I5 {c.id} vested before its window closed")
            if any(w.reviews[r].status == "open" for r in c.reviews):
                _fail(f"I5 {c.id} vested with an open review")


def I6_commit_before_audit(w):
    for c in w.cases.values():
        for rid in c.reviews:
            r = w.reviews[rid]
            if r.role == "audit" and (c.t_verdict is None or r.t_assign < c.t_verdict):
                _fail(f"I6 {c.id}: audit assigned at {r.t_assign} before the verdict at {c.t_verdict}")


def I7_child_milestone_before_parent_submit(w):
    """A parent submits only after every nested request reached its milestone (§9.1): an
    initial verdict, or a terminal state — the same definition the submit guard uses."""
    for c in w.cases.values():
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


def I8_positions_bound(w):
    for c in w.cases.values():
        if w.positions(c.id) > w.p.V_max:
            _fail(f"I8 {c.id} holds {w.positions(c.id)} review positions > V_max")


def I9_reserve(w):
    if not w.enforce_reserve:
        return
    n = sum(1 for a in w.actors.values() if a.on_duty)
    if n < w.p.X:
        _fail(f"I9 reserve {n} < X={w.p.X}")


def I10_no_post_vesting_adjudication_moves_money(w):
    """After vesting, no adjudication moves money on account of the case (§6). Obligations
    established before vesting — deferred reimbursements, Ω claims — may still be paid."""
    for c in w.cases.values():
        if c.t_vest is None:
            continue
        for e in w.ledger.events:
            if e.case == c.id and e.t > c.t_vest and "deferred" not in e.note and "Ω claim" not in e.note:
                _fail(f"I10 {c.id}: {e.kind} {e.amount} at t={e.t} after vesting at {c.t_vest}")
        if c.post_vesting_funds_moved > EPS:
            _fail(f"I10 {c.id}: override moved funds after vesting")


def I11_exclusive_failure_indicators(w):
    for c in w.cases.values():
        if c.I_N and c.I_pool:
            _fail(f"I11 {c.id}: I_N and I_pool both set")


def I12_frozen_nominals(w):
    """Nominals are fixed at the case's first lock (§4.5) and G at award; neither changes after."""
    for c in w.cases.values():
        if c.nominals is not None and (c.D, c.K, c.G_V, c.phi) != c.nominals:
            _fail(f"I12 {c.id}: nominals changed after they were frozen")
        if c.G_award is not None and c.G != c.G_award:
            _fail(f"I12 {c.id}: G changed after award")
        if c.is_nested() and c.nominals is not None and c.state == "AVAILABLE":
            if abs(c.rejection_bond - c.G_V) > EPS:
                _fail(f"I12 {c.id}: rejection bond {c.rejection_bond} != frozen G_V {c.G_V}")


def I13_grade_provenance(w):
    """Every settled case carries exactly one grade, and the grade is justified by the record:
    human/delegate-explicit needs a matching explicit root judgment; procedural needs a
    challenge, an audit, or a nested case; protocol-default needs none of these."""
    for c in w.cases.values():
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


def I14_one_active_assignment(w):
    """One active assignment per actor: at most one ordinary commitment, at most one open
    review, and never both (§2.2)."""
    open_by = {}
    for r in w.reviews.values():
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


def I15_locks_reconcile(w):
    """Every wallet's L equals the sum of its lock records, and every live obligation in the
    engine has a lock record of exactly its size: guarantees, bonds, nested ceilings,
    rejection bonds. No record exists for an obligation that has ended."""
    L = w.ledger
    for wid, wl in L.wallets.items():
        recs = sum(L.locks.get(wid, {}).values())
        if abs(recs - wl.L) > EPS:
            _fail(f"I15 {wid}: L={wl.L} but lock records sum to {recs}")
    expected = {}
    for c in w.cases.values():
        if c.actor and c.state in ("COMMITTED", "SUBMITTED", "AWAITING_RESPONSE", "RESUBMITTING", "PENDING"):
            expected[(c.actor, f"G:{c.id}")] = c.G
        if c.is_nested() and c.state == "AVAILABLE":
            expected[(c.requester, f"beta:{c.id}")] = c.beta
        if c.is_nested() and c.rejection_bond > EPS:
            expected[(c.requester, f"rej:{c.id}")] = c.rejection_bond
    for r in w.reviews.values():
        if r.status in ("open", "done"):
            expected[(r.reviewer, f"bond:{r.id}")] = r.bond
    actual = {(wid, key): amt for wid, d in L.locks.items() for key, amt in d.items() if amt > EPS}
    for k, amt in expected.items():
        if abs(actual.get(k, 0.0) - amt) > EPS:
            _fail(f"I15 obligation {k} expects lock {amt}, record holds {actual.get(k, 0.0)}")
    for k in actual:
        if k not in expected:
            _fail(f"I15 lock record {k} has no live obligation")


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
        want = committed_case.get(c.id, [])
        if len(c.log) != len(want):
            _fail(f"I16 case log of {c.id} holds {len(c.log)} entries; the record holds {len(want)}")
        for entry, hseq in zip(c.log, want):
            if len(entry) != 3 or entry[2] != hseq or \
                    not w.history.matches(hseq, "case", {"t": entry[0], "case": c.id, "msg": entry[1]}):
                _fail(f"I16 case log of {c.id} differs from its committed entry: {entry!r}")


def I17_debts_and_claims_reconcile(w):
    """Deferred and pending reimbursements are non-negative; every Ω claim names a review whose
    pending field covers it; the pending fields sum to the claims; no ended nested obligation
    still carries a rejection bond."""
    pending = {}
    for r in w.reviews.values():
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
    for c in w.cases.values():
        if c.is_nested() and c.state in ("VESTED", "FINAL_N", "CANCELLED", "WITHDRAWN") and c.rejection_bond > EPS:
            _fail(f"I17 nested {c.id} is {c.state} but still carries a rejection bond")


def I18_no_audit_outlives_a_ruling(w):
    """Once a human has ruled on a case, no audit of it is open or assigned afterwards: an
    audit open at the ruling was voided by it, and none is admitted after it."""
    for c in w.cases.values():
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
    for chk in CHECKS:
        chk(world)

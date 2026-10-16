"""The loop itself: cases, reviews, challenges, delegation, settlement, rotation, and the
tick order (baseline v1.0.1; section numbers in comments refer to the working-spec versions they were written against).

Decisions are injected. The engine validates each action against the case state machine
and the current tick, applies its financial effects through the ledger atomically (an
action either completes under its rules or changes nothing), and advances time with the
§2.2 ordering:

    step 0  participant actions (applied as they are called, at the current tick)
    step 1  challenges filed this tick are admitted            (applied at call time)
    step 2  deadlines: delivery, response, resubmission, review, nested wait
    step 3  vesting checks and review settlement (one emission batch per tick)
    step 4  Ω services its outstanding claims
    step 5  rotation handovers
    step 6  assignment/awards   (driven by the caller)

Nothing here chooses a bid, a verdict, or a ruling.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
import math
import os

from .params import Params
from .ledger import Ledger, LedgerError, History, amount
from .record import Archive, PagedDict


class RuleError(Exception):
    """An action the rules do not permit in the current state."""


F, N, P, BOT = "F", "N", "P", "⊥"
VERDICTS = {F, N, P, BOT}
UPHELD, REJECTED = "upheld", "rejected"          # disposition of a ⊥ objection (§8.1)

# Label grades (§15.3)
HUMAN, DELEGATE, DEFAULT, PROCEDURAL = "human-explicit", "delegate-explicit", "protocol-default", "procedural"

ROLE_W = {"initial": "w_ordinary", "appeal": "w_appeal", "audit": "w_audit"}


class Claim(tuple):
    """An outstanding Ω claim: compares and prints as (reviewer, amount), and carries the
    review whose cost it is, so servicing credits the right obligation (§4.3)."""

    def __new__(cls, reviewer: str, amt: float, review: str):
        obj = super().__new__(cls, (reviewer, amt))
        obj.review = review
        return obj

    @property
    def reviewer(self):
        return self[0]

    @property
    def amount(self):
        return self[1]


def _int_ticks(x, name) -> int:
    if isinstance(x, bool) or not isinstance(x, (int,)) or x < 1:
        raise RuleError(f"{name} must be a positive integer number of ticks, got {x!r}")
    return x


@dataclass
class Actor:
    id: str
    on_duty: bool = False
    committed: Optional[str] = None
    open_review: Optional[str] = None       # one active assignment (§2.2)
    outcomes: list = field(default_factory=list)   # (t, stood) over the trailing rho window
    vests: list = field(default_factory=list)      # ticks of vested reviews, for kappa
    p_audit: float = 0.5
    streak: int = 0
    duty_since: Optional[int] = None
    duty_reviews: int = 0
    volunteer: bool = False
    _world: object = None

    @property
    def s(self) -> int:
        return sum(1 for _, ok in self.outcomes if ok)

    @property
    def o(self) -> int:
        return sum(1 for _, ok in self.outcomes if not ok)

    @property
    def rho(self) -> float:
        return (self.s + 1) / (self.s + self.o + 2)

    @property
    def kappa(self) -> int:
        w = self._world
        horizon = w.t - w.p.kappa_window
        return sum(1 for tv in self.vests if tv > horizon)


@dataclass
class ReviewView:
    """What a reviewer is allowed to see (§14): the submission and the assignment's terms,
    and the answers it may give. A fulfillment question is answered F or N; it may also be
    answered P or ⊥ exactly when `responses_available` says so — the first review of an
    unrevised submission. The view does not say whether a fulfillment question is an initial
    review or an audit; it says what may be answered, so identical views admit identical
    answers (§8.3). An appeal or a dispute states the question it asks (§8.1). Other verdicts
    and identities stay hidden."""
    review_id: str
    case_id: str
    actor: str
    t_submit: Optional[int]
    deadline: int
    bond: float
    cap: float
    resumed: bool
    is_nested: bool
    question: str = "fulfillment"              # fulfillment | appeal | dispute
    appealed_assessment: Optional[str] = None  # N, ⊥ (appeal) or F (dispute)
    objection_text: Optional[str] = None       # the challenger's explanation d_q
    responses_available: bool = False          # may this review answer P or ⊥? (§8.3)


@dataclass
class Review:
    id: str
    case: str
    reviewer: str
    role: str                     # initial | appeal | audit
    t_assign: int
    deadline: int
    bond: float
    cost: float = 0.0             # credits spent
    reimbursed: float = 0.0
    deferred: float = 0.0
    verdict: Optional[str] = None
    objection: Optional[str] = None   # ⊥ appeals: upheld | rejected
    t_done: Optional[int] = None
    status: str = "open"          # open | done | withdrawn | overturned | vested
    fee: float = 0.0
    is_audit_as_appeal: bool = False
    resumed: bool = False
    contradicted_by_override: bool = False
    reimbursed_pending: float = 0.0   # an Ω claim outstanding for this review's costs


@dataclass
class Case:
    id: str
    root: str
    requester: str
    is_root: bool
    beta: float
    t_post: int
    parent: Optional[str] = None
    actor: Optional[str] = None
    B: float = 0.0
    tau: int = 0
    G: float = 0.0
    t_award: Optional[int] = None
    deadline: Optional[int] = None
    # nominals frozen at the case's first lock (§4.5): award for root, posting for nested
    D: float = 0.0
    K: float = 0.0
    G_V: float = 0.0
    phi: float = 0.0
    omega: float = 0.0
    nominals: Optional[tuple] = None   # (D, K, G_V, phi) at the first lock
    G_award: Optional[float] = None    # G at award
    # state
    state: str = "AVAILABLE"
    t_submit: Optional[int] = None
    t_verdict: Optional[int] = None
    verdict: Optional[str] = None
    outcome: Optional[str] = None
    window_end: Optional[int] = None
    response_deadline: Optional[int] = None
    resubmit_deadline: Optional[int] = None
    revisions_used: int = 0
    resubmitted: bool = False      # the submission has been revised or evidenced once: F or N only from here
    open_items: int = 0
    challenge_round_used: bool = False
    challenge: Optional[dict] = None
    audit_vacated: bool = False
    reviews: list = field(default_factory=list)
    excluded: set = field(default_factory=set)
    # money
    reimb_total: float = 0.0
    omega_advance: float = 0.0
    court_fee_paid_by: Optional[str] = None
    court_fee_reimbursed: float = 0.0
    actor_cost: float = 0.0       # credits: resource spend + nested payments + kill fees
    rejection_bond: float = 0.0
    needs_review_settlement: bool = False
    # outcome record
    grade: Optional[str] = None
    assessments: list = field(default_factory=list)
    t_vest: Optional[int] = None
    final: bool = False
    I_N: bool = False
    I_pool: bool = False
    corrective_obligation: Optional[str] = None
    post_vesting_funds_moved: float = 0.0
    children: list = field(default_factory=list)
    log: list = field(default_factory=list)

    def is_nested(self) -> bool:
        return not self.is_root

    def outcome_or_verdict(self):
        return self.outcome or self.verdict


class World:
    def __init__(self, params: Params, actors: list[str], humans: dict[str, float] | None = None,
                 on_duty: list[str] | None = None, delegates: list[str] | None = None,
                 enforce_reserve: bool = True):
        self.p = params
        self.t = 0
        if len(set(actors)) != len(actors):
            raise RuleError("duplicate actor ids")
        n = len(actors)
        need = n * params.float_per_actor + params.Omega0
        if need > params.M0:
            raise RuleError(f"initialization invalid: {n} actors need {need} > M0={params.M0} (§19)")
        # The record. In memory by default. With `record_dir` set, the History and the event
        # copy are written through to files there, and settled cases and reviews are paged out
        # to archives; RAM then holds the working set (sim/record.py). Same behaviour either way.
        self._paged = bool(params.record_dir)
        if self._paged:
            rd = params.record_dir
            os.makedirs(rd, exist_ok=True)
            self.history = History(path=os.path.join(rd, "history.jsonl"))
            self.ledger = Ledger(params.Res0, params.v0, history=self.history,
                                 events_path=os.path.join(rd, "events.jsonl"))
        else:
            self.history = History()
            self.ledger = Ledger(params.Res0, params.v0, history=self.history)
        self.actors: dict[str, Actor] = {}
        for a in actors:
            self.actors[a] = Actor(a, p_audit=params.p_start, _world=self)
            self.ledger.transfer("SPONSOR", a, params.float_per_actor, note="cold-start float")
        self.ledger.transfer("SPONSOR", Ledger.OMEGA, params.Omega0, note="Ω float")
        # root requesters: humans, and delegates (systems holding a human's budget). A delegate
        # may post, pay, accept and dispute; it holds no ruling authority (§15.2).
        self.requesters: set[str] = set()
        for h, credits in (humans or {}).items():
            self.ledger.wallet(h)
            self.ledger.transfer("SPONSOR", h, credits, note="requester budget")
            self.requesters.add(h)
        self.delegates: set[str] = set(delegates or [])
        if not self.delegates <= self.requesters:
            raise RuleError("a delegate must be a funded requester")
        self.humans: set[str] = self.requesters - self.delegates
        if on_duty is None:
            on_duty = sorted(actors)[: params.X]            # §19: lowest ids
        for a in on_duty:
            self.actors[a].on_duty = True
            self.actors[a].duty_since = 0
        self.enforce_reserve = enforce_reserve
        self._case_entries: dict[str, list[int]] = {}   # case id -> positions of its History entries
        if self._paged:
            # a paged-out case takes its History positions with it and brings them back when it
            # becomes resident again; a transient copy for an audit leaves them alone
            def pack_case(c):
                return c, self._case_entries.pop(c.id, [])

            def unpack_case(blob, resident):
                c, entries = blob
                if resident:
                    self._case_entries[c.id] = entries
                return c
            self.cases = PagedDict(Archive(os.path.join(rd, "cases.pickle")), "q", pack_case, unpack_case)
            self.reviews = PagedDict(Archive(os.path.join(rd, "reviews.pickle")), "r")
        else:
            self.cases: dict[str, Case] = {}
            self.reviews: dict[str, Review] = {}
        self.omega_claims: list[Claim] = []    # (reviewer, amount) FIFO, each carrying its review
        self._n_case = 0
        self._n_review = 0
        # The working set. `cases` and `reviews` hold everything ever created; these hold what
        # can still change: a case until it is settled with every review of it settled and no
        # claim outstanding, a review until it is withdrawn, overturned or vested with nothing
        # pending. The tick loop and the per-tick invariant check read these; a settled case
        # that is touched again (a post-settlement correction, a serviced Ω claim) is marked
        # dirty and re-checked once. Insertion order is creation order, as in `cases`.
        self._live_cases: dict[str, Case] = {}
        self._live_reviews: dict[str, Review] = {}
        self._dirty_cases: set[str] = set()
        self._court_fee_reimb: dict[str, int] = {}      # case id -> court-fee reimbursements recorded
        self._violations: list[str] = []                # I4/I10 facts established as events were recorded
        self._events_checked = 0                        # ledger events already checked by the tick check
        self.ledger.on_event = self._on_ledger_event
        for e in self.ledger.events:                    # the floats and budgets paid in above
            self._on_ledger_event(e)

    # ------------------------------------------------------------------ util
    def _case(self, cid) -> Case:
        if cid not in self.cases:
            raise RuleError(f"unknown case {cid}")
        return self.cases[cid]

    def _review(self, rid) -> Review:
        if rid not in self.reviews:
            raise RuleError(f"unknown review {rid}")
        return self.reviews[rid]

    def _actor(self, aid) -> Actor:
        if aid not in self.actors:
            raise RuleError(f"unknown actor {aid}")
        return self.actors[aid]

    def _log(self, case: Case, msg: str):
        """Commit a case event to the authoritative History; the case log keeps a copy with
        its commitment position, which I16 checks against the chain."""
        self.history.append("case", {"t": self.t, "case": case.id, "msg": msg})
        hseq = len(self.history.entries) - 1
        case.log.append((self.t, msg, hseq))
        self._case_entries.setdefault(case.id, []).append(hseq)
        self._dirty_cases.add(case.id)

    def _on_ledger_event(self, e):
        """Every ledger movement attributed to a case marks that case for the tick's check, and
        establishes the two facts I4 and I10 would otherwise have to rescan the record for: how
        many times a case's court fee was reimbursed, and whether money moved on account of a
        vested case after its vesting (deferred reimbursements and Ω claims excepted, §6)."""
        cid = e.case
        if cid is None:
            return
        self._dirty_cases.add(cid)
        if e.kind == "forfeit_to" and "court fee" in e.note:
            n = self._court_fee_reimb.get(cid, 0) + 1
            self._court_fee_reimb[cid] = n
            if n > 1:
                self._violations.append(f"I4 {cid}: court fee reimbursed {n} times")
        c = self.cases.get(cid)
        if c is not None and c.t_vest is not None and e.t > c.t_vest \
                and "deferred" not in e.note and "Ω claim" not in e.note:
            self._violations.append(f"I10 {cid}: {e.kind} {e.amount} at t={e.t} after vesting at {c.t_vest}")

    def _touch(self, case: Case):
        self._dirty_cases.add(case.id)

    def _w(self, role: str) -> float:
        return getattr(self.p, ROLE_W[role])

    def wallet(self, wid):
        return self.ledger.wallet(wid)

    def W(self, wid) -> float:
        return self.ledger.wallet(wid).W

    def _record_outcome(self, aid: str, stood: bool):
        a = self.actors[aid]
        a.outcomes.append((self.t, stood))
        if len(a.outcomes) > self.p.rho_window:
            del a.outcomes[: len(a.outcomes) - self.p.rho_window]

    def _freeze(self, c: Case):
        c.nominals = (c.D, c.K, c.G_V, c.phi)

    # --------------------------------------------------------------- requests
    def post_root(self, requester: str, beta: float) -> str:
        beta = amount(beta, "beta")
        if requester not in self.requesters:
            raise RuleError("a root requester must be a human or a delegate (§2.1)")
        self._n_case += 1
        cid = f"q{self._n_case}"
        c = Case(cid, root=cid, requester=requester, is_root=True, beta=beta, t_post=self.t)
        self.cases[cid] = c
        self._live_cases[cid] = c
        self._log(c, f"posted root beta={beta}")
        return cid

    def post_nested(self, parent_id: str, beta: float) -> str:
        beta = amount(beta, "beta")
        parent = self._case(parent_id)
        if parent.state != "COMMITTED":
            raise RuleError("only a committed actor may post a nested request (§9.1)")
        A = parent.actor
        idx = self.ledger.index()                 # §4.5: a nested case is denominated at posting
        D, K, GV = self.p.D * idx, self.p.K * idx, self.p.G_V * idx
        if self.ledger.wallet(A).U + 1e-9 < beta + GV:
            raise LedgerError(f"{A} cannot lock beta' + G_V = {beta + GV}")
        self._n_case += 1
        cid = f"q{self._n_case}"
        c = Case(cid, root=parent.root, requester=A, is_root=False, beta=beta, t_post=self.t, parent=parent_id)
        c.D, c.K, c.G_V, c.phi = D, K, GV, 0.0
        c.rejection_bond = GV
        self.cases[cid] = c
        self._live_cases[cid] = c
        self.ledger.lock(A, beta, key=f"beta:{cid}", case=cid, note="nested price ceiling")
        self.ledger.lock(A, GV, key=f"rej:{cid}", case=cid, note="rejection bond")
        self._freeze(c)
        parent.children.append(cid)
        self._log(c, f"posted nested under {parent_id} beta={beta}; denominated at posting (G_V={GV})")
        return cid

    def withdraw_unawarded(self, cid: str):
        """§9.3: before award, the requester-actor withdraws freely."""
        c = self._case(cid)
        if c.state != "AVAILABLE":
            raise RuleError("withdraw_unawarded: case already awarded")
        if c.is_nested():
            A = c.requester
            self.ledger.release(A, self.ledger.lock_record(A, f"beta:{cid}"), key=f"beta:{cid}", case=cid)
            self.ledger.release(A, self.ledger.lock_record(A, f"rej:{cid}"), key=f"rej:{cid}", case=cid)
            c.rejection_bond = 0.0
        c.state, c.final = "WITHDRAWN", True
        self._log(c, "withdrawn before award")

    # ----------------------------------------------------------------- award
    def award(self, cid: str, actor_id: str, B: float, tau: int):
        B = amount(B, "B")
        tau = _int_ticks(tau, "tau")
        c = self._case(cid)
        a = self._actor(actor_id)
        if c.state != "AVAILABLE":
            raise RuleError(f"award: case {cid} is {c.state}")
        if B > c.beta + 1e-9:
            raise RuleError(f"award: bid {B} exceeds beta {c.beta} (§5.1)")
        if a.committed is not None or a.open_review is not None:
            raise RuleError(f"award: {actor_id} already holds an assignment")
        if a.on_duty:
            raise RuleError(f"award: {actor_id} is on verification duty")
        if actor_id == c.requester:
            raise RuleError("an actor cannot be awarded its own request")
        G = max(1.0, math.ceil(self.p.G_frac * B))
        omega = self.p.omega_rate * B
        # --- pre-checks: no mutation until every leg is known to be fundable (atomicity)
        if self.ledger.wallet(actor_id).U + 1e-9 < G:
            raise LedgerError(f"award: {actor_id} cannot fund the guarantee {G}")
        if c.is_root:
            idx = self.ledger.index()
            D, K, GV, phi = self.p.D * idx, self.p.K * idx, self.p.G_V * idx, self.p.phi_root * idx
            need = B + phi + omega
            if self.ledger.wallet(c.requester).U + 1e-9 < need:
                raise LedgerError(f"award: requester {c.requester} cannot fund {need} (B + φ + ω)")
        else:
            D, K, GV, phi = c.D, c.K, c.G_V, 0.0     # frozen at posting
            if self.ledger.wallet(c.requester).U + 1e-9 < omega:
                raise LedgerError(f"award: requester {c.requester} cannot fund ω {omega}")
        # --- mutate
        c.D, c.K, c.G_V, c.phi, c.omega, c.G = D, K, GV, phi, omega, G
        c.G_award = G
        c.B, c.tau, c.actor = B, tau, actor_id
        c.t_award, c.deadline = self.t, self.t + tau
        self.ledger.lock(actor_id, G, key=f"G:{cid}", case=cid, note="guarantee")
        if c.is_root:
            self.ledger.fund_escrow(c.requester, cid, B, note="delivery price")
            self.ledger.fund_deposit(c.requester, cid, phi, note="verification deposit")
            if omega > 0:
                self.ledger.transfer(c.requester, Ledger.OMEGA, omega, case=cid, note="service fee")
                self._service_omega_claims()
            self._freeze(c)
        else:
            A = c.requester
            self.ledger.fund_escrow(A, cid, B, from_locked=f"beta:{cid}", note="nested escrow")
            unspent = self.ledger.lock_record(A, f"beta:{cid}")
            if unspent > 1e-12:
                self.ledger.release(A, unspent, key=f"beta:{cid}", case=cid, note="unspent beta'")
            if omega > 0:
                self.ledger.transfer(A, Ledger.OMEGA, omega, case=cid, note="service fee (nested)")
                self._service_omega_claims()
        c.state = "COMMITTED"
        a.committed = cid
        self._log(c, f"awarded to {actor_id} B={B} tau={tau} G={G}; deadline {c.deadline}")

    EXECUTING = ("COMMITTED", "SUBMITTED", "AWAITING_RESPONSE", "RESUBMITTING")

    def spend(self, actor_id: str, real_cost: float, cid: Optional[str] = None) -> float:
        """Resource purchase by an actor. Attributed to a case only if the actor is that case's
        committed actor and the case is still executing (§4.6): nobody else's spending is the
        contractor's cost, and a settled case takes no further cost. Validated before purchase."""
        real_cost = amount(real_cost, "real_cost")
        self._actor(actor_id)
        c = self._case(cid) if cid else None
        if c is not None:
            if c.actor != actor_id:
                raise RuleError(f"spend: {actor_id} is not the committed actor of {cid}; its spending is its own")
            if c.state not in self.EXECUTING:
                raise RuleError(f"spend: case {cid} is {c.state}; execution cost is incurred while executing")
        credits = self.ledger.purchase(actor_id, real_cost, case=cid, note="execution")
        if c is not None:
            c.actor_cost += credits
        return credits

    # ---------------------------------------------------------------- submit
    def submit(self, cid: str):
        c = self._case(cid)
        if c.state != "COMMITTED":
            raise RuleError(f"submit: case {cid} is {c.state}")
        if self.t > c.deadline:
            raise RuleError("submit: past the delivery deadline (deadline is inclusive)")
        for ch in c.children:
            child = self.cases[ch]
            if not self._child_milestone_reached(child):
                raise RuleError(f"submit: nested {ch} has not reached its initial verdict (§9.1)")
        c.state, c.t_submit = "SUBMITTED", self.t
        self._log(c, "submitted")

    @staticmethod
    def _child_milestone_reached(child: "Case") -> bool:
        """§9.1: a nested request reaches its milestone at its initial verdict, or at any
        terminal state — withdrawn, cancelled, or final N without a submission (a missed
        delivery). The parent carries that failure as its own risk."""
        return child.t_verdict is not None or child.state in ("WITHDRAWN", "CANCELLED", "FINAL_N")

    def resubmit(self, cid: str):
        """After choosing to revise (P) or to supply evidence (⊥): the same reviewer resumes."""
        c = self._case(cid)
        if c.state != "RESUBMITTING":
            raise RuleError(f"resubmit: case {cid} is {c.state}")
        if self.t > c.resubmit_deadline:
            raise RuleError("resubmit: window closed")
        r = self._initial_review(c)
        r.deadline += (self.t - r.t_done)        # the review clock paused while the actor acted
        r.status, r.verdict, r.objection, r.resumed = "open", None, None, True
        c.resubmitted = True                     # a property of the submission, not of who reviews it
        c.state, c.t_submit, c.resubmit_deadline = "SUBMITTED", self.t, None
        self._log(c, f"resubmitted; {r.reviewer} resumes review {r.id} (F or N only)")

    # --------------------------------------------------------------- reviews
    def _eligible(self, c: Case, reviewer: str) -> None:
        a = self._actor(reviewer)
        if not a.on_duty:
            raise RuleError(f"{reviewer} is not on verification duty")
        if reviewer in c.excluded or reviewer == c.actor or reviewer == c.requester:
            raise RuleError(f"{reviewer} is excluded from case {c.id}")
        if a.open_review is not None or a.committed is not None:
            raise RuleError(f"{reviewer} already holds an active assignment (one at a time, §2.2)")
        if self.ledger.wallet(reviewer).U + 1e-9 < c.G_V:
            raise RuleError(f"{reviewer} cannot fund the bond {c.G_V} (§7.1)")

    def _positions(self, c: Case) -> int:
        """Review positions on the current challenge path (§12). A withdrawn review vacates its
        position."""
        return sum(1 for rid in c.reviews if self.reviews[rid].status != "withdrawn")

    def _new_review(self, c: Case, reviewer: str, role: str) -> Review:
        self._eligible(c, reviewer)
        if self._positions(c) + 1 > self.p.V_max:
            raise RuleError(f"case {c.id} would exceed V_max={self.p.V_max} review positions")
        self._n_review += 1
        rid = f"r{self._n_review}"
        r = Review(rid, c.id, reviewer, role, self.t, self.t + self.p.T_review, bond=c.G_V)
        self.ledger.lock(reviewer, c.G_V, key=f"bond:{rid}", case=c.id, note=f"bond ({role})")
        self.reviews[rid] = r
        self._live_reviews[rid] = r
        c.reviews.append(rid)
        c.excluded.add(reviewer)
        self.actors[reviewer].open_review = rid
        return r

    @staticmethod
    def _responses_available(c: Case, r: Review) -> bool:
        """§8.3: P and ⊥ are responses to a submission — they send the actor back to act. They are
        available on the first review of a submission that has not yet been revised or
        evidenced, and the view states this, so identical views admit identical answers. An
        audit reviews a finished verdict after the actor's window has closed, so it is answered
        F or N; so is any appeal, dispute, or resumed review."""
        return r.role == "initial" and r.status == "open" and not r.resumed and not c.resubmitted

    def observe(self, reviewer: str, rid: str) -> ReviewView:
        """The filtered view a policy gets for a review assignment (§14, §8.1)."""
        r = self._review(rid)
        if r.reviewer != reviewer:
            raise RuleError("observe: not this reviewer's assignment")
        c = self.cases[r.case]
        view = ReviewView(r.id, c.id, c.actor, c.t_submit, r.deadline, r.bond, c.K,
                          r.resumed or c.resubmitted, c.is_nested(),
                          responses_available=self._responses_available(c, r))
        if r.role == "appeal" and c.challenge:
            view.question = "dispute" if c.challenge["kind"] == "dispute" else "appeal"
            view.appealed_assessment = c.verdict
            view.objection_text = c.challenge.get("d")
        return view

    def assign_initial(self, cid: str, reviewer: str) -> str:
        c = self._case(cid)
        if not c.is_root:
            raise RuleError("nested cases are judged by their requester-actor (§9.1)")
        if c.state != "SUBMITTED":
            raise RuleError(f"assign_initial: case {cid} is {c.state}")
        if any(self.reviews[r].role == "initial" and self.reviews[r].status in ("open", "done", "vested")
               for r in c.reviews):
            raise RuleError("initial review already assigned")
        r = self._new_review(c, reviewer, "initial")
        self._log(c, f"initial review {r.id} -> {reviewer}, deadline {r.deadline}")
        return r.id

    def assign_audit(self, cid: str, reviewer: str) -> str:
        c = self._case(cid)
        if c.state != "PENDING" or c.outcome_or_verdict() != F:
            raise RuleError("audit: only an F verdict in PENDING may be audited (§8.3)")
        if self.t > c.window_end and not c.audit_vacated:
            raise RuleError("audit: window closed")
        if c.challenge_round_used:
            raise RuleError("audit: challenge round already used")
        if any(a[3] == "override" for a in c.assessments):
            raise RuleError("audit: a human ruling has settled this case's assessment; nothing to audit (§15.2)")
        if self.t == c.t_verdict and c.outcome is not None and c.outcome != c.verdict:
            raise RuleError("audit: the assessment was superseded this tick")
        if any(self.reviews[r].role == "audit" and self.reviews[r].status != "withdrawn" for r in c.reviews):
            raise RuleError("audit: already audited")
        if c.t_verdict is None or self.t < c.t_verdict:
            raise RuleError("audit: the verdict must be committed before the audit is assigned (§14)")
        r = self._new_review(c, reviewer, "audit")
        if c.audit_vacated:
            c.audit_vacated = False                      # the vacated obligation is taken over
        else:
            c.open_items += 1
        self._log(c, f"audit {r.id} -> {reviewer} (vesting suspended)")
        return r.id

    def waive_audit(self, cid: str):
        """§7.5: the orchestrator may lift a vacated audit's suspension instead of refilling it."""
        c = self._case(cid)
        if not c.audit_vacated:
            raise RuleError("waive_audit: no vacated audit position")
        c.audit_vacated = False
        c.open_items -= 1
        self._log(c, "vacated audit position waived by the orchestrator")

    def assign_appeal(self, cid: str, reviewer: str) -> str:
        c = self._case(cid)
        if not c.challenge or c.challenge.get("resolved"):
            raise RuleError("assign_appeal: no open challenge")
        if len(c.challenge["reviews"]) >= 2:
            raise RuleError("assign_appeal: two appeal reviews already assigned")
        r = self._new_review(c, reviewer, "appeal")
        c.challenge["reviews"].append(r.id)
        self._log(c, f"appeal review {r.id} -> {reviewer}")
        return r.id

    def _reimburse(self, c: Case, r: Review):
        """§4.3 order: the root's deposit, then an Ω advance, then deferral to settlement."""
        target = min(r.cost, c.K)
        amt = target - (r.reimbursed + r.deferred)
        if amt <= 1e-12:
            return
        root = self.cases[c.root]
        pool = self.ledger.pool(root.id)
        take = min(amt, pool.deposit)
        if take > 0:
            self.ledger.pay_from_deposit(root.id, r.reviewer, take, note=f"reimburse {r.id}")
        rest = amt - take
        adv = 0.0
        if rest > 1e-12:
            adv = min(rest, self.ledger.wallet(Ledger.OMEGA).U)
            if adv > 0:
                self.ledger.transfer(Ledger.OMEGA, r.reviewer, adv, case=c.id, note=f"Ω advance {r.id}")
                c.omega_advance += adv
            rest -= adv
        r.reimbursed += take + adv
        r.deferred += rest
        c.reimb_total += amt

    def complete_review(self, rid: str, verdict: str, cost: float, objection: Optional[str] = None):
        cost = amount(cost, "cost")
        r = self._review(rid)
        c = self._case(r.case)
        if r.status != "open":
            raise RuleError(f"review {rid} is {r.status}")
        if verdict not in VERDICTS:
            raise RuleError(f"bad verdict {verdict}")
        if self.t > r.deadline:
            raise RuleError("review past its deadline (it should have been withdrawn)")
        if verdict in (P, BOT) and not self._responses_available(c, r):
            raise RuleError("P and ⊥ are responses to a submission and are available only while the actor "
                            "can still respond — the view says so (`responses_available`); here F or N")
        is_bot_appeal = (r.role == "appeal" and c.verdict == BOT)
        if is_bot_appeal:
            if objection not in (UPHELD, REJECTED):
                raise RuleError("an appeal of ⊥ must state the objection disposition: 'upheld' "
                                "(the evidence was missing) or 'rejected' (it was present) (§8.1)")
            if objection == UPHELD and verdict != N:
                raise RuleError("if the evidence was missing the fulfillment verdict is N")
        elif objection is not None:
            raise RuleError("objection disposition applies only to appeals of ⊥")
        credits = self.ledger.purchase(r.reviewer, cost, case=c.id, note=f"review {rid}") if cost > 0 else 0.0
        r.cost += credits
        r.verdict, r.objection, r.t_done, r.status = verdict, objection, self.t, "done"
        self._reimburse(c, r)
        self._log(c, f"review {rid} by {r.reviewer}: {verdict}{' / ' + objection if objection else ''} (cost {credits:.3f} credits)")
        a = self.actors[r.reviewer]
        if r.role == "initial":
            if verdict in (F, N):
                a.open_review = None                    # a P or ⊥ keeps the reviewer attached (§6)
            self._initial_verdict(c, verdict)
        elif r.role == "audit":
            a.open_review = None
            self._audit_result(c, r)
        else:
            a.open_review = None
            self._maybe_settle_challenge(c)

    # ------------------------------------------------------- initial verdict
    def _initial_verdict(self, c: Case, verdict: str):
        c.verdict, c.t_verdict = verdict, self.t
        c.window_end = self.t + self.p.W
        if verdict == F:
            c.state = "PENDING"
            self._release_capacity(c)
        else:
            c.state = "AWAITING_RESPONSE"
            c.response_deadline = self.t + self.p.T_resp

    def judge_nested(self, cid: str, verdict: str):
        c = self._case(cid)
        if not c.is_nested():
            raise RuleError("judge_nested: root cases get an independent reviewer")
        if c.state != "SUBMITTED":
            raise RuleError(f"judge_nested: case {cid} is {c.state}")
        if verdict not in (F, N):
            raise RuleError("a requester-actor accepts or rejects")
        A = c.requester
        self._log(c, f"{A} judges {verdict}")
        if verdict == F:
            self.ledger.release(A, c.rejection_bond, key=f"rej:{cid}", case=cid, note="released on acceptance")
            c.rejection_bond = 0.0
        self._initial_verdict(c, verdict)

    def _release_capacity(self, c: Case):
        a = self.actors.get(c.actor)
        if a and a.committed == c.id:
            a.committed = None

    def _release_attached_reviewer(self, c: Case):
        for rid in c.reviews:
            r = self.reviews[rid]
            if r.role == "initial" and r.status in ("open", "done") and self.actors[r.reviewer].open_review == rid:
                self.actors[r.reviewer].open_review = None

    # ---------------------------------------------------------- responses
    def respond(self, cid: str, action: str, d: Optional[str] = None):
        c = self._case(cid)
        if c.state != "AWAITING_RESPONSE":
            raise RuleError(f"respond: case {cid} is {c.state}")
        if self.t > c.response_deadline:
            raise RuleError("respond: response window closed")
        if action == "accept":
            self._finalize_N(c, reason="rejection accepted")
        elif action == "appeal":
            if c.verdict not in (N, BOT):
                raise RuleError("appeal: only N and ⊥ are appealable; a P is revised or accepted (§6.1)")
            self._check_grounds(d)
            if self.ledger.wallet(c.actor).U + 1e-9 < c.D:
                raise LedgerError(f"appeal: {c.actor} cannot fund the court fee {c.D}")
            self._open_challenge(c, kind="appeal", challenger=c.actor, d=d)
            self._release_attached_reviewer(c)
            c.state = "PENDING"
            self._release_capacity(c)
        elif action == "revise":
            if c.verdict != P:
                raise RuleError("revise only after P")
            if c.revisions_used >= 1:
                raise RuleError("one revision only (§6)")
            c.revisions_used += 1
            c.state, c.resubmit_deadline = "RESUBMITTING", self.t + self.p.T_rev
            self._log(c, f"revision chosen; resubmit by {c.resubmit_deadline}")
        elif action == "supply_evidence":
            if c.verdict != BOT:
                raise RuleError("supply_evidence only after ⊥")
            c.state, c.resubmit_deadline = "RESUBMITTING", self.t + self.p.T_evid
            self._log(c, f"evidence to be supplied by {c.resubmit_deadline}")
        else:
            raise RuleError(f"unknown response {action}")

    def _initial_review(self, c: Case) -> Review:
        for rid in reversed(c.reviews):
            r = self.reviews[rid]
            if r.role == "initial" and r.status == "done":
                return r
        raise RuleError("no completed initial review")

    # ---------------------------------------------------------- challenges
    def _open_challenge(self, c: Case, kind: str, challenger: Optional[str], audit_review: Optional[Review] = None,
                        d: Optional[str] = None):
        if c.challenge_round_used:
            raise RuleError("one challenge round per case (§8)")
        if challenger is not None:
            # collect the fee first: an unpaid filing changes nothing (atomicity)
            self.ledger.transfer(challenger, Ledger.OMEGA, c.D, case=c.id, note=f"court fee ({kind})")
            c.court_fee_paid_by = challenger
            self._service_omega_claims()
        c.challenge_round_used = True
        c.challenge = {"kind": kind, "challenger": challenger, "reviews": [], "resolved": False, "d": d}
        if audit_review is not None:
            audit_review.is_audit_as_appeal = True
            c.challenge["reviews"].append(audit_review.id)
        c.open_items += 1
        # the grounds the reviewers will examine are part of the admitted action: commit them
        self.history.append("challenge", {"t": self.t, "case": c.id, "kind": kind, "challenger": challenger,
                                          "appealed": c.verdict, "d": d})
        self._log(c, f"challenge opened: {kind} by {challenger}")

    def dispute(self, cid: str, challenger: str, d: Optional[str] = None):
        c = self._case(cid)
        if not c.is_root:
            raise RuleError("only root requesters dispute; a requester-actor is its own judge")
        if challenger != c.requester:
            raise RuleError("only the case's requester may dispute")
        if c.state != "PENDING" or c.outcome_or_verdict() != F:
            raise RuleError("dispute: no F verdict pending")
        if self.t > c.window_end:
            raise RuleError("dispute: window closed")
        if c.challenge_round_used:
            raise RuleError("one challenge round per case (§8)")
        if any(a[3] == "override" for a in c.assessments):
            raise RuleError("dispute: a human ruling has settled this case's assessment; a disagreement with "
                            "the ruling is for human review, not a model challenge (§15.2)")
        self._check_grounds(d)
        if self.ledger.wallet(challenger).U + 1e-9 < c.D:
            raise LedgerError(f"dispute: {challenger} cannot fund the court fee {c.D}")   # validate before any change
        audit = next((self.reviews[r] for r in c.reviews
                      if self.reviews[r].role == "audit" and self.reviews[r].status != "withdrawn"), None)
        if audit is not None and audit.status == "open":
            self._open_challenge(c, "dispute", challenger, audit_review=audit, d=d)
            c.open_items -= 1                   # the audit's suspension merges into the challenge
        elif audit is not None and audit.status == "done" and audit.verdict == F:
            self._open_challenge(c, "dispute", challenger, audit_review=audit, d=d)
        else:
            self._open_challenge(c, "dispute", challenger, d=d)
            if c.audit_vacated:                 # an admitted dispute takes over the vacated audit obligation
                c.audit_vacated = False
                c.open_items -= 1
        c.assessments.append((self.t, challenger, N, "dispute"))
        self._log(c, f"{challenger} disputes the approval")

    def _audit_result(self, c: Case, r: Review):
        if r.is_audit_as_appeal:
            self._maybe_settle_challenge(c)
            return
        c.open_items -= 1
        if r.verdict == c.outcome_or_verdict():        # the live assessment, never a superseded one
            self._log(c, f"audit {r.id} agrees")
        else:
            self._open_challenge(c, "audit", challenger=None, audit_review=r)

    def _maybe_settle_challenge(self, c: Case):
        ch = c.challenge
        if ch is None or ch["resolved"]:
            return
        done = [self.reviews[r] for r in ch["reviews"] if self.reviews[r].status == "done"]
        if len(done) < 2:
            return
        r1, r2 = done[0], done[1]
        if c.verdict == BOT:
            if r1.objection != r2.objection:
                self._log(c, "appeal reviewers split on the ⊥ objection; awaiting orchestrator ruling")
                return
            if r1.objection == UPHELD:
                self._settle_challenge(c, outcome=N, by="appeal reviewers", objection=UPHELD)
                return
            if r1.verdict == r2.verdict:
                self._settle_challenge(c, outcome=r1.verdict, by="appeal reviewers", objection=REJECTED)
            else:
                self._log(c, "⊥ objection rejected but fulfillment split; awaiting orchestrator ruling")
            return
        if r1.verdict == r2.verdict:
            self._settle_challenge(c, outcome=r1.verdict, by="appeal reviewers")
        else:
            self._log(c, "appeal reviewers split; awaiting orchestrator ruling")

    def rule(self, cid: str, outcome: str, objection: Optional[str] = None):
        """Orchestrator ruling on a split (§8.4). For an appeal of ⊥ the ruling states both answers."""
        c = self._case(cid)
        ch = c.challenge
        if ch is None or ch["resolved"]:
            raise RuleError("rule: no open challenge")
        done = [self.reviews[r] for r in ch["reviews"] if self.reviews[r].status == "done"]
        if len(done) < 2:
            raise RuleError("rule: both appeal reviews must be complete")
        if outcome not in (F, N):
            raise RuleError("rule: outcome is F or N")
        if c.verdict == BOT:
            if objection not in (UPHELD, REJECTED):
                raise RuleError("rule: an appeal of ⊥ needs the objection disposition")
            if objection == UPHELD and outcome != N:
                raise RuleError("rule: an upheld ⊥ settles as N")
            split = (done[0].objection != done[1].objection) or \
                    (done[0].objection == REJECTED and done[0].verdict != done[1].verdict)
        else:
            if objection is not None:
                raise RuleError("rule: objection disposition applies only to ⊥")
            split = done[0].verdict != done[1].verdict
        if not split:
            raise RuleError("rule: the orchestrator rules only on a split")
        self._settle_challenge(c, outcome=outcome, by="orchestrator", objection=objection)

    def _settle_challenge(self, c: Case, outcome: str, by: str, objection: Optional[str] = None):
        ch = c.challenge
        ch["resolved"] = True
        ch["outcome"], ch["by"], ch["objection"] = outcome, by, objection
        challenger = ch["challenger"]
        if c.verdict == BOT:
            original_overturned = (objection == REJECTED)
        else:
            original_overturned = (c.verdict != outcome)
        if original_overturned:
            if c.is_root:
                self._overturn_review(c, self._initial_review(c), pay_fee_to=challenger)
            else:
                self._overturn_requester_verdict(c, pay_fee_to=challenger)
        self._release_attached_reviewer(c)
        for rid in ch["reviews"]:
            r = self.reviews[rid]
            if r.status != "done":
                continue
            if c.verdict == BOT:
                wrong = (r.objection != objection) or (objection == REJECTED and r.verdict != outcome)
            else:
                wrong = (r.verdict != outcome)
            if wrong:
                self._overturn_review(c, r, pay_fee_to=None)
        c.open_items -= 1
        c.outcome = outcome
        self._log(c, f"challenge settled {outcome}{' / ' + objection if objection else ''} by {by}")
        if outcome == N:
            self._finalize_N(c, reason=f"{ch['kind']} upheld nonfulfillment")
        else:
            c.state = "PENDING"
            self._release_capacity(c)

    def _overturn_review(self, c: Case, r: Review, pay_fee_to: Optional[str]):
        r.status = "overturned"
        a = self.actors[r.reviewer]
        self._record_outcome(r.reviewer, False)
        a.p_audit = min(self.p.p_cap, a.p_audit * 2)
        a.streak = 0
        if a.open_review == r.id:
            a.open_review = None
        bond = r.bond
        if pay_fee_to is not None and c.court_fee_paid_by == pay_fee_to and c.court_fee_reimbursed == 0:
            self.ledger.transfer_locked(r.reviewer, pay_fee_to, c.D, key=f"bond:{r.id}", case=c.id, note="court fee")
            c.court_fee_reimbursed = c.D
            bond -= c.D
        self.ledger.burn_locked(r.reviewer, bond, key=f"bond:{r.id}", case=c.id, note="bond burned")
        self._log(c, f"review {r.id} overturned; {r.reviewer} forfeits bond")

    def _overturn_requester_verdict(self, c: Case, pay_fee_to: Optional[str]):
        A = c.requester
        self._record_outcome(A, False)
        bond = c.rejection_bond
        if pay_fee_to is not None and c.court_fee_paid_by == pay_fee_to and c.court_fee_reimbursed == 0:
            self.ledger.transfer_locked(A, pay_fee_to, c.D, key=f"rej:{c.id}", case=c.id, note="court fee")
            c.court_fee_reimbursed = c.D
            bond -= c.D
        self.ledger.burn_locked(A, bond, key=f"rej:{c.id}", case=c.id, note="rejection bond burned")
        c.rejection_bond = 0.0
        self._log(c, f"requester {A}'s rejection overturned; rejection bond forfeited")

    # ---------------------------------------------------------- delegation
    def cancel_nested(self, cid: str):
        c = self._case(cid)
        if not c.is_nested():
            raise RuleError("cancel_nested: not a nested case")
        if c.state == "AVAILABLE":
            return self.withdraw_unawarded(cid)
        if c.state != "COMMITTED":
            raise RuleError("cancel_nested: cancellation is available only until the subcontractor submits")
        A, B_ = c.requester, c.actor
        fee = min(c.actor_cost, c.K)
        pool = self.ledger.pool(cid)
        from_escrow = min(fee, pool.escrow)
        rest = fee - from_escrow
        if rest > 1e-12 and self.ledger.wallet(A).U + 1e-9 < rest:
            raise RuleError("cancel_nested: requester-actor cannot fund the kill fee")
        if from_escrow > 0:
            self.ledger.pay_from_escrow(cid, B_, from_escrow, note="kill fee from escrow")
        if rest > 1e-12:
            self.ledger.transfer(A, B_, rest, case=cid, note="kill fee from unlocked")
        if pool.escrow > 1e-12:
            self.ledger.pay_from_escrow(cid, A, pool.escrow, note="escrow returned")
        self.ledger.release(B_, c.G, key=f"G:{cid}", case=cid, note="subcontractor guarantee released")
        self.ledger.release(A, c.rejection_bond, key=f"rej:{cid}", case=cid, note="rejection bond released")
        c.rejection_bond = 0.0
        self.actors[B_].committed = None
        self.cases[c.parent].actor_cost += fee
        self._touch(self.cases[c.parent])
        self._terminal_cleanup(c)
        c.state, c.final = "CANCELLED", True
        self._log(c, f"cancelled by {A}; kill fee {fee} to {B_}")

    def withdraw_pool_exhaustion(self, parent_id: str, nested_id: str):
        parent, nested = self._case(parent_id), self._case(nested_id)
        if nested.parent != parent_id or nested.state != "AVAILABLE":
            raise RuleError("pool exhaustion: nested request must be unawarded")
        if self.t < nested.t_post + self.p.T_wait:
            raise RuleError("pool exhaustion: T_wait has not elapsed")
        if parent.state != "COMMITTED":
            raise RuleError("pool exhaustion: parent not committed")
        if self.t > parent.deadline:
            raise RuleError("pool exhaustion: parent's deadline already passed (ordinary miss)")
        parent.I_pool = True
        self._finalize_N(parent, reason="pool exhaustion (reduced forfeiture, not actor fault)",
                         forfeit_fraction=self.p.rho_pool, actor_fault=False)

    def _terminal_cleanup(self, c: Case):
        """On any exit, unawarded nested requests fall with their parent (§9.4)."""
        for ch in c.children:
            if self.cases[ch].state == "AVAILABLE":
                self.withdraw_unawarded(ch)

    # ------------------------------------------------------------ finality
    def _finalize_N(self, c: Case, reason: str, forfeit_fraction: float = 1.0, actor_fault: bool = True):
        c.outcome = N
        if forfeit_fraction >= 1.0:
            c.I_N = True
        forfeit = forfeit_fraction * c.G
        self.ledger.transfer_locked(c.actor, c.requester, forfeit, key=f"G:{c.id}", case=c.id, note=f"forfeit: {reason}")
        if c.G - forfeit > 1e-12:
            self.ledger.release(c.actor, c.G - forfeit, key=f"G:{c.id}", case=c.id, note="guarantee remainder")
        if actor_fault:
            self._record_outcome(c.actor, False)
        self._return_escrow(c)
        if any(self.reviews[r].status == "done" for r in c.reviews):
            c.needs_review_settlement = True            # fee entitlements need the tick's emission batch
        else:
            self._settle_reviews(c, 0.0)                # debts and unused deposit settle at once
        if c.is_nested() and c.rejection_bond > 0:
            self.ledger.release(c.requester, c.rejection_bond, key=f"rej:{c.id}", case=c.id, note="rejection stood")
            c.rejection_bond = 0.0
        self._release_attached_reviewer(c)
        self._terminal_cleanup(c)
        c.state, c.final = "FINAL_N", True
        c.grade = self._grade(c)
        self._release_capacity(c)
        self._log(c, f"final N: {reason}")

    def _return_escrow(self, c: Case):
        """The delivery price goes back to the requester on final N. The deposit does not go
        back here: settlement pays cost debts from it first and returns only what is unused."""
        pool = self.ledger.pool(c.id)
        if pool.escrow > 1e-12:
            self.ledger.pay_from_escrow(c.id, c.requester, pool.escrow, note="escrow returned")

    def override(self, cid: str, human: str, outcome: str, objection: Optional[str] = None):
        """§15.2: before vesting an override is the ruling; after, the record changes, money does not.
        One path for every entry: validate the whole ruling first, then void every unfinished
        assignment without fault, overturn every completed verdict that contradicts it — a
        reviewer's or a requester-actor's — and settle."""
        c = self._case(cid)
        # ---- validate everything before recording anything (atomicity)
        if human not in self.humans:
            raise RuleError("override: only a human may rule; a delegate accepts or disputes (§15.2)")
        if outcome not in (F, N):
            raise RuleError("override: outcome is F or N")
        if c.state in ("AVAILABLE", "COMMITTED", "WITHDRAWN", "CANCELLED"):
            raise RuleError(f"override: case {cid} is {c.state}; there is no result to rule on")
        settled_before = c.final
        open_challenge = c.challenge is not None and not c.challenge["resolved"]
        if c.verdict == BOT and c.state != "SUBMITTED":
            if objection not in (UPHELD, REJECTED):
                raise RuleError("override of a ⊥ needs the objection disposition (§8.1)")
            if objection == UPHELD and outcome != N:
                raise RuleError("an upheld ⊥ settles as N (§8.1)")
        elif objection is not None:
            raise RuleError("objection disposition applies only to a ⊥")
        # ---- record
        c.assessments.append((self.t, human, outcome, "override"))
        self._log(c, f"human {human} overrides to {outcome}{' / ' + objection if objection else ''}")
        if settled_before:
            before = self.ledger.total_credits()
            c.outcome = outcome
            if c.is_root:
                c.grade = self._grade(c)
            if c.actor and c.state == "VESTED" and outcome == N:
                self._record_outcome(c.actor, False)
            for rid in c.reviews:
                r = self.reviews[rid]
                if r.status == "vested" and self._assessment_contradicts(c, r, outcome, objection):
                    r.contradicted_by_override = True   # settled: the reliability record changes, money does not
                    self._record_outcome(r.reviewer, False)
                elif r.status == "done" and self._assessment_contradicts(c, r, outcome, objection):
                    self._overturn_review(c, r, pay_fee_to=None)   # not yet settled: the ruling precedes its payout
            if c.challenge is not None:
                c.challenge["objection"] = objection if c.verdict == BOT else c.challenge.get("objection")
            c.corrective_obligation = f"corrective request to be posted by {human}"
            c.post_vesting_funds_moved += abs(self.ledger.total_credits() - before)
            return
        # ---- unfinished assignments are voided without fault
        for rid in list(c.reviews):
            r = self.reviews[rid]
            if r.status == "open":
                self._withdraw_review(r, burn=False)
        if c.audit_vacated:
            c.audit_vacated = False
            c.open_items -= 1
        self._release_attached_reviewer(c)
        if open_challenge:
            self._settle_challenge(c, outcome=outcome, by=f"human {human}", objection=objection)
            if c.final and c.is_root:
                c.grade = self._grade(c)
            return
        # ---- completed verdicts that contradict the ruling are overturned
        for rid in list(c.reviews):
            r = self.reviews[rid]
            if r.status == "done" and self._assessment_contradicts(c, r, outcome, objection):
                self._overturn_review(c, r, pay_fee_to=None)
        if c.is_nested() and c.rejection_bond > 0:
            if self._contradicts(c.verdict, outcome, objection):
                self._overturn_requester_verdict(c, pay_fee_to=None)      # a rejection the ruling contradicts
            elif outcome == F:
                # the ruling accepts the result: the rejection obligation ends, whether or not A had judged
                self.ledger.release(c.requester, c.rejection_bond, key=f"rej:{c.id}", case=c.id,
                                    note="released: result accepted by ruling")
                c.rejection_bond = 0.0
        if outcome == N:
            self._finalize_N(c, reason="human override")
        else:
            c.outcome = F
            c.state = "PENDING"
            if c.window_end is None or c.t_verdict is None:
                c.t_verdict, c.window_end = self.t, self.t
            self._release_capacity(c)

    @staticmethod
    def _check_grounds(d) -> None:
        """A challenge's grounds are text, or absent. Checked before any fee or state change,
        because the grounds are committed to the record as part of the admitted action (§14)."""
        if d is not None and not isinstance(d, str):
            raise RuleError(f"grounds must be text, got {type(d).__name__}")

    def _assessment_contradicts(self, c: Case, r: Review, outcome: str, objection: Optional[str]) -> bool:
        """Does a reviewer's complete assessment contradict a ruling? An appeal reviewer of a ⊥
        answered two questions and is contradicted on either (§8.1); every other review is
        judged by its verdict."""
        if r.role == "appeal" and c.verdict == BOT:
            if r.objection != objection:
                return True
            return objection == REJECTED and r.verdict != outcome
        return self._contradicts(r.verdict, outcome, objection)

    @staticmethod
    def _contradicts(verdict: Optional[str], outcome: str, objection: Optional[str]) -> bool:
        """Does a completed verdict contradict a ruling? F contradicts N; N and P contradict F;
        a ⊥ is contradicted only by a rejected objection (§8.1)."""
        if verdict is None:
            return False
        if verdict == BOT:
            return objection == REJECTED
        if verdict == F:
            return outcome == N
        return outcome == F          # N or P against F

    def accept_explicit(self, cid: str, requester: str):
        c = self._case(cid)
        if requester != c.requester or c.state != "PENDING" or c.outcome_or_verdict() != F:
            raise RuleError("accept_explicit: not a pending F for this requester")
        c.assessments.append((self.t, requester, F, "accept"))
        self._log(c, f"{requester} explicitly accepts")

    # ----------------------------------------------------------- labelling
    def _grade(self, c: Case) -> str:
        """§15.3: the grade is that of the event that *established* the settled outcome, by the
        author of that event — a human who rules on a delegate's request establishes a
        human-explicit outcome; a delegate who accepts establishes a delegate-explicit one."""
        if c.is_nested():
            return PROCEDURAL
        explicit = [a for a in c.assessments if a[2] == c.outcome and a[3] in ("accept", "dispute", "override")]
        if explicit:
            author = explicit[-1][1]
            return DELEGATE if author in self.delegates else HUMAN
        if c.challenge_round_used or any(self.reviews[r].role == "audit" and self.reviews[r].status != "withdrawn"
                                         for r in c.reviews):
            return PROCEDURAL
        return DEFAULT

    # ------------------------------------------------------------ settlement
    def _settle_reviews(self, c: Case, emission_per_weight: float):
        """§4.3 single payout rule. Unconditional cost debts are processed first and for every
        review of the case, whether or not any review survives; conditional fee entitlements
        are then paid to the survivors by pro-rata haircut; with no survivor, what the deposit
        did not need goes back to the requester as unused."""
        surviving = [self.reviews[r] for r in c.reviews if self.reviews[r].status == "done"]
        pool_obj = self.ledger.pool(c.id)
        for r in surviving:
            e = self._w(r.role) * emission_per_weight
            self.ledger.mint_emission_to_pool(c.id, e)
            r.fee = e
        n = len(surviving)
        dep_remainder = pool_obj.deposit
        for r in surviving:
            r.fee += dep_remainder / n
        pool_total = self.ledger.fee_pool_balance(c.id)
        repaid = 0.0
        # 1. cost debts, every review — an overturned reviewer's bond was the penalty; its cost survives
        for rid in c.reviews:
            r = self.reviews[rid]
            if r.deferred > 1e-12:
                pay = min(r.deferred, pool_total - repaid)
                if pay > 0:
                    self.ledger.pay_from_fee_pool(c.id, r.reviewer, pay, note="deferred reimbursement")
                    r.deferred -= pay
                    r.reimbursed += pay
                    repaid += pay
                if r.deferred > 1e-12:
                    self.omega_claims.append(Claim(r.reviewer, r.deferred, r.id))
                    r.reimbursed_pending += r.deferred
                    r.deferred = 0.0
        if c.omega_advance > 1e-12:
            pay = min(c.omega_advance, pool_total - repaid)
            if pay > 0:
                self.ledger.pay_from_fee_pool(c.id, Ledger.OMEGA, pay, note="Ω advance repaid")
                repaid += pay
            c.omega_advance -= pay
        # 2. fee entitlements, survivors only
        if surviving:
            remaining = max(0.0, pool_total - repaid)
            scale = (remaining / pool_total) if pool_total > 1e-12 else 0.0
            for r in surviving:
                r.fee *= scale
                if r.fee > 1e-12:
                    self.ledger.pay_from_fee_pool(c.id, r.reviewer, r.fee, note="review fee")
                self.ledger.release(r.reviewer, r.bond, key=f"bond:{r.id}", case=c.id, note="bond released")
                r.status = "vested"
                a = self.actors[r.reviewer]
                self._record_outcome(r.reviewer, True)
                a.vests.append(self.t)
                horizon = self.t - self.p.kappa_window     # a vest this old can never count again
                while a.vests and a.vests[0] <= horizon:
                    a.vests.pop(0)
                a.streak += 1
                if a.on_duty:
                    a.duty_reviews += 1
                if a.streak % self.p.p_halve_every == 0:
                    a.p_audit = max(self.p.p_floor, a.p_audit / 2)
            left = self.ledger.pool(c.id).minted
            if left > 1e-9:                            # rounding residue of minted emission only
                self.ledger.pay_from_fee_pool(c.id, Ledger.OMEGA, left, note="pool sweep")
        else:
            left = self.ledger.pool(c.id).deposit
            if left > 1e-12:                           # unused deposit: no entitled reviewer
                self.ledger.pay_from_deposit(c.id, c.requester, left, note="unused deposit returned")
        c.needs_review_settlement = False
        self._service_omega_claims()

    def _vest(self, c: Case, epw: float):
        self.ledger.pay_from_escrow(c.id, c.actor, c.B, note="delivery price")
        self.ledger.release(c.actor, c.G, key=f"G:{c.id}", case=c.id, note="guarantee released")
        if c.is_nested():
            self.cases[c.parent].actor_cost += c.B          # §4.6: nested payments are execution cost
            self._touch(self.cases[c.parent])
        self._settle_reviews(c, epw)
        c.outcome = c.outcome or F
        c.t_vest, c.final, c.state = self.t, True, "VESTED"
        c.grade = self._grade(c)
        self._record_outcome(c.actor, True)
        self._log(c, f"vested; grade {c.grade}")

    def _service_omega_claims(self):
        """§4.3 / §10.4: Ω pays its outstanding reviewer claims first in, first out, whenever it has funds."""
        om = self.ledger.wallet(Ledger.OMEGA)
        while self.omega_claims and om.U > 1e-12:
            claim = self.omega_claims[0]
            who, amt = claim.reviewer, claim.amount
            pay = min(amt, om.U)
            self.ledger.transfer(Ledger.OMEGA, who, pay, case=self.reviews[claim.review].case, note="Ω claim serviced")
            r = self.reviews[claim.review]                 # the obligation being paid, not a lookalike
            r.reimbursed += pay
            r.reimbursed_pending -= pay
            if amt - pay <= 1e-12:
                self.omega_claims.pop(0)
            else:
                self.omega_claims[0] = Claim(who, amt - pay, claim.review)

    # ---------------------------------------------------------------- ticks
    def advance(self, to_t: int):
        from .invariants import check_all, check_tick
        if to_t < self.t:
            raise RuleError("time does not run backwards")
        while self.t < to_t:
            self._process_tick(self.t)
            self.t += 1
            self.ledger.t = self.t
            check_tick(self)
            every = self.p.full_check_every
            if every and self.t % every == 0:
                check_all(self)

    def _process_tick(self, tick: int):
        # step 2: deadlines (inclusive)
        for c in list(self._live_cases.values()):
            if c.state == "COMMITTED" and tick >= c.deadline:
                self._finalize_N(c, reason="delivery deadline missed")
            elif c.state == "AWAITING_RESPONSE" and tick >= c.response_deadline:
                self._finalize_N(c, reason="no response: rejection accepted by default")
            elif c.state == "RESUBMITTING" and tick >= c.resubmit_deadline:
                self._finalize_N(c, reason="resubmission window missed")
        for r in list(self._live_reviews.values()):
            if r.status == "open" and tick >= r.deadline:
                self._withdraw_review(r)
        # step 3: vesting and settlement, one emission batch
        vesting = [c for c in self._live_cases.values()
                   if c.state == "PENDING" and c.open_items == 0 and c.window_end is not None
                   and tick >= c.window_end and (c.challenge is None or c.challenge["resolved"])]
        vesting_ids = {c.id for c in vesting}
        settling = [c for c in self._live_cases.values() if c.needs_review_settlement and c.id not in vesting_ids]
        batch = vesting + settling
        if batch:
            total_w = sum(self._w(self.reviews[rid].role)
                          for c in batch for rid in c.reviews if self.reviews[rid].status == "done")
            E = self.p.emission(tick)
            epw = (E / total_w) if total_w > 0 else 0.0
            for c in vesting:
                self._vest(c, epw)
            for c in settling:
                if c.needs_review_settlement:
                    self._settle_reviews(c, epw)
        # step 4: Ω services claims
        self._service_omega_claims()
        # step 5: rotation
        self._rotate(tick)

    def _withdraw_review(self, r: Review, burn: bool = True):
        """Timeout (burn=True): half the bond burns, the reviewer is at fault, and the position
        is vacated but the case's obligation stands — a vacated audit keeps the case suspended
        until refilled or waived (§7.5). Voiding (burn=False): a human ruling mooted the
        assignment; the bond returns whole, no fault, and the obligation ends with it."""
        c = self.cases[r.case]
        r.status = "withdrawn"
        a = self.actors[r.reviewer]
        if burn:
            half = r.bond / 2
            self.ledger.burn_locked(r.reviewer, half, key=f"bond:{r.id}", case=c.id, note="timeout: half burned")
            self.ledger.release(r.reviewer, r.bond - half, key=f"bond:{r.id}", case=c.id, note="timeout: half released")
            self._record_outcome(r.reviewer, False)
        else:
            self.ledger.release(r.reviewer, r.bond, key=f"bond:{r.id}", case=c.id, note="assignment voided")
        if a.open_review == r.id:
            a.open_review = None
        if c.challenge and r.id in c.challenge["reviews"]:
            c.challenge["reviews"].remove(r.id)        # the appeal position is vacated
        if r.role == "audit" and not r.is_audit_as_appeal:
            if burn:
                c.audit_vacated = True                   # obligation stands; replacement admissible after the window
            elif c.open_items > 0:
                c.open_items -= 1                        # ruling supersedes the audit
        self._log(c, f"review {r.id} by {r.reviewer} {'timed out' if burn else 'voided'}; position vacated")

    def _rotate(self, tick: int):
        """§13: replacement-before-release; a turn is duty_turn_reviews vested reviews or
        duty_turn_ticks ticks; incoming replacements are the free actors with the lowest κ."""
        GV = self.p.G_V * self.ledger.index()
        # batch-start snapshot: only actors off duty when the tick began may be conscripted this
        # tick, so a released actor has at least one tick of ordinary eligibility (§13)
        pool = {a.id for a in self.actors.values()
                if not a.on_duty and a.committed is None and a.open_review is None
                and self.ledger.wallet(a.id).U + 1e-9 >= GV}
        for out in sorted((a for a in self.actors.values() if a.on_duty), key=lambda a: a.id):
            if out.volunteer or out.open_review is not None or out.duty_since is None:
                continue
            turn_done = (out.duty_reviews >= self.p.duty_turn_reviews
                         or tick - out.duty_since >= self.p.duty_turn_ticks)
            if not turn_done:
                continue
            candidates = [self.actors[i] for i in pool]
            if not candidates:
                continue
            inc = min(candidates, key=lambda a: (a.kappa, a.id))
            pool.discard(inc.id)
            inc.on_duty, inc.duty_since, inc.duty_reviews = True, tick, 0
            out.on_duty, out.duty_since, out.duty_reviews = False, None, 0
            self.history.append("rotation", {"t": tick, "in": inc.id, "out": out.id})

    def volunteer(self, aid: str, flag: bool = True):
        self._actor(aid).volunteer = flag
        self.history.append("actor", {"t": self.t, "actor": aid, "msg": f"volunteer={flag}"})

    # ------------------------------------------------------------ working set
    @staticmethod
    def _review_quiescent(r: Review) -> bool:
        return r.status in ("withdrawn", "overturned", "vested") and r.reimbursed_pending <= 1e-12 \
            and r.deferred <= 1e-12

    def _case_quiescent(self, c: Case) -> bool:
        return c.final and not c.needs_review_settlement \
            and all(self._review_quiescent(self.reviews[rid]) for rid in c.reviews)

    def _prune_working_set(self):
        """Called by the tick check after it has examined the working set: what can no longer
        change leaves it. Anything that is touched again comes back through the dirty set."""
        for cid in [cid for cid, c in self._live_cases.items() if self._case_quiescent(c)]:
            del self._live_cases[cid]
        for rid in [rid for rid, r in self._live_reviews.items() if self._review_quiescent(r)]:
            del self._live_reviews[rid]
        # the v1.0.1 engine scanned every case each tick; a settled case touched again that can
        # still change therefore belongs in the working set, in creation order like the rest
        back = [cid for cid in self._dirty_cases
                if cid not in self._live_cases and cid in self.cases and not self._case_quiescent(self.cases[cid])]
        if back:
            for cid in back:
                self._live_cases[cid] = self.cases[cid]
            self._live_cases = dict(sorted(self._live_cases.items(), key=lambda kv: int(kv[0][1:])))
        if self._paged:
            self._page_out()
        self._dirty_cases.clear()

    def _page_out(self):
        """Record mode: a resident case outside the working set, with nothing left to change,
        goes to the archive with its reviews; its per-case indexes and its empty pool go too."""
        for cid, c in self.cases.resident_items():
            if cid in self._live_cases or not self._case_quiescent(c):
                continue
            self.ledger.events_by_case.pop(cid, None)
            pl = self.ledger.pools.get(cid)
            if pl is not None and abs(pl.escrow) + abs(pl.deposit) + abs(pl.minted) <= 1e-12:
                del self.ledger.pools[cid]            # an empty pool is recreated empty on demand
            self.cases.evict(cid)
        for rid, r in self.reviews.resident_items():
            if not self.cases.is_resident(r.case):
                self.reviews.evict(rid)

    def close(self):
        """Record mode: flush and close the files. The record on disk is then complete; the
        world is not to be read or advanced afterwards."""
        if self._paged:
            self.history.entries.close()
            self.ledger.events.close()
            self.cases.close()
            self.reviews.close()

    # ---------------------------------------------------------------- views
    def distinct_reviewers(self, cid: str) -> int:
        return len({self.reviews[r].reviewer for r in self._case(cid).reviews})

    def positions(self, cid: str) -> int:
        return self._positions(self._case(cid))

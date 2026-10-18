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
import hashlib
import math
import os

from .params import Params
from .ledger import Ledger, LedgerError, History, amount, _i10_exempt, _i19_event_ok
from .record import Archive, PagedDict


class RuleError(Exception):
    """An action the rules do not permit in the current state."""


F, N, P, BOT = "F", "N", "P", "⊥"
VERDICTS = {F, N, P, BOT}
UPHELD, REJECTED = "upheld", "rejected"          # disposition of a ⊥ objection (§8.1)

# Label grades (§15.3); `plant` since 1.2.0 — truth known by construction, never promoted
HUMAN, DELEGATE, DEFAULT, PROCEDURAL, PLANT = "human-explicit", "delegate-explicit", "protocol-default", "procedural", "plant"

ROLE_W = {"initial": "w_ordinary", "appeal": "w_appeal", "audit": "w_audit"}
PANEL_ROLES = ("appeal", "audit")              # the challenge-panel seats (1.2.0 §2.2)

# The orchestrator's two system wallets (1.2.0 §2.1, Appendix A): a plant's requester and its actor.
# Funded by transfer from Ω when a plant is created and swept back to Ω when its tree closes.
PLANT_REQ, PLANT_ACT = "OMEGA-REQ", "OMEGA-ACT"
# The duty fund (1.3.0 §2.4): the dial's raised tax, (m_t − 1) ω_0 B of each award, paid out to the reviews
# settling in each batch by role weight as an uplift on the fixed fee.
DUTY_FUND = "DUTY-FUND"
TROOP_ACCT = "TROOP-ACCT"     # 1.7.0 §2.1: the troop account, the troops' wallet when Params.troop_account
TROOP_PREFIX = "T"                              # 1.4.0: a troop id, single-use, aliased to the fund's wallet


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
    # the plant record (1.2.0 §2.2): trailing n_P outcomes per kind — for a bad plant whether it was
    # approved, for a good plant whether it was rejected — and the suspension clock
    plant_bad: list = field(default_factory=list)    # (t, approved)
    plant_good: list = field(default_factory=list)   # (t, rejected)
    suspended_until: Optional[int] = None
    probation: bool = False     # 1.3.0: a probationer — initial reviews only, odds pinned, no awards, earning its way back
    since_susp: int = 0         # plant outcomes adjudicated since the suspension began (1.3.0 §2.2: ≥ n_min to be readmitted)
    susp_started: Optional[int] = None
    readmitted_at: Optional[int] = None
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

    # -- the plant record (1.2.0 §2.2) --------------------------------------------------------
    @property
    def a_hat(self) -> float:
        """Smoothed bad-plant approval rate, (o_bad + 1) / (n_bad + 2)."""
        return (sum(1 for _, x in self.plant_bad if x) + 1) / (len(self.plant_bad) + 2)

    @property
    def r_hat(self) -> float:
        """Smoothed good-plant rejection rate, (o_good + 1) / (n_good + 2)."""
        return (sum(1 for _, x in self.plant_good if x) + 1) / (len(self.plant_good) + 2)

    def record_passes(self, theta: float) -> bool:
        """Each kind's rate is within the threshold, or that kind's record is undetermined
        (fewer than n_min plants of the kind)."""
        p = self._world.p
        if len(self.plant_bad) >= p.n_min and self.a_hat > theta + 1e-12:
            return False
        if len(self.plant_good) >= p.n_min and self.r_hat > theta + 1e-12:
            return False
        return True

    @property
    def duty_eligible(self) -> bool:
        """Eligible for any review: not suspended, and the record within θ_duty — or readmitted on
        probation, until its next plant adjudication re-checks the record."""
        return self.suspended_until is None and (self.probation or self.record_passes(self._world.p.theta_duty))

    @property
    def panel_eligible(self) -> bool:
        """Eligible for a challenge-panel seat (appeal, dispute, audit): duty-eligible, not on
        probation, and the record within θ_panel."""
        w = self._world
        if w.p.panel_determined and w.first_plant_adjudicated_at is not None and len(self.plant_bad) < w.p.n_min:
            return False                                # 1.6.0 §2.4: a determined record, once the clock has started
        return self.duty_eligible and not self.probation and self.record_passes(w.p.theta_panel)

    # -- membership (1.3.0 §2.1–2.2) ---------------------------------------------------------
    @property
    def is_member(self) -> bool:
        """A member of the market: neither suspended nor on probation. Only members win awards."""
        return self.suspended_until is None and not self.probation

    @property
    def pinned(self) -> bool:
        """1.3.0 §2.2: a probationer's audit odds, and an undetermined newcomer's (fewer than n_min bad
        plants judged), are pinned at 1; the §8.3 update does not run for them."""
        p = self._world.p
        return p.membership and (self.probation or len(self.plant_bad) < p.n_min)

    @property
    def p_eff(self) -> float:
        """The audit odds a driver rolls: 1 while pinned, else the adaptive p_j scaled by the dial, min(1, m_t · p_j)."""
        if self.pinned:
            return 1.0
        return min(1.0, self._world.m_t * self.p_audit)


@dataclass
class ReviewView:
    """What a reviewer is allowed to see (§14): the submission and the assignment's terms,
    and the answers it may give. A fulfillment question is answered F or N; it may also be
    answered P or ⊥ exactly when `responses_available` says so — the first review of an
    unrevised submission. The view does not say whether a fulfillment question is an initial
    review or an audit; it says what may be answered, so identical views admit identical
    answers (§8.3). An appeal or a dispute states the question it asks (§8.1). Other verdicts
    and identities stay hidden — since 1.2.0 (§14 amended) the submission's actor too: the
    reviewer judges the work, not the worker, and a plant's view then carries nothing a case's
    does not. The view is a function of case fields that exclude the actor and the plant marker."""
    review_id: str
    case_id: str
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
    fee: float = 0.0              # what the review was paid at settlement: fixed fee + emission share
    fee_owed: float = 0.0         # the fixed fee by role, w_r * f (§4.3); fee_fixed < fee_owed is a haircut
    fee_fixed: float = 0.0        # the fixed fee actually paid from the root's fee pot
    is_audit_as_appeal: bool = False
    resumed: bool = False
    contradicted_by_override: bool = False
    reimbursed_pending: float = 0.0   # an Ω claim outstanding for this review's costs
    panel_ok: bool = True             # the reviewer was eligible for this tier when assigned (1.2.0 §2.2, I21)
    uplift: float = 0.0               # the duty-fund uplift paid at settlement (1.3.0 §2.4), included in `fee`


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
    phi_E: float = 0.0            # expense allowance (root only; nested 0)
    phi_F: float = 0.0            # fee pot (root only; nested 0)
    omega: float = 0.0
    nominals: Optional[tuple] = None   # (D, K, G_V, phi_E, phi_F) at the first lock
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
    # the two pots, accounted on the root (§4.3, I19): what left the fee pot as fees and, at tree
    # closure, as expense debts; what came back to the requester; and when the tree closed
    fees_from_pot: float = 0.0
    expenses_from_pot: float = 0.0
    allowance_refunded: float = 0.0
    pot_refunded: float = 0.0
    tree_closed: bool = False
    t_closed: Optional[int] = None
    # planted work (1.2.0 §2.1): the truth known by construction (True = good, False = bad), the
    # sealed marker committed at creation and where, and the adjudication once given
    plant: Optional[bool] = None
    plant_commit: Optional[str] = None
    plant_nonce: Optional[str] = None
    plant_hseq: Optional[int] = None
    plant_outcome: Optional[str] = None    # stood | failure | spent
    plant_reveal_hseq: Optional[int] = None
    member_at_award: bool = True           # 1.3.0 §2.1 / I22: the actor was a member when awarded
    # 1.4.0: the audit obligation, the seats' clocks, and troops
    audit_obligation: bool = False         # a rolled audit not yet seated holds the case (I25)
    audit_rolled_at: Optional[int] = None
    audit_vacated_at: Optional[int] = None
    seat_since: Optional[int] = None       # the initial seat has been required since this tick
    market_audit_only: bool = False        # a troop reviewer approved a troop's delivery: only a member audits it
    troop_award: bool = False              # awarded to a troop by summons (§2.3)
    initial_pinned: bool = False           # the initial approval was a pinned reviewer's (I25)
    # 1.6.0 §2.1: the service clock — ticks counted from posting while β ≥ B̄, stopped at the first verdict or at a
    # final without one; the lateness past T_s and the rebate owed, paid at the stop or carried as Ω's liability
    clock_ticks: int = 0
    clock_stopped_at: Optional[int] = None
    first_verdict_at: Optional[int] = None
    late_ticks: int = 0
    rebate_owed: float = 0.0
    rebate_paid: float = 0.0
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
        # The effort dial (1.2.0 §2.3) and the reserve it sizes. m_t is updated once per period from
        # the bad-plant approval rate; π_t, the audit odds, X_t and ω_t follow it. `plant_credit` is
        # what the plant rate calls for and has not been created: it grows by π_t at every real
        # initial assignment and falls by one per plant; what is still owed at the period's end is
        # the period's plant shortfall. With `dial` off, m_t stays 1 and X_t stays X.
        self.m_t: float = 1.0
        self.pi_t: float = params.pi0
        self.X_t: int = params.X
        self.plant_credit: float = 0.0
        self.plants_created = 0
        self.plant_shortfall = 0                        # plants the rate called for that Ω could not fund
        self.eligibility_shortfall = 0                  # Σ over ticks of (X_t − actors on duty) when the pool was empty
        self.reserve_shortfall_now = 0
        self.suspensions = 0
        self.alarm_streak = 0
        self.alarms = 0
        self.periods: list[dict] = []
        self.period = self._new_period(0)
        # 1.3.0: the reserve's member seats (sized each period on applied audit odds and the challenge
        # rate), the duty fund's flows, and readmissions
        self.member_seats: int = max(0, params.V_max - 1)
        self.fund_in = 0.0
        self.fund_out = 0.0
        self.readmissions = 0
        self.readmission_ticks_sum = 0
        self._member_pool_exhausted = True              # at the last rotation, no free fundable member was left to seat
        # 1.4.0: troops and the fund's order
        self.troops: dict[str, dict] = {}               # troop id -> kind, case, review, t_summons, t_release, cost, lock
        self._n_troop = 0
        self.advance_outstanding = 0.0                  # Ω's advance to the fund, repaid before uplift (≤ A_T)
        self.troop_capital_peak = 0.0                   # peak troop capital this period
        self.troop_capital_peak_prev = 0.0              # and the previous one; R_T is the larger (1.4.0 reading)
        # 1.5.0 §2.1: the troop demand D_s at each seating and its peak over the current period
        self.troop_demand_peak = 0.0                    # peak D_s this period — R_T under reserve_demand
        self.troop_demand_peak_refused = 0.0            # the refused component of D_s at the seating that set the peak
        self.troop_demand_held = 0.0                    # D_s at the last seating: capital held by live troops ...
        self.troop_demand_refused = 0.0                 # ... plus the cost of the summonses refused for funds
        self._pass_refused = 0.0                        # the refused demand of the summons pass in progress
        self._last_refusal_funds = False                # the last summons returned None because the fund could not carry it
        self.troop_demand_peak_prev = 0.0               # 1.6.0 §2.5: the previous period's peak demand (R_T over two periods)
        # 1.6.0 §2.1: the service clock's readings and Ω's liabilities
        self.first_plant_adjudicated_at: Optional[int] = None   # §2.4's switch
        self.omega_liabilities: list = []               # [{requester, amount, t, case}] — rebates Ω could not pay at the stop
        self.rebates_owed = 0.0
        self.rebates_paid = 0.0
        self.liabilities_accrued = 0.0
        self.liabilities_paid = 0.0
        self.on_time_n = 0
        self.late_n = 0
        self.lateness_sum = 0
        self._last_initial_rate = 0.0                   # the previous period's initial reviews a tick (the plant reserve's floor)
        self._x_target = params.X                       # 1.6.0 §2.3: the reserve target at the last rotation
        self._waiting_initial = 0
        self._waiting_panel = 0
        self._priority_violation = None                 # I26: a younger case summoned after an older one was refused
        self.fund_flow = 0.0                            # Σ of every event into/out of the troops' wallet (I23)
        # 1.7.0 §2.1: the troop surplus paid to Ω and Ω's record by source
        self.troop_surplus_paid = 0.0
        self.omega_fee_income = 0.0                     # the base service fee ω₀B per award, Ω's own income
        self.advances_made = 0.0
        self.advances_repaid = 0.0
        self._uplift_violation = None
        self.troop_summons_reviews = 0
        self.troop_summons_deliveries = 0
        self.troop_shortfall_seats = 0
        self.troop_shortfall_awards = 0
        self.troop_held_ticks = 0                       # case-ticks held for want of a seat no troop could take
        self.troop_ticks_reviews = 0
        self.troop_ticks_deliveries = 0
        self.held_market_audit_now = 0
        self.held_market_audit_max_age = 0
        self._pool_exhausted = False                    # at the last rotation, no eligible free actor was left
        self._reserve_dirty = False                     # an actor left duty since the last rotation (mid-tick)
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
        L = self.ledger
        if e.kind not in ("lock", "release"):
            tw = self.troop_wallet
            if e.dst is not None and L.resolve(e.dst) == tw and not str(e.dst).startswith("pool:"):
                self.fund_flow += e.amount
            if e.src is not None and L.resolve(e.src) == tw:
                self.fund_flow -= e.amount
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
        if c is not None and c.t_vest is not None and e.t > c.t_vest and not _i10_exempt(e.note):
            self._violations.append(f"I10 {cid}: {e.kind} {e.amount} at t={e.t} after vesting at {c.t_vest}")
        if not _i19_event_ok(e):
            self._violations.append(f"I19 {cid}: {e.kind} {e.amount} '{e.note}' crosses the pots")

    def _touch(self, case: Case):
        self._dirty_cases.add(case.id)

    def _w(self, role: str) -> float:
        return getattr(self.p, ROLE_W[role])

    def wallet(self, wid):
        return self.ledger.wallet(wid)

    def W(self, wid) -> float:
        return self.ledger.wallet(wid).W

    def _record_outcome(self, aid: str, stood: bool):
        a = self.actors.get(aid)
        if a is None:
            return                                      # a troop or the plant actor keeps no record (1.2.0, 1.4.0)
        a.outcomes.append((self.t, stood))
        if len(a.outcomes) > self.p.rho_window:
            del a.outcomes[: len(a.outcomes) - self.p.rho_window]

    def _freeze(self, c: Case):
        c.nominals = (c.D, c.K, c.G_V, c.phi_E, c.phi_F)

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
        if self.is_troop(parent.actor):
            raise RuleError("a troop never delegates (1.4.0 §2.1)")
        A = parent.actor
        idx = self.ledger.index()                 # §4.5: a nested case is denominated at posting
        D, K, GV = self.p.D * idx, self.p.K * idx, self.p.G_V * idx
        if self.ledger.wallet(A).U + 1e-9 < beta + GV:
            raise LedgerError(f"{A} cannot lock beta' + G_V = {beta + GV}")
        self._n_case += 1
        cid = f"q{self._n_case}"
        c = Case(cid, root=parent.root, requester=A, is_root=False, beta=beta, t_post=self.t, parent=parent_id)
        c.D, c.K, c.G_V, c.phi_E, c.phi_F = D, K, GV, 0.0, 0.0
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
        if c.is_nested():
            self._maybe_close_tree(self.cases[c.root])

    # ----------------------------------------------------------------- award
    def award(self, cid: str, actor_id: str, B: float, tau: int):
        B = amount(B, "B")
        tau = _int_ticks(tau, "tau")
        c = self._case(cid)
        if self.is_troop(actor_id):
            raise RuleError(f"award: {actor_id} is a troop — awarded only by the engine's summons (1.4.0 §2.3)")
        a = self._actor(actor_id)
        if c.state != "AVAILABLE":
            raise RuleError(f"award: case {cid} is {c.state}")
        if B > c.beta + 1e-9:
            raise RuleError(f"award: bid {B} exceeds beta {c.beta} (§5.1)")
        if a.committed is not None or a.open_review is not None:
            raise RuleError(f"award: {actor_id} already holds an assignment")
        if self.p.membership and not a.is_member:
            raise RuleError(f"award: {actor_id} is not a member of the market — suspended or on probation (1.3.0 §2.1)")
        if a.on_duty:
            raise RuleError(f"award: {actor_id} is on verification duty")
        if actor_id == c.requester:
            raise RuleError("an actor cannot be awarded its own request")
        G = max(1.0, math.ceil(self.p.G_frac * B))
        omega_base = self.p.omega_rate * B
        omega = omega_base * self.m_t                      # ω_t = ω_0 · m_t (1.2.0 §2.3)
        # 1.3.0 §2.4: Ω keeps the base; the raised part goes to the duty fund
        omega_fund = (omega - omega_base) if self.p.duty_fund else 0.0
        # --- pre-checks: no mutation until every leg is known to be fundable (atomicity)
        if self.ledger.wallet(actor_id).U + 1e-9 < G:
            raise LedgerError(f"award: {actor_id} cannot fund the guarantee {G}")
        if c.is_root:
            idx = self.ledger.index()
            D, K, GV = self.p.D * idx, self.p.K * idx, self.p.G_V * idx
            phi_E, phi_F = self.p.phi_E_root * idx, self.p.phi_F_root * idx
            need = B + phi_E + phi_F + omega
            if self.ledger.wallet(c.requester).U + 1e-9 < need:
                raise LedgerError(f"award: requester {c.requester} cannot fund {need} (B + φ^E + φ^F + ω)")
        else:
            D, K, GV, phi_E, phi_F = c.D, c.K, c.G_V, 0.0, 0.0     # frozen at posting
            if self.ledger.wallet(c.requester).U + 1e-9 < omega:
                raise LedgerError(f"award: requester {c.requester} cannot fund ω {omega}")
        # --- mutate
        c.D, c.K, c.G_V, c.phi_E, c.phi_F, c.omega, c.G = D, K, GV, phi_E, phi_F, omega, G
        c.G_award = G
        c.B, c.tau, c.actor = B, tau, actor_id
        c.t_award, c.deadline = self.t, self.t + tau
        self.ledger.lock(actor_id, G, key=f"G:{cid}", case=cid, note="guarantee")
        if c.is_root:
            self.ledger.fund_escrow(c.requester, cid, B, note="delivery price")
            self.ledger.fund_deposit(c.requester, cid, phi_E, note="expense allowance")
            if phi_F > 0:
                self.ledger.fund_fee_pot(c.requester, cid, phi_F, note="fee pot")
            if omega - omega_fund > 1e-12:
                self.ledger.transfer(c.requester, Ledger.OMEGA, omega - omega_fund, case=cid, note="service fee")
                self._fee_income(omega - omega_fund)
            if omega_fund > 1e-12:
                self.ledger.transfer(c.requester, DUTY_FUND, omega_fund, case=cid, note="duty fund")
                self.fund_in += omega_fund
            if omega > 0:
                self._service_omega_claims()
            self._freeze(c)
        else:
            A = c.requester
            self.ledger.fund_escrow(A, cid, B, from_locked=f"beta:{cid}", note="nested escrow")
            unspent = self.ledger.lock_record(A, f"beta:{cid}")
            if unspent > 1e-12:
                self.ledger.release(A, unspent, key=f"beta:{cid}", case=cid, note="unspent beta'")
            if omega - omega_fund > 1e-12:
                self.ledger.transfer(A, Ledger.OMEGA, omega - omega_fund, case=cid, note="service fee (nested)")
                self._fee_income(omega - omega_fund)
            if omega_fund > 1e-12:
                self.ledger.transfer(A, DUTY_FUND, omega_fund, case=cid, note="duty fund (nested)")
                self.fund_in += omega_fund
            if omega > 0:
                self._service_omega_claims()
        c.state = "COMMITTED"
        c.member_at_award = a.is_member
        if c.is_root:
            self.period["award_price_sum"] += B
            self.period["award_n"] += 1
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
        c.seat_since = self.t                              # the initial seat is required from now (1.4.0 §2.2)
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
        if self.is_troop(r.reviewer):            # 1.4.0: a resumed review is the same assignment — the troop resumes its seat
            self.troops[r.reviewer]["t_release"] = None
            self.history.append("troop", {"t": self.t, "troop": r.reviewer, "kind": "review", "case": c.id, "msg": "resumes"})
        c.resubmitted = True                     # a property of the submission, not of who reviews it
        c.state, c.t_submit, c.resubmit_deadline = "SUBMITTED", self.t, None
        self._log(c, f"resubmitted; {r.reviewer} resumes review {r.id} (F or N only)")

    # --------------------------------------------------------------- reviews
    def is_troop(self, wid) -> bool:
        return isinstance(wid, str) and wid in self.troops

    def _eligible(self, c: Case, reviewer: str, role: str = "initial") -> None:
        if self.is_troop(reviewer):
            raise RuleError(f"{reviewer} is a troop: seated only by summons (1.4.0 §2.2)")
        a = self._actor(reviewer)
        if not a.on_duty:
            raise RuleError(f"{reviewer} is not on verification duty")
        if reviewer in c.excluded or reviewer == c.actor or reviewer == c.requester:
            raise RuleError(f"{reviewer} is excluded from case {c.id}")
        if a.open_review is not None or a.committed is not None:
            raise RuleError(f"{reviewer} already holds an active assignment (one at a time, §2.2)")
        if self.ledger.wallet(reviewer).U + 1e-9 < c.G_V:
            raise RuleError(f"{reviewer} cannot fund the bond {c.G_V} (§7.1)")
        # 1.2.0 §2.2: eligibility is a property at assignment — duty eligibility for any review,
        # panel eligibility for a seat on an appeal, dispute or audit panel
        if not a.duty_eligible:
            raise RuleError(f"{reviewer} is not eligible for duty by its plant record (§7.1, 1.2.0)")
        if role in PANEL_ROLES and not a.panel_eligible:
            raise RuleError(f"{reviewer} may not sit on a challenge panel: plant record above θ_panel (§7.1, 1.2.0)")

    def _positions(self, c: Case) -> int:
        """Review positions on the current challenge path (§12). A withdrawn review vacates its
        position."""
        return sum(1 for rid in c.reviews if self.reviews[rid].status != "withdrawn")

    def _new_review(self, c: Case, reviewer: str, role: str) -> Review:
        self._eligible(c, reviewer, role)
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
        view = ReviewView(r.id, c.id, c.t_submit, r.deadline, r.bond, c.K,
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
        if c.plant is None:
            self.plant_credit += self.pi_t              # the plant rate: π_t plants per real initial review
            self.period["initial"] += 1
        self._log(c, f"initial review {r.id} -> {reviewer}, deadline {r.deadline}")
        return r.id

    def assign_audit(self, cid: str, reviewer: str) -> str:
        c = self._case(cid)
        if c.plant is not None:
            raise RuleError("audit: a plant is adjudicated by its known truth; no challenge is opened on it (1.2.0 §2.1)")
        if c.state != "PENDING" or c.outcome_or_verdict() != F:
            raise RuleError("audit: only an F verdict in PENDING may be audited (§8.3)")
        if self.t > c.window_end and not c.audit_vacated and not c.audit_obligation:
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
        self.period["audits"] += 1
        if c.audit_vacated:
            c.audit_vacated = False                      # the vacated obligation is taken over
        elif c.audit_obligation:
            c.audit_obligation = False                   # 1.4.0 §2.2: the rolled audit's obligation is discharged
        else:
            c.open_items += 1
        self._log(c, f"audit {r.id} -> {reviewer} (vesting suspended)")
        return r.id

    def waive_audit(self, cid: str):
        """§7.5: the orchestrator may lift a vacated audit's suspension instead of refilling it."""
        c = self._case(cid)
        if not c.audit_vacated:
            raise RuleError("waive_audit: no vacated audit position")
        if c.market_audit_only:
            raise RuleError("waive_audit: the audit of the state's own work is an obligation without exception (1.4.0 §2.3, I25)")
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
        self.period["challenge_reviews"] += 1
        self._log(c, f"appeal review {r.id} -> {reviewer}")
        return r.id

    def _reimburse(self, c: Case, r: Review):
        """§4.3 order: the root's expense allowance, then an Ω advance, then deferral to
        settlement. A nested case's draw on its root's allowance is attributed to the root (whose
        money it is) with a note I10 recognises."""
        target = min(r.cost, c.K)
        amt = target - (r.reimbursed + r.deferred)
        if amt <= 1e-12:
            return
        root = self.cases[c.root]
        pool = self.ledger.pool(root.id)
        take = min(amt, pool.deposit)
        if take > 0:
            self.ledger.pay_from_deposit(root.id, r.reviewer, take,
                                         note=f"{'nested ' if c.is_nested() else ''}reimburse {r.id}")
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
        troop = self.is_troop(r.reviewer)
        if troop and cost > 0:
            raise RuleError("a troop's cost was purchased from the fund at summons; its review reports no further cost (1.4.0 §2.1)")
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
        self.period["dur_sum"] += max(1, self.t - r.t_assign)      # mean review duration, for the reserve's sizing
        self.period["dur_n"] += 1
        if troop:
            self._release_troop(r.reviewer)
            if r.role == "initial":
                self._initial_verdict(c, verdict, None, troop_reviewer=True)
            elif r.role == "audit":
                self._audit_result(c, r)
            else:
                self._maybe_settle_challenge(c)
            return
        a = self.actors[r.reviewer]
        if r.role == "initial":
            if verdict in (F, N):
                a.open_review = None                    # a P or ⊥ keeps the reviewer attached (§6)
            if c.plant is not None:
                self._adjudicate_plant(c, r, verdict)   # 1.2.0 §2.1: by the known truth, at once
            else:
                self._initial_verdict(c, verdict, a)
        elif r.role == "audit":
            a.open_review = None
            self._audit_result(c, r)
        else:
            a.open_review = None
            self._maybe_settle_challenge(c)

    # ------------------------------------------------------- initial verdict
    def _initial_verdict(self, c: Case, verdict: str, reviewer: Optional[Actor] = None, troop_reviewer: bool = False):
        c.verdict, c.t_verdict = verdict, self.t
        if c.first_verdict_at is None and c.plant is None:
            c.first_verdict_at = self.t
            self._stop_clock(c, "the first verdict")             # 1.6.0 §2.1
        c.window_end = self.t + self.p.W
        c.initial_pinned = reviewer is not None and reviewer.pinned
        if self.is_troop(c.actor):
            # 1.4.0 §2.1: a troop accepts every verdict on its own work — recorded at the verdict, not
            # the deadline (the reviewer's note on rc.2), so the case settles and the troop is released now
            if verdict != F:
                self._release_attached_reviewer(c)
                self._finalize_N(c, reason="troop accepts the verdict on its work", actor_fault=False)
                return
            c.market_audit_only = troop_reviewer        # §2.3: only a member audits the state's own work
            if troop_reviewer:
                # odds 1 is not a roll: the engine records the obligation at the verdict (I25)
                c.audit_obligation, c.audit_rolled_at = True, self.t
                c.open_items += 1
        if verdict == F:
            c.state = "PENDING"
            if c.is_root:
                self.period["approvals"] += 1           # audit demand, for the reserve's sizing ...
                # ... on the applied odds (1.3.0 §2.3; 1.4.0 §2.3 for the state's own work)
                self.period["audit_demand"] += self.audit_odds(c.id)
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
            a = self.actors.get(r.reviewer)
            if a is not None and r.role == "initial" and r.status in ("open", "done") and a.open_review == rid:
                a.open_review = None

    # ---------------------------------------------------------- responses
    def respond(self, cid: str, action: str, d: Optional[str] = None):
        c = self._case(cid)
        if c.plant is not None:
            raise RuleError("respond: a plant has no response path; it is adjudicated by its known truth (1.2.0 §2.1)")
        if self.is_troop(c.actor):
            raise RuleError("respond: a troop accepts every verdict on its own work (1.4.0 §2.1)")
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
        c.challenge = {"kind": kind, "challenger": challenger, "reviews": [], "resolved": False, "d": d,
                       "seat_since": self.t}            # 1.4.0 §2.2: the panel seats are required from admission
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
        if c.plant is not None:
            raise RuleError("dispute: no challenge is opened on a plant (1.2.0 §2.1)")
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
        a = self.actors.get(r.reviewer)                # None for a troop: no record, no odds (1.4.0 §2.1)
        if a is not None:
            self._record_outcome(r.reviewer, False)
            if not a.pinned:                           # 1.3.0 §2.2: the §8.3 update does not run while pinned
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
        self._maybe_close_tree(self.cases[c.root])

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
        if c.is_root and c.plant is None and c.first_verdict_at is None:
            self._stop_clock(c, "a final without a verdict")       # 1.6.0 §2.1
        if forfeit_fraction >= 1.0:
            c.I_N = True
        forfeit = forfeit_fraction * c.G
        if not self._plant_notional(c):                 # 1.3.0 §2.5: a plant's guarantee binds nothing
            self.ledger.transfer_locked(c.actor, c.requester, forfeit, key=f"G:{c.id}", case=c.id, note=f"forfeit: {reason}")
            if c.G - forfeit > 1e-12:
                self.ledger.release(c.actor, c.G - forfeit, key=f"G:{c.id}", case=c.id, note="guarantee remainder")
        if actor_fault and c.actor in self.actors:          # the plant actor is Ω's and keeps no record
            self._record_outcome(c.actor, False)
        self._return_escrow(c)
        if any(self.reviews[r].status == "done" for r in c.reviews):
            c.needs_review_settlement = True            # fee entitlements need the tick's emission batch
        else:
            self._settle_reviews(c, 0.0)                # debts settle at once; the pots return at tree closure
        if c.is_nested() and c.rejection_bond > 0:
            self.ledger.release(c.requester, c.rejection_bond, key=f"rej:{c.id}", case=c.id, note="rejection stood")
            c.rejection_bond = 0.0
        self._release_attached_reviewer(c)
        self._terminal_cleanup(c)
        c.state, c.final = "FINAL_N", True
        c.grade = self._grade(c)
        self._release_capacity(c)
        if self.is_troop(c.actor):
            self._release_troop(c.actor)
        self._log(c, f"final N: {reason}")
        self._maybe_close_tree(self.cases[c.root])     # final now; a settlement still pending defers this

    def _return_escrow(self, c: Case):
        """The delivery price goes back to the requester on final N. The deposit does not go
        back here: settlement pays expense debts from the allowance first, and the pots return
        only when the tree has closed (§4.3 step 3)."""
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
        if c.plant is not None:
            raise RuleError("override: no ruling is sought on a plant; its truth is known by construction (1.2.0 §2.1)")
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
        if c.audit_obligation:                          # 1.4.0: the ruling supersedes the rolled audit's obligation (I18)
            c.audit_obligation = False
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
        if c.plant is not None:
            raise RuleError("accept_explicit: a plant's outcome is set only by its known truth (1.2.0 §2.1)")
        if requester != c.requester or c.state != "PENDING" or c.outcome_or_verdict() != F:
            raise RuleError("accept_explicit: not a pending F for this requester")
        c.assessments.append((self.t, requester, F, "accept"))
        self._log(c, f"{requester} explicitly accepts")

    # ----------------------------------------------------------- labelling
    def _grade(self, c: Case) -> str:
        """§15.3: the grade is that of the event that *established* the settled outcome, by the
        author of that event — a human who rules on a delegate's request establishes a
        human-explicit outcome; a delegate who accepts establishes a delegate-explicit one."""
        if c.plant is not None:
            return PLANT                                    # truth known by construction, never promoted (1.2.0)
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
    def _settle_reviews(self, c: Case, emission_per_weight: float, uplift_per_weight: float = 0.0):
        """§4.3 (1.1.0) settlement, one rule. The root's two pots serve every case in its tree.
        1. Expense debts, for every review of the case, from what remains of the root's expense
           allowance only: deferred reimbursements, then Ω's advances. What it cannot cover becomes
           a named reviewer claim on Ω, or stays an unrecovered advance borne by Ω.
        2. Fees, survivors only: each is owed its fixed fee w_r·f from the root's fee pot — scaled
           pro rata only when what is left of the pot cannot pay this case's fees in full — plus its
           emission share, minted into this case's pool and paid in full.
        3. Tree closure (`_maybe_close_tree`): when every case in the tree has settled."""
        root = self.cases[c.root]
        rpool = self.ledger.pool(root.id)
        nested = "nested " if c.is_nested() else ""
        surviving = [self.reviews[r] for r in c.reviews if self.reviews[r].status == "done"]
        for r in surviving:
            e = 0.0 if self.is_troop(r.reviewer) else self._w(r.role) * emission_per_weight   # a troop claims no emission (1.4.0)
            if e > 0:
                self.ledger.mint_emission_to_pool(c.id, e)
            r.fee = e
            r.fee_owed = self._w(r.role) * self.p.f_fee
        # 1. expense debts, every review — an overturned reviewer's bond was the penalty; its cost survives
        for rid in c.reviews:
            r = self.reviews[rid]
            if r.deferred > 1e-12:
                pay = min(r.deferred, rpool.deposit)
                if pay > 1e-12:
                    self.ledger.pay_from_deposit(root.id, r.reviewer, pay, note=f"{nested}deferred reimbursement")
                    r.deferred -= pay
                    r.reimbursed += pay
                if r.deferred > 1e-12:
                    self.omega_claims.append(Claim(r.reviewer, r.deferred, r.id))
                    r.reimbursed_pending += r.deferred
                    r.deferred = 0.0
        if c.omega_advance > 1e-12:
            pay = min(c.omega_advance, rpool.deposit)
            if pay > 1e-12:
                self.ledger.pay_from_deposit(root.id, Ledger.OMEGA, pay, note=f"{nested}Ω advance repaid")
                c.omega_advance -= pay
        # 2. fees, survivors only: the fixed fee from the root's pot, the emission share in full
        if surviving:
            owed = sum(r.fee_owed for r in surviving)
            scale = min(1.0, rpool.fee_pot / owed) if owed > 1e-12 else 0.0
            for r in surviving:
                fixed = r.fee_owed * scale
                if fixed > 1e-12:
                    self.ledger.pay_from_fee_pot(root.id, r.reviewer, fixed, note=f"{nested}review fee")
                    root.fees_from_pot += fixed
                r.fee_fixed = fixed
                if r.fee > 1e-12:
                    self.ledger.pay_emission(c.id, r.reviewer, r.fee, note="emission share")
                r.fee += fixed
                # 1.3.0 §2.4: the duty fund's uplift, by role weight, like emission — real money, so it carries;
                # a troop claims none (1.4.0 §2.1)
                uplift = 0.0 if self.is_troop(r.reviewer) else min(self._w(r.role) * uplift_per_weight, self.ledger.wallet(DUTY_FUND).U)
                if uplift > 1e-12:
                    self.ledger.transfer(DUTY_FUND, r.reviewer, uplift, case=c.id, note="duty uplift")
                    r.uplift = uplift
                    r.fee += uplift
                    self.fund_out += uplift
                self.ledger.release(r.reviewer, r.bond, key=f"bond:{r.id}", case=c.id, note="bond released")
                r.status = "vested"
                if self.is_troop(r.reviewer):
                    continue                            # no reliability, duty credit or odds for a troop
                a = self.actors[r.reviewer]
                self._record_outcome(r.reviewer, True)
                a.vests.append(self.t)
                horizon = self.t - self.p.kappa_window     # a vest this old can never count again
                while a.vests and a.vests[0] <= horizon:
                    a.vests.pop(0)
                a.streak += 1
                if a.on_duty:
                    a.duty_reviews += 1
                if a.streak % self.p.p_halve_every == 0 and not a.pinned:   # pinned odds do not taper (1.3.0 §2.2)
                    a.p_audit = max(self.p.p_floor, a.p_audit / 2)
            left = self.ledger.pool(c.id).minted
            if left > 1e-9:                            # rounding residue of minted emission only
                self.ledger.pay_emission(c.id, Ledger.OMEGA, left, note="pool sweep")
        c.needs_review_settlement = False
        self._service_omega_claims()
        if c.is_nested():
            self._touch(root)
        self._maybe_close_tree(root)

    # ------------------------------------------------------------ the tree
    def _tree(self, root: Case):
        """Every case under a root, the root first, in creation order of posting."""
        out, stack = [], [root]
        while stack:
            c = stack.pop(0)
            out.append(c)
            stack.extend(self.cases[ch] for ch in c.children)
        return out

    def _maybe_close_tree(self, root: Case):
        """§4.3 step 3 / §2.4 of design revision 1: when the root and every nested case under it
        have settled, what remains of the fee pot settles the tree's own expense debts — first
        the tree's outstanding reviewer claims, paid to the claimants and retired from Ω's queue;
        then the tree's unrecovered advances, repaid to Ω — and only then do both pots' remainders
        return to the root requester as unused. The one movement of fee money toward expenses."""
        if root.tree_closed or not root.is_root or root.t_award is None:
            return
        tree = self._tree(root)
        if any(not c.final or c.needs_review_settlement for c in tree):
            return
        pool = self.ledger.pool(root.id)
        ids = {c.id for c in tree}
        if pool.fee_pot > 1e-12 and self.omega_claims:
            kept = []
            for cl in self.omega_claims:
                r = self.reviews[cl.review]
                if r.case in ids and pool.fee_pot > 1e-12:
                    pay = min(cl.amount, pool.fee_pot)
                    self.ledger.pay_from_fee_pot(root.id, cl.reviewer, pay, note=f"tree closure: Ω claim {cl.review} paid from the fee pot")
                    r.reimbursed += pay
                    r.reimbursed_pending -= pay
                    root.expenses_from_pot += pay
                    if cl.amount - pay > 1e-12:
                        kept.append(Claim(cl.reviewer, cl.amount - pay, cl.review))
                else:
                    kept.append(cl)
            self.omega_claims = kept
        for c in tree:
            if c.omega_advance > 1e-12 and pool.fee_pot > 1e-12:
                pay = min(c.omega_advance, pool.fee_pot)
                self.ledger.pay_from_fee_pot(root.id, Ledger.OMEGA, pay, note="tree closure: Ω advance repaid from the fee pot")
                c.omega_advance -= pay
                root.expenses_from_pot += pay
        back_E, back_F = pool.deposit, pool.fee_pot
        if back_E > 1e-12:
            self.ledger.pay_from_deposit(root.id, root.requester, back_E, note="tree closure: unused allowance returned")
            root.allowance_refunded += back_E
        if back_F > 1e-12:
            self.ledger.pay_from_fee_pot(root.id, root.requester, back_F, note="tree closure: unused fee pot returned")
            root.pot_refunded += back_F
        root.tree_closed, root.t_closed = True, self.t
        self._log(root, f"tree closed; unused allowance {back_E:g} and fee pot {back_F:g} returned")
        if root.plant is not None:
            # 1.2.0 Appendix A: the two system wallets hold Ω's money; what a closed plant left in
            # them — the price, the refunds, the released or forfeited guarantee — goes back to Ω
            for wid in (PLANT_REQ, PLANT_ACT):
                u = self.ledger.wallet(wid).U
                if u > 1e-12:
                    self.ledger.transfer(wid, Ledger.OMEGA, u, case=root.id, note="tree closure: plant funds swept to Ω")
                    self.period["plant_back"] += u
        self._service_omega_claims()

    def _plant_notional(self, c: Case) -> bool:
        """1.3.0 §2.5: a plant's award and guarantee are Ω paying itself and tie up no balance."""
        return c.plant is not None and self.p.net_plant_capital

    def _vest(self, c: Case, epw: float, upw: float = 0.0):
        if c.is_root and c.plant is None and c.clock_stopped_at is None:
            self._stop_clock(c, "a final without a verdict")      # 1.6.0 §2.1: a human's override vests with no initial verdict
        if not self._plant_notional(c):                 # a plant's price and guarantee are notional (1.3.0 §2.5)
            self.ledger.pay_from_escrow(c.id, c.actor, c.B, note="delivery price")
            self.ledger.release(c.actor, c.G, key=f"G:{c.id}", case=c.id, note="guarantee released")
        if c.is_nested():
            self.cases[c.parent].actor_cost += c.B          # §4.6: nested payments are execution cost
            self._touch(self.cases[c.parent])
        self._settle_reviews(c, epw, upw)
        c.outcome = c.outcome or F
        c.t_vest, c.final, c.state = self.t, True, "VESTED"
        c.grade = self._grade(c)
        if c.actor in self.actors:                          # the plant actor is Ω's and keeps no record
            self._record_outcome(c.actor, True)
        if self.is_troop(c.actor):
            self._release_troop(c.actor)
        self._log(c, f"vested; grade {c.grade}")
        self._maybe_close_tree(self.cases[c.root])     # final now: the tree may have closed with this vest

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
                          for c in batch for rid in c.reviews
                          if self.reviews[rid].status == "done" and not self.is_troop(self.reviews[rid].reviewer))
            E = self.p.emission(tick)
            epw = (E / total_w) if total_w > 0 else 0.0
            self._repay_advance()                               # 1.4.0 §2.4: the advance is repaid before any uplift
            fund_u = self.ledger.wallet(DUTY_FUND).U
            if not self.p.duty_fund:
                avail = 0.0
            elif self.p.troop_account:
                avail = fund_u                                  # 1.7.0 §2.1: the uplift fund pays its whole balance (1.3.0)
            else:
                avail = max(0.0, fund_u - self.R_T)             # the merged fund: uplift only above the troops' reserve
            upw = (avail / total_w) if total_w > 0 else 0.0
            paid_before = self.fund_out
            for c in vesting:
                self._vest(c, epw, upw)
            for c in settling:
                if c.needs_review_settlement:
                    self._settle_reviews(c, epw, upw)
            if self.fund_out - paid_before > avail + 1e-6:          # I23: uplift only from above the reserve
                self._uplift_violation = f"uplift {self.fund_out - paid_before} paid from a fund of {fund_u} with reserve {self.R_T}"
            self._repay_advance()                               # the batch's inflows (fees, released locks) repay Ω first
            self._pay_troop_surplus()                           # 1.7.0 §2.1: the troop account's unlocked balance above R_T is Ω's
        # step 4: Ω services claims
        self._service_omega_claims()
        # step 5: the dial, once per period (1.2.0 §2.3), then rotation under the reserve it sized
        self._maybe_end_period(tick)
        self._rotate(tick)
        self._summon_troops(tick)                              # 1.4.0 §2.2–2.3: after the market has had its chance

    def _withdraw_review(self, r: Review, burn: bool = True):
        """Timeout (burn=True): half the bond burns, the reviewer is at fault, and the position
        is vacated but the case's obligation stands — a vacated audit keeps the case suspended
        until refilled or waived (§7.5). Voiding (burn=False): a human ruling mooted the
        assignment; the bond returns whole, no fault, and the obligation ends with it."""
        c = self.cases[r.case]
        r.status = "withdrawn"
        a = self.actors.get(r.reviewer)                # None for a troop
        if burn:
            half = r.bond / 2
            self.ledger.burn_locked(r.reviewer, half, key=f"bond:{r.id}", case=c.id, note="timeout: half burned")
            self.ledger.release(r.reviewer, r.bond - half, key=f"bond:{r.id}", case=c.id, note="timeout: half released")
            if a is not None:
                self._record_outcome(r.reviewer, False)
        else:
            self.ledger.release(r.reviewer, r.bond, key=f"bond:{r.id}", case=c.id, note="assignment voided")
        if a is not None and a.open_review == r.id:
            a.open_review = None
        if a is None:
            self._release_troop(r.reviewer)
        if r.role == "initial":
            c.seat_since = self.t                        # the initial seat is required again (1.4.0 §2.2)
        if c.challenge and r.id in c.challenge["reviews"]:
            c.challenge["reviews"].remove(r.id)        # the appeal position is vacated
            c.challenge["seat_since"] = self.t
        if r.role == "audit" and not r.is_audit_as_appeal:
            if burn:
                c.audit_vacated = True                   # obligation stands; replacement admissible after the window
                c.audit_vacated_at = self.t
            elif c.open_items > 0:
                c.open_items -= 1                        # ruling supersedes the audit
        self._log(c, f"review {r.id} by {r.reviewer} {'timed out' if burn else 'voided'}; position vacated")

    def _rotate(self, tick: int):
        """§12: replacement-before-release; a turn is duty_turn_reviews vested reviews or
        duty_turn_ticks ticks; incoming replacements are the free, eligible actors with the lowest κ.
        Since 1.2.0 (§2.2, §2.3): a suspension that has run its course is re-checked against the
        record; a duty-ineligible actor leaves when its active review is complete, replacement or
        not; the reserve is then filled up to X_t from the eligible pool or shrunk to it, and the
        gap, when no eligible actor is left, is the eligibility shortfall."""
        GV = self.p.G_V * self.ledger.index()
        self._x_target = self._reserve_target()        # 1.6.0 §2.3: at least the reviews waiting
        # 0. suspensions that have run their course. The record persists; a passing record is
        # readmitted clean. A record that still fails cannot change while the actor is off duty (it
        # is a trailing window of plant outcomes, and a suspended actor judges no plants), so the
        # actor is readmitted on probation: to duty, not to panels, until its next plant
        # adjudication re-checks the record — a still-failing record suspends it again at once.
        # [Implementer's reading of 1.2.0 §2.2, October 17, 2026; confirmed as the rule by patch 1.2.1 (§11.2).]
        for a in sorted(self.actors.values(), key=lambda a: a.id):
            if a.suspended_until is not None and tick >= a.suspended_until:
                a.suspended_until = None
                a.p_audit, a.streak = self.p.p_start, 0              # a newcomer for the audit odds (§2.4)
                if self.p.membership:
                    # 1.3.0 §2.2: the way back is probation — initial reviews only, odds pinned, no awards —
                    # until the trailing record passes with n_min new outcomes judged
                    a.probation, a.since_susp = True, 0
                    self.history.append("suspension", {"t": tick, "actor": a.id, "msg": "probation begins"})
                elif a.record_passes(self.p.theta_duty):
                    self.history.append("suspension", {"t": tick, "actor": a.id, "msg": "readmitted: record passes"})
                else:
                    a.probation = True
                    self.history.append("suspension", {"t": tick, "actor": a.id,
                                                       "msg": "readmitted on probation: record still fails; "
                                                              "re-checked at its next plant"})
        # 1. ineligible duty actors with no active review leave now, whether or not a replacement exists
        for a in sorted((a for a in self.actors.values() if a.on_duty), key=lambda a: a.id):
            if not a.duty_eligible and a.open_review is None:
                self._leave_duty(a, tick, "ineligible by plant record")
        # batch-start snapshot: only actors off duty when the tick began may be conscripted this
        # tick, so a released actor has at least one tick of ordinary eligibility (§12)
        pool = {a.id for a in self.actors.values()
                if not a.on_duty and a.committed is None and a.open_review is None and a.duty_eligible
                and self.ledger.wallet(a.id).U + 1e-9 >= GV}
        if self.p.membership:
            self._rotate_membership(tick, pool)
            return
        # 2. turns: replacement before release
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
        # 3. the reserve holds min(X_t, eligible): fill up to X_t (or the queue's target, 1.6.0 §2.3) ...
        X = self._x_target
        n = sum(1 for a in self.actors.values() if a.on_duty)
        while n < X and pool:
            inc = min((self.actors[i] for i in pool), key=lambda a: (a.kappa, a.id))
            pool.discard(inc.id)
            inc.on_duty, inc.duty_since, inc.duty_reviews = True, tick, 0
            self.history.append("rotation", {"t": tick, "in": inc.id, "out": None, "why": "reserve sized up"})
            n += 1
        # ... or shrink to it: idle, non-volunteer duty actors, those whose turn is done first
        if n > X:
            idle = [a for a in self.actors.values() if a.on_duty and not a.volunteer and a.open_review is None]
            idle.sort(key=lambda a: (0 if (a.duty_since is not None and (a.duty_reviews >= self.p.duty_turn_reviews
                                           or tick - a.duty_since >= self.p.duty_turn_ticks)) else 1, a.id))
            for a in idle[: n - X]:
                self._leave_duty(a, tick, "reserve sized down")
                n -= 1
        self.reserve_shortfall_now = max(0, X - n)
        self._pool_exhausted = not pool
        self._reserve_dirty = False
        if self.reserve_shortfall_now:
            self.eligibility_shortfall += self.reserve_shortfall_now
            self.period["eligibility_shortfall"] += self.reserve_shortfall_now

    # ------------------------------------------------ 1.6.0: the queue, Ω's order, the service clock
    def _waiting_reviews(self) -> tuple:
        """The reviews waiting for a reviewer, by kind (1.6.0 §2.3): root submissions without an open initial review;
        rolled or vacated audits without an open audit, and challenge seats not yet filled (panel seats)."""
        initial = panel = 0
        for c in self._live_cases.values():
            if c.final:
                continue
            if c.state == "SUBMITTED" and c.is_root and not any(self.reviews[r].role == "initial" and self.reviews[r].status == "open"
                                                                for r in c.reviews):
                initial += 1
            if c.state == "PENDING" and (c.audit_obligation or c.audit_vacated) \
                    and not any(self.reviews[r].role == "audit" and self.reviews[r].status == "open" for r in c.reviews):
                panel += 1
            ch = c.challenge
            if ch and not ch["resolved"] and len(ch["reviews"]) < 2:
                panel += 2 - len(ch["reviews"])
        return initial, panel

    def _reserve_target(self) -> int:
        """1.6.0 §2.3: the reserve is at least the reviews waiting plus the period's initial-review rate, never less than
        the period's sizing X_t; taken at every rotation."""
        self._waiting_initial, self._waiting_panel = self._waiting_reviews()
        if not self.p.seat_the_queue:
            return self.X_t
        elapsed = max(1, self.t - self.period["start"])
        rate = max(self.period["initial"] / elapsed, self._last_initial_rate)
        return max(self.X_t, self._waiting_initial + self._waiting_panel + int(math.ceil(rate - 1e-9)))

    def _plant_reserve(self) -> float:
        """1.6.0 §2.2: the capital the honesty clock will need for the rest of the period — the period's plant rate so far
        (π_t × the initial-review rate, floored at the previous period's) × (φ^E + φ^F) × the ticks remaining — held back
        from Ω's advances and from rebate liabilities."""
        if not (self.p.omega_backs_fund or self.p.service_clock) or not self.p.dial or self.pi_t <= 0:
            return 0.0
        elapsed = max(1, self.t - self.period["start"])
        rate = max(self.period["initial"] / elapsed, self._last_initial_rate)
        remaining = max(0, self.p.period_ticks - elapsed)
        horizon = min(remaining, self.p.plant_reserve_life) if self.p.plant_reserve_life > 0 else remaining
        return self.pi_t * rate * (self.p.phi_E_root + self.p.phi_F_root) * self.ledger.index() * horizon

    def _omega_available(self) -> float:
        """What Ω may advance now: its unlocked balance above the plant reserve (1.6.0 §2.2), or under 1.5.0 the room left
        under A_T."""
        om = self.ledger.wallet(Ledger.OMEGA).U
        if self.p.omega_backs_fund:
            return max(0.0, om - self._plant_reserve())
        return max(0.0, min(self.p.A_T - self.advance_outstanding, om))

    def _service_omega_liabilities(self, min_age: int):
        """1.6.0 §2.2: Ω pays its rebate liabilities of at least `min_age` ticks, oldest first, from its balance above the
        plant reserve."""
        if not self.omega_liabilities:
            return
        keep = []
        for l in self.omega_liabilities:
            avail = max(0.0, self.ledger.wallet(Ledger.OMEGA).U - self._plant_reserve())
            if self.t - l["t"] >= min_age and avail > 1e-12:
                pay = min(l["amount"], avail)
                self.ledger.transfer(Ledger.OMEGA, l["requester"], pay, case=l["case"], note="rebate (Ω liability serviced)")
                self.liabilities_paid += pay
                self.period["liabilities_paid"] += pay
                c = self.cases[l["case"]]
                c.rebate_paid += pay
                if l["amount"] - pay > 1e-12:
                    keep.append({**l, "amount": l["amount"] - pay})
            else:
                keep.append(l)
        self.omega_liabilities = keep

    def _clock_runs(self, c: Case) -> bool:
        """1.6.0 §2.1: a root request's clock runs from posting to its first verdict while its ceiling admits the market
        price; never a plant's, never a nested case's."""
        if not self.p.service_clock or not c.is_root or c.plant is not None or c.final or c.clock_stopped_at is not None:
            return False
        if c.state == "AVAILABLE":
            B = self.mean_awarded_price() or c.beta
            return c.beta + 1e-9 >= B
        return True

    def _stop_clock(self, c: Case, reason: str):
        """1.6.0 §2.1: the clock stops at the first verdict or at a final without one; the lateness past T_s owes the
        requester r_s a tick, capped at B, paid from Ω above the plant reserve or carried as Ω's liability."""
        if not self.p.service_clock or not c.is_root or c.plant is not None or c.clock_stopped_at is not None:
            return
        c.clock_stopped_at = self.t
        c.late_ticks = max(0, c.clock_ticks - self.p.T_s)
        if c.late_ticks:
            self.late_n += 1
            self.lateness_sum += c.late_ticks
            self.period["late"] += 1
            self.period["lateness_sum"] += c.late_ticks
        else:
            self.on_time_n += 1
            self.period["on_time"] += 1
        B = c.B if c.B else 0.0
        r_s = self.p.r_s if self.p.r_s > 0 else self.p.omega_rate * B
        owed = min(r_s * c.late_ticks, B) if B > 0 else 0.0
        c.rebate_owed = owed
        self.rebates_owed += owed
        if owed <= 1e-12:
            self._log(c, f"clock stopped at {reason}: {c.clock_ticks} ticks, on time" if not c.late_ticks
                      else f"clock stopped at {reason}: {c.clock_ticks} ticks, {c.late_ticks} late, nothing owed")
            return
        avail = max(0.0, self.ledger.wallet(Ledger.OMEGA).U - self._plant_reserve())
        pay = min(owed, avail)
        if pay > 1e-12:
            self.ledger.transfer(Ledger.OMEGA, c.requester, pay, case=c.id, note="rebate")
            c.rebate_paid += pay
            self.rebates_paid += pay
            self.period["rebates_paid"] += pay
        if owed - pay > 1e-12:
            self.omega_liabilities.append({"requester": c.requester, "amount": owed - pay, "t": self.t, "case": c.id})
            self.liabilities_accrued += owed - pay
            self.period["liabilities_accrued"] += owed - pay
        self._log(c, f"clock stopped at {reason}: {c.clock_ticks} ticks, {c.late_ticks} late; rebate {owed:g} "
                     f"(paid {pay:g}, Ω's liability {owed - pay:g})")

    def open_late(self) -> int:
        """Requests whose clock is running past T_s (1.6.0 §2.1 reading)."""
        return sum(1 for c in self._live_cases.values() if self._clock_runs(c) and c.clock_ticks > self.p.T_s)

    def _member_cap(self, E_t: int) -> int:
        """1.3.0 §2.3: at most ⌈E_t/2⌉ members on duty — and never a cap below the reserve's own floor
        V_max + 1, so that a small membership can still seat the reserve the baseline requires.
        [Implementer's reading, October 17, 2026: read literally, ⌈E_t/2⌉ at six actors is 3, below the
        X₀ = 4 of Appendix A's initialization and §20's worked example (C, D, E, F on duty), which would
        make the baseline's own worlds — and every reviewer test built on them — violate the revision at
        tick 0. The cap yields to the reserve floor as the panel floor yields to the cap. Flagged in the
        consolidated text and HANDOFF; confirmed as the rule by patch 1.3.1.]"""
        return max(int(math.ceil(self.p.duty_cap_frac * E_t - 1e-9)), self.p.V_max + 1)

    def _turn_done(self, a: Actor, tick: int) -> bool:
        return a.duty_since is not None and (a.duty_reviews >= self.p.duty_turn_reviews
                                             or tick - a.duty_since >= self.p.duty_turn_ticks)

    def _seat(self, a: Actor, tick: int, why: str, out: Optional[Actor] = None):
        a.on_duty, a.duty_since, a.duty_reviews = True, tick, 0
        if out is not None:
            out.on_duty, out.duty_since, out.duty_reviews = False, None, 0
        self.history.append("rotation", {"t": tick, "in": a.id, "out": out.id if out else None, "why": why})

    def _rotate_membership(self, tick: int, pool: set):
        """1.3.0 §2.3: two kinds of seat. Members hold the seats only members may hold — the period's
        audit and challenge demand, never fewer than min(V_max − 1, E_t) when that many free, fundable
        members exist — and no member is seated while on-duty members number ⌈E_t/2⌉ or more; a member
        above the cap leaves at the completion of its active review. Probationers fill the initial-review
        seats, lowest duty credit first; members take what initial demand is left while below the cap.
        Turns are refilled by the kind of seat vacated. The remaining gap is the eligibility shortfall."""
        members_pool = {i for i in pool if self.actors[i].is_member}
        probs_pool = {i for i in pool if self.actors[i].probation}
        E_t = sum(1 for a in self.actors.values() if a.is_member and a.record_passes(self.p.theta_duty))
        cap = self._member_cap(E_t)
        floor = min(self.p.V_max - 1, E_t)
        on_m = lambda: [a for a in self.actors.values() if a.on_duty and a.is_member]
        on_p = lambda: [a for a in self.actors.values() if a.on_duty and a.probation]
        lowest = lambda ids: min((self.actors[i] for i in ids), key=lambda a: (a.kappa, a.id))
        # the seats only members may hold: the sized demand within the cap, never below the floor — and since
        # 1.6.0 §2.3 at least the panel seats waiting, within the cap
        X = self._x_target
        seats_m = max(self.member_seats, self._waiting_panel) if self.p.seat_the_queue else self.member_seats
        target_m = max(min(seats_m, cap), floor)
        # members above the cap leave as their reviews complete (idle ones now), down to max(cap, floor)
        idle_m = sorted((a for a in on_m() if a.open_review is None and not a.volunteer),
                        key=lambda a: (0 if self._turn_done(a, tick) else 1, a.id))
        while len(on_m()) > max(cap, floor) and idle_m:
            self._leave_duty(idle_m.pop(0), tick, "above the members' duty cap")
        # probationers first for the initial seats: an idle member holding one makes room (1.3.0 §2.3)
        idle_m = sorted((a for a in on_m() if a.open_review is None and not a.volunteer),
                        key=lambda a: (0 if self._turn_done(a, tick) else 1, a.id))   # recomputed: turns moved people
        while probs_pool and len(on_m()) > target_m and idle_m:
            out = idle_m.pop(0)
            inc = lowest(probs_pool)
            probs_pool.discard(inc.id)
            self._seat(inc, tick, "initial seat to a probationer", out)
        # turns: replacement before release, by the kind of seat vacated — a member holding an
        # initial seat (beyond the member seats) is replaced by a probationer first
        for out in sorted((a for a in self.actors.values() if a.on_duty), key=lambda a: a.id):
            if out.volunteer or out.open_review is not None or not self._turn_done(out, tick):
                continue
            if out.is_member:
                if len(on_m()) > target_m and probs_pool:
                    inc = lowest(probs_pool)
                    probs_pool.discard(inc.id)
                    self._seat(inc, tick, "turn: initial seat to a probationer", out)
                elif members_pool:
                    inc = lowest(members_pool)
                    members_pool.discard(inc.id)
                    self._seat(inc, tick, "turn: member seat", out)
            else:
                # a probationer's seat goes to a free probationer; with none free the outgoing one stays —
                # "probationers first" would otherwise seat a member and displace it back next tick
                if probs_pool:
                    inc = lowest(probs_pool)
                    probs_pool.discard(inc.id)
                    self._seat(inc, tick, "turn: initial seat", out)
        # member seats
        while len(on_m()) < target_m and members_pool:
            inc = lowest(members_pool)
            members_pool.discard(inc.id)
            self._seat(inc, tick, "member seat")
        # initial seats: probationers first, lowest duty credit — all of them if the queue needs them (1.6.0 §2.3)
        while len(on_m()) + len(on_p()) < X and probs_pool:
            inc = lowest(probs_pool)
            probs_pool.discard(inc.id)
            self._seat(inc, tick, "initial seat: probationer")
        # then members for what initial demand is left, while below the cap
        while len(on_m()) + len(on_p()) < X and len(on_m()) < cap and members_pool:
            inc = lowest(members_pool)
            members_pool.discard(inc.id)
            self._seat(inc, tick, "initial seat: member")
        # shrink to the target: idle probationers first, then idle members above the member seats and the floor
        n = len(on_m()) + len(on_p())
        if n > X:
            idle_p = sorted((a for a in on_p() if a.open_review is None), key=lambda a: (0 if self._turn_done(a, tick) else 1, a.id))
            while n > X and idle_p:
                self._leave_duty(idle_p.pop(0), tick, "reserve sized down")
                n -= 1
            idle_m = sorted((a for a in on_m() if a.open_review is None and not a.volunteer),
                            key=lambda a: (0 if self._turn_done(a, tick) else 1, a.id))
            while n > X and len(on_m()) > max(target_m, floor) and idle_m:
                self._leave_duty(idle_m.pop(0), tick, "reserve sized down")
                n -= 1
        n = len(on_m()) + len(on_p())
        self.reserve_shortfall_now = max(0, X - n)
        self._member_pool_exhausted = not members_pool
        self._pool_exhausted = (not probs_pool) and (not members_pool or len(on_m()) >= cap)
        self._reserve_dirty = False
        if self.reserve_shortfall_now:
            self.eligibility_shortfall += self.reserve_shortfall_now
            self.period["eligibility_shortfall"] += self.reserve_shortfall_now

    def _leave_duty(self, a: Actor, tick: int, why: str):
        a.on_duty, a.duty_since, a.duty_reviews = False, None, 0
        self._reserve_dirty = True                      # the tick's rotation refills or counts the gap
        self.history.append("rotation", {"t": tick, "in": None, "out": a.id, "why": why})

    def volunteer(self, aid: str, flag: bool = True):
        self._actor(aid).volunteer = flag
        self.history.append("actor", {"t": self.t, "actor": aid, "msg": f"volunteer={flag}"})

    # --------------------------------------------- planted work (1.2.0 §2.1, §2.2)
    def create_plant(self, truth: bool, B: float) -> str:
        """The orchestrator introduces a case whose fulfillment it knows by construction: `truth`
        True is a good plant (fulfilled), False a bad one. The case is created in the submitted
        state, attributed to the orchestrator's plant requester and plant actor, funded by Ω — the
        price, both pots and the actor's guarantee — and assigned an initial reviewer like any case.
        The marker is committed to the History sealed (a hash of the case, its truth and a nonce)
        and revealed at adjudication. Refused whole when Ω cannot fund it; what the rate called for
        and could not be funded is the period's plant shortfall (§2.3)."""
        if not isinstance(truth, bool):
            raise RuleError("create_plant: truth is True (good) or False (bad)")
        B = amount(B, "B")
        idx = self.ledger.index()
        D, K, GV = self.p.D * idx, self.p.K * idx, self.p.G_V * idx
        phi_E, phi_F = self.p.phi_E_root * idx, self.p.phi_F_root * idx
        G = max(1.0, math.ceil(self.p.G_frac * B))
        netted = self.p.net_plant_capital                   # 1.3.0 §2.5: award and guarantee are Ω paying itself
        need = (phi_E + phi_F) if netted else (B + phi_E + phi_F + G)
        if self.ledger.wallet(Ledger.OMEGA).U + 1e-9 < need:
            what = "φ^E + φ^F" if netted else "B + φ^E + φ^F + G"
            raise LedgerError(f"create_plant: Ω cannot fund {need} ({what}) from its unlocked balance")
        self._n_case += 1
        cid = f"q{self._n_case}"
        c = Case(cid, root=cid, requester=PLANT_REQ, is_root=True, beta=B, t_post=self.t)
        c.plant = truth
        c.plant_nonce = hashlib.sha256(f"{self.history.head}|{cid}".encode()).hexdigest()[:16]
        c.plant_commit = hashlib.sha256(f"{cid}|{'good' if truth else 'bad'}|{c.plant_nonce}".encode()).hexdigest()
        self.cases[cid] = c
        self._live_cases[cid] = c
        # Ω funds its two system wallets; the plant is then awarded and submitted at once
        self.ledger.transfer(Ledger.OMEGA, PLANT_REQ, need if netted else B + phi_E + phi_F, case=cid,
                             note="plant: requester funded by Ω")
        self.period["plant_out"] += need if netted else B + phi_E + phi_F
        if not netted:
            self.ledger.transfer(Ledger.OMEGA, PLANT_ACT, G, case=cid, note="plant: actor funded by Ω")
            self.period["plant_out"] += G
        c.D, c.K, c.G_V, c.phi_E, c.phi_F, c.omega, c.G = D, K, GV, phi_E, phi_F, 0.0, G
        c.G_award = G
        c.B, c.tau, c.actor = B, 1, PLANT_ACT
        c.t_award, c.deadline = self.t, self.t + 1
        if not netted:                                      # netted: the price and guarantee are notional terms
            self.ledger.lock(PLANT_ACT, G, key=f"G:{cid}", case=cid, note="guarantee")
            self.ledger.fund_escrow(PLANT_REQ, cid, B, note="delivery price")
        self.ledger.fund_deposit(PLANT_REQ, cid, phi_E, note="expense allowance")
        if phi_F > 0:
            self.ledger.fund_fee_pot(PLANT_REQ, cid, phi_F, note="fee pot")
        self._freeze(c)
        c.state, c.t_submit = "SUBMITTED", self.t
        self.history.append("plant_created", {"t": self.t, "case": cid, "commit": c.plant_commit})
        c.plant_hseq = len(self.history.entries) - 1
        self._log(c, f"plant created and submitted (B={B}); marker sealed")
        self.plant_credit -= 1.0
        self.plants_created += 1
        self.period["plants_created"] += 1
        return cid

    def plants_due(self) -> int:
        """How many plants the rate calls for that have not been created (whole plants)."""
        return int(math.floor(self.plant_credit + 1e-9)) if self.plant_credit > 0 else 0

    def _adjudicate_plant(self, c: Case, r: Review, verdict: str):
        """1.2.0 §2.1: a plant's initial verdict is judged against its known truth the moment it
        is given. Right → stood (paid at settlement, plant record +1). Wrong → plant failure: the
        bond is forfeited whole and burned, no fee, expenses already reimbursed, reliability down,
        audit odds doubled, plant record −1. P or ⊥ → spent: no plant outcome. The marker is
        revealed; the plant then settles by its truth — a good plant runs its window and vests, a
        bad one is final N — and its pots return to Ω at closure."""
        a = self.actors[r.reviewer]
        truth = c.plant
        c.verdict, c.t_verdict = verdict, self.t
        c.window_end = self.t + self.p.W
        if verdict in (P, BOT):
            c.plant_outcome = "spent"
            a.open_review = None                        # the plant actor never responds
            self._reveal_plant(c, r, "spent")
            self._finalize_N(c, reason="plant spent: P/⊥ has no response path on a plant", actor_fault=False)
            return
        right = (verdict == F) == truth
        rec = a.plant_bad if truth is False else a.plant_good
        rec.append((self.t, not right))
        if len(rec) > self.p.n_P:
            del rec[: len(rec) - self.p.n_P]
        c.plant_outcome = "stood" if right else "failure"
        if self.first_plant_adjudicated_at is None:
            self.first_plant_adjudicated_at = self.t         # 1.6.0 §2.4: the determination requirement is live from here
        self.period["plants"] += 1
        if truth is False:
            self.period["bad"] += 1
            if not right:
                self.period["bad_approved"] += 1
        self._reveal_plant(c, r, c.plant_outcome)
        if not right:
            self._overturn_review(c, r, pay_fee_to=None)
        if truth:
            c.outcome, c.state = F, "PENDING"
        else:
            self._finalize_N(c, reason="plant: not fulfilled by construction", actor_fault=False)
        self._check_record(a, failed=not right)

    def _reveal_plant(self, c: Case, r: Review, outcome: str):
        self.history.append("plant_revealed", {"t": self.t, "case": c.id, "truth": "good" if c.plant else "bad",
                                               "nonce": c.plant_nonce, "commit": c.plant_commit,
                                               "review": r.id, "reviewer": r.reviewer, "verdict": r.verdict,
                                               "outcome": outcome})
        c.plant_reveal_hseq = len(self.history.entries) - 1
        self._log(c, f"plant revealed: {'good' if c.plant else 'bad'}; review {r.id} {r.verdict} → {outcome}")

    def _check_record(self, a: Actor, failed: bool = False):
        """After a plant adjudication. 1.3.0 §2.2 (membership): a member whose record has crossed
        θ_duty is suspended from the market for T_susp ticks; a probationer is re-suspended by any
        plant failure, the clock restarting, and readmitted to membership when its trailing record
        passes θ_duty with at least n_min outcomes judged since the suspension began. 1.2.1 (membership
        off): a crossing suspends from duty; a probationer's record speaks again at its next plant.
        An actor suspended while on duty with no active review leaves now (its review has just completed)."""
        if self.p.membership:
            if a.probation:
                a.since_susp += 1
                if failed:
                    self._suspend(a, "probation failed: plant failure")
                elif a.since_susp >= self.p.n_min and a.record_passes(self.p.theta_duty):
                    a.probation = False
                    a.readmitted_at = self.t
                    self.readmissions += 1
                    self.readmission_ticks_sum += self.t - (a.susp_started if a.susp_started is not None else self.t)
                    self.history.append("suspension", {"t": self.t, "actor": a.id, "msg": "readmitted to membership",
                                                       "a_hat": round(a.a_hat, 4), "r_hat": round(a.r_hat, 4),
                                                       "since_suspension": a.since_susp})
            elif a.suspended_until is None and not a.record_passes(self.p.theta_duty):
                self._suspend(a, "record crossed θ_duty")
            return
        a.probation = False                               # a plant has been judged: the record speaks again
        if a.suspended_until is None and not a.record_passes(self.p.theta_duty):
            self._suspend(a, "record crossed θ_duty")

    def _suspend(self, a: Actor, why: str):
        a.probation = False
        a.suspended_until = self.t + self.p.T_susp
        a.susp_started = self.t
        a.since_susp = 0
        self.suspensions += 1
        self.period["suspensions"] += 1
        self.history.append("suspension", {"t": self.t, "actor": a.id, "until": a.suspended_until, "why": why,
                                           "a_hat": round(a.a_hat, 4), "r_hat": round(a.r_hat, 4)})
        if a.on_duty and a.open_review is None:
            self._leave_duty(a, self.t, "suspended")

    # ------------------------------------------------ the effort dial (1.2.0 §2.3)
    @staticmethod
    def _new_period(start: int) -> dict:
        return {"start": start, "plants": 0, "bad": 0, "bad_approved": 0, "plants_created": 0, "initial": 0,
                "approvals": 0, "audit_demand": 0.0, "audits": 0, "challenge_reviews": 0, "dur_sum": 0, "dur_n": 0,
                "suspensions": 0, "eligibility_shortfall": 0,
                "award_price_sum": 0.0, "award_n": 0,
                "troop_ticks_reviews": 0, "troop_ticks_deliveries": 0, "troop_summons_reviews": 0,
                "troop_summons_deliveries": 0, "troop_shortfall_seats": 0, "troop_shortfall_awards": 0,
                "troop_held_ticks": 0, "held_market_audit_max": 0,
                # 1.6.0: the network rating and Ω's readings
                "on_time": 0, "late": 0, "lateness_sum": 0, "rebates_paid": 0.0, "liabilities_accrued": 0.0,
                "omega_min": None, "troop_panel_summons": 0,
                # 1.7.0 §2.1: Ω's record by source — its two incomes, its own money's flows, its outflows
                "omega_fee": 0.0, "troop_surplus": 0.0, "advances_made": 0.0, "advances_repaid": 0.0,
                "liabilities_paid": 0.0, "plant_out": 0.0, "plant_back": 0.0}

    def _maybe_end_period(self, tick: int):
        """Once per period — period_plants adjudicated plants or period_ticks ticks, whichever first —
        the clock is read and the dial moves: m_{t+1} = clamp(m_t (F̂/F*)^γ, 0.9 m_t, 2 m_t) into
        [1, m_max]; then π_t, X_t (sized to the period's review demand, floor V_max + 1) follow.
        With no bad plant adjudicated there is no reading and m_t holds. At m_max with F̂ > F* for
        two consecutive periods the capture alarm is committed and the reserve re-seated by plant
        record. The period's plant shortfall is what the rate called for and was not created."""
        per = self.period
        if per["plants"] < self.p.period_plants and tick - per["start"] < self.p.period_ticks:
            return
        ticks = max(1, tick - per["start"])
        F_hat = (per["bad_approved"] / per["bad"]) if per["bad"] else None
        m_old = self.m_t
        if self.p.dial and F_hat is not None:
            ratio = (F_hat / self.p.F_star) ** self.p.gamma if F_hat > 0 else 0.0
            m_new = min(max(m_old * ratio, 0.9 * m_old), 2.0 * m_old)
            self.m_t = min(max(m_new, 1.0), self.p.m_max)
        alarm = False
        if self.p.dial:
            self.pi_t = min(self.p.pi_max, self.p.pi0 * self.m_t)
            d_bar = max(1.0, per["dur_sum"] / per["dur_n"]) if per["dur_n"] else 1.0
            if self.p.membership:
                # 1.3.0 §2.3: audit demand on the approving reviewers' applied odds, not a population mean
                audit_rate = per["audit_demand"] / ticks
            else:
                duty = [a for a in self.actors.values() if a.on_duty]
                p_bar = (sum(a.p_audit for a in duty) / len(duty)) if duty else self.p.p_start
                audit_rate = self.m_t * p_bar * (per["approvals"] / ticks)
            challenge_rate = per["challenge_reviews"] / ticks
            r_t = (per["initial"] / ticks) * (1.0 + self.pi_t) + audit_rate + challenge_rate
            self.X_t = max(self.p.V_max + 1, int(math.ceil(r_t * d_bar - 1e-9)))
            # the seats only members may hold: the period's audit and challenge demand (1.3.0 §2.3)
            self.member_seats = int(math.ceil((audit_rate + challenge_rate) * d_bar - 1e-9))
            if F_hat is not None and m_old >= self.p.m_max - 1e-12 and F_hat > self.p.F_star:
                self.alarm_streak += 1
                alarm = self.alarm_streak >= 2
            else:
                self.alarm_streak = 0
        shortfall = self.plants_due()
        self.plant_shortfall += shortfall
        self.plant_credit -= shortfall
        rec = {"t": tick, "start": per["start"], "plants": per["plants"], "bad": per["bad"],
               "bad_approved": per["bad_approved"], "F_hat": None if F_hat is None else round(F_hat, 6),
               "m_before": round(m_old, 6), "m": round(self.m_t, 6), "pi": round(self.pi_t, 6), "X": self.X_t,
               "member_seats": self.member_seats,
               "plants_created": per["plants_created"], "plant_shortfall": shortfall,
               "suspensions": per["suspensions"], "eligibility_shortfall": per["eligibility_shortfall"],
               "alarm": alarm,
               # 1.4.0 §2.5: the readings
               "troop_ticks_reviews": per["troop_ticks_reviews"], "troop_ticks_deliveries": per["troop_ticks_deliveries"],
               "troop_summons": [per["troop_summons_reviews"], per["troop_summons_deliveries"]],
               "troop_shortfall": [per["troop_shortfall_seats"], per["troop_shortfall_awards"], per["troop_held_ticks"]],
               "held_market_audit_max": per["held_market_audit_max"],
               "fund": round(self.ledger.wallet(self.troop_wallet).U, 6), "fund_reserve": round(self.R_T, 6),
               # 1.7.0 §2.1: the uplift fund and Ω's record by source
               "uplift_fund": round(self.ledger.wallet(DUTY_FUND).U, 6),
               "omega_income": {"fee": round(per["omega_fee"], 6), "troop_surplus": round(per["troop_surplus"], 6)},
               "omega_advances": {"made": round(per["advances_made"], 6), "repaid": round(per["advances_repaid"], 6)},
               "omega_out": {"rebates_paid": round(per["rebates_paid"], 6), "liabilities_paid": round(per["liabilities_paid"], 6),
                             "plant_out": round(per["plant_out"], 6), "plant_back": round(per["plant_back"], 6)},
               "advance": round(self.advance_outstanding, 6), "B_bar": round(self.mean_awarded_price(), 6),
               # 1.5.0 §2.1: the period's peak demand, how much of it was refused, and the demand at its last seating
               "demand_peak": round(self.troop_demand_peak, 6), "demand_peak_refused": round(self.troop_demand_peak_refused, 6),
               "demand_last": round(self.troop_demand_now, 6),
               # 1.6.0 §2.1–2.2: the network rating and Ω's readings
               "on_time": per["on_time"], "late": per["late"],
               "lateness_mean": (per["lateness_sum"] / per["late"]) if per["late"] else 0.0,
               "rebates_paid": round(per["rebates_paid"], 6), "liabilities_accrued": round(per["liabilities_accrued"], 6),
               "liabilities_outstanding": round(sum(l["amount"] for l in self.omega_liabilities), 6),
               "open_late": self.open_late(), "omega_min": per["omega_min"], "plant_reserve": round(self._plant_reserve(), 6),
               "troop_panel_summons": per["troop_panel_summons"]}
        self.periods.append(rec)
        self.history.append("period", rec)
        self.troop_capital_peak_prev, self.troop_capital_peak = self.troop_capital_peak, self._troop_capital_now()
        self.troop_demand_peak_prev = self.troop_demand_peak                   # 1.6.0 §2.5
        self._last_initial_rate = per["initial"] / max(1, ticks)
        # 1.5.0 §2.1: the new period's peak starts at the standing demand — every troop still in the field; the same
        # tick's summons pass adds whatever that seating refuses
        self.troop_demand_peak, self.troop_demand_peak_refused = self._troop_capital_now(), 0.0
        if alarm:
            self.alarms += 1
            self._reseat_reserve(tick)
        self.period = self._new_period(tick)

    def _reseat_reserve(self, tick: int):
        """The capture alarm (1.2.0 §2.3): the duty reserve is re-seated from the actors with the
        lowest bad-plant approval rate (ties: lowest good-plant rejection rate, then duty credit) —
        the one place a record chooses the panel. Duty actors holding a review leave at its
        completion if their record then fails; the rest are released now and the seats refilled."""
        GV = self.p.G_V * self.ledger.index()
        for a in sorted((a for a in self.actors.values() if a.on_duty), key=lambda a: a.id):
            if a.open_review is None:
                self._leave_duty(a, tick, "capture alarm: reserve re-seated")
        pool = [a for a in self.actors.values()
                if not a.on_duty and a.committed is None and a.open_review is None and a.duty_eligible
                and self.ledger.wallet(a.id).U + 1e-9 >= GV]
        pool.sort(key=lambda a: (round(a.a_hat, 9), round(a.r_hat, 9), -a.kappa, a.id))
        n = sum(1 for a in self.actors.values() if a.on_duty)
        seated = []
        if self.p.membership:
            E_t = sum(1 for a in self.actors.values() if a.is_member and a.record_passes(self.p.theta_duty))
            cap = self._member_cap(E_t)
        for a in pool:
            if n >= self.X_t:
                break
            if self.p.membership and a.is_member and \
                    sum(1 for b in self.actors.values() if b.on_duty and b.is_member) >= cap:
                continue                                   # no member is seated at or above the cap (1.3.0 §2.3)
            a.on_duty, a.duty_since, a.duty_reviews = True, tick, 0
            seated.append(a.id)
            n += 1
        self.history.append("capture_alarm", {"t": tick, "m": self.m_t, "X": self.X_t, "seated": seated})

    # ------------------------------------------------ the orchestrator's troops (1.4.0)
    def roll_audit(self, cid: str):
        """1.4.0 §2.2: a rolled audit is an obligation of the case. The driver rolls (the engine has no
        roll) and calls this to record it: from now the window does not close and the case does not
        vest until an audit completes — seated by a member when one is free, by a troop after w_R
        (§2.2), or, for the state's own work, by a member only (§2.3)."""
        c = self._case(cid)
        if c.plant is not None:
            raise RuleError("roll_audit: no audit is rolled on a plant (1.2.0 §2.1)")
        if c.state != "PENDING" or c.outcome_or_verdict() != F:
            raise RuleError("roll_audit: only a pending F verdict is audited (§8.3)")
        if self.t > c.window_end:
            raise RuleError("roll_audit: window closed")
        if c.challenge_round_used or c.audit_obligation or c.audit_vacated \
                or any(self.reviews[r].role == "audit" and self.reviews[r].status != "withdrawn" for r in c.reviews):
            raise RuleError("roll_audit: the case's challenge round is used, or an audit is already rolled or seated")
        if any(a[3] == "override" for a in c.assessments):
            raise RuleError("roll_audit: a human ruling has settled this case's assessment (§15.2)")
        c.audit_obligation, c.audit_rolled_at = True, self.t
        c.open_items += 1
        self._log(c, "audit rolled: an obligation of the case until an audit completes")

    def audit_odds(self, cid: str) -> float:
        """The odds a driver rolls for a pending approval: 1 for a troop reviewer's approval of a troop's
        delivery (1.4.0 §2.3); the approving reviewer's applied odds otherwise (1.3.0 §2.2); for a troop
        reviewer's approval of a member's work, the adaptive floor scaled by the dial — the odds a reviewer
        whose record stood would carry (a default chosen at implementation, Appendix I)."""
        c = self._case(cid)
        if c.market_audit_only:
            return 1.0
        r = self._initial_review(c) if any(self.reviews[x].role == "initial" and self.reviews[x].status == "done"
                                            for x in c.reviews) else None
        if r is None:
            return self.p.p_start
        if self.is_troop(r.reviewer):
            return min(1.0, self.m_t * self.p.p_floor)
        return self.actors[r.reviewer].p_eff

    def mean_awarded_price(self) -> float:
        """B̄: the mean price awarded to members over the trailing period (this period if it has awards,
        else the last period's), the ceiling of the request when there is none (1.4.0 §2.3)."""
        if self.period["award_n"]:
            return self.period["award_price_sum"] / self.period["award_n"]
        if self.periods and self.periods[-1].get("B_bar"):
            return self.periods[-1]["B_bar"]
        return 0.0

    @property
    def R_T(self) -> float:
        """The fund's troop reserve. 1.5.0 §2.1: the peak troop demand of the current period; 1.4.0: the peak capital
        carried over this period and the previous one (`reserve_demand=False`)."""
        if self.p.reserve_demand and not self.p.troop_account:   # 1.7.0 §2.1: the troop account's reserve is capital held
            if self.p.reserve_periods >= 2:            # 1.6.0 §2.5: over this and the previous period
                return max(self.troop_demand_peak, self.troop_demand_peak_prev)
            return self.troop_demand_peak
        return max(self.troop_capital_peak, self.troop_capital_peak_prev)

    @property
    def troop_demand_now(self) -> float:
        """D_s at the last seating: capital held plus the cost of summonses refused for funds (1.5.0 §2.1)."""
        return self.troop_demand_held + self.troop_demand_refused

    def _troop_capital_now(self) -> float:
        return sum(t["cost"] + t["lock"] for t in self.troops.values() if t["t_release"] is None)

    def _fund_can_carry(self, need: float, cid: str) -> bool:
        """The fund carries a summons from its unlocked balance; Ω advances the difference, up to A_T
        outstanding, repaid first from the fund's inflows (1.4.0 §2.4)."""
        if not self.p.duty_fund:
            return False
        fund = self.ledger.wallet(self.troop_wallet)
        if fund.U + 1e-9 >= need:
            return True
        short = need - fund.U
        room = self._omega_available()                 # 1.6.0 §2.2: above the plant reserve; 1.5.0: under A_T
        adv = min(short, room)
        if adv > 1e-12:
            self.ledger.transfer(Ledger.OMEGA, self.troop_wallet, adv, case=cid,
                                 note="Ω advance to the troop account" if self.p.troop_account else "Ω advance to the duty fund")
            self.advance_outstanding += adv
            self.advances_made += adv
            self.period["advances_made"] += adv
        return fund.U + 1e-9 >= need

    @property
    def troop_wallet(self) -> str:
        """The troops' wallet: the troop account (1.7.0 §2.1) or, under the merged fund of 1.4.0–1.6.0, the duty fund."""
        return TROOP_ACCT if self.p.troop_account else DUTY_FUND

    def _fee_income(self, amount: float):
        self.omega_fee_income += amount
        self.period["omega_fee"] += amount

    def _pay_troop_surplus(self):
        """1.7.0 §2.1: at each settlement batch, after the advance is repaid, the troop account's unlocked balance above
        R_T — the two-period peak of the capital troops held — flows to Ω: a troop is an actor of the state and what it
        earns is the state's. R_T already counts the locks held, so under stress the account keeps more than R_T in
        total and nothing flows until it has refilled (the implementer's reading, Appendix L)."""
        if not (self.p.duty_fund and self.p.troop_account):
            return
        acct = self.ledger.wallet(TROOP_ACCT)
        surplus = acct.U - self.R_T
        if surplus > 1e-9:
            self.ledger.transfer(TROOP_ACCT, Ledger.OMEGA, surplus, note="troop surplus to Ω")
            self.troop_surplus_paid += surplus
            self.period["troop_surplus"] += surplus

    def _repay_advance(self):
        if self.advance_outstanding <= 1e-12:
            return
        fund = self.ledger.wallet(self.troop_wallet)
        pay = min(fund.U, self.advance_outstanding)
        if pay > 1e-12:
            self.ledger.transfer(self.troop_wallet, Ledger.OMEGA, pay,
                                 note="troop account repays Ω's advance" if self.p.troop_account else "duty fund repays Ω's advance")
            self.advance_outstanding -= pay
            self.advances_repaid += pay
            self.period["advances_repaid"] += pay
            if self.advance_outstanding < 1e-12:
                self.advance_outstanding = 0.0

    def _new_troop(self, kind: str, cid: str, cost: float, lock: float) -> str:
        self._n_troop += 1
        tid = f"{TROOP_PREFIX}{self._n_troop}"
        self.ledger.aliases[tid] = self.troop_wallet
        self.troops[tid] = {"kind": kind, "case": cid, "review": None, "t_summons": self.t, "t_release": None,
                            "cost": cost, "lock": lock}
        return tid

    def _release_troop(self, tid: str):
        t = self.troops.get(tid)
        if t is not None and t["t_release"] is None:
            t["t_release"] = self.t
            self.history.append("troop", {"t": self.t, "troop": tid, "kind": t["kind"], "case": t["case"], "msg": "released"})

    def _free_eligible_reviewer(self, c: Case, role: str) -> bool:
        """Is any on-duty reviewer eligible for this seat free to take it? (1.4.0 §2.2's test for 'unfilled'.)"""
        GV = c.G_V
        for a in self.actors.values():
            if not a.on_duty or a.open_review is not None or a.committed is not None:
                continue
            if a.id in c.excluded or a.id == c.actor or a.id == c.requester:
                continue
            if self.ledger.wallet(a.id).U + 1e-9 < GV:
                continue
            if not a.duty_eligible or (role in PANEL_ROLES and not a.panel_eligible):
                continue
            return True
        return False

    def _free_fundable_member(self, G: float) -> bool:
        for a in self.actors.values():
            if not a.on_duty and a.committed is None and a.open_review is None and a.is_member \
                    and self.ledger.wallet(a.id).U + 1e-9 >= G:
                return True
        return False

    def _summon_review(self, c: Case, role: str, tick: int) -> Optional[str]:
        if self._positions(c) + 1 > self.p.V_max:
            return None                                 # no seat to take: the path is full (I8)
        cost_credits = self.p.c_T                      # declared in credits at v ≈ 1; purchased as real cost c_T · v
        need = cost_credits + c.G_V
        self._last_refusal_funds = False
        if not self._fund_can_carry(need, c.id):
            self.troop_shortfall_seats += 1
            self.period["troop_shortfall_seats"] += 1
            self._pass_refused += need                  # 1.5.0 §2.1: the amount the carry check refused is demand
            self._last_refusal_funds = True
            if self._pass_refused_review_tpost is None or (c.t_post is not None and c.t_post < self._pass_refused_review_tpost):
                self._pass_refused_review_tpost = c.t_post
            return None
        tid = self._new_troop("review", c.id, cost_credits, c.G_V)
        credits = self.ledger.purchase(tid, cost_credits * self.ledger.v, case=c.id, note="troop cost (review)")
        self.ledger.lock(tid, c.G_V, key=None or f"bond:r{self._n_review + 1}", case=c.id, note=f"bond ({role}, troop)")
        self._n_review += 1
        rid = f"r{self._n_review}"
        r = Review(rid, c.id, tid, role, tick, tick + self.p.T_review, bond=c.G_V)
        r.cost = credits
        self.reviews[rid] = r
        self._live_reviews[rid] = r
        c.reviews.append(rid)
        c.excluded.add(tid)
        self.troops[tid]["review"] = rid
        if role == "audit":
            if c.audit_vacated:
                c.audit_vacated = False
            elif c.audit_obligation:
                c.audit_obligation = False
            else:
                c.open_items += 1
            self.period["audits"] += 1
        elif role == "appeal":
            c.challenge["reviews"].append(rid)
            self.period["challenge_reviews"] += 1
        self.troop_summons_reviews += 1
        self.period["troop_summons_reviews"] += 1
        if role in PANEL_ROLES:
            self.period["troop_panel_summons"] += 1
        if self._pass_refused_review_tpost is not None and c.t_post is not None and c.t_post > self._pass_refused_review_tpost:
            self._priority_violation = f"review seat of {c.id} (posted {c.t_post}) summoned after an older case was refused"
        self.troop_capital_peak = max(self.troop_capital_peak, self._troop_capital_now())
        self.history.append("troop", {"t": tick, "troop": tid, "kind": "review", "seat": role, "case": c.id,
                                      "review": rid, "msg": "summoned"})
        self._log(c, f"troop {tid} summoned for the {role} seat ({rid}) after it waited {self.p.w_R} ticks")
        return tid

    def _summon_delivery(self, c: Case, tick: int) -> Optional[str]:
        B = self.mean_awarded_price() or c.beta
        if c.beta + 1e-9 < B:
            return None                                 # priced below the market: not a shortage; waits
        G = max(1.0, math.ceil(self.p.G_frac * B))
        omega_base = self.p.omega_rate * B
        omega = omega_base * self.m_t
        omega_fund = (omega - omega_base) if self.p.duty_fund else 0.0
        idx = self.ledger.index()
        D, K, GV = self.p.D * idx, self.p.K * idx, self.p.G_V * idx
        phi_E, phi_F = self.p.phi_E_root * idx, self.p.phi_F_root * idx
        if self.ledger.wallet(c.requester).U + 1e-9 < B + phi_E + phi_F + omega:
            return None                                 # the requester cannot pay in: no award, troop or not
        cost_credits = self.p.c_D_T
        # 1.6.0 §2.2: a delivery carries its inspection — a check against the fund plus Ω's available advance for its
        # own capital and two review seats; the advance drawn is the delivery's own shortfall
        carries = True
        if self.p.omega_backs_fund:
            need_all = cost_credits + G + 2 * (self.p.c_T + GV)
            carries = self.ledger.wallet(self.troop_wallet).U + self._omega_available() + 1e-9 >= need_all
        if not carries or not self._fund_can_carry(cost_credits + G, c.id):
            self.troop_shortfall_awards += 1
            self.period["troop_shortfall_awards"] += 1
            self._pass_refused += cost_credits + G       # 1.5.0 §2.1: the amount the carry check refused is demand
            if self._pass_refused_delivery_tpost is None or c.t_post < self._pass_refused_delivery_tpost:
                self._pass_refused_delivery_tpost = c.t_post
            return None
        if self._pass_refused_delivery_tpost is not None and c.t_post > self._pass_refused_delivery_tpost:
            self._priority_violation = f"delivery of {c.id} (posted {c.t_post}) summoned after an older request was refused"
        tid = self._new_troop("delivery", c.id, cost_credits, G)
        c.D, c.K, c.G_V, c.phi_E, c.phi_F, c.omega, c.G = D, K, GV, phi_E, phi_F, omega, G
        c.G_award = G
        c.B, c.tau, c.actor = B, self.p.tau_T, tid
        c.t_award, c.deadline = tick, tick + self.p.tau_T
        self.ledger.purchase(tid, cost_credits * self.ledger.v, case=c.id, note="troop cost (delivery)")
        self.ledger.lock(tid, G, key=f"G:{c.id}", case=c.id, note="guarantee (troop)")
        self.ledger.fund_escrow(c.requester, c.id, B, note="delivery price")
        self.ledger.fund_deposit(c.requester, c.id, phi_E, note="expense allowance")
        if phi_F > 0:
            self.ledger.fund_fee_pot(c.requester, c.id, phi_F, note="fee pot")
        if omega - omega_fund > 1e-12:
            self.ledger.transfer(c.requester, Ledger.OMEGA, omega - omega_fund, case=c.id, note="service fee")
            self._fee_income(omega - omega_fund)
        if omega_fund > 1e-12:
            self.ledger.transfer(c.requester, DUTY_FUND, omega_fund, case=c.id, note="duty fund")
            self.fund_in += omega_fund
        self._freeze(c)
        c.state = "COMMITTED"
        c.troop_award, c.member_at_award = True, True
        self.troop_summons_deliveries += 1
        self.period["troop_summons_deliveries"] += 1
        self.troop_capital_peak = max(self.troop_capital_peak, self._troop_capital_now())
        self.history.append("troop", {"t": tick, "troop": tid, "kind": "delivery", "case": c.id, "B": B, "msg": "summoned"})
        self._log(c, f"troop {tid} awarded at the market price B={B:g} after the request waited {self.p.w_A} ticks unawarded")
        self._service_omega_claims()
        return tid

    def _summon_troops(self, tick: int):
        """1.4.0 §2.2–2.3, after the tick's seating: a required seat unfilled for w_R with no free eligible
        on-duty reviewer, or a root request unawarded for w_A with no free fundable member, is taken by a
        troop when the fund can carry it. The audit of a troop reviewer's approval of a troop's delivery is
        never summoned for: it waits for a member and is counted. A seat's wait is the number of seating
        steps since it was required — required at t, it has waited 1 at t's seating and w_R at the seating
        of t + w_R − 1. Also the tick's readings."""
        held_now, held_max_age = 0, 0
        self._pass_refused = 0.0
        self._pass_refused_review_tpost = None
        self._pass_refused_delivery_tpost = None
        self._priority_violation = None
        # 1.6.0 §2.1: the clocks run — one tick for every open root request whose ceiling admits the market price
        for c in self._live_cases.values():
            if self._clock_runs(c):
                c.clock_ticks += 1
        # 1.6.0 §2.2: Ω's order — liabilities older than a period before any advance
        self._service_omega_liabilities(self.p.period_ticks)
        # first pass: the review seats (1.6.0 §2.2: inspection first), oldest case first
        for c in list(self._live_cases.values()):
            if c.plant is not None or any(a[3] == "override" for a in c.assessments):
                continue                                # never a plant; never a case a human has ruled on (I18)
            # the audit seat
            if c.state == "PENDING" and (c.audit_obligation or c.audit_vacated) \
                    and not any(self.reviews[r].role == "audit" and self.reviews[r].status == "open" for r in c.reviews):
                since = c.audit_vacated_at if c.audit_vacated else c.audit_rolled_at
                if c.market_audit_only:
                    held_now += 1
                    held_max_age = max(held_max_age, tick - (since or tick))
                elif self.p.troops and since is not None and tick - since + 1 >= self.p.w_R \
                        and not self._free_eligible_reviewer(c, "audit"):
                    if self._summon_review(c, "audit", tick) is None:
                        self.troop_held_ticks += 1
                        self.period["troop_held_ticks"] += 1
            # the initial seat
            if c.state == "SUBMITTED" and c.is_root and self.p.troops and c.seat_since is not None \
                    and not any(self.reviews[r].role == "initial" and self.reviews[r].status in ("open", "done", "vested")
                                for r in c.reviews) \
                    and tick - c.seat_since + 1 >= self.p.w_R and not self._free_eligible_reviewer(c, "initial"):
                if self._summon_review(c, "initial", tick) is None:
                    self.troop_held_ticks += 1
                    self.period["troop_held_ticks"] += 1
            # the panel seats
            ch = c.challenge
            if self.p.troops and ch and not ch["resolved"] and len(ch["reviews"]) < 2 \
                    and tick - ch.get("seat_since", tick) + 1 >= self.p.w_R and not self._free_eligible_reviewer(c, "appeal"):
                remaining = 2 - len(ch["reviews"])
                for i in range(remaining):
                    if self._summon_review(c, "appeal", tick) is None:
                        self.troop_held_ticks += 1
                        self.period["troop_held_ticks"] += 1
                        if self._last_refusal_funds:    # 1.5.0 §2.1: a case's demand is its unfilled seats — both
                            self._pass_refused += (remaining - i - 1) * (self.p.c_T + c.G_V)
                        break
        # second pass: the awards, oldest request first
        for c in list(self._live_cases.values()):
            if c.plant is not None or any(a[3] == "override" for a in c.assessments):
                continue
            if c.state == "AVAILABLE" and c.is_root and self.p.troops and c.requester in self.requesters \
                    and tick - c.t_post + 1 >= self.p.w_A:
                B = self.mean_awarded_price() or c.beta
                G = max(1.0, math.ceil(self.p.G_frac * B))
                if not self._free_fundable_member(G):
                    self._summon_delivery(c, tick)
        # 1.6.0 §2.2: younger liabilities after the pass; Ω's minimum balance is the period's solvency reading
        self._service_omega_liabilities(0)
        om = self.ledger.wallet(Ledger.OMEGA).U
        self.period["omega_min"] = om if self.period["omega_min"] is None else min(self.period["omega_min"], om)
        self.held_market_audit_now = held_now
        self.held_market_audit_max_age = max(self.held_market_audit_max_age, held_max_age)
        self.period["held_market_audit_max"] = max(self.period["held_market_audit_max"], held_now)
        # 1.5.0 §2.1: the troop demand at this seating — capital held plus what was refused for funds — and the
        # period's peak; each refused case counted once per seating, at the amount the carry check refused
        held = self._troop_capital_now()
        self.troop_demand_held, self.troop_demand_refused = held, self._pass_refused
        d_s = held + self._pass_refused
        if d_s > self.troop_demand_peak + 1e-12:
            self.troop_demand_peak, self.troop_demand_peak_refused = d_s, self._pass_refused
        active_r = sum(1 for t in self.troops.values() if t["kind"] == "review" and t["t_release"] is None)
        active_d = sum(1 for t in self.troops.values() if t["kind"] == "delivery" and t["t_release"] is None)
        self.troop_ticks_reviews += active_r
        self.troop_ticks_deliveries += active_d
        self.period["troop_ticks_reviews"] += active_r
        self.period["troop_ticks_deliveries"] += active_d

    # ------------------------------------------------------------ working set
    @staticmethod
    def _review_quiescent(r: Review) -> bool:
        return r.status in ("withdrawn", "overturned", "vested") and r.reimbursed_pending <= 1e-12 \
            and r.deferred <= 1e-12

    def _case_quiescent(self, c: Case) -> bool:
        """Final, settled, every review quiescent, and nothing left in its pool: a root whose pots
        are still open (its tree has not closed) can still change, and stays in the working set."""
        pl = self.ledger.pools.get(c.id)
        return c.final and not c.needs_review_settlement \
            and (pl is None or pl.total <= 1e-12) \
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
            if pl is not None and pl.total <= 1e-12:
                del self.ledger.pools[cid]            # an empty pool is recreated empty on demand
            self.cases.evict(cid)
        for rid, r in self.reviews.resident_items():
            if not self.cases.is_resident(r.case):
                self.reviews.evict(rid)

    def __getstate__(self):
        """A pickled world is an in-memory world: its journals pickle as lists and its paged
        mappings as dicts (sim/record.py), so a snapshot is the same object graph in both modes."""
        state = self.__dict__.copy()
        if self._paged:
            state["_paged"] = False
            # the positions index travels with a paged-out case; the in-memory world has it for every case
            state["_case_entries"] = {cid: [entry[2] for entry in c.log] for cid, c in self.cases.items()}
        return state

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

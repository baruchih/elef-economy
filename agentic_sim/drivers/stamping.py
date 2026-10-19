"""Scoped run — careful versus careless review (spec §18.1 question 1).

Permitted operations, declared before the run (§18.2): root cases only; F/N reviewers; actors
accept every N (no appeals); human requesters silent (no disputes, no overrides); no delegation,
no P/⊥, no resource spend by actors; the orchestrator selects, rolls audits and rules on splits;
rotation is the engine's (§13). Seeded; the engine itself is deterministic.

    python3 -m drivers.stamping --actors 20 --ticks 1000 --stampers 0.5 --seed 1
    python3 -m drivers.stamping --on-duty 8 --fee 4 --seed 1        # the 1.1.0 rerun's other cells

Task world. Each task has a hidden truth: it fails at base rate b, independent of the actor
(actor competence is question 2's subject and is kept out). Actors are the same population as
reviewers — the reserve rotates through them — and each has a fixed reviewing disposition:

  careful   verdict equals the truth with probability a; costs 2–3 credits per review (within K),
            or what its unlocked credit can buy when earlier bonds have left it short (counted)
  stamper   always F, cost 0 — or, with --camouflage k, N on a random fraction k of its reviews
            (the red-team disposition of 1.2.0 §8: looking careful without looking)

Planted work (1.2.0 §2.1). The engine states how many plants its rate calls for (`plants_due`); the
orchestrator supplies them each tick before assigning reviews — bad with probability β_P — from
the same task world, so a plant's truth is as hidden from the reviewer as a task's. No audit is
rolled and no dispute filed on a plant; the engine refuses both. `--rules 1.1.0` is the control:
no plants, dial off, p_start = p_cap = 0.5, Ω float 20 — the 1.1.0 engine's behaviour, declared.

Membership (1.3.0). A suspended actor wins no award and the orchestrator offers none; after T_susp it is a
probationer — initial reviews only, odds pinned at 1 — until its trailing record passes with n_min new plant
outcomes. The dial's raised tax goes to the duty fund and is paid out as a fee uplift. `--rules 1.2.0` is the
control for this revision (membership, fund and netted plant capital off); `--fund off` isolates the fund.
Dispositions: `--stamper-mode reformer` makes a stamper review carefully while on probation and stamp again
once readmitted (the red team of 1.3.0 §8).

Orchestrator. Every free actor offers the ceiling (B = β) with the same τ, so S_θ = ρ − λB/β
reduces to argmax ρ, with the κ tie band: among offers within `band` of the best score the
highest duty credit wins, then the lowest id. Audits: after an initial F the engine's p_audit of
that reviewer is rolled once, honestly; the auditor is whoever the reserve rotation makes
eligible, stampers included — a stamper auditing a stamper agrees, and that self-protection is
part of the dynamic. A split (audit N against a second review's F, or the reverse) is ruled by
the truth with probability r, otherwise the other way.

What is measured, per disposition over time: wealth, delivery income, review fees (and of them
the fixed fee, and the haircut when the fee pot was short), costs, bonds and guarantees forfeited,
awards won, reviews done and overturned, ρ, κ, p_audit; and for the economy: false approvals that
vested, false rejections, label accuracy by grade, audits rolled/assigned/unassignable, reviews
unassignable for lack of an eligible reviewer (the reviewer capital ceiling), rulings, Ω's
unrecovered advances and outstanding claims, and what came back to the requester from the two pots.

Prediction under test. Under v1.0.1 (run 1, October 16, 2026) a stamper earned more per review:
care was reimbursed from the same pot the fee came from, +1.3 predicted, +1.6 measured. Under
1.1.0 (design revision 1) the fee is fixed by role and expenses are made whole from the
allowance, so the money term is −p·b·(1−ε)·(f̄ + G^V) per review, about −0.3 at run 1's
effective catch rate and −0.7 at the nominal p = 0.5, b = 0.2. The rerun of §8 of the revision
is this driver with only the rule changed, at X ∈ {4, 8} and f ∈ {2, 4}, 20 seeds or more.
A finding here is an evaluation under the fixed rules (§19).

The price of work (2.0.0, design revision 8; `--rules 2.0.0`, the default). Demand is six requesters (`--requesters`)
with wallets of 200 (`--wallet`) issued 10 a tick each (`--issuance`); each posts at most one request a tick while fewer
than K_open (`--k-open`; 0 = no limit) of its requests are open, at a ceiling β = min(β_max, a third of its unlocked wallet)
(`--beta-max`, `--ceiling-share`) — or, under `--ceiling-policy market`, β = min(β_max, `--ceiling-mult` × B̄), the
market-aware policy that locks less and posts more (run 13 §3) — when the all-in maximum fits — the engine locks it at posting and refuses what does not
fit; a request flagged below market is raised to the market price when the wallet allows. Supply: a free member bids
c_D (1 + m) — its nominal effort cost 8 (`--c-d`) with a margin raised 0.3 on each award and lowered 0.25 per three idle
ticks (continuously, a twelfth a tick), floored at 0 (`--bid margin`); `--bid ceiling` is the 1.x behaviour, every offer at the ceiling; `--c-d-adaptive`
makes the cost follow the price level with a one-period lag (the spiral, swept). Selection is S_θ = ρ − λ B/β with the
bid live (`--lam`). At submission the actor burns its effort (`spend`). The state delivers at cost (`--c-d-t-mode cost`;
`half` is the 1.x margin) and fields at most N_T troops (`--n-t`, 0 unbounded). A riot is a crowd: `--spike-requesters n`
requesters arrive at `--spike-from` with the default wallet and issuance, post for `--spike-ticks`, and leave once their
requests are served out (their wallets depart M). The deficit shock is `--create-at t --create-amount X`, the declared
scenario operation. Readings: P_t, the deficit by peak and age, real wealth (W · P_0/P_t), the flags, the capacity case.

The bank (2.1.0, design revision 9; `--rules 2.1.0`, the default; `--rules 2.0.0` is the control with Ω's creation). The state
burns its expected cost (`--c-d-t-mode expected`; `at_cost` is 2.0.0's, `half` the 1.x margin) with the trailing fail rate's
prior and window (`--b-t-prior`, `--b-t-min-n`); the bank lends a summons's shortfall and refuses a delivery while the debt is
above the wall (`--debt-bound-periods`, 0 unbounded); every refusal is told and the requester's declared policy holds or
withdraws and reposts (`--requester-on-refusal hold|withdraw`). Red team (§8.9): `--troop-fail-rate` re-draws the truth of the
state's deliveries at the troop's submission (the state made to fail at a half, or three quarters); `--state-rejecters` is a
share of the careful actors that reject every delivery of the state's — reading the case's actor, which the reviewer's view
does not carry (a declared non-conforming reading of what the rule would do if a reviewer could tell). Readings: the bank's
books — minted and destroyed by kind, loans outstanding, the debt by peak and age, the liabilities and their oldest age, the
wall and its slack, Ω's retained income, the cost of truth, b_T and the burn, the marks and what the requesters did at them.

The supply side (2.3.0, design revision 11; `--rules 2.3.0`, the default; `--rules 2.2.0` the control with the fixed population and
one cost). Competence: each actor's effort cost is drawn once at its creation from a log-normal around the anchor (`--c-d-median` 8,
`--c-d-sigma` 0.43, clipped `--c-d-clip` 2 40; σ 0 is one cost) — private to the driver, revealed through bids. Entry: a pool of
candidates (`--entry-pool` 20, costs from the same distribution, `--entry-stampers` share dishonest) read the public view each tick and
arrive (`arrive`, as probationers with a float the bank mints) when their expected real earnings — (B̄ − c) × the awards a free member
wins a tick × the share of the run left after the time to membership — exceed a reservation (`--reservation` 0.8 a tick), at most
`--arrivals-per-tick`; a member whose trailing period's real earnings fall below the reservation for `--exit-patience` periods and
holds no obligation departs (`depart`, its wallet leaving M). Delegation (`--delegation on`): a member awarded a root request whose
cost exceeds the expected child's bid plus the overhead (the nested fee, the pots' net cost, its care in judging) posts a nested
request at that saving as its ceiling (`--nested-pots parent|root`), carrying a longer τ; free members other than the parent bid as
on roots; the parent judges by its disposition (careful: the truth w.p. accuracy, spending its care; stamper: F) and builds on the
child's work (a bad child accepted makes the parent's work bad); a child rejected appeals truthfully; a nested request unawarded for
T_wait is withdrawn and the parent self-executes. Readings: arrivals, admissions, time to membership, departures, members and
probationers, the members' and the population's median cost (the driver's own declaration), nested posted / awarded / self-executed /
vested / final N, the gain from trade, brokers (parents delegating more than half their awards), nested false approvals and overturns.
"""
from __future__ import annotations
import argparse
import math
import os
import random
import sys
import time
from dataclasses import dataclass, field

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sim import Params, World, RuleError, LedgerError, check_all   # noqa: E402
from sim.engine import F, N, PLANT                                  # noqa: E402
from drivers.view import Public                                     # noqa: E402
from drivers.results import RunRecorder                             # noqa: E402

CAREFUL, STAMPER = "careful", "stamper"
GRADES = ("human-explicit", "delegate-explicit", "procedural", "protocol-default", PLANT)

PERMITTED = ["post_root (human H, β fixed)", "award (every free actor offers B = β, τ = work_ticks; S_θ argmax ρ, κ tie band)",
             "submit (after work_ticks, no spend)",
             "assign_initial / assign_audit / assign_appeal (among eligible on-duty actors, by --assignment: round-robin as "
             "§7.5 states — the default; or seeded, a seeded random choice, the policy of the October 16–17 sweeps)",
             "complete_review F/N (verdict by disposition and the hidden truth; cost by disposition)",
             "respond accept / appeal (by --appeal-policy: none = accept every N; truthful = appeal an N on work that is "
             "truly fulfilled, accept otherwise; always = appeal every N; an actor that cannot fund the court fee accepts)",
             "dispute (by --dispute-policy: none; truthful = H disputes a pending F on work that truly failed; half = the "
             "same, half the time; always = H disputes every pending F; H pays the court fee D)",
             "assign_audit (the initial reviewer's effective audit odds min(1, m_t p_j) rolled once per F verdict)",
             "assign_appeal (the second review of an audit challenge)", "rule (split ruled by the truth w.p. r)",
             "create_plant (1.2.0: the orchestrator supplies the plants the engine's rate calls for, bad w.p. β_P, "
             "at B = β; no audit roll, no dispute on a plant)",
             "advance"]
PERMITTED_200 = ["post_root (six requesters, β = min(β_max, a third of the unlocked wallet) or min(β_max, mult × B̄) under --ceiling-policy market, "
                 "one a tick while K_open (0: no limit) and the all-in fit; "
                 "the engine locks the all-in maximum at posting and refuses what does not fit — 2.0.0 §2.1)",
                 "raise_ceiling (a requester flagged below market raises to the market price when its wallet allows)",
                 "award at the bid (a member bids c_D (1 + m), m up on award and down after idle ticks; S_θ = ρ − λ B/β live; "
                 "or every offer at the ceiling under --bid ceiling)",
                 "spend (the actor burns its nominal effort c_D at submission — §4.6, used for the first time)",
                 "add_requester / remove_requester (a crowd arrives with wallets and leaves when served out — 2.0.0 §2.1, Appendix M)",
                 "scenario_create (the deficit shock, declared — 2.0.0 §8.3; the bank's mint_scenario under 2.1.0)",
                 "withdraw_unawarded at a refusal's mark (2.1.0 §2.6: the requester's declared policy under --requester-on-refusal withdraw; "
                 "withdrawn before award, owed nothing)",
                 "arrive / depart (2.3.0 §2.1–2.2: the entry pool's declared policy on the public view; a departure with no live obligation)",
                 "post_nested / award (a child) / judge_nested / withdraw_unawarded + self-execution (2.3.0 §2.4 under --delegation on: the parent's "
                 "declared rule and judgment by disposition; a child rejected appeals truthfully)"]
NOT_IN_RUN = ["appeals by actors (unless --appeal-policy is set)", "disputes (unless --dispute-policy is set)", "human overrides", "P/⊥", "revision/evidence", "delegation (nested cases)",
              "cancellation", "resource spend by actors", "volunteering for duty", "actor competence (truth is actor-independent)",
              "price competition (every offer is at the ceiling)", "requester budget pressure (H is funded beyond the run)",
              "a reviewer that tries to tell a plant from real work (the view carries nothing to tell by; 1.2.0 §2.1)"]


@dataclass
class Task:
    cid: str
    title: str
    fulfilled: bool              # hidden truth
    nested: bool = False          # 2.3.0: a child's task
    audit_rolled: bool = False
    audit_wanted: bool = False   # rolled yes, not yet assigned
    appeal_wanted: bool = False
    appealed: bool = False       # the actor appealed its N (the appeals run)
    dispute_rolled: bool = False
    disputed: bool = False       # H disputed the pending F (the dispute run)
    plant: bool = False          # the orchestrator's planted work (1.2.0)
    probation_false_approval: bool = False   # a probationer approved truly failed work (1.3.0: audited at 1)


@dataclass
class Tally:
    """Per-actor money and outcome counters, accumulated from the public event record."""
    delivery: float = 0.0
    fees: float = 0.0            # fixed fees + emission shares received
    fee_fixed: float = 0.0       # the fixed fees alone (from the fee pot)
    fee_haircut: float = 0.0     # Σ (fee owed − fee paid) over the reviews that vested
    fee_uplift: float = 0.0      # the duty fund's uplift received (1.3.0)
    reimbursed: float = 0.0
    costs: float = 0.0
    bonds_forfeited: float = 0.0
    guarantees_forfeited: float = 0.0
    awards: int = 0
    reviews: int = 0
    overturned: int = 0
    audits_done: int = 0
    plant_reviews: int = 0       # plants judged F or N
    plant_failures: int = 0      # of them, wrong: bond forfeited, record −1
    probation_reviews: int = 0   # reviews completed while a probationer (1.3.0)
    probation_approvals: int = 0 # of them, approvals (every one audited)


class Stamping:
    def __init__(self, a, rec: RunRecorder | None = None):
        self.a = a
        self.rng = random.Random(a.seed)
        self.actors = [f"a{i:02d}" for i in range(a.actors)]
        n_st = round(a.actors * a.stampers)
        ids = list(self.actors)
        self.rng.shuffle(ids)
        self.kind = {aid: (STAMPER if i < n_st else CAREFUL) for i, aid in enumerate(ids)}
        if a.rules == "1.1.0":                   # the control: the 1.1.0 engine's behaviour, declared
            a.pi0, a.dial, a.p_start, a.p_cap, a.omega0 = 0.0, "off", 0.5, 0.5, 20.0
        rev3 = a.rules in ("1.3.0", "1.4.0", "1.5.0", "1.6.0", "1.7.0", "1.7.1", "2.0.0", "2.1.0", "2.2.0", "2.3.0")     # 1.2.0 and 1.1.0: membership, the fund and netted capital off
        rev4 = a.rules in ("1.4.0", "1.5.0", "1.6.0", "1.7.0", "1.7.1", "2.0.0", "2.1.0", "2.2.0", "2.3.0") and a.troops == "on"
        rev5 = a.rules in ("1.5.0", "1.6.0", "1.7.0", "1.7.1", "2.0.0", "2.1.0", "2.2.0", "2.3.0")    # 1.4.0: the reserve is the peak capital carried, over two periods
        rev6 = a.rules in ("1.6.0", "1.7.0", "1.7.1", "2.0.0", "2.1.0", "2.2.0", "2.3.0")     # 1.6.0: the five rules, each behind its flag; `--rules 1.5.0` turns them off
        rev7 = a.rules in ("1.7.0", "1.7.1", "2.0.0", "2.1.0", "2.2.0", "2.3.0")  # 1.7.0: the troop account behind its flag and the cap at two thirds; `--rules 1.6.0` is the control
        rev8 = a.rules in ("2.0.0", "2.1.0", "2.2.0", "2.3.0")     # 2.0.0: the price of work — floating prices, N_T; `--rules 1.7.1` is the fixed-price control
        rev9 = a.rules in ("2.1.0", "2.2.0", "2.3.0")     # 2.1.0: the bank — loans, the debt, the wall, P_t once a period; `--rules 2.0.0` is the control
        rev10 = a.rules in ("2.2.0", "2.3.0")    # 2.2.0: the rebate from income — the period's fee pool, claims pro rata at the close; `--rules 2.1.0` the control
        rev11 = a.rules == "2.3.0"               # 2.3.0: the supply side — entry, exit, the parent's pots; `--rules 2.2.0` the control
        self.rev9, self.rev10, self.rev11 = rev9, rev10, rev11
        self.floating = rev8
        on = lambda flag: rev6 and flag == "on"
        if a.duty_cap is None:
            a.duty_cap = "twothirds" if rev7 else "half"
        p = Params(Res0=a.res0, X=a.on_duty, G_V=a.gv, p_start=a.p_start, p_cap=a.p_cap, p_floor=a.p_floor, band=a.band,
                   record_dir=a.record_dir, f_fee=a.fee, phi_E_root=a.phi_e, phi_F_root=a.phi_f,
                   pi0=a.pi0, dial=(a.dial == "on"), beta_P=a.beta_p, Omega0=a.omega0,
                   membership=rev3, duty_fund=(rev3 and a.fund == "on"), net_plant_capital=rev3, m_max=a.m_max,
                   troops=rev4, eps_T=a.eps_t, w_R=a.w_r, w_A=a.w_a, c_T=a.c_t, c_D_T=a.c_d_t, A_T=a.a_t, tau_T=a.work_ticks,
                   reserve_demand=rev5,
                   service_clock=on(a.clock), T_s=a.t_s, omega_backs_fund=on(a.backing), seat_the_queue=on(a.seat_queue),
                   panel_determined=on(a.panel_determined), reserve_periods=(a.reserve_periods if rev6 else 1),
                   duty_cap_frac={"half": 0.5, "twothirds": 2.0 / 3.0, "all": 1.0}[a.duty_cap],
                   plant_reserve_life=(0 if a.plant_reserve == "period" else 15),
                   troop_account=(rev7 and a.accounts == "on"), omega_rate=a.omega_rate, r_s=a.r_s, T_susp=a.t_susp,
                   theta_panel=a.theta_panel, n_P=a.record_window,
                   floating=rev8, P0=20.0, issuance=(a.issuance if rev8 else 0.0), N_T=(a.n_t if rev8 else 0),
                   troop_cost_at_price=(rev8 and a.c_d_t_mode in ("cost", "at_cost")), lam=a.lam, bbar_counts_troops=(rev8 and a.bbar_troops == "on"),
                   bank=rev9, c_d_t_mode=("at_cost" if a.c_d_t_mode == "cost" else a.c_d_t_mode), b_t_prior=a.b_t_prior,
                   b_t_min_n=a.b_t_min_n, debt_bound_periods=a.debt_bound_periods, rebate_pool=rev10,
                   supply=rev11, F0=a.f0, nested_pots=a.nested_pots)
        self.p = p
        if rev8:
            humans = {f"R{i:02d}": a.wallet for i in range(1, a.requesters + 1)}
        else:
            humans = {"H": a.human_budget}
        self.requesters = sorted(humans)                 # the standing requesters, in order
        self.crowd: list[str] = []                       # the crowd's members while present
        self.crowd_posting = False
        self.owner: dict[str, str] = {}                  # root case -> its requester
        self.margin = {aid: a.margin0 for aid in self.actors}   # 2.0.0 §2.2: each member's bid margin m
        self.idle = {aid: 0 for aid in self.actors}
        self.c_d_now = a.c_d                              # the effort cost in force (the adaptive variant moves it by period)
        # 2.3.0 §2.3: competence — each actor's effort cost drawn once at its creation, private to the driver (σ 0: one cost)
        self.cost_rng = random.Random(a.seed * 7919 + 17)
        self.c_d_of = {aid: self.draw_cost() for aid in self.actors}
        # 2.3.0 §2.5: the entry pool — candidates with costs from the same distribution and a reservation in real earnings a tick
        self.candidates = [{"name": f"n{i:03d}", "cost": self.draw_cost(),
                            "kind": STAMPER if self.cost_rng.random() < a.entry_stampers else CAREFUL} for i in range(a.entry_pool)]
        self.arrived: list[str] = []
        self.departed: list[str] = []
        self.wealth_at_boundary: dict[str, float] = {}
        self.below_reservation: dict[str, int] = {}
        self.periods_seen = 0
        self.awards_window: list[tuple[int, int, int]] = []     # (tick, member awards this tick, free members) for the entry pool's rate
        self.boundary_cost_median: list[tuple[float, float]] = []   # per period: (members' median cost, the population's)
        # 2.3.0 §2.4: delegation — the parent's rule, the children, the readings
        self.nested_parent: dict[str, str] = {}          # nested case -> its parent's root case
        self.parent_delegated: dict[str, int] = {}       # parent actor -> nested requests posted
        self.parent_awards: dict[str, int] = {}          # parent actor -> root awards (for the broker reading)
        self.parent_waiting: dict[str, str] = {}         # root case -> its open nested case while it waits
        self.parent_self_exec: set[str] = set()          # root cases the parent executed itself after a failed delegation
        self.deleg_considered: set[str] = set()         # root cases the parent has decided on
        # 2.0.0 §8.8 red team: lowballers bid half their cost to win reputation; stingy requesters post below the market and never raise
        ids_l = list(self.actors); self.rng.shuffle(ids_l)
        self.lowballers = set(ids_l[: round(len(ids_l) * a.lowball_share)])
        self.stingy = set(self.requesters[: a.stingy_requesters])
        self.small = set(self.requesters[-a.small_requests:]) if a.small_requests > 0 else set()
        ids_c = [aid for aid in self.actors if self.kind[aid] == CAREFUL]
        self.state_rejecters = set(ids_c[: round(len(ids_c) * a.state_rejecters)]) if a.state_rejecters > 0 else set()
        world = World(p, self.actors, humans=humans, on_duty=sorted(self.actors)[: a.on_duty])
        self.w = Public(world)
        self._world = world            # for the final check_all and the fingerprint only
        self.tasks: dict[str, Task] = {}
        self.active: dict[str, bool] = {}        # ordered: creation order, never a set (determinism)
        self.tally = {aid: Tally() for aid in self.actors}
        self.review_owner: dict[str, str] = {}          # rid -> reviewer, for overturn counting
        self.rr_last = -1                                # round-robin pointer (§7.5)
        self.n_events = 0
        self.rec = rec
        # economy counters
        self.c = {"posted": 0, "awarded": 0, "vested": 0, "final_n": 0, "false_approvals": 0, "false_rejections": 0,
                  "audits_rolled": 0, "audits_assigned": 0, "audit_unassignable_ticks": 0, "audits_lapsed": 0,
                  "challenges": 0, "rulings": 0, "rulings_wrong": 0, "reviews_unassignable_ticks": 0,
                  "appeals_filed": 0, "appeals_unfunded": 0, "appeals_won": 0, "appeals_lost": 0,
                  "false_rejections_total": 0, "false_rejections_appealed": 0, "false_rejections_overturned": 0,
                  "true_rejections_appealed": 0, "true_rejections_overturned": 0,
                  "duty_short_of_bond_ticks": 0,   # Σ over ticks of on-duty actors that cannot fund G^V (q6 solvency)
                  "disputes_filed": 0, "disputes_refused": 0, "disputes_won": 0, "disputes_lost": 0,
                  "false_approvals_disputed": 0, "false_approvals_overturned": 0,
                  "true_approvals_disputed": 0, "true_approvals_overturned": 0,
                  "awards_unfilled_ticks": 0, "appeals_unassignable_ticks": 0, "underfunded_careful_reviews": 0,
                  "omega_unrecovered_advances": 0.0, "allowance_refunded": 0.0, "pot_refunded": 0.0,
                  "trees_closed": 0, "disposition_switches": 0,
                  # 1.2.0: planted work and the dial
                  "plants_created": 0, "plants_unfunded": 0, "plants_bad": 0, "plants_stood": 0, "plants_failed": 0,
                  "plants_spent": 0, "bad_plants_approved": 0, "good_plants_rejected": 0, "omega_plant_spend": 0.0,
                  # 1.3.0: membership
                  "awards_refused_members_only_ticks": 0, "probation_false_approvals": 0,
                  # 1.4.0: troops
                  "audit_obligations": 0, "troop_reviews": 0, "troop_audits": 0, "troop_deliveries": 0,
                  "troop_delivered_vested": 0, "troop_delivered_final_n": 0, "troop_false_approvals": 0,
                  # 1.6.0: panels held by troops; the red team's withdrawals
                  "troop_panel_seats": 0, "withdrawn_unawarded": 0,
                  # 2.0.0: the demand side and the effort burned
                  "posts_unaffordable": 0, "posts_k_open": 0, "effort_burned": 0.0, "effort_unpaid": 0.0,
                  "crowd_arrived": 0, "crowd_departed": 0, "shock_created": 0.0,
                  "member_price_sum": 0.0, "member_price_n": 0, "troop_price_sum": 0.0, "troop_price_n": 0,
                  # 2.1.0: the marks and what the requesters did at them; the red team's readings
                  "marked_capacity": 0, "marked_credit": 0, "withdrawn_at_mark": 0, "reposted_after_mark": 0,
                  "state_rejections": 0, "troop_truth_redrawn": 0,
                  # 2.3.0: the supply side
                  "arrivals": 0, "departures": 0, "departed_cost_sum": 0.0, "nested_posted": 0, "nested_awarded": 0, "nested_unaffordable": 0,
                  "nested_self_executed": 0, "nested_judged": 0, "nested_false_approvals": 0, "nested_false_rejections": 0,
                  "nested_price_sum": 0.0, "nested_price_n": 0, "gain_sum": 0.0, "gain_vs_cost_sum": 0.0, "nested_award_refused": 0}
        self._awarded_last = 0
        self.marked: set[str] = set()                    # requests seen with a mark (counted once)
        self.repost_due: dict[str, int] = {}             # requester -> withdrawals not yet reposted
        self.omega0_total = self.w.money()["omega_total"]
        self.by_grade = {g: [0, 0] for g in GRADES}       # grade -> [cases, correct]
        # 1.5.0 §2.3: the route-and-kind reading
        self.pfa_upheld_by: list[tuple[str, int]] = []   # (auditor, tick assigned) of each upheld probation false approval
        self.pfa_overturned = 0
        self.pfa_other = 0
        self.susp_log: dict[str, list[int]] = {}         # actor -> ticks at which a suspension began
        self._susp_seen: dict[str, int | None] = {}
        # 1.5.0 §8.6 red team: careful members that offer for nothing and live on fees and uplift
        careful_ids = [aid for aid in ids if self.kind[aid] == CAREFUL]
        n_dec = round(len(careful_ids) * a.decline_awards)
        self.decliners = set(careful_ids[:n_dec])
        self.title_n = 0

    # -- populations -------------------------------------------------------------
    def verdict(self, reviewer: str, truth: bool) -> tuple[str, float]:
        """A stamper answers F at no cost. A careful reviewer answers the truth with probability a
        and pays its care cost, 2 or 3 credits of real resources — or as much of it as its unlocked
        credit can buy, when bonds locked in earlier reviews have left it short (the engine refuses
        an unaffordable purchase whole). Accuracy is a parameter of the disposition, not of the
        money spent; the shortfall is counted as `underfunded_careful_reviews`."""
        if self.kind[reviewer] == STAMPER:
            if self.a.stamper_mode == "reformer" and self.w.actor(reviewer).probation:
                pass                             # a reformer reviews carefully while on probation (1.3.0 §8 red team) ...
            else:
                if self.a.camouflage > 0 and self.rng.random() < self.a.camouflage:
                    return N, 0.0                # looks careful without looking (1.2.0 §8 red team)
                return F, 0.0
        right = self.rng.random() < self.a.accuracy
        v = F if (truth == right) else N
        want = float(self.rng.randint(2, 3))
        affordable = (self.w.unlocked(reviewer) if self.floating else self.w.unlocked(reviewer) * self.w.money()["v"]) - 1e-6   # 2.0.0: credits
        if affordable >= want:
            return v, want
        self.c["underfunded_careful_reviews"] += 1
        return v, max(0.0, math.floor(affordable * 100) / 100)

    def free_workers(self) -> list[str]:
        """Free, fundable, and — since 1.3.0 §2.1 — a member of the market; the engine refuses the rest. A decliner
        (1.5.0 §8.6) never offers."""
        out = []
        for aid in self.actors:
            if aid in self.decliners:
                continue
            ac = self.w.actor(aid)
            if not ac.on_duty and ac.committed is None and ac.open_review is None \
                    and (not self.p.membership or ac.is_member) \
                    and self.w.unlocked(aid) + 1e-9 >= max(1.0, -(-self.p.G_frac * self.a.beta // 1)):
                out.append(aid)
        return out

    def eligible_reviewers(self, cid: str, panel: bool = False) -> list[str]:
        """§7.1: on duty, fresh, free, able to fund the bond — and, since 1.2.0 §2.2, eligible by
        plant record for the tier: any review needs duty eligibility, a challenge-panel seat
        (audit, appeal, dispute review) panel eligibility. The engine refuses what this misses."""
        c = self.w.case(cid)
        out = []
        for aid in self.actors:
            ac = self.w.actor(aid)
            if ac.on_duty and ac.open_review is None and ac.committed is None and aid != c.actor \
                    and aid not in c.excluded and self.w.unlocked(aid) + 1e-9 >= c.G_V \
                    and (ac.panel_eligible if panel else ac.duty_eligible):
                out.append(aid)
        return out

    def pick_reviewer(self, el: list[str]) -> str:
        """§7.5: volunteers first (none in this run); otherwise round-robin among the eligible duty
        actors — the next eligible actor, in id order, after the one assigned last. `seeded` is the
        policy the first sweeps declared: a seeded random choice among the eligible."""
        if self.a.assignment == "seeded":
            return self.rng.choice(el)
        order = sorted(el, key=lambda s: int(s[1:]))
        after = [aid for aid in order if int(aid[1:]) > self.rr_last]
        chosen = (after or order)[0]
        self.rr_last = int(chosen[1:])
        return chosen

    def duty_funding(self):
        """Solvency (§18.1 q6): how many on-duty actors cannot fund the bond right now."""
        short = 0
        for aid in self.actors:
            ac = self.w.actor(aid)
            if ac.on_duty and self.w.unlocked(aid) + 1e-9 < self.a.gv:
                short += 1
        return short

    def select(self, offers: list[str]) -> str:
        """S_θ: score = ρ − λ·B/β with B = β; the κ tie band; then the lowest id."""
        lam, band = self.p.lam, self.p.band
        scored = [(self.w.actor(aid).rho - lam, aid) for aid in offers]
        best = max(s for s, _ in scored)
        tied = [aid for s, aid in scored if s >= best - band]
        return max(tied, key=lambda aid: (self.w.actor(aid).kappa, -int(aid[1:])))

    # -- 2.0.0: bids, the requester model, the crowd ----------------------------------
    def draw_cost(self) -> float:
        """2.3.0 §2.3: a log-normal around the anchor — median --c-d-median, σ --c-d-sigma, clipped; σ 0 is the one cost of 2.0.0–2.2.0."""
        a = self.a
        if a.c_d_sigma <= 0:
            return a.c_d
        x = a.c_d_median * math.exp(self.cost_rng.gauss(0.0, a.c_d_sigma))
        return round(min(a.c_d_clip[1], max(a.c_d_clip[0], x)), 4)

    def cost_now(self, aid: str) -> float:
        """An actor's effort cost in force: its own, scaled by the adaptive reservation when that variant is on."""
        return round(self.c_d_of[aid] * (self.c_d_now / self.a.c_d), 6)

    def bid_of(self, aid: str, beta: float) -> float:
        """2.0.0 §2.2: c_D (1 + m), or the ceiling under --bid ceiling (the 1.x behaviour); 2.3.0: the actor's own c_D."""
        if self.a.bid == "ceiling":
            return beta
        if aid in self.lowballers:
            return round(0.5 * self.cost_now(aid), 6)   # below cost, to win awards and ρ (2.0.0 §8.8)
        return round(self.cost_now(aid) * (1.0 + self.margin[aid]), 6)

    def median_cost(self, ids) -> float:
        xs = sorted(self.c_d_of[i] for i in ids if i in self.c_d_of)
        if not xs:
            return float("nan")
        n = len(xs)
        return xs[n // 2] if n % 2 else 0.5 * (xs[n // 2 - 1] + xs[n // 2])

    # -- 2.3.0 §2.5: the entry pool and exit, on the public view ---------------------
    def entry_step(self, t: int):
        a, w = self.a, self.w
        if a.entry_pool <= 0 or not self.rev11:
            return
        mk = w.market()
        window = [x for x in self.awards_window if x[0] > t - 50]
        awards = sum(x[1] for x in window)
        free_ticks = sum(max(1, x[2]) for x in window)
        rate = awards / free_ticks if free_ticks else 0.0           # awards a free member wins a tick
        ttm = mk.get("time_to_membership") or mk.get("time_to_membership_run") or 250.0
        left = max(0.0, (a.ticks - t - ttm) / max(1, a.ticks - t))  # the share of what is left of the run after the gate
        real = mk["P0"] / mk["P_t"] if mk["P_t"] > 0 else 1.0
        arrived = 0
        for cand in list(self.candidates):
            if arrived >= a.arrivals_per_tick:
                break
            expected = max(0.0, mk["B_bar"] - cand["cost"]) * rate * left * real
            if expected > a.reservation:
                name = cand["name"]
                w.arrive(name)
                self.candidates.remove(cand)
                self.actors.append(name)
                self.kind[name] = cand["kind"]
                self.c_d_of[name] = cand["cost"]
                self.margin[name], self.idle[name] = a.margin0, 0
                self.tally[name] = Tally()
                self.arrived.append(name)
                self.wealth_at_boundary[name] = w.wealth(name)
                self.c["arrivals"] += 1
                arrived += 1

    def exit_step(self, t: int):
        """At each period boundary: a member whose real earnings over the last period fell below the reservation for --exit-patience
        periods and that holds no live obligation departs; its wallet leaves M."""
        a, w = self.a, self.w
        if not self.rev11:
            return
        per = w.dial()["periods"]
        if len(per) <= self.periods_seen:
            return
        self.periods_seen = len(per)
        length = max(1, per[-1]["t"] - per[-1]["start"])
        real = self.p.P0 / w.market()["P_t"]
        members = [aid for aid in self.actors if w.actor(aid).is_member]
        self.boundary_cost_median.append((self.median_cost(members), self.median_cost(self.actors)))
        if a.entry_pool <= 0:
            return
        for aid in list(self.actors):
            ac = w.actor(aid)
            earned = (w.wealth(aid) - self.wealth_at_boundary.get(aid, w.wealth(aid))) * real / length
            self.wealth_at_boundary[aid] = w.wealth(aid)
            if ac.probation and ac.arrived_at is not None and ac.admitted_at is None:
                continue                                 # an arrival waits out its gate
            if earned < a.reservation:
                self.below_reservation[aid] = self.below_reservation.get(aid, 0) + 1
            else:
                self.below_reservation[aid] = 0
            if self.below_reservation[aid] >= a.exit_patience:
                try:
                    w.depart(aid)
                except RuleError:
                    continue                             # an obligation is live; it departs after
                self.actors.remove(aid)
                self.departed.append(aid)
                self.c["departures"] += 1
                self.c["departed_cost_sum"] += self.c_d_of[aid]

    # -- 2.3.0 §2.4: delegation -------------------------------------------------------
    def nested_overhead(self, beta_nested: float) -> float:
        """The parent's overhead on a child: the nested fee, the pots' expected net cost (a reviewer's cost and fee at the index), its care."""
        idx = self.w.market()["index"]
        pots = 4.5 * idx if self.a.nested_pots == "parent" else 0.0
        return self.p.omega_rate * self.w.dial()["m"] * beta_nested + pots + 2.0

    def expected_child_bid(self) -> float:
        if self.c["nested_price_n"]:
            return self.c["nested_price_sum"] / self.c["nested_price_n"]
        return self.median_cost(self.actors) * (1.0 + self.a.margin0)

    def delegation_step(self, t: int):
        a, w = self.a, self.w
        if a.delegation != "on" or not self.rev11:
            return
        # 1. a parent just awarded a root decides: delegate when its cost exceeds the expected child bid plus the overhead
        for cid in list(self.active):
            c = w.case(cid)
            if not c.is_root or c.state != "COMMITTED" or w.is_troop(c.actor) or cid in self.deleg_considered \
                    or c.children or t - c.t_award > 2:        # the world's clock runs a tick behind the driver's
                continue
            self.deleg_considered.add(cid)
            parent = c.actor
            cost = self.cost_now(parent)
            child_bid = self.expected_child_bid()
            beta_n = round(cost - self.nested_overhead(child_bid), 2)
            if beta_n <= 1.0 or child_bid > beta_n:
                continue
            try:
                nid = w.post_nested(cid, beta_n)
            except (RuleError, LedgerError):
                self.c["nested_unaffordable"] += 1
                continue
            self.nested_parent[nid] = cid
            self.parent_waiting[cid] = nid
            self.title_n += 1
            self.tasks[nid] = Task(nid, f"nested #{self.title_n}", fulfilled=self.rng.random() >= a.fail_rate)
            self.tasks[nid].nested = True
            self.active[nid] = True
            self.c["nested_posted"] += 1
            self.parent_delegated[parent] = self.parent_delegated.get(parent, 0) + 1
        # 2. children bid on open nested requests; a request unawarded for T_wait is withdrawn and the parent executes itself
        for nid in [x for x in self.active if x in self.nested_parent]:
            c = w.case(nid)
            if c.state != "AVAILABLE":
                continue
            root = w.case(self.nested_parent[nid])
            offers = [(aid, bid) for aid, bid in self.offers_for(nid) if aid != root.actor]
            if offers:
                actor, bid = self.select_bid(offers, c.beta)
                try:
                    w.award(nid, actor, bid, a.work_ticks)
                except (RuleError, LedgerError):
                    self.c["nested_award_refused"] += 1  # the 1.1.0 reading: the parent must fund ω unlocked at the award
                    continue
                self.margin[actor] = round(self.margin[actor] + a.margin_up, 6)
                self.idle[actor] = 0
                self.tally[actor].awards += 1
                self.c["nested_awarded"] += 1
                self.c["nested_price_sum"] += bid
                self.c["nested_price_n"] += 1
                self.c["gain_sum"] += root.B - bid - self.nested_overhead(bid) - 0.0      # against the parent's own cost below
                self.c["gain_vs_cost_sum"] += self.cost_now(root.actor) - bid - self.nested_overhead(bid)
            elif t - c.t_post >= self.p.T_wait:
                w.withdraw_unawarded(nid)
                self.active.pop(nid, None)
                self.parent_waiting.pop(self.nested_parent[nid], None)
                self.parent_self_exec.add(self.nested_parent[nid])
                self.c["nested_self_executed"] += 1
        # 3. the parent judges a submitted child by its disposition, spending its care
        for nid in [x for x in self.active if x in self.nested_parent]:
            c = w.case(nid)
            if c.state != "SUBMITTED":
                continue
            root = w.case(self.nested_parent[nid])
            parent = root.actor
            truth = self.tasks[nid].fulfilled
            if self.kind[parent] == STAMPER:
                v = F
            else:
                v = F if (truth == (self.rng.random() < a.accuracy)) else N
                have = max(0.0, math.floor((w.unlocked(parent) - 1e-6) * 100) / 100)
                pay = min(2.0, have)
                if pay > 0:
                    w.spend(parent, pay, self.nested_parent[nid])
                    self.c["effort_burned"] = round(self.c["effort_burned"] + pay, 6)
            w.judge_nested(nid, v)
            self.c["nested_judged"] += 1
            if v == F and not truth:
                self.c["nested_false_approvals"] += 1
                self.tasks[self.nested_parent[nid]].fulfilled = False      # the parent built on bad work (§9.2)
            if v == N and truth:
                self.c["nested_false_rejections"] += 1

    def offers_for(self, cid: str) -> list[tuple[str, float]]:
        """Free members whose bid is at or under the ceiling and who can fund the guarantee at it."""
        beta = self.w.case(cid).beta
        out = []
        for aid in self.free_members():
            bid = self.bid_of(aid, beta)
            if bid <= beta + 1e-9 and self.w.unlocked(aid) + 1e-9 >= max(1.0, math.ceil(self.p.G_frac * bid)):
                out.append((aid, bid))
        return out

    def free_members(self) -> list[str]:
        out = []
        for aid in self.actors:
            if aid in self.decliners:
                continue
            ac = self.w.actor(aid)
            if not ac.on_duty and ac.committed is None and ac.open_review is None and (not self.p.membership or ac.is_member):
                out.append(aid)
        return out

    def select_bid(self, offers: list[tuple[str, float]], beta: float) -> tuple[str, float]:
        """S_θ = ρ − λ B/β with the bid live; the κ tie band; then the lowest id."""
        lam, band = self.p.lam, self.p.band
        scored = [(self.w.actor(aid).rho - lam * bid / beta, aid, bid) for aid, bid in offers]
        best = max(sc for sc, _, _ in scored)
        tied = [(aid, bid) for sc, aid, bid in scored if sc >= best - band]
        return max(tied, key=lambda ab: (self.w.actor(ab[0]).kappa, -int(ab[0][1:])))

    def requester_posts(self, r: str, t: int):
        """2.0.0 §2.1 (the driver's declared policy): one request a tick while fewer than K_open are open and the all-in
        maximum fits the unlocked wallet, at β = min(β_max, share × unlocked)."""
        a, w = self.a, self.w
        open_n = sum(1 for cid in self.active if self.owner.get(cid) == r)
        k_open = a.k_open * 3 if r in self.small else a.k_open
        if k_open > 0 and open_n >= k_open:
            self.c["posts_k_open"] += 1
            return
        U = w.unlocked(r)
        mk = w.market()
        if a.ceiling_policy == "market":
            # run 13 §3 (the reviewer's demand-unbound cell): a market-aware ceiling — a little above the market price, so a
            # posting locks less than the wallet rule's and the requester posts more; the wallet still has to carry the all-in
            beta = math.floor(min(a.beta_max, a.ceiling_mult * mk["B_bar"]) * 100) / 100
        else:
            beta = math.floor(min(a.beta_max, a.ceiling_share * U) * 100) / 100
        if r in self.small:                               # 2.2.0 §8.5 red team: many small requests at the market price exactly
            beta = min(beta, math.ceil(mk["B_bar"] * 100) / 100)
        if r in self.stingy:                              # 2.0.0 §8.8: underbids the market and waits for a troop (expected: flagged, waits)
            beta = min(beta, math.floor(0.6 * mk["B_bar"] * 100) / 100)
        m = w.dial()["m"]
        all_in = beta + self.p.phi_root * mk["index"] + self.p.omega_rate * m * beta
        if beta < 1.0 or all_in > U + 1e-9:
            self.c["posts_unaffordable"] += 1
            return
        cid = w.post_root(r, beta)
        self.owner[cid] = r
        self.title_n += 1
        self.tasks[cid] = Task(cid, f"task #{self.title_n}", fulfilled=self.rng.random() >= a.fail_rate)
        self.active[cid] = True
        self.c["posted"] += 1
        if self.repost_due.get(r, 0) > 0:               # 2.1.0 §2.6: a posting after a withdrawal at the mark is a repost
            self.repost_due[r] -= 1
            self.c["reposted_after_mark"] += 1

    def raise_below_market(self):
        """2.0.0 §2.8: a requester whose request is below the market price raises it to the market price when it can. The
        engine's flag is set at posting; a request the market overtakes afterwards is below market too and would otherwise
        wait forever (no troop comes for β < B̄ and the members bid above it), so the policy reads the live condition."""
        w = self.w
        B_bar = w.market()["B_bar"]
        for cid in sorted(self.active, key=lambda s: int(s[1:])):
            c = w.case(cid)
            if c.state != "AVAILABLE" or c.beta + 1e-9 >= B_bar or self.owner.get(cid) in self.stingy:
                continue
            target = min(self.a.beta_max, math.ceil(B_bar * 100) / 100)
            if target <= c.beta + 1e-9:
                continue
            try:
                w.raise_ceiling(cid, target)
            except (RuleError, LedgerError):
                pass                                         # the wallet does not allow it yet; the flag stands

    def read_marks(self, t: int):
        """2.1.0 §2.6: every refusal is told — the request carries its mark in the public view. The declared policy: hold
        (default; nothing changes), or withdraw at the mark and repost (the next tick's posting; withdrawn before award, owed
        nothing). Each marked request is counted once by the kind of its first mark."""
        w = self.w
        for cid in sorted(self.active, key=lambda s: int(s[1:])):
            c = w.case(cid)
            if c.state != "AVAILABLE" or c.refused is None:
                continue
            if cid not in self.marked:
                self.marked.add(cid)
                self.c["marked_capacity" if c.refused == "capacity" else "marked_credit"] += 1
            if self.a.requester_on_refusal == "withdraw":
                owner = self.owner.get(cid)
                if owner in self.stingy or owner is None:
                    continue
                w.withdraw_unawarded(cid)
                self.active.pop(cid, None)
                self.c["withdrawn_at_mark"] += 1
                self.repost_due[owner] = self.repost_due.get(owner, 0) + 1

    def crowd_step(self, t: int):
        """A riot is a crowd (2.0.0 §2.1): n requesters arrive at --spike-from with the default wallet, post for
        --spike-ticks, and leave once their requests are served out — their wallets depart M (Appendix M)."""
        a, w = self.a, self.w
        if a.spike_requesters <= 0:
            return
        if t == a.spike_from:
            for i in range(1, a.spike_requesters + 1):
                name = f"C{i:02d}"
                w.add_requester(name, a.wallet)
                self.crowd.append(name)
                self.c["crowd_arrived"] += 1
            self.crowd_posting = True
        if t >= a.spike_from + a.spike_ticks:
            self.crowd_posting = False
            for name in list(self.crowd):
                if any(self.owner.get(cid) == name for cid in self.active):
                    continue
                try:
                    w.remove_requester(name)
                    self.crowd.remove(name)
                    self.c["crowd_departed"] += 1
                except RuleError:
                    pass                                     # a tree still open: next tick

    # -- one tick ----------------------------------------------------------------
    def stamper_share(self) -> float:
        return sum(1 for aid in self.actors if self.kind[aid] == STAMPER) / max(1, len(self.actors))

    def move_dispositions(self, t: int):
        """1.2.0 §8 runs 2 and 3. Drift: every `drift_every` ticks the stamper share rises by
        `drift_step` toward `drift_to`, careful actors re-drawn as stampers at random. Adaptive: every
        `adapt_every` ticks each actor compares the mean wealth of the two dispositions (public wallets)
        and, with probability `adapt_rate`, takes the richer one. Both are the driver's declared
        policies; the engine sees only verdicts."""
        a = self.a
        if a.drift_to > 0 and t >= a.drift_from and t % a.drift_every == 0:
            target = min(a.drift_to, self.stamper_share() + a.drift_step)
            want = round(target * len(self.actors))
            careful = [aid for aid in self.actors if self.kind[aid] == CAREFUL]
            while sum(1 for aid in self.actors if self.kind[aid] == STAMPER) < want and careful:
                aid = careful.pop(self.rng.randrange(len(careful)))
                self.kind[aid] = STAMPER
                self.c["disposition_switches"] += 1
        if a.adapt_rate > 0 and t % a.adapt_every == 0 and t > 0:
            by = {CAREFUL: [], STAMPER: []}
            for aid in self.actors:
                by[self.kind[aid]].append(self.w.wealth(aid))
            if by[CAREFUL] and by[STAMPER]:
                richer = CAREFUL if sum(by[CAREFUL]) / len(by[CAREFUL]) >= sum(by[STAMPER]) / len(by[STAMPER]) else STAMPER
                for aid in self.actors:
                    if self.kind[aid] != richer and self.rng.random() < a.adapt_rate:
                        self.kind[aid] = richer
                        self.c["disposition_switches"] += 1

    def tick(self, t: int):
        a, w = self.a, self.w
        self.move_dispositions(t)
        if self.floating:
            # 2.0.0: the margins decay while idle; the adaptive reservation follows the last period's price level
            if a.c_d_adaptive == "on":
                per = w.dial()["periods"]
                self.c_d_now = round(a.c_d * (per[-1]["P_level"] / self.p.P0 if per else 1.0), 6)
            for aid in self.free_members():
                # the margin falls by margin_down per idle_k idle ticks — continuously, margin_down / idle_k a tick, so a wait
                # of four ticks counts four (a threshold would lose the fraction and ratchet the margin up)
                self.idle[aid] += 1
                self.margin[aid] = max(0.0, round(self.margin[aid] - a.margin_down / a.idle_k, 6))
            # the deficit shock, once
            if a.create_amount > 0 and t == a.create_at:
                w.scenario_create(a.create_amount)
                self.c["shock_created"] += a.create_amount
            # the crowd arrives, posts, leaves
            self.crowd_step(t)
            for r in self.requesters + (self.crowd if self.crowd_posting else []):
                self.requester_posts(r, t)
            self.raise_below_market()
            self.read_marks(t)
            self.exit_step(t)                            # 2.3.0 §2.2: at a period boundary, below the reservation → depart
            self.entry_step(t)                           # 2.3.0 §2.1: the pool reads the view and arrives
            self.delegation_step(t)                      # 2.3.0 §2.4: parents delegate, children bid, parents judge
        # requester posts — the spike cell (run 11 §1): --spike-tasks a tick from --spike-from for --spike-ticks, then back
        tasks_now = 0 if self.floating else (a.spike_tasks if a.spike_tasks > 0 and a.spike_from <= t < a.spike_from + a.spike_ticks else a.tasks)
        for _ in range(tasks_now):
            if w.unlocked("H") < a.beta + self.p.phi_root + self.p.omega_rate * a.beta:
                break
            low = a.beta_low > 0 and self.rng.random() < a.beta_low_share       # 1.6.0 §8 red team: the below-market poster
            cid = w.post_root("H", a.beta_low if low else a.beta)
            self.owner[cid] = "H"
            self.title_n += 1
            self.tasks[cid] = Task(cid, f"task #{self.title_n}", fulfilled=self.rng.random() >= a.fail_rate)
            self.active[cid] = True
            self.c["posted"] += 1
        # 1.6.0 §8 red team: a requester that withdraws its late unawarded requests (expected: nothing owed, nothing gained)
        if a.withdraw_after > 0:
            for cid in sorted(self.active, key=lambda s: int(s[1:])):
                c = w.case(cid)
                if c.state == "AVAILABLE" and t - c.t_post >= a.withdraw_after:
                    w.withdraw_unawarded(cid)
                    self.c["withdrawn_unawarded"] += 1
                    self.active.pop(cid, None)
        # orchestrator awards
        for cid in sorted(self.active, key=lambda s: int(s[1:])):
            if w.case(cid).state != "AVAILABLE" or cid in self.nested_parent:
                continue
            if self.floating:
                # 2.0.0 §2.2: members bid; the award is at the bid; a request nobody bids under waits (the state's after w_A)
                if not self.free_members():
                    self.c["awards_unfilled_ticks"] += 1
                    break
                bids = self.offers_for(cid)
                if not bids:
                    continue
                beta = w.case(cid).beta
                actor, bid = self.select_bid(bids, beta)
                tau = a.work_ticks + (a.nested_tau if a.delegation == "on" and self.rev11 else 0)   # 2.3.0: room for a child
                w.award(cid, actor, bid, tau)
                self.parent_awards[actor] = self.parent_awards.get(actor, 0) + 1
                self.margin[actor] = round(self.margin[actor] + a.margin_up, 6)
                self.idle[actor] = 0
                self.tally[actor].awards += 1
                self.c["awarded"] += 1
                self.c["member_price_sum"] += bid
                self.c["member_price_n"] += 1
                continue
            offers = self.free_workers()
            if not offers:
                self.c["awards_unfilled_ticks"] += 1
                if self.p.membership and any(not w.actor(x).is_member and w.actor(x).committed is None and not w.actor(x).on_duty
                                             for x in self.actors):
                    self.c["awards_refused_members_only_ticks"] += 1
                break
            actor = self.select(offers)
            w.award(cid, actor, min(a.beta, w.case(cid).beta), a.work_ticks)
            self.tally[actor].awards += 1
            self.c["awarded"] += 1
        # actors work and submit
        for cid in list(self.active):
            c = w.case(cid)
            if c.state == "COMMITTED" and cid in self.parent_waiting:
                nid = self.parent_waiting[cid]
                child = w.case(nid)
                if child.t_verdict is None and child.state not in ("WITHDRAWN", "CANCELLED", "FINAL_N"):
                    continue                             # §9.1: the parent submits after its child's milestone
                self.parent_waiting.pop(cid, None)
                if child.verdict == N or child.state in ("WITHDRAWN", "CANCELLED", "FINAL_N"):
                    self.parent_self_exec.add(cid)       # the child failed: the parent does the work itself
            if c.state == "COMMITTED" and t >= c.t_award + min(a.work_ticks, c.tau) and cid not in self.parent_waiting:
                if self.floating and not w.is_troop(c.actor):
                    # 2.0.0 §2.2: the actor's effort, burned at submission (§4.6) — what its unlocked credit can pay of it
                    # 2.3.0: the actor's own cost; a parent that delegated and was served pays its care, not the work
                    delegated = c.is_root and c.children and cid not in self.parent_self_exec
                    want = 0.0 if delegated else self.cost_now(c.actor)
                    have = max(0.0, math.floor((w.unlocked(c.actor) - 1e-6) * 100) / 100)
                    pay = min(want, have)
                    if pay > 0:
                        w.spend(c.actor, pay, cid)
                        self.c["effort_burned"] = round(self.c["effort_burned"] + pay, 6)
                    if want - pay > 1e-9:
                        self.c["effort_unpaid"] = round(self.c["effort_unpaid"] + (want - pay), 6)
                if w.is_troop(c.actor) and a.troop_fail_rate is not None:
                    # 2.1.0 §8.9 red team: the state's deliveries made to fail at this rate — the truth re-drawn at the submission
                    self.tasks[cid].fulfilled = self.rng.random() >= a.troop_fail_rate
                    self.c["troop_truth_redrawn"] += 1
                w.submit(cid)
                if w.is_troop(c.actor):
                    self.c["troop_deliveries"] += 1
                    self.c["troop_price_sum"] += c.B
                    self.c["troop_price_n"] += 1
        # reviewers complete reviews assigned at an earlier tick
        for cid in list(self.active):
            c = w.case(cid)
            for rid in c.reviews:
                r = w.review(rid)
                if r.status == "open" and r.t_assign < t:
                    view = w.observe(r.reviewer, rid)
                    if w.is_troop(r.reviewer):
                        # 1.4.0 §2.1: the troop's declared disposition — the truth with probability 1 − ε_T, no cost
                        truth = self.tasks[cid].fulfilled
                        right = self.rng.random() >= a.eps_t
                        w.complete_review(rid, F if (truth == right) else N, 0.0)
                        self.c["troop_reviews"] += 1
                        if r.role == "audit":
                            self.c["troop_audits"] += 1
                        if r.role in ("audit", "appeal"):
                            self.c["troop_panel_seats"] += 1
                        continue
                    on_probation = w.actor(r.reviewer).probation
                    v, cost = self.verdict(r.reviewer, self.tasks[cid].fulfilled)
                    if r.reviewer in self.state_rejecters and w.is_troop(c.actor) and not self.tasks[cid].plant:
                        v = N                            # 2.1.0 §8.9 red team: rejects the state's work (reads the case's actor — declared)
                        self.c["state_rejections"] += 1
                    w.complete_review(rid, v, cost)
                    self.tally[r.reviewer].reviews += 1
                    if on_probation:
                        self.tally[r.reviewer].probation_reviews += 1
                        if v == F:
                            self.tally[r.reviewer].probation_approvals += 1
                            if not self.tasks[cid].fulfilled and not self.tasks[cid].plant:
                                self.tasks[cid].probation_false_approval = True
                    if r.role == "audit":
                        self.tally[r.reviewer].audits_done += 1
        # actors respond to N: accept, or appeal by the declared policy
        for cid in list(self.active):
            c = w.case(cid)
            if c.state != "AWAITING_RESPONSE":
                continue
            task = self.tasks[cid]
            if task.fulfilled:
                self.c["false_rejections_total"] += 1
            want = a.appeal_policy == "always" or (a.appeal_policy == "truthful" and task.fulfilled)
            if not c.is_root and a.delegation == "on" and task.fulfilled:
                want = True                              # 2.3.0 §2.4: a child rejected appeals truthfully (declared)
            if want and w.unlocked(c.actor) + 1e-9 < c.D:
                self.c["appeals_unfunded"] += 1
                want = False
            if want:
                w.respond(cid, "appeal", "the work meets the request")
                task.appealed = True
                self.c["appeals_filed"] += 1
                self.c["false_rejections_appealed" if task.fulfilled else "true_rejections_appealed"] += 1
            else:
                w.respond(cid, "accept")
        # orchestrator: the plants the rate calls for (1.2.0 §2.1), created before this tick's
        # assignments so they join the queue behind the real work submitted so far
        for _ in range(w.plants_due()):
            truth = self.rng.random() >= a.beta_p            # bad with probability β_P
            try:
                cid = w.create_plant(truth, (w.market()["P_t"] if self.floating else a.beta))   # 2.0.0: a plant at the price level
            except LedgerError:
                self.c["plants_unfunded"] += 1               # Ω's working capital is the cap; the engine counts the shortfall
                break
            self.title_n += 1
            self.tasks[cid] = Task(cid, f"plant #{self.title_n}", fulfilled=truth, plant=True)
            self.active[cid] = True
            self.c["plants_created"] += 1
            if not truth:
                self.c["plants_bad"] += 1
        # orchestrator: initial reviews, audits, appeal reviews, rulings
        for cid in sorted(self.active, key=lambda s: int(s[1:])):
            c = w.case(cid)
            task = self.tasks[cid]
            if c.state == "SUBMITTED" and not c.is_root:
                continue                                     # 2.3.0 §2.4: the parent judges its child (delegation_step)
            if c.state == "SUBMITTED" and not any(w.review(r).status == "open" for r in c.reviews):
                el = self.eligible_reviewers(cid)
                if el:
                    rid = w.assign_initial(cid, self.pick_reviewer(el))
                    self.review_owner[rid] = w.review(rid).reviewer
                else:
                    self.c["reviews_unassignable_ticks"] += 1
            if task.plant:
                continue                                     # no audit roll, no dispute: adjudicated by truth
            if c.state == "PENDING" and c.verdict == F and c.challenge is None and not task.dispute_rolled \
                    and a.dispute_policy != "none":
                task.dispute_rolled = True             # the requester acts once, before the audit roll
                pol = a.dispute_policy
                rate = 0.5 if pol == "half" else a.dispute_rate
                want = pol == "always" or (not task.fulfilled and pol in ("truthful", "half")
                                           and (rate >= 1.0 or self.rng.random() < rate))
                if want:
                    try:
                        w.dispute(cid, self.owner.get(cid, "H"), "the result does not meet the request")
                        task.disputed = True
                        task.audit_wanted = False
                        self.c["disputes_filed"] += 1
                        self.c["true_approvals_disputed" if task.fulfilled else "false_approvals_disputed"] += 1
                    except (RuleError, LedgerError):
                        self.c["disputes_refused"] += 1
                c = w.case(cid)
            if c.state == "PENDING" and c.verdict == F and c.challenge is None:
                if not task.audit_rolled and not c.audit_obligation:
                    task.audit_rolled = True
                    self.c["audits_rolled"] += 1
                    # 1.4.0 §2.2: the roll on the applied odds (1 for the state's own work); a yes is recorded as
                    # an obligation of the case and never dropped — a member takes it, or a troop after w_R
                    if self.rng.random() < w.audit_odds(cid):
                        w.roll_audit(cid)
                        task.audit_wanted = True
                        self.c["audit_obligations"] += 1
                elif c.market_audit_only and not task.audit_rolled:
                    task.audit_rolled, task.audit_wanted = True, True      # the engine recorded this one at the verdict
                if task.audit_wanted and (c.audit_obligation or c.audit_vacated):
                    el = self.eligible_reviewers(cid, panel=True)
                    if el:
                        rid = w.assign_audit(cid, self.pick_reviewer(el))
                        self.review_owner[rid] = w.review(rid).reviewer
                        task.audit_wanted = False
                        self.c["audits_assigned"] += 1
                    else:
                        self.c["audit_unassignable_ticks"] += 1
                elif task.audit_wanted:
                    task.audit_wanted = False                             # a troop took the seat
            ch = c.challenge
            if ch and not ch["resolved"]:
                if not task.appeal_wanted:
                    task.appeal_wanted = True
                    self.c["challenges"] += 1
                done = [w.review(r) for r in ch["reviews"] if w.review(r).status == "done"]
                if len(ch["reviews"]) < 2:
                    el = self.eligible_reviewers(cid, panel=True)
                    if el:
                        rid = w.assign_appeal(cid, self.pick_reviewer(el))
                        self.review_owner[rid] = w.review(rid).reviewer
                    else:
                        self.c["appeals_unassignable_ticks"] += 1
                elif len(done) == 2 and done[0].verdict != done[1].verdict:
                    truth = F if task.fulfilled else N
                    by_truth = self.rng.random() < a.ruling_accuracy
                    outcome = truth if by_truth else (N if truth == F else F)
                    w.rule(cid, outcome)
                    self.c["rulings"] += 1
                    if not by_truth:
                        self.c["rulings_wrong"] += 1
        self.c["duty_short_of_bond_ticks"] += self.duty_funding()
        self.awards_window.append((t, self.c["awarded"] - self._awarded_last, len(self.free_members())))
        self._awarded_last = self.c["awarded"]
        w.advance(t)
        self.harvest()
        for aid in self.actors:                           # 1.5.0 §2.3: when each suspension began
            s0 = w.actor(aid).susp_started
            if s0 is not None and s0 != self._susp_seen.get(aid):
                self._susp_seen[aid] = s0
                self.susp_log.setdefault(aid, []).append(s0)

    # -- bookkeeping from the public record ---------------------------------------
    def harvest(self):
        w = self.w
        for e in w.events_since(self.n_events):
            if e.dst in self.tally:
                ty = self.tally[e.dst]
                if e.kind == "escrow_out":
                    ty.delivery += e.amount
                elif e.kind == "feepot_out" and e.note.endswith("review fee"):
                    ty.fees += e.amount
                    ty.fee_fixed += e.amount
                elif e.kind == "fee_out" and e.note == "emission share":
                    ty.fees += e.amount
                elif e.kind == "transfer" and e.note == "duty uplift":
                    ty.fees += e.amount
                    ty.fee_uplift += e.amount
                elif e.kind in ("fee_out", "deposit_out", "feepot_out") or (e.kind == "transfer" and e.src == "OMEGA"):
                    ty.reimbursed += e.amount          # reimbursements, deferred ones, Ω advances and claims
            if e.src in self.tally:
                ty = self.tally[e.src]
                if e.kind == "purchase":
                    ty.costs += e.amount
                elif e.kind in ("forfeit_to", "burn_bond"):
                    if e.note.startswith("bond:"):
                        ty.bonds_forfeited += e.amount
                    elif e.note.startswith("G:"):
                        ty.guarantees_forfeited += e.amount
        self.n_events = w.n_events()
        for cid in list(self.active):
            c = w.case(cid)
            task = self.tasks[cid]
            if task.plant:
                # a plant leaves the queue once adjudicated and closed; its outcome is the reviewer's
                if c.plant_outcome is not None and c.tree_closed:
                    r = w.review(c.reviews[-1])
                    if c.plant_outcome == "spent":
                        self.c["plants_spent"] += 1
                    else:
                        self.tally[r.reviewer].plant_reviews += 1
                        if c.plant_outcome == "failure":
                            self.tally[r.reviewer].plant_failures += 1
                            self.c["plants_failed"] += 1
                            self.c["bad_plants_approved" if task.fulfilled is False else "good_plants_rejected"] += 1
                        else:
                            self.c["plants_stood"] += 1
                    # what the plant's pots paid reviewers is Ω's cost of the plant
                    self.c["omega_plant_spend"] = round(self.c["omega_plant_spend"] + (c.phi_E - c.allowance_refunded)
                                                        + (c.phi_F - c.pot_refunded), 6)
                    for rid in c.reviews:
                        if w.review(rid).status == "overturned":
                            self.tally[w.review(rid).reviewer].overturned += 1
                    if c.grade in self.by_grade:
                        self.by_grade[c.grade][0] += 1
                        self.by_grade[c.grade][1] += int((c.outcome_or_verdict() == F) == task.fulfilled)
                    self.active.pop(cid, None)
                continue
            if c.state in ("VESTED", "FINAL_N"):
                correct = (c.outcome_or_verdict() == F) == task.fulfilled
                if c.state == "VESTED":
                    self.c["vested"] += 1
                    if w.is_troop(c.actor):
                        self.c["troop_delivered_vested"] += 1
                    if not task.fulfilled:
                        self.c["false_approvals"] += 1
                        if task.probation_false_approval:
                            self.c["probation_false_approvals"] += 1
                            # 1.5.0 §2.3: the route — the pinned audit upheld it, or rejected it and the ruling overturned
                            audits = [w.review(x) for x in c.reviews if w.review(x).role == "audit"]
                            if any(r.status == "overturned" for r in audits):
                                self.pfa_overturned += 1
                            else:
                                upheld = [r for r in audits if r.verdict == F and r.status in ("done", "vested")]
                                if upheld:
                                    r = upheld[-1]
                                    self.pfa_upheld_by.append((r.reviewer, r.t_assign))
                                else:
                                    self.pfa_other += 1
                        if any(w.is_troop(w.review(x).reviewer) and w.review(x).role == "initial" for x in c.reviews):
                            self.c["troop_false_approvals"] += 1
                    if task.appealed:
                        self.c["appeals_won"] += 1
                        self.c["false_rejections_overturned" if task.fulfilled else "true_rejections_overturned"] += 1
                    if task.disputed:
                        self.c["disputes_lost"] += 1
                else:
                    self.c["final_n"] += 1
                    if w.is_troop(c.actor):
                        self.c["troop_delivered_final_n"] += 1
                    if task.fulfilled:
                        self.c["false_rejections"] += 1
                    if task.appealed:
                        self.c["appeals_lost"] += 1
                    if task.disputed:
                        self.c["disputes_won"] += 1
                        self.c["true_approvals_overturned" if task.fulfilled else "false_approvals_overturned"] += 1
                if c.grade in self.by_grade:
                    self.by_grade[c.grade][0] += 1
                    self.by_grade[c.grade][1] += int(correct)
                for rid in c.reviews:
                    r = w.review(rid)
                    if r.reviewer not in self.tally:
                        continue                                          # a troop's seat: the fund's, not a population's
                    if r.status == "overturned":
                        self.tally[r.reviewer].overturned += 1
                    elif r.status == "vested":
                        self.tally[r.reviewer].fee_haircut += max(0.0, r.fee_owed - r.fee_fixed)
                # root cases only in this run: the tree is the case, and it closes with it
                if c.tree_closed:
                    self.c["trees_closed"] += 1
                    self.c["omega_unrecovered_advances"] = round(self.c["omega_unrecovered_advances"] + c.omega_advance, 6)
                    self.c["allowance_refunded"] = round(self.c["allowance_refunded"] + c.allowance_refunded, 6)
                    self.c["pot_refunded"] = round(self.c["pot_refunded"] + c.pot_refunded, 6)
                self.active.pop(cid, None)

    # -- metrics row ---------------------------------------------------------------
    def row(self, t: int) -> dict:
        w = self.w
        row = {"t": t, "head": w.head()}
        for kind in (CAREFUL, STAMPER):
            ids = [aid for aid in self.actors if self.kind[aid] == kind]
            n = max(1, len(ids))
            T = [self.tally[aid] for aid in ids]
            row.update({
                f"{kind}_n": len(ids),
                f"{kind}_wealth": round(sum(w.wealth(aid) for aid in ids) / n, 3),
                f"{kind}_delivery": round(sum(x.delivery for x in T) / n, 3),
                f"{kind}_fees": round(sum(x.fees for x in T) / n, 3),
                f"{kind}_fee_fixed": round(sum(x.fee_fixed for x in T) / n, 3),
                f"{kind}_fee_haircut": round(sum(x.fee_haircut for x in T) / n, 3),
                f"{kind}_reimbursed": round(sum(x.reimbursed for x in T) / n, 3),
                f"{kind}_costs": round(sum(x.costs for x in T) / n, 3),
                f"{kind}_bonds_forfeited": round(sum(x.bonds_forfeited for x in T) / n, 3),
                f"{kind}_guarantees_forfeited": round(sum(x.guarantees_forfeited for x in T) / n, 3),
                f"{kind}_awards": round(sum(x.awards for x in T) / n, 3),
                f"{kind}_reviews": round(sum(x.reviews for x in T) / n, 3),
                f"{kind}_overturned": round(sum(x.overturned for x in T) / n, 3),
                f"{kind}_rho": round(sum(w.actor(aid).rho for aid in ids) / n, 4),
                f"{kind}_kappa": round(sum(w.actor(aid).kappa for aid in ids) / n, 3),
                f"{kind}_p_audit": round(sum(w.actor(aid).p_audit for aid in ids) / n, 4),
                f"{kind}_on_duty": sum(1 for aid in ids if w.actor(aid).on_duty),
                # 1.2.0: the plant record and its consequences, per population
                f"{kind}_plant_reviews": round(sum(x.plant_reviews for x in T) / n, 3),
                f"{kind}_plant_failures": round(sum(x.plant_failures for x in T) / n, 3),
                f"{kind}_a_hat": round(sum(w.actor(aid).a_hat for aid in ids) / n, 4),
                f"{kind}_suspended": sum(1 for aid in ids if w.actor(aid).suspended_until is not None),
                f"{kind}_probationers": sum(1 for aid in ids if w.actor(aid).probation),
                f"{kind}_members": sum(1 for aid in ids if w.actor(aid).is_member),
                f"{kind}_fee_uplift": round(sum(x.fee_uplift for x in T) / n, 3),
                f"{kind}_probation_reviews": round(sum(x.probation_reviews for x in T) / n, 3),
                f"{kind}_probation_approvals": round(sum(x.probation_approvals for x in T) / n, 3),
                f"{kind}_duty_eligible": sum(1 for aid in ids if w.actor(aid).duty_eligible),
                f"{kind}_panel_eligible": sum(1 for aid in ids if w.actor(aid).panel_eligible),
            })
        # 1.5.0 §8.6 red team: the decliners against the careful actors that offer
        dec = [aid for aid in self.actors if aid in self.decliners]
        off = [aid for aid in self.actors if self.kind[aid] == CAREFUL and aid not in self.decliners]
        row.update({"decliner_n": len(dec),
                    "decliner_wealth": round(sum(w.wealth(aid) for aid in dec) / max(1, len(dec)), 3),
                    "careful_offering_wealth": round(sum(w.wealth(aid) for aid in off) / max(1, len(off)), 3),
                    "decliner_awards": round(sum(self.tally[aid].awards for aid in dec) / max(1, len(dec)), 3),
                    "careful_offering_awards": round(sum(self.tally[aid].awards for aid in off) / max(1, len(off)), 3)})
        row.update(self.c)
        row["stamper_share"] = round(self.stamper_share(), 4)
        for g, (nn, ok) in self.by_grade.items():
            row[f"grade_{g}_n"] = nn
            row[f"grade_{g}_acc"] = round(ok / nn, 4) if nn else ""
        m = w.money()
        d = w.dial()
        last = d["periods"][-1] if d["periods"] else {}
        row.update({"M": round(m["M"], 3), "Res": round(m["Res"], 3), "v": round(m["v"], 6), "omega": round(m["omega"], 3),
                    "omega_total": round(m["omega_total"], 3), "omega_in_plants": round(m["omega_in_plants"], 3),
                    "omega_net": round(m["omega_total"] - self.omega0_total, 3),
                    "claims_outstanding": round(m["claims_outstanding"], 3),
                    "H_unlocked": round(sum(w.unlocked(r) for r in self.requesters) / max(1, len(self.requesters)), 3), "active_cases": len(self.active),
                    "m": round(d["m"], 4), "pi": round(d["pi"], 4), "X_t": d["X_t"], "on_duty": sum(1 for aid in self.actors if w.actor(aid).on_duty),
                    "F_hat": last.get("F_hat", ""), "periods": len(d["periods"]), "suspensions": d["suspensions"],
                    "alarms": d["alarms"], "eligibility_shortfall": d["eligibility_shortfall"],
                    "plant_shortfall": d["plant_shortfall"],
                    "member_seats": d["member_seats"], "readmissions": d["readmissions"],
                    "readmission_ticks_mean": round(d["readmission_ticks_mean"], 1) if d["readmission_ticks_mean"] else "",
                    "duty_fund": round(m["duty_fund"], 3), "fund_in": round(m["fund_in"], 3), "fund_out": round(m["fund_out"], 3),
                    # 1.7.0 §2.1: the troop account and Ω's record by source
                    "troop_account": round(m["troop_account"], 3), "troop_surplus": round(m["troop_surplus_paid"], 3),
                    "omega_fee_income": round(m["omega_fee_income"], 3), "advances_made": round(m["advances_made"], 3),
                    "advances_repaid": round(m["advances_repaid"], 3),
                    "members_on_duty": sum(1 for aid in self.actors if w.actor(aid).on_duty and w.actor(aid).is_member),
                    "probationers_on_duty": sum(1 for aid in self.actors if w.actor(aid).on_duty and w.actor(aid).probation),
                    # the trace of run 9's addendum: who is where, and what waits
                    "members_total": sum(1 for aid in self.actors if w.actor(aid).is_member),
                    "members_free": sum(1 for aid in self.actors if w.actor(aid).is_member and not w.actor(aid).on_duty
                                        and w.actor(aid).committed is None),
                    "members_committed": sum(1 for aid in self.actors if w.actor(aid).is_member and w.actor(aid).committed is not None),
                    "suspended_waiting": sum(1 for aid in self.actors if w.actor(aid).suspended_until is not None),
                    "probationers": sum(1 for aid in self.actors if w.actor(aid).probation),
                    "awards_waiting": sum(1 for cid in self.active if w.case(cid).state == "AVAILABLE")})
        tr = w.troops()
        row.update({"troops_active_reviews": tr["active_reviews"], "troops_active_deliveries": tr["active_deliveries"],
                    "troop_summons_reviews": tr["summons_reviews"], "troop_summons_deliveries": tr["summons_deliveries"],
                    "troop_shortfall_seats": tr["shortfall_seats"], "troop_shortfall_awards": tr["shortfall_awards"],
                    "troop_held_ticks": tr["held_ticks"], "troop_ticks_reviews": tr["troop_ticks_reviews"],
                    "awards_waiting_w_a": tr["awards_waiting_now"], "members_free_at_seating": tr["members_free_now"],
                    "awards_left_to_members": tr["awards_left_to_members"],
                    "troop_ticks_deliveries": tr["troop_ticks_deliveries"], "held_market_audit_now": tr["held_market_audit_now"],
                    "held_market_audit_max_age": tr["held_market_audit_max_age"], "fund_reserve": round(tr["fund_reserve"], 3),
                    "advance_outstanding": round(tr["advance_outstanding"], 3), "B_bar": round(tr["B_bar"], 3),
                    # 1.5.0 §2.1: the troop demand at the last seating, its refused component, and the peak's refused part
                    "troop_demand": round(tr["demand"], 3), "troop_demand_refused": round(tr["demand_refused"], 3),
                    "demand_peak_refused": round(tr["demand_peak_refused"], 3)})
        # 1.5.0 §2.3: how each probationer's false approval reached the customer — the route, then the auditor's kind
        # (classified now from what is known so far; the final row is the reading, since a record that later fails is
        # known only at the end)
        kinds = {"troop": 0, "standing": 0, "lag": 0, "readmitted": 0}
        for aid, t_audit in self.pfa_upheld_by:
            if w.is_troop(aid):
                kinds["troop"] += 1
            else:
                susp = self.susp_log.get(aid, [])
                if any(ts > t_audit for ts in susp):
                    kinds["lag"] += 1
                elif any(ts < t_audit for ts in susp):
                    kinds["readmitted"] += 1
                else:
                    kinds["standing"] += 1
        sv = w.service()
        served = sv["on_time"] + sv["late"]
        row.update({"on_time": sv["on_time"], "late": sv["late"], "on_time_share": round(sv["on_time"] / served, 4) if served else "",
                    "mean_lateness": round(sv["lateness_sum"] / sv["late"], 3) if sv["late"] else 0.0,
                    "rebates_owed": round(sv["rebates_owed"], 3), "rebates_paid": round(sv["rebates_paid"], 3),
                    "omega_liability": round(sv["liabilities_outstanding"], 3), "liabilities_accrued": round(sv["liabilities_accrued"], 3),
                    "liabilities_paid": round(sv["liabilities_paid"], 3), "liabilities_old": round(sv["liabilities_old"], 3),
                    "open_late": sv["open_late"],
                    "omega_unlocked": round(tr["omega_unlocked"], 3), "omega_min_period": round(tr["omega_min_period"], 3) if tr["omega_min_period"] is not None else "",
                    "plant_reserve": round(tr["plant_reserve"], 3), "x_target": tr["x_target"],
                    "waiting_initial": tr["waiting_initial"], "waiting_panel": tr["waiting_panel"],
                    "troop_panel_summons_period": tr["troop_panel_summons_period"],
                    "first_plant_adjudicated_at": tr["first_plant_adjudicated_at"] if tr["first_plant_adjudicated_at"] is not None else ""})
        # 2.0.0: the price level and the market price, the deficit, issuance and departures, the flags, the capacity case,
        # real wealth (W · P_0/P_t) and the demand side
        mk = w.market()
        real = mk["P0"] / mk["P_t"] if mk["P_t"] > 0 else 1.0
        reqs = [r for r in self.requesters]
        row.update({"P_t": round(mk["P_t"], 4), "price_index": round(mk["index"], 4), "credit_value": round(mk["v"], 4),
                    "deficit": round(mk["deficit"], 3), "deficit_created": round(mk["created"], 3), "deficit_retired": round(mk["retired"], 3),
                    "deficit_peak": round(mk["deficit_peak"], 3), "deficit_age": (t - mk["deficit_since"]) if mk["deficit_since"] is not None else 0,
                    "omega_net_position": round(mk["omega_net"], 3), "issued": round(mk["issued"], 3), "departed": round(mk["departed"], 3),
                    "below_market_flagged": mk["below_market_flagged"], "below_market_waiting": mk["below_market_waiting"],
                    "ceilings_raised": mk["ceilings_raised"], "places_held": mk["places_held"],
                    "refused_capacity_seats": mk["refused_capacity_seats"], "refused_capacity_awards": mk["refused_capacity_awards"],
                    "refused_capacity_waiting": mk["refused_capacity_waiting"], "capacity_wait_max": mk["capacity_wait_max"],
                    "careful_wealth_real": round(row["careful_wealth"] * real, 3), "stamper_wealth_real": round(row["stamper_wealth"] * real, 3),
                    "requester_wallet_mean": round(sum(w.wealth(r) for r in reqs) / max(1, len(reqs)), 3),
                    "requester_unlocked_mean": round(sum(w.unlocked(r) for r in reqs) / max(1, len(reqs)), 3),
                    "crowd_present": len(self.crowd),
                    "crowd_wallet_mean": round(sum(w.wealth(r) for r in self.crowd) / max(1, len(self.crowd)), 3) if self.crowd else 0.0,
                    "member_price_mean": round(self.c["member_price_sum"] / self.c["member_price_n"], 4) if self.c["member_price_n"] else "",
                    "troop_price_mean": round(self.c["troop_price_sum"] / self.c["troop_price_n"], 4) if self.c["troop_price_n"] else "",
                    "c_d_now": self.c_d_now,
                    "lowballer_n": len(self.lowballers),
                    "lowballer_wealth_real": round(sum(w.wealth(x) for x in self.lowballers) / max(1, len(self.lowballers)) * real, 3) if self.lowballers else "",
                    "lowballer_awards": round(sum(self.tally[x].awards for x in self.lowballers) / max(1, len(self.lowballers)), 3) if self.lowballers else "",
                    "lowballer_rho": round(sum(w.actor(x).rho for x in self.lowballers) / max(1, len(self.lowballers)), 4) if self.lowballers else "",
                    "stingy_n": len(self.stingy),
                    "stingy_open": sum(1 for cid in self.active if self.owner.get(cid) in self.stingy and w.case(cid).state == "AVAILABLE"),
                    "stingy_wallet_mean": round(sum(w.wealth(x) for x in self.stingy) / max(1, len(self.stingy)), 3) if self.stingy else "",
                    "margin_mean": round(sum(self.margin.values()) / max(1, len(self.margin)), 4)})
        # 2.1.0: the bank's books, the marks and the red team's readings
        bk = w.bank()
        row.update({"bank_on": int(bk["on"]), "loans_outstanding": round(bk["loans_outstanding"], 3), "loans_peak": round(bk["loans_peak"], 3),
                    "loans_open": bk["loans_open"], "debt": round(bk["debt"], 3), "debt_created": round(bk["debt_created"], 3),
                    "debt_repaid": round(bk["debt_repaid"], 3), "debt_peak": round(bk["debt_peak"], 3),
                    "debt_age": (t - bk["debt_since"]) if bk["debt_since"] is not None else 0,
                    "liabilities": round(bk["liabilities"], 3), "liabilities_n": bk["liabilities_n"], "liabilities_oldest": bk["liabilities_oldest"],
                    "wall": round(bk["wall"], 3) if bk["wall"] is not None else "", "wall_slack": round(bk["wall_slack"], 3) if bk["wall_slack"] is not None else "",
                    "omega_retained": round(bk["omega_retained"], 3), "omega_net_bank": round(bk["omega_net"], 3),
                    "omega_review_fee_income": round(bk["omega_review_fee_income"], 3),
                    "minted_issuance": round(bk["minted"]["issuance"], 3), "minted_emission": round(bk["minted"]["mint_emission"], 3),
                    "minted_plant": round(bk["minted"]["mint_plant"], 3), "minted_scenario": round(bk["minted"]["mint_scenario"], 3),
                    "minted_loan": round(bk["minted"]["loan"], 3), "destroyed_repayment": round(bk["destroyed"]["repayment"], 3),
                    "destroyed_plant": round(bk["destroyed"]["retire_plant"], 3), "cost_of_truth": round(bk["cost_of_truth"], 3),
                    "b_T": round(bk["b_T"], 4), "c_d_t_last": round(bk["last_c_d_t"], 3) if bk["last_c_d_t"] is not None else "",
                    "refused_credit_awards": mk["refused_credit_awards"], "refused_credit_seats": mk["refused_credit_seats"],
                    "refused_waiting_capacity": mk["refused_waiting"]["capacity"], "refused_waiting_credit": mk["refused_waiting"]["credit"],
                    "marked_capacity": self.c["marked_capacity"], "marked_credit": self.c["marked_credit"],
                    "withdrawn_at_mark": self.c["withdrawn_at_mark"], "reposted_after_mark": self.c["reposted_after_mark"],
                    "state_rejections": self.c["state_rejections"], "troop_truth_redrawn": self.c["troop_truth_redrawn"],
                    # 2.2.0: the rebate from income
                    "pool_on": int(sv["pool_on"]), "pool": round(sv["pool"], 3), "claims_period": round(sv["claims_period"], 3),
                    "rebates_forgone": round(sv["rebates_forgone"], 3), "forgone_share": round(sv["forgone_share"], 4),
                    "forgone_share_period": round(sv["forgone_share_period"], 4), "omega_retained_period": round(sv["omega_retained_period"], 3),
                    "small_requesters_wallet": round(sum(w.wealth(x) for x in self.small) / max(1, len(self.small)), 3) if self.small else "",
                    "small_requesters_rebates": round(sum(w.case(cid).rebate_paid for cid in self.owner if self.owner[cid] in self.small), 3) if self.small else ""})
        # 2.3.0: the supply side — the population, the gate, the costs (the driver's own), delegation
        members = [aid for aid in self.actors if w.actor(aid).is_member]
        brokers = [p for p, n in self.parent_delegated.items() if p in self.c_d_of and self.parent_awards.get(p, 0) >= 5
                   and n > 0.5 * self.parent_awards.get(p, 0)]
        cost_rank = sorted(self.c_d_of[x] for x in self.actors if x in self.c_d_of)
        rank = lambda x: (cost_rank.index(self.c_d_of[x]) + 1) / max(1, len(cost_rank))
        nested_vested = sum(1 for nid in self.nested_parent if w.case(nid).state == "VESTED")
        nested_final_n = sum(1 for nid in self.nested_parent if w.case(nid).state == "FINAL_N")
        row.update({"actors_n": len(self.actors), "members_total": mk.get("members_total", len(members)), "probationers": mk.get("probationers", 0),
                    "arrivals": self.c["arrivals"], "admissions": mk.get("admissions", 0), "departures": self.c["departures"],
                    "candidates_left": len(self.candidates),
                    "time_to_membership": round(mk["time_to_membership_run"], 2) if mk.get("time_to_membership_run") else "",
                    "members_median_cost": round(self.median_cost(members), 3) if members else "",
                    "population_median_cost": round(self.median_cost(self.actors), 3) if self.actors else "",
                    "departed_median_cost": round(self.median_cost(self.departed), 3) if self.departed else "",
                    "arrived_median_cost": round(self.median_cost(self.arrived), 3) if self.arrived else "",
                    "careful_median_cost": round(self.median_cost([x for x in self.actors if self.kind[x] == CAREFUL]), 3) if self.actors else "",
                    "nested_posted": self.c["nested_posted"], "nested_awarded": self.c["nested_awarded"], "nested_unaffordable": self.c["nested_unaffordable"],
                    "nested_self_executed": self.c["nested_self_executed"], "nested_vested": nested_vested, "nested_final_n": nested_final_n,
                    "nested_award_refused": self.c["nested_award_refused"],
                    "nested_share": round(self.c["nested_posted"] / max(1, self.c["awarded"]), 4),
                    "nested_price_mean": round(self.c["nested_price_sum"] / self.c["nested_price_n"], 3) if self.c["nested_price_n"] else "",
                    "gain_from_trade_mean": round(self.c["gain_vs_cost_sum"] / self.c["nested_price_n"], 3) if self.c["nested_price_n"] else "",
                    "nested_false_approvals": self.c["nested_false_approvals"], "nested_false_rejections": self.c["nested_false_rejections"],
                    "brokers_n": len(brokers), "brokers_cost_rank": round(sum(rank(b) for b in brokers) / len(brokers), 3) if brokers else "",
                    "brokers_award_share": round(sum(self.parent_awards.get(b, 0) for b in brokers) / max(1, self.c["awarded"]), 4),
                    "pool_advances": round(mk.get("pool_advances", 0.0), 3),
                    "hoards_over_M": round(sum(w.wealth(x) for x in self.actors) / max(1e-9, mk["M"]), 4)})
        row.update({"pfa_route_upheld": len(self.pfa_upheld_by), "pfa_route_overturned": self.pfa_overturned,
                    "pfa_route_other": self.pfa_other, "pfa_kind_troop": kinds["troop"], "pfa_kind_standing": kinds["standing"],
                    "pfa_kind_lag": kinds["lag"], "pfa_kind_readmitted": kinds["readmitted"]})
        return row


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--actors", type=int, default=20)
    ap.add_argument("--on-duty", type=int, default=4)
    ap.add_argument("--ticks", type=int, default=1000)
    ap.add_argument("--tasks", type=int, default=3, help="root tasks posted per tick")
    ap.add_argument("--beta", type=float, default=20.0)
    ap.add_argument("--work-ticks", type=int, default=2)
    ap.add_argument("--stampers", type=float, default=0.5, help="fraction of actors whose disposition is stamper")
    ap.add_argument("--accuracy", type=float, default=0.95, help="careful reviewer: P(verdict = truth)")
    ap.add_argument("--fail-rate", type=float, default=0.2, help="b: P(task is truly unfulfilled)")
    ap.add_argument("--ruling-accuracy", type=float, default=0.8, help="r: P(orchestrator rules by the truth)")
    ap.add_argument("--p-start", type=float, default=1.0, help="a newcomer's audit odds (1.2.0 §2.4: 1.0; 1.1.0: 0.5)")
    ap.add_argument("--p-cap", type=float, default=1.0, help="the audit odds' cap on doubling (1.2.0 §2.4: 1.0; 1.1.0: 0.5)")
    ap.add_argument("--p-floor", type=float, default=0.2, help="the audit rate's floor (§8.3)")
    ap.add_argument("--rules", choices=["2.3.0", "2.2.0", "2.1.0", "2.0.0", "1.7.1", "1.7.0", "1.6.0", "1.5.0", "1.4.0", "1.3.0", "1.2.0", "1.1.0"], default="2.3.0",
                    help="2.3.0: the supply side (entry and exit, the parent's pots, the reviewer advance from the pool); 2.2.0: the rebate from income (the period's fee pool, claims pro rata at the close, the rest forgone); 2.1.0: the bank with the liability stock (the control); 2.1.0 also: the bank (loans, the debt, the wall, the expected cost, P_t once a period, refusals told); 2.0.0: the price of work with "
                         "Ω's creation and retirement (the control); 1.7.1 (= 1.7.0): the fixed-price control — "
                         "one bottomless requester at β, the backing, the reserves; 1.6.0: the merged fund (uplift from troop earnings) and the half cap; 1.5.0: also the five 1.6.0 rules off; "
                         "1.3.0: troops off; 1.2.0: also membership, the duty fund and netted plant capital off; 1.1.0: also no "
                         "plants, dial off, p_start = p_cap = 0.5, Ω float 20 — declared controls. The audit obligation holds in all")
    ap.add_argument("--troops", choices=["on", "off"], default="on", help="the orchestrator's troops (1.4.0)")
    # 1.6.0: one flag per rule (all on under --rules 1.6.0; --rules 1.5.0 and earlier turn them off together)
    ap.add_argument("--clock", choices=["on", "off"], default="on", help="1.6.0 §2.1 the service clock and the orchestrator's rebate")
    ap.add_argument("--t-s", type=int, default=8, help="T_s, the service target in ticks (posting to first verdict)")
    ap.add_argument("--backing", choices=["on", "off"], default="on", help="1.6.0 §2.2 Ω backs the fund above the plant reserve; A_T removed")
    ap.add_argument("--seat-queue", choices=["on", "off"], default="on", help="1.6.0 §2.3 the reserve at least the reviews waiting")
    ap.add_argument("--panel-determined", choices=["on", "off"], default="on", help="1.6.0 §2.4 a panel seat needs a determined record")
    ap.add_argument("--reserve-periods", type=int, choices=[1, 2], default=2, help="1.6.0 §2.5 R_T over this and the previous period")
    ap.add_argument("--duty-cap", choices=["half", "twothirds", "all"], default=None,
                    help="the members' duty cap as a share of E_t: two thirds under 1.7.0 (§2.3), half under --rules 1.6.0 and earlier; its own knob for the OFAT cells")
    # 1.7.0: the troop account behind its flag; the take swept with the rebate pinned
    ap.add_argument("--accounts", choices=["on", "off"], default="on",
                    help="1.7.0 §2.1 the troop account beside the uplift fund (off: the 1.4.0–1.6.0 merged fund, uplift from troop earnings)")
    ap.add_argument("--omega-rate", type=float, default=0.05, help="ω₀, the base service fee as a share of B (1.7.0 §2.4 sweeps 0.05, 0.10, 0.15)")
    ap.add_argument("--r-s", type=float, default=0.0, help="r_s, the rebate a tick late (0 = ω₀B, the 1.6.0 default; 1.7.0 §2.4 pins 1 for the ω₀ sweep)")
    ap.add_argument("--t-susp", type=int, default=100, help="T_susp, the suspension length before probation (1.3.0 Appendix A: 100; run 9's addendum sweeps 0, 50, 100)")
    ap.add_argument("--theta-panel", type=float, default=0.20, help="θ_panel, the panel tier's bad-plant approval threshold (1.6.0 §8 sweeps 0.15)")
    ap.add_argument("--record-window", type=int, default=20, help="n_P, the plant record's trailing window (1.6.0 §8 sweeps 12)")
    ap.add_argument("--withdraw-after", type=int, default=0,
                    help="1.6.0 §8 red team: H withdraws an unawarded request older than this many ticks (0: never)")
    ap.add_argument("--plant-reserve", choices=["life", "period"], default="life",
                    help="1.6.0 §2.2 the plant reserve's horizon: a plant's life (W + T_review; the implementer's reading) or the ticks remaining in the period (the text's literal formula)")
    ap.add_argument("--beta-low", type=float, default=0.0, help="1.6.0 §8 red team: a share of requests posted at this lower ceiling (0: none)")
    ap.add_argument("--beta-low-share", type=float, default=0.0, help="the share of requests posted at --beta-low")
    ap.add_argument("--decline-awards", type=float, default=0.0,
                    help="1.5.0 §8.6 red team: the share of careful actors that offer for nothing and live on fees and uplift")
    ap.add_argument("--eps-t", type=float, default=0.05, help="ε_T, a troop reviewer's error rate (declared)")
    ap.add_argument("--w-r", type=int, default=2, help="w_R, ticks a review seat waits before a troop takes it")
    ap.add_argument("--w-a", type=int, default=2, help="w_A, ticks a request waits unawarded before a troop delivers it")
    ap.add_argument("--c-t", type=float, default=3.0, help="c_T, a troop review's cost to the fund")
    ap.add_argument("--c-d-t", type=float, default=10.0, help="c^D_T, a troop delivery's cost to the fund")
    ap.add_argument("--a-t", type=float, default=100.0, help="A_T, Ω's advance to the fund, outstanding at most")
    ap.add_argument("--fund", choices=["on", "off"], default="on", help="the duty fund (1.3.0 §2.4)")
    ap.add_argument("--m-max", type=float, default=4.0, help="m_max, the dial's cap (1.3.0 §2.6 sweeps 2 against 4)")
    ap.add_argument("--stamper-mode", choices=["plain", "reformer"], default="plain",
                    help="reformer: a stamper reviews carefully while on probation and stamps again once readmitted (1.3.0 §8)")
    ap.add_argument("--pi0", type=float, default=0.10, help="π_0, plants per real initial review at m = 1 (0: no plants)")
    ap.add_argument("--dial", choices=["on", "off"], default="on", help="the effort dial (off: m_t = 1, X_t = X fixed)")
    ap.add_argument("--beta-p", type=float, default=0.75, help="β_P, the share of plants that are bad")
    ap.add_argument("--camouflage", type=float, default=0.0,
                    help="red team (1.2.0 §8): a stamper answers N on this fraction of its reviews at random")
    ap.add_argument("--omega0", type=float, default=300.0, help="Ω's cold-start float (1.2.0 Appendix A: 300)")
    ap.add_argument("--drift-to", type=float, default=0.0,
                    help="1.2.0 §8 run 2: raise the stamper share toward this value (0: no drift)")
    ap.add_argument("--drift-every", type=int, default=100, help="ticks between drift steps")
    ap.add_argument("--drift-from", type=int, default=0, help="the tick drift begins (run 11's capture wave: a quiet market first)")
    ap.add_argument("--spike-tasks", type=int, default=0, help="run 11's demand spike: tasks a tick during the spike (0: none)")
    ap.add_argument("--spike-from", type=int, default=400, help="the spike's first tick")
    ap.add_argument("--spike-ticks", type=int, default=50, help="the spike's length in ticks")
    ap.add_argument("--drift-step", type=float, default=0.05, help="stamper share added per drift step")
    ap.add_argument("--adapt-rate", type=float, default=0.0,
                    help="1.2.0 §8 run 3: probability per adaptation step that an actor takes the richer disposition (0: fixed)")
    ap.add_argument("--adapt-every", type=int, default=100, help="ticks between adaptation steps")
    ap.add_argument("--assignment", choices=["round-robin", "seeded"], default="round-robin",
                    help="choice among eligible duty actors: round-robin (§7.5) or seeded random (the first sweeps' declared policy)")
    ap.add_argument("--dispute-rate", type=float, default=1.0,
                    help="with --dispute-policy truthful: the probability H disputes a given false approval (1 = every one)")
    ap.add_argument("--dispute-policy", choices=["none", "truthful", "half", "always"], default="none",
                    help="H's response to a pending F: none; truthful = dispute when the work truly failed; half = the same "
                         "with probability 0.5; always = dispute every pending F (H pays D)")
    ap.add_argument("--appeal-policy", choices=["none", "truthful", "always"], default="none",
                    help="the actor's response to an N: none = accept; truthful = appeal when the work is truly fulfilled; "
                         "always = appeal every N (the court fee D is paid when the actor can fund it)")
    ap.add_argument("--band", type=float, default=0.05, help="the κ tie band of selection (§5.2)")
    ap.add_argument("--gv", type=float, default=5.0, help="G^V, the reviewer bond")
    ap.add_argument("--fee", type=float, default=2.0, help="f, the ordinary-review fee (1.1.0 §4.3); appeal/audit pay 1.5 f")
    ap.add_argument("--phi-e", type=float, default=10.0, help="φ^E, the expense allowance of a root request")
    ap.add_argument("--phi-f", type=float, default=5.0, help="φ^F, the fee pot of a root request")
    # 2.0.0: the demand side, the bids, the state at cost, the capacity, the shock, the crowd
    ap.add_argument("--requesters", type=int, default=6, help="2.0.0 §2.9: the standing requesters")
    ap.add_argument("--wallet", type=float, default=200.0, help="a requester's initial wallet (the crowd's too)")
    ap.add_argument("--issuance", type=float, default=10.0, help="credits a tick issued to each requester (swept 15)")
    ap.add_argument("--beta-max", type=float, default=40.0, help="β_max, the ceiling policy's cap")
    ap.add_argument("--ceiling-share", type=float, default=1.0 / 3.0, help="s: β = min(β_max, s × unlocked wallet)")
    ap.add_argument("--k-open", type=int, default=5, help="K_open: a requester posts while fewer than this many of its requests are open (0: no limit)")
    ap.add_argument("--ceiling-policy", choices=["wallet", "market"], default="wallet",
                    help="the requesters' ceiling: min(β_max, share × unlocked wallet), or market-aware min(β_max, mult × B̄) (run 13 §3)")
    ap.add_argument("--ceiling-mult", type=float, default=1.2, help="the market-aware ceiling's multiple of B̄")
    ap.add_argument("--bid", choices=["margin", "ceiling"], default="margin", help="members' bid policy: c_D (1 + m), or at the ceiling (the 1.x behaviour, the control)")
    ap.add_argument("--c-d", type=float, default=8.0, help="c_D, a member's nominal effort cost per task (burned at submission)")
    ap.add_argument("--c-d-adaptive", choices=["on", "off"], default="off", help="the adaptive reservation: c_D follows P_t with a one-period lag (the spiral, swept)")
    ap.add_argument("--margin0", type=float, default=0.3, help="each member's starting margin m")
    ap.add_argument("--margin-up", type=float, default=0.3, help="m rises by this on each award")
    ap.add_argument("--margin-down", type=float, default=0.25, help="m falls by this per --idle-k idle ticks (margin_down / idle_k a tick), floored at 0")
    ap.add_argument("--idle-k", type=int, default=3, help="k: idle ticks before the margin falls")
    ap.add_argument("--lam", type=float, default=0.2, help="λ, price against reputation in selection (swept 0.5)")
    ap.add_argument("--c-d-t-mode", choices=["expected", "at_cost", "cost", "half"], default=None,
                    help="the state's burn: expected (2.1.0: (1 − b_T) B̄ − b_T G, floored), at_cost (= cost; 2.0.0: B̄), half (0.5 P_t, the 1.x margin); "
                         "default expected under 2.1.0, at_cost under 2.0.0")
    ap.add_argument("--b-t-prior", type=float, default=0.2, help="2.1.0 §2.2: b_T until the state has closed --b-t-min-n deliveries (§8.8 sweeps 0.1 / 0.3)")
    ap.add_argument("--b-t-min-n", type=int, default=10, help="2.1.0 §2.2: the state's deliveries a period must have closed for its own rate (else trailing back)")
    ap.add_argument("--debt-bound-periods", type=int, default=1, help="2.1.0 §2.4: the wall, in closed periods of Ω's fee income (0 unbounded, the control; §8.8 sweeps 2)")
    ap.add_argument("--requester-on-refusal", choices=["hold", "withdraw"], default="hold",
                    help="2.1.0 §2.6: what a requester does at a refusal's mark — hold (default) or withdraw and repost (the §8.6 variant; the §8.9 rebate farmer)")
    ap.add_argument("--troop-fail-rate", type=float, default=None,
                    help="2.1.0 §8.9 red team: the state's deliveries re-drawn to fail at this rate at the troop's submission (0.5, 0.75; default: the task's own truth)")
    # 2.3.0: competence, the entry pool, delegation
    ap.add_argument("--c-d-sigma", type=float, default=0.43, help="2.3.0 §2.3: σ of the log-normal effort cost (0: one cost; swept 0.2 / 0.43 / 0.8)")
    ap.add_argument("--c-d-median", type=float, default=8.0, help="the cost distribution's median (the anchor)")
    ap.add_argument("--c-d-clip", type=float, nargs=2, default=[2.0, 40.0], help="the cost distribution's clip")
    ap.add_argument("--entry-pool", type=int, default=0, help="2.3.0 §2.5: candidates reading the view (0: a fixed population; the §8 cells use 20)")
    ap.add_argument("--entry-stampers", type=float, default=0.0, help="the share of candidates that are stampers (the §8.7 swarm)")
    ap.add_argument("--reservation", type=float, default=0.8, help="r: real earnings a tick below which a candidate stays out and a member leaves (swept 0.5 / 1.2)")
    ap.add_argument("--arrivals-per-tick", type=int, default=1, help="at most this many arrivals a tick (swept 3)")
    ap.add_argument("--exit-patience", type=int, default=1, help="periods below the reservation before a member departs")
    ap.add_argument("--f0", type=float, default=50.0, help="F_0, an arrival's float at P_0 (swept 0)")
    ap.add_argument("--delegation", choices=["on", "off"], default="off", help="2.3.0 §2.4: parents delegate when their cost exceeds the expected child's bid plus the overhead")
    ap.add_argument("--nested-tau", type=int, default=6, help="the extra ticks a member's bid carries under delegation, for a child's work")
    ap.add_argument("--nested-pots", choices=["parent", "root"], default="parent", help="2.3.0 §2.4: the parent posts the nested pots; root = the 1.1.0 reading (the control)")
    ap.add_argument("--small-requests", type=int, default=0,
                    help="2.2.0 §8.5 red team: this many requesters post at the market price exactly with K_open tripled — many small requests to collect pro-rata rebates (expected: nothing beyond the capped claims)")
    ap.add_argument("--state-rejecters", type=float, default=0.0,
                    help="2.1.0 §8.9 red team: the share of careful actors that reject every delivery of the state's (reads the case's actor — declared non-conforming)")
    ap.add_argument("--n-t", type=int, default=40, help="N_T, the most troops ELEF can field at once (0 = unbounded, the control)")
    ap.add_argument("--create-at", type=int, default=0, help="the deficit shock's tick (with --create-amount)")
    ap.add_argument("--create-amount", type=float, default=0.0, help="the deficit shock: Ω creates this and pays it to the requesters (0: none)")
    ap.add_argument("--spike-requesters", type=int, default=0, help="a riot as a crowd: this many requesters arrive at --spike-from for --spike-ticks (0: none)")
    ap.add_argument("--lowball-share", type=float, default=0.0, help="2.0.0 §8.8 red team: the share of actors that bid half their cost to win reputation")
    ap.add_argument("--stingy-requesters", type=int, default=0, help="2.0.0 §8.8 red team: this many requesters post at 0.6 B̄ and never raise (expected: flagged, wait)")
    ap.add_argument("--bbar-troops", choices=["on", "off"], default="off", help="2.0.0 §8.8 control: count troop awards in B̄ (the rule excludes them)")
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--res0", type=float, default=1e7)
    ap.add_argument("--human-budget", type=float, default=1e6)
    ap.add_argument("--record-dir", default=None)
    ap.add_argument("--log-every", type=int, default=10)
    ap.add_argument("--name", default=None)
    ap.add_argument("--expect-head", default=None)
    ap.add_argument("--results-root", default=None, help="write results/runs under this directory instead of results/")
    a = ap.parse_args(argv)
    if a.c_d_t_mode is None:
        a.c_d_t_mode = "expected" if a.rules in ("2.1.0", "2.2.0", "2.3.0") else "cost"
    if a.rules != "2.3.0":
        a.c_d_sigma = 0.0                                # one cost before 2.3.0: the controls are run 15's cells

    name = a.name or f"stamping-s{a.stampers:g}-p{a.p_start:g}-gv{a.gv:g}-b{a.fail_rate:g}-f{a.fee:g}-X{a.on_duty}-seed{a.seed}"
    run = Stamping(a)
    rec = RunRecorder(name, kind="scoped run — §18.1 q1 careful vs careless review; policies fixed by disposition",
                      params=run.p, **({"root": a.results_root} if a.results_root else {}),
                      declared={"actors": a.actors, "on_duty": a.on_duty, "ticks": a.ticks, "tasks_per_tick": a.tasks,
                                "spike": None if a.spike_tasks == 0 else {"tasks": a.spike_tasks, "from": a.spike_from, "ticks": a.spike_ticks},
                                "beta": a.beta, "work_ticks": a.work_ticks, "seed": a.seed,
                                "rules": a.rules, "fund": a.fund if a.rules in ("1.3.0", "1.4.0", "1.5.0", "1.6.0") else "n/a", "m_max": a.m_max,
                                "troops": {"spec": "1.4.0 design revision 4 — the orchestrator's troops" if a.rules in ("1.4.0", "1.5.0", "1.6.0") and a.troops == "on" else "off",
                                           "reserve": ("1.5.0 design revision 5 — the reserve is sized to the need: R_T is the current period's peak "
                                                       "troop demand, held plus refused for funds" if a.rules in ("1.5.0", "1.6.0") else
                                                       "1.4.0: the peak capital carried over this period and the previous one"),
                                           "eps_T": a.eps_t, "w_R": a.w_r, "w_A": a.w_a, "c_T": a.c_t, "c_D_T": a.c_d_t, "A_T": a.a_t,
                                           "disposition": "the truth with probability 1 − ε_T; delivery fails at b as any; no cost at completion",
                                           "summons": "the engine's, at the seating step; the driver supplies the verdict and the submission"},
                                "audit_roll": "on the engine's applied odds (audit_odds); a yes is recorded as an obligation (roll_audit) and never dropped",
                                "stamper_mode": a.stamper_mode,
                                "decline_awards": {"share_of_careful": a.decline_awards, "decliners": sorted(run.decliners)},
                                "auto_scale": {"spec": "1.6.0 design revision 6 — auto-scale" if a.rules == "1.6.0" else "off (control)",
                                               "service_clock": a.clock if a.rules == "1.6.0" else "off", "T_s": a.t_s,
                                               "omega_backs_fund": a.backing if a.rules == "1.6.0" else "off (A_T binds)",
                                               "seat_the_queue": a.seat_queue if a.rules == "1.6.0" else "off",
                                               "panel_determined": a.panel_determined if a.rules == "1.6.0" else "off",
                                               "reserve_periods": a.reserve_periods if a.rules == "1.6.0" else 1,
                                               "duty_cap": a.duty_cap, "plant_reserve_horizon": a.plant_reserve,
                                               "theta_panel": a.theta_panel, "record_window": a.record_window, "withdraw_after": a.withdraw_after,
                                               "beta_low": a.beta_low, "beta_low_share": a.beta_low_share,
                                               "awards": "oldest request first (case-id order) — conformance, I26"},
                                "dispositions": {"stamper_fraction": a.stampers,
                                                 "assignment": dict(sorted(run.kind.items())),
                                                 "careful": {"accuracy": a.accuracy, "cost": "uniform {2, 3} credits, or what unlocked "
                                                                                           "credit can buy (counted as underfunded)"},
                                                 "stamper": {"verdict": "F" if a.camouflage == 0 else f"F, N w.p. {a.camouflage} (camouflage)",
                                                             "cost": 0,
                                                             "on_probation": "careful" if a.stamper_mode == "reformer" else "as above"}},
                                "membership": {"spec": "1.3.0 design revision 3 — inspection is membership" if a.rules in ("1.3.0", "1.4.0", "1.5.0", "1.6.0") else "none (control)",
                                               "offers": "members only; a suspended actor or probationer is not offered work",
                                               "panel": "the engine's two tiers; probationers are offered initial reviews only"},
                                "task_world": {"fail_rate_b": a.fail_rate, "truth": "hidden, independent of actor"},
                                "fee_rule": {"spec": "1.1.0 design revision 1 — the verification deposit is two pots",
                                             "f": a.fee, "phi_E": a.phi_e, "phi_F": a.phi_f, "K": run.p.K, "G_V": a.gv},
                                "dispositions_move": {"drift": None if a.drift_to == 0 else
                                                      {"to": a.drift_to, "every": a.drift_every, "step": a.drift_step, "from": a.drift_from,
                                                       "how": "careful actors re-drawn as stampers at random"},
                                                      "adaptive": None if a.adapt_rate == 0 else
                                                      {"rate": a.adapt_rate, "every": a.adapt_every,
                                                       "how": "each actor takes the richer disposition by mean public wealth, w.p. rate"}},
                                "clock": {"spec": "1.2.0 design revision 2 — the loop's own clock" if a.rules != "1.1.0" else "none (1.1.0 control)",
                                          "pi0": a.pi0, "beta_P": a.beta_p, "dial": a.dial, "p_start": a.p_start, "p_cap": a.p_cap,
                                          "Omega0": a.omega0,
                                          "plant_supplier": "the orchestrator creates plants_due() plants each tick before assigning "
                                                            "reviews, bad w.p. β_P, at B = β; truth from the task world; refused plants "
                                                            "(Ω short) stop the tick's supply and are counted",
                                          "panel": "the engine's two tiers (§2.2) refuse ineligible assignments; the driver offers "
                                                   "the next eligible duty actor in round-robin"},
                                "orchestrator": {"selection": "argmax ρ − λB/β at B = β; κ tie band; lowest id",
                                                 "assignment": {"round-robin": "round-robin among eligible duty actors (§7.5)",
                                                                "seeded": "seeded random choice among eligible duty actors"}[a.assignment],
                                                 "audit": "p_audit of the initial reviewer rolled once per F verdict; "
                                                          "auditor: " + ("next eligible duty actor in round-robin" if a.assignment == "round-robin"
                                                                         else "seeded choice among eligible on-duty actors"),
                                                 "ruling": f"by the truth with probability {a.ruling_accuracy}"},
                                "actors": {"offer": "B = β, τ = work_ticks",
                                           "respond_to_N": {"none": "accept", "truthful": "appeal iff truly fulfilled, else accept",
                                                            "always": "appeal every N"}[a.appeal_policy] + " (accept when D cannot be funded)",
                                           "spend": "none"},
                                "requester": {"H": "posts tasks_per_tick per tick at β; " + {
                                    "none": "silent", "truthful": f"disputes a pending F on work that truly failed with probability {a.dispute_rate}",
                                    "half": "disputes a pending F on work that truly failed with probability 0.5",
                                    "always": "disputes every pending F"}[a.dispute_policy], "budget": a.human_budget},
                                "the_supply_side": None if a.rules != "2.3.0" else {
                                    "spec": "2.3.0 design revision 11 — entry as a probationer with a bank-minted float, exit with the wallet out, competence "
                                            "as a private per-actor cost, delegation under competence with the parent posting the pots, the reviewer advance from the pool",
                                    "competence": {"median": a.c_d_median, "sigma": a.c_d_sigma, "clip": a.c_d_clip, "drawn once per actor; private to the driver": True,
                                                   "genesis_costs": {k: v for k, v in sorted(run.c_d_of.items())}},
                                    "entry_pool": None if a.entry_pool == 0 else {"candidates": a.entry_pool, "stamper_share": a.entry_stampers, "reservation_real_per_tick": a.reservation,
                                                                                  "arrivals_per_tick": a.arrivals_per_tick, "exit_patience_periods": a.exit_patience, "F0": a.f0,
                                                                                  "decision": "(B̄ − c) × awards a free member wins a tick (last 50 ticks) × the share of the run left after the time to membership × P0/P_t > r"},
                                    "delegation": None if a.delegation != "on" else {"rule": "delegate when c_A > expected child bid + overhead (nested fee + the pots' expected net cost + care 2); β' = c_A − overhead",
                                                                                        "tau": a.work_ticks + a.nested_tau, "nested_pots": a.nested_pots,
                                                                                        "judgment": "by disposition — careful: the truth w.p. accuracy, spending 2; stamper: F; a bad child accepted makes the parent's work bad",
                                                                                        "child_appeals": "truthfully", "unawarded_T_wait": "withdrawn; the parent self-executes"}},
                                "the_rebate_from_income": None if a.rules not in ("2.2.0", "2.3.0") else {
                                    "spec": "2.2.0 design revision 10 — the claim recorded at the stop; Ω's fee income after the debt pooled as a lock on Ω; at the period's close the "
                                            "claims stopped in the period paid pro rata, the rest forgone and read; no liability stock",
                                    "red_team": {"small_requesters": sorted(run.small)}},
                                "the_bank": None if a.rules not in ("2.1.0", "2.2.0", "2.3.0") else {
                                    "spec": "2.1.0 design revision 9 — the bank: a second account that alone creates and destroys; mints by rule, publishes "
                                            "P_t once a period, lends a summons's shortfall tied to it; the state burns its expected cost and delivers at B̄; "
                                            "every inflow to Ω ordered at once (debt → liabilities → Ω); the wall on deliveries; every refusal told",
                                    "c_D_T": a.c_d_t_mode, "b_T_prior": a.b_t_prior, "b_T_min_n": a.b_t_min_n,
                                    "wall_periods": a.debt_bound_periods if a.debt_bound_periods > 0 else "unbounded (control)",
                                    "requester_on_refusal": a.requester_on_refusal,
                                    "red_team": {"troop_fail_rate": a.troop_fail_rate, "state_rejecters": sorted(run.state_rejecters),
                                                 "state_rejecters_reading": "the case's actor through the public view's case — not the reviewer's view (§14 carries no actor); declared"}},
                                "price_of_work": None if a.rules not in ("2.0.0", "2.1.0", "2.2.0", "2.3.0") else {
                                    "spec": "2.0.0 design revision 8 — the price of work",
                                    "requesters": {"n": a.requesters, "wallet": a.wallet, "issuance_per_tick": a.issuance,
                                                   "ceiling": (f"min({a.beta_max:g}, {a.ceiling_mult:g} × B̄) — market-aware" if a.ceiling_policy == "market"
                                                               else f"min({a.beta_max:g}, {a.ceiling_share:.4g} × unlocked wallet)"),
                                                   "K_open": a.k_open if a.k_open > 0 else "no limit",
                                                   "posting": "one a tick while K_open and the all-in maximum fit; the engine locks the all-in at posting",
                                                   "below_market": "a request below the market price (flagged at posting, or overtaken by it) is raised to the market price when the wallet allows"},
                                    "bids": {"policy": a.bid, "c_D": a.c_d, "adaptive_reservation": a.c_d_adaptive, "margin0": a.margin0,
                                             "margin_up": a.margin_up, "margin_down": a.margin_down, "idle_k": a.idle_k, "lambda": a.lam,
                                             "selection": "argmax ρ − λ B/β with the bid live; κ tie band; lowest id"},
                                    "effort": "c_D burned at submission (spend), or what unlocked credit can pay (counted unpaid)",
                                    "state": {"c_D_T": a.c_d_t_mode, "N_T": a.n_t, "places": "a delivery holds two until its inspection is seated"},
                                    "shock": None if a.create_amount == 0 else {"at": a.create_at, "amount": a.create_amount},
                                    "crowd": None if a.spike_requesters == 0 else {"n": a.spike_requesters, "from": a.spike_from, "ticks": a.spike_ticks,
                                                                                  "wallet": a.wallet, "issuance": a.issuance},
                                    "plants": "at B = P_t", "P0": 20.0,
                                    "red_team": {"lowball_share": a.lowball_share, "lowballers": sorted(run.lowballers),
                                                 "stingy_requesters": sorted(run.stingy), "bbar_counts_troops": a.bbar_troops}},
                                "permitted_operations": PERMITTED + (PERMITTED_200 if a.rules in ("2.0.0", "2.1.0", "2.2.0", "2.3.0") else []), "not_in_run": NOT_IN_RUN,
                                "record_dir": a.record_dir,
                                "checks": {"per_tick": "check_tick after every tick — always; not configurable",
                                           "full_audit_every_n_ticks": "not scheduled",
                                           "final_full_audit": "check_all after the last tick; outcome in full_audit"}})
    t0 = time.time()
    for t in range(1, a.ticks + 1):
        run.tick(t)
        if t % a.log_every == 0 or t == a.ticks:
            rec.tick(run.row(t))
    run_s = time.time() - t0
    t1 = time.time()
    try:
        check_all(run._world)
        audit = {"full_audit": "passed", "full_audit_s": round(time.time() - t1, 1)}
    except AssertionError as e:
        audit = {"full_audit": f"FAILED: {e}", "full_audit_s": round(time.time() - t1, 1)}
    fp = run.w.fingerprint()
    final = run.row(a.ticks)
    if a.record_dir:
        run.w.close()
    ok = audit["full_audit"] == "passed"
    determinism = None
    if a.expect_head:
        determinism = {"expected_head": a.expect_head, "reproduced": fp["head"] == a.expect_head}
        ok = ok and determinism["reproduced"]
    summary = {k: v for k, v in final.items() if k != "head"}
    out = rec.finish(fp=fp, status="completed" if ok else "FAILED", run_s=round(run_s, 1),
                     ticks_per_s=round(a.ticks / run_s, 1), determinism=determinism, final=summary, **audit)
    print(f"{name}: {run_s:.1f}s, {a.ticks / run_s:.0f} ticks/s; {audit['full_audit']} in {audit['full_audit_s']}s; "
          f"results in {os.path.relpath(out)}")
    for kind in (CAREFUL, STAMPER):
        print(f"  {kind:8s} n={final[kind + '_n']:2d} wealth={final[kind + '_wealth']:8.2f} delivery={final[kind + '_delivery']:8.2f} "
              f"fees={final[kind + '_fees']:7.2f} (fixed {final[kind + '_fee_fixed']:6.2f}, haircut {final[kind + '_fee_haircut']:5.2f}) "
              f"costs={final[kind + '_costs']:6.2f} bonds_lost={final[kind + '_bonds_forfeited']:6.2f} "
              f"G_lost={final[kind + '_guarantees_forfeited']:6.2f} awards={final[kind + '_awards']:6.1f} "
              f"reviews={final[kind + '_reviews']:6.1f} overturned={final[kind + '_overturned']:5.2f} rho={final[kind + '_rho']:.3f} "
              f"p_audit={final[kind + '_p_audit']:.3f}")
    print(f"  posted={final['posted']} vested={final['vested']} final_N={final['final_n']} false_approvals={final['false_approvals']} "
          f"false_rejections={final['false_rejections']} audits rolled/assigned/lapsed={final['audits_rolled']}/{final['audits_assigned']}/"
          f"{final['audits_lapsed']} challenges={final['challenges']} rulings={final['rulings']} "
          f"appeals filed/won/lost/unfunded={final['appeals_filed']}/{final['appeals_won']}/{final['appeals_lost']}/{final['appeals_unfunded']} "
          f"false rejections total/appealed/overturned={final['false_rejections_total']}/{final['false_rejections_appealed']}/{final['false_rejections_overturned']} "
          f"disputes filed/won/lost/refused={final['disputes_filed']}/{final['disputes_won']}/{final['disputes_lost']}/{final['disputes_refused']} "
          f"false approvals disputed/overturned={final['false_approvals_disputed']}/{final['false_approvals_overturned']} "
          f"reviews_unassignable_ticks={final['reviews_unassignable_ticks']} awards_unfilled_ticks={final['awards_unfilled_ticks']} "
          f"underfunded_careful_reviews={final['underfunded_careful_reviews']}")
    print(f"  Ω unrecovered advances={final['omega_unrecovered_advances']} claims outstanding={final['claims_outstanding']} "
          f"returned to H: allowance={final['allowance_refunded']} fee pot={final['pot_refunded']} trees closed={final['trees_closed']}")
    print(f"  membership: members on duty={final['members_on_duty']} probationers on duty={final['probationers_on_duty']} member_seats={final['member_seats']} "
          f"readmissions={final['readmissions']} (mean ticks {final['readmission_ticks_mean']}) fund in/out={final['fund_in']}/{final['fund_out']} "
          f"awards refused (members only) ticks={final['awards_refused_members_only_ticks']} probation false approvals={final['probation_false_approvals']}")
    print(f"  troops: active r/d={final['troops_active_reviews']}/{final['troops_active_deliveries']} summons r/d={final['troop_summons_reviews']}/"
          f"{final['troop_summons_deliveries']} troop-ticks r/d={final['troop_ticks_reviews']}/{final['troop_ticks_deliveries']} shortfall s/a/held="
          f"{final['troop_shortfall_seats']}/{final['troop_shortfall_awards']}/{final['troop_held_ticks']} held for market audit now/max age="
          f"{final['held_market_audit_now']}/{final['held_market_audit_max_age']} fund reserve={final['fund_reserve']} advance={final['advance_outstanding']} "
          f"troop deliveries={final['troop_deliveries']} vested/finalN={final['troop_delivered_vested']}/{final['troop_delivered_final_n']} "
          f"troop reviews/audits={final['troop_reviews']}/{final['troop_audits']} troop FA={final['troop_false_approvals']} obligations={final['audit_obligations']}")
    print(f"  clock: m={final['m']} pi={final['pi']} X_t={final['X_t']} periods={final['periods']} F_hat(last)={final['F_hat']} "
          f"plants created/bad/stood/failed/spent={final['plants_created']}/{final['plants_bad']}/{final['plants_stood']}/"
          f"{final['plants_failed']}/{final['plants_spent']} unfunded={final['plants_unfunded']} shortfall={final['plant_shortfall']} "
          f"suspensions={final['suspensions']} alarms={final['alarms']} eligibility_shortfall={final['eligibility_shortfall']} "
          f"Ω plant spend={final['omega_plant_spend']} Ω net={final['omega_net']}")
    print(f"  accounts (1.7.0): uplift fund={final['duty_fund']} troop account={final['troop_account']} troop surplus to Ω={final['troop_surplus']} "
          f"Ω fee income={final['omega_fee_income']} advances made/repaid={final['advances_made']}/{final['advances_repaid']} "
          f"rebates paid={final['rebates_paid']} liabilities paid={final['liabilities_paid']} liability={final['omega_liability']}")
    for kind in (CAREFUL, STAMPER):
        print(f"  {kind:8s} plant reviews={final[kind + '_plant_reviews']:6.2f} failures={final[kind + '_plant_failures']:5.2f} "
              f"a_hat={final[kind + '_a_hat']:.3f} suspended={final[kind + '_suspended']} duty-eligible={final[kind + '_duty_eligible']} "
              f"panel-eligible={final[kind + '_panel_eligible']}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

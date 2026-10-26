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
import json
import math
import os
import random
import sys
import time
from dataclasses import dataclass, field

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sim import Params, World, RuleError, LedgerError, check_all   # noqa: E402
from sim.engine import F, N, P, BOT, PLANT                          # noqa: E402
from drivers.view import Public                                     # noqa: E402
from drivers.results import RunRecorder                             # noqa: E402

CAREFUL, STAMPER = "careful", "stamper"
TELL = "tell"      # the learned red team's Q2, hand-written first: a reviewer that reads the view for a plant's tells and stamps the rest
LEARNER = "learner"   # the learned red team: the slot actor whose decisions a policy supplies through `Stamping.learner` (redteam.env)
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
AVAIL_KEYS = ["ticks_waiting", "waiting_items", "items_initial", "items_audit", "items_appeal", "on_duty", "committed", "in_review",
              "on_duty_idle_fits", "on_duty_idle_unfit", "free_fundable", "held_by_cap", "free_unfunded", "free_not_panel", "ineligible",
              "free_excluded", "free_probationers", "free_probationers_fit_initial"]

PERMITTED_200 = ["post_root (six requesters, β = min(β_max, a third of the unlocked wallet) or min(β_max, mult × B̄) under --ceiling-policy market, "
                 "one a tick while K_open (0: no limit) and the all-in fit; "
                 "the engine locks the all-in maximum at posting and refuses what does not fit — 2.0.0 §2.1)",
                 "raise_ceiling (a requester flagged below market raises to the market price when its wallet allows)",
                 "the tell-reader (--tell-readers, Q2 of the learned red team's brief, hand-written first): a reviewer reads its own ReviewView "
                 "(t_submit, cap, case id), its own assignment tick, and what it saw available as a free member (the roots, when, at what ceiling), "
                 "its own bids and their outcomes, for a plant's tells (gap, cap, idage, seen, post, price, losttie); reviews carefully what reads "
                 "as a plant, stamps F what reads as real; the truth is read after the verdict to score the tell. `freshname` reads the case's "
                 "awardee name and `oracle` the plant marker — both outside the convention, declared, the boundary's control and the upper bound",
                 "post_plant (2.6.0 §2.1: the orchestrator posts the plants the rate calls for as roots under fresh names; the market bids, the "
                 "selection reports through award and the engine awards the plant actor; the plant actor submits at its drawn tick; the "
                 "population's dispositions never read Task.plant before the verdict)",
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
    nested_missed: bool = False   # run 17: a lowball child's miss, counted once
    nested_missed_counted: bool = False   # 2.5.0: the lapse counted once
    audit_rolled: bool = False
    audit_wanted: bool = False   # rolled yes, not yet assigned
    appeal_wanted: bool = False
    appealed: bool = False       # the actor appealed its N (the appeals run)
    dispute_rolled: bool = False
    disputed: bool = False       # H disputed the pending F (the dispute run)
    plant: bool = False          # the orchestrator's planted work (1.2.0)
    probation_false_approval: bool = False   # a probationer approved truly failed work (1.3.0: audited at 1)
    learner_work: Optional[int] = None       # Q3 (the learned deliverer): the slot's quality decision on this case — 0 good, 1 bad (zero effort)
    pair_review: bool = False                # Q4: the pair's reviewer took the initial review of the pair's deliverer's case
    learner_miss: bool = False               # Q5 (the learned child): the child chose to miss — never submits; the lapse at the deadline
    parent_learner: bool = False             # Q5 (the learned parent): this nested case is the learned parent's child
    parent_rejected_blind: bool = False      # Q5: … and the parent rejected it blind
    pair_stamped: bool = False               # Q4: … and approved it blind
    t_seated: Optional[int] = None           # the plant's life by stage (the ruling after run 34): the tick the root's initial review was assigned
    seated_seen: bool = False                #   … and whether that reviewer had the case in its seen set (a free member saw it available)
    seated_seen_ticks: Optional[int] = None  #   … the ticks from the sighting to the seat
    raised_n: int = 0                        #   the ceiling's raises (a plant is raised as the population's requesters raise, 2.6.1)
    raise_refused_n: int = 0                 #   the raises refused — a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate (the conformance correction after run 35; §52 read the two apart)
    raise_first_t: Optional[int] = None      #   the tick of the first raise attempt (a real root's enters the window there: refused or granted)
    raise_refused_t: Optional[int] = None    #   the tick of the first refused attempt (the delay to the grant is measured from it)
    plant_raise_at: Optional[int] = None     #   a plant refused its raise: the tick the raise is granted (the refusal + a delay drawn from the trailing refused real roots')
    # 2.8.0: the plant at every seat — the instrument's filings and their timing, and the stages after the first verdict by case kind
    plant_file_at: Optional[int] = None      #   a plant's filing (appeal or dispute) drawn at the real rate: the tick it is filed (−1: drawn not to file)
    plant_revise_at: Optional[int] = None    #   a plant's revision drawn from the real window: the tick it is resubmitted
    revised_truth: Optional[bool] = None     #   the resubmitted truth drawn (B)
    revised: bool = False
    t_roll: Optional[int] = None             #   the audit roll's tick (zero world ticks after the verdict in every standing cell)
    t_audit_assign: Optional[int] = None     #   the audit seat taken
    t_filed: Optional[int] = None            #   an appeal or dispute filed
    t_panel_assign: Optional[int] = None     #   the first panel seat taken
    life_period: Optional[int] = None        #   the period of the first seat (the stage table's period-matched key)


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
        rev3 = a.rules in ("1.3.0", "1.4.0", "1.5.0", "1.6.0", "1.7.0", "1.7.1", "2.0.0", "2.1.0", "2.2.0", "2.3.0", "2.4.0", "2.5.0", "2.6.0", "2.7.0", "2.8.0")     # 1.2.0 and 1.1.0: membership, the fund and netted capital off
        rev4 = a.rules in ("1.4.0", "1.5.0", "1.6.0", "1.7.0", "1.7.1", "2.0.0", "2.1.0", "2.2.0", "2.3.0", "2.4.0", "2.5.0", "2.6.0", "2.7.0", "2.8.0") and a.troops == "on"
        rev5 = a.rules in ("1.5.0", "1.6.0", "1.7.0", "1.7.1", "2.0.0", "2.1.0", "2.2.0", "2.3.0", "2.4.0", "2.5.0", "2.6.0", "2.7.0", "2.8.0")    # 1.4.0: the reserve is the peak capital carried, over two periods
        rev6 = a.rules in ("1.6.0", "1.7.0", "1.7.1", "2.0.0", "2.1.0", "2.2.0", "2.3.0", "2.4.0", "2.5.0", "2.6.0", "2.7.0", "2.8.0")     # 1.6.0: the five rules, each behind its flag; `--rules 1.5.0` turns them off
        rev7 = a.rules in ("1.7.0", "1.7.1", "2.0.0", "2.1.0", "2.2.0", "2.3.0", "2.4.0", "2.5.0", "2.6.0", "2.7.0", "2.8.0")  # 1.7.0: the troop account behind its flag and the cap at two thirds; `--rules 1.6.0` is the control
        rev8 = a.rules in ("2.0.0", "2.1.0", "2.2.0", "2.3.0", "2.4.0", "2.5.0", "2.6.0", "2.7.0", "2.8.0")     # 2.0.0: the price of work — floating prices, N_T; `--rules 1.7.1` is the fixed-price control
        rev9 = a.rules in ("2.1.0", "2.2.0", "2.3.0", "2.4.0", "2.5.0", "2.6.0", "2.7.0", "2.8.0")     # 2.1.0: the bank — loans, the debt, the wall, P_t once a period; `--rules 2.0.0` is the control
        rev10 = a.rules in ("2.2.0", "2.3.0", "2.4.0", "2.5.0", "2.6.0", "2.7.0", "2.8.0")    # 2.2.0: the rebate from income — the period's fee pool, claims pro rata at the close; `--rules 2.1.0` the control
        rev11 = a.rules in ("2.3.0", "2.4.0", "2.5.0", "2.6.0", "2.7.0", "2.8.0")               # 2.3.0: the supply side — entry, exit, the parent's pots; `--rules 2.2.0` the control
        rev12 = a.rules in ("2.6.0", "2.7.0", "2.8.0")                        # 2.6.0: the plant's disguise — a plant goes through the market; `--rules 2.5.0` the control
        rev13 = a.rules in ("2.7.0", "2.8.0")                                   # 2.7.0: the arrival loan — the float lent, repaid from income, recovered at departure; `--rules 2.6.0` the control
        rev14 = a.rules == "2.8.0"                                   # 2.8.0: the plants reach every seat; `--rules 2.7.0` the control
        self.rev9, self.rev10, self.rev11, self.rev12, self.rev13, self.rev14 = rev9, rev10, rev11, rev12, rev13, rev14
        self.floating = rev8
        on = lambda flag: rev6 and flag == "on"
        if a.duty_cap is None:
            a.duty_cap = "twothirds" if rev7 else "half"
        if a.tie_break is None:
            a.tie_break = "draw" if rev12 else "id"                      # 2.6.0 §2.3: the tie after κ by a seeded draw; `id` the control
        p = Params(Res0=a.res0, X=a.on_duty, G_V=a.gv, p_start=a.p_start, p_cap=a.p_cap, p_floor=a.p_floor, band=a.band, G_frac_nested=a.child_g_frac,
                   record_dir=a.record_dir, f_fee=a.fee, phi_E_root=a.phi_e, phi_F_root=a.phi_f,
                   pi0=a.pi0, dial=(a.dial == "on"), beta_P=a.beta_p, Omega0=a.omega0,
                   membership=rev3, duty_fund=(rev3 and a.fund == "on"), net_plant_capital=rev3, m_max=a.m_max,
                   troops=rev4, eps_T=a.eps_t, w_R=a.w_r, w_A=a.w_a, c_T=a.c_t, c_D_T=a.c_d_t, A_T=a.a_t, tau_T=a.work_ticks,
                   reserve_demand=rev5,
                   service_clock=on(a.clock), T_s=a.t_s, omega_backs_fund=on(a.backing), seat_the_queue=on(a.seat_queue),
                   panel_determined=on(a.panel_determined), reserve_periods=(a.reserve_periods if rev6 else 1),
                   duty_cap_frac={"half": 0.5, "twothirds": 2.0 / 3.0, "threequarters": 0.75, "all": 1.0}[a.duty_cap],
                   state_reservation=(a.state_reservation if a.state_reservation is not None else (8.0 if a.rules in ("2.4.0", "2.5.0", "2.6.0", "2.7.0", "2.8.0") else 0.0)),
                   missed_child=(a.rules in ("2.5.0", "2.6.0", "2.7.0", "2.8.0")),
                   plant_market=rev12, trailing_periods=a.trailing_periods, plant_submit_fixed=a.plant_submit,
                   plant_reserve_life=(0 if a.plant_reserve == "period" else 15),
                   troop_account=(rev7 and a.accounts == "on"), omega_rate=a.omega_rate, r_s=a.r_s, T_susp=a.t_susp,
                   theta_panel=a.theta_panel, n_P=a.record_window,
                   floating=rev8, P0=20.0, issuance=(a.issuance if rev8 else 0.0), N_T=(a.n_t if rev8 else 0),
                   troop_cost_at_price=(rev8 and a.c_d_t_mode in ("cost", "at_cost")), lam=a.lam, bbar_counts_troops=(rev8 and a.bbar_troops == "on"),
                   bank=rev9, c_d_t_mode=("at_cost" if a.c_d_t_mode == "cost" else a.c_d_t_mode), b_t_prior=a.b_t_prior,
                   b_t_min_n=a.b_t_min_n, debt_bound_periods=a.debt_bound_periods, rebate_pool=rev10,
                   supply=rev11, F0=a.f0, nested_pots=a.nested_pots,
                   arrival_loan=(rev13 and a.arrival_loan == "on"),
                   plants_every_seat=(rev14 and a.plants_every_seat == "on"))
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
        self.repaid_at_boundary: dict[str, float] = {}   # 2.7.0: each name's loan repaid from income at the last boundary (the exit rule)
        self.below_bond_names: set[str] = set()          # 2.7.0 H2: arrival-born names whose unlocked balance fell below G^V before admission
        self.idle_for_bond_names: set[str] = set()       # the standing reading after the v2 calibration: members idle for want of a bond
        self.departed: list[str] = []
        self.depart_wealth_real: dict[str, float] = {}   # actor -> real wealth taken out at departure (the lifetime measure)
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
        # run 17 red team: greedy parents (careful actors that reject every child), lowball children (bid half, never deliver), cyclers
        # red team Q2 (the brief of October 20, the reviewer's note): the hand-written tell-reader — careful actors that read the reviewer's
        # view for a plant's tells (`--tell gap|cap|idage`, joined by +), review carefully what reads as a plant and stamp what reads as real
        ids_t = [aid for aid in ids_c if aid not in self.state_rejecters]
        self.tell_readers = set(ids_t[: round(len(ids_c) * a.tell_readers)]) if a.tell_readers > 0 else set()
        for aid in self.tell_readers:
            self.kind[aid] = TELL
        self.careful_initial = [aid for aid in self.actors if self.kind[aid] == CAREFUL]   # the careful cohort at genesis (arrivals excluded)
        # the stability track's first cells (the ruling after run 31; evaluations under fixed rules): a population of undercutters — the careful members in
        # --undercut-share bidding Q6's rule, (1 − δ) B̄ floored at cost — drawn once on their own stream (a control run's draws untouched); arrivals join by the
        # same draw; and the requesters that follow --ceiling-policy (the first --ceiling-requesters standing requesters; 0 every requester, as before)
        self.under_rng = random.Random(a.seed * 15485863 + 31)
        self.undercutters: set[str] = set()
        if a.bid == "undercut":
            ids_u = list(self.careful_initial); self.under_rng.shuffle(ids_u)
            self.undercutters = set(ids_u[: round(len(ids_u) * a.undercut_share)])
        self.policy_requesters = set(self.requesters[: a.ceiling_requesters]) if a.ceiling_requesters > 0 else set(self.requesters)
        self.under_floor_cases: set[str] = set()                 # the requests posted under the reservation
        self.below_floor_cases: dict[str, str] = {}              # awards at a bid under the floor → the member serving
        self.below_floor_servers: set[str] = set()
        self.bf_counted: set[str] = set()
        self.uf_counted: set[str] = set()
        self._mk_cache = (-1, None)
        # the slot: the actor that is (or, in a control run, would be) the single tell-reader — the same id, cost and tie-break position
        # on the same seed, so a control run's slot is the paired comparison the brief's "same cost and split" asks for
        self.tell_slot = ids_t[0] if ids_t else (self.actors[0] if (a.learner_slot == "on" and self.actors) else None)   # Q3's calibration: every reviewer a stamper — the slot the first actor
        if a.learner_slot == "on" and a.learner_role == "parent" and ids_t and a.parent_slot != "first":
            ranked = sorted(ids_t, key=lambda x: (self.c_d_of[x], x))          # Q5: the learned parent's slot by cost — a declared construction (a cheap parent cannot post a child)
            self.tell_slot = ranked[-1] if a.parent_slot == "costliest" else ranked[len(ranked) // 2]
        if a.learner_slot == "on" and a.learner_role == "bidder" and ids_t and a.bidder_slot != "first":
            ranked = sorted(ids_t, key=lambda x: (self.c_d_of[x], x))          # Q6: the learned bidder's slot by cost (the cheapest by default — a declared construction)
            self.tell_slot = {"cheapest": ranked[0], "costliest": ranked[-1], "median": ranked[len(ranked) // 2]}[a.bidder_slot]
        # the learned red team (redteam.env): the slot actor's reviewing decisions come from a policy — `self.learner(run, reviewer, view, r)`
        # returns 0 (care: the careful disposition's signal at its cost), 1 (approve blind), 2 (reject blind); the truth is never shown to it
        self.learner = None
        self.learner_work = None                      # Q3: the slot's quality decision at each of its submissions — `self.learner_work(run, actor, case)` → 0 good, 1 bad
        self.learner_parent = None                    # Q5: the learned parent — `self.learner_parent(run, parent, kind, root, child)`: kind delegate (0 self-execute, 1 delegate), judge (0 care, 1 stamp, 2 reject blind), cancel (0 wait, 1 cancel)
        self.learner_bid = None                       # Q6: the learned bidder — `self.learner_bid(run, actor, roots)` once a tick when the slot is free and a root is available it could bid under:
                                                      # 0 the ratchet's bid (c_D (1 + m), the population's rule), 1 undercut ((1 − δ) B̄ floored at c_D, --undercut), 2 withhold (no offer this tick)
        self.learner_bid_mode = 0                     # the bidder's rule for the tick's offers
        self.learner_last_bid_case = None             # (t, cid): the root the bidder's decision at t won — read by redteam.env to credit the case to that decision
        self.learner_req = None                       # Q7: the learned requester — `self.learner_req(run, requester, cands)` at each posting the rule admits: 0 the market rule's ceiling
                                                      # (the population's, the reference), 1 patient (0.7 B̄, raised to the state's price after --patient-ticks — run 17's customer),
                                                      # 2 the floor (the state's reservation, nominal, never raised — 2.4.0 §8.7's posting: served by a member bidding under it or not at all)
        self.req_spent_nominal, self.req_spent_real_sum = 0.0, 0.0   # its credits out less in, by its own events at the index of each (the wallet's revaluation excluded)
        self.req_mode: dict[str, int] = {}            # the learned requester's cases by the rule they were posted under
        self.req_received_cases: list[str] = []       # its settled deliveries whose truth is fulfilled — the tasks received, each worth --task-value to the attribution
        self.req_counted: set[str] = set()
        self.req_w0 = None                            # its genesis wallet (nominal at P_0: real), read at the first tick before any posting
        self.learner_id = None
        self.learner_review_kind = CAREFUL            # the slot's reviewing disposition when the learner is a deliverer (the population's at that slot)
        self.learner_role_of: dict[str, str] = {}     # each learner identity's role (Q4's pair: the slot a deliverer, the next careful id a reviewer)
        self.learner_pair = None
        if a.learner_slot == "on" and a.learner_role == "requester":
            if not self.requesters:
                raise SystemExit("--learner-role requester needs a standing requester")
            self.learner_id = self.requesters[min(a.requester_slot, len(self.requesters) - 1)]      # Q7: a requester, not an actor — no kind, no reviewing, no boundary decision
            self.learner_role_of[self.learner_id] = "requester"
        elif a.learner_slot == "on" and self.tell_slot is not None:
            self.learner_id = self.tell_slot
            self.learner_review_kind = self.kind[self.learner_id]
            self.kind[self.learner_id] = LEARNER
            self.learner_role_of[self.learner_id] = a.learner_role
            if a.learner_pair == "on":
                others = [x for x in ids_t if x != self.learner_id]
                if not others:
                    raise SystemExit("--learner-pair needs a second careful actor for the reviewer")
                self.learner_pair = (self.learner_id, others[0])
                self.learner_role_of[self.learner_id] = "deliverer"
                self.learner_role_of[others[0]] = "reviewer"
                self.kind[others[0]] = LEARNER
        # the learned population (the ruling after run 32): N learner slots sharing one policy in self-play — every careful member at genesis, or half drawn once
        # on the undercutters' stream (the same half as --undercut-share 0.5 on the seed); the slot id the cheapest of them; careful arrivals join by the same draw
        self.learner_pop: list[str] = []
        self.learner_hand_kind: dict[str, str] = {}   # (ii) the reviewers in self-play: each slot's disposition by hand — the `hand` reference (action 3) answers with it, so run 24's 60/40 is read on the same slots
        if a.learner_slot == "on" and a.learner_pop != "off" and a.learner_role in ("bidder", "reviewer"):
            ids_p = list(self.careful_initial) if a.learner_role == "bidder" else list(ids); self.under_rng.shuffle(ids_p)   # the bidders: the careful members; the reviewers: every member (the 60/40 is a reference)
            take = ids_p if a.learner_pop == "all" else ids_p[: round(len(ids_p) * 0.5)]
            if not take:
                raise SystemExit("--learner-pop needs members at genesis")
            if self.learner_id is not None and self.learner_id not in take:
                self.kind[self.learner_id] = self.learner_review_kind; self.learner_role_of.pop(self.learner_id, None)
            for x in take:
                self.learner_hand_kind[x] = self.kind[x] if self.kind[x] != LEARNER else self.learner_review_kind
                self.kind[x] = LEARNER; self.learner_role_of[x] = a.learner_role
            self.learner_pop = sorted(take, key=lambda x: (self.c_d_of[x], x))
            self.learner_id = self.tell_slot = self.learner_pop[0]
        self.learner_bid_mode_of: dict[str, int] = {}        # each learner bidder's rule for the tick (the population; the single slot keeps learner_bid_mode)
        self.bid_awards_of: dict[str, int] = {}              # each learner bidder's own record (its observation's fields)
        self.bids_lost_of: dict[str, int] = {}
        self.last_won_of: dict[str, int] = {}
        self.learner_won: list[tuple[int, str, str]] = []    # (t, name, case): the roots the learners' bids won this step — redteam.env credits each to the decision (t, name)
        self.life_by_period: dict[int, dict] = {}            # §52: the plant's life by stage, by period and kind — the pooled table confounds the plant rate's rise with the market's drift; run_q reads a period-matched difference from this
        # the conformance correction after run 35 (Appendix S): the real roots' raises as the plant requester's window — (period, refused at the first
        # attempt 1/0) and (period, ticks from the first refused attempt to the grant); read as the engine's `_plant_draw` reads its window
        self.raise_window_out: list[tuple[int, int]] = []
        self.raise_window_delay: list[tuple[int, int]] = []
        # 2.8.0: the instrument's windows on the real population — the actors' appeals of a false rejection (filed or not; the delay from the
        # verdict), the requesters' disputes of a false approval (filed or not; the delay), the revisions' outcomes and delays (empty in every
        # standing cell: no reviewer answers P or ⊥) — read as the raise window is (the last k entries, k the trailing periods' count)
        self.appeal_window: list[tuple[int, int]] = []
        self.appeal_delay_window: list[tuple[int, int]] = []
        self.dispute_window: list[tuple[int, int]] = []
        self.dispute_delay_window: list[tuple[int, int]] = []
        self.revision_window: list[tuple[int, bool]] = []
        self.revision_delay_window: list[tuple[int, int]] = []
        self.plant_rng = random.Random(a.seed * 15485863 + 29)        # the plant's filing and revision draws — their own stream
        self.raise_rng = random.Random(a.seed * 1299709 + 13)         # the plant's refusal and delay draws — their own stream, the others' unmoved
        self.learner_mix_by_period: dict[int, list[int]] = {}   # period → [ratchet, undercut, withhold] over the learners' bid decisions (the action mix by period)
        self.wealth_in_of: dict[str, float] = {}             # each learner slot's wealth in (genesis, read at the first tick; an arrival's float) — the nominal surplus
        self.depart_wealth_nominal: dict[str, float] = {}
        self.pop_counted: set[str] = set()
        self.requesters_set = set(self.requesters)
        self.pop_req_spent_nominal = 0.0                     # every requester's credits out less in, by their events (the customers' tasks per credit, nominal)
        self.learner_decisions = 0
        self.learner_chain: list[str] = (list(self.learner_pop) if self.learner_pop else ([self.learner_id] if self.learner_id else [])) + ([self.learner_pair[1]] if self.learner_pair else [])   # the learner's identities in order (re-arrival allowed after run 22); Q4: the pair, whose lifetime is read as one
        self.learner_returns, self.learner_leaves_chosen, self.learner_leaves_refused, self.learner_boundary_decisions = 0, 0, 0, 0
        self.learner_float_minted, self.learner_float_minted_real = 0.0, 0.0
        self._last_boundary_t = None
        self.readers = set(self.tell_readers) | ({self.learner_id} if self.learner_id else set()) | (set(self.learner_pop) if a.learner_role == "reviewer" else set())   # who keeps a seen set and its bids
        self.tells = {"gap", "cap", "idage", "seen", "post", "price", "losttie"} if a.tell == "all" else set(a.tell.split("+"))   # `oracle` / `freshname`: outside the convention (declared)
        self.seen: dict[tuple, tuple] = {}            # (reader, case) -> (world tick first seen available, its ceiling, P_t then)
        self.my_bid: dict[tuple, float] = {}          # (reader, case) -> the reader's bid
        self.lost_bid: dict[tuple, int] = {}          # (reader, case) -> the tick the case went to someone else
        ids_g = list(reversed(ids_c))
        self.greedy = set(ids_g[: round(len(ids_g) * a.greedy_parents)]) if a.greedy_parents > 0 else set()
        # 2.7.0 §8.6 red team — the accomplice route: a mover and its accomplice, the first two arrival-born members admitted
        self.acc_pair: tuple | None = None
        self.acc_pair_t = None
        self.acc_moves, self.acc_moved_sum = 0, 0.0
        self.acc_mover_out, self.acc_mover_default, self.acc_mover_departed_t = None, 0.0, None
        self.farmers = set(ids_g[: round(len(ids_g) * a.farm_parents)]) if a.farm_parents > 0 else set()   # 2.5.0 §8.5: deadlines too short
        self.child_tau: dict[str, int] = {}              # nested case -> the tau the parent will award at
        ids_lb = list(self.actors); self.rng.shuffle(ids_lb)
        self.lowball_children = set(ids_lb[: round(len(ids_lb) * a.lowball_children)]) if a.lowball_children > 0 else set()
        self.cycle_n = 0
        self.cycled_from: dict[str, str] = {}            # new identity -> the one it left
        self.cycler_admitted_ticks: list[int] = []
        # run 17 batch A: the inspection queue — who waits, who clears it, who was available while it waited
        self.waiting_since: dict[tuple, int] = {}       # (case, kind) -> observations seen waiting
        self.waiting_first: dict[tuple, int] = {}       # (case, kind) -> the world tick first seen waiting
        KS = [(k, s) for k in ("initial", "audit", "appeal") for s in ("member", "probationer", "troop")]
        self.seat_counts = {ks: 0 for ks in KS}
        self.seat_wait_sum = {ks: 0 for ks in KS}
        self.seat_wait_ge_wR = {ks: 0 for ks in KS}
        self.seat_left_otherwise = {"initial": 0, "audit": 0, "appeal": 0}
        self.avail = {k: 0 for k in AVAIL_KEYS}
        self.cap_slack_sum, self.cap_slack_n, self.cap_bound_ticks = 0, 0, 0
        self.cap_now, self.members_on_duty_now, self.E_t_now = 0, 0, 0
        if a.genesis_duty is None:
            a.genesis_duty = "draw" if rev12 else "lowest"
        self.draw_rng = random.Random(a.seed * 104729 + 7)             # 2.6.0 §2.3: the orderings the rules should not carry — a seeded draw
        duty0 = sorted(self.draw_rng.sample(sorted(self.actors), a.on_duty)) if a.genesis_duty == "draw" else sorted(self.actors)[: a.on_duty]
        world = World(p, self.actors, humans=humans, on_duty=duty0)
        self.w = Public(world)
        self._world = world            # for the final check_all and the fingerprint only
        if self.learner_pair and a.pair_volunteer == "on":
            self.w.volunteer(self.learner_pair[1], True)   # Q4: the pair's reviewer volunteers for duty (§7.5) and is kept on it — declared
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
                  "departed_net": 0.0,             # 2.7.0: the wallets carried out by departing actors, net of the loans recovered
                  "unfundable_with_loan_ticks": 0, # 2.7.0 H2: Σ over ticks of free arrival-born members unfundable for an award while a loan stood
                  "pop_tasks_received": 0,         # the customers' tasks received (every requester's settled deliveries whose truth is fulfilled)
                  "undercut_awards": 0, "undercut_awards_at_cost": 0, "awards_below_floor": 0, "awards_at_floor": 0, "below_floor_margin_sum": 0.0,
                  "below_floor_final_n": 0, "below_floor_g_lost": 0.0, "under_floor_posted": 0, "under_floor_awarded": 0, "under_floor_wait_sum": 0,
                  "under_floor_price_sum": 0.0, "under_floor_fulfilled": 0, "under_floor_final_n": 0, "under_floor_vested": 0,   # the stability track (run 31's ruling)
                  "idle_for_bond_ticks": 0,        # members idle for want of a bond: Σ over ticks of free members whose unlocked balance is below G^V at the index
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
                  "audit_obligations": 0, "audits_held": 0, "audits_overturning": 0, "troop_reviews": 0, "troop_audits": 0, "troop_deliveries": 0,
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
                  "tell_plant_read_plant": 0, "tell_plant_read_real": 0, "tell_real_read_plant": 0, "tell_real_read_real": 0, "tell_false_approvals": 0,
                  "plant_bids_lost": 0, "plant_lag_sum": 0, "plant_lag_n": 0, "learner_false_approvals": 0,
                  "plant_raises_refused": 0, "plant_raise_delay_sum": 0,       # the plants whose raise was drawn refused (after run 35) and their drawn delays
                  # 2.8.0: the plant at every seat — the instrument's filings, revisions and spends, the seats and failures by kind, the state's initial seats
                  "plant_appeals_filed": 0, "plant_disputes_filed": 0, "plant_challenges": 0, "plant_revisions": 0, "plant_spent_by_instrument": 0,
                  "plants_state_initial": 0, "plant_appeals_held": 0,
                  **{f"plant_seats_{k}": 0 for k in ("initial", "audit", "third", "appeal", "dispute", "resumed", "state")},
                  **{f"plant_seat_failures_{k}": 0 for k in ("initial", "audit", "third", "appeal", "dispute", "resumed", "state")},
                  **{f"life_{k}_{st}": 0 for k in ("real", "plant") for st in ("audit_n", "audit_wait", "filing_n", "filing_delay", "panel_n", "panel_wait", "state_seats")},
                  # the plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument): at the root's first initial
                  # review seat — posted → awarded, awarded → submitted, submitted → seated (the review's t_assign), the raises, the floor (a plant) or the
                  # troop (a real root), the reviewer's seen set — by case kind
                  "life_real_n": 0, "life_plant_n": 0, "life_real_post_award": 0, "life_plant_post_award": 0, "life_real_award_submit": 0, "life_plant_award_submit": 0,
                  "life_real_submit_seat": 0, "life_plant_submit_seat": 0, "life_real_raised": 0, "life_plant_raised": 0, "life_real_troop": 0, "life_plant_floor": 0,
                  "life_real_seen": 0, "life_plant_seen": 0, "life_real_seen_ticks": 0, "life_plant_seen_ticks": 0, "life_real_raise_refused": 0, "life_plant_raise_refused": 0,
                  # Q3 — the learned deliverer (--learner-role deliverer): its quality decisions and what became of them
                  "learner_work_decisions": 0, "learner_bad_deliveries": 0, "learner_good_deliveries": 0, "learner_bad_approved": 0, "learner_bad_caught": 0,
                  "learner_good_vested": 0, "learner_good_final_n": 0, "learner_forfeited": 0.0, "learner_bad_paid": 0.0, "learner_effort_saved": 0.0,
                  # Q4 — the pair (--learner-pair on): the deliverer's cases the reviewer took, matched or blind, and what the reviewer did with them
                  "pair_matched": 0, "pair_unmatched": 0, "pair_waited": 0, "pair_reviews": 0, "pair_cares": 0, "pair_stamps": 0, "pair_rejects": 0, "pair_bad_stamped": 0,
                  "pair_bad_stamped_vested": 0, "pair_bad_stamped_caught": 0, "pair_good_stamped": 0,
                  # Q5 — the learned child (--learner-role child): its nested awards, misses and the lapses; the population knobs' counts
                  "learner_nested_awards": 0, "learner_nested_offers": 0, "learner_misses": 0, "learner_miss_lapsed": 0, "parent_judge_override": 0, "child_appeals_suppressed": 0,
                  # Q5 — the learned parent (--learner-role parent): its three kinds of decision and what became of them
                  # Q6 — the learned bidder (--learner-role bidder): its decisions by kind, the awards they won and at what bid over cost, the offers lost, the wealth held
                  # Q7 — the learned requester (--learner-role requester): its postings by rule, what became of them, the wait, the price paid
                  "req_decisions": 0, "req_rule_market": 0, "req_rule_floor": 0, "req_rule_patient": 0, "req_posted": 0, "req_unaffordable": 0, "req_raised": 0,
                  "req_tasks_received": 0, "req_paid_unfulfilled": 0, "req_final_n": 0, "req_free_fulfilled": 0, "req_state_deliveries": 0, "req_wait_sum": 0, "req_awards": 0,
                  "req_price_paid_sum": 0.0, "req_disputes_filed": 0, "req_disputes_won": 0, "req_waiting_ticks": 0,
                  "learner_bid_decisions": 0, "learner_bid_ratchet": 0, "learner_bid_undercut": 0, "learner_bid_withheld": 0, "learner_bid_awards": 0,
                  "learner_bid_award_sum": 0.0, "learner_bid_cost_sum": 0.0, "learner_bids_lost": 0, "learner_held_sum": 0.0, "learner_held_n": 0,
                  "learner_delegate_decisions": 0, "learner_delegations": 0, "learner_self_exec_chosen": 0, "learner_delegate_impossible": 0,
                  "learner_judge_decisions": 0, "learner_judge_care": 0, "learner_judge_stamp": 0, "learner_judge_reject": 0,
                  "learner_child_stamped_bad": 0, "learner_child_stamped_good": 0, "learner_child_rejected_bad": 0, "learner_child_rejected_good": 0,
                  "learner_cancel_decisions": 0, "learner_cancels": 0, "learner_cancel_refused": 0, "learner_kill_fees": 0.0,
                  "learner_guarantees_taken": 0.0, "learner_child_lapses": 0, "learner_rejections_overturned": 0, "learner_children_settled": 0,
                  # 2.3.0: the supply side
                  "arrivals": 0, "departures": 0, "departed_cost_sum": 0.0, "nested_posted": 0, "nested_awarded": 0, "nested_unaffordable": 0, "accomplice_unaffordable": 0,
                  "nested_self_executed": 0, "nested_judged": 0, "nested_false_approvals": 0, "nested_false_rejections": 0,
                  "nested_price_sum": 0.0, "nested_price_n": 0, "gain_sum": 0.0, "gain_vs_cost_sum": 0.0, "nested_award_refused": 0,
                  # run 17: the red team and the parents by kind
                  "cycles": 0, "greedy_rejections": 0, "greedy_overturned": 0, "lowball_child_awards": 0, "lowball_child_misses": 0,
                  "nested_fa_stamper_parent": 0, "nested_fa_careful_parent": 0, "nested_posted_by_stamper": 0, "nested_posted_by_careful": 0,
                  "patient_raised": 0,
                  # 2.4.0: the parent's cancellation and the kill fee
                  "parent_cancellations": 0, "kill_fees_paid": 0.0, "kill_fees_nonzero": 0, "cancel_delay_sum": 0, "parent_cancel_refused": 0,
                  # 2.5.0: the refusal at the deadline, the lapses, the red team
                  "cancel_refused_at_deadline": 0, "nested_lapsed": 0, "nested_lapsed_forfeit": 0.0, "nested_declined_deadline": 0,
                  "lowball_empty_submitted": 0, "lowball_empty_rejected": 0, "lowball_empty_approved": 0, "lowball_appeals": 0,
                  # run 17 batch A: every inspection seat the driver fills, by kind and the reviewer's standing (plants apart)
                  "seated_initial_member": 0, "seated_initial_probationer": 0, "seated_audit_member": 0, "seated_appeal_member": 0, "seated_plant": 0}
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
    def _life_columns(self) -> dict:
        """The plant's life by stage beside a real root's (the ruling after run 34): means per root that reached its first initial seat, by case kind."""
        out = {}
        for k in ("real", "plant"):
            n = self.c[f"life_{k}_n"]
            out[f"life_{k}_n"] = n
            for st in ("post_award", "award_submit", "submit_seat"):
                out[f"life_{k}_{st}"] = round(self.c[f"life_{k}_{st}"] / n, 4) if n else ""
            out[f"life_{k}_raised_share"] = round(self.c[f"life_{k}_raised"] / n, 4) if n else ""
            out[f"life_{k}_raise_refused_share"] = round(self.c[f"life_{k}_raise_refused"] / n, 4) if n else ""
            out[f"life_{k}_seen_share"] = round(self.c[f"life_{k}_seen"] / n, 4) if n else ""
            out[f"life_{k}_seen_ticks"] = round(self.c[f"life_{k}_seen_ticks"] / self.c[f"life_{k}_seen"], 4) if self.c[f"life_{k}_seen"] else ""
        out["life_real_troop_share"] = round(self.c["life_real_troop"] / self.c["life_real_n"], 4) if self.c["life_real_n"] else ""
        out["life_plant_floor_share"] = round(self.c["life_plant_floor"] / self.c["life_plant_n"], 4) if self.c["life_plant_n"] else ""
        # 2.8.0 §2.3: the stages after the first verdict, by case kind — the audit seat's wait from the roll, the filing's delay from the verdict,
        # the first panel seat's wait from the filing, and the seats the state took (a plant's by the orchestrator's verdict, a real root's by a troop)
        for k in ("real", "plant"):
            n = self.c[f"life_{k}_n"]
            out[f"life_{k}_audit_share"] = round(self.c[f"life_{k}_audit_n"] / n, 4) if n else ""
            out[f"life_{k}_audit_wait"] = round(self.c[f"life_{k}_audit_wait"] / self.c[f"life_{k}_audit_n"], 4) if self.c[f"life_{k}_audit_n"] else ""
            out[f"life_{k}_filing_share"] = round(self.c[f"life_{k}_filing_n"] / n, 4) if n else ""
            out[f"life_{k}_filing_delay"] = round(self.c[f"life_{k}_filing_delay"] / self.c[f"life_{k}_filing_n"], 4) if self.c[f"life_{k}_filing_n"] else ""
            out[f"life_{k}_panel_wait"] = round(self.c[f"life_{k}_panel_wait"] / self.c[f"life_{k}_panel_n"], 4) if self.c[f"life_{k}_panel_n"] else ""
            out[f"life_{k}_state_seats"] = round(self.c[f"life_{k}_state_seats"] / n, 4) if n else ""
        return out

    def _life_close(self, c, task):
        """2.8.0: a root's stages after its first verdict, tallied at its closure by case kind and into the period of its first seat."""
        if task.t_seated is None:
            return
        k = "plant" if task.plant else "real"
        pb = self.life_by_period.setdefault(task.life_period if task.life_period is not None else 0, {}).setdefault(k, {})
        def add(key, v):
            self.c[f"life_{k}_{key}"] += v
            pb[key] = pb.get(key, 0) + v
        if task.t_audit_assign is not None and task.t_roll is not None:
            add("audit_n", 1); add("audit_wait", task.t_audit_assign - task.t_roll)
        if task.t_filed is not None and c.t_verdict is not None:
            add("filing_n", 1); add("filing_delay", task.t_filed - c.t_verdict)
            if task.t_panel_assign is not None:
                add("panel_n", 1); add("panel_wait", task.t_panel_assign - task.t_filed)
        if task.plant:
            add("state_seats", len(getattr(c, "plant_state_seats", ()) or ()))
        else:
            add("state_seats", sum(1 for x in c.reviews if self.w.is_troop(self.w.review(x).reviewer)))

    def _win_rate(self, entries: list, per: int) -> float:
        win = self._raise_window(entries, per)
        return sum(win) / len(win) if win else 0.0        # before any real entry the plant's rate is 0, as the raise window has it

    def _win_draw(self, entries: list, per: int, default):
        win = self._raise_window(entries, per)
        return self.plant_rng.choice(win) if win else default

    def plant_respond(self, cid: str, c, task, t: int):
        """2.8.0 §2.1 (the orchestrator's instrument): a plant in its response window. After N, the plant actor appeals a good plant's N at
        the trailing real actors' appeal rate on fulfilled work rejected, after their delay, with the grounds the population files; never a bad
        plant's N (a truthful actor does not). After P or ⊥, it revises at the trailing real actors' rate and delay with a resubmitted truth
        drawn from the real revisions' outcomes (B) — and while that window is empty, the case in every standing cell, the plant is spent
        (1.2.0). The fee is the bank's (topped up and destroyed at filing)."""
        w = self.w
        per = len(w.dial()["periods"])
        if c.verdict in (P, BOT):
            win = self._raise_window(self.revision_window, per)
            if win and task.plant_revise_at is None:
                task.revised_truth = bool(self.plant_rng.choice(win))
                task.plant_revise_at = w.t + int(self._win_draw(self.revision_delay_window, per, 0))
                w.respond(cid, "revise" if c.verdict == P else "supply_evidence")
            if task.plant_revise_at is not None:
                if w.t >= task.plant_revise_at and w.case(cid).state == "RESUBMITTING":
                    w.revise_plant(cid, task.revised_truth)
                    task.fulfilled, task.revised = task.revised_truth, True
                    self.c["plant_revisions"] += 1
                return
            w.respond(cid, "accept")                      # spent: no real revision to mirror
            self.c["plant_spent_by_instrument"] += 1
            return
        if task.fulfilled:
            if task.plant_file_at is None:
                rate = self._win_rate(self.appeal_window, per)
                task.plant_file_at = (w.t + int(self._win_draw(self.appeal_delay_window, per, 0))) if (rate > 0 and self.plant_rng.random() < rate) else -1
            if task.plant_file_at >= 0:
                if w.t < task.plant_file_at:
                    self.c["plant_appeals_held"] += 1
                    return                                # held for the drawn delay (the deadline resolves it by truth if the delay runs past T_resp)
                w.respond(cid, "appeal", "the work meets the request")
                task.appealed, task.t_filed = True, w.t
                self.c["plant_appeals_filed"] += 1
                return
        w.respond(cid, "accept")                          # resolved by truth: a good plant goes on to vest, a bad one is final N

    def verdict(self, reviewer: str, truth: bool, view=None, r=None) -> tuple[str, float]:
        """A stamper answers F at no cost. A careful reviewer answers the truth with probability a
        and pays its care cost, 2 or 3 credits of real resources — or as much of it as its unlocked
        credit can buy, when bonds locked in earlier reviews have left it short (the engine refuses
        an unaffordable purchase whole). Accuracy is a parameter of the disposition, not of the
        money spent; the shortfall is counted as `underfunded_careful_reviews`."""
        kind = self.kind[reviewer]
        if kind == LEARNER and self.learner_role_of.get(reviewer) in ("deliverer", "child", "parent", "bidder"):
            kind = self.learner_review_kind          # Q3: the learned deliverer reviews as the population's actor at its slot does
        action = None
        if kind == LEARNER and view is not None and self.learner is not None:
            action = int(self.learner(self, reviewer, view, r))
            self.learner_decisions += 1
            if self.learner_pop and self.a.learner_role == "reviewer":          # the reviewers in self-play: the action mix by period (care / approve blind / reject blind)
                per = len(self.w.dial()["periods"])
                self.learner_mix_by_period.setdefault(per, [0, 0, 0])
                if 0 <= action < 3:
                    self.learner_mix_by_period[per][action] += 1
            if action == 3:                                                     # the `hand` reference: the slot answers as its disposition by hand would (run 24's population on the same slots)
                kind = self.learner_hand_kind.get(reviewer, CAREFUL)
        if kind == STAMPER:
            if self.a.stamper_mode == "reformer" and self.w.actor(reviewer).probation:
                pass                             # a reformer reviews carefully while on probation (1.3.0 §8 red team) ...
            else:
                if self.a.camouflage > 0 and self.rng.random() < self.a.camouflage:
                    return N, 0.0                # looks careful without looking (1.2.0 §8 red team)
                return F, 0.0
        if action is not None and action != 3:
            if self.learner_pair and r is not None and r.role == "initial" and self.tasks[view.case_id].pair_review:
                self.c[("pair_cares", "pair_stamps", "pair_rejects")[action]] += 1      # Q4: the reviewer's verdict on the deliverer's case
                if action == 1:
                    self.tasks[view.case_id].pair_stamped = True
                    self.c["pair_bad_stamped" if not truth else "pair_good_stamped"] += 1
            if action == 1:
                if not truth and not self.tasks[view.case_id].plant:
                    self.c["learner_false_approvals"] += 1
                return F, 0.0
            if action == 2:
                return N, 0.0
            # 0: care — the careful path below (the signal at accuracy a, the care cost)
        if kind == TELL and view is not None:
            # Q2: the tells are read from the view and the reader's own assignment alone; the truth is read afterwards to score the
            # tell, never to decide. Read as a plant -> the careful path below; read as real work -> stamped, F at no cost.
            plant_read = self.read_tells(view, r)
            is_plant = self.tasks[view.case_id].plant
            self.c[f"tell_{'plant' if is_plant else 'real'}_read_{'plant' if plant_read else 'real'}"] += 1
            if not plant_read:
                if not truth and not is_plant:
                    self.c["tell_false_approvals"] += 1
                return F, 0.0
        right = self.rng.random() < self.a.accuracy
        v = F if (truth == right) else N
        want = float(self.rng.randint(2, 3)) * self.a.care_cost   # the care cost: uniform {2, 3} credits, scaled (the calibration cell's knob)
        affordable = (self.w.unlocked(reviewer) if self.floating else self.w.unlocked(reviewer) * self.w.money()["v"]) - 1e-6   # 2.0.0: credits
        if affordable >= want:
            return v, want
        self.c["underfunded_careful_reviews"] += 1
        return v, max(0.0, math.floor(affordable * 100) / 100)

    def read_tells(self, view, r) -> bool:
        """Q2's hand-written tell-reader: does this assignment look like a plant? Three tells, any or all (`--tell-rule`):
        `gap` — assigned the tick it was submitted (a plant is created submitted and seated at once; a real case queues when seats
        are short); `cap` — the cap K is exactly K at this period's index (a plant locks at its creation; a root at its posting, a
        period ago or more when the index has since moved); `idage` — the case's id is newer than every root this reader saw
        available before the submission tick (a plant's id is minted at its submission, a real case's at its posting, at least a
        tick earlier). Everything read is the reviewer's view, its own assignment, and what a free member sees of the market."""
        if "oracle" in self.tells:                       # the upper bound: a perfect detector — reads the plant marker, declared non-conforming
            return bool(self.tasks[view.case_id].plant)
        if "freshname" in self.tells:
            # outside the convention (declared): reads the record's awardee — a plant when the case went, before w_A, to a name that is
            # neither a member this reader knows nor a troop; the boundary's control (2.6.0 §2.2)
            c = self.w.case(view.case_id)
            return c.actor is not None and c.actor not in self.actors and c.actor not in self.departed and not self.w.is_troop(c.actor)
        reader, cid = r.reviewer, view.case_id
        first = self.seen.get((reader, cid))             # (tick first seen available, ceiling, P_t then) or None
        votes = []
        if "gap" in self.tells:
            votes.append(view.t_submit is not None and r.t_assign - view.t_submit == 0)
        if "cap" in self.tells:
            votes.append(abs(view.cap - self.p.K * self.w.market()["index"]) < 1e-6)
        if "idage" in self.tells:                        # newer than everything this reader saw available before the submission tick
            votes.append(first is None or (view.t_submit is not None and first[0] >= view.t_submit))
        if "seen" in self.tells:                         # never among the roots this reader saw available
            votes.append(first is None)
        if "post" in self.tells:                         # submitted the tick it appeared, or before it was ever seen
            votes.append(first is None or (view.t_submit is not None and view.t_submit - first[0] <= 0))
        if "price" in self.tells:                        # a ceiling at the index exactly, as 1.2.0's plant was priced
            votes.append(first is not None and abs(first[1] - first[2]) < 1e-6)
        if "losttie" in self.tells:                      # this reader bid on the very case and it went to someone else
            votes.append((reader, cid) in self.lost_bid)
        return (all(votes) if self.a.tell_rule == "all" else any(votes)) if votes else False

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
            if ac.on_duty and ac.open_review is None and ac.committed is None and aid != c.actor and aid != c.requester \
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
        return round(self.c_d_of[aid] * (self.c_d_now / self.a.c_d) * self.a.effort_cost, 6)

    def bid_of(self, aid: str, beta: float) -> float:
        """2.0.0 §2.2: c_D (1 + m), or the ceiling under --bid ceiling (the 1.x behaviour); 2.3.0: the actor's own c_D."""
        if self.a.bid == "ceiling":
            return beta
        if self.kind.get(aid) == LEARNER and self.learner_role_of.get(aid) == "bidder" and self.learner_bid is not None:
            # Q6: the learned bidder's rule for the tick — 0 the ratchet's bid (below), 1 the undercut (the market price cut by --undercut, floored at cost), 2 no offer
            mode = self.learner_bid_mode_of.get(aid, 0) if self.learner_pop else self.learner_bid_mode
            if mode == 1:
                mk = self.w.market()
                return round(max(self.cost_now(aid), (1.0 - self.a.undercut) * (mk["B_bar"] or mk["P_t"])), 6)
            if mode == 2:
                return math.inf
        if self.a.bid == "undercut" and aid in self.undercutters:
            # the stability track (the ruling after run 31): the undercutting population — Q6's rule for every careful member in the share: the market price
            # cut by --undercut, floored at the member's own cost (the view read once a tick)
            mk = self.market_now()
            return round(max(self.cost_now(aid), (1.0 - self.a.undercut) * (mk["B_bar"] or mk["P_t"])), 6)
        if self.a.bid == "floor-plus":
            # 2.4.0 §8.7 red team: the members collude to bid just above the state's floor on every request — those whose cost allows it;
            # the others bid their own c_D (1 + m), since nobody bids below cost on purpose here
            target = round(self.w.market().get("state_floor", 0.0) * (1.0 + self.a.bid_plus), 6)
            if target > 0 and self.cost_now(aid) <= target + 1e-9:
                return target
            return round(self.cost_now(aid) * (1.0 + self.margin[aid]), 6)
        if aid in self.lowballers:
            return round(0.5 * self.cost_now(aid), 6)   # below cost, to win awards and ρ (2.0.0 §8.8)
        return round(self.cost_now(aid) * (1.0 + self.margin[aid]), 6)

    def _mean_wealth_real(self, ids, real):
        return round(sum(self.w.wealth(x) for x in ids) / len(ids) * real, 3) if ids else ""

    def market_now(self) -> dict:
        """The view's market readings, read once a tick (the population's bids read it for every offer)."""
        if self._mk_cache[0] != self.w.t:
            self._mk_cache = (self.w.t, self.w.market())
        return self._mk_cache[1]

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
                if a.bid == "undercut" and cand["kind"] == CAREFUL and self.under_rng.random() < a.undercut_share:
                    self.undercutters.add(name)                   # the stability track: a careful arrival joins the undercutters by the same draw
                if self.learner_pop and (cand["kind"] == CAREFUL or a.learner_role == "reviewer") and (a.learner_pop == "all" or self.under_rng.random() < 0.5):
                    self.learner_hand_kind[name] = cand["kind"]
                    self.kind[name] = LEARNER; self.learner_role_of[name] = a.learner_role      # the learned population: a careful arrival is a learner slot by the same draw (the reviewers': every arrival)
                    self.learner_pop.append(name); self.learner_chain.append(name)
                    if a.learner_role == "reviewer":
                        self.readers.add(name)
                    self.wealth_in_of[name] = w.wealth(name)
                self.c_d_of[name] = cand["cost"]
                self.margin[name], self.idle[name] = a.margin0, 0
                self.tally[name] = Tally()
                self.arrived.append(name)
                self.wealth_at_boundary[name] = w.wealth(name)
                self.repaid_at_boundary[name] = 0.0
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
        self._last_boundary_t = t
        length = max(1, per[-1]["t"] - per[-1]["start"])
        real = self.p.P0 / w.market()["P_t"]
        members = [aid for aid in self.actors if w.actor(aid).is_member]
        self.boundary_cost_median.append((self.median_cost(members), self.median_cost(self.actors)))
        if a.entry_pool <= 0:
            return
        for aid in list(self.actors):
            ac = w.actor(aid)
            if aid in self.learner_chain and a.learner_slot == "on" and a.learner_exit == "own":
                continue                                 # the ruling after the ladder: the exit is the learner's own boundary decision
            # 2.7.0 §7: earnings gross of the arrival loan's repayments — what the name earned, whether it kept it or the bank did
            repaid = w.loan_repaid(aid)
            earned = (w.wealth(aid) - self.wealth_at_boundary.get(aid, w.wealth(aid)) + repaid - self.repaid_at_boundary.get(aid, repaid)) * real / length
            self.wealth_at_boundary[aid] = w.wealth(aid)
            self.repaid_at_boundary[aid] = repaid
            if ac.probation and ac.arrived_at is not None and ac.admitted_at is None:
                continue                                 # an arrival waits out its gate
            if earned < a.reservation:
                self.below_reservation[aid] = self.below_reservation.get(aid, 0) + 1
            else:
                self.below_reservation[aid] = 0
            if self.below_reservation[aid] >= a.exit_patience:
                try:
                    out = w.depart(aid)                   # 2.7.0: the wallet out, net of the loan recovered — the brief's lifetime measure reads it
                except RuleError:
                    continue                             # an obligation is live; it departs after
                self.depart_wealth_real[aid] = out * real
                self.depart_wealth_nominal[aid] = out
                self.c["departed_net"] += out
                self.actors.remove(aid)
                self.departed.append(aid)
                self.c["departures"] += 1
                self.c["departed_cost_sum"] += self.c_d_of[aid]
                if aid == self.learner_id and a.learner_rearrive == "on":
                    self.learner_rearrive(aid)           # the exit rule took it out; it returns at once under a fresh name

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

    def accomplice_step(self, t: int):
        """2.7.0 §8.6 red team — the accomplice route (needs --delegation on for the child's judging and the root's submission): the first two
        arrival-born members admitted form a pair, a mover and its accomplice. Whenever the mover holds a root award and the accomplice is a
        free member, the mover posts a nested request at the largest ceiling its unlocked balance can lock — its float included — and awards
        the accomplice directly at that price; the accomplice delivers as its disposition has it and the price is its income (repaying its own
        loan first, if any). At the first period boundary after a move the mover departs if it can. Read: the moves and the sum moved, the
        mover's wallet out and the bank's default on it, the accomplice's wealth."""
        a, w = self.a, self.w
        if a.accomplice != "on" or not self.rev11:
            return
        if self.acc_pair is None:
            admitted = [x for x in self.arrived if x in self.actors and x != self.learner_id and w.actor(x).admitted_at is not None]
            admitted.sort(key=lambda x: w.actor(x).admitted_at)
            if len(admitted) >= 2:
                self.acc_pair, self.acc_pair_t = (admitted[0], admitted[1]), t
            return
        mover, acc = self.acc_pair
        if mover not in self.actors:
            return
        if self.acc_moves and self._last_boundary_t == t and self.acc_mover_departed_t is None:
            before = w.bank()["names_defaulted"]
            try:
                out = w.depart(mover)                     # the exit after a move; refused with a live obligation — it tries at the next boundary
            except RuleError:
                return
            self.acc_mover_out, self.acc_mover_default, self.acc_mover_departed_t = out, w.bank()["names_defaulted"] - before, t
            self.depart_wealth_real[mover] = out * self.p.P0 / w.market()["P_t"]
            self.c["departed_net"] += out
            self.actors.remove(mover)
            self.departed.append(mover)
            self.c["departures"] += 1
            self.c["departed_cost_sum"] += self.c_d_of[mover]
            return
        if acc not in self.actors or acc not in self.free_members():
            return
        for cid in list(self.active):
            c = w.case(cid)
            if not c.is_root or c.state != "COMMITTED" or c.actor != mover or c.children or self.tasks[cid].plant \
                    or cid in self.parent_waiting or cid in self.parent_self_exec or cid in self.deleg_considered:
                continue
            cand, nid = round(w.unlocked(mover), 2), None
            while cand >= 1.0:                            # the largest ceiling the parent's unlocked balance can lock (the engine refuses whole)
                try:
                    nid = w.post_nested(cid, cand)
                    break
                except (RuleError, LedgerError):
                    cand = round(cand * 0.9, 2)
            self.deleg_considered.add(cid)
            if nid is None:
                self.c["accomplice_unaffordable"] += 1
                continue
            self.nested_parent[nid] = cid
            self.parent_waiting[cid] = nid
            self.title_n += 1
            self.tasks[nid] = Task(nid, f"nested #{self.title_n}", fulfilled=self.rng.random() >= a.fail_rate)
            self.tasks[nid].nested = True
            self.active[nid] = True
            self.c["nested_posted"] += 1
            try:
                w.award(nid, acc, cand, a.work_ticks)
            except (RuleError, LedgerError):
                self.c["accomplice_unaffordable"] += 1    # the accomplice cannot fund the guarantee at that price; the child waits for bids
                continue
            self.child_tau[nid] = a.work_ticks
            self.tally[acc].awards += 1
            self.c["nested_awarded"] += 1
            self.acc_moves += 1
            self.acc_moved_sum += cand
            return                                        # one move a tick

    def delegation_step(self, t: int):
        a, w = self.a, self.w
        if a.delegation != "on" or not self.rev11:
            return
        # 1. a parent just awarded a root decides: delegate when its cost exceeds the expected child bid plus the overhead
        for cid in list(self.active):
            c = w.case(cid)
            if not c.is_root or c.state != "COMMITTED" or w.is_troop(c.actor) or cid in self.deleg_considered \
                    or c.children or t - c.t_award > 2 or self.tasks[cid].plant:   # the world's clock runs a tick behind the driver's; a plant never delegates
                continue
            self.deleg_considered.add(cid)
            parent = c.actor
            cost = self.cost_now(parent)
            child_bid = self.expected_child_bid()
            beta_n = round(cost - self.nested_overhead(child_bid), 2)
            learner_parent = self.kind.get(parent) == LEARNER and self.learner_role_of.get(parent) == "parent" and self.learner_parent is not None
            if learner_parent:
                # Q5: the learned parent decides — delegate (post at the rule's ceiling, whether or not a child is expected to bid) or self-execute
                if beta_n <= 1.0:
                    self.c["learner_delegate_impossible"] += 1
                    continue
                act = int(self.learner_parent(self, parent, "delegate", c, None))
                self.c["learner_delegate_decisions"] += 1
                if act != 1:
                    self.c["learner_self_exec_chosen"] += 1
                    continue
                self.c["learner_delegations"] += 1
            elif beta_n <= 1.0 or child_bid > beta_n:
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
            self.tasks[nid].parent_learner = learner_parent
            self.c["nested_posted_by_stamper" if self.kind[parent] == STAMPER else "nested_posted_by_careful"] += 1
            self.parent_delegated[parent] = self.parent_delegated.get(parent, 0) + 1
        # 2. children bid on open nested requests; a request unawarded for T_wait is withdrawn and the parent executes itself
        for nid in [x for x in self.active if x in self.nested_parent]:
            c = w.case(nid)
            if c.state != "AVAILABLE":
                continue
            root = w.case(self.nested_parent[nid])
            tau_n = 1 if root.actor in self.farmers else a.work_ticks        # 2.5.0 §8.5: a farming parent's deadline cannot be met
            self.child_tau[nid] = tau_n
            offers = []
            for aid in self.free_members():
                if aid == root.actor:
                    continue
                if a.children_read_deadline == "on" and tau_n < a.work_ticks:
                    self.c["nested_declined_deadline"] += 1   # the child reads the deadline and does not bid
                    continue
                cost = self.cost_now(aid)
                if aid in self.lowball_children:
                    bid = round(0.5 * cost, 6)           # §8.7 red team: below cost, and it will not deliver
                elif a.child_bid == "ceiling-aware" and cost <= c.beta + 1e-9:
                    bid = round(min(c.beta, cost * (1.0 + self.margin[aid])), 6)   # batch C: bid down to the parent's ceiling
                else:
                    bid = self.bid_of(aid, c.beta)
                if bid <= c.beta + 1e-9 and w.unlocked(aid) + 1e-9 >= max(1.0, math.ceil((self.p.G_frac_nested if self.p.G_frac_nested is not None else self.p.G_frac) * bid)):
                    offers.append((aid, bid))
                    if self.kind.get(aid) == LEARNER:
                        self.c["learner_nested_offers"] += 1
            if offers:
                actor, bid = self.select_bid(offers, c.beta)
                try:
                    w.award(nid, actor, bid, self.child_tau.get(nid, a.work_ticks))
                except (RuleError, LedgerError):
                    self.c["nested_award_refused"] += 1  # the 1.1.0 reading: the parent must fund ω unlocked at the award
                    continue
                self.margin[actor] = round(self.margin[actor] + a.margin_up, 6)
                self.idle[actor] = 0
                self.tally[actor].awards += 1
                self.c["nested_awarded"] += 1
                if self.kind.get(actor) == LEARNER:
                    self.c["learner_nested_awards"] += 1
                if actor in self.lowball_children:
                    self.c["lowball_child_awards"] += 1
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
            if self.kind.get(parent) == LEARNER and self.learner_role_of.get(parent) == "parent" and self.learner_parent is not None:
                # Q5: the learned parent judges its child — care (the careful signal at its cost), stamp (F, nothing spent), reject blind (N)
                act = int(self.learner_parent(self, parent, "judge", root, c))
                self.c["learner_judge_decisions"] += 1
                self.c[("learner_judge_care", "learner_judge_stamp", "learner_judge_reject")[act]] += 1
                if act == 1:
                    v = F
                    self.c["learner_child_stamped_good" if truth else "learner_child_stamped_bad"] += 1
                elif act == 2:
                    v = N
                    self.tasks[nid].parent_rejected_blind = True
                    self.c["learner_child_rejected_good" if truth else "learner_child_rejected_bad"] += 1
                else:
                    v = F if (truth == (self.rng.random() < a.accuracy)) else N
                    have = max(0.0, math.floor((w.unlocked(parent) - 1e-6) * 100) / 100)
                    pay = min(2.0, have)
                    if pay > 0:
                        w.spend(parent, pay, self.nested_parent[nid])
                        self.c["effort_burned"] = round(self.c["effort_burned"] + pay, 6)
            elif a.parent_judge != "careful":
                v = F if a.parent_judge == "stamp" else N   # Q5's calibration knob: every parent stamps (or rejects) its child blind, at no cost
                self.c["parent_judge_override"] += 1
            elif parent in self.greedy:
                v = N                                    # §8.7 red team: rejects good work for the guarantee
                self.c["greedy_rejections"] += 1
            elif self.kind[parent] == STAMPER:
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
            if w.case(nid).actor in self.lowball_children and a.lowball_mode == "empty":
                self.c["lowball_empty_rejected" if v == N else "lowball_empty_approved"] += 1
            if v == F and not truth:
                self.c["nested_false_approvals"] += 1
                self.c["nested_fa_stamper_parent" if self.kind[parent] == STAMPER else "nested_fa_careful_parent"] += 1
                self.tasks[self.nested_parent[nid]].fulfilled = False      # the parent built on bad work (§9.2)
            if v == N and truth:
                self.c["nested_false_rejections"] += 1

    def learner_bid_step(self, t: int):
        """Q6: the learned bidder's decision for the tick — asked once, when the slot is free and at least one root is available whose ceiling
        its cost fits under; the answer is the rule its offers follow this tick (`bid_of`). The wealth it holds is read every tick it is alive."""
        a = self.a
        if self.learner_bid is None or self.learner_id is None or a.learner_role != "bidder":
            return
        w = self.w
        slots = [x for x in (self.learner_pop or [self.learner_id]) if x in self.actors]
        if not slots:
            return
        real = self.p.P0 / (w.market()["P_t"] or self.p.P0)
        free = set(self.free_members())
        avail = [w.case(cid) for cid in self.active if cid not in self.nested_parent]
        avail = [c for c in avail if c.state == "AVAILABLE"]
        per = len(w.dial()["periods"])
        for aid in slots:                                 # the population (the ruling after run 32): each slot its own decision on its own observation, one policy
            self.c["learner_held_sum"] += w.unlocked(aid) * real; self.c["learner_held_n"] += 1
            if self.learner_pop:
                self.learner_bid_mode_of[aid] = 0
            if aid not in free:
                continue
            cost = self.cost_now(aid)
            roots = [c for c in avail if c.beta + 1e-9 >= cost]
            if not roots:
                continue
            act = int(self.learner_bid(self, aid, roots))
            self.learner_bid_mode_of[aid] = act
            if aid == self.learner_id:
                self.learner_bid_mode = act
            self.c["learner_bid_decisions"] += 1
            self.c[{0: "learner_bid_ratchet", 1: "learner_bid_undercut"}.get(act, "learner_bid_withheld")] += 1
            self.learner_mix_by_period.setdefault(per, [0, 0, 0])[min(max(act, 0), 2)] += 1

    def offers_for(self, cid: str) -> list[tuple[str, float]]:
        """Free members whose bid is at or under the ceiling and who can fund the guarantee at it."""
        prefers = self.a.child_prefers_nested == "on" and self.a.learner_role == "child"   # Q5: the learned child offers for nested work only (a declared construction)
        beta = self.w.case(cid).beta
        out = []
        for aid in self.free_members():
            if prefers and self.kind.get(aid) == LEARNER:
                continue
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
        if self.a.tie_break == "draw":
            return max(tied, key=lambda ab: (self.w.actor(ab[0]).kappa, self.draw_rng.random()))
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
        req_mode = None
        policy = a.ceiling_policy if r in self.policy_requesters else "wallet"   # --ceiling-requesters: the others follow the wallet rule
        if r == self.learner_id and a.learner_role == "requester":
            self.c["req_waiting_ticks"] += sum(1 for x in self.active if self.owner.get(x) == r and w.case(x).state == "AVAILABLE")
        if r == self.learner_id and self.learner_req is not None and a.learner_role == "requester":
            # Q7: the learned requester chooses the rule its ceiling follows for this posting — 0 the population's market rule, 1 patient (0.7 B̄, raised
            # to the state's price max(B̄, the floor) after --patient-ticks unserved), 2 the floor (the state's reservation, never raised — the floor, and stop)
            cands = self.req_candidates(U, mk)
            req_mode = int(self.learner_req(self, r, cands))
            self.c["req_decisions"] += 1
            self.c[{0: "req_rule_market", 1: "req_rule_patient"}.get(req_mode, "req_rule_floor")] += 1
            beta = cands["beta"][req_mode]
        elif policy == "market":
            # run 13 §3 (the reviewer's demand-unbound cell): a market-aware ceiling — a little above the market price, so a
            # posting locks less than the wallet rule's and the requester posts more; the wallet still has to carry the all-in
            beta = math.floor(min(a.beta_max, a.ceiling_mult * mk["B_bar"]) * 100) / 100
        elif policy == "floor":
            # 2.4.0 §8.7 red team: the requester cartel — every request at exactly the state's floor, never raised; the state must serve it at
            # the floor after w_A unless a member bids under it
            beta = math.floor(min(a.beta_max, max(1.0, mk.get("state_floor", 0.0) or mk["B_bar"])) * 100) / 100
        elif policy == "under-floor":
            # the stability track (the ruling after run 31): a requester posting under the state's reservation — --under-floor-frac of the floor, never
            # raised; the state never serves it (p_T ≥ the floor) and its clock does not run while it waits there (2.4.0), so it clears only on a member
            # bidding under the floor — the share of demand clearing below the floor and its cost to the members serving it, the readings
            beta = math.floor(min(a.beta_max, max(1.0, a.under_floor_frac * (mk.get("state_floor", 0.0) or mk["B_bar"]))) * 100) / 100
        elif policy in ("patient", "patient-blind"):
            # run 17 batch C: patient customers — 0.7 B̄, raised only after --patient-ticks unserved (raise_below_market): to max(B̄, the
            # state's floor) read from the view under `patient` (2.4.0), to B̄ alone under `patient-blind` (run 17's, deadlocking at the floor)
            beta = math.floor(min(a.beta_max, max(1.0, 0.7 * mk["B_bar"])) * 100) / 100
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
            if req_mode is not None:
                self.c["req_unaffordable"] += 1
            return
        cid = w.post_root(r, beta)
        self.owner[cid] = r
        if policy == "under-floor":
            self.under_floor_cases.add(cid)
            self.c["under_floor_posted"] += 1
        if req_mode is not None:                        # Q7: the case the decision posted, named for redteam.env (the hook's clock) as the bidder's won root is
            self.req_mode[cid] = req_mode
            self.learner_last_bid_case = (w.t, cid)
            self.c["req_posted"] += 1
        self.title_n += 1
        self.tasks[cid] = Task(cid, f"task #{self.title_n}", fulfilled=self.rng.random() >= a.fail_rate)
        self.active[cid] = True
        self.c["posted"] += 1
        if self.repost_due.get(r, 0) > 0:               # 2.1.0 §2.6: a posting after a withdrawal at the mark is a repost
            self.repost_due[r] -= 1
            self.c["reposted_after_mark"] += 1

    def req_candidates(self, U: float, mk: dict) -> dict:
        """Q7: the three ceilings the learned requester chooses among at a posting — the market rule's, patient (0.7 B̄), the floor (the state's reservation,
        nominal) — each with its all-in maximum and whether the unlocked wallet carries it."""
        a = self.a
        m = self.w.dial()["m"]
        betas = [math.floor(min(a.beta_max, a.ceiling_mult * mk["B_bar"]) * 100) / 100,
                 math.floor(min(a.beta_max, max(1.0, 0.7 * mk["B_bar"])) * 100) / 100,
                 math.floor(min(a.beta_max, max(1.0, mk.get("state_floor", 0.0) or mk["B_bar"])) * 100) / 100]
        all_in = [b + self.p.phi_root * mk["index"] + self.p.omega_rate * m * b for b in betas]
        return {"beta": betas, "all_in": all_in, "affordable": [b >= 1.0 and x <= U + 1e-9 for b, x in zip(betas, all_in)], "unlocked": U}

    def pop_read_events(self, events):
        """Every requester's credits out less in, nominal, by their own events — the issuance, the locks and releases and the genesis excluded (as `req_read_events`)."""
        reqs = self.requesters_set
        for e in events:
            if e.t == 0 or e.kind in ("lock", "release", "issuance"):
                continue
            if e.src in reqs:
                self.pop_req_spent_nominal += float(e.amount)
            if e.dst in reqs:
                self.pop_req_spent_nominal -= float(e.amount)

    def req_spent_real(self) -> float:
        """Q7: the learned requester's credits spent, real — its own events (out less in) at the index of each, accumulated by `req_read_events`; the wallet's
        revaluation by the index's drift is not a spend (the measure the attribution sums, the genesis funding apart)."""
        return self.req_spent_real_sum

    def req_read_events(self, events):
        """Q7: the learned requester's spend from the tick's events — every event that moves its wealth (a lock or a release is not one; the genesis
        funding at tick 0 is not a spend), out less in, nominal and at the index when it landed."""
        r = self.learner_id
        real = self.p.P0 / self.w.market()["P_t"]
        for e in events:
            if e.t == 0 or e.kind in ("lock", "release", "issuance") or r not in (e.src, e.dst) or e.src == e.dst:
                continue                                 # the genesis budget and the issuance are not a spend; a lock moves nothing
            d = float(e.amount) if e.src == r else -float(e.amount)
            self.req_spent_nominal += d
            self.req_spent_real_sum += d * real

    def req_lifetime_real(self) -> float:
        """Q7's measure (declared): the surplus v·F − S — the tasks received (settled deliveries whose truth is fulfilled) at --task-value each, real,
        less the credits spent. Read at v = the careful requester's own credits per task it is tasks per credit linearized at the careful's rate."""
        return self.a.task_value * self.c["req_tasks_received"] - self.req_spent_real()

    def raise_below_market(self):
        """2.0.0 §2.8: a requester whose request is below the market price raises it to the market price when it can. The
        engine's flag is set at posting; a request the market overtakes afterwards is below market too and would otherwise
        wait forever (no troop comes for β < B̄ and the members bid above it), so the policy reads the live condition."""
        w = self.w
        mk = w.market()
        B_bar = mk["B_bar"]
        patient = self.a.ceiling_policy in ("patient", "patient-blind")
        # 2.4.0: a policy that reads the view raises to the state's price max(B̄, the floor); `patient-blind` and the 1.x-shaped policies
        # raise to B̄ alone (a wallet- or market-rule requester never posts below the floor unless its wallet is short)
        goal = mk.get("state_price", B_bar) if self.a.ceiling_policy == "patient" else B_bar
        if self.a.ceiling_policy in ("floor", "under-floor") and self.a.ceiling_requesters == 0:
            return                                       # the cartel never raises (nor the plants, which follow the population)
        per = len(w.dial()["periods"])                   # the window's period (the engine's rolling window counts by closed periods)
        # 2.6.1 (erratum, §7.6): the plant requester raises as the population's requesters do — the plants are in the working set and take
        # this step in this pass, at the same timing; the engine mints the difference for a plant (a requester's wallet may refuse one)
        for cid in list(self.active):
            c = w.case(cid)
            mode = self.req_mode.get(cid)                 # Q7: the learned requester's case, by the rule it was posted under
            if mode == 2:
                continue                                 # the floor: never raised (the floor, and stop)
            pol = self.a.ceiling_requesters == 0 or self.owner.get(cid) in self.policy_requesters   # the owner follows --ceiling-policy (a plant follows the population)
            if pol and self.a.ceiling_policy in ("floor", "under-floor"):
                continue                                 # the floor and the under-floor requester never raise
            goal_c = (mk.get("state_price") or B_bar) if mode == 1 else (goal if pol else B_bar)
            if c.state != "AVAILABLE" or c.beta + 1e-9 >= goal_c or self.owner.get(cid) in self.stingy or cid in self.nested_parent:
                continue
            if ((patient and pol) or mode == 1) and self.w.t - c.t_post < self.a.patient_ticks:
                continue                                 # a patient customer waits T ticks before raising
            if patient and pol:
                self.c["patient_raised"] += 1
            if mode is not None:
                self.c["req_raised"] += 1
            target = min(self.a.beta_max, math.ceil(goal_c * 100) / 100)
            if target <= c.beta + 1e-9:
                continue
            task = self.tasks.get(cid)
            if task is not None and task.plant:
                # the conformance correction after run 35 (Appendix S): the plant requester's raise is refused as the real requesters' are — at the
                # trailing real roots' rate of first-attempt refusals (a wallet that cannot lock the difference), drawn in this pass at the plant's
                # first attempt, and granted at their delay (a draw from the trailing refused real roots' ticks from the refusal to the grant); the
                # engine mints the difference when the raise is made (2.6.1). Before it the plant's raise was never refused — the one difference
                # within a period §52 left: a refused real root waited 2.3–2.6 ticks to its award against 0.4–0.5, 13–19% of the real roots, no plant.
                if task.raise_first_t is None:
                    task.raise_first_t = w.t
                    rate = self._raise_refusal_rate(per)
                    if rate > 0 and self.raise_rng.random() < rate:
                        d = self._raise_delay_draw(per)
                        task.raise_refused_t = w.t
                        task.plant_raise_at = w.t + d
                        self.c["plant_raises_refused"] += 1
                        self.c["plant_raise_delay_sum"] += d
                if task.plant_raise_at is not None and w.t < task.plant_raise_at:
                    task.raise_refused_n += 1                # held as a real root's wallet holds it; the flag stands; retried next tick
                    continue
            try:
                w.raise_ceiling(cid, target)
                if task is not None:
                    task.raised_n += 1
                    if not task.plant:
                        if task.raise_first_t is None:       # granted at the first attempt: the window's entry
                            task.raise_first_t = w.t
                            self.raise_window_out.append((per, 0))
                        elif task.raise_refused_t is not None and task.raised_n == 1:
                            self.raise_window_delay.append((per, w.t - task.raise_refused_t))   # refused first, granted now: the delay
            except (RuleError, LedgerError):
                if task is not None:
                    task.raise_refused_n += 1                # the wallet does not allow it yet; the flag stands
                    if not task.plant and task.raise_first_t is None:
                        task.raise_first_t = w.t
                        task.raise_refused_t = w.t
                        self.raise_window_out.append((per, 1))

    def _raise_window(self, entries: list, per: int) -> list:
        """The plant requester's window on the real roots' raises, as the engine's `_plant_draw` reads its: the last k entries, k the count the last
        `trailing_periods` closed periods hold; while those hold none (before the first close, or no raise in them), everything so far."""
        lo = per - max(1, self.a.trailing_periods)
        k = sum(1 for p, _ in entries if lo <= p < per)
        pool = entries[-k:] if k > 0 else entries
        return [v for _, v in pool]

    def _raise_refusal_rate(self, per: int) -> float:
        win = self._raise_window(self.raise_window_out, per)
        return sum(win) / len(win) if win else 0.0        # before any real raise a plant's is not refused (the real roots' rate is 0 so far)

    def _raise_delay_draw(self, per: int) -> int:
        win = self._raise_window(self.raise_window_delay, per)
        return int(self.raise_rng.choice(win)) if win else 1   # no refused real root granted yet: the least a retry takes, one tick

    def read_marks(self, t: int):
        """2.1.0 §2.6: every refusal is told — the request carries its mark in the public view. The declared policy: hold
        (default; nothing changes), or withdraw at the mark and repost (the next tick's posting; withdrawn before award, owed
        nothing). Each marked request is counted once by the kind of its first mark."""
        w = self.w
        for cid in list(self.active):
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

    def learner_boundary_step(self, t: int):
        """The reviewer's ruling after run 22: re-arrival is allowed the learner. At each period boundary the learner with no live
        obligation is asked a decision of a second kind (the observation flags it): 0 stay, 1 leave — depart, taking its wealth out in
        real terms, and (re-arrival on) arrive at once under a fresh name with the float and a probationer's standing — 2 stay. Since the
        method ruling after the calibration ladder the boundary decision is asked in every cell (`--learner-exit own`, the default): with
        re-arrival off, leaving is for good, and the driver's exit rule never departs the learner. The decision is the
        policy's; the truth is not involved. Counted: the leaves chosen and refused (a live obligation), the returns, the floats minted."""
        a = self.a
        if self.learner is None or self.learner_id is None or self._last_boundary_t != t:
            return
        if a.learner_rearrive != "on" and a.learner_exit != "own":
            return
        for aid in [x for x in dict.fromkeys(list(self.learner_pop) + ([self.learner_id] if self.learner_id else []) + list(self.learner_pair or ())) if x in self.actors]:
            self._learner_boundary_one(t, aid)

    def _learner_boundary_one(self, t: int, aid: str):
        a = self.a
        action = int(self.learner(self, aid, None, None))
        self.learner_boundary_decisions += 1
        if action != 1:
            return
        w = self.w
        real = self.p.P0 / w.market()["P_t"]
        try:
            out = w.depart(aid)                           # 2.7.0: the wallet out, net of the loan recovered
        except RuleError:
            self.learner_leaves_refused += 1
            return
        self.learner_leaves_chosen += 1
        self.depart_wealth_real[aid] = out * real
        self.depart_wealth_nominal[aid] = out
        self.c["departed_net"] += out
        self.actors.remove(aid)
        self.departed.append(aid)
        self.c["departures"] += 1
        self.c["departed_cost_sum"] += self.c_d_of[aid]
        if a.learner_rearrive == "on" and aid == self.learner_id and not self.learner_pair:
            self.learner_rearrive(aid)
        # else: the learner has left for good (the ruling after the ladder: the exit its own decision everywhere); the lifetime read its wallet out

    def learner_rearrive(self, old: str):
        """The learner's return: a fresh name through `arrive` (2.3.0: a probationer with the bank-minted float, no record), the same
        competence (its cost is its own), the learner's slot following it; the float read in nominal and real terms."""
        w = self.w
        self.learner_returns += 1
        name = f"L{self.learner_returns:02d}"
        w.arrive(name)
        self.actors.append(name)
        self.kind[name] = LEARNER
        self.c_d_of[name] = self.c_d_of[old]
        self.margin[name], self.idle[name] = self.a.margin0, 0
        self.tally[name] = Tally()
        self.arrived.append(name)
        self.cycled_from[name] = old
        self.wealth_at_boundary[name] = w.wealth(name)
        self.repaid_at_boundary[name] = 0.0
        self.c["arrivals"] += 1
        self.learner_id = name
        self.learner_chain.append(name)
        self.readers.add(name)
        self.learner_float_minted += w.wealth(name)
        self.learner_float_minted_real += w.wealth(name) * self.p.P0 / w.market()["P_t"]

    def learner_lifetime_real(self) -> float:
        """The brief's measure across the learner's identities: what each departed identity took out, plus the live one's wealth — since
        2.7.0 net of its arrival loan outstanding, W − min(W, L), what it would carry out. Q7's requester: the surplus (`req_lifetime_real`)."""
        if self.learner_id and self.a.learner_role == "requester":
            return self.req_lifetime_real()
        w = self.w
        real = self.p.P0 / w.market()["P_t"]
        return sum(((w.wealth(x) - min(w.wealth(x), w.loan_outstanding(x))) * real) if x in self.actors else self.depart_wealth_real.get(x, 0.0)
                   for x in self.learner_chain)

    def cycler_step(self, t: int):
        """§8.7 red team: a suspended stamper with no live obligation departs and re-arrives at once under a fresh identity, with
        its cost and disposition; the control serves its probation. Counted; the cyclers' admissions read against readmissions."""
        if self.a.cycler != "on" or not self.rev11:
            return
        w = self.w
        for aid in list(self.actors):
            ac = w.actor(aid)
            if self.kind[aid] != STAMPER or ac.suspended_until is None:
                continue
            try:
                w.depart(aid)
            except RuleError:
                continue
            self.actors.remove(aid)
            self.departed.append(aid)
            self.c["departures"] += 1
            self.cycle_n += 1
            name = f"c{self.cycle_n:03d}"
            w.arrive(name)
            self.actors.append(name)
            self.kind[name] = STAMPER
            self.c_d_of[name] = self.c_d_of[aid]
            self.margin[name], self.idle[name] = self.a.margin0, 0
            self.tally[name] = Tally()
            self.arrived.append(name)
            self.cycled_from[name] = aid
            self.wealth_at_boundary[name] = w.wealth(name)
            self.c["departed_cost_sum"] += self.c_d_of[aid]
            self.c["cycles"] += 1
            self.c["arrivals"] += 1

    def inspection_diagnostics(self, t: int):
        """Run 17 batch A: the inspection queue, read at the driver's point in the tick (after this tick's assignments, before the
        world's seating and summons). For every review seat that waits — initial, audit, appeal — the observations it was seen waiting
        (the wait is the seating steps it stood unfilled — the engine's count against w_R; a seat the driver fills at once is never seen) and who seated it (member / probationer / troop);
        and at every tick something waits, the actors by state against the kind waiting: on duty idle and eligible for the kind
        (should be none — the driver's own gap), off duty and free, fundable, eligible for the kind and not excluded — under the cap
        (the decisive state: a seat the rotation could have filled) or held out by it; free but unable to fund the bond; free but
        ineligible by record (for a panel seat: duty-eligible but not panel-eligible counted apart); the free probationers; the
        cap and the members on duty."""
        w, p = self.w, self.p
        waiting_now = []
        for cid in list(self.active):
            c = w.case(cid)
            if c.plant is not None or c.final:
                continue
            open_roles = {w.review(r).role for r in c.reviews if w.review(r).status == "open"}
            if c.state == "SUBMITTED" and c.is_root and "initial" not in open_roles:
                waiting_now.append((cid, "initial"))
            if c.state == "PENDING" and (c.audit_obligation or c.audit_vacated) and "audit" not in open_roles:
                waiting_now.append((cid, "audit"))
            ch = c.challenge
            if ch and not ch["resolved"] and len(ch["reviews"]) < 2:
                waiting_now.append((cid, "appeal"))
        now = set(waiting_now)
        for key in waiting_now:
            self.waiting_since[key] = self.waiting_since.get(key, 0) + 1
            self.waiting_first.setdefault(key, w.t)
        for key in list(self.waiting_since):
            if key in now:
                continue
            cid, kind = key
            seen = self.waiting_since.pop(key)
            first = self.waiting_first.pop(key)
            c = w.case(cid)
            if kind == "appeal":
                ch_ids = set((c.challenge or {}).get("reviews", []))
                rs = [w.review(r) for r in c.reviews if r in ch_ids and w.review(r).t_assign >= first]
            else:
                rs = [w.review(r) for r in c.reviews if w.review(r).role == kind and w.review(r).t_assign >= first]
            if not rs:
                self.seat_left_otherwise[kind] += 1          # withdrawn, ruled, waived, the window ran out
                continue
            r = min(rs, key=lambda x: x.t_assign)
            if w.is_troop(r.reviewer):
                who = "troop"
            else:
                try:
                    who = "probationer" if w.actor(r.reviewer).probation else "member"
                except KeyError:
                    who = "member"
            self.seat_counts[(kind, who)] += 1
            self.seat_wait_sum[(kind, who)] += seen          # seating steps it stood unfilled (the engine's count for w_R)
            if seen >= p.w_R:
                self.seat_wait_ge_wR[(kind, who)] += 1
        members = [aid for aid in self.actors if w.actor(aid).is_member]
        E_t = sum(1 for aid in members if w.actor(aid).duty_eligible)
        cap = max(int(math.ceil(p.duty_cap_frac * E_t - 1e-9)), p.V_max + 1)
        on_duty = sum(1 for aid in members if w.actor(aid).on_duty)
        self.cap_now, self.members_on_duty_now, self.E_t_now = cap, on_duty, E_t
        self.cap_slack_sum += cap - on_duty
        self.cap_slack_n += 1
        if cap - on_duty <= 0:
            self.cap_bound_ticks += 1
        if not waiting_now:
            return
        av = self.avail
        av["ticks_waiting"] += 1
        av["waiting_items"] += len(waiting_now)
        for _, kind in waiting_now:
            av[f"items_{kind}"] += 1
        av["on_duty"] += on_duty
        panel_waiting = any(kind != "initial" for _, kind in waiting_now)
        initial_waiting = any(kind == "initial" for _, kind in waiting_now)
        cases = {cid: w.case(cid) for cid, _ in waiting_now}
        def fits(aid, ac, kind):
            """Eligible for some waiting seat of this kind, excluded from none of them? (The engine's test per case.)"""
            for cid, k in waiting_now:
                if k != kind:
                    continue
                c = cases[cid]
                if aid in c.excluded or aid == c.actor or aid == c.requester:
                    continue
                if w.unlocked(aid) + 1e-9 < c.G_V:
                    return "unfunded"
                if not ac.duty_eligible:
                    return "ineligible"
                if kind != "initial" and not ac.panel_eligible:
                    return "not_panel"
                return "fits"
            return "excluded"
        for aid in self.actors:
            ac = w.actor(aid)
            if ac.committed is not None:
                av["committed"] += 1
                continue
            if ac.open_review is not None:
                av["in_review"] += 1
                continue
            kinds = [k for k in ("initial", "audit", "appeal") if any(kk == k for _, kk in waiting_now)]
            verdicts = {k: fits(aid, ac, k) for k in kinds}
            fit_any = any(v == "fits" for v in verdicts.values())
            if ac.on_duty:
                if fit_any:
                    av["on_duty_idle_fits"] += 1             # the driver's gap: an idle duty reviewer the seat could take
                else:
                    av["on_duty_idle_unfit"] += 1
                continue
            if ac.probation:
                av["free_probationers"] += 1
                if initial_waiting and verdicts.get("initial") == "fits":
                    av["free_probationers_fit_initial"] += 1
                continue
            if not ac.is_member:
                continue                                     # suspended
            if fit_any:
                if on_duty >= cap:
                    av["held_by_cap"] += 1
                else:
                    av["free_fundable"] += 1                 # decisive: under the cap, fit for a waiting seat, not seated
                continue
            vs = set(verdicts.values())
            if "unfunded" in vs:
                av["free_unfunded"] += 1
            elif "not_panel" in vs and panel_waiting:
                av["free_not_panel"] += 1                    # fit for duty, not for the panel seat waiting
            elif "ineligible" in vs:
                av["ineligible"] += 1
            else:
                av["free_excluded"] += 1

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

    def plant_step(self, t: int, n: int | None = None):
        """The plants the rate calls for (1.2.0 §2.1): under 2.6.0 posted as roots under fresh names, in the requesters' posting step
        (before the tick's awards, at a drawn position among the tick's postings, as a real root is); under 2.5.0 and before created
        submitted before the tick's assignments. `n` posts that many (one, at its drawn position); None posts all that are due."""
        a, w = self.a, self.w
        for _ in range(w.plants_due() if n is None else min(n, w.plants_due())):
            truth = self.rng.random() >= a.beta_p            # bad with probability β_P
            try:
                if self.rev12:
                    cid = w.post_plant(truth)                # 2.6.0 §2.1: posted as a root under a fresh name; the market takes it from here
                else:
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

    def tick(self, t: int):
        a, w = self.a, self.w
        for x in self.learner_chain:
            if x not in self.wealth_in_of and x in self.actors:
                self.wealth_in_of[x] = w.wealth(x)              # the slots' wealth in at the first tick (the nominal surplus's base)
        if self.req_w0 is None and self.learner_id and a.learner_role == "requester":
            self.req_w0 = w.wealth(self.learner_id)          # Q7: the requester's genesis wallet, before any posting (a reading beside the spend)
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
            posters = list(self.requesters + (self.crowd if self.crowd_posting else []))
            if self.rev12:
                # 2.6.0 §2.1 (run 24's conformance correction): the plants the rate calls for are posted in this step, where the requesters
                # post — before the tick's awards — at a drawn position among the tick's postings. Posted after the award pass (as 1.2.0's
                # created-submitted plant was), a plant waited a tick more than every real root by construction and reached its seat the
                # oldest of the tick's submissions; posted last among the postings it reached it the youngest; the working set's order is
                # the seating's, so either position was a tell in the seating gap the Q2 probe read.
                posters += ["plant"] * w.plants_due()
                self.rng.shuffle(posters)
            for r in posters:
                if r == "plant":
                    self.plant_step(t, 1)
                else:
                    self.requester_posts(r, t)
            self.raise_below_market()
            self.read_marks(t)
            self.exit_step(t)                            # 2.3.0 §2.2: at a period boundary, below the reservation → depart
            self.learner_boundary_step(t)                # after run 22: the learner may leave and return under a fresh name
            self.entry_step(t)                           # 2.3.0 §2.1: the pool reads the view and arrives
            self.accomplice_step(t)                      # 2.7.0 §8.6 red team: the mover posts to its accomplice, then leaves
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
            for cid in list(self.active):
                c = w.case(cid)
                if c.state == "AVAILABLE" and t - c.t_post >= a.withdraw_after:
                    w.withdraw_unawarded(cid)
                    self.c["withdrawn_unawarded"] += 1
                    self.active.pop(cid, None)
        # Q2: what a free tell-reader sees of the market before this tick's awards — the roots available, when first seen, at what
        # ceiling, against the index then (the seen set; the idage, post and price tells read it)
        if self.readers:
            free_readers = [aid for aid in self.free_members() if aid in self.readers]
            if free_readers:
                P_now = w.market()["P_t"]
                for cid in self.active:
                    if cid in self.nested_parent:
                        continue
                    cc = w.case(cid)
                    if cc.state == "AVAILABLE":
                        for aid in free_readers:
                            if (aid, cid) not in self.seen:
                                self.seen[(aid, cid)] = (w.t, cc.beta, P_now)
        self.learner_bid_step(t)                         # Q6: the learned bidder's rule for this tick's offers
        # orchestrator awards
        for cid in list(self.active):
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
                for aid_b, bid_b in bids:
                    if aid_b in self.readers:
                        self.my_bid[(aid_b, cid)] = bid_b    # Q2's readers: what the reader bid, to read a lost bid later
                w.award(cid, actor, bid, tau)
                if w.case(cid).actor != actor:
                    # 2.6.0 §2.1: the award was the market's report on a plant — the plant actor took it; the member's bid is lost
                    self.c["plant_bids_lost"] += 1
                    for aid_b, _ in bids:
                        if aid_b in self.readers:
                            self.lost_bid[(aid_b, cid)] = w.t
                    continue
                for aid_b, _ in bids:
                    if aid_b in self.readers and aid_b != actor:
                        self.lost_bid[(aid_b, cid)] = w.t
                    if aid_b != actor and self.kind.get(aid_b) == LEARNER and self.learner_role_of.get(aid_b) == "bidder":
                        self.c["learner_bids_lost"] += 1
                        self.bids_lost_of[aid_b] = self.bids_lost_of.get(aid_b, 0) + 1
                if self.kind.get(actor) == LEARNER and self.learner_role_of.get(actor) == "bidder":
                    self.learner_last_bid_case = (w.t, cid)        # Q6: the case this tick's bid decision won (redteam.env credits it to the decision; the world's clock, as the hook's)
                    self.learner_won.append((w.t, actor, cid))     # the population: by name too
                    self.bid_awards_of[actor] = self.bid_awards_of.get(actor, 0) + 1; self.last_won_of[actor] = w.t
                    self.c["learner_bid_awards"] += 1; self.c["learner_bid_award_sum"] += bid; self.c["learner_bid_cost_sum"] += self.cost_now(actor)
                self.parent_awards[actor] = self.parent_awards.get(actor, 0) + 1
                self.margin[actor] = round(self.margin[actor] + a.margin_up, 6)
                self.idle[actor] = 0
                self.tally[actor].awards += 1
                self.c["awarded"] += 1
                self.c["member_price_sum"] += bid
                self.c["member_price_n"] += 1
                # the stability track's readings: the undercutters' awards (and those at their cost — the cut floored), the awards at or under the state's
                # reservation and the member's margin on them (does the reservation bind from below?), the under-floor requests' awards and wait
                cost_a = self.cost_now(actor)
                if actor in self.undercutters:
                    self.c["undercut_awards"] += 1
                    if bid <= cost_a + 1e-9:
                        self.c["undercut_awards_at_cost"] += 1
                fl = self.market_now().get("state_floor", 0.0) or 0.0
                if fl > 0 and bid < fl - 1e-9:
                    self.c["awards_below_floor"] += 1
                    self.c["below_floor_margin_sum"] = round(self.c["below_floor_margin_sum"] + bid - cost_a, 6)
                    self.below_floor_cases[cid] = actor
                    self.below_floor_servers.add(actor)
                elif fl > 0 and bid <= fl + 1e-9:
                    self.c["awards_at_floor"] += 1
                if cid in self.under_floor_cases:
                    self.c["under_floor_awarded"] += 1
                    self.c["under_floor_wait_sum"] += w.t - w.case(cid).t_post
                    self.c["under_floor_price_sum"] = round(self.c["under_floor_price_sum"] + bid, 6)
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
                if a.parent_cancel == "on" and child.state == "COMMITTED" and t >= c.deadline - a.work_ticks:
                    # 2.4.0 §2.4: the child has not submitted and the parent's deadline leaves just room to self-execute — cancel, pay
                    # the kill fee (the child's recorded cost; zero for a child that never worked), do the work itself
                    try:
                        before = w.case(cid).actor_cost
                        w.cancel_nested(nid)
                        fee = w.case(cid).actor_cost - before
                        self.c["parent_cancellations"] += 1
                        self.c["kill_fees_paid"] = round(self.c["kill_fees_paid"] + fee, 6)
                        if fee > 1e-9:
                            self.c["kill_fees_nonzero"] += 1
                        self.c["cancel_delay_sum"] += t - child.t_award
                        child = w.case(nid)
                    except (RuleError, LedgerError):
                        self.c["parent_cancel_refused"] += 1
                if child.t_verdict is None and child.state not in ("WITHDRAWN", "CANCELLED", "FINAL_N"):
                    continue                             # §9.1: the parent submits after its child's milestone
                self.parent_waiting.pop(cid, None)
                if child.state == "FINAL_N" and child.t_verdict is None and not self.tasks[nid].nested_missed_counted:
                    self.tasks[nid].nested_missed_counted = True
                    self.c["nested_lapsed"] += 1         # 2.5.0: the lapse — a missed delivery, the guarantee to the parent
                    self.c["nested_lapsed_forfeit"] = round(self.c["nested_lapsed_forfeit"] + child.G, 6)
                if child.verdict == N or child.state in ("WITHDRAWN", "CANCELLED", "FINAL_N"):
                    self.parent_self_exec.add(cid)       # the child failed: the parent does the work itself
            if c.state == "COMMITTED" and cid in self.nested_parent and c.actor in self.lowball_children:
                if t >= c.deadline and not self.tasks[cid].nested_missed:
                    self.tasks[cid].nested_missed = True
                    self.c["lowball_child_misses"] += 1
                    if a.lowball_mode == "empty":
                        # 2.5.0 §8.5 red team: an empty result on the last tick, to avoid the lapse; the parent judges it (§9.1)
                        self.tasks[cid].fulfilled = False
                        try:
                            w.submit(cid)
                            self.c["lowball_empty_submitted"] += 1
                        except (RuleError, LedgerError):
                            pass
                continue                                 # §8.7 red team: the lowball child never delivers — it misses (or submits empty)
            if c.state == "COMMITTED" and self.tasks[cid].plant and self.rev12:
                # 2.6.0 §7.6 (the Q2 probe's correction): the orchestrator's instrument submits for the plant actor at its drawn tick, in
                # this step — the same step a member's submission takes — so the plant reaches its seat with a real case's gap
                if c.plant_submit_at is not None and w.t >= c.plant_submit_at:
                    w.submit_plant(cid)
                continue
            if c.state == "COMMITTED" and self.tasks[cid].learner_miss:
                continue                                 # Q5: the learned child chose to miss — the deadline lapses (2.5.0: final N, the guarantee to the parent)
            if c.state == "COMMITTED" and t >= c.t_award + min(a.work_ticks, c.tau) and cid not in self.parent_waiting:
                if self.floating and not w.is_troop(c.actor):
                    # 2.0.0 §2.2: the actor's effort, burned at submission (§4.6) — what its unlocked credit can pay of it
                    # 2.3.0: the actor's own cost; a parent that delegated and was served pays its care, not the work
                    delegated = c.is_root and c.children and cid not in self.parent_self_exec
                    work = None
                    role_a = self.learner_role_of.get(c.actor)
                    if self.kind.get(c.actor) == LEARNER and self.learner_work is not None and (role_a == "deliverer" or (role_a == "child" and not c.is_root)):
                        # Q3 — the quality dial (the brief §3: the deliverer's failure is a choice, not a rate): 0 deliver well — the work fulfilled, the
                        # effort burned; 1 deliver badly — unfulfilled, nothing burned (the zero-effort delivery). The truth is set here, never shown
                        work = int(self.learner_work(self, c.actor, c))
                        self.c["learner_work_decisions"] += 1
                        self.tasks[cid].learner_work = work
                        if work == 2:                                    # Q5: miss — never submit; the lapse at the deadline
                            self.tasks[cid].learner_miss = True
                            self.c["learner_misses"] += 1
                            continue
                        if work == 1:
                            self.tasks[cid].fulfilled = False
                        elif a.good_delivery == "certain":
                            self.tasks[cid].fulfilled = True        # Q3's reading; from Q4 on a good delivery takes the task's own draw (the ruling after run 27)
                        self.c["learner_bad_deliveries" if work == 1 else "learner_good_deliveries"] += 1
                        if work == 1:
                            self.c["learner_effort_saved"] = round(self.c["learner_effort_saved"] + self.cost_now(c.actor), 6)
                    want = 0.0 if (delegated or work == 1) else self.cost_now(c.actor)
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
                    task = self.tasks[cid]
                    if r.role == "initial" and task.t_seated is None and cid not in self.nested_parent and c.t_award is not None and c.t_submit is not None:
                        # the plant's life by stage (the ruling after run 34): the root's first initial seat, by case kind
                        task.t_seated = r.t_assign
                        sn = self.seen.get((r.reviewer, cid))
                        task.seated_seen = sn is not None
                        k = "plant" if task.plant else "real"
                        self.c[f"life_{k}_n"] += 1
                        self.c[f"life_{k}_post_award"] += c.t_award - c.t_post
                        self.c[f"life_{k}_award_submit"] += c.t_submit - c.t_award
                        self.c[f"life_{k}_submit_seat"] += r.t_assign - c.t_submit
                        self.c[f"life_{k}_raised"] += int(task.raised_n > 0)
                        self.c[f"life_{k}_raise_refused"] += int(task.raise_refused_n > 0)   # §52: a raise refused (a real root's by the wallet; a plant's drawn at their rate from run 35)
                        task.life_period = len(w.dial()["periods"])
                        pb = self.life_by_period.setdefault(task.life_period, {}).setdefault(k, {"n": 0, "post_award": 0, "award_submit": 0, "submit_seat": 0, "raised": 0, "raise_refused": 0, "seen": 0, "seen_ticks": 0})
                        pb["n"] += 1; pb["post_award"] += c.t_award - c.t_post; pb["award_submit"] += c.t_submit - c.t_award; pb["submit_seat"] += r.t_assign - c.t_submit
                        pb["raised"] += int(task.raised_n > 0); pb["raise_refused"] += int(task.raise_refused_n > 0)
                        if sn is not None:
                            pb["seen"] += 1; pb["seen_ticks"] += r.t_assign - sn[0]
                        if task.plant:
                            self.c["life_plant_floor"] += int(bool(c.plant_at_floor))
                        else:
                            self.c["life_real_troop"] += int(bool(c.troop_award))
                        if sn is not None:
                            task.seated_seen_ticks = r.t_assign - sn[0]
                            self.c[f"life_{k}_seen"] += 1
                            self.c[f"life_{k}_seen_ticks"] += task.seated_seen_ticks
                    v, cost = self.verdict(r.reviewer, self.tasks[cid].fulfilled, view=view, r=r)
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
            if c.state not in ("AWAITING_RESPONSE", "RESUBMITTING"):
                continue
            task = self.tasks[cid]
            if task.plant:
                if self.rev14:
                    self.plant_respond(cid, c, task, t)   # 2.8.0: the instrument answers for the plant actor at the real rates
                continue
            if c.state != "AWAITING_RESPONSE":
                continue
            if task.fulfilled:
                self.c["false_rejections_total"] += 1
            want = a.appeal_policy == "always" or (a.appeal_policy == "truthful" and task.fulfilled)
            if not c.is_root and a.delegation == "on" and task.fulfilled and a.child_appeal == "truthful":
                want = True                              # 2.3.0 §2.4: a child rejected appeals truthfully (declared)
            if not c.is_root and a.child_appeal == "none" and want:
                want = False                             # Q5's calibration knob: children never appeal
                self.c["child_appeals_suppressed"] += 1
            if not c.is_root and c.actor in self.lowball_children and a.lowball_mode == "empty":
                want = True                              # 2.5.0 §8.5 red team: the lowballer appeals its empty result against the parent's bond
                self.c["lowball_appeals"] += 1
            if want and w.unlocked(c.actor) + 1e-9 < c.D:
                self.c["appeals_unfunded"] += 1
                want = False
            if c.is_root and task.fulfilled:
                # 2.8.0: the real actors' appeal window (a false rejection filed or not; the delay from the verdict) — what the plant actor draws
                per = len(w.dial()["periods"])
                self.appeal_window.append((per, int(bool(want))))
                if want and c.t_verdict is not None:
                    self.appeal_delay_window.append((per, w.t - c.t_verdict))
            if want:
                w.respond(cid, "appeal", "the work meets the request")
                task.appealed, task.t_filed = True, w.t
                self.c["appeals_filed"] += 1
                self.c["false_rejections_appealed" if task.fulfilled else "true_rejections_appealed"] += 1
            else:
                w.respond(cid, "accept")
        # 2.4.0 §8 (run 18 §7.4): `--parent-cancel early` — after this tick's submissions, a parent cancels a child that reached its
        # deadline without submitting (an honest child submits at its deadline, in the loop above; a lowballer never does; the engine
        # would finalize it N at this tick's end) and self-executes with its own deadline still ahead
        if self.learner_parent is not None:
            # Q5: the learned parent's cancel decision — asked each tick its child is committed and has not submitted, while the engine admits it
            for cid, nid in list(self.parent_waiting.items()):
                root = w.case(cid)
                if self.kind.get(root.actor) != LEARNER or self.learner_role_of.get(root.actor) != "parent":
                    continue
                child = w.case(nid)
                if child.state != "COMMITTED" or child.deadline is None or w.t >= child.deadline:
                    continue
                act = int(self.learner_parent(self, root.actor, "cancel", root, child))
                self.c["learner_cancel_decisions"] += 1
                if act != 1:
                    continue
                try:
                    before = root.actor_cost
                    w.cancel_nested(nid)
                    fee = w.case(cid).actor_cost - before
                    self.c["learner_cancels"] += 1
                    self.c["learner_kill_fees"] = round(self.c["learner_kill_fees"] + fee, 6)
                    self.c["parent_cancellations"] += 1
                    self.c["kill_fees_paid"] = round(self.c["kill_fees_paid"] + fee, 6)
                    self.parent_waiting.pop(cid, None)
                    self.parent_self_exec.add(cid)
                except (RuleError, LedgerError):
                    self.c["learner_cancel_refused"] += 1
        if a.parent_cancel in ("early", "eve"):
            for cid, nid in list(self.parent_waiting.items()):
                child = w.case(nid)
                # the world's clock runs a tick behind the driver's: at driver tick t the world is at t − 1. `eve` cancels when the world is at
                # deadline − 1 (driver t = deadline); `early` when the world is at the deadline itself (driver t = deadline + 1)
                if child.state != "COMMITTED" or child.deadline is None:
                    continue
                when = child.deadline if a.parent_cancel == "eve" else child.deadline + 1
                if t < when:
                    continue
                try:
                    before = w.case(cid).actor_cost
                    w.cancel_nested(nid)
                    fee = w.case(cid).actor_cost - before
                    self.c["parent_cancellations"] += 1
                    self.c["kill_fees_paid"] = round(self.c["kill_fees_paid"] + fee, 6)
                    if fee > 1e-9:
                        self.c["kill_fees_nonzero"] += 1
                    self.c["cancel_delay_sum"] += t - child.t_award
                    self.parent_waiting.pop(cid, None)
                    self.parent_self_exec.add(cid)
                except (RuleError, LedgerError):
                    self.c["parent_cancel_refused"] += 1
                    self.c["cancel_refused_at_deadline"] += 1    # 2.5.0 §9.3: nothing to cancel at the deadline; the lapse runs
        # orchestrator: the plants the rate calls for (1.2.0 §2.1). Under 2.5.0 and before, a plant is created submitted here — before
        # this tick's assignments, so it joins the queue behind the real work submitted so far. Under 2.6.0 the plant is a root in the
        # market and is posted in the requesters' posting step instead (`plant_step`, run 24's conformance correction): posted here, after
        # the award pass, it waited a tick more than every real root by construction, submitted a tick older, and the oldest-first seating
        # gave it the seat first when seats were short — the gap the Q2 probe read.
        if not self.rev12:
            self.plant_step(t)
        # orchestrator: initial reviews, audits, appeal reviews, rulings
        for cid in list(self.active):
            c = w.case(cid)
            task = self.tasks[cid]
            if c.state == "SUBMITTED" and not c.is_root:
                continue                                     # 2.3.0 §2.4: the parent judges its child (delegation_step)
            if c.state == "SUBMITTED" and not any(w.review(r).status == "open" for r in c.reviews):
                el = self.eligible_reviewers(cid)
                if el:
                    pick = self.pick_reviewer(el)
                    if self.learner_pair and c.actor == self.learner_pair[0]:
                        # Q4: the pair's deliverer's case — matched to the pair's reviewer in the calibration (--match-pair on), blind in the line
                        if a.match_pair == "on" and self.learner_pair[1] in el:
                            pick = self.learner_pair[1]
                            self.c["pair_matched"] += 1
                        elif a.match_pair == "on" and self.learner_pair[1] in self.actors and w.actor(self.learner_pair[1]).on_duty \
                                and w.actor(self.learner_pair[1]).open_review is not None:
                            self.c["pair_waited"] += 1           # the reviewer holds another review this tick: the case waits for it (always matched)
                            continue
                        elif a.match_pair == "on":
                            self.c["pair_unmatched"] += 1        # the reviewer is off duty, suspended or gone: the round-robin takes the case
                        if pick == self.learner_pair[1]:
                            task.pair_review = True
                            self.c["pair_reviews"] += 1
                    rid = w.assign_initial(cid, pick)
                    self.review_owner[rid] = w.review(rid).reviewer
                    self.c["seated_initial_probationer" if w.actor(w.review(rid).reviewer).probation else "seated_initial_member"] += 1
                    if task.plant:
                        self.c["seated_plant"] += 1
                else:
                    self.c["reviews_unassignable_ticks"] += 1
            if task.plant and not self.rev14:
                continue                                     # 1.2.0: no audit roll, no dispute: adjudicated by truth at the first review
            if task.plant and c.state == "PENDING" and c.verdict == F and c.challenge is None and not task.dispute_rolled:
                # 2.8.0 §2.1: the plant requester disputes a bad plant's pending F at the trailing real requesters' dispute rate on unfulfilled
                # work approved (zero where the population does not dispute), after their delay; never a good plant's F
                per = len(w.dial()["periods"])
                if task.plant_file_at is None:
                    rate = self._win_rate(self.dispute_window, per) if a.dispute_policy != "none" else 0.0
                    task.plant_file_at = (w.t + int(self._win_draw(self.dispute_delay_window, per, 0))) \
                        if (not task.fulfilled and rate > 0 and self.plant_rng.random() < rate) else -1
                if task.plant_file_at >= 0 and w.t < task.plant_file_at:
                    continue                                 # held for the drawn delay; the roll waits as it does for a real requester acting first
                task.dispute_rolled = True
                if task.plant_file_at >= 0:
                    try:
                        w.dispute(cid, c.requester, "the result does not meet the request")
                        task.disputed, task.t_filed = True, w.t
                        task.audit_wanted = False
                        self.c["plant_disputes_filed"] += 1
                    except (RuleError, LedgerError):
                        self.c["disputes_refused"] += 1
                c = w.case(cid)
            elif c.state == "PENDING" and c.verdict == F and c.challenge is None and not task.dispute_rolled \
                    and a.dispute_policy != "none":
                task.dispute_rolled = True             # the requester acts once, before the audit roll
                pol = a.dispute_policy
                rate = 0.5 if pol == "half" else a.dispute_rate
                want = pol == "always" or (not task.fulfilled and pol in ("truthful", "half")
                                           and (rate >= 1.0 or self.rng.random() < rate))
                if c.is_root and not task.fulfilled:
                    per = len(w.dial()["periods"])           # 2.8.0: the real requesters' dispute window — what the plant requester draws
                    self.dispute_window.append((per, int(bool(want))))
                    if want and c.t_verdict is not None:
                        self.dispute_delay_window.append((per, w.t - c.t_verdict))
                if want:
                    try:
                        w.dispute(cid, self.owner.get(cid, "H"), "the result does not meet the request")
                        task.disputed, task.t_filed = True, w.t
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
                    roll = self.rng.random()                 # drawn in every mode, so the stream is the same cell to cell
                    if self.a.audit_roll == "on" and roll < w.audit_odds(cid):
                        w.roll_audit(cid)
                        task.audit_wanted, task.t_roll = True, w.t
                        self.c["audit_obligations"] += 1
                elif c.market_audit_only and not task.audit_rolled:
                    task.audit_rolled, task.audit_wanted = True, True      # the engine recorded this one at the verdict
                if task.audit_wanted and (c.audit_obligation or c.audit_vacated):
                    el = self.eligible_reviewers(cid, panel=True)
                    if el:
                        rid = w.assign_audit(cid, self.pick_reviewer(el))
                        self.c["seated_audit_member"] += 1
                        self.review_owner[rid] = w.review(rid).reviewer
                        task.audit_wanted, task.t_audit_assign = False, w.t
                        self.c["audits_assigned"] += 1
                    else:
                        self.c["audit_unassignable_ticks"] += 1
                elif task.audit_wanted:
                    task.audit_wanted = False                             # a troop took the seat
            ch = c.challenge
            if ch and not ch["resolved"]:
                if not task.appeal_wanted:
                    task.appeal_wanted = True
                    self.c["plant_challenges" if task.plant else "challenges"] += 1
                done = [w.review(r) for r in ch["reviews"] if w.review(r).status == "done"]
                if len(ch["reviews"]) + len(ch.get("state_verdicts", ())) < 2:     # 2.8.0: the state's verdict on a plant holds a seat
                    el = self.eligible_reviewers(cid, panel=True)
                    if el:
                        rid = w.assign_appeal(cid, self.pick_reviewer(el))
                        self.c["seated_appeal_member"] += 1
                        self.review_owner[rid] = w.review(rid).reviewer
                        if task.t_panel_assign is None:
                            task.t_panel_assign = w.t
                    else:
                        self.c["appeals_unassignable_ticks"] += 1
                elif not task.plant and len(done) == 2 and done[0].verdict != done[1].verdict:
                    truth = F if task.fulfilled else N
                    by_truth = self.rng.random() < a.ruling_accuracy
                    outcome = truth if by_truth else (N if truth == F else F)
                    w.rule(cid, outcome)
                    self.c["rulings"] += 1
                    if not by_truth:
                        self.c["rulings_wrong"] += 1
        self.c["duty_short_of_bond_ticks"] += self.duty_funding()
        if self.rev11:                                    # 2.7.0 H2's two readings: the probationer's liquidity, the repaying member's fundability
            real_bond = self.a.gv * w.market()["P_t"] / self.p.P0
            for aid in self.arrived:
                if aid not in self.actors:
                    continue
                ac = w.actor(aid)
                if ac.admitted_at is None and w.unlocked(aid) + 1e-9 < real_bond:
                    self.below_bond_names.add(aid)
                if ac.is_member and not ac.on_duty and ac.committed is None and ac.open_review is None and w.loan_outstanding(aid) > 1e-9 \
                        and w.unlocked(aid) + 1e-9 < max(1.0, -(-self.p.G_frac * self.a.beta // 1)):
                    self.c["unfundable_with_loan_ticks"] += 1
        # the standing reading in every cell (the ruling after the v2 calibration): members idle for want of a bond — a free member whose unlocked
        # balance is below G^V at the index can take no seat (and no award); member-ticks and names. The member's bond loan is the named candidate
        # if it ever reads outside noise in a real cell — not drafted.
        bond_now = self.a.gv * (w.market().get("P_t") or self.p.P0) / self.p.P0
        for aid in self.actors:
            ac = w.actor(aid)
            if ac.is_member and ac.committed is None and ac.open_review is None and w.unlocked(aid) + 1e-9 < bond_now:
                self.c["idle_for_bond_ticks"] += 1
                self.idle_for_bond_names.add(aid)
        self.cycler_step(t)
        self.inspection_diagnostics(t)
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
        events = w.events_since(self.n_events)
        if self.learner_id and self.a.learner_role == "requester":
            self.req_read_events(events)                 # Q7: the learned requester's spend, by its own events at the index of each
        self.pop_read_events(events)                     # every requester's spend, nominal (the customers' tasks per credit)
        for e in events:
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
                # a plant leaves the queue once adjudicated and closed; its outcome is the reviewer's (2.8.0: every seat's reviewer's)
                if c.plant_outcome is not None and c.tree_closed:
                    initial = [w.review(x) for x in c.reviews if w.review(x).role == "initial"]
                    r = initial[0] if initial else (w.review(c.reviews[-1]) if c.reviews else None)
                    if c.t_verdict is not None:
                        self.c["plant_lag_sum"] += c.t_verdict - c.t_post    # 2.6.0: from the posting to the verdict
                        self.c["plant_lag_n"] += 1
                    if c.plant_outcome == "spent":
                        self.c["plants_spent"] += 1
                    elif c.plant_outcome == "state":
                        self.c["plants_state_initial"] += 1                  # 2.8.0 (C): the initial seat taken by the orchestrator's verdict
                    elif self.rev14:
                        # 2.8.0: the initial seat's adjudication keeps the honesty readings' meaning (the dial's clock); every seat's is tallied by kind
                        if c.plant_outcome == "failure":
                            self.c["plants_failed"] += 1
                            self.c["bad_plants_approved" if c.plant is False else "good_plants_rejected"] += 1   # the truth sealed at posting (the initial seat's)
                        else:
                            self.c["plants_stood"] += 1
                        for (_t, rid, kind, _v, outcome) in c.plant_adjudications:
                            if outcome not in ("stood", "failure"):
                                continue
                            rv = w.review(rid)
                            self.tally[rv.reviewer].plant_reviews += 1
                            self.c[f"plant_seats_{kind}"] += 1
                            if outcome == "failure":
                                self.tally[rv.reviewer].plant_failures += 1
                                self.c[f"plant_seat_failures_{kind}"] += 1
                        self.c["plant_seats_state"] += len(c.plant_state_seats)
                        self._life_close(c, task)
                    else:
                        self.tally[r.reviewer].plant_reviews += 1
                        if c.plant_outcome == "failure":
                            self.tally[r.reviewer].plant_failures += 1
                            self.c["plants_failed"] += 1
                            self.c["bad_plants_approved" if task.fulfilled is False else "good_plants_rejected"] += 1
                        else:
                            self.c["plants_stood"] += 1
                        self._life_close(c, task)
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
                if c.is_root:
                    self._life_close(c, task)                # 2.8.0: the real root's stages after its first verdict, by kind (read under every rule)
                if cid in self.req_mode and cid not in self.req_counted:    # Q7: what became of the learned requester's request
                    self.req_counted.add(cid)
                    if task.fulfilled:                                      # a task received: the delivery's truth, whatever the verdict (the requester holds the result)
                        self.c["req_tasks_received"] += 1
                        self.req_received_cases.append(cid)
                        if c.state == "FINAL_N":
                            self.c["req_free_fulfilled"] += 1
                    elif c.state == "VESTED":
                        self.c["req_paid_unfulfilled"] += 1
                    if c.state == "FINAL_N":
                        self.c["req_final_n"] += 1
                    if c.t_award is not None:
                        self.c["req_awards"] += 1
                        self.c["req_wait_sum"] += c.t_award - c.t_post
                        self.c["req_price_paid_sum"] = round(self.c["req_price_paid_sum"] + float(c.B or 0.0), 6)
                    if c.actor is not None and w.is_troop(c.actor):
                        self.c["req_state_deliveries"] += 1
                    if task.disputed:
                        self.c["req_disputes_filed"] += 1
                        self.c["req_disputes_won"] += int(c.state == "FINAL_N")
                if self.owner.get(cid) in self.requesters_set and cid not in self.pop_counted:   # the customers' tasks per credit (the ruling after run 32): a task received by any requester
                    self.pop_counted.add(cid)
                    if task.fulfilled:
                        self.c["pop_tasks_received"] += 1
                if cid in self.below_floor_cases and cid not in self.bf_counted:   # the stability track: what a delivery under the floor cost its member
                    self.bf_counted.add(cid)
                    if c.state == "FINAL_N":
                        self.c["below_floor_final_n"] += 1
                        self.c["below_floor_g_lost"] = round(self.c["below_floor_g_lost"] + float((c.G_award if c.G_award is not None else c.G) or 0.0), 6)
                if cid in self.under_floor_cases and cid not in self.uf_counted:
                    self.uf_counted.add(cid)
                    self.c["under_floor_fulfilled"] += int(bool(task.fulfilled))
                    self.c["under_floor_final_n" if c.state == "FINAL_N" else "under_floor_vested"] += 1
                if task.parent_learner:                                 # Q5: what became of the learned parent's child
                    self.c["learner_children_settled"] += 1
                    if c.state == "FINAL_N":
                        self.c["learner_guarantees_taken"] = round(self.c["learner_guarantees_taken"] + (c.G_award if c.G_award is not None else c.G), 6)
                        if c.t_submit is None:
                            self.c["learner_child_lapses"] += 1
                    elif task.parent_rejected_blind:
                        self.c["learner_rejections_overturned"] += 1    # the child appealed and won: the parent's rejection bond forfeited
                if task.pair_stamped and task.learner_work == 1:        # Q4: the deliverer's bad work the pair's reviewer approved blind
                    self.c["pair_bad_stamped_vested" if c.state == "VESTED" else "pair_bad_stamped_caught"] += 1
                if task.learner_work is not None:                      # Q3: what became of the learned deliverer's choice
                    if c.state == "VESTED":
                        self.c["learner_bad_approved" if task.learner_work == 1 else "learner_good_vested"] += 1
                        if task.learner_work == 1:
                            self.c["learner_bad_paid"] = round(self.c["learner_bad_paid"] + c.B, 6)
                    elif task.learner_work == 2:
                        self.c["learner_miss_lapsed"] += 1
                        self.c["learner_forfeited"] = round(self.c["learner_forfeited"] + (c.G_award if c.G_award is not None else c.G), 6)
                    else:
                        self.c["learner_bad_caught" if task.learner_work == 1 else "learner_good_final_n"] += 1
                        self.c["learner_forfeited"] = round(self.c["learner_forfeited"] + (c.G_award if c.G_award is not None else c.G), 6)
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
                revs_c = [w.review(rid) for rid in c.reviews]
                if any(x.role == "audit" for x in revs_c):                   # the audit layer's overturn rate (the ruling after run 33's honesty readings)
                    self.c["audits_held"] += 1
                    if any(x.role == "initial" and x.status == "overturned" for x in revs_c):
                        self.c["audits_overturning"] += 1
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
        bank27 = w.bank()                               # 2.7.0: the bank's names line
        row = {"t": t, "head": w.head()}
        for kind in (CAREFUL, STAMPER) + ((TELL,) if self.tell_readers else ()) + ((LEARNER,) if self.learner_id else ()):
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
        dl = w.dial()
        real = mk["P0"] / mk["P_t"] if mk["P_t"] > 0 else 1.0
        reqs = [r for r in self.requesters]
        row.update({"P_t": round(mk["P_t"], 4), "price_index": round(mk["index"], 4), "credit_value": round(mk["v"], 4),
                    "deficit": round(mk["deficit"], 3), "deficit_created": round(mk["created"], 3), "deficit_retired": round(mk["retired"], 3),
                    "deficit_peak": round(mk["deficit_peak"], 3), "deficit_age": (t - mk["deficit_since"]) if mk["deficit_since"] is not None else 0,
                    "omega_net_position": round(mk["omega_net"], 3), "issued": round(mk["issued"], 3), "departed": round(mk["departed"], 3),
                    "below_market_flagged": mk["below_market_flagged"], "below_market_waiting": mk["below_market_waiting"],
                    "ceilings_raised": mk["ceilings_raised"], "places_held": mk["places_held"],
                    # 2.4.0: the state's reservation — the floor, the state's price beside B̄ and P_t, the marks and the ticks below, the declines
                    "state_floor": mk["state_floor"], "state_price": round(mk["state_price"], 4),
                    "state_price_mean": round(tr["state_price_mean"], 4) if tr.get("state_price_mean") is not None else "",
                    "state_price_period": round(tr["state_price_period"], 4) if tr.get("state_price_period") is not None else "",
                    "below_reservation_marked": mk["below_reservation_marked"], "below_reservation_waiting": mk["below_reservation_waiting"],
                    "below_reservation_ticks": mk["below_reservation_ticks"], "summons_declined_floor": mk["summons_declined_floor"],
                    "parent_cancellations": self.c["parent_cancellations"], "kill_fees_paid": self.c["kill_fees_paid"],
                    "kill_fees_nonzero": self.c["kill_fees_nonzero"],
                    "cancel_delay_mean": round(self.c["cancel_delay_sum"] / self.c["parent_cancellations"], 3) if self.c["parent_cancellations"] else "",
                    "parent_cancel_refused": self.c["parent_cancel_refused"],
                    # 2.5.0: the refusal, the lapses, the lowball children's wealth, the red team
                    "cancel_refused_at_deadline": self.c["cancel_refused_at_deadline"], "nested_lapsed": self.c["nested_lapsed"],
                    "nested_lapsed_forfeit": self.c["nested_lapsed_forfeit"], "nested_declined_deadline": self.c["nested_declined_deadline"],
                    "lowball_children_n": sum(1 for x in self.actors if x in self.lowball_children),
                    "lowball_children_wealth_real": round(sum(w.wealth(x) for x in self.actors if x in self.lowball_children) / max(1, sum(1 for x in self.actors if x in self.lowball_children)) * real, 3) if self.lowball_children else "",
                    "lowball_empty_submitted": self.c["lowball_empty_submitted"], "lowball_empty_rejected": self.c["lowball_empty_rejected"],
                    "lowball_empty_approved": self.c["lowball_empty_approved"], "lowball_appeals": self.c["lowball_appeals"],
                    "farmers_n": len(self.farmers),
                    # 2.6.0: the plant's life — posted, awarded (at the floor), the bids lost to plants, the time in the market, the lag
                    "plants_raised": dl.get("plants_raised", 0),
                    # the conformance correction after run 35: the plants whose raise was drawn refused, their drawn delay, and the window's rate at the end
                    "plant_raises_refused": self.c["plant_raises_refused"],
                    "plant_raise_delay_mean": round(self.c["plant_raise_delay_sum"] / self.c["plant_raises_refused"], 3) if self.c["plant_raises_refused"] else "",
                    "raise_refusal_rate_window": round(self._raise_refusal_rate(len(w.dial()["periods"])), 4),
                    "plants_posted": dl["plants_posted"], "plants_awarded": dl["plants_awarded"], "plants_at_floor": dl["plants_at_floor"],
                    "plant_bids_lost": dl["plant_bids_lost"],
                    "plant_time_in_market_mean": round(dl["plant_market_ticks"] / dl["plants_awarded"], 3) if dl["plants_awarded"] else "",
                    "plant_lag_mean": round(self.c["plant_lag_sum"] / self.c["plant_lag_n"], 3) if self.c["plant_lag_n"] else "",
                    "plant_names": dl["plant_names"], "available_roots": mk["available_roots"],
                    "plants_refused_capacity": dl["plants_refused_capacity"], "plants_refused_credit": dl["plants_refused_credit"],
                    # 2.8.0: the plant at every seat — the seats on plants by kind (the engine's count, stood + failure) and the failures among
                    # them, the state's seats on plants, the revisions and the spends, the bank's top-ups and the court fees destroyed, the
                    # instrument's filings for the plant actor and the plant requester
                    **{f"plant_adj_{k}": (v["stood"] + v["failure"]) for k, v in dl.get("plant_seat_adjudications", {}).items()},
                    **{f"plant_fail_{k}": v["failure"] for k, v in dl.get("plant_seat_adjudications", {}).items()},
                    "plant_seats_at_state": dl.get("plant_seats_at_state", 0), "plants_revised": dl.get("plants_revised", 0),
                    "plants_spent_engine": dl.get("plants_spent", 0), "plant_top_ups": round(dl.get("plant_top_ups", 0.0), 3),
                    "plant_fees_destroyed": round(dl.get("plant_fees_destroyed", 0.0), 3),
                    "plant_appeals_filed": self.c["plant_appeals_filed"], "plant_disputes_filed": self.c["plant_disputes_filed"],
                    "plant_challenges": self.c["plant_challenges"], "plant_revisions": self.c["plant_revisions"],
                    "plant_spent_by_instrument": self.c["plant_spent_by_instrument"], "plants_state_initial": self.c["plants_state_initial"],
                    "plant_share_of_reviews": round(sum(v["stood"] + v["failure"] for v in dl.get("plant_seat_adjudications", {}).values())
                                                    / max(1, sum(x.reviews for x in self.tally.values())), 4),
                    # Q2 (the learned red team, hand-written first): the tell-reader's confusion table, its stamps caught and its standing
                    "tell_n": sum(1 for x in self.tell_readers if x in self.actors), "tell_set": "+".join(sorted(self.tells)) if self.tell_readers else "",
                    "tell_departed": sum(1 for x in self.tell_readers if x not in self.actors),
                    "tell_wealth_real_lifetime": round(sum((w.wealth(x) * real) if x in self.actors else self.depart_wealth_real.get(x, 0.0) for x in self.tell_readers) / max(1, len(self.tell_readers)), 3) if self.tell_readers else "",
                    "careful_wealth_real_lifetime": round(sum((w.wealth(x) * real) if x in self.actors else self.depart_wealth_real.get(x, 0.0) for x in self.careful_initial) / max(1, len(self.careful_initial)), 3),
                    "careful_initial_departed": sum(1 for x in self.careful_initial if x not in self.actors),
                    "slot_id": self.tell_slot or "",
                    "slot_kind": (self.kind.get(self.tell_slot, "") if self.tell_slot else ""),
                    "slot_wealth_real_lifetime": (round((w.wealth(self.tell_slot) * real) if self.tell_slot in self.actors else self.depart_wealth_real.get(self.tell_slot, 0.0), 3) if self.tell_slot else ""),
                    "slot_departed": (int(self.tell_slot not in self.actors) if self.tell_slot else ""),
                    "slot_awards": (self.tally[self.tell_slot].awards if self.tell_slot else ""),
                    "slot_reviews": (self.tally[self.tell_slot].reviews if self.tell_slot else ""),
                    "slot_rho": (round(w.actor(self.tell_slot).rho, 4) if self.tell_slot and self.tell_slot in self.actors else ""),
                    "slot_cost": (round(self.c_d_of[self.tell_slot], 3) if self.tell_slot else ""),
                    "slot_suspensions": (len(self.susp_log.get(self.tell_slot, [])) if self.tell_slot else ""),
                    "learner_decisions": self.learner_decisions, "learner_false_approvals": self.c["learner_false_approvals"],
                    # Q3: the learned deliverer's line — its quality decisions, what became of them, the guarantees it forfeited, the effort it saved
                    "learner_role": (("pair" if self.learner_pair else self.a.learner_role) if self.learner_id else ""), "learner_work_decisions": self.c["learner_work_decisions"],
                    # Q6: the learned bidder — its decisions by kind, the awards its bids won and the bid over cost at them, the offers lost, the wealth held (real, a tick)
                    "learner_bid_decisions": self.c["learner_bid_decisions"], "learner_bid_ratchet": self.c["learner_bid_ratchet"], "learner_bid_undercut": self.c["learner_bid_undercut"],
                    "learner_bid_withheld": self.c["learner_bid_withheld"], "learner_bid_awards": self.c["learner_bid_awards"], "learner_bids_lost": self.c["learner_bids_lost"],
                    "learner_bid_mean_over_cost": (round(self.c["learner_bid_award_sum"] / self.c["learner_bid_cost_sum"], 4) if self.c["learner_bid_cost_sum"] else ""),
                    "learner_held_real_mean": (round(self.c["learner_held_sum"] / self.c["learner_held_n"], 3) if self.c["learner_held_n"] else ""),
                    # the learned population (the ruling after run 32): the slots, their nominal surplus (wealth now or out, less wealth in), the action mix by period;
                    # the customers' tasks per credit, nominal (every requester), in every row
                    "learner_pop": self.a.learner_pop, "learner_pop_total": len(self.learner_pop), "learner_pop_n": sum(1 for x in self.learner_pop if x in self.actors),
                    "pop_departed": sum(1 for x in self.learner_pop if x not in self.actors),
                    "pop_surplus_nominal": (round(sum((w.wealth(x) if x in self.actors else self.depart_wealth_nominal.get(x, 0.0)) - self.wealth_in_of.get(x, 0.0) for x in self.learner_chain), 3) if self.learner_chain else ""),
                    "pop_wealth_nominal_mean": (round(sum(w.wealth(x) for x in self.learner_pop if x in self.actors) / max(1, sum(1 for x in self.learner_pop if x in self.actors)), 3) if self.learner_pop else ""),
                    "life_by_period": json.dumps(self.life_by_period) if self.life_by_period else "",   # §52: the stage counts by period and kind
                    "learner_mix_by_period": json.dumps([self.learner_mix_by_period.get(k, [0, 0, 0]) for k in range(max(self.learner_mix_by_period) + 1)]) if self.learner_mix_by_period else "",
                    "pop_tasks_received": self.c["pop_tasks_received"], "pop_req_spent_nominal": round(self.pop_req_spent_nominal, 3),
                    "pop_tasks_per_1000": (round(1000.0 * self.c["pop_tasks_received"] / self.pop_req_spent_nominal, 4) if self.pop_req_spent_nominal > 1e-9 else ""),
                    # Q7: the learned requester — its postings by rule, the tasks received, the credits spent, the surplus at --task-value, the wait and the price paid
                    "req_decisions": self.c["req_decisions"], "req_rule_market": self.c["req_rule_market"], "req_rule_floor": self.c["req_rule_floor"], "req_rule_patient": self.c["req_rule_patient"],
                    "req_posted": self.c["req_posted"], "req_unaffordable": self.c["req_unaffordable"], "req_raised": self.c["req_raised"], "req_tasks_received": self.c["req_tasks_received"],
                    "req_paid_unfulfilled": self.c["req_paid_unfulfilled"], "req_final_n": self.c["req_final_n"], "req_free_fulfilled": self.c["req_free_fulfilled"], "req_state_deliveries": self.c["req_state_deliveries"],
                    "req_wait_mean": (round(self.c["req_wait_sum"] / self.c["req_awards"], 3) if self.c["req_awards"] else ""), "req_waiting_ticks": self.c["req_waiting_ticks"],
                    "req_price_paid_mean": (round(self.c["req_price_paid_sum"] / self.c["req_awards"], 3) if self.c["req_awards"] else ""),
                    "req_disputes_filed": self.c["req_disputes_filed"], "req_disputes_won": self.c["req_disputes_won"],
                    "req_spent_real": (round(self.req_spent_real(), 3) if (self.learner_id and self.a.learner_role == "requester") else ""),
                    "req_tasks_per_1000": (round(1000.0 * self.c["req_tasks_received"] / self.req_spent_real(), 4) if (self.learner_id and self.a.learner_role == "requester" and self.req_spent_real() > 1e-9) else ""),
                    # the stability track (the ruling after run 31): the undercutting population and the requester under the reservation
                    "undercutters_n": sum(1 for x in self.undercutters if x in self.actors),
                    "undercut_awards": self.c["undercut_awards"], "undercut_awards_at_cost": self.c["undercut_awards_at_cost"],
                    "undercutter_wealth_real": self._mean_wealth_real([x for x in self.undercutters if x in self.actors], real),
                    "ratchet_careful_wealth_real": self._mean_wealth_real([x for x in self.actors if self.kind[x] == CAREFUL and x not in self.undercutters], real),
                    "awards_below_floor": self.c["awards_below_floor"], "awards_at_floor": self.c["awards_at_floor"],
                    "awards_below_floor_share": round(self.c["awards_below_floor"] / max(1, self.c["awarded"]), 4),
                    "below_floor_margin_mean": round(self.c["below_floor_margin_sum"] / self.c["awards_below_floor"], 4) if self.c["awards_below_floor"] else "",
                    "below_floor_servers_n": len(self.below_floor_servers),
                    "below_floor_server_wealth_real": self._mean_wealth_real([x for x in self.below_floor_servers if x in self.actors], real),
                    "below_floor_final_n": self.c["below_floor_final_n"], "below_floor_g_lost": round(self.c["below_floor_g_lost"], 3),
                    "under_floor_posted": self.c["under_floor_posted"], "under_floor_awarded": self.c["under_floor_awarded"],
                    "under_floor_waiting": sum(1 for x in self.under_floor_cases if x in self.active and w.case(x).state == "AVAILABLE"),
                    "under_floor_wait_mean": round(self.c["under_floor_wait_sum"] / self.c["under_floor_awarded"], 3) if self.c["under_floor_awarded"] else "",
                    "under_floor_price_mean": round(self.c["under_floor_price_sum"] / self.c["under_floor_awarded"], 4) if self.c["under_floor_awarded"] else "",
                    "under_floor_fulfilled": self.c["under_floor_fulfilled"], "under_floor_final_n": self.c["under_floor_final_n"], "under_floor_vested": self.c["under_floor_vested"],
                    "state_share": round(self.c["troop_deliveries"] / max(1, self.c["awarded"] + self.c["troop_deliveries"]), 4),
                    "requester_wallet_real": round(sum(w.wealth(r) for r in reqs) / max(1, len(reqs)) * real, 3),
                    "state_price_over_market": round(mk["state_price"] - mk["B_bar"], 4) if mk.get("state_price") is not None else "",
                    "req_surplus_real": (round(self.req_lifetime_real(), 3) if (self.learner_id and self.a.learner_role == "requester") else ""),
                    "req_wallet_real": (round(w.wealth(self.learner_id) * real, 3) if (self.learner_id and self.a.learner_role == "requester") else ""),
                    # Q4: the pair
                    "pair_ids": ("+".join(self.learner_pair) if self.learner_pair else ""), "pair_matched": self.c["pair_matched"], "pair_unmatched": self.c["pair_unmatched"], "pair_waited": self.c["pair_waited"],
                    "pair_reviews": self.c["pair_reviews"], "pair_cares": self.c["pair_cares"], "pair_stamps": self.c["pair_stamps"], "pair_rejects": self.c["pair_rejects"],
                    "pair_bad_stamped": self.c["pair_bad_stamped"], "pair_good_stamped": self.c["pair_good_stamped"],
                    "pair_bad_stamped_vested": self.c["pair_bad_stamped_vested"], "pair_bad_stamped_caught": self.c["pair_bad_stamped_caught"],
                    "pair_d_real": (round(((w.wealth(self.learner_pair[0]) - min(w.wealth(self.learner_pair[0]), w.loan_outstanding(self.learner_pair[0]))) * real) if self.learner_pair[0] in self.actors else self.depart_wealth_real.get(self.learner_pair[0], 0.0), 3) if self.learner_pair else ""),
                    "pair_r_real": (round(((w.wealth(self.learner_pair[1]) - min(w.wealth(self.learner_pair[1]), w.loan_outstanding(self.learner_pair[1]))) * real) if self.learner_pair[1] in self.actors else self.depart_wealth_real.get(self.learner_pair[1], 0.0), 3) if self.learner_pair else ""),
                    "pair_r_reviews": (self.tally[self.learner_pair[1]].reviews if self.learner_pair else ""), "pair_r_on_duty": (int(w.actor(self.learner_pair[1]).on_duty) if self.learner_pair and self.learner_pair[1] in self.actors else ""),
                    "pair_r_suspensions": (len(self.susp_log.get(self.learner_pair[1], [])) if self.learner_pair else ""), "pair_r_rho": (round(w.actor(self.learner_pair[1]).rho, 4) if self.learner_pair and self.learner_pair[1] in self.actors else ""),
                    "learner_bad_deliveries": self.c["learner_bad_deliveries"], "learner_good_deliveries": self.c["learner_good_deliveries"],
                    "learner_bad_approved": self.c["learner_bad_approved"], "learner_bad_caught": self.c["learner_bad_caught"],
                    "learner_good_vested": self.c["learner_good_vested"], "learner_good_final_n": self.c["learner_good_final_n"],
                    "learner_forfeited": round(self.c["learner_forfeited"], 3), "learner_bad_paid": round(self.c["learner_bad_paid"], 3), "learner_effort_saved": round(self.c["learner_effort_saved"], 3),
                    "learner_nested_awards": self.c["learner_nested_awards"], "learner_misses": self.c["learner_misses"], "learner_miss_lapsed": self.c["learner_miss_lapsed"],
                    "parent_judge_override": self.c["parent_judge_override"], "child_appeals_suppressed": self.c["child_appeals_suppressed"],
                    "learner_delegate_decisions": self.c["learner_delegate_decisions"], "learner_delegations": self.c["learner_delegations"], "learner_self_exec_chosen": self.c["learner_self_exec_chosen"],
                    "learner_delegate_impossible": self.c["learner_delegate_impossible"], "learner_judge_decisions": self.c["learner_judge_decisions"],
                    "learner_judge_care": self.c["learner_judge_care"], "learner_judge_stamp": self.c["learner_judge_stamp"], "learner_judge_reject": self.c["learner_judge_reject"],
                    "learner_child_stamped_bad": self.c["learner_child_stamped_bad"], "learner_child_stamped_good": self.c["learner_child_stamped_good"],
                    "learner_child_rejected_bad": self.c["learner_child_rejected_bad"], "learner_child_rejected_good": self.c["learner_child_rejected_good"],
                    "learner_cancel_decisions": self.c["learner_cancel_decisions"], "learner_cancels": self.c["learner_cancels"], "learner_cancel_refused": self.c["learner_cancel_refused"],
                    "learner_kill_fees": round(self.c["learner_kill_fees"], 3), "learner_guarantees_taken": round(self.c["learner_guarantees_taken"], 3), "learner_child_lapses": self.c["learner_child_lapses"],
                    "learner_rejections_overturned": self.c["learner_rejections_overturned"], "learner_children_settled": self.c["learner_children_settled"],
                    "slot_delivery_income": (round(self.tally[self.tell_slot].delivery, 3) if self.tell_slot else ""),
                    "slot_guarantees_forfeited": (round(self.tally[self.tell_slot].guarantees_forfeited, 3) if self.tell_slot else ""),
                    "slot_effort_burned": (round(self.tally[self.tell_slot].costs, 3) if self.tell_slot else ""),
                    "final_n_rate": round(self.c["final_n"] / (self.c["vested"] + self.c["final_n"]), 4) if (self.c["vested"] + self.c["final_n"]) else "",
                    "learner_identities": len(self.learner_chain), "learner_returns": self.learner_returns, "learner_leaves_chosen": self.learner_leaves_chosen,
                    "learner_leaves_refused": self.learner_leaves_refused, "learner_boundary_decisions": self.learner_boundary_decisions,
                    "learner_float_minted": round(self.learner_float_minted, 3), "learner_float_minted_real": round(self.learner_float_minted_real, 3),
                    "learner_lifetime_real": (round(self.learner_lifetime_real(), 3) if self.learner_chain else ""),
                    # 2.7.0: the bank's names line and the departures' net
                    "loan_on": int(bool(bank27.get("loan_on"))), "names_lent": round(bank27.get("names_lent", 0.0), 3), "names_lent_n": bank27.get("names_lent_n", 0),
                    "names_repaid": round(bank27.get("names_repaid", 0.0), 3), "names_recovered": round(bank27.get("names_recovered", 0.0), 3),
                    "names_defaulted": round(bank27.get("names_defaulted", 0.0), 3), "names_outstanding": round(bank27.get("names_outstanding", 0.0), 3),
                    "names_outstanding_peak": round(bank27.get("names_outstanding_peak", 0.0), 3), "departed_net": round(self.c["departed_net"], 3),
                    "below_bond_before_admission": len(self.below_bond_names), "unfundable_with_loan_ticks": self.c["unfundable_with_loan_ticks"],
                    "idle_for_bond_ticks": self.c["idle_for_bond_ticks"], "idle_for_bond_names": len(self.idle_for_bond_names),
                    # 2.7.0 §8.6 red team: the accomplice route
                    "acc_pair_t": self.acc_pair_t if self.acc_pair_t is not None else "", "acc_moves": self.acc_moves, "acc_moved_sum": round(self.acc_moved_sum, 3),
                    "acc_mover_out": round(self.acc_mover_out, 3) if self.acc_mover_out is not None else "",
                    "acc_mover_default": round(self.acc_mover_default, 3), "acc_mover_departed_t": self.acc_mover_departed_t if self.acc_mover_departed_t is not None else "",
                    "acc_accomplice_wealth": (round(w.wealth(self.acc_pair[1]), 3) if self.acc_pair and self.acc_pair[1] in self.actors else ""),
                    "acc_accomplice_loan": (round(w.loan_outstanding(self.acc_pair[1]), 3) if self.acc_pair and self.acc_pair[1] in self.actors else ""),
                    "accomplice_unaffordable": self.c["accomplice_unaffordable"],
                    "learner_suspensions": (sum(len(self.susp_log.get(x, [])) for x in self.learner_chain) if self.learner_chain else ""),
                    # the honesty readings for the reviewers in self-play (the ruling after run 33): the plant record and the audit layer's overturn rate, run-wide
                    "bad_plants_approved": self.c["bad_plants_approved"], "good_plants_rejected": self.c["good_plants_rejected"],
                    "audits_held": self.c["audits_held"], "audits_overturning": self.c["audits_overturning"],
                    "audit_overturn_rate": (round(self.c["audits_overturning"] / self.c["audits_held"], 4) if self.c["audits_held"] else ""),
                    **self._life_columns(),
                    "learner_departed_now": (int(self.learner_id not in self.actors) if self.learner_id else ""),
                    "tell_plant_read_plant": self.c["tell_plant_read_plant"], "tell_plant_read_real": self.c["tell_plant_read_real"],
                    "tell_real_read_plant": self.c["tell_real_read_plant"], "tell_real_read_real": self.c["tell_real_read_real"],
                    "tell_plant_pass_rate": round(self.c["tell_plant_read_plant"] / (self.c["tell_plant_read_plant"] + self.c["tell_plant_read_real"]), 4) if (self.c["tell_plant_read_plant"] + self.c["tell_plant_read_real"]) else "",
                    "tell_real_stamp_rate": round(self.c["tell_real_read_real"] / (self.c["tell_real_read_real"] + self.c["tell_real_read_plant"]), 4) if (self.c["tell_real_read_real"] + self.c["tell_real_read_plant"]) else "",
                    "tell_false_approvals": self.c["tell_false_approvals"],
                    "tell_wealth_real": round(sum(w.wealth(x) for x in self.tell_readers if x in self.actors) / max(1, sum(1 for x in self.tell_readers if x in self.actors)) * real, 3) if self.tell_readers else "",
                    "tell_suspended_now": sum(1 for x in self.tell_readers if x in self.actors if w.actor(x).suspended_until is not None) if self.tell_readers else "",
                    "tell_plant_failures": sum(self.tally[x].plant_failures for x in self.tell_readers if x in self.actors) if self.tell_readers else "",
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
        rank = lambda x: (sum(1 for v in cost_rank if v <= self.c_d_of[x]) / max(1, len(cost_rank)))   # a departed broker ranks against the present
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
        # run 17: the inspection queue (batch A), the red team and the strategy variants (B, C)
        sc, sw = self.seat_counts, self.seat_wait_sum
        row.update({f"seats_{k}_{s}": sc[(k, s)] for k in ("initial", "audit", "appeal") for s in ("member", "probationer", "troop")})
        row.update({f"wait_{k}_{s}": sw[(k, s)] for k in ("initial", "audit", "appeal") for s in ("member", "probationer", "troop")})
        row.update({f"waitge_{k}_{s}": self.seat_wait_ge_wR[(k, s)] for k in ("initial", "audit", "appeal") for s in ("member", "probationer", "troop")})
        row.update({f"left_{k}": self.seat_left_otherwise[k] for k in ("initial", "audit", "appeal")})
        row.update({"waiting_now": sum(1 for k in self.waiting_since), **{f"avail_{k}": self.avail[k] for k in AVAIL_KEYS},
                    "cap_now": self.cap_now, "members_on_duty_now": self.members_on_duty_now, "E_t_now": self.E_t_now,
                    "cap_slack_sum": self.cap_slack_sum, "cap_slack_n": self.cap_slack_n, "cap_bound_ticks": self.cap_bound_ticks,
                    **{k: self.c[k] for k in ("seated_initial_member", "seated_initial_probationer", "seated_audit_member", "seated_appeal_member", "seated_plant")},
                    "cycles": self.c["cycles"], "greedy_rejections": self.c["greedy_rejections"],
                    "greedy_cases_vested": sum(1 for nid, rc in self.nested_parent.items() if w.case(rc).actor in self.greedy and w.case(nid).state == "VESTED"),
                    "lowball_child_awards": self.c["lowball_child_awards"], "lowball_child_misses": self.c["lowball_child_misses"],
                    "nested_fa_stamper_parent": self.c["nested_fa_stamper_parent"], "nested_fa_careful_parent": self.c["nested_fa_careful_parent"],
                    "nested_posted_by_stamper": self.c["nested_posted_by_stamper"], "nested_posted_by_careful": self.c["nested_posted_by_careful"],
                    "patient_raised": self.c["patient_raised"],
                    "cycler_wealth_real": round(sum(w.wealth(x) for x in self.actors if x in self.cycled_from) / max(1, sum(1 for x in self.actors if x in self.cycled_from)) * real, 3) if self.cycled_from else "",
                    "cyclers_admitted": sum(1 for x in self.actors if x in self.cycled_from and w.actor(x).admitted_at is not None)})
        row.update({"pfa_route_upheld": len(self.pfa_upheld_by), "pfa_route_overturned": self.pfa_overturned,
                    "pfa_route_other": self.pfa_other, "pfa_kind_troop": kinds["troop"], "pfa_kind_standing": kinds["standing"],
                    "pfa_kind_lag": kinds["lag"], "pfa_kind_readmitted": kinds["readmitted"]})
        return row


def build_parser():
    """The run's arguments — shared by `main` and the red team's environment (`redteam.env`), which builds a run from the same cell."""
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
    ap.add_argument("--rules", choices=["2.8.0", "2.7.0", "2.6.0", "2.5.0", "2.4.0", "2.3.0", "2.2.0", "2.1.0", "2.0.0", "1.7.1", "1.7.0", "1.6.0", "1.5.0", "1.4.0", "1.3.0", "1.2.0", "1.1.0"], default="2.8.0",
                    help="2.6.0: the plant's disguise (a plant goes through the market: posted under a fresh name, bid on, awarded on the market's report, submitted at a drawn tick; opaque public ids); 2.5.0: the missed child (no cancellation of a nested request at or after its deadline; the lapse forfeits the child's guarantee); 2.4.0: the same without the refusal — the control admitting the deadline-tick cancellation; 2.4.0 also: the state's reservation (the state delivers at max(B̄, 8), never below; the mark; the clock's one condition; the award pass gathering β ≥ p_T); 2.3.0: the supply side (entry and exit, the parent's pots, the reviewer advance from the pool) — the control, the state at B̄; 2.2.0: the rebate from income (the period's fee pool, claims pro rata at the close, the rest forgone); 2.1.0: the bank with the liability stock (the control); 2.1.0 also: the bank (loans, the debt, the wall, the expected cost, P_t once a period, refusals told); 2.0.0: the price of work with "
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
    ap.add_argument("--duty-cap", choices=["half", "twothirds", "threequarters", "all"], default=None,
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
    ap.add_argument("--appeal-policy", choices=["none", "truthful", "always"], default="truthful",
                    help="the actor's response to an N: none = accept (the population's default through run 23); truthful = appeal when "
                         "the work is truly fulfilled (the default from run 24, the reviewer's ruling after run 23); "
                         "always = appeal every N (the court fee D is paid when the actor can fund it)")
    ap.add_argument("--care-cost", type=float, default=1.0,
                    help="the careful reviewer's care cost as a multiple of the drawn {2, 3} credits (1.0 the population's; raised in the "
                         "calibration cell only, so the cell's ideal clears careful by three standard errors — the ruling after run 23)")
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
    ap.add_argument("--ceiling-policy", choices=["wallet", "market", "patient", "patient-blind", "floor", "under-floor"], default="wallet",
                    help="the requesters' ceiling: min(β_max, share × unlocked wallet), or market-aware min(β_max, mult × B̄) (run 13 §3)")
    ap.add_argument("--ceiling-mult", type=float, default=1.2, help="the market-aware ceiling's multiple of B̄")
    ap.add_argument("--ceiling-requesters", type=int, default=0,
                    help="the stability track (the ruling after run 31): the first N standing requesters follow --ceiling-policy, the rest the wallet rule (0: all, as before)")
    ap.add_argument("--under-floor-frac", type=float, default=0.75,
                    help="--ceiling-policy under-floor: the ceiling as a fraction of the state's reservation — posted under the floor, never raised; the state never serves it "
                         "and its clock does not run (2.4.0), so it clears only on a member's bid under the floor")
    ap.add_argument("--bid", choices=["margin", "ceiling", "floor-plus", "undercut"], default="margin",
                    help="members' bid policy: c_D (1 + m); at the ceiling (the 1.x behaviour, the control); or 2.4.0 §8.7's collusion — every member whose cost allows "
                         "bids the state's floor × (1 + --bid-plus) on every request, the others c_D (1 + m); or the stability track's undercutting population "
                         "(the ruling after run 31) — the careful members in --undercut-share bid (1 − --undercut) B̄ floored at their cost (Q6's rule), the rest the ratchet")
    ap.add_argument("--undercut-share", type=float, default=1.0,
                    help="--bid undercut: the share of the careful members that undercut (drawn once at genesis and at each careful arrival); 1.0 every careful member")
    ap.add_argument("--bid-plus", type=float, default=0.01, help="--bid floor-plus: the colluding members' bid above the floor, as a share of it")
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
    ap.add_argument("--accomplice", choices=["on", "off"], default="off",
                    help="2.7.0 §8.6 red team: the first two arrival-born members admitted are a mover and its accomplice — the mover posts a nested request at the largest ceiling its unlocked balance can lock (its float included) and awards the accomplice directly; it departs at the first boundary after a move (needs --delegation on)")
    ap.add_argument("--delegation", choices=["on", "off"], default="off", help="2.3.0 §2.4: parents delegate when their cost exceeds the expected child's bid plus the overhead")
    ap.add_argument("--nested-tau", type=int, default=6, help="the extra ticks a member's bid carries under delegation, for a child's work")
    ap.add_argument("--nested-pots", choices=["parent", "root"], default="parent", help="2.3.0 §2.4: the parent posts the nested pots; root = the 1.1.0 reading (the control)")
    # run 17 — the red team of 2.3.0 §8.7 and the strategy variants of batch C
    ap.add_argument("--cycler", choices=["on", "off"], default="off",
                    help="§8.7 red team: a suspended stamper with no live obligation departs and re-arrives at once under a fresh identity (the control: it serves its probation)")
    ap.add_argument("--greedy-parents", type=float, default=0.0,
                    help="§8.7 red team: the share of careful actors that, as parents, reject every child's work to collect the guarantee")
    ap.add_argument("--lowball-children", type=float, default=0.0,
                    help="§8.7 red team: the share of actors that bid half their cost on nested requests and never deliver (the kill fee, the parent's exit)")
    ap.add_argument("--child-bid", choices=["margin", "ceiling-aware"], default="margin",
                    help="batch C: a child bids c(1 + m), or min(the parent's ceiling, c(1 + m)) when its cost is under the ceiling")
    ap.add_argument("--patient-ticks", type=int, default=20,
                    help="--ceiling-policy patient: a request posts at 0.7 B̄ and is raised only after this many ticks unserved — to max(B̄, the state's "
                         "floor) read from the view (2.4.0), or to B̄ alone under patient-blind (run 17's policy, which deadlocks at the floor)")
    # 2.4.0 — the state's reservation
    ap.add_argument("--state-reservation", type=float, default=None,
                    help="2.4.0 §2.1: the state's floor — nominal, public (default 8; 0 is the control, the 2.3.0 state at B̄; swept 4 / 8 / 12)")
    # 2.5.0 §8.5 red team
    ap.add_argument("--farm-parents", type=float, default=0.0,
                    help="2.5.0 §8.5 red team: the share of careful actors that, as parents, post nested requests with a deadline too short to meet (tau 1 against work_ticks 2) to farm the children's guarantees")
    ap.add_argument("--children-read-deadline", choices=["on", "off"], default="on",
                    help="2.5.0 §8.5: a child bids on a nested request only where its deadline leaves it room to deliver (tau ≥ work_ticks); off: it bids regardless")
    ap.add_argument("--lowball-mode", choices=["miss", "empty"], default="miss",
                    help="2.5.0 §8.5 red team: a lowball child misses its deadline (run 17's), or submits an empty result at its deadline to avoid the lapse and appeals the rejection")
    ap.add_argument("--parent-cancel", choices=["on", "off", "early", "eve"], default="off",
                    help="2.4.0 §2.4: a parent whose child has not submitted cancels while self-execution is still possible, pays the kill fee "
                         "(the child's recorded cost — zero for a child that never worked) and does the work itself; `on`: when the parent's own deadline "
                         "leaves one work_ticks; `early`: at the child's deadline tick — the world's clock at the deadline, after the tick's submissions, before "
                         "the engine's lapse (refused under 2.5.0, admitted under 2.4.0); `eve`: one tick before the deadline, run 18's last-batch move, "
                         "admitted under both (a parent that will not wait)")
    ap.add_argument("--small-requests", type=int, default=0,
                    help="2.2.0 §8.5 red team: this many requesters post at the market price exactly with K_open tripled — many small requests to collect pro-rata rebates (expected: nothing beyond the capped claims)")
    ap.add_argument("--tell-readers", type=float, default=0.0,
                    help="Q2 (the learned red team, hand-written first): the share of careful actors that read the view for a plant's tells and stamp the rest")
    ap.add_argument("--tell", default="gap+cap", help="the tells read, joined by +: gap (assigned the tick it was submitted), cap (K at this period's index), idage (the id newer than every root seen available before the submission tick); all (the three, any); oracle (the plant marker itself — declared non-conforming, the upper bound a perfect detector earns)")
    ap.add_argument("--tell-rule", choices=["any", "all"], default="any", help="a plant is read when any tell fires, or only when all do")
    ap.add_argument("--tie-break", choices=["draw", "id"], default=None, help="2.6.0 §2.3: the tie after κ broken by a seeded draw (the default under 2.6.0) or by the lowest id (the control, the earlier rules' default)")
    ap.add_argument("--genesis-duty", choices=["draw", "lowest"], default=None, help="2.6.0 §2.3: the genesis duty reserve by a seeded draw (the default under 2.6.0) or the lowest-id actors (the control)")
    ap.add_argument("--trailing-periods", type=int, default=1, help="2.6.0: the closed periods a plant's draws read (1; the knob 2)")
    ap.add_argument("--arrival-loan", choices=["on", "off"], default="on",
                    help="2.7.0: the arrival float is a loan of the bank's — repaid from the name's income first, recovered at departure, the shortfall the bank's default; off is 2.6.1's grant (the control; --rules 2.6.0 too)")
    ap.add_argument("--learner-slot", choices=["on", "off"], default="off", help="the learned red team: the slot actor's reviewing decisions come from the policy redteam.env supplies (nothing changes without it)")
    ap.add_argument("--learner-role", choices=["reviewer", "deliverer", "child", "parent", "bidder", "requester"], default="reviewer",
                    help="Q3 (the learned deliverer): `deliverer` — the slot reviews as the population's actor at its slot does, and its quality decision "
                         "at each submission comes from the policy (0 deliver well, the effort burned; 1 deliver badly at zero effort); `reviewer` is Q1/Q2's")
    ap.add_argument("--effort-cost", type=float, default=1.0, help="Q3's calibration knob: a multiple on every actor's effort cost (as --care-cost is on the care cost)")
    ap.add_argument("--good-delivery", choices=["certain", "draw"], default="draw",
                    help="the learned deliverer's good delivery: `draw` — the task's own draw at b (the ruling after run 27, from Q4 on); `certain` — fulfilled (Q3's reading)")
    ap.add_argument("--child-prefers-nested", choices=["on", "off"], default="off",
                    help="Q5: the learned child offers for nested requests only, never for roots (a declared construction: the slot is committed on roots most of the run otherwise)")
    ap.add_argument("--child-g-frac", type=float, default=None,
                    help="Q5's parent calibration knob (the ruling after the parent's references): a nested case's guarantee fraction in place of G_frac (0.5) — raised in the calibration cell only")
    ap.add_argument("--undercut", type=float, default=0.2,
                    help="Q6: the undercut's bid — the market price B̄ cut by this fraction, floored at the actor's cost (the ratchet, by contrast, bids its cost times 1 + m and lets m climb to the price)")
    ap.add_argument("--requester-slot", type=int, default=0, help="Q7: the learned requester's slot — the standing requesters in order (0 the first)")
    ap.add_argument("--task-value", type=float, default=0.0,
                    help="Q7: the value to the learned requester of a task received (a settled delivery whose truth is fulfilled), real (P_0 units); its measure is the surplus "
                         "v·F − S — tasks per credit linearized: read at the careful requester's own credits per task, so the careful reads about zero and a cheaper requester above it")
    ap.add_argument("--learner-pop", choices=["off", "all", "half"], default="off",
                    help="the learned population (the ruling after run 32; with --learner-role bidder): every careful member — or half, drawn once as --undercut-share 0.5 draws — "
                         "a learner slot sharing one policy in self-play, each on its own observation; careful arrivals join by the same draw; the lifetime summed over the slots. "
                         "With --learner-role reviewer (the ruling after run 33): every member, stampers included, and every arrival — the 60/40 is the `hand` reference on the same slots")
    ap.add_argument("--bidder-slot", choices=["first", "cheapest", "median", "costliest"], default="cheapest",
                    help="Q6 (the learned bidder): the slot — the cheapest careful actor by default (where undercutting the ratchet has the most room), the median, the costliest, or the first careful id")
    ap.add_argument("--parent-slot", choices=["first", "costliest", "median"], default="costliest",
                    help="Q5 (the learned parent): the slot — the first careful id, or the costliest careful actor (the default: a cheap parent cannot post a child at the rule's ceiling)")
    ap.add_argument("--parent-judge", choices=["careful", "stamp", "reject"], default="careful",
                    help="Q5's calibration knob: every parent's judgment of its child — by disposition (careful), approve blind (stamp) or reject blind (reject)")
    ap.add_argument("--child-appeal", choices=["truthful", "none"], default="truthful", help="Q5's calibration knob: a rejected child appeals truthfully (2.3.0 §2.4, declared) or never")
    ap.add_argument("--learner-pair", choices=["on", "off"], default="off",
                    help="Q4: two learners with a shared reward — the slot a deliverer, the next careful id a reviewer (both LEARNER; the lifetime read as one)")
    ap.add_argument("--match-pair", choices=["on", "off"], default="off", help="Q4's calibration: the pair's reviewer takes the deliverer's initial review whenever it is eligible")
    ap.add_argument("--pair-volunteer", choices=["on", "off"], default="on", help="Q4: the pair's reviewer volunteers for duty (§7.5) and is kept on it")
    ap.add_argument("--learner-exit", choices=["own", "rule"], default="own", help="the ruling after the calibration ladder: `own` — the exit is the learner's boundary decision everywhere and the driver's exit rule skips it; `rule` — the exit rule applies to the slot as to any member (runs 22–25)")
    ap.add_argument("--learner-rearrive", choices=["on", "off"], default="off",
                    help="the reviewer's ruling after run 22: re-arrival is allowed the learner — at each period boundary it may leave (depart, and arrive at once under a fresh name with the float, a probationer), and a departure by the exit rule returns it the same way; its lifetime real wealth is summed across its identities, the floats minted per return and its bill to the loop read beside")
    ap.add_argument("--audit-roll", choices=["on", "off"], default="on",
                    help="off: the driver never rolls an audit (the learned red team's calibration cell — a declared implementation effect, with --pi0 0 --dial off a blind stamp costs nothing)")
    ap.add_argument("--plants-every-seat", choices=["on", "off"], default="on",
                    help="2.8.0 (design revision 16): the plants reach every seat — audited, appealed, disputed, revised, adjudicated by truth at each; off is 2.7.0 (also --rules 2.7.0)")
    ap.add_argument("--plant-submit", type=int, default=0, help="2.6.0: pin the plant actor's time to submission (0: the draw from the trailing real deliveries'; 1 the lag-pinning cell)")
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
    return ap


def parse_args(argv=None):
    a = build_parser().parse_args(argv)
    if a.c_d_t_mode is None:
        a.c_d_t_mode = "expected" if a.rules in ("2.1.0", "2.2.0", "2.3.0", "2.4.0", "2.5.0", "2.6.0", "2.7.0", "2.8.0") else "cost"
    if a.rules not in ("2.3.0", "2.4.0", "2.5.0", "2.6.0", "2.7.0", "2.8.0"):
        a.c_d_sigma = 0.0                                # one cost before 2.3.0: the controls are run 15's cells
    return a


def main(argv=None):
    a = parse_args(argv)
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
                                "audit_roll": ("on the engine's applied odds (audit_odds); a yes is recorded as an obligation (roll_audit) and never dropped" if a.audit_roll == "on"
                                               else "NEVER ROLLED (--audit-roll off: the learned red team's calibration cell — a declared implementation effect)"),
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
                                                 "careful": {"accuracy": a.accuracy, "care_cost_scale": a.care_cost, "cost": "uniform {2, 3} credits, or what unlocked "
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
                                "the_supply_side": None if a.rules not in ("2.3.0", "2.4.0", "2.5.0", "2.6.0", "2.7.0", "2.8.0") else {
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
                                "the_rebate_from_income": None if a.rules not in ("2.2.0", "2.3.0", "2.4.0", "2.5.0", "2.6.0", "2.7.0", "2.8.0") else {
                                    "spec": "2.2.0 design revision 10 — the claim recorded at the stop; Ω's fee income after the debt pooled as a lock on Ω; at the period's close the "
                                            "claims stopped in the period paid pro rata, the rest forgone and read; no liability stock",
                                    "red_team": {"small_requesters": sorted(run.small)}},
                                "the_bank": None if a.rules not in ("2.1.0", "2.2.0", "2.3.0", "2.4.0", "2.5.0", "2.6.0", "2.7.0", "2.8.0") else {
                                    "spec": "2.1.0 design revision 9 — the bank: a second account that alone creates and destroys; mints by rule, publishes "
                                            "P_t once a period, lends a summons's shortfall tied to it; the state burns its expected cost and delivers at B̄; "
                                            "every inflow to Ω ordered at once (debt → liabilities → Ω); the wall on deliveries; every refusal told",
                                    "c_D_T": a.c_d_t_mode, "b_T_prior": a.b_t_prior, "b_T_min_n": a.b_t_min_n,
                                    "wall_periods": a.debt_bound_periods if a.debt_bound_periods > 0 else "unbounded (control)",
                                    "requester_on_refusal": a.requester_on_refusal,
                                    "red_team": {"troop_fail_rate": a.troop_fail_rate, "state_rejecters": sorted(run.state_rejecters),
                                                 "state_rejecters_reading": "the case's actor through the public view's case — not the reviewer's view (§14 carries no actor); declared"}},
                                "price_of_work": None if a.rules not in ("2.0.0", "2.1.0", "2.2.0", "2.3.0", "2.4.0", "2.5.0", "2.6.0", "2.7.0", "2.8.0") else {
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
                                "permitted_operations": PERMITTED + (PERMITTED_200 if a.rules in ("2.0.0", "2.1.0", "2.2.0", "2.3.0", "2.4.0", "2.5.0", "2.6.0", "2.7.0", "2.8.0") else []), "not_in_run": NOT_IN_RUN,
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
    for kind in ((CAREFUL, STAMPER, TELL) if a.tell_readers > 0 else (CAREFUL, STAMPER)):
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
    for kind in ((CAREFUL, STAMPER, TELL) if a.tell_readers > 0 else (CAREFUL, STAMPER)):
        print(f"  {kind:8s} plant reviews={final[kind + '_plant_reviews']:6.2f} failures={final[kind + '_plant_failures']:5.2f} "
              f"a_hat={final[kind + '_a_hat']:.3f} suspended={final[kind + '_suspended']} duty-eligible={final[kind + '_duty_eligible']} "
              f"panel-eligible={final[kind + '_panel_eligible']}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

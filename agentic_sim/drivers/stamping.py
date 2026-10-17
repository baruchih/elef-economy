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
NOT_IN_RUN = ["appeals by actors (unless --appeal-policy is set)", "disputes (unless --dispute-policy is set)", "human overrides", "P/⊥", "revision/evidence", "delegation (nested cases)",
              "cancellation", "resource spend by actors", "volunteering for duty", "actor competence (truth is actor-independent)",
              "price competition (every offer is at the ceiling)", "requester budget pressure (H is funded beyond the run)",
              "a reviewer that tries to tell a plant from real work (the view carries nothing to tell by; 1.2.0 §2.1)"]


@dataclass
class Task:
    cid: str
    title: str
    fulfilled: bool              # hidden truth
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
        rev3 = a.rules in ("1.3.0", "1.4.0")     # 1.2.0 and 1.1.0: membership, the fund and netted capital off
        rev4 = a.rules == "1.4.0" and a.troops == "on"
        p = Params(Res0=a.res0, X=a.on_duty, G_V=a.gv, p_start=a.p_start, p_cap=a.p_cap, p_floor=a.p_floor, band=a.band,
                   record_dir=a.record_dir, f_fee=a.fee, phi_E_root=a.phi_e, phi_F_root=a.phi_f,
                   pi0=a.pi0, dial=(a.dial == "on"), beta_P=a.beta_p, Omega0=a.omega0,
                   membership=rev3, duty_fund=(rev3 and a.fund == "on"), net_plant_capital=rev3, m_max=a.m_max,
                   troops=rev4, eps_T=a.eps_t, w_R=a.w_r, w_A=a.w_a, c_T=a.c_t, c_D_T=a.c_d_t, A_T=a.a_t, tau_T=a.work_ticks)
        self.p = p
        world = World(p, self.actors, humans={"H": a.human_budget}, on_duty=sorted(self.actors)[: a.on_duty])
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
                  "troop_delivered_vested": 0, "troop_delivered_final_n": 0, "troop_false_approvals": 0}
        self.omega0_total = self.w.money()["omega_total"]
        self.by_grade = {g: [0, 0] for g in GRADES}       # grade -> [cases, correct]
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
        affordable = self.w.unlocked(reviewer) * self.w.money()["v"] - 1e-6     # real units purchasable
        if affordable >= want:
            return v, want
        self.c["underfunded_careful_reviews"] += 1
        return v, max(0.0, math.floor(affordable * 100) / 100)

    def free_workers(self) -> list[str]:
        """Free, fundable, and — since 1.3.0 §2.1 — a member of the market; the engine refuses the rest."""
        out = []
        for aid in self.actors:
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
        if a.drift_to > 0 and t % a.drift_every == 0:
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
        # requester posts
        for _ in range(a.tasks):
            if w.unlocked("H") < a.beta + self.p.phi_root + self.p.omega_rate * a.beta:
                break
            cid = w.post_root("H", a.beta)
            self.title_n += 1
            self.tasks[cid] = Task(cid, f"task #{self.title_n}", fulfilled=self.rng.random() >= a.fail_rate)
            self.active[cid] = True
            self.c["posted"] += 1
        # orchestrator awards
        for cid in sorted(self.active, key=lambda s: int(s[1:])):
            if w.case(cid).state != "AVAILABLE":
                continue
            offers = self.free_workers()
            if not offers:
                self.c["awards_unfilled_ticks"] += 1
                if self.p.membership and any(not w.actor(x).is_member and w.actor(x).committed is None and not w.actor(x).on_duty
                                             for x in self.actors):
                    self.c["awards_refused_members_only_ticks"] += 1
                break
            actor = self.select(offers)
            w.award(cid, actor, a.beta, a.work_ticks)
            self.tally[actor].awards += 1
            self.c["awarded"] += 1
        # actors work and submit
        for cid in list(self.active):
            c = w.case(cid)
            if c.state == "COMMITTED" and t >= c.t_award + min(a.work_ticks, c.tau):
                w.submit(cid)
                if w.is_troop(c.actor):
                    self.c["troop_deliveries"] += 1
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
                        continue
                    on_probation = w.actor(r.reviewer).probation
                    v, cost = self.verdict(r.reviewer, self.tasks[cid].fulfilled)
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
                cid = w.create_plant(truth, a.beta)
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
                        w.dispute(cid, "H", "the result does not meet the request")
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
        w.advance(t)
        self.harvest()

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
                    "H_unlocked": round(w.unlocked("H"), 3), "active_cases": len(self.active),
                    "m": round(d["m"], 4), "pi": round(d["pi"], 4), "X_t": d["X_t"], "on_duty": sum(1 for aid in self.actors if w.actor(aid).on_duty),
                    "F_hat": last.get("F_hat", ""), "periods": len(d["periods"]), "suspensions": d["suspensions"],
                    "alarms": d["alarms"], "eligibility_shortfall": d["eligibility_shortfall"],
                    "plant_shortfall": d["plant_shortfall"],
                    "member_seats": d["member_seats"], "readmissions": d["readmissions"],
                    "readmission_ticks_mean": round(d["readmission_ticks_mean"], 1) if d["readmission_ticks_mean"] else "",
                    "duty_fund": round(m["duty_fund"], 3), "fund_in": round(m["fund_in"], 3), "fund_out": round(m["fund_out"], 3),
                    "members_on_duty": sum(1 for aid in self.actors if w.actor(aid).on_duty and w.actor(aid).is_member),
                    "probationers_on_duty": sum(1 for aid in self.actors if w.actor(aid).on_duty and w.actor(aid).probation)})
        tr = w.troops()
        row.update({"troops_active_reviews": tr["active_reviews"], "troops_active_deliveries": tr["active_deliveries"],
                    "troop_summons_reviews": tr["summons_reviews"], "troop_summons_deliveries": tr["summons_deliveries"],
                    "troop_shortfall_seats": tr["shortfall_seats"], "troop_shortfall_awards": tr["shortfall_awards"],
                    "troop_held_ticks": tr["held_ticks"], "troop_ticks_reviews": tr["troop_ticks_reviews"],
                    "troop_ticks_deliveries": tr["troop_ticks_deliveries"], "held_market_audit_now": tr["held_market_audit_now"],
                    "held_market_audit_max_age": tr["held_market_audit_max_age"], "fund_reserve": round(tr["fund_reserve"], 3),
                    "advance_outstanding": round(tr["advance_outstanding"], 3), "B_bar": round(tr["B_bar"], 3)})
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
    ap.add_argument("--rules", choices=["1.4.0", "1.3.0", "1.2.0", "1.1.0"], default="1.4.0",
                    help="1.3.0: troops off; 1.2.0: also membership, the duty fund and netted plant capital off; 1.1.0: also no "
                         "plants, dial off, p_start = p_cap = 0.5, Ω float 20 — declared controls. The audit obligation holds in all")
    ap.add_argument("--troops", choices=["on", "off"], default="on", help="the orchestrator's troops (1.4.0)")
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
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--res0", type=float, default=1e7)
    ap.add_argument("--human-budget", type=float, default=1e6)
    ap.add_argument("--record-dir", default=None)
    ap.add_argument("--log-every", type=int, default=10)
    ap.add_argument("--name", default=None)
    ap.add_argument("--expect-head", default=None)
    ap.add_argument("--results-root", default=None, help="write results/runs under this directory instead of results/")
    a = ap.parse_args(argv)

    name = a.name or f"stamping-s{a.stampers:g}-p{a.p_start:g}-gv{a.gv:g}-b{a.fail_rate:g}-f{a.fee:g}-X{a.on_duty}-seed{a.seed}"
    run = Stamping(a)
    rec = RunRecorder(name, kind="scoped run — §18.1 q1 careful vs careless review; policies fixed by disposition",
                      params=run.p, **({"root": a.results_root} if a.results_root else {}),
                      declared={"actors": a.actors, "on_duty": a.on_duty, "ticks": a.ticks, "tasks_per_tick": a.tasks,
                                "beta": a.beta, "work_ticks": a.work_ticks, "seed": a.seed,
                                "rules": a.rules, "fund": a.fund if a.rules in ("1.3.0", "1.4.0") else "n/a", "m_max": a.m_max,
                                "troops": {"spec": "1.4.0 design revision 4 — the orchestrator's troops" if a.rules == "1.4.0" and a.troops == "on" else "off",
                                           "eps_T": a.eps_t, "w_R": a.w_r, "w_A": a.w_a, "c_T": a.c_t, "c_D_T": a.c_d_t, "A_T": a.a_t,
                                           "disposition": "the truth with probability 1 − ε_T; delivery fails at b as any; no cost at completion",
                                           "summons": "the engine's, at the seating step; the driver supplies the verdict and the submission"},
                                "audit_roll": "on the engine's applied odds (audit_odds); a yes is recorded as an obligation (roll_audit) and never dropped",
                                "stamper_mode": a.stamper_mode,
                                "dispositions": {"stamper_fraction": a.stampers,
                                                 "assignment": dict(sorted(run.kind.items())),
                                                 "careful": {"accuracy": a.accuracy, "cost": "uniform {2, 3} credits, or what unlocked "
                                                                                           "credit can buy (counted as underfunded)"},
                                                 "stamper": {"verdict": "F" if a.camouflage == 0 else f"F, N w.p. {a.camouflage} (camouflage)",
                                                             "cost": 0,
                                                             "on_probation": "careful" if a.stamper_mode == "reformer" else "as above"}},
                                "membership": {"spec": "1.3.0 design revision 3 — inspection is membership" if a.rules == "1.3.0" else "none (control)",
                                               "offers": "members only; a suspended actor or probationer is not offered work",
                                               "panel": "the engine's two tiers; probationers are offered initial reviews only"},
                                "task_world": {"fail_rate_b": a.fail_rate, "truth": "hidden, independent of actor"},
                                "fee_rule": {"spec": "1.1.0 design revision 1 — the verification deposit is two pots",
                                             "f": a.fee, "phi_E": a.phi_e, "phi_F": a.phi_f, "K": run.p.K, "G_V": a.gv},
                                "dispositions_move": {"drift": None if a.drift_to == 0 else
                                                      {"to": a.drift_to, "every": a.drift_every, "step": a.drift_step,
                                                       "how": "careful actors re-drawn as stampers at random"},
                                                      "adaptive": None if a.adapt_rate == 0 else
                                                      {"rate": a.adapt_rate, "every": a.adapt_every,
                                                       "how": "each actor takes the richer disposition by mean public wealth, w.p. rate"}},
                                "clock": {"spec": "1.2.0 design revision 2 — the loop's own clock" if a.rules == "1.2.0" else "none (1.1.0 control)",
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
                                "permitted_operations": PERMITTED, "not_in_run": NOT_IN_RUN,
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
    for kind in (CAREFUL, STAMPER):
        print(f"  {kind:8s} plant reviews={final[kind + '_plant_reviews']:6.2f} failures={final[kind + '_plant_failures']:5.2f} "
              f"a_hat={final[kind + '_a_hat']:.3f} suspended={final[kind + '_suspended']} duty-eligible={final[kind + '_duty_eligible']} "
              f"panel-eligible={final[kind + '_panel_eligible']}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

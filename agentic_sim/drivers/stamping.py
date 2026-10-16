"""Scoped run — careful versus careless review (spec §18.1 question 1).

Permitted operations, declared before the run (§18.2): root cases only; F/N reviewers; actors
accept every N (no appeals); human requesters silent (no disputes, no overrides); no delegation,
no P/⊥, no resource spend by actors; the orchestrator selects, rolls audits and rules on splits;
rotation is the engine's (§13). Seeded; the engine itself is deterministic.

    python3 -m drivers.stamping --actors 20 --ticks 1000 --stampers 0.5 --seed 1

Task world. Each task has a hidden truth: it fails at base rate b, independent of the actor
(actor competence is question 2's subject and is kept out). Actors are the same population as
reviewers — the reserve rotates through them — and each has a fixed reviewing disposition:

  careful   verdict equals the truth with probability a; costs 2–3 credits per review (within K),
            or what its unlocked credit can buy when earlier bonds have left it short (counted)
  stamper   always F, cost 0

Orchestrator. Every free actor offers the ceiling (B = β) with the same τ, so S_θ = ρ − λB/β
reduces to argmax ρ, with the κ tie band: among offers within `band` of the best score the
highest duty credit wins, then the lowest id. Audits: after an initial F the engine's p_audit of
that reviewer is rolled once, honestly; the auditor is whoever the reserve rotation makes
eligible, stampers included — a stamper auditing a stamper agrees, and that self-protection is
part of the dynamic. A split (audit N against a second review's F, or the reverse) is ruled by
the truth with probability r, otherwise the other way.

What is measured, per disposition over time: wealth, delivery income, review fees, costs,
bonds and guarantees forfeited, awards won, reviews done and overturned, ρ, κ, p_audit; and for
the economy: false approvals that vested, false rejections, label accuracy by grade, audits
rolled/assigned/unassignable, reviews unassignable for lack of an eligible reviewer (the reviewer
capital ceiling), rulings. Prediction under test: a stamper earns more per review (+1.3 at the
defaults) and the question is whether lost awards and forfeited bonds outweigh it, and at which
(p_start, G^V, b) the sign flips. A finding here is an evaluation under the fixed rules (§19).
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
from sim.engine import F, N                                         # noqa: E402
from drivers.view import Public                                     # noqa: E402
from drivers.results import RunRecorder                             # noqa: E402

CAREFUL, STAMPER = "careful", "stamper"
GRADES = ("human-explicit", "delegate-explicit", "procedural", "protocol-default")

PERMITTED = ["post_root (human H, β fixed)", "award (every free actor offers B = β, τ = work_ticks; S_θ argmax ρ, κ tie band)",
             "submit (after work_ticks, no spend)", "assign_initial (eligible on-duty reviewer, seeded choice)",
             "complete_review F/N (verdict by disposition and the hidden truth; cost by disposition)",
             "respond accept (every N)", "assign_audit (p_audit of the initial reviewer rolled once per F verdict)",
             "assign_appeal (the second review of an audit challenge)", "rule (split ruled by the truth w.p. r)",
             "advance"]
NOT_IN_RUN = ["appeals by actors", "disputes", "human overrides", "P/⊥", "revision/evidence", "delegation (nested cases)",
              "cancellation", "resource spend by actors", "volunteering for duty", "actor competence (truth is actor-independent)",
              "price competition (every offer is at the ceiling)", "requester budget pressure (H is funded beyond the run)"]


@dataclass
class Task:
    cid: str
    title: str
    fulfilled: bool              # hidden truth
    audit_rolled: bool = False
    audit_wanted: bool = False   # rolled yes, not yet assigned
    appeal_wanted: bool = False


@dataclass
class Tally:
    """Per-actor money and outcome counters, accumulated from the public event record."""
    delivery: float = 0.0
    fees: float = 0.0
    reimbursed: float = 0.0
    costs: float = 0.0
    bonds_forfeited: float = 0.0
    guarantees_forfeited: float = 0.0
    awards: int = 0
    reviews: int = 0
    overturned: int = 0
    audits_done: int = 0


class Stamping:
    def __init__(self, a, rec: RunRecorder | None = None):
        self.a = a
        self.rng = random.Random(a.seed)
        self.actors = [f"a{i:02d}" for i in range(a.actors)]
        n_st = round(a.actors * a.stampers)
        ids = list(self.actors)
        self.rng.shuffle(ids)
        self.kind = {aid: (STAMPER if i < n_st else CAREFUL) for i, aid in enumerate(ids)}
        p = Params(Res0=a.res0, X=a.on_duty, G_V=a.gv, p_start=a.p_start, record_dir=a.record_dir)
        self.p = p
        world = World(p, self.actors, humans={"H": a.human_budget}, on_duty=sorted(self.actors)[: a.on_duty])
        self.w = Public(world)
        self._world = world            # for the final check_all and the fingerprint only
        self.tasks: dict[str, Task] = {}
        self.active: dict[str, bool] = {}        # ordered: creation order, never a set (determinism)
        self.tally = {aid: Tally() for aid in self.actors}
        self.review_owner: dict[str, str] = {}          # rid -> reviewer, for overturn counting
        self.n_events = 0
        self.rec = rec
        # economy counters
        self.c = {"posted": 0, "awarded": 0, "vested": 0, "final_n": 0, "false_approvals": 0, "false_rejections": 0,
                  "audits_rolled": 0, "audits_assigned": 0, "audit_unassignable_ticks": 0, "audits_lapsed": 0,
                  "challenges": 0, "rulings": 0, "rulings_wrong": 0, "reviews_unassignable_ticks": 0,
                  "awards_unfilled_ticks": 0, "appeals_unassignable_ticks": 0, "underfunded_careful_reviews": 0}
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
        out = []
        for aid in self.actors:
            ac = self.w.actor(aid)
            if not ac.on_duty and ac.committed is None and ac.open_review is None \
                    and self.w.unlocked(aid) + 1e-9 >= max(1.0, -(-self.p.G_frac * self.a.beta // 1)):
                out.append(aid)
        return out

    def eligible_reviewers(self, cid: str) -> list[str]:
        c = self.w.case(cid)
        out = []
        for aid in self.actors:
            ac = self.w.actor(aid)
            if ac.on_duty and ac.open_review is None and ac.committed is None and aid != c.actor \
                    and aid not in c.excluded and self.w.unlocked(aid) + 1e-9 >= c.G_V:
                out.append(aid)
        return out

    def select(self, offers: list[str]) -> str:
        """S_θ: score = ρ − λ·B/β with B = β; the κ tie band; then the lowest id."""
        lam, band = self.p.lam, self.p.band
        scored = [(self.w.actor(aid).rho - lam, aid) for aid in offers]
        best = max(s for s, _ in scored)
        tied = [aid for s, aid in scored if s >= best - band]
        return max(tied, key=lambda aid: (self.w.actor(aid).kappa, -int(aid[1:])))

    # -- one tick ----------------------------------------------------------------
    def tick(self, t: int):
        a, w = self.a, self.w
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
                break
            actor = self.select(offers)
            w.award(cid, actor, a.beta, a.work_ticks)
            self.tally[actor].awards += 1
            self.c["awarded"] += 1
        # actors work and submit
        for cid in list(self.active):
            c = w.case(cid)
            if c.state == "COMMITTED" and t >= c.t_award + a.work_ticks:
                w.submit(cid)
        # reviewers complete reviews assigned at an earlier tick
        for cid in list(self.active):
            c = w.case(cid)
            for rid in c.reviews:
                r = w.review(rid)
                if r.status == "open" and r.t_assign < t:
                    view = w.observe(r.reviewer, rid)
                    v, cost = self.verdict(r.reviewer, self.tasks[cid].fulfilled)
                    w.complete_review(rid, v, cost)
                    self.tally[r.reviewer].reviews += 1
                    if r.role == "audit":
                        self.tally[r.reviewer].audits_done += 1
        # actors respond to N: accept
        for cid in list(self.active):
            if w.case(cid).state == "AWAITING_RESPONSE":
                w.respond(cid, "accept")
        # orchestrator: initial reviews, audits, appeal reviews, rulings
        for cid in sorted(self.active, key=lambda s: int(s[1:])):
            c = w.case(cid)
            task = self.tasks[cid]
            if c.state == "SUBMITTED" and not any(w.review(r).status == "open" for r in c.reviews):
                el = self.eligible_reviewers(cid)
                if el:
                    rid = w.assign_initial(cid, self.rng.choice(el))
                    self.review_owner[rid] = w.review(rid).reviewer
                else:
                    self.c["reviews_unassignable_ticks"] += 1
            if c.state == "PENDING" and c.verdict == F and c.challenge is None:
                if not task.audit_rolled:
                    task.audit_rolled = True
                    initial = w.review(c.reviews[0])
                    self.c["audits_rolled"] += 1
                    task.audit_wanted = self.rng.random() < w.actor(initial.reviewer).p_audit
                if task.audit_wanted:
                    if t > c.window_end:
                        task.audit_wanted = False
                        self.c["audits_lapsed"] += 1
                    else:
                        el = self.eligible_reviewers(cid)
                        if el:
                            rid = w.assign_audit(cid, self.rng.choice(el))
                            self.review_owner[rid] = w.review(rid).reviewer
                            task.audit_wanted = False
                            self.c["audits_assigned"] += 1
                        else:
                            self.c["audit_unassignable_ticks"] += 1
            ch = c.challenge
            if ch and not ch["resolved"]:
                if not task.appeal_wanted:
                    task.appeal_wanted = True
                    self.c["challenges"] += 1
                done = [w.review(r) for r in ch["reviews"] if w.review(r).status == "done"]
                if len(ch["reviews"]) < 2:
                    el = self.eligible_reviewers(cid)
                    if el:
                        rid = w.assign_appeal(cid, self.rng.choice(el))
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
                elif e.kind == "fee_out" and e.note == "review fee":
                    ty.fees += e.amount
                elif e.kind in ("fee_out", "deposit_out") or (e.kind == "transfer" and e.src == "OMEGA"):
                    ty.reimbursed += e.amount
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
            if c.state in ("VESTED", "FINAL_N"):
                task = self.tasks[cid]
                correct = (c.outcome_or_verdict() == F) == task.fulfilled
                if c.state == "VESTED":
                    self.c["vested"] += 1
                    if not task.fulfilled:
                        self.c["false_approvals"] += 1
                else:
                    self.c["final_n"] += 1
                    if task.fulfilled:
                        self.c["false_rejections"] += 1
                if c.grade in self.by_grade:
                    self.by_grade[c.grade][0] += 1
                    self.by_grade[c.grade][1] += int(correct)
                for rid in c.reviews:
                    if w.review(rid).status == "overturned":
                        self.tally[w.review(rid).reviewer].overturned += 1
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
            })
        row.update(self.c)
        for g, (nn, ok) in self.by_grade.items():
            row[f"grade_{g}_n"] = nn
            row[f"grade_{g}_acc"] = round(ok / nn, 4) if nn else ""
        m = w.money()
        row.update({"M": round(m["M"], 3), "Res": round(m["Res"], 3), "v": round(m["v"], 6), "omega": round(m["omega"], 3),
                    "H_unlocked": round(w.unlocked("H"), 3), "active_cases": len(self.active)})
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
    ap.add_argument("--p-start", type=float, default=0.5)
    ap.add_argument("--gv", type=float, default=5.0, help="G^V, the reviewer bond")
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--res0", type=float, default=1e7)
    ap.add_argument("--human-budget", type=float, default=1e6)
    ap.add_argument("--record-dir", default=None)
    ap.add_argument("--log-every", type=int, default=10)
    ap.add_argument("--name", default=None)
    ap.add_argument("--expect-head", default=None)
    a = ap.parse_args(argv)

    name = a.name or f"stamping-s{a.stampers:g}-p{a.p_start:g}-gv{a.gv:g}-b{a.fail_rate:g}-seed{a.seed}"
    run = Stamping(a)
    rec = RunRecorder(name, kind="scoped run — §18.1 q1 careful vs careless review; policies fixed by disposition",
                      params=run.p,
                      declared={"actors": a.actors, "on_duty": a.on_duty, "ticks": a.ticks, "tasks_per_tick": a.tasks,
                                "beta": a.beta, "work_ticks": a.work_ticks, "seed": a.seed,
                                "dispositions": {"stamper_fraction": a.stampers,
                                                 "assignment": dict(sorted(run.kind.items())),
                                                 "careful": {"accuracy": a.accuracy, "cost": "uniform {2, 3} credits, or what unlocked "
                                                                                           "credit can buy (counted as underfunded)"},
                                                 "stamper": {"verdict": "F", "cost": 0}},
                                "task_world": {"fail_rate_b": a.fail_rate, "truth": "hidden, independent of actor"},
                                "orchestrator": {"selection": "argmax ρ − λB/β at B = β; κ tie band; lowest id",
                                                 "audit": "p_audit of the initial reviewer rolled once per F verdict; "
                                                          "auditor: seeded choice among eligible on-duty actors",
                                                 "ruling": f"by the truth with probability {a.ruling_accuracy}"},
                                "actors": {"offer": "B = β, τ = work_ticks", "respond_to_N": "accept", "spend": "none"},
                                "requester": {"H": "silent; posts tasks_per_tick per tick at β", "budget": a.human_budget},
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
              f"fees={final[kind + '_fees']:7.2f} costs={final[kind + '_costs']:6.2f} bonds_lost={final[kind + '_bonds_forfeited']:6.2f} "
              f"G_lost={final[kind + '_guarantees_forfeited']:6.2f} awards={final[kind + '_awards']:6.1f} "
              f"reviews={final[kind + '_reviews']:6.1f} overturned={final[kind + '_overturned']:5.2f} rho={final[kind + '_rho']:.3f} "
              f"p_audit={final[kind + '_p_audit']:.3f}")
    print(f"  posted={final['posted']} vested={final['vested']} final_N={final['final_n']} false_approvals={final['false_approvals']} "
          f"false_rejections={final['false_rejections']} audits rolled/assigned/lapsed={final['audits_rolled']}/{final['audits_assigned']}/"
          f"{final['audits_lapsed']} challenges={final['challenges']} rulings={final['rulings']} "
          f"reviews_unassignable_ticks={final['reviews_unassignable_ticks']} awards_unfilled_ticks={final['awards_unfilled_ticks']} "
          f"underfunded_careful_reviews={final['underfunded_careful_reviews']}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

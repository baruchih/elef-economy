# The learned red team — a brief

**Prepared:** October 20, 2026 · **Rules in force:** 2.5.0 (the consolidated account `economy-2x-consolidated-account.md` is the one-document summary; the specs and run records hold the full text) · **Tool:** the learned actors are to be built with **LeWorldModel** — a world model learned from what the public view shows, and a policy over the loop's public operations; its architecture is the implementer's and LeWorldModel's own documentation's, not this brief's · **For:** the implementer, who builds the learners as drivers; the design reviewer, who reads the results as runs 20 onward.

---

## 1. The question

**Is there a strategy that is unfaithful and still pays under these rules?** — being paid for work not done, or for verdicts not given, and ending richer than an honest actor who did the work.

Nineteen runs tested the rules against hand-written strategies: stampers who stamp everything, deliverers who fail at a fixed rate, lowballers, cyclers, cartels, patient customers. Every one of them was either caught by the record, priced by a rule, or found to be honest-but-ugly (the ratchet, patience). None of them *adapted*. The red team's job is to find out whether an actor that learns the rules from inside can do what none of the fixed dispositions could.

**What "beats honesty" means, in numbers.** A learned actor's **lifetime real wealth** over a run of 1,000 ticks — $W\cdot P_0/P_t$ at the end, counting every tick on probation or suspension — **above a careful actor's at the same cost and the same split**, averaged over the evaluation seeds, outside seed noise. Beside it, always: false approvals, suspensions and readmissions, the lagging auditor, the state's share — the cost of the strategy to the loop. A strategy that earns more for a while, is suspended twice and ends poorer has not beaten honesty. A strategy that earns the same as honesty while damaging the loop has not beaten it either, but is reported with its damage.

---

## 2. Ground rules

1. **The learner is a driver.** It uses only the public operations of `World` and reads only `drivers.view.Public` — nothing per actor, no record fields, no costs, no wallets but its own. It never drops the audit roll and reads `p_audit` honestly (spec §18.2). A learner that reaches past the view produces an implementation effect, not an economic one, and its result is discarded.
2. **The rules do not move during the red team.** Every question runs under 2.5.0 as consolidated; a red-team win is a finding for a design revision, drafted after the run as every revision has been, never a patch applied mid-study.
3. **The population is the environment.** One learned actor of one kind inside an otherwise hand-written population first — the honest 60/40 world with the pool of twenty (run 16's cell) unless a question says otherwise — then several of the kind, then a learned population. The cleanest signal first.
4. **Seeds.** Train on seeds 1–20, evaluate on 21–40, report both; the hand-written population on the same seeds is the control, as every run has had.
5. **Reproducibility as before.** Every run a folder with its manifest and metrics; the engine and driver commits recorded; the summariser named; every per-tick check and the final audit passed or the run is not reported.
6. **The learner is described in words.** For every question the report says, in plain language, *what the learner does* — when it cheats, what it reads, what it waits for — read from its behaviour, not its weights. A result nobody can describe is not a finding.

---

## 3. The learner

**Observation.** The public view at each tick (prices $P_t$, $\bar B$, the state's floor and price; members and free members; posts a tick; the state's share; time to membership; on-time share; the marks on its own requests) plus its own history (its awards, verdicts, audits received, outcomes, wallet, status — member, probationer, suspended). Nothing about any other actor by name.

**Actions, by the role the question gives it.** *A worker:* bid or not, at what price; deliver well or badly (the driver's quality dial — the deliverer's failure is a choice, not a rate); delegate or not, at what ceiling and deadline; cancel a child before its deadline or wait; enter or leave. *A reviewer:* the verdict on a case (approve / reject / partial / cannot assess) and how much care to spend (the care cost); appeal or not; the audit roll taken honestly. *A customer:* the ceiling, when to raise, when to withdraw, how many to hold open. *A parent:* judge the child's work, bond the rejection or not, cancel or wait.

**Reward.** Its own real wealth at the end of the run (the lifetime measure of §1); variants with a per-period reward are allowed and named. Nothing else — not the loop's honesty, not the price. The red team is adversarial by construction.

**Episodes.** A run of 1,000 ticks; the learner's identity persists through suspension and probation (it is one actor, like any member); departure and re-arrival are actions available to it under 2.3.0's rules (a fresh identity, no record, the float).

---

## 4. The questions, in order

### Q1 — The sleeper
*Setup:* one learned reviewer-worker in the honest population. *What it may find:* behave carefully until admitted and until the adaptive audit odds taper, then stamp (approve without care) exactly where the odds are lowest; take the suspension, serve probation, repeat. *Win:* lifetime real wealth above the careful's. *Read beside:* false approvals the sleeper passes before it is caught; the odds at which it chose to stamp; time between admissions. *What a win means:* the taper (§8.3) is too generous, and the number says by how much; the rules' answer would be in the odds' schedule, not in a new mechanism.

### Q2 — Can plants be told apart?
*Setup:* one learned reviewer, scored on **reviews only** (the reward is its review income less its forfeits), in a population where it receives plants at the ordinary rate. *What it may find:* any feature of the view, the timing, the case, or the dial's rhythm that separates planted cases from real ones; then pass every plant and stamp every real case. *Win:* a stamping rate on real cases well above its rate on plants, sustained, with the record passing. *Read beside:* the feature it uses (the implementer finds it by ablation — remove fields from the view until the separation vanishes). *What a win means:* **an emergency** — the gate is blind; the fix is in what the view and the plants' construction leak, and is drafted before anything else runs.

### Q3 — The selective cheat
*Setup:* one learned deliverer with the quality dial. *What it may find:* deliver bad work where it predicts it will not be caught — low audit odds, a stamper likely on the panel, a parent that approves — and good work otherwise. *Win:* lifetime real wealth above the careful deliverer's at the same cost. *Read beside:* its final-N rate against the honest's, the guarantees it forfeits, its reliability $\rho$ and what selection does with it. *What a win means:* the guarantee and the reliability score price bad work too cheaply at the margin the learner found.

### Q4 — Collusion through the blind view
*Setup:* two learned actors with a shared reward (a ring): a worker and a reviewer, in the honest population. *What they may find:* a way to recognize each other's cases through the blind view — by timing, by price, by anything — so the reviewer approves the worker's bad work. *Win:* the ring's joint lifetime wealth above two careful actors'. *Read beside:* the signal they use (ablation again); the panel's catch rate on the ring's cases. *What a win means:* §14's blindness leaks, and the leak is named.

### Q5 — The delegation chain
*Setup:* one learned child in a population with delegation at the wide spread (σ 0.8); then one learned parent (a broker). *What it may find:* how bad its work can be before a given parent catches it (run 19: an empty result passes 19% of parents); which parents to lowball; as a broker, which children to judge carefully. *Win:* lifetime wealth above an honest child's / parent's. *Read beside:* nested false approvals, forfeits, the parents' losses upstream. *What a win means:* the chain's price (the rejection bond, the child's guarantee, the parent's forfeit upstream) is wrong at the margin found.

### Q6 — Money games (lower priority)
*Setup:* one learned actor of any role with the index, the period boundary and issuance in its view. *What it may find:* timing postings, bonds or bids around the boundary to lock at a stale index; hoarding against the index's move. *Win:* real wealth above the honest's from timing alone. *What a win means:* the per-period index needs a smoothing or a lock-at-award rule.

### Q7 — The customer (lowest priority)
*Setup:* one learned requester maximizing tasks per credit. *Expected:* it rediscovers the floor and stops. Cheap; run it once.

---

## 5. The second track — stability under learned bidding (not the thesis)

Honest-but-ugly strategies are known: the members' ratchet (one award per 3.6 free member-ticks), the patient customer, the ceiling-aware child. The question here is not "does it pay" but **"is the market stable when everyone learns to bid"**: a learned population of honest workers and customers with the price as the reading — does it settle, oscillate, or collapse; where; and is the floor met. Run after Q1–Q5, as evaluations; nothing in it is a red-team win.

---

## 6. Reporting

Each question is a run in the established form — notes for the design reviewer: the cells, the seeds, the control, the tables, the reading, and *for the decision*. Each report answers, in this order: **did it win** (the numbers of §1); **what it does** (in words, §2.6); **what it cost the loop** (the readings beside); **what rule it points at**, if any. The design reviewer records each as `run-2N` in the project and drafts a revision only on a win.

---

## 7. Out of scope

Strategies that reach past the view; changes to the rules during the study; the real-work domain (q10, constructibility, is a domain question); the integration layer's problems (identity is free in the loop and priced outside it); human override (an assumption, not a question).

---

## 8. Order and stop rules

Q2 first, alone, before anything else is trained on top of it — if the gate is blind nothing else matters. Then Q1, Q3, Q4, Q5; Q6 and Q7 when convenient; the stability track last. A question stops when the learner's lifetime wealth is within seed noise of the careful's over the evaluation seeds after a training budget the implementer sets and records — that is a *no-win*, reported as such — or when it is above it, which is a win and goes to the design reviewer at once. A win on Q2 halts the study.

---

*The learners are LeWorldModel agents; the environment is the 2.5.0 engine through the drivers' conventions; the population is the hand-written one the runs have used since 1.x. What the red team finds, the rules answer — or they don't, and that is the finding.*

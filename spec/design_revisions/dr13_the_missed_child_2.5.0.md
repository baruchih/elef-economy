# Agentic Economics — The Task, Verification, and Dispute Loop

## Design revision 13 — specification 2.5.0-rc.2: the missed child

**Project:** ELEF / Agentic Economics  
**Version:** 2.5.0-rc.2 — a release candidate, not yet in force. rc.1 (October 19) was the sketch as first sent; rc.2 settles the implementation review [I28]: one correction of fact — the lapse at the deadline is what the engine has done since v1.0; the open door was the cancellation *at the deadline tick itself*, which the driver's step reaches before the engine's lapse — so the rule this revision adds is the **refusal**, and the lapse is stated as what already is; three readings taken into the text. On acceptance it becomes **2.5.0**, consolidated into one standalone text, and 2.4.0 moves to history.  
**Prepared:** October 19, 2026 (rc.1–rc.2)  
**Supersedes:** 2.4.0 where this document speaks — one rule, in §9.3 — and nowhere else.  
**Nature of this revision:** A **design revision** (minor, by §19), the smallest of the 2.x series. Run 18's last batch found the one thing the supply side left open: a child that bids below cost on a nested request and never delivers **risks nothing**. If the parent waits, the child's deadline lapses to a final $\mathsf N$ and its guarantee forfeits — but the parent has lost its own deadline by then (its guarantee and pots, about 16, against the child's 2.5). If the parent cancels at the child's deadline and self-executes in time — the right move, and the one the driver now makes — §9.3's cancellation *releases* the child's guarantee, because cancellation was written for a parent changing its mind, not for a child that did not show up. So the parent's roots are saved (568 failures against 675) and the child walks away whole: 131 misses a run, 131 cancellations, every guarantee released, the honest's loss closed from 4% to 3% and no further. The lapse itself — a child that reaches its deadline without submitting is final $\mathsf N$, its guarantee forfeits to the parent, the parent is free — has been the engine's since v1.0; what let the child go was a cancellation **at the deadline tick itself**, reached before the lapse. This revision closes that door: **cancellation is admissible only before the deadline; at or after it there is nothing to cancel.** One refusal.  
**Design assumptions, unchanged.**  
**Status:** Proposed. Accompanied by what required it (§1) and the runs that test it (§8).

> **One guarantee secures one obligation.** *(§9.2, v1.0)* **A missed deadline is the obligation unmet.** *(new)*

---

## 1. Why: what run 18's last batch said

1. **The lowballer's miss is free [S18 addendum].** With `--parent-cancel early` — a parent cancels a child that reached its deadline without submitting, after the tick's submissions, and self-executes — every one of 131 lowball awards a run is cancelled, every kill fee is zero (the child's recorded cost is nothing), **every guarantee is released**, the nested failures vanish (5 against 106), and the roots that waited no longer fail (568 against 675, below the base). The honest's loss closes from 4% to 3%; what remains is the parents' overhead on 299 nested postings — pots and fee locked, two ticks lost — against a child that risked nothing, and delegation held at 13% of awards because the parents' rule keeps seeing a cheap child that pays.
2. **The lapse is in force and the door is beside it.** §9.1 names "final $\mathsf N$ without a submission (a missed delivery)" as a terminal state, §9.2 forfeits the child's guarantee on it, and the engine has done exactly that since v1.0: at every tick, after the tick's submissions, a committed case past its deadline is final $\mathsf N$, the guarantee goes to the requester — the parent, for a nested case — the rejection bond is released, and the parent may submit from the next step. Run 18's no-cancellation cell shows it: 98.5 misses, 98.5 nested final $\mathsf N$, the guarantees forfeited. What let the child go was §9.3's cancellation — "after award and before $B$ submits" — used **at the deadline tick**: the driver's step at tick $d$ runs before the engine's lapse at $d$, the child is still committed at that instant, and `cancel_nested`, which checks only the state, releases what the lapse an instant later would have forfeited. Two paths from the same fact — no submission by the deadline — ended in different places for the child, one tick apart.
3. **The asymmetry named in 2.4.0 §2.4 [I26, S18 §6].** rc.2 of 2.4.0 called it exactly: "the cancellation closes the parent's loss entirely, at the price of the delay, and leaves the child's miss free … a lowballer risks nothing and costs its parent time," and named this revision's rule as the next candidate.

**Classification.** A design revision: one refusal in §9.3 — no cancellation at or after the deadline. The lapse, §9.1, §9.2, the kill fee before the deadline, the pool-exhaustion exit, and everything else stand. Minor, by the rule.

**Recorded and rejected.** *A nested guarantee floored to the parent's exposure*: changes the price of every nested bid, honest children's included, to catch a lowballer the lapse already catches once the lapse is immediate — held, with the reading of §8 to say whether 2.5 a miss is enough. *A kill fee floored above the recorded cost*: a fee is for work done; a miss is not work. *The parent's guarantee reduced when a child misses*: the parent chose the child; the customer did not. *Nothing — leave it to the driver*: the driver found the right move and the rule punished the wrong party for it.

---

## 2. The rule

### 2.1 No cancellation at or after the deadline

**The lapse, as it stands (stated, not new).** A nested request $q'$ awarded to $B$ whose deadline arrives without a submission is final $\mathsf N$ at that tick, after the tick's submissions have been read — a missed delivery, §9.1's terminal state. $B$'s guarantee forfeits to $A$ (§9.2); $A$'s rejection bond is released; $q'$'s pots settle at its closure as 2.3.0 has it; the milestone §9.1 requires is reached, and $A$ may submit from the next step. This is the engine's step after submissions since v1.0.

**Rule — cancellation is before the deadline only.** §9.3's cancellation — the kill fee of $\min(C_B,K)$, the guarantee and the bond released — is admissible **after award and before the earlier of $B$'s submission and $q'$'s deadline**: at tick $d$ the deadline has arrived, the window is the child's (it may still submit on its last tick), and there is nothing for the parent to cancel. A cancellation attempted at or after the deadline is **refused with no effect**. A parent that wants out must act by $d-1$.

**Consequence.** Two paths from one fact become one: a child that does not deliver by its deadline forfeits its guarantee, whether or not the parent wanted to go on waiting. A parent that cancels early — before the deadline, because it no longer needs the work, or because it has read the child's silence and will not wait — still pays the fee and releases the guarantee: that is the parent's choice and the child's protection. The lowballer's miss now costs it $G=\lceil0.5B'\rceil$ — about 2.5 on a bid of 5, half of what it was never going to earn and all of what it posted. Whether that is enough to make lowballing not pay is §8's reading.

**Consequence — honest children.** The deadline tick is the child's: it may submit on its last tick, and the refusal keeps a parent from pre-empting it there. A child that submits at its deadline submits before the lapse is read; nothing changes for it. A child that submits late has always been a missed delivery.

**Consequence — one step.** The parent self-executes from the step after the lapse, one driver step later than the cancellation-at-the-deadline it replaces; its room (work plus nested room, eight ticks against a child's two) carries it.

### 2.2 Defaults

| Default | Value | Note |
|---|---|---|
| The lapse | final $\mathsf N$ at the deadline tick after submissions; guarantee to the parent; bond released; the parent may submit from the next step | as the engine has had it since v1.0 |
| Cancellation | admissible before the earlier of the submission and the deadline; **refused at or after the deadline, no effect** | the one rule |
| `Params.missed_child` | on; off is 2.4.0 | one flag |
| Everything else | as 2.4.0 | |

---

## 3. Hypotheses

**Hypothesis 1 — the miss costs the child, and the parent's roots stay saved.** On run 18's lowballer cell (σ 0.8, 20% lowballers, the pool of twenty): about 130 lapses a run, as many guarantees of about 2.5 forfeited to the parents, every cancellation attempted at the deadline refused, the parents self-executing from the step after the lapse; root final N between run 18's 568 (cancel at the deadline) and 675 (no cancellation), nearer 568, the one-step difference; the lowballers' real wealth down by their forfeits (about 330 a run across the cohort); the honest's loss against the base closes from 3% toward 1–2% (the parents' overhead on the postings remains).

**Hypothesis 2 — honest children are untouched.** On the σ 0.8 delegation cell without lowballers: nested final N, vested, self-executed, the gain from trade, brokers and the honest's wealth within noise of run 18 (77 / 41 / 32 / 9 / 36; 1,304). No honest child lapses that submitted at its deadline.

**Hypothesis 3 — everything else is identical.** Every cell without delegation reproduces run 18 to the decimal; the goldens stand unless the equivalence scenario holds a nested lapse.

**Hypothesis 4 — the free miss is closed and the price of lowballing is read.** Delegation under the lowballers falls from 13% toward the base's 4% only if the parents' rule reads the child's forfeits (it does not — it reads the bid); so the reading is the lowballer's loss per miss, 2.5, against its nothing before. Whether 2.5 deters is a strategy's question; the rule's job is that the miss is not free.

---

## 4. What does not change

Everything in 2.4.0; §9.1 and §9.2 as written; §9.3's kill fee, cancellation before the deadline, self-execution and pool exhaustion as written. What changes is when a missed deadline becomes final and that no cancellation follows it.

---

## 5. Invariants, notation (amendments)

**I38 (new) — the missed child.** No cancelled nested case closed at or after its deadline; every committed nested case past its deadline is final $\mathsf N$ with its guarantee forfeited to the parent (the lapse's own check, stated); the parent may submit from the next step.
**I10, I19** as 2.3.0 has them (the pots settle at the node's closure; the lapse is a closure).

**Notation (Appendix C).** *A missed delivery* (§9.1) — now the lapse at the deadline tick.

**§18.1.** *Q21* (the chain under delegation): the lowballer's miss priced; the guarantee floor held as the next candidate if 2.5 does not deter.

---

## 6. Worked example

A parent with cost 14, awarded at 24 with a deadline at tick 40, posts a nested request at 9 with a deadline at tick 30; a lowballer with cost 10 bids 5 and wins, locking $G=3$. Tick 30: the tick's submissions are read — none from the child. The nested case is final $\mathsf N$: the 3 forfeits to the parent; the parent's rejection bond is released; the nested pots settle. The parent, free that tick, self-executes at 14 and submits by tick 40; its own case vests at 24. The parent's take: $24-14+3-$ the nested overhead (pots' net cost about 1.5, the fee on 5) $\approx11$, against 10 with no child at all and about 8 under 2.4.0's driver (the same self-execution, the overhead paid, the guarantee released). The lowballer's take: $-3$. Had the parent wanted out at tick 25, before the deadline, it would have cancelled under §9.3 as before — a fee of the child's recorded cost (zero), the guarantee released — and self-executed from tick 25: its choice, the child's protection. Had the child submitted at tick 30, the submission is read before the lapse and the parent judges it as §9.1 has it.

**An honest child with cost 3** bids 3.9 on the same request and submits at tick 28. Nothing in this revision touches it.

---

## 7. Implementation note (no code here)

- **One flag.** `Params.missed_child`; off is 2.4.0.
- **The refusal.** `cancel_nested` refuses when `t >= c.deadline` ("the deadline has arrived: the case is final $\mathsf N$ by the lapse, nothing to cancel"), whole-world snapshot unchanged; before the deadline, unchanged. The lapse (`advance`'s step after submissions: `_finalize_N` "delivery deadline missed", the guarantee to the requester, the bond released, the node closed, `_child_milestone_reached`) is as it stands.
- **The driver.** `--parent-cancel early` keeps its name and does nothing at the deadline: the engine lapses the child and the existing `FINAL_N → self-execute` path runs next step; `cancel_refused_at_deadline` counts a parent that tries. The pre-deadline cancellation stays as `on`.
- **Readings.** Lapses of nested cases (count, guarantees forfeited to parents), cancellations refused at the deadline, parents' self-executions after the lapse, the lowball children's wealth (a per-kind column), delegation share.
- **Tests.** `test_v25`: the refusal at and after the deadline with the snapshot; the cancellation before it unchanged (fee, release); a child submitting at its deadline tick before the lapse; the lapse forfeiting to the parent and releasing the bond with the parent submitting after; §6 in the six-actor world (the lowballer's $-3$, the parent's self-execution); the flag off admitting the cancellation at the deadline (2.4.0's behaviour). `EXPECTED_FAIL` 32 unless a reviewer test cancels at a deadline (none does on the implementer's reading of their timings). Goldens re-pinned once if the equivalence scenario's random cancellation lands at or after a deadline.

---

## 8. After acceptance — the runs

Against run 18's cells on the identical seeds; `missed_child` off is the control.

1. **Reproduce §6.**
2. **The lowballer cell** (σ 0.8, 20% lowballers, pool 20): lapses, forfeits, cancellations refused, root final N, the honest's and the lowballers' wealth (Hypotheses 1, 4).
3. **The honest delegation cell** (σ 0.8, no lowballers) and run 16's spread cells (Hypothesis 2).
4. **Everything else**: the 60/40 entry cell, the patient cell at the floor, the crowd with the pool — identical (Hypothesis 3).
5. **Red team**: a parent that posts nested requests with deadlines too short to meet, to farm honest children's guarantees (expected: the drivers' honest child reads the deadline and does not bid; if it bids, the forfeit is its own misjudgment and the parent's reliability carries the final N on its tree); a lowballer that submits an empty result at the deadline to avoid the lapse (expected: the parent rejects, the child's guarantee forfeits on the rejection as §9.2 has it, and the child may appeal against the parent's bond — the chain as run 16 read it).

---

## 9. Provenance

**[S18 addendum] Run 18's last batch** (October 19, 2026) — the kill fee with the parent cancelling at the child's deadline: 131 misses, 131 cancellations, every guarantee released, the roots saved (568), the honest's loss closed from 4% to 3% and no further; "the child's miss stays free"; the rule's answer named as the next candidate. **[I26] Review of 2.4.0-rc.1**: the kill fee is the child's recorded cost; a lowballer that never worked pays nothing and keeps its guarantee; "a guarantee not released on a cancellation the child's non-performance forced" named. **[C-2.5] Design discussion (October 19, 2026)**: the design reviewer — "cancelling a child that reached its deadline without submitting *is* that child's non-delivery — its guarantee forfeits to the parent, as on a failure, and the parent self-executes at once"; Baruchi: "ok, let's draft 2.5.0." **§9.1–9.3 (v1.0)** as the text this revision reconciles with itself. **[I28] Implementation review of rc.1 (October 19, 2026)** — implementable, with one correction of fact and three readings. The correction, adopted: the lapse is not new — the engine has finalized a committed case past its deadline, forfeited the guarantee to the requester and released the bond since v1.0, and run 18's no-cancellation cell showed it (98.5 misses, 98.5 final $\mathsf N$); the open door was the cancellation at the deadline tick, reached by the driver's step before the engine's lapse. §1.2 and §2.1 redrafted: the refusal is the rule, the lapse is stated. The readings, taken as written: the deadline tick is the child's (the submission window is inclusive; a parent that wants out acts by $d-1$); Hypothesis 1's roots between 568 and 675, nearer 568, the parent self-executing one step later than the cancellation it replaces; the goldens re-pinned once if the equivalence scenario's random cancellation lands at a deadline, `EXPECTED_FAIL` 32 on the reviewer tests' timings.

---

## Closing statement

> The rules always said a child that does not deliver forfeits its guarantee, and the engine always did it — one instant after the moment a parent could still cancel. In that instant a child that never showed up could be let go whole. Now the deadline tick is the child's alone: it may still deliver on its last tick, and if it does not, it owes what it posted. The parent is free the step after. One refusal; nothing else moves. It is the smallest revision in the series, and it closes the last door the supply side left open.

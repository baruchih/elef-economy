# Agentic Economics — The Task, Verification, and Dispute Loop

## Design revision 5 — specification 1.5.0-rc.2: the reserve is sized to the need

**Project:** ELEF / Agentic Economics  
**Version:** 1.5.0-rc.2 — a release candidate, not yet in force. rc.1 (October 17) was the proposal as first sent; rc.2 settles the six points of the implementation review [I12] — a peak holds until its period ends, and the period is one; a refusal is a refusal for funds; a case's demand is its unfilled seats; the refused cost is the amount the carry check refused; the §6 figures with a delivery's capital held to vesting; the §2.3 reading attributed by route and then by kind — and its smaller points. On acceptance it becomes **1.5.0**, consolidated into one standalone text, and 1.4.0 moves to history. Semver as before.  
**Prepared:** October 17, 2026 (rc.1 and rc.2)  
**Supersedes:** 1.4.0 where this document speaks; everywhere else 1.4.0 stands unchanged.  
**Nature of this revision:** A **design revision** under §19 — the fifth since the freeze, and the smallest: it changes **one rule**, what the duty fund's reserve measures. It adds no participant, no verdict, no challenge, no state. It also restates one hypothesis of revision 4 (text only) and adds one reading (a driver column, no rule). **Why minor:** the reserve's definition decides how many troops the fund can carry at once — behaviour, not wording — so it is not a patch; it changes nothing a member may do, so it is not a change of approach.  
**Design assumptions, unchanged:** humans do not intervene; troops bear no malicious intent.  
**Status:** Proposed. Accompanied by the evidence that required it (§1) and the runs that test it (§8).

> **The state has servers of its own. It uses as few as it can, for as short as it can, and says how many.**
>
> **The treasury keeps what the need requires, and pays out the rest.** *(new)*

---

## 1. Why: what run 6 found

Run 6 — 780 runs under 1.4.0, every final audit passed, truthful appeals and no disputes — established that troops do what revision 4 said and measured where the text was wrong [S6]:

1. **Troops supply the slowness.** Vesting is back at the 1.2.0 control at 50–70% and above it at 80% (2,376 against 2,024); at drift it doubles (3,621 against 1,856). The state's share reads the capture — 12 / 27 / 44 / 56% at 50–80%. False approvals fall below the controls at every split. Hypotheses 2 and 6 hold.
2. **Troops retract on their own.** Under adaptive dispositions the stamper share falls to ≤10% at the same tick as under 1.3.0 (900 against 870), troops are about 0.9 at a time through tick 1,000 and **zero from tick 1,500 in every seed**. Hypothesis 3 holds — minimization needs no hand.
3. **The reserve is self-limiting — by the accepted rule, implemented as written.** 1.4.0 §2.4 sizes $R_T$ to the peak capital troops *did* carry, and pays every batch's uplift from the unlocked balance above it. So the fund is drained to $R_T$ each tick, a summons needing more than $R_T$ is refused, and the peak can never rise: the fund refused 4,800–8,800 award summonses a run while paying 6,400–12,700 in uplift; at drift it refused 10,000–22,000. $A_T$ is not the binding constraint (300 against 100 cut refusals 4,832 → 1,640 and moved no delivery). Hypothesis 5 fails: **the treasury, not the market's need, set the state's share.** The decision of 1.4.0 §2.4 — the fund carries the troops first — was right; the formula meant to carry it out did the opposite.
4. **Troops consume member capacity.** Members' awards fall by a fifth to a half at 70–80%: every troop delivery is reviewed, most are audited, and that work keeps members on duty. Their wealth still rises — the gap widens by the uplift, 545–2,709 per careful actor — but it moves from awards to fees. Hypothesis 4 held in sign and failed in its clause; the clause was wrong, not the mechanism (§2.2).
5. **The ruling is not the residual leak.** Ruling accuracy 0.80 → 0.95 cut wrong rulings 34 → 9 at drift and 19 → 5 at the tipping cells, but probationers' false approvals fell only 62 → 52 ($m_{\max}=2$) and 22 → 16 ($m_{\max}=4$), not at all at 60/40 and 80/20, and false rejections fell by about as many — a wrong ruling cuts both ways. Most of what remains is **the audit itself**: the auditor of a pinned approval is whichever panel-eligible member or troop is free, and under drift a member whose record has not yet failed — a careful actor turned stamper, inside its detection lag — approves what the probationer approved. That is the lag of any record-based gate, not a rule defect; it is measured before anything moves (§2.3). The ruling's default does not move.
6. **The controls with the roll held barely moved** — the dropped audit hid almost nothing at $m_{\max}=4$, only run 5's $m_{\max}=2$ drift. The design reviewer's expectation at acceptance that they would worsen was wrong; the baseline is in place either way.

**Classification.** A design revision motivated by a strategy finding against one rule of revision 4. It changes what the reserve measures; it alters no settlement, verdict, challenge or membership rule.

**Recorded and rejected.** *Uplift paid only when the period's troop shortfall was zero* — the degenerate form of §2.1: it accumulates while short and pays out everything once served, so it would sawtooth with the period. *The raised tax split between reserve and uplift at a fixed ratio* — arbitrary, and blind to need. *A reserve that tracks the stock* (the maximum of the current demand and a decayed peak of refused demand) — more responsive, one more definition, and a decay rule the text would have to choose; not taken unless the §8 sweep shows the one-period retention costs something that matters. *Moving the ruling's default to $1-\varepsilon_T$* — the sweep did not earn it (§1.5); recorded as a default that may move later with evidence.

---

## 2. The rules

### 2.1 The reserve is sized to the attempted demand, and holds for the period

**Rule — demand.** At each seating step $s$ the **troop demand** is
$$D_s=\sum_{\text{troops holding a seat at }s}\text{capital held}\;+\;\sum_{\text{cases whose summons the fund could not carry at }s}\text{the capital the case's unfilled seats would have drawn},$$
where

- **"could not carry" means refused for funds** — the carry check's own refusal, the branch that counts troop shortfall. A request priced below $\bar B$ is the rule's own exclusion, a requester that cannot pay in is the market's refusal, a challenge path already full is not a need: none of these adds to demand.
- **a case's demand is its unfilled seats**: a delivery is one seat, an audit one, a challenge missing both panel seats two — $2\,(c_T+G^V)$. "Once per seating" is about ticks, not seats: a case refused at ten consecutive seatings adds its seats' cost to each of those ten stocks, never ten times to one. A case refused at $s$ and carried at $s+1$ appears in $D_s$ as refused cost and in $D_{s+1}$ as capital held; no stock counts it twice.
- **the refused cost is the amount the carry check refused** — the costs as they would have been purchased and posted at $s$: a delivery's $c^D_T$ plus its indexed guarantee $G=\max(1,\lceil G_{\text{frac}}\bar B\rceil)$, a seat's $c_T$ plus the case's indexed bond — not the Appendix A defaults.

**Rule — reserve.** The reserve is the **peak demand of the current period**: $R_T=\max_{s\in\text{period}}D_s$, where the period is the dial's (200 ticks or 50 adjudicated plants), and at the period's first seating the peak **starts at the demand then standing** — the capital of every troop still in the field plus whatever is refused at that seating — so there is no drop while troops are carried. The previous period does not enter. The uplift of 1.4.0 §2.4 is paid, as before, only from the fund's unlocked balance above $R_T$.

**Consequence — a peak holds.** The stock $D_s$ falls as the backlog is served; the reserve does not: it stands at the period's peak until the period ends, and comes down to the standing demand at the next boundary. The money returns to the reviewers **at the period's end**, not the moment the shortage passes. That retention — one period, the dial's own lag — is a feature: a fund that has just been short does not pay out the moment it is not. Until then the uplift resumes only when the balance has grown past the peak, which a self-financing ramp does within the period (§6).

**Consequence — the fund grows into the need.** A refusal raises the reserve by what was refused; the fund keeps its inflows instead of paying them out until it can carry the summonses that were made. Every troop seat is net-positive to the fund at the defaults (a review about $+2$, a delivery about $+4$ in expectation, $+10$ realised at a vesting), so a fund allowed to keep what it earns grows into the demand on its own; what bounds the state's share is then the market's unmet need and the fund's inflows, as 1.4.0 §2.4 intended. At rest, $D_s=0$ for a whole period, $R_T=0$, and the whole fund flows to the reviewers as in 1.3.0.

### 2.2 Hypothesis 4 of revision 4, restated (text only)

The honest keep their income; its composition shifts. A troop takes only what the market left, but what it delivers the market inspects — a probationer's initial review, a member's pinned audit — so as the state's share rises, members spend more of their time on duty and less delivering. Their wealth rises by the uplift; their awards fall, bounded by the duty cap, which keeps at least half of them free. A member whose award count fell while the state delivered is the mechanism; a member whose award was *taken by a troop it had offered for* would be the failure, and none was observed.

### 2.3 A reading: how a probationer's false approval reached the customer

**Reading, not rule.** For every probationer's false approval that vests, the drivers record **the route**: the pinned audit **upheld** it (the auditor missed), or the audit **rejected** it and **the ruling overturned** the rejection (the ruling erred — a sixth of the leak at drift in the sweep). For the first route they record **the auditor's kind at the time**: a **troop**; a **member never suspended** in the run; a **member suspended at a later tick** than the audit — inside its detection lag; a **member readmitted before** the audit. Attribution is after the run (a record that later fails is known only at the end); the driver holds every audit's reviewer id and sees every suspension. No engine change.

### 2.4 Defaults

| Default | Value | Note |
|---|---|---|
| $R_T$ | peak troop demand of the current period (§2.1), starting at the standing demand | replaces peak capital carried over a trailing window; the period is one |
| Everything else | as 1.4.0 §2.6 | $A_T=100$; ruling accuracy 0.80 (driver) — not moved |

---

## 3. Consequences and hypotheses

**Hypothesis 1 — the fund carries the need.** Refused award summonses fall from thousands a run to a ramp of a few tens of ticks and then near zero at 50–70%; the state's share rises to the unmet demand — at 60/40, from 27% toward the third of tasks the four free members cannot deliver; vesting rises with it. Uplift is zero while the fund accumulates toward a reserve of a few hundred and higher than run 6's once it is serving the backlog, because every carried delivery returns about $+10$ at its vesting. The retention lag shows as uplift paid late in each stressed period, not never.

**Hypothesis 2 — $w_A$ begins to matter.** In run 6 the award window barely moved anything because the fund, not the window, limited deliveries. With the fund sized to need, $w_A$ is the knob it was meant to be: shorter, more troops and faster service; longer, fewer troops and a longer customer wait.

**Hypothesis 3 — minimization still holds.** In the adaptive run troops still reach zero as the population turns honest; the reserve falls to zero one period after the last troop; the convergence tick is unchanged within noise.

**Hypothesis 4 — the auditor's lag.** Under drift, most probationers' false approvals travel the upheld route and are audited by members suspended later than the audit; under fixed splits, the upheld route with the auditor's $\varepsilon$ miss dominates and the overturned route is a sixth or less. If the lag dominates, a later revision may ask whether a pinned approval's auditor should itself have a *determined* record (as a newcomer's odds already require); that is not proposed here.

**Limit, restated.** A fund sized to need can grow; the state's share in a captured market will be larger than under 1.4.0, and the text accepts that — the share is the reading of the capture, and the market comes first at every seat.

---

## 4. What does not change

Everything in 1.4.0 not named above: troops and their summons, windows, the obligation, the fund's order of payment and the advance, membership, probation, the cap, plants, the dial, the pots, verdicts, challenges, $\rho$, $\kappa$, overrides, grades.

---

## 5. Invariants, notation (amendments)

**I23 (amended) — the fund.** $R_T$ is the peak troop demand of the current period — capital held plus the capital the fund-refused summonses' unfilled seats would have drawn, at the amounts the carry check refused, each case once per seating — starting at the standing demand at the period's first seating. **Checkable:** $R_T\ge$ the capital held by live troops, and $R_T\ge D_s$ at the last seating; uplift is paid only from the unlocked balance above $R_T$. $D_s$ and the pass's refused demand are world readings, so the predicate is over explicit state. All else as 1.4.0.

**Notation (Appendix C).** $D_s$ troop demand at seating $s$, with its two components, held and refused; $R_T$ redefined.

**§18.1.** *Q13* (the fund under troops) continues: where the fund fails to carry, with the reserve sized to need, and what one period's retention costs. *New Q14*: how a probationer's false approval reaches a customer — the route, and the auditor's kind on the upheld route.

---

## 6. Worked example

Twenty actors, 60/40, defaults, $m=2$, tick 500, inside a period that began at tick 400. Four free members deliver two tasks a tick; the third request each tick waits $w_A=2$ and is summoned for. A delivery troop's capital — $c^D_T=10$ purchased and $G=10$ locked, 20 in all — is held from the summons until the case **vests**: a tick or two to deliver, a tick to review, then the window $W=10$ — about thirteen ticks.

**Under 1.4.0.** The batch drains the fund's unlocked balance to $R_T$, which is the peak capital carried — near 50. At the next seating the fund can carry two deliveries and a review, no more; the rest of the waiting requests are refused, about nine a tick, every tick. Deliveries settle at about 0.8 a tick, which is what run 6 measured. The capital that two deliveries and a review hold is 48 at the seating; what thirteen ticks of carrying would hold is never reached, because the fund is never allowed to grow to it.

**Under 1.5.0, the ramp.** At the seating of tick 502 the demand is 48 carried plus three waiting requests refused at 20 each: $D_{502}=108$; $R_T$ rises to 108 and the uplift stops. The fund's unlocked balance grows by its net inflow — 3 of surcharge, plus about 30 returned at each vesting of a carried delivery (price 20, guarantee 10), less 20 drawn per new summons — roughly $+10$ a tick while it carries what it did. Within a few ticks it carries the backlog; from then on it summons one extra delivery a tick. Each adds 20 to the capital held for thirteen ticks, so $D_s$ climbs by about 20 a tick toward a steady $13\times20+8\approx270$, and $R_T$ climbs with it. During the climb the fund is cash-negative on the new cohort — 20 out now, 30 back thirteen ticks later — so its balance stays below the rising peak and no uplift is paid: that is the working capital the ramp needs, about 220, and the fund assembles it from its own retained inflows (Ω's advance covering the first ticks). By about tick 540 the first extra cohort is vesting: inflow about 33 a tick against 20 drawn, $+13$ a tick, and the unlocked balance crosses the peak of about 280–300 within a couple of dozen ticks more. **The uplift resumes, inside the period**, at about 16 a tick (13 of troop surplus and 3 of surcharge) — above run 6's 6–13 — because the fund is now serving a third of the market rather than a quarter of its need. Refusals: zero. The state's share: a third. The customer's wait at the award: $w_A$.

**At the boundary, tick 600.** $R_T$ restarts at the standing demand — about 270, every troop still in the field — not at zero; nothing drops while troops are carried. If demand had fallen meanwhile, the reserve follows it down here, one period after the fact.

**At rest (adaptive run, tick 1,600).** No troops for a whole period: $D_s=0$, $R_T=0$; the fund pays out everything, as 1.3.0 did.

---

## 7. Implementation note (no code here)

- **$D_s$** at the end of each summons pass: capital held by live troops (as `_troop_capital_now`) plus, over the distinct cases refused *for funds* in that pass, the `need` the carry check refused — summed over the case's unfilled seats (a panel short of both seats counts both, though the loop stops at the first refusal). **$R_T$** as the running maximum of $D_s$ over the current period, reset at the boundary to the $D_s$ of that seating; the previous period's peak dropped. The uplift check unchanged, against the new $R_T$.
- **Readings**: $D_s$ with its held and refused components, and $R_T$, as world readings; in the period record alongside `fund`, `fund_reserve`, `advance`, `troop_shortfall`, add the period's peak demand and its refused component, so the History shows how much of the reserve is need and how much is carrying. Driver: a `fund_reserve` column per tick for the $R_T$ trajectory; the route-and-kind attribution of §2.3 after the run.
- **Appendix I (consolidation).** The 1.4.0 engine computed $R_T$ over this period and the previous one; recorded there as the 1.4.0 reading, superseded by §2.1's one-period rule.
- **Tests**: `test_v15.py` — $R_T$ rises on a refusal for funds by the refused cost, once per seating; a price- or pay-in-excluded request and a full path add nothing; a challenge short of both panel seats adds two; **a refused summons carried at the next seating raises the peak once** (the stock moves from refused to held, the maximum does not double); no uplift while unlocked balance $\le R_T$; the peak holds within the period and resets to standing demand at the boundary; the §6 reproduction with the revised figures; rest returns $R_T$ to zero. `test_v14`'s $R_T=8$ for one seat with no refusal stands.
- **Goldens**: the History head re-pinned once at the implementing commit (uplift changes wherever a refusal occurred); no reviewer test reads $R_T$; no new expected failure expected.
- **Drivers for §8.6**: `--decline-awards <share>` — a member that offers for nothing and lives on fees and uplift; the requester flood is `--tasks-per-tick` raised, bounded by the requesters' wallets.
- **Defaults**: unchanged.

---

## 8. After acceptance — the runs

1. **Reproduce §6.**
2. **Tipping under 1.5.0** against run 6: refused summonses, state's share, vesting, members' awards, uplift paid and when in the period, $R_T$ and $D_s$ trajectories (Hypothesis 1; Q13).
3. **Windows** at 60/40: $w_A\in\{1,2,5\}$ — the knob now that the fund does not bind (Hypothesis 2).
4. **Adaptive**: convergence tick, troop-ticks to zero, $R_T$ to zero one period later (Hypothesis 3).
5. **Drift** $m_{\max}\in\{2,4\}$ with the route-and-kind reading (Hypothesis 4; Q14).
6. **Red team**: `--decline-awards` (expected: the decliner loses 20 an award and gains a fraction of 4); the requester flood (expected: served, paid for, fund grows, no exploit); the reformer and camouflage once more.

---

## 9. Provenance

**[S6] Run 6 (October 17, 2026)** — `agentic_sim/results/studies/1.4.0-troops/`, 780 runs, engine `f0779ac`; the ruling sweep, `ruling/`, 160 runs. **[I11]** The implementer's run-6 notes and ruling-sweep note: the reserve self-limiting under the accepted rule as written; members' awards falling; the ruling not the residual leak and the auditor-kind reading proposed; the case-ticks point adopted in §2.1. **[C-rev5] Design discussion (October 17, 2026).** The design reviewer proposed the reserve sized to attempted demand, Hypothesis 4 restated, and the ruling sweep before any default moved; the implementer ran the sweep first and declined the default move on its result. **[I12] Implementation review of rc.1 (October 17, 2026)** — six points, all adopted: a peak does not fall within its period (the consequence and §6 said it did; rc.2 keeps the peak and says so, and settles the period as one, starting at the standing demand — the reviewer's (a)); "refused" means refused for funds; a case's demand is its unfilled seats; the refused cost is the amount the carry check refused, at indexation; §6's capital figures revised for a delivery held to vesting (the 1.4.0 §6 figure of 48 had the same understatement); §2.3 attributed by route, then by four auditor kinds. Smaller points — I23 made checkable over explicit readings, the period record's two components, the carried-next-seating test, goldens, the red-team dispositions — adopted. Naming: in these texts "Claude" is the design reviewer and "the implementer" is the reviewer of the implementation; the run-6 record attributes the reserve rule and the controls expectation to the design reviewer, which is where they belong.

---

## Closing statement

> Revision 4 gave the state servers of its own and told the treasury to carry them first. Run 6 showed the treasury obeying the letter and starving the army: it kept only what it had once spent, and tipped out the rest. This revision tells it what to keep — enough for what was asked, held for the period in which it was asked — and leaves everything else where it was. The honest earn more and deliver less, which is what a market of inspectors looks like when the state does the work they could not get to. What still leaks is mostly the lag before a turncoat's record catches up with it; that is measured now, by route and by hand, and decided later.

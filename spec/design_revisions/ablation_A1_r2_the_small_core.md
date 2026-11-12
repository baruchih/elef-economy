# Ablation brief A1, revision 2 — the small core's arms

**Status:** candidate configurations for evaluation, **not in force**. No version number, nothing consolidated, no rule moved. Built behind flags and labelled as release candidates are. Adoption of any arm is a design revision drafted after the runs.  
**Date:** November 10, 2026 (r1 and r2) · **From:** the economy's reviewer · **Supersedes:** r1 of the same day.  
**What r2 settles:** the implementer's review against the engine at `2417219ba` (notes §78): eight corrections accepted (D1–D3, A1.1, A1.2, A2.1, A2.2, A3.1, A4.1, with A4.2 and A5.1–A5.3 noted); the four items put to the reviewer ruled (D4, C1, A1.3, Q1); hypothesis 1 restated, because its second clause was wrong; two arms and two pinned cells added, on the arithmetic of §2.  
**Addenda 1–9** (November 10–12: after the payoff table; after the scripted sweep and the panel check; B5 amended before its cells; the dial's clock; after the learned chains; after E3 and the stressed world's first read; after Baruchi's rulings of November 11–12; after the stake reads; after the entry test) are at the end. Nothing in §1–§9 is changed by them except §7.3, which gains two chains (B3, D3) and one evaluation (D2); addendum 6 sets the order from here, addendum 7 amends its item 2, addendum 8 sets two reads, and addendum 9 rules on them and sets the next two.  
**Rulebook in force:** 2.9.0 with the consolidated defaults.

## 1. The question

Run 34 found that a population stamps the seats past the first review. 2.8.0 and 2.9.0 answered by sending the orchestrator's truth to those seats as plants. The other answer was never tried: give those seats to the orchestrator. This brief sets the answers side by side, on what leaks and what it costs.

Arms 2–4 run against a standing design position — the troops minimized. They are measurements of what that position costs or saves, not proposals.

## 2. The arithmetic the arms are built on

At any seat, in an inspector's own money and with care reimbursed:

- an inspector that **checks** is punished for its own mistakes — about ε = 5 in 100 verdicts, each caught nearly surely when it is a rejection of good work;
- an inspector that **stamps** is punished only when a bad case *whose truth is checked* arrives at that seat: a bad plant, a planted approval. A stamp on bad real work is a confirmation, and a confirmation is checked by nobody.

With equal penalties for both kinds of error the stake cancels, and **checking pays only if truth-checked bad cases at the seat are more frequent than the inspector's own mistakes**:

  share of truth-checked bad cases at the seat × (penalty for a miss) > ε × (penalty for a false alarm) + any real cost of checking

Read against the record: the first review meets a bad plant about 15 times in 100 against 5 — checked. The 2.7.0 audit seat met none — stamped nineteen in twenty. At 2.9.0 the dial held planted approvals at 4–5 in 100 of the members' audit seats, on the line — stamped about half the time. The implementer's own point (a careful review's 5% error is what checking costs) is this inequality's right-hand side.

Three ways to satisfy it at a later seat, and the brief tests all three: **more stings** (arm 0 with its own lever pinned above the line); **a cheaper false alarm** (arm 1c, which lowers the line); **the orchestrator's seat** (arms 2–4, which remove the member from it). A bigger bond does not appear: it multiplies both sides, and helps only against a real cost of checking once the line is cleared.

## 3. One definition used by every arm

**The deciding verdict.** The orchestrator's own verdict on a real case: two seats of its own inspectors; if they agree, that is the verdict; if they differ, a third decides.
- Each seat is a troop's Review on the summons road, seated in the tick's pass without the w_R wait or the free-member test, and answered by the driver at the next tick's reviews as every troop's is; a third seat on a split is seated the tick after the two answer. I8 admits these positions beyond V_max under the flag.
- Wrong about 0.7 times in 100 at ε_T = 0.05; step 5's shared difficulty reaches it through the driver's verdict.
- **Its money (D4, ruled):** the pots as they are — nothing minted, nothing topped up. Each seat's cost c_T is reimbursed from the root's expense allowance while it lasts, up to K a seat; what the allowance does not cover is the orchestrator's own cost, read apart. **The deciding verdict's seats take no fee** (a system review with no fee, as 2.9.0's plant reviewer is), so no member's fee is diluted by them and the pot's remainder returns to the requester as leftovers do. If the settlement makes "no fee" costly to build, the fallback is members first and the state's seats from the remainder.
- Its seats lock a bond as a troop's seat does and are never overturned; a split's minority seat stands.
- Never taken on a plant, whose truth is known; never taken on the orchestrator's own delivery (§5).

## 4. The arms

**Arm 0 — 2.9.0 as in force.** The reference. With it, two cells of its own lever pinned above the line — planted approvals at **0.10** and **0.20** per real approval a member audits, the dial's other multipliers live — as evaluations under fixed rules.

**Arm 1 — the trusted ruling** (`trusted_ruling`).
- An audit that disagrees with the verdict it audits opens the challenge record as today (kind `audit`, the audit its first review) and seats no member's third seat: the deciding verdict is taken and settles it (`by = deciding verdict`). The driver's ruling is never sought.
- An appeal or dispute panel sits as today (two fresh members). **A member panel confirms or escalates; it never overturns**: if both confirm the standing verdict it stands as today; otherwise the deciding verdict is taken and is the outcome. This is a change from today's rule, where two agreeing panelists settle either way.
- A member's review is overturned — bond burned, as today — only if its verdict differs from the deciding verdict or from a plant's truth. A member that matches the deciding verdict stands and is paid. The court fee by the outcome, as today. Plants unchanged.
- The ⊥ objection path and the human's override are untouched and unmeasured.

**Arm 1b — the sampled confirmation** (arm 1 + `sampled_confirmation`, r = 0.25). (Q1, ruled: yes.) A confirming member audit, and a confirming member panel, on a member's delivery is sampled to the deciding verdict at rate r; where the deciding verdict differs, the confirming members are overturned and the outcome is the deciding verdict's. Expected by §2 to price a confirmation only where bad work is common at the seat (its share above ε / r) and not to hold an honest population's audit seat; built to test that.

**Arm 1c — the cheaper false alarm** (arm 1 + `lenient_false_alarm`). At an audit or panel seat, a member whose **rejection** is overruled — by the deciding verdict or by a plant's truth — forfeits its fee and keeps its bond — the review overturned as today in every other respect (its odds, its reliability, its record's entry); a member whose **approval** is overruled forfeits the bond as today. By §2 the line falls from about 5 stings in 100 to about 2, under where 2.9.0's dial already sits.

**Arm 2 — the state's audit** (arm 1 + `state_audit`).
- Every audit obligation on a member's approval of a member's delivery — the pinned reviewers' included — is taken by one seat of the orchestrator's own inspectors in the tick's pass; `assign_audit` refuses a member on such a case. If it agrees the approval stands; if it differs it is the deciding verdict's first seat and the verdict is completed. That audit seat earns the audit's fee as a troop's audit seat does today; the seats added to complete a verdict take none.
- `planted_approval` off (its base is zero by construction). A plant's audit obligation is discharged at once with no seat: under arm 2 the plants test the first review and the panels.

**Arm 3 — the state's bench** (arm 1 + `state_bench`).
- An appeal and a dispute on a member's delivery are decided by the deciding verdict, seated at the filing's pass. No member panel. The fee by the outcome; a dispute's settlement discharges a standing obligation as it does today.
- Plants file no challenge — the truthful ones as well as the lies (`planted_lie` off does not cover the first). Under arm 3 the plants test the first review and the audit seat.

**Arm 4 — the small core** (arms 1 + 2 + 3). Members hold initial reviews (and resumed reviews, which no population has yet produced). `plants_every_seat` **stays on**, so that 2.8.0's roll at the verdict's odds is not reverted; arms 2 and 3 make a plant's later seats vacuous, and the plant closes at its first verdict.

**Arm 5 — no plants** (second wave; a text only if arm 4 reads well). The implementer's three corrections stand for that text: the record's entries mapped from the state's adjudications (an agreeing state audit is one seat at ε_T, not the deciding verdict; the good-work window fills from appeals alone); admission restated on n_min adjudications of bad work; F* restated for the statistic the audits give.

**Defaults swept under the implementer's step 3, not arms:** the ruling's accuracy on arm 0 (0.8 / 0.95 / 1.0) and the bond at the audit and panel seats (×2, ×4) — the second expected by §2 to change nothing where care is reimbursed.

## 5. Two rulings every arm shares

**The orchestrator's own work (A1.3, ruled: exempt, in every arm).** The orchestrator does not judge its own work. Its own deliveries are judged as 2.9.0 has it in every arm — a member's audit, a member's panel, the ruling as today, Appendix V's second reading as it stands; I25 unchanged. Under arms 2–4 the audit and the panel of the orchestrator's own deliveries are therefore the only member seats past the first review; no plant reaches them; **their blind-verdict rate and the orchestrator's bad work standing are read, and nothing is added to price them.**

**The roster (C1, ruled: exclude).** Under `state_audit` and `state_bench` the reserve's target and the member seats are sized without the demand the orchestrator carries; the roster's size is read in every arm.

## 6. Readings, every arm and population

- **The payoff table first, with no learner**: on the scripted eps population, own money by action and seat — inspect, approve blind, reject blind — as reviewer 1 measured it, with the share of truth-checked bad cases at each seat beside. This is §2 measured instead of assumed, and it is read before any chain is trained.
- **The leak**: bad paid work over all paid work (vested roots), and over all bad deliveries; by channel, with the new channel "escalated, deciding verdict" and, apart, the orchestrator's own bad work standing.
- **The overhead per delivered task**, two views: the customer's cost beyond the price (pots consumed less the closure refund, the service fee, court fees less refunds, less rebates); and the system's verification consumption — care at every seat, the orchestrator's c_T in full with its unreimbursed part apart, the cost of truth, and each plant's own awarded price as its shadow cost. Each also as a share of the price.
- **The state**: seats by kind, share of all review seats, peak seats per tick, Ω's net and debt.
- **The members**: fee income by seat kind, nominal and real surplus, members alive, the roster's size.
- **False penalties**: bonds burned on reviews whose verdict equals the task's truth, by seat kind.
- Challenges filed and won by the challenge's truth; time from submission to vesting (median, 90th percentile); the customers' tasks per 1,000; P_t; every invariant.

## 7. Populations and order

1. **The payoff table** for arms 0 (floor, and pinned at 0.10 and 0.20), 1, 1b, 1c.
2. **Scripted**, seeds 21–40 paired against arm 0: all-careful with arrivals; the 60/40 entry cell; fixed 60/40; entry with truthful disputes; entry with liars at 0.1. Arms 1, 1b, 1c, 2, 3, 4.
3. **Learned on own money**, the earnings predictor, careful start first: arm 0 pinned at 0.10; arm 1c; arm 4 — against run 42. The stamper start for whichever hold. Arm 1 alone only if the table surprises.
4. **The stressed world** that steps 3–5 define: arms 0, 1c and 4, scripted then learned.

## 8. Hypotheses, stated before the runs

1. **Arm 1** cuts the bonds burned on correct member verdicts by peers' error — the two-wrong-peers overturn and the ruling's — and the leak does not rise. **It does not lower the audit seat's blind-verdict rate**: the price of checking at that seat is the inspector's own false rejections, which a more accurate judge punishes more surely (from about 0.8 to 0.99 of them); the edge moves by a few hundredths of a credit, against checking if anything. (r1 said the rate would fall; that was wrong. A correct rejection is burned about one time in ten in the careful basin today, as the implementer notes, not one in five.)
2. **Arm 0 pinned** at 0.10 and 0.20: the audit seat's blind-verdict rate falls below 0.15 on the learned population — the seat closes on 2.9.0's own lever once it is held above the line; the cost of truth rises with the stings.
3. **Arm 1c** closes the audit seat at 2.9.0's present dial (blind verdicts below 0.15) without more stings; blind rejections do not appear (an overruled rejection still loses its fee).
4. **Arm 1b** prices a confirmation in the stamper-heavy scripted cells and not in the careful ones, by ε / r.
5. **Arm 2**: the member-confirmed channel is zero by construction on members' work; the total leak at or below arm 0's in every population; the members' income falls by their audit fees and the orchestrator's rises by the same; its cost is its c_T — about 2,900 a run in the hand's world.
6. **Arm 3**: a lying challenge is paid at the deciding verdict's error (under one in a hundred), a truthful one won 99 in 100.
7. **Arm 4**: the leak near the careful reference in every population, the learned ones from both starts; the customer's cost unchanged or lower; the orchestrator's share of review seats from about a tenth to about a third.
8. **In the stressed world** the member's audit seat costs far more to hold than the orchestrator's: by §2, against a real cost of checking the stake needed grows as that cost over (stings − ε), and arm 4's advantage over arms 0 and 1c widens.

**What would refute the review.** If arm 4 does not hold the leak at or below arm 0's, or its system overhead — the orchestrator's seats at cost — is above arm 0's and arm 1c's, the members' later seats are load-bearing and cheaper, and the plants were the better answer to run 34. **What would refute §2:** the pinned cells leave the audit seat stamped, or arm 1c does. Either is recorded as plainly as the other.

## 9. Invariants under the flags

I8 admits the deciding verdict's positions under `trusted_ruling`. Under `trusted_ruling`: no member review is overturned except by a plant's truth or a deciding verdict, and no ruling is recorded on a member's delivery (the orchestrator's own deliveries keep the ruling). Under `state_audit`: no member audit review exists on a member's delivery, and every such obligation is discharged by a state seat. Under `state_bench`: no member review of role `appeal` on a member's delivery. Under `lenient_false_alarm`: no bond is burned on an overruled rejection at an audit or panel seat. I25 unchanged in every arm; I20 live with `plants_every_seat` on; I43–I44 vacuous where their flags are off.

---

## Addendum 1 to revision 2 — after the payoff table

*November 10, 2026. Read at `ce0694775` (the payoff table, notes §80) and `e781edc0f` (both blind verdicts' edges, every arm and seat). §1–§9 stand as built at `24490af3b`: no arm, flag or hypothesis is changed. Added here: what the table measured; one guard; a drafting point on arm 1c's panels and how it is decided; readings with two counters; and what the reviewer expects of the chains, stated after the table and before any of them.*

### A1. §2, measured

The audit seat on the scripted eps population, in an inspector's own money: a blind approval's edge over inspecting, in credits an audit.

| Cell | Blind approval − inspecting |
|---|---|
| Arm 0 at its dial (3.8 truth-checked bad cases in 100) | +0.02 ± 0.06 |
| Arm 0, the lever pinned at 0.10 | −0.62 |
| Arm 0, the lever pinned at 0.20 | −1.33 |
| Arm 1 | +0.19 |
| Arm 1b | −0.02 |
| Arm 1c | −0.13 |

- §2's inequality is the money's own account: on the line at 2.9.0's dial, under it at the pins. 2.9.0's half-stamped audit seat is the line.
- Arm 1 moves the edge against checking, as hypothesis 1 (restated) says — by 0.17, not "a few hundredths": the sign was right, the size understated.
- Arm 1b returns the seat to the line and no further, as §4 expected of it.
- Arm 1c is under the line at the present dial, by about a fifth of the 0.10 pin's margin.

### A2. The guard: both blind verdicts, every seat

Each arm's row carries the blind approval's and the blind rejection's edge over inspecting at every seat. At the audit seat a blind rejection reads −6.51 ± 0.10 under arm 0 and −4.64 ± 0.09 under arm 1c. (The "−1.93 → +0.36" first reported was that action's own money in absolute credits, not its edge.) Arm 1c does not open the blind rejection at the audit seat; **hypothesis 3 stands as written and arm 1c is as written.** The bounty form drafted in case — an upheld rejection earning the overturned review's bond — is withdrawn unbuilt.

Before any arm's chain is trained its row is reported beside arm 0's, with any blind verdict that pays under the arm and not under arm 0 flagged. The member seats on the orchestrator's own deliveries under arms 2–4 are expected to show it and are read as §5 rules; any other waits for a word.

### A3. Arm 1c at the panels — a drafting point, the reviewer's

§4 gives the lenience to an overruled **rejection** "at an audit or panel seat". At the audit seat and at the dispute panel a rejection is the verdict that disagrees with the standing one — the alarm the arm is named for. **At the appeal panel a rejection is the confirming verdict.** There the lenience cheapens what the arm means to keep dear: a blind confirmation of a wrong rejection, priced since 2.8.0 by the truthful planted appeal and by a careful partner's disagreement, falls from bond and fee to the fee. At the dispute panel the lenience is on the alarm, as meant, and about halves what 2.9.0's planted lying dispute costs a blind uphold; under arm 1 an uphold only escalates, so what that can add is the state's seats and a panel's fee paid for nothing, not a wrong outcome. Neither pays bad work. The first can let a panel wave away an honest worker's appeal more cheaply.

Not rebuilt on reasoning. The appeal panel's and the dispute panel's rows are read under arms 0, 1 and 1c before arm 1c's chain: **if under arm 1c a blind verdict at either panel is at or above inspecting, within the spread, where under arm 1 it is clearly below, arm 1c's chain runs with the lenience at the audit seat only** — the seat hypothesis 3 is about — and its scripted cells are re-read under that scope. Otherwise as built. If the arm is ever drafted as a rule, its text gives the lenience to the verdict that disagrees with the standing one, at every seat.

### A4. Readings added to §6, and two counters

- **Latency:** the escalation's tick, and a split's two.
- **The state's cost under arm 2:** its own-error verdicts (about 30 a run), with the false overturns the second seat prevented counted.
- **Arm 1b:** the round spent by a sampled confirmation that stands, with the disputes refused for it counted.
- **Every learned chain:** the first review's blind-verdict rate beside the audit seat's — what a seat the plants have always priced looks like to the same learner.

The two counts are built as counters before the ablation's chains start.

### A5. What the reviewer expects of the chains, stated before them

1. **The order.** On the learned population the audit seat's blind-verdict rate follows the table's edge: arm 0 at its dial highest, arm 1c under it, the pin at 0.10 under that, the pin at 0.20 lowest.
2. **Arm 1c's margin.** On own money this learner has turned an edge of +0.36 into 94–97 blind verdicts in 100 (2.7.0's audit seat) and one of +0.01 to +0.02 into 41–56 (2.9.0's). By those two points an edge of −0.13 gives about a quarter. The reviewer therefore expects **hypothesis 3's threshold (below 0.15) to be missed** — the seat between a quarter and arm 0's rate — **and hypothesis 2's to be met** at the pins. Hypothesis 3 is left as written and is refuted as written if so.
3. **The refuter of §2, amended before any chain, and marked as an amendment.** §8 named arm 1c beside the pins before its margin was known. §2 is refuted if the order of (1) is broken beyond the seeds' spread, or if the pins leave the audit seat no better than arm 0's. Arm 1c leaving the seat above 0.15 and under arm 0's rate refutes hypothesis 3 and not §2: the lenience lowers the line and, at this dial, not far enough alone.

---

## Addendum 2 to revision 2 — after the scripted sweep and the panel check

*November 10, 2026. Read at `80fbec3df` (§7.2: 1,100 scripted runs, notes §81), `5233e468d` (I45 scoped) and `daaadd578` (the panels by their question). No arm or flag is changed. Ruled here: the ruling's default; hypothesis 1 in two parts; one chain added to §7.3; arm 1c at the panels; one watch item for the detection sweep; I45. The sweep's figures are in the run record, "Ablation A1 — first reads".*

### B1. The ruling's default: 0.8 stays for every cell of record

The sweep puts 2.9.0's false penalties on the driver's ruling: at an accuracy of 1.0 they fall from 20 / 12 to 4 / 0 a run in every cell with no arm. The default is **not moved** — for the owed cells, for arm 0 and its pins, and for the learned chains:

- it is the world every run on record was read in, run 42 — the chains' reference — included; it was swept at 1.5.0 and left; and the rulebook is frozen while the ablation runs;
- 0.95 or 1.0 is not a default to move to: the driver's ruling is drawn, not seated, and an accurate ruling at no cost is free truth. What an accurate ruling costs is what arm 1 pays — 240 deciding verdicts and 940 of c_T a run.

What changes is the reading. **False penalties are reported by source** — the ruling's error, two wrong peers, the deciding verdict's error — and the swept cells (0.95, 1.0) stay beside arm 0's. **The ruling seated only where it is sought today** (one troop's seat at 0.95, or the deciding verdict) is costed from the swept cells and the count of rulings a run, with no build, beside arm 1's 240 verdicts. Who rules, and at what cost, is for the design revision after the runs.

### B2. Hypothesis 1, in two parts

It stands on the scripted cells (false penalties −18 / −11 a run, of 20 / 12; the leak does not rise) and is recorded as two effects: **the judge's accuracy**, which carries most of it and needs no restructuring of the members' seats; and **the structure** — a panel that confirms or escalates — which removes the two-wrong-peers overturn, about 4 a run.

### B3. §7.3 gains one chain: arm 2 on the learned population

Hypothesis 5 says "every population", and §7.3 set no learned chain for it. Added after arm 1c's: **arm 2, the earnings predictor, careful start** (the stamper start if it holds). Arm 2 is the lighter of the two state arms — the orchestrator takes the audits and nothing else — and the one in which the members' panels still have to hold. Order of the learned chains: arm 0 pinned at 0.10; arm 4; arm 1c; arm 2. Every learned chain's note carries the system's overhead a task beside the leak, so that the pins (+2.4 / +4.5 a task on the scripted cells), the lenience, and the state's seats (−0.7 / −1.4) are read on both together.

### B4. Arm 1c at the panels: the condition of A3 is not met

- **Appeal panel.** Both blind verdicts are clearly under inspecting in every arm. The blind confirmation reads −5.03 ± 0.41 under arm 1 and −2.50 ± 0.17 under arm 1c: the lenience is worth half of its price, as A3 said, and it is still 2.5 under.
- **Dispute panel, the blind rejection** (siding with the dispute): −5.09 ± 0.22 under arm 1c, halved from −10.13 and still 5 under.
- **Dispute panel, the blind confirmation** of the standing approval: at inspecting under arm 0 (+0.13 ± 0.54) and arm 1c (+0.46 ± 0.25) alike; arm 1's −2.06 ± 2.26 is one seed's lump on 170 decisions. The lenience does not touch a confirmation; this is the world's composition (B5).

**Arm 1c runs as built.** The drafting point of A3 stands for any later text.

### B5. The dispute panel's confirmation — a watch item, stated before the detection sweep

In run 24's world no customer disputes, so every dispute is a planted lie on a good plant and the standing approval is always right: at the dispute panel a blind confirmation is at inspecting **in every arm, arm 0 included**. Harmless there — no truthful dispute exists to be waved away. The suspicion it raises, to be tested and not built on: **where customers dispute rarely, a panel taught by planted lies confirms blind, two confirmations stand unchecked, and the rare truthful dispute is lost** — under arms 0, 1 and 2 alike, whose dispute panels are members'; not under arms 3 and 4. The planted lie prices siding with a dispute; it also fills the panel with cases on which confirming is right.

- Read now, from data on disk: the dispute panel's blind-confirmation rate in run 42's finals.
- Read in the implementer's step 4 (the customer's detection swept from 0 to 1) and in §7.4: truthful disputes won, by the customer's detection, on the learned population. **Expected:** far under the scripted figure at low detection under arms 0, 1 and 2; 99 in 100 under arms 3 and 4. **Refuted** if at a detection of 0.25 the learned dispute panel inspects and truthful disputes are won at the scripted rate.

### B6. I45

Scoped as the implementer has it: the deciding verdict's seats are never overturned; a troop's ordinary seat is overturned as today.

---

## Addendum 3 to revision 2 — B5 amended before its cells

*November 10, 2026. Read at `8929a6304` (notes §82) and `a45201457` (notes §83). The frozen evaluation of B5's suspicion is running; the retrained cells are not. The expectation for the retrained cells is amended here, before them, because the panel's composition is now known. Marked as an amendment.*

### C1. What is now known

- **The first half of B5 is shown.** On run 42's population (the round-10 collection) the dispute panel confirms blind 0.787 ± 0.045 on 187 decisions, every one a planted lie, and inspects 0.17. No truthful dispute was lost there, because none exists there.
- **The engine, confirmed by the implementer.** The truthful planted dispute follows the real requesters' rate on a wrongly approved bad plant and is zero where none disputes; the planted lie comes at the dial's floor. In the careful basin the dispute panel sees lies only.
- **A second point.** The liar chain's panel is 28 in 100 truthful, half of those on bad plants; its population inspects 0.90 on both kinds and confirms blind 0.055 / 0.048. The two kinds are not told apart.

### C2. The line at this seat, by §2

A blind confirmation is punished on a truthful dispute whose truth is checked — surely on a plant, and through the partner's disagreement and the ruling otherwise. Inspecting is punished for its own mistakes, ε. So the panel looks where truthful disputes are a large enough share of what it sees, and the line is a truthful share of roughly one in twenty to one in eight, by the start and by the plants' share of the truthful disputes.

### C3. The expectations, the second one amended

With T the truthful disputes a run at a detection of 1 (the customers' and the plants') and L the lies a run, the truthful share at a detection d is d·T / (d·T + L). The floor's lies are few, so the share is large at any moderate detection.

1. **The frozen evaluation (unchanged, running).** Run 42's policy at a detection of 0.1 and 0.25 wins under a half of the customers' truthful disputes — about three in ten — against more than nine in ten for the scripted careful population. Read on the customers' disputes; the plants' apart. Refuted above eight in ten.
2. **The retrained cells (amended).** At a detection of 0.25 the retrained population's dispute panel **inspects** and truthful disputes are won near the scripted rate; at 0.1 probably the same. B5 expected the opposite at low detection and named 0.25 in its refuter; with the composition known, the reviewer expects that refuter to be met. A capture in a retrained population, if there is one, lies under the detection d* at which the truthful share falls to the line of C2. d* is stated from T and L before those cells run, and the sweep takes points on both sides of it.
3. **What would then remain of B5.** A population taught where nobody disputes loses the first disputes it meets (1); and the customers' dispute is void where disputes are rarer than d*.

The candidates of the run record stand for a later draft, none drafted: the planted challenge in both truths at the dial's rate; the sampled confirmation; the state's bench.

### C4. The frozen evaluation, read (`26c8fd367`, notes §84)

C1–C3 were written before this result reached the reviewer.

- Run 42's policy, frozen, at a detection of 0.1 / 0.25 wins truthful disputes 0.72 / 0.70 (4.1 / 11.0 filed a run; 1.2 / 3.3 lost a run, with the court fee each), against the scripted careful population's 0.97 / 0.99 and the hand's 0.98 / 0.96.
- **The expectation of C3.1 (under a half, about three in ten) is missed on this figure; its refuter (above eight in ten) is not met.** The trained population loses about three truthful disputes in ten where a careful one loses one to three in a hundred.
- **One split is open, and the expectation was about the customers' disputes:** how many of those filed are the customers' and how many the plants', and whether a plant's truthful dispute is settled by the panel's verdicts or by its truth. By the standing false approvals (about 16 a run) the customers would file about 1.6 / 4.1 of the 4.1 / 11.0; if the rest are the plants' and are settled by truth, the losses are all the customers' and their rate is about a quarter. Recorded when the split is read.
- At these detections the customers' disputes hardly move the standing false approvals (16.3 a run at none; 14.7 / 15.4), still +7.6 / +8.8 over the hand's, and the audit seat is blind 0.52–0.54. The leak remains the audit seat's.
- The result gives T of C3: about 42 truthful disputes a run at a detection of 1. L, the floor's lies a run, places d*.

### C5. The split, d*, and what the next read separates (the implementer's reply to C4)

- **The split.** The driver counts the plants' disputes apart: the 4.1 / 11.0 filed and the 2.95 / 7.7 won are the customers' alone, and a plant's truthful dispute settles by its truth, never by the panel's verdicts. The customers lose 28–30 truthful disputes in 100. The alternative reading of C4 (about a quarter won) is withdrawn. **The expectation of C3.1 is missed as stated: seven in ten won, not three.** Its refuter (above eight in ten) is not met.
- **d\*.** L is the floor, about 10 lies a run (two a period, five periods); T about 42. d* is 0.012 at a line of one in twenty and 0.034 at one in eight. The truthful share the panel saw in the frozen cells was about 0.42 at 0.1 and 0.62 at 0.25.
- **The retrained cells, ordered by what they decide.** After the ablation's chains: run 42's final policy as the start — its dispute panel is the captured start — at a detection of 0.25, then 0.1, read beside the frozen figures. One point under d* (0.01) last, and only if the machine is free: at that rate a customer files fewer than one dispute in two runs, and the loss is small whatever the panel does. This replaces "points on both sides" of C3.2.
- **Why seven in ten and not three — what the next read separates.** The reviewer's three in ten assumed two members' seats at the round-10 collection's rate. Seven in ten needs each seat to confirm a truthful dispute about 0.44 of the time. Three ways that can be: the orchestrator's inspectors hold part of those seats; the members confirm blind far more on the planted lies than on the customers' disputes in the same cell — a tell; or the final policy's own rate is lower than the collection's. The panel's actions by the dispute's truth, its owner and the seat's holder separate them. **If it is the second, the tell is found before anything else is read on the panels.**

### C6. The panel, read; and the standing points (notes §85–§86; `077e6d4b6`, `73231d019`, `77226f959`, `235ed2b96`)

- **Which of C5's three ways.** The first and the third, not the second. The orchestrator's inspectors hold 39 in 100 of the panel seats in the learned population at both detections (27 in the careful's and the hand's). There is no tell: the members confirm blind the customers' truthful disputes 0.62 / 0.69 and the planted lies 0.61 / 0.69. The final policy's rate is 0.65 / 0.70, under the collection's 0.79.
- **By the panel's make-up**, the customers' truthful disputes won at a detection of 0.1 / 0.25: two members 0.44 / 0.23; one of each 0.89 / 0.82; two of the orchestrator's 1.00 / 0.98. Three in ten is what two members win; seven in ten is the orchestrator's seats.
- **Why the orchestrator sits: the tier.** A free member was kept off the panel tier at all but 0.5 / 0.1 of the 263 / 276 unfilled seat-ticks a run; the learned population has 29 panel-ineligible member-periods a run more than the careful's 63, by its members' own records. 2.9.0's price on the audit seat does not deter this learner, which cannot perceive eligibility; it filters.
- **One read asked.** On the two-member panels, the joint of the two verdicts on a truthful dispute — both confirm, split, both reject — against the product of the single-seat rates. Two members win 0.23 at 0.25 where independent seats would win about 0.43; if they confirm together it is the one shared policy making the same choice on the same case, recorded as correlated verdicts already in the population.
- **The retrained cells** (C5's order) are read by the panel's make-up as well, with the orchestrator's share of the panel seats beside the members' own rate.
- **Provenance, standing from here.** Every collection on record is made by a script kept in the repo, and its note names the script and the commit. The probe collections of notes §53 and §57 were made by a script not kept; nothing is re-made for them — both are the shared-purse cells', and the owed §8.4 re-reads the probe on own-name credit. No read on record was taken through a fresh fit where a frozen policy was meant (confirmed by the implementer).
- **Readings noted for the design revision, no arm.** One seat of the orchestrator's on a panel is worth most of two; the careful population's 27 in 100 is the tier's own cost — the undetermined kept off the panel in a population that fails no plant.

---

## Addendum 4 to revision 2 — the dial's clock, and two cells added under arm 0

*November 10, 2026, evening. Read at `f4b59c233` (the addendum of notes §88), notes §89–§90 as summarised, and `73e8097df`. Notes §88 itself — the owed cells' finals — has not reached the reviewer; the cap cell is ruled when it does. No rule, arm or flag of the rulebook is changed. Added: what is now known of the dial in the cells of record; one evaluation and one chain under arm 0, both harness options; their expectations, stated before them.*

### D1. What is now known

- **A run starts its dials at the floor and lasts five periods.** In run 42 m^A is first fed at the fourth close and doubles at each close after: 1 → 1 → 1.15 → 2.30 → 4.37, ending at 4.8 / 3.8 (π^A 0.095 / 0.076) — a quarter of the way to the cap as the run ends. The hand's stays at 1 (its failure estimate 0.03–0.09). The liar chain's is never fed: every planted approval is disputed before its audit.
- **So every 2.9.0 cell on record has read the lever mostly at its floor**, reaching the line's neighbourhood only as the run ends. The half-stamped audit seat is that reading. A run that begins with a cold dial is the harness's assumption — each run a newborn economy — and not the rulebook's. (The reviewer's guess that the dial never left 1 was wrong; it is fed late.)
- **§8.7's floor cell** pinned π_t, which run 42 never moves, and so reproduced run 42 to the decimal. It is recorded as that, and not as the cell 2.9.0's §8.7 named (m^A at 1). That cell is closed without a chain: run 42, three periods of five at the floor, is its reading to within the last two periods' climb.
- **§8.5's first half:** the deliverer unmoved; the CEM on the expected line (−695 ± 282, its audit seats 211 → 57); the line planner −65 ± 323. Notes §58's −1,012 returns at the old roll defaults on the corrected engine (−673 ± 318): what took the stamp away is the consolidated roll defaults of the reviewer's fourth ruling, not a correction of the plants' path. (§58's 0.22 / 0.16 was a per-seed mean; pooled 0.100 / 0.098, now 0.065 / 0.077.)
- **§8.4 on own money** (notes §90, as summarised): the probe blind at the audit seat, at its floor at the initial seat, and the panel's gap the question's base rate whole. No tell at any seat.

### D2. An evaluation: the frozen policy in a long run (the reviewer's word given)

Run 42's policy, frozen, in runs of 2,000 ticks. It reads the climb directly and what the tiers do at full length. It does not read whether a population that learns closes the seat itself.

**Expected.** Against a population that does not adapt, the dial reaches the cap by about the eighth close. Every member stamps about half its stings, so the members' records fail across the population and they leave the tier; the orchestrator takes the audit seats they lose, as it took the panel seats in the frozen dispute cells. By the last quarter of the run the orchestrator holds more than half of the audit seats on members' work and the member-confirmed channel is under half of run 42's: **2.9.0, left to run against a population that does not learn, moves the audit seat to the state by itself.** Refuted if the members keep most of the audit seats at the cap, or the member-confirmed channel stays at run 42's.

Read by quarter of the run: each dial's path; the audit seats by holder; the panel- and duty-ineligible member-periods; the channel split; the cost of truth; the members' fee income and the members alive.

### D3. A chain: arm 0 with the dials carried

A harness option, no rule: each run of a round starts its dials where the runs of the round before ended (all four dials; the carry rule the implementer's, stated in the note). From run 42's final policy; the stamper start if it holds. It is 2.9.0 as written in an economy that does not restart, and it is the reference the ablation's arms should be set against.

**Expected.** Once carried, the dial climbs past the line and the audit seat's blind-verdict rate falls below 0.15 in the rounds where π^A is above about 0.08. The dial then comes down by its slow step and settles, or cycles, in a band of π^A between about 0.05 and 0.2. Over the chain's last three rounds the blind-verdict rate averages under 0.25 and the standing false approvals are within 4 a run of the hand's; the cost of truth rises by about the 0.10 pin's on the scripted read (+2.4 a task) or less. **Refuted** if the audit seat stays above 0.3 in rounds with the dial above 0.10, or the dial runs to the cap and stays there.

If this holds, 2.9.0 as written closes the audit seat by its own dial, the finals of record under-read it for the cold dial, and the ablation's question becomes which is cheaper — the dial's stings or the state's seat — and no longer whether the seat can be closed.

### D4. Order of the learned chains

Arm 0 pinned at 0.10; arm 0 with the dials carried; arm 4; arm 1c; arm 2. The frozen long evaluation whenever the machine has a gap; it trains nothing.

---

## Addendum 5 to revision 2 — after the learned chains

*November 11, 2026. Read at `4cd513fc4`, `171fec881` and `d4a2a4344` and the summaries of notes §91–§95; the figures are in the run record, "Ablation A1 — the learned chains". No rule, arm or flag is changed. Here: the reads against what was stated; what they say of 2.9.0's own lever; and the reads from here, with their expectations.*

### E1. Against what was stated

- **Hypothesis 2** met by the head alone (0.080), at the threshold by the direct (0.151); the leak 11 / 8 per thousand bad deliveries against arm 0's 31 / 19; one basin from both starts. The policies of record carry no exploration, so 0.080 is one audit in twelve answered blind and not a closed seat.
- **Hypothesis 3** refuted as written (0.348 / 0.290; the leak 23 / 14); no blind rejections. **The order of A5.1 holds**, and §2 stands on it.
- **Hypothesis 5** met on the leak (8.8 / 6.2), the overhead 9.9 / 9.7, the panels the members' and holding at run 42's rate; the orchestrator on 45 in 100 of the review seats.
- **Hypothesis 7** met by the head alone, missed by the direct (10 against the careful's 5), the excess two thirds the roll's floor and a third ε_T; the lowest overhead (9.7 / 9.4); one basin. The review's refuter is not met.
- **D3** (the dials carried): the audit seat closed (0.020 / 0.006 at π^A 0.16–0.28) and the leak the lowest of any cell (6) — met. **Its cost missed by a wide margin**: 20.9 / 19.5 a task, about twice the pin's, where the reviewer stated the pin's or less. The dials did not settle in the band stated: the rounds' exploration held them near the cap (π_t 0.30, m^A 13–17). Under the policies of record the dial falls a tenth at nearly every close, toward its own target — a seat answered blind about one time in twenty.
- **D2, read down.** The head alone's closed seat in the long run is its policy turning to inspecting along its own record, past the range it was fit on, and not the dial. It is not evidence of the dial; D3 is. The price read there stands: 25.0 a task at m^A 8.3.

### E2. What the reads say of 2.9.0's own lever

The planted approval's floor (π^A_0 = 0.02, the reviewer's default) sits under the line of §2. From a floor under the line the lever either reads its floor (the cold start on record) or, carried, overshoots to twice the price. Held at 0.10 it cuts the leak by two thirds at 11.4 / 11.6 a task. **A floor above the line is a default and not a rule, and the cell that measures it is the pin's, already on record.** Not moved now; it is the tests road's candidate for the ruling after the runs.

### E3. The reads from here

1. **The 0.20 pin's chain**, owed under hypothesis 2. With the 0.10 pin it brackets where a dial whose floor is 0.10 would move — one audit in twenty answered blind lies between the two — and prices it. **Expected:** the audit seat under 0.05 blind, the leak 6–9 per thousand bad deliveries, the system's overhead about 2 a task over the 0.10 pin's. Refuted if the seat stays above 0.10 blind at 0.20.
2. **Arm 2's stamper start**: the basin test, owed for what holds.
3. **Arm 2's policies, frozen, at a detection of 0.1 and 0.25**: the customers' truthful disputes won by the panel's make-up, and the orchestrator's share of the panel seats, beside arm 0's 0.72 / 0.70 and 39 in 100. Under arm 2 no planted approval fails a member at the audit seat, so the tier no longer moves members off the panel. **Expected:** the orchestrator's share of the panel seats falls toward the careful's 27 in 100. Whether the customers' disputes then hold on the members' own care is the read; no direction is claimed.
4. **The retrained dispute cells** of C5 (0.25, then 0.1, from run 42's final policy).
5. **Not run:** the frozen 2,000-tick read on D3's policies. The direct is valid to tick 1,000 and the head alone extrapolates along its record; and where a frozen policy lets the dial fall is not where a population that keeps learning leaves it. The two pins bracket it.

Then the stressed world of the implementer's steps 3–5 on the finalists: arm 0 with the planted approval's floor at 0.10, arm 2, arm 4.

---

## Addendum 6 to revision 2 — after E3 and the stressed world's first read

*November 11, 2026, evening. Read from the notes themselves, §88–§103 at `11b17d000` — the file reached the reviewer today; everything before this was read from summaries. No rule, arm or flag is changed. Here: E3 against what was stated; the stressed world at a temptation of 1; what the two days' reads say of the member's audit seat; and the order from here, with expectations.*

### F1. E3 against what was stated

- **E3.1, the 0.20 pin:** met by the head alone (0.021 blind), at the line by the direct (0.054); the leak 8 / 6 per thousand bad deliveries; the overhead +2.3 a task over the 0.10 pin's (13.7 / 13.9). Not refuted. The blind verdict that remains moves to the panels and turns to a rejection.
- **E3.2:** arm 2 is one basin from both starts; only the panels move, a point and a half.
- **E3.3:** the tier part met — under arm 2 the members no longer lose the panel tier. **The state's share of the panel seats is refuted as stated**: it rises (0.48 / 0.45 against run 42's 0.39 / 0.43), by composition — the third seats go to the deciding verdict and the state's seats past w_R stay. The read itself: the customers' disputes do not hold on the direct's own care under arm 2 (two learned members win one in four; 0.77 / 0.68 overall), and do on the head alone's (0.98 / 1.00). The leak is the state's audit's whatever the panel does.
- **E3.4 (C3.2 as amended):** met at both detections — two learned members win the customer's truthful dispute 0.97 at a quarter and 0.95 at a tenth. **Not foreseen:** the retrained population stamps the audit seat more (+0.154 at a quarter, +0.079 at a tenth), because a dispute discharges a planted approval before its audit and the seat meets fewer of them — §2 again. The standing false approvals fall at a quarter (15.4 → 10.8 / 9.9) and not at a tenth. With the liar chain's audit seat (blind 0.93 / 0.95 where every approval is disputed first, and paid 4,000 a run) it is one reading: **2.9.0's lever on the audit seat weakens as the customers look more.**
- **The owed cells of 2.9.0** (notes §88), now read: π_t at its cap closes the audit seat to 0.21 / 0.18 at 23.4 / 22.7 a task; the half reads 0.34 / 0.24. Across every learned cell the seat's blind rate follows the truth-checked bad share at the seat — §2 on the learned populations.

### F2. The stressed world at a temptation of 1 and the bond ×1 (notes §97, §99, §102)

| | The pin (π^A 0.10) | Arm 2 | Arm 4 |
|---|---|---|---|
| Claimed at the first review | 0.29 / 0.25 | 0.27 / 0.24 | 0.25 / 0.22 |
| Claimed at a member's audit seat | 0.94 / 0.99 | 0.99 / 1.00 (the state's own work only) | 0.99 / 1.00 (the same) |
| Leak per thousand bad deliveries (unstressed) | 67 / 64 (11 / 8) | 22 / 22 (9 / 6) | 19 / 18 (10 / 6) |
| System overhead a task (unstressed) | 16.4 / 17.0 (11.4 / 11.6) | 16.9 / 17.0 (9.9 / 9.7) | 16.5 / 16.2 (9.7 / 9.4) |

- **Hypothesis 8 is met on the leak** — from parity to three times apart — **and not on the cost**: every finalist at 16–17 a task, the suspensions' churn and the thinned population.
- A member's audit seat is claimed nearly whole wherever a member holds one. The first review is claimed one time in four in every finalist, where the table reads a coin. The panels hold best.
- No finalist holds the careful's leak. Every learned population ends poorer than the careful's with the private benefit counted.
- Read with its limits: the learners credit one decision at a time; the construction is the harness's and is off in every run of record.

### F3. What the two days' reads say of the member's audit seat

In every world read, the member's audit of a member's work is the seat that fails: half-stamped at the dial's floor; held only by stings that cost 2 to 4 a task and more; stamped more where customers dispute; stamped nineteen in twenty where every approval is disputed; claimed whole under a temptation of 1, at every bond read. The orchestrator's audit holds the leak at 6–9 per thousand bad deliveries at the lowest overhead unstressed, from both starts, and at a third of the pin's under the temptation.

**The reviewer's recommendation, for Baruchi's decision and against a standing design position: the audit of a member's work is the orchestrator's.** Its price as measured: the orchestrator on 45 in 100 of the review seats where it sat 18; the members' surplus a fifth to a quarter lower; about three slots in twenty-three fewer alive. Nothing is drafted until he rules.

### F4. The order from here — the reviewer's call

1. **Trap or equilibrium** (frozen policies, no training; first). On each finalist at a temptation of 1: the stressed policy of record on half the slots and the careful on the other half, in one world. Read by half: the slots' real lifetime with the private benefit counted, the suspensions, the seats held. **Expected:** the careful half ends ahead of the claiming half by more than 1,500 real a slot in every finalist — a claim is worth 2–3 real and a suspension a tenth of a run. If so, the claim's basin is the short-sighted learner's, a member that counted its own suspensions would not enter it, and the learner's horizon (the implementer's step 7) is read before any stake is drafted on the learned chains. **Refuted** if the claiming half is level or ahead: then the claim pays the member that makes it and only the stake answers it.
2. **The stake at every member seat** — G_V ×2 and ×4, the first review's bond with it (the later seats' multiple at 1) — at a temptation of 1 and 2. The payoff table first, on the three finalists. **Expected:** the first review's claim edge falls 0.3–0.5 real a multiple; at a temptation of 1 it is under −1 at ×4 in every finalist; at 2 it stays open at ×4. Then one learned chain each on arms 4 and 2 at a temptation of 1 and the multiple the table says closes the first review by more than 1 real. **Expected there:** the first review claimed under 0.10, the leak within one and a half times the unstressed, the suspensions under 10 a run. Read beside, because the stake is paid by the honest too: the careful population's surplus and false penalties, the members' idle-for-bond time, the underfunded reviews, the slots alive.
3. **The joint-verdict read at ρ 0.5** on the scripted populations, beside the others; it trains nothing.
4. **Not run:** the dial under the temptation (a claimed seat reads F̂^A near 0.8 and sends the dial to the cap, where the seat is at best a coin at more than twice the overhead); further learned chains on the pin (its audit seat pays the claim at every bond read); learned chains at a temptation of 2 until the table names a stake that closes it; 2.9.0 §8.7's m^A-at-1 cell, closed in addendum 4.

**Two readings asked:** the orchestrator's own bad work standing a run under the temptation — §5 left the member's audit of the orchestrator's own deliveries unpriced, and it is now claimed whole while the orchestrator delivers 4 to 7 in 100 of the awards; and the private benefit a slot, by policy.

---

## Addendum 7 to revision 2 — after Baruchi's rulings of November 11–12

*November 12, 2026. No note is read here. This addendum follows the owner's rulings on the staged loop: the life-cycle map of the real loop, revision 9, and "The economy's answer to the life-cycle map, revision 9", third edition, section 12. No rule, arm or flag of record is changed, and nothing is drafted: the rulebook stays 2.9.0 and frozen, and no 3.0.0 is written before the loop's first experiment on inspection plans reports. Here: the rulings that bear on the simulation; cells added to F4.2's table; one learned chain; what stands; and the limits.*

### G1. The rulings that bear on the simulation

- **F3's recommendation is not adopted.** The orchestrator stays minimal. Its inspectors are the last word on a difference, an appeal, a dispute and a ruling on cause — arm 1's deciding verdict — and not the routine audit of members' work. Arms 2 and 4 stay on record as what the orchestrator's audit holds and costs.
- **The audit of a member's approval is a premium member's seat**: earned by record, tested by planted approvals at a rate above the line of §2, better paid, and carrying a stake that is felt at once. Its nearest cell in this instrument is arm 0 with π^A pinned: gated by θ_panel, at a weight of 1.5.
- **Money and marks move on trusted truth only.** A difference between two members is a signal. Here that is arm 1's rule, on record.
- **A reviewer is paid a fixed fee for each recorded act, and its own cost never enters.** It then carries the cost of its care itself, so skipping saves exactly that cost. **The stressed world at a temptation of 1 is therefore the base case for the staged loop. The world of record — care reimbursed, nothing saved by skipping — is the special case.** No cell of record is relabelled; the stressed cells are read with this in mind.
- **No number that moves money comes from the side it pays.** In this instrument the stressed world's fourth action is that hole: an allowance paid on the reviewer's own claim.
- **Reviewing stays a duty of every member that takes work**, as 1.2.0, 1.3.0 and 2.7.0 have it. One addition for the staged loop, not built here: repeated no-shows bar a member from new awards, as a failed plant record does.
- **The way of working:** the simulation with the implementer and the loop's own experiments run in parallel, and the two are merged from time to time.

### G2. Cells added to F4.2's payoff table — the premium seat's stake

On the scripted ε population of §99, arm 0 with π^A pinned, the member-held audit seat. §99 read its claim edge at π^A 0.10: +1.94 at ×1, +1.38 at ×2 and +0.81 at ×4 at a temptation of 1; +4.48, +4.52 and +3.35 at 2. Added:

| Dimension | Values |
|---|---|
| The bond at the audit and panel seats | ×6, ×8 |
| π^A, pinned | 0.10, 0.20 |
| The audit seat's role weight | 1.5 (of record), 3 |
| The temptation | 1, 2 |

Sixteen cells; and beside them π^A 0.20 at ×1 and ×4 with the weight at 1.5, for the slope. The first review's bond as §99 had it. If the weight is not exposed as an option, it is a harness option, off in every run of record; say so before running.

**Read, in each cell:** the two edges against inspecting at the audit seat and at the panels, as §99; the truth-checked bad share at the seat; and, because the honest pay the stake too, the careful population's false penalties by seat, its surplus, its idle-for-bond time, the underfunded reviews, the slots alive, and the orchestrator's share of the audit seats.

**Expected**, from §99's own slope (the stamp's edge at the seat is about 0.7 real plus 0.3 real a multiple at a truth-checked bad share of 0.11, and both parts follow that share):

- a temptation of 1, π^A 0.10: the claim's edge +0.1 ± 0.4 at ×6 and −0.6 ± 0.4 at ×8;
- a temptation of 1, π^A 0.20: about +1.2 at ×1, −0.5 at ×4, −1.6 at ×6 and −2.7 at ×8, each ± 0.5;
- a temptation of 2: open at π^A 0.10 at every bond (above +1.5); at π^A 0.20 about +1.4 at ×6 and on the line at ×8;
- the weight at 3 lowers the edge by about 0.2 at π^A 0.10 and 0.3 at 0.20, small beside the bond's part;
- the careful population's false penalties at the audit seat unchanged in count and larger by the multiple.

**Refuted** if the edge at π^A 0.10 is still above +0.5 at ×8, or already under −1 at ×6; or if doubling π^A does not about double the bond's part.

### G3. One learned chain, after the table

On arm 0 with π^A pinned, at a temptation of 1, at the cheapest added cell where the table reads the audit seat's claim edge under −1, with the first review's bond at the multiple F4.2's table names. The recipe of §102: the careful start, ten rounds, the finals on seeds 21–40 with the careful, the stamper, the claimer and the hand on the same slots. **It takes the place of arm 2's chain in F4.2. Arm 4's stays as stated, as the reference.** If arm 2's chain is already running or read, it stays on record and this one is added. F4.4's "no further learned chains on the pin" is lifted for this chain alone.

**Expected:** the member audit seat claimed under 0.10, from 0.94–0.99; the first review claimed under 0.10; the leak within one and a half times the unstressed pin's 11 / 8; the suspensions under 10 a run; the system's overhead under the stressed pin's 16.4 / 17.0 and above the unstressed 11.4 / 11.6.

**Refuted** if the audit seat is still claimed above 0.3 at a cell the table read closed by more than 1 real. Then the table does not carry to a learning population at this seat, as the first review's coin did not (§102), and the size of a stake is not to be read from tables.

Read beside it: what the stake costs the honest, as in G2; how many members hold the audit seat, and the orchestrator's share of it.

### G4. What stands

F4.1, trap or equilibrium, first and as stated; it now also says whether a seat worth keeping is felt at all by these learners. F4.2's table and arm 4's chain. F4.3. The two readings asked. Every collection's note names its script and commit.

### G5. Limits, stated before the cells

- The premium idea has two ingredients this instrument does not hold: choosing the better members, and a seat worth keeping. Every learner shares one policy and credits one decision at a time. Those two are the loop's to test, in its experiment on second opinions, and here they are the implementer's steps 6 and 7, which this addendum does not order.
- The cells read a stake. They do not read a premium population.
- A harness construction, off in every run of record.

---

## Addendum 8 to revision 2 — after the trap, the stake's table and the two chains

*November 12, 2026. Read: notes §104–§108 at `2dbf303b0`, in full. The record of them is "Ablation A1 — the stake reads: the trap, the stake's table, the premium seat's chain". No rule, arm or flag of record is changed, and nothing is drafted. Here: the rulings on the notes; the reviewer's misses; two reads without training; and what is not ordered.*

### H1. Rulings on the notes

- **§104** is accepted. `--w-audit` is a harness option on a parameter of record, 1.5 in every run of record.
- **F4.1 is not refuted.** The careful half ends ahead of the claiming half in every finalist on both learners, by 434–737 real a slot. Its stated consequence stands: the learner's horizon is read before any stake is drafted on learned chains. Nothing is being drafted.
- **G2 is not refuted**, and its sizes at π^A 0.20, at a temptation of 2 and for the weight were understated by the reviewer's arithmetic.
- **F4.2:** met at a temptation of 1; refuted at 2, where the first review closes at ×4 in every finalist.
- **G3 is not refuted by the letter and is not a success.** The audit seat is claimed 0.25 / 0.13 where under 0.10 was stated, and the leak is 34 / 23 where within one and a half times the unstressed pin's was stated. A seat the table read closed by 2.5 real is still claimed one time in four to one in eight by a learning population: the size of a stake is not read from the table alone.
- **Arm 4 at G_V ×2:** met on the first review, at the line, and on the leak; missed on the suspensions (12.5 / 18.4 against under 10).
- **The two reader corrections** are accepted as stated. Asked, by the provenance rule: every place on record — the notes and the published record — that quotes the plant kind's state-seat stage of a 2.9.0 stage table, with the figure before and after.

### H2. The reviewer's misses, stated

- **F4.1's size.** More than 1,500 real a slot was stated, and it was impossible: a slot's whole lifetime in the mixed world is 960–1,240. The reviewer took the gap between two worlds for the gap inside one.
- **G2 and F4.2, the sizes.** The bond's part at π^A 0.20 is 0.80 real a multiple where about 0.5 was stated; the weight's doubling is worth 0.25 to 1.4 where 0.2 to 0.3 was stated; the first review's slope is three times the 0.3–0.5 stated.
- **G3's bound named the wrong pin**: the 0.10 pin's figures for a chain at 0.20. The notes read it against both, and it missed against both.
- **The direction of the errors.** The reviewer's arithmetic understated how hard a stake bites in the table, and the table overstates what a stake does to a learning population.

### H3. Two reads, both without training

**1. The entry test.** F4.1's construction, with the claiming slots at 1 in 10, 1 in 4 and 3 in 4 of the population (F4.1 read 1 in 2). On the pin and on arm 4, both learners, seeds 21–40, the policies of record §102's, the cell theirs: a temptation of 1, the bond ×1. If the wrapper draws only halves, the share is a reader-side option; say so before running.

Read by group as in §105, and beside it: the careful group's suspensions a slot and its lifetime against the all-careful population's in the same cell, which is what the honest pay for the company; the member audit seats held by each group, a slot; the dials at the end; the leak and the overhead.

**Expected:**
- the careful ahead at every share, and at 1 in 10 by at least 200 real a slot;
- the careful group's suspensions falling with the claimers' share: under 0.3 a slot at 1 in 10, from 0.6 at 1 in 2;
- the leak at 1 in 10 within one and a half times the unstressed (the pin's 11 / 8, arm 4's 10 / 6), and at 3 in 4 above half the all-claiming world's (above 33 under the pin, above 9 under arm 4);
- at every share a claiming slot holding less than a tenth of the member audit seats that a careful slot holds.

**Refuted** if the claiming slots end level or ahead at 1 in 10. Then a careful population can be entered by a few claimers, and the claim is an equilibrium at the margin, whatever the even split showed.

**2. The missing cells of the stake's table.** On §106's instrument, arm 0 with π^A pinned, the member's audit seat, at a temptation of 1 and 2:

| π^A | The bond at the audit and panel seats | The weight |
|---|---|---|
| 0.20 | ×2 | 1.5 and 3 |
| 0.20 | ×4 | 3 |
| 0.30 | ×1, ×2, ×4 | 1.5 and 3 |

Eighteen cells. The first review's bond as §99 had it. The honest side for each stake as in §106's addendum, ten seeds.

**Expected**, from §106's slopes:
- the truth-checked bad share at the seat about 0.25 at π^A 0.30, and the bond's part there at least 1.2 real a multiple;
- a temptation of 1, π^A 0.30, the weight of record: the claim's edge +0.7 ± 0.4 at ×1, under −0.3 at ×2 and under −3 at ×4;
- π^A 0.20 at ×4 with the weight at 3: under −1.2;
- at a temptation of 2, π^A 0.30 closes by more than 1 at ×4;
- the honest side: π^A 0.30 beside 0.20 at the same bond costs the careful population under 3 in 100 of its surplus, and the system about 1.5 a task more in overhead.

**Refuted** if the bond's part at π^A 0.30 is under the 0.80 read at 0.20. Then more frequent planted approvals stop adding to the stake's bite, and the test rate is not the cheap lever it looks.

**The purpose of both:** which mix of the three levers — the fee at the seat, the rate of planted approvals, the bond — closes the member's seat at the least cost to the honest; and whether a careful population holds against a few claimers with no stake at all.

### H4. Not ordered

- **No learned chain** until both reads are in.
- **A learner with a horizon.** It is a build, and it is Baruchi's decision. Asked now, so that he can decide: what it would take in this instrument — what changes in a decision's credit, what stays the driver's convention, how long to build, and how long to run on the pin and on arm 4 at a temptation of 1. F4.1 says what it should find. Whether it finds it is the question.
- **The dial under the temptation**, as before.

---

## Addendum 9 to revision 2 — after the entry test and the completed table

*November 12, 2026. Read: notes §109 and its addendum, in full; the note is dated November 13 by its author. The record of them is "Ablation A1 — the entry test, and the stake's table completed". No rule, arm or flag of record is changed, and nothing is drafted. Here: the rulings; the reviewer's misses; readings asked from worlds on record; two reads without training; the learner with a horizon, which waits for Baruchi; and what is not ordered.*

### I1. Rulings on the notes

- **§109 is accepted as read.** The share is a reader-side option, stated at `121a6c4da`, and at one half it gives F4.1's halves to the name. Nine honest cells in place of eighteen are accepted: a careful population never claims, so the temptation changes nothing for it.
- **H3.1, the entry test, is not refuted.** The careful are ahead in all sixteen worlds, and at 1 in 10 by 353 to 459 real a slot where at least 200 was stated. Of the four expectations the reviewer counts three met, one of them at the line in one world (arm 4, head alone: a leak of 9 where above 9 was stated), and one void: the careful group's suspensions "from 0.6" rested on a figure that §109 withdraws.
- **H3.2, the missing cells, is not refuted.** The bond's part at π^A 0.30 is 0.93 real a multiple over ×1 to ×4: above the 0.80 that refutes, under the 1.2 stated. The misses are in I2.
- **"Not an equilibrium at the margin"** is accepted for the conduct read, §102's frozen policy. A smaller dose of skipping and a name that returns are not read (I4).
- **Two sentences are not accepted as written.**
  - *That the bond's slope steepens with the multiple at both rates.* At 0.30 it reads 0.43 ± 0.21 and then 1.18 ± 0.19. At 0.20 it reads 0.91, 0.54, 0.90, 0.89, each ± 0.2 to 0.3 with the cells taken as independent: no steepening.
  - *That the tests pay the careful.* The surplus is nominal. Between π^A 0.20 and 0.30 the price level is 6 to 9 in 100 higher, and the real lifetime is level within its error at all three bonds (+900 ± 1,190; −767 ± 1,026; +517 ± 1,083). The step from 0.10 to 0.20, on record, paid nothing. The ruling: the tests cost the careful nothing in real terms, and that they pay them is not shown. For the fee's doubling the rows suggest about 5 in 100 in real terms at ×1 and ×2; the paired figure is asked in I3.
- **The suspension log's correction** (`4df18f1bc`) is accepted with its list. §105's sentence on the careful half is withdrawn, and the reviewer's records that carried it are corrected: the stake reads' section 1, this brief's H3.1, and "everything we know". The older records that quote false approvals for each suspension (runs 34 and 36, and specification 2.8.0's first finding) are listed in the record with the figure before and after, and are not rewritten.
- **The provenance listing** is accepted. §108's "up to four hundredths" is five and a half; and the filed share and the panel wait moved too, where disputes are on. None of the reviewer's records quotes a figure the listing moved, other than that sentence.

### I2. The reviewer's misses, stated

- **The bond's part at 0.30:** at least 1.2 stated, 0.93 read. Two errors of arithmetic. The 0.80 at 0.20 was the slope over ×1 to ×8, and the cells ordered run from ×1 to ×4, where 0.20 reads 0.67. And the share of approvals at the seat that a truth check finds bad rises 1.3 times from 0.20 to 0.30, where the reviewer took the rate's 1.5. With both right the expectation was about 0.9.
- **So three cells were stated closed by more than they are:** ×2 at 0.30 (+0.13 where under −0.3), ×4 at 0.30 (−2.24 where under −3), and ×4 at a temptation of 2 (on the line where closed by more than 1).
- **The system's cost of the higher rate:** 1.5 a task stated, 2.1 to 2.4 read.
- **An expectation built on a wrong figure.** The reviewer recorded §105's 0.6 suspensions a slot, drew a sentence from it, and built H3.1's second expectation on it. The figure was a reader's fault.
- **"Twice the tests, 2.6 times the bite"** in the stake reads' record was the ×1 to ×8 figure given alone. Over ×1 to ×4 it is 1.8 times.
- **The direction.** In addendum 7 the reviewer's arithmetic understated the bond's bite, and in addendum 8 it overstated it. The stated ranges were too narrow both times.

### I3. Asked from the worlds on record — no run

1. **The entry test's worlds, by group:** the ticks a slot is in place; the lifetime for each tick in place; and where a claiming slot's wallet comes from (awards, review fees, the rest).
2. **The standard error** of the careful group's suspensions a slot at each share, beside the all-careful population's. At 3 in 4, three of the four worlds read 0.15 to 0.17 against 0.12.
3. **How the group's lifetime, wallet and benefit are averaged.** At 1 in 10 and 1 in 4 the lifetime is not the sum shown beside it: 418 against 355 + 68; 479 against 399 + 78; 395 against 346 + 47; 423 against 366 + 51.
4. **Whether the private benefit is off the ledger, and unread by the frozen policies.** If both, the same worlds read any temptation by scaling the benefit. The reviewer's arithmetic on that footing: at 1 in 10 a claiming slot gives up 410 to 520 of wallet for 51 to 78 of benefit, so the conduct of record draws level with the careful at a temptation of about 7 to 8, and of 10 to 15 at the larger shares. Please confirm or correct.
5. **The honest side in real terms, paired by seed:** the real lifetime for the fee's doubling at each stake; the surplus deflated by each cell's price level, for the step from 0.20 to 0.30 and for the fee; and both again for the step from 0.10 to 0.20 at ×1, from §106's cells.
6. **Which clock dates the notes.** §109 is dated November 13 and reached the reviewer on November 12 at 21:54, Israel time.

### I4. Two reads, both without training

**1. The dose.** The entry test read one conduct: a policy that claims the member's audit seat nearly always and the first review two to six times in ten. Not read: a member that is careful and skips now and then, which is what a member that counts its future would try first. A scripted policy: careful, and at each review decision a claim with probability q. If this is a reader-side wrapper, as the share was, say so before running.

- The dosing slots 1 in 4 and the rest careful; the pin and arm 4; a temptation of 1, the bond ×1; seeds 21–40.
- Doses of 0.1, 0.3 and 1 at every review seat. On the pin, two more at 0.3: at the member's audit seat only, and at the first review only. Eight worlds.
- The two worlds at 0.1 on forty seeds, 21–60, if seeds 41–60 are free of any other use. Say if they are not.
- Read as the entry test, and beside it: the claims a slot, and the lifetime lost for each claim (the careful slot's lifetime less the dosing slot's, over its claims), with its error.

**Expected:**
- the dosing slots behind at every dose: by at least 350 real a slot at 1, and by at least 150 at 0.3;
- at 0.1 behind, by 30 to 250. The read cannot tell less than about 100 from nothing, so at this dose the mechanism is read beside it: suspensions a slot at least one and a half times the careful's, and fewer member audit seats a slot than a careful slot holds;
- the lifetime lost for each claim at least 5 real at 0.3 and at 1, against the table's edge of +1.94 for a claim at the audit seat.

**Refuted** if the dosing slots at 0.3 are level or ahead. Then a member that counts its future does better with some skipping than with none, and the tests and the stake have work to do that the record does not do.

**2. The name that returns.** What the entry test shows a skipper losing is its place. Run 23 found the way round a lost place: leave, and come back under a fresh name. 2.7.0's loan closed it for a stamper in the world of record (run 25: the harvester 1,137 behind the careful, carrying out nothing). In the stressed world a skipper's gain is the effort it saves, which no loan takes back. Not read.

- The conduct, scripted: a name that claims at every review seat it is given, leaves when it is suspended, and returns at once under a fresh name.
- The cell: 1 slot in 10 run by such operators, as in the entry test, if the return can be put on the mixed world's claiming slots without a build; one operator in a careful population, as in Q1's re-arrival cell, if not. Say which before running, and what a returning name starts with: the loan, its probation, its first seats.
- On the pin and on arm 4; a temptation of 1, the bond ×1; seeds 21–40. If the benefit is off the ledger (I3, item 4), a temptation of 2 is read from the same worlds.
- Read for the operator over the run: the names used; the wallets carried out, summed; the private benefit, summed; the bank's loans to it and what it left unpaid; the seats and the plants its names took. Beside it the careful slot in the same world. And for the loop: the leak, the overhead and the bank's loss with such operators against without.

**Expected:**
- at a temptation of 1 the operator behind the careful by at least 300 real over the run; its names carry out about nothing; its benefit under 40 real a name; 5 to 15 names a run;
- at a temptation of 2 still behind. The reviewer cannot size it.

**Refuted** if the operator is level or ahead at a temptation of 1. Then the record holds a name and not an operator, and what a new name costs is the stake that matters. That price is admission, which the orchestrator sets.

**If either can be answered from worlds on record**, say how, and the reviewer will rule on whether the arithmetic stands in for the run.

**The purpose of both:** whether careful is the best life against the two things a member that counts its future would try first — a little skipping, and a fresh start. They are also the known answers that a learner with a horizon would be tested against (I5).

### I5. A learner with a horizon — for Baruchi's decision; nothing is ordered

§109 answers H4. A decision's target would become its slot's own return: its later decisions' rewards and the slot's own work-side money in between, to a horizon or to the slot's exit. Both changes are in the instrument. Nothing in the engine, the rules, the observation or the driver's conventions moves. At a horizon of 1 every chain of record is reproduced to the decimal. About two working days to build; about six hours of wall time for one horizon on the pin and arm 4 with both learners.

**The reviewer recommends building it**, for three reasons. Every learned chain so far skips, and the entry test says the skippers lose: with the learner of record the two cannot be told apart from a weak rule. A stake sized on such chains is sized for an agent that cannot see its future, and the honest pay for it. And a learner that sees its future is also a stronger adversary: it can look for the long game — a record built and then spent — which the learner of record cannot.

**If Baruchi decides yes**, three things before any chain is read:

1. The implementer's regression test: a horizon of 1 reproduces a chain of record to the decimal on a stored collection.
2. A known answer. On the offline collection, where actions are drawn at random, the fitted difference in return between a claim and an inspection at the member's audit seat, and at the first review, is set beside I4.1's lifetime lost for each claim: the same sign, and within a factor of three. A learner that cannot see what the scripted read shows is not an instrument for this question.
3. The return's spread, and the number of decisions behind each action at each seat, reported with the fit.

The first cells are the implementer's: the pin and arm 4 at a temptation of 1 and the bond ×1, both learners, the slot's remaining life at γ 0.98; a horizon of 32 only if the first moves the audit seat.

**Expected**, stated now and before any build:
- under the pin, the member's audit seat claimed under 0.10, from 0.94 / 0.99, and the first review under 0.10, from 0.29 / 0.25; the leak within one and a half times the unstressed 11 / 8;
- under arm 4, the first review claimed under 0.10, from 0.25 / 0.22, and the leak within one and a half times the unstressed 10 / 6;
- the population's real lifetime within 10 in 100 of the careful population's in the same cell.

**Refuted** if, with the three tests passed, the member's audit seat is still claimed above 0.5. Then a learner that sees its own future still skips, the careful's lead in the entry test is not something a member can learn its way to, and the stake and the tests carry the weight after all.

### I6. Not ordered

- **No learned chain on the learner of record**, and no further cell of the stake's table.
- **The dial under the temptation**, as before.

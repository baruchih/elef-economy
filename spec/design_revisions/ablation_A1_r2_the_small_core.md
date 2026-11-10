# Ablation brief A1, revision 2 — the small core's arms

**Status:** candidate configurations for evaluation, **not in force**. No version number, nothing consolidated, no rule moved. Built behind flags and labelled as release candidates are. Adoption of any arm is a design revision drafted after the runs.  
**Date:** November 10, 2026 (r1 and r2) · **From:** the economy's reviewer · **Supersedes:** r1 of the same day.  
**What r2 settles:** the implementer's review against the engine at `2417219ba` (notes §78): eight corrections accepted (D1–D3, A1.1, A1.2, A2.1, A2.2, A3.1, A4.1, with A4.2 and A5.1–A5.3 noted); the four items put to the reviewer ruled (D4, C1, A1.3, Q1); hypothesis 1 restated, because its second clause was wrong; two arms and two pinned cells added, on the arithmetic of §2.  
**Addenda 1 and 2** (same day: after the payoff table; after the scripted sweep and the panel check) are at the end. Nothing in §1–§9 is changed by them except §7.3, which gains one chain (B3).  
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

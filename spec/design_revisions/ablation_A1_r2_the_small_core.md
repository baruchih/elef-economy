# Ablation brief A1, revision 2 — the small core's arms

**Status:** candidate configurations for evaluation, **not in force**. No version number, nothing consolidated, no rule moved. Built behind flags and labelled as release candidates are. Adoption of any arm is a design revision drafted after the runs.  
**Date:** November 10, 2026 (r1 and r2) · **From:** the economy's reviewer · **Supersedes:** r1 of the same day.  
**What r2 settles:** the implementer's review against the engine at `2417219ba` (notes §78): eight corrections accepted (D1–D3, A1.1, A1.2, A2.1, A2.2, A3.1, A4.1, with A4.2 and A5.1–A5.3 noted); the four items put to the reviewer ruled (D4, C1, A1.3, Q1); hypothesis 1 restated, because its second clause was wrong; two arms and two pinned cells added, on the arithmetic of §2.  
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

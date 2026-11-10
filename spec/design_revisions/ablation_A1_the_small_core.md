# Ablation brief A1 — the small core's arms

**Status:** candidate configurations for evaluation, **not in force**. No version number, nothing consolidated, no rule moved. Built behind flags and labelled as release candidates are. If an arm is ever adopted it is drafted as a design revision in the usual way, after the runs.  
**Date:** November 10, 2026 · **From:** the economy's reviewer · **For:** the implementer's review against the engine before anything is built — correct the words wherever they meet the code, as with every rc.  
**Rulebook in force:** 2.9.0 with the consolidated defaults (the roll's floor 0.5, window 20; the correctly rounded emission).

## The question

Run 34 found that a population stamps the seats past the first review. 2.8.0 and 2.9.0 answered by sending the orchestrator's truth to those seats as plants. The other answer was never tried: **give those seats to the orchestrator.** This brief sets the two side by side, on what leaks and what it costs, and separately tests one principle the record's own conclusion implies: *a member's bond burns only against trusted truth.*

Arms 2–4 run against a standing design position — the troops minimized. They are measurements of what that position costs or saves, not proposals. Adoption is Baruchi's call, after the numbers.

## One definition used by every arm

**The deciding verdict.** The orchestrator's own verdict on a real case: two seats of its own inspectors, taken at once; if they agree, that is the verdict; if they differ, a third decides. Each seat is a troop's seat as the rules have it (the truth with probability 1 − ε_T; step 5's shared difficulty applies when on), paid as a troop's seat is paid. Never taken on a plant, whose truth is known.

## The arms

**Arm 0 — 2.9.0 as in force.** The reference.

**Arm 1 — the trusted ruling** (`trusted_ruling`).
- An audit that disagrees with the verdict it audits opens no member's third seat: the deciding verdict is taken at once and is the outcome.
- An appeal or dispute panel sits as today (two fresh members). If both confirm the standing verdict, it stands as today. Otherwise the deciding verdict is taken and is the outcome. The driver's ruling is never sought.
- A member's review is overturned — bond burned, as today — **only** if its verdict differs from the deciding verdict or from a plant's truth. An auditor or panelist that matches the deciding verdict stands and is paid.
- The court fee by the outcome, as today. Plants unchanged: truth adjudicates every seat on a plant.

**Arm 2 — the state's audit** (`trusted_ruling` + `state_audit`).
- Every audit obligation on a member's approval of a member's delivery is discharged by one seat of the orchestrator's own inspectors, at the audit's step, without waiting for a member. If it agrees, the approval stands. If it differs, the deciding verdict is completed — the audit seat counting as its first — and is the outcome.
- No member sits an audit of a member's work. The orchestrator's own deliveries keep the market's audit by a member; I25 unchanged.
- `planted_approval` off. A plant's audit obligation is discharged at once with no seat. Panels remain members'; the truthful planted challenges and the planted lies continue.

**Arm 3 — the state's bench** (`trusted_ruling` + `state_bench`).
- An appeal and a dispute are decided by the deciding verdict, taken at the filing's step. No member panel. The fee by the outcome.
- `planted_lie` off; plants file no challenge. Audits as 2.9.0 with arm 1's escalation; `planted_approval` on.

**Arm 4 — the small core** (arms 1 + 2 + 3).
- Members hold initial reviews and resumed reviews. Every later seat is the orchestrator's.
- Plants as 2.7.0 had them: a plant closes at its first verdict (`plants_every_seat`, `planted_approval`, `planted_lie` off). The 2.6.x disguise and all eight conformance items unchanged.
- The duty tier of the record stands; the panel tier has no seat left to gate.

**Arm 5 — no plants** (second wave; built only if arm 4 reads well; a sketch here, a text then).
- Arm 4 with the plant rate at zero. The record 1.2.0 keeps on plants is kept on the orchestrator's adjudications of real cases instead — each state audit and each deciding verdict that judges a member's verdict enters the same windows and thresholds; probationers' approvals are all audited, as they are; the dial moves the roll's floor in place of the plant rate.
- Its question: can trusted audits of real work replace planted cases altogether — the one dependency (constructing and disguising plants) that the simulation gets for free and reality does not.

Two of the review's proposals are **defaults, not arms**, and are swept under the implementer's step 3: the ruling's accuracy (`--ruling-accuracy` 0.8 / 0.95 / 1.0 on arm 0) and a larger bond at the audit and panel seats (×2, ×4).

## Readings, every arm and population

- **The leak**: bad paid work over all paid work, and over all bad deliveries; by channel (member-confirmed, state-confirmed, never audited, challenged-and-confirmed by members / by the state).
- **The overhead per delivered task**, two views: what the task cost its customer beyond the price; and what verification consumed in the whole system (care at every seat, members' and the state's, on real cases and plants; the cost of truth; **the plants' own work at the trailing market price, as a shadow cost**) — each also as a share of the price.
- **The state**: its seats by kind, its share of all review seats, its peak seats per tick.
- **The members**: fee income by seat kind, nominal and real surplus, members alive.
- **False penalties**: bonds burned on verdicts that agreed with the truth, by seat kind.
- Challenges filed and won, by the challenge's truth; time from submission to vesting (median, 90th percentile); the customers' tasks per 1,000; P_t; every invariant.

## Populations and order

1. **Scripted**, seeds 21–40 paired against arm 0: all-careful with arrivals; the 60/40 entry cell; fixed 60/40; entry with truthful disputes; entry with liars at 0.1. All arms 1–4.
2. **Learned on own money**, the earnings predictor first, careful and stamper starts: arms 1 and 4 against arm 0's chains on record.
3. **The stressed world** that steps 3–5 define (a temptation at the frontier, the customer's detection at 0.25, correlated errors at a stated level): arms 0, 1 and 4, scripted then learned.

## Hypotheses, stated before the runs

1. **Arm 1**: bonds burned on correct member verdicts fall by at least half in every scripted cell; the leak does not rise; on the learned population the audit seat's blind-verdict rate falls, a correct rejection no longer being punished one time in five.
2. **Arm 2**: the member-confirmed channel is zero by construction and the total leak is at or below arm 0's in every population, the learned ones included; the cost of truth falls by the planted approvals' and the plants' audits' share; the members' income falls by their audit fees.
3. **Arm 3**: a lying challenge is paid at the deciding verdict's error rate (under one in a hundred) and a truthful one is won 99 times in 100, in every population.
4. **Arm 4**: the leak is within noise of the careful reference in every population — the learned ones from both starts — because members hold only the seat the plants already price; the customer's overhead is unchanged and the system's is below arm 0's; the orchestrator's share of review seats roughly doubles.
5. **In the stressed world** arm 4's advantage over arm 0 on the leak widens, and arm 0's member audit seat re-opens.

**What would refute the review.** If arm 4 does not hold the leak at or below arm 0's, or its system overhead — the orchestrator's seats counted at cost — is above arm 0's, then the members' later seats are load-bearing and cheaper than the orchestrator's, and 2.8.0 and 2.9.0 were the better answer to run 34. That result would be recorded as plainly as the other.

## Invariants under the flags

I25 unchanged in every arm. Under `trusted_ruling`: no member review is overturned except by a plant's truth or a deciding verdict; no ruling is recorded. Under `state_audit`: no member audit review exists on a member's delivery. I20 and I42–I44 are vacuous where their flags are off.

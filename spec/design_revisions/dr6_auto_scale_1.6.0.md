# Agentic Economics — The Task, Verification, and Dispute Loop

## Design revision 6 — specification 1.6.0-rc.2: auto-scale

**Project:** ELEF / Agentic Economics  
**Version:** 1.6.0-rc.2 — a release candidate, not yet in force. rc.1 (October 17) was the proposal as first sent; rc.2 settles the seven points of the implementation review [I14] — the panel-record requirement dormant until the world's first plant is adjudicated, and the first period's panels named as the state's; a plant reserve held back from Ω's advances, and liabilities bounded in age; Hypothesis 1 restated against the ceiling (the seat binds the queue, not the rate); the delivery check against the fund plus Ω's available advance, drawing only the delivery's own shortfall; a clock settled at the case's final when there is no verdict; "withdrawn before award"; the cold start read from every run's first periods rather than an arrivals process — and its smaller points, chiefly one flag per rule and one-factor-at-a-time cells first. On acceptance it becomes **1.6.0**, consolidated into one standalone text, and 1.5.0 moves to history. Semver as before.  
**Prepared:** October 17, 2026 (rc.1 and rc.2)  
**Supersedes:** 1.5.0 where this document speaks; everywhere else 1.5.0 stands unchanged.  
**Nature of this revision:** A **design revision** under §19 — the sixth since the freeze. It gives every request a **service clock** and makes the orchestrator pay for lateness; it lets the orchestrator **scale** — troops for inspection seats and deliveries, backed by Ω's own balance — to whatever the market leaves undone, inspection first; it sizes the reviewing reserve on the reviews **waiting**; it requires a **determined** record of anyone who holds a panel seat; and it restores the two-period reserve. It adds no participant, no verdict, no challenge; it adds one clock per request and one flow (Ω → requester). **Why minor:** what members may do changes in one place only — an undetermined member no longer holds a panel seat, which the newcomer pin already implied — and nothing changes in how they are paid or how truth enters; the rest is what the orchestrator does with what the market leaves.  
**Design assumptions, unchanged:** humans do not intervene; troops bear no malicious intent. **New, stated:** ELEF operates the servers and the treasury, so capacity is a decision of the orchestrator's, not a fact of the market's; the orchestrator is therefore answerable, in money, for the customer's wait.  
**Status:** Proposed. Accompanied by the evidence that required it (§1) and the runs that test it (§8).

> **The state has servers of its own. It uses as few as it can, for as short as it can, and says how many.**
>
> **The treasury keeps what the need requires, and pays out the rest.**
>
> **The state scales to the queue, inspection first, and pays the customer for every tick it is late.** *(new)*

---

## 1. Why: what run 7 found

Run 7 — 482 runs under 1.5.0, every final audit passed, truthful appeals and no disputes — established that the reserve rule does what it says and does not help, and found what does bind [S7]:

1. **The capacity that binds is the reviewing seat, not the treasury.** On duty 4.5–5 at every split under every rule since 1.3.0; reviews that found no reviewer 7,300–11,400 case-ticks a run; vesting pinned at 2.2–2.4 a tick **whoever delivers**. Troop deliveries wait for their initial review and their pinned audit with their capital held; cash tied in deliveries waiting for inspection is cash the fund cannot put into an inspection seat (290–530 seat refusals) or the next delivery. This has been true since run 1 — "X = 4 is saturated… harmless here; matters once delay carries cost" — and every throughput control since run 4 was already capped by it. Twelve probationers at 60/40 sat idle while reviews waited, because the reserve is sized on expected demand and seats three of them.
2. **The demand stock counts the queue, and the queue never ends.** Requests do not expire; about 300 are open at 50–60%, each refused at every seating; $D_s$ is the queue's price (peak 3,568 against the text's 270; 94 troops in flight against 13) and $R_T$ is unreachable. Hypothesis 1 of revision 5 fails: refusals rose, deliveries did not, vesting and uplift were identical to 1.4.0.
3. **The boundary reset saw-tooths** — the sawtooth rc.2 rejected for the shortfall-zero rule arrived by the reset (3,135 and 3,146 paid out in one batch each while refusing nine summonses a tick). The two-period reading had damped it.
4. **The award window is not a knob** while the seat and the tied-up cash bind ($w_A$ 1 / 2 / 5 → vested 2,112 / 2,186 / 2,063).
5. **Q14 — the leak is the auditor's record.** Of probationers' false approvals that reached a customer, 85–90% travelled the upheld route; of those, **55–75% at fixed splits and 73–80% under drift were audited by a member whose record had not yet failed** — at a fixed split, a stamper the plant record had not caught. A member in standing misses 2–3 a run, a troop under 1, the ruling 10–15%. The lag is the record's, not the drift's.
6. **Minimization holds** (troops ≈ 0 from tick 500 in the adaptive run; $R_T$ 0–4 from 1,000), and **the red team buys nothing** — decliners end 901–2,040 poorer and starve the state; a requester flood is not served and not an exploit; the reformer ends 2,479–3,958 poorer.

Baruchi's reading [C-rev6]: a request that is on hold for a long time is a problem for the network's rating — re-queue it with priority and have the orchestrator take some of the blame in money; and if ELEF controls the network and the servers, allow **auto-scale** — send more troops and add money to the treasury when needed. Both are adopted here. His third suggestion — that the network should earn less when the state has to scale, to make it faster — is adopted where "the network" is ELEF (the rebate and the working capital are ELEF's cost) and **rejected where it is the members** (§1, recorded and rejected).

**Classification.** A design revision motivated by run 7's capacity finding and Q14, read on its own. It alters no settlement rule between members and requesters; it adds the orchestrator's liability for lateness and the orchestrator's authority to scale.

**Recorded and rejected.** *Requests expire* (the design reviewer's run-7 proposal — a request unawarded for $T$ withdrawn by the orchestrator): bounded the queue by turning customers away; replaced by the service clock and the rebate. *Members earn less while the state scales* (fees or emission cut by the state's share): at 60/40 the members standing are the honest ones at capacity, the actors who caused the shortage already earn nothing, and in the model nobody can "go faster" — speeds are fixed; what a market does under shortage is raise the price and draw supply, which is §18.1 question 2 and the next frontier, not this revision. The one "earn less" already in and already right stands: while the state carries, the uplift stops. *A rebate paid in cash before anything was bought*: a posting locks nothing (pay-in is at award), so a rebate on an unawarded request would be money for nothing and a flood would farm it; the rebate is a discount at the first verdict (§2.1). *Lateness measured to the award*: with Ω backing the fund an award to a troop is almost never late; the customer's wait is for the verdict, and the inspection seat is where it is lost.

---

## 2. The rules

### 2.1 The service clock: priority and the orchestrator's rebate

**Rule — the clock.** Every root request carries a **service clock** from its posting to its **first verdict** (approval or rejection; a P or ⊥ response is not a verdict) — **or to the case's final settlement without one**, whichever comes first: a delivery that misses its deadline is final N with no review, and the customer waited either way. Its **service target** is $T_s$ ticks. The clock runs only for a request whose ceiling admits the market price ($\beta\ge\bar B$); a request priced below the market is not the state's to answer for, and its clock is stopped while it is so priced. (In every driver so far each offer is at the ceiling, so $\bar B=\beta$ and the exclusion is dead until a driver varies $\beta$ per request — the red team's below-market poster is the first.)

**Rule — priority.** The orchestrator serves **the oldest clock first** in every pass it runs: the award summons (1.4.0 §2.3), the assignment of waiting initial reviews, the review-seat summons. This is what the engine already does — it iterates live cases in creation order, which for root requests is posting order — stated as a rule so that it can be checked (I26); drivers award members oldest-first as a matter of conformance. A late request is never dropped; the human's withdrawal of an **unawarded** request remains the only withdrawal — a request cannot be withdrawn after award.

**Rule — the rebate.** For every tick a request's clock stands past $T_s$ the orchestrator owes the requester $r_s$ (default $\omega_0 B$, the base service fee, 1 at $B=20$), **capped at the price $B$** — so a request more than $B/r_s=20$ ticks late is owed nothing further, and the orchestrator's total liability is bounded by $B$ times the open requests. The rebate is **settled when the clock stops** — at the first verdict, or at a final without one, using the lateness to that final — from Ω, as a payment to the requester against its pay-in: a discount on service rendered, never cash on a request that bought nothing. A request **withdrawn before award** is owed nothing — so a requester cannot farm the clock before award and cannot escape its benefit after, which is the point. A rebate Ω cannot pay when the clock stops is recorded as **Ω's liability** to that requester and paid in Ω's order (§2.2).

**Readings — the network rating.** Per period: **on-time share** (requests whose first verdict came within $T_s$, over requests with a first verdict), **mean lateness** (ticks past $T_s$, over late requests), **rebates paid**, **rebates accrued and unpaid** (Ω's liability), **open late requests**. These are the rating; nothing is estimated.

**Consequence.** The queue is bounded in *liability* instead of unbounded in count: every tick of waiting has a price, the price is the orchestrator's, and the reserve has something real to chase. ELEF now has a cost for not scaling — which is what §2.2 answers — and a customer who waits is paid for it in the loop's own currency.

### 2.2 Auto-scale: Ω backs the fund; inspection first; a delivery carries its inspection

**Rule — Ω backs the fund, above a plant reserve.** The advance cap $A_T$ is **removed**. When the fund cannot carry a summons, Ω advances the difference from its unlocked balance **above a plant reserve** — the capital the honesty clock will need for the rest of the period: the period's plant rate so far ($\pi_t$ times the initial-review rate) times $\varphi^E+\varphi^F$ times the ticks remaining. There is no plant cap in the engine — a plant is refused when Ω is short — and without the reserve the stress that summons the troops would spend the capital of the plants that detect it, and the dial would go blind exactly under capture. The state's reach is Ω's balance above that reserve, which is the honest limit of any treasury that also runs the clock. Advances are repaid from the fund's inflows before any uplift, as before.

**Rule — Ω's order of payment each tick.** (1) The plant reserve is held back. (2) **Rebate liabilities older than one period** are paid — a debt is owed, an advance is optional, and a debt does not wait more than a period. (3) Advances to the fund for summonses, **inspection seats before deliveries**. (4) Younger rebate liabilities. (5) Whatever Ω keeps. Advances rank above young liabilities for one reason, stated: scaling is what stops lateness accruing, so a tick of scaling reduces the liabilities of every later tick; the age bound is what keeps that reason from becoming an excuse.

**Readings:** Ω's unlocked balance and its minimum over the period; the plant reserve; advance outstanding; **plants unfunded for want of Ω** — which must read zero in every run, or the finding is that the float could not carry both the clock and the army; summonses refused for want of Ω's money (troop shortfall, now meaning the state is out of money, not out of policy); liabilities by age.

**Rule — inspection first.** In every summons pass, **review-seat summonses are processed before delivery summonses**, oldest clock first within each.

**Rule — a delivery carries its inspection.** A troop delivery is summoned only when **the fund's unlocked balance plus Ω's available advance** can carry **its own capital and the capital of two review seats** — $c^D_T+G+2\,(c_T+G^V)$, 36 at the defaults — the initial review it will need and the audit it will probably draw (a probationer's approval of it is pinned; a troop reviewer's carries $\min(1,m_t p_{\text{floor}})$). It is a **check, not a hold**: the advance actually drawn is the delivery's own shortfall on its 20, the review seats are not earmarked, and the order of the pass funds them first when they come. The demand stock $D_s$ keeps the delivery's own 20. The state never starts work it cannot get inspected.

**Consequence.** The state scales to the unmet need in both kinds of seat, and in the right order: an inspection seat costs 8, settles in a tick and returns about $+3$; a delivery costs 20, settles in about thirteen and returns about $+10$ — but only if inspected. Stress raises the state's share; as the market catches up, the summonses stop, the advances are repaid, and the readings fall to zero. This is the dial's philosophy applied to capacity: effort rises with the stress and relaxes after, and the gauges — the state's share, lateness, Ω's advance outstanding, Ω's minimum balance — say how much it cost. **Ω's minimum balance under stress is ELEF's solvency**, a number the loop has never produced before; at 80/20 with Ω₀ = 300 it is expected to go to zero (§3), and that is the finding, not a defect.

### 2.3 Seat the queue

**Rule.** At each seating the reserve $X_t$ is **at least the number of reviews waiting for a reviewer** plus the period's initial-review rate so far (the reviews expected this tick), and never less than the 1.2.0 §2.3 sizing, which is computed once a period; the maximum is taken at every rotation. Seats are filled in the 1.3.0 §2.3 order — members for member-only seats to the cap and the floor, **probationers lowest duty credit first for initial seats, all of them if the queue needs them**, members for remaining initial demand to the cap — and a review still unfilled after $w_R$ is a troop's (1.4.0 §2.2). The eligibility shortfall counts what no eligible free actor could fill before the troop did.

**Consequence.** Idle probationers while reviews wait is the waste run 7 found; this ends it. At 60/40 twelve probationers carry about four initial reviews a tick with room to spare; the members' four seats under the cap carry the pinned audits, and a troop takes an audit only after two ticks with no member free. The seat stops being the cap on the market; the cap on members' duty becomes the only one left — and it is a default (§2.6).

### 2.4 A panel seat requires a determined record

**Rule.** A **panel seat** — audit, appeal review, dispute panel — is held only by a member whose bad-plant record is **determined** ($\ge n_{\min}$ bad plants adjudicated, seen on duty) **and passes $\theta_{\text{panel}}$**. An undetermined member holds initial seats only, as a probationer does; its approvals are pinned, as 1.3.0 §2.2 already has it. A panel seat no determined passing member is free to take goes to a troop after $w_R$.

**Rule — dormant until the clock starts.** The determination requirement is **dormant until the world's first plant has been adjudicated**; from then on it is a Rule the engine applies at assignment and at the summons. A market whose clock has not started has asked nobody to prove a record. Worlds that never plant — the reviewer-authored test worlds, which carry the default $\pi_0$ and simply never receive one — are untouched; "plants off" is not a state the engine can see, so the first adjudication is the switch.

**Consequence — in every run, the first period's panels are the state's.** A record determines on four bad plants *seen on duty*; an actor off duty sees none. Bad plants arrive at about $\pi_t\times$ initial reviews a tick $\times\beta_P$ — 0.3 a tick at $m=1$, 0.6 at $m=2$ — shared among the five or so on duty, and a duty turn is three reviews or thirty ticks. A member is determined after roughly seventy on-duty ticks at $m=1$, spread over several turns; the eight careful members at 60/40 need thirty-two bad plants between them, **100–200 ticks**. So from the first adjudication until records form — the first period of every run at every split, sometimes two — every panel seat is a troop's. §8 therefore reads every comparison against run 7 **from the second period on**, or the first period's all-troop panels will be mistaken for the rule's steady effect; the first period is Hypothesis 5's measurement, not a defect.

**Consequence — at a fixed split the lagging auditor is gone.** A stamper's record fails the moment it is determined (four bad plants approved, $\hat a=0.83$), so no stamper is ever both determined and passing, and the 55–75% of the upheld route that stampers-not-yet-caught carried goes to determined careful members or to troops. **Under drift it does not close the lag**: a careful actor turned stamper holds a determined, passing record until its approvals accumulate in the trailing window — about four bad plants, some fifty reviews — and audits through that lag. That lag is the record's: $\theta_{\text{panel}}$, the window of twenty, and $n_{\min}$ are defaults, swept in §8; a rule that plants panel-holders more often is a candidate for a later revision and is recorded, not proposed. **What §2.4 does not change:** a careful member that slips once in its first four bad plants has $\hat a=2/6>0.2$ and is already panel-ineligible under 1.3.0 until its record dilutes ($n\ge8$); about a fifth of careful members pass through that state at determination, as before.

### 2.5 The reserve over two periods

**Rule.** $R_T$ is the peak troop demand $D_s$ over **the current and the previous period** (the 1.4.0 engine's reading, recorded in its Appendix I), with $D_s$ as 1.5.0 §2.1 defines it. The one-period reset of 1.5.0 is withdrawn.

**Consequence.** The boundary no longer pays out an accumulated balance in one batch when the in-flight cohort happens to have just vested. With Ω backing the fund, the reserve's remaining job is to decide when the fund repays Ω and when it pays uplift — not whether a troop is summoned.

### 2.6 Defaults

| Default | Value | Note |
|---|---|---|
| $T_s$ | 8 ticks | posting to first verdict; the fastest path with a troop is $w_A+\tau+1=5$; swept $\{5,8,12\}$ |
| $r_s$ | $\omega_0 B$ (1 at $B=20$) per tick late, capped at $B$ | settled at the first verdict, from Ω |
| $A_T$ | removed (kept in `Params` as the 1.5.0 control) | Ω's unlocked balance above the plant reserve is the bound |
| Plant reserve | $\pi_t\cdot$ initial-review rate $\cdot(\varphi^E+\varphi^F)\cdot$ ticks remaining in the period | held back from advances and liabilities |
| Liability age bound | one period | older liabilities are paid before any advance |
| Delivery carry check | $c^D_T+G+2(c_T+G^V)=36$ against fund + available advance; advance drawn on 20 | a check, not a hold |
| $X_t$ | $\max(\text{1.2.0 §2.3 sizing},\ \text{reviews waiting}+\text{period's initial-review rate})$, at every rotation | |
| Panel eligibility | determined ($\ge n_{\min}$ bad plants seen) and $\hat a\le\theta_{\text{panel}}$; dormant until the first plant is adjudicated | |
| $R_T$ | peak $D_s$ over the current and previous period | |
| Rule flags | `service_clock`, `omega_backs_fund`, `seat_the_queue`, `panel_determined`, `reserve_periods` — all on | each rule toggles alone for attribution (§8.1); `--rules 1.5.0` is the control |
| **Members' duty cap** | $\lceil E_t/2\rceil$, **swept against $\lceil 2E_t/3\rceil$ and $E_t$** | a product stance — at $E_t$ no member is ever free to deliver, every award is the state's; at $\lceil 2E_t/3\rceil$ six of eight at 60/40; Baruchi decides on the numbers, members' income by source beside them |
| $\Omega_0$ | 300, swept against 1,000 | the float the ramp needs |
| $\theta_{\text{panel}}$, record window | 0.2, 20 — swept 0.15, 12 for the drift lag | |

Everything else as 1.5.0. **Not in this revision, by decision:** any reduction of members' fees, emission or uplift as a function of the state's share.

---

## 3. Consequences and hypotheses

**Hypothesis 1 — the seat unbinds the queue, not the rate.** Three tasks a tick at $b=0.2$ vest at most $3\times0.8=2.4$ a tick plus the false approvals — a ceiling near 2.45; the 1.2.0 control at 50/50 (2,399) is *at* it and run 7's 2,175–2,375 within a few percent of it. The seat does not cap the long-run rate; it caps **the queue** — about 300 open cases at 60/40 and the latency of each. So: reviews waiting fall from 7,300–11,400 case-ticks a run to a few hundred; the open-case queue falls from ~300 to the in-flight count, a few tens; vesting rises by the backlog cleared — a few percent, toward the ceiling, not past it; the state's share rises to the unmet delivery demand and no further. The yardstick is the queue and the on-time share (§2.1), not vestings a tick — which is also why the harm the seat did was lateness, and why the clock prices exactly that.

**Hypothesis 2 — on time, from the second period.** From the second period at 50–70% the on-time share exceeds 90% at $T_s=8$ and rebates are small — a customer waits $w_A$ for the state and a tick for inspection. In the first period panels are the state's (§2.4) and the readings are Hypothesis 5's. At 80/20 the on-time share falls and rebates accrue, because Ω's balance, not policy, is the limit: **Ω's minimum balance above the plant reserve reaches zero at Ω₀ = 300** and recovers at 1,000, and plants unfunded for want of Ω read zero in both. This is the solvency reading; it says what float ELEF needs to carry a market that captured.

**Hypothesis 3 — $w_A$ is a knob now.** Shorter, more troops and a higher on-time share; longer, fewer troops and more lateness. Run 7's flat response was the seat's doing.

**Hypothesis 4 — the auditor's record.** At fixed splits the upheld route's "member suspended later" kind falls from 55–75% to near zero; probationers' false approvals fall by that share. Under drift it falls little; the drift lag is the record's window, and the $\theta_{\text{panel}}$ / window sweep says what it costs to shorten.

**Hypothesis 5 — the ramp, which every run is.** All twenty actors are undetermined at tick 0, so every run is a cold start for records: from the first plant's adjudication until records form (100–200 ticks at 60/40), panels are the state's, Ω's advance is drawn hard and repaid as determined members take the seats back, the state's share of *panels* falls from 100% toward its steady value by the second period, and rebates accrue early and stop. Measured in the first two periods of every §8 run, by period; no arrivals process is needed for it, and none exists — adding an actor to a running world is a new public operation and a design question of its own, recorded for later.

**Hypothesis 6 — the cap decides the market's shape.** At $\lceil E_t/2\rceil$ the honest deliver and inspect in roughly equal measure; at $E_t$ they inspect only, the state delivers everything the stampers cannot, vesting is highest and the state's share is highest. Honesty is unchanged across the three. Which to choose is a product decision; the run puts the numbers beside it.

**Hypothesis 7 — minimization still holds.** In the adaptive run troops, advances, lateness and rebates all reach zero as the population turns honest; the clock and the backing cost nothing at rest.

**Limit, restated.** A market the state can always carry is a market that need not grow. Members first at every seat, windows, cost at summons and the state's share on the record are the guards; the price signal that would make the market grow on its own is §18.1 question 2, untouched, and now the next question.

---

## 4. What does not change

Everything in 1.5.0 not named above: troops and their summons rules other than order and the delivery check, the obligation, the fund's order of payment, membership, probation and its pin, plants, the dial, the pots, verdicts, challenges, $\rho$, $\kappa$, emission, uplift, overrides, grades. The duty cap's rule is unchanged; its default is swept.

---

## 5. Invariants, notation (amendments)

**I26 (new) — service.** Every root request with $\beta\ge\bar B$ carries a running clock from posting until its first verdict or its final without one; waiting items are served oldest-first in every orchestrator pass; the rebate owed equals $\min(r_s\cdot\text{ticks late},\,B)$, is settled when the clock stops from Ω or recorded as Ω's liability, and is zero for a request withdrawn before award. Rebates paid are Ω → requester transfers (I1 covers them); a liability is a counter on Ω, not credits; "paid plus accrued equals owed" is a bookkeeping identity over that counter, and the counter is bounded by $B$ times the open requests.
**I23 (amended) — the fund and Ω.** No $A_T$: Ω advances from its unlocked balance above the plant reserve, in the §2.2 order — the reserve held back; liabilities older than a period; inspection-seat summonses; delivery summonses; younger liabilities; advances repaid before uplift; $R_T$ over two periods; **plants unfunded for want of Ω is zero** (a reading the invariant watches, a finding when it is not).
**I24 (amended) — troops.** Review-seat summonses precede delivery summonses in a pass; a delivery is summoned only when the fund plus Ω's available advance can carry $c^D_T+G+2(c_T+G^V)$, and the advance drawn is its own shortfall; once the world's first plant is adjudicated, a panel seat is held only by a determined, passing member or a troop.
**I22 (amended) — membership.** Once the world's first plant is adjudicated, no probationer **and no undetermined member** holds an audit, appeal or dispute seat.
**I9 (amended).** On-duty seats are at least the reviews waiting whenever eligible free actors exist to seat; the gap otherwise is the eligibility shortfall.

**Notation (Appendix C additions).** service clock; $T_s$; $r_s$; on-time share; lateness; rebate; Ω liability; determined record (as 1.3.0 §2.2); $X_t$ redefined; $R_T$ over two periods.

**§18.1 (amended).** *Q11* (throughput) is now measured against the posting rate, not a review-capped control. *New Q15*: the network rating — on-time share and lateness at each split, and what they cost Ω. *New Q16*: ELEF's solvency — Ω's minimum balance under stress against Ω₀. *Q14* continues under §2.4. *Q2* (price and competence) is named as the next frontier.

---

## 6. Worked example

Twenty actors, 60/40, defaults, $m=2$, tick 500: eight members (four on duty under the cap, four free), twelve probationers.

**The seat.** Three requests a tick and about one troop delivery a tick need about four initial reviews a tick. Under 1.5.0 the reserve seated three probationers and reviews waited; under §2.3 the waiting reviews size the reserve, and the probationers are seated until nothing waits — six to eight of the twelve on duty, the rest free (and, suspended from the market, with nothing else to do). Every probationer approval is pinned; about three audits a tick go to the four members on duty, who are all determined and passing; a fourth audit in a busy tick waits $w_R=2$ and goes to a troop. Reviews waiting: a handful of case-ticks a tick, not eleven.

**A request's clock.** Posted at tick 500 at $\beta=20\ge\bar B$. No member free at 500 or 501; at 502 the award summons — oldest clock first — and the carry check: $20+16=36$ against the fund's unlocked balance plus Ω's available advance above the plant reserve; the check passes, the fund is short on the delivery's own 20, and Ω advances that difference and no more. Troop $\tau_{91}$ delivers at 504; a probationer reviews at 505 — **first verdict at tick 505, five ticks on the clock, three inside $T_s=8$**: on time, no rebate. Its pinned audit is summoned for at 505 as an inspection seat, ahead of that tick's delivery summonses; a member takes it at 506. The case vests at 516; the fund receives 30 and repays Ω's advance before any uplift.

**A late one.** At 80/20 (four members, two free; sixteen probationers) troops deliver about two of three tasks a tick; each needs 36 of carrying capacity on summons and holds 20 for thirteen ticks: about 26 deliveries in flight, 520 of capital, plus audit seats. Ω₀ = 300 is spent by about tick 60 of the stress; summonses are refused for Ω's money, not policy; requests wait past $T_s$; rebates accrue at 1 a tick each. A request posted at tick 600 gets its verdict at 614: six ticks late, rebate 6 settled at the verdict against its pay-in of 37 — or recorded as Ω's liability if Ω is empty. **On-time share at 80/20: well under half at Ω₀ = 300; near full at 1,000.** That is the reading §3 expects, and it is a statement about ELEF's float, not about the rules.

**The network rating at tick 1,000 — the figures §8.1 is to reproduce or refute. 60/40:** on-time about 95%, mean lateness about a tick, rebates paid a few tens, liability 0, open late 0–1. **80/20, Ω₀ 300:** on-time under half, mean lateness near ten, rebates paid in the low thousands, a liability in the hundreds, open late a few tens. **80/20, Ω₀ 1,000:** on-time above 90%, liability 0, Ω's minimum balance in the low hundreds.

**The panel at tick 120, fixed 60/40.** The world's first plant was adjudicated at tick 9, so §2.4 is live. A stamper has approved two bad plants ($n=2$, undetermined); under 1.5.0 it could take a probationer's pinned audit and stamp it; under §2.4 it holds initial seats only. The audit goes to a determined careful member if one is free — at tick 120 perhaps two of the eight are — or, after $w_R$, to a troop; in this first period most panel seats are troops'. The stamper's third and fourth bad plants determine its record at $\hat a=0.83$; it is suspended having never sat on a panel. By tick 200–300 the careful eight are determined, the panels are theirs again, and the comparisons against run 7 begin.

**The clock with no verdict.** A member awarded at tick 700 misses its deadline; the case is final N at 712 with no review. Its clock stops at 712: twelve ticks, four late, rebate 4 settled at the final against the pay-in the requester recovers anyway.

---

## 7. Implementation note (no code here)

- **One flag per rule**: `service_clock`, `omega_backs_fund`, `seat_the_queue`, `panel_determined`, `reserve_periods` in `Params`, all on by default; `--rules 1.5.0` turns them off together (and keeps `A_T` at its 1.5.0 default — `omega_backs_fund=False` means "$A_T$ binds"). Run 7 could attribute because 1.5.0 changed one thing; the flags are what let run 8 attribute five.
- **Service clock**: per root request, `t_post` (exists) and the clock's stop — `_initial_verdict` (F or N; P and ⊥ are responses) or `_finalize_N` without one; the clock excludes ticks while $\beta<\bar B$ by a counter in the per-tick loop over open requests; lateness and the rebate computed at the stop; the rebate as one transfer Ω → requester, or an `omega_liability` counter with the tick it accrued, serviced in Ω's order; per-period readings (on-time share, mean lateness, rebates paid, liabilities by age, open late). `withdraw_unawarded` settles nothing.
- **Priority**: the summons passes and the review assignment already iterate live cases in creation order; the stamping and adaptive drivers award members in case-id order — stated and checked (I26), nothing new.
- **Ω's order**: one function applies §2.2's order each tick: compute the plant reserve from the period's plant rate and ticks remaining; service liabilities older than a period; advance for inspection seats, then deliveries, from the balance above the reserve; service younger liabilities. Readings for Ω's unlocked balance, its period minimum, the reserve, advance outstanding, plants unfunded for want of Ω, refusals for Ω's money.
- **Inspection first**: `_summon_troops` runs its review-seat loop before its delivery loop; the delivery carry check tests `cost + G + 2*(c_T + G_V)` against `fund.U + omega_available_advance`; the advance drawn is `max(0, cost + G − fund.U)`; `need` for the demand stock stays the delivery's own 20.
- **Seat the queue**: at each rotation the reserve target is `max(X_t, waiting_reviews + period_initial_rate)`; fill order unchanged; probationers seated as far as the queue needs; I9's amendment is the predicate.
- **Panel eligibility**: `panel_eligible(actor) = duty_eligible and not probationer and (not world.first_plant_adjudicated or determined(actor)) and record_passes(theta_panel)`; the summons for a panel seat applies the same. Reviewer-authored worlds never plant and are untouched; the implementer's own tests that plant and seat an undetermined member on a panel are revised, with the reason.
- **$R_T$**: two-period window restored over 1.5.0's $D_s$ (both halves exist).
- **Tests**: `test_v16.py` — the clock, its exclusion, and its stop at a final without a verdict; priority as a checked order; the rebate at the stop, its cap, the liability path and its age, nothing on `withdraw_unawarded`; Ω's order with the plant reserve (a plant is never refused while a summons was advanced in the same tick); inspection-first and the delivery check (atomic refusals; the advance drawn on 20); $X_t$ on the queue; panel eligibility dormant then live; $R_T$ over two periods; the §6 figures.
- **Drivers**: columns for the network rating, Ω's readings, seat counts (probationers seated, members seated, troop seats, panels held by troops), members' income by source, the route-and-kind reading of 1.5.0 §2.3; `--duty-cap {half,twothirds,all}`; `--omega0`; `--T-s`; `--beta` per request share for the below-market poster; `--rules 1.5.0`.
- **Goldens** re-pinned once; the equivalence scenario plants, so §2.4 reseats its panels.

---

## 8. After acceptance — the runs

**Every comparison against run 7 is read from the second period on** (§2.4); the first period is Hypothesis 5's.

1. **One factor at a time**: at 60/40 against `--rules 1.5.0`, each of the five flags on alone — reviews waiting, open-case queue, vesting, state's share, panels held by troops, on-time share, Ω's readings. A hundred runs that say which rule did what; if `seat_the_queue` alone unbinds the seat, that is known before Ω's backing is judged.
2. **Reproduce §6** (the 60/40 and 80/20 figures, both Ω₀), with the five on.
3. **Tipping under 1.6.0** against run 7: reviews waiting and the open-case queue (Hypothesis 1), vesting against the ceiling, the state's share, on-time share and lateness (Q15), rebates and Ω's minimum balance, plant reserve and advance (Q16), plants unfunded for want of Ω (must be zero), members' awards, false approvals by route and kind (Q14).
4. **The cap**: $\lceil E_t/2\rceil$ / $\lceil 2E_t/3\rceil$ / $E_t$ at 60/40 and 80/20 — vesting, state's share, members' income by source, honesty (Hypothesis 6) — for Baruchi's decision.
5. **Float and target**: Ω₀ ∈ {300, 1,000} × $T_s$ ∈ {5, 8, 12} at 60/40 and 80/20 (Hypothesis 2).
6. **Windows**: $w_A$ ∈ {1, 2, 5} at 60/40 (Hypothesis 3).
7. **Drift** $m_{\max}$ ∈ {2, 4} with the route-and-kind reading; $\theta_{\text{panel}}$ 0.2 / 0.15 and window 20 / 12 (Hypothesis 4).
8. **Adaptive** (Hypothesis 7).
9. **The ramp** (Hypothesis 5): the first two periods of the tipping runs, read by period — panels held by troops, Ω's advance, the state's share, on-time share, as records determine.
10. **Red team**: a requester that posts below market to run a clock (`--beta` on a share of requests; expected: the clock does not run); a flood (`--tasks`; expected: paid for at award, discounts bounded by $B$, Ω's liability is the reading); a requester that withdraws unawarded requests (expected: nothing owed, nothing gained); the decliner, the reformer, camouflage once more.

---

## 9. Provenance

**[S7] Run 7 (October 17, 2026)** — `agentic_sim/results/studies/1.5.0-reserve/`, 482 runs, engine `01b75e2`. **[I13]** The implementer's run-7 notes: the seat as the binding capacity; the queue as a never-expiring stock; the boundary sawtooth; Q14's attribution; the four items for decision (the queue, the seat, the reset, Q14) — all answered here. **[C-rev6] Design discussion (October 17, 2026).** Baruchi: "customer request never expires — this is a big problem. a customer request that is on hold for a long time is problematic for the 'network rating'. we should maybe re-queue them with priority and have the orchestrator take some of the blame in a monetary form"; "if elef controls the network and control the servers we should allow for auto-scale. i.e. send more troops out, and add more money to treasury if needed. such a case should also punish the network somehow — earn less or something. this might incentivize doing things faster." The design reviewer's expiry proposal withdrawn in favour of the clock; the members-earn-less reading declined (§1, recorded and rejected), the ELEF-earns-less reading adopted as the rebate and the working capital; the duty cap put to a sweep rather than a decision at Baruchi's call to see the numbers first. **[I14] Implementation review of rc.1 (October 17, 2026)** — seven points, all adopted: §2.4 refused every panel seat in a world that had not planted (resolved: dormant until the first plant is adjudicated; the first period's panels named as the state's; the determination arithmetic and the second-period reading in the text); §2.2 named a plant cap the engine lacks (resolved: the plant reserve, "plants unfunded for want of Ω" as a must-be-zero reading; liabilities bounded in age, with the reason advances rank above young ones stated); Hypothesis 1 asked for a rate above the ceiling (restated: the seat binds the queue); the delivery check's advance (drawn on 20); the clock with no verdict (stops at the final); "withdrawn before award"; the cold start read from every run's first periods, no arrivals process (recorded as a later design question). Smaller — one flag per rule and OFAT cells first, the dead exclusion named, the cap's bound on the liability, I26 as a bookkeeping identity, the period's rate for "expected", the cap sweep's income-by-source reading, goldens, $A_T$ as the control — adopted.

---

## Closing statement

> Seven runs in, the loop keeps itself honest with nobody watching, turns a captured market honest where its actors can learn, and lends the state's own servers where they cannot. What it had not done was admit that the inspection bench was five seats wide and had been since the first run, or that a customer could wait forever at no cost to anyone. This revision puts a clock on every request and sends the bill to the orchestrator; lets the orchestrator scale — inspection first, out of its own treasury, with the balance on the record; seats the inspectors it already had; and asks of anyone who judges a probationer that their own record be proven first. What the market cannot do, the state does, and pays for; what the state should not do — make the market unnecessary — is held off by the same rule as before: members first, at every seat, and the state's share written down where everyone can read it.

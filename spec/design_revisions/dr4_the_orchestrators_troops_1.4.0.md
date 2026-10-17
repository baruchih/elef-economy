# Agentic Economics — The Task, Verification, and Dispute Loop

## Design revision 4 — specification 1.4.0-rc.2: the orchestrator's troops

**Project:** ELEF / Agentic Economics  
**Version:** 1.4.0-rc.2 — a release candidate, not yet in force. rc.1 (October 17) was the proposal as first sent; rc.2 settles the six points of the implementation review [I10] — the audit of a troop-reviewed troop delivery as an obligation like any other, seated by a member only; the engine summons and the driver answers; the troop's cost as a resource purchase; the held case accepted and retried; why 1.4.0 and not 2.0.0; three figures — and its five smaller points. On acceptance it becomes **1.4.0**, consolidated into one standalone text, and 1.3.1 moves to history. Semver as before.  
**Prepared:** October 17, 2026 (rc.1 and rc.2)  
**Supersedes:** 1.3.1 where this document speaks; everywhere else 1.3.1 stands unchanged. (1.3.1 is 1.3.0 with the two implementer readings of run 5 applied as wording — Appendix A; a patch, confirmed and applied October 17: `spec/agentic_economics_loop_spec_v1_3_1.md`, 1.3.0 to history.)  
**Nature of this revision:** A **design revision** under §19 — the fourth since the freeze, and the first to **add a participant**: the orchestrator's own reviewers and deliverers, *troops*. It changes who may hold a seat the market cannot fill and who may take an award the market does not take; it makes a rolled audit an obligation of the case; it gives the duty fund a first charge. It adds no verdict and no challenge. **Why minor, not major:** the rules for members are untouched — what a member may do, how it is paid, how truth enters — and a troop is an instrument of a party that already exists: the orchestrator already acts as requester and deliverer in every plant and already holds the fund. A change of approach would alter what members may do or where truth comes from; this alters only what the orchestrator does when the market leaves a seat empty.  
**Design assumption, unchanged:** humans do not intervene. **New design assumption, stated:** troops bear no malicious intent — they are ELEF's own servers, honest by construction. Their *competence* is a declared parameter, not an assumption.  
**Status:** Proposed. Accompanied by the evidence that required it (§1) and the runs that test it (§8). This is the remedy for the slowness that revision 3 reserved, and it closes the probation-safety gap run 5 found, by the same mechanism.

> **Money enters with requests. Truth enters with requesters — and with the orchestrator's own planted work.**
>
> **Verification effort is a living thing.**
>
> **Inspection is membership.**
>
> **The state has servers of its own. It uses as few as it can, for as short as it can, and says how many.** *(new)*

---

## 1. Why: what run 5 found

Run 5 — 360 runs under 1.3.0, every final audit passed, truthful appeals and no disputes throughout — established that membership works and measured what it costs [S5]:

1. **The gate holds everywhere.** Stampers end 2,100–2,500 per actor poorer at every split from 50/50 to 80/20, richer in 0 of 20 seeds; the +215 of run 4 at 60/40 is gone. The channel is the award, as predicted: stampers' delivery income 3,311 → 1,221. Plain stampers were never readmitted; the reformer that behaves until readmitted and then stamps cycles twenty times a run and ends 1,700–1,970 poorer. Hypothesis 1 holds.
2. **Where actors learn, the market turns honest and then gets faster.** Under adaptive dispositions the stamper share falls to ≤10% in all 20 seeds by tick ~800 (1,468 under 1.2.0), and vesting recovers above 1.2.0's once the population is honest (7,150 against 6,800). Hypothesis 2 holds. The slowness is a property of a *captured fixed population*, not of the honest market.
3. **Where they do not, the market is honest and short-staffed.** Vesting 20–42% below 1.2.0 at fixed splits; awards unfilled for want of a free member in 816–899 of 1,000 ticks. The arithmetic is plain: at 60/40, three tasks a tick of two ticks each need six free actors; eight members with four on duty leave four. Honesty and delivery draw on the same few members. This is Q11, now measured.
4. **The fund is fair pay, not an accelerator.** Convergence was slightly faster without it (770 against 865); its effect is distributional — 8,048 paid to reviewers over 3,000 ticks instead of banked by Ω. Hypothesis 4 fails as stated. The money is right where it goes, but it is money looking for a job.
5. **Probation safety binds on member availability, not on the cap.** At $m_{\max}=2$, two thirds of the false approvals (65 of 97) are probationers' whose pinned audits found no panel-eligible member free — the members were out delivering. The approvals reached customers. Hypothesis 5 is half right: the audit load does not exceed the members' seats; the members are not there to sit in them. This leak is older than probation: the drivers have, since run 1, dropped a rolled audit that found no auditor (run 1: 647 assigned of 2,666 rolled); the reserve sized on demand narrowed it, and probation's pinned odds exposed what was left.
6. **Two implementer readings**, both confirmed as 1.3.1 (Appendix A): the members' cap yields to the reserve floor $V_{\max}+1$ as the panel floor yields to the cap; an outgoing probationer whose turn ends with no free probationer stays.

Both costs — the audit nobody was free to take and the award nobody was free to accept — are one shortage: the market's only source of capacity is its own members, and the government's only way to get work inspected or delivered is to wait for one. Baruchi's answer [C-rev4]: *the orchestrator is like the government; it has troops — not paid as reviewers, employees of ELEF; honest by construction; and ELEF should optimize to minimize the troops at any time and retract them as early as possible.*

**Classification.** A design revision motivated by two strategy findings, labelled and read on its own. It adds a participant of last resort and one obligation; it alters no settlement, verdict or challenge rule — a troop's seat settles by the ordinary rules with the fund as its wallet.

**Recorded and rejected.** Three remedies for the audit leak were weighed: *a member seat held for probationers' audits* (spends delivery capacity on standby — the scarce thing — whether or not an audit comes); *probation paused when no member is free to audit* (stalls first looks and lengthens every probationer's way back for a shortage not of its making); *a provisional approval that holds the case until a member audits it* (right in what it refuses — nothing a probationer approved vests unaudited — and adopted here as the obligation of §2.2, but on its own it converts the shortage into waiting rather than supplying what is short). The *duty levy* of revision 3 stays rejected. *Pricing a troop's delivery at the customer's ceiling* was considered and rejected (§2.3): it rewards the state for scarcity.

---

## 2. The rules

### 2.1 Troops

**Rule.** A **troop** is a reviewer or deliverer owned by the orchestrator, summoned for **one seat** and released at that seat's completion. A troop

- is **not a member**: it holds no wallet of its own — **the duty fund is its wallet** (§2.4); it has no $\rho$, no $\kappa$, no membership state, no plant record, and no capacity of its own; it is never on duty in the reserve, never counts toward $E_t$, the duty cap or the panel floor, and is never selected — it is **summoned** (§2.2, §2.3);
- is **honest by construction** and **fallible by declaration**: a troop reviewer's verdict is the truth with probability $1-\varepsilon_T$, $\varepsilon_T$ a declared default (careful's 0.05); its verdict may be appealed by the actor and challenged by the requester exactly as any verdict, and when it is overturned the fund pays the court fee and the rest of the bond burns, as for any reviewer;
- **accepts every verdict on its own work**: a troop never appeals, never disputes, never revises, never delegates, never posts a nested request;
- is paid as a reviewer is paid and bears what a reviewer bears, with the fund as its wallet: at summons the fund **spends the troop's declared cost** ($c_T$ for a review, $c^D_T$ for a delivery) as a **resource purchase** (baseline §4.4: the credits are burned and the real cost — ELEF's servers — is paid from the reserve, value-neutral; not a bond burn, which removes credits against nothing and raises $v_t$; I3's two burns stand) — and posts the bond $G^V$ or the guarantee $G$ from the fund; at completion its expenses are reimbursed from the allowance $\varphi^E$ up to $K$ as any reviewer's; at settlement the fee, the price, a court fee won, a released bond or guarantee go **to the fund**, and a forfeited guarantee or burned bond leave it;
- **claims no emission and no uplift**: a troop's role weight is not minted (as unclaimed emission is not) and is excluded from the batch's uplift distribution;
- **never reviews a plant and never acts in one**: a plant whose seat finds no market reviewer waits; the orchestrator does not test itself;
- is **recorded as a troop** in the History — troop id, seat kind, case, tick of summons, tick of release. The reviewer's view (1.2.0 §14) and the actor's view are unchanged: a party sees of a troop what it sees of any reviewer.

**Consequence.** A troop adds a trust assumption only about ELEF's own servers, and ELEF is already the party trusted to plant honestly, keep the chain and rule on splits. It adds nothing a member could envy: no awards competed for, no reputation, no emission, no uplift, no seat in the reserve.

### 2.2 Summons for a seat: a rolled audit is an obligation; the last resort after a window

**Rule — the obligation.** **A rolled audit is an obligation of the case.** From the roll, the case's window does not close and the case does not vest until the audit completes; it is seated by a panel-eligible on-duty member when one is free, as before. This holds for every rolled audit — pinned or adaptive — and ends the dropped audit.

**Rule — summons.** A review seat the rules require — an initial review, an audit, an appeal review, a dispute panel seat — that has gone **unfilled for $w_R$ ticks** is taken by a troop, when the fund can carry it (§2.4). A seat is unfilled at a tick when, after that tick's seating of the reserve (1.3.0 §2.3, turns refilled by kind), no on-duty reviewer eligible for that seat is free to take it. The clock runs from the moment the seat was required: submission for an initial review, the roll for an audit, admission for an appeal, filing for a dispute. A troop takes **that seat only** and is released at the review's completion. **One audit no troop takes:** the audit of a troop reviewer's approval of a troop's delivery (§2.3) — the orchestrator does not audit itself — so that seat is the one that may wait past its window for a member.

**Rule — the engine summons, the driver answers.** The summons is a **Rule the engine applies** at the tick's seating step: the engine can see that a required seat has waited $w_R$ ticks with no free eligible on-duty reviewer, or that a root request has waited $w_A$ with no free fundable member (§2.3), and that the fund can carry the cost; it creates the troop, posts its bond or guarantee, spends its cost and records the summons in the History. The troop's **verdict and delivery are the driver's**: a declared disposition — the truth with probability $1-\varepsilon_T$, delivery failing at $b$ — supplied through the ordinary review and submission operations on the troop's seat, exactly as every member's verdict is. The engine has no roll, no selection and no truth; the driver has all three; this keeps that division. A run that answers for a troop otherwise than it declares produces an implementation effect, declared under §18.2.

**Rule — the roll is an engine operation.** The driver's audit roll now calls an engine operation that records the obligation on the case; the driver no longer drops a roll that finds no auditor. This is also a **conformance correction of the drivers** — since run 1 they have dropped such rolls because the engine offered no way to hold a case for one — and it changes the audit counts of the 1.2.0 and 1.3.0 controls in every run after this revision, troops on or off. The controls are re-run with the roll held before they are compared.

**Rule — a seat the fund cannot carry** stays unfilled, counts as **troop shortfall** (a reading, §2.5), and the case waits; an audit's obligation keeps holding the case, and the summons is retried at every tick's seating until a member is free or the fund can carry it. **This holding is accepted.** The actor's capacity was released at the verdict; its guarantee stays locked and the requester's price and pots stay in escrow until the audit completes. That is the honest outcome — a case nobody could check is not paid — and troop shortfall counts the ticks it holds. Nothing a probationer approved vests unaudited — by a member, by a troop, or not at all.

**Rule — panels.** A troop may hold an appeal or dispute seat under this section, so a challenge may be decided by a member and a troop, or by two troops. §2.1's honesty by construction makes that admissible; a split between a member and a troop goes to the orchestrator's ruling as any split does. A troop never sits on a plant's panel — plants carry no challenge, so there is none to sit on.

**Consequence.** Every pinned audit is served: by a member within the window, by a troop after it. Probationers' false approvals fall to the audited residual — the share a 95%-accurate auditor misses — instead of the share that found no auditor. A probationer loses nothing: its reviews are assigned as before; the troop takes only what no on-duty reviewer could.

**Why a window, and why not zero.** Reviews wait a tick or two in every run since run 1 (reviews waited in 92–96% of ticks at $X=4$); a troop summoned at the first tick of waiting would take the market's ordinary slack and never retract. $w_R$ is the knob that says how long the customer waits before the state steps in. Its default is **2 ticks** — in every driver so far a review completes the tick after assignment, so that is two review durations, not one — and it is swept.

### 2.3 Summons for an award: the state delivers what nobody takes

**Rule.** A root request that **no eligible member has been awarded within $w_A$ ticks of its posting** — because no member free to commit and able to fund the guarantee offered — is awarded to a troop, when the fund can carry it, **at the trailing market price** $\bar B$: the mean price awarded to members over the trailing period, the ceiling $\beta$ when there is none. A troop is summoned only for a request whose ceiling admits the market price, $\beta\ge\bar B$; a request priced below the market is not a shortage and waits. The requester pays in exactly as for any award ($\bar B+\varphi^E+\varphi^F+\omega_t$); the troop's guarantee $G=\lceil 0.5\bar B\rceil$ is locked from the fund; the troop delivers once, **within the ordinary commitment**, and its submission is reviewed as any submission — by the on-duty reserve, round-robin; by a troop reviewer only under §2.2. The troop is released at the case's vesting or final settlement.

**Rule — members first, always.** A troop never takes an award a member offered for, never takes a seat a member or probationer is free to fill, and is never preferred to one on price, reputation or duty credit. The window is the whole of the market's chance; nothing shortens it.

**Rule — the state's work is seen by the market.** An approval of a troop's delivery given by a troop reviewer carries audit odds 1. That audit is **an obligation like any other** (§2.2) with one difference: **only a member may take it** — no troop audits the state's own work — so it is the one audit seat that may wait past its window. The case is held until a member completes it; the History counts cases **held for the market's audit** and their age (§2.5). In a corner with no member alive the case holds indefinitely, which is the honest outcome: the requester has the work in hand (approval released the troop's seat and the case is pending), and what waits is the fund's own price. There is no exception to the obligation anywhere.

**Consequence.** At 60/40 and three tasks a tick, four free members deliver two; the third goes to a troop after $w_A$ ticks. The customer is served at the market price; the member who would have had it did not exist. ELEF's income from the delivery is the fund's, not Ω's (§2.4): the surplus over the troop's cost pays the next troop, and what no troop needs goes to the market's reviewers as uplift. The state does not profit from scarcity; the market does.

**A limit of the drivers, not of the rule.** In every driver so far each offer is at the ceiling, so $\bar B=\beta=20$ always and "$\beta\ge\bar B$" never binds in the §8 runs; it binds only once price competition is in scope (§18.1 question 2).

### 2.4 The fund carries the troops first

**Rule.** The duty fund of 1.3.0 §2.4 is the troops' wallet and keeps its name. **In:** the raised tax $(m_t-1)\,\omega_0 B$ per award, as before; every troop's earnings — fee, price, court fee won, released bond or guarantee. **Out, in this order each tick:** (1) troop costs at summons and bonds or guarantees posted; (2) repayment of any advance from Ω (below); (3) at each settlement batch, the **uplift** of 1.3.0 §2.4 — distributed exactly as before, but only from the fund's **unlocked balance above a reserve** $R_T$, where $R_T$ is the largest capital troops had tied up at once during the trailing period (costs spent plus bonds and guarantees held). At rest, $R_T=0$ and the whole fund flows to the reviewers as in 1.3.0; under stress the fund keeps one period's worth of troops.

**Rule — the advance.** When the fund cannot carry a summons, Ω advances the difference from its unlocked balance, up to $A_T$ outstanding; the advance is repaid first from the fund's inflows. Beyond $A_T$ the summons fails and is counted (§2.2, §2.3). Ω keeps the base rate $\omega_0 B$ and the plant capital, as before; nothing a troop earns reaches Ω except by repayment of an advance.

**Consequence.** The state's reach is its treasury: what the dial has levied, what its own troops have earned, and a bounded float — never more. Stress raises $m_t$, $m_t$ raises the surcharge, the surcharge pays for the force that answers the stress; as the stress passes, troop usage falls, $R_T$ falls with it, and the money returns to the reviewers. The dial sizes the army without a second dial. ELEF's conflict of interest — troops earn the fund a fee and a price — is answered structurally: the window, members-first, cost at summons, and no route from the fund to Ω.

### 2.5 Minimization is a rule, and a reading

**Rule.** No troop persists: one seat, one summons, released at completion, nothing carried over; a turn vacated in the reserve is refilled by kind from members and probationers before any troop is summoned; a troop is summoned only for a seat or an award that has waited its window. The History carries, per period: **troop-ticks** (review seats and deliveries separately), **troop shortfall** (seats and awards no troop could be summoned for, and the ticks cases held for want of one), **cases held for the market's audit** (count and age), the fund's balance, reserve and advance. In an honest population at rest every one of these reads zero; a nonzero reading is a stress gauge, like the dial, not a feature.

**Consequence.** There is nothing to size and nothing to retract, because nothing persists: the number of troops at any tick *is* the shortfall at that tick, after the market has had its chance.

### 2.6 Defaults

| Default | Value | Note |
|---|---|---|
| $\varepsilon_T$ | 0.05 | a troop reviewer's error rate; careful's |
| $w_R$ | 2 ticks | review seat window — two review durations in the drivers so far; swept $\{1,2,4\}$ |
| $w_A$ | 2 ticks | award window, one task's duration; swept $\{1,2,5\}$ |
| $c_T$ | 3 | a troop review's cost to the fund, spent at summons; the top of careful's $\{2,3\}$; reimbursed up to $K$ |
| $c^D_T$ | $\lceil 0.5\bar B\rceil=10$ | a troop delivery's cost to the fund; **no empirical anchor** — members' delivery has no cost in the drivers; swept $\{5,10,20\}$ |
| Troop price | $\bar B$, trailing mean awarded price over the period; $\beta$ if none | summoned only when $\beta\ge\bar B$ — $=\beta$ in the drivers so far |
| $R_T$ | peak troop capital over the trailing period (200 ticks or 50 adjudicated plants, as the dial's) | |
| $A_T$ | 100 outstanding | Ω's advance to the fund — five troop deliveries' capital, about one tick's demand at 80/20; swept $\{100,300\}$ |
| Troop delivery failure | the base rate $b$, as any delivery | competence is not assumed |

All are defaults. Every member's figure in the drivers — a careful review at 2–3, delivery at 0 — is unchanged, so the comparisons of runs 1–5 carry over.

---

## 3. Consequences and hypotheses

**Hypothesis 1 — the audit leak closes.** Under 1.4.0 a probationer's every approval is audited, by a member or a troop. Its false approvals fall from "those that found no auditor plus those an auditor missed" to the second term alone: at 95% auditor accuracy, about one in twenty of its stamped bad work. Run 5's 65 probationer false approvals at $m_{\max}=2$ fall by most of their number; troop review seats measure how many audits the market could not take.

**Hypothesis 2 — the slowness is supplied.** At fixed splits, vesting recovers toward the 1.2.0 control (2,399–2,412 at 50–70%) with troops delivering the awards the members could not: about a third of tasks at 60/40, two thirds at 80/20. The state's share rises with capture — that is the reading. Customers' waiting time at the award falls from "most ticks" to the window.

**Hypothesis 3 — minimization under adaptation.** In the adaptive population, troop-ticks fall to zero as the stamper share falls, and the tick at which they reach zero is close to the tick at which the population is honest (~800). If troops persist after the market is honest, the windows are too short or the market's own slack is being taken; the sweep says which.

**Hypothesis 4 — no crowding out.** Members' award counts and delivery income at every split are unchanged from run 5: a troop takes only what was unfilled. The stamper − careful gap keeps its **sign**; its **size changes by the uplift** — troops' earnings flow to the fund and from it to the reviewers, so the honest gain and the gap widens by about that much. A gap that widens is not a failure of this hypothesis; a member whose award count fell is.

**Hypothesis 5 — the fund carries it.** At the defaults the fund is net positive per troop seat — a review nets about $+2$ (fee, with cost reimbursed), a delivery about $+4$ in expectation ($0.8\times(\bar B-c^D_T)-0.2\times(c^D_T+G)$) — so the treasury bounds *simultaneous* troops (through $R_T$ and $A_T$), not their number over time, and troop shortfall at 60/40 is zero at the defaults. The sweep of $c^D_T$ finds where the fund fails to carry.

**Hypothesis 6 — the state's work is seen.** Cases held for the market's audit are few and short-lived at every split with members on duty — a member takes the seat within a few ticks of its window — and grow old only in an all-troop corner. If they are many or old at 80/20, the duty cap is the suspect: members held free to deliver are not free to audit the state, and the cap's default is the knob.

**Limit, restated.** The accuracy bar stands for members. For troops it is a declared $\varepsilon_T$: the runs sweep it, and a troop worse than a careful member is a finding against ELEF's servers, not a rule.

**Open, deliberately.** Whether troop usage should feed the dial (as plant failures do) is not decided here; troop-ticks are a reading first. Whether the duty cap should loosen now that the floor is the state rather than "whoever is free" is a default question for the sweep after this revision is in force.

---

## 4. What does not change

Everything in 1.3.1 not named above: membership, probation and its pin, the duty cap and the panel floor, reserve sizing on applied odds and fill order by kind, plants, the record and its two thresholds, the dial, the alarm, the actor-less view, the two pots and settlement, verdicts, challenges, delegation, $\rho$ and $\kappa$, overrides and grades. The uplift is distributed as before; what it is distributed from has a reserve.

---

## 5. Invariants, notation (amendments)

**I24 (new) — troops.** A troop holds exactly one seat from summons to release and no seat thereafter; a troop holds no $\rho$, $\kappa$, membership state, plant record, emission or uplift; no troop reviews a plant or acts in one; a troop is summoned only by the engine, only for a seat or award that has been unfilled for its window after the tick's seating, and only when the fund (with the advance) can carry its cost and bond; no troop takes the audit of a troop reviewer's approval of a troop's delivery; no troop appeals, disputes, revises or delegates; a troop's delivery is at $\bar B$ and only where $\beta\ge\bar B$.
**I25 (new) — the obligation.** A case with a rolled audit outstanding does not vest — without exception; a probationer's or undetermined newcomer's approval vests only after its audit completed; an approval of a troop's delivery by a troop reviewer carries audit odds 1 and its audit is a member's.
**I23 (amended) — the fund.** The fund equals the raised tax plus troop earnings plus advances, less troop costs purchased, uplifts paid and advances repaid (conservation, with I1; a troop's cost is a resource purchase under I3 and §4.4 — value-neutral, not a bond burn); uplift is paid only from the unlocked balance above $R_T$; the advance outstanding never exceeds $A_T$; a troop's role weight claims no uplift.
**I22 (amended) — membership.** No award is made to a suspended actor or a probationer; an award to a troop is made only by summons under §2.3.
**I9 (amended).** The eligibility shortfall counts seats unfilled by the market after seating; troop seats are counted separately as troop-ticks, and seats no troop could take as troop shortfall.

**Notation (Appendix C additions).** troop; $\varepsilon_T$; $w_R$, $w_A$; $c_T$, $c^D_T$; $\bar B$; $R_T$; $A_T$; troop-ticks; troop shortfall; held for the market's audit.

**§18.1 (amended).** *Q11* is answered by this revision and measured in §8. *New Q12*: the state's share — troop-ticks per tick at each split, its trajectory under adaptation, and the tick at which it reaches zero. *New Q13*: the fund under troops — balance, reserve, advance drawn, uplift paid, and where the treasury fails to carry.

---

## 6. Worked example

Twenty actors, 60/40 careful to stamper, defaults, $m=2$, tick 500: eight members (four on duty under the cap, four free), twelve probationers on duty for initial reviews, every probationer approval audited.

**An award.** Three tasks a tick, two ticks each: six free actors needed, four exist. One request a tick finds no member. At tick 502 the request posted at tick 500 is still unawarded; $\beta=20\ge\bar B=20$; a troop $\tau_{41}$ is summoned. The fund spends $c^D_T=10$ and locks $G=10$; the requester pays in $20+10+5+2$ as for any award. $\tau_{41}$ delivers at tick 504; a probationer reviews it (round-robin), approves; the approval's pinned audit is rolled — the case is held.

**The audit.** At tick 504 the four on-duty members are all mid-review. Tick 505, 506: still none free — the seat has waited $w_R=2$. Troop $\tau_{42}$ is summoned for the audit: the fund spends $c_T=3$ and locks $G^V=5$. $\tau_{42}$ finds the work good (truth, w.p. 0.95), the audit stands; at settlement the fund is reimbursed 3 from $\varphi^E$, receives the audit fee 3, and the bond is released. Net to the fund from the seat: $+3$. The case vests at the window's close; $\tau_{41}$'s price 20 reaches the fund and its guarantee is released: net $+10$. Had the delivery failed (w.p. $b=0.2$), $\tau_{42}$'s audit would have challenged the approval; the split goes to a second review and a ruling by the ordinary procedure (the second seat a member's, or a troop's after its window), and when the overturn stands the probationer loses its bond and $\rho$, as under 1.3.0, the troop accepts the verdict on its work, and its guarantee goes to the requester: net to the fund $-20$.

**The probationer that stamps.** C, a probationer, approves bad work at tick 510. Under 1.3.0 its audit found nobody and the approval reached the customer. Under 1.4.0 the case is held; a member takes the audit at tick 511 or a troop at 512; the audit challenges, the challenge runs its course, and when it stands C loses its bond, its $\rho$ falls, and the customer is not paid for failed work. C's record is unchanged by this — plants decide the record; the audit decides the case.

**The fund.** Per tick at this split: surcharge $3\times1=3$; about one troop delivery ($+4$ expected) and one troop review ($+2$ to $+3$); call it $+9$ a tick against 1.3.0's $+3$. Troop capital outstanding at a time: about two deliveries and one review, $2\times20+8=48$; $R_T\approx50$. The uplift above the reserve, shared by role weight across about four settling reviews a tick, is about 2.25 per unit of weight — three times run 5's — paid to the members and probationers doing the reviewing. Ω's advance is drawn in the first ticks of stress (the fund starts the period near its reserve) and repaid within a few.

**The readings at tick 500.** Troop-ticks: about 3 a tick (two deliveries in flight, one review). Troop shortfall: 0. Held for the market's audit: 0 — every troop delivery here was reviewed by a probationer, a market actor, so no troop-on-troop audit arose. In the adaptive run at tick 900, the same row reads 0, 0, 0.

**Who did what.** The engine summoned $\tau_{41}$ and $\tau_{42}$ at the seating step of ticks 502 and 506 and recorded both; the driver supplied $\tau_{41}$'s submission and $\tau_{42}$'s verdict through the ordinary operations, from the declared troop disposition. Had the driver answered otherwise — a troop that always approves, say — that would be the driver's declared effect, not the rule's.

**At 80/20.** Four members, two on duty, two free: capacity one task a tick against three; troops deliver two of three. The state is most of the market — and says so.

---

## 7. Implementation note (no code here)

- **Troop identity**: a troop id per summons, sequential, with seat kind, case, tick of summons and release in the History; the fund as its wallet in every flow; a single-use identity outside I14 and the record's rotation events.
- **The summons is the engine's**: at the tick's seating step, after turns are refilled by kind, the engine checks each required seat's wait against $w_R$ and each unawarded root request's against $w_A$, the free-eligible-reviewer and free-fundable-member conditions, $\beta\ge\bar B$, and the fund's carrying capacity with the advance; it creates the troop, posts its bond or guarantee, purchases its cost, seats it or awards to it, and records the summons. No driver call reaches a troop seat except the troop's own verdict (`complete_review`) or submission (`submit`), supplied from the driver's declared troop disposition ($\varepsilon_T$, $b$). The seat of a troop reviewer's approval of a troop's delivery is never summoned for; it waits for a member.
- **The obligation**: the driver's roll calls an engine operation that records an audit obligation on the case — the same shape as the existing vacated-audit hold (`open_items` / `audit_vacated`), one step earlier; the pending window does not close while one is outstanding; `assign_audit` discharges it; a case with one outstanding cannot vest (I25). The driver no longer drops a roll that finds no auditor (`audits_lapsed` goes to zero by construction); the 1.2.0 and 1.3.0 controls are re-run with the roll held.
- **Windows**: a seat's required-since tick and an award's posted-at tick; $w_R$, $w_A$ as params; a summons that fails for want of funds is retried at every seating step and counted.
- **Cost and bonds**: the fund purchases $c_T$ / $c^D_T$ at summons through the existing resource-purchase operation with the fund as the wallet (I3, §4.4 — value-neutral); reimbursement from $\varphi^E$ up to $K$ at completion as for any reviewer; bond and guarantee locks on the fund; settlement routes a troop's fee, price, court fee, released lock to the fund.
- **Emission and uplift**: a troop's role weight excluded from both; the uplift paid from unlocked balance above $R_T$; $R_T$ tracked per period as peak troop capital; the advance as a lock on Ω's side with an outstanding counter capped at $A_T$ and repaid before uplift.
- **Plants**: the plant round-robin skips troops (there is nothing to skip — troops are not on duty); a plant's unfilled seat never summons; a troop never receives a plant's award.
- **Troop reviewer behaviour**: a Protocol in `strategies.py` like any disposition — truth with probability $1-\varepsilon_T$; no appeal, dispute, revision or delegation on its own work. A troop's delivery fails at $b$ as any.
- **Readings**: troop-ticks (reviews, deliveries), troop shortfall (seats, awards, held ticks), cases held for the market's audit (count, age), fund balance/reserve/advance — in the History per period and in the drivers' columns.
- **Tests**: `test_v14.py` with the §6 figures; summons refusals (window not elapsed, member free, $\beta<\bar B$, fund cannot carry, the troop-on-troop audit seat — atomic); the obligation holding a case, with no exception; troop flows and conservation under I3; no emission/uplift to troops; plants never to troops; readings. Driver tests for the dropped-roll path are revised: a roll that finds no auditor now holds the case. Goldens re-pinned once.
- **Defaults**: §2.6 as params; the sweeps of §8.

---

## 8. After acceptance — the runs

1. **Reproduce §6.**
2. **Controls re-run with the roll held**: 1.2.0 and 1.3.0 at the run-5 cells, troops off — the audit counts and false approvals the dropped roll was hiding. Every later comparison is against these.
3. **Tipping point under 1.4.0**: 50/60/70/80 fixed splits, 1,000 ticks, against the re-run controls — vesting (Q11), the state's share (Q12), false approvals by probationers (Hypothesis 1), the gap's sign and the uplift's part in its size (Hypothesis 4), the fund (Q13).
4. **Adaptive dispositions**: 1.4.0 against 1.3.0, 3,000 ticks — convergence tick, and the troop-ticks trajectory to zero (Hypothesis 3).
5. **Drift** as in run 5, $m_{\max}\in\{2,4\}$: probationers' false approvals with every audit served.
6. **Windows and the float**: $w_R\in\{1,2,4\}\times w_A\in\{1,2,5\}$ at 60/40 — troop-ticks, vesting, customers' wait; $A_T\in\{100,300\}$ at 80/20 — advance drawn in the first stress, troop shortfall.
7. **Cost and competence**: $c^D_T\in\{5,10,20\}$, $\varepsilon_T\in\{0.05,0.10\}$ — where the fund fails to carry; what a worse troop costs in false approvals.
8. **Red team**: the camouflaged stamper and the reformer re-run under 1.4.0 (expected: no new yield); a member that declines awards to collect uplift (expected: none — uplift falls under stress); a requester that posts below the market to be served by a troop (expected: waits — not exercised while offers are at the ceiling); an all-troop corner (10/90 and worse) for cases held for the market's audit and their age.

---

## 9. Provenance

**[S5] Run 5 (October 17, 2026)** — `agentic_sim/results/studies/1.3.0-membership/`, 360 runs, engine `91a49e5`; hand-off sections "Design revision 3" and "Run 5". **[I9]** The implementer's run-5 notes: the two readings (confirmed, Appendix A); the three items for the next decision — the slowness, probation safety on member availability (candidates: a held member seat; probation paused), and the readings. **[C-rev4] Design discussion (October 17, 2026).** Claude proposed the provisional approval (adopted as the obligation of §2.2; recorded and rejected as a remedy on its own). Baruchi: "so we have an orchestrator, and in a sense he is like 'the government'"; asked what a government does in a riot; "it's like the 'orchestrator's troops'. with a special case. those troops are not paid as reviewers. not really in the end, they are employees/soldiers of elef in a sense"; "elef reviewers should be honest. or at least constructed as such by elef (that is a task for another time), but we can assume that elef's troops bear no malicious intent. these are 'elef servers'"; "elef should optimize to minimize the troops at any time and should retract them back as early as possible." Claude's shape — no standing force, members first, windows, no emission, a public reading, the dial's surcharge as the funding — accepted; three rungs (audits, shortfall seats, unfilled awards) and 1.4.0 as the version agreed. **[I10] Implementation review of rc.1 (October 17, 2026)** — every run-5 and run-1 figure and the §6 arithmetic checked; six points: §2.3's "unverified by the market" contradicted §2.2 and I25 (resolved: the obligation holds without exception, a member only takes that seat, the reading is cases held for the market's audit — the reviewer's 1(a) and 6(c) together); the engine summons and the driver answers; the troop's cost is a resource purchase under §4.4 and I3, not a bond burn; the held case accepted and retried; why minor; $w_R$ is 2 ticks not $\bar d$, $\bar B=\beta$ in the drivers, no troop audits the state's own work — all adopted in rc.2; and five smaller — the obligation as a conformance correction of the drivers (controls re-run), panels with troops, $A_T$ named and swept, Hypothesis 4's size, 1.3.1 applied — adopted.

---

## Appendix A — the 1.3.1 sentences (applied October 17; `spec/agentic_economics_loop_spec_v1_3_1.md`)

For 1.3.0 §2.3, after "The panel floor yields over the cap, bounded by availability":

> *The members' cap yields to the reserve floor $V_{\max}+1$ as the panel floor yields to the cap: a reserve that cannot seat $V_{\max}+1$ fresh reviewers cannot run the loop, so at memberships of four to seven the floor wins; at larger memberships the two agree.*

For 1.3.0 §2.3, "Rule — turns", after "an initial-review seat by a probationer first":

> *An outgoing probationer whose turn ends with no free probationer stays, rather than being replaced by a member the next tick's "probationers first" would hand back.*

---

## Closing statement

> Run 5 showed the gate holds and the honest market, where it can learn, turns honest and then gets faster. It also showed a captured market that is honest and short of hands — short of an auditor when a probationer approves, short of a deliverer when a customer posts. This revision gives the orchestrator what every government has and the loop did not: servers of its own, used last, used briefly, paid from the tax the dial already levies, and counted in public. The market comes first, always; the state fills what is left, and says how much that was.

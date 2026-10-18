# Agentic Economics — The Task, Verification, and Dispute Loop

## Major revision — specification 2.0.0-rc.3: the price of work

**Project:** ELEF / Agentic Economics  
**Version:** 2.0.0-rc.3 — a release candidate, not yet in force. rc.1 (October 18) was the sketch as first sent; rc.2 settled the seven points of the implementation review [I17]; rc.3 settles the three of the rc.2 review [I18] — the riot defined as a crowd of requesters; $N_T=40$, clear of the quiet field at every split; issuance 10 as the default so the worked example and the default agree — and carries its four implementation readings and smaller points into the text. On acceptance it becomes **2.0.0**, consolidated into one standalone text, and 1.7.1 moves to history. The first **major** version: *a change of approach.*  
**Prepared:** October 18, 2026 (rc.1–rc.3)  
**Supersedes:** 1.7.1 where this document speaks; everywhere else 1.7.1 stands unchanged — and that is most of it: every rule about honesty, membership, inspection and the state's troops stands.  
**Nature of this revision:** A **change of approach** to money. Through eleven runs the price of a task was fixed by fiat at the customer's ceiling, demand was a constant with a bottomless wallet, and credits were a scoreboard — the backing index $v_t$ moved from 1.0000 to 0.9995 in a thousand ticks against a driver's backing of $10^7$. This revision makes the price of work **float**: customers with finite wallets choose what they will pay, members bid, the price level is what clears. On that footing it gives **inflation** a meaning, **decouples the servers** from the economy (the state's capacity is a parameter outside the ledger; the state is never broke — it runs a deficit, read in public, and retires it), and retires the fictional backing and the solvency machinery of 1.5–1.7 that stood in for it. Giving actors something to buy — delegation — is **deferred to 2.1.0**, because a market in sub-work needs costs that differ across actors, and that is competence, a revision of its own.  
**Design assumptions, unchanged:** humans do not intervene; troops bear no malicious intent. **New, stated:** the economy is closed — nothing is redeemed and there is no backing; a credit is worth what it buys inside the loop; ELEF's servers are outside it; and the agents' effort costs are their own reservation prices, outside it too.  
**Status:** Proposed. Accompanied by what required it (§1) and the runs that test it (§8).

> **Money enters with requests. Truth enters with requesters — and with the orchestrator's own planted work.**
>
> **A credit is worth the work it buys. Nothing else.** *(new)*

---

## 1. Why: what eleven runs could not say

1. **Every run was priced by fiat.** Every offer was at the customer's ceiling $\beta=20$ and the customer never ran out. The selection rule has penalized price since v1.0 ($\arg\max[S_\theta-\lambda B/\beta]$) and no bid ever moved; the execution-cost operation (§4.6, `spend`) exists and no driver ever called it; actors may delegate since v1.0 and none ever did. §18.1 questions 2 and 5 — price and delegation — are the demand side of the economy, and the programme never touched it.
2. **So the credit was a score, not money.** With the price nailed and demand infinite, a credit could not be worth more or less than it was. "The state is broke" (runs 8–9) was never the loop breaking but a cash rule imposed on Ω as a stand-in for servers; the two accounts, $R_T$, the plant reserve and the order of payment existed to ration that cash; and the honest answer to "what if the state printed money" under 1.7.1 was that printing is free inside the loop — nothing for it to be worth less *against*.
3. **Scarcity had no signal but a queue** (run 11's hard spike: 20–40 ticks in line, unspoken to). A market says "the price is up."
4. **Baruchi's position [C-2.0]:** the servers must be decoupled from the economy or they contaminate it; inflation must mean that printing makes money worth less, so that one gets less for one's work; what is missing is something to balance the money against.

**Classification.** A change of approach: fixed price to a market; a backed credit to a credit valued by the work it buys; a rationed treasury to a public deficit. Everything about honesty is untouched. Major, by the rule.

**Recorded and rejected.** *Emergency emission against a backing*: there is no backing. *The server budget inside the ledger*: contaminates the economy; the bound is a parameter outside it (§2.6). *The busy-line protocol as a rule now*: the price is the signal; what remains is the below-market flag (§2.8) and the capacity case, which §2.6 now records when $N_T$ binds. *Effort costs indexed to the price level*: a slack market would deflate without limit — bids at cost, cost following the price — so the agents' costs stay nominal and anchor the price (§2.3). *The state's delivery at a margin* ($c^D_T=0.5\,\bar B$, the 1.x default): with the funds check moot and volume unbounded, a riot would be the state's windfall; the state delivers at cost (§2.6). *Delegation in this revision* (rc.1 §2.7): with one cost for every actor there is no gain from trade — a delegate does half the work for $B-B'$ and no child bids under its own cost — and the parent judges its child, so the disposition entangles the honesty dispositions; deferred to 2.1.0 with heterogeneous costs.

---

## 2. The rules

### 2.1 Demand: customers with wallets, the pay-in locked at posting

**Rule — requesters.** A requester is an agent with a **wallet** and a declared **budget policy**. Its credits come from **issuance** — the orchestrator credits each requester's wallet on a declared schedule, the stream "money enters with requests" names — and from its own earnings if it is also an actor. Issuance is a source of money (I1) and is recorded as one.

**Rule — the posting lock.** A root request locks, at posting, the **all-in maximum** of its pay-in: $\beta+\varphi^E+\varphi^F+\omega(\beta)$, at the index of that moment (§2.3). A request the requester cannot lock is **refused at posting** — the reading §2.1 of rc.1 wanted, now the engine's. **A root's first lock is therefore its posting**, as a nested case's already is (§4.5 amended): the case's nominals ($D,K,G^V,\varphi$) freeze there, **and so does the fee rate** — $\omega=\omega_0 m_t B$ is locked at the posting tick's $m_t$ and the case carries that $m$, so a dial that rises before the award cannot make the fee exceed the lock. At award, $\beta-B$ and $\omega_0 m(\beta-B)$ are released; at a troop's summons likewise. This is §9.1's model for nested requests, generalised to roots; the award's and the summons's pay-in checks are moot.

**Rule — a crowd.** Demand from outside the loop — a riot — is **more requesters**: $n$ requesters arrive with the default wallet and issuance and leave when the event ends, their open requests served out. Six requesters at the default policy post about three a tick, so run 11's hard spike (fifteen a tick) is a crowd of about thirty for 100 ticks, and its flood (six a tick sustained) is twelve requesters throughout. A riot is a *demand* event; the deficit shock (§8.3) is a *money* event — the same six requesters given credits — and the two are kept apart so that Hypotheses 2 and 3 measure different things. A change of posting policy is the third shape and is not used.

**Rule — the ceiling.** The requester's ceiling $\beta$ is its policy's choice, bounded by what its unlocked wallet can lock all-in. Default policy: $\beta=\min(\beta_{\max},\ s\cdot W_{\text{unlocked}})$, posting one request a tick while the all-in fits and fewer than $K_{\text{open}}$ of its requests are open.

**Rule — raising the ceiling.** A requester may **raise the ceiling** of its own unawarded request, locking the difference; it may still withdraw it (`withdraw_unawarded`). These are the only changes to a posted request.

**Consequence — the arithmetic.** A task's all-in, net of refunds, is about $1.6B$: the price, the deposit's net cost of about 8 at $P_0$ (run 10: the allowance refunded about 6 of 10 and the pot about 0.8 of 5 at tree closure), the fee $\omega_0 m_t B$ with the dial at 4. Supply at 60/40 under $N_T=40$ is the members' 1.24 a tick (run 10's awards) plus the troops' $N_T/13.4$ (a troop delivery holds its place 13.4 ticks) — about 4.2 a tick. **Issuance of 10 a tick per requester — 60 a tick — clears at $B\approx 60/(1.6\times4.2)\approx 9$**, just above the members' cost of 8, with 60/40 near capacity; issuance 15 clears near 13 and leaves every quiet cell mildly capacity-bound (the sweep). Initial wallets of 200 carry the deposit's float (about 75 per requester at tree closure) so the first period is not the float's. **$M$ at genesis**: actors $20\times50=1{,}000$, $\Omega_0=300$, requesters $6\times200=1{,}200$ — about 2,500; issuance adds 60 a tick against burns of about 40 (effort, troop costs, forfeits), so $M$ grows about 20 a tick until the price level rises enough for the all-in to absorb it. Richer requesters post more and bid higher; that is how money reaches prices. Under unbounded $N_T$ the same arithmetic gives the state about three quarters of the market at 60/40 — what §2.4's caution predicts, and the control shows.

### 2.2 Supply: members bid at or above their reservation; the state bids the market

**Rule.** A member free to commit offers a **bid** $B\le\beta$; the orchestrator selects by the existing rule, $\arg\max[S_\theta-\lambda B/\beta]$ with the $\kappa$ tie band, and the awarded price is the bid (`award` already takes it). A member bears an **effort cost** $c_D$ per unit of work — the §4.6 execution cost, a resource spend burned at submission — and its bid policy is its strategy; a bid below cost is its own loss. Default policy: $c_D(1+m)$, $m$ raised on an award and lowered after $k$ idle ticks, floored at 0.

**Rule — the state's price.** A troop delivers at $\bar B$, **the trailing mean of prices awarded to members** — troop awards have been excluded since 1.4.0 because a summons never passes through `award`; the engine's reading is now the rule, so that a state delivering most of the market cannot set its own price — and only where $\beta\ge\bar B$. The per-request summons of 1.7.1 is unchanged.

**Consequence.** With $\lambda=0.2$ a bid at the ceiling against one at half of it costs 0.1 of $\rho$ — more than the whole spread of $\rho$ among the honest in run 10 — so **price will decide every award among members**; that is the design, and Hypothesis 1 says so. With members plentiful bids fall toward cost; with members scarce, toward the ceiling; the state charges what the members charge.

### 2.3 The price level, indexing frozen per case, effort costs as the anchor

**Rule — $P_t$.** The **price level** is the trailing mean of awarded prices — members' and troops' — on the same window rule as $\bar B$ (§12.3: this period's mean if it has awards, else the last period's), $P_0=20$ before the first award. $P_0$ is the former fixed price, so every 1.x figure is at $P_t/P_0=1$.

**Rule — indexing.** Every nominal amount **the rules fix** is indexed: the fee $f$, the bond $G^V$, the court fee $D$, the pots $\varphi^E,\varphi^F$, the cap $K$, the rebate $r_s$, the troops' costs $c_T,c^D_T$, the plant pots — each its 1.x default times $P_t/P_0$, **frozen at the case's first lock** as §4.5 has always frozen a case's nominals (so a pot funded at award pays its fees a dozen ticks later in full, and $G^V\ge D$ holds for every review of the case). §4.5 stands with $P_t/P_0$ in the place of $v_0/v_t$; `ledger.index()` is that one function. The guarantee $G=\lceil 0.5B\rceil$ and the service fee $\omega_0B$ scale with the price already.

**Rule — what is not indexed.** **The agents' effort costs are not** — a member's $c_D$ and a careful reviewer's care cost (the driver's 2–3 a review) are their own reservation prices, nominal, declared in the strategy; they are the economy's anchor, as labour is. An **adaptive reservation** — a cost that follows $P_t$ with a lag, as wages chase prices — is a declared variant and a sweep (§8), so that the spiral it risks is measured, not assumed. **Emission is not** — $E_t=E_0\,2^{-t/H}$ in credits, a fixed nominal schedule whose real value falls as prices rise, and which halves on its own inside every run (read apart, Q4).

**Consequence.** A bond deters the same *work* and a review is paid the same *work* whatever the money supply: the deterrents are price-neutral. What inflation reaches is balances held, emission, and the agents' nominal costs — so when work is dear, inspection (paid at an indexed fee) is well paid against a fixed care cost, and when it is cheap the reverse; that is a real effect of the price level on the relative price of honesty, named here and measured in §8 rather than indexed away. **The credit's value is $P_0/P_t$** in tasks (`ledger.v`, kept as a reading with the backing retired); **real wealth** is $W\cdot P_0/P_t$, and every §18 reading is stated in it from here on.

### 2.4 Money: sources and sinks, no backing

**Rule.** $M_t$ is the sum of every wallet and lock. **Sources:** issuance (§2.1); emission (§2.3); state creation (§2.5) — the genesis floats are issuance. **Sinks:** bonds and guarantees forfeited and burned; resource spend (effort, troop costs — burns with no outside leg); state retirement (§2.5). **The backing $\text{Res}_t$ is retired** (held at 0 as a reading); I3's value-neutral purchase becomes a plain burn. Conservation (I1) holds over the kinds: `issuance`, `mint_emission`, `creation` in; `burn_bond`, `purchase`, `retirement` out.

**Consequence.** Whether a credit is worth more or less is the loop's own question. **One caution the text owns:** without delegation (2.1.0) members have nothing to buy, so money flows one way — from the mint through customers to members' hoards and the burns — and inflation shows in prices only when **capacity binds** (§2.6); in a slack market it shows as hoards. That is the textbook output gap, and it is why $N_T$ has a finite default.

### 2.5 The state is never broke: creation, retirement, the deficit

**Rule — creation.** Ω receives its income as before — the base fee $\omega_0B$, the troops' review fees — and pays as before — plants, rebates at the clock's stop, troop costs and locks at summons. **When Ω's unlocked balance cannot meet a payment the rules require, Ω creates the shortfall** (`creation`, a source) and pays at once. Creation is **only** for a required payment — a summons the rules call for, a rebate the clock owes, a plant the dial calls for — never a discretionary spend (I28).

**Rule — retirement, in one sentence.** **While the deficit stands, every credit that reaches Ω's unlocked balance is burned against it at once** (`retirement`, a sink): Ω's unlocked balance is zero for as long as it owes created credits, and it creates again for the next required payment. **Deficit outstanding** $=$ created $-$ retired is Ω's negative position; **Ω's net position** $=\Omega_U-$ deficit is the reading that replaces "Ω's minimum balance" (Q16); both are public.

**Retired as rules:** the advance cap $A_T$ (1.4.0); the demand reserve $R_T$ (1.5.0) and its two-period window (1.6.0); the plant reserve and Ω's order of payment (1.6.0); the troop account as a wallet and its reserve (1.7.0); rebate **liabilities** as an unpaid stock (1.6.0) — a rebate is paid when the clock stops. The reading *plants unfunded for want of Ω* **reads zero by construction** from here and retires with the plant reserve. **Standing:** the duty fund (surcharge in, uplift out); the service clock and the rebate; troops, their per-request summons, inspection first, and the delivery check for inspection *seats* (its funds clause is moot).

**Consequence — what a riot's deficit is.** It is **the in-flight capital of the state's share**: at each summons Ω burns the troop's cost and locks its guarantee and, when the inspection is summoned, its seats' costs and bonds — about 20–36 at $P_0$ per delivery — and recovers the price and the locks at vesting, thirteen ticks later. Run 11's ramp put 200 extra troops in the field inside two windows: **4,000–7,000 created in the first window of a hard spike**, a third of $M$ at the §2.1 genesis, retired as the cohort vests. Its effect on $P_t$ is that stock's share of $M$ for a window; the readings are the deficit's **peak** and **age**, not only its end-of-period value. Nothing is lost and nothing is refused for cash: the cost of the riot is a dip in every holder's purchasing power while the state's capital is in the field, handed back as it comes home.

**Guard.** A state that can create has every reason to prefer its own troops; the guards of 1.4.0 §2.1 and 1.7.0 §2.1 stand — members first, the windows, the per-request summons, the state's share and income by source on the record — and §2.6 removes the motive.

### 2.6 Servers out of the economy; the state at cost; the capacity case

**Rule — at cost.** A troop's delivery cost is $c^D_T=\bar B$: the state **delivers at cost**, burning the price it will receive, so that a delivery that vests is neutral to Ω and **a riot is nobody's windfall**. A delivery that ends in a final $\mathsf N$ is the state's loss — the burned $\bar B$ is not recovered and $G$ is forfeited to the requester, about $1.5\,\bar B$ — at the base fail rate times the state's volume; nobody's windfall, and a real cost, read in Ω's income by source. The 1.x default $c^D_T=10$ at $P_0$ — a margin of half of $\bar B$ on unbounded volume — is the control. A troop's review-seat cost $c_T$ stays indexed as before and its fee is Ω's, as 1.7.1 has it.

**Rule — the capacity parameter.** The state's physical capacity is $N_T$, **the most troops ELEF can field at once** — deliveries and review seats together — a parameter outside the ledger, not a cost. **Default 40**: clear of the quiet field at every split (run 10's field at rest, ticks 600–1,000: 18 / 23 / 26 / 29 at 50–80%, peaks to 34) and inside every riot peak (run 11: 75–221), so the tipping comparison carries no capacity refusal the 1.7.1 cells never had and every riot binds; **unbounded is the control.** **A delivery's summons needs room in the field for itself and its inspection seat** — two of $N_T$ — else the delivery would be fielded and its pinned audit refused for capacity: 1.6.0's "a delivery carries its inspection", in capacity terms. A summons $N_T$ refuses is **the capacity case**: the request's wait runs, the clock runs, and the case is recorded — *refused for capacity*, the request's wait, and whether its requester was told (a flag at the refusal, the capacity half of the busy line; the message itself is 2.x). This is the one case the market cannot answer with a price.

**Consequence.** Scarcity exists because capacity does. Under $N_T$ the state's share is bounded, bids rise toward ceilings when members and troops are both short, and the price level responds to money. Without $N_T$ the state is an infinite supplier at $\bar B$ and nothing is ever scarce.

### 2.7 Delegation — deferred to 2.1.0

Unchanged from v1.0 in the rules (§9). **Not run in this revision.** The 2.1.0 question: a cost per unit of work drawn once per actor (the spread that makes a market in sub-work — competence by another name), the child's cost as its share, troops never taking a nested request, the parent judging its child and what that does to the honesty dispositions, and §9.3's nested-first priority as the driver's. §8.5 keeps the question.

### 2.8 The below-market flag

**Rule.** A request posted with $\beta<\bar B$ is **flagged at posting** — *below market* — and waits, as 1.4.0 §2.3 has it, until a member bids under its ceiling or the requester raises it (§2.1). Its service clock is stopped while it is below market (1.6.0 §2.1, evaluated per tick) and runs again once raised; the time below market is not late. The engine has no channel to a requester; the flag and its counter are the reading, and the requester's policy may read the flag (the driver's). The share of requests flagged, and the stock flagged-and-waiting, are the price half of the network rating.

### 2.9 Defaults

| Default | Value | Note |
|---|---|---|
| $P_0$ | 20 | the former fixed price; indexing base |
| Requesters | 6; initial wallet 200; **issuance 10 a tick each** (60 total), swept 15 | about three posts a tick at $P_0$, clearing near 9 (§2.1) |
| A riot | a crowd: $n$ requesters added for the event with the default wallet and issuance, removed after; the hard spike $n=30$ for 100 ticks, the flood $n=12$ sustained | a demand event; the deficit shock is the money event |
| Ceiling policy | $\beta=\min(\beta_{\max},\ s\,W_{\text{unlocked}})$, $s=1/3$, $\beta_{\max}=40$; one post a tick while the all-in fits; $K_{\text{open}}=5$ | a declared strategy |
| Members' bid | $c_D(1+m)$; $m$ up on an award, down after $k=3$ idle ticks, floored at 0 | swept against "at the ceiling" (the 1.x behaviour) |
| $c_D$ | 8 per task, **nominal**; adaptive variant follows $P_t$ with a one-period lag | the anchor; the variant a sweep |
| Care cost | the driver's 2–3 a review, nominal | within indexed $K$ |
| $\lambda$ | 0.2, swept 0.5 | |
| $\bar B$ | trailing mean of members' awarded prices, §12.3's window | troop awards excluded |
| $P_t$ | trailing mean of all awarded prices, same window; $P_0$ before the first award | troop awards included |
| Indexed (frozen per case) | $f,G^V,D,\varphi^E,\varphi^F,K,r_s,c_T$, plant pots | $\times P_t/P_0$ at the case's first lock |
| $c^D_T$ | $\bar B$ (at cost); control $0.5\,P_t$ | a failed delivery costs the state about $1.5\bar B$ |
| $N_T$ | **40**, deliveries and review seats together; a delivery needs two of it; control unbounded | clear of the quiet field, inside every riot |
| Issuance in `Params` | 0 | the driver declares the requesters' issuance in the manifest; reviewer tests see none |
| Emission | $E_0=10$, $H=1000$, nominal | not indexed |
| Creation / retirement | last resort for a required payment; every inflow burned while the deficit stands | |
| Everything else | as 1.7.1 | membership, probation, panels, plants, the dial, the clock, the duty fund, troops |

---

## 3. Consequences and hypotheses

**Hypothesis 1 — price decides, and finds itself.** Among members, price decides every award at $\lambda=0.2$. Awarded prices sit between cost (8) and the ceiling: near cost where members are plentiful, near the ceiling where members and $N_T$ are both short. $P_t$ rises with $M$ once capacity binds and not before; against the at-the-ceiling control, members' real income is lower and customers' real spending higher.

**Hypothesis 2 — inflation is real and lands where it should.** A deficit shock — a declared scenario operation creating a fixed sum paid to customers as rebates — raises $P_t$ in proportion to its share of $M$ *where capacity binds*, and raises hoards where it does not; indexed fees keep their real value; balances, emission and the nominal effort costs lose theirs; Ω retires on every inflow and $P_t$ comes back. Under the adaptive-reservation variant the text expects the spiral: costs chase prices, bids chase costs, $P_t$ drifts — the run says how fast.

**Hypothesis 3 — the riot is neutral to the state and a dip to everyone.** Under the crowd of thirty (run 11's hard spike) with $N_T=40$: $\bar B$ rises as members and troops run short, the state delivers at cost, the deficit peaks at the in-flight capital of the state's share — thousands, a third of $M$ — and retires inside two periods; $P_t$ rises by that share for a window; nobody waits past $w_A$ *for cash*, and those who wait *for capacity* are recorded as such. Under unbounded $N_T$ the same spike leaves no queue and a smaller rise in $P_t$.

**Hypothesis 4 — honesty is price-neutral in its deterrents, and care's relative price moves.** False approvals, the lagging auditor, suspensions and readmissions are unchanged from run 10 at every split; indexed bonds and fees keep the deterrents constant in work. Where $P_t$ rises, inspection's indexed fee rises against the nominal care cost and the careful's real margin on a review improves; where it falls, the reverse. Measured, not assumed.

**Hypothesis 5 — deferred.** Delegation is 2.1.0's; §8.5 keeps the question.

**Hypothesis 6 — the state does not profit from scarcity, in price or volume.** $\bar B$ from members' awards only; delivery at cost; Ω's income by source shows the review fees and the base fee, and the surplus at zero in expectation.

**Hypothesis 7 — the deficit never binds and always clears.** Plants unfunded reads zero by construction; no summons is refused for cash; the deficit's age at every split is under two periods except in the hard spike.

**Limit, restated.** A floating price makes the loop an economy, and an economy with one good and no spending by its workers is a pipe from the mint to hoards. 2.1.0 closes the circuit. Until then the readings are honest about where the money goes.

---

## 4. What does not change

Everything in 1.7.1 about honesty and capacity: verdicts, challenges, the two pots, emission's recipients, plants and the record, the dial, membership, probation and the pin, the duty cap, panel eligibility, troops and the per-request summons, inspection first, the service clock and the rebate (now paid at the stop), the duty fund. What changes is what a credit is worth and how the state pays.

---

## 5. Invariants, notation (amendments)

**I1 (amended).** $M_t$ equals its last value plus the sources (issuance, emission, creation) less the sinks (bond and guarantee burns, resource spend, retirement), every tick; the kinds are as §2.4.
**I3 (amended).** Burns are bond and guarantee forfeiture, resource spend, retirement. No backing; no value-neutral purchase.
**I27 (new) — price and indexing.** $P_t$ is the trailing mean awarded price on §12.3's window, $P_0$ before the first award; every amount in §2.3's indexed list equals its base times $P_t/P_0$ **at the case's first lock** (§4.5); a troop's $c_T$ at its summons; $\bar B$ from members' awards only; effort costs are not the engine's to index.
**I28 (new) — the deficit.** Ω creates only for a payment the rules require and only when its unlocked balance cannot meet it; while the deficit stands Ω's unlocked balance is zero and every inflow is retired; deficit outstanding $=$ created $-$ retired; the deficit shock is a declared scenario operation of the driver, exempt by its note, as a plant's truth is.
**I29 (new) — the posting lock.** A root request holds, from posting to award, a lock of its all-in maximum at its posting index; a request that cannot lock is refused whole; the release at award equals the unspent part.
**Retired:** $v_t=\text{Res}_t/M_t$ as a backing (kept as $P_0/P_t$); I23's reserves and orders ($A_T$, $R_T$, the plant reserve, the order of payment, the troop account, liabilities by age); I25's funds clause. I22, I24, I26 stand as amended by 1.7.1.

**Notation (Appendix C).** $P_t$; $c_D$; issuance; creation; retirement; deficit outstanding; Ω's net position; real wealth; $N_T$; *below market*; *refused for capacity*. "Reserve" means the on-duty pool $X_t$ only; the retired quantity is the *backing*. Retired: $\text{Res}_t$, $R_T$, $A_T$.

**§18.1.** *Q2* opened: price discovery. *Q5* kept for 2.1.0. *New Q18*: the price level under a deficit. *Q16*: the deficit's peak, age and clearance. *Q4*: emission's real value under $P_t$, read apart from its halving. *Q11, Q15*: in real terms. *New Q19*: the capacity case — refusals for capacity under $N_T$, the waits they cause, whether the requester was told.

---

## 6. Worked example

Twenty actors, 60/40, defaults, tick 500, records determined: eight members, cap six on duty, two to three free; twelve probationers; six requesters, wallets near 150–200, issued 10 a tick, ceilings a third of the unlocked wallet — 40 at the cap when rich, less when the float is out; $N_T=40$, the quiet field about 23 of it; $P_t\approx9$.

**A quiet tick.** Three requests posted; each locks its all-in — $\beta+15\times0.45+\omega(\beta)$ at the posting tick's $m$, about 45 at $\beta=40$ — from a wallet of 170. Two free members bid: one awarded last tick bids $8\times1.3=10.4$; one idle four ticks bids $8\times1.05=8.4$. On the oldest request the two differ in $\rho$ by 0.01 and in price by $0.2\times(10.4-8.4)/40=0.01$ — the cheaper wins at 8.4, and its requester's lock releases $40-8.4$ and $\omega_0 m\,(40-8.4)$. The second goes at 10.4. The third waits $w_A=2$ and goes to a troop at $\bar B\approx9$ (its ceiling is above it); the summons needs two places in the field — the delivery's and its inspection seat's — and has them; Ω burns 9 and locks $G=5$; if its unlocked balance is short, it creates the shortfall and the deficit rises by it, to be retired on Ω's next inflow. The members and probationers who review these cases are paid at $9/20$ of the 1.x fee — the same work in fewer credits; the careful reviewer's care cost is its own 2–3 as before, so its real margin on a review is thinner than at $P_0$ (§2.3's named effect). $P_t$ stays near 9: cost 8, margins of 5–30%, capacity just slack.

**A customer below market.** A requester whose wallet has run down to 30 can lock all-in only for $\beta\approx6$; it posts, is flagged *below market* (9), its clock stopped, and waits. Three ticks of issuance later it raises the ceiling to 10, locking the difference; a member idle six ticks bids 8.4 and takes it.

**The hard spike, with $N_T=40$.** A crowd of thirty requesters arrives at tick 400 with wallets of 200 and issuance of 10, and posts about fifteen a tick for 100 ticks. The members' bids rise to the ceilings as idleness vanishes; the state summons until forty places are filled — about twenty-six deliveries and their seats — and then **refuses for capacity**: those requests wait, their clocks run, and each is recorded — *refused for capacity*, its wait, told. $\bar B$ climbs from 9 toward the ceilings (40), $P_t$ with it; Ω creates the in-flight capital of the field (about $26\times(c^D_T+G)$ at the risen prices — some 1,500) and retires it as the cohort vests; at cost the state's surplus is nil and its failed deliveries cost it $1.5\bar B$ each. The crowd leaves at tick 500 with its open requests served out; ceilings recover, bids fall, $P_t$ returns toward 9 over a period; the refusals for capacity are the riot's one reading the price could not answer. **With $N_T$ unbounded** the same crowd fields 200 troops, creates 4,000–7,000 in its first window — a third of $M$ — retires it inside two periods, and leaves no queue; $P_t$ rises less, because nothing was scarce but money.

**A deficit shock.** At tick 600 the driver's scenario operation (recorded as "scenario: deficit shock", not as a rebate) creates 2,000 and pays it to the six requesters, against $M\approx9{,}000$ (2,500 at genesis plus 20 a tick, less the burns of the first periods). Their wallets rise by a third; their ceilings and posting rate with them; capacity binds at 40, bids rise, $P_t$ toward 12. A member's 500 credits buy 42 tasks' worth instead of 55; its indexed fee still buys the same work; its nominal $c_D$ of 8 is now a third below the going price, so its margin widens. Ω retires on every inflow; $P_t$ returns toward 9 over a period and a half; the 500 buys 55 again.

---

## 7. Implementation note (no code here)

- **One flag.** `Params.floating`; off is 1.7.1 for the tests and the goldens. §8 reads against runs 10–11 as the fixed-price controls rather than re-running the 1.7.1 cells under a new engine.
- **Indexing is one function.** `ledger.index()` returns $P_t/P_0$, frozen per case at its first lock by the existing §4.5 code; `ledger.v` is $P_0/P_t$ as a reading; $P_t$ a period statistic beside `award_price_sum`, fed by `award` and `_summon_delivery`; `mean_awarded_price` is $\bar B$ unchanged.
- **$c_D$ is `spend`, and the cost API is in credits.** `spend(actor, cost)` and `complete_review(rid, verdict, cost)` take a *real* cost today and burn $\text{cost}/v$; under the flag they take the cost **in credits** and burn exactly that — effort costs are nominal, not the engine's to index — while `ledger.v` is a reading only and the troops' indexed $c_T$ is indexed by the engine before its burn. Reviewer tests run at $v=1$ and see no difference. `purchase` becomes a plain burn with `Res` held at 0; I2's "bad reserve" clause retires with it; `mint_backed` at genesis becomes `issuance`.
- **The posting lock** is `post_root`'s new validation and lock (the nested path generalised), with the release in `award` and `_summon_delivery`; the case carries its posting $m$ for the fee; `raise_ceiling(cid, β)` locks the difference; I29. Six reviewer files fund their humans at 1,000 and post one request at a time; at most one is expected to trip the lock, and becomes an expected failure with I29 as the reason.
- **Issuance defaults to 0 in `Params`** — every reviewer test asserts a human's wallet after a sequence — and the driver declares the requesters' issuance in the manifest; the engine mints it at the tick's start as the `issuance` kind.
- **The crowd**: `--spike-requesters n --spike-from t --spike-ticks k` adds $n$ requesters with the default wallet and issuance and removes them after $k$ ticks once their open requests are served out; the flood is the crowd sustained.
- **Ω.** One internal `_omega_pay(to, amount, note)` that pays from Ω's unlocked balance and creates the shortfall with the note checked against the required kinds (I28); one `_omega_retire()` on every inflow while the deficit stands; `_stop_clock` pays through it; the 1.5–1.7 machinery (`omega_liabilities`, `_service_omega_liabilities`, `_plant_reserve`, `_omega_available`, the funds branch of `_fund_can_carry`, `_repay_advance`, `_pay_troop_surplus`, `TROOP_ACCT`, `R_T`) behind the flag; the summons keeps its inspection-seat clause only.
- **Requesters and issuance.** `World(..., humans={name: wallet})` as now, plus `Params.issuance` minted to each requester at the tick's start — an engine schedule so I1 sees it, declared in the manifest.
- **$N_T$** in `Params`, checked in the summons before the seat clause and counting deliveries and review seats together, a delivery needing two places; a refusal for capacity is a counter, carries the request's wait and a *told* flag, and the I26 priority check applies to it.
- **The deficit shock** is a driver scenario operation (`--create-at`, `--create-amount`) that pays the requesters from Ω through `_omega_pay` with the note "scenario: deficit shock" — the declared exemption I28 recognises, and not a rebate, so Q15's rebate readings are not inflated by it.
- **Drivers.** Six requesters with wallets, issuance, the ceiling policy and $K_{\text{open}}$, reading the below-market flag; bids by disposition with the margin dynamics, the at-the-ceiling control, and the adaptive-reservation variant; real-wealth columns ($W\,P_0/P_t$) beside the nominal; `--n-t`, `--c-d`, `--c-d-t`, `--lam`, `--issuance`.
- **Tests.** `test_v20`: I1 over every kind; the freeze at first lock under a moving $P_t$; $\bar B$ excludes troops and $P_t$ includes them; the posting lock, its release and `raise_ceiling`; creation only when short and required, retirement on the next inflow, the deficit identity; $N_T$'s refusal and its record; the §6 quiet tick and below-market post reproduced in the six-actor world. **One reviewer test becomes an expected failure** — `test_review_04_reimbursement_uses_spent_credits_not_real_cost`, which pins §4.4's $v_t=\text{Res}_t/M_t$ — superseded with the reason, mirrored in `conftest.py`; its principle (reimbursement in credits spent, indexed) re-asserted in `test_v20` with $P_t$ in the index's place. Goldens re-pinned once.

---

## 8. After acceptance — the runs

Every 1.x comparison is read in real terms ($W\,P_0/P_t$) and from the second period on, against runs 10–11 as the fixed-price controls.

1. **Reproduce §6.**
2. **Price discovery** at 50–80%: bidding against the at-the-ceiling control — awarded prices, $P_t$, members' and troops' shares, real wealth, honesty (Hypotheses 1, 4, 6).
3. **The deficit shock** at 60/40: 1,000 / 2,000 / 5,000 at tick 600, $N_T$ 40 and unbounded — $P_t$'s rise and recovery, real wealth by disposition, hoards (Hypothesis 2; Q18).
4. **The riot under prices**: the crowd — thirty requesters for 100 ticks (run 11's hard spike), twelve sustained (its flood) — at $N_T$ 40 and unbounded: $P_t$, lateness, refusals for capacity and their waits, the deficit's peak and age (Hypothesis 3; Q16, Q19).
5. **Delegation** — held for 2.1.0; the question recorded.
6. **Knobs**: $\lambda$ 0.2 / 0.5; $c^D_T$ at cost / $0.5P_t$ (the state's margin, Hypothesis 6); issuance 10 / 15; the adaptive-reservation variant (the spiral).
7. **Adaptive and drift** in real terms.
8. **Red team**: members colluding at the ceiling (the 1.x behaviour, now a strategy against undercutters); a member bidding below cost to win reputation; a requester that underbids to wait for a troop (expected: flagged, waits); the state's price if troop awards were counted in $\bar B$ (the control that shows why they are not).

---

## 9. Provenance

**[S1–S11]** Eleven runs at a fixed price; run 11's hard spike as the case the price answers. **[C-2.0] Design discussion (October 18, 2026).** Baruchi: "the servers needs to be decoupled from the economy. otherwise we contaminate it"; "maybe it is time we introduce floating prices"; "if I print more money then money is worth less, if money is worth less you get less on the work that you do"; "we are missing something to balance this money with and the actors have nothing to 'buy' with their credits"; earlier, "the reserve is not real… the reserve is made up just like everything else." The design reviewer's two prior answers — emergency emission against a backing, and the server budget inside the ledger — withdrawn; this revision is on Baruchi's frame. **[I17] Implementation review of rc.1 (October 18, 2026)** — seven points, all adopted: the demand defaults did not clear (the deposit, not the bid, set the price; resolved with initial wallets, issuance at the all-in, a capped ceiling policy and $M$ at genesis stated); delegation cannot pay with one cost (deferred to 2.1.0 with heterogeneous costs); the pay-in locked at posting (§9.1's model for roots, `raise_ceiling` added); indexing frozen at the case's first lock (§4.5 stands) — with the design reviewer's addition that **effort costs stay nominal** as the anchor, the care cost with them, and an adaptive variant swept; the state's margin on a riot (resolved: at cost, $0.5P_t$ the control; $N_T=30$ the default so the capacity case is run, with what it records); the deficit's size (thousands, the in-flight capital, read by peak and age); retirement defined (every inflow burned while the deficit stands; Ω's net position; plants unfunded zero by construction; the shock a declared scenario op). Smaller — one expected failure named; `ledger.v` as $P_0/P_t$ and "backing" for the retired quantity; $P_t$ on $\bar B$'s window; the flag and `raise_ceiling`; I1's kinds; emission read apart; $\lambda$ live; one flag and runs 10–11 as controls — adopted. **[I18] Review of rc.2 (October 18, 2026)** — three to settle, settled: the riot's shape under finite wallets (a crowd of requesters — thirty for the hard spike, twelve for the flood — so the spike stays a demand event and the shock a money event); $N_T=30$ bound at rest at 80/20 (now 40, clear of run 10's quiet field at every split and inside every riot peak); the quiet price under issuance 15 was about 16 against §6's 11 (issuance 10 is the default and the example agrees with it, clearing near 9). Four implementation readings taken into the text: a root's first lock is its posting and the fee rate freezes with it; the cost API in credits under the flag; issuance 0 in `Params`; the posting lock against the reviewer tests. Smaller — the delivery check as two of $N_T$; the state's loss on a failed delivery at $1.5\bar B$; the clock stopped below market; the ledger's kinds; the shock's note; Hypothesis 1's "near cost" read in the adaptive tail — adopted.

---

## Closing statement

> For eleven runs the loop had rules about honesty and a token to keep score with, and it called the token money. It was not: nothing in the loop could make it worth more or less. This revision lets the price of work move, and with that one change the token becomes money — worth the work it buys, cheapened by printing, dearer when the state's servers are full, the one price the agents' own effort anchors. The state can never be broke, only in debt to everyone at once, in public, until every credit that reaches it has been burned back. The servers stay outside, where they belong; so do the agents' costs. What the workers will do with the money they earn is the next revision's question, and the honest answer for now is: nothing yet.

# Agentic Economics — The Task, Verification, and Dispute Loop

## Design revision 9 — specification 2.1.0-rc.2: the bank

**Project:** ELEF / Agentic Economics  
**Version:** 2.1.0-rc.2 — a release candidate, not yet in force. rc.1 (October 19) was the sketch as first sent; rc.2 settles the implementation review [I20]: the one correction (a plant is netted since 1.3.0 — the bank mints its pots, and whatever its wallets hold at closure returns to the bank), the one design choice the review left open (a binding wall refuses deliveries, never review seats), and seven readings taken into the text as written. On acceptance it becomes **2.1.0**, consolidated into one standalone text, and 2.0.0 moves to history.  
**Prepared:** October 19, 2026 (rc.1–rc.2)  
**Supersedes:** 2.0.0 where this document speaks; everywhere else 2.0.0 stands unchanged — the floating price, the posting lock, the indexing, the capacity parameter, the state's price at $\bar B$, and every rule of 1.x about honesty, membership, inspection and the troops.  
**Nature of this revision:** A **design revision** (minor, by §19). 2.0.0 gave the orchestrator one pocket for two jobs — running the state and making money — and runs 12–13 showed what that costs: a deficit nobody can read (part the money the economy needed, part the state's losses), a state that bled $0.3\,\bar B$ a delivery and printed to cover it, and a rebate that printed money against every refusal. This revision splits the pocket. **The bank** is a second account of the orchestrator's, with three jobs and no discretion: it **mints by rule** (issuance, emission, the cost of planted truth), it **publishes the index** once a period, and it **lends to the state only against capital that comes back** — never for losses, never for rebates. The state **delivers at its expected cost** so that its deliveries are neutral, **repays its losses from its fees**, and **retracts** if its debt outruns a period of its income. A request the state cannot serve for capacity **is told**. What members and requesters may do is unchanged.  
**Design assumptions, unchanged:** humans do not intervene; troops bear no malicious intent; the economy is closed, with nothing redeemed and no backing; ELEF's servers are outside it. **New, stated:** the bank is not an actor — it has no interests and no strategy; like the troops, it is honest by construction and visible in the ledger.  
**Status:** Proposed. Accompanied by what required it (§1) and the runs that test it (§8).

> **Money enters with requests. Truth enters with requesters — and with the orchestrator's own planted work.**
>
> **A credit is worth the work it buys. Nothing else.**
>
> **The state never prints for itself.** *(new)*

---

## 1. Why: what runs 12 and 13 said

1. **The state at cost was below cost [S12].** $c^D_T=\bar B$ burned at the summons, $\bar B$ recovered at vesting — and a fifth of the state's deliveries end in a final $\mathsf N$, recovering nothing and forfeiting $G$: about $0.3\,\bar B$ a delivery, created to cover it, the deficit growing 10–20 a tick for the rest of every run (Hypothesis 7 of 2.0.0 failed). The $0.5P_t$ control ran the identical path solvent. *Neither margin nor bleed* is what "at cost" meant.
2. **The rebate was a pump [S12].** Under the flood, refusal for capacity → rebate created → unspendable → hoards: deficit 59,700, $M$ 99,400, the requesters holding 3,022 each. A rebate created against a refusal is money printed for a service not rendered.
3. **The index moving within a period** broke three reviewer tests that pin a case's amounts against an index that does not drift under their feet [S12].
4. **The deficit could not be read [S12, S13].** Run 13's cheapest market (26.7 at 60/40, the state delivering 75%) carried a deficit of 14,037 — which is the bleed, $0.3\,\bar B\times2{,}007$ deliveries, not the pricing; but the one number could not say so. Capital in flight, losses and rebates owed were one figure.
5. **Run 13 settled the price question [S13]** so that this revision does not touch it: the high price is the members' strategy restricting quantity under scarce supply (one award per 3.6 free member-ticks, the margin rule's own constant); adding workers takes the price to cost (22.5 → 11.6 → 10.9 at 20 / 30 / 40 honest); the state at $\bar B$ never lowers it; the cap is the price level only when requesters bid above the market. The lever is entry — 2.2.0's. The implementer's warning is taken: a state priced *below* $\bar B$ becomes the lowest offer wherever members are scarce and crowds them out (the 75% cell). **The state's price stays $\bar B$. What changes is what it burns.**
6. **Baruchi's position [C-2.1]:** the state is "like a living organism, sending and retrieving troops all the time to regulate the market… turning the knobs to stabilize"; and, asked for real, a central bank as a separate entity — agreed as *a second account with rules, not a second actor*: mint by rule, publish the index, lend only against what comes back; losses from the state's income "or they don't come out at all"; when income does not cover losses, "charge for it, or retract."

**Classification.** A design revision: a new account in the ledger and rules on how the state is financed. The rules of honesty, the price, the lock, the index's base and the capacity parameter are untouched; one new thing a requester may read (*refused for capacity*). Minor, by the rule.

**Recorded and rejected.** *The state pricing below $\bar B$* (its expected cost as its price): run 13 — the price-setter wherever members are scarce, the largest state, the members crowded out. *Issuance as a dial* (a price-targeting bank): money moves the price tag, not the work — the quantity is the strategy's and the costs are nominal — and 2.0.0 indexed the rule amounts precisely so that printing would be neutral; a knob on a number we invented. *The bank as an actor*: no interests, no strategy, nothing to optimise. *The oligopoly as a rule*: a strategy under scarce supply; the lever is entry. *The state refusing for cash*: 2.0.0's "never broke" stands for capital — a summons is always lent for while the state's debt is within a period of its income; only a state that has lost more than it earns retracts (§2.4), and Hypothesis 1 says that never happens under §2.2. **Recorded and held:** *the state's window as the knob* — $w_A$ shortening as the price runs above cost and lengthening as it returns, the organism regulating a quantity rather than the money — held until entry exists (2.2.0), so that the knob is tested against the lever and not in its place.

---

## 2. The rules

### 2.1 The bank: a second account, three jobs, no discretion

**Rule — the account.** The orchestrator keeps two accounts in the ledger. **Ω** is the state: the base fee and the troops' review fees in; plants' awards, rebates, the troops' costs and locks out — as 2.0.0 has it. **𝔅 is the bank**: it is the only account that creates and destroys credits. It has no wallet in the economy's sense — its balance is a *position*, the credits it has created and not yet destroyed — and it is not an actor: no bid, no verdict, no strategy, no interest. Everything it does is a rule, and everything it does is public.

**Rule — three jobs.** The bank (i) **mints by rule** (§2.3); (ii) **publishes the index** (§2.5); (iii) **lends to the state against capital in flight** (§2.4). It does nothing else: no payment to a member, a requester or Ω that is not one of the three.

**Consequence.** "The state never printed for itself" becomes a sentence the ledger can prove: every credit the bank created is on one of three lines — minted (issuance, emission, plants), lent (against a summons, repaid by it), or destroyed — and the state's own losses are on none of them.

### 2.2 The state at its expected cost; its price unchanged

**Rule — the price.** A troop delivers at $\bar B$, as 2.0.0 §2.2 has it: the trailing mean of members' awarded prices, only where $\beta\ge\bar B$, after the members have taken theirs. *A request past $w_A$ goes to the state at $\bar B$, not at its cost.*

**Rule — the burn.** A troop's delivery cost is $c^D_T=\max\!\big(0,\ (1-b_T)\,\bar B-b_T\,G\big)$, with $G=\lceil0.5\,\bar B\rceil$ the delivery's guarantee and $b_T$ the **trailing fail rate of the state's deliveries**: the share ending in a final $\mathsf N$ among the state's deliveries closed in the last closed period, if it closed ten or more; else over the trailing closed periods extended back until ten; else the prior $b=0.2$ (run 12's base). The burn is at the summons, as before. A delivery that vests returns $\bar B$ and its locks; one that ends in a final $\mathsf N$ returns nothing and forfeits $G$. **In expectation the delivery is neutral to Ω**: a success leaves $\bar B-c^D_T=b_T(\bar B+G)$, a failure costs $c^D_T+G=(1-b_T)(\bar B+G)$, and at the trailing rate they cancel. Neither margin nor bleed. The 2.0.0 default $c^D_T=\bar B$ is the control. A troop's review-seat cost $c_T$ stays indexed as before.

**Consequence — the charge is automatic, up to two thirds.** If the state's deliveries fail more often, $b_T$ rises, the burn falls, and the state keeps more of each success until its losses are covered; if they fail less, the reverse. With $G=\lceil0.5\bar B\rceil$ the burn is $\bar B(1-1.5\,b_T)$ — **zero at $b_T=2/3$**, and above that no burn makes the state neutral (a success returns $\bar B$, a failure forfeits $G$, and $(1-b)\bar B<bG$): there the automatic charge runs out and only §2.4's wall is left. There is no other charge: the state's price does not move, and neither does ELEF's fee.

### 2.3 Minting by rule: issuance, emission, the cost of truth

**Rule — issuance.** The requesters' issuance (2.0.0 §2.1: the genesis floats and the declared schedule, 10 a tick each) is the bank's: minted at the tick's start, recorded as `issuance`. Unchanged in amount and timing; moved in the books.

**Rule — emission.** $E_t=E_0\,2^{-t/H}$, nominal, to its recipients as before — the bank's, recorded as `mint_emission`.

**Rule — plants.** A planted case — the dial's known-truth work (1.2.0) — is **minted, not lent**. A plant has been netted since 1.3.0 §2.5: its award and guarantee are notional, Ω paying itself, and only its two pots are funded. So at its posting the bank mints **the plant's pots**, $\varphi^E+\varphi^F$ at the posting index, recorded as `mint_plant`; and **whatever the plant's wallets hold at its closure returns to the bank and is destroyed** (`retire_plant`) — the refunds, and anything else the sweep finds, whatever it is called — so that nothing minted for a plant ever reaches Ω. The plant's net cost — the pots spent on its reviewers' fees and expenses — is the **cost of truth**, created by rule like emission, bounded by the dial ($m_{\max}$, the plants a tick it may call for). **It does not touch Ω and does not wait for Ω's cash**: inspection's budget is not the state's purse, which is the lesson of 1.6.0's plant reserve, now by construction and without the reserve.

**Consequence.** The verification security budget — emission since v1.0, plants since 1.2.0 — is one line in the bank's books, read together (Q4): money created for truth, in real terms.

### 2.4 Lending against capital in flight; losses from income; the wall

**Rule — the loan.** When a summons the rules call for — a delivery's $c^D_T$ and $G$, an inspection seat's $c_T$ and $G^V$ — exceeds Ω's unlocked balance, **the bank lends Ω the shortfall** (`loan`, a source), **tied to that summons**. The loan is capital in flight: it is repaid from **its own summons's return** — a delivery's at its vesting or final $\mathsf N$ (the price received, the guarantee released), a seat's at its review's settlement (the cost reimbursed, the fee, the bond released), which may fall before or after the case's close — before anything of that return reaches Ω (`repayment`, a sink). What the return does not cover is **the state's debt**; what exceeds the loan is Ω's income.

**Rule — the debt.** Debt is the sum of every settled summons's unrepaid loan, and nothing else: the bank never lends for a loss, a rebate, or any payment that is not a summons. **Every inflow to Ω's unlocked balance repays the debt first** — the base fee, the review fees, the surplus of a vesting delivery — before Ω keeps anything; the order is applied at the start of the tick's summons pass and again at the tick's end, so that while debt or liabilities stand Ω's unlocked balance is zero at both points and every summons in between is the bank's.

**Rule — rebates are liabilities.** A rebate the clock owes (1.6.0 §2.1) is paid at the stop from Ω's unlocked balance; **when Ω cannot pay it, it accrues as a liability** — 1.6.0's stock, oldest first — paid from Ω's income **after the debt**. Nothing is created for a rebate. The stock, its oldest age and its total are the readings (Q15); the rebate's amount, the clock, and the rule that a request withdrawn before its award is owed nothing are unchanged.

**Rule — the wall.** The bank lends for a **delivery** only while the state's debt is within $\Delta_{\max}$: **one period of Ω's fee income** — the base fees and the troops' review fees of the last closed period, so the wall rises with the market's activity and with its prices; unbounded in the first period, which is the state's (as 1.6.0's first panels were). A delivery the bank will not lend for is funded from Ω's unlocked balance or not at all: it is **refused for credit** — recorded like the capacity case (the request's wait, the clock running, told), and the state retracts until its income has brought the debt back within the wall. **A review seat is lent for regardless of the wall.** The wall answers the state's losses on its *own* deliveries; an inspection seat serves a member's delivery, not the state's, and 1.6.0 found that the seat, not the treasury, is what caps the market — so inspection is never hostage to the state's delivery losses, as plants are not (§2.3), and its capital is small and returns at settlement (its loss is an overturned troop verdict's bond). *Seats refused for credit* reads zero by construction and is kept as a check. **Unbounded is the control** (2.0.0's state). Hypothesis 1 says the wall never binds under §2.2; if it binds, the burn rule is wrong, not the wall.

**Rule — the order of Ω's payments, in one line.** An inflow to Ω: debt → liabilities, oldest first → Ω's balance. A summons: Ω's balance → the bank's loan — for a seat always, for a delivery while the debt is within the wall → refused for credit. Ω's balance is ELEF's retained income, and it funds the next summons before the bank does.

**Retired as rules:** Ω's **creation** and **retirement** (2.0.0 §2.5) — a loan is creation tied to a summons and repaid by it; a repayment is retirement tied to a case; "deficit outstanding" becomes three readings: **loans outstanding** (capital in flight), **debt** (losses not yet repaid), **liabilities** (rebates owed). **Ω's net position** $=\Omega_U-\text{debt}-\text{liabilities}$.

**Consequence — what a riot costs, by line.** The crowd of thirty under $N_T=40$ puts the field's capital on the loans line — about $26\times(c^D_T+G)$ at the risen prices, 1,500; unbounded, 4,000–7,000 in the first window — repaid as the cohort vests; its failed deliveries put their losses on the debt line, repaid from the riot's own fees (a riot is many awards, so the wall is high in a riot); its lateness puts rebates on the liabilities line, paid after. Each is read apart; none is printed for.

### 2.5 The index, once a period

**Rule.** The bank **publishes $P_t$ at each period boundary**: the mean awarded price — members' and troops' — of the period just closed, carried if it had no awards; $P_0=20$ before the first. **Within a period the index does not move.** Every indexed amount is frozen at the case's first lock as before (2.0.0 §2.3, I27), at the index then published. $\bar B$ — the state's price and the below-market flag's reference — stays on §12.3's live window: the state is a price-taker, and it takes the current price.

**Consequence.** A case's amounts cannot drift under a reviewer's feet within a period (the three reviewer tests pass); the ratchet, which reads $\bar B$ and the requesters' ceilings, is untouched (run 13 §6). **The first period is at base by construction**: the index is $P_0$ while $\bar B$ runs from 9 to 30 (run 12's first hundred ticks), so the first period's pots, court fee, bond and cap are at base while the price triples — stated so that every comparison with 2.0.0 is read from the second period on, as it always has been.

### 2.6 The capacity case, told

**Rule.** A summons $N_T$ refuses (2.0.0 §2.6), and a delivery the bank refuses (§2.4), **mark the request** — *refused for capacity* / *refused for credit*, with the tick — and the mark is readable by the requester's policy through the public view, as the below-market flag is. The requester may hold or withdraw (`withdraw_unawarded`; withdrawn before award, owed nothing); the clock runs either way. 2.0.0's engine already marked a capacity refusal *told* at the first refusal; this revision widens the mark to its kind and its tick and gives the requester's policy something to read. **Every refusal is told.** The share of refused requests withdrawn is the busy line's reading, beside on-time share and lateness.

### 2.7 Delegation and entry — 2.2.0

Unchanged in the rules (§9); not run. 2.2.0 is the supply side: a cost per unit of work drawn once per actor (competence), the child's cost as its share, troops never taking a nested request; and **entry** — the arrival of honest members as a public operation, the one lever run 13 found for the price. §8 keeps the questions.

### 2.8 Defaults

| Default | Value | Note |
|---|---|---|
| The bank 𝔅 | one account; mints `issuance`, `mint_emission`, `mint_plant`; lends `loan`; destroys `repayment`, `retire_plant` | not an actor |
| $c^D_T$ | $\max(0,(1-b_T)\bar B-b_T G)$ (expected cost); control $\bar B$ (2.0.0's at cost) | neutral in expectation up to $b_T=2/3$ |
| $b_T$ | final-$\mathsf N$ share of the state's deliveries over the last closed period if it closed ten or more, else trailing periods back until ten, else the prior 0.2 | the state's own record |
| $\Delta_{\max}$ (the wall) | one period of Ω's fee income (base fees and troops' review fees); unbounded in the first period; control unbounded; deliveries only — seats always lent for | `debt_bound_periods` 1 / 0 |
| Loan | the shortfall of a summons over Ω's unlocked balance, tied to the summons, repaid from its own return (a delivery's at vesting or final N, a seat's at its review's settlement) | capital in flight |
| Rebate | paid at the stop from Ω; else a liability, oldest first, after the debt | never created |
| $P_t$ | published at the period boundary: last period's mean awarded price; $P_0=20$ through the first period | constant within a period |
| $\bar B$ | §12.3's live window, members' awards only | unchanged |
| Plants | the pots minted at posting (`mint_plant`); whatever the plant's wallets hold at closure destroyed (`retire_plant`) | the cost of truth |
| Refusals | for capacity, for credit: the request marked, told, readable; requester holds (default) or withdraws (variant) | the busy line |
| Issuance | 10 a tick a requester; **swept 5 / 10 / 20** at 20 honest (§8.5) | the inflation test |
| Everything else | as 2.0.0 | the price, the lock, indexing at first lock, $N_T$, the crowd, the below-market flag |

---

## 3. Consequences and hypotheses

**Hypothesis 1 — the state's deliveries are neutral, and the wall never binds.** At every split 50–80% and in every §8 cell, Ω's net on the state's deliveries per period is zero within its variance; the debt stays within a period's fees; no delivery is refused for credit. Against the control ($c^D_T=\bar B$) on the identical path, run 12's deficit of 3,700–10,100 reads as loans outstanding of a few hundred and a debt near zero. **Where the driver fails a fifth and the prior is a fifth, neutrality holds by construction from tick 0**, and the default cells measure only the debt's variance and $b_T$'s lag; §2.2 is actually tested where the two differ — the prior at 0.1 / 0.3 (§8.8) and the half-failure cell (§8.9) — and those are read first. *If the wall binds anywhere, §2.2's burn is wrong — the prior, the window or the formula — and that is the finding.*

**Hypothesis 2 — the pump is off.** Under the flood (twelve requesters sustained, $N_T=40$) and under 60/40 with $K_{\text{open}}$ lifted (run 13's 3,364 refusals a run): $M$ does not grow with refusals; rebates accrue as liabilities and are paid from income; the requesters' hoards of run 12 (3,022 each; $M$ 99,400) do not appear; on-time share and lateness are unchanged, because the clock is unchanged. The liability stock's age is the price the customers pay for the state's lateness in a riot, read in periods.

**Hypothesis 3 — the index per period changes nothing in kind.** Run 12's discovery cells repeated: $P_t$, margins, the state's share, honesty within seed variance of 2.0.0; the three reviewer tests pass without an expected failure.

**Hypothesis 4 — the books read.** The bank's position decomposes every run: minted by kind (issuance, emission, plants), loans outstanding, debt, liabilities; and "the state never printed for itself" holds as an invariant (I30) in every cell, the riots included.

**Hypothesis 5 — the inflation test (from run 13, stated as a hypothesis).** Where the ratchet binds, the requesters spend what is minted and the members' quantity is the strategy's constant $k\cdot F$ ($k=0.278$, $F$ the free members), so the price is issuance over quantity: at 20 honest, issuance 5 / 10 / 20 a requester gives $P_t\approx11/22/45$ — $60\div(0.278\times9.6)=22.5$ was the measured 22.5 — unless a nominal ceiling ($\beta_{\max}$, the wallet rule) binds first; **real wealth by disposition is unchanged across the sweep**, because printing moves the price tag and not the work. If it holds, that is the inflation [C-2.0] asked for, and the reason issuance is not a dial.

**Hypothesis 6 — told, and what it changes.** With every refusal told, the default requester holds and nothing changes from 2.0.0; the withdrawing variant withdraws and reposts, and the share withdrawn is the busy-line reading the price could not give. Honesty is unmoved.

**Hypothesis 7 — plants never wait for the state.** Plants posted equal plants the dial called for in every cell, the first period included; the cost of truth in real terms is read beside emission (Q4).

---

## 4. What does not change

Everything in 2.0.0 about the price and the lock, and everything in 1.x about honesty and capacity: verdicts, challenges, the two pots, emission's recipients, plants and the record, the dial, membership, probation and the pin, the duty cap, panel eligibility, troops and the per-request summons, inspection first, the service clock and the rebate's amount, the duty fund, the state's price at $\bar B$, $N_T$, the crowd, the below-market flag. What changes is who creates money, what the state burns, and what the state's losses are paid from.

---

## 5. Invariants, notation (amendments)

**I1 (amended).** Sources: `issuance`, `mint_emission`, `mint_plant`, `loan` — all the bank's. Sinks: `burn_bond`, `purchase`, `repayment`, `retire_plant`, `departure`. $M_t$ equals its last value plus the sources less the sinks, every tick.
**I28 (rewritten) — the bank.** Ω never creates; the bank creates only by §2.3's three mintings and §2.4's loans; a loan is tied to a summons the rules called for and is repaid from that summons's own return before Ω receives any of it; debt is the sum of settled summonses' unrepaid loans and changes only at a settlement or a repayment; nothing is created for a rebate; nothing minted for a plant reaches Ω; the scenario deficit shock is a declared operation of the bank (`mint_scenario`), exempt by its note.
**I30 (new) — the bank's identity.** The bank's position $=$ minted (by kind) $+$ loans outstanding $-$ destroyed, every tick; loans outstanding $=\sum$ open summonses' loans; debt $\le\Delta_{\max}$ whenever a loan for a delivery is made, and a seat's loan is never refused; while debt $>0$ or liabilities $>0$, Ω's unlocked balance is zero at the start of the summons pass and at the tick's end.
**I31 (new) — the index per period.** $P_t$ changes only at a period boundary, to the closed period's mean awarded price or carried; within a period every `index()` reading is equal.
**I27, I29** stand. **Retired:** "creation" and "retirement" as kinds; "deficit outstanding" as a quantity (the three lines replace it); the *told* flag as a driver's input.

**Notation (Appendix C).** 𝔅 the bank; `loan`, `repayment`; **loans outstanding**; **debt**; **liabilities**; $\Delta_{\max}$ the wall; $b_T$; `mint_plant`, `retire_plant`; *refused for credit*; the cost of truth. Ω's net position $=\Omega_U-\text{debt}-\text{liabilities}$.

**§18.1.** *Q16* restated: loans outstanding, debt and liabilities by peak and age — not one deficit. *Q15*: the liability stock's age under riots. *Q4*: emission and plants together as the cost of truth, in real terms. *Q18*: the price level under issuance, as Hypothesis 5. *Q19*: refusals told and the share withdrawn. *Q5* and *new Q20* (entry) kept for 2.2.0.

---

## 6. Worked example

Twenty actors, 60/40, defaults, tick 500, records determined; eight members, two to three free; six requesters issued 10 a tick by the bank; $N_T=40$; $\bar B\approx30$ (run 12's level — the ratchet's, not the rules'), $P_t$ published at tick 500 as the fourth period's mean, 31; $b_T=0.2$ from the last period's 67 state deliveries (run 12's 670 a run at this split), 13 of them final $\mathsf N$.

**A summons.** A request past $w_A$ with $\beta\ge30$ goes to a troop at $\bar B=30$. The burn is $c^D_T=0.8\times30-0.2\times15=21$, not 30; Ω locks $G=15$. Ω's unlocked balance is 4 (it funds summonses before the bank does), so the bank lends the shortfall, 32, tied to the summons; loans outstanding rise by 32. Its inspection seat, summoned when the delivery is submitted, is lent for likewise — $c_T$ and $G^V$ — and repaid at the review's settlement, before or after the delivery's own close. Thirteen ticks later the delivery vests: it returns 30 and releases 15; 32 repays the loan, 13 reaches Ω — of which, if the state has debt, every credit goes to the debt first. Had the delivery ended in a final $\mathsf N$: nothing returns, $G$ goes to the requester, and the 32 lent becomes debt. Over the period's 67 deliveries: about 54 successes at $+9$ and 13 failures at $-36$ — 486 against 468, neutral within the rounding. The period's base fees (about 570) and the troops' review fees are Ω's to keep, after any debt from the variance (about 150 — three failures more or fewer than the rate, at 45 a swing — well within a period's fees) and after rebates owed.

**A period boundary.** At tick 600 the bank publishes $P_t=$ the fifth period's mean, 32; every case locked from tick 600 to 699 is indexed at $32/20$ and keeps it; a case locked at tick 599 keeps $31/20$. $\bar B$ went on moving every tick.

**A plant.** The dial calls for a plant at tick 610; the bank mints its two pots, $(10+5)\times32/20=24$; the plant is posted (its award and guarantee notional, as since 1.3.0), awarded, reviewed and closed; at closure its wallets hold about 11 of refunds (run 10's 6 of 10 and 0.8 of 5, at the index), which the sweep returns to the bank and destroys. The cost of truth that plant: about 13, beside emission's $E_{610}\approx6.6$ a tick. Ω's balance was never asked, and nothing minted for the plant reached it.

**The flood.** Twelve requesters sustained; the field full; 3,500 refusals a run, every one told. The default requesters hold: their clocks run, the state owes rebates at the stops, Ω pays what it can at each stop and the rest accrues — a liability stock that peaks at a few thousand and ages a period or two, paid down from the flood's own fees after the debt. $M$ grows by issuance alone. The withdrawing variant withdraws at the mark and reposts; its share withdrawn is the reading. The loans line carries the field's capital, 1,000–1,500, repaid as it vests; the debt line carries the failures' losses, repaid from the flood's fees inside a period; the wall — a flood period's fees, in the thousands — is never reached.

**The wall, if it were reached.** Suppose the state's deliveries began failing at a half while $b_T$ still read a fifth: for a period each delivery is $0.5\times9-0.5\times36=-13.5$ in expectation, about 900 on 67 — above a period's fees. The bank stops lending for deliveries; they are funded from Ω's balance, which is zero while the debt stands; requests past $w_A$ wait, marked *refused for credit*, told; the state has retracted. **Review seats are still lent for**: the members' deliveries are inspected as before, and the market runs on without the state. At the period's close $b_T$ reads a half, the burn falls to $0.5\times30-0.5\times15=7.5$, each success now leaves 22.5, and the debt is repaid within the next period's deliveries and fees; lending resumes. Had the failures run above two thirds, no burn would make the state neutral (§2.2) and the wall would hold until the state's fee income alone had repaid the debt. The customers waited, in public, for a state that had lost more than it earns. That is what the wall is for, and Hypothesis 1 says the §8 runs will not show it except where §8.9 makes it so.

---

## 7. Implementation note (no code here)

- **One flag.** `Params.bank`; off is 2.0.0 for the goldens. On: `BANK` as a second orchestrator account beside `OMEGA` — not an actor, no wallet, a position.
- **Kinds.** `creation` → `loan` (with the case and the summons kind in the note); `retirement` → `repayment` (with the case); new `mint_plant`, `retire_plant`, `mint_scenario`; `issuance` and `mint_emission` booked to `BANK`. I1 over the kinds; I30 as the bank's identity; the bank is counters and kinds, not a wallet.
- **The summons.** `_omega_ensure` becomes `_bank_lend(cid, kind, amount)` for the summons kinds only, the loan on the summons. Each loan is repaid from its own summons's return — a delivery's at `vest` or final $\mathsf N$, a seat's at the batch that settles its review — `_bank_repay` first; the remainder to Ω through one `_omega_income(amount)` that applies the order debt → liabilities (oldest first) → Ω, **run at the start of the summons pass and at the tick's end**. Debt and liabilities are two scalars with per-summons and per-request provenance for the readings.
- **The wall.** `Params.debt_bound_periods` (1; 0 unbounded); `_fund_can_carry` reads it: a *delivery* is refused when debt $>$ the last closed period's Ω fee income (base fees plus the troops' review fees — the review-fee line is new to `omega_fee_income`); a *seat* is never refused for credit. A refused delivery reads Ω's balance alone and, failing it, records *refused for credit* with the same fields as the capacity refusal and the I26 priority check; *seats refused for credit* is kept as a reading that should read zero.
- **$c^D_T$.** `c_d_t_mode expected` (default) / `at_cost` (control) / `half` (1.x); floored at 0; $b_T$ over the last closed period if it closed `b_t_min_n` (10) of the state's deliveries, else trailing periods back until it does, else `b_t_prior` (0.2).
- **Rebates.** `_stop_clock` pays from Ω's unlocked balance, else appends to `omega_liabilities`; `_service_omega_liabilities` returns behind the flag in the order debt → liabilities oldest first, without 1.6.0's minimum age and without its order against advances — there are no advances.
- **Plants.** `_post_plant` mints the two pots through `BANK` (`mint_plant`) at the posting index — the award and guarantee stay notional (1.3.0 `net_plant_capital`); at tree closure **the whole sweep of the plant's wallets** routes to `BANK` and is destroyed (`retire_plant`), whatever it holds. The plant-reserve reading retires; "plants posted / called for" is the reading.
- **The index.** `price_level()` set at the period boundary from the closed period's `price_sum / price_n` (members' and troops'; carried if none); `index()` reads it; `_record_price` no longer moves the index; `mean_awarded_price` ($\bar B$) unchanged on the live window. The three reviewer tests broken by the moving index leave `EXPECTED_FAIL`; `test_review_04` ($v_t=\text{Res}_t/M_t$) and `test_review_14` (the pay-in refused whole at posting, I29) stay — the count goes to 28.
- **Told.** 2.0.0's `capacity_told` widens to `refused: capacity | credit | None` with `refused_at`, in `drivers.view.Public`; the driver's requester reads it; `--requester-on-refusal hold|withdraw` (hold default).
- **The deficit shock** is `mint_scenario` on `BANK` with its note; nothing else changes.
- **Drivers.** `--issuance 5|10|20`; `--debt-bound-periods`; `--c-d-t-mode`; real-wealth columns beside the nominal; the bank's books per period in `metrics.csv`: minted by kind, loans outstanding (peak, age), debt (peak, age), liabilities (total, oldest age), Ω's retained income.
- **Tests.** `test_v21`: I30 every tick; a loan only at a summons kind and only for the shortfall; repayment from the summons's own return before Ω, a seat's at its settlement; debt only at a settlement; the order of Ω's income at both points of the tick; a rebate never creates; the wall refuses a delivery and records it, and never a seat; $c^D_T$ floored; $P_t$ constant within a period and set at the boundary; plants' pots minted and the whole sweep destroyed through the bank with Ω untouched; the §6 summons, boundary, plant and wall reproduced in the six-actor world. Goldens re-pinned once.

---

## 8. After acceptance — the runs

Every comparison in real terms and from the second period on; 2.0.0's cells (runs 12–13) are the controls, with `bank` off where a control is wanted. Every cell names its requester policy (wallet rule / market-aware) and $K_{\text{open}}$, as run 13 asked.

1. **Reproduce §6.**
2. **The state neutral** at 50–80%, wallet rule, $K_{\text{open}}$ 5: Ω's net on deliveries per period, loans outstanding, debt (peak, age), the wall's slack; against `c_d_t_mode at_cost` on the identical path (Hypothesis 1). Read with 8 and 9, where $b_T$ and the driver's rate differ — the default cells are neutral by construction.
3. **The pump**: the flood and the crowd at $N_T=40$; 60/40 with $K_{\text{open}}$ lifted, both ceiling policies — $M$, liabilities (total, age), hoards, on-time, lateness; against 2.0.0's flood (Hypothesis 2).
4. **The index per period**: run 12's discovery cells repeated (Hypothesis 3).
5. **The inflation test**: issuance 5 / 10 / 20 a requester at 20 honest, $\beta_{\max}$ 60, both ceiling policies — $P_t$, posts, real wealth by disposition (Hypothesis 5; Q18).
6. **Told**: 60/40 with $K_{\text{open}}$ lifted under the withdrawing requester — share withdrawn, reposted, served; honesty (Hypothesis 6; Q19).
7. **The books**: in every cell, the bank's position decomposed; run 12's deficit re-read as loans and debt (Hypothesis 4; Q16).
8. **Knobs**: `debt_bound_periods` 1 / 2 / unbounded; $b_T$'s prior 0.1 / 0.2 / 0.3 and window one / two periods.
9. **Red team**: a reviewer that rejects the state's deliveries to raise $b_T$ (expected: the burn falls, the state keeps more per success, the reviewer gains nothing and meets the plants); a requester that posts, waits for the mark and withdraws to farm rebates (expected: withdrawn before award is owed nothing); the state's deliveries made to fail at a half — and at three quarters, above §2.2's two thirds — with the wall at one period (the §6 wall, reproduced; seats still lent for, the members' work read beside the state's) and unbounded (the control: 2.0.0's bleed).
10. **Delegation and entry** — held for 2.2.0; the questions recorded.

---

## 9. Provenance

**[S12] Run 12** (October 18, 2026) — the bleed ($0.3\,\bar B$ a delivery, the deficit never retired), the pump (the flood's hoards), the index moving within a period (three reviewer tests), the oligopoly first read. **[S13] Run 13** (October 19, 2026) — the price question classified: supply the trigger and the cure (22.5 / 11.6 / 10.9 at 20 / 30 / 40 honest), the strategy's constant (0.278), the state at $\bar B$ never lowering the price, the cap the price level only when requesters bid above the market, run 12's "cap at 40" corrected to the wallet rule; the implementer's reading that "cost in expectation" would price the state below $\bar B$ — answered here by two rules in two sentences (§2.2) — and that the demand model must be named per cell (§8). **[C-2.1] Design discussion (October 19, 2026).** Baruchi: "the state is like a living organism sending and retrieving troops all the time to regulate the market. raising and lowering the inflation to keep the market stable. turning the knobs to stabalize"; "should we introduce a central bank as a separate entity? asking for real, not sure"; "ok, I agree". The design reviewer's answer: a second account with rules, not a second actor — mint by rule, publish the index, lend only against what comes back, losses from the state's income, and when income does not cover losses, charge for it or retract; inflation not a dial (money moves the price tag, not the work); the state's window as the knob held for after entry. **[C-2.0]** stands: the servers decoupled, the reserve not real, printing must make money worth less. **[I20] Implementation review of rc.1 (October 19, 2026)** — implementable, with one correction and nine readings. The correction, adopted: a plant has been netted since 1.3.0 §2.5 (award and guarantee notional, only the pots funded), so the bank mints the pots, about 23 at $P_t=31$ and not 45, and the whole sweep of the plant's wallets at closure returns to the bank — if any of it reached Ω the state would be earning minted money and I30 would be false by construction (§2.3, §6 recomputed). The one design choice left open, ruled: a binding wall refuses deliveries and never review seats (§2.4) — the seat serves a member's delivery, 1.6.0 found the seat caps the market, and its loss is a bond. The readings, taken as written: $c^D_T$ floored at 0, and above $b_T=2/3$ no burn makes the state neutral — the automatic charge runs out and only the wall is left; $b_T$'s window extended back until ten have closed, else the prior; a seat's loan repaid at its review's settlement, each loan from its own summons's return; the order of Ω's income applied at the start of the summons pass and at the tick's end; the first period's index at $P_0$ by construction, every comparison from the second period on; Hypothesis 1 neutral by construction where the driver's rate and the prior agree, so §8.8–8.9 are the test and are read first; `test_review_14` stays an expected failure (28); the *told* mark was the engine's already and is widened; §6 at 67 state deliveries a period, not 180.

---

## Closing statement

> 2.0.0 made the token money and left the state holding the press. This revision takes the press away and gives it rules. The bank mints what the economy is owed — the customers' issuance, the reviewers' emission, the cost of planted truth — and lends the state what it will get back, tied to the case that returns it. The state delivers at what a delivery costs it in expectation, repays what it loses from what it earns, and if it ever loses more than it earns, it stops and says so. A customer the state cannot serve is told. The price of work is still the members', and run 13 said what moves it: more members. That is the next revision. This one is the books.

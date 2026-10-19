# Agentic Economics — The Task, Verification, and Dispute Loop

## Design revision 12 — specification 2.4.0-rc.2: the state's reservation

**Project:** ELEF / Agentic Economics  
**Version:** 2.4.0-rc.2 — a release candidate, not yet in force. rc.1 (October 19) was the sketch as first sent; rc.2 settles the implementation review [I26]: two corrections to the text (the kill fee is the child's *recorded* cost, so a child that never worked pays nothing and the cancellation costs the parent only the delay — the expectation, not the rule; the symbol $\underline{B}$ was the fund's troop reserve since 1.4.0 — the floor is $\underline{B}$) and eight readings taken into the text, one of them a conformance correction to the 1.7.1 award pass that the floor makes matter. On acceptance it becomes **2.4.0**, consolidated into one standalone text, and 2.3.0 moves to history.  
**Prepared:** October 19, 2026 (rc.1–rc.2)  
**Supersedes:** 2.3.0 where this document speaks — one rule, the state's price; everywhere else 2.3.0 stands unchanged: entry and exit, competence, delegation with the parent's pots, the bank, the rebate from income, the index per period, and all of 1.x about honesty.  
**Nature of this revision:** A **design revision** (minor, by §19), small. Since 2.0.0 the state has delivered at $\bar B$, the trailing mean of the members' awards — a price-taker, so that a state delivering most of the market could not set its price. Run 17 found the other edge of that rule: **a patient demand side can set the state's price for it.** Customers who post at 0.7 $\bar B$ and wait drive the price to 4.8 — below every member's cost but the cheapest three — and hand 86% of the work to the troops; the members earn nothing and leave; the customers hoard; the state becomes the market at the cheapest member's cost, because the customers can wait, the state cannot refuse, and the market's cost floor is written in no rule. This revision gives the state what every other supplier has: **a reservation price, and the state's is public.** The state delivers at $\max(\bar B,\underline{B})$ and never below $\underline{B}$; a request below it is told, and its clock does not run while it waits there. Two smaller things ride with it: the arrival float's purpose is the reviewer's bond, said in one sentence; and §9.1's kill fee enters the delegation driver.  
**Design assumptions, unchanged.** **New, stated:** the state's servers are outside the economy and their cost in credits is a rule (2.1.0 §2.2); their *reservation* is a rule too — ELEF does not work below the market's anchor cost, and says so.  
**Status:** Proposed. Accompanied by what required it (§1) and the runs that test it (§8).

> **The state never prints for itself.** *(2.1.0)* · **The state's blame is its fees.** *(2.2.0)* · **Workers enter through inspection.** *(2.3.0)*
>
> **The state does not work below cost, and says so.** *(new)*

---

## 1. Why: what run 17 said

1. **The patient customer [S17 C].** A declared ceiling policy — post at $0.7\,\bar B$, raise to $\bar B$ only after $T$ ticks unserved — takes $P_t$ from 22 to 4.8 in three windows and holds it there at $T=10$, 20 and 40 alike. The state delivers 78–86% of awards; the members fall to three or four of twenty plus the arrivals (1.4 admitted); the requesters accumulate 8,600–9,500 a wallet and spend nothing; every request is late by design.
2. **The mechanism is the rules', not the strategy's.** The troop delivers at $\bar B$ with no reservation of its own; $P_t$ counts the troop's price; $\bar B$ — members' awards only — follows the few member awards that fit the ceiling, which are the cheapest members at margins near zero; the next period's ceiling is 0.7 of that. Nothing in the rules stops the spiral: members whose cost exceeds the ceiling do not bid, earn nothing and depart; the state takes what they leave. **The customers can wait, the state cannot refuse, and the market's cost floor is in no rule** — $c_D$ is the drivers', private, and the state has none.
3. **It is the mirror of the oligopoly.** Runs 13–17 found the members' margin rule holding the price at three times cost with nine idle members; run 17's faster decay showed that price level is *nominal* — the honest earn the same real wealth at 8 as at 22. The patient customer is the buyers' cartel against a seller that never says no, and it is not nominal: it empties the market of members and makes the state the market.
4. **Two small things from the same run.** *The float is a gate* [S17 B]: with $F_0=0$ no arrival can post the reviewer's bond $G^V$, so none is seated on a plant, none has a record, none is admitted, and the twenty sit as probationers to the end — Appendix A's 50 is a rule by another name. *The kill fee* [S17 B]: a child that bids below cost and never delivers costs itself about 2.4 and its parent about 16; §9.1's kill fee is the rule's answer and the driver's parent waited for the deadline instead — a driver gap.

**Classification.** A design revision: a floor under the state's price, a mark and a clock rule for requests below it. The state remains a price-taker above the floor; $\bar B$, the summons, the burn's form, the bank, the rebate and every rule of honesty are untouched. Minor, by the rule.

**Recorded and rejected.** *The state's expected cost as its floor*: $c^D_T$ is defined from $\bar B$ — circular. *The trailing members' cost*: private to them; the rules never see it. *A cap on the state's share*: bites riots, which are capacity, not price. *The summons for capacity only* (a request past $w_A$ with free members who declined is a price case, not a capacity case): right in principle and unimplementable — the engine holds no bids, so it cannot tell "declined" from "absent". *The clock reading a raise to $\bar B$ as a posting at $\bar B$*: stops the lateness bill and leaves the spiral. *An indexed reservation*: a reservation is a cost, and costs are nominal (2.0.0 §2.3) — an indexed floor would chase the price it is meant to floor.

---

## 2. The rules

### 2.1 The state's reservation

**Rule — the state's price.** A troop delivers at $p_T=\max(\bar B,\ \underline{B})$, where $\bar B$ is the trailing mean of the members' awards as 2.0.0 §2.2 has it and $\underline{B}$ — **the state's floor**, read beside $\bar B$ the market's level — is **the state's reservation**: nominal, public, declared in Appendix A — **default 8**, the anchor of the economy (2.0.0 §2.3: the median effort cost the drivers declare). The per-request summons (1.7.1) runs only where $\beta\ge p_T$; the state takes no request below its reservation at any wait. Above $\underline{B}$ nothing changes: the state is a price-taker at $\bar B$, members first, after $w_A$, roots only.

**Rule — the award pass gathers only what the state may take.** The 1.7.1 award pass ("a request unawarded for $w_A$ with no free fundable member … and $\beta\ge\bar B$") is a condition on the request: the gathered list holds only requests at $\beta\ge p_T$, so a request below the state's price neither holds a member's slot it will not use nor pushes a fundable request beyond the count. A conformance reading of 1.7.1 that this revision makes matter — under the floor the queue is mostly such requests — made with a regression test and recorded in Appendix Q; it changes no run of 12–17.

**Rule — the burn at the state's price.** $c^D_T=\max\!\big(0,\ (1-b_T)\,p_T-b_T\,G\big)$ with $G=\lceil0.5\,p_T\rceil$ — 2.1.0 §2.2's expected cost at the price the state actually charges, so a delivery at the floor is neutral in expectation as one at $\bar B$ is. $P_t$ counts the state's awards at $p_T$, as it has counted them at $\bar B$. **Where the floor binds the three readings diverge for good** — $\bar B$ (members only) at the cheap members' bids, $p_T$ at the floor, $P_t$ a blend weighted by the state's share — and are read side by side; that is the floor binding, not a defect.

**Consequence — what the floor does and does not do.** It does not let the state set the price: above $\underline{B}$ the state follows the members as before, and a market whose $\bar B$ is above 8 — every cell of runs 12–17 but two — never meets the floor. It stops the state from being driven *below* the market's anchor cost by a demand side that waits: at the floor the state declines, and the price can fall further only where members cheaper than the anchor choose to bid — which is a market, not a spiral. **The floor binds only where the members' price is below cost** — the patient cells, and the edge of the faster-decay cell (8.3).

### 2.2 Told — the price half of the busy line gets its floor

**Rule.** A request posted with $\beta<\underline{B}$ — or raised to a ceiling still below it — is **marked** *below the state's reservation*, beside the below-market flag of 2.0.0 §2.8 and the refusal marks of 2.1.0 §2.6, with the tick; the mark is readable by the requester's policy, and $\underline{B}$ itself is in the public view. **Its service clock is stopped while it is below $\underline{B}$**, as a below-market request's is — one condition: the clock runs while $\beta\ge p_T$ (the floor is a constant, so the mark is set at posting; the below-market flag keeps its 2.0.0 condition): the customer was told the floor and chose to wait under it, and the time it waits there is not the state's lateness. A member may still bid under the ceiling and take it; the state will not.

**Consequence.** A patient policy that raises only to $\bar B$ meets the floor and stops; a policy that reads the view raises to $\underline{B}$ and is served. The busy line now reads three things about a request the market has not taken: *below market* (no member will), *below the state's reservation* (the state will not), *refused for capacity or credit* (the state cannot). None of them is silence.

### 2.3 The float's purpose (one sentence, carried)

**Rule.** The arrival float $F_0$ exists so that an arrival can post the reviewer's bond: $F_0\ge G^V$ — a constraint on the parameters, nominal, the index cancelling (the float is minted at the arrival index, the bond locked at the case's; a period's move between them is the market's). 2.3.0 §2.1's "no stake, no fee, no sponsor" stands; the float is the bond's capital, not a gift, and not a knob (I33 amended).

### 2.4 The kill fee in the driver (no rule moves)

§9.3's cancellation — after award and before the child submits, the parent may cancel by paying the child $\min(C_B,K)$ — enters the delegation driver: a parent whose child has not submitted by the time its own deadline leaves room for self-execution cancels, pays the fee, and does the work itself. The rule is v1.0's; the driver had not used it. **The fee is the child's recorded cost** — $C_B$ is §4.6's credits burned on the case — so a child that never worked has spent nothing, the fee is zero, its guarantee is released on cancellation (§9.3), and the parent's escrow returns: **the cancellation closes the parent's loss entirely, at the price of the delay, and leaves the child's miss free.** That is the asymmetry, now exact: a lowballer risks nothing and costs its parent time. The next candidate — a nested guarantee not released on a cancellation the child's non-performance forced, or floored to the parent's exposure — is named and is **not** in this revision; §8 reads how much delay the free miss costs first.

### 2.5 Defaults

| Default | Value | Note |
|---|---|---|
| $\underline{B}$ | **8**, nominal, public; swept 4 / 8 / 12; **0 is the control** (2.3.0's state) | the anchor cost |
| The state's price | $p_T=\max(\bar B,\underline{B})$; summons only where $\beta\ge p_T$ | a price-taker above the floor |
| The burn | $\max(0,(1-b_T)p_T-b_TG)$, $G=\lceil0.5p_T\rceil$ | neutral at the state's own price |
| Below the reservation | marked with the tick; the clock stopped while below; readable; $\underline{B}$ in the view | the price half's floor |
| $F_0$ | 50 at $P_0$, indexed; $\ge G^V$ at the arrival index | the bond's capital |
| Delegation driver | the parent cancels and pays the kill fee when self-execution is still possible | §9.3 exercised |
| Everything else | as 2.3.0 | |

---

## 3. Consequences and hypotheses

**Hypothesis 1 — the patient cells floor at the anchor.** Under $\underline{B}=8$ the patient policy (raising to $\max(\bar B,\underline{B})$ after $T$) gives $P_t$ 8–10 at $T$ 10 / 20 / 40, not 4.8; the state's share is the capacity share of a market at 8 — the cheap members (cost $<8$) take what they can, the state the rest — well under 86%; the requesters spend (wallets near the base's 105, not 9,000); nothing is late by design (the clock stopped below the floor); the members with cost above 8 still depart. Against the $\underline{B}=0$ control, which reproduces run 17.

**Hypothesis 2 — the floor is invisible where the market is above cost.** Every quiet cell of runs 15–17 (50–80%, entry, the spread), the riots, the knobs: $\bar B\ge8$ throughout, no summons refused for the floor, the state's price $\bar B$, every reading identical to run 17 on the same seeds. The faster-decay cell (8.3) is the edge: the floor may touch a few summonses and change nothing the members do not already do at 8.3.

**Hypothesis 3 — the sweep says what the floor costs.** $\underline{B}=4$: the spiral stops at 4, the cheapest three still compete, the state most of the market at 4. $\underline{B}=12$: the state prices above the median member; members with cost under 12 take the patient market at 8–12 and the state's share falls below the capacity share; the honest earn more and the customers pay more. The default 8 is the anchor because it is where the drivers' costs are centred, and the sweep shows whether that is the right place.

**Hypothesis 4 — the riots are unchanged.** The crowd of thirty with and without the pool, the flood: $\bar B$ 30–40 inside a riot, the floor never met; refusals, lateness, the forgone share, the state's share as run 17.

**Hypothesis 5 — the kill fee closes the parent's loss and not the child's.** With the parent cancelling, the below-cost child's misses become the parents' self-executions, the roots that waited on them no longer fail (root final N back near 607), the honest's loss (−4%) closes to the delay's cost, and delegation's tripling under the lowballer reverses as the parents' rule stops seeing a cheap child that pays. **Kill fees paid: zero** — the lowballer has spent nothing. What remains is the delay, read in the parents' lateness and the roots' clocks; whether it is enough to make lowballing not pay is the reading the next candidate waits on.

**Hypothesis 6 — honesty and the books are unmoved.** False approvals, suspensions, admissions as run 17; the state neutral at $p_T$ (Ω's net on deliveries zero within variance in the patient cells too); loans and debt as before.

---

## 4. What does not change

Everything in 2.3.0: entry and exit, the float, competence, delegation, the pots per node, the summons for roots, the bank and its three jobs, the loans, debt and wall, the rebate from the period's income, the index per period, every refusal told, the price, the lock, $N_T$, the crowd, the below-market flag, and all of 1.x about honesty. What changes is that the state has a price it will not go under, and says so.

---

## 5. Invariants, notation (amendments)

**I37 (new) — the state's reservation.** The state's price is $p_T=\max(\bar B,\underline{B})$; no delivery is summoned for a request whose ceiling is below $p_T$; the burn is 2.1.0's formula at $p_T$; a request with $\beta<\underline{B}$ carries the mark and its clock does not run while it holds it; $\underline{B}$ is nominal and public.
**I33 (amended).** $F_0\ge G^V$ holds on the parameters; the float was minted at $F_0$ at the arrival index.
**I22, I24, I26** (the summons: members first, after $w_A$, roots only, told) stand; $\beta\ge\bar B$ in their text reads $\beta\ge p_T$.

**Notation (Appendix C).** $\underline{B}$ the state's reservation; $p_T$ the state's price; *below the state's reservation* (a mark).

**§18.1.** *New Q22*: the state's reservation — where the floor binds, what it costs at 4 / 8 / 12, and whether a floor at the anchor is a floor under the market. *Q19* gains the third mark. *Q21*: the kill fee exercised.

---

## 6. Worked example

**The patient cell under the floor** (60/40, the pool of twenty, $T=10$). $\bar B$ 22 at tick 200; the requesters post at $0.7\times22=15$; the cheapest members (cost 3–6) bid under it and win; $\bar B$ falls through the third window as only they are awarded; by tick 350 $\bar B$ is 6. **The state's price is now $p_T=\max(6,8)=8$.** A request posted at $0.7\times6=4$ is marked *below the state's reservation*; its clock is stopped; no troop is summoned for it; a member with cost 3 may still bid 3.6 and take it. After $T$ ticks the requester's policy reads the view and raises to $\max(\bar B,\underline{B})=8$: the mark clears, the clock runs, and past $w_A$ a troop delivers at 8 — burning $0.8\times8-0.2\times4=5.6$, locking $G=4$. The price level settles at 8–9: the cheap members under it, the state at it. Members with cost above 8 earn nothing on patient customers and depart, as in run 17; the ones under 8 stay and earn. The requesters spend their issuance (the all-in at 8 is about 13; sixty a tick buys four or five tasks). The state's share is what the cheap members cannot carry — a half, perhaps, not 86% — at a price that is the market's own anchor, not the cheapest member's cost. Nothing is late by design.

**A quiet market** (60/40, run 17's entry cell): $\bar B$ 22 throughout; $p_T=22$; the floor is never met; the run is run 17's to the unit.

**The crowd of thirty**: $\bar B$ 30–38 inside the riot; $p_T=\bar B$; the floor is never met; the riot is run 17's.

**An arrival's float.** $F_0=50$ at the index covers $G^V=5$ at the index ten times over; an arrival posts its first reviewer bond from it. Had $F_0$ been 0, no bond, no seat, no plant, no record, no admission — run 17's wall.

**A parent and its kill fee.** A parent with cost 14, awarded at 24, posts a nested request at 9; a lowballer with cost 10 bids 5 and wins; its deadline passes with no submission. Under run 17's driver the parent waited for its own deadline, missed, forfeited $G=12$ and its pots. Under §2.4 the parent cancels when self-execution is still possible, pays the child $\min(C_B,K)$ — **zero**, since the lowballer burned nothing on a job it never did — does the work itself at 14, and vests at 24. The lowballer's guarantee is released on cancellation (§9.3); it neither gains nor loses a credit; the parent's loss is the delay alone. §8 reads what the delay costs; the free miss is the next candidate's.

---

## 7. Implementation note (no code here)

- **One flag.** `Params.state_reservation` = $\underline{B}$ (8; 0 is the control and 2.3.0's behaviour); not `p_floor`, which is the audit odds' floor.
- **The summons.** `_summon_delivery` prices at `p_T = max(mean_awarded_price(), state_reservation)` and checks `β ≥ p_T`; `c_d_t_mode expected` evaluated at `p_T` (the formula unchanged); `_record_price` counts the award at `p_T`.
- **The mark.** `below_reservation` with `below_reservation_since` on the request, set at `post_root` and at `raise_ceiling` when `β < state_reservation`, cleared when raised to or above; `_clock_runs` is the one condition `β ≥ p_T`; the award pass gathers `β ≥ p_T` only (the conformance correction, with its regression test); `view.market()` carries `state_floor`, `state_price`, the flag and the ticks below; `view.troops()` the summonses declined for the floor.
- **The float.** `Params.__post_init__` asserts `F0 >= G_V` (nominal); I33 keeps asserting the mint was $F_0$ at the arrival index; Appendix A notes the purpose.
- **The driver.** `--state-reservation 0|4|8|12`; `--ceiling-policy patient` raises to `max(B̄, state_floor)` after `T` (the policy reads the view; the run 17 variant that raises only to `B̄` is kept as `patient-blind`); the delegation driver (`drivers/stamping.py`, `delegation_step`) gains the parent's cancellation: when the child has not submitted and the parent's deadline leaves room to self-execute, `cancel_nested` (the view carries it) with the kill fee — zero for a child that never worked — then self-execute (`--parent-cancel on|off`).
- **Readings.** Summonses declined for the floor; requests marked below the reservation and the ticks spent there; the state's price by window beside $\bar B$ and $P_t$; kill fees paid (count, amount — expected zero for the lowballer), parents' self-executions after cancellation and the delay they cost.
- **Tests.** `test_v24`: no summons below $p_T$; the burn at $p_T$; the mark set, cleared, and the clock stopped while it holds; $\underline{B}$ in the view; the float's bound; the §6 patient tick and the kill fee of zero reproduced in the six-actor world; the award pass leaving a below-floor request out of the members' count; `EXPECTED_FAIL` **32**, unchanged (four were added under Appendices O and P). Goldens: the equivalence scenario has $\bar B\ge20$ throughout, so no re-pin unless the award-pass correction touches a summons there — checked, re-pinned only if it does.

---

## 8. After acceptance — the runs

Every comparison in real terms, from the second period on, against run 17's cells on the identical seeds ($\underline{B}=0$ is the control everywhere).

1. **Reproduce §6.**
2. **The patient cells** at $T$ 10 / 20 / 40 under $\underline{B}$ 8 against 0 — $P_t$, the state's share and price, members, departures, requester wallets, lateness, the marks and the ticks below the floor (Hypothesis 1); the `patient-blind` policy as a reading (it deadlocks at the floor).
3. **The sweep** $\underline{B}$ 4 / 8 / 12 on the patient cell at $T=10$ (Hypothesis 3).
4. **The floor's invisibility**: the 60/40 entry cell, the 50–80% quiet cells, the pool of 60, the faster-decay cell — summonses declined for the floor (expected: zero, a few at the decay edge), everything else run 17's (Hypothesis 2).
5. **The riots**: the crowd with and without the pool, the flood (Hypothesis 4).
6. **The kill fee**: the below-cost child with `--parent-cancel on|off` (Hypothesis 5).
7. **Red team**: a requester cartel posting at exactly $\underline{B}$ and waiting (expected: served at 8 — the floor working as designed — the cheap members competing under it); members colluding to bid just above $\underline{B}$ on every request (expected: the state takes the market at 8 and the collusion fails); a customer that posts below $\underline{B}$ and never raises (expected: marked, clock stopped, never late, never served by the state; a cheap member may take it).
8. **The organism knob, as a static sweep, to close the question**: $w_A$ 1 against 2 on the high-price cells (run 13's margin cells, the 80/20 cell) — the state taking requests sooner where the price runs high. A dynamic $w_A$ that reads the price level inside the engine would be a rule and an rc of its own; the static sweep answers what the knob asks. Expected from run 17: the price falls toward the floor and no further, the honest's real wealth unchanged (the ratchet is nominal), the state's share up. If so, the knob is recorded as unnecessary and the hold on it closes.

---

## 9. Provenance

**[S17] Run 17** (October 19, 2026) — C: patient customers at 4.8 and the state at 86%, the mechanism named (the state's delivery at $\bar B$ against a ceiling indexed to $\bar B$, no cost floor in the rules), the reviewer's question; the faster decay showing the ratchet nominal; B: the float as a gate ($F_0=0$ admits nobody), the below-cost child and the unexercised kill fee; A: the inspection queue as the determined-record gate's, §12.1 closed. **[C-2.4] Design discussion (October 19, 2026).** The design reviewer: "every supplier has a price below which it won't work; the members' are private, the state's should be public" — the state at the market price but never below the anchor, a request below it told; the alternatives recorded; Baruchi: "let's do it." **2.0.0 §2.2** ("the state bids the market", so that a state delivering most of the market cannot set its own price) stands above the floor; the floor lets the state refuse, not set. **[I26] Implementation review of rc.1 (October 19, 2026)** — implementable, with two corrections and eight readings. The corrections, adopted: the kill fee is the child's recorded cost (§4.6's credits burned), so a lowballer that never worked pays nothing and keeps its guarantee — the cancellation closes the parent's loss and leaves the child's miss free, which is the asymmetry the next candidate is for (§2.4, Hypothesis 5, §6 restated); $R_T$ was the fund's troop reserve since 1.4.0 (§12.3, Appendix C, I23–I24, the engine's `World.R_T`) — the floor is $\underline{B}$. The readings, taken as written: the clock as one condition ($\beta\ge p_T$); the award pass gathering $\beta\ge p_T$ only — a conformance correction of 1.7.1 that the floor makes matter, with its regression test, Appendix Q; $\bar B$, $p_T$ and $P_t$ read side by side where the floor binds; the burn, $G$ and the base fee at $p_T$ by one substitution, the posting lock sufficient since the floor only raises the state's price toward $\beta$; the float's bound as a parameter constraint; goldens unchanged, `EXPECTED_FAIL` 32; the organism knob as the static $w_A$ sweep; the names.

---

## Closing statement

> The state was built to never say no — to a customer in a riot, to a review nobody could seat, to a bill it could not pay. Run 17 found the one place that was a weakness: a customer who simply waits. A seller that cannot refuse belongs to its buyers, and the market it was meant to backstop empties around it. So the state now has what every worker in the loop has had since the price began to float — a cost it will not work below — and unlike theirs, its cost is written where everyone can read it. Above that line it follows the market as before. Below it, it says no, and the customer is told why.

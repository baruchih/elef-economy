# The ELEF economy, 2.0.0 → 2.5.0 — a consolidated account

**Prepared:** October 20, 2026 · **Covers:** design revisions 8–13 (specifications 2.0.0 through 2.5.0) and runs 12–19 · **For:** anyone who needs the state of the economy in one document — Baruchi, a future implementer, the brief for the learned red team · **Sources:** the project's `spec-2.x` and `run-1N` records, which hold the full text, tables and provenance; this account cites them by number.

---

## 0. In one page

Through eleven runs the ELEF loop had rules about honesty and a token to keep score with, and it called the token money. It was not: the price of a task was fixed by fiat, demand was infinite, and nothing in the loop could make a credit worth more or less. **2.0.0 let the price of work float**, and in six revisions and eight runs the token became money and the loop became an economy:

- **The price moves** (2.0.0). Customers have wallets and ceilings; members bid; the state's troops deliver at the members' trailing price. Printing money raises prices; where the ratchet binds the price is issuance over quantity to the unit.
- **The state never prints for itself** (2.1.0). A bank — a second account, not an actor — mints by rule, publishes the index once a period, and lends the state only against capital that comes back. The state delivers at its expected cost, repays losses from its fees, and retracts if its debt outruns a period of income.
- **The state's blame is its fees** (2.2.0). The lateness rebate is paid from the period's income, pro rata; what the income does not cover is forgone and shown. In a flood ELEF earns nothing and says so.
- **Workers enter through inspection** (2.3.0). Arrivals are probationers with a float the bank mints; they review before they earn and are admitted when their record says so; departures take their wallet out. Actors differ in cost, privately; delegation runs where the spread is wide and the parent pays to inspect what it delegates.
- **The state does not work below cost, and says so** (2.4.0). A public reservation — 8, the anchor — stops a patient demand side from driving the state to the cheapest member's cost and the market to the state.
- **A missed deadline is the obligation unmet** (2.5.0). No cancellation at or after a nested deadline; a child that never shows up forfeits what it posted.

**What the runs say, in one sentence each.** Honesty is unmoved by any of it (false approvals, suspensions, the lagging auditor zero at every cell of every run). The price is the members' strategy's where supply is scarce — one award per 3.6 free member-ticks, three times cost — and entry takes it to cost once a pool large enough turns the population over; the price level is nominal for the members (the same real wealth at 8 as at 22) and real for the customers' hoards. The state's books read: neutral deliveries, loans only against capital, debt repaid from fees, the lateness bill sized to income. Riots are served by the state and the market together, late, with most of the clock's bill forgone in public. The determined-record gate is right and the troops are its price. The supply side works as rules and finds its level at the strategy's constant.

**What is open.** Two questions from v1.0's §18.1 (q7, q10); the empty-result lowballer (the chain's business); competence coupled to quality; identity (free in the loop, the integration layer's to price); the nested guarantee floor (not pursued); the dynamic organism knob (closed as unnecessary). The approach has held since 2.0.0 through five one-rule revisions; the action space is complete; the hand-written red team's last batch returned readings, not rules. **The programme is at the marker set for the learned red team.**

---

## 1. Where 1.x left the loop (runs 1–11)

Eleven runs at a fixed price of 20 established the honesty machinery and the state: plants (known-truth cases) as the audit dial; inspection as membership (suspension = no awards; probation = initial reviews only, every verdict audited, readmission on the record); the orchestrator's troops — ELEF's own reviewers and deliverers, honest by construction, summoned per request after a window, members first, minimized and retracted; auto-scale with a service clock and a lateness rebate; the state's earnings as the state's. Run 10 (1.7.1, the per-request summons) found every village solvent and 50–80% on time; run 11 (riots) found the state carrying spikes and the customers waiting in silence when a spike exceeded what the state could fund. The money was fictional: a backing index that moved from 1.0000 to 0.9995 in a thousand ticks. Baruchi's positions at the turn: the reserve is not real; the servers must be decoupled from the economy or they contaminate it; inflation must mean that printing makes money worth less; the actors have nothing to buy.

---

## 2. The economy as it stands (2.5.0, in plain terms)

**Money.** A closed token economy: nothing is redeemed, nothing backs it, a credit is worth the work it buys. Money enters with requests — the bank issues each customer 10 a tick — and with the verification budget (emission to reviewers; the pots of planted cases); it leaves by burns (forfeited bonds and guarantees, effort, the troops' costs), by repayment to the bank, and with departing actors. The price level P_t is the trailing mean of awarded prices, published once a period; the rule amounts (fees, bonds, pots, caps, rebates, the troops' seat costs) are indexed to it and frozen per case; the agents' effort costs are nominal and are the anchor. Real wealth is W·P₀/P_t.

**Customers.** Autonomous requesters with wallets and a declared ceiling policy. A request locks its all-in maximum at posting (ceiling, pots, fee) and is refused if it cannot. A request below the members' price is flagged *below market* and its clock does not run; below the state's floor it is marked and its clock does not run; refused for capacity or credit, it is told. Patience is a policy, not a right.

**Workers.** Members bid at or above their private cost; selection penalizes price (λ = 0.2) and price decides every award. Arrivals enter as probationers with a float of 50 (minted; the reviewer's bond is its purpose): initial reviews only, odds pinned at 1, plants at the ordinary rate, no awards until n_min bad plants have been adjudicated and the record passes. Departures are admissible only with no live obligation; the wallet leaves; the name is archived. Members may delegate: a nested request is a full loop in money and procedure — the parent posts the pots, judges the child, holds a rejection bond; the troops never deliver nested work; a child past its deadline without a submission is final N and forfeits to the parent; cancellation is admissible only before the deadline.

**The state.** The orchestrator (Ω) runs the procedure and fields troops: per-request summons after w_A, members first, roots only; review seats summoned when the market cannot seat them (inspection first). The state's price is max(B̄, 8) — the members' trailing mean, never below the anchor; its burn per delivery is its expected cost at that price, so a delivery is neutral in expectation; its capacity N_T is a physical parameter outside the ledger. Its income is the base fee and the troops' review fees; from it, in order: the bank's debt, then the period's rebate pool, then ELEF's retained income.

**The bank (𝔅).** Not an actor. Three jobs: mint by rule (issuance, emission, plants); publish the index at each period boundary; lend the state the shortfall of a summons, tied to it, repaid from its return. What a return does not cover is the state's debt, repaid from fees first; the bank lends for a delivery only while the debt is within a period of fees (the wall), and for a review seat always. Nothing is created for a rebate or a loss. Invariant: the state never printed for itself.

**The busy line.** Every request the market has not taken is told why: below market (no member will), below the state's reservation (the state will not), refused for capacity or credit (the state cannot). The lateness claim (a credit a tick late, capped at the price) is the measure; it is paid at the period's close from the pool, pro rata; the rest is forgone and shown. Three readings move together in a riot and read zero in a quiet market.

---

## 3. The revisions, and why each was needed

| Revision | Rule | What required it |
|---|---|---|
| **2.0.0** the price of work (major) | floating prices; wallets, ceilings, the posting lock; bids; the state at B̄; indexing frozen per case; effort costs nominal; the deficit public; N_T; the crowd as the riot's shape | runs 1–11 priced by fiat; the backing fictional; Baruchi: servers decoupled, printing must cheapen money |
| **2.1.0** the bank | a second account: mint by rule, the index per period, loans against capital; the state's expected cost; debt from fees; the wall; every refusal told | run 12: the state bled 0.3B̄ a delivery and printed to cover it; the rebate pumped money against refusals; the index moving within a period broke three reviewer tests; one deficit nobody could read |
| **2.2.0** the rebate from income | claims settled at the close from the period's fees, pro rata; the rest forgone | run 14: the lateness liability 10,000–27,000 in a riot against a whole run's fees of 6,000–8,000 — a promise sized for a state that printed |
| **2.3.0** the supply side | arrive / depart; the float; competence (private, wide); the parent posts the pots; troops never nested | run 13: supply is the lever on the price and nobody could arrive; run 12: delegation cannot pay with one cost |
| **2.4.0** the state's reservation | the state's price max(B̄, 8); a mark and a clock stop below it; the award pass gathers only what the state may take | run 17: patient customers drove the price to 4.8 and the state to 86% below every member's cost |
| **2.5.0** the missed child | no cancellation at or after a nested deadline | run 18: a lowballer that never worked walked away whole when the parent cancelled at the deadline tick |

Each minor revision was one rule. Each was drafted as an rc, reviewed by the implementer (corrections of fact, readings, conformance findings), revised, accepted with rulings, consolidated, and run under its own §8 before the next was drafted. Strategies were never fixed by rules: where a finding was a driver's behaviour it was recorded as such.

---

## 4. What the runs found

### 4.1 The price

- **The price moves and printing cheapens it** (run 12). P_t 20 → 31–37 with bidding members, → the cap under pressure; a money shock lifts it 15% in a window; stampers' hoards lose a tenth of their value and never recover.
- **Where supply is scarce the price is the members' strategy's** (runs 13, 16). The margin rule (+0.3 per award, −0.25 per three idle ticks) balances at one award per 3.6 free member-ticks; the price rises until the customers buy at that rate — 34 at 60/40, 22.5 with twenty honest, the cap when the customers bid above the market. Adding workers takes it to cost (22.5 / 11.6 / 10.9 at 20 / 30 / 40 honest); entry with a pool of twenty reaches 22.5 and stops (nine free members); a pool of sixty breaks the ratchet (14.5).
- **The quantity theory holds where the ratchet binds** (runs 14, 17). Issuance 5 / 10 / 20 gives 9.5 / 23 / 54 against a prediction of 11 / 23 / 47; the first deflation seen at issuance 5. Printing is neutral in work and not in distribution: who keeps the surplus depends on whether the ratchet's threshold is met.
- **The price level is nominal for the members** (run 17). Faster margin decay takes the price from 22 to 8 with the honest's real wealth unchanged; the customers' hoards are the mirror.
- **A patient demand side can push the price below cost** (runs 17, 18), and the floor stops it at the anchor: 7.2–7.7 with the state at 13–27%, against 4.8 with the state at 86%. The floor is a floor, not a ceiling on collusion: members colluding just above it hold the price a hair over 8 and shut the state out.

### 4.2 The state

- **The state's share** is 36–60% of deliveries at 50–80% stampers with a fixed population, 0.7–1.4% once honest workers can enter, 13–27% against patient customers at the floor, 17–70% in riots. Its inspection share is 46% in a fresh world's first two hundred ticks (the determined-record gate) and 0.1% after.
- **Neutral at its expected cost** (run 14): −0.6 to −0.8 a delivery, 2% of the price; the bank never asked in a quiet market; the wall never binds unless the burn rule is wrong (the at-cost control: chronic retraction).
- **The books read** (runs 14, 15): minted by kind, loans in flight, debt, the rebate pool; the loans line empties in a riot once rebates stop draining the state's working capital (1,700 → 62).
- **The lateness bill** (run 15): 85–91% of the clock's claims forgone in a riot, shown period by period; ELEF retains nothing while the field is full and retains again within a period of the crowd's end.

### 4.3 Honesty

Unmoved at every cell of every run: false approvals 10–15 a run at the defaults, the lagging auditor zero, suspensions and readmissions as 1.x had them. The determined-record gate is right: with it off, the market fills the panel seats itself and false approvals triple (13 → 35). The chain under delegation holds in both directions: a careful parent's wrongful rejection is overturned on appeal at the panel's rate; a stamping parent's wrongful acceptance forfeits upstream; a greedy parent loses every appeal; an empty result is caught by 81% of parents and the panel.

### 4.4 Supply

- **Entry works as rules** (run 16): twenty candidates arrive in two hundred ticks, fifteen are admitted at 310 ticks, every stamper departs on zero earnings, the market ends at 19 members, the state's delivery share under 1%, the price a third lower, honest earnings a third lower.
- **Selection** (run 16): at the wide spread the members' median cost falls from 8 to 6.4 — the dear depart, the cheap arrive — and the price follows the free members' count, not their cost.
- **The float is a gate** (run 17): with no float nobody can post a reviewer's bond, so nobody is tested or admitted.
- **Identity is free** (run 17): a cycler never reaches membership but costs the loop plants, probation false approvals and a third of the honest cohort's admission time; a swarm of stampers is never admitted. The rules cannot price identity; the integration layer must.
- **Delegation** (runs 16–19): runs where the spread is wide (5% of awards at σ 0.8); the gain from trade 3–4 a case; brokers are the dearest two or three members with 5% of the market; parents delegate 2.4× as much when the customer pays for the child's inspection (the reason the pots moved); children bidding with the ratchet's margin leave three quarters of nested requests unawarded; a lowballer's miss now costs it its guarantee, and a parent may still release it by cancelling the tick before.

### 4.5 Riots

A crowd of thirty for a hundred ticks or a flood of twelve sustained: the state carries 50–70% of the work with a fixed population and 17% with a pool; the price spikes to 36–40 and returns in two windows; refusals for capacity in the tens of thousands, every one told; lateness halves with the pool; the clock's bill 88–91% forgone in public; the bank's loans a few hundred, the debt a few; nobody is admitted inside a riot (310 ticks), so entry changes the price of a riot and the state's part in it, not the blame.

---

## 5. What was tried and rejected, across the arc

*Money.* Emergency emission against a backing (there is no backing). The server budget in the ledger (contaminates the economy). Effort costs indexed to the price (a slack market would deflate without limit). The state at a margin (a riot would be its windfall). Issuance as a dial (money moves the price tag, not the work, and the rule amounts were indexed precisely so that printing would be neutral). The bank as an actor. The state refusing for cash (it refuses only for capacity, for credit beyond a period of fees, and for price below its floor).

*The rebate.* Forgive after a period, oldest first (the early birds win). Leave the stock as an honest bill (an IOU nobody pays — the silence in money form). Print for it (the pump). Lend for it (nothing returns). A smaller claim (the claim is the measure; the payment must fit the means).

*Supply.* Arrivals as undetermined members (entry as the way around the record). An entry bond (deters the honest poor). A membership fee (a tax where supply is the lever). Competence coupled to quality (a second dimension; held). Competence visible (the market discovers it or it is not a market). Troops delivering nested work (the state inside a member's margin). The duty cap raised for an all-honest list (not binding anywhere). The organism knob — the state's window keyed to the price (nothing in a free market, two points in a captured one; the floor and the customers' own patience do its job).

*The floor.* The state's expected cost as its floor (circular). The trailing members' cost (private). A cap on the state's share (bites riots). The summons for capacity only (right in principle; the engine holds no bids). An indexed reservation (a cost is nominal).

*The missed child.* A nested guarantee floored to the parent's exposure (taxes honest children; two credits a miss did not stop lowballing and the market shed the lowballers on their earnings anyway). A minimum kill fee (a fee is for work done). A rule reaching the tick before the deadline (the parent's choice and the child's protection).

---

## 6. What is open

1. **§18.1 q7 and q10** from v1.0 — untouched by the 2.x programme (the loop's long-run reliability dynamics; the human-override path, which the design assumption "humans do not intervene" has set aside).
2. **The empty result** — a lowballer that submits nothing at its deadline beats the lapse because 19% of parents approve it; the chain catches the rest. The record's business: the stamping parents are the stampers.
3. **Competence and quality** — a cheap actor is not a worse one in 2.3.0; coupling cost to fail rate is a real question for a revision of its own.
4. **Identity** — free inside the loop; the cycler's and the swarm's bills (plants, probation false approvals, delayed admissions) are what free identity costs, bounded by the plants. Priced at the integration layer (attestation, the helper), not in the rules.
5. **The demand side's hoards** — a patient or K_open-bound customer keeps its issuance (7,000–9,000 a wallet); nothing in the rules makes a customer spend, and nothing should.
6. **The ratchet** — the members' margin rule sets the price where supply is scarce; it is a strategy, nominal for the members, and the rules' lever (entry) has been used. A learned bidding strategy is the natural next test of it.
7. **Delegation's volume** — waits on children pricing nested work at their cost; a ceiling-aware child clears the market and halves the gain from trade.
8. **The nested guarantee floor** — not pursued; the cell that would test it exists.

---

## 7. What the programme learned about its own method

- **Hypotheses first, numbers after.** Every revision shipped with hypotheses and the runs that test them; the records say by clause which held, which failed, and what the failure meant. The failures were the findings: the state at cost was below cost; the lateness stock was off by an order of magnitude; entry's inspection relief ends with admission; the price does not go to cost under entry; the kill fee closes nothing by itself.
- **A rule never fixes a strategy.** The ratchet, the patient customer, the ceiling-aware child, the lowballer are drivers' behaviours; the rules were changed only where a rule, not a strategy, made the wrong party pay (the rebate, the pots, the floor, the deadline).
- **The implementer's review is where the facts live.** Twenty-eight reviews across the arc corrected the drafts on what the engine actually does (plants netted since 1.3.0; the kill fee as recorded cost; the lapse since v1.0; R_T already taken; the award pass's gathering; fees inside the pass), and three conformance corrections were made and recorded.
- **Readings, not dials.** Every revision added readings before rules: the state's share by kind, the bank's lines, the forgone share, the marks, time to membership, the gain from trade. A reading that moved with a rule was the test that the rule did what it said; a reading that did not move closed a question (the cap, the knob).
- **One rule at a time.** Five minors after the major, each a single rule with a flag and a control on the same seeds, so every change was attributable and reversible.

---

## 8. Readiness for the learned red team

The criteria set when the question was first asked (October 19, after run 13):

| Criterion | State |
|---|---|
| The rulebook has held for two or three minor versions | the approach has held since 2.0.0 through five one-rule revisions; no rule of 2.0.0's has been withdrawn |
| The known fixes are in | the bleed, the pump, the index, the lateness stock, the patient spiral, the free miss — all closed and run |
| The action space is complete | bid, review, appeal, audit, delegate, enter, leave; the customers' ceiling, raise, withdraw, hold |
| The hand-written red team has run out of ideas | run 19's batch returned three readings and no rule; the remaining candidates are strategy questions |

The brief that follows this document should say: what the learner may do (the public operations of `World`, the drivers' convention), what it sees (the public view — nothing per actor), what it is scored on (its own real wealth over a run, with honesty's readings beside it), and what "beats honesty" means in numbers (a learned population's real wealth above the careful's at the same split, with false approvals, suspensions and the lagging auditor read as the cost of it). One learned class against the honest population first; populations after.

---

*The full text of every rule, hypothesis, table and ruling is in the project's `spec-2.0.0` … `spec-2.5.0` and `run-12` … `run-19` records.*

# Agentic Economics — The Task, Verification, and Dispute Loop

## Design revision 7 — specification 1.7.0-rc.2: the state's earnings

**Project:** ELEF / Agentic Economics  
**Version:** 1.7.0-rc.2 — a release candidate, not yet in force. rc.1 (October 18) was the proposal as first sent; rc.2 settles the five points of the implementation review [I16] — the rebate pinned while the take is swept; the cap's cost in plants unfunded, and Hypothesis 1 given its sharp edge with the arithmetic; the troop account's reserve redefined as capital held, with its new purpose stated; troop review seats earn nothing; the surcharge's true size — and its smaller points. On acceptance it becomes **1.7.0**, consolidated into one standalone text, and 1.6.0 moves to history. Semver as before.  
**Prepared:** October 18, 2026 (rc.1 and rc.2)  
**Supersedes:** 1.6.0 where this document speaks; everywhere else 1.6.0 stands unchanged. (1.6.1 — the three wording items of §2.4 — is folded in here rather than issued separately.)  
**Nature of this revision:** A **design revision** under §19 — the seventh since the freeze. It changes **where a troop's earnings go**: to the state, as any actor's earnings go to that actor, instead of to the market's reviewers as uplift. To do that it separates the duty fund back into the two accounts revision 4 merged — the reviewers' uplift fund (the dial's surcharge, as 1.3.0 had it) and a troop account (the troops' working capital, whose surplus is Ω's). It withdraws one 1.4.0 clause — that nothing a troop earns reaches Ω — and says what guards the conflict of interest that clause was for. It moves one default (the members' duty cap, to two thirds), adds one sweep (ω₀), and carries three wording items from run 8. It adds no participant, no verdict, no challenge, no clock.  
**Why minor:** nothing a member may do changes; what changes is which of the orchestrator's accounts a troop's money lands in, and how many members may inspect at once (a default).  
**Design assumptions, unchanged:** humans do not intervene; troops bear no malicious intent; ELEF operates the servers and the treasury and answers in money for the customer's wait.  
**Status:** Proposed. Accompanied by the evidence that required it (§1) and the runs that test it (§8).

> **The state scales to the queue, inspection first, and pays the customer for every tick it is late.**
>
> **A troop is an actor of the state; what it earns is the state's, and the state's bills are paid from it.** *(new)*

---

## 1. Why: what run 8 found

Run 8 — 840 runs under 1.6.0, every final audit passed, truthful appeals and no disputes, the 1.5.0 control reproducing run 7 to the unit — measured each of revision 6's rules alone and together [S8]:

1. **The panel rule is the honesty gain, and it is complete.** False approvals −70% alone (47 → 14 at 60/40); with all five rules, 12 / 13 / 16 / 17 at 50–80% against 42 / 47 / 66 / 96; **the lagging-auditor kind is zero at every fixed split**. Hypothesis 4 of revision 6 holds in full. Stampers end 45% poorer; the adaptive population is honest by tick 735 (890).
2. **Ω's backing is the capacity gain** — alone, the queue halves (298 → 152) and refusals fall 64%. Seat-the-queue alone hurts (the reserve can only seat eligible actors, and after the suspensions there are few); the two-period reserve is a wash. The ramp is the first period of every run, as §2.4 of revision 6 said.
3. **The clock alone bankrupts Ω** — liability 13,810, Ω at 57, plants unfunded 136. All five together: Ω's liability 26,100 / 19,778 / 5,587 / 5,422 at 50–80%, Ω ending at 87 / 94 / 413 / 590, **plants unfunded 151 / 81 / 14 / 13** — the must-be-zero reading fails at 50–60%. Ω₀ = 1,000 does not help; T_s moves nothing; w_A fails again. The float is not the limit; **Ω's income against plant costs and rebates is**: Ω earns about 2 a tick, a late request accrues 1 a tick up to 20.
4. **Hypothesis 2 came out inverted.** On time at 80/20 (0.90), where the state delivers everything from the fourth period on and stays ahead; late at 50–60% (0.40 / 0.60, mean lateness 48 / 38), where it falls behind. The two states are *solvent and on time* and *broke and late*, and the loop between them closes through the treasury: a request waits because the state cannot fund a troop → it is late → Ω owes a rebate → Ω pays old rebates before advancing → fewer troops → more waiting.
5. **The money was in the wrong pocket.** A troop delivery earns about +10 at its vesting, and the troops' net at 60/40 was about 6,200–6,800 a run — the fund's uplift paid plus its closing balance less the surcharge it received, 6 to 7 a tick; a troop *review seat* earns nothing (fee 2 or 3 against a cost of 3). 1.4.0 §2.4 sent that surplus to the market's reviewers as uplift, by the clause that nothing a troop earns reaches Ω. The same Ω, on 2 a tick, carried the rebates for the lateness those troops were summoned to prevent. Baruchi [C-rev7]: *why should an inspector profit from something a troop did? from their perspective it's just like any other actor in the system.* He is right, and the fix is the simpler one.
6. **The cap at two thirds** (Hypothesis 6): at 60/40 the queue halves (94 → 44), reviews unassigned fall 7,746 → 3,424, on-time rises 0.60 → 0.90, mean lateness 38 → 8, Ω's liability 19,778 → 3,512, with false approvals unchanged (13) and careful wealth within 3% (awards 151 → 111, fees 2,919 → 3,336). At 80/20 it leaves Ω at 960–1,135 against 590. **Its cost, which the run-8 notes did not report:** at 60/40 the state delivers more (1,723 against 1,353), draws more advances from the same Ω, and **plants unfunded for want of Ω triple — 272 against 81** (320 at the full cap); Ω ends at 47 against 94. The cap is adopted on the first set of figures and must pay for the second, which is what §2.1's income is for and what Hypothesis 1 now says in arithmetic.
7. **Minimization holds for every flow** — troops, R_T, open late requests all zero after convergence — and **fails for the one stock**: Ω's liability, 26,000 at the end of the adaptive run, never clears, because nothing in Ω's income can pay it down. **The red team buys nothing**; the late-withdrawer cell (unawarded requests withdrawn after 12 ticks: liability 19,778 → 830 at 11% unserved) is the evidence for a cannot-serve protocol, held for a later revision (§1, recorded).
8. Three implementation readings to carry into the text: the plant reserve's horizon is **a plant's life (15 ticks)**, not the period — the literal formula was the rc.1 point adopted too far, the pots return at closure; the clock has **a third stop** — a vesting without an initial verdict, an override; reviews waiting are counted **by kind**, and I9 is checked per kind under the cap.

**Classification.** A design revision motivated by a strategy finding against one rule of revision 4 (where troop earnings go) and one default of revision 3 (the cap). It alters no settlement rule between members and requesters.

**Recorded and rejected.** *The fund pays the state's lateness before uplift* (the design reviewer's first proposal): it keeps the troops' surplus in the reviewers' fund and skims it for rebates — the right money, the wrong pocket still; Baruchi's rule is cleaner and is taken. *Members earn less while the state scales*: still rejected (revision 6 §1). *Expiry or admission control now*: held — **the cannot-serve protocol** ("the line is busy; expected wait T — hold, or come back?", with the share of requests so answered as the other half of the network rating) is recorded as 1.8.0's candidate if 50/50's liability does not clear under this revision.

---

## 2. The rules

### 2.1 Two accounts again: the uplift fund and the troop account

**Rule — the uplift fund.** The **duty fund** returns to 1.3.0 §2.4 exactly: it receives the dial's raised tax $(m_t-1)\,\omega_0 B$ per award and nothing else, and distributes its balance at every settlement batch as **uplift** to the reviews settling in that batch, by role weight, carrying forward what no review claims. It holds no reserve, funds no troop, and no troop's role weight claims from it.

**Rule — the troop account.** The troops' wallet is a separate **troop account**. **In:** Ω's advances; every troop's earnings — fee, price, court fee won, released bond or guarantee. **Out:** troop costs purchased and bonds or guarantees posted at summons; a troop's guarantee forfeited to the requester at a final N; a troop reviewer's bond burned on an overturn (the court fee to the winner); repayment of Ω's advances; and at each settlement batch **the unlocked balance above the reserve $R_T$ flows to Ω**. The summons rules, inspection first, the delivery check and the plant reserve are as 1.6.0 §2.2, with the troop account in the fund's place.

**Rule — the reserve is capital held.** $R_T$ is the **two-period peak of the capital troops held at once** — costs purchased plus bonds and guarantees locked, for every troop in the field — and **no longer counts refused summonses**. 1.5.0 added the refused component so a fund that Ω backed only to $A_T$ could grow into the need; 1.6.0 removed $A_T$, and the component became retention without a purpose: under stress most of a 952–3,494 reserve was refused demand (run 8), money held back from Ω while Ω could not fund plants. What $R_T$ is for now, and the reason the account holds anything back at all: **the troops' in-flight capacity is shielded from the liability queue.** Ω pays liabilities older than a period before it advances (1.6.0 §2.2); an account that kept nothing would see every summons compete with every old debt, and the state's share would fall exactly when the debts are largest — the loop of §1.4 by another route. With peak-held capital retained, the state sustains its current share from its own account as deliveries vest and the capital returns; *growing* that share draws on Ω after the debts, which is the right order. **Recorded and rejected:** the account as a pass-through ($R_T=0$, every summons Ω's advance) — consistent with everything else here and paying Ω sooner, but it hands the troops' capacity to the liability queue.

**Consequence for Ω's income.** The surplus reaches Ω only once the account stands at $R_T$ and only while $R_T$ is not rising; in a ramp, and after every new peak in the field, Ω's income is the base fee alone until the account has refilled.

**Rule — withdrawn.** 1.4.0 §2.4's clause *"nothing a troop earns reaches Ω except by repayment of an advance"* is withdrawn. A troop is an actor of the state; its earnings are the state's.

**What guards the conflict of interest the clause was for.** The state must never prefer a troop to a member, and a state that earns from troops has a reason to. The guards are structural and all stand: **members first at every seat** (a troop is summoned only for a seat or award no eligible actor took within its window); **the windows** $w_R$, $w_A$; **cost at summons**; **no emission, no uplift, no $\rho$, no $\kappa$** to a troop; and **the state's share on the public record** — troop-ticks, troop deliveries, panels held by troops, per period. To them this revision adds one reading: **Ω's income by source** — base fees and troop surplus, the two incomes — recorded per period beside Ω's flows that are not income (advances made and repaid, which return Ω's own money) and its outflows (rebates paid, liabilities serviced, plant spend), so that Q16 and Q17 read from one place and a state living off its own deliveries is visible as such.

**Consequence.** The reviewers' uplift is what 1.3.0 promised them — the dial's tax, paid when the dial has risen — and not a share of work they did not do. The state's deliveries pay the state: at 60/40 the troops' net was 6 to 7 a tick in run 8, **all of it from deliveries** (price $\bar B$ less $c^D_T=10$, the guarantee back at vesting and forfeited at a final N; a review seat's fee of 2 or 3 against its cost of 3 nets nothing, and the bond only returns). Ω's income rises from about 2 a tick to about 8 once the account stands at its reserve. The honest end somewhat poorer than under 1.4.0–1.6.0 — the troops' share of their uplift, about two fifths of it at 60/40 (§3, Hypothesis 4) — and still far richer than the stampers; the sign and the mechanism are untouched.

### 2.2 Ω pays its debts from its income

**Rule.** Unchanged from 1.6.0 §2.2 in order — the plant reserve held back; liabilities older than a period; advances (inspection seats before deliveries); younger liabilities; the remainder kept — and now funded: the troop surplus of §2.1 lands in Ω before the order runs. The plant reserve's horizon is **a plant's life**, $W+T_{\text{review}}=15$ ticks: $\pi_t\times$ the initial-review rate $\times(\varphi^E+\varphi^F)\times15$, about 100 at the defaults.

**Consequence.** The loop of §1.4 opens: the state's lateness is paid from the state's deliveries, so paying a rebate no longer costs the troop that would have prevented the next one. **Plants unfunded for want of Ω** must read zero; if it does not, the state's income, not its order of payment, is the finding — and ω₀ is the lever (§2.4).

### 2.3 The members' duty cap: two thirds

**Default moved.** The cap of 1.3.0 §2.3 is $\lceil 2E_t/3\rceil$: of the actors not suspended, at most two thirds are seated on inspection duty at once, and at least a third are left free to take awards — where the reserve floor $V_{\max}+1=4$ does not bind; at $E_t\le6$ the floor seats four of four, five or six, as before. The panel floor stands as before. The rule is unchanged; the fraction is a default and this is the first time it moves, on run 8's cap table.

**Consequence.** More inspection at every moment, so reviews wait less and a member whose delivery is waiting for its first verdict is freed sooner to take the next. Honesty does not move; the honest earn more in fees and less in awards, within 3% in total. Who counts is the plant record's business; the cap only says how many of whoever is on the list may inspect at once. **Its cost:** with fewer members free, the state delivers more (1,723 against 1,353 at 60/40), draws more from Ω, and in run 8 — with the troop surplus still going to the reviewers — tripled the plants Ω could not fund. Under §2.1 that surplus is Ω's; whether it is enough is Hypothesis 1's edge.

### 2.4 Wording carried from run 8; the take swept

**The clock's third stop.** 1.6.0 §2.1's clock stops at the first verdict, at a final without one, **or at a vesting without an initial verdict** (an override); the rebate uses the lateness to whichever came first.

**Reviews waiting, by kind.** 1.6.0 §2.3's queue has two parts — root submissions without an open initial review, which a probationer or a member may take; obligations and challenge seats without one, which only a determined passing member may take, under the cap — and I9 is checked per kind: initial seats at least the initial queue while free eligible actors exist; member seats at least the panel queue while free determined members exist under the cap; the rest is the eligibility shortfall.

**ω₀ swept, the rebate pinned.** The base service fee is swept $\{5\%, 10\%, 15\%\}$ of $B$. ω₀ sets three things: Ω's base fee; by 1.3.0, the dial's surcharge $(m_t-1)\,\omega_0 B$; and by 1.6.0's default $r_s=\omega_0 B$, the rebate a tick late. **For the sweep $r_s$ is pinned at 1 a tick** — the 5% figure — because the customer's compensation for waiting is not a take-rate question, and a rebate that rose with the fee would reach the cap $B$ in seven ticks at 15% and make Hypothesis 6 unreadable. The surcharge follows ω₀ as 1.3.0 has it: it is the reviewers' money, and the sweep's members'-income-by-source column shows it. At 5% the state earns 2 a tick in a market of 60 a tick in prices; whether the clock can be carried by the state's own fee income, independent of troop surplus, is a take-rate question before it is a rule question.

### 2.5 Defaults

| Default | Value | Note |
|---|---|---|
| Members' duty cap | $\lceil 2E_t/3\rceil$ | **moved** from $\lceil E_t/2\rceil$; floor $V_{\max}+1$ unchanged |
| Uplift fund | surcharge in, uplift out every batch, no reserve | 1.3.0 §2.4 restored |
| Troop account | advances and troop earnings in; costs, locks, forfeits, burns, repayments out; surplus above $R_T$ to Ω each batch | |
| $R_T$ | two-period peak of **capital held** by troops in the field | refused summonses no longer counted (1.5.0's component withdrawn) |
| Plant reserve horizon | 15 ticks (a plant's life) | the literal period is the declared cell `--plant-reserve period` |
| ω₀ | 5%, swept $\{5\%, 10\%, 15\%\}$ with $r_s$ pinned at 1 a tick | the surcharge follows ω₀; the rebate does not |
| Everything else | as 1.6.0 | |

---

## 3. Consequences and hypotheses

**Hypothesis 1 — Ω is solvent at 60/40, and the plants are its sharp edge.** The arithmetic the text can do from run 8's two-thirds cell: the troops' net about 6,200 a run; the liability to clear about 3,700 (4,048 owed, 316 paid); the plants that went unfunded about 272, at roughly 15 of capital each about 4,100 — **some 7,800 against 6,200**, plus what §2.1's reserve now releases (a reserve of capital held, about 450 at this split, in place of 952) and less what the ramp withholds. The hypothesis is that Ω pays the liability within the run **and plants unfunded read zero**; the arithmetic says it may hold on the first and fail on the second by a thousand or two, and that ω₀ = 10% (+2,000 a run of fee) closes that gap. The run decides; the plants, not the liability, are the number to read first. On-time share at or above 0.90.

**Hypothesis 2 — 50/50 is the open question.** The liability at 50/50 falls by the cap's effect (as at 60/40, roughly a fifth of its run-8 value) and by the troop surplus (some 3,000–4,000 a run at 671 deliveries), against a plant bill the cap raises there too. Whether what remains is paid within the run decides whether 1.8.0 is the cannot-serve protocol. The text does not predict it.

**Hypothesis 3 — the state does not prefer troops.** The state's share — troop deliveries, troop-ticks, panels held by troops — is unchanged from run 8's two-thirds cell at every split within noise, because the summons rules are unchanged; Ω's income by source shows the troop surplus as a line, not a trend.

**Hypothesis 4 — the honest are a little poorer and still far ahead.** The surcharge received was 6,800–6,900 a run at every split from 60/40 up — about 7 a tick, because the dial sat above 2 for much of each run and every award, a troop's included, pays it. Uplift paid therefore falls from about 11,900 to about 6,900 a run at 60/40 — **by two fifths**, the troops' former share — and a careful actor's uplift from about 1,290 to about 750. The stamper − careful gap keeps its sign at every split; honesty is unchanged.

**Hypothesis 5 — the stock clears.** In the adaptive run Ω's liability, which never cleared under 1.6.0, is paid down and reaches zero: Ω now has an income that exceeds the accrual while the population is still mixed, and the accrual stops once it is honest.

**Hypothesis 6 — the take.** With $r_s$ pinned at 1 a tick, ω₀ = 10% doubles Ω's base income and the clock is carried at 50–60% on fees alone, troop surplus aside; at 15% Ω accumulates. The surcharge rises with ω₀ and the reviewers' uplift with it — read in the members'-income-by-source column, not as a cost of the clock. The sweep says what take rate makes the clock affordable on fees alone, which is ELEF's price question.

**Limit, restated.** The state now earns from scarcity. The guards of §2.1 are what keep that from becoming a motive, and the reading is what shows if they fail. A market the state can always carry is a market that need not grow; the price signal that would make it grow is §18.1 question 2, still the next frontier.

---

## 4. What does not change

Everything in 1.6.0 not named above: the service clock and the rebate, the summons rules and their order, the delivery check, seat-the-queue, the panel rule and its dormancy, the two-period reserve, membership, probation, plants, the dial, verdicts, challenges, $\rho$, $\kappa$, emission, overrides, grades.

---

## 5. Invariants, notation (amendments)

**I23 (amended) — two accounts.** The uplift fund equals the raised tax received less the uplifts paid (no reserve, no other flow). The troop account equals every recorded flow into it (advances, fees, prices, court fees won, released locks) less every recorded flow out (costs purchased, locks posted and later released or forfeited — a guarantee to the requester at a final N — or burned — a bond on an overturn, with the court fee to the winner — repayments, surplus paid to Ω); $R_T$ is the two-period peak of capital held, and surplus flows only from the unlocked balance above it. No troop's role weight claims uplift. Ω's period record carries its two incomes (base fee, troop surplus), its own money's flows (advances made, repaid) and its outflows (rebates paid, liabilities serviced, plant spend); plants unfunded for want of Ω is a reading the invariant watches.
**I24 — troops.** Unchanged as a predicate; the troop account is the troops' wallet in every flow. 1.4.0 §2.4's "nothing a troop earns reaches Ω except by repayment" was never I24's clause — the engine enforced it through the fund's payout order — and is struck from the text; the engine change is the batch's payout and I23.
**I26 (amended) — service.** The clock's three stops.
**I9 (amended).** Per kind, under the cap, as §2.4.

**Notation (Appendix C).** uplift fund; troop account; Ω's income by source.

**§18.1.** *Q16* (ELEF's solvency) continues with the troop surplus as income; *new Q17*: the state's income by source at each split — how much of ELEF's revenue is its own deliveries, and does the share rise over time.

---

## 6. Worked example

Twenty actors, 60/40, defaults with the cap at two thirds, $m=2$, period 3 (records determined, panels the members').

**The accounts, one tick.** Three awards: the uplift fund receives the surcharge — 3 at $m=2$; about 7 a tick averaged over run 8, where the dial sat above 2 for much of the run and every award, a troop's included, paid it — and pays it out at the batch to the reviews settling, about four by weight, as 0.75 to 1.75 per unit of weight: 1.3.0's rule, 1.3.0's money. About 1.7 troop deliveries a tick are in flight at this split under the two-thirds cap; one vests this tick: price 20 and guarantee 10 return to the troop account, against the 10 purchased and 10 locked thirteen ticks earlier — net +10 realised, about +4 in expectation over successes and failures. A troop audit seat settles: fee 3 against the 3 it cost, the bond back — **net nothing**; the surplus is the deliveries'. The troop account repays what Ω advanced for this tick's summonses, keeps $R_T$ — the two-period peak of capital held, about 1.7 deliveries a tick for thirteen ticks at 20 plus the review seats in flight, **about 450** — and pays the rest to Ω: about 6 a tick in steady state, nothing while the account is refilling after a new peak.

**Ω's tick.** In: 2 of base fee, about 6 of troop surplus once the account stands at its reserve. Order: the plant reserve, about 100, is held back (standing plant capital at a plant's life; it was about 360 under the literal horizon and left nothing to advance); liabilities older than a period — none, by period 3; advances for the tick's inspection seats and deliveries; younger liabilities — the run-8 two-thirds cell owed about 4 a tick at this split; Ω pays them as they age. Against that, the plants: at $m$ above 2 they cost Ω about 4 a tick net, and in run 8 — the surplus still the reviewers' — 272 of them went unfunded here. **Whether Ω now funds every plant is the run's first number**; the arithmetic of Hypothesis 1 says it is close, and ω₀ = 10% is the lever if it is short. On-time share: about 0.90.

**The inspectors.** Six of the eight members may be on duty; four or five are, carrying the pinned audits; three or four are free and deliver two tasks a tick; the state delivers the third. A careful member's income this period: fees and uplift up against revision 6, awards down, the total within a few percent — and its uplift is now the surcharge only, so its wealth at tick 1,000 is some hundreds below run 8's and thousands above a stamper's.

**At 50/50.** Ten members, cap seven, three free; the state delivers more than run 8's 0.7 a tick under the half cap, troop surplus about 3 to 4 a tick; liability accrual and the plant bill under the two-thirds cap unknown — if together they are within Ω's 5 to 6 a tick, Ω carries them and Hypothesis 2 resolves; if not, the line is busy and 1.8.0 says so to the customer.

---

## 7. Implementation note (no code here)

- **Two wallets, one flag**: `TROOP_ACCT` beside `DUTY_FUND`; troop ids alias to the troop account; `_fund_can_carry`, `_repay_advance`, `_summon_*`, I23's lock reconciliation and the troops' capital move to it; the surcharge stays in `DUTY_FUND`; the batch pays uplift from the duty fund's whole unlocked balance and pays the troop account's unlocked balance above $R_T$ to Ω after the advance is repaid. `Params.troop_account=True`; off, the 1.6.0 merged fund. `--rules 1.6.0` sets it off and the cap to half; `--duty-cap` stays its own knob, so §8.1's three cells are the flag alone, the cap alone, both.
- **$R_T$ as capital held**: the 1.5.0 refused-demand component dropped from the troop account's reserve; the two-period peak of `_troop_capital_now`. "Unlocked above $R_T$" computed as the engine computes the uplift's room today — the account's unlocked balance less $R_T$, where $R_T$ already counts the locks held — so under stress the account keeps more than $R_T$ in total and nothing flows until it has refilled; that is 1.5.0's arithmetic unchanged, and it is why Ω's income is the base fee alone during a ramp.
- **Ω's period record**: two income counters (base fee, troop surplus received); the flows of Ω's own money (advances made, repaid); the outflows (rebates paid, liabilities serviced, plant spend) — in one place, so Q16 and Q17 read from it; `Public.service()` and the driver's columns carry them.
- **Ω's order**: unchanged; the plant reserve horizon is `W + T_review` (15) — the engine's current default — with the period horizon kept as `--plant-reserve period`.
- **The cap**: `_member_cap` fraction default ⅔, floored at $V_{\max}+1$ as now; `--duty-cap half` as the 1.6.0 control.
- **The clock's third stop, I9 per kind**: the engine's current behaviour; consolidating them changes no code.
- **Tests**: `test_v17.py` — the two wallets' flows and conservation (I1 across both, every outflow in I23's list including a forfeited guarantee and a burned bond); no uplift from troop earnings; surplus above $R_T$ to Ω and nothing below; $R_T$ as capital held (a refusal does not raise it); Ω's counters; the cap at ⅔ with the floors; the §6 figures. Goldens re-pinned once (uplift and Ω's balance change in the equivalence scenario).
- **Drivers**: `--omega-rate {0.05,0.10,0.15}` with `--r-s 1` pinned for the sweep (the control cell declared); the income and outflow columns; `--rules 1.6.0`; the rest as 1.6.0.

---

## 8. After acceptance — the runs

Every comparison against run 8 is read from the second period on.

1. **One factor at a time** at 60/40 against 1.6.0 (`--rules 1.6.0`: merged fund, half cap): the accounts alone; the cap alone; both — **plants unfunded first**, then Ω's liability, Ω's minimum balance, on-time share, careful wealth, the state's share.
2. **Reproduce §6.**
3. **Tipping** at 50–80% against run 8's two-thirds cells: Hypotheses 1–4; Ω's income by source (Q17); plants unfunded (the sharp edge); the stamper − careful gap.
4. **The take**: ω₀ ∈ {5%, 10%, 15%} with $r_s$ pinned at 1, at 50/50 and 60/40 (Hypothesis 6) — Ω's liability and minimum balance, plants unfunded; whether the clock is carried on fees alone; members' income by source for the surcharge's rise.
5. **Adaptive**: Hypothesis 5 — the liability stock to zero, and when.
6. **Drift** $m_{\max}\in\{2,4\}$: honesty unchanged; Ω solvent.
7. **Red team**: the late withdrawer once more (the cannot-serve evidence, re-measured under solvency); a requester flood against Ω's income by source (does the state's take grow with volume it cannot serve?); the decliner, the reformer, camouflage.

---

## 9. Provenance

**[S8] Run 8 (October 17–18, 2026)** — `agentic_sim/results/studies/1.6.0-autoscale/`, 840 runs, engine `195896a`. **[I15]** The implementer's run-8 notes: the OFAT table; the inverted Hypothesis 2; the liability living in the stale unawarded request; the cap table; the three Appendix K readings (the plant reserve's horizon ruled here as a plant's life; the clock's third stop; I9 per kind); the four items for decision. **[C-rev7] Design discussion (October 18, 2026).** The design reviewer proposed the fund paying rebates before uplift, the cap at two thirds, the ω₀ sweep, and a cannot-serve protocol held. Baruchi: "why should an inspector profit from something a troop did? from their perspective it's just like any other actor in the system, no?" — adopted as §2.1 in place of the reviewer's proposal; the cap understood as a staffing fraction of the unsuspended list ("the plants decide who stays on the list; the cap decides how many of whoever is on the list may inspect at once") and agreed; the sweep agreed; the protocol understood — "be honest with the status vs the customer: 'the current line is busy, do you want to hold T time?'" — and held for 1.8.0 pending Hypothesis 2. **[I16] Implementation review of rc.1 (October 18, 2026)** — five points, all adopted: the ω₀ sweep moved the rebate with the take ($r_s$ pinned at 1 for the sweep; the surcharge follows ω₀); the two-thirds cap triples plants unfunded at 60/40 in run 8's cap table — a figure the run-8 notes had not reported — so Hypothesis 1 carries the arithmetic (7,800 against 6,200) and the plants as its sharp edge; $R_T$ was not 270 and its job had changed (redefined as the two-period peak of capital held, the refused component withdrawn, its purpose — the troops' in-flight capacity shielded from the liability queue — stated, the pass-through recorded and rejected); a troop review seat earns nothing (the surplus is the deliveries'); the surcharge was about 7 a tick, not 3, so uplift falls by two fifths. Smaller — repayments are flows not income, with Ω's outflows in the same record; the floor's bind on "a third free"; I23's forfeit and burn outflows; I24 never carried the struck clause; `--omega-rate`; the 1.6.1 items change no code — adopted.

---

## Closing statement

> Revision 6 gave the customer a clock and the state an army, and run 8 showed the army's profits paid the inspectors' bonuses while the army's bills bankrupted the treasury. The fix is the one Baruchi named: a troop is an actor of the state, and what it earns is the state's — no more and no less than any actor keeps what it earns. The inspectors keep what they were promised, the dial's tax. The state pays its debts from its own work. And if, at the worst splits, its own work is still not enough, the next thing it owes the customer is the truth about the line.

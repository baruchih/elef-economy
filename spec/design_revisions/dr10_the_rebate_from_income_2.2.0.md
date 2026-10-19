# Agentic Economics — The Task, Verification, and Dispute Loop

## Design revision 10 — specification 2.2.0-rc.2: the rebate from income

**Project:** ELEF / Agentic Economics  
**Version:** 2.2.0-rc.2 — a release candidate, not yet in force. rc.1 (October 19) was the sketch as first sent; rc.2 settles the implementation review [I23]: the one correction (the pool takes **fee income** — I32 had said every inflow, which would have locked the state's working capital), and five readings taken into the text. On acceptance it becomes **2.2.0**, consolidated into one standalone text, and 2.1.0 moves to history. The supply side — entry and delegation — moves to **2.3.0**.  
**Prepared:** October 19, 2026 (rc.1–rc.2)  
**Supersedes:** 2.1.0 where this document speaks — one rule, the rebate's settlement; everywhere else 2.1.0 stands unchanged: the bank, the state's expected cost, the loans, the debt, the wall, the index per period, every refusal told, and all of 2.0.0 and 1.x beneath them.  
**Nature of this revision:** A **design revision** (minor, by §19), small. The service clock's rebate — 1.6.0's "the orchestrator takes some of the blame in money" — was sized when the state could print to pay it: a credit a tick late, capped at the price, on every late request. 2.1.0 took the press away, and run 14 showed what the promise then is: in a flood the state owes its customers 27,000 and earns 7,900 in the whole run; the stock ages five hundred ticks and is never paid. This revision sizes the promise to the means. **A rebate claim is unchanged as the measure of lateness; it is paid from the state's fee income of the period, pro rata, and what the income does not cover is forgone — not owed — and read.** ELEF earns less when it is late, down to nothing, and the ledger says so. Two rulings from run 14 are recorded with it: the reviewer's view stays blind to the actor (§14), and Hypothesis 5 of 2.1.0 is restated as the finding it became.  
**Design assumptions, unchanged.**  
**Status:** Proposed. Accompanied by what required it (§1) and the runs that test it (§8).

> **The state never prints for itself.** *(2.1.0)*
>
> **The state's blame is its fees.** *(new)*

---

## 1. Why: what run 14 said

1. **The liability stock was off by an order of magnitude [S14].** 2.1.0 §6 expected "a liability stock that peaks at a few thousand and ages a period or two, paid down from the flood's own fees after the debt." Under the flood of twelve the stock reached 26,839 (accrued 32,503), under the crowd of thirty 9,968 (accrued 14,190), ageing 420–520 ticks and growing at the run's end, against a whole run's fee income of 7,852 and 5,832. The state's income is a quarter of what the clock says it owes.
2. **The cause is the rebate's sizing, not the bank.** A claim of $r_s$ a tick, capped at $B$, on every late request scales with the crowd's size times its wait; the state's means scale with $N_T$, the most it can field. When the field is full the two part by construction, and no rule about money can close the gap — the bank's refusal to print for it is correct, and leaves a promise nobody keeps. Run 12's answer to the same gap was to print (the pump: $M$ 99,400, hoards 3,022 a requester), rejected in 2.1.0.
3. **The customers' real protection is elsewhere [S14].** Every refusal is told; the withdrawing requester reads the mark, withdraws and reposts, and gains nothing by it (rebates 78 against 75) — the mark does the work the rebate was meant to do, and the clock still measures the lateness. The rebate's job is the state's own punishment, in money, as 1.6.0 said: "punish the network somehow — earn less or something" [C-1.6].
4. **Two rulings, recorded.** *The state-rejecter red team* was run as a declared non-conforming reading — §14's reviewer view carries no actor — and showed what a leak would cost: $b_T$ driven to the two-thirds limit, the state 63% of the market at a loss. *Hypothesis 5's second half* (real wealth invariant under issuance) failed: 790 / 1,410 / 1,310 at issuance 5 / 10 / 20.

**Classification.** A design revision: the rebate's settlement moves from a stock the state owes to a share of what the state earns. The clock, the claim, the mark, the bank and every rule of honesty are untouched. Minor, by the rule.

**Recorded and rejected.** *Forgive after a period, oldest first* (the liability stock with a horizon): pays the first period's claimants in full and the rest nothing — the early birds win, and the stock still exists for a period. *Leave the stock as the honest bill*: an IOU nobody pays, ageing forever — the silence of run 11 in money form. *Print for it*: the pump. *The bank lends for rebates*: a rebate is not capital in flight; nothing returns. *A smaller $r_s$*: the claim is the measure of lateness and should stay honest; it is the payment that must fit the means.

---

## 2. The rules

### 2.1 The claim — unchanged, the measure of lateness

**Rule.** The service clock and the claim are as 1.6.0 §2.1 and 2.0.0 have them: a root request's clock runs from posting, stops at the first verdict (or the final, or vesting without a verdict), is stopped while the request is below market; a request late past $T_s$ accrues a **rebate claim** of $r_s$ a tick, indexed, capped at the request's price $B$; a request withdrawn before its award is owed nothing. **The claim is recorded at the stop**, on the request, and is the lateness reading of the network rating as before: on-time share, lateness, claims accrued.

### 2.2 Settlement — from the period's income, pro rata, the rest forgone

**Rule — the pool.** Ω's **fee income** — the base fee $\omega_0 B$ at an award or a summons, the troops' review fees at settlement, and a court fee a troop wins (income of the same kind: the troop's bond is the state's) — accrues during a period, **after the debt** (2.1.0 §2.4: every inflow repays the debt first), to the **period's pool**. **Fee income only.** The returns of capital — a troop delivery's price and released guarantee at vesting, a seat's reimbursed cost and released bond at settlement — repay their own loans and land in Ω's balance as 2.1.0 §2.4 has it, not in the pool: they are the state's working capital, and pooling them would make every summons the bank's from the second period on. Nor does a delivery's surplus $b_T(\bar B+G)$ go to the pool: it is the expected-cost margin that nets to zero against the failures over a period (2.1.0 §2.2), the failures' cover, and the customers are not paid out of it. The pool is **a lock on Ω's balance**, raised as each fee arrives after the debt and released at the close, so Ω's *unlocked* balance excludes it: summonses are funded from Ω's unlocked balance — retained from earlier periods, and the capital that came back — then by the bank's loans as 2.1.0 has it; the pool is touched by nothing during the period.

**Rule — the close.** At the period boundary — when the bank publishes the index, inside the tick before the summons pass — **the claims recorded at stops inside the period are paid from the pool, pro rata**: each claim times $\min(1,\ \text{pool}/\text{claims})$, paid to its requester as the rebate. A claim recorded earlier in the closing tick belongs to the closing period; one recorded later in it to the next. **What the pool does not cover is forgone**: not owed, not carried, not created — recorded on the request (claimed, paid, forgone) and in the period's readings. What the claims do not take is released to Ω's unlocked balance: ELEF's retained income for the period. A request whose clock is still running at the close is settled at the close of the period in which it stops.

**Rule — nothing else.** No liability stock; no order of liabilities; no payment at the stop. The 2.1.0 order of Ω's income becomes **debt → the period's pool → (at the close) claims pro rata → Ω's balance**.

**Consequence — ELEF earns less, down to nothing.** In a quiet market claims are a few credits a period against fees of several hundred: paid in full, the rest retained, nothing changes. Under a crowd, the pool is a fifth or a sixth of the claims: every late requester gets that fraction of its claim, the state retains nothing for the period, and the rest of the clock's bill is forgone — in public, on every request. The state is punished by exactly what it earned while it was failing its customers, and the customers are told how much of the bill went unpaid. Nothing is printed, nothing is owed into the next period, and the stock of run 14 does not exist.

**Consequence — the order matters.** Debt before the pool: a state that is losing on its deliveries repays the bank before it refunds its customers, so the customers of a state at the wall get less — read in §8 as the forgone share under the at-cost control and the three-quarters failure. That is the design: the bank's money comes back before the state's blame is paid, because the bank's money is everyone's.

### 2.3 What is read

Per period and per run: **claims, paid, forgone**, and the **forgone share** (forgone / claims) — the unpaid part of the state's blame, the busy line's third reading beside the marks and the lateness; **Ω retained** per period, zero in a flood by construction. The network rating is the on-time share and lateness as before, with the forgone share beside them.

### 2.4 Rulings carried (no rule moves)

**The reviewer's view stays blind to the actor (§14).** A reviewer judges work, not workers. Run 14's state-rejecter cell — a reviewer that could tell the state's work and rejected it — drives $b_T$ to the two-thirds limit and makes the state most of the market at a loss; it is recorded as the price of a leak and struck from the red team as impossible by construction. Whether a reviewer should know it is inspecting a plant is the same question with the same answer.

**Hypothesis 5 of 2.1.0, restated as the finding.** Where the ratchet binds, the price is issuance over the strategy's quantity (23 against 22.7 at the middle); printing is neutral *in work* — quantity and honesty unmoved — and **not in distribution**: below the ratchet's threshold the members work at cost and the customers keep the surplus (the first deflation: 9.5 at issuance 5); at it the members take a margin; far above it the customers hoard what $K_{\text{open}}$ will not let them post. Issuance is still not a dial — the lever is the quantity, which is entry's (2.3.0) — and it is not neutral either.

### 2.5 Defaults

| Default | Value | Note |
|---|---|---|
| The claim | $r_s=1$ a tick late past $T_s=8$, indexed, capped at $B$; recorded at the stop; withdrawn before award owed nothing | unchanged — the measure |
| The pool | Ω's fee income of the period (base fees, troops' review fees) after debt; untouched until the close | the means |
| Settlement | at the period's close: claims stopped in the period paid pro rata from the pool; the rest forgone and read; the remainder to Ω's balance | nothing owed across a close |
| Order of Ω's income | debt → pool → (close) claims → Ω's balance | the liability stock retired |
| Readings | claims, paid, forgone, forgone share, Ω retained — per period | the busy line's third reading |
| Everything else | as 2.1.0 | |

---

## 3. Consequences and hypotheses

**Hypothesis 1 — the stock is gone and the bill is read.** Under the flood and the crowd (run 14's cells): liabilities zero at every close; the forgone share about five sixths in the flood (claims ≈ 5,400 a period against a pool ≈ 900) and about four fifths under the crowd for its two periods, zero after; Ω retained zero in every flooded period and positive again within one of the crowd's end. $M$, hoards, on time, lateness, refusals, loans and debt within seed variance of run 14.

**Hypothesis 2 — the quiet market does not notice, less one period's fees.** At 50–80% (wallet rule, $K_{\text{open}}$ 5) claims are paid in full every period; forgone zero. Because a period's fees (about 465 at 60/40) are locked until the close and the first period starts from Ω's float of 300, the quiet cells show loans in the first period or two and Ω retained lower than run 14's 4,300–4,500 by about one period's fees; every other reading — the price, the state's share, honesty, wealth — is identical to run 14 on the same seeds.

**Hypothesis 3 — the order shows.** Under the at-cost control and the three-quarters failure (2.1.0 §8.9), where the debt takes the income first, the forgone share is higher than in the honest cells at the same lateness — the customers of a losing state are refunded less — and the wall's retraction is unchanged.

**Hypothesis 4 — no one games the pool.** A requester that posts many small requests to collect pro-rata rebates gains nothing beyond its claims (each capped at $B$, each a share of the same pool); the withdrawing requester's rebates are as run 14's (78 against 75). Honesty is unmoved.

---

## 4. What does not change

The clock, the claim, the mark and the withdrawal; the bank's three jobs, the loans, the debt and the wall; the state's expected cost and its price at $\bar B$; the index per period; $N_T$, the crowd, the below-market flag; everything in 1.x about honesty. What changes is how a rebate is paid and what happens when it cannot be.

---

## 5. Invariants, notation (amendments)

**I32 (new) — the pool.** Every **fee** inflow to Ω after the debt — base fees, the troops' review fees, court fees a troop wins — accrues to the current period's pool, a lock on Ω's balance; the returns of capital and a delivery's surplus do not; the pool is untouched until the period's close; at the close, paid $=\min(\text{claims},\text{pool})$ distributed pro rata over the claims stopped in the period, forgone $=\text{claims}-\text{paid}$, and the remainder of the pool is released to Ω's unlocked balance; nothing is created for a rebate and nothing is owed across a close.
**I30 (amended).** "While debt $>0$ or liabilities $>0$" becomes **while debt $>0$**: Ω's unlocked balance is zero at the start of the summons pass and at the tick's end; the pool, being locked, is not Ω's unlocked balance, and I15 reconciles the lock.
**I10 (note).** A rebate settled at the period's close may reach a request that vested earlier in the period; admitted by its note, `rebate (settled at the period's close)`, as the serviced liability was.
**I28** stands (nothing created for a rebate). **Retired:** liabilities as a stock and their age; the order "debt → liabilities oldest first → Ω".

**Conformance, found on the way (no rule moves).** §4.5 lists $r_s$ among the indexed amounts; the engine indexed the default ($r_s=0$, meaning $\omega_0B$) but not a stated $r_s$. No run was affected — every driver used the default; corrected under §19 with a regression test in `test_v22`.

**Notation (Appendix C).** *Claim*; *pool*; *forgone*; *forgone share*; *Ω retained*. Retired: *liabilities* (2.1.0), *liability stock* (1.6.0).

**§18.1.** *Q15* restated: claims, paid, forgone, the forgone share under riots. *Q19*: the busy line's three readings — marks, lateness, the forgone share. *Q14*: the reviewer's view stays blind; the state-rejecter cell recorded as the price of a leak.

---

## 6. Worked example

**A quiet period at 60/40** (run 14's cell). The period's fees: base ≈ 275, the troops' review fees ≈ 190 — a pool of 465 after a debt of 0, locked on Ω as it arrives; the troop deliveries' prices and guarantees coming back during the period land unlocked and fund the next summonses, as before. Eight requests stopped late inside the period, claims 1–4 each, 9 in all. At the close each is paid in full; 456 is released to Ω's unlocked balance; forgone 0. Nothing a requester or a member can see has changed from 2.1.0, except that the rebate came at the close rather than at the stop — and that in the first period, with only the float of 300 unlocked, a few summonses are the bank's loans until the first close.

**The flood of twelve, $N_T=40$** (run 14: claims accrued 32,503 over six flooded periods). In a flooded period some 300 requests stop late with claims near the cap — about 5,400; the state's fees for the period are about 900 (more awards than in a quiet period), its debt repayments about 50; the pool is 850. At the close each late requester receives $850/5{,}400\approx16\%$ of its claim; 4,550 is forgone, recorded on each request and in the period's readings as a forgone share of 0.84; Ω retains 0. Over the flood's six periods the customers are paid about 5,100 of the 32,500 the clock says they were owed, and the ledger shows the other 27,400 as forgone, period by period. Nothing is printed; no stock exists at any close; the state earned nothing while it was failing its customers, and said so.

**The crowd of thirty, 100 ticks** (run 14: claims accrued 14,190). Two periods of claims near 7,000 each against pools near 1,200: the forgone share about 0.83 while the crowd is in; the period after, claims fall to a few hundred as the queue drains and are paid in full; Ω retains again from the second period after the crowd leaves.

**A state at the wall** (the three-quarters failure; run 14: debt repaid 6,831 a run, liabilities 8,878). The debt takes about 680 of a period's fees of about 900; the pool is 220 against claims near 900 — a forgone share of 0.75 at a lateness where the honest flood's would be lower. The customers of a losing state get less back: the bank's money first.

---

## 7. Implementation note (no code here)

- **One flag.** `Params.rebate_pool` (on, with `bank`); off is 2.1.0 for the goldens; `test_v21`'s rebate tests pin `rebate_pool=False` as `test_v20` pins `bank=False`.
- **The pool is a lock on Ω, not a wallet.** Fees land in Ω's wallet by transfer; `omega_pool` is a lock record on Ω (`pool:<period>`) raised in the inflow hook from **fee events** after the debt — never from the returns of capital or a delivery's surplus — so Ω's unlocked balance excludes it, the summons and `_fund_can_carry` read the unlocked balance alone, I15 reconciles the record, and I30 holds without a special case. `period["claims"]` holds the period's stopped claims by request. The close runs in `_maybe_end_period` beside the index, at step 5 before the summons pass: paid $=\min(\text{claims},\text{pool})$ pro rata, `rebate_claimed` / `rebate_paid` / `rebate_forgone` on each request, the remainder released to Ω.
- **The claim.** `_stop_clock` records `rebate_claimed` on the request (the 1.6.0 arithmetic, with $r_s$ now indexed when stated — the conformance correction of §5) and pays nothing; `omega_liabilities` and `_service_omega_liabilities` retire behind the flag; I10's exempt note for the rebate at the close.
- **Readings.** The period record's `claims`, `paid`, `forgone`, `forgone_share`, `omega_retained_period`; `view.service()` with the forgone share; the driver's columns; `--small-requests` for the red team.
- **Tests.** `test_v22`: I32 at every close; a claim paid only at the close and only from the pool; the pool raised by fee events only; pro rata exact to the rounding; forgone recorded and never carried; nothing created; Ω's unlocked balance excludes the pool during the period; $r_s$ indexed when stated; the §6 quiet period and flood period reproduced in the six-actor world. Goldens re-pinned once. No reviewer test touches the rebate's timing; `EXPECTED_FAIL` unchanged (28).

---

## 8. After acceptance — the runs

Every comparison in real terms, from the second period on, against run 14's cells on the identical seeds.

1. **Reproduce §6.**
2. **The riots**: the crowd of thirty and the flood of twelve at $N_T=40$ — claims / paid / forgone by period, Ω retained, liabilities (zero), $M$, hoards, on time, lateness (Hypothesis 1).
3. **The quiet market** at 50–80%, wallet rule, $K_{\text{open}}$ 5 — paid in full, everything else identical (Hypothesis 2).
4. **The order**: the at-cost control and the three-quarters failure with the wall at one period — the forgone share against the honest flood at the same lateness (Hypothesis 3).
5. **Red team**: the small-request requester; the withdrawing requester (Hypothesis 4).
6. **Told, read whole**: 60/40 with $K_{\text{open}}$ lifted under both ceiling policies — the busy line's three readings together.

---

## 9. Provenance

**[S14] Run 14** (October 19, 2026) — the bank's books read and the state neutral; the liability stock 10,000–27,000 ageing 400–500 ticks against a whole run's fees of 5,800–7,900; the three candidates the implementer set out (cap the stock, price the rebate from income, leave it as the reading); the state-rejecter cell as a declared non-conforming reading; Hypothesis 5's second half failed. **[C-1.6] Baruchi, on 1.6.0 (October 17, 2026):** "re-queue them with priority and have the orchestrator take some of the blame in a monetary form"; "such a case should also punish the network somehow — earn less or something. this might incentivize doing things faster." **[C-2.2] Design discussion (October 19, 2026):** the design reviewer's recommendation — the rebate is the state's fees returned to the late, settled once a period pro rata, the rest forgone and read; a small 2.2.0, supply to 2.3.0 — and Baruchi: "ok, let's draft it." **[I23] Implementation review of rc.1 (October 19, 2026)** — implementable, with one correction and five readings. The correction, adopted: I32 said "every inflow" where §2.2 said "fee income"; pooling the returns of capital would lock the state's working capital and make every summons the bank's from the second period on — the pool is fee income after the debt (base fees, the troops' review fees, court fees a troop wins), not the returns of capital and not the delivery's surplus, which is the failures' cover. The readings, taken as written: the pool as a lock on Ω (I15 reconciles it; I30 without a special case); Hypothesis 2 restated — loans in the first period or two and Ω retained lower by one period's fees, everything else identical; $r_s$ indexed when stated (a conformance gap found on the way, corrected under §19 with a regression test, no run affected); the close inside the tick at step 5, claims assigned by the tick's granularity; I10's exempt note and `test_v21` pinning `rebate_pool=False`, the expected failures unchanged at 28.

---

## Closing statement

> The clock still says how late the state was, to the tick. What changed is what the state can do about it: not print, not promise, but hand back what it earned while its customers waited — all of it, if that is what it takes — and write down the rest as unpaid. A customer told the field is full, and told how much of the bill went unpaid, has been told everything the state knows. That is the busy line, complete. The supply side is next.

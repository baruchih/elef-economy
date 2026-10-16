# Agentic Economics — The Task, Verification, and Dispute Loop

## Working specification v0.5

**Project:** Agentic-OS / Agentic Economics  
**Prepared:** October 15, 2026  
**Supersedes:** v0.4 (October 15, 2026). Where this document is silent, v0.4, then v0.3, v0.2, v0.1 stand.  
**Nature of this revision:** A conformance pass. The third external review [R3] ran the v0.4 reference implementation against twenty independent regressions and found that several exceptional paths departed from the selected rules, that three rules were not yet decided, and that several specified mechanisms were bracketed rather than implemented. This revision decides the three rules, repairs the paths, implements the bracketed mechanisms, and strengthens the invariants so that their names say what they check. No economic mechanism is added.  
**Status:** Agreed rules, consequences, provisional defaults, and an initialization, all exercised by code: the original examples, the reviewer's regressions, and the new rules in explicit form. The appropriate claim remains the reviewer's: *scripted examples execute, and independent executable checks were answered* — not that incentives have been shown to work. What the simulation must still find is §18.2.

> **The wallet supports the purpose; it does not define the purpose.**
>
> **The actor competes on its promise, is assessed on its delivery, and bears the cost of its execution.**
>
> **The past is append-only. The present is committed. The future is mutable.**
>
> **Money enters with requests. Truth enters with requesters. Verification is the security work of the economy.**
>
> **The human is the battery — and holds the plug.**

### What changed from v0.4

| Finding [R3] | v0.5 resolution |
|---|---|
| A. Negative and non-finite amounts were accepted; a failed award or filing left partial effects | Every amount is validated at the boundary; an action either completes or changes nothing (§2.2, §5, §8) |
| B. A reviewer could hold two unfinished reviews | One active assignment per actor, enforced; a P or ⊥ keeps the reviewer attached until the actor acts (§2.2, §6) |
| C. Timed-out appeal and audit positions could not be replaced | A withdrawn review vacates its slot in the challenge or the audit; a replacement audit stays admissible after the window if the original was timely (§7.5, §12) |
| D. Review cost was recorded in real units and compared to a cap in credits | Cost is recorded as the credits the purchase burned (§7.3) |
| D. A completed subcontract's price was not in the kill-fee cost basis | It is, as §4.6 already said: execution cost includes nested payments (§9.3) |
| E. A nested rejection bond locked at posting was not reconciled at award | **Rule:** a case is denominated at its *first lock* — root at award, nested at posting; nothing to reconcile (§4.5) |
| F. Ω claims were recorded but never paid; an overturned reviewer's deferred cost vanished; a no-review settlement swept the deposit to Ω | Ω services claims FIFO on every inflow; the cost obligation survives an overturn; a settlement with no entitled reviewer returns the deposit (§4.3) |
| G. Overrides did not reconcile reviewers; a nested override changed the grade | Before vesting an override is a ruling and contradicting reviews are overturned; after vesting contradicted reviewers take the reliability hit; nested grades stay procedural (§15.2) |
| H. A second P was accepted; $T_{\mathrm{rev}}$ and $T_{\mathrm{evid}}$ were unused | Revision and evidence are two steps — choose within $T_{\mathrm{resp}}$, resubmit within $T_{\mathrm{rev}}$ or $T_{\mathrm{evid}}$ — and the resumed review returns F or N only (§6) |
| H. An appeal of ⊥ could not express "the evidence really was missing" | **Rule:** an appeal of ⊥ answers two questions, the objection's disposition and the fulfillment verdict, both stated explicitly (§8.1) |
| I. Pool-exhaustion withdrawal orphaned sibling requests | One terminal-cleanup routine on every exit, cancellation included (§9.4) |
| J. Rotation, default reserve, trailing windows, audit blindness, committed history were bracketed | Implemented (§13, §19, §11, §14); what remains bracketed is listed in §22 |
| Invariants were weaker than their names | I1 reconstructs $M$ from the event log; I3 validates amounts; I14 checks occupancy; I15 reconciles every lock to a named obligation; I13 checks grade provenance; I16 verifies the chain (§17) |

### Reading the status labels

As in v0.4, plus **[I2]** for choices the v0.5 implementation forced.

## Contents

1. Purpose and measurement boundary (unchanged)
2. Participants, time, and the order within a tick
3. Request fulfillment and evidence (unchanged)
4. Money: where it enters, where it goes
5. Offers, selection, and guarantees
6. Task lifecycle: committed, pending, vested
7. Verification: eligibility, bond, compensation, deadline
8. Challenges: appeal, requester dispute, and audit
9. Delegation: nested requests
10. Wallet accounting and settlement
11. Reliability and duty credit
12. Protected verification capacity
13. Rotation of verification duty
14. Verifiable history and trust boundary
15. The human in the loop
16. Worked example
17. Rule and invariant checklist
18. Provisional defaults, hypotheses, and remaining opens
19. Initialization
20. Deferred ideas and superseded alternatives
21. Sources and decision provenance
22. Reference implementation  
Appendix A. Learning (unchanged)

---

## 2. Participants, time, and the order within a tick

### 2.2 One active assignment, and atomic actions

**Agreed (made enforceable).** An actor holds at most one active assignment: an ordinary commitment, or an open review — never both, never two reviews. A review that returns $\mathsf P$ or $\bot$ is not finished from the reviewer's side: the reviewer stays attached to the case until the actor resubmits (and the same reviewer resumes), appeals, or accepts. A review that returns $\mathsf F$ or $\mathsf N$ releases the reviewer at once; its bond and liability persist (R23). [R3-B]

**Agreed (new).** An action either completes under its rules or changes nothing. Every amount crossing the boundary — price, cost, duration, balance — is validated as a finite, non-negative number; an award checks that every leg is fundable before it locks or moves anything; a challenge collects its court fee before it marks the round used. Recording the attempt is permitted; partial execution is not. [R3-A]

Tick order as in v0.4 §2.2, with Ω claim servicing at step 4 and rotation at step 5 now implemented.

---

## 4. Money: where it enters, where it goes

### 4.3 The deposit, the single payout rule, and Ω's obligations (completed)

The single payout rule of v0.4 stands. Three obligations it left implicit are now rules:

- **Ω services its claims.** Whenever Ω receives anything — a service fee, a court fee, a repayment — it pays its outstanding reviewer claims first in, first out, partially if it must. A claim is not a record; it is a debt that the next receipt pays. [R3-F]
- **A cost obligation survives an overturn.** An overturned reviewer forfeits its bond and earns no fee. Its capped, eligible, unpaid reimbursement is still owed: it is paid from the case pool at settlement with the other deferred reimbursements, and what the pool cannot cover becomes a claim on Ω. The bond was the penalty; the cost was not. [R3-F]
- **Unused deposit.** A settlement with no entitled reviewer — no surviving review of any kind — returns the deposit remainder to the requester. The "pool sweep" removes rounding residue of minted emission only; it never touches deposit. [R3-F]

### 4.5 Valuation time: a case is denominated at its first lock

**Agreed (revised from v0.4).** A case's nominals — $D$, $K$, $G^V$, $\varphi$, and the bonds of every review assigned to it — are indexed once, at the case's **first lock**, and frozen. For a root case that is its award. For a nested case it is its **posting**, when the requester-actor locks $\beta'+G^V$: the rejection bond, the court fee $B$ would pay, and the cap are then one index, and the award that follows re-indexes nothing. The actor's guarantee $G=\lceil 0.5B\rceil$ is fixed at award. The reconciliation step the review asked for does not arise. [R3-E]

### 4.6 Execution cost (clarified)

$C_{iq}$ is measured in credits and includes the credits burned by resource purchases, the delivery prices paid on nested requests the actor posted, and kill fees it paid. A review's cost is likewise the credits its purchases burned, not the real units, so that the cap $K$ compares like with like under a moving $v_t$. [R3-D]

---

## 5. Offers, selection, and guarantees (unchanged in substance)

$\tau$ is a positive integer number of ticks; $B\le\beta$; a bid that cannot be funded on every leg is refused without effect (§2.2).

---

## 6. Task lifecycle: committed, pending, vested

### 6.1 Responses are one choice and, sometimes, one resubmission

**Agreed (revised).** Within $T_{\mathrm{resp}}$ of a $\mathsf P$ or $\bot$ the actor **chooses**: for $\mathsf P$, to revise or to accept $\mathsf N$; for $\bot$, to supply the evidence, to appeal, or to accept $\mathsf N$. Choosing to revise or to supply evidence opens a **resubmission window** — $T_{\mathrm{rev}}$ or $T_{\mathrm{evid}}$ — within which the actor resubmits. The same reviewer resumes; its review clock, paused while the actor acted, resumes; the resumed review is the same assignment under the same reimbursement cap and returns **$\mathsf F$ or $\mathsf N$ only**. A missed resubmission window is final $\mathsf N$. One revision per case. [R3-H]

| State | Entered by | Leaves by |
|---|---|---|
| Awaiting response | a $\mathsf N$, $\mathsf P$ or $\bot$ verdict | accept / appeal / revise / supply evidence, or $T_{\mathrm{resp}}$ |
| Resubmitting | choosing revise or supply evidence | resubmit, or $T_{\mathrm{rev}}$ / $T_{\mathrm{evid}}$ → final $\mathsf N$ |
| Submitted (resumed) | resubmit | the same reviewer's $\mathsf F$ or $\mathsf N$ |

Everything else in v0.4 §6 stands: suspension while a challenge or audit is open, vesting at $\max(t_0+W,t_{\mathrm{resolve}})$, financial finality at vesting, inclusive deadlines, final-$\mathsf N$ reviews settling in the tick's batch.

---

## 7. Verification: eligibility, bond, compensation, deadline

### 7.1 Eligibility (completed)

On duty; not excluded from the case; able to fund the case's frozen bond; **holding no active assignment** (§2.2).

### 7.3 Compensation (clarified)

Reimbursement is $\min(\text{credits spent},K)$, paid from the root's deposit at completion, else advanced by Ω, else deferred; the fee is the haircut entitlement at settlement (v0.4 §4.3). A resumed review's reimbursement is incremental: the cap applies to the assignment, not to each sitting.

### 7.5 Deadlines, withdrawal, and replacement (revised)

**Agreed.** A review not completed by its deadline (plus any paused ticks) is **withdrawn**: half the bond burns, half is released, no reimbursement, reliability down, the reviewer excluded from the case, and its position vacated. A vacated position is refilled by the ordinary assignment rule for whatever it was: an initial review, an appeal review (the challenge's slot reopens), or an audit (the audit slot reopens and its suspension lifts). A replacement audit is admissible after the window closes when the withdrawn one was assigned inside it. [R3-C]

**[I2]** An open review on a case that a human override settles is **voided**, not withdrawn: the bond is released whole and no reliability hit is recorded, because the reviewer did nothing wrong.

---

## 8. Challenges: appeal, requester dispute, and audit

### 8.1 Appeal — including the appeal of a ⊥

**Agreed (new rule).** An appeal of a $\bot$ ("I could not assess this; the evidence I need is missing") is an appeal of a *claim about the submission*, not a request to re-grade the task. The two fresh reviewers therefore answer **two questions**, both stated explicitly:

1. **Objection** — *was the first reviewer right that the evidence was missing?* `upheld` (it was missing) or `rejected` (it was present).
2. **Fulfillment** — $\mathsf F$ or $\mathsf N$. An `upheld` objection entails $\mathsf N$, since what cannot be assessed cannot be fulfilled.

Settlement:

| Both say | Original $\bot$ | Court fee | Outcome |
|---|---|---|---|
| rejected, same verdict | overturned: bond forfeited, fee reimbursed from it, reliability down | reimbursed to the actor | their verdict |
| rejected, different verdicts | overturned | reimbursed | orchestrator rules on fulfillment |
| upheld | stands: bond released at settlement, fee vests | borne by the actor | $\mathsf N$ — an unverifiable submission is the actor's failure (§3.2) |
| split on the objection | — | — | orchestrator rules on **both** questions |

An appeal reviewer is overruled, and forfeits its bond, if its objection disposition differs from the settled one, or — when the objection is rejected — if its verdict differs from the settled outcome. The orchestrator's ruling on a $\bot$ case states both answers. Nothing infers one answer from the other: a reviewer who returns $\mathsf N$ without a disposition has not answered the appeal, and the engine refuses the completion. [R3-H]

Appeals of $\mathsf N$, requester disputes, audits, the merged audit-and-dispute rule, and the court fee's path (to Ω at filing, reimbursed from the liable bond) are as in v0.4 §8.

---

## 9. Delegation: nested requests

### 9.2 Denomination (see §4.5)

Posting locks $\beta'+G^V$ at the posting index and freezes the nested case's nominals there. The rejection bond is released on acceptance and is the requester-actor's reviewer bond on rejection, as in v0.4.

### 9.3 Cancellation — the cost basis (clarified)

The kill fee is $\min(C_{B},K)$ where $C_B$ is the subcontractor's execution cost on the nested case as §4.6 defines it: credits burned on resources, **plus the delivery prices it has paid on its own completed subcontracts**, plus kill fees it has paid. Cancellation is available after award and before the subcontractor submits; the fee comes from the nested escrow first, then the requester-actor's unlocked balance, and is refused if unfundable. [R3-D]

### 9.4 Every exit cleans up (completed)

Final $\mathsf N$ for any reason, pool-exhaustion withdrawal, and cancellation all withdraw the exiting case's unawarded nested requests and release the locks behind them. Awarded ones continue. [R3-I]

---

## 10. Wallet accounting and settlement (unchanged in form)

Lock records: every locked credit is attributable to a named obligation — a guarantee $G{:}q$, a bond $\text{bond}{:}v$, a nested price ceiling $\beta{:}q'$, a rejection bond $\text{rej}{:}q'$ — and a wallet's $L$ is the sum of its records. This is what I15 reconciles.

---

## 11. Reliability and duty credit (windows implemented)

$\rho_i$ is computed over the trailing 100 settled outcomes; $\kappa_i$ counts reviews vested in the trailing 100 ticks. A contradicted reviewer after a post-vesting override records a failed outcome without any money moving (§15.2).

---

## 12. Protected verification capacity (clarified)

$V_{\max}$ bounds **positions** per challenge path; a withdrawn position is vacated and refilled (§7.5). Two counts are kept beside membership: *occupancy* (eligible duty actors are busy) and *solvency shortfall* (fewer than $V_{\max}$ duty actors can fund the bond). Reserve membership never falls below $X$ during a handover because the handover is one atomic swap (§13).

---

## 13. Rotation of verification duty (implemented)

**Agreed (as implemented).** At step 5 of each tick, for each duty actor whose turn is complete — $3$ vested reviews or $30$ ticks on duty, whichever first — and who holds no open review and has not volunteered to stay: the free actor with the lowest $\kappa$ (then lowest id) who is uncommitted, holds no review, and can fund a bond at the current index enters duty, and the outgoing actor leaves, **in one step**. If no such actor exists, the outgoing actor stays. Each handover is a recorded event. [R3-J]

---

## 14. Verifiable history and trust boundary

**Implemented.** The record — ledger events, case log entries, rotations — is a single append-only, hash-chained history; every tick verifies the chain (I16). This is tamper-evidence *within the harness*: an edit to any past entry breaks verification. It is not a trust anchor, because no head is committed outside the process; that remains the trusted recording authority of v0.1 §14, still bracketed (§22). [R3-J]

**Implemented.** Blindness is a visibility rule, and the harness now has the view that enforces it: a reviewer is handed a `ReviewView` — the submission, the actor, the deadline, the bond and cap, whether the review is resumed — and not the case's verdicts, challenge records, reviewer identities, or the assignment's role. A policy that is given the world instead of the view is outside the specification. [R3-J]

---

## 15. The human in the loop

### 15.2 The plug (completed)

**Agreed (revised).** An override **before vesting is the ruling.** Completed reviews whose verdict contradicts the override are overturned with the standard consequences; open assignments are voided without a burn; if a challenge is open, the override settles it, stating both answers when the case is a $\bot$. The grade is human-explicit for a root case. An override **after vesting** moves no money; it changes the recorded outcome and grade, records a failed outcome for the actor and for every settled reviewer whose verdict it contradicts, and may create a corrective obligation. A nested case's grade stays procedural under any override; the override is recorded as an assessment. [R3-G]

---

## 16. Worked example

v0.4 §16 stands unchanged: at $v=1$ the credit cost of a review equals its real cost, so every number is the same, and the reference implementation reproduces them (A $+23$, B $+2$, C $+4$, D $+5$, H $-50$, Ω untouched, grade procedural). Two variants are added for the new rules.

**Variant — appeal of ⊥, objection rejected.** C returns $\bot$ at 6 (cost 3, reimbursed from the deposit). A appeals at 7 ($D=2$ to Ω). E and F each answer *rejected, F* at cost 3. The $\bot$ is overturned: 2 from C's bond to A, 3 burned; outcome $\mathsf F$; vesting at 16. The numbers are those of the ordinary appeal variant: A $+23$, C $-5$, E and F $3$ each.

**Variant — appeal of ⊥, objection upheld.** Same to the appeal. E and F each answer *upheld, N*. The $\bot$ stands; A bears the fee; the case is final $\mathsf N$ at once: A forfeits $G=20$ to H and its escrow returns; C's bond is released at that tick's settlement and C, E and F are paid as correct verdicts. A: $-12-2-20$ for work it could not show.

---

## 17. Rule and invariant checklist

Carried unchanged: everything in v0.4 §17 not listed here. Revised or new:

| ID | Rule | Status |
|---|---|---|
| R48′ | A case is denominated at its first lock: root at award, nested at posting. | Agreed |
| R56 | One active assignment per actor; a P or ⊥ keeps its reviewer attached until the actor acts. | Agreed |
| R57 | Every amount is validated; an action completes under its rules or changes nothing. | Agreed |
| R58 | A withdrawn review vacates its position, whichever kind; a replacement audit after the window is admissible if the original was timely. | Agreed |
| R59 | Costs are recorded in credits burned; the kill-fee basis is §4.6 execution cost. | Agreed |
| R60 | Ω pays its claims FIFO on every inflow; an overturned reviewer's cost obligation survives; a no-reviewer settlement returns the deposit. | Agreed |
| R61 | Revision and evidence are two steps with their own windows; the resumed review returns F or N only; one revision per case. | Agreed |
| R62 | An appeal of ⊥ states the objection's disposition and the fulfillment verdict; nothing infers one from the other. | Agreed |
| R63 | An override before vesting is a ruling for reviewers too; after vesting it records failed outcomes for contradicted reviewers and moves no money. | Agreed |
| R64 | Every exit withdraws the exiting case's unawarded nested requests. | Agreed |
| R65 | Rotation: a turn is 3 vested reviews or 30 ticks; lowest-κ free actor replaces before release; volunteers stay. | Provisional (as implemented) |

**Invariants, as implemented (`sim/invariants.py`):** I1 every credit is in a wallet, a case pool or Ω, their sum is $M$, *and* $M$ equals mints minus burns reconstructed from the event log; I2 no negative or non-finite balance anywhere; I3 only known event kinds with finite non-negative amounts; I4 a court fee is reimbursed at most once, never above the bond, $G^V\ge D$ per case; I5 no case vests with an open item, an unresolved challenge, an open review, or before its window; I6 an audit is assigned no earlier than the verdict it audits; I7 a nested case reaches its initial verdict before its parent submits; I8 positions per case $\le V_{\max}$; I9 the reserve holds $X$; I10 no adjudication moves money after vesting; I11 $I_N$ and $I_{\mathrm{pool}}$ are exclusive; I12 nominals do not change after the first lock, $G$ not after award, and an unawarded nested case's rejection bond equals its frozen $G^V$; I13 every settled case has one grade and the record justifies it; I14 one active assignment per actor; I15 every wallet's $L$ is the sum of its lock records and every live obligation has a record of exactly its size, with no orphan records; I16 the history chain verifies.

---

## 18. Provisional defaults, hypotheses, and remaining opens

Defaults as in v0.4 §18.1, with the reserve enforced and the lowest-$X$ actors on duty by default, rotation at 3 reviews / 30 ticks, and $\rho$, $\kappa$ windows of 100. The hypotheses of v0.4 §18.2 stand; the review's own framing is adopted for what a run can show: a passing suite is evidence of conformance, and only strategy-driven runs are evidence about incentives.

---

## 19. Initialization (completed)

As in v0.4 §19, with the validity check enforced in code ($\lvert\mathcal A_0\rvert\cdot\text{float}+\Omega_0\le M_0$), the lowest-id $X$ actors on duty by default, and the reserve invariant on by default.

---

## 20. Superseded in v0.5

Denomination at award for nested cases; "every case repays its advance"; one-step revision and evidence; the single-answer appeal of ⊥; overrides that left reviewers untouched; rotation, windows, the reviewer view and the chained record as bracketed items.

---

## 21. Sources and decision provenance

**[C0]–[C12], [R1], [R2], [I]** as before.

**[R3] Third external review (October 15, 2026), of v0.4 and its reference implementation.** Reproduced the supplied suites; added twenty targeted regressions, of which all failed on v0.4; identified input validation and atomicity (A), reviewer occupancy (B), replacement of timed-out appeal and audit positions (C), cost units and the kill-fee basis (D), the nested bond's valuation gap (E), unserviced Ω claims, lost deferred costs and the swept deposit (F), override semantics (G), partial-revision and ⊥-appeal representation (H), orphaned siblings (I), and the bracketed mechanisms (J); and showed why the v0.4 invariants did not catch these. Its closing scope — repair transitions, preserve units and liabilities, implement the selected mechanisms, then run strategies — is what this revision followed. The three rule decisions it surfaced were taken in discussion: denomination at first lock, the §4.6 cost basis for kill fees, and the two-question appeal of ⊥.

**[I2] Reference implementation, v0.5.** The attached reviewer after P or ⊥; voided versus withdrawn reviews; partial FIFO servicing; the `ReviewView` fields; the chain's scope.

---

## 22. Reference implementation

`agentic_sim/` is the rules as code, with no strategies. Every action is validated and atomic; after every tick the sixteen invariants of §17 run.

| File | Contents |
|---|---|
| `sim/params.py` | §18.1 defaults, §19 values, windows, rotation |
| `sim/ledger.py` | wallets with named lock records; case pools; Ω; the backed credit and halt state; amount validation; the hash-chained `History` |
| `sim/engine.py` | cases, reviews, challenges including the two-question ⊥ appeal, delegation, settlement, Ω servicing, rotation, `observe()`, the tick order |
| `sim/invariants.py` | I1–I16, each stating what it establishes |
| `sim/strategies.py` | the decision seams; reviewers receive a `ReviewView` |
| `tests/test_spec.py` | §16 and variants; R1/R2 exceptional paths — 23 |
| `tests/test_review_regressions.py` | R3's twenty regressions, verbatim — 19 pass; case 12 is the expected failure, because it appeals a ⊥ without stating the objection's disposition, which §8.1 now requires and refuses to infer |
| `tests/test_v05.py` | the v0.5 rules in explicit form, including the three ⊥ cases — 15 |
| `run_tests.py` | plain Python; pytest optional |

**Implemented:** every rule in §§2–15, rotation, trailing windows, the reviewer view, the chained record, the reserve default and its enforcement, validation and atomicity.

**Bracketed, deliberately:** strategies, learned selection, and any actual evaluator behavior (the harness has no request content and no judgment); an external commitment of the history head (the chain is tamper-evident in-process only); physical tick duration; the real-value exchange behind $\mathrm{Res}_t$. A passing suite is evidence that the rules agree and that the harness obeys them. It is not evidence about incentives; that is what strategies behind the seams are for.

---

## Closing statement

> The rules now agree with each other, the harness obeys them under independent regression, and each invariant checks what its name claims. An appeal of "you didn't look" is decided by whether there was something to look at. A case is priced when its first credit is locked. Nobody holds two assignments. Every lock has a name. Every exit cleans up. Ω pays its debts. The human's override is a ruling before vesting and a record after it. The next step is unchanged, and now unobstructed: strategies behind the seams, and runs.

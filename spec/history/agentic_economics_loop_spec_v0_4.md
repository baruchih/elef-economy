# Agentic Economics — The Task, Verification, and Dispute Loop

## Working specification v0.4

**Project:** Agentic-OS / Agentic Economics  
**Prepared:** October 15, 2026  
**Supersedes:** v0.3 (October 15, 2026). Where this document is silent, v0.3, then v0.2, then v0.1 stand.  
**Nature of this revision:** The last prose-only reconciliation. Every finding of the second external review [R2] is resolved to a rule, and the rules are now also expressed as a reference implementation (§22) whose tests replay the worked example and every exceptional path both reviews raised. Where writing the implementation forced a choice that prose had left loose, the choice is recorded here and marked **[I]**.  
**Status:** Agreed rules, consequences, provisional defaults, and an initialization, all exercised by code. The loop is simulable. It is not a validated mechanism: what the simulation must find is listed in §18.2.

> **The wallet supports the purpose; it does not define the purpose.**
>
> **The actor competes on its promise, is assessed on its delivery, and bears the cost of its execution.**
>
> **The past is append-only. The present is committed. The future is mutable.**
>
> **Money enters with requests. Truth enters with requesters. Verification is the security work of the economy.**
>
> **The human is the battery — and holds the plug.**

### What changed from v0.3

| Finding | v0.4 resolution |
|---|---|
| [R2] §4.3 gave two payout instructions after a shortfall | One rule: entitlements, then repayments, then a pro-rata haircut (§4.3) |
| [R2] "Every case repays its advance" vs FIFO claims on future ω | Ω is a revolving float that bears cross-case risk; a case repays to the extent its pool covers; the remainder is a bounded claim on Ω (§4.3, §10.4) |
| [R2] Nested cases have φ = 0, so nested audits always landed on Ω | Verification of a nested case draws on its **root's** deposit (§4.3) |
| [R2] Deferred payment contradicted "no funds move after vesting" | Invariant reworded: no *adjudication* moves money after vesting; obligations established before vesting may still be paid (§6, §17) |
| [R2] "Unused deposit returned" vs residue paid as fees | "Unused" means a case that settles with no entitled reviewer (§4.3) |
| [R2] Appeal against an unbonded nested rejection had no reimbursement source | Posting a nested request locks β′ + G^V; the G^V is released on acceptance and is the requester-actor's bond on rejection (§9.2) |
| [R2] Indexing could make a later court fee exceed the bond already locked | A case is denominated at award; every nominal attached to it is indexed once and frozen (§4.5) |
| [R2] Review timeouts broke the "three distinct reviewers" invariant | V_max bounds *positions* on a challenge path; distinct actors over a lifetime are unbounded under replacement (§12) |
| [R2] $\lvert\mathcal R_t\rvert<V_{\max}$ was called a working-capital shortfall even when reviewers were merely busy | Occupancy and solvency shortfall are distinguished (§12) |
| [R2] $\mathrm{Res}_t\to0\Rightarrow p_r\to\infty$ did not follow | Corrected: purchases are value-neutral; reserve and supply exhaust together; the halt is Res = 0 (§4.4) |
| [R2] "Human disputed" was graded human-explicit even when the dispute lost | The grade attaches to the event that *established* the settled outcome; a losing assessment is recorded beside a procedural outcome (§15.3) |
| [R2] Kill fee had no delivery boundary; could exceed escrow | Cancellation only until the subcontractor submits; fee from escrow then unlocked; must be fundable (§9.3) |
| [R2] Timeout reimbursement term; tick placement of submissions; resumed-review clock; absolute deadline for pool exhaustion; initialization bounds; §7.4 overbreadth | Each fixed where it lives (§2.2, §7.4, §7.5, §9.4, §10.3, §19) |
| **[I]** Carry-forward emission made the first reviews after a quiet start a lottery | Unclaimed emission is not minted (§4.2) |
| **[I]** "Court fee stays with the loser" named no recipient | The fee is Ω's income at filing; a winning challenger is reimbursed from the liable bond (§8) |
| **[I]** Reviews on a final-N case had no settlement tick | They settle in that tick's emission batch, like a vesting case (§6) |
| **[I]** Grade of an audited case that vests in silence was ambiguous | Procedural: the outcome was established by more than one model verdict (§15.3) |
| **[I]** Unawarded nested requests of a failed parent were orphaned | They fall with the parent; awarded ones continue (§9.4) |

### Reading the status labels

| Label | Meaning |
|---|---|
| **Agreed** | A working rule accepted in discussion. A design commitment, not proof the mechanism works. |
| **Consequence** | A rule that follows from agreed rules, recorded so it is not rediscovered. |
| **Provisional default** | A concrete value or mechanism chosen so the loop can run. Expected to change under simulation. |
| **Formalization** | Notation or accounting used to express the model. |
| **Hypothesis** | A claim about behavior under the rules that the simulation must test. Not a rule. |
| **[I]** | A choice the reference implementation forced; recorded here so prose and code agree. |
| **Open** | Not selected and not on the critical path. |
| **Deferred** | Outside the current core loop; not silently adopted. |

Nominal defaults are stated in $t=0$ credits and frozen per case at award (§4.5).

## Contents

1. Purpose and measurement boundary
2. Participants, time, and the order within a tick
3. Request fulfillment and evidence
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
Appendix A. Learning

---

## 1. Purpose and measurement boundary

**Agreed (unchanged).** The actor's purpose is to fulfill requests economically over time. Currency is an instrument. We assess fulfillment of the request in context; we do not price the outcome's value to the requester's life. Cheap nonfulfillment is not economical fulfillment; extra work is not automatically better. [C1]

**Agreed (unchanged).** The economy has an outside: root requesters supply value, and their explicit judgments are the only ones that are not a model's opinion of another model. Everything internal is calibrated against them and never replaces them. A root case that vests by silence supplies a protocol-default label, not a human one (§15.3). [C12]

---

## 2. Participants, time, and the order within a tick

### 2.1 Participants (unchanged)

Root requesters (a human, or a delegate holding a human budget); derived requesters (actors delegating while committed); actors; the orchestrator — judge and escrow, not bank and not first-line reviewer. Every request carries $\operatorname{root}(q)$; a rootless request is a proposal until sponsored. [C2, C10, C12]

### 2.2 Time, capacity, and the order within a tick

**Agreed (unchanged).** Discrete time; one ordinary commitment per actor; *committed* until the actor responds to its initial verdict, then *pending* until vesting.

**Provisional default (revised).** Within tick $t$:

0. **Participant actions** — submissions, review completions, evidence, revisions, nested postings, responses, challenges, disputes — are recorded as they occur at $t$, in ledger order.
1. Challenges and disputes filed at $t$ are admitted.
2. Deadlines are checked, **inclusive**: an action recorded at the deadline tick is on time. Delivery ($t_0+\tau$), response ($T_{\mathrm{resp}}$), review ($T_{\mathrm{review}}$), nested wait ($T_{\mathrm{wait}}$).
3. Vesting checks and review settlement: a case whose window has closed with nothing open vests; its surviving reviews, and those of any case that reached final $\mathsf N$ this tick, settle in one emission batch.
4. Transfers for everything settled in step 3.
5. Rotation handovers (§13).
6. Assignments and awards: reviews and audits first; nested requests before root requests when the pool is thin.

A challenge filed at $t$ is admitted before the same tick's vesting check. Two events of the same kind at the same tick are ordered by ledger record position. **[I]** The reference implementation applies step 0 as actions are called and runs steps 2–4 when time advances past $t$.

### 2.3 Notation (additions)

| Symbol | Meaning |
|---|---|
| $\mathrm{Reimb}_q$ | Total reimbursement charged to case $q$'s verification |
| $e_v$ | Emission allocated to vested review $v$ |
| $\mathrm{pool}_q$ | Fee pool of case $q$ at settlement: deposit remainder plus $\sum e_v$ |
| $\Omega_t$ | Operating account; a revolving float funded by $\omega$ |
| $\mathcal R_t$ | Review-eligible duty actors: on duty, not excluded from the case, $U_j\ge G^V$ |
| $n_{\mathrm{flight}}(\operatorname{root})$ | In-flight nodes of a root's delegation tree |

All v0.2 and v0.3 symbols otherwise stand.

---

## 3. Request fulfillment and evidence (unchanged from v0.3)

Semantic fit; the actor bears the burden of verifiability; $\bot$ is a substantiated, appealable claim; evidence makes the *properties it exercises* checkable, not the request.

---

## 4. Money: where it enters, where it goes

### 4.1 Money enters with requests (unchanged)

On award of $q$ at delivery price $B$: pay-in $=B+\varphi_q+\omega_q$. $B$ to the actor at vesting; $\varphi_q$ the verification deposit; $\omega_q$ to $\Omega$. [C9, C12]

### 4.2 Emission funds verification

**Agreed (unchanged).** A fixed, decaying schedule $E_t$ is distributed only to reviews that vest or settle in the period, weighted by role. [C9, C11]

**Provisional default (revised, [I]).** $E_t=E_0\cdot2^{-t/H}$, $E_0=10$, $H=1000$. **Emission not claimed in a period is not minted.** v0.3 carried it forward, which made the first reviews to vest after a quiet start a lottery — sixteen quiet ticks and two reviewers would have split sixteen periods of emission. A block reward that is not mined is not banked; neither is this.

**Consequence (unchanged).** Emission mints claims on the same reserve; it adds no real resources.

### 4.3 The verification deposit and the single payout rule

**Agreed.** $\varphi_q$ funds the verification of $q$ **and of every nested case under $q$**: a nested case has $\varphi=0$ and its reviews — appeals of the requester-actor's rejection, and audits of its acceptances — draw on the root's deposit, because they protect the root's outcome. [R2]

**Reimbursement at completion.** Each review's $\min(\widetilde C^V,K)$ is paid from the root's deposit; if that is exhausted, advanced from $\Omega_t$; if $\Omega_t$ cannot cover it, deferred to settlement.

**Settlement — one rule.** At the tick a case vests or reaches final $\mathsf N$:

1. *Entitlements.* For each surviving review $v$ of the case: $\text{ent}_v=e_v+\dfrac{(\varphi_q-\mathrm{Reimb}_q)^+}{\lvert\mathrm{Surv}(q)\rvert}$, where $e_v=\dfrac{w_{r(v)}}{\sum_{v'\in\mathrm{Batch}_t}w_{r(v')}}E_t$ over every review settling at $t$ across cases.
2. *Pool.* $\mathrm{pool}_q=(\varphi_q-\mathrm{Reimb}_q)^+ +\sum_{v\in\mathrm{Surv}(q)}e_v$. The emission is minted into the pool.
3. *Repayments, from the pool first:* deferred reimbursements to reviewers, then $\Omega$ advances. Whatever the pool cannot cover becomes a reviewer claim on $\Omega$ (deferred reimbursement) or an unrepaid advance (absorbed by $\Omega$).
4. *Haircut.* Fees are the entitlements scaled by $\dfrac{\mathrm{pool}_q-\text{repaid}}{\mathrm{pool}_q}$. The no-shortfall formula of v0.3 is the case where the scale is 1.

An overturned or withdrawn review has no entitlement; its share passes to the surviving reviews. **Unused deposit** — a case that settles with no surviving review — is returned to the requester; otherwise the deposit remainder is fees, not a refund. [R2]

**$\Omega$ is a revolving float, not a per-case guarantee.** It advances reimbursements, is repaid from case pools to the extent they cover, and bears the cross-case risk of what they do not. Unpaid reviewer claims on $\Omega$ are settled from later $\omega$ receipts, first in, first out. Each claim is bounded by $K$; the *aggregate* outstanding claim is a monitored quantity, not a cap (§18.2). [R2]

**Provisional default.** $\varphi_q=2K=10$ at root; $w$: 1 / 1.5 / 1.5 (ordinary / appeal / audit); $\omega_q=0.05\,B$.

### 4.4 Floating prices: a backed credit (corrected)

**Provisional default (unchanged mechanism).** $v_t=\mathrm{Res}_t/M_t$. Root pay-in mints against reserve; a resource purchase burns $c/v_t$ credits and pays $c$ from reserve; emission mints against nothing; forfeited bonds burn; guarantees, kill fees and court fees transfer.

**Corrected from v0.3.** A resource purchase is value-neutral: $v'=\dfrac{\mathrm{Res}-c}{M-c/v}=v$. Purchases do not move the price; they consume real backing and credits in step. Emission lowers $v$; nothing else does. With no new root pay-in, actor income is emission only, which is finite, so busywork halts when actors can no longer afford resources — through their wallets, not through a rising price. The reserve and the supply exhaust *together*, because the dilution from emission was spread over every holder along the way; nothing "remains" at $\mathrm{Res}=0$. $\mathrm{Res}_t=0$ is the **halt state**: $v_t=0$ by definition, never $0/0$, and any emission minted afterwards is worthless. [R2]

The plug is held by the root-request rule and the interruption rules (§15); the reserve is the backstop.

### 4.5 Valuation time: a case is denominated at award

**Agreed (new).** Every nominal amount attached to a case — $D$, $K$, $G^V$, $\varphi$, and the bonds of every review assigned to it — is indexed once, at the case's award, and frozen for the case's life. $G^V\ge D$ then holds jointly for every review of the case, and so does the deposit-to-cap relation, whatever $v_t$ does afterwards. A review assigned later to the same case locks the case's frozen $G^V$, not a re-indexed one. [R2]

### 4.6 Execution cost (unchanged, plus kill fees)

---

## 5. Offers, selection, and guarantees

**Unchanged from v0.3.** The bid commits price and time, $(B,\tau,G)$ with $B\le\beta_q$; $\beta_q$ is the maximum delivery price and the requester sees the all-in; selection is predicted fulfillment minus $\lambda B/\beta$, ties by vested duty credit; $G=\lceil0.5B\rceil$.

---

## 6. Task lifecycle: committed, pending, vested

| Stage | What happens | Capacity | Funds |
|---|---|---|---|
| Available | $q\in\mathcal P_t$ | — | — |
| Award | Escrow and deposit funded; $G$ locked; nominals frozen; deadline $t_0+\tau$ | Committed | $G$ locked |
| Executing | Work; nested requests (§9); revision | Committed | — |
| Submitted | Result and evidence recorded, at or before the deadline | Committed | — |
| Initial verdict | $\mathsf F/\mathsf N/\mathsf P/\bot$ | Committed until response | — |
| Pending | Window $W$ runs from the verdict | **Released** | $G$ locked |
| Suspended | A challenge or audit is open; the window does not close | Released | $G$ locked |
| Vested | Window closed, nothing open, verdict standing | Free | $B$ paid; $G$ released; reviews settled |
| Final $\mathsf N$ | Deadline missed, rejection accepted or defaulted, appeal lost, dispute upheld | Free | $G$ forfeited; escrow returned; reviews settled **this tick** |

**Agreed.** Vesting is at $\max(t_0+W,\ t_{\mathrm{resolve}})$. A challenge filed at $t\le t_0+W$ is admitted (step 1 precedes step 3). **Vesting is financial finality.** The invariant, reworded: *after vesting, no adjudication changes the case's financial obligations; obligations established before vesting may still be paid.* [R2]

**[I]** Surviving reviews of a case that reaches final $\mathsf N$ settle in that tick's emission batch, exactly as for a vesting case, so a correct rejection is paid the same way as a correct approval.

**Responses** within $T_{\mathrm{resp}}$ (no response is acceptance): $\mathsf N$ → appeal or accept; $\mathsf P$ → one revision; $\bot$ → supply evidence, appeal, or accept. **The review clock pauses** while the actor acts: when the same reviewer resumes after evidence or a revision, its deadline is extended by the ticks the actor used, and the resumed work is the same assignment under one reimbursement cap. [R2]

**Provisional default.** $W=10$, $T_{\mathrm{resp}}=2$, $T_{\mathrm{rev}}=5$, $T_{\mathrm{evid}}=3$, $P^{\mathrm{fail}}=0$.

---

## 7. Verification: eligibility, bond, compensation, deadline

### 7.1 Roles and eligibility

Initial reviewer at root ($m_0=1$); none at nested (the requester-actor judges); two fresh appeal reviewers; one blind auditor plus one more on disagreement. Eligibility for a review of $q$: on duty, not excluded from $q$ (its actor, its requester, its previous reviewers, and any reviewer withdrawn from it), and $U_j\ge G^V_q$.

### 7.2 The bond is the whole liability (unchanged)

$G^V$ locked per verdict; on overturn, the winning challenger's court fee is paid from it and the remainder burned; on survival, released at settlement. Appeal reviewers who dissent from the outcome forfeit the bond and owe no fee. **Provisional default.** $G^V=5$, $D=2$, frozen at award.

### 7.3 Compensation (unchanged in structure)

Capped reimbursement at completion from the root's deposit (§4.3); fee at settlement by the single payout rule.

### 7.4 What the rules establish about careless review

**Hypothesis (rewritten).** For a reviewer that approves without examining, with audit rate $p$, base failure rate $b$, expected surviving fee $\bar f$, and bond $G^V$, and assuming audits catch every failure:

$$\mathbb E[\Delta W]=(1-pb)\,\bar f-pb\,G^V,\qquad\text{negative iff }G^V>\bar f\,\frac{1-pb}{pb}.$$

This is a joint condition on all four quantities; it is not "monetary deterrence holds only at high audit rates." At $p=1$ with $b=0.2$, $\bar f=2$, $G^V=5$ the expectation is still $+0.6$. And the sign of this expectation is not the test that matters: careful review may dominate careless approval while both are positive. The question for the simulation is whether the combination of fee, bond, audit rate, and the reliability consequences of an overturn makes careful review the better response (§18.2). A verdict that survives is procedurally settled, not correct. [R2]

**Provisional default.** $p_j$ starts 0.5, halves after 5 consecutive survivals, floor 0.2, doubles on overturn, cap 0.5.

### 7.5 Review deadline

**Agreed (clarified).** A review not completed by $t_{\mathrm{assign}}+T_{\mathrm{review}}$ (plus any paused ticks) is withdrawn: half the bond burned, half released, **no reimbursement**, reliability down, the reviewer excluded from the case, and the position vacated for reassignment. **Provisional default.** $T_{\mathrm{review}}=5$.

---

## 8. Challenges: appeal, requester dispute, and audit

One challenge round per case; a dispute consumes it; an audit that disagrees consumes it.

**[I] The court fee.** The challenger pays $D$ to $\Omega$ at filing. If the challenger wins, the liable bond reimburses $D$ to the challenger; if it loses, nothing further moves. The loser therefore bears the fee, and $\Omega$ always receives it. "Stays with the loser" in v0.3 named no recipient; this does.

**8.1 Appeal** (unchanged in flow): $D$, $d_q$, two fresh reviewers, orchestrator on a split; applies to $\mathsf N$ and $\bot$.

**8.2 Requester dispute** (unchanged): within the window, same terms; upheld → final $\mathsf N$; rejected → vest.

**8.3 Audit** (clarified): blind, assigned by the orchestrator, suspends vesting. Agreement → a second settled review. Disagreement → the audit verdict stands as one appeal review, one more fresh reviewer, orchestrator on a split. If a dispute opens while an audit is open or after it agreed, the audit verdict is one of the two dispute reviews. If the audit already disagreed, the round is in use and no dispute is admitted.

**8.4 Final authority** (unchanged).

---

## 9. Delegation: nested requests

### 9.1 A nested request is a full loop (clarified)

$A$ posts $q'$ under $q$; $B$ wins and locks its guarantee; $A$ escrows $B'$, judges, and its judgment is $q'$'s initial verdict. $A$ submits $q$ only after every nested request it posted has reached its **initial verdict** or been withdrawn or cancelled; nested vesting is independent and $A$ bears that risk.

**Narrowed (unchanged from v0.3).** The root pointer forbids rootless requests, not unnecessary ones. Unnecessary delegation is constrained by $A$ paying for it from its own margin.

### 9.2 Posting locks the price ceiling and a rejection bond

**Agreed (new).** Posting $q'$ with maximum price $\beta'$ locks $\beta'+G^V$ from $A$'s unlocked balance. At award, $B'$ moves into escrow and $\beta'-B'$ is released; the $G^V$ stays locked as $A$'s **rejection bond**. If $A$ accepts, the rejection bond is released at once — acceptance is not bonded, because its downside flows through $A$'s own delivery. If $A$ rejects, the rejection bond is $A$'s reviewer bond for $B$'s appeal: on overturn it pays $B$'s court fee and the remainder burns; if the rejection stands, it is released at $q'$'s settlement. $A$ is then exactly an original reviewer for appeal purposes, and the case is affordable by construction. [R2]

The principle: bond the verdict whose wrongness harms the *other* party with no other recourse. A wrong acceptance harms $A$; a wrong rejection harms $B$.

**Exception (unchanged).** $A$'s guarantee secures one obligation — delivery of $q$. An acceptance overturned by audit forfeits $B$'s guarantee to $A$ and lowers $A$'s reliability; it imposes no separate monetary loss on $A$.

### 9.3 Self-execution is always an exit — with two boundaries

**Agreed (revised).** Before award, $A$ withdraws $q'$ freely. After award and **before $B$ submits**, $A$ may cancel by paying $B$ a kill fee of $\min(\widetilde C_{B},K)$ — from the nested escrow first, then from $A$'s unlocked balance — and cancellation is available only if $A$ can fund it. $B$'s guarantee and $A$'s rejection bond are released; $B$ is unmarked; the fee counts in $A$'s cost. **Once $B$ has submitted, $A$ must judge.** [R2]

### 9.4 When the pool is thin

**Agreed (clarified).** Pool-exhaustion withdrawal is available when $q'$ has been open and unawarded since $t_{\mathrm{post}}$ and $t\ge t_{\mathrm{post}}+T_{\mathrm{wait}}$ **and** $t\le$ the parent's absolute delivery deadline. If the deadline arrives first, it is an ordinary miss with full forfeiture: posting the child late does not create the reduced-forfeiture exit. Nested requests are awarded first when the pool is thin. **[I]** When a parent reaches final $\mathsf N$ for any reason, its unawarded nested requests are withdrawn with it and $A$'s locks released; awarded ones continue, since $B$'s work is still owed to $A$. [R2]

**Provisional default.** $T_{\mathrm{wait}}=5$, $\rho_{\mathrm{pool}}=0.25$, thin $\le2$ free.

### 9.5 Capacity accounting (corrected)

A delegation tree commits $n_{\mathrm{flight}}(\operatorname{root})$ actors — its in-flight nodes — not its depth. [R2]

---

## 10. Wallet accounting and settlement

### 10.1 Locks and escrow (unchanged)

### 10.2 Actor settlement

$$\Delta W^{\mathrm{case}}_{iq}=P_{iq}-C_{iq}-I_DD_q+I_WD_q-I_NG_{iq}-I_{\mathrm{pool}}\,\rho_{\mathrm{pool}}G_{iq},\qquad I_N+I_{\mathrm{pool}}\le1,$$

with $I_N=1$ on any final $\mathsf N$ including a missed deadline, $I_{\mathrm{pool}}=1$ only on a §9.4 withdrawal, $I_WD_q$ paid from the liable bond, and $C_{iq}$ including nested payments and kill fees.

### 10.3 Reviewer settlement

$$\Delta W^V_{jv}=I_{\mathrm{paid}}\min(\widetilde C^V_{jv},K)-C^V_{jv}+I_{\mathrm{vest}}\,f_{jv}-I_{\mathrm{over}}\,G^V-I_{\mathrm{late}}\,\tfrac12G^V,$$

where $I_{\mathrm{paid}}=0$ for a withdrawn review (§7.5), the court fee is inside $I_{\mathrm{over}}G^V$ and is owed only by the reviewer whose verdict was challenged, and $f_{jv}$ is the haircut entitlement of §4.3.

### 10.4 Escrow and the operating account

Per root request: in $=B+\varphi+\omega$; out $=B$ at vesting, reimbursements from $\varphi$ at completion (for the root and its nested cases), fees and any unused deposit at settlement, $\omega$ to $\Omega$. Court fees to $\Omega$ at filing; reimbursed to a winning challenger from the liable bond. Forfeited guarantees to the requester; forfeited bonds, net of court-fee reimbursement, burned. Kill fees transfer. $\Omega$: receives $\omega$ and court fees, advances reimbursements, is repaid from case pools to the extent they cover, and carries bounded claims otherwise.

---

## 11. Reliability and duty credit (unchanged from v0.3, with one correction)

$\rho_i$ from settled outcomes only — including missed deadlines and withdrawn reviews; $\kappa_i$ counts vested reviews; both vest on survival; $\kappa_i$ is a privilege (tie-break, conscription relief, release order) and **not** an emission weight. Emission is weighted by role only.

---

## 12. Protected verification capacity

**Agreed (unchanged).** $\lvert\mathcal V_t\rvert\ge X$, $X=4$.

**Corrected.** $V_{\max}=3$ bounds the **review positions** a case can hold on one challenge path — initial, plus two appeal, or audit plus one — and is what the reserve is sized for. A withdrawn review vacates its position. The number of *distinct actors* a case consumes over its lifetime is unbounded under replacement, since each withdrawn reviewer is excluded from the case's later positions; when no eligible actor remains, the case waits under the ordinary rule. The invariant is on positions. [R2]

**Corrected.** Two conditions, not one: *occupancy* — eligible duty actors exist but are busy — and *solvency shortfall* — fewer than $V_{\max}$ duty actors, busy or idle, can fund the bond. Only the second is a working-capital condition; both are recorded. [R2]

---

## 13. Rotation of verification duty (unchanged)

---

## 14. Verifiable history and trust boundary

**Corrected.** Committing a verdict before an audit is assigned establishes *ordering*. **Blindness is a visibility rule**: the auditor's view excludes the case's verdicts, challenge records and reviewer identities, and the auditor is not told whether an assignment is an initial review or an audit. Leakage through other channels is outside the ledger's guarantee. [R2]

---

## 15. The human in the loop

### 15.1 The battery (unchanged from v0.3)

### 15.2 The plug (unchanged)

Before vesting an override is the ruling. After vesting: no clawback; the recorded outcome and its grade change; reliability adjusts; a corrective obligation may follow.

### 15.3 Label grades attach to what established the outcome

**Agreed (revised).** Every settled case records two things: its **outcome**, and the **grade of the event that established it**. Precedence:

1. An explicit root judgment *that matches the settled outcome* — an accept, a dispute that won, an override — establishes it: **human-explicit**, or **delegate-explicit** when the root requester is a delegate.
2. Otherwise, if any challenge, audit, or ruling occurred, the procedure established it: **procedural**. **[I]** This includes an audited case that then vests in silence.
3. Otherwise — one initial verdict, no challenge, no audit, silence — **protocol-default**.

A root judgment that *disagrees* with the settled outcome — a dispute that lost — is recorded as an assessment beside a procedural outcome. The disagreement is the learning signal; it does not label the outcome human-explicit. Nested cases are always procedural. [R2]

### 15.4 Two classes of verification (unchanged)

---

## 16. Worked example

Illustrative; $\omega$ omitted (with it on, H pays 52 and $\Omega$ receives 2.25). Actors A–F, each able to fund a bond; C, D, E, F on duty ($X=4$). Root requester H. Emission at any settlement tick is taken as 5 credits, i.e. 2 per unit of role weight when C (1) and D (1.5) settle together. Every number below is reproduced by `tests/test_spec.py` (§22).

**Setup.** H posts $q$, $\beta=45$. A bids $B=40$, $\tau=8$, locks $G=20$; H pays $40+10=50$. At $t=1$ A posts $q'$ with $\beta'=6$, locking $6+5=11$; B bids $B'=5$, $\tau'=3$, locks $G'=3$; 5 moves to escrow and 1 is released. B costs 3; A's own work costs 12; C and D each cost 3.

| Tick | Event |
|---|---|
| 0 | A awarded; due by 8 |
| 1 | $q'$ posted and awarded to B; due by 4 |
| 1–3 | B executes, submits with evidence |
| 3 | A accepts $q'$: rejection bond released; B released; $q'$ window to 13 |
| 4 | A submits $q$; C assigned (review deadline 9), locks 5 |
| 6 | C: $\mathsf F$, reimbursed 3 from the deposit; A pending, window to 16; audit rolled: D assigned, blind; vesting suspended |
| 8 | D: $\mathsf F$, reimbursed 3; agrees; suspension lifted |
| 13 | $q'$ vests: B paid 5, $G'$ released; no reviews to settle |
| 16 | $q$ vests, H silent: A paid 40, $G$ released; deposit remainder $10-6=4$ split 2/2; emission C 2, D 3; bonds released; $\kappa_C,\kappa_D$ +1 |

**Nets.** A $+23$ $(40-12-5)$; B $+2$; C $+4$; D $+5$; H $-50$; $\Omega$ untouched. Escrow for $q$: in 50 $=40+6+4$ out. Grade of $q$: **procedural** (an audit occurred); of $q'$: procedural.

**Variant — rejection and appeal.** C returns $\mathsf N$ at 6. A appeals at 7 ($D=2$ to $\Omega$), capacity released; E and F assigned, each cost 3, both $\mathsf F$ at 10; settled without the orchestrator; vest at $\max(16,10)=16$. A $+23$ (fee reimbursed from C's bond); C $-5$ (bond: 2 to A, 3 burned; costs reimbursed; no fee); $\Omega$ $+2$; E and F each $2.5$ emission $+0.5$ deposit remainder $=3$. Grade procedural.

**Variant — pool exhaustion.** No actor takes $q'$. $T_{\mathrm{wait}}=5$ elapses at 6, before the deadline at 8: A withdraws, forfeits $0.25\times20=5$ to H, 15 released, $q'$ withdrawn, A's 11 released; escrow and unused deposit returned. A $-17$; H $+5$. Had A bid $\tau=4$, the deadline would have fallen at 4 and the miss would have been an ordinary final $\mathsf N$: A $-20$, and $q'$ withdrawn with its parent.

**Variant — cancellation.** At 2, after B has spent 2, A cancels: kill fee $\min(2,5)=2$ from escrow, 3 returned, $G'$ and the rejection bond released. B nets 0; A's cost includes the 2; A may still submit $q$. After B submits at 3, cancellation is refused. If $B'=1$ and B had spent 3, the fee is 3: 1 from escrow, 2 from A's unlocked balance, and refused if A cannot fund the 2.

**Variant — nested rejection, appealed.** A rejects $q'$ at 3; its rejection bond (5) stays locked. B appeals at 4 ($D=2$ to $\Omega$); E and F assigned, reimbursed from the **root's** deposit ($10\to4$); both $\mathsf F$ at 7. A's rejection bond: 2 to B, 3 burned; A's reliability down. $q'$ vests at 13: B paid 5. B nets $+2$ — exactly as if accepted; A is down 10 (B's price, and the bond).

**Variant — shortfall and haircut.** C approves at cost 5 (deposit $10\to5$). H disputes at 3 ($D=2$ to $\Omega$, now 22). E and F cost 5 each: the deposit goes to 0 and $\Omega$ advances 5 (now 17). Both $\mathsf F$: the dispute is rejected and all three verdicts stand. At vesting (12) with emission 6 over weights $1+1.5+1.5$: entitlements $1.5,\ 2.25,\ 2.25$; pool $=0+6$; repay $\Omega$ 5; remaining 1; scale $1/6$; fees $0.25,\ 0.375,\ 0.375$. $\Omega$ back to 22. Grade **procedural**, with H's $\mathsf N$ recorded beside it.

**Variant — timeout and replacement.** C is assigned at 1 and never completes; withdrawn at 6 (half bond burned: $-2.5$), excluded, position vacated. D replaces and approves at 8; E audits at 9 and rejects at 10 — the audit stands as one appeal review; F is assigned and approves at 11; the orchestrator rules $\mathsf F$; E's bond burns. Positions on the path: 3. Distinct reviewers over the case: 4.

**Variant — finality.** C approves at 2, window to 12. H disputes at 12 — the window's last tick — and the dispute is admitted; E and F approve at 14; the case vests at 14, not 12. At 20 H overrides to $\mathsf N$: the outcome and grade change, A's reliability drops, a corrective obligation is recorded, and no credit moves.

---

## 17. Rule and invariant checklist

Carried unchanged: R01–R04, R07, R10, R11, R14, R19, R21–R24, R26, R06′, R12′, R18′, R27–R31, R33–R36, R37, R38, R41–R44, R46. Revised or new:

| ID | Rule | Status |
|---|---|---|
| R16‴ | Reimbursement from the root's deposit, then $\Omega$ advance, then deferral; settlement by the single payout rule: entitlements, repayments, pro-rata haircut. | Agreed |
| R17‴ | $\varphi$ at root funds the root's and its nested cases' verification; nested $\varphi=0$. | Agreed |
| R20″ | $V_{\max}=3$ bounds review positions per challenge path; withdrawn positions are vacated; distinct actors over a lifetime are unbounded. | Agreed |
| R39′ | Reserve membership, occupancy, and solvency shortfall are three recorded quantities. | Agreed |
| R40′ | Posting a nested request locks $\beta'+G^V$; the $G^V$ is released on acceptance and is the rejection bond on rejection. One guarantee still secures one obligation. | Agreed |
| R41′ | Cancellation after award is available only until the subcontractor submits; fee from escrow then unlocked; must be fundable. | Agreed |
| R45′ | Emission is weighted by role and unclaimed emission is not minted. | Agreed / [I] |
| R48 | A case is denominated at award: every nominal attached to it is indexed once and frozen. | Agreed |
| R49 | The grade attaches to the event that established the settled outcome; a losing root assessment is recorded beside a procedural outcome. | Agreed |
| R50 | The court fee is paid to $\Omega$ at filing; a winning challenger is reimbursed from the liable bond. | [I] |
| R51 | Reviews of a final-$\mathsf N$ case settle in that tick's emission batch. | [I] |
| R52 | Deadlines are inclusive; participant actions at $t$ precede the tick's processing. | Provisional |
| R53 | Pool-exhaustion withdrawal requires $t_{\mathrm{post}}+T_{\mathrm{wait}}\le t\le$ the parent's absolute deadline. | Agreed |
| R54 | Unawarded nested requests of a failed parent are withdrawn with it. | [I] |
| R55 | An initialization is valid only if $\lvert\mathcal A_0\rvert\cdot\text{float}+\Omega_0\le M_0$. | Provisional |

**Invariants, as implemented (§22, `sim/invariants.py`):** I1 every credit is in a wallet, a case pool, a fee pool or $\Omega$, and their sum is $M$; I2 no negative balance; I3 the only mints are backed pay-in and emission, the only burns are bond forfeiture and resource purchase; I4 a court fee is reimbursed at most once, never above the bond, and $G^V\ge D$ per case; I5 no case vests with an open challenge or audit, or before its window; I6 an audit is assigned no earlier than the verdict it audits; I7 a nested case reaches its initial verdict before its parent submits; I8 positions per case $\le V_{\max}$; I9 the reserve holds $X$ when enforced; I10 no adjudication moves money after vesting; I11 $I_N$ and $I_{\mathrm{pool}}$ are exclusive; I12 nominals do not change after award; I13 every settled case carries exactly one of four grades, nested cases procedural; I14 one commitment per actor; I15 every bond a reviewer holds is locked.

---

## 18. Provisional defaults, hypotheses, and remaining opens

### 18.1 Provisional defaults

As in v0.3 §18.1, with: emission **not carried forward**; $p$ floor $0.2$; $T_{\mathrm{wait}}=5$; the tick order of §2.2; and the initialization validity check of §19.

### 18.2 Hypotheses the simulation must test

1. **Careful vs careless review** (§7.4): under the defaults, is careful review the better response once reliability consequences are included, and at which $(p,G^V,\bar f)$ does it stop being so?
2. **Price pressure:** does $\lambda=0.2$ produce competition without starving reliable actors?
3. **Verification funding:** how often does $\Omega$ advance, how large is its aggregate outstanding claim, and does $\varphi=2K$ cover root-plus-nested verification at realistic tree sizes?
4. **Emission scale:** total scheduled emission is $\approx1443E_0$ against $M_0$; is it a subsidy or a flood, and does the no-carry rule leave quiet periods underfunded?
5. **Delegation liveness:** with $T_{\mathrm{wait}}=5$, the kill fee, nested-first priority, and the rejection bond's capital cost, do trees of 2–4 nodes move?
6. **Reserve solvency vs occupancy:** how often is each condition recorded, and do fees restore solvency?
7. **Monetary behavior:** $v_t$ under a varying human request rate; whether busywork halts through wallets as §4.4 now says.
8. **Dominant strategies:** anything cheap the rules missed.

### 18.3 Remaining opens (off the critical path)

As in v0.3 §18.3, plus: the recipient side of corrective obligations; the cadence and funding of human review of rulings; whether delegate-explicit labels should calibrate differently from human-explicit ones.

---

## 19. Initialization

**Provisional default.** As in v0.3 §19 — $v_0=1$, $\mathrm{Res}_0=10{,}000$, float 50 per actor, $\Omega_0=20$, $X=4$ lowest ids, $\rho_i(0)=0.5$, $p_j(0)=0.5$ — with the validity check: a run is rejected unless $\lvert\mathcal A_0\rvert\cdot50+20\le M_0$, i.e. at most 199 actors at the defaults. The float is sized so that every initial reserve member can fund a bond and a modest first guarantee. [R2]

---

## 20. Deferred ideas and superseded alternatives

**Superseded in v0.4:** two-step payout after shortfall; "every case repays its advance"; nested verification on $\Omega$; unbonded nested rejections; nominals indexed at use; $V_{\max}$ as a lifetime count; carry-forward emission; "stays with the loser"; grades by participation; "self-execution at any time" without a delivery boundary; "$\mathrm{Res}\to0\Rightarrow p_r\to\infty$".

**Still deferred:** as in v0.3 §20, plus clawback after vesting (rejected; corrective obligations instead) and any per-case cap on $\Omega$'s aggregate claims.

---

## 21. Sources and decision provenance

**[C0]–[C12]** as in v0.1–v0.2. **[R1]** as in v0.3.

**[R2] Second external review (October 15, 2026), of v0.3.** Confirmed as resolved: reimbursement funding, bond versus liability, timely challenges outlasting the window, post-vesting override, the nested milestone, $\beta_q$. Found: the two-step payout after shortfall and the over-strong repayment claim; the unbonded nested rejection; indexing versus the locked bond; timeouts versus the three-reviewer invariant and the occupancy/solvency conflation; the $p_r\to\infty$ non sequitur; "human-explicit" attached to a losing dispute; the kill fee's missing delivery boundary and escrow overrun; and the table of timing and initialization corrections. Its closing distinction — that simulation reveals whether incentives work but must not silently choose between incompatible rules — is what §22 answers.

**[I] Reference implementation (October 15, 2026).** Choices the code forced, each recorded in the "What changed" table: no-carry emission; the court fee's recipient; final-$\mathsf N$ settlement timing; the grade of an audited silent case; orphaned nested requests; inclusive deadlines.

**[M1], [S1]–[S3]** unchanged.

---

## 22. Reference implementation

`agentic_sim/` is the rules as code, with no strategies. Every bid, verdict, appeal, audit assignment, ruling and human action is injected; the engine validates it against the case state machine and the tick, applies its ledger effects, and after every tick runs the invariants of §17. A failing invariant is a bug in the engine or a contradiction in this document — never a property of a strategy.

| File | Contents |
|---|---|
| `sim/params.py` | §18.1 defaults, §19 values, the emission schedule |
| `sim/ledger.py` | wallets ($U$, $L$), case pools (escrow, deposit, fee pool), $\Omega$, the backed credit, the halt state |
| `sim/engine.py` | cases, reviews, challenges, delegation, settlement, the tick order |
| `sim/invariants.py` | I1–I15 |
| `sim/strategies.py` | the decision seams a driver fills — Protocols only |
| `tests/test_spec.py` | §16 and its seven variants; every exceptional path from [R1] and [R2]; the guards; 23 tests |
| `run_tests.py` | runs with plain Python; pytest also works |

The tests assert *nets*, so the cold-start float does not matter, and they set a flat emission of 5 per tick with $\omega=0$ to reproduce §16's stated assumptions exactly; a separate test turns $\omega$ on. The next review has something to run: a disputed reading of this document becomes a failing test, not a paragraph.

---

## Appendix A. Learning

**Agreed direction (revised).** Observations and labels at the four grades of §15.3, where the grade is of the event that *established* the outcome; a root assessment that lost is a separate recorded signal. No training step promotes a grade; no label at any grade is read as "correct" rather than "accepted." Audit outcomes are procedural labels about reviewers. Representation, update schedule, parameter sharing, and calibration remain open.

---

## Closing statement

> Requesters pay in a price, a verification deposit and a service fee, and judge. Actors commit to a price and a time, execute at their own cost, and submit verifiable results. Reviewers post a bond that is their whole liability and earn only when a verdict stands, by one payout rule. Approvals are audited blind; rejections are appealable; a challenge inside the window holds the case open; vesting is final. Delegation is a full loop: the requester-actor's rejection is bonded, cancellation ends at submission, and self-execution is the exit wherever it is possible. A rotating reserve keeps review positions available and solvency is counted beside it. A case is denominated when it is awarded. The human powers the circuit and holds the plug; idle costs nothing; busywork exhausts the reserve and the supply together. The ledger forgets nothing, and every settled outcome says who established it.

The rules now agree with each other as far as code can tell, which is further than reading could. The next step is to put strategies behind the seams and run.

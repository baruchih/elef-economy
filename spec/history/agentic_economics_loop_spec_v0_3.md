# Agentic Economics — The Task, Verification, and Dispute Loop

## Working specification v0.3

**Project:** Agentic-OS / Agentic Economics  
**Prepared:** October 15, 2026  
**Supersedes:** v0.2 (October 15, 2026). Where this document is silent, v0.2 and then v0.1 stand.  
**Nature of this revision:** A reconciliation pass. No mechanism is added. Every finding of the external review of v0.2 [R1] is resolved to a rule, a narrowed claim, or an explicit exception, so that the selected mechanisms agree with one another.  
**Status:** Agreed rules, consequences, and provisional defaults for every parameter on the critical path, plus an initialization (§19) that defines the first tick. The loop is simulable. It is not an implemented or validated mechanism.

> **The wallet supports the purpose; it does not define the purpose.**
>
> **The actor competes on its promise, is assessed on its delivery, and bears the cost of its execution.**
>
> **The past is append-only. The present is committed. The future is mutable.**
>
> **Money enters with requests. Truth enters with requesters. Verification is the security work of the economy.**
>
> **The human is the battery — and holds the plug.**

### What changed from v0.2

| Review finding [R1] | v0.3 resolution |
|---|---|
| Reimbursements had no funding source | $\varphi_q$ is a verification *deposit*, sized to expected verification cost; reimbursements draw from it first, with a stated shortfall order (§4.3, §7.3, §10.4) |
| Reviewer bond (5) did not cover bond-plus-court-fee liability (7) | The bond is the reviewer's total liability; court-fee reimbursement is paid from it, the remainder burned; $G^V\ge D$ by construction (§7.2) |
| Reserve membership ≠ financially eligible reviewers | Review eligibility requires unlocked balance $\ge G^V$; the reserve invariant and the eligible count are tracked separately (§7.1, §12) |
| "A stamper is negative in expectation" did not follow | Withdrawn. Deterrence is a hypothesis with the inequality stated; at low audit rates the deterrent is reliability, not money (§7.4) |
| A challenge can outlast the window | A challenge or audit opened inside the window suspends vesting until it resolves (§6, §8) |
| Human override after vesting undefined | Vesting is financial finality; a later override changes the record and may create a corrective obligation, never a clawback (§15.2) |
| "Dispute replaces audit" undefined when an audit is already running | The audit verdict becomes one of the two dispute reviews; $V_{\max}$ stays 3 (§8.3) |
| A's guarantee described as backing two obligations | Stated as an explicit exception: one guarantee, one obligation; a wrong nested acceptance has no separate monetary penalty (§9.2) |
| "Self-execution at any time" ignored an awarded subcontract | Pre-award: withdraw freely. Post-award: cancel with a kill fee (§9.3) |
| Root pointer does not prevent unnecessary nesting | Claim narrowed; what constrains nesting is that A pays for it from its own margin (§9.1, §15.1) |
| "Unplug the human and $v_t\to0$" did not follow | Corrected: idle drains nothing; busywork drains the reserve through resource purchases (§4.4) |
| Ground-truth labels conflated four events | Four label grades; nothing promotes between them (§15.3, Appendix A) |
| Emission weight: role $w_r$ vs duty credit $\kappa_i$ | Role weight only; $\kappa_i$ counts the same vesting events and is not a weight (§4.3, §11.3) |
| $I_N$ and $I_{\mathrm{pool}}$ could both fire | Mutually exclusive by rule (§10.2) |
| Child-loop milestone inconsistent ("settles" / "vests" / "initial verdict") | Initial verdict, everywhere (§9.1) |
| Depth $d$ vs committed population | In-flight nodes, not depth (§9.5) |
| $\beta_q$ ambiguous | Maximum delivery price; the requester is shown the all-in (§5.1) |
| Blindness attributed to commit ordering | Ordering from the commit; blindness from a visibility rule (§14) |
| Tick-internal ordering, two missing deadlines, initialization | Tick order (§2.2); delivery time in the bid and a review deadline (§5.1, §7.5); initialization (§19) |

### Reading the status labels

| Label | Meaning |
|---|---|
| **Agreed** | A working rule accepted in discussion. A design commitment, not proof the mechanism works. |
| **Consequence** | A rule that follows from agreed rules, recorded so it is not rediscovered. |
| **Provisional default** | A concrete value or mechanism chosen so the loop can run. Expected to change under simulation; changing it is not a design reversal. |
| **Formalization** | Notation or accounting used to express the model. |
| **Hypothesis** | A claim about behavior under the rules that the simulation must test. Not a rule. |
| **Open** | Not selected and not on the critical path. |
| **Deferred** | Outside the current core loop; not silently adopted. |

Nominal defaults are stated in credits at $t=0$ and indexed once the credit value floats (§4.5).

## Contents

1. Purpose and measurement boundary
2. Participants, time, and notation
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
Appendix A. Learning

---

## 1. Purpose and measurement boundary

**Agreed (unchanged).** The actor's purpose is to fulfill requests economically over time. Currency is an instrument. We assess fulfillment of the request in its applicable context; we do not price the outcome's value to the requester's life. Fulfill with the least necessary work and resource expenditure. Cheap nonfulfillment is not economical fulfillment; extra work is not automatically better. [C1]

**Agreed.** The economy has an outside. Root requesters supply value (they pay in) and the only judgments that are not a model's opinion of another model. Everything internal — reviewers, auditors, the orchestrator — is calibrated against root outcomes and never replaces them. [C12]

**Narrowed from v0.2.** "Calibrated against root outcomes" means against *explicit* root judgments. A root case that vests by silence supplies a protocol-default label, not a human one (§15.3).

The four concerns remain distinct: purpose, assessment, accounting, learning.

---

## 2. Participants, time, and notation

### 2.1 Participants (unchanged)

Requesters: a **root requester** is a human, or a system acting for a human with a delegated budget; a **derived requester** is an actor needing work from another actor while executing its own commitment. Actors offer and execute work and serve as reviewers in rotation. The orchestrator holds the pool, selects, assigns verification and audits, holds escrow, and rules when needed — a judge and an escrow, not a bank and not a first-line reviewer. [C2, C10, C12]

Every request carries $\operatorname{root}(q)$. A rootless actor-initiated request is a proposal until a root requester sponsors it. [C12]

### 2.2 Time, capacity, and order within a tick

**Agreed (unchanged).** Discrete global time $t\in\mathbb N_0$; one ordinary commitment per actor; an actor is *committed* from award until it has responded to its initial verdict, then *pending* — capacity free, guarantee locked — until the case vests (v0.2 §2.2).

**Provisional default (new).** Events at tick $t$ are processed in this order:

1. Challenges and disputes filed with timestamp $\le t$ are admitted.
2. Deadlines are checked: delivery ($\tau$), response ($T_{\mathrm{resp}}$), revision ($T_{\mathrm{rev}}$), evidence ($T_{\mathrm{evid}}$), review ($T_{\mathrm{review}}$), nested wait ($T_{\mathrm{wait}}$).
3. Vesting checks: a case whose window has closed and that has no open challenge or audit vests.
4. Settlements and transfers for everything that vested or finalized in steps 1–3.
5. Rotation handovers (§13).
6. Assignments and awards: reviews and audits first, then nested requests when the pool is thin, then root requests.

A challenge filed at $t$ is therefore admitted before the same tick's vesting check. Two events of the same kind at the same tick are ordered by ledger record position (§14).

### 2.3 Notation carried over

v0.2 §2.3–2.4 stand, with these additions and replacements:

| Symbol | Meaning |
|---|---|
| $\tau_{iq}$ | Delivery time committed in the bid, in ticks after award |
| $T_{\mathrm{review}}$ | Review deadline, in ticks after assignment |
| $\mathrm{Reimb}_q$ | Total reimbursement paid on case $q$ |
| $e_v$ | Emission allocated to vested review $v$ |
| $\Omega_t$ | Orchestrator operating account, funded by $\omega$ |
| $\mathcal R_t$ | Review-eligible duty actors: idle, on duty, with $U_j\ge G^V$ |
| $n_{\mathrm{flight}}(\operatorname{root})$ | Number of in-flight (committed) nodes in a root's delegation tree |

$C_{iq}$ (v0.2 §4.6) continues to include nested payments and, now, kill fees paid by $i$.

---

## 3. Request fulfillment and evidence

### 3.1 What is assessed (unchanged)

Semantic fit between request and result in context; criteria from the request, not invented retroactively; vocabulary $\{\mathsf N,\mathsf P,\mathsf F,\bot\}$.

### 3.2 The actor bears the burden of verifiability (unchanged)

A submission carries its evidence. An unverifiable submission is an actor failure. $\bot$ is a substantiated, appealable claim naming the missing evidence; the actor has $T_{\mathrm{evid}}$ to supply it, the same reviewer resumes, and a $\bot$ overturned on appeal is a reviewer failure. [C10]

**Narrowed from v0.2.** Evidence makes the *properties it exercises* mechanically checkable — a passing test establishes what that test checks. It does not convert a semantic request into a mechanical one unless every criterion of the request is itself mechanically checkable. The class a case falls in is a property of the request's criteria, not of the presence of evidence (§15.4).

### 3.3 Preserve the basis (unchanged)

---

## 4. Money: where it enters, where it goes

### 4.1 Money enters with requests (unchanged)

A root requester pays in real value; the system issues credits against it. A derived requester pays from its wallet. Every credit traces to a root pay-in or to emission. The orchestrator does not print on demand. [C9, C12]

On award of $q$ at delivery price $B$:

$$\text{pay-in}_q=B+\varphi_q+\omega_q.$$

$B$ is paid to the actor at vesting. $\varphi_q$ is the case's **verification deposit** (§4.3). $\omega_q$ goes to the operating account $\Omega$.

### 4.2 Emission funds verification (unchanged)

A fixed, decaying schedule $E_t$ is distributed only to reviews that vest in the period, weighted by role. Requester deposits take over as emission decays. [C9, C11]

**Provisional default.** $E_t=E_0\cdot2^{-t/H}$, $E_0=10$, $H=1000$; a period is one tick. Emission with no vesting reviews carries forward. Total scheduled emission is $E_0/(1-2^{-1/H})\approx1443\,E_0$; its scale relative to $M_0$ is a calibration question (§18.2).

**Consequence.** Emission mints claims on the same reserve; it does not add real resources. A verification subsidy in credits is a redistribution of the reserve's purchasing power, not new purchasing power.

### 4.3 The verification deposit and the derived fee

**Agreed (revised from v0.2).** $\varphi_q$ funds the case's verification. It is drawn down in this order:

1. **Reimbursements at completion** — each reviewer's $\min(\widetilde C^V_{jv},K_r)$ is paid from $\varphi_q$ when the review completes.
2. **Shortfall at completion** — if $\varphi_q$ is exhausted, the reimbursement is advanced from $\Omega_t$; if $\Omega_t$ cannot cover it, it is deferred to vesting.
3. **At vesting** — the case's fee pool is formed: $\mathrm{pool}_q=(\varphi_q-\mathrm{Reimb}_q)^+ +\sum_{v\in\mathrm{Vest}(q)}e_v$, where $e_v=\dfrac{w_{r(v)}}{\sum_{v'\in\mathrm{Vest}_t}w_{r(v')}}E_t$. Deferred reimbursements and $\Omega$ advances are repaid from the pool first.
4. **Fees** — the remainder is paid to the vested reviewers of $q$: each receives its own $e_v$ plus an equal share of $(\varphi_q-\mathrm{Reimb}_q)^+$ net of repayments.

A reviewer whose verdict was overturned receives no fee; its emission share is not minted for it, and its deposit share passes to the surviving reviewers of the case.

**Formalization (no shortfall).**

$$f_{jv}=e_v+\frac{(\varphi_q-\mathrm{Reimb}_q)^+}{\lvert\mathrm{Vest}(q)\rvert}.$$

**Provisional default.** $\varphi_q=2K=10$ for root requests — one initial review and one audit at cap. $\varphi_q=0$ for nested requests (the requester judges; §9). $\omega_q=0.05\,B$. $w_{\mathrm{ordinary}}=1$, $w_{\mathrm{appeal}}=w_{\mathrm{audit}}=1.5$. An unused deposit is returned to the requester at vesting.

**Consequence.** The deposit, not "the orchestrator pays," is the funding source for reimbursement. $\Omega$ is a float, not a source: every advance is repaid from the case that drew it.

### 4.4 Floating prices: a backed credit

**Provisional default (unchanged mechanism).** $v_t=\mathrm{Res}_t/M_t$. Root pay-in mints against reserve (neutral). Resource purchase burns $p_r(t)=c_r/v_t$ credits and pays $c_r$ from reserve (neutral). Emission mints against nothing ($v_t$ falls). Forfeited bonds are burned ($v_t$ rises). Guarantees and kill fees transfer (neutral).

**Corrected from v0.2.** With no new root pay-in, the reserve never rises and falls only through resource purchases. An idle economy drains nothing: $v_t$ stays bounded below by $\mathrm{Res}_t/(M_t+\text{remaining emission})>0$. A *busy* economy with no human at the root — actors buying inference to serve each other — spends real backing with nothing replenishing it, so $\mathrm{Res}_t\to0$ and $p_r\to\infty$. That is the halt, and it is the right one: idle costs nothing; busywork is self-terminating. The plug is held by the root-request rule and the interruption rules (§15), with the reserve as the backstop.

### 4.5 Nominal thresholds are indexed (unchanged)

### 4.6 Execution cost (unchanged, plus kill fees)

---

## 5. Offers, selection, and guarantees

### 5.1 The bid

**Agreed (revised).** The bid commits to price **and time**:

$$b_{iq}=(B_{iq},\tau_{iq},G_{iq},\text{terms}),\qquad B_{iq}\le\beta_q.$$

$\tau_{iq}$ is the delivery time in ticks after award. Missing it is nonfulfillment (§6). An actor that may need to subcontract prices sourcing risk into both $B$ and $\tau$.

**Clarified.** $\beta_q$ is the requester's maximum *delivery price*. The requester is shown the all-in maximum $\beta_q+\varphi_q+0.05\,\beta_q$ before posting.

### 5.2 Selection (unchanged)

$$i^*\in\arg\max_{i\in\mathcal I_q(t),\;B_{iq}\le\beta_q}\Big[S_\theta(q,h_t^O,b_{iq},\rho_i(t))-\lambda\,\tfrac{B_{iq}}{\beta_q}\Big],$$

ties within a band broken by vested duty credit $\kappa_i$. $S_\theta$ reads $\rho_i$, $\tau_{iq}$ and the ledger; never $\kappa_i$. **Provisional default.** $\lambda=0.2$, band $0.05$.

### 5.3 Guarantee (unchanged)

$G_{iq}=\lceil0.5B_{iq}\rceil$, minimum 1; released at vesting; forfeited to the requester on final $\mathsf N$; a reduced fraction on pool-exhaustion withdrawal (§9.4).

---

## 6. Task lifecycle: committed, pending, vested

| Stage | What happens | Capacity | Funds |
|---|---|---|---|
| Available | $q\in\mathcal P_t$ | — | — |
| Award | Escrow funded; $G$ locked; delivery deadline $t_0+\tau$ set | Committed | $G$ locked |
| Executing | Work, delegation (§9), revision | Committed | — |
| Submitted | Result and evidence recorded by the deadline | Committed | — |
| Initial verdict | $\mathsf F/\mathsf N/\mathsf P/\bot$ | Committed until response | — |
| Pending | Window $W$ runs from the verdict; audit or dispute may open | **Released** | $G$ locked |
| Suspended | A challenge or audit is open; the window does not close | Released | $G$ locked |
| Vested | Window closed, nothing open, verdict standing | Free | $B$ paid; $G$ released; deposit remainder and fees settled |
| Final $\mathsf N$ | Deadline missed, rejection accepted, appeal lost, or dispute upheld | Free | $P^{\mathrm{fail}}=0$; $G$ forfeited |

**Agreed (new).** A missed delivery deadline is final $\mathsf N$ with full forfeiture. It is mechanical and not appealable. A delivery before the deadline that is later rejected follows the ordinary path.

**Agreed (new).** Vesting occurs at $\max(t_0+W,\ t_{\mathrm{resolve}})$, where $t_0$ is the initial verdict and $t_{\mathrm{resolve}}$ the resolution of any challenge or audit opened inside the window. A challenge filed at $t\le t_0+W$ is admitted; one filed later is not (§2.2 step 1 precedes step 3).

**Agreed (new).** Vesting is **financial finality**. Released funds are not clawed back by any later event. What a later event can change is stated in §15.2.

Responses to the initial verdict, the $\mathsf P$ revision rule, and the $\bot$ path are as in v0.2 §6. **Provisional default.** $W=10$, $T_{\mathrm{resp}}=2$, $T_{\mathrm{rev}}=5$, $T_{\mathrm{evid}}=3$.

```text
award ──► execute ──► submit by t0+τ ──► initial verdict at t0
  │ (miss deadline → final N)                 │
  │                                           ├─ F ──► pending ──┬─ audit opens ───────┐ suspend until
  │                                           │                  ├─ dispute opens ─────┤ resolved, then
  │                                           │                  └─ silence ───────────┤ vest at
  │                                           ├─ N ──► appeal ──► 2 fresh ──► ruling ──┤ max(t0+W, t_resolve)
  │                                           ├─ P ──► one revision ──► F / N ─────────┤
  │                                           └─ ⊥ ──► evidence / appeal / accept N ───┤
  │                                                                                    ▼
  └────────────────────────────────────────────────────────────────────► VEST (financial finality)
```

---

## 7. Verification: eligibility, bond, compensation, deadline

### 7.1 Roles and eligibility

Roles as in v0.2 §7.1; $m_0=1$ at root, $0$ nested.

**Agreed (new).** A duty actor is *review-eligible* only if it can fund the bond: $U_j\ge G^V$. The eligible set for a case is $\mathcal E_{q,r}(t)\subseteq\mathcal R_t$. An actor on duty that cannot fund a bond is counted in the reserve but cannot be assigned, and the orchestrator records the shortfall (§12).

### 7.2 The reviewer bond is the reviewer's total liability

**Agreed (revised).** Taking a review locks $G^V$ for the life of the verdict. If the verdict is overturned:

- any court fee the winning challenger paid is reimbursed **from the bond**;
- the remainder of the bond is burned.

If the verdict stands, the bond is released at vesting. $G^V\ge D$ by construction, so an overturned reviewer never owes more than it has locked. An overruled *appeal* reviewer forfeits its bond entirely; it owes no court fee. Liability is symmetric for a wrong $\mathsf F$ and a wrong $\mathsf N$. [C10]

**Provisional default.** $G^V=5$, indexed; $D=2$.

### 7.3 Compensation: reimbursement from the deposit, fee at vesting

**Agreed (revised).** $\Pi_{jv}=\min(\widetilde C^V_{jv},K_r)$ at completion, paid from $\varphi_q$ under §4.3, plus $f_{jv}\cdot\mathbb 1[\text{vested}]$ at vesting. **Provisional default.** $K=5$ for all roles.

### 7.4 What the rules do and do not establish about careless review

**Withdrawn from v0.2.** The claim that a reviewer who approves without reading is negative in expectation does not follow from the rules; an unexamined approval that survives earns its fee like any other.

**Hypothesis.** Let $\bar f$ be the reviewer's expected fee on a surviving verdict, $p$ its audit rate, $b$ the base rate of submissions that fail on examination, and assume audits catch every failed submission. A reviewer who approves everything expects

$$\mathbb E[\Delta W]=(1-pb)\,\bar f-pb\,G^V,$$

which is negative only when $G^V>\bar f\,(1-pb)/(pb)$. At $p=0.5$, $b=0.2$, $\bar f=2$: $+1.3$ with $G^V=5$; deterrence needs $G^V>18$. At the floor $p=0.2$: $+1.72$; deterrence needs $G^V>48$. Monetary deterrence therefore holds, if at all, only at high audit rates. At lower rates the deterrent is **reliability**: an overturn lowers $\rho_i$, which lowers future awards. Whether the combined effect makes careless review unattractive is the first question the simulation answers (§18.2). Rating does not change by whether the verdict was $\mathsf F$ or $\mathsf N$.

A verdict that survives its window is *procedurally settled*. That is not the same as *correct*, and the record keeps the two apart (§15.3).

### 7.5 Review deadline

**Agreed (new).** A review not completed within $T_{\mathrm{review}}$ ticks of assignment is withdrawn: the reviewer's bond is half burned, its reliability drops, it receives no reimbursement for that assignment, and the case is reassigned to the next eligible actor. **Provisional default.** $T_{\mathrm{review}}=5$.

### 7.6 Assignment and waiting (unchanged)

Volunteers first, then round-robin over $\mathcal E_{q,r}(t)$, otherwise wait.

---

## 8. Challenges: appeal, requester dispute, and audit

One challenge round per case. A dispute consumes it; an audit that disagrees with the original verdict consumes it; an audit that agrees does not.

### 8.1 Appeal by the actor (unchanged in flow)

Pay $D$, submit $d_q$, two fresh reviewers, orchestrator rules on a split. Overturned: $G$ released at vesting; $D$ reimbursed from the original reviewer's bond; that reviewer's remaining bond burned, reliability down, audit rate doubled. Upheld: $G$ forfeited; $D$ borne by the actor. Matching appeal verdicts settle without the orchestrator.

### 8.2 Dispute by the requester (unchanged in flow)

Within the window, on the same terms. Upheld: the approving reviewer's bond pays $D$ and the rest burns; final $\mathsf N$ for the actor. Rejected: the requester bears $D$; the case vests.

### 8.3 Audit of approvals

**Agreed (unchanged).** Blind audits of $\mathsf F$ verdicts, assigned by the orchestrator, performed by a fresh reviewer that receives $(q,y_q)$ only. The original verdict is committed before assignment (§14). Agreement: a second vested review. Disagreement: the audit verdict stands as one appeal review, one more fresh reviewer is assigned, the orchestrator rules on a split.

**Agreed (new).** Opening an audit suspends vesting (§6). If a requester dispute opens while an audit is in progress or after it has completed in agreement, the audit verdict stands as one of the two dispute reviews and one more fresh reviewer is assigned; the case still consumes at most three distinct reviewers. If the audit already disagreed, the challenge round is in use and a further dispute is not admitted.

**Provisional default.** $p_j$ starts at $0.5$; halves after every 5 consecutive vested verdicts, **floor $0.2$**; doubles on any overturn, cap $0.5$.

### 8.4 Final authority (unchanged)

---

## 9. Delegation: nested requests

### 9.1 A nested request is a full loop

**Agreed (unchanged).** $A$ posts $q'$ with $\operatorname{root}(q')=\operatorname{root}(q)$, funded from its unlocked balance; $B$ locks its guarantee; $A$ is the requester and its judgment is the initial verdict ($m_0=0$, $\varphi_{q'}=0$). [C12]

**Clarified (one milestone).** $A$ may submit $q$ only after every nested request it posted has reached its **initial verdict** — $A$ has accepted, rejected, cancelled (§9.3), or withdrawn it. Nested vesting is independent and may complete after the parent submits; the parent bears that risk (§9.2).

**Narrowed from v0.2.** The root pointer forbids *rootless* requests. It does not forbid unnecessary nested ones. What constrains unnecessary nesting is that $A$ pays for every nested award out of its own margin $B_{Aq}-C_{Aq}$: delegation that does not reduce $A$'s cost reduces $A$'s profit.

### 9.2 Accountability cascades — with one stated exception

**Consequence (unchanged).** $B$'s guarantee is to $A$. If $A$ delivers bad work built on $B$'s bad work and did not catch it, $A$ forfeits upstream with no recourse. If $A$ catches it, $B$ forfeits to $A$; $B$ may appeal. [C12]

**Exception (made explicit).** $A$'s guarantee secures **one obligation**: delivery of $q$ to its requester. $A$'s verdicts on nested results are *not* bonded. An acceptance overturned by audit forfeits $B$'s guarantee to $A$ and lowers $A$'s reliability; it imposes no separate monetary loss on $A$. $A$'s monetary exposure to a careless nested acceptance is whatever flows through its own delivery. This is a deliberate departure from paid-reviewer liability, chosen so that one guarantee is never pledged to two obligations.

### 9.3 Self-execution is always an exit — with an award boundary

**Agreed (rule, unchanged).** $A$ may perform nested work itself at its own cost whenever that is possible.

**Agreed (new).** *Before* $q'$ is awarded, $A$ withdraws it freely. *After* award, $A$ may cancel $q'$ by paying $B$ a **kill fee** equal to $B$'s reimbursable cost to date, $\min(\widetilde C_{Bq'},K)$; $B$'s guarantee is released, $B$ receives no delivery price, and $B$'s reliability is unaffected. The cancellation is recorded. The kill fee counts in $C_{Aq}$.

### 9.4 When the pool is thin

**Agreed (unchanged in substance).** A thin pool is $A$'s risk and is priceable at bid time. If $q'$ has been open and unawarded for $T_{\mathrm{wait}}$ ticks and $A$ cannot self-execute, $A$ may withdraw its commitment to $q$ as *pool-exhaustion nonfulfillment*: $\rho_{\mathrm{pool}}G_{Aq}$ forfeited, the rest released, $P^{\mathrm{fail}}=0$. Nested requests are awarded before root requests when the pool is thin. [C12]

**Consequence (new).** $T_{\mathrm{wait}}$ must be shorter than the delivery times actors commit to, or the reduced-forfeiture exit can never be reached before an ordinary deadline miss. If the deadline arrives first, it is an ordinary missed delivery.

**Provisional default.** $T_{\mathrm{wait}}=5$ (was 20); $\rho_{\mathrm{pool}}=0.25$; thin $=$ at most 2 free ordinary-eligible actors.

### 9.5 Capacity accounting (corrected)

**Consequence.** A delegation tree commits $n_{\mathrm{flight}}(\operatorname{root})$ actors — its in-flight nodes — not its depth. A chain of depth $d$ is the special case $n_{\mathrm{flight}}=d$. The reserve (§12) guards verification capacity; §9.3–9.4 guard delegation capacity.

---

## 10. Wallet accounting and settlement

### 10.1 Locks and escrow (unchanged)

### 10.2 Actor settlement

$$\Delta W^{\mathrm{case}}_{iq}=P_{iq}-C_{iq}-I_DD_q+I_WD_q-I_NG_{iq}-I_{\mathrm{pool}}\,\rho_{\mathrm{pool}}G_{iq},\qquad I_N+I_{\mathrm{pool}}\le1.$$

$I_N=1$ on any final $\mathsf N$ including a missed deadline; $I_{\mathrm{pool}}=1$ only on a §9.4 withdrawal, which is not an $I_N$ event. $I_WD_q$ is paid from the liable reviewer's bond. $C_{iq}$ includes nested payments and kill fees. $P^{\mathrm{fail}}=0$.

### 10.3 Reviewer settlement

$$\Delta W^V_{jv}=\min(\widetilde C^V_{jv},K_r)-C^V_{jv}+I_{\mathrm{vest}}\,f_{jv}-I_{\mathrm{over}}\,G^V-I_{\mathrm{late}}\,\tfrac12G^V.$$

Court-fee reimbursement is inside $I_{\mathrm{over}}G^V$: of a forfeited bond, $D_q$ goes to the winning challenger if one paid a fee, the rest is burned. The liable reviewer is the one whose verdict was challenged; overruled appeal reviewers forfeit the bond and owe no fee. A challenger is reimbursed at most once.

### 10.4 Escrow and operating account

Per root request: in $=B+\varphi+\omega$. Out: $B$ to the actor at vesting; reimbursements from $\varphi$ at completion; fees and any deposit remainder at vesting; $\omega$ to $\Omega$. Shortfalls follow §4.3. Court fees pass from challenger to winner or stay with the loser. Emission is minted into fees. Forfeited guarantees go to the requester; forfeited bonds, after any court-fee reimbursement, are burned. Kill fees are transfers.

$\Omega$ receives $\omega$, advances reimbursements under §4.3, and is repaid from case pools. If $\Omega$ and a case pool together cannot cover a deferred reimbursement, the reviewer holds a claim against $\Omega$ settled from the next $\omega$ receipts, first in, first out. This is the one place the loop can carry debt, and it is bounded by $K$ per review.

---

## 11. Reliability and duty credit

### 11.1 Two counters (unchanged)

$\rho_i$ from settled outcomes only — survived up, overturned or failed down, including missed deadlines and withdrawn reviews — input to $S_\theta$ and audit rates. $\kappa_i$: $+1$ per vested review; never an input to $S_\theta$. **Provisional default.** $\rho_i=(s_i+1)/(s_i+o_i+2)$ over 100 settled outcomes; $\kappa_i$ over 100 ticks.

### 11.2 Credit vests on survival (unchanged)

### 11.3 Duty credit buys privileges (corrected)

$\kappa_i$ breaks ties in selection, reduces conscription, and releases first from duty. **Correction:** $\kappa_i$ is *not* an emission weight. Emission is allocated by role weight $w_r$ (§4.3); $\kappa_i$ counts the same vesting events. The currency reward and the privilege reward vest on the same event; they are not the same formula.

---

## 12. Protected verification capacity

**Agreed (unchanged).** $\lvert\mathcal V_t\rvert\ge X$, $X>V_{\max}=3$, $X=4$.

**Agreed (new).** Two counts are kept: reserve membership $\lvert\mathcal V_t\rvert$ and the review-eligible idle subset $\lvert\mathcal R_t\rvert$. The invariant is on the first. When $\lvert\mathcal R_t\rvert<V_{\max}$, the orchestrator records a *working-capital shortfall*; cases wait as under §7.6. Reserve membership is a capacity statement; eligibility is a solvency statement, and the reserve does not guarantee the second. The cold-start float (§19) is sized so the initial reserve is eligible.

---

## 13. Rotation of verification duty (unchanged)

Replacement-before-release; duty turn 3 vested reviews or 30 ticks; incoming replacements are the free actors with the lowest $\kappa_i$; volunteers may stay.

---

## 14. Verifiable history and trust boundary

**Agreed (unchanged).** Append-only past, committed present, mutable future; trusted recording authority; integrity is not truth.

**Corrected from v0.2.** Committing a verdict before an audit is assigned establishes *ordering*: the verdict cannot be changed after the audit begins. It does not by itself hide the verdict. **Blindness is a visibility rule:** an auditor's view of the ledger excludes the verdicts, challenge records, and reviewer identities of the case it is auditing, and the auditor is not told whether an assignment is an initial review or an audit. Whether other channels leak that information is an implementation concern outside the ledger's guarantee.

---

## 15. The human in the loop

### 15.1 The battery (narrowed)

Human root requests supply value and explicit judgment. With no root request pending and no in-flight tree, the correct state is idle. A busywork economy — actors serving each other with no human at the root — is forbidden at the pool boundary by the root-pointer rule, made unprofitable inside a tree by §9.1, and self-terminating at the reserve by §4.4. None of these establishes that every nested request was necessary. [C12]

### 15.2 The plug (made specific)

**Agreed (unchanged).** The human may dispute an approval, request an audit, override a ruling, or freeze awards; each is a recorded human event. Silence inside the window is protocol-default acceptance.

**Agreed (new).** The financial effect of an override depends on when it lands:

- *Before vesting:* the override is the ruling. Settlement follows it.
- *After vesting:* funds already released are not clawed back. The override (a) changes the recorded outcome and its label grade, (b) adjusts the reliability of the actor and reviewers involved as if the verdict had been overturned, and (c) may create a **corrective obligation** — a new root request, funded by the human, to repair the result. The original actor's bond and guarantee are not touched; its reliability is.

Human review of split-appeal rulings remains an agreed direction with open cadence.

### 15.3 Label grades

**Agreed (new).** Every settled case carries exactly one label grade, and nothing promotes between grades:

| Grade | Established by |
|---|---|
| **Human-explicit** | A human accepted, disputed, or overrode |
| **Delegate-explicit** | A system holding a delegated human budget accepted or disputed |
| **Protocol-default** | The window closed in silence |
| **Procedural** | A verdict vested, or the orchestrator ruled, with no root judgment |

Only the first grade is a human judgment. The second is a delegate's. The third records that no one objected. The fourth records that the procedure accepted an outcome. "Survived" and "correct" are different descriptions at every grade.

### 15.4 Two classes of verification (narrowed)

For a request whose criteria are *all* mechanically checkable, reviewer agreement is meaningful and verification is cheap. For any other request, reviewer agreement is correlated opinion and a human-explicit label is what anchors it. §3.2 moves *properties* into the first class; it moves a *request* there only when nothing semantic remains.

---

## 16. Worked example

Illustrative; $\omega$ omitted. Actors A–F; C, D, E, F on duty ($X=4$), each with $U\ge5$ so all are review-eligible. Root requester H.

**Setup.** H posts $q$ with $\beta=45$ (all-in shown: $45+10+2.25$). A bids $B=40$, $\tau=8$, locks $G=20$. H pays $40+10=50$ into escrow ($\varphi=10$). A's own execution costs 12. A posts nested $q'$ with $\beta'=6$; B bids $B'=5$, $\tau'=3$, locks $G'=3$; A escrows 5; $\varphi'=0$. B's execution costs 3. C and D each cost 3. This period's emission works out to 2 credits per unit of role weight.

| Tick | Event | Capacity |
|---|---|---|
| 0 | A awarded; H escrows 50; A locks 20; delivery due by 8 | A committed |
| 1 | A posts $q'$; B awarded; A escrows 5; B locks 3; due by 4 | A, B committed |
| 1–3 | B executes (cost 3), submits with evidence | — |
| 3 | A judges $\mathsf F$ — initial verdict of $q'$; B pending; $q'$ window to 13 | B released |
| 1–4 | A executes own part (cost 12); submits $q$ at 4 (deadline 8) | — |
| 4–6 | C assigned (deadline 9): locks bond 5; cost 3 reimbursed **from $\varphi$** at 6; verdict $\mathsf F$ at 6 | A pending from 6; window to 16 |
| 6 | Audit rolled at $p_C=0.5$: D assigned, blind; vesting suspended | D busy on duty |
| 6–8 | D: bond 5, cost 3 reimbursed from $\varphi$; $\mathsf F$; agrees; suspension lifted | — |
| 13 | $q'$ vests: B paid 5 from A's escrow; $G'$ released | — |
| 16 | $q$ vests, H silent (protocol-default): A paid 40, $G$ released; deposit remainder $10-6=4$ split 2/2; emission C 2, D 3; bonds released; $\kappa_C,\kappa_D$ +1 | — |

**A** (start 60): lock 20 → $U=40$; escrow 5 → $U=35,\ L=25$; cost 12 → $U=23,\ W=48$; escrow paid to B at 13 → $L=20,\ W=43$; receive 40 at 16 → $U=63,\ W=83$; release 20 → $U=83$. Net $+23=40-(12+5)$.

**B** (start 20): lock 3; cost 3 → $W=17$; receive 5 → $W=22$; release 3 → $U=22$. Net $+2$.

**C** (start 30): bond 5 → $U=25$; cost 3 → $U=22,\ W=27$; reimbursed 3 from $\varphi$ → $W=30$; vest: deposit share 2 + emission $2\times1=2$ → $W=34$; bond released → $U=34$. Net $+4$.

**D** (start 30): same to $W=30$; vest: deposit share 2 + emission $2\times1.5=3$ → $W=35$. Net $+5$.

**Escrow for $q$:** in 50; out $40$ (A) $+6$ (reimbursements C, D) $+4$ (deposit remainder as fees) $=50$. Emission minted: 5. $\Omega$ untouched.

**Variant — rejection and appeal.** At 6, C returns $\mathsf N$. A appeals at 7, pays $D=2$; E and F are assigned (deadline 12), each costs 3, reimbursed from $\varphi$ (now $10-3-3-3=1$ remaining); both $\mathsf F$ at 10; settled without the orchestrator. Vesting at $\max(16,10)=16$. A: $+23$, the court fee reimbursed from C's bond. C: reimbursed 3, cost 3, bond forfeited — 2 to A, 3 burned — net $-5$; reliability down; $p_C$ doubles. E and F vest at appeal weight 1.5 and split the deposit remainder of 1; C gets no fee.

**Variant — pool exhaustion.** At 1, no actor takes $q'$ and A cannot self-execute. $T_{\mathrm{wait}}=5$ elapses at 6, before A's deadline at 8: A may withdraw; forfeits $0.25\times20=5$ to H, 15 released; H's escrow returned including the unused deposit. A nets $-12-5=-17$ if it had already spent 12. Had A bid $\tau=4$, the deadline would have arrived first and the miss would have been an ordinary final $\mathsf N$ with full forfeiture.

**Variant — cancellation.** At 2, A decides to self-execute $q'$ after B has spent 2. A cancels: pays B a kill fee of $\min(2,5)=2$ from its escrow (the other 3 returned to A), B's $G'$ released, B unmarked. A's $C_{Aq}$ now includes the 2.

---

## 17. Rule and invariant checklist

Carried from v0.1 and v0.2 unchanged: R01–R04, R07, R10, R11, R14, R19, R21–R24, R26, R06′, R08′ (with the exclusivity below), R12′, R14, R18′, R20′, R27–R31, R33–R36. Revised or new:

| ID | Rule | Status |
|---|---|---|
| R09″ | Committed until the actor responds to its initial verdict; pending until vesting; suspended while a challenge or audit is open. | Consequence |
| R13″ | A winning challenger is reimbursed $D$ **from the liable reviewer's bond**, once. | Agreed |
| R15″ | The reviewer bond is the reviewer's total liability: court fee from it, remainder burned. $G^V\ge D$. | Agreed |
| R16″ | Reimbursement is paid from the case's verification deposit at completion; the fee from the deposit remainder plus emission at vesting; shortfalls follow the §4.3 order. | Agreed |
| R17″ | $\varphi_q$ is a deposit sized to expected verification cost, not a percentage of $B$. | Provisional |
| R32′ | A nested request reaches its initial verdict before the parent submits; nested vesting is independent. | Agreed |
| R37 | Vesting is financial finality; a post-vesting override changes the record and may create a corrective obligation, never a clawback. | Agreed |
| R38 | A challenge or audit opened inside the window suspends vesting until resolved. | Agreed |
| R39 | Review eligibility requires $U_j\ge G^V$; reserve membership and eligibility are separate counts. | Agreed |
| R40 | One guarantee secures one obligation; nested verdicts are not bonded (explicit exception). | Agreed |
| R41 | Post-award cancellation of a nested request pays a kill fee of the subcontractor's capped cost; pre-award withdrawal is free. | Agreed |
| R42 | The bid commits a delivery time; a missed deadline is final $\mathsf N$, not appealable. | Agreed |
| R43 | A review not completed by its deadline is withdrawn and reassigned; half the bond burns. | Agreed |
| R44 | Every settled case carries one of four label grades; nothing promotes between grades. | Agreed |
| R45 | Emission is weighted by role; duty credit is a count, not a weight. | Correction |
| R46 | $I_N$ and $I_{\mathrm{pool}}$ are mutually exclusive. | Correction |
| R47 | Tick-internal order: challenges, deadlines, vesting, settlement, rotation, assignment. | Provisional |

**Invariants to test:** locks, escrows and kill fees never change total $W$; emission is the only unbacked mint; burned bonds and resource purchases are the only burns; every reimbursement has a named source in the §4.3 order and $\Omega$ advances are repaid; a court fee is reimbursed at most once and never exceeds the bond; no reviewer owes more than its locked bond; a verdict's commit precedes its audit assignment; a challenge filed inside the window is admitted before that tick's vesting check; no case vests with an open challenge or audit; a nested loop reaches its initial verdict before its parent submits; no case consumes more than $V_{\max}$ distinct reviewers; the reserve never dips below $X$ during a handover; no funds move after vesting on account of that case.

---

## 18. Provisional defaults, hypotheses, and remaining opens

### 18.1 Provisional defaults ($t=0$ credits, indexed)

| Parameter | Default | Where |
|---|---|---|
| $P^{\mathrm{fail}}$ | 0 | §6 |
| $\mathsf P$ handling | one revision, same reviewer | §6 |
| $W$ / $T_{\mathrm{resp}}$ / $T_{\mathrm{rev}}$ / $T_{\mathrm{evid}}$ / $T_{\mathrm{review}}$ | 10 / 2 / 5 / 3 / 5 ticks | §6, §7.5 |
| $G_{iq}$ | $\lceil0.5B\rceil$, min 1 | §5.3 |
| $G^V$ / $D$ | 5 / 2 | §7.2 |
| $K$, all roles | 5 | §7.3 |
| $\varphi$ root / nested | 10 ($=2K$) / 0 | §4.3 |
| $\omega$ | 5% of $B$ | §4.1 |
| $m_0$ | 1 root / 0 nested | §7.1 |
| $X$ | 4 | §12 |
| $\lambda$ / tie band | 0.2 / 0.05 | §5.2 |
| $E_0$ / $H$ | 10 per tick / 1000 ticks | §4.2 |
| $w$: ordinary / appeal / audit | 1 / 1.5 / 1.5 | §4.3 |
| $p_j$ | start 0.5; halve per 5 survivals, **floor 0.2**; double on overturn, cap 0.5 | §8.3 |
| $\rho_i$ / $\kappa_i$ windows | 100 outcomes / 100 ticks | §11.1 |
| Duty turn | 3 vested reviews or 30 ticks | §13 |
| $T_{\mathrm{wait}}$ / $\rho_{\mathrm{pool}}$ / thin | **5** / 0.25 / ≤ 2 free | §9.4 |
| Tick order | challenges, deadlines, vesting, settlement, rotation, assignment | §2.2 |

### 18.2 Hypotheses the simulation must test

1. **Deterrence (§7.4).** Does reliability loss plus the monetary term make careless approval unattractive at $p$ between 0.2 and 0.5, and at what $G^V$? If not, which of $p_{\min}$, $G^V$, or $\bar f$ moves it?
2. **Price pressure.** Does $\lambda=0.2$ produce competition without starving reliable actors?
3. **Verification funding.** At realistic review volume, does $\varphi=2K$ cover reimbursements, and how often does $\Omega$ advance? Is the emission scale (total $\approx1443\,E_0$ against $M_0$) a subsidy or a flood?
4. **Delegation liveness.** Do $X=4$, $T_{\mathrm{wait}}=5$, the kill fee and nested-first priority keep trees of 2–4 nodes moving, and how often is pool-exhaustion withdrawal taken?
5. **Reserve solvency.** How often does $\lvert\mathcal R_t\rvert<V_{\max}$ occur, and does it self-correct through fees?
6. **Monetary behavior.** How does $v_t$ move under a varying human request rate, and does busywork actually terminate at the reserve?
7. **Dominant strategies.** Does any role have a cheap strategy the rules above missed?

### 18.3 Remaining opens, off the critical path

Physical tick duration; evaluator choice and calibration; $S_\theta$ implementation; identity and sybil resistance; collusion between actor and reviewer or across nested pairs; insolvency beyond the bounded $\Omega$ claim; wealth concentration; the real-value exchange mechanics behind $\mathrm{Res}_t$; human review cadence for rulings; multi-verifier liability if $m_0>1$ is ever used; multi-round revision; long-horizon tasks spanning many windows; what a corrective obligation (§15.2) costs the human beyond the new request's price.

---

## 19. Initialization

**Provisional default (new).** A run begins with:

| Quantity | Value | Note |
|---|---|---|
| $v_0$ | 1 | Convention: one credit equals one real unit at $t=0$ |
| $\mathrm{Res}_0$ | 10,000 real units | Paid in by a sponsor, who is the first root requester |
| $M_0$ | 10,000 credits | Minted against $\mathrm{Res}_0$ |
| Actor float | 50 credits per actor | Cold-start subsidy; $\ge G^V+G$ for a modest first bid; paid once, from the sponsor's credits |
| $\Omega_0$ | 20 credits | From the sponsor's credits |
| Sponsor's remaining credits | $M_0-50\lvert\mathcal A_0\rvert-\Omega_0$ | The sponsor's requester budget |
| $c_r$ | Inputs | Real cost per unit of each resource; e.g., inference 1 real unit per unit |
| Initial reserve | $X$ actors, lowest ids | All eligible, since float $\ge G^V$ |
| $\rho_i(0)$, $\kappa_i(0)$ | $0.5$, $0$ | Laplace prior; no credit |
| $p_j(0)$ | $0.5$ | New reviewer |

The actor float is the "small additional budget" first proposed in discussion, placed where it belongs: a one-time cold-start subsidy, not a recurring print. Further human requests are the only ongoing source of backed credits; emission is the only ongoing unbacked one.

---

## 20. Deferred ideas and superseded alternatives

**Superseded in v0.3:** $\varphi$ as a percentage fee (now a deposit sized to verification cost); bond smaller than liability; "stamper negative in expectation" (now a hypothesis); vesting at a fixed window end regardless of open challenges (now suspended); $\kappa_i$ as emission weight; "self-execution at any time" without an award boundary; $T_{\mathrm{wait}}=20$ (now 5, so it can precede a delivery deadline); the audit-rate floor of 0.05 (now 0.2); the "$v_t\to0$" argument (now the reserve-drain argument).

**Still deferred:** insurance; transferable upgrades; explicit bankruptcy beyond the bounded $\Omega$ claim; starting calibration tasks; sold concurrency; reviewer collateral beyond $G^V$; depth or node limits on delegation (not adopted; §9.3–9.4 are the chosen controls); requester-specified $\lambda$; rent; clawback after vesting (rejected in favor of corrective obligations).

---

## 21. Sources and decision provenance

**[C0]–[C8]** as in v0.1. **[C9]–[C12]** as in v0.2.

**[R1] External review of v0.2 (October 15, 2026).** An independent model review that endorsed v0.2's directions — requester funding, contested approvals, delayed vesting, the reliability/duty split, explicit nested contracts, learning outside the core — and identified the inconsistencies resolved above: reimbursement funding; bond versus liability; the §7.4 overclaim; finality under an open challenge and after a human override; the audit/dispute overlap; the double-pledged guarantee; cancellation after award; the limits of the root pointer; the $v_t$ argument; label grades; and the table of corrections (emission weight, court-fee liability, indicator exclusivity, the nested milestone, nodes versus depth, $\beta$, blindness). Its closing advice — add no mechanisms, make the selected ones agree — is the brief this revision followed.

**[M1]** _line — The actor and its economic life, revision 4, unchanged.

**[S1]** LeWorldModel (Maes et al., 2026) — Appendix A only. **[S2]** RFC 9162 — background for §14 only. **[S3]** Optimistic rollups and Bitcoin's subsidy-plus-fees security budget — design analogies, not adopted protocols.

---

## Appendix A. Learning

**Agreed direction (unchanged).** Actors and the orchestrator learn consequences from recorded outcomes. LeWorldModel-style latent dynamics are the initial direction; nothing in the loop depends on it.

**Revised.** The loop supplies per-decision observations and labels at the four grades of §15.3. Training keeps the grades distinct: a human-explicit label is a human judgment; a delegate-explicit label is a delegate's; a protocol-default label records that no one objected; a procedural label records that the procedure accepted an outcome. No training step promotes a lower grade to a higher one, and no label — at any grade — is read as "correct" rather than "accepted." Audit outcomes arrive at a controlled rate and are procedural labels about reviewers. Representation, update schedule, parameter sharing and calibration remain open.

---

## Closing statement

> Requesters pay in — a price, a verification deposit, a service fee — and judge. Actors commit to a price and a time, execute at their own cost, and submit verifiable results. Reviewers post a bond that is their whole liability and earn only when a verdict stands. Approvals are audited blind; rejections are appealable; a challenge inside the window holds the case open until it resolves; vesting is final. Delegation is a full loop with cascading guarantees, an exit by self-execution wherever that is possible, and a kill fee where it is not free. A rotating reserve keeps review capacity out of ordinary commitments, and solvency is tracked beside it. The human powers the circuit and holds the plug; idle costs nothing, busywork burns the reserve. The ledger forgets nothing, and labels say what they are.

Every rule in the loop now agrees with every other rule in it, as far as reading can tell. The next step is to run it.

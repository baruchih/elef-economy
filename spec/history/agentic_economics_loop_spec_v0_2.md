# Agentic Economics — The Task, Verification, and Dispute Loop

## Working specification v0.2

**Project:** Agentic-OS / Agentic Economics  
**Prepared:** October 15, 2026  
**Supersedes:** v0.1 (October 15, 2026). Where this document is silent, v0.1 stands.  
**Discussion boundary:** Through the agreement on delegation rules — self-execution as a guaranteed exit, wait timeout with reduced forfeiture, nested-first award priority, and cascading guarantees.  
**Status:** Agreed conceptual rules plus provisional defaults for every parameter on the critical path. The loop is specified end-to-end and is simulable. It is not an implemented or validated mechanism.

> **The wallet supports the purpose; it does not define the purpose.**
>
> **The actor competes on its promise, is assessed on its delivery, and bears the cost of its execution.**
>
> **The past is append-only. The present is committed. The future is mutable.**
>
> **Money enters with requests. Truth enters with requesters. Verification is the security work of the economy.**
>
> **The human is the battery — and holds the plug.**

### What changed from v0.1

| Area | v0.1 | v0.2 |
|---|---|---|
| Funding | Open; orchestrator pays from "funding received" | Requester pays in; orchestrator is escrow; a fixed emission schedule subsidizes verification |
| Prices | Fixed resource prices | Floating: credits backed by requester pay-in, diluted by emission |
| Price pressure | None (fulfillment-first selection) | Requester maximum price plus a price term in selection |
| Reviewer liability | One-sided: wrong $\mathsf N$ costs $D$, wrong $\mathsf F$ costs nothing | Symmetric: bond on every verdict, blind audits of approvals, requester disputes |
| $\bot$ (cannot assess) | Payable; handling open | A substantiated claim; the actor bears the burden of verifiability |
| Reviewer fee | Fixed $f=2$ | Derived from emission and requester verification fees; paid at vesting |
| Rating | One scalar, $+\epsilon_R$ per completed review | Split: reliability (settled outcomes) and duty credit (vests on survival; a privilege, not a prediction input) |
| Requester | "The user", opaque | Root (human) and derived (actor) requesters; provenance pointer to root |
| Delegation | Subcontracting mentioned | First-class nested loops: self-execute exit, wait timeout, nested-first priority, cascading guarantees |
| Actor release | Stuck until settlement | Capacity released at the initial verdict; funds settle at vesting |
| Learning | §13 in the core | Appendix; the loop is learner-agnostic |
| Critical-path opens | Six unresolved | All assigned provisional defaults (§18) |

### Reading the status labels

| Label | Meaning |
|---|---|
| **Agreed** | A working rule accepted in discussion. A design commitment, not proof the mechanism works. |
| **Consequence** | A rule that follows from agreed rules, recorded so it is not rediscovered. |
| **Provisional default** | A concrete value or mechanism chosen so the loop can run. Expected to change under simulation; changing it is not a design reversal. |
| **Formalization** | Notation or accounting used to express the model. |
| **Open** | Not selected and not on the critical path. |
| **Deferred** | Outside the current core loop; not silently adopted. |

Nominal defaults are stated in credits at $t=0$. Once the credit value floats (§4), nominal thresholds are indexed to it (§4.5).

## Contents

1. Purpose and measurement boundary
2. Participants, time, and notation
3. Request fulfillment and evidence
4. Money: where it enters, where it goes
5. Offers, selection, and guarantees
6. Task lifecycle: committed, pending, vested
7. Verification: assignment, bond, and compensation
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
18. Provisional defaults and remaining opens
19. Deferred ideas and superseded alternatives
20. Sources and decision provenance  
Appendix A. Learning

---

## 1. Purpose and measurement boundary

**Agreed (unchanged).** The actor's purpose is to fulfill requests economically over time. Currency is an instrument. We assess fulfillment of the request in its applicable context; we do not price the outcome's value to the requester's life. The efficiency direction is: fulfill with the least necessary work and resource expenditure. Cheap nonfulfillment is not economical fulfillment; extra work is not automatically better. [C1]

**Agreed (new framing).** The economy has an outside. Human requesters supply two things nothing inside can supply: *value* (they pay in) and *truth* (their acceptance of a root result is the only judgment that is not a model's opinion of another model). Everything internal — reviewers, auditors, the orchestrator — is calibrated against root acceptances and never replaces them. [C12]

The four concerns remain distinct: **purpose** (economical fulfillment), **assessment** (was this request fulfilled), **accounting** (prices, fees, locks, transfers), **learning** (using experience). One score does not serve all four.

---

## 2. Participants, time, and notation

### 2.1 Participants

**Agreed.** *Requesters* submit requests. A **root requester** is a human, or a system acting for a human with a delegated budget. A **derived requester** is an actor that needs work from another actor while executing a commitment of its own. *Actors* offer and execute work, and serve as reviewers in rotation. The *orchestrator* holds the request pool, selects, assigns verification and audits, holds funds in escrow, and issues final rulings when needed. The orchestrator is a judge and an escrow — not a bank, and not a first-line reviewer. [C2, C10, C12]

**Agreed.** Every request $q$ carries a provenance pointer $\operatorname{root}(q)$ to the root request whose fulfillment ultimately funds and judges it. A root request points to itself. An actor-initiated request with no root is a *proposal* and does not enter the pool until a root requester sponsors it. [C12]

### 2.2 Time and capacity

**Agreed (unchanged).** Discrete global time $t\in\mathbb N_0$. An assignment occupies several ticks. One ordinary commitment per actor at a time.

**Consequence (revises v0.1).** An actor is *committed* from award until it has received its initial verdict and responded to it (accepted, appealed, supplied evidence, or revised). It is then *pending* — execution capacity free, guarantee still locked — until the case vests. A pending actor may take ordinary work, if it can fund a new guarantee, or enter verification duty. The v0.1 "stuck until settlement" rule is replaced: capacity releases at the verdict; money settles at vesting. This follows from the challenge window (§6, §8) exactly as R23 already separated a reviewer's capacity from its liability.

### 2.3 Notation carried over

$\mathcal A_t,\ O,\ \mathcal P_t,\ q,\ i,\ j,\ y_q,\ \tau_{iq},\ h_t,\ \nu_q,\ \widehat F,\ Z_q,\ \delta_v,\ B_{iq},\ C_{iq},\ G_{iq},\ W_i,\ L_i,\ U_i,\ P_{iq},\ D_q,\ C^V_{jv},\ \widetilde C^V_{jv},\ K_r,\ \Pi_{jv},\ \mathcal V_t,\ X,\ V_{\max},\ \mathcal E_{q,r}(t),\ \mathcal I_q(t),\ m_0(q)$ keep their v0.1 meanings. $R_i$, $\epsilon_R$, $f_r$, $\ell_{jv}$ and $\rho_{jv}$ are superseded by §7 and §11.

### 2.4 New notation

| Symbol | Meaning |
|---|---|
| $\operatorname{root}(q)$ | Root request of $q$ |
| $\beta_q$ | Requester's maximum price for $q$ |
| $\varphi_q$ | Verification fee paid by the requester; distributed to $q$'s vested reviewers |
| $\omega_q$ | Orchestrator service fee on $q$ |
| $E_t$ | Emission in period $t$, fixed schedule |
| $M_t$ | Credits in circulation at $t$ |
| $\mathrm{Res}_t$ | Real-value reserve backing credits at $t$ |
| $v_t=\mathrm{Res}_t/M_t$ | Value of one credit in real units |
| $c_r$ | Real cost of one unit of resource $r$ |
| $p_r(t)=c_r/v_t$ | Credit price of resource $r$ at $t$ |
| $W$ | Challenge window, in ticks, after an initial verdict |
| $T_{\mathrm{resp}}$ | Window for an actor to respond to its initial verdict |
| $T_{\mathrm{rev}}$ | Window for one revision after $\mathsf P$ |
| $T_{\mathrm{evid}}$ | Window to supply evidence named by a $\bot$ |
| $T_{\mathrm{wait}}$ | Wait before a derived requester may withdraw with reduced forfeiture |
| $\rho_{\mathrm{pool}}$ | Fraction of $G$ forfeited on pool-exhaustion withdrawal |
| $G^V$ | Reviewer bond, locked per verdict |
| $p_j(t)$ | Audit rate applied to reviewer $j$'s approvals |
| $w_r$ | Emission weight of review role $r$ |
| $\kappa_i(t)$ | Duty credit of actor $i$ over a trailing window |
| $\rho_i(t)$ | Reliability of actor $i$, from settled outcomes only |
| $\lambda$ | Price weight in selection |

---

## 3. Request fulfillment and evidence

### 3.1 What is assessed (unchanged)

Reviewers evaluate the semantic fit between request and result in context. Criteria follow from the request and known context and are not invented retroactively. Vocabulary $\{\mathsf N,\mathsf P,\mathsf F,\bot\}$ with v0.1 meanings. "Fulfilled" means enough for the request, not the best conceivable output.

### 3.2 The actor bears the burden of verifiability

**Agreed.** A submission carries what a competent reviewer needs to assess it: the result, and the evidence that supports it — tests, logs, diffs, traces, references, whatever the request's criteria call for. An unverifiable submission is an actor failure, not a reviewer failure. [C10]

**Agreed.** $\bot$ is a *claim*, not a shrug. A reviewer returning $\bot$ names the evidence it needed and could not find. The actor then has $T_{\mathrm{evid}}$ ticks to supply it; if supplied, the same reviewer resumes. If not, the case settles as $\mathsf N$. The actor may instead appeal the $\bot$ (§8.1) on the ground that the named evidence was present; a $\bot$ overturned on appeal is a reviewer failure with the same consequences as any overturned verdict, and the appeal reviewers return a fulfillment verdict in the same assignment. [C10]

**Consequence.** Pushing evidence into submissions moves work from the semantic class into the mechanically checkable class, where verification is cheap and reviewer agreement is meaningful (§15.3).

### 3.3 Preserve the basis; clarification is not misconduct (unchanged)

A review records reviewer, request and result versions, criteria used, verdict, and supporting reasons. Later clarification of a request creates a new version; it does not retroactively convict the actor. For an appeal the original submission is fixed; an improved result is a revision, not proof that the rejection was wrong.

---

## 4. Money: where it enters, where it goes

### 4.1 Money enters with requests

**Agreed.** A root requester pays for its request in real value; the system issues credits against it. A derived requester pays from its wallet, which it earned upstream. Every credit in circulation traces to a root request or to emission. The orchestrator does not print on demand. [C9, C12]

On award of $q$ at price $B$, the requester's payment into escrow is

$$\text{pay-in}_q=B+\varphi_q+\omega_q,$$

and the unspent part of $\beta_q$ never leaves the requester. $B$ goes to the actor at vesting; $\varphi_q$ goes to the vested reviewers of $q$ at vesting; $\omega_q$ is the orchestrator's operating income.

### 4.2 Emission funds verification

**Agreed.** A fixed, decaying emission schedule $E_t$ subsidizes verification the way a block reward subsidizes mining. Emission is distributed only to reviews that *vest* in the period, weighted by role. Over time, requester-paid $\varphi$ dominates and the subsidy decays. Verification is the economy's security work; its floor funding does not depend on any single requester's willingness to pay for it. [C9, C11]

**Provisional default.** $E_t=E_0\cdot2^{-t/H}$ with $E_0=10$ credits per period and $H=1000$ periods; a period is one tick. Emission in a period with no vesting reviews carries to the next period.

### 4.3 The review fee is derived, not set

**Consequence.** With emission fixed per period, the fee per review floats with review volume — the difficulty adjustment:

$$f_{jv}=\frac{w_{r(v)}}{\sum_{v'\in\mathrm{Vest}_t}w_{r(v')}}\,E_t\;+\;\frac{1}{\lvert\mathrm{Vest}(q)\rvert}\,\varphi_q,$$

where $\mathrm{Vest}_t$ is the set of reviews vesting in period $t$ and $\mathrm{Vest}(q)$ the set of vested reviews of request $q$. More reviews, less emission each; the requester's $\varphi_q$ keeps per-case verification funded under load.

**Provisional default.** $w_{\mathrm{ordinary}}=1$, $w_{\mathrm{appeal}}=w_{\mathrm{audit}}=1.5$. $\varphi_q=0.1\,B$ for root requests and $0$ for nested requests, where the requester judges (§9). $\omega_q=0.05\,B$ for all requests.

### 4.4 Floating prices: a backed credit

**Agreed direction.** Resource prices float; fixed prices in v0.1 were for the initial model only. [C9]

**Provisional default (one mechanism).** The credit is backed by the reserve of real value paid in by root requesters:

- A root pay-in of real amount $a$ mints $a/v_t$ credits and adds $a$ to $\mathrm{Res}_t$. Backed issuance; neutral to $v_t$.
- Buying one unit of resource $r$ burns $p_r(t)=c_r/v_t$ credits and pays $c_r$ from the reserve. Neutral to $v_t$.
- Emission mints $E_t$ against nothing. $v_t$ falls.
- Forfeited reviewer bonds are burned. $v_t$ rises.
- Forfeited guarantees transfer to the requester. Transfers are neutral.

The credit's value is set by human demand versus emission, and resource prices in credits rise when emission outpaces pay-in. Unplug the human and $v_t\to0$: emission buys nothing, actors cannot afford inference, the economy halts — the intended behavior.

### 4.5 Nominal thresholds are indexed

**Consequence.** $D$, $G^V$, $K$, minimum guarantees and similar thresholds are stated in $t=0$ credits and applied as $x\cdot v_0/v_t$, so emission cannot erode penalties.

### 4.6 Execution cost (unchanged in form)

$C_{iq}=\sum_t\sum_r p_r(t)\,u_{irq}(t)$, including payments on nested requests the actor posted. Elapsed time is an opportunity cost, not a priced expenditure. Actor expenditure is not system-wide consumption; nested payments are transfers (§9).

---

## 5. Offers, selection, and guarantees

### 5.1 The bid (unchanged)

$b_{iq}=(B_{iq},G_{iq},\text{terms})$ with $B_{iq}\le\beta_q$. $B$ is a delivery price, not an execution cap. Overruns are the actor's; a low bid does not lower the fulfillment standard; a high guarantee is not evidence the result is correct.

### 5.2 Selection: predicted fulfillment, priced

**Agreed.** The orchestrator selects for predicted fulfillment, now with a price term, over bids within the requester's maximum: [C3, C9]

$$i^*\in\arg\max_{i\in\mathcal I_q(t),\;B_{iq}\le\beta_q}\Big[\,S_\theta\big(q,h_t^O,b_{iq},\rho_i(t)\big)-\lambda\,\tfrac{B_{iq}}{\beta_q}\,\Big].$$

$\lambda$ is how much predicted fulfillment the requester would give up for a cheaper bid. **Provisional default:** $\lambda=0.2$, constant; a requester-specified $\lambda$ is deferred.

**Agreed.** Ties within a score band are broken by vested duty credit $\kappa_i$ (§11.3). **Provisional default:** band width $0.05$.

$S_\theta$ reads reliability $\rho_i$ and the ledger. It does not read duty credit, which is a privilege, not evidence of competence.

### 5.3 Guarantee

**Agreed (unchanged).** The winner locks $G_{iq}$. Released on vested fulfillment; forfeited to the requester on final nonfulfillment; locked while pending. A fulfillment bond, not insurance.

**Provisional default.** $G_{iq}=\lceil0.5\,B_{iq}\rceil$, minimum 1.

---

## 6. Task lifecycle: committed, pending, vested

| Stage | What happens | Capacity | Funds |
|---|---|---|---|
| Available | $q\in\mathcal P_t$; actors offer | — | — |
| Award | Selection; escrow funded; $G$ locked | Committed | $G$ locked |
| Executing | Actor works, delegates (§9), revises its approach | Committed | — |
| Submitted | Result and evidence recorded; review requested | Committed | — |
| Initial verdict | Reviewer returns $\mathsf F$, $\mathsf N$, $\mathsf P$ or $\bot$ | Committed until response | — |
| Pending | Actor has responded; window $W$ runs; audit or dispute may occur | **Released** | $G$ locked |
| Vested | Window closed with the verdict standing | Free | $B$ paid; $G$ released |
| Final $\mathsf N$ | Rejection accepted, appeal lost, or dispute upheld | Free | $P^{\mathrm{fail}}$; $G$ forfeited |

**Responses to the initial verdict**, within $T_{\mathrm{resp}}$; no response is acceptance of the verdict:

- $\mathsf F$: nothing to do; the case is pending.
- $\mathsf N$: appeal (pay $D$, submit $d_q$; §8.1) or accept (final $\mathsf N$).
- $\mathsf P$: **Provisional default.** One revision within $T_{\mathrm{rev}}$ ticks at the actor's cost, re-reviewed by the same reviewer; the revised result is assessed $\mathsf F$ or $\mathsf N$ only. No revision → $\mathsf N$. The actor stays committed during revision.
- $\bot$: supply the named evidence within $T_{\mathrm{evid}}$ (review resumes), appeal the $\bot$, or accept $\mathsf N$ (§3.2).

**Provisional default.** $P^{\mathrm{fail}}=0$. $W=10$, $T_{\mathrm{resp}}=2$, $T_{\mathrm{rev}}=5$, $T_{\mathrm{evid}}=3$ ticks.

```text
Request (root or nested) ──► offers ──► priced selection ──► escrow + lock G
      │
      ▼
Execute ──► [delegate: nested loop, §9] ──► submit result + evidence
      │
      ▼
Initial verdict  (root: independent reviewer; nested: the requester-actor)
      │
      ├─ F ──► PENDING (capacity free, G locked) ──┬─ blind audit (rate p_j) ──┐
      │                                            ├─ requester dispute ───────┤
      │                                            └─ silence ─────────────────┤
      ├─ N ──► appeal? ──► 2 fresh reviewers ──► orchestrator rules on split ──┤
      ├─ P ──► one revision ──► F / N ─────────────────────────────────────────┤
      └─ ⊥ ──► supply evidence / appeal / accept N ────────────────────────────┤
                                                                               ▼
                                                             window W closes ──► VEST
                                                               pay B · release G · pay reviewer fees
                                                               release bonds · credit and reliability vest
```

---

## 7. Verification: assignment, bond, and compensation

### 7.1 Roles and eligibility (extended)

Initial reviewer(s); two fresh appeal reviewers; one blind auditor and, on disagreement, one more fresh reviewer. No self-review; original reviewers are excluded from appeals and audits of their own verdicts; appeal reviewers are distinct from each other. **Provisional default.** $m_0=1$ for root requests; $m_0=0$ for nested requests, where the requester-actor's judgment is the initial verdict (§9).

### 7.2 The reviewer bond

**Agreed.** Taking a review locks a bond $G^V$ for the life of the verdict — through completion, through the window, until vesting. Overturned by appeal, audit, or requester dispute → the bond is forfeited and burned (§4.4). Survives the window → released. Liability is symmetric: a wrong $\mathsf F$ and a wrong $\mathsf N$ cost the same. [C10]

**Provisional default.** $G^V=5$, indexed. The deterrence condition the simulation must confirm: for a reviewer that stamps without reading, expected loss per review $p_j\cdot b\cdot G^V$ — with $b$ the base rate of actually failed submissions — must exceed what stamping saves. At $p=0.1$ and $b=0.2$ the catch rate is 2%, so either $p$ or $G^V$ must be high early; the adaptive rate in §8.3 starts at $0.5$.

Capacity is released at completion (unchanged, R23); the bond and the liability are not.

### 7.3 Compensation: costs now, fee at vesting

**Agreed.** Two components, paid at different times:

- **Reimbursement at completion:** $\min(\widetilde C^V_{jv},K_r)$, evidence-backed and capped. An honest reviewer does not float its costs through the window.
- **Fee at vesting:** $f_{jv}$ from §4.3 — the emission share plus the requester's $\varphi$ share. Paid only if the verdict survives. An overturned verdict earns no fee; its share passes to the surviving reviewers of the case.

$$\Pi_{jv}=\underbrace{\min(\widetilde C^V_{jv},K_r)}_{\text{at completion}}\;+\;\underbrace{f_{jv}\cdot\mathbb 1[\text{vested}]}_{\text{at vesting}}.$$

**Provisional default.** $K_{\mathrm{ordinary}}=K_{\mathrm{appeal}}=K_{\mathrm{audit}}=5$.

**Consequence.** A stamper gets its near-zero costs back and nothing else; with audits it is negative in expectation. The margin from reviewing comes only from being right.

### 7.4 Assignment and waiting (unchanged)

Prefer eligible volunteers; otherwise round-robin among eligible available duty actors; otherwise wait. A $\bot$ that names missing evidence is a completed review for reimbursement; its fee vests only if the $\bot$ stands.

---

## 8. Challenges: appeal, requester dispute, and audit

All three use the same adjudication machinery and carry the same consequences. One challenge round per case; there is no appeal against appeal reviewers, and a dispute consumes the case's challenge round.

### 8.1 Appeal by the actor (extended to $\bot$)

The actor pays $D_q$ and submits $d_q$; two fresh reviewers receive $(q,y_q,d_q)$; the orchestrator rules on $(q,y_q,v_0,d_q,v_1,v_2)$ when they split. Applies to $\mathsf N$ and to $\bot$.

| Outcome | Guarantee | Court fee | Original reviewer |
|---|---|---|---|
| Overturned | Released at vesting | Reimbursed by the original reviewer | Bond forfeited; reliability down; audit rate doubled |
| Upheld | Forfeited | Borne by the actor | Bond released at vesting; fee vests |

**Provisional default.** $D=2$, indexed. Matching appeal verdicts settle without orchestrator action; a split goes to the orchestrator.

### 8.2 Dispute by the requester

**Agreed.** The requester of $q$ — a root human or a derived actor — may challenge an $\mathsf F$ within $W$ on the same terms: pay $D_q$, submit $d_q$, two fresh reviewers, orchestrator rules on a split. Upheld: the approving reviewer forfeits its bond and reimburses $D_q$, and the case is final $\mathsf N$ for the actor. Rejected: the requester bears $D_q$ and the case vests. [C10, C12]

### 8.3 Audit of approvals

**Agreed.** The orchestrator assigns blind audits of $\mathsf F$ verdicts inside the window. The auditor is a fresh reviewer from the reserve, receives $(q,y_q)$ only — not the original verdict — and is not told it is auditing rather than reviewing. The original verdict is committed to the ledger before the audit is assigned (§14). The orchestrator assigns audits; it does not perform them, because it is also the adjudicator and would otherwise rule on its own finding. [C10]

Agreement: the audit counts as a second vested review of $q$. Disagreement: the audit verdict stands as one appeal review, one more fresh reviewer is assigned, and the orchestrator rules on a split; consequences as in §8.1.

**Provisional default (adaptive rate).** $p_j$ starts at $0.5$ for a new reviewer; halves after every 5 consecutive vested verdicts, floor $0.05$; doubles on any overturn, cap $0.5$. A requester dispute replaces the audit for that case.

**Consequence.** Audits produce labeled examples — verdict and audit outcome — at a rate the orchestrator controls. That is most of the training signal it will ever have (Appendix A).

### 8.4 Final authority (unchanged)

$Z_q=\operatorname{Adjudicate}_O(\mathcal E_D)$. The ruling is the accepted result for settlement, not a claim of objective truth. The known incentive to predict the orchestrator rather than the truth is addressed by human oversight of rulings (§15.2), not assumed away.

---

## 9. Delegation: nested requests

### 9.1 A nested request is a full loop

**Agreed.** While committed to $q$, actor $A$ may post a nested request $q'$ with $\operatorname{root}(q')=\operatorname{root}(q)$, a maximum price $\beta_{q'}$ funded from $A$'s unlocked balance, and standard selection. The winner $B$ locks its own guarantee $G_{Bq'}$. $A$ is the requester of $q'$: it escrows $B_{Bq'}$, it judges $B$'s result, and its judgment is the initial verdict for $q'$ ($m_0=0$). [C12]

**Agreed.** $A$ settles $q'$ — accepts, rejects, or lets it reach its initial verdict — before submitting $q$. Submitting is accepting.

### 9.2 Accountability cascades

**Consequence.** $B$'s guarantee is to $A$: on $B$'s final nonfulfillment it forfeits to $A$. $A$'s guarantee is to its own requester. If $A$ delivers bad work built on $B$'s bad work and did not catch it, $A$ forfeits upstream and has no recourse — the structure pays for "verify yourself." If $A$ catches it, $A$ rejects and $B$ forfeits to $A$. $B$ may appeal $A$'s rejection exactly as under §8.1, which keeps $A$ from rejecting good work to collect guarantees. [C12]

$A$'s acceptances of nested results are audited at $A$'s own $p_A$ (§8.3), backed by $A$'s upstream guarantee rather than a separate bond. An acceptance overturned by audit forfeits $B$'s guarantee to $A$ and reduces $A$'s reliability.

### 9.3 Self-execution is always an exit

**Agreed (rule).** At any time $A$ may withdraw $q'$ and perform the work itself at its own cost — no award, no reviewer, no permission needed. This is what makes delegation deadlock-free whenever self-execution is possible. [C12]

### 9.4 When the pool is thin

**Agreed.** Sourcing a subcontractor is part of $A$'s promise when it bid on $q$; a thin pool is $A$'s risk, and floating prices make it priceable — nested bids rise when free actors are scarce, and $A$ sees that at its own bid time. [C12]

**Agreed.** If $q'$ receives no award within $T_{\mathrm{wait}}$ ticks and $A$ cannot self-execute, $A$ may withdraw its commitment to $q$ as *pool-exhaustion nonfulfillment*: $P^{\mathrm{fail}}$ applies, $\rho_{\mathrm{pool}}\cdot G_{Aq}$ is forfeited and the rest released. Pool exhaustion is not actor fault; it is part of a real economy. [C12]

**Agreed.** When the free pool is thin, the orchestrator awards nested requests before root requests. Finishing an in-flight tree frees every actor committed in it; starting a root consumes one. [C12]

**Provisional default.** $T_{\mathrm{wait}}=20$ ticks; $\rho_{\mathrm{pool}}=0.25$; "thin" means at most 2 free ordinary-eligible actors.

### 9.5 Capacity accounting

**Consequence.** A tree of depth $d$ commits $d$ actors at once. The protected reserve (§12) guards verification capacity, not delegation capacity; §9.3–9.4 are what guard delegation capacity.

---

## 10. Wallet accounting and settlement

### 10.1 Locks and escrow (unchanged in form)

$W_i=U_i+L_i$. Locking — a guarantee, a bond, a nested escrow — moves $U\to L$ and leaves $W$ unchanged; release reverses it; forfeiture reduces $W$; expenses reduce $U$ and $W$; receipts increase both. No double-pledging; no overdraft (insolvency deferred).

### 10.2 Actor settlement

Fulfilled and vested: $\Delta W^{\mathrm{task}}_{iq}=B_{iq}-C_{iq}$, where $C_{iq}$ includes nested payments made by $i$.

General single-challenge case, with $P^{\mathrm{fail}}=0$ provisional:

$$\Delta W^{\mathrm{case}}_{iq}=P_{iq}-C_{iq}-I_DD_q+I_WD_q-I_NG_{iq}-I_{\mathrm{pool}}\,\rho_{\mathrm{pool}}G_{iq}.$$

### 10.3 Reviewer settlement

$$\Delta W^V_{jv}=\min(\widetilde C^V_{jv},K_r)-C^V_{jv}+I_{\mathrm{vest}}\,f_{jv}-I_{\mathrm{over}}\big(G^V+D_q\,I_{\mathrm{fee\ paid}}\big).$$

A vested review nets $f_{jv}-\max(C^V_{jv}-K_r,0)$. An overturned review nets $-\max(C^V_{jv}-K_r,0)-G^V-D_q$ when the winning challenger paid a court fee.

### 10.4 Escrow accounting

Per request: in $=B+\varphi+\omega$; out $=B$ to the actor at vesting, $\varphi$ to the vested reviewers, $\omega$ to the orchestrator. Court fees pass from the challenger to the winner, or stay with the loser. Emission is minted into the reviewer payout, not through escrow. Forfeited guarantees go to the requester; forfeited bonds are burned.

---

## 11. Reliability and duty credit

### 11.1 Two counters, not one

**Agreed.** The v0.1 rating $R_i$ is split. [C11]

- **Reliability $\rho_i$** — were your verdicts and deliveries right. Moves only on settled outcomes: a verdict that vests → up; overturned → down; a delivery that vests → up; final $\mathsf N$ → down. Input to $S_\theta$ and to audit rates.
- **Duty credit $\kappa_i$** — did you do verification that stood. $+1$ per review that vests. Never an input to $S_\theta$.

**Provisional default.** $\rho_i=(s_i+1)/(s_i+o_i+2)$ over a trailing window of 100 settled outcomes, $s$ survived and $o$ overturned or failed. $\kappa_i$ counts vested reviews over a trailing 100 ticks.

### 11.2 Credit vests on survival

**Agreed.** Nothing accrues at completion. Currency (the fee, §7.3), reliability, and duty credit all vest on the same event: window closed, verdict standing. Society benefits from correct verification, not from verification events. [C11]

### 11.3 Duty credit buys privileges

**Agreed.** Verification is a public good; under-provision is a real risk; rewarding it is right — as privilege, not as a claim about competence. $\kappa_i$ breaks ties in selection (§5.2), reduces conscription frequency (§13), releases first from duty, and is the weight for the emission share — so the currency reward and the privilege reward are one rule. [C11]

---

## 12. Protected verification capacity

**Agreed (unchanged).** $\lvert\mathcal V_t\rvert\ge X$ with $X>V_{\max}$. Duty actors may be idle or reviewing; committed actors do not count; pending actors may count if on duty.

**Consequence.** With $m_0=1$, two appeal reviewers, and audit-plus-one, the maximum distinct reviewers one root case can require is 3. **Provisional default.** $X=4$. For one committed actor to coexist with the reserve, $\lvert\mathcal A_t\rvert\ge5$.

The reserve addresses verification starvation. It does not bound waiting, prove deadlock freedom, or cover delegation (§9.5).

---

## 13. Rotation of verification duty

**Agreed (unchanged).** Replacement-before-release; three distinguishable states (reviewing on duty, idle on duty, released); a pending liability is not an execution lock; if no replacement is available the outgoing actor stays.

**Provisional default.** A duty turn is 3 vested reviews or 30 ticks, whichever comes first. Incoming replacements are the free actors with the *lowest* $\kappa_i$ over the trailing window — duty credit reduces conscription. Volunteers may stay beyond a turn.

---

## 14. Verifiable history and trust boundary

**Agreed (unchanged).** Append-only past, committed present, mutable future; registration with an initial empty commitment; a trusted recording authority; compromise of that authority is outside the guarantee; integrity is not truth. Record scope now includes requests with their root pointers, offers, awards, locks and escrows, submissions with evidence, verdicts, challenges, audit assignments, rulings, vesting events, transfers, and role changes.

**Agreed (new use).** A verdict is committed before any audit of it is assigned, and the auditor's assignment is recorded without the auditor seeing the verdict. The ledger is what makes blind audits blind. [C10]

---

## 15. The human in the loop

### 15.1 The battery

**Agreed.** Human root requests power the economy: they are the only source of value that is not emission and the only source of truth that is not a model's opinion. Actor-to-actor requests are current flowing in the circuit. With no human request pending and no in-flight tree, the correct state is idle. Actors generating requests for each other with no root is the failure mode — a busywork economy — and the provenance rule (§2.1) is what forbids it. [C12]

### 15.2 The plug

**Agreed.** The human can interrupt the loop at any point, and every interruption is a recorded human event: dispute an approval (§8.2); request an audit of a specific case; override an orchestrator ruling — the override becomes the settled outcome and a ground-truth label; freeze awards. Silence inside the window is optimistic acceptance. [C12]

**Agreed direction.** Orchestrator rulings on split appeals are flagged for human review when a human is available. Cadence open.

### 15.3 Two classes of verification

**Consequence.** For results that are *mechanically checkable* — tests pass, numbers reconcile, output validates — reviewer agreement is meaningful because the check needs no judgment; verification is cheap and disputes rare. For *semantic* results, reviewer agreement is correlated opinion, and the human anchor is what makes it mean anything. §3.2 pushes as much work as possible into the first class.

---

## 16. Worked example

Illustrative numbers; $\omega$ omitted. Actors A–F; C, D, E, F on duty ($X=4$); A and B ordinary-eligible. The root requester is a human H.

**Setup.** H posts $q$ with $\beta=45$. A bids $B=40$ and locks $G=20$. H pays $40+4=44$ into escrow ($\varphi=4$). A's own execution costs 12. A posts nested $q'$ with $\beta'=6$; B bids $B'=5$ and locks $G'=3$; A escrows 5. B's execution costs 3. Reviewer C costs 3; auditor D costs 3. Assume this period's emission share works out to 2 credits per unit of weight.

| Tick | Event | Capacity |
|---|---|---|
| 0 | A awarded; H escrows 44; A locks 20 | A committed |
| 1 | A posts $q'$; B awarded; A escrows 5; B locks 3 | A and B committed |
| 1–3 | B executes (cost 3) and submits with evidence | — |
| 3 | A judges $\mathsf F$; $q'$ pending; the 5 in escrow goes to B at $t=13$ | B released |
| 1–4 | A executes its own part (cost 12), submits $q$ with evidence | — |
| 4–6 | C reviews: locks bond 5, cost 3 reimbursed at 6; verdict $\mathsf F$ | A pending from 6 |
| 6 | Orchestrator rolls $p_C=0.5$: audit assigned to D, blind | D busy on duty |
| 6–8 | D reviews: bond 5, cost 3 reimbursed; verdict $\mathsf F$; agrees | — |
| 16 | Window closes, H silent: **vest**. A paid 40, $G$ released. C and D paid fees; bonds released; $\kappa_C$, $\kappa_D$ and reliabilities up | — |

**A** (start 60): lock 20 → $U=40$; escrow 5 → $U=35,\ L=25$; cost 12 → $U=23,\ W=48$; escrow paid to B at $t=13$ → $L=20,\ W=43$; receive 40 at $t=16$ → $U=63,\ W=83$; release 20 → $U=83$. Net $+23=40-(12+5)$.

**B** (start 20): lock 3 → $U=17$; cost 3 → $U=14,\ W=17$; receive 5 → $U=19,\ W=22$; release 3 → $U=22$. Net $+2=5-3$.

**C** (start 30): bond 5 → $U=25$; cost 3 → $U=22,\ W=27$; reimbursed 3 → $U=25,\ W=30$; vest: $\varphi$ share 2 plus emission $2\times1=2$ → $U=29,\ W=34$; release 5 → $U=34$. Net $+4$.

**D** (start 30): same path to $W=30$; vest: $\varphi$ share 2 plus emission $2\times1.5=3$ → $W=35$. Net $+5$.

**H**: paid 44. The unspent 1 of $\beta$ never left.

**Variant — rejection and appeal.** If at $t=6$ C returns $\mathsf N$: A appeals at 7 and pays $D=2$; E and F review 7–10, both $\mathsf F$; settled without the orchestrator. A nets $+23$ (court fee reimbursed by C). C: reimbursed 3, no fee, bond 5 burned, pays A 2 — net $-7$; reliability down; $p_C$ doubles. E and F vest at appeal weight 1.5 each.

**Variant — pool exhaustion.** If at $t=1$ no actor takes $q'$ and A cannot self-execute: at $t=21$ A may withdraw; forfeits $0.25\times20=5$ to H, 15 released; $P^{\mathrm{fail}}=0$; H's remaining escrow returned. A nets $-12-5=-17$ if it had already spent 12.

---

## 17. Rule and invariant checklist

Carried from v0.1 unchanged: R01–R04, R07, R10, R11, R14, R19, R21–R24, R26. Revised or new:

| ID | Rule | Status |
|---|---|---|
| R05' | Resource prices float; the credit is backed by root pay-in and diluted by emission. | Agreed direction; mechanism provisional |
| R06' | Selection maximizes predicted fulfillment minus a price term over bids within $\beta_q$; ties by duty credit. | Agreed |
| R08' | Vested fulfillment releases $G$; final $\mathsf N$ forfeits it to the requester; pool-exhaustion withdrawal forfeits $\rho_{\mathrm{pool}}G$. | Agreed |
| R09' | An actor is committed until it responds to its initial verdict, then pending until vesting. | Consequence |
| R12' | The requester pays $B+\varphi+\omega$ into escrow; emission subsidizes reviewer fees; the orchestrator does not print on demand. | Agreed |
| R13' | A winning challenger — actor or requester — is reimbursed $D$ by the overturned reviewer. | Agreed |
| R15' | An overturned verdict forfeits the reviewer's bond and reduces reliability; symmetric for $\mathsf F$ and $\mathsf N$. | Agreed |
| R16' | Reviewer pay is capped reimbursement at completion plus a derived fee at vesting. | Agreed |
| R17' | The reviewer fee is derived from emission and $\varphi$; there is no fixed $f$. | Consequence |
| R18' | Appeal and audit reviews carry a higher emission weight. | Agreed direction; weight provisional |
| R20' | $X>V_{\max}=3$; $X=4$. | Provisional |
| R27 | The actor bears the burden of verifiability; $\bot$ is a substantiated, appealable claim. | Agreed |
| R28 | $\mathsf F$ verdicts are blind-audited at an adaptive per-reviewer rate; audits are assigned by, not performed by, the orchestrator. | Agreed |
| R29 | Requesters may dispute an $\mathsf F$ within the window. | Agreed |
| R30 | Reliability and duty credit are separate; both vest on survival; duty credit is a privilege and never an input to $S_\theta$. | Agreed |
| R31 | Every request has a root; rootless requests are proposals needing a sponsor. | Agreed |
| R32 | A nested request is a full loop; the requester-actor is its initial verdict; it settles before the parent submits. | Agreed |
| R33 | Self-execution is always an exit from a nested request. | Agreed (rule) |
| R34 | Nested requests are awarded before root requests when the free pool is thin. | Agreed |
| R35 | Human interruptions — dispute, audit request, override, freeze — are recorded events; silence is optimistic acceptance. | Agreed |
| R36 | One challenge round per case. | Agreed |

**Invariants to test:** locks and escrows never change $W$; emission is the only mint without reserve backing; forfeited bonds and resource purchases are the only burns; a court fee is reimbursed at most once; nothing accrues to a reviewer at completion except reimbursement; a verdict's ledger commit precedes its audit assignment; a nested loop reaches its initial verdict before its parent submits; the reserve never dips below $X$ during a handover; no case consumes more than $V_{\max}$ distinct reviewers.

---

## 18. Provisional defaults and remaining opens

### 18.1 Provisional defaults (all in $t=0$ credits, indexed)

| Parameter | Default | Where |
|---|---|---|
| $P^{\mathrm{fail}}$ | 0 | §6 |
| $\mathsf P$ handling | one revision, same reviewer | §6 |
| $W$ / $T_{\mathrm{resp}}$ / $T_{\mathrm{rev}}$ / $T_{\mathrm{evid}}$ | 10 / 2 / 5 / 3 ticks | §6 |
| $G_{iq}$ | $\lceil0.5B\rceil$, minimum 1 | §5.3 |
| $G^V$ | 5 | §7.2 |
| $D$ | 2 | §8.1 |
| $K$, all roles | 5 | §7.3 |
| $m_0$ | 1 root; 0 nested | §7.1 |
| $X$ | 4 | §12 |
| $\lambda$ / tie band | 0.2 / 0.05 | §5.2 |
| $\varphi$ / $\omega$ | 10% / 5% of $B$ at root; 0 / 5% nested | §4.3 |
| $E_0$ / $H$ | 10 per tick / 1000 ticks | §4.2 |
| $w$: ordinary / appeal / audit | 1 / 1.5 / 1.5 | §4.3 |
| $p_j$ | start 0.5; halve per 5 survivals, floor 0.05; double on overturn, cap 0.5 | §8.3 |
| $\rho_i$ / $\kappa_i$ windows | 100 outcomes / 100 ticks | §11.1 |
| Duty turn | 3 vested reviews or 30 ticks | §13 |
| $T_{\mathrm{wait}}$ / $\rho_{\mathrm{pool}}$ / thin pool | 20 ticks / 0.25 / ≤ 2 free | §9.4 |

### 18.2 What the simulation must find

Whether the deterrence inequality (§7.2) holds at these $p$, $b$ and $G^V$; whether $\lambda=0.2$ produces price competition without starving reliable actors; whether emission at $E_0=10$ over- or under-funds verification at realistic review volume; whether $X=4$ and $T_{\mathrm{wait}}=20$ keep trees of depth 2–3 moving; how $v_t$ behaves under a varying human request rate; whether any role has a cheap dominant strategy the rules above missed.

### 18.3 Remaining opens, off the critical path

Tick duration and intra-tick ordering; evaluator choice and calibration; $S_\theta$ implementation; identity and sybil resistance; collusion between actor and reviewer or across nested pairs; insolvency and debt; wealth concentration; the real-value exchange mechanics behind $\mathrm{Res}_t$; human review cadence for rulings; multi-verifier liability if $m_0>1$ is ever used; multi-round revision; long-horizon tasks spanning many windows.

---

## 19. Deferred ideas and superseded alternatives

**Superseded in v0.2:** fixed resource prices (now floating); the orchestrator as funding source (now escrow plus emission); fixed reviewer fee $f$ (now derived); one scalar rating with participation increments (now reliability plus duty credit, vesting on survival); payable $\bot$ (now a substantiated claim); one-sided reviewer liability (now symmetric, with bond, audit and requester dispute); the actor stuck until settlement (now pending after the verdict); the opaque "user" (now root and derived requesters); learning in the core (now Appendix A); discretionary printing (never adopted — emission is a rule).

**Still deferred:** insurance; transferable upgrades; explicit bankruptcy; starting calibration tasks; sold concurrency; reviewer collateral beyond $G^V$; depth limits on delegation (not adopted; §9.3–9.4 are the chosen controls); requester-specified $\lambda$; rent.

---

## 20. Sources and decision provenance

**[C0]–[C8]** as in v0.1.

**[C9] Money and prices (October 15, 2026).** Money enters with requests; the orchestrator is escrow, not bank; a fixed emission subsidizes verification as a block reward does mining, with requester fees taking over as emission decays; the reviewer fee is derived from emission and review volume; resource prices float — fixed prices in v0.1 were "only for an initial model." User: "agreed, this is the right model"; "I do like the fact that verification moves the economy."

**[C10] Verification accountability (October 15, 2026).** $\bot$ is not paid as a shrug; it is substantiated as a claim and the actor bears verifiability. Surprise checks: blind audits assigned, not performed, by the orchestrator at an adaptive rate. Requester dispute of approvals. Symmetric liability through a reviewer bond. User: "agreed, I like it."

**[C11] Reliability and duty credit (October 15, 2026).** Verification is a public good and should be rewarded; credit vests on survival, not completion; the reward is a privilege — tie-break, conscription relief, emission weight — not an input to the fulfillment predictor. User: "exactly."

**[C12] Requesters and delegation (October 15, 2026).** Any actor can be a requester; the human is the battery, not a breaker on the loop — the breaker is where humans interrupt; provenance to root; rootless requests need a sponsor; nested requests are full loops with cascading guarantees; the requester-actor's acceptance is the initial verdict; self-execution is always an exit (user: "yes (rule)"); a wait timeout converts to nonfulfillment with reduced forfeiture ("part of a real economy"); nested-first priority when the pool is thin. User: "accountability is the name of the game."

**[M1]** _line — The actor and its economic life, revision 4, unchanged.

**[S1]** LeWorldModel (Maes et al., 2026) — Appendix A only.  
**[S2]** RFC 9162 — background for §14 only.  
**[S3]** Optimistic rollups (fraud-proof windows) and Bitcoin's subsidy-plus-fees security budget — design analogies for §4.2 and §6, not adopted protocols.

---

## Appendix A. Learning

**Agreed direction (moved from v0.1 §13).** Actors and the orchestrator learn consequences from recorded outcomes and use predictions to decide. LeWorldModel-style latent dynamics are the initial direction; nothing in the loop depends on it. The loop supplies: per-decision observations — request, bids, verdicts, challenges, rulings, vesting, transfers; labels at two grades — *root acceptances and human overrides* (ground truth) and *vested verdicts and rulings* (procedural, provisional); and audit outcomes at a controlled rate. Training keeps the grades distinct and never relabels "overruled" as "lied." Representation, update schedule, parameter sharing and calibration remain open.

---

## Closing statement

> Requesters pay in and judge. Actors make priced commitments, execute at their own cost, and submit verifiable results. Reviewers post a bond on every verdict and earn only when it stands. Approvals are audited blind; rejections are appealable; both cost the same to get wrong. A fixed emission keeps verification funded as the economy's security work. Delegation is a full loop with cascading guarantees and a guaranteed exit. A rotating reserve keeps review capacity out of ordinary commitments. The human powers the circuit and holds the plug. The ledger forgets nothing.

Every parameter needed to run one task now has a value. The next step is to run many.

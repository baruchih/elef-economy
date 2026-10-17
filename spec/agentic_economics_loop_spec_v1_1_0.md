# Agentic Economics — The Task, Verification, and Dispute Loop

## Baseline specification 1.1.0

**Project:** ELEF / Agentic Economics  
**Prepared:** October 17, 2026  
**Supersedes:** 1.0.1 (October 15, 2026), by **design revision 1** — the verification deposit is two pots (§4.3). The revision was proposed after the first scoped run of the frozen baseline (§18.1 question 1, October 16), read on its own as a release candidate through two implementation reviews (rc.1–rc.3), accepted on October 17, and is consolidated here in place; the accepted text is kept verbatim in `spec/design_revisions/` and summarised in Appendix F. It changes one rule — how a reviewer is paid — and amends what follows from it (§4.1, §4.3, §7.3, §10, I10, I12, I17, I19, §18.1, §20, Appendices A and C). It adds no participant, no verdict, no challenge, no state. Everywhere else 1.0.1 stands unchanged, and 1.0.1 itself is in `spec/history/`.  
**Versioning (semver):** patch = wording only, no rule changed (1.0.0 → 1.0.1); minor = a design revision under §19 (1.0.1 → 1.1.0); major = a change of approach. A proposal under review is a release candidate (`-rc.N`) and is not in force.  
**Nature of this document:** A consolidation. It states the rules in force as one standalone text, so that a reader need not resolve precedence across files to learn what a word means. Where a later revision corrected an earlier one, only the correction appears. Superseded ideas are in Appendix B, with the reason each was dropped.  
**Status:** The research baseline in force. Changes to it are classified before they are made (§19). It is a rulebook, not a validated economy: what the rules do under self-interested participants is the question strategy runs exist to answer (§18).

> **The wallet supports the purpose; it does not define the purpose.**
>
> **The actor competes on its promise, is assessed on its delivery, and bears the cost of its execution.**
>
> **The past is append-only. The present is committed. The future is mutable.**
>
> **Money enters with requests. Truth enters with requesters. Verification is the security work of the economy.**
>
> **The human is the battery — and holds the plug.**
>
> **Care is paid for, not charged for.** *(1.1.0)*

### How to read this document

Each rule carries one label. **Rule** — a design commitment. **Consequence** — follows from rules, recorded so it is not rediscovered. **Default** — a concrete value or mechanism chosen so the loop runs; expected to move under simulation, and moving it is not a design change. **Hypothesis** — a claim about behavior under the rules that only a run can test. **Bracketed** — outside this baseline on purpose.

Nominal amounts are in credits at $t=0$ and are frozen per case at its first lock (§4.5).

## Contents

1. Purpose and measurement boundary
2. Participants, time, and the order within a tick
3. Requests, submissions, and the four verdicts
4. Money
5. Offers, selection, and the guarantee
6. The case lifecycle
7. Verification
8. Challenges: appeal, dispute, audit, ruling
9. Delegation
10. Settlement and accounting
11. Reliability and duty credit
12. The verification reserve and rotation
13. The record
14. The reviewer's view: the information contract
15. The human
16. Permitted and forbidden operations
17. Invariants
18. Hypotheses, scoped runs, and what is bracketed
19. Changing this baseline
20. Worked example  
Appendix A. Defaults and initialization  
Appendix B. Superseded ideas and why  
Appendix C. Notation  
Appendix D. Provenance  
Appendix E. Errata applied in v1.0.1  
Appendix F. Design revision 1 — the verification deposit is two pots (1.1.0)

---

## 1. Purpose and measurement boundary

**Rule.** The actor's purpose is to fulfill requests economically over time. Currency is an instrument toward that, never the purpose. Accumulating wealth, maximizing task count, and maximizing visible activity are not the purpose.

**Rule.** The boundary of assessment is *fulfillment of the request in its applicable context*. The economy does not price how much an outcome improved the requester's life; it decides whether the request, as made and understood, was met. The efficiency direction is: fulfill with the least necessary work and resource expenditure. Cheap nonfulfillment is not economical fulfillment; extra work is not automatically better.

**Rule.** The economy has an outside. Root requesters — humans, or delegates holding a human's budget — supply *value*, because they pay in. Humans at the root also supply *judgment that is not a model's opinion of another model*; a delegate's acceptance or dispute is a model's judgment and is recorded at its own grade (§15.4). Everything internal is calibrated against explicit human judgments and never replaces them.

Four concerns stay distinct and are never one score: **purpose** (economical fulfillment), **assessment** (was this request fulfilled), **accounting** (prices, fees, locks, transfers), **learning** (using experience).

---

## 2. Participants, time, and the order within a tick

### 2.1 Participants

**Requesters** post requests and pay for them. A **root requester** is a human, or a **delegate** — a system acting on a human's delegated budget. A **derived requester** is an actor that needs work from another actor while executing a commitment of its own (§9). A delegate posts, pays, accepts and disputes exactly as a human requester does; it holds no ruling authority (§15).

**Actors** offer and execute work, and serve as reviewers in rotation. There is no permanent reviewer class.

The **orchestrator** holds the request pool, selects among offers, assigns reviews and audits, holds funds in escrow, services the operating account, and issues a ruling when two appeal reviewers split. It is a judge and an escrow — not a bank, not a first-line reviewer, and not an auditor.

### 2.2 Time and the one-assignment rule

Time is discrete, $t\in\mathbb N_0$. An assignment occupies ticks.

**Rule.** An actor holds at most one active assignment: an ordinary commitment, or an open review — never both and never two reviews. An actor is *committed* from award, and stays committed through any revision or supply of evidence it chooses and the assessment that follows. Its execution capacity is released — the case becomes *pending*, guarantee still locked — when its submission is approved or when its appeal is admitted; terminal closure (accepting a rejection, a missed deadline, final $\mathsf N$) releases the commitment outright. Choosing to revise or to supply evidence is a response that keeps the actor committed: it may not take other ordinary work or enter verification duty until that work is assessed. A pending actor may take ordinary work or enter verification duty. A review that returns $\mathsf P$ or $\bot$ keeps its reviewer attached to the case until the actor acts; a review that returns $\mathsf F$ or $\mathsf N$ releases the reviewer at once, while its bond and liability persist.

### 2.3 Actions are atomic

**Rule.** An action either completes under its rules or changes nothing — no balance, no state, no admissible assessment, no history entry. Every amount is validated as a finite, non-negative number; every precondition is checked before the first effect. A refused attempt is a refused attempt; it is never stored as if admitted.

### 2.4 The order within a tick

**Default.** At tick $t$:

0. Participant actions are applied as they occur, in record order, and deadlines are **inclusive** — an action at the deadline tick is on time.
1. Challenges and disputes filed at $t$ are admitted.
2. Deadlines are checked: delivery, response, resubmission, review, nested wait.
3. Cases whose window has closed with nothing open **vest**; their surviving reviews, and the reviews of any case that reached final $\mathsf N$ this tick, settle in one emission batch.
4. The operating account services its outstanding claims.
5. Rotation handovers.
6. Assignments and awards: reviews and audits first; nested requests before root requests when the free pool is thin.

A challenge filed at $t$ is admitted before the same tick's vesting check.

---

## 3. Requests, submissions, and the four verdicts

### 3.1 Requests

A request $q$ carries a requester, a maximum delivery price $\beta_q$, and a provenance pointer $\operatorname{root}(q)$ to the root request whose fulfillment ultimately funds and judges it. A root request points to itself. A request posted by an actor with no root is a *proposal* and enters the pool only when a root requester sponsors it.

### 3.2 Submissions carry their evidence

**Rule.** The actor bears the burden of verifiability. A submission carries the result and whatever a competent reviewer needs to assess it — tests, logs, diffs, references, as the request's criteria require. An unverifiable submission is the actor's failure, not the reviewer's.

### 3.3 The four verdicts

A review returns one of:

| Verdict | Meaning |
|---|---|
| $\mathsf F$ fulfilled | The request's material requirements are adequately met — enough, not the best conceivable |
| $\mathsf N$ not fulfilled | No meaningful fulfillment of the expressed need |
| $\mathsf P$ partially fulfilled | Some contribution; material requirements unmet; the actor may revise once |
| $\bot$ cannot assess | The evidence the reviewer needed is missing; the reviewer names it |

**Rule.** $\mathsf P$ and $\bot$ are *responses to a submission*: they send the actor back to act. They are available only where the actor can still act — on the **first review of a submission that has not been revised or evidenced**. Every other review is answered $\mathsf F$ or $\mathsf N$: an audit, an appeal or dispute review, and a review resumed after a resubmission, whoever holds the position.

**Rule.** $\bot$ is a claim, not a shrug: the reviewer names the missing evidence, and the claim can be upheld or rejected on appeal (§8.1).

### 3.4 The basis is preserved

A review records reviewer, request and result versions, the criteria used, the verdict, and its reasons. A later clarification of a request creates a new version; it does not retroactively convict the actor. On appeal the original submission is fixed: an improved result is a revision, not proof that the rejection was wrong.

---

## 4. Money

### 4.1 Money enters with requests

**Rule.** A root requester pays in real value; the system issues credits against it. A derived requester pays from its wallet, which it earned upstream. Every credit in circulation traces to a root pay-in or to emission. The orchestrator does not print on demand.

On award of $q$ at delivery price $B$, the requester pays into escrow

$$\text{pay-in}_q = B + \varphi^E_q + \varphi^F_q + \omega_q ,$$

where $B$ is held for the actor, $\varphi^E_q+\varphi^F_q=\varphi_q$ is the **verification deposit** in its two pots (§4.3), and $\omega_q$ is the orchestrator's service fee. The unspent part of $\beta_q$ never leaves the requester.

### 4.2 Emission funds verification

**Rule.** A fixed, decaying emission schedule $E_t$ subsidizes verification the way a block reward subsidizes mining. Emission is distributed only to reviews that settle in the period, weighted by role; emission not claimed in a period is **not minted** — a block reward that is not mined is not banked. As emission decays, requester deposits take over.

**Default.** $E_t = E_0\,2^{-t/H}$ with $E_0=10$, $H=1000$, one period per tick. Total scheduled emission is $E_0/(1-2^{-1/H})\approx 1443\,E_0$.

**Consequence.** Emission mints claims on the same reserve; it adds no real resources.

### 4.3 The verification deposit: two pots, and the single payout rule

**Rule.** The verification deposit of a root request is two named amounts, both paid in by the root requester at award:

$$\varphi_q = \varphi^E_q + \varphi^F_q ,$$

the **expense allowance** $\varphi^E$ and the **fee pot** $\varphi^F$. Both belong to the root case and serve every review in its tree; nested cases carry $\varphi^E=\varphi^F=0$ — their reviews protect the root's outcome, so they draw on the root's pots. Money in one pot is never used for the other's purpose, with one exception, stated in step 3 below: at the tree's closure, fee money that no review in the tree is owed may settle the tree's expense debts.

**Reimbursement, at completion.** Each review's capped cost, $\min(\text{credits spent},K)$, is paid from the root's allowance; if the allowance is exhausted, advanced from the operating account $\Omega$; if $\Omega$ cannot cover it, deferred to settlement. A review resumed after a resubmission is the same assignment under one cap. Spending above $K$ is the reviewer's loss. Overturned and withdrawn reviews keep their reimbursement: the bond was the penalty, the cost was not.

**Fees are fixed by role.** Every surviving review $v$ of case $q$ — completed, not overturned, not withdrawn — is owed a **fixed fee** $f_{r(v)} = w_{r(v)}\,f$, where $f$ is the ordinary-review fee and $w$ the role weights, plus its emission share $e_v=\dfrac{w_{r(v)}}{\sum_{v'\in\mathrm{Batch}_t} w_{r(v')}}\,E_t$ over every review settling at $t$ across cases (§4.2). The fee does not depend on what the reviewer spent, on what any other reviewer spent, or on how much of the allowance is left.

**Settlement — one rule.** At the tick a case $q$ vests or reaches final $\mathsf N$, with $\mathrm{Surv}(q)$ its surviving reviews and $\mathrm{Owed}_q=\sum_{v\in\mathrm{Surv}(q)} f_{r(v)}$:

1. *Expense debts first, for every review of the case* — surviving, overturned, or withdrawn with a reimbursable balance: deferred reimbursements are paid, then $\Omega$'s advances are repaid, **from what remains of the root's $\varphi^E$ only**. What it cannot cover: a *reviewer reimbursement* becomes a named reviewer **claim on $\Omega$**, carrying the review it belongs to; an *advance* $\Omega$ already paid stays an **unrecovered advance borne by $\Omega$** — the reviewer has been paid, and no second claim arises from it. The fee pot is not touched at a case's settlement, because other cases in the same tree may still be owed from it.
2. *Fees.* Each surviving review receives $f_{r(v)}\cdot\min\!\big(1,\ \varphi^F_{\text{left}}/\mathrm{Owed}_q\big)$ from the root's fee pot — scaled pro rata only when what is left of the pot cannot pay this case's fees in full — and its emission share $e_v$, minted and paid in full. An overturned or withdrawn review receives no fee.
3. *At tree closure* — when the root and every nested case under it have settled — what remains of the fee pot settles the tree's own expense debts: first **this tree's outstanding reviewer claims, paid to the claimant reviewers directly, each claim retired from $\Omega$'s queue as it is paid**; then this tree's unrecovered advances, repaid to $\Omega$. Only then does whatever remains of $\varphi^E$ and $\varphi^F$ return to the root requester as unused. A requester's deposit services its own tree's verification before anyone else's: it is not an inflow to $\Omega$ and does not wait in $\Omega$'s first-in-first-out line, which governs $\Omega$'s own money (service fees, court fees) alone. This is the one movement of fee money toward expenses, and it uses only money no review in the tree is owed.

With no surviving review, step 2 pays nothing. The rounding residue of minted emission goes to $\Omega$; deposit never does.

**Consequence — the refund waits for the tree.** The expenses and fixed fees of a nested case's reviews draw on the root's pots at the nested case's own settlement, exactly as the root's reviews do at the root's; the nested reviews settle first and draw first, so a root with delegated children may see its own reviews' fees scaled. The root requester's unused deposit therefore returns when the tree is closed, not at the root's vesting alone. A tree cannot stay open long past its root: every nested case has reached its milestone before the root could submit, and nested vesting is independent of the parent's (§9). Two consequences are rule-level: a nested settlement draws on a root's pots after the root has vested, and the closure moves the root's money after its vesting — so invariant I10 admits exactly those two movements after vesting and no others; and a root whose pots are still open remains reachable until closure (in record mode, it is not paged out). Whether the pots should grow with the tree is part of §18.1 question 3.

**$\Omega$ is a revolving float.** It receives service fees and court fees, advances expenses when an allowance is exhausted, and is repaid only as the settlement allows — from the allowance's remainder at each settlement, and from the fee pot's remainder at tree closure. An advance those cannot repay is $\Omega$'s own loss, funded by the service fee $\omega$; $\Omega$ is thereby the pooled expense fund of the economy, and $\omega$ is the premium every request pays toward expense overflow in any tree. $\Omega$ pays its outstanding reviewer claims first in, first out, partially if it must, on every inflow. Each claim is bounded by $K$; the aggregate of claims and unrecovered advances is monitored, not capped (§18).

**Default.** $K=5$. $f=2$ per unit of role weight: ordinary 2, appeal 3, audit 3. $\varphi^E=2K=10$ at root. $\varphi^F=f\,(w_{\text{ordinary}}+w_{\text{audit}})=5$ at root — sized for the common full case, one review and one audit; nested $0/0$. $\omega_q=0.05\,B$. Role weights $w$: ordinary 1, appeal 1.5, audit 1.5. A challenged case has three surviving reviews at most (one initial, two challenge) or two challenge reviews after an overturn; with $\varphi^F=5$ two challenge fees (6) are scaled to 2.5 each. This is deliberate: the pot is sized for the common case, the shortfall is small, and challenge reviews also carry the 1.5 emission weight. Sizing $\varphi^F$ for the worst case ($f(1+2\cdot1.5)=8$) is a default the sweep may choose. **Default under consideration:** $K=3$, $\varphi^E=6$, $\varphi^F=5$ — total deposit 11, one credit above 1.0.1's; moving $K$ is a default change, not a rule change.

**Consequence — reviewer income from deposits falls, and the fee level is the lever.** Under 1.0.1 an uncontested single review took the whole deposit remainder, about 10 credits; under 1.1.0 it takes $f=2$ plus emission, and the requester is refunded about 8. In the common case the deposit flow to reviewers drops by roughly three quarters, the requester's net deposit cost falls from 10 to between 4 and 7 (fee 2 plus the reviewer's actual expense of 2–5), and emission carries a larger share of reviewer income than 1.0.1 intended ("deposits take over as emission fades" no longer holds at $f=2$). Whether reviewers can still fund the bond $G^V=5$ and their care from unlocked credit is a solvency question for §18.1 questions 3 and 6. $f$ is a default; the rerun of question 1 carries $f\in\{2,4\}$.

### 4.4 The credit: backed, floating, and the halt state

**Default (one mechanism).** The credit is backed by the reserve $\mathrm{Res}_t$ of real value paid in by root requesters, and its value is

$$v_t=\frac{\mathrm{Res}_t}{M_t}.$$

- Root pay-in of real amount $a$ mints $a/v_t$ credits and adds $a$ to the reserve — neutral to $v_t$.
- A resource purchase burns $p_r(t)=c_r/v_t$ credits and pays the real cost $c_r$ from the reserve — **value-neutral**: $v'=\dfrac{\mathrm{Res}-c}{M-c/v}=v$.
- Emission mints against nothing — $v_t$ falls.
- Forfeited bonds are burned — $v_t$ rises.
- Guarantees, kill fees and court fees transfer — neutral.

**Consequence.** Resource purchases are value-neutral. Emission lowers credit value; bond burning raises it. Backed issuance and transfers leave it unchanged. With no new root pay-in, actor income is emission only, which is finite, and aggregate real-resource spending is bounded by the backing: reserve and supply can only exhaust together. $\mathrm{Res}_t=0$ is the **halt state**: $v_t=0$ by definition, never $0/0$. Idle costs nothing.

**Hypothesis.** That an economy of actors serving each other with no human at the root *reaches* the halt state — stops through empty wallets rather than idling with funds held elsewhere, or spending ceasing before the reserve is gone — is a claim about behavior, not a consequence of the rules. The rules bound spending; they do not force it. It is item 7 of §18.1.

### 4.5 Denomination: a case is priced at its first lock

**Rule.** Every nominal amount attached to a case — the court fee $D$, the reimbursement cap $K$, the reviewer bond $G^V$, the deposit $\varphi$, and the bond of every review ever assigned to it — is indexed once, by $v_0/v_t$ at the case's **first lock**, and frozen for the case's life. A root case's first lock is its award; a nested case's is its posting. The actor's guarantee $G$ is fixed at award. $G^V\ge D$ then holds for every review of the case whatever $v_t$ does afterwards.

### 4.6 Execution cost

$C_{iq}$ is measured in credits and includes the credits burned by actor $i$'s resource purchases on $q$, the delivery prices it has paid on completed nested requests under $q$, and kill fees it has paid. **Rule.** A purchase is attributed to a case only if the purchaser is the case's committed actor and the case is executing; any other attributed purchase is refused before it happens. Review costs are likewise recorded in credits burned, so the cap compares like with like.

---

## 5. Offers, selection, and the guarantee

### 5.1 The bid

An actor's offer commits to a price **and a time**:

$$b_{iq}=(B_{iq},\ \tau_{iq},\ G_{iq},\ \text{terms}),\qquad B_{iq}\le\beta_q ,$$

where $\tau_{iq}$ is the delivery time in ticks after award. $B$ is a delivery price, not an execution cap: overruns are the actor's. A low bid does not lower the fulfillment standard; a high guarantee is not evidence the result is correct. $\beta_q$ is the requester's maximum *delivery price*; the requester is shown the all-in maximum $\beta_q+\varphi_q+\omega(\beta_q)$ before posting.

### 5.2 Selection

**Rule.** The orchestrator selects for predicted fulfillment with a price term, over bids within the requester's maximum:

$$i^*\in\arg\max_{i\in\mathcal I_q(t),\ B_{iq}\le\beta_q}\Big[\,S_\theta\big(q,h_t^O,b_{iq},\rho_i(t)\big)-\lambda\,\frac{B_{iq}}{\beta_q}\Big],$$

where $S_\theta$ estimates fulfillment under assignment to $i$ from the request, the ledger, the bid and the actor's reliability $\rho_i$; and $\lambda$ is how much predicted fulfillment the requester would give up for a cheaper bid. Ties within a band are broken by duty credit $\kappa_i$ (§11). $S_\theta$ never reads $\kappa_i$.

**Default.** $\lambda=0.2$; band $0.05$. $S_\theta$'s implementation is bracketed.

### 5.3 The guarantee

**Rule.** The winner locks $G_{iq}$ from its unlocked balance. It is released at vesting, forfeited to the requester on final $\mathsf N$, and locked while pending. It is a fulfillment bond, not insurance: an execution overrun alone does not forfeit it.

**Default.** $G_{iq}=\lceil 0.5\,B_{iq}\rceil$, minimum 1.

---

## 6. The case lifecycle

| Stage | What happens | Actor capacity | Funds |
|---|---|---|---|
| Available | $q$ is in the pool; actors offer | — | — |
| Award | Escrow and deposit funded; $G$ locked; nominals frozen; deadline $t_0+\tau$ set | Committed | $G$ locked |
| Executing | Work; nested requests (§9); revision | Committed | — |
| Submitted | Result and evidence recorded, at or before the deadline | Committed | — |
| Initial verdict | $\mathsf F$, $\mathsf N$, $\mathsf P$ or $\bot$ | Committed until the actor responds | — |
| Pending | Window $W$ runs from the verdict | **Released** | $G$ locked |
| Suspended | A challenge or audit is open; the window does not close | Released | $G$ locked |
| Vested | Window closed, nothing open, verdict standing | Free | $B$ paid; $G$ released; reviews settled |
| Final $\mathsf N$ | Deadline missed; rejection accepted or defaulted; appeal lost; dispute upheld; ruling | Free | $G$ forfeited; escrow returned; reviews settled |

### 6.1 Deadlines

**Rule.** A missed delivery deadline is final $\mathsf N$ with full forfeiture; it is mechanical and not appealable.

### 6.2 Responses to the initial verdict

Within $T_{\mathrm{resp}}$ ticks — no response is acceptance of the verdict:

- after $\mathsf F$: nothing to do; the case is pending.
- after $\mathsf N$: **appeal** (§8.1) or accept (final $\mathsf N$).
- after $\mathsf P$: choose to **revise** — then resubmit within $T_{\mathrm{rev}}$ — or accept $\mathsf N$. One revision per case. $\mathsf P$ is not appealable.
- after $\bot$: choose to **supply the evidence** — then resubmit within $T_{\mathrm{evid}}$ — or appeal the $\bot$ (§8.1), or accept $\mathsf N$.

On resubmission the same reviewer resumes; its review clock, paused while the actor acted, resumes; the resumed review is the same assignment under one cap and returns $\mathsf F$ or $\mathsf N$ only. The resubmitted stage belongs to the submission, not the reviewer: a replacement reviewer inherits it. A missed resubmission window is final $\mathsf N$.

### 6.3 Vesting is financial finality

**Rule.** A case vests at $\max(t_0+W,\ t_{\mathrm{resolve}})$, where $t_0$ is the initial verdict and $t_{\mathrm{resolve}}$ the resolution of any challenge or audit opened inside the window. A challenge filed at $t\le t_0+W$ is admitted; later ones are not. **After vesting, no adjudication changes a case's financial obligations.** Obligations established before vesting — deferred reimbursements, claims on $\Omega$ — may still be paid. What a later human correction can do is in §15.

**Default.** $W=10$, $T_{\mathrm{resp}}=2$, $T_{\mathrm{rev}}=5$, $T_{\mathrm{evid}}=3$; $P^{\mathrm{fail}}=0$ (nothing is paid for nonfulfillment).

---

## 7. Verification

### 7.1 Positions and eligibility

A root case has one initial reviewer. A nested case has none: its requester-actor's judgment is its initial verdict (§9). An appeal has two fresh reviewers. An audit has one blind auditor plus, on disagreement, one more.

**Rule.** A reviewer is eligible for a case if it is on duty, not excluded from the case (its actor, its requester, its previous reviewers, and any reviewer withdrawn from it), able to fund the case's frozen bond from its unlocked balance, and holding no active assignment.

### 7.2 The reviewer's bond is its whole liability

**Rule.** Taking a review locks $G^V$ for the life of the verdict. If the verdict is overturned — by appeal, dispute, audit, or ruling — a winning challenger's court fee is reimbursed from the bond and the remainder is burned. If it stands, the bond is released at settlement. Liability is symmetric: a wrong $\mathsf F$ and a wrong $\mathsf N$ cost the same. An appeal reviewer who dissents from the outcome forfeits its bond and owes no fee. $G^V\ge D$ by construction, so no reviewer ever owes more than it has locked.

**Default.** $G^V=5$, $D=2$, both frozen per case.

### 7.3 Compensation: costs now, fee at settlement

$$\Pi_{jv}=\underbrace{\min(\text{credits spent},K)}_{\text{at completion, from the allowance}}\ +\ \underbrace{\big(f_{r(v)}+e_v\big)\cdot\mathbb 1[\text{verdict stood}]}_{\text{at settlement, by §4.3}} .$$

A reviewer that is right earns the fixed fee of its role and its emission share; a reviewer that is wrong gets its costs back and nothing else, and loses its bond.

**Consequence.** Within the cap, care costs the reviewer nothing: a careful reviewer that spends $c\le K$ is made whole and earns the same fee as one that spent nothing. The fee is for the work of reviewing, not for the answer, and not for the thrift. (Under 1.0.1 the fee was the deposit's remainder after reimbursements, so every credit of care reimbursed was a credit of fee lost; §7.3 of that text reasoned with a fixed $\bar f=2$ that its §4.3 did not pay. Design revision 1 restored the fixed fee — Appendix F.)

**Hypothesis.** Let $p$ be the effective audit rate, $b$ the base failure rate, $\varepsilon$ the careful reviewer's error rate, $\bar f=f+\bar e$ the surviving fee with emission, $G^V$ the bond. In the regime where actors accept every rejection (no appeals), per review,

$$\mathbb E[\Delta W_{\text{stamp}}]-\mathbb E[\Delta W_{\text{careful}}] \;=\; -\,p\,b\,(1-\varepsilon)\,\big(\bar f+G^V\big)\;-\;(\text{reliability loss}) \;<\;0 \quad\text{for every } pb>0 :$$

stamping is weakly dominated in money and strictly dominated once reliability loss counts — the opposite sign of 1.0.1, where the same quantity was $+1.3$ at the defaults and was measured at $+1.6$ in strategy run 1. With actor appeals in scope the inequality gains a term stampers never pay: a careful reviewer rejects good work at rate $\varepsilon(1-b)$, and an appealed and overturned false rejection costs it $\bar f+G^V$, so the right-hand side becomes $-\,pb(1-\varepsilon)(\bar f+G^V)+a\,\varepsilon(1-b)(\bar f+G^V)$, with $a$ the rate at which false rejections are appealed and overturned. At $\varepsilon=0.05$, $b=0.2$ it stays negative while $pb>0.04\,a$, which the defaults satisfy, but it is no longer unconditional; the appeals run measures $a$. At the defaults with run 1's effective catch rate of about 3%, the money term is roughly $-0.3$ per review; at the nominal $p=0.5$, $b=0.2$, about $-0.7$. How *fast* stamping loses, and whether the reliability channel (§11) adds anything at the current tie band, is what the rerun of §18.1 question 1 must find. A verdict that survives is *procedurally settled*; it is not thereby correct.

### 7.4 Deadlines, withdrawal, replacement, voiding

**Rule.** A review not completed by $t_{\mathrm{assign}}+T_{\mathrm{review}}$, plus any paused ticks, is **withdrawn**: half its bond burns, half is released, no reimbursement, reliability down, the reviewer is excluded from the case, and its position is vacated. A vacated position — initial, appeal or audit — is refilled by the ordinary assignment rule. A vacated **audit** is an obligation: the case stays suspended until a replacement audit completes, the orchestrator **waives** it, or a requester dispute takes it over; a replacement audit is admissible after the window closes if the withdrawn one was assigned inside it.

An open assignment that a human ruling moots is **voided**, not withdrawn: the bond returns whole, no fault is recorded, and the obligation ends with the ruling.

**Default.** $T_{\mathrm{review}}=5$; $K=5$ for every role.

### 7.5 Assignment

Volunteers first; otherwise round-robin among eligible duty actors; otherwise wait. Refusing to volunteer does not exempt an actor from mandatory duty.

---

## 8. Challenges: appeal, dispute, audit, ruling

**Rule.** One challenge round per case. A dispute consumes it; an audit that disagrees consumes it; an audit that agrees does not. There is no appeal against appeal reviewers.

**Rule.** The challenger pays the court fee $D$ to $\Omega$ at filing. If the challenger wins, the liable bond reimburses $D$ to the challenger; if it loses, nothing further moves. The loser bears the fee. The grounds of a challenge are text and are committed to the record with the challenge; they are shown to the reviewers who decide it.

### 8.1 Appeal by the actor

After $\mathsf N$ or $\bot$ the actor pays $D$, states its grounds $d_q$, and two fresh reviewers receive the submission, the appealed assessment and the grounds. Matching verdicts settle the appeal; a split goes to the orchestrator.

**An appeal of $\mathsf N$:** overturned → $G$ released at vesting, $D$ reimbursed from the original reviewer's bond, that reviewer's remaining bond burned, its reliability down and its audit rate doubled; upheld → $G$ forfeited, $D$ borne by the actor.

**An appeal of $\bot$ answers two questions**, both stated explicitly by each appeal reviewer and never inferred one from the other:

1. **Objection** — was the first reviewer right that the evidence was missing? `upheld` or `rejected`.
2. **Fulfillment** — $\mathsf F$ or $\mathsf N$. An upheld objection entails $\mathsf N$: what cannot be assessed cannot be fulfilled.

| Both reviewers say | The $\bot$ | Court fee | Outcome |
|---|---|---|---|
| rejected, same verdict | overturned | reimbursed to the actor | their verdict |
| rejected, different verdicts | overturned | reimbursed | the orchestrator rules on fulfillment |
| upheld | stands; its reviewer is paid as correct | borne by the actor | $\mathsf N$ — an unverifiable submission is the actor's failure |
| split on the objection | — | — | the orchestrator rules on **both** questions |

An appeal reviewer is overruled if its objection disposition differs from the settled one, or — when the objection is rejected — if its verdict differs from the settled outcome.

### 8.2 Dispute by the requester

Within the window, the requester of a root case may dispute a pending $\mathsf F$ on the same terms: fee, grounds, two fresh reviewers, orchestrator on a split. Upheld → the approving reviewer's bond pays the fee and the rest burns; final $\mathsf N$ for the actor. Rejected → the requester bears the fee; the case vests. A dispute is admitted only if the round is free, the window is open, the grounds are text, and the requester can fund the fee — all checked before anything changes. A requester may not dispute a case a human has ruled on (§15).

### 8.3 Audit of approvals

**Rule.** The orchestrator assigns blind audits of pending $\mathsf F$ verdicts, each to a fresh reviewer that receives the submission and not the case's verdicts, challenge records or reviewer identities. The orchestrator assigns audits; it does not perform them, because it also rules. The verdict is committed to the record before the audit is assigned. Opening an audit suspends vesting.

An audit is answered $\mathsf F$ or $\mathsf N$ (§3.3). Its agreement is judged against the case's **live** assessment. Agreement → a second settled review. Disagreement → the audit verdict stands as one appeal review, one more fresh reviewer is assigned, and the orchestrator rules on a split, with the consequences of §8.1. If a requester disputes while an audit is open or after it agreed, the audit verdict is one of the two dispute reviews. No audit is assigned to a case a human has ruled on; an audit open at a ruling is voided.

**Default (adaptive audit rate).** $p_j$ starts at $0.5$ for a new reviewer; halves after every 5 consecutive verdicts that stood, floor $0.2$; doubles on any overturn, cap $0.5$.

### 8.4 The orchestrator's ruling

$Z_q=\operatorname{Adjudicate}_O(\mathcal E_D)$ over the full record of the challenge. The ruling is the accepted result for settlement, not a claim of objective truth. The known incentive to predict the orchestrator rather than the truth is addressed by human review of rulings (§15), not assumed away.

---

## 9. Delegation

### 9.1 A nested request is a full loop

**Rule.** While committed to $q$, actor $A$ may post a nested request $q'$ with $\operatorname{root}(q')=\operatorname{root}(q)$ and a maximum price $\beta'$. Posting locks $\beta'+G^V$ from $A$'s unlocked balance and freezes $q'$'s nominals at that index (§4.5). On award, $B'$ moves into escrow and the unspent $\beta'-B'$ is released; the $G^V$ stays locked as $A$'s **rejection bond**. The winner $B$ locks its own guarantee. $A$ is $q'$'s requester: it judges $B$'s result, and its judgment is $q'$'s initial verdict.

**Rule.** $A$ may submit $q$ only after every nested request it posted has reached its **milestone**: its initial verdict, or a terminal state — withdrawn, cancelled, or final $\mathsf N$ without a submission (a missed delivery). Nested vesting is independent of the parent's; $A$ carries that risk.

**Consequence.** The root pointer forbids rootless requests, not unnecessary ones. What constrains unnecessary delegation is that $A$ pays for every nested award from its own margin.

### 9.2 Accountability cascades; one guarantee secures one obligation

**Consequence.** $B$'s guarantee is to $A$: on $B$'s final nonfulfillment it forfeits to $A$. $A$'s guarantee is to its own requester. If $A$ delivers bad work built on $B$'s bad work and did not catch it, $A$ forfeits upstream with no recourse. If $A$ catches it, $A$ rejects, $B$ forfeits to $A$, and $B$ may appeal exactly as under §8.1 — which keeps $A$ from rejecting good work to collect guarantees.

**Rule.** The rejection bond is released the moment $A$ accepts; acceptance is not bonded, because its downside flows through $A$'s own delivery. If $A$ rejects, the bond is $A$'s reviewer bond for $B$'s appeal: on overturn it pays $B$'s court fee and the remainder burns; if the rejection stands, it is released at settlement. The principle: bond the verdict whose wrongness harms the *other* party with no other recourse. A wrong acceptance harms $A$; a wrong rejection harms $B$. $A$'s guarantee secures one obligation — delivery of $q$ — and nothing else; a nested acceptance overturned by audit forfeits $B$'s guarantee to $A$ and lowers $A$'s reliability, with no separate monetary loss to $A$.

### 9.3 Exits: self-execution, cancellation, pool exhaustion

**Rule.** Self-execution is always an exit: $A$ may do the nested work itself at its own cost whenever that is possible. Before award, $A$ withdraws $q'$ freely. After award and **before $B$ submits**, $A$ may cancel by paying $B$ a **kill fee** of $\min(C_B,K)$ — $B$'s execution cost on $q'$ as §4.6 defines it — from the nested escrow first, then $A$'s unlocked balance, and only if $A$ can fund it; $B$'s guarantee and $A$'s rejection bond are released, $B$ is unmarked, and the fee counts in $A$'s cost. Once $B$ has submitted, $A$ must judge.

**Rule.** If $q'$ has been open and unawarded for $T_{\mathrm{wait}}$ ticks, $A$ cannot self-execute, and the parent's own deadline has not yet arrived, $A$ may withdraw its commitment to $q$ as *pool-exhaustion nonfulfillment*: $\rho_{\mathrm{pool}}\,G$ is forfeited and the rest released; it is not actor fault. If the deadline arrives first it is an ordinary miss. When the free pool is thin the orchestrator awards nested requests before root requests, since finishing a tree frees actors and starting a root consumes one.

**Rule.** On every exit — final $\mathsf N$ for any reason, pool exhaustion, cancellation — the exiting case's unawarded nested requests are withdrawn with it and the locks behind them released; awarded ones continue.

**Consequence.** A delegation tree commits as many actors as it has in-flight nodes, not its depth. The reserve (§12) guards verification capacity; these exits guard delegation capacity.

**Default.** $T_{\mathrm{wait}}=5$; $\rho_{\mathrm{pool}}=0.25$; "thin" is at most 2 free ordinary-eligible actors.

---

## 10. Settlement and accounting

### 10.1 Wallets and locks

$W_i=U_i+L_i$. Locking — a guarantee, a bond, a nested price ceiling, a rejection bond — moves $U\to L$ and leaves $W$ unchanged; release reverses it; forfeiture reduces $W$; expenses reduce $U$ and $W$; receipts increase both. **Every locked credit is attributable to a named obligation**, and a wallet's $L$ is the sum of its lock records. No double-pledging; no overdraft.

### 10.2 The actor

Fulfilled and vested: $\Delta W^{\mathrm{task}}_{iq}=B_{iq}-C_{iq}$. In general, with $P^{\mathrm{fail}}=0$:

$$\Delta W^{\mathrm{case}}_{iq}=P_{iq}-C_{iq}-I_D D_q+I_W D_q-I_N G_{iq}-I_{\mathrm{pool}}\,\rho_{\mathrm{pool}}G_{iq},\qquad I_N+I_{\mathrm{pool}}\le 1 .$$

### 10.3 The reviewer

$$\Delta W^V_{jv}=I_{\mathrm{paid}}\min(\text{spent},K)-\text{spent}+I_{\mathrm{stood}}\,\big(s_q\,f_{r(v)}+e_v\big)-I_{\mathrm{over}}\,G^V-I_{\mathrm{late}}\,\tfrac12 G^V ,$$

with $I_{\mathrm{paid}}=0$ for a withdrawn review, the court fee inside $I_{\mathrm{over}}G^V$ and owed only by the reviewer whose verdict was challenged, $f_{r(v)}$ the fixed fee by role and $s_q=\min(1,\varphi^F_{\text{left}}/\mathrm{Owed}_q)$ the fee-pot scale of §4.3.

### 10.4 Escrow and the operating account

Per root request: in $=B+\varphi^E+\varphi^F+\omega$; out $=B$ at vesting, reimbursements from $\varphi^E$ at completion (for the root and its nested cases), fixed fees from $\varphi^F$ and emission at each settlement in the tree, the tree's expense debts from the fee pot's remainder and both pots' unused remainders at tree closure, $\omega$ to $\Omega$. Forfeited guarantees go to the requester; forfeited bonds, net of court-fee reimbursement, are burned — they do not fund fees; kill fees and court fees transfer; emission is minted into case pools.

---

## 11. Reliability and duty credit

**Rule.** Two counters, never one.

- **Reliability $\rho_i$** — were your verdicts and deliveries right. Moves only on settled outcomes: a verdict or delivery that stood → up; overturned, failed, missed, or withdrawn → down. Input to $S_\theta$ and to audit rates. A human correction after settlement records a failed outcome for every contradicted assessment (§15).
- **Duty credit $\kappa_i$** — did you do verification that stood. $+1$ per review that settled standing. Never an input to $S_\theta$.

**Rule.** Nothing accrues at completion. Fee, reliability and duty credit all vest on the same event — the verdict stood at settlement. Society benefits from correct verification, not from verification events.

**Rule.** Verification is a public good and under-provision is a real risk, so duty credit is rewarded — as *privilege*, not as evidence of competence: it breaks ties in selection, reduces conscription, and releases first from duty.

**Default.** $\rho_i=(s_i+1)/(s_i+o_i+2)$ over the trailing 100 settled outcomes; $\kappa_i$ counts reviews settled in the trailing 100 ticks.

---

## 12. The verification reserve and rotation

**Rule.** At least $X$ actors are on verification duty at all times — idle on duty or reviewing — outside ordinary commitments, with $X>V_{\max}$, where $V_{\max}$ is the maximum **review positions** one case can hold on a challenge path: initial plus two appeal, or audit plus one — three. A withdrawn position is vacated and refilled; distinct actors over a case's lifetime are unbounded under replacement. Three counts are kept: reserve membership, *occupancy* (eligible duty actors are busy), and *solvency shortfall* (fewer than $V_{\max}$ duty actors can fund a bond). Only the last is a working-capital condition.

**Rule.** Duty rotates: replacement before release. A turn ends after a fixed number of reviews that stood or a fixed number of ticks; the incoming replacement is the free actor with the lowest duty credit, among those who were **off duty when the tick's rotation began** — so a released actor has at least one tick of ordinary eligibility. If no replacement is available the outgoing actor stays. Volunteers may stay beyond a turn.

**Default.** $X=4$; a turn is 3 reviews or 30 ticks.

---

## 13. The record

**Rule.** There is one authoritative record: an append-only, hash-chained history of every admitted action with its material parameters — postings, awards, submissions, verdicts, responses, challenges with their grounds, audit assignments, rulings, cancellations, withdrawals, acceptances, corrections, rotations, and every ledger event. The ledger's event list and each case's log are working copies, each entry carrying its commitment position, and the per-tick checks verify the chain **and** that each copy holds exactly its committed entries in order. Changes are appended, never rewritten; two disagreeing assessments can coexist in an integrity-valid history.

**Limit.** The chain is tamper-evident within the process. An external commitment of its head — the trusted recording authority — is bracketed. Integrity is not truth: a verified chain establishes that an assessment was made on identified evidence and that the procedure accepted an outcome, not that the outcome is correct.

---

## 14. The reviewer's view: the information contract

**Rule.** A reviewer receives the information its question requires and the set of responses it may give, and nothing else about the case:

| Field | Content |
|---|---|
| the submission | result, evidence, actor, time of submission, whether it has been resubmitted |
| the terms | deadline, bond, cap, whether the case is nested |
| `question` | `fulfillment`, `appeal`, or `dispute` |
| `responses_available` | whether $\mathsf P$ and $\bot$ may be answered (§3.3) |
| for an appeal or dispute | the assessment under appeal and the challenger's grounds |

Other reviewers' identities and unrelated judgments are not supplied. **The question and the permitted responses may reveal the stage or kind of assignment; audit-role indistinguishability is not guaranteed.** In particular, a fulfillment question on an unrevised submission with $\mathsf P$ and $\bot$ unavailable is an audit, and recognizing it reveals that a prior approval exists — not what it said or who gave it. This is the trade-off chosen: the view states the admissible answers truthfully, so identical views admit identical answers and no refusal reveals anything the view did not say; in exchange the role is inferable. Whether role secrecy is required is a design question; this baseline answers no, because the deterrents an auditor faces — bond, audit rate, reliability — do not depend on it.

---

## 15. The human

### 15.1 The battery

**Rule.** Human root requests power the economy: they are the only source of value that is not emission and the only source of judgment that is not a model's. Actor-to-actor requests are current in the circuit. With no human request pending and no in-flight tree, the correct state is idle.

### 15.2 The plug: rulings and corrections

**Rule.** Two different things are called ruling, and the word is kept for both because the record uses it for both. The **orchestrator rules on procedural disagreements**: a split between appeal or dispute reviewers (§8.4), inside the ordinary procedure. **Only a human may issue a human override** — the ruling of §15.2 — which bypasses the economy's machinery, and the only ground for it is that a human's judgment is not a model's opinion of another model. A delegate holds no override authority; it accepts or disputes through the ordinary procedure like any requester. Where this document says "a human ruling" or "a ruling before vesting" it means the override. Whether a particular human is authorized over a particular request is bracketed; in this baseline every human is.

**Rule.** A human may interrupt a case at any point, and every interruption is a recorded human event: dispute an approval, request an audit, **rule**, or freeze awards. Silence inside the window is protocol-default acceptance.

**A ruling before vesting** is the ruling. It is validated whole — the human, the outcome, that there is a result to rule on, and for a $\bot$ the disposition and its entailment — then: every unfinished assignment is voided without fault; every completed verdict that contradicts the ruling is overturned with the standard consequences, a reviewer's or a requester-actor's rejection alike; a ruling that accepts a nested result ends the rejection obligation whether or not the requester-actor had judged; and the case is settled — an open challenge by the ruling, otherwise directly. No audit or dispute may be opened afterwards. Contradiction is defined once: $\mathsf F$ contradicts $\mathsf N$; $\mathsf N$ and $\mathsf P$ contradict $\mathsf F$; a $\bot$ is contradicted only by a rejected objection; an appeal reviewer of a $\bot$ is contradicted on either of its two answers.

**A correction after settlement** moves no money. It changes the recorded outcome and grade, records a failed outcome for the actor and for every settled assessment it contradicts — by the complete assessment, two answers where there were two — and may create a corrective obligation: a new request, funded by the human, to repair the result. A review that has not yet reached its payout batch when the correction arrives is treated as unsettled: contradicted, it is overturned.

### 15.3 Label grades

**Rule.** Every settled case records its outcome and the grade of the event that **established** it, by that event's **author**:

| Grade | Established by |
|---|---|
| human-explicit | a human's acceptance, winning dispute, or ruling |
| delegate-explicit | a delegate's acceptance or winning dispute |
| procedural | a challenge, an audit, or a ruling on a split, with no matching root judgment |
| protocol-default | one initial verdict, no challenge, no audit, silence |

A root judgment that disagrees with the settled outcome — a dispute that lost — is recorded as an assessment beside a procedural outcome; the disagreement is the learning signal. Nested cases are always procedural. Nothing promotes between grades, and no label at any grade is read as "correct" rather than "accepted."

---

## 16. Permitted and forbidden operations

**Permitted.** Post a root request (human or delegate). Post a nested request (a committed actor). Withdraw an unawarded request. Award within $\beta$. Spend on a case (its committed actor, while executing). Submit by the deadline. Resubmit within the window after choosing to revise or supply evidence. Assign an initial review, an appeal review, an audit; replace a withdrawn position; waive a vacated audit. Complete a review with an admissible answer. Respond to a verdict within the window. Appeal an $\mathsf N$ or a $\bot$ with text grounds. Dispute a pending $\mathsf F$ within the window with text grounds. Rule on a split. Judge a nested result. Cancel a nested request before its submission. Withdraw for pool exhaustion within the stated bounds. Rule (a human), before or after settlement. Accept explicitly (a requester). Volunteer for or leave duty.

**Forbidden, and refused without effect.** A bid above $\beta$ or a non-positive delivery time. A second active assignment. A review by the case's actor, requester, prior or withdrawn reviewer, or an unfunded reviewer. $\mathsf P$ or $\bot$ outside the first review of an unrevised submission. An appeal of a $\mathsf P$; an appeal of a $\bot$ without the objection's disposition; an upheld disposition with $\mathsf F$. A second challenge round. A dispute or audit after a human ruling. A ruling by a delegate. A ruling on a case with no result. Spending attributed to another actor's case or to a settled case. Non-text grounds. A kill fee the requester-actor cannot fund; a cancellation after submission. A submission while a nested request is short of its milestone. Any amount that is negative or not finite. Any action whose preconditions fail — nothing partial is ever kept.

**Not offered in this baseline.** Reopening an approved case through an audit (Appendix B). Clawback after vesting. Appeal against appeal reviewers. A second revision. Multiple initial reviewers at root.

---

## 17. Invariants

Nineteen, checked after every tick. A failure is a bug in the engine or a contradiction in this document, never a property of a strategy.

| | Property |
|---|---|
| I1 | Every credit is in a wallet, a case pool, or $\Omega$; their sum is $M$; and $M$ equals mints minus burns reconstructed from the record |
| I2 | No balance, pool, or reserve is negative or non-finite |
| I3 | Only known event kinds, finite non-negative amounts; the only unbacked mint is emission; the only burns are bond forfeiture and resource purchase |
| I4 | A court fee is reimbursed at most once, never above the bond; $G^V\ge D$ per case |
| I5 | No case vests with an open item, an unresolved challenge, an open review, or before its window |
| I6 | An audit is assigned no earlier than the verdict it audits |
| I7 | A parent submits only after every nested request reached its milestone |
| I8 | Review positions per case $\le V_{\max}$ |
| I9 | The reserve holds $X$ |
| I10 | No adjudication moves money after vesting; after it only obligations established before it, a nested case's draws on its root's pots, and the tree's closure move money on account of the case |
| I11 | Full forfeiture and pool-exhaustion forfeiture are exclusive |
| I12 | Nominals — $D,K,G^V$ and both pots — do not change after the first lock; $G$ not after award; an unawarded nested case's rejection bond equals its frozen $G^V$ |
| I13 | Every settled case has exactly one grade, and the record justifies it by the establishing event's author |
| I14 | One active assignment per actor |
| I15 | Every wallet's $L$ is the sum of its lock records; every live obligation has a record of exactly its size; no orphan records |
| I16 | The history chain verifies, and every working copy holds exactly its committed entries, in order |
| I17 | Reimbursement fields are non-negative and within the cap; every claim on $\Omega$ names a review whose pending balance covers it; no ended nested case carries a rejection bond |
| I18 | No audit is open or assigned after a human ruling |
| I19 | The pots (1.1.0): for every tree, fees paid from the fee pot $\le\varphi^F$; fee money reached expenses only at closure and only up to the pot's remainder after every fee in the tree; no fee was paid from $\varphi^E$; a refund occurs only when the tree is closed, and a closed tree has every case settled and both pots empty |

---

## 18. Hypotheses, scoped runs, and what is bracketed

### 18.1 What a run must find

1. **Careful versus careless review.** Under 1.1.0, how fast does stamping lose (§7.3), and does the reliability channel add anything at the current tie band? Strategy run 1 answered the 1.0.1 form of this question — careful review did not beat stamping at the defaults — and led to design revision 1 (Appendix F); the rerun with only the rule changed, at $X\in\{4,8\}$ and $f\in\{2,4\}$ with twenty seeds or more, measures the rule's effect alone.
2. **Price pressure.** Does $\lambda=0.2$ produce competition without starving reliable actors?
3. **Verification funding.** Does $\varphi^E=2K$ cover root-plus-nested expenses; how often does $\Omega$ advance; how much does it bear unrecovered; is $\omega=5\%$ enough to fund it; should the pots grow with the tree?
4. **Emission scale.** Is $\approx1443\,E_0$ against $M_0$ a subsidy or a flood?
5. **Delegation liveness.** Do trees of 2–4 nodes move under $T_{\mathrm{wait}}$, the kill fee, nested-first priority, and the rejection bond's capital cost?
6. **Reserve solvency versus occupancy.** How often does each occur; do fees restore solvency?
7. **Monetary behavior.** How does $v_t$ move with the human request rate; does an economy with no human at the root reach the halt state through empty wallets, as §4.4 hypothesizes, or idle short of it?
8. **Dominant strategies.** Anything cheap the rules missed.

### 18.2 Scoped runs

**Rule.** A strategy run states its **permitted operations** before it runs. A run on a subset — root cases only, $\mathsf F/\mathsf N$ reviewers, human rulers, no post-settlement corrections — is legitimate and interpretable provided it says what it does not exercise. A result from a path the run excluded is not a result; a skipped penalty or a forced answer from the harness is an implementation effect, not an economic one.

### 18.3 Bracketed

Strategies and policies. Learned selection ($S_\theta$'s implementation) and the learning direction (Appendix A of earlier revisions; LeWorldModel-style latent dynamics remain the initial direction, with labels kept at their four grades and never promoted). Evaluator behavior — the harness has no request content and no judgment. Authorization among humans. An external commitment of the history head. Physical tick duration. The real-value exchange behind $\mathrm{Res}_t$. Insolvency beyond the bounded claim on $\Omega$. Collusion and sybil resistance. Rent. Insurance. Multi-round revision. Long-horizon tasks spanning many windows.

---

## 19. Changing this baseline

**Rule.** Three activities, three change criteria:

| Activity | Question | What a finding warrants |
|---|---|---|
| Rulebook design | What is allowed, owed, observed, and final? | Change only for an explicit design decision or an unresolved contradiction between active rules |
| Implementation conformance | Does the engine apply these rules, including refusals and timing? | Repair the engine, add a regression; never introduce a different permitted behavior |
| Strategy research | Which allowed choices work, for a participant or the system? | A separate run against this fixed baseline with declared permitted operations |

A future finding is classified before it is acted on: an admitted operation misapplying a rule, or a refused one with effects → repair and regression; two active rules demanding contradictory outcomes → the smallest explicit rule decision, versioned and reviewed as a rule change; a workflow that would be useful but is not offered → a proposal for a later design revision, not an obligation; a strategy that performs badly or an incentive that looks wrong → an evaluation under the fixed rules. A conformance pass may change *how* a rule is applied; a change to *what participants may do* is a design revision, is labeled as one, and is read on its own before it is implemented.

---

## 20. Worked example

Illustrative; $\omega$ omitted (with it, H pays 57 and $\Omega$ receives 2.25). Six actors; C, D, E, F on duty; root requester H. Emission at the settlement tick is taken as 5 credits — 2 per unit of role weight when C (weight 1) and D (1.5) settle together. The reference implementation reproduces every figure.

**Setup.** H posts $q$ with $\beta=45$. A bids $B=40$, $\tau=8$, and locks $G=20$; H pays $40+10+5=55$ ($B$, the allowance, the fee pot). At $t=1$ A posts $q'$ with $\beta'=6$, locking $6+5=11$; B bids $B'=5$, $\tau'=3$, locks $G'=3$; 5 moves to escrow and 1 is released. B's work costs 3; A's own costs 12; C and D each cost 3.

| Tick | Event |
|---|---|
| 0 | A awarded; due by 8 |
| 1 | $q'$ posted and awarded to B; due by 4 |
| 1–3 | B executes and submits with evidence |
| 3 | A accepts $q'$: rejection bond released; B pending; $q'$ window to 13 |
| 4 | A submits $q$; C assigned, locks 5 |
| 6 | C: $\mathsf F$, reimbursed 3 from the allowance (7 left); A pending, window to 16; audit rolled: D assigned, blind; vesting suspended |
| 8 | D: $\mathsf F$, reimbursed 3 from the allowance (4 left); agrees; suspension lifted |
| 13 | $q'$ vests: B paid 5, $G'$ released |
| 16 | $q$ vests, H silent: A paid 40, $G$ released. Fixed fees C $f=2$, D $3$: $\mathrm{Owed}=5=\varphi^F$, paid in full; emission C 2, D 3; bonds released; reliability and duty credit vest. The tree is closed ($q'$ vested at 13): the allowance remainder 4 returns to H |

**Nets.** A $+23=40-12-5$; B $+2$; C $+4=-3+3+2+2$; D $+6=-3+3+3+3$; H $-51$; $\Omega$ untouched. Escrow: in 55 $=40+6+5+4$ out. Grade of $q$: procedural (an audit occurred); of $q'$: procedural. Under the default under consideration ($K=3$, $\varphi^E=6$, $\varphi^F=5$): H pays 51; both reimbursements exhaust the allowance; fees as above; refund 0; every net is identical.

**Variants** — each reproduced in the test suite: rejection and appeal (A $+23$, C $-5$: bond pays A's fee and burns 3, costs reimbursed, no fee; E and F each owed 3, $\mathrm{Owed}=6>5$, paid 2.5 each plus emission 2.5); appeal of a $\bot$ with the objection rejected (same figures) and upheld (A bears the fee, final $\mathsf N$, A $-12-2-20$); pool exhaustion (A withdraws at 6, forfeits 5, nets $-17$; both pots return to H at closure; with $\tau=4$ the deadline falls first and A $-20$); cancellation (kill fee $\min(2,5)=2$ from escrow, 3 returned); nested rejection appealed and overturned (A's rejection bond pays B's fee; B $+2$ as if accepted); shortfall and haircut (allowance exhausted, $\Omega$ advances 5; the fee pot pays $\mathrm{Owed}=8$ scaled by $5/8$ and has nothing left at closure, so the advance stays unrecovered, borne by $\Omega$; emission in full); timeout and replacement (3 positions on the path, 4 distinct reviewers); a dispute at the window's last tick (admitted; vest at 14 not 12); a correction after vesting (record and reliability change, no credit moves).

---

## Appendix A. Defaults and initialization

| Parameter | Default | Section |
|---|---|---|
| $W$ / $T_{\mathrm{resp}}$ / $T_{\mathrm{rev}}$ / $T_{\mathrm{evid}}$ / $T_{\mathrm{review}}$ / $T_{\mathrm{wait}}$ | 10 / 2 / 5 / 3 / 5 / 5 ticks | §6, §7.4, §9.3 |
| $G$ | $\lceil0.5B\rceil$, min 1 | §5.3 |
| $G^V$ / $D$ / $K$ | 5 / 2 / 5, frozen per case | §7.2, §7.4 |
| $\varphi^E$ root / nested; $\varphi^F$ root / nested; $\omega$ | 10 / 0; 5 / 0; 5% of $B$ | §4.3 |
| $f$ (ordinary-review fee; appeal and audit $1.5f$) | 2 | §4.3 |
| $P^{\mathrm{fail}}$ | 0 | §6.3 |
| $m_0$ | 1 root; 0 nested | §7.1 |
| $V_{\max}$ / $X$ | 3 / 4 | §12 |
| $\lambda$ / tie band | 0.2 / 0.05 | §5.2 |
| $E_0$ / $H$; emission carry-forward | 10 / 1000; none | §4.2 |
| $w$ ordinary / appeal / audit | 1 / 1.5 / 1.5 | §4.3 |
| $p_j$ | start 0.5; halve per 5 survivals, floor 0.2; double on overturn, cap 0.5 | §8.3 |
| $\rho$ / $\kappa$ windows | 100 outcomes / 100 ticks | §11 |
| duty turn | 3 reviews or 30 ticks | §12 |
| $\rho_{\mathrm{pool}}$ / thin | 0.25 / ≤ 2 free | §9.3 |

**Initialization.** $v_0=1$; $\mathrm{Res}_0=10{,}000$ real units paid in by a sponsor, who is the first root requester; $M_0=10{,}000$ credits; a one-time cold-start float of 50 credits per actor and 20 for $\Omega$, from the sponsor's credits — valid only if $|\mathcal A_0|\cdot 50+20\le M_0$; the lowest-id $X$ actors on duty; $\rho_i(0)=0.5$, $\kappa_i(0)=0$, $p_j(0)=0.5$. The float is the only subsidy that is not emission, and it is paid once.

---

## Appendix B. Superseded ideas and why

| Idea | Held in | Dropped because |
|---|---|---|
| Fixed resource prices | v0.1 | For the initial model only; prices float by §4.4 |
| The orchestrator as funding source, "funding received" | v0.1 | Nothing pushed price down and no budget existed; money now enters with requests |
| Fulfillment-first selection with no price term | v0.1 | Bids rose unbounded; $\lambda$ added |
| One-sided reviewer liability (wrong $\mathsf N$ costs $D$, wrong $\mathsf F$ costs nothing) | v0.1 | Approving everything was dominant; bond, audit and dispute made it symmetric |
| $\bot$ paid regardless | v0.1 | A free exit; now a substantiated claim the actor may contest |
| One scalar rating with $+\epsilon$ per completed review | v0.1 | Rewarded participation, not correctness; split into $\rho$ and $\kappa$, both vesting on survival |
| Actor stuck until settlement | v0.1 | A 10-tick window would idle it; capacity releases at the verdict |
| Fixed reviewer fee $f=2$ | v0.1 | Could not hold with fixed emission; derived |
| $\varphi$ as 10% of $B$ | v0.2 | Not a funding source for reimbursement; now a deposit sized to verification cost |
| Carry-forward emission | v0.2–v0.3 | The first reviews after a quiet start won a lottery |
| Bond smaller than liability | v0.2 | A reviewer could owe 7 with 5 locked |
| "Stamping is negative in expectation" | v0.2 | Did not follow; now a hypothesis with the inequality stated |
| $\kappa$ as an emission weight | v0.2 | Confused a count with a weight |
| Discretionary printing | never adopted | Inflation erodes fixed penalties first; emission is a rule |
| "$\mathrm{Res}\to0\Rightarrow p_r\to\infty$" | v0.3 | Purchases are value-neutral; the halt is through wallets |
| Nominals indexed at use | v0.3 | A later court fee could exceed the bond already locked; frozen at first lock |
| Unbonded nested rejection | v0.3 | An overturned rejection had no reimbursement source; the posting lock is the bond |
| $V_{\max}$ as a lifetime count of reviewers | v0.3 | Unbounded under replacement; it counts positions |
| Grade by participation; by requester's role | v0.3, v0.8 | A losing dispute is not a human label; the author of the establishing event decides |
| "Self-execution at any time" | v0.3 | Ignored an awarded subcontract; the kill fee, and no cancellation after submission |
| Clawback after vesting | considered | Rejected for corrective obligations; vesting is final |
| A delegate with ruling authority | an unstated reading | A delegate is a model; the override exists because a human is not |
| **Audit reopening** — an auditor's $\mathsf P$/$\bot$ sending an approved case back to the actor | v0.9 | A design change made in a conformance pass; collided with timestamps, capacity, replacement, nested liability and merged disputes at once. An audit judges a finished verdict. Withdrawn in v0.10; the interface problem it addressed is solved by the view stating its admissible answers (§14) |
| Role-indistinguishable audits | claimed through v0.9 | Not true once the view states admissible answers; stated as the trade-off it is (§14) |

---

## Appendix C. Notation

| Symbol | Meaning |
|---|---|
| $q$, $\operatorname{root}(q)$, $\beta_q$ | a request, its root, its maximum delivery price |
| $B,\tau,G$ | delivery price, delivery time, guarantee |
| $\varphi_q=\varphi^E_q+\varphi^F_q,\ \omega_q$ | verification deposit — expense allowance and fee pot — and service fee |
| $f,\ f_r=w_r f,\ \mathrm{Owed}_q,\ s_q$ | ordinary-review fee, fee by role, the fees owed to a case's surviving reviews, the fee-pot scale |
| $D,K,G^V$ | court fee, reimbursement cap, reviewer bond |
| $W,T_{\mathrm{resp}},T_{\mathrm{rev}},T_{\mathrm{evid}},T_{\mathrm{review}},T_{\mathrm{wait}}$ | the windows |
| $E_t,w_r,e_v$ | emission, role weight, a review's emission share |
| $\mathrm{Res}_t,M_t,v_t,c_r,p_r(t)$ | reserve, supply, credit value, real resource cost, credit price |
| $W_i,U_i,L_i$ | total, unlocked, locked balance |
| $\Omega$ | the operating account |
| $\rho_i,\kappa_i,p_j$ | reliability, duty credit, audit rate |
| $S_\theta,\lambda$ | the fulfillment predictor, the price weight |
| $X,V_{\max},\mathcal V_t,\mathcal R_t$ | reserve size, positions per path, duty set, review-eligible set |
| $\mathsf F,\mathsf N,\mathsf P,\bot$ | the four verdicts |
| $Z_q$ | the accepted settlement outcome |

---

## Appendix D. Provenance

Discussion anchors [C0]–[C12] (October 15, 2026) settled the purpose and boundary, fixed-then-floating prices, learned selection and the guarantee, verification and appeal, the reserve and rotation, money entering with requests and emission funding verification, symmetric reviewer liability, reliability versus duty credit, and requesters and delegation. Eight external reviews [R1]–[R8] of v0.2 through v0.9 found, in order: the funding gap, bond-versus-liability and the stamping overclaim; the payout-after-shortfall and indexing gaps; atomicity, occupancy, replacement, cost units and the Ω claims; the interaction defects of those repairs; the boundary defects of those; the follow-through defects; the correction-logic and interface defects; and the consequences of reopening. A ninth review [R9] of v0.10 found no new execution defect in its bounded checks, corrected the "blindness stands" claim to the trade-off stated in §14, and recommended this consolidation and the change discipline of §19. A tenth review [R10] of v1.0 accepted it as the frozen baseline, recommended keeping it frozen, and found four places where the consolidated wording said more or less than the decisions it consolidates — the two senses of "ruling", when a response releases capacity, what moves credit value and whether halting is a consequence or a hypothesis, and the two kinds of shortfall at settlement; each is corrected in place and recorded in Appendix E. The reference implementation, `agentic_sim/`, encodes every rule here with injected decisions, checks the nineteen invariants (eighteen through 1.0.1) after every tick, and carries every reviewer's test file verbatim — 156 passing (four added with v1.0.1 for the one permitted operation no suite had exercised, withdrawing an unawarded request), with 24 expected failures each stating why, strict and parameter-exact in both entry points. The `_line` map "The actor and its economic life" (revision 4) records the Section 1 discussion and is superseded by the map of this baseline. **1.1.0.** The first scoped run of the frozen baseline [S1] (October 16, 2026; §18.1 question 1, ten runs) found that careful review did not beat stamping at the defaults, through the fee: 1.0.1's remainder rule charged care against the reviewer's own fee. Design revision 1 — the verification deposit is two pots — was proposed the same day as a release candidate, read on its own through two implementation reviews [I1], [I2] (October 17; the per-case "unowed fee money" defect in trees, the I10 and record-mode consequences, the reviewer-income consequence, the appeals qualification of §7.3, the test list, the rerun's power; then the net-cost figure, who the fee pot's remainder pays, and the provenance), accepted as rc.3 on October 17, and consolidated here. The engine implements it; the suite is 181 passing with 25 expected failures (the twenty-fifth: the fifth review's unfunded-dispute test, which pinned the 1.0.1 deposit through the human's budget; its principle is re-asserted in `test_v11` at the 1.1.0 pay-in); the golden History heads were re-pinned once, at the implementing commit.

---

## Appendix E. Errata applied in v1.0.1

Four textual corrections from the tenth review [R10]. Each clarifies a decision already made; none changes a rule, a default, a permitted operation, or the engine. Classification under §19: consolidation wording, not design and not conformance — the engine was checked against each item and already behaves as the corrected text says.

| # | Where | v1.0 said | v1.0.1 says | Why |
|---|---|---|---|---|
| E1 | §1, §15.2, closing | "Only a human rules," while §8.4 has the orchestrator rule on a split; §1 credited every root requester, delegates included, with non-model judgment | The orchestrator rules on procedural disagreements (splits); only a human may issue the override; a delegate's judgment is a model's and is graded as such (§15.3) | The two senses of "ruling" contradicted each other read literally; the label grades already kept the distinction |
| E2 | §2.2 | An actor is committed "until it has responded to its initial verdict; it is then pending — execution capacity released" | Approval or an admitted appeal releases capacity; choosing to revise or supply evidence keeps the actor committed through that work and its assessment; terminal closure releases the commitment | "Respond" includes revise and supply-evidence, which return the actor to work; the engine holds `RESUBMITTING` as executing and a standalone reader would otherwise free the actor on "revise" |
| E3 | §4.4, §18.1(7) | "Purchases never move the price; only emission does"; busywork "is self-terminating" stated as a consequence | Purchases are value-neutral; emission lowers credit value, bond burning raises it, backed issuance and transfers leave it unchanged. The halt state is a definition; that a rootless economy reaches it is the hypothesis of §18.1(7) | The sentence contradicted the table above it; the rules bound real spending but do not force it to exhaust the reserve |
| E4 | §4.3 step 3 | "What the pool cannot cover becomes a reviewer claim on $\Omega$" | An unpaid reviewer reimbursement becomes a named claim on $\Omega$; an advance $\Omega$ paid but could not recover is an unrecovered advance borne by $\Omega$ and creates no reviewer claim | The v1.0 sentence admitted a double-payment reading; the engine already writes the unrecovered advance down against $\Omega$ and files claims only for unpaid reimbursements |

---

## Appendix F. Design revision 1 — the verification deposit is two pots (1.1.0)

The accepted text is `spec/design_revisions/dr1_two_pots_1.1.0-rc.3.md`, kept verbatim; this appendix records what it changed and why, so the consolidated text above can be read without it.

**Finding [S1].** Strategy run 1 (October 16, 2026): at the defaults, with half the reserve stamping, stampers ended richer in four of five seeds; 47% of truly failed work was paid in full, 88% with nine stampers in ten. The channel was the fee: a careful reviewer earned 7.9 per review and a stamper 9.5 — a gap equal to the careful reviewer's own expenses.

**Mechanism.** Under 1.0.1 §4.3 the deposit was one pot doing two jobs: reimbursing capped expenses, and paying *what remained* as the fee. Every credit reimbursed was a credit of fee lost. The rule charged for diligence at the margin, while 1.0.1 §7.3 still reasoned with the fixed fee of v0.1 R16–R17 ("capped expense reimbursement plus a fixed fee … for review work, not for the answer"), which v0.3 had replaced by the remainder when it repaired the second review's shortfall finding. The accounting closed; the incentive inverted.

**Classification.** A design revision motivated by a strategy finding and justified by the spec's own §7.3 assuming a fee its §4.3 did not pay — the case §19 permits when the revision is labelled, read on its own, and reviewed before implementation. It restores a decision already on the record. The selection tie band and the audit floor, which the run also implicated, were left as defaults, to be swept separately.

**What changed.** §4.1 pay-in; §4.3 whole (two pots; expenses from the allowance alone; fixed fees by role from the fee pot, scaled only when short; the cross-pot step and the refund at tree closure; $\Omega$ as the pooled expense fund); §7.3 (compensation and the restated hypothesis, with the appeals term); §10.3–10.4; I10's two exceptions, I12 (both pots are nominals), I17's note and the new I19; §18.1 questions 1 and 3; §20 re-settled; Appendices A and C. Defaults: $f=2$, $arphi^E=10$, $arphi^F=5$; under consideration $K=3$, $arphi^E=6$.

**Found in review and adopted.** rc.1 computed "unowed fee money" per case, which in a tree would pay a root's expenses with money its nested case's reviewers were still owed; rc.2 moved the cross-pot step to tree closure. rc.1 said "nothing else moves"; rc.2 recorded that reviewer income from deposits falls by about three quarters in the common case and that I10 and record mode gain the tree consequences. rc.1 stated the hypothesis unconditionally; rc.2 qualified it to the no-appeals regime and added the appeals term. rc.3 settled the requester's net-cost figure, that the fee pot's remainder pays the tree's claimants directly, and the provenance. The revision's own text calls the post-vesting invariant "I4"; in this baseline's numbering it is I10 (I4 is the court-fee invariant).

**Engine.** The ledger's case pool holds the allowance (the field keeps its 1.0.1 name, `deposit`) and the fee pot; settlement follows §4.3 in order and reads the root's pool for a nested case; the refund waits for tree closure; I19 is checked per tick; a root with open pots stays resident in record mode. Reviewer-authored tests were not edited: one is superseded (above); the rest pass unchanged.

**After acceptance.** Rerun strategy run 1 with only this rule changed — twenty seeds or more, at $X\in\{4,8\}$ and $f\in\{2,4\}$, the $X=4$, $f=2$ cell the like-for-like comparison — then the default sweep (band, audit floor, bond), the appeals run, and the requester-dispute run, in that order.

---

## Closing statement

> A request is paid for by the one who makes it, judged first by a reviewer who is bonded on the answer, audited blind, open to appeal and dispute for a window, and then final. The actor commits to a price and a time and bears its own cost. The reviewer is made whole for its care, earns its fee only when right, and loses only what it locked. Verification is funded as the security work it is. Delegation is the same loop one level down, with the requester-actor's rejection bonded and its acceptance its own risk. The human powers the circuit and holds the plug: the orchestrator rules on splits inside the procedure, and only a human overrides it. The record is one record. The reviewer is told what it may answer and nothing it need not know. These are the rules of this version. The engine is corrected to them; they change only by decision; and what they do under self-interest is for runs to show.

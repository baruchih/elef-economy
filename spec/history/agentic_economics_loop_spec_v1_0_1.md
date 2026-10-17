# Agentic Economics — The Task, Verification, and Dispute Loop

## Baseline specification v1.0.1

**Project:** Agentic-OS / Agentic Economics  
**Prepared:** October 15, 2026  
**Supersedes:** v1.0 (October 15, 2026), by errata only. The tenth external review [R10] read v1.0 as a standalone text and found four places where the consolidation's wording said more, or less, than the decisions it consolidates. Each is corrected here in place and listed in Appendix E with its before and after. No rule, default, permitted operation or implementation changed; the reference implementation already behaves as the corrected wording says, and was checked against each item before the wording was changed.  
**Nature of this document:** A consolidation. It states the rules in force after v0.1–v0.10 as one standalone text, so that a reader need not resolve precedence across ten files to learn what a word means. It adds no rule, changes no default, and decides nothing that was not already decided; where a later revision corrected an earlier one, only the correction appears. Superseded ideas are in Appendix B, with the reason each was dropped.  
**Status:** A frozen research baseline. Changes to it are classified before they are made (§19). It is a rulebook, not a validated economy: what the rules do under self-interested participants is the question strategy runs exist to answer (§18).

> **The wallet supports the purpose; it does not define the purpose.**
>
> **The actor competes on its promise, is assessed on its delivery, and bears the cost of its execution.**
>
> **The past is append-only. The present is committed. The future is mutable.**
>
> **Money enters with requests. Truth enters with requesters. Verification is the security work of the economy.**
>
> **The human is the battery — and holds the plug.**

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

$$\text{pay-in}_q = B + \varphi_q + \omega_q ,$$

where $B$ is held for the actor, $\varphi_q$ is the **verification deposit**, and $\omega_q$ is the orchestrator's service fee. The unspent part of $\beta_q$ never leaves the requester.

### 4.2 Emission funds verification

**Rule.** A fixed, decaying emission schedule $E_t$ subsidizes verification the way a block reward subsidizes mining. Emission is distributed only to reviews that settle in the period, weighted by role; emission not claimed in a period is **not minted** — a block reward that is not mined is not banked. As emission decays, requester deposits take over.

**Default.** $E_t = E_0\,2^{-t/H}$ with $E_0=10$, $H=1000$, one period per tick. Total scheduled emission is $E_0/(1-2^{-1/H})\approx 1443\,E_0$.

**Consequence.** Emission mints claims on the same reserve; it adds no real resources.

### 4.3 The verification deposit and the single payout rule

**Rule.** $\varphi_q$ funds the verification of $q$ *and of every nested case under it* (nested cases carry $\varphi=0$; their reviews protect the root's outcome, so they draw on the root's deposit).

**Reimbursement, at completion.** Each review's capped cost, $\min(\text{credits spent},K)$, is paid from the root's deposit; if the deposit is exhausted, advanced from the operating account $\Omega$; if $\Omega$ cannot cover it, deferred to settlement. A review resumed after a resubmission is the same assignment under one cap.

**Settlement — one rule.** At the tick a case vests or reaches final $\mathsf N$, with $\mathrm{Surv}(q)$ its surviving reviews (completed and not overturned or withdrawn):

1. *Entitlements.* For each $v\in\mathrm{Surv}(q)$: $\text{ent}_v = e_v + \dfrac{(\varphi_q-\mathrm{Reimb}_q)^+}{|\mathrm{Surv}(q)|}$, where $e_v=\dfrac{w_{r(v)}}{\sum_{v'\in\mathrm{Batch}_t} w_{r(v')}}\,E_t$ over every review settling at $t$ across cases.
2. *Pool.* $\mathrm{pool}_q=(\varphi_q-\mathrm{Reimb}_q)^+ + \sum_{v\in\mathrm{Surv}(q)} e_v$; the emission is minted into it.
3. *Cost debts first, for every review of the case* — surviving, overturned, or withdrawn with a reimbursable balance: deferred reimbursements are paid from the pool, then $\Omega$'s advances are repaid. The two shortfalls are different debts. A *reviewer reimbursement* the pool cannot cover becomes a named reviewer **claim on $\Omega$**, carrying the review it belongs to. An *advance* $\Omega$ already paid to a reviewer but the pool cannot repay remains an **unrecovered advance borne by $\Omega$**; the reviewer has been paid, and no second claim arises from it. An overturned reviewer forfeits its bond and fee; its cost obligation survives.
4. *Haircut.* Fees are the entitlements scaled by $\dfrac{\mathrm{pool}_q-\text{repaid}}{\mathrm{pool}_q}$.

With no surviving review, the deposit left after step 3 is returned to the requester as unused. The rounding residue of minted emission goes to $\Omega$; deposit never does.

**$\Omega$ is a revolving float.** It receives service fees and court fees, advances reimbursements, is repaid from case pools to the extent they cover, and pays its outstanding reviewer claims first in, first out, partially if it must, on every inflow. Each claim is bounded by $K$; the aggregate outstanding claim is monitored, not capped (§18). An advance the case pool could not repay is $\Omega$'s own loss, monitored alongside the claims.

**Default.** $\varphi_q=2K=10$ at root; $\omega_q=0.05\,B$; role weights $w$: ordinary 1, appeal 1.5, audit 1.5.

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

$$\Pi_{jv}=\underbrace{\min(\text{credits spent},K)}_{\text{at completion, from the deposit}}\ +\ \underbrace{f_{jv}\cdot\mathbb 1[\text{verdict stood}]}_{\text{at settlement, by §4.3}} .$$

A reviewer that is right earns the fee; a reviewer that is wrong gets its costs back and nothing else, and loses its bond.

**Hypothesis.** For a reviewer that approves without examining, with audit rate $p$, base failure rate $b$, expected surviving fee $\bar f$ and bond $G^V$:

$$\mathbb E[\Delta W]=(1-pb)\,\bar f-pb\,G^V,$$

negative only when $G^V>\bar f\,(1-pb)/(pb)$ — a joint condition on all four, not satisfied at the defaults ($+1.3$ at $p=0.5$, $b=0.2$, $\bar f=2$, $G^V=5$; $+0.6$ even at $p=1$). Monetary deterrence alone does not make careless review unprofitable. The deterrent the rulebook relies on is **reliability loss** (§11): an overturn lowers $\rho_i$, which lowers future awards. Whether careful review beats careless review once that is included is the first question a strategy run must answer (§18). A verdict that survives is *procedurally settled*; it is not thereby correct.

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

$$\Delta W^V_{jv}=I_{\mathrm{paid}}\min(\text{spent},K)-\text{spent}+I_{\mathrm{stood}}\,f_{jv}-I_{\mathrm{over}}\,G^V-I_{\mathrm{late}}\,\tfrac12 G^V ,$$

with $I_{\mathrm{paid}}=0$ for a withdrawn review, the court fee inside $I_{\mathrm{over}}G^V$ and owed only by the reviewer whose verdict was challenged, and $f_{jv}$ the haircut entitlement of §4.3.

### 10.4 Escrow and the operating account

Per root request: in $=B+\varphi+\omega$; out $=B$ at vesting, reimbursements from $\varphi$ at completion (for the root and its nested cases), fees and any unused deposit at settlement, $\omega$ to $\Omega$. Forfeited guarantees go to the requester; forfeited bonds, net of court-fee reimbursement, are burned; kill fees and court fees transfer; emission is minted into fee pools.

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

Checked after every tick. A failure is a bug in the engine or a contradiction in this document, never a property of a strategy.

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
| I10 | No adjudication moves money after vesting |
| I11 | Full forfeiture and pool-exhaustion forfeiture are exclusive |
| I12 | Nominals do not change after the first lock; $G$ not after award; an unawarded nested case's rejection bond equals its frozen $G^V$ |
| I13 | Every settled case has exactly one grade, and the record justifies it by the establishing event's author |
| I14 | One active assignment per actor |
| I15 | Every wallet's $L$ is the sum of its lock records; every live obligation has a record of exactly its size; no orphan records |
| I16 | The history chain verifies, and every working copy holds exactly its committed entries, in order |
| I17 | Reimbursement fields are non-negative and within the cap; every claim on $\Omega$ names a review whose pending balance covers it; no ended nested case carries a rejection bond |
| I18 | No audit is open or assigned after a human ruling |

---

## 18. Hypotheses, scoped runs, and what is bracketed

### 18.1 What a run must find

1. **Careful versus careless review.** Under the defaults, does careful review beat stamping once reliability loss is included (§7.3), and at which $(p,G^V,\bar f)$ does it stop?
2. **Price pressure.** Does $\lambda=0.2$ produce competition without starving reliable actors?
3. **Verification funding.** Does $\varphi=2K$ cover root-plus-nested verification; how often does $\Omega$ advance; how large does its outstanding claim get?
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

Illustrative; $\omega$ omitted (with it, H pays 52 and $\Omega$ receives 2.25). Six actors; C, D, E, F on duty; root requester H. Emission at the settlement tick is taken as 5 credits — 2 per unit of role weight when C (weight 1) and D (1.5) settle together. The reference implementation reproduces every figure.

**Setup.** H posts $q$ with $\beta=45$. A bids $B=40$, $\tau=8$, and locks $G=20$; H pays $40+10=50$. At $t=1$ A posts $q'$ with $\beta'=6$, locking $6+5=11$; B bids $B'=5$, $\tau'=3$, locks $G'=3$; 5 moves to escrow and 1 is released. B's work costs 3; A's own costs 12; C and D each cost 3.

| Tick | Event |
|---|---|
| 0 | A awarded; due by 8 |
| 1 | $q'$ posted and awarded to B; due by 4 |
| 1–3 | B executes and submits with evidence |
| 3 | A accepts $q'$: rejection bond released; B pending; $q'$ window to 13 |
| 4 | A submits $q$; C assigned, locks 5 |
| 6 | C: $\mathsf F$, reimbursed 3 from the deposit; A pending, window to 16; audit rolled: D assigned, blind; vesting suspended |
| 8 | D: $\mathsf F$, reimbursed 3; agrees; suspension lifted |
| 13 | $q'$ vests: B paid 5, $G'$ released |
| 16 | $q$ vests, H silent: A paid 40, $G$ released; deposit remainder $10-6=4$ split 2/2; emission C 2, D 3; bonds released; reliability and duty credit vest |

**Nets.** A $+23=40-12-5$; B $+2$; C $+4$; D $+5$; H $-50$; $\Omega$ untouched. Escrow: in 50 $=40+6+4$ out. Grade of $q$: procedural (an audit occurred); of $q'$: procedural.

**Variants** — each reproduced in the test suite: rejection and appeal (A $+23$, C $-5$: bond pays A's fee and burns 3; E and F 3 each); appeal of a $\bot$ with the objection rejected (same figures) and upheld (A bears the fee, final $\mathsf N$, A $-12-2-20$); pool exhaustion (A withdraws at 6, forfeits 5, nets $-17$; with $\tau=4$ the deadline falls first and A $-20$); cancellation (kill fee $\min(2,5)=2$ from escrow, 3 returned); nested rejection appealed and overturned (A's rejection bond pays B's fee; B $+2$ as if accepted); shortfall and haircut (deposit exhausted, $\Omega$ advances 5, repaid first, fees scaled by $1/6$); timeout and replacement (3 positions on the path, 4 distinct reviewers); a dispute at the window's last tick (admitted; vest at 14 not 12); a correction after vesting (record and reliability change, no credit moves).

---

## Appendix A. Defaults and initialization

| Parameter | Default | Section |
|---|---|---|
| $W$ / $T_{\mathrm{resp}}$ / $T_{\mathrm{rev}}$ / $T_{\mathrm{evid}}$ / $T_{\mathrm{review}}$ / $T_{\mathrm{wait}}$ | 10 / 2 / 5 / 3 / 5 / 5 ticks | §6, §7.4, §9.3 |
| $G$ | $\lceil0.5B\rceil$, min 1 | §5.3 |
| $G^V$ / $D$ / $K$ | 5 / 2 / 5, frozen per case | §7.2, §7.4 |
| $\varphi$ root / nested; $\omega$ | 10 / 0; 5% of $B$ | §4.3 |
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
| $\varphi_q,\omega_q$ | verification deposit, service fee |
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

Discussion anchors [C0]–[C12] (October 15, 2026) settled the purpose and boundary, fixed-then-floating prices, learned selection and the guarantee, verification and appeal, the reserve and rotation, money entering with requests and emission funding verification, symmetric reviewer liability, reliability versus duty credit, and requesters and delegation. Eight external reviews [R1]–[R8] of v0.2 through v0.9 found, in order: the funding gap, bond-versus-liability and the stamping overclaim; the payout-after-shortfall and indexing gaps; atomicity, occupancy, replacement, cost units and the Ω claims; the interaction defects of those repairs; the boundary defects of those; the follow-through defects; the correction-logic and interface defects; and the consequences of reopening. A ninth review [R9] of v0.10 found no new execution defect in its bounded checks, corrected the "blindness stands" claim to the trade-off stated in §14, and recommended this consolidation and the change discipline of §19. A tenth review [R10] of v1.0 accepted it as the frozen baseline, recommended keeping it frozen, and found four places where the consolidated wording said more or less than the decisions it consolidates — the two senses of "ruling", when a response releases capacity, what moves credit value and whether halting is a consequence or a hypothesis, and the two kinds of shortfall at settlement; each is corrected in place and recorded in Appendix E. The reference implementation, `agentic_sim/`, encodes every rule here with injected decisions, checks the eighteen invariants after every tick, and carries every reviewer's test file verbatim — 156 passing (four added with v1.0.1 for the one permitted operation no suite had exercised, withdrawing an unawarded request), with 24 expected failures each stating why, strict and parameter-exact in both entry points. The `_line` map "The actor and its economic life" (revision 4) records the Section 1 discussion and is superseded by the map of this baseline.

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

## Closing statement

> A request is paid for by the one who makes it, judged first by a reviewer who is bonded on the answer, audited blind, open to appeal and dispute for a window, and then final. The actor commits to a price and a time and bears its own cost. The reviewer earns only when right and loses only what it locked. Verification is funded as the security work it is. Delegation is the same loop one level down, with the requester-actor's rejection bonded and its acceptance its own risk. The human powers the circuit and holds the plug: the orchestrator rules on splits inside the procedure, and only a human overrides it. The record is one record. The reviewer is told what it may answer and nothing it need not know. These are the rules of this version. The engine is corrected to them; they change only by decision; and what they do under self-interest is for runs to show.

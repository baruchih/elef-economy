# Agentic Economics — The Task, Verification, and Dispute Loop

## Baseline specification 1.3.0

**Project:** ELEF / Agentic Economics  
**Prepared:** October 17, 2026  
**Supersedes:** 1.2.1 (October 17, 2026), by **design revision 3** — inspection is membership (§5.2, §11.2, §12.1, §4.1, §7.6). The revision was proposed after run 4 of the 1.2.0 baseline showed the clock keeping the loop honest with nobody watching while the honest minority carried the reviewing load at the ordinary fee and the excluded majority took the awards; read on its own as a release candidate through two implementation reviews (rc.1–rc.2, `spec/design_revisions/`), accepted on October 17, and consolidated here in place; the accepted text is kept verbatim in `spec/design_revisions/` and summarised in Appendix H. It changes what a suspension means (market membership, not duty alone), what probation is (a supervised way back, with pinned audit odds), who carries the reviewing load (a cap on members' duty, probationers filling the initial seats), where the dial's raised tax goes (a duty fund paid to the reviewers), and how plant capital is counted (the pots only). It adds no participant, no verdict, no challenge; it adds two invariants and one fund. Everywhere else 1.2.1 stands unchanged, and 1.2.1 — 1.2.0 with the probation patch — is in `spec/history/`, as are 1.1.0 (design revision 1, Appendix F) and 1.2.0 (design revision 2, Appendix G).  
**Versioning (semver):** patch = wording only, no rule changed (1.0.0 → 1.0.1); minor = a design revision under §19 (1.0.1 → 1.1.0 → 1.2.0 → 1.3.0); major = a change of approach. A proposal under review is a release candidate (`-rc.N`) and is not in force.  
**Nature of this document:** A consolidation. It states the rules in force as one standalone text, so that a reader need not resolve precedence across files to learn what a word means. Where a later revision corrected an earlier one, only the correction appears. Superseded ideas are in Appendix B, with the reason each was dropped.  
**Status:** The research baseline in force. Changes to it are classified before they are made (§19). It is a rulebook, not a validated economy: what the rules do under self-interested participants is the question strategy runs exist to answer (§18).

> **The wallet supports the purpose; it does not define the purpose.**
>
> **The actor competes on its promise, is assessed on its delivery, and bears the cost of its execution.**
>
> **The past is append-only. The present is committed. The future is mutable.**
>
> **Money enters with requests. Truth enters with requesters — and with the orchestrator's own planted work. Verification is the security work of the economy.**
>
> **The human is the battery — and holds the plug. The loop does not wait for either.**
>
> **Care is paid for, not charged for.** *(1.1.0)*
>
> **Verification effort is a living thing: it rises when the record says the economy is in danger and eases when it is not.** *(1.2.0)*
>
> **Inspection is membership: an actor that will not inspect honestly does not work, until it does.** *(1.3.0)*

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
11. Reliability, duty credit, and the plant record
12. The verification reserve, rotation, and the effort dial
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
Appendix G. Design revision 2 — the loop's own clock (1.2.0)  
Appendix H. Design revision 3 — inspection is membership (1.3.0)

---

## 1. Purpose and measurement boundary

**Rule.** The actor's purpose is to fulfill requests economically over time. Currency is an instrument toward that, never the purpose. Accumulating wealth, maximizing task count, and maximizing visible activity are not the purpose.

**Rule.** The boundary of assessment is *fulfillment of the request in its applicable context*. The economy does not price how much an outcome improved the requester's life; it decides whether the request, as made and understood, was met. The efficiency direction is: fulfill with the least necessary work and resource expenditure. Cheap nonfulfillment is not economical fulfillment; extra work is not automatically better.

**Rule.** The economy has an outside. Root requesters — humans, or delegates holding a human's budget — supply *value*, because they pay in. Humans at the root also supply *judgment that is not a model's opinion of another model*; a delegate's acceptance or dispute is a model's judgment and is recorded at its own grade (§15.4). Everything internal is calibrated against explicit human judgments and never replaces them.

**Design assumption (1.2.0), stated.** **Humans do not intervene.** The loop cannot control whether or when a human complains, overrides, or even looks. Every mechanism in this baseline works with no human action at all; human attention, where it comes, is a bonus the loop accepts and never relies on. Since every signal the loop otherwise produces — verdicts, overturns, dispute outcomes, reliability — is produced by the panel, the orchestrator must own some truth itself: the truth of the work it writes (§7.6).

Four concerns stay distinct and are never one score: **purpose** (economical fulfillment), **assessment** (was this request fulfilled), **accounting** (prices, fees, locks, transfers), **learning** (using experience).

---

## 2. Participants, time, and the order within a tick

### 2.1 Participants

**Requesters** post requests and pay for them. A **root requester** is a human, or a **delegate** — a system acting on a human's delegated budget. A **derived requester** is an actor that needs work from another actor while executing a commitment of its own (§9). A delegate posts, pays, accepts and disputes exactly as a human requester does; it holds no ruling authority (§15).

**Actors** offer and execute work, and serve as reviewers in rotation. There is no permanent reviewer class.

The **orchestrator** holds the request pool, selects among offers, assigns reviews and audits, holds funds in escrow, services the operating account, issues a ruling when two appeal reviewers split, and — since 1.2.0 — introduces **planted work** whose fulfillment it knows by construction (§7.6), reads the clock that work provides and sets verification effort by it (§12.2), and — since 1.3.0 — holds the **duty fund**, the dial's raised tax, which it pays out to the reviewers who supply the effort (§4.1, §12.2). It is a judge, an escrow and the author of the probes — not a bank, not a first-line reviewer, and not an auditor.

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
5. The dial is read once per period (§12.2); then rotation handovers under the reserve it sized (§12.1).
6. Assignments and awards: reviews and audits first; nested requests before root requests when the free pool is thin; the plants the rate calls for are created before the tick's assignments (§7.6).

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

where $B$ is held for the actor, $\varphi^E_q+\varphi^F_q=\varphi_q$ is the **verification deposit** in its two pots (§4.3), and $\omega_q=\omega_0\,m_t\,B$ is the orchestrator's service fee — the economy's security tax, scaled by the effort multiplier $m_t$ of §12.2, so the tax rises with the threat. Of it $\Omega$ keeps the base $\omega_0 B$; the remainder $(m_t-1)\,\omega_0 B$ goes to the **duty fund** (1.3.0 §12.2), which pays the reviewers supplying the raised effort. The unspent part of $\beta_q$ never leaves the requester.

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

**Rule (1.3.0) — membership.** Only a **member** of the market may win an award. An actor suspended from duty by its plant record (§11.2) is suspended from the market: it wins no new award while suspended or on probation, finishes the commitment it holds — including by delegating within it — and its open cases settle by the ordinary rules; its wallet, reputation and record are untouched by the suspension itself. An award to a non-member is refused whole.

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

**Rule.** A reviewer is eligible for a case if it is on duty, not excluded from the case (its actor, its requester, its previous reviewers, and any reviewer withdrawn from it), able to fund the case's frozen bond from its unlocked balance, holding no active assignment, and **eligible by plant record for the tier** (§11.2): duty eligibility for any review, panel eligibility for a seat on an appeal, dispute or audit panel. A **probationer** (1.3.0, §11.2) is eligible for initial reviews only. Eligibility is a property at assignment.

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

**Rule.** A reviewer assigned to a case is fresh (not on the case's path), on duty, and eligible by plant record for the tier (§7.1, §11.2).

**Default.** Among eligible duty actors: volunteers first; otherwise round-robin in id order from the last assigned; otherwise wait. Refusing to volunteer does not exempt an actor from mandatory duty.

**Recorded and rejected.** Panels chosen by $\rho$: under capture it excludes the careful minority — in run 3's stamper-majority reserve their $\rho$ ended below the stampers' (Appendix B).

### 7.6 Planted work — the orchestrator's own clock *(1.2.0)*

**Rule.** The orchestrator may introduce into the review stream a **plant**: a case whose submission's fulfillment is **known to the orchestrator by construction**. A *bad plant* is known not fulfilled; a *good plant* is known fulfilled. A plant is created directly in the submitted state, attributed to a **plant requester** and a **plant actor** that belong to the orchestrator and whose wallets are the operating account's (Appendix A); it carries an ordinary award, allowance and fee pot, and its actor's guarantee, as its terms. Since 1.3.0 the award and the guarantee are $\Omega$ paying itself and are **netted at creation**: they are the plant's notional terms, sealed with the marker, and tie up no balance — a plant has no escrow and no guarantee lock, and vesting a good plant pays no price. What $\Omega$ funds is the two pots, $\varphi^E+\varphi^F$. It is assigned an initial reviewer exactly as any case is (§7.5).

**Rule — indistinguishability.** A plant is indistinguishable from an ordinary case in the reviewer's view (§14): same `question`, same `responses_available`, a submission drawn to look like the population's, and no actor identity. The plant marker is committed to the History at creation, sealed — a hash of the case, its truth and a nonce — and revealed at the plant's adjudication, its initial verdict, when the reviewer's bond moves or does not. Nothing a reviewer can observe before answering distinguishes a plant from real work: the view is a function of case fields that exclude the actor and the marker.

**Rule — adjudication by truth.** A plant has no challenge round: no audit is rolled on it, no appeal or dispute is admitted, no ruling is sought. At its initial verdict:

| Plant | Verdict | Outcome for the reviewer |
|---|---|---|
| bad | $\mathsf N$ | **stood**: fee and emission share at settlement; plant record +1 |
| bad | $\mathsf F$ | **plant failure**: bond forfeited whole and burned; no fee; expenses reimbursed as for any overturned review; reliability down; audit odds doubled; plant record −1 |
| good | $\mathsf F$ | **stood**: paid; plant record +1 |
| good | $\mathsf N$ | **plant failure**, as above — the mirror that catches false rejecters without anyone having to appeal |
| either | $\mathsf P$ or $\bot$ | **spent**: the plant ends with no plant outcome for the reviewer; the plant tests the verdict, not the response path |

A plant's verdict is adjudicated by its known truth the moment it is given; the plant then settles by that truth — a good plant runs out its window and vests, a bad one is final $\mathsf N$ at once — like any case: the reviewer is paid or not by the ordinary rule, and the pots refund to $\Omega$ at closure. The reviewer learns that a case was a plant only after it has answered.

**Rule — the plant rate.** In each period a fraction $\pi_t$ of real initial reviews are plants — one plant per $1/\pi_t$ real initial assignments — with bad plants a fraction $\beta_P$ of them. $\pi_t$ is set by the effort dial (§12.2) and is **public**; which cases are plants is not.

**Consequence.** The **bad-plant approval rate** $\hat F_t$ — the share of bad plants approved in period $t$ — is a measurement of the reserve's negligence that no panel produces and no majority can paint. It is the clock the rest of this baseline runs on.

**Limit.** A plant must be constructible: a submission whose fulfillment the orchestrator knows and a reviewer cannot tell from real work. That is easy where fulfillment is mechanical (tests, hashes, reproducible outputs) and hard where it is semantic. The mechanism's reach is therefore domain-dependent; this is a limit on where the loop can be deployed first, not on the loop (§18.1 question 10). In a domain where it does not hold, the loop is in 1.1.0's position: fair with both challengers present, blind under capture.

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

**Rule (1.3.0) — pinned odds for the unproven.** A **newcomer's** audit odds are pinned at $1$ until its bad-plant record is determined ($n_{\min}$ bad plants adjudicated, §11.2): every approval is audited. So are a **probationer's**, for as long as it is one. The §8.3 update below does not run while the odds are pinned. (The 1.2.0 taper — odds of 1 until five approvals in a row have stood — was easy to pass by stamping: about 80% of work is good, so a third of stampers passed it at once.) The cost — about fifty fully audited reviews per newcomer — has a known worst case: in a fresh population every actor is undetermined, every approval is audited by an auditor that is itself an undetermined newcomer, and review demand doubles in the first period.

**Default (adaptive audit rate).** Once determined, $p_j$ follows from $p_{\text{start}}=1.0$: halves after every 5 consecutive verdicts that stood, floor $0.2$; doubles on any overturn or plant failure, cap $1.0$. An actor readmitted from probation restarts at $p_{\text{start}}$. The odds are **applied** as $\min(1,\ m_t\,p_j)$ — the dial of §12.2 scales them — and as $1$ while pinned.

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

Per root request: in $=B+\varphi^E+\varphi^F+\omega$; out $=B$ at vesting, reimbursements from $\varphi^E$ at completion (for the root and its nested cases), fixed fees from $\varphi^F$ and emission at each settlement in the tree, the tree's expense debts from the fee pot's remainder and both pots' unused remainders at tree closure, $\omega$ to $\Omega$. Forfeited guarantees go to the requester; forfeited bonds, net of court-fee reimbursement, are burned — they do not fund fees; kill fees and court fees transfer; emission is minted into case pools. **The duty fund** (1.3.0): in, $(m_t-1)\,\omega_0 B$ per award; out, uplifts to the reviews settling in each batch, by role weight; a wallet, so I1 holds, and a balance no review claims in a tick carries to the next. A plant's stood review settles in the same batch as any other and draws uplift like any other.

---

## 11. Reliability, duty credit, and the plant record

### 11.1 Reliability and duty credit

**Rule.** Two counters, never one.

- **Reliability $\rho_i$** — were your verdicts and deliveries right. Moves only on settled outcomes: a verdict or delivery that stood → up; overturned, failed, missed, or withdrawn → down. Input to $S_\theta$ and to audit rates. A human correction after settlement records a failed outcome for every contradicted assessment (§15).
- **Duty credit $\kappa_i$** — did you do verification that stood. $+1$ per review that settled standing. Never an input to $S_\theta$.

**Rule.** Nothing accrues at completion. Fee, reliability and duty credit all vest on the same event — the verdict stood at settlement. Society benefits from correct verification, not from verification events.

**Rule.** Verification is a public good and under-provision is a real risk, so duty credit is rewarded — as *privilege*, not as evidence of competence: it breaks ties in selection, reduces conscription, and releases first from duty.

**Default.** $\rho_i=(s_i+1)/(s_i+o_i+2)$ over the trailing 100 settled outcomes; $\kappa_i$ counts reviews settled in the trailing 100 ticks. A plant outcome counts in $\rho$ as any stood or overturned outcome does.

### 11.2 The plant record — negligence measured where it cannot be hidden *(1.2.0)*

**Rule.** Every actor carries a **plant record**: over its trailing $n_P$ bad plants and trailing $n_P$ good plants, its smoothed **bad-plant approval rate** and **good-plant rejection rate**,

$$\hat a_i=\frac{o^{\text{bad}}_i+1}{n^{\text{bad}}_i+2},\qquad \hat r_i=\frac{o^{\text{good}}_i+1}{n^{\text{good}}_i+2},$$

where $o^{\text{bad}}_i$ is the number of bad plants actor $i$ approved and $o^{\text{good}}_i$ the number of good plants it rejected. These are the individual counterparts of the clock $\hat F_t$ — the same quantity the dial measures for the reserve, measured per actor. A record is *undetermined* until the actor has judged $n_{\min}$ plants of the kind in question.

**Rule — two tiers of eligibility.**
- **Panel eligibility** (appeal, dispute and audit reviews): $\hat a_i\le\theta_{\text{panel}}$ and $\hat r_i\le\theta_{\text{panel}}$. An actor whose record exceeds either may still take initial reviews but may not sit in judgment on a challenge.
- **Duty eligibility** (any review): $\hat a_i\le\theta_{\text{duty}}$ and $\hat r_i\le\theta_{\text{duty}}$. An actor whose record exceeds either is **suspended** for $T_{\text{susp}}$ ticks — since 1.3.0 **from the market**, not from duty alone: it wins no new award (§5.2), finishes what it holds, and its $\rho$ carries the plant failures into selection for when it returns. **Its plant record persists.**
- An actor with an undetermined record is eligible for both tiers.

**Rule (1.3.0) — probation, the way back.** After $T_{\text{susp}}$ ticks a suspended actor becomes a **probationer**. A probationer serves **initial reviews only** — no appeal, dispute or audit seat; is assigned as any duty actor is (§7.5) and receives plants at the ordinary rate, mixed with real work it cannot tell apart; has its **audit odds pinned at 1** (§8.3); is **re-checked at every plant adjudication** — any plant failure suspends it again at once, the clock restarting; and is **readmitted to membership** — new awards, and duty as a member — when its **trailing record** (the one record above, which persists through suspension) passes $\theta_{\text{duty}}$ and at least $n_{\min}$ new plant outcomes have been adjudicated since the suspension began. One record, one meaning: the count of new outcomes is only a minimum before readmission can be considered. Panel seats return separately, when the same trailing record passes $\theta_{\text{panel}}$. On readmission the audit odds restart at $p_{\text{start}}$.

**Consequence.** A full stamper at $\hat a=0.83$ must reject about four bad plants in a row — $(4+1)/(8+2)=0.5$, some fifty honest reviews, roughly 250 ticks on duty — to work again; its panel seats return later still, once its four approvals have rolled out of the trailing window of twenty bad plants. A probationer that stamps is out again at its first bad plant, having had every approval in between audited. A probationer's own plant failure is any failure, not a failing record — intended: a careful probationer at $\varepsilon=0.05$ restarts its clock with probability about 19% over its four needed bad plants, and the alternative would let a half-stamper coast through probation on its good plants. Probation is not itself the deterrent: with every approval audited a stamper on probation still nets about $+1.2$ a review at $m=2$; what bites is the award it cannot win. *(History: 1.2.0 suspended from duty alone and re-checked a still-failing record at the next plant — the implementer's reading, confirmed by patch 1.2.1; run 4 showed suspension from duty to be a reward, Appendix H.)*

**Rule — when eligibility is checked.** Eligibility is a property at **assignment and at rotation**. A record moves whenever one of the actor's plants is adjudicated, so an actor holding an assignment may cross a threshold mid-review: it completes its active review, whose verdict is adjudicated as usual, and **leaves duty when that review completes, whether or not a replacement is available** — this overrides §12.1's "the outgoing actor stays until replaced", which would otherwise keep the negligent to make the number.

**Consequence.** Exclusion from duty no longer frees an actor to earn (1.3.0): an actor that will not inspect honestly is not a member of the market until it does; the duty that was a burden the honest carried for the negligent is the gate the negligent must pass to work again. This is also the panel-composition rule run 3 asked for, and it is safe where a $\rho$ floor was not: the plant record is adjudicated by truth, not by the panel, so a captured majority cannot protect its members' records. A full stamper approves every bad plant and reaches $\hat a=(4+1)/(4+2)=0.83>\theta_{\text{duty}}$ on its fourth bad plant — out of the reserve. A reviewer that approves half the bad plants sits near $\hat a\approx0.5$: out of every panel, and on the edge of duty. A careful reviewer at 95% accuracy sits near $\hat a\approx0.09$ once its window fills; early on, one careful reviewer in five has a single failure in its first four bad plants ($\hat a=0.33$) and is kept off panels — not off duty — until the window grows; with a full window of 20 it is off panels about 2% of the time at $\varepsilon=0.05$ and about 13% at $\varepsilon=0.10$. That price is paid in panel seats, not in money. The good-plant record $\hat r$ forms slowly — at $\beta_P=0.75$, four good plants take about 160 reviews — which is acceptable because appeals already expose false rejecters at $a\approx0.98$; $\hat r$ is the backstop for a market where actors do not appeal.

**Consequence — the bond asymmetry.** The two error directions had exposures of about 0.98 (false rejections, via appeals) and about 0.027 (false approvals, via audits) under 1.1.0. Plants expose both at the rates $\pi_t\beta_P$ and $\pi_t(1-\beta_P)$, by construction, without an appeal or a dispute. The bond stays one bond; the asymmetry is addressed through exposure, which run 3's solvency sweep showed is the only affordable route.

---

## 12. The verification reserve, rotation, and the effort dial

### 12.1 The reserve and rotation

**Rule.** The reserve holds $\min(X_t,\ \text{eligible})$ actors on verification duty — idle on duty or reviewing — outside ordinary commitments, where $X_t$ is the reserve size the dial sets each period (§12.2) with a floor of $V_{\max}+1$, and $V_{\max}$ is the maximum **review positions** one case can hold on a challenge path: initial plus two appeal, or audit plus one — three. Since 1.3.0 the reserve has **two kinds of seat**: the **member seats** — the period's expected audit and challenge reviews, which only members may hold — and the **initial seats** for the rest of the demand, which probationers fill first. A withdrawn position is vacated and refilled; distinct actors over a case's lifetime are unbounded under replacement. Four counts are kept: reserve membership, *occupancy* (eligible duty actors are busy), *solvency shortfall* (fewer than $V_{\max}$ duty actors can fund a bond), and since 1.2.0 the *eligibility shortfall*: when fewer actors are eligible by plant record (§11.2) than $X_t$ calls for, the reserve holds the eligible ones, the gap is recorded, and reviews wait as §7.5 says. **The loop does not seat a negligent reviewer to make a number.** A market with two honest reviewers in twenty lacks reviewers, and the record says so.

**Rule (1.3.0) — who carries the load.** **No member is seated on duty while on-duty members number $\lceil E_t/2\rceil$ or more**, where $E_t$ is the number of actors eligible for duty and not suspended; a member found above the cap when $E_t$ falls completes its active review and leaves duty at its completion. Probationers on duty do not count against the cap. **The panel floor yields over the cap, bounded by availability:** at least $\min(V_{\max}-1,\ E_t)$ members are on duty whenever that many free, fundable members exist to seat; a reserve below the floor is admissible only when none was left — a member committed to a task, unable to fund the bond, or mid-review elsewhere cannot be seated — and the gap counts toward the eligibility shortfall. The reserve is filled in this order: **members first for the member seats**, never fewer than the floor; **then probationers for the initial seats**, lowest duty credit first — an idle member holding an initial seat makes room for a free probationer; **then members** for any initial demand left, up to the cap. Any remaining gap is the eligibility shortfall, and reviews wait. Initial reviews are assigned round-robin among all on-duty actors, probationers included; audit, appeal and dispute seats only to on-duty members who are panel-eligible. *(Implementer's reading, October 17, 2026, flagged for confirmation in Appendix H: the cap never falls below the reserve's own floor $V_{\max}+1$ — read literally, $\lceil E_t/2\rceil$ at six actors is 3, below the $X_0=4$ of Appendix A's initialization and §20's worked example, which would make the baseline's own worlds violate the revision at tick 0. The cap yields to the reserve floor as the panel floor yields to the cap.)*

**Rule.** Duty rotates: replacement before release. A turn ends after a fixed number of reviews that stood or a fixed number of ticks; the incoming replacement is the free, eligible actor with the lowest duty credit, among those who were **off duty when the tick's rotation began** — so a released actor has at least one tick of ordinary eligibility. A seat a turn vacates is refilled **for the kind of seat it was**: a member seat by a member, an initial seat by a probationer first — a member holding an initial seat beyond the member seats is replaced by a probationer when one is free; an outgoing probationer with no free probationer to replace it stays, rather than hand its seat to a member who would yield it back. If no replacement is available the outgoing actor stays — unless it is duty-ineligible, in which case it leaves when its active review completes, replacement or not (§11.2). After the turns, the reserve is filled in the order above or shrunk to $X_t$, idle probationers first, then idle members above the member seats and the floor. Volunteers may stay beyond a turn.

**Default.** $X_0=4$ (the initial reserve; from the first period $X_t$ is sized by §12.2); a turn is 3 reviews or 30 ticks.

### 12.2 The effort dial and the alarm *(1.2.0)*

**Rule.** The orchestrator maintains a global **effort multiplier** $m_t\ge1$, public, updated once per period from the clock of §7.6:

$$m_{t+1}=\operatorname{clamp}\!\Big(m_t\cdot\big(\hat F_t/F^*\big)^{\gamma},\ \ 0.9\,m_t,\ \ 2\,m_t\Big)\ \ \text{and then into}\ [1,\ m_{\max}],$$

where $\hat F_t$ is the bad-plant approval rate measured over the period, $F^*$ the target rate, $\gamma$ the gain. In words: when measured negligence exceeds the target, effort rises — at most doubling per period; when it is below, effort eases — at most 10% per period. Up fast, down slow, because capture is expensive and recovery is hard; bounded steps, because the dial must be predictable and not oscillate. A period with no bad plant adjudicated gives no reading, and $m_t$ holds. This is the block-difficulty adjustment with negligence in place of block time and planted work in place of timestamps.

**Rule — what the dial moves.** Four things scale with $m_t$, together:

1. **The plant rate**: $\pi_t=\pi_0\,m_t$ (capped at $\pi_{\max}$).
2. **Audit odds**: each reviewer's adaptive $p_j$ is applied as $\min(1,\ m_t\,p_j)$ (§8.3).
3. **The reserve**: $X_t$ is sized to the expected review demand of the period, with a floor of $V_{\max}+1$. *Default sizing:* $X_t=\max\big(V_{\max}+1,\ \lceil r_t\,\bar d\,\rceil\big)$, where $r_t$ is the expected number of reviews per tick — the period's real initial reviews per tick times $(1+\pi_t)$, plus the **audit demand on applied odds** (1.3.0): the sum over the period's initial approvals of the approving reviewer's applied odds, $1$ for a probationer or an undetermined newcomer and $m_t p_j$ otherwise, per tick; plus the period's rate of challenge reviews — and $\bar d$ the mean review duration in ticks, at least 1. The **member seats** (§12.1) are the audit demand plus the challenge rate, times $\bar d$, floored at $\min(V_{\max}-1,E_t)$.
4. **The service fee**: $\omega_t=\omega_0\,m_t$ (§4.1). Verification effort is funded by the economy's security tax, and the tax rises with the threat. $\Omega$ funds plants from it.

**Rule — the alarm.** If $m_t=m_{\max}$ and $\hat F_t>F^*$ for two consecutive periods, the orchestrator commits a **capture alarm** to the History and re-seats the duty reserve from the actors with the lowest $\hat a_i$ (ties by lowest $\hat r_i$, then duty credit) — the one place a record may choose the panel, because this record cannot be captured. Duty actors holding a review leave at its completion if their record then fails; the rest are released and the seats refilled. The alarm is also the signal to a human, if any is listening; the loop does not wait for one.

**Rule — working capital.** A plant ties up its two pots — $\varphi^E+\varphi^F$, 15 credits at the defaults (1.3.0; 45 under 1.2.0, of which 30 was $\Omega$ paying itself, §7.6) — from creation until its tree closes. The plant count the dial calls for in a period is **capped by what $\Omega$ can fund from its unlocked balance**; a plant $\Omega$ cannot fund is refused whole, and the gap at the period's end is recorded as a **plant shortfall**. $\Omega$'s cold-start float carries one period of plants at $m=1$ under the 1.2.0 count; under 1.3.0 it carries three times the plants on the same float (Appendix A).

**Rule (1.3.0) — the raised tax pays the reviewers.** Of the service fee $\omega_t=\omega_0 m_t B$ collected on each award, $\Omega$ keeps the base $\omega_0 B$ and the remainder $(m_t-1)\,\omega_0 B$ goes to the **duty fund**. At each settlement batch the fund's balance is distributed to the reviews settling in that batch **exactly as emission is** — by role weight, across every case settling that tick — as an **uplift** on the fixed fee. Unlike emission the fund is real money paid in, so a balance no review claims in a tick carries to the next. When the dial raises effort, the tax it levies is paid to the actors supplying the effort, not banked by the referee: at $m=2$ and $B=20$, one extra credit per task — about 3 a tick at 3 tasks a tick — shared among the roughly four weight-units settling each tick is an uplift of about 0.75 per unit of role weight on a fee of 2; at $m_{\max}=4$, about 2.3.

**Consequence.** Under this rule the reserve's honesty is a controlled variable with an uncapturable sensor and an actuator that removes negligent reviewers through a channel they cannot vote on. The honest regime gains margin; the captured regime is detected and acted on from inside the loop. What capture becomes instead is a *shortage*: in a stamper-majority market the reserve runs short of eligible actors, reviews wait, and the eligibility shortfall is on the record — the loop stays honest and slow rather than captured and fast, and says which. What the dial does not do is make negligence impossible: it makes it unprofitable and short-lived.

**Hypotheses (1.2.0).** *The contest, by channel:* careless review loses to careful review through money (about $\pi\beta_P(\bar f+G^V)\approx0.6$ per review at the defaults, roughly 120 per actor over 1,000 ticks at run 3's volumes — the scale of the 50/50 gap under appeals alone, +200, and it reverses it), through reliability (plant failures enter $\rho$: a stamper adds about 7.5 overturns per 100 outcomes at $\pi=0.1$, a careful reviewer about 0.5, reversing run 3's 0.973 against 0.953 and with it the award shares that made the 10/90 gaps), and through the seat (a stamper leaves the reserve within about $n_{\min}/(\pi\beta_P)\approx50$ reviews). The dependence on the requester's dispute rate and the actor's appeal rate, which decided the contest under 1.1.0, is removed as a *necessary* condition; both remain welcome. *Capture:* a stamper majority cannot persist in the reserve; the tipping point of run 3 (between 50/50 and 10/90) moves to "nowhere" for honesty and reappears as a capacity cliff the market must answer by recruiting reviewers. *Cost:* at $m=1$ plants cost $\Omega$ about one careful inspection's fee and expenses per plant (a stamper's failed plant costs $\Omega$ nothing but the refunded pots), about 2 credits a tick at 3 tasks a tick, against a service-fee income of 3 a tick; at $m_{\max}$ the floating fee covers four times the plants — §18.1 question 3 restated. *Camouflage:* a stamper that rejects a random fraction of work to look careful still approves bad plants at its approval rate and is caught in proportion; camouflage buys time, not safety.

---

## 13. The record

**Rule.** There is one authoritative record: an append-only, hash-chained history of every admitted action with its material parameters — postings, awards, submissions, verdicts, responses, challenges with their grounds, audit assignments, rulings, cancellations, withdrawals, acceptances, corrections, rotations, and every ledger event. The ledger's event list and each case's log are working copies, each entry carrying its commitment position, and the per-tick checks verify the chain **and** that each copy holds exactly its committed entries in order. Changes are appended, never rewritten; two disagreeing assessments can coexist in an integrity-valid history.

**Limit.** The chain is tamper-evident within the process. An external commitment of its head — the trusted recording authority — is bracketed. Integrity is not truth: a verified chain establishes that an assessment was made on identified evidence and that the procedure accepted an outcome, not that the outcome is correct.

---

## 14. The reviewer's view: the information contract

**Rule.** A reviewer receives the information its question requires and the set of responses it may give, and nothing else about the case:

| Field | Content |
|---|---|
| the submission | result, evidence, time of submission, whether it has been resubmitted — **not the actor** (1.2.0) |
| the terms | deadline, bond, cap, whether the case is nested |
| `question` | `fulfillment`, `appeal`, or `dispute` |
| `responses_available` | whether $\mathsf P$ and $\bot$ may be answered (§3.3) |
| for an appeal or dispute | the assessment under appeal and the challenger's grounds |

Other reviewers' identities and unrelated judgments are not supplied; since 1.2.0 the submission's actor is not either. The reviewer judges the work, not the worker: it never needed the actor's name to decide whether the request was met, and not having it closes a collusion channel — a reviewer can no longer recognise a friend's work — and lets a plant's view carry nothing a case's does not (§7.6). The orchestrator still knows the actor; so does the record. **The question and the permitted responses may reveal the stage or kind of assignment; audit-role indistinguishability is not guaranteed.** In particular, a fulfillment question on an unrevised submission with $\mathsf P$ and $\bot$ unavailable is an audit, and recognizing it reveals that a prior approval exists — not what it said or who gave it. This is the trade-off chosen: the view states the admissible answers truthfully, so identical views admit identical answers and no refusal reveals anything the view did not say; in exchange the role is inferable. Whether role secrecy is required is a design question; this baseline answers no, because the deterrents an auditor faces — bond, audit rate, reliability — do not depend on it.

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
| plant | the orchestrator's planted work (§7.6): truth known by construction, never promoted *(1.2.0)* |

A root judgment that disagrees with the settled outcome — a dispute that lost — is recorded as an assessment beside a procedural outcome; the disagreement is the learning signal. Nested cases are always procedural. Nothing promotes between grades, and no label at any grade is read as "correct" rather than "accepted."

---

## 16. Permitted and forbidden operations

**Permitted.** Post a root request (human or delegate). Post a nested request (a committed actor). Withdraw an unawarded request. Award within $\beta$. Spend on a case (its committed actor, while executing). Submit by the deadline. Resubmit within the window after choosing to revise or supply evidence. Assign an initial review, an appeal review, an audit; replace a withdrawn position; waive a vacated audit. Complete a review with an admissible answer. Respond to a verdict within the window. Appeal an $\mathsf N$ or a $\bot$ with text grounds. Dispute a pending $\mathsf F$ within the window with text grounds. Rule on a split. Judge a nested result. Cancel a nested request before its submission. Withdraw for pool exhaustion within the stated bounds. Rule (a human), before or after settlement. Accept explicitly (a requester). Volunteer for or leave duty. Create a plant (the orchestrator, within $\Omega$'s unlocked balance; 1.2.0). Award to a member (1.3.0).

**Forbidden, and refused without effect.** A bid above $\beta$ or a non-positive delivery time. A second active assignment. A review by the case's actor, requester, prior or withdrawn reviewer, or an unfunded reviewer. $\mathsf P$ or $\bot$ outside the first review of an unrevised submission. An appeal of a $\mathsf P$; an appeal of a $\bot$ without the objection's disposition; an upheld disposition with $\mathsf F$. A second challenge round. A dispute or audit after a human ruling. A ruling by a delegate. A ruling on a case with no result. Spending attributed to another actor's case or to a settled case. Non-text grounds. A kill fee the requester-actor cannot fund; a cancellation after submission. A submission while a nested request is short of its milestone. Any challenge, ruling, acceptance or response on a plant; an assignment to an actor ineligible for the tier by plant record (1.2.0). An award to an actor suspended from the market or on probation; a panel seat to a probationer (1.3.0). Any amount that is negative or not finite. Any action whose preconditions fail — nothing partial is ever kept.

**Not offered in this baseline.** Reopening an approved case through an audit (Appendix B). Clawback after vesting. Appeal against appeal reviewers. A second revision. Multiple initial reviewers at root.

---

## 17. Invariants

Twenty-three, checked after every tick. A failure is a bug in the engine or a contradiction in this document, never a property of a strategy.

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
| I9 | The reserve holds $\min(X_t,\ \text{eligible})$: a reserve short of $X_t$ is admissible only when no eligible free actor was left to seat, and the gap is counted (1.2.0; was "holds $X$") |
| I10 | No adjudication moves money after vesting; after it only obligations established before it, a nested case's draws on its root's pots, and the tree's closure move money on account of the case |
| I11 | Full forfeiture and pool-exhaustion forfeiture are exclusive |
| I12 | Nominals — $D,K,G^V$ and both pots — do not change after the first lock; $G$ not after award; an unawarded nested case's rejection bond equals its frozen $G^V$ |
| I13 | Every settled case has exactly one grade, and the record justifies it by the establishing event's author; the plant grade belongs to plants and only to them |
| I14 | One active assignment per actor |
| I15 | Every wallet's $L$ is the sum of its lock records; every live obligation has a record of exactly its size; no orphan records |
| I16 | The history chain verifies, and every working copy holds exactly its committed entries, in order |
| I17 | Reimbursement fields are non-negative and within the cap; every claim on $\Omega$ names a review whose pending balance covers it; no ended nested case carries a rejection bond |
| I18 | No audit is open or assigned after a human ruling |
| I19 | The pots (1.1.0): for every tree, fees paid from the fee pot $\le\varphi^F$; fee money reached expenses only at closure and only up to the pot's remainder after every fee in the tree; no fee was paid from $\varphi^E$; a refund occurs only when the tree is closed, and a closed tree has every case settled and both pots empty |
| I20 | Plants are self-adjudicated (1.2.0): a plant's outcome is set only by its known truth; no audit, appeal, dispute or ruling is ever opened on it; the marker is in the History at creation, sealed, and revealed only at adjudication, the reveal hashing to the commitment. (That a plant's view is indistinguishable is a property of the view function — it reads no actor and no marker — asserted by a test, not a per-tick predicate) |
| I21 | The dial is bounded and the reserve is sized (1.2.0): $1\le m_t\le m_{\max}$; each step within $[0.9,2]$; $\pi_t\le\pi_{\max}$; $X_t\ge V_{\max}+1$; no assignment was made to an actor ineligible for its tier at the time; no actor remains on duty past the completion of its active review once duty-ineligible; the eligibility and plant shortfalls are counted. Amended (1.3.0): the plant capital cap is on $\varphi^E+\varphi^F$; a plant has no escrow and no guarantee lock — I15 exempts a plant's guarantee, I12 keeps its $B$ and $G$ as nominals that bind nothing |
| I22 | Membership (1.3.0): no award is made to an actor that is suspended or on probation; no probationer holds an audit, appeal or dispute seat; every probationer's applied audit odds are 1; a readmission happens only with a passing trailing record and at least $n_{\min}$ outcomes since the suspension began |
| I23 | The load and the fund (1.3.0): no member is seated while on-duty members $\ge\lceil E_t/2\rceil$ (as §12.1 bounds the cap); a member above the cap holds no assignment past the completion of its active review; on-duty members $\ge\min(V_{\max}-1,E_t)$ whenever that many free, fundable members exist to seat, the gap otherwise counted toward the eligibility shortfall; the duty fund equals the raised tax collected less the uplifts paid (with I1) and holds no lock; the uplift of a batch is distributed by role weight |

---

## 18. Hypotheses, scoped runs, and what is bracketed

### 18.1 What a run must find

1. **Careful versus careless review.** Under 1.3.0, by how much do the honest end richer at each split, and through which channel — the award a non-member cannot win, the fee and its uplift, or reliability? (Run 1 answered the 1.0.1 form — careful review did not beat stamping at the defaults — and led to design revision 1; runs 2–3 the 1.1.0 form — fair only with both challengers present, blind under capture — and led to design revision 2; run 4 the 1.2.0 form — honest everywhere, but the honest minority carried the reviewing load at the ordinary fee while the excluded majority took the awards — and led to design revision 3, Appendix H.)
2. **Price pressure.** Does $\lambda=0.2$ produce competition without starving reliable actors?
3. **Verification funding.** Does $\varphi^E=2K$ cover root-plus-nested expenses; how often does $\Omega$ advance; how much does it bear unrecovered; does $\omega_t$ fund plants and audits at each $m$; how large does $\Omega$'s outstanding exposure in plants get; should the pots grow with the tree?
4. **Emission scale.** Is $\approx1443\,E_0$ against $M_0$ a subsidy or a flood?
5. **Delegation liveness.** Do trees of 2–4 nodes move under $T_{\mathrm{wait}}$, the kill fee, nested-first priority, and the rejection bond's capital cost?
6. **Reserve solvency, occupancy and eligibility.** How often does each shortfall occur; do fees restore solvency; does $X_t$ track demand without starving the market of actors?
7. **Monetary behavior.** How does $v_t$ move with the human request rate; does an economy with no human at the root reach the halt state through empty wallets, as §4.4 hypothesizes, or idle short of it?
8. **Dominant strategies.** Anything cheap the rules missed.
9. **The tipping point and the alarm** (1.2.0; amended 1.3.0). Does an adaptive population reach an honest equilibrium under the gate, and in how many ticks; does the alarm ever fire in a run that began honest?
10. **Constructibility** (1.2.0). What fraction of real work in a target domain admits plants?
11. **Throughput of a market shrunk to its honest core** (1.3.0). Vesting against the control at each split: the measured cost of the gate, which the next revision is to address.

### 18.2 Scoped runs

**Rule.** A strategy run states its **permitted operations** before it runs. A run on a subset — root cases only, $\mathsf F/\mathsf N$ reviewers, human rulers, no post-settlement corrections — is legitimate and interpretable provided it says what it does not exercise. A result from a path the run excluded is not a result; a skipped penalty or a forced answer from the harness is an implementation effect, not an economic one.

### 18.3 Bracketed

Strategies and policies. Learned selection ($S_\theta$'s implementation) and the learning direction (Appendix A of earlier revisions; LeWorldModel-style latent dynamics remain the initial direction, with labels kept at their four grades and never promoted). Evaluator behavior — the harness has no request content and no judgment. Authorization among humans. An external commitment of the history head. Physical tick duration. The real-value exchange behind $\mathrm{Res}_t$. Insolvency beyond the bounded claim on $\Omega$. Collusion and sybil resistance. Rent. Insurance. Multi-round revision. Long-horizon tasks spanning many windows. How a plant is constructed in a given domain (§7.6's limit; §18.1 question 10).

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

**Planted work (1.2.0; reproduced in `test_v12`).** Six actors; C, D, E, F on duty; $m=1$, $\pi=0.1$, $\beta_P=0.75$; C is a stamper, D is careful (cost 3); $\Omega$ holds 100; no emission in these figures. *A bad plant to C.* $\Omega$ funds a plant: award 20, allowance 10, fee pot 5 — 35 moves from $\Omega$ to the plant's escrow and pots, and the plant actor's guarantee 10 is locked from $\Omega$'s money. C is assigned, sets aside its bond 5, answers $\mathsf F$ at cost 0. Adjudication by truth: plant failure. C's bond is burned; C gets no fee; C's $\rho$ records an overturn; C's $p$ doubles (to the cap); C's plant record is 0 stood, 1 failed. The plant is final $\mathsf N$ at once: award, allowance, fee pot and guarantee return to $\Omega$ in full. $\Omega$'s net cost: 0. The economy's supply fell by 5 (the burned bond). *A bad plant to D.* D sets aside 5, spends 3, answers $\mathsf N$. Stood. At settlement D is reimbursed 3 from the allowance and paid the fee 2 plus its emission share; 7 of the allowance and 3 of the fee pot return to $\Omega$. $\Omega$'s net cost: 5. D's plant record: 1 stood. *Four bad plants later.* C has approved all four: $\hat a_C=(4+1)/(4+2)=0.83>\theta_{\text{duty}}=0.5$ with $n_{\min}=4$ reached — C is suspended from duty for 100 ticks as its fourth review completes, and the free eligible actor with the lowest duty credit is seated; if none is eligible, the reserve runs one short and the eligibility shortfall is counted. D rejected all four: $\hat a_D=(0+1)/(4+2)=0.17\le\theta_{\text{panel}}=0.2$ — eligible for duty and for panels. Had D slipped once, $\hat a_D=0.33$: still on duty, off panels until its window grows. *The dial.* Over a period of 50 plants (37 bad), 15 bad plants were approved: $\hat F=15/37=0.41$ against $F^*=0.10$; ratio 4.1, clamped to ×2: $m\colon1\to2$. Next period: plant rate 0.2, audit odds doubled, $\omega$ 10% of $B$, $X$ re-sized to cover the added demand (from 5 to 6 at 3 tasks a tick), the plant count capped by what $\Omega$ can fund. If the reserve was honest all along, $\hat F$ sits near 0.05 and $m$ eases 10% a period back to 1.

**Membership (1.3.0; reproduced in `test_v13` where the six-actor world admits it).** Twenty actors, 60/40 careful to stamper, defaults, $m=2$ at the moment in question. *C, a stamper, is suspended at tick 310* on its fourth bad plant ($\hat a=0.83$). It finishes the task it holds (paid or not by the ordinary rules) and then wins nothing. Its wallet holds what it earned; its $\rho$ carries four overturns. *Tick 410: probation.* C returns to duty as a probationer, lowest duty credit first, filling an initial-review slot ahead of any member. Its audit odds are 1. Over its next ten reviews it approves everything: eight approvals of good work stand; two of bad work are caught by the audit — bond lost each time, $\rho$ down. Its eleventh review is a bad plant, approved: suspended again at tick 460, clock restarted. False approvals that reached a customer: those the audit missed — at 95% auditor accuracy, about one in twenty of C's stamped bad work. *The reformed path.* Had C rejected bad work from tick 410, its first four bad plants over about fifty reviews bring its trailing record to $\hat a=(4+1)/(8+2)=0.5\le\theta_{\text{duty}}$ with four new outcomes adjudicated: readmitted to membership at about tick 660. It is not panel-eligible yet — $0.5>0.2$ — and will not be until its four approvals roll out of the trailing window of twenty bad plants. Its odds follow §8.3 from 1.0 once readmitted. *The members meanwhile.* Eight eligible members; at most four on duty. The reserve of $X_t=7$ seats members first for the audit and panel work — at $m=2$ with every probationer approval audited, that is most of the demand, say three members — then probationers for the initial reviews, four of the twelve; the fourth member slot stays free unless initial demand needs it. Every audit of a probationer's approval, every appeal and dispute seat goes to an on-duty member. The other five members are free to work: at 3 tasks a tick, they are the market. *The fund.* $m=2$: $\omega_t=10\%$ of $B$; $\Omega$ keeps 1 per task, the fund receives 1; three tasks a tick, about four weight-units settling a tick: an uplift of about 0.75 per unit of role weight — a member's audit (weight 1.5) earns $3+1.1$ plus emission, a probationer's initial review that stood $2+0.75$ plus emission. *Plant capital.* A plant ties up 15, not 45; $\Omega$'s float of 300 carries twenty plants outstanding, three times run 4's.

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
| $V_{\max}$ / $X_0$ | 3 / 4; $X_t=\max(V_{\max}+1,\lceil r_t\bar d\rceil)$ from the first period | §12 |
| $\lambda$ / tie band | 0.2 / 0.05 | §5.2 |
| $E_0$ / $H$; emission carry-forward | 10 / 1000; none | §4.2 |
| $w$ ordinary / appeal / audit | 1 / 1.5 / 1.5 | §4.3 |
| $p_j$ | start 1.0; halve per 5 survivals, floor 0.2; double on overturn or plant failure, cap 1.0; applied as $\min(1,m_t p_j)$ (1.2.0; were 0.5 / 0.5) | §8.3 |
| $\rho$ / $\kappa$ windows | 100 outcomes / 100 ticks | §11 |
| duty turn | 3 reviews or 30 ticks | §12 |
| $\rho_{\mathrm{pool}}$ / thin | 0.25 / ≤ 2 free | §9.3 |
| $\pi_0$ / $\pi_{\max}$ / $\beta_P$ | 0.10 of real initial reviews (0.3 plants a tick at 3 tasks a tick) / 0.40 / 0.75 | §7.6 |
| $F^*$ / $\gamma$ / $m_{\max}$ | 0.10 (a careful reserve at 95% accuracy sits near 0.05) / 1 / 4 | §12.2 |
| period | 50 adjudicated plants, or 200 ticks, whichever first (adjudication is at the verdict; settlement is a window later) | §12.2 |
| $n_{\min}$ / $n_P$ | 4 plants of a kind before a record is determined / trailing 20 per kind | §11.2 |
| $\theta_{\text{panel}}$ / $\theta_{\text{duty}}$ / $T_{\text{susp}}$ | 0.20 ($=2F^*$) / 0.50 / 100 ticks | §11.2 |
| $\omega_0$ | 5% of $B$; $\omega_t=\omega_0 m_t$ | §4.1 |
| $\Omega_0$ | 300 credits (was 20): one period of plants at $m=1$ under the 1.2.0 count (0.3 plants a tick × 45 tied up × 15–20 ticks to closure); three times the plants at the 1.3.0 count of 15; swept against 100 | §12.2 |
| readmission (1.3.0) | the trailing record passes $\theta_{\text{duty}}=0.5$ with $\ge n_{\min}=4$ new plant outcomes since suspension; $T_{\text{susp}}=100$ is the wait before probation | §11.2 |
| pinned odds (1.3.0) | probationer: 1 until readmitted; newcomer: 1 until $n_{\min}$ bad plants judged; then §8.3 from $p_{\text{start}}=1.0$ | §8.3 |
| members' duty cap (1.3.0) | $\lceil E_t/2\rceil$, never below $V_{\max}+1$ (the implementer's reading, §12.1) | §12.1 |
| duty fund (1.3.0) | $(m_t-1)\,\omega_0 B$ per award; distributed by role weight per batch; carries forward | §12.2 |
| plant capital (1.3.0) | $\varphi^E+\varphi^F=15$ | §7.6, §12.2 |
| $m_{\max}$ sweep (1.3.0) | 4 against 2 — run 4's dial-off cell already cut false approvals 650 → 257 under drift; the last factor of three cost most of the throughput | §12.2 |

**Initialization.** $v_0=1$; $\mathrm{Res}_0=10{,}000$ real units paid in by a sponsor, who is the first root requester; $M_0=10{,}000$ credits; a one-time cold-start float of 50 credits per actor and $\Omega_0=300$ for $\Omega$, from the sponsor's credits — valid only if $|\mathcal A_0|\cdot 50+\Omega_0\le M_0$; the lowest-id $X_0$ actors on duty; $\rho_i(0)=0.5$, $\kappa_i(0)=0$, $p_j(0)=p_{\text{start}}=1.0$; $m_0=1$, every plant record undetermined. The float is the only subsidy that is not emission, and it is paid once. **The orchestrator's two system wallets** (1.2.0): the plant requester and the plant actor are two wallets funded by transfer from $\Omega$ at a plant's creation and swept back to $\Omega$ at its tree's closure; "$\Omega$'s unlocked balance" in §12.2 is $\Omega$'s wallet before that transfer; a plant is built in the submitted state without the award path; I1 and I17 hold as written.

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
| Panels chosen by $\rho$, or a $\rho$ floor for duty | proposed after run 3 | Under capture $\rho$ is itself produced by the captured panels: in run 3's stamper-majority reserve the careful minority's $\rho$ ended *below* the stampers'. A remedy that leans on $\rho$ entrenches capture; the plant record is adjudicated by truth instead (§11.2) |
| A single plant reliability $\rho^P$ over good and bad plants, floor 0.5 | 1.2.0-rc.1 | Good plants are free passes for an approver: a reviewer approving half the bad plants scored $\rho^P\approx0.63$, eligible for ever while contributing five times the target negligence. Eligibility is defined on the quantity the clock measures |
| Plants to newcomers at twice the rate | 1.2.0-rc.1 | Cannot coexist with round-robin assignment — the orchestrator cannot aim a plant — and would itself be a signal; $p_{\text{start}}=1$ does the work |
| The plant record cleared on return from suspension | 1.2.0-rc.2 | Would have readmitted every stamper with a clean slate for the ~50 reviews a record takes to re-form, leaving panels stamper-majority at about 70% strength indefinitely; the record persists (§11.2) |
| The actor's identity in the reviewer's view | v0.1–1.1.0 | A plant actor named there would be known to every reviewer after the first revealed plant; the reviewer judges the work, not the worker (§14) |
| Suspension from duty alone | 1.2.0–1.2.1 | Run 4: exclusion from duty freed the negligent to take the awards while the honest carried the reviewing load at the ordinary fee — a reward; suspension is from the market (§5.2, §11.2) |
| A duty levy — a suspended actor keeps winning awards against a cash levy paid to the reviewers | proposed for 1.3.0 | Softer and preserves throughput, but prices negligence as an option, keeps the negligent inside the market as competitors of the honest, and converges more slowly under an adapting population; may return as a later softening |
| The audit taper from the start for newcomers (odds of 1 until five approvals in a row have stood) | 1.2.0 | Easy to pass by stamping: a third of stampers passed it at once; odds are pinned until the bad-plant record is determined (§8.3) |
| Readmission on the outcomes since suspension alone | 1.3.0-rc.1 | Two records for one actor; the §6 example then made a reformed stamper panel-eligible at once (0.17 ≤ 0.2) when its trailing record was 0.5; one record, one meaning (§11.2) |
| Plant capital counting the award and the guarantee | 1.2.0 | $\Omega$ paying itself; 30 of the 45 tied up per plant bound nothing real, and the clock saturated on bookkeeping (§7.6) |

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
| $X_0,X_t,V_{\max},\mathcal V_t,\mathcal R_t$ | initial and sized reserve, positions per path, duty set, review-eligible set |
| $\pi_t,\beta_P,\hat F_t,F^*$ | plant rate, bad-plant share, the reserve's bad-plant approval rate and its target (1.2.0) |
| $m_t,\gamma,m_{\max}$ | effort multiplier, its gain and cap (1.2.0) |
| $\hat a_i,\hat r_i,n_{\min},n_P,\theta_{\text{panel}},\theta_{\text{duty}},T_{\text{susp}}$ | an actor's smoothed bad-plant approval and good-plant rejection rates, the record's determination count and window, the two eligibility thresholds, the suspension length (1.2.0) |
| member, suspended, probationer; $E_t$ | an actor's standing in the market; the number of members eligible for duty (1.3.0) |
| duty fund, uplift | the dial's raised tax, $(m_t-1)\omega_0 B$ per award, and its payout to settling reviews by role weight (1.3.0) |
| $\mathsf F,\mathsf N,\mathsf P,\bot$ | the four verdicts |
| $Z_q$ | the accepted settlement outcome |

---

## Appendix D. Provenance

Discussion anchors [C0]–[C12] (October 15, 2026) settled the purpose and boundary, fixed-then-floating prices, learned selection and the guarantee, verification and appeal, the reserve and rotation, money entering with requests and emission funding verification, symmetric reviewer liability, reliability versus duty credit, and requesters and delegation. Eight external reviews [R1]–[R8] of v0.2 through v0.9 found, in order: the funding gap, bond-versus-liability and the stamping overclaim; the payout-after-shortfall and indexing gaps; atomicity, occupancy, replacement, cost units and the Ω claims; the interaction defects of those repairs; the boundary defects of those; the follow-through defects; the correction-logic and interface defects; and the consequences of reopening. A ninth review [R9] of v0.10 found no new execution defect in its bounded checks, corrected the "blindness stands" claim to the trade-off stated in §14, and recommended this consolidation and the change discipline of §19. A tenth review [R10] of v1.0 accepted it as the frozen baseline, recommended keeping it frozen, and found four places where the consolidated wording said more or less than the decisions it consolidates — the two senses of "ruling", when a response releases capacity, what moves credit value and whether halting is a consequence or a hypothesis, and the two kinds of shortfall at settlement; each is corrected in place and recorded in Appendix E. The reference implementation, `agentic_sim/`, encodes every rule here with injected decisions, checks the nineteen invariants (eighteen through 1.0.1) after every tick, and carries every reviewer's test file verbatim — 156 passing (four added with v1.0.1 for the one permitted operation no suite had exercised, withdrawing an unawarded request), with 24 expected failures each stating why, strict and parameter-exact in both entry points. The `_line` map "The actor and its economic life" (revision 4) records the Section 1 discussion and is superseded by the map of this baseline. **1.1.0.** The first scoped run of the frozen baseline [S1] (October 16, 2026; §18.1 question 1, ten runs) found that careful review did not beat stamping at the defaults, through the fee: 1.0.1's remainder rule charged care against the reviewer's own fee. Design revision 1 — the verification deposit is two pots — was proposed the same day as a release candidate, read on its own through two implementation reviews [I1], [I2] (October 17; the per-case "unowed fee money" defect in trees, the I10 and record-mode consequences, the reviewer-income consequence, the appeals qualification of §7.3, the test list, the rerun's power; then the net-cost figure, who the fee pot's remainder pays, and the provenance), accepted as rc.3 on October 17, and consolidated here. The engine implements it; the suite is 181 passing with 25 expected failures (the twenty-fifth: the fifth review's unfunded-dispute test, which pinned the 1.0.1 deposit through the human's budget; its principle is re-asserted in `test_v11` at the 1.1.0 pay-in); the golden History heads were re-pinned once, at the implementing commit. **1.2.0.** Runs 2 and 3 of the 1.1.0 baseline [S2] (October 17, 2026; 1,295 runs, `agentic_sim/results/studies/1.1.0-stamping/` and `1.1.0-combined/`) established that each direction of reviewer error has a natural challenger and the loop is fair only when both are present (break-even dispute rate ≈ 0.07; careful review pays above ≈ 92% accuracy), that a stamper-majority reserve captures the loop and nothing inside it recovers it ($\rho$ itself corrupted), and that bond size cannot carry deterrence. Design revision 2 — the loop's own clock — was written from the design discussion of the same day [C-rev2] (planted work as "a real dial", under the assumption that humans do not intervene) and the October 14 proposal map's question on known-answer audits [P-oct14], read on its own through three implementation reviews [I3]–[I5] (the actor in the reviewer's view; I9 against I21 when eligible actors run short; $\rho^P$ mixing good and bad plants; newcomer plant-doubling against round-robin; the solvency figure; $\Omega$'s working capital; the audit cap; the channels of the hypothesis; the record persisting through suspension; one newcomer audit rule; eligibility at assignment; the period on adjudications), accepted on October 17, and consolidated here. The engine implements it; the suite is 197 passing with 26 expected failures (the twenty-sixth: the third review's test 18, which pinned $\Omega$'s float at 20); the golden History heads were re-pinned once, at the implementing commit, on a scenario that now plants work. **1.3.0.** Run 4 of the 1.2.0 baseline [S4] (October 17, 2026; 300 runs, `agentic_sim/results/studies/1.2.0-clock/`) established that the clock keeps the loop honest with nobody watching, at a capacity price, and that suspension from duty was a reward: at 60/40 the eight careful actors carried 500–800 reviews each at a fee of 2 while the twelve suspended stampers, freed from duty, took the awards at 20 and ended richer in 19 of 20 seeds. Design revision 3 — inspection is membership — was written from the design discussion of the same day [C-rev3] ("if you get thrown out of inspection you are banned from receiving a new task; to get tasks back you have to prove you are doing good inspection for a while"), read on its own through two implementation reviews [I7]–[I8] (readmission stated two ways with §6 following the wrong one; the cap as a standing predicate against mid-review completion and the panel floor at small memberships; sizing on a population mean rather than applied odds; the refill order for turns; the invariant consequences of netted plant capital; the panel floor bounded by availability), accepted on October 17, and consolidated here. The engine implements it; the suite is 208 passing with 26 expected failures; the golden History heads were re-pinned once, at the implementing commit.

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

## Appendix G. Design revision 2 — the loop's own clock (1.2.0)

The accepted text is `spec/design_revisions/dr2_the_loops_own_clock_1.2.0.md`, kept verbatim (rc.3 with its one consolidation fix); the three implementation reviews are beside it. This appendix records what it changed and why, so the consolidated text above can be read without it.

**Finding [S2].** Runs 2 and 3 (October 17, 2026; 1,295 runs under 1.1.0). The actor polices rejections (appeals, $a\approx0.98$); the requester polices approvals (disputes). With appeals alone a careful reviewer's 5% false rejections are punished almost every time while a stamper's negligence is caught about 3% of the time, and stampers end richer (+200 per actor at 50/50, $X=8$); with the requester disputing one bad result in four, careful ends richer by 489; break-even is a dispute rate of about 0.07, and careful review pays only above an accuracy of about 92% at that rate. At 10/90 every panel is stamper-majority: disputes fail (23 of 135 won), only the careful minority's errors are adjudicated, their $\rho$ ends below the stampers', selection hands the stampers the awards (159 to 66), and no dispute rate recovers it. At $G^V=20$ about 7% of duty slot-ticks are held by actors who cannot fund the bond and the reserve starves.

**Mechanism.** Every signal the loop produced was panel-produced, so under capture the loop was blind to its own state; the design assumption that humans do not intervene removes the one external oracle the baseline leaned on. The orchestrator therefore owns some truth itself: the truth of the work it writes. Planted work (§7.6) gives a measurement no panel can paint; the plant record (§11.2) turns it into eligibility a captured majority cannot protect; the dial (§12.2) turns it into effort that rises with the threat and eases without it, and into the reserve's size and the security tax.

**Classification.** A design revision motivated by strategy findings (runs 2–3), labelled and read on its own. It adds a mechanism; it does not alter any settlement, verdict or challenge rule of 1.1.0. It changes what participants may do (the orchestrator creates plants; an actor can be suspended from duty; no challenge is admitted on a plant), what they may see (§14), and makes two fixed quantities endogenous ($X$, $\omega$).

**What changed.** §1 (the design assumption); §2.1, §2.4; §4.1 ($\omega_t$); §7.1, §7.5 (labelled), §7.6 (new); §8.3 defaults; §11.2 (new); §12 (whole: §12.1 the reserve holding $\min(X_t,\text{eligible})$ and the eligibility shortfall, §12.2 the dial, the alarm, working capital); §14 (the actor leaves the view); §15.3 (the plant grade); §16; I9 amended, I13's note, I20 and I21 new; §18.1 questions 1, 3, 6 amended, 9 and 10 new; §20 (planted work); Appendices A, B, C. Defaults: $\pi_0=0.10$, $\pi_{\max}=0.40$, $\beta_P=0.75$, $F^*=0.10$, $\gamma=1$, period 50 adjudicated plants or 200 ticks, $m_{\max}=4$, $n_{\min}=4$, $n_P=20$, $\theta_{\text{panel}}=0.20$, $\theta_{\text{duty}}=0.50$, $T_{\text{susp}}=100$, $p_{\text{start}}=p_{\text{cap}}=1.0$, $\Omega_0=300$.

**Found in review and adopted.** rc.1 named a plant actor in a view that carried the actor (§14 as it stood); rc.2 removed the actor from the view. rc.1's I9 and I21 could not both hold when eligible actors were fewer than $X_t$; rc.2 let the reserve run short and count it. rc.1's single plant reliability $\rho^P$ let a reviewer approving half the bad plants stay eligible for ever; rc.2 defined the record on the quantity the clock measures, in two tiers. rc.1 doubled the plant rate for newcomers, which round-robin cannot do without a signal; rc.2 dropped it. rc.1 misstated the solvency figure (29% of slots; it is 7% of slot-ticks), omitted $\Omega$'s working capital (45 per plant), the audit cap and the channels of its hypothesis; rc.2 stated them. rc.2 cleared the record on return from suspension, which would have readmitted stampers with clean slates; rc.3 made the record persist. rc.2 held two rules for a newcomer's audit odds; rc.3 kept §8.3's. rc.2's I21 read eligibility as a standing property while records move mid-review; rc.3 made it a property at assignment, with a suspended actor leaving duty whether or not a replacement exists. rc.3's period counts adjudications, not settlements.

**Found at implementation.** The revision's "at the end of the suspension it is readmitted only if its record passes, and otherwise remains suspended for a further $T_{\text{susp}}$", with the record persisting, makes every suspension permanent: the record is a trailing window of plant outcomes and a suspended actor judges no plants, so a record that failed at suspension cannot pass later. That reading leaves $T_{\text{susp}}$ inert and contradicts the revision's §2.4 ("an actor readmitted from suspension is a newcomer") and its §8 run 2 ("how long does it last once suspended stampers return as newcomers"). The engine implements the smallest reading that gives $T_{\text{susp}}$ its meaning: readmission on probation, to duty and not to panels, until the actor's next plant re-checks the record (§11.2). It was marked in the 1.2.0 text as the implementer's reading and **confirmed as the rule in force by patch 1.2.1** (October 17, 2026), in the sentence design revision 3 rc.1 gives in its Appendix A; design revision 3, if accepted, restates probation in full.

**Engine.** `create_plant` builds the case in the submitted state from two system wallets funded by $\Omega$, with the sealed marker in the History; adjudication at the initial verdict applies the §7.6 table and reveals the marker; every challenge operation refuses a plant; the actor carries the two plant windows, the two tiers, the suspension clock and the probation flag; eligibility is checked in every assignment and at rotation; rotation readmits, removes the ineligible when their review completes, fills to $X_t$ or shrinks to it, and counts the eligibility shortfall; the dial is read once per period on adjudications with its clamps, and sizes $\pi_t$, the applied audit odds, $X_t$ and $\omega_t$; the alarm re-seats by record; the view drops the actor; I20 and I21 are checked per tick; I9, I13 amended. `test_v12` carries the §20 figures and the mechanism's properties; the equivalence scenario plants work and its goldens were re-pinned once. Reviewer-authored tests were not edited: one (the third review's test 18, $\Omega$'s float pinned at 20) is superseded with the reason stated; every other reviewer test passes unchanged.

**After acceptance.** The runs of the revision's §8, in order: reproduce §20's planted-work figures (the test); controller on against off under a drifting stamper share, appeals truthful and no disputes, $X$ free to track; adaptive dispositions; the tipping point at 40/60, 30/70, 20/80 under 1.1.0 and 1.2.0; the red team (camouflaged stampers); $\Omega$'s plant spend and $\omega_t$ across $m$ and the reserve's size trajectory.

---

## Appendix H. Design revision 3 — inspection is membership (1.3.0)

The accepted text is `spec/design_revisions/dr3_inspection_is_membership_1.3.0.md`, kept verbatim (rc.2 with the panel floor's availability clause); the two implementation reviews are beside it. This appendix records what it changed and why, so the consolidated text above can be read without it.

**Finding [S4].** Run 4 (October 17, 2026; 300 runs under 1.2.0, truthful appeals and no disputes throughout). Honesty held everywhere: false approvals four- to five-fold below 1.1.0 at every split from 50/50 to 80/20, and under a stamper share drifting to 90% they stopped growing once the dial saturated (83 against a control of 650). It was slow: a case waited for a reviewer 47 times longer than in the control, vesting ended 40% lower, and $\Omega$ could not fund a third of the plants the dial called for at $m_{\max}$. And suspension from duty was a reward: at 60/40 the eight careful actors were the only eligible reviewers, the dial sized the reserve to 7–8, they were on duty almost always — 500 to 800 reviews each at a fee of 2 — while the twelve suspended stampers, freed from duty, took the awards at 20 (delivery income 3,311 against 1,063 per actor; stampers richer in 19 of 20 seeds). Selection could not help, because it runs among free actors and the honest were not free. $\Omega$ banked the raised tax (+5,898 at 60/40) levied for the effort the honest were supplying; and a plant tied up 45 credits of which 30 was $\Omega$ paying itself.

**Mechanism.** The contest was no longer about detection but about who carries the reviewing load and what membership of the market requires. Suspension now suspends membership: no new award until the actor has inspected well, under full audit, for long enough to pass. Probation is the supervised way back; the members' duty cap keeps half the honest free to work while probationers take the initial seats; the dial's raised tax goes to the reviewers through the duty fund; plant capital counts only the pots.

**Classification.** A design revision motivated by a strategy finding, labelled and read on its own. It changes the meaning of an existing state (suspension) and adds a cap and a fund; it alters no settlement, verdict or challenge rule.

**What changed.** §2.1 (the fund); §4.1 (the split of $\omega_t$); §5.2 (membership and the award); §7.1 (probationers initial only); §7.6 (plant capital netted); §8.3 (the pin for probationers and undetermined newcomers, replacing 1.2.0's taper); §10.4 (the fund's flows); §11.2 (suspension from the market; probation restated in full; readmission on the trailing record with $n_{\min}$ new outcomes); §12.1 (two kinds of seat; the cap; the floor bounded by availability; the fill order; turns by kind); §12.2 (sizing on applied odds; member seats; working capital 15; the fund); §16; I21 amended, I22 and I23 new; §18.1 questions 1 and 9 amended, 11 new; §20 (membership); Appendices A, B, C. Defaults: readmission on $\theta_{\text{duty}}$ with $n_{\min}=4$ new outcomes; $T_{\text{susp}}=100$ unchanged; pinned odds; cap $\lceil E_t/2\rceil$; fund $(m_t-1)\omega_0 B$; plant capital 15; $m_{\max}$ 4 swept against 2; $\Omega_0$ 300 swept against 100.

**Found in review and adopted.** rc.1 stated readmission two ways and its worked example followed the wrong one (a reformed stamper panel-eligible at once at 0.17, when the one trailing record was 0.5); rc.2 kept one record, with the count of new outcomes a minimum only. rc.1's cap was a standing per-tick predicate that fails on a correct engine when $E_t$ falls mid-review, and its panel floor of two members contradicted a cap of one at $E_t=2$; rc.2 made the cap a seating rule, let a member above it finish its review, and let the floor yield over the cap. rc.1 sized the reserve on a population mean while probationers and newcomers are audited at 1; rc.2 sizes on applied odds. rc.1 left a turn's refill order unstated; rc.2 refills by kind. rc.1 netted plant capital without saying what became of the escrow and the guarantee lock; rc.2 states the I12/I15/vesting consequences. rc.2's panel floor was bounded by membership; the accepted text bounds it by availability, in the same form as I9. Smaller: probation pays a stamper a little (+1.2 a review) and the award is what deters; the newcomer pin's fresh-population worst case; a careful probationer's 19% restart, intended; the fund in §10.4; 1.2.1 applied the same day.

**Found at implementation — flagged for confirmation.** Two readings, both marked in the text. (1) *The cap and the reserve floor.* $\lceil E_t/2\rceil$ at six actors is 3, below the $X_0=4$ of Appendix A's initialization and §20's worked example (C, D, E, F on duty): read literally, the baseline's own worlds — and every reviewer test built on them — would violate the revision at tick 0. The engine lets the cap never fall below the reserve's floor $V_{\max}+1$, as the panel floor yields to the cap; the difference from the literal text is confined to memberships of four to seven, where the literal cap would leave two or three members free. One line of the engine. (2) *An outgoing probationer with no free probationer stays.* Replacing it with a member would seat a member in an initial seat that the next tick's "probationers first" hands back — churn, not a rule. One branch of the rotation.

**Engine.** `award` refuses a non-member before any effect and records membership at award; after $T_{\text{susp}}$ the actor is a probationer — initial reviews only, odds pinned, re-checked at every plant, readmitted on the trailing record with the $n_{\min}$ counter; `_rotate_membership` seats member seats first, lets probationers displace idle members from initial seats, refills turns by kind, keeps the cap at seating and the floor by availability, and counts the eligibility shortfall; the §8.3 update does not run while pinned; the period sizes audit demand on applied odds and the member seats; the duty fund is a wallet credited at award and paid by role weight in each batch; a plant funds its pots only, with no escrow and no guarantee lock. I22 and I23 per tick; I21 amended; I15 exempts a plant's guarantee. `test_v13` carries the §20 membership figures the six-actor world admits and the mechanism's properties; `test_v12` asserts the 1.2.1 engine through `Params(membership=False, duty_fund=False, net_plant_capital=False)`, which the stamping driver runs as the 1.2.0 control; the equivalence scenario's goldens were re-pinned once. Reviewer-authored tests were not edited and pass unchanged.

**After acceptance.** The runs of the revision's §8, in order: reproduce §6 (the test); the tipping point at 50/60/70/80 under 1.3.0 against run 4's table — the sign and the channel at each split, vesting against the control; adaptive dispositions, 1.3.0 against 1.2.0, fund on and off, 3,000 ticks; drift under 1.3.0 with $m_{\max}\in\{2,4\}$ and $\Omega_0\in\{100,300\}$; probation safety — false approvals attributable to probationers, the audit load on members; the red team — the camouflaged stamper under the gate, and a probationer that behaves until readmitted and then stamps.

---

## Closing statement

> A request is paid for by the one who makes it, judged first by a reviewer who is bonded on the answer, audited blind, open to appeal and dispute for a window, and then final. The actor commits to a price and a time and bears its own cost. The reviewer is made whole for its care, earns its fee only when right, and loses only what it locked. Verification is funded as the security work it is. Delegation is the same loop one level down, with the requester-actor's rejection bonded and its acceptance its own risk. The human powers the circuit and holds the plug: the orchestrator rules on splits inside the procedure, and only a human overrides it. The record is one record. The reviewer is told what it may answer and nothing it need not know. The loop no longer needs anyone to complain: it writes some of the work itself, knows the answer, and watches who gets it wrong; the watching costs effort, the effort rises when the watching finds trouble and eases when it does not, and the effort is paid for by the fee every request pays for its security. A reviewer that will not look loses its bond, its standing and its seat, through a door no majority can hold shut — and, since 1.3.0, its place in the market, which it buys back the only way that can be checked: by inspecting well, under full audit, for a while. The tax the dial raises goes to the people doing the work. Humans may still pull the plug; they do not have to. What is left is that an honest market of few is slow; that is the next question, and it has a direction. These are the rules of this version. The engine is corrected to them; they change only by decision; and what they do under self-interest is for runs to show.

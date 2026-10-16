# Agentic Economics — The Task, Verification, and Dispute Loop

## Working specification v0.1

**Project:** Agentic-OS / Agentic Economics  
**Prepared:** October 15, 2026  
**Discussion boundary:** Through the agreement on a protected verification reserve, no self-review, reviewer-capacity release, and rotation of verification duty.  
**Status:** Agreed conceptual rules with explicit open parameters; not an implemented or validated economic mechanism.

> **The wallet supports the purpose; it does not define the purpose.**
>
> **The actor competes on its promise, is assessed on its delivery, and bears the cost of its execution.**
>
> **The past is append-only. The present is committed. The future is mutable.**

This document consolidates the discussion into one reference. It does not require a new operating system, prescribe an agent's internal reasoning, or resolve every part of the wider economy. The task and review lifecycles below describe commitments and observable events—not mandatory internal cell types.

The existing map, **The actor and its economic life**, revision 4, captures the earlier purpose and assessment discussion [M1]. Subsequent decisions in this conversation extend and, where stated below, supersede that snapshot. The maps have not been edited as part of preparing this file.

### Reading the status labels

| Label | Meaning |
|---|---|
| **Agreed** | A working rule or boundary accepted in the conversation. It is a design commitment, not proof that the mechanism works. |
| **Initial value** | A numerical starting example explicitly discussed; not a calibrated universal constant. |
| **Formalization** | Notation, accounting, or a logical consequence used here to express the agreed model. It is not an additional economic preference. |
| **Open** | A parameter, unresolved branch, or implementation choice that has not been selected. |
| **Deferred** | An earlier possibility outside the current core loop. It has not been silently adopted. |

## Contents

1. Purpose and measurement boundary
2. Participants, time, and notation
3. Request fulfillment and evidence
4. Fixed resource prices and execution cost
5. Offers, learned selection, and guarantees
6. Task lifecycle and waiting
7. Verification assignments and compensation
8. Disputes and final adjudication
9. Wallet accounting and settlement
10. Ratings and learning signals
11. Protected verification capacity
12. Rotation of verification duty
13. Learning through a world model
14. Verifiable history and trust boundary
15. Worked examples
16. Rule and invariant checklist
17. Open parameters and unresolved branches
18. Deferred ideas and superseded alternatives
19. Sources and decision provenance

---

## 1. Purpose and measurement boundary

### 1.1 The purpose

**Agreed.** The actor seeks to contribute useful outcomes for users over time. Currency helps it sustain and develop its ability to do so. Accumulating wealth, maximizing task count, and maximizing visible activity are not the chosen ultimate purpose. [C1]

The operational boundary is narrower than estimating the user's total benefit:

> **Assess fulfillment of the request in its applicable context. Do not attempt to price how much the outcome improves the user's life.**

“Useful” is therefore operationalized here through request fulfillment. Answering “2 + 2” with “4” can fulfill a request just as a much larger output can fulfill another request. We do not have to establish that the requests have equal importance, and comparing their ultimate human value is not a prerequisite for this model.

The efficiency direction is:

> **Fulfill the request using the least necessary work and resource expenditure.**

Cheap nonfulfillment is not equivalent to economical fulfillment. Additional work is not automatically better. Fixing a recurring issue once may eliminate many future tasks; counting tasks alone would miss that contribution.

### 1.2 A comparison criterion, not a complete decision algorithm

**Formalization.** For one request, a way to express the efficiency preference is:

$$
\begin{aligned}
\min_{\tau\in\mathcal T(q)}\quad & C(\tau)\\
\text{subject to}\quad & \widehat F_\nu(q,\tau)=\mathsf F.
\end{aligned}
$$

Here, an execution $\tau$ includes what actually unfolded, not just an original plan. The expression says to prefer lower cost among executions assessed as fulfilled. It does not assume the actor knows the outcome beforehand, and it is not an instruction to select the cheapest bidder regardless of likely fulfillment.

We have not chosen a numerical trade-off between partially fulfilled work and additional expense. Nor have we selected a single lifetime reward formula. The model can have a clear task-level interaction while those questions remain open.

### 1.3 Currency is an instrument

A wallet can fund information, execution, delegation, and verification. Spending may make fulfillment possible; retaining funds may preserve future capability. A high balance alone is not evidence that an actor is serving requests well.

Crucially, the model distinguishes:

- **Purpose:** fulfill users' requests economically over time.
- **Assessment:** determine fulfillment of a particular request.
- **Accounting:** record prices, expenses, payments, and losses.
- **Learning:** use experience to inform subsequent decisions.

These are related, but they are not one interchangeable score.

---

## 2. Participants, time, and notation

### 2.1 Participants

**Agreed.** Users submit requests. Actors offer and execute work. The orchestrator maintains the request pool, selects actors, arranges verification, pays reviewers, and can make a final dispute ruling. Actors can temporarily act as reviewers; verification is not a permanently separate class of agents. [C2–C8]

The orchestrator has judgment and accountability to the user. Its exact funding, whether it owns a wallet distinct from administered accounts, and broader governance remain open.

### 2.2 Time and capacity

**Agreed.** The economy is described in discrete global time:

$$t\in\mathbb N_0=\{0,1,2,\ldots\}.$$

At every time $t$, the orchestrator has a request pool $\mathcal P_t$, possibly empty. An assignment can occupy several time units. An actor taking a three-unit review at $t=5$ is occupied during $[5,8)$ and can become execution-available at $t=8$.

**Current core assumption:** one active assignment at a time. An actor with its own task awaiting verification or dispute settlement remains committed and cannot take another ordinary task or count toward the verification reserve. This is the agreed “stuck” condition. Finishing a review, by contrast, releases the reviewer's execution capacity even when its assessment remains challengeable.

Multiple actors may work at the same time. The physical duration of a time unit and ordering of events within a unit have not been selected. A time unit is not assumed to equal one model call, one action, or one cell.

### 2.3 People, cases, and execution

| Symbol | Meaning |
|---|---|
| $\mathcal A_t$ | Actors participating at time $t$ |
| $O$ | Orchestrator |
| $\mathcal P_t$ | Requests available for assignment at $t$ |
| $q$ | One identified request, with its version and applicable context |
| $i$ | Actor performing the ordinary task |
| $j$ | Actor performing a review |
| $y_q$ | Submitted result, bound to a particular version |
| $\tau_{iq}$ | Actual execution by actor $i$ for request $q$ |
| $h_t^i, h_t^O$ | Information available to actor $i$ and orchestrator $O$ at $t$ |
| $\nu_q$ | Assessment criteria, interpretation, and evaluator version |
| $\widehat F_{j,\nu_q}(q,y_q)$ | Reviewer $j$'s attributed fulfillment assessment |
| $Z_q$ | Accepted settlement outcome for the case, distinct from individual assessments |
| $\delta_v$ | Duration of review assignment $v$, in time units |

### 2.4 Economic quantities

| Symbol | Meaning |
|---|---|
| $B_{iq}$ | Actor $i$'s committed delivery price for $q$ |
| $C_{iq}$ | Actual execution cost for $q$, excluding guarantee principal and court fees |
| $G_{iq}$ | Fulfillment guarantee locked by the winning actor |
| $R_i(t)$ | Actor's rating at $t$; detailed scale is open |
| $W_i(t)$ | Total recorded wallet balance, including locked funds |
| $L_i(t)$ | Locked part of that balance |
| $U_i(t)=W_i(t)-L_i(t)$ | Unlocked balance; “available” means not locked, not a complete credit policy |
| $P_{iq}$ | Task compensation actually settled |
| $D_q$ | Fee paid by the actor to open a dispute |
| $C^V_{jv}$ | Reviewer's actual execution cost for review $v$ |
| $\widetilde C^V_{jv}$ | Actual review cost accepted as eligible for reimbursement |
| $K_r$ | Reimbursement cap for review role $r$ |
| $f_r$ | Fixed service fee for role $r$, ordinary or appeal |
| $\Pi_{jv}$ | Payment from the orchestrator to reviewer $j$ for assignment $v$ |
| $\epsilon_R$ | Small positive rating increment for completed verification work |
| $\ell_{jv},\rho_{jv}$ | Other financial and rating losses imposed on a reviewer; amounts open |

Guarantee $G$, court fee $D$, reviewer service fee $f$, and execution cost $C$ are different quantities. Returning a locked guarantee is not income.

### 2.5 Reserve and eligibility

| Symbol | Meaning |
|---|---|
| $\mathcal V_t$ | Verification-duty pool: idle duty actors plus actors actively reviewing |
| $X$ | Minimum size of the verification-duty pool |
| $V_{\max}$ | Maximum distinct eligible reviewers needed for one task and its defined dispute procedure |
| $\mathcal E_{q,r}(t)$ | Actors currently idle and eligible to perform review role $r$ for case $q$ |
| $\mathcal I_q(t)$ | Actors eligible for an ordinary award without violating capacity or reserve rules |
| $m_0(q)$ | Number of initial reviewers assigned to case $q$ |

An actor can be idle but unavailable for ordinary work because it is on verification duty. An actor can have financial liability for an earlier review while being free to execute another assignment.

---

## 3. Request fulfillment and evidence

### 3.1 What is assessed

**Agreed.** Reviewers evaluate the fit between the request and the actual result, in applicable context. “Correlation(request, result)” is shorthand for this semantic fit, not a requirement to compute a statistical correlation coefficient or textual similarity score. [C1, C4]

A Jev/Jev-like structured evaluator is an option. The model, training, score calibration, and precise rubric implementation remain open; mentioning it does not establish its suitability or accuracy.

Criteria follow from the request and known context. They must not be retroactively invented merely to defend or reject an outcome. Any interpretive assumptions should be visible.

### 3.2 Assessment vocabulary

The previously discussed working vocabulary is retained:

$$\widehat F_{j,\nu_q}(q,y_q)\in\{\mathsf N,\mathsf P,\mathsf F,\bot\}.$$

| Value | Meaning |
|---|---|
| $\mathsf N$ — Not fulfilled | No meaningful fulfillment of the expressed need |
| $\mathsf P$ — Partially fulfilled | Some contribution, but material requirements are unmet |
| $\mathsf F$ — Fulfilled | Material requirements are adequately satisfied |
| $\bot$ — Cannot assess | Available evidence is insufficient |

These are not numerical values 0, 0.5, and 1. “Fulfilled” means enough for the request, not the best conceivable output. “Cannot assess” is not a low-performance score and is not automatic nonfulfillment.

The monetary branches below are defined most clearly for final $\mathsf F$ and final $\mathsf N$. Treatment of partial or insufficient-evidence outcomes remains open.

### 3.3 Preserve the basis

A review records the reviewer identity, the request and result versions, the criteria or interpretation used, the assessment, and its supporting reasons or evidence. The actor's own completion claim is not accepted as sufficient verification of itself.

Mechanical checks may support some criteria; semantic criteria may require judgment. An attributed judgment remains an assessment, even when its record is cryptographically protected.

### 3.4 Clarification is not retroactive misconduct

Feedback may reveal a previously unstated audience or an evolving need. An updated request or assessment can follow, while the earlier information basis stays recorded. That does not automatically establish that the actor violated the earlier commitment.

For an appeal about an allegedly incorrect rejection, the original submitted result and applicable request are fixed. A new improved result is a revision or new submission, not proof that the earlier rejection was wrong.

---

## 4. Fixed resource prices and execution cost

**Agreed.** Resource prices start fixed for this formulation. Price changes may later become part of the wider economy. The initial tariff itself has not been populated with a complete numerical price list. [C2]

For resource type $r$, let its fixed unit price be $p_r\geq0$, and let $u_{irq}(t)$ be units consumed by actor $i$ for request $q$ at time $t$.

**Formalization:**

$$C_{iq}=\sum_t\sum_r p_r\,u_{irq}(t).$$

Possible resource categories include inference, information retrieval, tool use, and subcontracted services. Retries and unsuccessful attempts still cost resources. Fixed prices do not imply a known total cost: an actor may discover that it needs additional actions.

Elapsed time is separate from priced expenditure. A reimbursed three-unit review can cost an actor an opportunity to take another task, without requiring an additional invented monetary charge for the missed opportunity.

**Accounting boundary:** actor expenditure is not automatically total network resource consumption. If A pays B for subcontracting, A's payment and B's downstream expenditure cannot both be counted as distinct physical resource consumption without an accounting definition. The present task accounting measures what the actor spends. System-wide cost attribution remains open.

Recurring rent was explored as an operating cost. Its numerical tariff, attribution during task waiting or verification duty, and recipient remain deferred economic settings. Rent is not silently included again in every formula below.

---

## 5. Offers, learned selection, and guarantees

### 5.1 Bid a delivery price, not an internal spending ceiling

**Agreed.** Actor $i$ makes a prior commitment:

> “I will fulfill request $q$ for $B_{iq}$ credits.”

It backs that commitment with guarantee $G_{iq}$. Its rating at the offer time is part of the information available to the orchestrator. A proposed plan may accompany the offer; its exact structure is not prescribed.

$$b_{iq}=(B_{iq},R_i(t),G_{iq},\text{other disclosed terms}).$$

The bid and accepted terms are recorded before execution. The actor remains free to choose and revise its operational approach within those terms.

**$B_{iq}$ is a delivery price, not a hard execution limit.** If fulfillment costs more, the actor bears the overrun. A low bid does not permit a lower fulfillment standard. A high guarantee is not evidence that the result is correct. [C2, C3]

### 5.2 Selection is a learned orchestrator decision

**Agreed direction.** The orchestrator aims to select for predicted fulfillment using the request, history, bid, rating, and guarantee. This supersedes the earlier suggestion to use lowest price with a rating tie-break. [C3]

**Formalization:**

$$i^*\in\arg\max_{i\in\mathcal I_q(t)}S_\theta(q,h_t^O,B_{iq},R_i(t),G_{iq}),$$

where $S_\theta$ estimates fulfillment under assignment to $i$. One possible interpretation is:

$$S_\theta=\widehat{\Pr}_\theta(Z_q=\mathsf F\mid q,h_t^O,B_{iq},R_i(t),G_{iq}).$$

The probability interpretation is notation for a possible predictor—not an assertion of calibrated probabilities or a direct native output of LeWorldModel.

The eligible set respects availability, the protected reserve, and the ability to place the required guarantee. A tie-breaking rule and what to do when no acceptable offer exists remain open.

**Important limit:** making bid price an input does not mathematically make price something the orchestrator minimizes. The accepted selection direction is fulfillment-first prediction. Any explicit price preference, affordability constraint, or same-fulfillment tie-break needs its own rule; none is invented here.

### 5.3 Place the guarantee

**Agreed.** The winner places its own guarantee at risk. Locking requires funds that are not already locked elsewhere. The guarantee cannot simultaneously finance another commitment or execution expenditure.

- Fulfillment: release the guarantee.
- Established final nonfulfillment: forfeit the guarantee.
- Pending verification or dispute: keep it locked.

This is a fulfillment bond, not insurance. An execution overrun alone does not trigger forfeiture. The size-setting rule for $G_{iq}$, its destination on forfeiture, and any extra collateral for reviewers remain open.

---

## 6. Task lifecycle and waiting

The following states organize the observable case. They do not specify an agent's internal reasoning loop.

| Case stage | What happens | Actor availability |
|---|---|---|
| Available request | Request is in $\mathcal P_t$; actors may offer | No obligation merely from being a possible bidder |
| Award and commitment | Orchestrator selects; bid terms are accepted; guarantee is locked | Actor committed |
| Executing | Actor performs, delegates, gathers information, or revises its approach | Actor committed |
| Submitted / awaiting verification | Result is recorded; review is requested | Actor remains stuck on this task |
| Initial assessment received | Result may be accepted or rejected, or remain uncertain | Release depends on settlement, not merely receiving a message |
| Disputed | Actor pays court fee and challenges rejection | Actor remains committed; guarantee remains locked |
| Settled | Accepted outcome and transfers are recorded | Actor may become eligible for ordinary work or verification duty |

If no reviewer is currently available, the case waits. The actor does not become free merely because it finished generating an output. The protected reserve is intended to prevent all execution capacity from being held by such ordinary tasks.

**Open:** settlement timing for an unchallenged initial rejection, appeal deadlines, insufficient evidence, timeouts, refusal to deliver, and partial fulfillment. The diagram does not hide these as automatic success or failure.

```text
Request pool
    |
    v
Offers -> learned selection -> lock guarantee
    |
    v
Execute -> submit result -> wait for initial verification
                                 |
               +-----------------+--------------------+
               |                 |                    |
          Fulfilled         Not fulfilled       Partial / unknown
               |                 |                    |
         Settle success     Accept rejection?    Handling remains open
                                 |
                        challenge + court fee
                                 |
                      two fresh appeal reviewers
                                 |
                     orchestrator ruling if needed
                                 |
                    settle outcome and consequences
                                 |
                    availability / duty rotation
                                 |
                       subsequent opportunities
```

There is no requirement that the actor's original plan remain unchanged. The request and committed delivery terms stay identifiable; any renegotiation must be recorded, and its policy remains open.

---

## 7. Verification assignments and compensation

### 7.1 Roles

**Agreed.** One or more initial reviewers assess $(q,y_q)$. The orchestrator chooses how many are needed. For the defined appeal flow, it assigns two additional, distinct reviewers. No actor reviews its own work, and original reviewers do not act as fresh appeal reviewers of their own assessment. [C4, C8]

Reviewing is an assignment with duration and execution cost. An actor may volunteer or be assigned mandatory duty. These modes do not change the compensation formula or relieve the reviewer of accountability.

### 7.2 Payment has two components

**Agreed structure.** The orchestrator pays capped eligible-cost reimbursement plus a fixed service fee:

$$\boxed{\Pi_{jv}=\min(\widetilde C^V_{jv},K_r)+f_r.}$$

The initial ordinary-review example is:

$$K_{\mathrm{ordinary}}=5,\qquad f_{\mathrm{ordinary}}=2.$$

These are starting values from the discussion. A higher fixed fee for dispute review was also agreed as a direction:

$$f_{\mathrm{appeal}}>f_{\mathrm{ordinary}},$$

but its amount and whether the same five-credit cap applies to appeal reviews have not been fixed.

A valid completed review also earns a small rating increment $\epsilon_R>0$, separately from any later adverse adjustment. What constitutes a payable completion when evidence is insufficient needs a precise operational definition; the reviewer must not be forced to invent certainty to get paid.

### 7.3 Reviewer margin

Before penalties and separately charged rent:

$$\Delta W^V_{jv}=\min(\widetilde C^V_{jv},K_r)+f_r-C^V_{jv}.$$

When all actual costs are eligible, $\widetilde C^V_{jv}=C^V_{jv}$, so:

$$\boxed{\Delta W^V_{jv}=f_r-\max(C^V_{jv}-K_r,0).}$$

For the ordinary-review example:

| Actual eligible cost | Payment | Margin before penalties/rent |
|---:|---:|---:|
| 1 | 3 | +2 |
| 3 | 5 | +2 |
| 5 | 7 | +2 |
| 6 | 7 | +1 |
| 8 | 7 | −1 |

The cap limits reimbursement, not necessarily how much the reviewer may spend. Above it, the reviewer bears the excess.

Below the cap, cheaper execution does not increase the direct fee margin. Finishing sooner can, however, restore execution availability sooner and reduce missed opportunities. A smaller action count is not inherently better if the assessment is unsupported.

### 7.4 Cost evidence and incentive limits

The goal is a supported assessment with the least necessary verification work. Reimbursement concerns eligible expenditure, not an unchecked number the reviewer announces.

Two problems remain distinct: claiming expenses that never happened, and actually incurring unnecessary expenses. A verifiable cost record can help with the first; it does not by itself resolve the second. The cap bounds some financial exposure but does not prove efficient or honest reviewing.

The fixed fee is for review work, not for reaching “fulfilled” rather than “not fulfilled.” The participation rating increment likewise does not make the assessment correct.

---

## 8. Disputes and final adjudication

### 8.1 The defined appeal

**Agreed.** The first fully specified dispute scenario is an actor challenging an initial nonfulfillment assessment. [C4, C5]

1. The initial verifier reports nonfulfillment.
2. The actor decides whether to challenge that assessment.
3. To challenge, the actor pays court-like dispute fee $D_q$ to the orchestrator.
4. It submits explanation $d_q$ of why the rejection is wrong.
5. The orchestrator assigns two other eligible reviewers.
6. The appeal reviewers evaluate the fixed request/result and the objection.
7. When needed, the orchestrator reviews the entire record and issues the final ruling.

The appeal reviewers receive at least:

$$x_D=(q,y_q,d_q).$$

The orchestrator's adjudication record contains:

$$\mathcal E_D=(q,y_q,v_0,d_q,v_1,v_2),$$

where $v_0$ is the original assessment or panel record and $v_1,v_2$ include the appeal assessments, identities, and bases. The objection is a claim to examine, not a conclusion reviewers must accept.

### 8.2 Final authority

**Agreed.** The orchestrator can become a verifier/adjudicator when needed. Its decision is the accepted result for economic settlement:

$$Z_q=\operatorname{Adjudicate}_O(\mathcal E_D).$$

The final decision is not an ordinary additional vote. It supplies authority when assessments disagree. No automatic majority rule, consensus protocol, or guarantee of objective semantic truth has been selected.

The procedure can accept a conclusion without establishing absolute truth. Training records must distinguish original claims, later judgments, and final settlement; they must not relabel “overruled” as a demonstrated lie.

Whether matching appeal assessments settle automatically or still require orchestrator action is open. The model currently describes one appeal round and a possible final orchestrator decision. It does not introduce an endless chain of appeals against appeal reviewers.

### 8.3 Outcomes for the actor

| Final appeal outcome | Guarantee | Court fee |
|---|---|---|
| Actor wins: rejection overturned | Released | Original rejecting verifier reimburses the actor |
| Actor loses: nonfulfillment upheld | Forfeited | Actor bears the fee already paid |
| No final outcome yet | Remains locked | Fee has been paid; final disposition awaits the case |

The successful actor is reimbursed once. Under the discussed route, the original verifier pays the actor back; the orchestrator does not also automatically refund the same fee.

### 8.4 Outcomes for reviewers

An initial rejecting verifier whose rejection is overturned owes the actor the dispute-fee reimbursement. The allocation of this obligation across a multi-verifier initial panel is open.

**Agreed.** An appeal reviewer whose assessment is overruled by the orchestrator loses something. This may be currency, rating, or a combination. The size and exact mechanism remain open. The outcome is defined relative to the procedure's final ruling, not guaranteed objective truth.

An overruled reviewer's loss is not automatically the full service fee, a newly invented reviewer bond, or the actor's guarantee. Those are different mechanisms and have not been adopted.

**Known incentive:** penalties tied to final rulings may teach actors to predict what the orchestrator will accept. That can coincide with good assessment but is not the same thing. It is a property to observe, not a demonstrated correctness guarantee.

### 8.5 Court fee versus reviewer compensation

The orchestrator pays ordinary and appeal reviewers. The challenger pays a separate court fee. There is no equation requiring:

$$D_q=\Pi_{v_1}+\Pi_{v_2}.$$

The fee is not necessarily sufficient to cover adjudication. Where the orchestrator obtains its operating funds remains open.

---

## 9. Wallet accounting and settlement

### 9.1 Locking is not spending

**Formalization.** Use:

$$W_i=U_i+L_i.$$

| Event | Change to unlocked $U_i$ | Change to locked $L_i$ | Change to total $W_i$ |
|---|---:|---:|---:|
| Lock guarantee $G$ | $-G$ | $+G$ | 0 |
| Release guarantee $G$ | $+G$ | $-G$ | 0 |
| Forfeit locked guarantee $G$ | 0 | $-G$ | $-G$ |
| Pay actual expense $c$ | $-c$ | 0 | $-c$ |
| Receive payment $p$ | $+p$ | 0 | $+p$ |

The guarantee must be fundable when locked and cannot be double-pledged. Broader borrowing, overdrafts, reviewer insolvency, and debt recovery have not been defined.

A generic total-balance identity is:

$$W_i(t+1)=W_i(t)+\operatorname{inflows}_i(t)-\operatorname{outflows}_i(t).$$

Locking and unlocking alone do not appear as changes to total wealth.

### 9.2 Actor settlement

For a fulfilled task paid at the agreed price:

$$P_{iq}=B_{iq},\qquad \boxed{\Delta W_{iq}^{\mathrm{task}}=B_{iq}-C_{iq}.}$$

The returned guarantee is already the actor's money. It is not added as earnings.

For a single appeal, define indicators $I_D$ for an appeal being opened, $I_W$ for that appeal being won, and $I_N$ for established final nonfulfillment with guarantee forfeiture. Then:

$$\boxed{\Delta W_{iq}^{\mathrm{case}}=P_{iq}-C_{iq}-I_DD_q+I_WD_q-I_NG_{iq}.}$$

This identity excludes separately incurred appeal-preparation costs, rent, and any additional penalties not yet defined. Such actual expenses must be accounted for separately, not assumed nonexistent in a real execution.

Useful special cases:

| Outcome | Net case effect before the excluded costs |
|---|---|
| Fulfilled, no appeal | $B-C$ |
| Rejection overturned, fulfilled payment made | $B-C$ because court fee and reimbursement cancel |
| Nonfulfillment upheld after appeal | $P^{\mathrm{fail}}-C-D-G$ |
| Final nonfulfillment without appeal | $P^{\mathrm{fail}}-C-G$ |

**Open:** $P^{\mathrm{fail}}$, compensation for an unfulfilled or partially fulfilled task. Zero payment is a possible choice, not an already agreed universal rule. Pending or insufficient-evidence cases are not silently put in a forfeiture row.

### 9.3 Reviewer settlement

For a completed review:

$$\Delta W^V_{jv}=\Pi_{jv}-C^V_{jv}-D_qI_{\mathrm{liable\ original},j}-\ell_{jv}.$$

The indicator identifies the liable original verifier when an actor wins the appeal. The additional financial loss $\ell_{jv}$ excludes that reimbursement so it is not counted twice. An appeal reviewer has no automatic obligation to reimburse the challenger under the single-original-verifier rule; its separate overrule consequence is still to be specified.

If an appeal-review penalty is purely in rating, $\ell_{jv}$ can be zero while the rating loss is positive.

### 9.4 Orchestrator accounting is not monetary policy

The orchestrator administers collection of court fees and pays reviewer compensation. For such an administered account, a case-level accounting identity is:

$$\Delta W_O^{\mathrm{admin}}=\text{funding received}+D_qI_D-\sum_v\Pi_{jv}-P_{iq}+\text{other specified transfers}.$$

This is an accounting illustration, not a decision that the orchestrator owns this account personally, may mint currency, or always receives forfeited guarantees. Rent and forfeiture may be transfers or removals from circulation; their destinations remain unselected.

---

## 10. Ratings and learning signals

**Agreed.** Completing verification work earns a small positive rating increment. Reviewers can incur later consequences for overruled assessments. Rating is distinct from currency.

**Formalization:** before any range normalization:

$$\Delta R_{jv}=\epsilon_R-\rho_{jv}.$$

The participation increment should not depend on whether the reviewer approves or rejects the result. An overruled appeal assessment incurs a loss in currency, rating, or both; the split is open.

The rating now reflects participation as well as accountability consequences. This must be acknowledged rather than describing it as a pure probability of honesty. We have not fixed the rating's range, starting prior, cap, decay, task-domain dependence, or aggregation rule.

Actors who frequently review can accumulate participation increments. Whether the increment should be limited or adjusted is not settled. No claim is made that the current reward and penalty sizes are manipulation-proof.

For learning, retain separate observations: request fulfilled or not under the accepted procedure; original assessment; appeal disposition; costs and time; rating changes; and the orchestrator's final ruling. A final ruling supplies the economic label, not privileged access to truth.

---

## 11. Protected verification capacity

### 11.1 Reserve duty, not permanent idleness

**Agreed.** At least $X$ actors remain outside ordinary task commitments for verification duty. They may be waiting for review work or actively reviewing:

$$\boxed{|\mathcal V_t|\geq X.}$$

Starting a review does not remove a duty actor from $\mathcal V_t$. It changes that actor from idle-on-duty to busy-on-duty. Ordinary actors waiting for review of their own work do not count toward this reserve. [C7, C8]

An ordinary award cannot consume the protected reserve. Under the one-ordinary-commitment-per-actor assumption:

$$\#\{\text{actors holding ordinary commitments at }t\}\leq |\mathcal A_t|-X.$$

This is an implication of the reserve, not a promise that all nonreserved capacity is always occupied.

### 11.2 Size and eligibility

**Agreed condition:**

$$\boxed{X>V_{\max}.}$$

$V_{\max}$ counts the maximum distinct eligible reviewers required for one task and its defined dispute flow. For a bounded initial panel size $m_{0,\max}$ and two fresh appeal reviewers, the actor-reviewer count is $m_{0,\max}+2$. Whether the orchestrator's possible adjudication consumes an additional counted resource must be made explicit; it is not automatically an actor in $\mathcal V_t$.

The bound therefore cannot be instantiated until the maximum initial panel and treatment of adjudication capacity are specified.

Eligibility for a particular review still matters:

$$\mathcal E_{q,r}(t)=\{j:\ j\text{ is execution-available for review and eligible for case }q\text{ in role }r\}.$$

At minimum, exclude the task actor. For appeals, exclude the original reviewers and require the two additional reviewers to be distinct. Broader rules covering subcontractors, closely related actors, or other conflicts have not been set.

### 11.3 Assignment and waiting

**Agreed.** Prefer eligible volunteers. If nobody accepts, assign an available eligible actor by round-robin. If no eligible actor is currently available, wait. A refusal to volunteer does not exempt an actor from mandatory duty.

The exact choice among several volunteers is open. Mandatory assignment uses the orchestrator's tracked availability and eligibility, not a permanent group of favored reviewers.

Completing a review releases its execution capacity even when a later dispute remains possible. Financial responsibility can persist independently of that capacity.

### 11.4 What the reserve does and does not guarantee

The reserve addresses the specific cycle in which all actors hold ordinary tasks and are waiting for verification that requires another actor.

It does **not** by itself prove bounded waiting or overall deadlock freedom. Progress additionally depends on review completion, access to evidence, case-specific eligibility, assignment order, and the orchestrator's ability to adjudicate. Concurrent cases can use all reserved capacity and leave new cases waiting. Infinite review duration or a continuously overloaded review pool is not fixed by a numerical reserve alone.

For the reserve to be feasible, the population must contain at least $X$ actors. For at least one ordinary task actor to coexist with it, at least $X+1$ actors are required under this capacity model. These are arithmetic consequences, not a selected population size.

Do not treat “no volunteers,” “all reviewers temporarily busy,” and “too few eligible participants exist” as the same condition. Only the first is directly resolved by mandatory round-robin.

---

## 12. Rotation of verification duty

**Agreed.** Rotate reserve membership, not only individual reviews within an unchanged reserve. Repeated voluntary specialization is allowed; permanent mandatory exclusion from ordinary work is not the intended behavior. [C8]

An actor that completes and settles its ordinary task may become a replacement duty actor. An outgoing duty actor must have finished its current review and completed the applicable duty turn.

A handover from outgoing $j$ to incoming $k$ preserves capacity:

$$\mathcal V_{t^+}=(\mathcal V_t\setminus\{j\})\cup\{k\}.$$

The replacement enters before the outgoing actor is released to ordinary work, or both changes occur as one logical handover. A real implementation must not expose an intermediate reserve deficit.

Three states must remain distinguishable:

| State | Can review now? | Can take ordinary work? |
|---|---|---|
| Actively reviewing on duty | No second assignment | No |
| Finished review, still on duty | Yes, if eligible | No |
| Released from duty after handover | Yes if volunteering and available | Yes, if otherwise eligible |

A lingering challenge or liability from an earlier review is not itself an execution lock. A reviewer may therefore do subsequent work even when an earlier assessment remains contestable.

If no replacement is available, an outgoing actor remains on duty. Rotation prevents a fixed roster by policy; it does not promise a fixed maximum duty duration under all workloads.

**Open:** whether a duty turn is one review, several reviews, or elapsed time; exact roster ordering; how to select incoming replacements; and how voluntary specialists interact with mandatory turns. No new numeric quota is selected here.

---

## 13. Learning through a world model

### 13.1 Chosen direction, adaptation still required

**Agreed direction.** Adapt LeWorldModel-style learning as an initial model of learning for both actors and the orchestrator. This is not a claim that an unmodified model already performs economic reasoning or verification. [C3]

**Research boundary.** LeWorldModel learns latent dynamics from offline visual observation/action trajectories without reward labels. It combines prediction and anti-collapse objectives. In its reported planning setup, model weights stay fixed while action sequences are optimized toward a goal representation. It does not demonstrate learning this agent economy, online adaptation here, or calibrated fulfillment judgments. [S1]

The common principle is to learn consequences and use those predictions for decisions. Sharing a principle or architecture does not decide whether actors and orchestrator share parameters, private memory, observations, or training data.

### 13.2 Different decisions in the same feedback world

| Role | Decision to learn about |
|---|---|
| Ordinary actor | Which approach to take and what price/guarantee to offer |
| Actor during execution | What to do next given observations, commitments, and cost |
| Actor after rejection | Whether there is a sufficient basis to dispute |
| Available actor | Whether to volunteer for verification |
| Reviewer | What evidence to inspect and what assessment it supports |
| Orchestrator | Which offer is likely to fulfill the request |
| Orchestrator in a dispute | Which outcome to accept after considering the evidence |

These are decision problems under the agreed purpose and economic rules, not declarations that each role independently maximizes its income.

### 13.3 Conceptual notation

For an adapted representation $z_t$ of available history and a decision $a_t$:

$$\widehat z_{t+\delta}=g_\theta(z_{\leq t},a_t,\delta).$$

This is a possible description of predicting a subsequent situation, including variable task duration. It is our adaptation notation, not an equation claimed to be implemented by the paper.

Observation supplies the actual later record for comparison. Wallet changes, accepted judgments, and outcomes can be recorded as aspects of the environment. What becomes prediction data versus a planning target versus a training reward is not yet selected.

The actor–environment interaction remains:

$$\text{current situation}\to\text{choice}\to\text{effects}\to\text{responses}\to\text{new situation}\to\text{next choice}.$$

A changing situation is not proof of learning. Neither a rating update nor payment alone specifies how the actor changes its future behavior. Online update frequency, observations, action representation, loss details, calibration, and initial data remain open.

---

## 14. Verifiable history and trust boundary

### 14.1 What is protected

**Agreed.** A loop has a persistent identity. Its committed past cannot be silently rewritten by that loop through the supported interface. Its recorded present can be checked against the committed history. Its planned future can change; an earlier plan snapshot remains part of the past. [C0]

The history should distinguish requests, offers, accepted terms, guarantee locks, submissions, reviews, disputes, rulings, payments, and changes in role or availability. This is a conceptual record scope, not a requirement to expose private model reasoning or capture every physical event.

Changes are appended as subsequent events, not replacements of inconvenient earlier claims. Two disagreeing assessments can coexist in an integrity-valid history.

### 14.2 Registration and state snapshots

The earlier loop discussion began with registration: an execution loop receives a stable identity and an authenticated initial empty-state commitment before adding its plan and later events. The trusted recording authority retains or authenticates accepted commitments; giving the loop an unprotected signing key is not itself a guarantee against rewriting history. The exact registration and key arrangement remains open.

For a loop $\ell$ at time $t$, let $H_{\ell,\leq t}$ be its recorded history, $S_{\ell,t}$ its recorded current state, and $\Phi_{\ell,t}$ its currently anticipated future. The future may be empty or incomplete.

**Conceptual snapshot:**

$$Q_{\ell,t}=\operatorname{Commit}(H_{\ell,\leq t},S_{\ell,t},\Phi_{\ell,t}).$$

This records what was known and planned then, not a promise that the planned future occurs. Revising a plan creates a later snapshot without replacing the earlier one. A hash match establishes consistency with the committed data; validating state transitions also needs their specified consistency rules.

An actor, its task contract, and an execution loop are related but not interchangeable identities. Their exact one-to-one or one-to-many mapping is not fixed by this document.

### 14.3 Separate time from record order

Several actors may generate events at the same global time $t$. Let $n$ identify an accepted record position; it is not necessarily equal to $t$.

**Illustrative commitment only:**

$$K_{\ell,n}=H(\operatorname{encode}(\ell,n,K_{\ell,n-1},e_{\ell,n})).$$

Here $\ell$ identifies the loop, $e$ is a recorded event, and encoding must be unambiguous. A protected checkpoint can bind a record position, its head, and the declared current-state representation. The exact hash, signing, storage, and consistency-proof mechanism is not selected.

Authenticated checkpoints and independently checkable append-only consistency are established techniques; RFC 9162 describes such mechanisms for a different application, certificate logs. It is technical background, not an adopted architecture for this system. [S2]

### 14.4 Limits

The accepted trust boundary includes a correctly functioning commitment/recording authority and protected references. Compromise of that trusted mechanism, firmware, or arbitrary protected-memory manipulation is outside the initial guarantee. A loop may be adversarial without being allowed to edit those references.

A hash chain alone does not establish truth, capture unrecorded actions, or stop an attacker from substituting an entire history if the trusted head is also replaceable. Checking current state against a history also requires a specified representation and consistency check; hashing an arbitrary state does not prove that it follows from the events.

Thus distinguish:

**Record integrity:** the supplied record matches the protected commitment.  
**Attributed assessment:** a reviewer made a particular judgment on identified evidence.  
**Settlement:** the procedure accepted a particular outcome and consequences.

None automatically establishes that every assertion about the external world is true.

---

## 15. Worked examples

All values beyond the discussed ordinary-review cap and service fee are illustrative. The examples demonstrate accounting and capacity, not selected tariffs or evidence that incentives work.

### 15.1 Delivery price versus execution cost

Actor A quotes $B=5$ and places a guarantee. Both executions below fulfill the request:

| Actual cost | Task margin | Guarantee |
|---:|---:|---|
| 3 | $5-3=+2$ | Released |
| 7 | $5-7=-2$ | Released |

Spending above the bid loses money but does not break the fulfillment promise. Spending below the bid without fulfillment does not count as success.

### 15.2 Time has an opportunity cost

A reviewer starts at $t=5$ and takes three time units. A desirable ordinary task arrives at $t=6$ and is awarded elsewhere. The reviewer cannot interrupt the capacity rule merely because it would rather take that task.

If its review costs three eligible credits, ordinary payment is $3+2=5$, for a two-credit margin. Reimbursement does not restore the missed opportunity. At $t=8$, completing the review frees execution capacity, but ordinary-work eligibility still depends on release from verification duty.

### 15.3 Full appeal example, including the reserve

Assume six actors A–F. B, C, D, and E are on verification duty, so $X=4$. A and F are ordinary-work candidates. Assume one initial reviewer and two fresh appeal reviewers, making the distinct actor-reviewer requirement three; $4>3$. The orchestrator is separate for this example.

A offers delivery for $B=10$, with guarantee $G=4$, and begins with $W_A=30$. The orchestrator selects A using its predicted-fulfillment decision—not merely because A is cheapest. Other offers need not be priced here.

For illustration only, the court fee is $D=2$ and appeal reviewers receive a fixed fee of 3 with a reimbursement cap of 5. Rent, appeal preparation costs, and extra penalty amounts are omitted explicitly.

| Time | Event | Capacity consequence |
|---|---|---|
| 0 | A is selected and locks 4 credits | A committed; B–E remain the four-person reserve |
| 0–3 | A executes at actual cost 7 | A cannot take another task |
| 3 | A submits; B starts initial review | A waits; B is busy on duty |
| 5 | B completes, reporting nonfulfillment; eligible cost 3 | B becomes idle on duty, not permanently blocked by its assessment |
| 5 | A challenges and pays court fee 2 | A remains committed; its guarantee stays locked |
| 5–8 | C and D perform the two fresh appeal reviews, each costing 4 | C and D busy on duty; B and E can remain available for other eligible review work |
| 8 | C says fulfilled; D says not fulfilled; orchestrator rules fulfilled | The split is settled by the orchestrator, not an invented majority rule |
| 8 onward | A receives payment, its guarantee is released, and B reimburses A's court fee | A becomes available after settlement |
| Handover | Once the applicable duty turn permits, A enters duty before B leaves it | Reserve becomes A, C, D, E; B may compete for ordinary work |

A's accounting:

| Event | Total wallet | Locked | Unlocked |
|---|---:|---:|---:|
| Start | 30 | 0 | 30 |
| Lock guarantee | 30 | 4 | 26 |
| Spend 7 on execution | 23 | 4 | 19 |
| Pay court fee 2 | 21 | 4 | 17 |
| Receive delivery payment 10 | 31 | 4 | 27 |
| Receive reimbursement 2 from B | 33 | 4 | 29 |
| Release guarantee | 33 | 0 | 33 |

A's net is $+3=B-C$. The guarantee return is not an extra four-credit reward.

B receives $\min(3,5)+2=5$, spends 3, and reimburses 2: net zero before any separately defined rating or other consequences.

C receives $\min(4,5)+3=7$ and spends 4: net $+3$ before other costs.

D receives the same fee and incurs the same cost, but its appeal assessment was overruled. It must lose currency, rating, or both under the agreed rule. The amount is left symbolic: wallet margin $3-\ell_D$ and rating increment $\epsilon_R-\rho_D$, with an adverse consequence required but not numerically chosen.

If the ruling instead upheld nonfulfillment and, **for illustration only**, failed-task compensation were zero, A would finish at:

$$30-7-2-4=17.$$

It would bear execution cost, court fee, and guarantee loss. Zero failed-task compensation is an example assumption, not a settled rule.

---

## 16. Rule and invariant checklist

These identifiers support later discussion and testing; they do not add software components.

| ID | Rule or boundary | Status |
|---|---|---|
| R01 | The purpose is economical request fulfillment over time, not maximum wealth or task count. | Agreed |
| R02 | We assess fulfillment against the request/context; ultimate personal value is outside the measurement boundary. | Agreed |
| R03 | Bid price, actual execution cost, and guarantee are distinct. | Agreed |
| R04 | An accepted delivery price is not an internal execution cap. | Agreed |
| R05 | Resource prices start fixed; numerical tariff remains to be set. | Agreed |
| R06 | Orchestrator selection learns predicted fulfillment using request/history and offer attributes. | Agreed direction |
| R07 | The winner locks its guarantee; locked currency cannot simultaneously be spent. | Agreed |
| R08 | Final fulfillment releases the guarantee; established nonfulfillment forfeits it. | Agreed; uncertain-result branches open |
| R09 | Ordinary task actors remain committed while awaiting review or dispute settlement. | Agreed |
| R10 | Actors cannot review their own work; fresh appeal reviewers exclude the original reviewers. | Agreed |
| R11 | The defined appeal adds two distinct eligible reviewers and the disputer's explanation. | Agreed |
| R12 | The orchestrator pays reviewers; the challenger pays a separate court fee. | Agreed |
| R13 | A successful appellant is reimbursed by the liable original verifier; a losing appellant bears fee and guarantee loss. | Agreed; initial-panel allocation open |
| R14 | The orchestrator can issue the final accepted ruling when needed. | Agreed |
| R15 | An overruled appeal reviewer incurs a loss; amount and currency/rating split remain open. | Agreed direction |
| R16 | Review payment is capped eligible-cost reimbursement plus a fixed fee. | Agreed |
| R17 | Ordinary-review starting example is cap 5, fixed fee 2; completed review adds small $\epsilon_R$. | Initial values / agreed structure |
| R18 | Dispute review pays a higher fixed fee; amount and appeal cap remain open. | Agreed direction |
| R19 | Time is discrete; occupying an assignment can cause missed opportunities. | Agreed |
| R20 | Reserve membership satisfies $\lvert\mathcal V_t\rvert\geq X$ and configured $X>V_{\max}$. | Agreed, subject to feasible population |
| R21 | Duty actors may be idle or reviewing; they are not ordinarily task-committed. | Agreed |
| R22 | Prefer volunteers; use eligible-available round-robin if none volunteer; otherwise wait. | Agreed |
| R23 | Review completion frees execution capacity even if later liability remains. | Agreed |
| R24 | Reserve membership rotates through replacement-before-release; it is not a permanent class. | Agreed; duty-turn length open |
| R25 | Initial learning direction is an adaptation of LeWorldModel; no native economic capability is assumed. | Agreed direction |
| R26 | Preserve committed history, attributed assessments, and rulings without silently rewriting past records. | Agreed trust-boundary principle |

**Formalization checks:** guarantee locking and release must not create or destroy total wallet value; court reimbursement must not be counted twice; spending beyond a delivery price must not automatically trigger forfeiture; unknown assessment must not silently become proven failure; reserve membership and current review availability must remain separate.

These checks are candidates for a later implementation's tests. This document does not claim such an implementation or a tested scheduler exists.

---

## 17. Open parameters and unresolved branches

A working interaction is now specified, but these choices must remain visible rather than be filled with defaults without discussion.

| Area | Still to decide |
|---|---|
| Assessment | Criteria ownership, evaluator choice, score calibration, category thresholds, and handling ambiguous criteria |
| Partial / unknown | Payment, retry, evidence gathering, settlement, and guarantee treatment when the answer is partial or cannot be assessed |
| Initial verification | Number of reviewers by task and how their assessments combine before a dispute |
| Selection | Score implementation, ties, unaffordable bids, empty eligible set, and any explicit preference for lower price at comparable fulfillment |
| Guarantee | Amount-setting rule, recipient of forfeitures, release timing, and treatment of a case that never reaches a ruling |
| Dispute | Court-fee size, appeal time window, withdrawal, failed-task compensation, and whether there is any further appeal after final adjudication |
| Multi-verifier liability | Who reimburses when several original reviewers supported an overturned rejection |
| Reviewer penalties | Currency/rating amounts, proportionality, collectible funds, and treatment of later insolvency |
| Review compensation | Appeal fee and cap, eligible-cost evidence, legitimate unknown reviews, service completion, and abuse of reimbursement |
| Rating | $\epsilon_R$, range, starting rating, update aggregation, decay, domain-specific evidence, and participation-versus-reliability interpretation |
| Reserve | Numerical $X$, maximum initial panel, definition of $V_{\max}$, case-specific exclusions, and treatment of population loss |
| Rotation | Duty-turn length, incoming/outgoing order, voluntary specialists, and temporarily unavailable replacements |
| Timing | Duration of a tick, simultaneous event order, review deadlines, long-running tasks, and scheduling of concurrent disputes |
| Progress | What happens when evidence cannot be obtained, all eligible reviewers stall, or the orchestrator cannot adjudicate |
| Learning | Economic observation/action representation, initial experience, training schedule, update privacy, actor/orchestrator parameter sharing, and confidence estimation |
| Funding | Source of reviewer payments and ordinary task rewards; orchestrator-owned versus administered funds; transfers versus currency destruction |

The protected reserve reduces a specific capacity risk. The compensation and guarantee rules create consequences. Neither constitutes a proof of truthful reports, economical behavior, fairness, or bounded completion time.

The model also does not solve insufficient demand, role collusion, repeated-identity creation, long-term wealth concentration, or strategic matching of the orchestrator's preferences. These remain wider economic questions, not reasons to erase the current agreements.

---

## 18. Deferred ideas and superseded alternatives

### Superseded or narrowed

- **Maximize task count or currency as the ultimate purpose:** not the preferred direction. The earnings alternative is retained for comparison.
- **Define usefulness by total human benefit:** outside the operational measurement boundary; fulfillment of the request is the chosen starting measure.
- **Choose actor economics or environmental selection:** both belong to the coupled interaction, not an either/or.
- **Always choose the cheapest offer, using rating only as a tie-break:** replaced by learned predicted-fulfillment selection using offer attributes and context.
- **Treat the bid as a hard internal spending limit:** replaced by committed delivery price; actual cost can exceed it.
- **Pay reviewers from the challenger's fee directly:** separated; the orchestrator pays review compensation and collects a court-like fee.
- **Either reimbursement or fixed review payment:** combined into capped reimbursement plus service fee, with a small rating increment.
- **Keep $X$ actors idle at every moment:** refined to $X$ actors outside ordinary commitments, either available on duty or actively reviewing.
- **Round-robin within one permanent reserve:** extended to rotation of reserve membership itself.
- **Hold a reviewer until every possible challenge ends:** rejected; execution availability and outstanding liability are separate.
- **Require a numeric chance constraint before an actor bids:** not selected; uncertainty is considered in commitments and learned decisions without an imposed probability threshold.

### Deferred, not quietly adopted

Insurance; transferable upgrades; adjustable resource prices; inflation; explicit bankruptcy/removal rules; starting calibration tasks; sold concurrency; nested subcontracting liability formulas; reviewer collateral; and global currency issuance policy.

Earlier commitments to a fixed cell taxonomy, mandatory internal intent–execute–observe stages, separate governance planes, or a new hardware operating system are not required by this specification.

---

## 19. Sources and decision provenance

### Conversation sources

The following anchors identify accepted discussion points. They support design provenance, not external empirical claims.

**[C0] Verifiable loops and trust boundary.** The earlier discussion established a persistent loop with an append-only past, a committed present, and a mutable future. It separated integrity from success or truth, described registration with an empty initial commitment, and accepted a trusted recording mechanism while excluding compromise of protected memory, firmware, or that authority itself.

**[C1] Purpose and measurement.** The user agreed: “The wallet supports the purpose; it does not define the purpose,” and later tightened the boundary: “we cannot say if something was useful to the user, only if it was fulfilled per his request.” The conversation distinguished fulfillment from activity and ultimate personal value.

**[C2] Pricing and commitment.** The user proposed initially fixed resource prices and corrected the spending question: “the actor will spend whatever it costs. the question is how much has it committed to,” using the Name That Tune analogy. The accepted interpretation separated delivery price from actual cost.

**[C3] Learning, selection, and guarantee.** The user chose LeWorldModel as the initial learning direction, accepted adaptation, proposed the orchestrator's learned “max(fulfillment | Bi, Ri, Gi)” selection, and accepted a guarantee against nonfulfillment.

**[C4] Verification and appeal.** The user proposed one or more reviewers of request/result, an actor's paid challenge, two other reviewers with the actor's explanation, reimbursement by the original verifier after a successful appeal, and fee-plus-guarantee loss after an unsuccessful appeal.

**[C5] Reviewer responsibility and final ruling.** The user proposed paid ordinary and higher-paid dispute review, losses for overruled dispute reviewers, and the orchestrator reviewing the request, response, original assessment, disputer's claim, and other assessments to make the final accepted decision.

**[C6] Time and compensation.** The user specified fixed time units, a possibly empty request pool, missed opportunities while reviewing, orchestrator-funded reviewer fees distinct from court fees, and capped reimbursement plus a fixed fee and a small rating boost. Five credits and two credits were the starting example.

**[C7] Mandatory review and blocked actors.** The user specified round-robin mandatory assignment when nobody volunteers, waiting when no actor is available, and the ordinary actor remaining “stuck” pending verification.

**[C8] Reserve and rotation.** The user agreed to a reserve outside ordinary commitments that may be idle or reviewing, no self-review, review completion releasing execution capacity, $X>V_{\max}$, and replacement-before-release rotation rather than a permanent verifier class.

### Existing project record

**[M1]** [_line — The actor and its economic life](https://app.thinkunderline.com/a/953d00ac-786c-46fb-876e-140d71633788?at=section_01), revision 4, read when preparing this document. It preserves the earlier Section 1 discussion; the later conversation above supplies the newer task-contract and review rules. The map remains unchanged by this file creation.

### Technical background checked for this document

**[S1]** Lucas Maes, Quentin Le Lidec, Damien Scieur, Yann LeCun, and Randall Balestriero. [LeWorldModel: Stable End-to-End Joint-Embedding Predictive Architecture from Pixels](https://arxiv.org/html/2603.19312v3), version 3, 2026. Sections 3.1–3.2 support the limited research description in Section 13. They do not establish the proposed economic adaptation.

**[S2]** IETF. [RFC 9162: Certificate Transparency Version 2.0](https://www.rfc-editor.org/rfc/rfc9162.html), 2021. Background on authenticated append-only logs, tree commitments and consistency proofs. The economic loop does not adopt Certificate Transparency as its protocol.

---

## Closing statement

This specification is a coherent record of the interaction we agreed to explore:

> **Actors make priced commitments, execute at their own cost, and submit results for paid independent review. Challenges have explicit consequences. The orchestrator supplies final adjudication when needed. A protected, rotating review reserve keeps capacity out of ordinary commitments. Experience and recorded outcomes inform subsequent decisions, while committed history remains intact.**

It is complete enough to reason about this loop without repeatedly reconstructing the conversation. It deliberately does not disguise open assessment, settlement, financing, or learning choices as already selected rules.

# Agentic Economics — The Task, Verification, and Dispute Loop

## Design revision 1 — specification 1.1.0-rc.3: the verification deposit is two pots

**Project:** ELEF / Agentic Economics  
**Version:** 1.1.0-rc.3 — a release candidate, not yet in force. rc.1 was the proposal as first sent (October 16); rc.2 adopted the six points of the implementation review [I1]; rc.3 settles its three follow-up notes [I2]: the requester's net cost figure, who is paid by the fee pot's remainder, and the provenance. On acceptance it becomes **1.1.0**, consolidated into one standalone text, and 1.0.1 moves to history.  
**Versioning from here (semver):** patch = wording only, no rule changed (1.0.0 → 1.0.1); minor = a design revision under §19 (1.0.1 → 1.1.0); major = a change of approach. A proposal under review is a release candidate (`-rc.N`).  
**Prepared:** October 16, 2026; rc.2 and rc.3 October 17, 2026  
**Supersedes:** 1.0.1 (October 15, 2026) where this document speaks; everywhere else 1.0.1 stands unchanged.  
**Nature of this revision:** A **design revision** under §19 of the baseline — the first since the freeze. It changes one rule: how a reviewer is paid. It is labeled as such, is to be read on its own before it is implemented, and is accompanied by the evidence that required it. It adds no participant, no verdict, no challenge, no state.  
**Status:** Proposed. Becomes the baseline when Baruchi accepts it and the reference implementation reproduces the figures in §6.

> **The wallet supports the purpose; it does not define the purpose.**
>
> **The actor competes on its promise, is assessed on its delivery, and bears the cost of its execution.**
>
> **Money enters with requests. Truth enters with requesters. Verification is the security work of the economy.**
>
> **Care is paid for, not charged for.** *(new)*

---

## 1. Why: what strategy run 1 found, and where the rule came from

**The finding [S1].** The first scoped run of the frozen baseline — §18.1 question 1, careful versus careless review, ten runs at the defaults — showed that careful review does not beat stamping. With half the reserve stamping, stampers ended richer in four of five seeds, +249 credits per actor over 1,000 ticks; 47% of truly failed work was paid in full. With nine stampers in ten, 88% was. The dominant channel was not the bond or the audit rate but the fee: a careful reviewer earned 7.90 per review and a stamper 9.54, a gap equal to the careful reviewer's own expenses.

**The mechanism.** Under v1.0.1 §4.3 the verification deposit $\varphi$ is one pot doing two jobs. A reviewer's capped expenses are reimbursed from it at completion, and *what remains of it* is divided among the surviving reviews as their fee. So every credit of expense reimbursed is a credit of fee lost: a reviewer that spends 3 on care is reimbursed 3 and then receives a fee 3 smaller than a reviewer that spent nothing. The reimbursement is real on paper and worth nothing in the wallet. At the margin the rule charges for diligence.

**Where it came from.** This was not a decision. v0.1 R16, marked *Agreed*, set review pay as **capped expense reimbursement plus a fixed fee** (R17: cap 5, fee 2), with the note that "the fixed fee is for review work, not for reaching 'fulfilled' rather than 'not fulfilled.'" v0.2 made the fee an emission share plus an equal share of the deposit — still fixed in effect. v0.3, repairing the second review's shortfall finding (a 10-credit deposit cannot pay 5 of reimbursement *and* a 10-credit fee), made the fee the **remainder of the deposit after reimbursements**. The accounting closed; the incentive inverted; and nobody noticed for seven versions because each sentence is correct on its own. The giveaway stood in plain sight: §7.3's stamping hypothesis still reasons with an "expected surviving fee" $\bar f = 2$ — the fixed fee of R16 — while the rule beside it pays a residual.

**Classification.** A design revision motivated by a strategy finding, and justified by the spec's own §7.3, which assumes a fixed fee the rule does not pay. §7.3 is a hypothesis and R16 is history, so this is not strictly "two active rules contradict"; it is the case §19 permits when a revision is labeled as one and read on its own — which this document is. It restores a decision already on the record rather than inventing a new one. The two default knobs the run also implicated — the selection tie band and the audit floor — are **not** part of this revision; they remain defaults, to be swept separately so the effect of this rule is measured in isolation.

---

## 2. The rule (replaces v1.0.1 §4.3 "Reimbursement" and "Settlement — one rule", and the formula of §7.3)

### 2.1 Two pots

**Rule.** The verification deposit of a root request is two named amounts, both paid in by the root requester at award:

$$\varphi_q = \varphi^E_q + \varphi^F_q ,$$

the **expense allowance** $\varphi^E$ and the **fee pot** $\varphi^F$. Both belong to the root case and serve every review in its tree; nested cases carry $\varphi^E=\varphi^F=0$ as before. The pay-in of §4.1 becomes $\text{pay-in}_q = B + \varphi^E_q + \varphi^F_q + \omega_q$.

**Rule.** Money in one pot is never used for the other's purpose, with one exception stated in §2.3: fee money that no surviving review is owed may cover expenses.

### 2.2 Expenses: reimbursed, up to the cap, from the allowance

**Rule (unchanged in substance).** At completion each review is reimbursed $\min(\text{credits spent}, K)$. Spending above $K$ is the reviewer's loss. The reimbursement is paid from the root's $\varphi^E$; if $\varphi^E$ is exhausted, advanced by the operating account $\Omega$; if $\Omega$ cannot cover it, deferred to settlement as a cost debt. A review resumed after a resubmission is one assignment under one cap. Overturned and withdrawn reviews keep their reimbursement; the bond was the penalty, the cost was not.

### 2.3 Fees: fixed by role, from the fee pot

**Rule.** Every surviving review $v$ of case $q$ — completed, not overturned, not withdrawn — is owed a **fixed fee** $f_{r(v)} = w_{r(v)}\,f$, where $f$ is the ordinary-review fee and $w$ the role weights already defined (ordinary 1, appeal 1.5, audit 1.5), plus its emission share $e_v$ exactly as in v1.0.1 §4.2. The fee does not depend on what the reviewer spent, on what any other reviewer spent, or on how much of the allowance is left.

**Settlement — one rule (replaces v1.0.1 §4.3 steps 1–4).** At the tick a case vests or reaches final $\mathsf N$, with $\mathrm{Surv}(q)$ its surviving reviews and $\mathrm{Owed}_q = \sum_{v\in\mathrm{Surv}(q)} f_{r(v)}$:

1. *Expense debts first, for every review of the case* — surviving, overturned, or withdrawn with a reimbursable balance: deferred reimbursements are paid, then $\Omega$'s advances are repaid, **from what remains of $\varphi^E$ only**. What it cannot cover: a deferred reimbursement becomes a named reviewer claim on $\Omega$; an advance already paid stays an unrecovered advance borne by $\Omega$ — exactly as in v1.0.1. The fee pot is not touched at a case's settlement, because other cases in the same tree may still be owed from it.
2. *Fees.* Each surviving review receives $f_{r(v)}\cdot\min\!\big(1,\ \varphi^F_{\text{left}}/\mathrm{Owed}_q\big)$ from the fee pot — scaled pro rata only when what is left of the pot cannot pay every fee of this case in full — and its emission share $e_v$, minted and paid in full. An overturned or withdrawn review receives no fee.
3. *At tree closure* (§2.4), when every fee in the tree is known and paid: what remains of the fee pot settles the tree's own expense debts — first **this tree's outstanding reviewer claims, paid to the claimant reviewers directly, each claim retired from $\Omega$'s queue as it is paid**; then this tree's unrecovered advances, repaid to $\Omega$ — and only then does whatever remains of $\varphi^E$ and $\varphi^F$ return to the root requester as unused. A requester's deposit services its own tree's verification before anyone else's: it is not an inflow to $\Omega$ and does not wait in $\Omega$'s first-in-first-out line, which governs $\Omega$'s own money (service fees, court fees) alone. This is the one movement of fee money toward expenses, and it uses only money no review in the tree is owed.

With no surviving review, step 2 pays nothing and step 3 returns both pots after step 1. The rounding residue of minted emission goes to $\Omega$; deposit never does.

*Why the cross-pot step waits for closure [I1].* Computed per case, "unowed fee money" would be wrong in a tree: a root overridden while its nested case is still pending has no surviving review, so its whole pot would look unowed and could pay the root's deferred expenses — and the nested case's appeal reviewers, owed from the same pot, would then get nothing. At closure the tree's $\mathrm{Owed}$ is complete and the step is safe.

### 2.4 Nested reviews and when the refund happens

**Rule.** The expenses and fixed fees of a nested case's reviews draw on the root's $\varphi^E$ and $\varphi^F$ at the nested case's own settlement, exactly as the root's reviews do at the root's. The root requester's unused deposit therefore returns **when the tree is closed** — the root and every nested case under it have settled — not at the root's vesting alone. A tree cannot stay open long past its root: every nested case has reached its milestone before the root could submit, and nested vesting is independent of the parent's (v1.0.1 §9). Two consequences for the engine, recorded here because they are rule-level: a nested settlement draws on a root's pots after the root has vested, and the closure refund moves the root's money after its vesting — so invariant I4 (no money moves on a vested case) gains those two exceptions and no others; and a root whose pots are still open must remain reachable until closure.

### 2.5 The operating account

**Rule (amended).** $\Omega$ receives service fees and court fees, advances expenses when an allowance is exhausted, and is repaid only as §2.3 allows — from the allowance's remainder at each settlement, and from the fee pot's remainder at tree closure. An advance those cannot repay is $\Omega$'s own loss, funded by the service fee $\omega$; $\Omega$ is thereby the pooled expense fund of the economy, and $\omega$ is the premium every request pays toward expense overflow in any tree. Reviewer claims on $\Omega$ are serviced first in, first out on every inflow, as before. The aggregate of claims and unrecovered advances is monitored (§18).

### 2.6 Defaults

**Default.** $K=5$ (unchanged). $f=2$ per unit of role weight: ordinary 2, appeal 3, audit 3. $\varphi^E=2K=10$. $\varphi^F=f\,(w_{\text{ordinary}}+w_{\text{audit}})=5$ — sized for the common full case, one review and one audit. Root pay-in at $B=40$: $40+10+5+\omega$. $\omega=5\%$ of $B$ (unchanged; expected to move under §18 question 3).

**Default under consideration.** $K=3$, $\varphi^E=6$, $\varphi^F=5$ — total deposit 11, one credit above today's. Run 1's careful reviewers cost 2–3. The sweep decides; moving $K$ is a default change, not a rule change.

**Consequence — reviewer income from deposits falls, and the fee level is the lever [I1].** Under v1.0.1 an uncontested single review took the whole deposit remainder, about 10 credits; under v1.1 it takes $f=2$ plus emission, and the requester is refunded about 8. In the common case the deposit flow to reviewers drops by roughly three quarters, the requester's net deposit cost falls from 10 to between 4 and 7 (fee 2 plus the reviewer's actual expense of 2–5), and emission carries a larger share of reviewer income than the baseline intended ("deposits take over as emission fades" no longer holds at $f=2$). Whether reviewers can still fund the bond $G^V=5$ and their care from unlocked credit — run 1 saw one careful reviewer unable to afford its care — is a solvency question for §18.1 questions 3 and 6. $f$ is a default; the rerun of §8 carries $f\in\{2,4\}$.

**Consequence.** A challenged case has three surviving reviews at most (one initial, two challenge) or two challenge reviews after an overturn; with $\varphi^F=5$ the fee pot is short for two challenge fees (6) and step 2 scales them to 2.5 each. This is deliberate: the pot is sized for the common case, the shortfall is small, and challenge reviews also carry the 1.5 emission weight. Sizing $\varphi^F$ for the worst case ($f(1+2\cdot1.5)=8$) is a default the sweep may choose. In a tree the nested reviews settle first and draw first, so a root with delegated children may see its own reviews' fees scaled; whether the pots should grow with the tree is part of §18 question 3, as the allowance's sizing already was.

---

## 3. Consequences for the stamping arithmetic (replaces v1.0.1 §7.3)

**Compensation.** $\Pi_{jv}=\min(\text{spent},K)$ at completion, plus $\big(f_{r(v)}+e_v\big)\cdot\mathbb 1[\text{verdict stood}]$ at settlement.

**Consequence.** Within the cap, care costs the reviewer nothing: a careful reviewer that spends $c\le K$ is made whole and earns the same fee as one that spent nothing. The fee is for the work of reviewing, not for the answer, and not for the thrift.

**Hypothesis (restated).** Let $p$ be the effective audit rate, $b$ the base failure rate, $\varepsilon$ the careful reviewer's error rate, $\bar f=f+\bar e$ the surviving fee with emission, $G^V$ the bond. Per review,

$$\mathbb E[\Delta W_{\text{stamp}}]-\mathbb E[\Delta W_{\text{careful}}] \;=\; -\,p\,b\,(1-\varepsilon)\,\big(\bar f+G^V\big)\;-\;(\text{reliability loss}) \;<\;0 \quad\text{for every } pb>0 .$$

**In the regime of run 1 — actors accept every rejection, no appeals** — stamping is weakly dominated in money and strictly dominated once reliability loss counts: the opposite sign of v1.0.1 §7.3, where the same quantity was $+1.3$ at the defaults and was measured at $+1.5$. **With actor appeals in scope the inequality gains a term stampers never pay:** a careful reviewer rejects good work at rate $\varepsilon(1-b)$, an appealed and overturned false rejection costs it $\bar f+G^V$, so the right-hand side becomes $-\,pb(1-\varepsilon)(\bar f+G^V)+a\,\varepsilon(1-b)(\bar f+G^V)$ with $a$ the rate at which false rejections are appealed and overturned. The sign then depends on $pb(1-\varepsilon)$ against $a\varepsilon(1-b)$ — at $\varepsilon=0.05$, $b=0.2$ it stays negative while $pb>0.04\,a$, which the defaults satisfy, but it is no longer unconditional. The appeals run (§8) measures $a$. At the defaults with run 1's effective catch rate of about 3%, the money term is roughly $-0.3$ per review; at the nominal $p=0.5$, $b=0.2$, about $-0.7$. How *fast* stamping loses, and whether the reliability channel adds anything at the current tie band, is what the rerun of §18.1 question 1 must now find. A verdict that survives is procedurally settled; it is not thereby correct.

---

## 4. What does not change

Verdicts and their availability (§3); emission (§4.2); the backed credit and the halt state (§4.4); denomination at first lock (§4.5) — both pots are frozen with the case; offers, selection, the guarantee (§5); the lifecycle and tick order (§6); the cap $K$, the bond, timeouts, replacement (§7); every challenge, the two-question appeal, audits, rulings (§8); delegation, the rejection bond, one guarantee one obligation, milestones, exits (§9); reliability and duty credit (§11); the reserve and rotation (§12); the record (§13); the reviewer's view (§14); the human, overrides, corrections, label grades (§15); permitted, forbidden and not-offered operations (§16). The service fee $\omega$ still goes to $\Omega$; court fees still go to $\Omega$ and are still reimbursed to a winning challenger from the loser's bond; the rest of a forfeited bond still burns — it does not fund fees.

Nested cases still carry no deposit of their own; the chain still pays for its own checking once, through the root.

What *does* move besides the rule: the amount of deposit money that reaches reviewers (§2.6, first consequence), and the two I4 exceptions of §2.4. "Nothing else moves" in rc.1 of this document was wrong on both counts.

---

## 5. Invariants and notation (amendments)

**I1** (conservation) is unchanged and covers both pots. **I17** is extended: the allowance and the fee pot are accounted separately; reimbursement fields are non-negative and within the cap; every claim on $\Omega$ names a review whose pending balance covers it. **I4** (no money moves on a vested case) gains exactly two exceptions: a nested case's settlement drawing on its root's pots, and the root's refund at tree closure. **I19 (new) — the pots.** For every tree, fees paid from the pot $\le\varphi^F$; fee money used for expenses $\le$ the pot's remainder after every fee in the tree was paid, and only at closure; no fee was paid from $\varphi^E$; a refund occurs only when the tree is closed. Record mode: a root whose pots are open is not paged out until closure (or its child's settlement reaches it on disk).

**Notation (Appendix C, additions).** $\varphi^E$ expense allowance; $\varphi^F$ fee pot; $f$ ordinary-review fee; $f_{r}=w_r f$ fee by role; $\mathrm{Owed}_q$ the sum of fees owed to a case's surviving reviews.

**Defaults (Appendix A, amended rows).** $\varphi$ root → $\varphi^E=10$, $\varphi^F=5$; nested 0 / 0. $f=2$. $\omega=5\%$ of $B$.

**§18.1 (amended questions).** *Q1:* under v1.1, how fast does stamping lose — and does the reliability channel add anything at the current tie band? *Q3:* does $\varphi^E=2K$ cover root-plus-nested expenses; how often does $\Omega$ advance; how much does it bear unrecovered; is $\omega=5\%$ enough to fund it?

---

## 6. The worked example re-settled (v1.0.1 §20 under v1.1)

Same setup: six actors; C, D, E, F on duty; H posts $q$ with $\beta=45$; A bids $B=40$, $\tau=8$, locks $G=20$; A delegates $q'$ to B ($B'=5$); B's work costs 3, A's own costs 12, C and D each cost 3; emission at the settlement tick is 5 — C (weight 1) gets 2, D (1.5) gets 3. $\omega$ omitted.

**H pays** $40+10+5=55$ (was 50).

| Tick | Event |
|---|---|
| 6 | C: $\mathsf F$, reimbursed 3 from $\varphi^E$ (7 left); audit rolled, D assigned |
| 8 | D: $\mathsf F$, reimbursed 3 from $\varphi^E$ (4 left); agrees |
| 13 | $q'$ vests: B paid 5, $G'$ released — $q'$ had no review of its own in this example |
| 16 | $q$ vests, H silent: A paid 40, $G$ released. Fees: C $f=2$, D $3$; $\mathrm{Owed}=5=\varphi^F$, paid in full. Emission: C 2, D 3. Tree closed: $\varphi^E$ remainder 4 returns to H |

**Nets.** A $+23$ (unchanged); B $+2$ (unchanged); C $+4=-3+3+2+2$ (unchanged, by coincidence: the old remainder share happened to equal $f$); D $+6=-3+3+3+3$ (was $+5$); H $-51$ (was $-50$); $\Omega$ untouched. Escrow: in 55 $=40+6+5+4$ out.

**Under the default under consideration** ($K=3$, $\varphi^E=6$, $\varphi^F=5$): H pays 51; both reimbursements exhaust the allowance; fees as above; refund 0; every net is identical. The requester pays one credit more than under v1.0.1 and the careful reviewers are made whole.

**Variants.** *Rejection and appeal:* C overturned — bond 2 to A, 3 burned, costs reimbursed, no fee; E and F surviving appeal reviews owed 3 each, $\mathrm{Owed}=6>5$, paid 2.5 each plus emission. *Pool exhaustion, cancellation, deadline:* unchanged in logic; refunds are now of both pots.

---

## 7. Implementation note (what the engine must do; no code here)

- The ledger's case pool holds two named balances, allowance and fee pot, frozen at first lock like every other case amount.
- Reimbursement at completion draws on the allowance, then $\Omega$, then defers — as now, from the new balance.
- Settlement follows §2.3 in order; the "unowed fee money may pay expenses" step is the only cross-pot movement and is recorded as such.
- The refund waits for tree closure; the engine already knows a case's children and their terminal states (I7).
- I19 is added to the per-tick checks; I17's accounting is split by pot.
- Drivers: the stamping driver's declared operations are unchanged; its per-population metrics gain *fixed fee paid* and *fee haircut* columns, and the economy metrics gain *$\Omega$ unrecovered advances*.

**Tests [I1].** The baseline's own suites are revised to the v1.1 figures where they pin fee or refund amounts to the old remainder: `test_spec.py` (main path nets, appeal variant, pool exhaustion, nested rejection, shortfall haircut), `test_v06.py` (cost debts before refund), and three asserts each in `test_v05.py` and `test_v09.py`. Golden History heads in the perf-equivalence and record-mode tests change because money flows change; they are re-pinned as the v1.1 goldens, not treated as failures. Reviewer-authored tests are **not edited**, and under the §2.3 wording of rc.2 none needs to be superseded: review 18 pins the human's wealth, 990 under both rules; r4_08 pins allowance arithmetic unchanged at $\varphi^E=10$; r4_07 passes with the tree-closure step (it would have failed under rc.1). A new `test_v11.py` carries the §6 figures and the I19 cases. Every other test must still pass unchanged; a failure elsewhere is a conformance bug, not a consequence of this revision.

---

## 8. After acceptance

1. Implement, and reproduce §6.
2. **Rerun strategy run 1 with only this rule changed** — same shares, same defaults for the tie band and audit floor — but with enough power to see a small effect [I1]: the predicted money term at run 1's catch rate is about $-0.3$ per review, roughly $-55$ per actor over a run, against a seed-to-seed spread of about $\pm160$. So: **20 seeds or more**, at both $X=4$ (run 1's reserve, which was saturated in 92–96% of ticks) and $X=8$, and at $f\in\{2,4\}$. The $X=4$, $f=2$ cell is the like-for-like comparison with run 1; the others separate the fee level and the capacity ceiling from the rule.
3. Then the default sweep (band, audit floor, bond), the appeals run — which measures the $a$ of §3 — and the requester-dispute run, in that order.

---

## 9. Provenance

**[S1] Strategy run 1 (October 16, 2026)** — `agentic_sim/results/runs/`, ten runs, engine `5425909`; write-up in the hand-off section *First scoped result — stamping at the defaults* (the only write-up the repo holds; a longer analysis lives in the ELEF project workspace outside the repo and is not cited as provenance here). **[I1] Implementation review of rc.1 (October 17, 2026)** — found the per-case "unowed fee money" defect in trees (r4_07), the I4 and record-mode consequences, the reviewer-income consequence, the appeals-regime qualification of §3, the test list corrections, and the statistical power the rerun needs; all adopted in rc.2. **[I2] Implementation review of rc.2 (October 17, 2026)** — verified the tree-closure step against the lifecycle (no new edge), r4_07 passing, the §3 threshold, and the rerun's power; three notes, all adopted in rc.3. **[R2]** — the second review's shortfall finding, which v0.3 repaired by making the fee a residual; the repair was correct accounting and lost an agreed decision. **[C6], v0.1 R16–R18** — the original decision: capped reimbursement plus a fixed fee, the fee for review work and not for the answer. This revision returns to it with the funding that was missing in v0.2.

---

## Closing statement

> A reviewer that does the work is made whole for it and paid the same fee as one that did not; the one that did not carries the bond and the record. The deposit says what it is for in two amounts, and neither pays for the other. Nothing else moves. Run it again, and see what stamping does when it is no longer paid to be careless.

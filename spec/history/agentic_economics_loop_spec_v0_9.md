# Agentic Economics — The Task, Verification, and Dispute Loop

## Working specification v0.9

**Project:** Agentic-OS / Agentic Economics  
**Prepared:** October 15, 2026  
**Supersedes:** v0.8 (October 15, 2026). Where this document is silent, v0.8 and its predecessors stand.  
**Nature of this revision:** A fifth conformance pass. The seventh external review [R7] ran the v0.8 implementation against seven targeted checks with ten passing controls, under full defaults, and found four groups: two correction-logic defects, a disagreement between the documented reviewer contract and the engine, and an authority boundary the spec had left to a reading. Two of the four needed a rule, decided in discussion; two were defects. No economic mechanism is added.  
**Status:** As in v0.8. The reviewer's closing characterization is adopted as the state of the work: the ordinary paths and previous repairs hold; what remains is in how assessments become authority, corrections, and learning signals, not in the task–payment loop.

> **The wallet supports the purpose; it does not define the purpose.**
>
> **The actor competes on its promise, is assessed on its delivery, and bears the cost of its execution.**
>
> **The past is append-only. The present is committed. The future is mutable.**
>
> **Money enters with requests. Truth enters with requesters. Verification is the security work of the economy.**
>
> **The human is the battery — and holds the plug.**

### What changed from v0.8

| Finding [R7] | v0.9 resolution |
|---|---|
| A. A post-settlement correction that changed only the objection of a ⊥ appeal did not reach the appeal reviewers | The correction applies each appeal reviewer's **complete** two-question answer, exactly as settlement does (§15.2) |
| B. A correction admitted between a case's finality and its reviews' payout batch was lost for reviews still awaiting payout | A ruling before a review's payout is a ruling *for that review*: a contradicted review still unsettled is overturned; one already paid takes the reliability record only (§15.2) |
| C. The documented fulfillment contract offered F/N/P/⊥, but an audit secretly accepted only F/N; a refusal could reveal the role | **Rule:** an auditor may answer P or ⊥; identical views admit identical answers. On an audit, P/⊥ suspends the approval and reopens the actor's response, as an initial reviewer's would (§8.3) |
| D. A delegate could invoke the human override | **Rule:** a delegate holds no ruling authority. It posts, pays, accepts and disputes; only a human rules (§15.2) |

---

## 8.3 An auditor may ask for more

**Agreed (new rule).** The reviewer view does not distinguish an initial review from an audit, so the set of admissible answers must not distinguish them either — a refusal is an observation. A fulfillment question is therefore answered $\mathsf F$, $\mathsf N$, $\mathsf P$ or $\bot$ on an initial review and on an audit alike.

On an audit, $\mathsf P$ or $\bot$ means what it means on an initial review: the auditor needs something from the actor before it can judge. The approval under audit is **suspended**, not overturned — nothing has yet shown it wrong — and the case reopens the actor's response window with the auditor attached as its current assessor. From there the ordinary paths apply, with the auditor in the initial reviewer's seat:

- the actor **resubmits** (revision or evidence) and the auditor answers $\mathsf F$ or $\mathsf N$: $\mathsf F$ reinstates the approval and the audit agrees; $\mathsf N$ reinstates it and the audit disagrees, opening the audit challenge as usual;
- the actor **appeals** the $\bot$: two fresh reviewers answer the two questions; a rejected objection overturns the *auditor*, reinstates the approval, and the actor's fee is reimbursed from the auditor's bond; an upheld objection settles the case $\mathsf N$;
- the actor **accepts** $\mathsf N$ or misses the window: the case is final $\mathsf N$, and the suspended approval was premature — the initial reviewer is overturned at finalization.

A suspended approval is off the challenge path while suspended, and an overruled reopening audit leaves the path, so every branch fits within $V_{\max}=3$. [R7-C]

---

## 15.2 Authority, corrections, and the payout boundary

**Agreed (new rule).** A delegate — a system acting on a human's budget — is a requester. It posts, pays, accepts and disputes, and every one of those runs through the economy's own machinery: a fee, a panel, a verdict it can lose. The human override is the one action that bypasses that machinery, and the only ground for it is that a human's judgment is not a model's opinion of another model (§1, v0.2). A delegate is exactly what that argument excludes. **A delegate cannot rule.** If a delegate disagrees with an outcome, it disputes; if its principal wants to overrule, the principal does. The harness now names its requesters and derives its humans as the requesters that are not delegates. [R7-D]

**Agreed (clarified).** A correction after settlement compares the ruling with each reviewer's **complete** assessment. An appeal reviewer of a $\bot$ answered two questions and is contradicted on either: an objection disposition that differs from the ruling's, or — when the objection is rejected — a fulfillment verdict that differs from the outcome. This is the same rule settlement applies (§8.1); the correction branch now applies it rather than the verdict alone. [R7-A]

**Agreed (clarified).** Case finality and review settlement are two events, and a ruling that arrives between them is *before* settlement for the review's purposes. A contradicted review that has not yet reached its payout batch is overturned as any pre-settlement ruling would overturn it — bond forfeited, no fee, reliability down. A contradicted review that has already been paid takes the reliability record only, and no money moves. Nothing in this is a clawback; the money of an unsettled review had not moved. [R7-B]

---

## 17. Rules and invariants (changes)

R82 identical fulfillment views admit identical answers; R83 a reopening audit suspends, does not overturn; R84 delegates cannot rule; R85 corrections compare complete assessments; R86 a ruling before payout overturns an unsettled review. I8 counts a suspended approval and an overruled reopening audit as off the path.

---

## 21. Provenance

**[R7] Seventh external review (October 15, 2026), of v0.8 and its implementation.** Verified the v0.8 repairs under full defaults and all three entry points; found the four groups resolved above; was explicit that two of them were readings to confirm, not merely code to fix, and declined to choose either — the audit contract and the delegate's authority — and gave the scoped-run advice adopted in §22. Its reviewer notes, shared separately, add the point that a refusal of P/⊥ on an audit would itself reveal the role, which decided the direction of §8.3.

---

## 22. Reference implementation and scoped runs

`agentic_sim/` as in v0.8 with the changes above. Suites: 23 + 19 (+1 expected failure) + 15 + 14 + 10 + 14 + 9 + 15 + 6 + 17 (the seventh review's checks and controls, verbatim) + 8 (v0.9 explicit form) — `python3 run_tests.py`: 148 pass, 1 expected failure; raw pytest and the no-site-packages runner agree. The runner expands stacked parametrization as pytest does.

**Agreed (standing rule for experiments).** A strategy run states its **permitted operations** before it runs. A run on a subset — root cases only, F/N reviewers, human rulers, no post-settlement corrections — is legitimate and interpretable, provided it says what it does not exercise. A result from a path the run excluded is not a result. [R7]

**Bracketed, unchanged:** strategies, learned selection, evaluator behavior, authorization among humans, an external commitment of the history head, physical time, the real-value exchange behind $\mathrm{Res}_t$.

---

## Closing statement

> An auditor who cannot judge says so, and the actor answers, as with any reviewer. A delegate requests; a human rules. A correction reads the whole answer it corrects. A ruling that arrives before a review is paid is a ruling for that review. The task–payment loop has held through seven reviews; what the last three have been reconciling is how judgment becomes authority and record. The next run states what it permits, and runs.

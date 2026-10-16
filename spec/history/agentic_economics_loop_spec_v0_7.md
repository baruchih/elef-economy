# Agentic Economics — The Task, Verification, and Dispute Loop

## Working specification v0.7

**Project:** Agentic-OS / Agentic Economics  
**Prepared:** October 15, 2026  
**Supersedes:** v0.6 (October 15, 2026). Where this document is silent, v0.6 and its predecessors stand.  
**Nature of this revision:** A third conformance pass. The fifth external review [R5] ran the v0.6 implementation against ten boundary checks at the edges of the v0.6 repairs, with four passing controls, and found seven groups of departures. Two needed a rule; the rest needed one definition where two had crept in, or validation before mutation on a path that had it only partly. This revision takes the two rules and finishes the paths. No economic mechanism is added.  
**Status:** As in v0.6. The review's framing is adopted: the counterexamples are selected, not sampled; a fully passing suite does not show the incentives are sound; strategy runs remain the only evidence about them, and should be run only once a release's known conformance defects are repaired or explicitly excluded.

> **The wallet supports the purpose; it does not define the purpose.**
>
> **The actor competes on its promise, is assessed on its delivery, and bears the cost of its execution.**
>
> **The past is append-only. The present is committed. The future is mutable.**
>
> **Money enters with requests. Truth enters with requesters. Verification is the security work of the economy.**
>
> **The human is the battery — and holds the plug.**

### What changed from v0.6

| Finding [R5] | v0.7 resolution |
|---|---|
| A. An unfunded dispute cleared the vacated-audit obligation before the fee was refused | The fee and every admission requirement are checked before the obligation is touched; a refused filing leaves the suspension in place (§8.2) |
| B. A human acceptance of a submitted child, before the requester-actor judged it, left the rejection bond locked and failed I17 after payment | The rejection obligation ends when a ruling accepts the result, whether or not the requester-actor had judged; a contradicted rejection still forfeits (§15.2) |
| C. An audit admitted after an override compared the auditor to the overruled verdict: a contrary audit was paid as agreeing, an agreeing one left the case stuck | **Rule:** no audit after a human ruling — the ruling settled the question; an audit open at the ruling is voided; any audit's agreement is judged against the live assessment (§8.3, §15.2) |
| D. Replacing a timed-out reviewer on a resubmitted result reset the F/N-only stage | The resubmission stage is a property of the submission, not of the reviewer; a replacement inherits it (§6.1) |
| E. A parent could submit after a child missed its delivery, then I7 rejected the state | **Rule:** a nested request's terminal state is a milestone; the submit guard and I7 use one definition (§9.1) |
| F. The appeal's grounds reached reviewers but were not in the chain | The challenge's admitted parameters — kind, challenger, the assessment appealed, the grounds — are committed as one entry (§14) |
| G. Working copies were checked for edits, not for omissions or order | I16 reconciles each copy's membership and order against the committed entries (§14, §17) |

---

## 6.1 The resubmission stage belongs to the submission

**Agreed (clarified).** Once an actor has revised or supplied evidence, the submission is in its resubmitted stage and is assessed $\mathsf F$ or $\mathsf N$ only. The stage is carried by the case, so a reviewer who replaces one that timed out inherits it; the reviewer view says so (`resumed`). Allocating a new review does not grant a new $\mathsf P$ or a new $\bot$. [R5-D]

---

## 8.2 Dispute admission is checked whole

**Agreed (clarified).** A dispute is admitted only if the round is free, the window is open, and the challenger can fund the court fee. These are checked before anything changes: the fee is collected, the challenge recorded, and only then is any vacated audit obligation taken over by it. A refused filing leaves the case exactly as it was, suspension included. [R5-A]

---

## 8.3 / 15.2 No audit after a ruling

**Agreed (new rule).** A human ruling before vesting settles the case's assessment for that phase. No audit may be assigned to the case afterwards — the assignment is refused without effect — and an audit open at the ruling is voided with the other unfinished assignments. The reason is the one §8.3 already gives for audits: they test whether a model's verdict should stand, and the ruling has answered that. An audit assigned before a ruling but completed after one does not arise, since the ruling voids it. Where an audit completes, its agreement is judged against the case's **live** assessment (the outcome if one has been ruled, else the verdict), never against a verdict that has been superseded. [R5-C]

**Agreed (clarified).** Under any ruling, a requester-actor's rejection bond is reconciled by the obligation that results, not only by whether a verdict was contradicted: a ruling that contradicts a rejection forfeits the bond; a ruling that accepts the result — including one made before the requester-actor had judged at all — ends the rejection obligation and releases it; a ruling that confirms a rejection releases it at the case's settlement as before. [R5-B]

---

## 9.1 A terminal child is a milestone

**Agreed (new rule).** The milestone a nested request must reach before its parent submits is its initial verdict **or any terminal state** — withdrawn, cancelled, or final $\mathsf N$ without a submission, as when the subcontractor misses its delivery. In the last case the parent carries the failure as its own risk, which §9.2 already says, and $B$'s guarantee has gone to $A$. The submission guard and invariant I7 use this one definition. [R5-E]

---

## 14. The record (completed)

**Agreed (clarified).** An admitted action is committed *with its material parameters*. For a challenge that means the kind, the challenger, the assessment under appeal, and the grounds the reviewers will examine, as one entry; two appeals with different grounds have different heads. [R5-F]

**Agreed (strengthened).** The working copies — the ledger's event list and each case's log — are complete, ordered projections of the record: each must hold exactly its committed entries, in order. An omitted or reordered entry is detected, not only an edited one. The record itself is unchanged by any of this; the guarantee is that nothing downstream of it can silently differ from it. [R5-G]

---

## 17. Invariants (changes)

I7 is now *child milestone before parent submit* with the §9.1 definition. I16 now checks membership and order of each copy against the chain. I18 (new): once a human has ruled on a case, no audit of it is open or assigned afterwards. Rules R70–R75 record the seven resolutions above.

---

## 21. Provenance

**[R5] Fifth external review (October 15, 2026), of v0.6 and its implementation.** Confirmed the v0.6 repairs across both entry points; found the boundary defects resolved above, two of which it correctly left to a rule choice (a follow-on audit after a ruling; a terminal child's milestone) and did not decide. Its advice stands: finish the transition boundaries, commit the parameters evaluators actually see, state copy completeness honestly — and treat a passing suite as conformance, not as evidence about incentives.

---

## 22. Reference implementation

`agentic_sim/` as in v0.6 with the repairs above. Suites: 23 + 19 (+1 expected failure) + 15 + 14 + 10 + 14 (the fifth review's checks and controls, verbatim) + 9 (v0.7 explicit form) — `python3 run_tests.py`: 104 pass, 1 expected failure; raw pytest and the no-site-packages runner agree. The runner now expands multi-argument parametrization as pytest does.

**Bracketed, unchanged:** strategies, learned selection, evaluator behavior, an external commitment of the history head, physical time, the real-value exchange behind $\mathrm{Res}_t$.

---

## Closing statement

> A ruling ends the audit question. A child that fails to deliver is a milestone, not a block. The stage of a submission belongs to the submission. A refused filing is a refused filing. Acceptance ends a rejection's bond. The grounds of an appeal are in the record, and the record's copies are the record. The loop's rules have now been read by five reviewers and run by three; what the economy does under them is for strategies to show.

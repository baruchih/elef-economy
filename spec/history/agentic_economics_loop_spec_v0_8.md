# Agentic Economics — The Task, Verification, and Dispute Loop

## Working specification v0.8

**Project:** Agentic-OS / Agentic Economics  
**Prepared:** October 15, 2026  
**Supersedes:** v0.7 (October 15, 2026). Where this document is silent, v0.7 and its predecessors stand.  
**Nature of this revision:** A fourth conformance pass. The sixth external review [R6] ran the v0.7 implementation against seven follow-through checks with six passing controls, all under full default parameters, and separately observed one consequence of the rotation rule as written. Three findings needed a rule, each decided in discussion; the rest were defects. This revision takes the rules, repairs the defects, and adopts a rotation refinement. No economic mechanism is added.  
**Status:** As in v0.7. The review's disposition is adopted: v0.8 repairs the previous review's reproduced cases; that is a narrower claim than general conformance for every admitted driver action, and it is the claim made.

> **The wallet supports the purpose; it does not define the purpose.**
>
> **The actor competes on its promise, is assessed on its delivery, and bears the cost of its execution.**
>
> **The past is append-only. The present is committed. The future is mutable.**
>
> **Money enters with requests. Truth enters with requesters. Verification is the security work of the economy.**
>
> **The human is the battery — and holds the plug.**

### What changed from v0.7

| Finding [R6] | v0.8 resolution |
|---|---|
| A. A requester dispute after a human ruling was admitted, targeted the overruled verdict, and could not settle | **Rule:** no dispute after a human ruling, for the same reason as no audit; refused before any fee or state change (§8.2) |
| B. A human override of a delegate's request was graded by the requester's role on some paths and the author's on others; I13 and the action disagreed | **Rule:** the grade is that of the event that established the outcome, by that event's *author*; `_grade()` and I13 share the definition on every route (§15.3) |
| C1. Any actor's spending on a case became the contractor's reimbursable cost | **Rule:** execution cost on a case is incurred by its committed actor; others' spending is refused before purchase (§4.6) |
| C2. Spending on a vested case was admitted and then rejected by I10 | Same rule: cost is incurred only while the case is executing; refused otherwise (§4.6) |
| D. Non-text appeal grounds failed serialization after the fee was taken | Grounds are validated — text or absent — before any fee or state change (§8.1, §8.2) |
| E. A post-settlement correction of a ⊥ did not reach the ⊥'s author | The post-settlement branch applies the two-question contradiction rule; a rejected objection contradicts the ⊥ (§15.2) |
| F. Rotation could release and re-conscript the same actor within one tick | Batch-start snapshot: only actors off duty when the tick began may be conscripted in it (§13) |
| Stale interface comment on ⊥ appeals | Replaced by the actual contract (§22) |

---

## 4.6 Execution cost is the committed actor's, while executing

**Agreed (new rule, from the existing definition).** $C_{iq}$ is the cost actor $i$ incurs on case $q$. A purchase attributed to $q$ is admitted only if the purchaser is $q$'s committed actor and $q$ is executing — committed, submitted, awaiting a response, or resubmitting. Any other attributed purchase is refused before it happens; unattributed purchases remain any actor's own business. Consequently a third party's spending can never enter a kill fee, and a settled case takes no further cost. [R6-C]

---

## 8.1 / 8.2 Grounds are validated first; no dispute after a ruling

**Agreed (clarified).** The grounds of an appeal or dispute are text, or absent, and are checked — together with the round, the window, the appealability of the verdict, and the challenger's ability to fund the fee — before any fee is collected or state recorded. [R6-D]

**Agreed (new rule).** A requester may not dispute a case a human has ruled on. The ruling settled the pre-vesting assessment; a requester who disagrees with the ruling disagrees with the human, and that belongs to human review of rulings (§15.2 direction), not to a model challenge. Refused atomically. This parallels v0.7's rule for audits. [R6-A]

---

## 13. Rotation: a batch-start snapshot

**Agreed (refined).** The actors eligible to enter duty during a tick's handovers are those who were off duty, uncommitted, free of open reviews, and able to fund a bond *when the tick's rotation began*. An actor released in that tick is therefore not re-conscripted in it, and has at least one tick of ordinary eligibility — which is what rotation is for. Replacement-before-release, the turn length, lowest-$\kappa$ selection, and volunteers are unchanged. [R6-F]

---

## 15.2 / 15.3 The grade is the establishing author's; ⊥ corrections are two-question

**Agreed (clarified).** The grade of a settled outcome is that of the event that established it, determined by **who authored that event**: a human's ruling, acceptance, or dispute establishes a human-explicit outcome even on a delegate's request; a delegate's acceptance or dispute establishes a delegate-explicit one. The same definition is used at settlement, in the post-settlement correction, and in the invariant that checks provenance. Whether a human is *authorized* to rule on a delegate's request is a separate question the harness does not model; here every human is. [R6-B]

**Agreed (clarified).** A post-settlement correction applies the same contradiction rule as a ruling before vesting: a $\bot$ is contradicted by a rejected objection, and its author then takes the reliability consequence; an upheld objection leaves the $\bot$ standing. A correction of a settled $\bot$ case therefore states the disposition, and an upheld disposition entails $\mathsf N$, exactly as before vesting. Money does not move. [R6-E]

---

## 17. Rules and invariants (changes)

R76 no dispute after a ruling; R77 grade by establishing author; R78 execution cost by the committed actor while executing; R79 grounds validated before the fee; R80 two-question corrections after settlement; R81 rotation snapshot. I13 now reads the establishing judgment's author.

---

## 21. Provenance

**[R6] Sixth external review (October 15, 2026), of v0.7 and its implementation.** Verified the v0.7 repairs under all three entry points and full defaults; found the follow-through defects resolved above, correctly leaving three to a rule choice (a dispute after a ruling; whose role grades an override of a delegate's request; cost attribution) and declining to choose them; and separately observed the rotation consequence as a policy question. The three rules and the rotation refinement were decided in discussion.

---

## 22. Reference implementation

`agentic_sim/` as in v0.7 with the changes above. Suites: 23 + 19 (+1 expected failure) + 15 + 14 + 10 + 14 + 9 + 15 (the sixth review's checks and controls, verbatim) + 6 (v0.8 explicit form) — `python3 run_tests.py`: 123 pass, 1 expected failure; raw pytest and the no-site-packages runner agree.

**Bracketed, unchanged:** strategies, learned selection, evaluator behavior, authorization of humans over delegates' requests, an external commitment of the history head, physical time, the real-value exchange behind $\mathrm{Res}_t$.

---

## Closing statement

> A ruling ends both the audit question and the dispute question. An outcome is graded by who established it. A case's cost is its actor's, and only while it works. The grounds of a challenge are checked before its fee. A corrected ⊥ reaches its author. A released reviewer gets a tick to be an actor. Six reviewers have read the rules and four have run them; the next thing to run is the economy.

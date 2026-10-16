# Agentic Economics — The Task, Verification, and Dispute Loop

## Working specification v0.6

**Project:** Agentic-OS / Agentic Economics  
**Prepared:** October 15, 2026  
**Supersedes:** v0.5 (October 15, 2026). Where this document is silent, v0.5 and its predecessors stand.  
**Nature of this revision:** A second conformance pass. The fourth external review [R4] ran the v0.5 reference implementation against thirteen interaction tests — paths where two repaired rules meet — and found seven groups of departures from the selected rules. Two of them needed a rule; the rest needed the implementation to do what the rules say on every entry path, not only the one that was tested. This revision takes the two rules, unifies the paths, and strengthens the invariants once more. No economic mechanism is added.  
**Status:** As in v0.5, with the review's framing adopted verbatim: the scripted examples execute, independent executable checks were answered, and strategy runs remain the only evidence about incentives (§18.2).

> **The wallet supports the purpose; it does not define the purpose.**
>
> **The actor competes on its promise, is assessed on its delivery, and bears the cost of its execution.**
>
> **The past is append-only. The present is committed. The future is mutable.**
>
> **Money enters with requests. Truth enters with requesters. Verification is the security work of the economy.**
>
> **The human is the battery — and holds the plug.**

### What changed from v0.5

| Finding [R4] | v0.6 resolution |
|---|---|
| A. Atomicity was action-specific: an unknown-case spend burned credits, a refused fee-pool payment consumed deposit, a refused override left an assessment that later became human provenance | Boundary-wide: every action is validated in full before any balance, state, or assessment is recorded (§2.2 R57, made true everywhere) |
| B1. An override during an open appeal left its unfinished reviewers to time out and be penalized | One override path: unfinished assignments are voided without fault, then the ruling settles the challenge (§15.2) |
| B2. An override of a ⊥ accepted "upheld" with F | The override validates the same constraint as a ruling: upheld entails N (§8.1, §15.2) |
| B3. An override contradicting a requester-actor's rejection stranded the rejection bond | **Rule:** the override is the ruling for the requester-actor's verdict too — a contradicted rejection forfeits its bond; a confirmed one releases it (§15.2) |
| C. A late audit timeout let the case vest before a replacement could be assigned | **Rule:** a vacated audit position is an obligation — the case stays suspended until a replacement completes, the orchestrator waives it, or a requester dispute takes it over (§7.5, §8.3) |
| D1. With no surviving review, deferred cost debts were neither paid nor registered | Cost debts are processed first and for every review, survivors or not; the deposit pays them before anything is returned as unused (§4.3) |
| D2. FIFO claims lost review identity and could mis-attribute payment | A claim carries the review whose cost it is; servicing credits that review (§4.3) |
| E1. Explicit acceptance changed provenance without a commitment | Every participant action is committed to the History (§14) |
| E2. Ledger and case-log copies were not checked against the chain | The History is the authoritative record; copies are checked against their committed entries each tick (§14, I16) |
| F. The reviewer view could not tell an appeal from an audit, so a policy could not know which answer schema was required | The view states the question: fulfillment, appeal, or dispute, with the appealed assessment and the objection (§14) |
| G. A P could be appealed | Guard added: only N and ⊥ are appealable (§6.1) |
| Runner: real pytest parametrization not understood; the expected failure unmarked under raw pytest | Both fixed; both entry points report the same result (§22) |

---

## 2.2 Atomicity, made boundary-wide

**Agreed (unchanged rule, now true everywhere).** An action either completes under its rules or changes nothing — no balance, no state, and no admissible assessment. Validation precedes recording on every public action: the case must exist before a purchase, the fee pool must cover a payment before any of it moves, a ruling must be internally consistent before it is recorded, and a verdict must be appealable before a fee is collected. A refused attempt may be logged as a refusal; it is never stored as if it had been admitted. [R4-A, R4-G]

---

## 4.3 Cost debts come first, for every review

**Agreed (clarified).** At a case's settlement, step 1 of the single payout rule processes **unconditional cost debts** — every review's deferred reimbursement, whether the review survived, was overturned, or was withdrawn with a reimbursable balance — from the case pool first, with the remainder registered as claims on Ω. Step 2 pays **conditional fee entitlements** to surviving reviews. With no surviving review, what the deposit did not need after step 1 is returned to the requester as unused. The two steps are independent: a case with no survivor still pays or registers every debt. [R4-D1]

**Agreed (clarified).** A claim on Ω identifies the reviewer, the amount, and **the review whose cost it is**. Ω services claims first in, first out on every inflow, partially if it must, and each payment is credited to the obligation being paid. [R4-D2]

---

## 6.1 Responses (guard)

An appeal is available after $\mathsf N$ or $\bot$. After $\mathsf P$ the actor revises or accepts; there is nothing to appeal, so the attempt is refused before any fee moves. [R4-G]

---

## 7.5 A vacated audit is an obligation

**Agreed (new rule).** When an audit times out, its position is vacated but the case's obligation stands: the case remains suspended until one of three things happens — a replacement audit is assigned (admissible after the window, since the original was timely) and completes; the orchestrator **waives** the vacated audit, lifting the suspension on its own authority; or the requester disputes inside the window, in which case the dispute takes over the obligation and the suspension passes to the challenge. Abandoning the audit by vesting would have changed the replacement rule silently; it is now an explicit orchestrator act. [R4-C]

An open assignment that a human ruling moots is **voided**, not withdrawn: the bond returns whole, no fault is recorded, and the obligation ends with the ruling.

---

## 14. Verifiable history and the reviewer view

**Agreed (completed).** The History is the single authoritative record. Every participant action is committed to it when admitted — postings, awards, submissions, verdicts, responses, appeals, disputes, audits, rulings, cancellations, withdrawals, explicit acceptances, overrides, volunteering — along with ledger events and rotations. The ledger's event list and each case's log are working copies: each entry carries its commitment position, and the per-tick check verifies the chain *and* each copy against its committed entry. The chain is tamper-evident within the process; the external commitment of its head remains bracketed. [R4-E]

**Agreed (completed).** The reviewer view distinguishes the *question* without revealing hidden labels: an initial review and an audit are indistinguishable and ask for fulfillment; an appeal or a dispute says so, carries the assessment under appeal and the challenger's explanation, and so tells the reviewer what it is being asked to decide — including, for a $\bot$, that the objection's disposition is required. [R4-F]

---

## 15.2 One override path

**Agreed (unified).** Whatever the case's state, a human override before vesting does the same four things in order: it is **validated** whole — the human, the outcome, that there is a result to rule on, and for a $\bot$ the disposition and its entailment (upheld ⇒ N); every **unfinished** assignment is voided without fault; every **completed** verdict that contradicts the ruling is overturned with the standard consequences — a reviewer's, or a requester-actor's rejection, whose bond is forfeited and burned; and the case is **settled**: an open challenge by the ruling, otherwise directly. Contradiction is defined once: $\mathsf F$ contradicts $\mathsf N$; $\mathsf N$ and $\mathsf P$ contradict $\mathsf F$; a $\bot$ is contradicted only by a rejected objection. A confirmed rejection releases its bond. After vesting the override is a record, as in v0.5. [R4-B]

---

## 17. Invariants (additions)

I16 now verifies both the chain and every working copy against it. I17 (new) checks that deferred and pending reimbursements are non-negative and never exceed a review's capped cost, that every Ω claim names a review whose pending balance covers it and that the two agree in sum, and that no settled, cancelled or withdrawn nested case still carries a rejection bond. Rule R66: a vacated audit holds the case; R67: a contradicted requester-actor rejection forfeits its bond under a ruling; R68: validation precedes recording on every action; R69: the History is the authoritative record and copies are checked against it.

---

## 21. Provenance

**[R4] Fourth external review (October 15, 2026), of v0.5 and its implementation.** Verified the v0.5 repairs; found the interaction defects resolved above and showed why the v0.5 invariants accepted them. Its priorities — unify the outcome paths and complete atomicity; repair post-window audit replacement and make debt processing independent of fee recipients; align the record and complete the appeal view — are the order this revision followed.

---

## 22. Reference implementation

`agentic_sim/` as in v0.5, with the repairs above. Suites: the §16 example and variants (23); the third review's regressions verbatim (19 pass, case 12 the expected failure, now marked for both entry points); the v0.5 rules in explicit form (15); the fourth review's interaction tests verbatim (13 functions, 14 runs, all pass); the v0.6 repairs in explicit form (10). `python3 run_tests.py`: 81 pass, 1 expected failure; raw pytest reports the same.

**Bracketed, unchanged:** strategies, learned selection, evaluator behavior, an external commitment of the history head, physical time, the real-value exchange behind $\mathrm{Res}_t$.

---

## Closing statement

> Every action is checked before it is written. Every ruling takes one path. A vacated audit holds its case. Every debt is paid or registered, and every claim knows whose it is. The record is one record, and its copies are checked against it. The reviewer is told what question it is answering. The rest is as before, and what the economy does is still for strategies and runs to show.

# Agentic Economics — The Task, Verification, and Dispute Loop

## Working specification v0.10

**Project:** Agentic-OS / Agentic Economics  
**Prepared:** October 15, 2026  
**Supersedes:** v0.9 (October 15, 2026). Where this document is silent, v0.9 and its predecessors stand — except §8.3 of v0.9, which is withdrawn here.  
**Nature of this revision:** A reversal. The eighth external review [R8] ran the v0.9 implementation against twenty-five checks and found sixteen failures in five groups — every one a consequence of the audit-reopening rule v0.9 introduced. That rule was a design change made in a conformance pass, and this revision withdraws it rather than repairing its consequences. The interface problem it was meant to solve is solved another way. No economic mechanism is added, and the state machine returns to its v0.8 shape with one honest addition to the reviewer view.  
**Status:** A rulebook to be re-read for sanity before any further rule is added. The eighth review's findings are closed by withdrawal, not repair; its controls pass; its reopening-dependent checks are retained in the suite as expected failures with the reason stated.

> **The wallet supports the purpose; it does not define the purpose.**
>
> **The actor competes on its promise, is assessed on its delivery, and bears the cost of its execution.**
>
> **The past is append-only. The present is committed. The future is mutable.**
>
> **Money enters with requests. Truth enters with requesters. Verification is the security work of the economy.**
>
> **The human is the battery — and holds the plug.**

### What changed from v0.9

| Finding [R8] | v0.10 resolution |
|---|---|
| A. An auditor's P/⊥ rewrote the case's verdict timestamp, invalidating the audit's own authorization and a parent's legal submission | Withdrawn with the rule: an audit never rewrites the verdict |
| B. A resumed auditor could time out and its position could not be refilled; a waiver drove the obligation count negative | Withdrawn with the rule: no audit is ever resumed |
| C. Appeals of an auditor's ⊥ counted four positions, charged the parent's released bond on a nested case, and omitted the parent's reliability consequence | Withdrawn with the rule: an auditor's verdict is F or N and is challenged as v0.8 challenged it |
| D. Reopening met an actor's later commitment or open review and created a second execution or an I14 violation | Withdrawn with the rule: an approved, capacity-released task never returns to the actor |
| E. A reopening audit already merged into a paid dispute changed the dispute's question | Withdrawn with the rule: a merged audit answers F or N |
| The seventh review's underlying problem — identical views, different admissible answers; a refusal reveals the role | The view states the admissible answers (`responses_available`); identical views admit identical answers, and no refusal reveals anything the view did not already say (§8.3) |

---

## 8.3 Audits are answered F or N; the view says what may be answered

**Withdrawn.** v0.9's rule that an auditor may answer $\mathsf P$ or $\bot$, suspending the approval and reopening the actor's response, is withdrawn. The reason is not the sixteen defects; it is what they revealed. An audit is a blind re-review of a *finished* verdict. By the time an auditor sees a case, the actor's response window has closed, its capacity has been released and may be committed elsewhere, a parent may have submitted on the strength of the approval, and a requester may have disputed it. "Send the actor back" from that state changes what *approved* meant to every party that acted on it. That is a change to the economy's commitments, not an extension of a reviewer's vocabulary, and it does not belong in a conformance pass — or, I think, in the rulebook at all. [R8]

**Agreed (replaces v0.9 §8.3).** $\mathsf P$ and $\bot$ are *responses to a submission*: they send the actor back to act, and they are available only where the actor can still act — on the **first review of a submission that has not been revised or evidenced**. Every other review is answered $\mathsf F$ or $\mathsf N$: an audit, an appeal or dispute review, and a review resumed after a resubmission, whoever holds the position.

**Agreed (new).** The reviewer view states which answers the review may give: `responses_available` is true exactly in the case above. The view still does not say whether a fulfillment question is an initial review or an audit — blindness stands — but it says what may be answered, so **identical views admit identical answers**, and a refusal of $\mathsf P$ or $\bot$ tells the reviewer nothing the view had not already told it. This is the problem the seventh review raised, solved at the interface rather than by changing the economy. The seventh review's "identical views" test is superseded by this, not refuted: an initial review's view and an audit's view now differ by their stated contract. [R7, R8]

The audit rules of v0.8 §8.3 — blind, assigned by the orchestrator, agreement is a second settled review, disagreement is one appeal review plus one more, merged into a dispute as one of its two reviews, vacated on timeout and refilled or waived — stand as they were.

---

## 17. Rules and invariants (changes)

R82′ identical fulfillment views admit identical answers, *because the view states them*; R83 (a reopening audit suspends) is withdrawn; R87 $\mathsf P$ and $\bot$ are available only on the first review of an unrevised submission. I8 counts positions plainly again; the suspension exceptions are gone.

---

## 21. Provenance

**[R8] Eighth external review (October 15, 2026), of v0.9 and its implementation.** Verified the v0.9 repairs; found that every one of its sixteen failures was a consequence of the reopening rule; was explicit that two of its findings were policy questions — a busy actor, a merged dispute — and declined to answer them; and recommended proceeding with scoped strategy runs while treating reopening as not reconciled. This revision takes the stronger course its findings implied: the rule is withdrawn, and its policy questions no longer arise. Its reviewer notes, shared separately, framed the point this document adopts: the new transition had to preserve the commitments, history and adjudication that already existed, and it could not.

**[R7], revisited.** The problem it raised was real and is solved in §8.3 by the view; the solution v0.9 chose was wrong.

---

## 22. Reference implementation

`agentic_sim/` as in v0.9 with reopening removed. Suites: `python3 run_tests.py` — 152 pass, 24 expected failures, each with a stated reason: one original (the single-answer ⊥ appeal), four superseded (the seventh review's identical-views test, in its four parameters), nineteen on the withdrawn path (the eighth review's reopening-dependent runs; its six controls pass). The withdrawal is asserted directly in `tests/test_v10.py`: an auditor's $\mathsf P$ or $\bot$ is refused whole, the verdict timestamp never moves, and each of the five paths the eighth review found cannot begin.

**A note on process, recorded so it is not repeated.** Across v0.5–v0.9 each revision was a conformance pass: fix the rules' agreement with each other, add no mechanism. v0.9 broke that discipline without saying so — it answered an interface finding with a state-machine expansion — and the next review found the cost at once. The standing rule for future revisions: a conformance pass may change *how* a rule is applied; a change to *what the rules permit* is a design revision, is labeled as one, and gets a reading on its own before it is implemented.

**Bracketed, unchanged:** strategies, learned selection, evaluator behavior, authorization among humans, an external commitment of the history head, physical time, the real-value exchange behind $\mathrm{Res}_t$.

---

## Closing statement

> An audit judges a finished verdict and says yes or no. The reviewer is told what it may answer, and nothing else about what it is. A task that was approved stays approved until a challenge, a ruling, or a vesting says otherwise. What v0.9 added is gone, with its reasons recorded; what the previous eight revisions settled stands. The rulebook is at rest. Read it for sanity before adding to it, and then let the economy run.

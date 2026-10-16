**v0.9 fixes the v0.8 review’s reproduced cases.** I tested the new ZIP, and all three supplied test entry points agree: **148 passed, one expected failure**. The previous independent regression file is included byte-for-byte unchanged and passes, matching the release note. agentic_economics_loop_spec_v0_9

The main remaining issue is **the newly introduced audit-reopening path**. Allowing an auditor to return “partially fulfilled” or “cannot assess” does more than extend its answer vocabulary: it lets an already approved task return to the actor. That now interacts with historical timestamps, later assignments, reviewer replacement, and existing disputes.

I added **25 targeted checks: 16 failed and nine passed**, grouped into five findings. Several failures are variations of the same underlying problem—not 16 independent defects or an estimated failure rate.

**agentic_economics_v09_review_bundle.zip[Download the v0.9 review bundle](sandbox:/mnt/data/agentic_economics_v09_review_bundle.zip)** · **agentic_economics_v09_review\.md[Read the detailed review](sandbox:/mnt/data/agentic_economics_v09_review.md)**

The bundle contains the additional tests, reproduction script, actual outputs, code locations, and checksums. All **21 supplied files remain unchanged**.

## What I ran

| Run | Observed result |
|---|---:|
| `python -S run_tests.py` | **148 passed, 1 expected failure** |
| `python run_tests.py` | **148 passed, 1 expected failure** |
| `python -m pytest tests -q -rxX` | **148 passed, 1 xfailed** |
| Additional targeted checks | **16 failed, 9 passed** |
| Supplied and additional tests together | **157 passed, 16 failed, 1 xfailed** |

I invoked the historical expected failure directly. It still fails because its missing-evidence appeal omits the required objection disposition—not because of a new unrelated error.

The independent checks use **default `Params()` values**. They inject protocol actions rather than learned strategies, and do not change case state or wallet balances directly.

## What is working now

The previous cases involving complete two-question corrections, corrections before reviewer payout, and delegate access to human ruling authority now pass.

The initial-review and audit interfaces also accept the same four answers in the supplied fixtures. Several new audit-reopening examples successfully settle when the actor is idle and the relevant actions happen within the same tick. These correspond to the four resolutions recorded in v0.9. agentic_economics_loop_spec_v0_9

**I would keep those decisions.** The findings below concern making the new paths agree with the rules that already surround them.

---

## 1. A later audit answer can make an earlier, valid action appear invalid

This is the most immediate problem because it occurs with ordinary elapsed time—not a complicated economic scenario.

### An audit taking time fails the commit-before-audit check

I ran:

| Tick | Event |
|---:|---|
| 0 | C approves A’s result |
| 1 | D is assigned to audit that approval |
| 2 | D returns **partially fulfilled** or **cannot assess** |

Both answers are now permitted. The completion is accepted, but the engine changes the case’s `t_verdict` from **0 to 2**. The invariant then compares the audit’s assignment time with that new timestamp and raises:

```text
I6 q1: audit assigned at 1 before the verdict at 2
```

**The audit was not assigned too early.** It was assigned after the initial approval. Its own later answer should not invalidate that historical fact.

The same elapsed-time sequence passes when the auditor returns F or N.

The error also occurs when the audit initially returns `⊥`, the actor takes one tick to supply evidence, and the resumed auditor returns F or N. The resume path updates the same timestamp.

### A child’s later audit can invalidate its parent’s legal submission

There is a related effect in delegation:

> A accepts B’s child result at tick 0.  
> A submits the parent at tick 0, after the required child milestone.  
> At tick 1, an audit of the child returns `⊥`.

The child’s verdict timestamp becomes 1. The invariant then reports that the parent submitted before the child reached its milestone—even though the parent’s submission was valid when it happened.

The standing rule explicitly permits the parent to proceed once the child reaches its initial verdict or an allowed terminal milestone. A subsequent assessment should not erase that event. agentic_economics_loop_spec_v0_7

**The fix is to distinguish the historical milestone from the current assessment.** The hash-chained history remains intact; the mutable timestamp used by the checks no longer refers to the event they intend to check.

The supplied new reopening tests perform the relevant events at one tick, which explains why they do not reveal this collision.

## 2. Reopening does not resolve what happens when the actor has already taken other work

This is the most important **remaining policy decision**, rather than something I would silently settle in a patch.

Our standing rules allow an actor to take another assignment after its task becomes pending. They also require one active assignment at a time. The new audit rule can subsequently require that actor to return to the earlier task. agentic_economics_loop_spec_v0_4 agentic_economics_loop_spec_v0_5 agentic_economics_loop_spec_v0_9

### An actor can execute two ordinary cases

I ran:

> C approves A’s first task, releasing A’s capacity.  
> A receives a second task.  
> An audit reopens the first task with `⊥`.  
> A supplies evidence and resubmits the first task.

The engine allows A to spend resources on both:

| Case | State |
|---|---|
| First task | **SUBMITTED**, following resubmission |
| Second task | **COMMITTED** |

A’s single `committed` field still points only to the second task. **All eighteen existing invariants pass**, despite both cases being in execution states for A.

The reopening code reacquires the old commitment only when that field is empty. Otherwise, it opens the response and execution states without accounting for the additional commitment.

### Reopening during an unrelated review fails I14

I also exercised this through normal reserve rotation:

| Tick | Event |
|---:|---|
| 29 | A’s result is approved; its challenge window ends at 39 |
| 30 | Normal rotation puts A on verification duty |
| 31 | A begins reviewing another actor’s task |
| 31 | An audit of A’s earlier result returns `⊥` |

The engine sets A’s ordinary commitment back to the old task while A retains the unrelated open review:

```text
I14 A is committed and holds an open review
```

**The question to decide is what should happen when reopened work meets an existing assignment:** wait, preempt, or some other explicitly bounded treatment. The response clock and reserve membership also need to follow that decision.

I am not recommending that the auditor’s valid answer simply be refused because the actor is busy. That would introduce another inconsistency with the reviewer contract.

## 3. A resumed auditor can time out, but its position cannot be refilled

The selected rule permits replacement after a reviewer times out. A vacant audit remains an obligation until it is replaced, waived, or taken over by an admitted dispute. agentic_economics_loop_spec_v0_5 agentic_economics_loop_spec_v0_6

That still works for an ordinary audit. It fails after reopening.

### Reproduction

> D’s audit returns P or `⊥`.  
> The actor revises or supplies evidence and resubmits.  
> D times out while reviewing that resubmission.

An eligible, funded replacement E is available, but both assignment routes reject it:

```text
assign_audit: only an F verdict in PENDING may be audited
assign_initial: initial review already assigned
```

The case is now **SUBMITTED**, which the audit assignment guard refuses. The earlier initial approval still exists, which the initial-review assignment guard refuses.

**This is not a reviewer shortage. The appropriate replacement position is unreachable through the public API.**

Calling `waive_audit()` instead is accepted, but decrements `open_items` from zero to **−1**, leaving the case SUBMITTED. All eighteen invariants accept that state.

The resumed-assessment position needs to survive its reviewer’s withdrawal. Waiver must also close the obligation that actually exists, rather than decrement a count left over from a different stage.

## 4. Reopening appeals still confuse the current assessor with the original one

The new rule is explicit: when an appeal rejects an auditor’s missing-evidence claim, **the auditor** is overturned and its bond reimburses the actor. The suspended approval is treated separately. agentic_economics_loop_spec_v0_9

Three paths need correction.

### A. A nested audit appeal tries to charge the parent’s already released bond

I ran:

> A hires B and accepts B’s result.  
> C audits the child and returns `⊥`.  
> B pays two credits to appeal.  
> D and E both reject C’s claim that evidence was missing.

The second appeal completion raises:

```text
LedgerError: A lock rej:q2 holds 0.0, cannot take 2.0
```

The engine tries to charge **A’s rejection bond**, even though A accepted the child and released that bond earlier. **C is the reviewer whose claim is being challenged.**

After the error:

| Item | State |
|---|---|
| Challenge | Marked **resolved** |
| Outstanding-item count | Still **1** |
| B’s court-fee reimbursement | Not paid |
| C’s reviewer bond | Still locked |
| A’s reliability | Incorrectly receives an adverse record |
| Existing invariants | **All pass** |

This happens whether the appeal reviewers conclude **rejected objection, F** or **rejected objection, N**.

The corresponding root appeals pass. An ordinary appeal against an actual parent rejection also passes. The broken combination is specifically **a nested auditor acting as the current assessor**.

### B. Upholding the auditor’s claim violates the three-position bound

For a root case:

> C approves.  
> D audits and returns `⊥`.  
> A appeals.  
> E and F both uphold the missing-evidence claim and return N.

The case becomes FINAL_N, and C’s premature approval is overturned. The position count then becomes four:

```text
I8 q1 holds 4 review positions > V_max
```

Finalization clears the suspension flag, causing the now-overturned historical approval to be counted again.

**This does not demonstrate that the reserve must grow.** It shows that ending the suspension restores a historical participant to a count intended to describe the current adjudication path.

### C. The equivalent nested premature-approval consequence is omitted

If A accepted B’s child result, an auditor reopens it, and B accepts nonfulfillment, B loses its guarantee. But A receives no reliability consequence for its premature approval.

The root-case equivalent does penalize the initial approving reviewer. The nested finalization path only searches for a paid review object with role `initial`; the parent’s judgment is not represented that way.

This concerns **the parent’s reliability**, not a proposal to reinstate a second financial bond for nested acceptance. If requester-actors are intended to be exempt here, that exception needs to be explicit.

## 5. A reopening audit can change an already-running requester dispute’s question

The inherited rule merges an in-progress audit into a requester dispute as one of its two reviews. The new rule also allows that auditor to return P or `⊥`. These two workflows have not yet been reconciled. agentic_economics_loop_spec_v0_4 agentic_economics_loop_spec_v0_9

I ran:

> C approves.  
> D starts an audit.  
> H disputes the approval and pays the fee.  
> E receives the other dispute-review assignment.  
> D returns P or `⊥`.

The reopening handler does not account for D already being part of the dispute. It changes the live case verdict and decrements the outstanding-item count, even though the paid dispute remains.

The concrete results are:

| Auditor’s answer | Follow-on behavior |
|---|---|
| **P** | E returns N. The orchestrator resolves the split as N. Settlement decrements the count again, leaving **`open_items = −1`**. All invariants pass. |
| **`⊥`** | E’s view still says **`question="dispute"`**, but its documented F/N-only answer is rejected unless E supplies the objection disposition required for a missing-evidence appeal. |

The control cases work when the merged auditor gives a definitive F or N.

**This needs an explicit workflow decision:** when an audit already belongs to a paid dispute, how does its request for revision or evidence interact with that dispute, the remaining reviewer, and the actor’s right to appeal?

Currently, the code changes the question while preserving the old challenge structure. That is not something a reviewer policy can reliably infer from the documented contract.

---

## What this means for v0.9

The previous repairs are real. **The additional failures are concentrated in the consequences of reopening an approval**, not a reversal of the demonstrated v0.8 fixes.

The recurring distinction is now:

| Fact that must remain identifiable | Different fact introduced by reopening |
|---|---|
| The approval that authorized an audit | The auditor’s later assessment |
| The child milestone the parent relied on | The child’s current assessment state |
| The actor’s released capacity | A later request to resume work |
| The parent or initial reviewer | The assessor whose claim is now challenged |
| An existing requester dispute | A new request for evidence or revision |

Most of this is applying existing rules consistently. **The busy-actor and merged-dispute cases need a policy choice as well**, and I would not substitute my preference for yours.

The reproduction commands are included in the bundle:

```bash
python -m pytest independent_tests/test_v09_audit_reopening.py -q --tb=short
python -S independent_tests/reproduce_findings.py
```

## My recommendation

**Proceed with the explicitly scoped strategy-run approach you adopted in §22, while treating audit reopening as not yet fully reconciled.** Root tasks with F/N-only reviewers, actual human rulers, and no post-settlement corrections avoid the reported reopening paths. Such a run remains an experiment within that declared boundary—not certification of every possible operation sequence. agentic_economics_loop_spec_v0_9

For the full four-answer interface, these fixes matter: a task executing twice, a stranded replacement, or the wrong reviewer bearing liability would distort cost and reliability results.

**We do not need another economic mechanism here. We need the new “return to the actor” transition to preserve the commitments, history, and adjudication process that already exist—and we can study a narrower economy without waiting for every richer path to be finished.**
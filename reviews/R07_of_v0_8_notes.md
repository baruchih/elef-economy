**v0.8 delivers on its narrower claim: the previously reproduced v0.7 cases are repaired.** I tested the new ZIP, and all three supplied test entry points agree: **123 passed, one expected failure**. The previous independent regression file is included byte-for-byte unchanged and passes. That supports the more careful status statement in this revision. agentic_economics_loop_spec_v0_8

I found **seven additional failed checks, alongside ten passing controls**, concentrated in four areas: two correction-logic defects, a reviewer-interface inconsistency, and a human-versus-delegate authority boundary.

**agentic_economics_v08_review_bundle.zip[Download the v0.8 review bundle](sandbox:/mnt/data/agentic_economics_v08_review_bundle.zip)** · **agentic_economics_v08_review\.md[Read the detailed review](sandbox:/mnt/data/agentic_economics_v08_review.md)**

The bundle contains the tests, reproduction script, actual outputs, code locations, and checksums. All **19 supplied files remain unchanged**.

## What I ran

| Run | Observed result |
|---|---:|
| `python -S run_tests.py` | **123 passed, 1 expected failure** |
| `python run_tests.py` | **123 passed, 1 expected failure** |
| `python -m pytest tests -q` | **123 passed, 1 xfailed** |
| Additional targeted checks | **7 failed, 10 passed** |

The supplied results match the release note. I also invoked the historical expected failure directly: it still fails because its missing-evidence appeal omits the required objection disposition—not because of a new unrelated error. agentic_economics_loop_spec_v0_8

The additional checks use **the supplied default parameters**. They are selected counterexamples and neighboring controls, not a random sample or an estimated defect rate.

## What is working now

The earlier fixes hold: a requester cannot open a dispute after a human ruling; an actual human’s override of a delegate-requested task is graded consistently; another actor’s spending cannot become the contractor’s reimbursable cost; non-text grounds are refused before charging; and the revised rotation releases the original duty actors without immediately recruiting them again.

These correspond to the decisions recorded in v0.8. **I would preserve those decisions rather than reopen them.** agentic_economics_loop_spec_v0_8

The remaining findings concern how the rules are applied in less-direct cases.

---

## 1. Correcting the objection without changing “not fulfilled” misses the appeal reviewers

This is the most direct remaining defect in the two-question model.

We explicitly distinguish:

**Was the required evidence missing?**  
**Did the task fulfill the request?**

An appeal reviewer can be overruled on the first question even when its answer to the second remains unchanged. That is already the selected rule, not a new proposal. agentic_economics_loop_spec_v0_5

### Reproduction

> C returns **cannot assess: evidence missing**.  
> A appeals.  
> D and E both answer **objection upheld, task not fulfilled**.  
> Everything settles.  
> H later corrects the decision to **objection rejected, task still not fulfilled**.

The human is saying: the evidence was present, but the result nevertheless failed the request.

### What happens

| Reviewer | Before correction | After correction |
|---|---:|---:|
| C—the original missing-evidence claim | Reliability \(2/3\) | **\(1/2\)**, correctly marked contradicted |
| D—upheld that claim | Reliability \(2/3\) | **Still \(2/3\)** |
| E—upheld that claim | Reliability \(2/3\) | **Still \(2/3\)** |

No money moves, which is correct. All eighteen invariants pass.

The reverse direction also fails: reviewers say **objection rejected, N**, and the human later says **objection upheld, N**. Their objection answers are contradicted, but their reliability remains unchanged.

**The cause:** the post-settlement code compares the reviewer’s fulfillment verdict, but does not pass the appeal reviewer’s objection answer into that comparison. The normal challenge-settlement branch does compare both.

The v0.8 correction reaches the original `⊥` author, but **does not yet apply the complete two-question rule to the appeal reviewers**. agentic_economics_loop_spec_v0_8

The neighboring control works when the correction changes **both** the objection and fulfillment verdict. That explains why the supplied test passes.

## 2. A correction can disappear between case finalization and reviewer payout

There is a short but valid interval in which:

> The actor’s case is already final, but the completed reviews have not yet reached the tick’s payout batch.

The selected tick ordering permits participant actions during that interval, and final-N reviews settle in the batch. agentic_economics_loop_spec_v0_4 agentic_economics_loop_spec_v0_4

### Reproduction

> C rejects the result.  
> A accepts the rejection.  
> Before the review payout batch runs, H overrides the outcome to **fulfilled**.  
> The tick advances.

The override is accepted. But C’s review is skipped by the correction logic because its status is `done`, not yet `vested`.

The payout batch then treats C as a surviving reviewer: it releases the bond, pays the fee, and records a positive reliability outcome.

### Changing only the timing changes the learning signal

| When the same correction arrives | C’s status then | Final reliability |
|---|---|---:|
| Before reviewer payout | `done` | **\(2/3\)**—only a positive outcome |
| After reviewer payout | `vested` | **\(1/2\)**—the correction is recorded |

Both paths pass all invariants.

In the zero-review-cost, tick-zero fixture, C receives **20 credits** in either path: ten from the remaining deposit and ten from that tick’s emission. This is the computed payout for that fixture, not a newly proposed fixed fee.

**My test does not prescribe a new clawback or fee rule.** It requires the accepted correction to reach the relevant completed reviewer. The precise financial treatment at this boundary can be clarified separately.

The underlying mistake is treating **case finality** and **review-payment completion** as though they happen together. The override rule is meant to reconcile completed assessments, not lose a correction because one payment is still queued. agentic_economics_loop_spec_v0_6

## 3. The blind-review interface permits four answers, but audits secretly accept only two

This is an interface inconsistency that will matter when you connect an evaluator.

The visibility rule deliberately makes an initial review and a blind audit indistinguishable: both receive a fulfillment question, without revealing whether the assignment is an audit. agentic_economics_loop_spec_v0_6

The new `ActorPolicy.review()` documentation also explicitly says that this question can return:

> **F, N, P, or `⊥`.**

But `complete_review()` rejects P and `⊥` when the hidden role is audit.

### I tested exactly equal reviewer views

The two independent worlds expose identical values—including the case and review identifiers, deadline, bond, cap, submission time, and `resumed=False`.

| Evaluator returns | Initial review | Blind audit |
|---|---|---|
| Fulfilled | Accepted | Accepted |
| Not fulfilled | Accepted | Accepted |
| Partially fulfilled | Accepted | **Refused** |
| Cannot assess | Accepted | **Refused** |

The refusals are atomic. The problem is **the hidden difference in the response contract**.

A policy can restrict itself to F/N and operate successfully. I am **not** saying that no valid reviewer policy exists.

But a policy following the documented four-category interface cannot tell whether its P or `⊥` answer will be accepted. Retrying after the refusal can also reveal that the assignment was an audit.

**The required correction is to make the interface and the audit rule agree.** That does not require choosing a Jev-like evaluator, changing the economic objective, or exposing the entire world to the reviewer.

## 4. A delegated requester can use the human-override power

This finding has an interpretation boundary, so I would make the intended role rule explicit before treating it as merely a code repair.

v0.8 distinguishes human and delegate authors. It brackets **which human may rule over a delegate’s request**, treating every human as authorized in the harness. It does not explicitly say that delegates themselves receive the human’s final-ruling power. agentic_economics_loop_spec_v0_8 agentic_economics_loop_spec_v0_8

### Reproduction

The standard setup identifies:

- **H** as a human requester.
- **S** as a requester explicitly marked in `delegates=['S']`.

Then:

> H commissions a task.  
> C approves A’s result.  
> **S invokes the human-override method**, changing the result to not fulfilled.

The engine accepts it.

| Participant | Wallet before S’s call | Wallet afterward |
|---|---:|---:|
| A | 50 | **45** |
| C | 50 | **45** |
| S | 100 | **100** |

A loses its guarantee. C loses its reviewer bond. S pays no dispute fee and needs no reviewer panel. The final grade is correctly **delegate-explicit**, but the authority check treated S as a human.

All invariants pass.

**Why:** the constructor stores funded requesters—including delegates—in `self.humans`. The override guard checks that set without excluding identities separately marked as delegates.

Under the literal human-only override rule, this is a role-guard defect. **If delegates are intentionally allowed to issue final rulings too, that is a broader authority decision and should be stated.** It should not result incidentally from the constructor argument’s name.

The control where **actual human H overrides a delegate-requested task** passes.

---

## What the passing invariants do—and do not—tell us

These counterexamples conserve recorded credits, maintain their lock records, and preserve internally consistent histories.

They expose different properties:

**The complete assessment must be compared with the correction.** A correct comparison of F versus N is insufficient for a two-question review.

**An admitted correction must survive a payment-state transition.** A financially consistent payout can still generate the wrong reliability signal.

**A policy’s permitted inputs and outputs must fit together.** Balance and history checks do not detect an interface that conceals which answers are legal.

**An author’s label and authority are separate.** Correctly labeling S as a delegate does not establish that S should have been allowed to rule.

That is why all eighteen checks can pass while these problems remain.

## My assessment

**I agree with v0.8’s narrowed claim: it repairs the previous review’s reproduced cases.** I would not turn these additional findings into a reason to redesign the economy or restart the specification.

The work remaining here is focused: apply both parts of an appeal assessment during corrections; preserve corrections across the review payout boundary; reconcile the blind-review response contract; and make the delegate authority rule explicit.

A first **scoped** strategy run does not need to wait for proof of every possible path. For example, root tasks with F/N-only reviewers, actual humans as ruling authors, and no post-settlement corrections avoid the reported failures. Such a run must state those exclusions; it would not test partial fulfillment, missing-evidence appeals, or correction behavior.

For a run using the full advertised interface, these issues matter because **a skipped reliability penalty or forced F/N audit response could look like an economic or learning effect when it is actually an implementation effect**.

The additional suite and standard-library reproduction script are in the bundle:

```bash
python -m pytest independent_tests/test_v08_review_contracts.py -q --tb=short
python -S independent_tests/reproduce_findings.py
```

**The ordinary paths and previous repairs hold. The remaining discrepancies are now primarily in how assessments become authority, corrections, and learning signals—not in the basic task–payment loop.**
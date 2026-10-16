# agentic_sim — reference implementation of the v1.0.1 baseline

Built up through v0.4–v0.10 and unchanged by the v1.0 consolidation and the v1.0.1 errata (the engine already
behaved as the corrected wording says; see spec Appendix E). Section numbers in code comments refer to the
working-spec versions they were written against; `spec/agentic_economics_loop_spec_v1_0_1.md` is the text in force,
and its Appendix A holds the defaults that `sim/params.py` encodes.

The loop's rules as code, with no strategies. Every bid, verdict, appeal, audit
assignment, ruling and human action is injected by the caller. Each action is validated in
full before anything is recorded or moved: it either completes under its rules or changes
nothing. After every tick eighteen invariants are checked; a failing invariant is a bug in
the engine or a contradiction in the spec, never a property of a strategy.

```
sim/params.py       §18.1 provisional defaults, §19 initialization values
sim/ledger.py       wallets with named lock records, case pools, Ω, the backed credit, amount
                    validation, and the hash-chained History that is the authoritative record
sim/engine.py       cases, reviews, challenges (incl. the two-question ⊥ appeal), delegation,
                    settlement, Ω claim servicing, rotation, the reviewer view, the tick order
sim/invariants.py   I1–I18, run after every tick; each says what it establishes
sim/strategies.py   the decision seams a driver would fill (Protocols only)
tests/test_spec.py                  §16 worked example and variants; R1/R2 exceptional paths — 23
tests/test_review_regressions.py    the third review's 20 regressions, verbatim — 19 + 1 expected failure
tests/test_v05.py                   the v0.5 rules in explicit form — 15
tests/test_review2_interactions.py  the fourth review's 13 interaction tests, verbatim — 14 runs
tests/test_v06.py                   the v0.6 repairs in explicit form — 10
tests/test_review3_boundaries.py    the fifth review's 10 boundary checks and 4 controls, verbatim — 14 runs
tests/test_v07.py                   the v0.7 rules and repairs in explicit form — 9
tests/test_review4_followthrough.py the sixth review's 7 checks and 6 controls, verbatim — 13 runs
tests/test_v08.py                   the v0.8 rules and repairs in explicit form — 6
tests/test_review5_contracts.py     the seventh review's 7 checks and 10 controls, verbatim — 17 runs
tests/test_v09.py                   the v0.9 rules and repairs in explicit form; reopening replaced by the view contract — 5
tests/test_review6_reopening.py     the eighth review's 25 checks, verbatim — 6 controls pass; 19 runs are expected
                                    failures because the path they exercise was withdrawn
tests/test_v10.py                   the withdrawal of reopening, asserted directly — 5
tests/test_v101.py                  withdrawing an unawarded request (§16), the one permitted operation no suite had
                                    exercised; root and nested, atomic refusal after award — 4
tests/test_perf_equivalence.py      the per-tick check equals the full audit; the working-set engine reproduces the
                                    v1.0.1 engine's History head on a seeded random scenario; the working set stays
                                    bounded — 5
run_tests.py        every suite with plain python; pytest reports the same (conftest marks the XFAIL)
```

Run: `python3 run_tests.py` — 161 pass, 0 fail, 24 expected failures, each with a stated reason (one original,
four superseded by the view contract, nineteen on the withdrawn reopening path). With pytest:
`python3 -m pytest tests -q` reports 161 passed, 24 xfailed; the runner expands pytest parametrization as pytest
does, including multi-argument and stacked marks. (Spec Appendix D records the count at the v1.0.1 freeze, 156.)

Expected failures are **strict and parameter-exact** in both entry points: `EXPECTED_FAIL_PARAMS` names the
parameter runs that are expected to fail inside a mixed test (the P/⊥ runs of the eighth review's first case;
its F/N controls must pass), and an expected failure that passes is reported as XPASS and fails the run — a
withdrawn or superseded path admitted again is a regression, not a bonus.

## Running long: the working set and the two checks (October 16, 2026)

Through v1.0.1 `advance` ran the full §17 audit after every tick, and three checks (I4, I10, I16)
rescanned the whole record each time, so a run slowed as the square of its length: twenty actors
reached 4 ticks/s by tick 300 and would have needed about 25 minutes for 1,000 ticks. The engine
now keeps a **working set** — cases and reviews that can still change — and checks per tick what
the tick touched:

- `check_all(w)` is unchanged in meaning: every predicate over everything, the chain re-hashed
  from genesis. Tests call it; `Params.full_check_every = n` schedules it every n ticks inside
  `advance` (default 0: only when asked). It is the only check that notices an edit to an entry
  it has already verified.
- `check_tick(w)` is what `advance` runs: the same predicates over the working set, the cases
  touched since the last tick, and the events and record entries added since then. I4 and I10 are
  established as events are recorded; I16 verifies the chain from where it left off and the new
  copies against their committed entries. For a world changed only through the engine's own
  operations it establishes every fact the full audit would.
- The ledger keeps a per-case index of its events, a running mints-minus-burns and a running pool
  total beside the full recomputations; `kappa`'s vest list is pruned at the window it can no
  longer count in.
- I1's tolerance scales with the money supply (one millionth of a credit per ten thousand in
  circulation): M is a running sum while the balances are recomputed, and at a ten-million-credit
  supply the two drift apart by rounding after a few hundred ticks. The fixed tolerance tripped a
  false conservation failure there; a leak of economic size is still caught.

The claim that none of this changes behaviour is `tests/test_perf_equivalence.py`: a seeded random
scenario through appeals, disputes, audits, rulings, overrides before and after settlement,
delegation, cancellation, pool exhaustion, timeouts and rotation, with the full audit after every
tick beside the tick check, reproduces the History head the v1.0.1 engine (commit 6a746a1) produced.

Measured after the change: 20 actors × 1,000 ticks in 1 s at a constant ~1,000 ticks/s (was ~25 min);
200 actors × 10,000 ticks (300,000 cases) in 104 s at a constant ~95 ticks/s, final full audit 35 s.
The remaining limit is memory, not time: the record is kept whole in memory — 4.85 million History
entries and 300,000 cases took 4.3 GB — so runs beyond that scale need the record spilled to disk,
a separate change.

## The expected failure

The third review's case 12 appeals a ⊥ and completes the appeal reviews with a plain `N`,
expecting the original ⊥ to stand. An appeal of ⊥ answers two questions — did the objection
stand, and is the task fulfilled — and v0.5+ requires the first explicitly:
`complete_review(r, N, cost, objection="upheld")`. Inferring the disposition from the verdict
would be the unjustified rule the review warned against, so the verbatim test fails with a
`RuleError` naming the missing disposition. Both entry points report it as XFAIL.

## What v0.10 withdrew (eighth review, R8)

- **Audit reopening is withdrawn.** v0.9 let an auditor answer P or ⊥ and send an approved,
  capacity-released task back to the actor. The eighth review found sixteen consequences in one
  pass — timestamps, capacity, replacement, nested liability, merged disputes — all of one
  decision. It was a design change made in a conformance pass, and it is reverted rather than
  repaired: an audit reviews a finished verdict after the actor's window has closed, and is
  answered F or N.
- **The fulfillment contract is stated by the view.** `ReviewView.responses_available` is True
  exactly when the review may answer P or ⊥: the first review of a submission that has not been
  revised or evidenced. The view still does not say whether a fulfillment question is an initial
  review or an audit — it says what may be answered — so identical views admit identical answers
  and no refusal reveals a role. The seventh review's "identical views" test is superseded by
  this, not refuted: the two views now differ by their stated contract.
- `suspended_verdict`, `_audit_reopens`, the audit-aware `_initial_review` and the path-count
  exceptions are gone; `_positions` is plain again.

## What v0.9 decided and repaired (seventh review, R7)

- **Delegates hold no ruling authority.** `World(humans=...)` names *requesters*; those also in
  `delegates` are delegates and the rest are humans. A delegate posts, pays, accepts and
  disputes; `override` refuses it before any effect. `w.humans` now excludes delegates.
- **A correction uses each appeal reviewer's complete answer.** For an appeal of a ⊥, an
  appeal reviewer is contradicted on either question — the objection or, when rejected, the
  verdict — in the post-settlement branch exactly as at settlement.
- **A ruling between a case's finality and its reviews' payout is a ruling for those
  reviews**: a contradicted review still in `done` is overturned (bond forfeited, no fee); a
  review already `vested` takes the reliability record only. Money never moves after payout.
- ~~An auditor may answer P or ⊥.~~ Withdrawn in v0.10; see above.

## What v0.8 decided and repaired (sixth review, R6)

- **No dispute after a human ruling**, for the same reason as no audit: the ruling settled the
  pre-vesting assessment. A requester who disagrees with the ruling is on the human-review
  path, not a model challenge. Refused before any fee or state change.
- **The grade is the establishing author's.** A human who rules on a delegate's request
  establishes a human-explicit outcome; a delegate who accepts establishes a delegate-explicit
  one. `_grade()` and I13 both read the author of the matching judgment, on every route.
- **Execution cost is the committed actor's, while executing.** `spend(actor, cost, case)` is
  refused before purchase if the actor is not the case's actor or the case is no longer
  executing; unattributed spending stays allowed. Nobody else's purchase becomes a kill fee.
- **Grounds are validated before the fee** for appeals and disputes: text or absent.
- **A post-settlement correction of a ⊥ uses the two-question rule**: a rejected objection
  contradicts the original ⊥ and its author takes the reliability hit; money does not move.
- **Rotation uses a batch-start snapshot**: only actors off duty when the tick began may be
  conscripted in that tick, so a released actor has a tick of ordinary eligibility.
- The stale `strategies.py` comment about ⊥ appeals is replaced by the actual contract.

## What v0.7 decided and repaired (fifth review, R5)

- **No audit after a human ruling.** The ruling settled the question an audit would ask; an
  assignment after it is refused atomically, and an audit open at the ruling is voided.
  Agreement of any audit is judged against the live assessment, never a superseded verdict.
- **A terminal child is a milestone.** A nested request that reached final N without a
  submission (a missed delivery) does not block the parent's submission; the parent carries
  that failure as its own risk. The submit guard and I7 share one definition.
- **The resubmission stage lives on the case.** A replacement reviewer on a revised or
  evidenced submission inherits the F/N-only constraint; the view says `resumed`.
- **A refused dispute changes nothing**: the fee is checked before the vacated-audit
  obligation is touched, under full defaults.
- **Acceptance by ruling ends the rejection obligation** whether or not the requester-actor
  had judged; a contradicted rejection still forfeits its bond.
- **The appeal's grounds are committed** to the History as part of the admitted action, so
  different grounds produce different heads.
- **Working copies are complete and ordered**: I16 now checks that the ledger's event list and
  each case log hold exactly their committed entries, in order — omissions and reorderings
  are detected, not only edits.

## What v0.6 repaired (fourth review, R4)

- **Atomicity is boundary-wide.** Unknown cases, unfundable fee-pool payments, inconsistent or
  mis-stated overrides, and appeals of a P are refused before any balance, state, or
  assessment changes. A refused override leaves no assessment behind to become provenance.
- **One override path.** Validate the whole ruling (including upheld ⇒ N for a ⊥), then void
  every unfinished assignment without fault, overturn every completed verdict that
  contradicts the ruling — a reviewer's, or a requester-actor's rejection, whose bond is then
  forfeited — and settle. Open appeal reviewers are voided, never later timed out.
- **A vacated audit is an obligation.** A timed-out audit keeps the case suspended until a
  replacement completes or the orchestrator calls `waive_audit`; a requester dispute folds
  the obligation into itself. The post-window replacement rule is now reachable.
- **Cost debts are processed first and for every review**, with or without survivors; the
  deposit pays them before anything unused is returned. Claims carry their review:
  `omega_claims` prints and compares as `(reviewer, amount)` pairs and each entry has a
  `.review`, so FIFO servicing credits the obligation being paid.
- **The History is the record.** Every participant action — including explicit acceptance,
  disputes, overrides, volunteering — is committed; ledger events and case logs are copies,
  and I16 checks each copy against its committed entry. The chain is tamper-evident
  in-process; no head is committed outside it.
- **The reviewer view states the question.** An initial review and an audit are
  indistinguishable (`question="fulfillment"`); an appeal or dispute says so and carries the
  appealed assessment and the challenger's explanation, since the reviewer must answer it.

## Driving it

```python
from sim import Params, World
w = World(Params(E0=5.0, H=1e9, omega_rate=0.0), ["A","B","C","D","E","F"],
          humans={"H": 100.0}, on_duty=["C","D","E","F"])
q = w.post_root("H", 45); w.award(q, "A", 40, 8)
w.advance(4); w.submit(q); r = w.assign_initial(q, "C")
w.advance(6); w.complete_review(r, "F", 3)
w.advance(17); print(w.cases[q].state, w.cases[q].grade, w.W("A") - 50)
```

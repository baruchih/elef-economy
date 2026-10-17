# agentic_sim — reference implementation of the 1.2.0 baseline

Built up through v0.4–v0.10, unchanged by the v1.0 consolidation and the v1.0.1 errata, and changed twice since:
for design revision 1 (1.1.0, October 17, 2026: the verification deposit is two pots) and design revision 2 (1.2.0,
the same day: the loop's own clock — planted work, the plant record, the effort dial; see the two sections below).
Section numbers in code comments refer to the working-spec versions they were written against;
`spec/agentic_economics_loop_spec_v1_2_0.md` is the text in force, and its Appendix A holds the defaults that
`sim/params.py` encodes.

The loop's rules as code, with no strategies. Every bid, verdict, appeal, audit
assignment, ruling and human action is injected by the caller. Each action is validated in
full before anything is recorded or moved: it either completes under its rules or changes
nothing. After every tick twenty-one invariants are checked; a failing invariant is a bug in
the engine or a contradiction in the spec, never a property of a strategy.

```
sim/params.py       §18.1 provisional defaults, §19 initialization values
sim/ledger.py       wallets with named lock records, case pools (escrow, expense allowance, fee pot, minted
                    emission), Ω, the backed credit, amount validation, and the hash-chained History that is
                    the authoritative record
sim/engine.py       cases, reviews, challenges (incl. the two-question ⊥ appeal), delegation,
                    settlement (the two pots, tree closure), Ω claim servicing, rotation, the reviewer view,
                    the tick order
sim/invariants.py   I1–I21, run after every tick; each says what it establishes
sim/strategies.py   the decision seams a driver would fill (Protocols only)
sim/record.py       record mode: journals for the History and the event copy, archives for settled
                    cases and reviews, the paged mapping the engine reads them through
drivers/results.py  keeping results: results/tests/<commit>.txt from the runner; results/runs/<run-id>/
                    (manifest, metrics.csv, fingerprint.json) from every run
drivers/load_run.py a throughput run with no economics in it, to size the engine
drivers/view.py     the public surface of World as a driver sees it — the operations a participant or
                    the orchestrator may take, and the reads the rules allow
drivers/stamping.py scoped run, §18.1 q1: careful vs stamping reviewers, declared populations and
                    orchestrator policy; every run writes its manifest, metrics and fingerprint
drivers/sweep.py    cells × seeds over the stamping run (full grid or one factor at a time), every run and
                    the summary under one study folder: results/studies/<study>/<sweep>/runs/
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
tests/test_v11.py                   design revision 1 (1.1.0): the §20 example re-settled, the K = 3 default under
                                    consideration, the appeal variant's scaled fees, the refund waiting for tree
                                    closure, the r4_07 shape, the fee pot's remainder paying a claim and an advance,
                                    nested-first draws, the pay-in, the superseded r5_a principle, I19, record mode, a tree whose expenses exceed the allowance — 14
tests/test_v12.py                   design revision 2 (1.2.0): the §20 planted-work figures, the dial's clamps and what it
                                    moves, the record persisting through suspension and probation, the two tiers, the reserve
                                    running short with its shortfall counted, the capital cap, plants due and the plant
                                    shortfall, the alarm and re-seating, the view without the actor, no challenge on a plant,
                                    I20/I21 catching, newcomer odds — 15
tests/test_perf_equivalence.py      the per-tick check equals the full audit; the working-set engine reproduces the
                                    pinned History head on a seeded random scenario that now plants work (re-pinned once for
                                    1.1.0 and once for 1.2.0); the working set stays bounded — 5
tests/test_record_mode.py           the record on disk (`Params.record_dir`): the same scenario gives the identical
                                    fingerprint, the chain re-hashes from the file alone, a paged-out case comes back
                                    when touched, the resident set stays bounded, the Journal reads like a list, identity and
                                    pickling match memory mode — 8
run_tests.py        every suite with plain python; pytest reports the same (conftest marks the XFAIL)
```

Run: `python3 run_tests.py` — 197 pass, 0 fail, 26 expected failures, each with a stated reason (one original,
four superseded by the view contract, nineteen on the withdrawn reopening path, one superseded by design
revision 1, one by design revision 2). With pytest: `python3 -m pytest tests -q` reports 197 passed, 26 xfailed; the
runner expands pytest parametrization as pytest does, including multi-argument and stacked marks. (Spec Appendix D
records the count at the v1.0.1 freeze, 156; at 1.1.0, 181; at 1.2.0, 197.)

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
tick beside the tick check, reproduces the pinned History head (the v1.0.1 engine's, commit 6a746a1, until
design revision 1 changed settlement; re-pinned once at the 1.1.0 commit).

Measured after the change: 20 actors × 1,000 ticks in 1 s at a constant ~1,000 ticks/s (was ~25 min);
200 actors × 10,000 ticks (300,000 cases) in 104 s at a constant ~95 ticks/s, final full audit 35 s.
The remaining limit was memory, not time: the record kept whole in memory — 4.85 million History
entries and 300,000 cases — took 4.3 GB. Record mode, below, lifts it.

## Record mode: the record on disk (October 16, 2026)

`Params.record_dir = "<directory>"` moves the record out of RAM (`sim/record.py`), with no change to
what the engine does:

- `history.jsonl` and `events.jsonl` hold the History and the ledger's event copy, one entry per
  line, written through as they are committed (`Journal`: an append-only sequence that keeps its
  newest few thousand items decoded in memory and reads older positions from the file). The chain
  re-hashes from `history.jsonl` alone: `tests/test_record_mode.py` does so without the engine.
- `cases.pickle` and `reviews.pickle` hold settled cases and their reviews (`Archive`). A case is
  paged out when it leaves the working set — settled, every review settled, nothing pending — and
  takes its History positions and its empty pool with it; it comes back resident when the engine
  touches it (a post-settlement override, a serviced Ω claim) and is paged out again afterwards.
  `w.cases` and `w.reviews` remain mappings in creation order (`PagedDict`): `w.cases[k]` makes an
  object resident, for code that may change it; `peek(k)` and iteration return a resident object or
  a transient copy, for readers that must not pull the archive in. The invariants read through
  `_peek`; new audit code must too.
- `check_all` streams the record in both modes: one pass over the events (I3, and the per-event
  halves of I4 and I10), one over the reviews, the cases in chunks of 2,048, and two passes for I16
  (ledger entries paired one-to-one with the event copy in order; each committed case entry found in
  its log at the position the log claims; logs strictly increasing and their total equal to the
  record's). It establishes the same facts as before; it no longer builds an index of every position.
- Two properties make record mode indistinguishable to a caller. Identity: an object handed out
  before it was paged out is the object handed back after (the mapping remembers paged-out
  objects weakly while anything holds them). Pickling: a `Journal` pickles as the list it
  replaces and a `PagedDict` as the dict, so `pickle.dumps(w)` — how the reviewer suites snapshot
  a world — is the same object graph in both modes. Both were found missing by running the whole
  suite in record mode (`python3 run_tests.py --record`), which now passes identically; that run
  is the storage layer's conformance check and its log goes to `results/tests/<commit>-record.txt`.
- `w.close()` flushes and closes the files; the world is not used after it.

Measured, 200 actors × 10,000 ticks, 300,000 cases, 4.81 million History entries, 3.0 million events:

|                    | in memory                 | record mode                              |
|--------------------|---------------------------|------------------------------------------|
| run                | 104 s, ~95 ticks/s        | 126 s, ~80 ticks/s (constant)            |
| peak RSS           | 4.3 GB, growing           | 81 MB during the run, 141 MB in the audit |
| final `check_all`  | 35 s                      | 95 s (about 0.3 ms per case)             |
| on disk            | —                         | 2.8 GB (history 1.47 GB, events 0.91 GB, cases 0.36 GB, reviews 0.11 GB) |

What still grows with the run is the journals' position index, eight bytes per entry — about 200 bytes
per case, so a gigabyte at five million cases — and the dead space an archive accumulates when a case
is paged out more than once. Both are far off; a sparse index would be the next step if they are
reached.

**Which check to run when.** The per-tick check *is* the incremental audit: it verifies the chain
from the last verified head, checks the copies appended since, and runs every predicate over
everything that could have changed — and `advance` always runs it. The full audit is from genesis
by definition; that is its only reason to exist (an independent re-derivation from the whole
record, and the one check that notices an edit to an entry already verified), so its cost is the
whole record every time, and scheduling it on a cadence makes a run quadratic in its length: with
`full_check_every=20`, 200 actors × 1,000 ticks took 244 s, of which about 230 s were the fifty
audits. Strategy runs therefore use the regime the 300,000-case run used — the per-tick check every
tick and one `check_all` at the end — and `full_check_every` is for conformance runs of the engine
itself. Every run's manifest records which regime it ran under.

## Design revision 1 — the verification deposit is two pots (1.1.0, October 17, 2026)

The first scoped run (`drivers/stamping.py`, October 16) showed careful reviewers paying for their own
care: under v1.0.1 §4.3 the deposit was one pot, reimbursing expenses and paying *what remained* as the
fee, so every credit of care reimbursed was a credit of fee lost. Design revision 1 (accepted as rc.3;
`spec/design_revisions/`, consolidated into `spec/agentic_economics_loop_spec_v1_1_0.md` §4.3 and
Appendix F) makes the deposit two named pots. In the engine:

- `CasePool` holds `escrow`, `deposit` (the expense allowance φ^E — the field keeps its v1.0.1 name;
  reviewer tests read it), `fee_pot` (φ^F) and `minted`. Two event kinds were added, `feepot_in` and
  `feepot_out`; `fee_out` now carries emission shares alone. `Params` gains `phi_E_root`, `phi_F_root`
  and `f_fee` (`phi_root` remains as their sum); a `Case` carries `phi_E`, `phi_F` in its frozen nominals.
- `_reimburse` is unchanged in order — the root's allowance, then an Ω advance, then deferral.
- `_settle_reviews` follows §4.3: expense debts from the root's allowance only (a shortfall is a claim
  on Ω or an unrecovered advance, as before); each survivor's fixed fee `w_r · f` from the root's fee
  pot, scaled pro rata only when the pot cannot pay this case's fees in full, plus its emission share in
  full. A nested case's reviews draw on the root's pool at the nested case's own settlement.
- `_maybe_close_tree` runs after every settlement and every terminal exit in a tree: once the root and
  every case under it are final and settled, the fee pot's remainder pays the tree's outstanding Ω
  claims to the claimants (retiring them from Ω's queue), then repays the tree's unrecovered advances
  to Ω, and only then both pots' remainders return to the root requester. The root logs "tree closed".
- I10 admits exactly the post-vesting movements the revision names, by the event's note: a nested case's
  draws on its root's pots (`"nested …"`) and the closure (`"tree closure…"`), beside the deferred
  reimbursements and Ω claims it already admitted. I12 freezes both pots. **I19** is new: per root, fees
  from the pot ≤ φ^F, fee money to expenses only at closure and only from what every fee in the tree left,
  no fee from the allowance (per event), no refund before closure, a closed tree has every case settled
  and both pots empty. A root with open pots is not quiescent, so it stays in the working set and, in
  record mode, resident until its tree closes.
- `drivers/view.py` reports Ω's outstanding claims in `money()`; `drivers/stamping.py` gains `--fee`,
  `--phi-e`, `--phi-f`, per-disposition fixed-fee and haircut columns, and Ω's unrecovered advances and the
  pots' refunds in the economy counters; run names carry `f` and `X`.
- Tests: the suite's own figures were revised to §20 under 1.1.0 (`test_spec`, `test_v06`, `test_v07`),
  the golden heads in `test_perf_equivalence` (and so `test_record_mode`) were re-pinned once, and
  `test_v11.py` carries the revision's figures and I19. Reviewer-authored tests are untouched: one,
  the fifth review's `test_r5_a_unfunded_dispute_keeps_vacated_audit_obligation`, pinned the v1.0.1
  deposit through a human budget of exactly B + 10 and is an expected failure for that stated reason,
  with its principle re-asserted in `test_v11`; every other reviewer test passes unchanged, including
  r4_07, which the revision's tree-closure wording was shaped to keep.

## Design revision 2 — the loop's own clock (1.2.0, October 17, 2026)

Runs 2–3 under 1.1.0 (`results/studies/`) showed the loop fair only when both challengers are present — the
actor appealing rejections, the requester disputing approvals — and blind under capture: a stamper-majority
reserve produces every signal the loop has, reliability included. Design revision 2 (accepted as rc.3 with one
consolidation fix; `spec/design_revisions/dr2_the_loops_own_clock_1.2.0.md`, consolidated into
`spec/agentic_economics_loop_spec_v1_2_0.md` §7.6, §11.2, §12.2 and Appendix G) gives the orchestrator truth of
its own. In the engine:

- **Plants.** `World.create_plant(truth, B)` builds a root case in the submitted state, attributed to two system
  wallets (`PLANT_REQ`, `PLANT_ACT`) that Ω funds at creation (price, both pots, the actor's guarantee — 45 at the
  defaults) and that are swept back to Ω when the plant's tree closes; the marker is committed sealed
  (`plant_created`, a hash of case, truth and nonce) and revealed at adjudication (`plant_revealed`). Refused whole
  when Ω's unlocked balance cannot fund it. `plants_due()` is what the rate π_t calls for — it accrues at every real
  initial assignment — and the driver supplies; what is still owed at a period's end is the plant shortfall.
- **Adjudication by truth.** `_adjudicate_plant` runs at a plant's initial F/N: right → stood (paid at settlement,
  record +1); wrong → `_overturn_review` (bond burned whole, ρ down, p doubled, record −1); P/⊥ → spent. The plant
  then settles by its truth (good: pending F, vests; bad: final N at once), grade `plant`. `assign_audit`, `dispute`,
  `respond`, `override`, `accept_explicit` refuse a plant.
- **The plant record.** `Actor.plant_bad` / `plant_good` are trailing windows of (tick, wrong); `a_hat`, `r_hat`,
  `record_passes(θ)`, `duty_eligible`, `panel_eligible`. `_eligible(c, reviewer, role)` refuses an ineligible
  assignment for the tier; `_check_record` suspends at a crossing (`suspended_until`) and the actor leaves duty as its
  review completes. **Implementer's reading:** a record that still fails when the suspension ends cannot have changed
  (a suspended actor judges no plants), so `_rotate` readmits it *on probation* — duty, not panels — until its next
  plant re-checks it; read literally the revision made every suspension permanent. Flagged in the text and Appendix
  G for confirmation; the alternative is one branch of `_rotate`.
- **The reserve.** `_rotate` readmits, removes duty-ineligible actors with no open review (replacement or not),
  swaps turns as before, fills to `X_t` from the eligible pool (lowest κ) or shrinks to it, and sets
  `reserve_shortfall_now` / `eligibility_shortfall`; I9 is `min(X_t, eligible)`.
- **The dial.** `_maybe_end_period` (step 5, before rotation) closes a period at `period_plants` adjudicated plants
  or `period_ticks` ticks: F̂ from the period's bad plants, m clamped to [0.9 m, 2 m] then [1, m_max], π_t, X_t from
  the period's demand (initial × (1 + π), audits at m p̄ × approvals, challenge reviews; × mean review duration;
  floor V_max + 1), the alarm after two periods at m_max with F̂ > F*, which `_reseat_reserve`s by lowest â. ω is
  `omega_rate × m_t` at award; `Actor.p_eff = min(1, m_t p_j)` is what a driver rolls. `Params.dial=False` holds m
  and X_t; with `pi0=0`, `p_start=p_cap=0.5`, `Omega0=20` that is the 1.1.0 engine (`--rules 1.1.0` in the driver).
- **I20** (plants self-adjudicated, the commitment and the reveal) and **I21** (the dial bounded, the reserve sized,
  no ineligible assignment, no ineligible actor past its review) per tick; I13 admits the plant grade. The reviewer's
  view drops `actor`.
- **Drivers.** `drivers/view.py` exposes `create_plant`, `plants_due`, `p_effective`, `dial`, and Ω's total with its
  plant capital in `money`. `drivers/stamping.py` supplies plants before the tick's assignments (bad w.p. β_P, truth
  from its task world), rolls `p_effective`, applies the two tiers when offering reviewers, has `--rules 1.1.0`,
  `--pi0`, `--dial`, `--beta-p`, `--camouflage` (the red team), `--p-cap`, `--omega0`, and new columns (m, π, X_t,
  F̂, suspensions, alarms, shortfalls, plants by outcome, Ω's plant spend and net, per-population plant failures,
  â, eligibility). `drivers/sweep.py` carries them.
- **Tests.** `test_v12.py` (15); `test_v05`'s view assertion and `test_spec`'s Ω figures, audit cap and
  initialization bound revised; `test_v11`'s advance test pins Ω's float at 20 explicitly; the equivalence scenario
  plants work with short periods and its goldens were re-pinned once. Reviewer tests untouched: the third review's
  test 18 pinned Ω's float at 20 and is an expected failure with that reason.

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

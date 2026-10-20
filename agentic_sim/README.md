# agentic_sim — reference implementation of the 1.7.0 baseline

Built up through v0.4–v0.10, unchanged by the v1.0 consolidation and the v1.0.1 errata, and changed four times
since, all on October 17, 2026: for design revision 1 (1.1.0: the verification deposit is two pots), design revision 2
(1.2.0: the loop's own clock — planted work, the plant record, the effort dial), design revision 3 (1.3.0: inspection
is membership), design revision 4 (1.4.0: the orchestrator's troops), design revision 5 (1.5.0: the reserve is sized to the need), design revision 6 (1.6.0: auto-scale) and, on October 18, design revision 7 (1.7.0: the state's earnings — see the seven sections below). Section numbers in code comments refer to the
working-spec versions they were written against; `spec/agentic_economics_loop_spec_v2_3_0.md` is the text in force,
and its Appendix A holds the defaults that `sim/params.py` encodes.

The loop's rules as code, with no strategies. Every bid, verdict, appeal, audit
assignment, ruling and human action is injected by the caller. Each action is validated in
full before anything is recorded or moved: it either completes under its rules or changes
nothing. After every tick twenty-five invariants are checked; a failing invariant is a bug in
the engine or a contradiction in the spec, never a property of a strategy.

```
sim/params.py       §18.1 provisional defaults, §19 initialization values
sim/ledger.py       wallets with named lock records, case pools (escrow, expense allowance, fee pot, minted
                    emission), Ω, the backed credit, amount validation, and the hash-chained History that is
                    the authoritative record
sim/engine.py       cases, reviews, challenges (incl. the two-question ⊥ appeal), delegation,
                    settlement (the two pots, tree closure), Ω claim servicing, rotation, the reviewer view,
                    the tick order
sim/invariants.py   I1–I25, run after every tick; each says what it establishes
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
                                    I20/I21 catching, newcomer odds — 15 (asserted on the 1.2.1 engine mode, the 1.2.0 control)
tests/test_v13.py                   design revision 3 (1.3.0): the award refused to a non-member, atomically; a pending actor
                                    suspended while its case settles; the 1.2.1 mode; probation's pin, initial-only seats and
                                    re-suspension on any failure; readmission on the trailing record with n_min new outcomes and
                                    panel seats later; the newcomer pin; the members' cap with probationers taking the initial
                                    seats; the cap's floor and the panel floor by availability; the duty fund's split and payout
                                    by role weight, and the fund off; plant capital on the pots alone; I22/I23 catching — 11
tests/test_v14.py                   design revision 4 (1.4.0): a rolled audit holds the case and is admitted after the window;
                                    an audit seat unfilled for w_R taken by a troop and netting the fund +3; summons refusals
                                    (window, free member, fund short with Ω's advance exhausted, the state's own audit); the
                                    advance drawn and repaid; plants never summon; a request unawarded for w_A delivered by a
                                    troop at the market price (+10); the troop accepting every verdict at the verdict; the
                                    state's own work audited by a member only and the held case counted; uplift only above the
                                    reserve; I24/I25 catching — 10
tests/test_v15.py                   design revision 5 (1.5.0): a refusal for funds raises the reserve by the refused cost once per
                                    seating (and the 1.4.0 reading does not move); a request below the market or unfundable by its
                                    requester adds nothing; a panel short of both seats adds two; refused-then-carried raises the
                                    peak once; no uplift at or below the reserve and the balance above it paid; the peak holds
                                    within the period and restarts at the standing demand at the boundary; I23 catching — 7
tests/test_v16.py                   design revision 6 (1.6.0): the service clock from posting to the first verdict, on time and
                                    late with the rebate capped at B; the clock stopped for a below-market request and at a final
                                    without a verdict; nothing owed on withdrawal before award; Ω's liability serviced oldest first;
                                    Ω advancing only above the plant reserve; review seats before deliveries and the delivery's
                                    inspection check with the advance drawn on its own shortfall; the reserve seating the queue;
                                    a panel seat needing a determined record once the first plant is adjudicated; R_T over two
                                    periods; I26 catching — 11
tests/test_v17.py                   design revision 7 (1.7.0): a troop delivery's earnings land in the troop account and the uplift
                                    fund sees none of them (the 1.6.0 control pays them out as uplift); the surplus flows to Ω only
                                    from above R_T, the two-period peak of capital held, and a refusal no longer raises it; the
                                    uplift fund pays its whole balance while the troop account keeps its reserve; a troop review
                                    seat nets its fee (its cost reimbursed from the allowance); Ω's record by source; I23 catching an
                                    uplift fund that does not reconcile or holds a lock; the cap at two thirds with its floor — 8
tests/test_v171.py                  patch 1.7.1: the award summons is per request — the requests past w_A beyond the free
                                    fundable members are summoned for, oldest first, the oldest left to the members; enough
                                    free members mean no summons; a long queue with two free is served two short of its
                                    length; the period record carries the market's share — 4
tests/test_v20.py                   design revision 8 (2.0.0): the price of work — issuance and conservation over every kind; the posting lock,
                                    its release and raise_ceiling; P_t indexing frozen at the first lock; B̄ members only, P_t troops too; the state at
                                    cost, creation and retirement; the rebate at the stop; N_T and two places; the flag; a crowd's arrival and
                                    departure; the scenario operation and I28; the cost API in credits; the period record; floating off = 1.7.1
tests/test_v21.py                   design revision 9 (2.1.0): the bank — a summons lent for its shortfall at the expected cost and repaid from its
                                    own return before Ω keeps; a failed delivery's loan as debt and the next inflow repaying it at once; the order
                                    debt → liabilities → Ω; the wall refusing a delivery, marked and told, and never a seat; unbounded the control;
                                    the burn floored and the state's own record; at_cost and half; P_t published at the boundary; a plant's pots
                                    minted and the sweep destroyed with Ω untouched; the scenario; the capacity mark; the period record; bank off
                                    = 2.0.0 — 13
tests/test_v22.py                   design revision 10 (2.2.0): the rebate from income — fees pooled as a lock on Ω, the returns of capital not;
                                    a claim recorded at the stop and paid at the close from the pool only; pro rata and the rest forgone, never
                                    carried; the pool funds no summons; r_s indexed when stated; debt before the pool; I32; the §6 quiet and
                                    flooded periods; rebate_pool off = 2.1.0 — 9
tests/test_v23.py                   design revision 11 (2.3.0): the supply side — an arrival as a probationer with a bank-minted float, no award
                                    root or nested, the float indexed; admission on n_min bad plants counted apart from readmissions; a plant failure
                                    suspends an arrival; depart refused for a commitment, an open or unsettled review, a lock, a claim on Ω, then the
                                    wallet out and the identity gone; the parent's pots, the child's audit on them, the root's deposit untouched, the
                                    node's closure; the root reading as the control; no troop delivers a nested request; the reviewer advance from
                                    the pool and the close net of it; the record and the view; supply off = 2.2.0 — 13
tests/test_perf_equivalence.py      the per-tick check equals the full audit; the working-set engine reproduces the
                                    pinned History head on a seeded random scenario that now plants work (re-pinned once for
                                    1.1.0 and once for 1.2.0); the working set stays bounded — 5
tests/test_record_mode.py           the record on disk (`Params.record_dir`): the same scenario gives the identical
                                    fingerprint, the chain re-hashes from the file alone, a paged-out case comes back
                                    when touched, the resident set stays bounded, the Journal reads like a list, identity and
                                    pickling match memory mode — 8
run_tests.py        every suite with plain python; pytest reports the same (conftest marks the XFAIL)
```
tests/test_v24.py                   design revision 12 (2.4.0): the state's reservation — the troop at max(B̄, 8) with the guarantee, the fee and
                                    the burn at it and P_t counting it; no summons below the state's price (declined, marked, waiting); a member may
                                    still take a request under the floor; the award pass gathering only β ≥ p_T against the 2.3.0 control; the
                                    mark set at posting, kept under a short raise, cleared at the floor; the clock's one condition; the view's
                                    floor, price and marks; F0 < G_V refused at construction; the kill fee zero for a child that never worked; I37
                                    catching a delivery under the floor and a mark out of place; the reservation at 0 = 2.3.0 — 11
tests/test_v25.py                   design revision 13 (2.5.0): the missed child — a cancellation before the deadline unchanged, at the deadline
                                    tick refused with the world unchanged, after the lapse refused; the lapse forfeiting to the parent, releasing the
                                    bond and freeing the parent; a child submitting on its last tick; the kill fee before the deadline; §6's lowballer
                                    at −3; I38 catching a deadline-tick cancellation and a lapse that did not run; missed_child off = 2.4.0 — 7
tests/test_v26.py                   design revision 14 (2.6.0): the plant's disguise — a plant posted as a root in sequence under a fresh name with the
                                    pots minted and the marker sealed; the award as the market's report (the plant actor takes it, the member not
                                    committed, no price recorded, no fee); the submission at the drawn tick and the adjudication and destruction as
                                    before; a good plant vesting to its actor; the p_T path past w_A counted apart; fresh names aliasing the two
                                    wallets; the mark and the available count; the draws reading the trailing real roots; the public identifiers
                                    translated both ways and carrying no order; the dial's counts at the close; I39's catches; plant_market off = 2.5.0; the
                                    capacity and credit refusals on the p_T path and the pinned draw (the ruling after run 21); submit_plant at the
                                    drawn tick and not before (the Q2 probe's correction) — 16

Run: `python3 run_tests.py` — 327 pass, 0 fail, 32 expected failures, each with a stated reason (one original,
four superseded by the view contract, nineteen on the withdrawn reopening path, one superseded by design
revision 1, one by design revision 2, two by design revisions 10 and 11 — a service fee pooled until the close and the pool's advance move the reimbursement figures they pin — two by design revision 11 — the parent's pots make three children unaffordable on a float of 50, and the root's allowance is no longer exhausted by a nested review — two by design revision 8 — the backing's v_t and the pay-in refused at posting; the three 1.x figures 2.0.0's moving index broke pass again under 2.1.0's index per period). With pytest: `python3 -m pytest tests -q` reports 259 passed, 31 xfailed; the
runner expands pytest parametrization as pytest does, including multi-argument and stacked marks. (Spec Appendix D
records the count at the v1.0.1 freeze, 156; at 1.1.0, 181; at 1.2.0, 197; at 1.3.0, 208; at 1.4.0, 218; at 1.5.0, 225; at 1.6.0, 236; at 1.7.0, 244; at 1.7.1, 248; at 2.0.0, 259; at 2.1.0, 275; at 2.2.0, 282; at 2.3.0, 293; at 2.4.0, 304; at 2.5.0, 311; at 2.6.0, 327.)

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
`spec/agentic_economics_loop_spec_v1_2_1.md` §7.6, §11.2, §12.2 and Appendix G) gives the orchestrator truth of
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

## Design revision 3 — inspection is membership (1.3.0, October 17, 2026)

Run 4 under 1.2.0 (`results/studies/1.2.0-clock/`) showed the clock keeping the loop honest with nobody watching,
and suspension from duty being a reward: the honest minority carried 500–800 reviews each at a fee of 2 while the
suspended stampers, freed from duty, took the awards at 20 and ended richer at 60/40. Design revision 3 (accepted
as rc.2 with the panel floor's availability clause; `spec/design_revisions/dr3_inspection_is_membership_1.3.0.md`,
consolidated into `spec/agentic_economics_loop_spec_v1_4_0.md` §5.2, §8.3, §11.2, §12.1–12.2 and Appendix H) makes
inspection the price of membership. In the engine:

- **Membership.** `Actor.is_member` (neither suspended nor on probation). `award` refuses a non-member before any
  effect and records `Case.member_at_award`. A suspended actor finishes what it holds by the ordinary rules.
- **Probation.** At `T_susp` a suspended actor becomes a probationer (`probation=True`, `since_susp=0`): initial
  reviews only (`panel_eligible` false), `p_eff` pinned at 1 (`Actor.pinned`, also for a newcomer with fewer than
  `n_min` bad plants judged; the §8.3 halving and doubling do not run while pinned). `_check_record(a, failed)`:
  any plant failure re-suspends (`_suspend`, clock restarted); readmission when the one trailing record passes
  `theta_duty` and `since_susp ≥ n_min` (`readmitted_at`, `readmissions`, `readmission_ticks_sum`). `Params.membership
  = False` is the 1.2.1 behaviour (suspension from duty only; probation re-checked at the next plant).
- **The reserve.** `_rotate_membership`: `E_t` eligible members, cap `_member_cap(E_t) = max(⌈E_t/2⌉, V_max + 1)`
  (the implementer's reading, flagged), floor `min(V_max − 1, E_t)`, `member_seats` sized each period on applied
  audit odds (`period["audit_demand"]`, the approving reviewer's `p_eff` per approval) plus the challenge rate.
  Order: idle members above the cap leave; probationers displace idle members from initial seats (`target_m`
  kept); turns refilled by kind (a member's initial seat to a probationer first; an outgoing probationer with no
  free probationer stays); member seats filled; probationers for initial seats; members for the rest below the cap;
  shrink (probationers first); `_member_pool_exhausted` for the floor, `_pool_exhausted` for I9. The alarm's
  re-seat respects the cap.
- **The duty fund.** `DUTY_FUND` wallet; `award` splits ω_t into ω₀B to Ω and (m − 1)ω₀B to the fund (`fund_in`);
  each settlement batch computes `upw = fund.U / total_w` and `_settle_reviews` pays `w_r · upw` to every surviving
  review (`Review.uplift`, in `fee`; `fund_out`); the residue carries. `Params.duty_fund=False` keeps ω with Ω.
- **Plant capital.** `create_plant` funds φ^E + φ^F only (`net_plant_capital`); no escrow, no guarantee lock;
  `_vest` pays no price and `_finalize_N` forfeits nothing for a plant (`_plant_notional`); I15 exempts a plant's
  guarantee; `I21_plant_capital` checks it.
- **I22** (membership: no award to a non-member, no probationer on a panel, probationers pinned, readmission only
  with the counter and a passing record) and **I23** (the cap at seating with mid-review tolerance, the floor by
  availability, the fund reconciling and lock-free) per tick and in the full audit.
- **Drivers.** `drivers/view.py`: `membership(aid)`, the fund and readmissions in `money()` / `dial()`.
  `drivers/stamping.py`: offers to members only; `--rules 1.3.0|1.2.0|1.1.0`, `--fund on|off`, `--m-max`,
  `--stamper-mode plain|reformer` (a stamper that reviews carefully on probation and stamps once readmitted);
  columns for members/probationers on duty, member seats, readmissions and their mean time, the fund's flows,
  per-population uplift, probation reviews and approvals, ticks with awards refused for want of members,
  probationers' false approvals that vested. `drivers/sweep.py` carries them.
- **Tests.** `test_v13.py` (11); `test_v12.py` now asserts the 1.2.1 engine mode explicitly; the equivalence
  scenario's goldens were re-pinned once (it now suspends actors from the market, puts them on probation and pays
  the fund). Reviewer tests untouched and passing.

## Design revision 4 — the orchestrator's troops (1.4.0, October 17, 2026)

Run 5 under 1.3.0 (`results/studies/1.3.0-membership/`) showed a captured fixed population honest and short of
hands — awards unfilled for want of a free member in 800–900 of 1,000 ticks, and probationers' false approvals
reaching customers because their pinned audits found no member free (a leak older than probation: the drivers
had dropped a rolled audit that found no auditor since run 1). Design revision 4 (accepted as rc.2 with the
external reviewer's note that a troop accepts a verdict at the verdict; `spec/design_revisions/
dr4_the_orchestrators_troops_1.4.0.md`, consolidated into `spec/agentic_economics_loop_spec_v1_4_0.md` §7.7,
§8.3, §12.3 and Appendix I) gives the orchestrator servers of its own. In the engine:

- **The obligation.** `roll_audit(cid)` records a rolled audit as an obligation of the case — `audit_obligation`
  with `open_items` up by one, the shape of the vacated-audit hold — so the window cannot close and the case
  cannot vest until an audit completes; `assign_audit` discharges it and is admitted after the window for it; a
  human ruling ends it (I18); `waive_audit` refuses the state's own work. `audit_odds(cid)` is what the driver
  rolls: 1 for a troop reviewer's approval of a troop's delivery (`market_audit_only`, recorded by the engine at
  the verdict), the reviewer's applied odds otherwise, `min(1, m p_floor)` for a troop reviewer's approval of a
  member's work (a default chosen at implementation). The stamping driver rolls, records, and never drops.
- **Troops.** `World.troops` holds each troop's kind, case, review, summons and release ticks, cost and lock. A
  troop id (`T<n>`) is aliased to the fund's wallet in the ledger (`Ledger.aliases`, `resolve`), so bonds,
  guarantees, costs, reimbursements, fees and prices land on `DUTY_FUND` and I15 reconciles through the alias;
  every reviewer lookup in the engine is guarded for a non-actor (`_record_outcome`, `_release_attached_reviewer`,
  `_overturn_review`, `_withdraw_review`, settlement). A troop's weight is excluded from the batch's emission and
  uplift; a troop's delivery is final N at any verdict but F (`_initial_verdict`), its `respond` and `post_nested`
  are refused, and a resumed review re-seats it.
- **Summons.** `_summon_troops(tick)` at step 5 after `_rotate`: per live case (never a plant, never a ruled case),
  the audit seat (since the roll or the vacate), the initial seat (`seat_since`, set at submission and at an
  initial review's withdrawal), the panel seats (`challenge["seat_since"]`), each after `w_R` seating steps with
  no free eligible on-duty reviewer (`_free_eligible_reviewer`), bounded by V_max; the award after `w_A` with no
  free fundable member (`_free_fundable_member`) and β ≥ B̄ (`mean_awarded_price`, the period's mean awarded price,
  the last period's, else the ceiling). `_fund_can_carry` draws Ω's advance up to `A_T`; `_summon_review` /
  `_summon_delivery` purchase the cost (`ledger.purchase` by the fund), lock the bond or guarantee, create the
  seat or the award, and record the summons in the History. The troop-on-troop audit seat is never summoned for
  and counted as held. Counters: summons, shortfall (seats, awards, held ticks), troop-ticks, held for the
  market's audit (now, max age); in the period record with the fund's balance, reserve and advance.
- **The fund's order.** `_repay_advance` before the batch (and after it, from the batch's inflows); uplift from
  `max(0, fund.U − R_T)` where `R_T` is the larger of this and the last period's peak troop capital; the engine
  flags an uplift paid from below the reserve (I23).
- **I24** (one seat per troop, not an actor, no plant, no emission or uplift, no troop-on-troop audit, delivery
  within the ceiling) and **I25** (no vest with an obligation outstanding; the state's own work vests only after a
  member's audit) per tick and in the full audit; I9, I22, I23 amended.
- **Drivers.** `drivers/view.py`: `roll_audit`, `audit_odds`, `is_troop`, `troops()`. `drivers/stamping.py`:
  rolls on `audit_odds` and records the roll; supplies a troop's verdict (truth w.p. 1 − ε_T, no cost) and
  submission (at its own τ); `--rules 1.4.0|1.3.0|1.2.0|1.1.0`, `--troops`, `--eps-t`, `--w-r`, `--w-a`, `--c-t`,
  `--c-d-t`, `--a-t`; troop columns (summons, troop-ticks, shortfall, held, fund reserve, advance, B̄, troop
  deliveries by outcome, troop false approvals, obligations). `drivers/sweep.py` carries them.
- **Tests.** `test_v14.py` (10); the equivalence scenario rolls audits as obligations and pays troops nothing
  at completion, and its goldens were re-pinned once. Reviewer tests untouched and passing.

## Design revision 5 — the reserve is sized to the need (1.5.0, October 17, 2026)

Run 6 under 1.4.0 (`results/studies/1.4.0-troops/`) showed the troops doing what revision 4 said — vesting back at
the 1.2.0 control, the state's share reading the capture, troops to zero as a population turned honest — and the
fund refusing 4,800–8,800 award summonses a run while paying 6,400–12,700 in uplift: R_T, the peak capital troops
*had* carried, was what every batch drained the fund to, so the peak could never rise. Design revision 5 (accepted as
rc.2; `spec/design_revisions/dr5_the_reserve_is_sized_to_the_need_1.5.0.md`, consolidated into
`spec/agentic_economics_loop_spec_v1_5_0.md` §12.3, I23 and Appendix J) changes one rule — what the reserve
measures. In the engine:

- **Demand.** `_summon_troops` zeroes `_pass_refused` at the start of its pass; `_summon_review` and
  `_summon_delivery` add the `need` the carry check refused (`_last_refusal_funds` tells the panel loop, which stops
  at the first refusal, to add the seats it did not attempt — only when the refusal was for funds); a request priced
  below B̄, a requester that cannot pay in, or a path at V_max returns before the carry check and adds nothing. At the
  pass's end `troop_demand_held` (capital of live troops, as `_troop_capital_now`) and `troop_demand_refused` are set;
  `troop_demand_now` is D_s.
- **Reserve.** `R_T` is `troop_demand_peak`, the running maximum of D_s over the current period, with
  `troop_demand_peak_refused` the refused part of the seating that set it. `_maybe_end_period` records `demand_peak`,
  `demand_peak_refused` and `demand_last` in the period record, then resets the peak to the capital still held — the
  standing demand — before the same tick's seating adds whatever it refuses. The uplift check (`max(0, fund.U − R_T)`)
  is unchanged. `Params.reserve_demand=False` keeps the 1.4.0 reading (the larger of this and the previous period's
  peak capital carried) as the declared control.
- **I23** gains two inequalities: R_T ≥ the capital live troops hold, and R_T ≥ D_s at the last seating.
- **Drivers.** `view.troops()` adds `demand`, `demand_held`, `demand_refused`, `demand_peak_refused`;
  `drivers/stamping.py` writes `troop_demand`, `troop_demand_refused`, `demand_peak_refused` per tick, attributes each
  probationer's false approval by route (`pfa_route_upheld` / `pfa_route_overturned` / `pfa_route_other`) and, on the
  upheld route, by the auditor's kind at the time (`pfa_kind_troop` / `_standing` / `_lag` / `_readmitted`, from its own
  suspension log, final in the last row), offers `--decline-awards <share>` (careful actors that offer for nothing;
  `decliner_wealth`, `careful_offering_wealth` and their award counts) and `--rules 1.5.0|1.4.0|1.3.0|1.2.0|1.1.0`.
  `drivers/sweep.py` carries the new columns and `dec`, `k` for `decline-awards`, `tasks`.
- **Tests.** `test_v15.py` (7); the equivalence scenario's goldens were re-pinned once (the uplift paid changes where
  a refusal occurred, and the period record carries the new readings). Reviewer tests untouched and passing.

## Design revision 6 — auto-scale (1.6.0, October 17, 2026)

Run 7 under 1.5.0 (`results/studies/1.5.0-reserve/`) showed the reserve rule doing what it said and not helping: the
reviewing seat, not the treasury, capped the market (reviews that found no reviewer 7,300–11,400 case-ticks a run, the
open-case queue ~300, vesting pinned near the posting-rate ceiling whoever delivered); the demand stock counted a
never-expiring queue; the one-period reset saw-toothed; and the probation leak was the plant record's lag on the
auditor. Design revision 6 (accepted as rc.2; `spec/design_revisions/dr6_auto_scale_1.6.0.md`, consolidated into
`spec/agentic_economics_loop_spec_v1_6_0.md` §3.1, §6.1, §7.1, §10.4, §12.1, §12.3, I26 and Appendix K) adds five
rules, each behind a `Params` flag so run 8 can attribute them; `--rules 1.5.0` turns them off together. In the engine:

- **The service clock** (`service_clock`, `T_s`, `r_s`). `Case.clock_ticks` counts one per tick in the summons pass for
  every live root request that is not a plant, while β ≥ B̄ before award (`_clock_runs`); `_stop_clock` runs once, from
  `_initial_verdict` (F or N), `_finalize_N` (a deadline missed) or `_vest` (a human's override with no initial
  verdict): lateness past `T_s`, rebate `min(r_s · late, B)` (r_s 0 means ω₀B), paid Ω → requester from Ω's balance
  above the plant reserve, the remainder appended to `omega_liabilities` with its tick. `_service_omega_liabilities`
  pays oldest first — those older than a period before the pass, the rest after it; the note is I10-exempt. Readings:
  `on_time_n`, `late_n`, `lateness_sum`, `rebates_owed/paid`, `liabilities_accrued/paid`, `open_late()`; per period in
  the record. `withdraw_unawarded` settles nothing.
- **Ω backs the fund above a plant reserve** (`omega_backs_fund`). `_omega_available()` is Ω's unlocked balance above
  `_plant_reserve()` — π_t × the period's initial-review rate (floored at the previous period's) × (φ^E + φ^F) ×
  `plant_reserve_life` ticks (15, a plant's life — the implementer's reading; 0 is the text's ticks remaining, kept as
  the declared cell `--plant-reserve period`) — and replaces A_T's room in `_fund_can_carry`; with the flag off A_T
  binds as under 1.5.0.
- **Inspection first; a delivery carries its inspection.** `_summon_troops` runs two passes over the live cases in
  creation order — the review seats, then the awards; `_summon_delivery` first checks fund.U + Ω available ≥
  c^D_T + G + 2(c_T + G^V) and then draws the delivery's own shortfall; a younger case summoned after an older one of
  the same kind was refused for funds sets `_priority_violation` (I26). Ω's minimum unlocked balance is read per period.
- **Seat the queue** (`seat_the_queue`). `_waiting_reviews()` counts root submissions without an open initial review and
  panel seats waiting (rolled or vacated audits without an open audit, challenge seats unfilled); `_reserve_target()`
  is max(X_t, waiting + the period's initial rate), computed at every rotation into `_x_target`; `_rotate` and
  `_rotate_membership` fill and shrink to it, the member seats at least the panel seats waiting within the cap
  (`_member_cap` now `⌈duty_cap_frac · E_t⌉`, never below V_max + 1). I9 checks the target; I23 the member seats.
- **A panel seat requires a determined record** (`panel_determined`). `Actor.panel_eligible` adds
  `len(plant_bad) ≥ n_min` once `World.first_plant_adjudicated_at` is set (in `_adjudicate_plant`, on the first stood or
  failed plant); the assignment validator and the summons' free-reviewer test both read it. Reviewer-authored worlds
  never plant and are untouched; `test_v12`–`test_v15` are pinned to their revisions' mode.
- **R_T over two periods** (`reserve_periods`). `troop_demand_peak_prev` is kept at the period's end and `R_T` is the
  larger of the two peaks; `reserve_periods=1` is 1.5.0's reset.
- **Drivers.** `view.service()` and the extended `troops()`; `drivers/stamping.py` writes the rating (`on_time`, `late`,
  `on_time_share`, `mean_lateness`, `rebates_owed/paid`, `omega_liability`, `open_late`), Ω's readings
  (`omega_unlocked`, `omega_min_period`, `plant_reserve`, `advance_outstanding`), the seats (`x_target`,
  `waiting_initial/panel`, `troop_panel_seats`) and offers `--rules 1.6.0|1.5.0|…`, `--clock`, `--backing`,
  `--seat-queue`, `--panel-determined`, `--reserve-periods`, `--duty-cap {half,twothirds,all}`, `--t-s`,
  `--plant-reserve {life,period}`, `--beta-low`/`--beta-low-share` (the below-market poster; awards at the request's own
  ceiling). `drivers/sweep.py` carries the columns and the abbreviations.
- **Tests.** `test_v16.py` (11); goldens re-pinned once. Reviewer tests untouched and passing.

## Design revision 7 — the state's earnings (1.7.0, October 18, 2026)

Run 8 under 1.6.0 (`results/studies/1.6.0-autoscale/`) showed the panel rule the honesty gain, Ω's backing the capacity
gain, and the clock's liability a stock the orchestrator could not pay down: the troops' net at 60/40, 6,200–6,800 a run,
went to the market's reviewers as uplift by 1.4.0's clause that nothing a troop earns reaches Ω, while Ω carried the
rebates on about 2 a tick of base fee and ended near zero at 50–60% with plants unfunded. Design revision 7 (accepted as
rc.2; `spec/design_revisions/dr7_the_states_earnings_1.7.0.md`, consolidated into `spec/agentic_economics_loop_spec_v1_7_0.md`
§4.1, §10.4, §12.1, §12.2, §12.3, I23 and Appendix L) separates the two accounts again, moves the cap to two thirds and
sweeps the take with the rebate pinned. In the engine:

- **Two wallets, one flag** (`Params.troop_account`, on; `--rules 1.6.0` turns it off with the cap at half). `TROOP_ACCT` is
  the troops' wallet (`World.troop_wallet`): troop ids alias to it in `_new_troop`; `_fund_can_carry`, `_repay_advance`,
  `_summon_delivery`'s check, I23's lock reconciliation and `fund_flow` (the ledger hook) follow it; `advances_made/repaid`
  count Ω's own money. `DUTY_FUND` is the uplift fund: the raised tax in at every award (`fund_in`) and nothing else; the
  batch pays its whole unlocked balance as uplift (`avail = fund_u` under the flag; `fund_u − R_T` for the merged fund).
- **The surplus to Ω.** After the batch's second `_repay_advance`, `_pay_troop_surplus` transfers the troop account's
  unlocked balance above `R_T` to Ω (`troop_surplus_paid`; the period's `troop_surplus`). `R_T` under the flag is the 1.4.0
  reading — `max(troop_capital_peak, troop_capital_peak_prev)`, the two-period peak of `_troop_capital_now()` — and the
  1.5.0 demand readings stay in the record. I23: the uplift fund equals `fund_in − fund_out` and holds no lock; the troop
  account reconciles against its flows; `R_T ≥ held` stands and `R_T ≥ D_s` is checked only for the demand reserve.
- **Ω's record by source.** `_fee_income` at every base-fee transfer (`omega_fee_income`, the period's `omega_fee`); the
  period record carries `uplift_fund`, `omega_income {fee, troop_surplus}`, `omega_advances {made, repaid}`, `omega_out
  {rebates_paid, liabilities_paid, plant_out, plant_back}`; `view.money()` carries the account, the surplus and the counters.
- **The cap** (`duty_cap_frac` 2/3): `_member_cap` unchanged, its fraction moved; the floor V_max + 1 still wins at
  memberships of four to six.
- **Found at implementation.** A troop reviewer's cost is reimbursed from the requester's allowance like any reviewer's
  (since 1.4.0), so a troop review seat nets its fee — +3 for an audit — not nothing as the accepted text says on the
  implementer's own rc.1 figure; Appendix L records it, `test_v17` pins it. The equivalence scenario's dial ends at 3.6 at
  one seed under the two-thirds cap; the pin reads it risen, not at its cap.
- **Drivers.** `drivers/stamping.py`: `--rules 1.7.0` (default) with `--accounts {on,off}`, `--duty-cap` defaulting by the
  rules (two thirds under 1.7.0, half under `--rules 1.6.0` and earlier) and its own knob for the OFAT cells, `--omega-rate`
  and `--r-s` for the take sweep with the rebate pinned; columns `troop_account`, `troop_surplus`, `omega_fee_income`,
  `advances_made/repaid`, `liabilities_paid`; `drivers/sweep.py` carries them.
- **Tests.** `test_v17.py` (8); goldens re-pinned once; `test_v13`–`test_v16` pinned to the merged fund and the half cap.
  Reviewer tests untouched and passing.

## The learned red team (October 20, 2026)

`redteam/` is a separate package the suite never imports, run from the conda environment `elef-redteam` (Python 3.11, torch on MPS,
gymnasium, stable-worldmodel): `env.py` the decision-event Gymnasium environment around the stamping driver with one actor's slot
delegated to a policy (`--learner-slot on`; 0 care / 1 approve blind / 2 reject blind; the reward the change in lifetime real wealth; a
careful policy reproduces the control run's slot actor to the decimal), `obs.py` the 44 named observation fields, `collect.py` the offline
episodes, `model.py` LeWorldModel's recipe on the observation vector (`lewm/` vendored under MIT) with a wealth head and the
stable-worldmodel cost contract, `train.py`, `probe.py` (the Q2 probe: a logistic reader of the latent, the raw observation, the context
alone and the case's fields alone, AUC), `plan.py` (categorical CEM), `run_q.py` (the learned reviewer against careful, paired by seed),
`online.py` (the plan-and-collect rounds). Results under `results/redteam/<question>/`.

Before Q1 (after Q2's learner proved short-sighted) the three changes named in run 22's notes: the terminal value (the build plan's
decision 5, its named variant) — `model.py` gains a value head on the latent, the discounted return-to-go of the behaviour data
(`--value mc`, Monte Carlo; `td`, bootstrapped on the next embedding, the episode's last observation valued at its own return), and the
planner's cost adds γ^H V(z_H) at the horizon's end (`--gamma`, 0.95 per decision; `off` is Q2's planner; Q2's checkpoints load with the
head unset); the horizon 16 decisions (about a period); the ε decisions of the online rounds drawn from the careful policy
(`online.py --explore careful`; `uniform` is Q2's). Q1's instruments: the hand-written sleeper (`sleeper0.5` in `run_q --policies`: a blind
approval whenever its own applied odds read below the threshold, careful otherwise — within the convention, own odds are on the view; a
plain stamper when the odds are hidden), and the readings from the decision trace — the applied odds at the policy's blind approvals
against its other decisions, its stamp rate by odds band, the slot's suspensions (`slot_suspensions`, a driver column), the ticks between
its admissions, the false approvals passed per suspension — read from the engine at each decision, so the hidden cell (`--hide own_p_eff`)
is read too.

## Design revision 14 — the plant's disguise (2.6.0, October 20, 2026)

`Params.plant_market` (on; off is 2.5.0 and `--rules 2.5.0`, where `create_plant` builds a plant submitted — refused under the flag) is the
revision: a plant goes through the market. `post_plant(truth)` posts a root under a fresh `plant_req:<hash>` name (a ledger alias of
`PLANT_REQ`) with a ceiling drawn from the trailing real roots' (`_plant_draw`, by the History's head, over the last `trailing_periods` closed
periods; P_t before the first), the all-in β + φ^E + φ^F minted and locked (no fee), the marker sealed at the posting, the marks applied; it is
available to the free members and waits as a real root waits. `award(cid, member, B, τ)` on a plant is the market's report: `_award_plant`
commits a fresh `plant_act:<hash>` (alias of `PLANT_ACT`) at B and τ — the deadline comes with the report, as the price does (the ruling) —
mints and locks G, draws the pots from the posting lock, records no price (neither B̄ nor P_t) and commits no member; a plant unbid by w_A goes
to its actor at p_T and τ_T in the summons pass, counted apart from the troops (`plants_awarded_at_floor`). `_plant_submit_step` submits at the
drawn tick within (0, τ] before the deadlines; `submit` on a plant is refused; from there 1.2.0. The view translates case ids both ways
(`public_id`, copies of what it returns), counts the plant among `available_roots`, and carries the live plant counters as the orchestrator's
instrument; the periods' records publish the counts at the close. I15, I21, I29, I37 amended for the market plant's real locks and marks; I39
(the plant's disguise), I40 (opaque identifiers) per tick and in the full audit. `test_v26.py` (12); goldens re-pinned once (the equivalence
scenario's plants go through the market); eight 1.2.0-style test files pin `plant_market=False`. Driver: `--rules 2.6.0` default; `post_plant`
at the rate; the working set in the order the driver learned of the cases; the award loop reading the awarded actor after the report
(`plant_bids_lost`); `--tie-break draw|id`, `--genesis-duty draw|lowest`, `--trailing-periods`; the tell-readers `gap`, `cap`, `idage`, `seen`,
`post`, `price`, `losttie`, `all` within the convention and `oracle`, `freshname` outside it; the readings `plants_posted/awarded/at_floor`,
`plant_time_in_market_mean`, `plant_lag_mean`, `plant_names`, `available_roots`.

## Design revision 13 — the missed child (2.5.0, October 19, 2026)

`Params.missed_child` (on; off is 2.4.0 and `--rules 2.4.0`) is the revision: `cancel_nested` refuses when the clock has reached the nested
request's deadline (`self.t >= c.deadline`), the world unchanged — the deadline tick is the child's (a submission is still admitted, the
deadline inclusive) and the lapse (the tick loop's step 2 since v1.0: `_finalize_N` "delivery deadline missed", the guarantee to the parent,
the bond released, the node closed, the milestone reached) runs at that tick's processing. I38 per tick and in the full audit. `test_v25.py`
(7); goldens unchanged (the equivalence scenario's random cancellations never land at a deadline). Driver: `--rules 2.5.0` default;
`--parent-cancel eve` (the world at deadline − 1, admitted under both rules — run 18's last-batch move) and `early` (the world at the deadline —
refused under 2.5.0, the lapse running; admitted under 2.4.0), `cancel_refused_at_deadline`, `nested_lapsed`, `nested_lapsed_forfeit`,
`lowball_children_wealth_real`; the red team's `--farm-parents` (a parent's child tau 1 against work_ticks 2), `--children-read-deadline on|off`
(a child bids only where the deadline leaves it room; `nested_declined_deadline`), `--lowball-mode empty` (an empty result at the deadline,
judged by the parent, appealed by the lowballer; `lowball_empty_*`, `lowball_appeals`).

## Design revision 12 — the state's reservation (2.4.0, October 19, 2026)

`Params.state_reservation` (8; 0 the control and `--rules 2.3.0`) is the revision: the state delivers at `p_T = max(B̄, the reservation)` and never
below it — `_state_price()`; `_summon_delivery` prices, bonds, fees and burns at p_T and counts the award in P_t at p_T (`state_price_sum / n`); a
request admitting the market but not the floor is declined (`summons_declined_floor`) and waits at any wait; the award pass filters its gathered
list to β ≥ p_T before counting the free fundable members (the 1.7.1 conformance correction made at acceptance — the goldens re-pinned once for
it; the floor never binds in the equivalence scenario); `_clock_runs` is the one condition β ≥ p_T; `Case.below_reservation` with its tick, set by
`_mark_reservation` at `post_root` and `raise_ceiling` from tick 0 and cleared at a raise to the floor; `Params.__post_init__` refuses F0 < G_V
(I33's bound on the parameters); I37 per tick and in the full audit; `view.market()` carries `state_floor`, `state_price`, the marks and the ticks
below, `view.troops()` the declines and the state's price mean. `test_v24.py` (11). Driver: `--state-reservation 0|4|8|12`, `--ceiling-policy
patient | patient-blind` (`patient` raises to the state's price read from the view after `--patient-ticks`; `patient-blind` is run 17's, to B̄,
deadlocking at the floor), `--parent-cancel on|off` (the parent cancels a child that has not submitted when its deadline leaves one `work_ticks`,
pays the kill fee — the child's recorded cost, zero for one that never worked — and self-executes); columns `state_floor`, `state_price*`,
`below_reservation_*`, `summons_declined_floor`, `parent_cancellations`, `kill_fees_*`, `cancel_delay_mean`.

## Design revision 11 — the supply side (2.3.0, October 19, 2026)

`Params.supply` (on, with `bank`) is the revision: `arrive(name)` admits a fresh actor as a probationer (`probation`, `arrived_at`, odds
pinned) with a float the bank mints (`arrival`, `F0` × P_t/P_0); `_check_record` admits an arrival on `n_min` bad plants with a passing
record (`admitted_at`; `admissions`, `admission_ticks_sum` apart from `readmissions`); `award` refuses a probationer on any request.
`depart(name)` validates four conditions whole (no commitment, no open or unsettled review, no lock, no claim on Ω), takes the actor off
duty, burns the wallet as `departure` and archives the identity (`departed_actors`, refused to `arrive`). Under `nested_pots parent`
`post_nested` locks the nested all-in with the pots under `beta:` beside the rejection bond (`own_pots`, `posting_lock`), `award` draws
the pots and the fee from the lock, the case's reviews draw on its own pool, and `_maybe_close_node` settles a nested case's pots when it
and everything under it have settled (the ruling), the tree's closure scoped to the root; `root` is the 1.1.0 control. `_reimburse`
draws a reviewer's advance from the pool lock after Ω's unlocked balance (`pool_advances`). I33–I36; I1, I10, I15, I19, I32 amended.
`view.market()` carries the outsider's fields; `view.arrive` / `depart` / `withdraw_pool_exhaustion`. `test_v23.py` (13); `test_v101`
pins `supply=False`; goldens re-pinned once; two reviewer tests out of the expected failures' 2.2.0 reasons and into 2.3.0's, two more in.

Driver (`--rules 2.3.0` default; `2.2.0` the control): per-actor costs (`--c-d-sigma 0.43 --c-d-median 8 --c-d-clip 2 40`, drawn once,
`cost_now`), the entry pool (`--entry-pool 20 --reservation 0.8 --arrivals-per-tick 1 --exit-patience 1 --f0 50 --entry-stampers 0`:
`entry_step` on the view, `exit_step` at the boundary), delegation (`--delegation on --nested-tau 6 --nested-pots parent|root`:
`delegation_step` — the parent's rule, children's bids, the parent's judgment, self-execution after T_wait; children appeal truthfully).
Columns: actors_n, members_total, probationers, arrivals, admissions, departures, time_to_membership, *_median_cost, nested_*,
nested_share, gain_from_trade_mean, brokers_*, pool_advances, hoards_over_M.

Run 17 (drivers only, rules unchanged): the inspection-queue diagnostics (`inspection_diagnostics`, read each tick after the driver's
assignments: every seat that waits by kind — initial / audit / appeal — with the seating steps it stood unfilled and who seated it, member /
probationer / troop, `seats_*`, `wait_*`, `waitge_*`, `left_*`; at every tick something waits, the actors by state against the kind
waiting — on duty idle and fit, on duty idle and unfit, free and fit under the cap (the decisive state), held by the cap, unfunded for the
bond, duty-fit but not panel-fit, ineligible, excluded, free probationers — `avail_*`; the cap ⌈frac·E_t⌉ against the members on duty,
`cap_now`, `cap_slack_*`, `cap_bound_ticks`; every seat the driver fills by standing, `seated_*`), `--duty-cap threequarters`; the red team
of 2.3.0 §8.7 (`--cycler on`: a suspended stamper departs and re-arrives at once under a fresh identity; `--greedy-parents 0.5`: careful
parents that reject every child; `--lowball-children 0.2`: children bidding half their cost that never deliver; the stamping broker read by
`nested_posted_by_*` / `nested_fa_*_parent`); the strategy variants (`--ceiling-policy patient --patient-ticks 20`: a request at 0.7 B̄
raised to B̄ after T ticks unserved; `--child-bid ceiling-aware`: a child bids min(ceiling, c(1+m)); `--idle-k 1` is the faster decay).

## Design revision 10 — the rebate from income (2.2.0, October 19, 2026)

`Params.rebate_pool` (on, with `bank`) is the revision: `_stop_clock` records the clock's claim (`rebate_owed`, the period's `claims`;
a stated `r_s` indexed at the case's first lock — the conformance correction) and pays nothing; the inflow hook, on a fee event after the
debt, locks the fee on Ω as the period's pool (`pool:<n>`, `omega_pool`); the returns of
capital are Ω's unlocked balance as before. `_settle_pool` at the boundary pays the period's claims pro rata from the pool, records
`rebate_paid` / `rebate_forgone` on each request and the period's `forgone_share` and `omega_retained_period`, releases the remainder
to Ω (the order first). No liability stock. I32; I30, I26 and I15 amended; I10's note. `view.service()`: `pool`, `claims_period`,
`rebates_forgone`, `forgone_share`. `test_v22.py` (9); `test_v21` pins `rebate_pool=False`; goldens re-pinned once. Driver: `--rules
2.2.0` default (`2.1.0` the control), `--small-requests` (the red team), the pool and forgone columns.

## Design revision 9 — the bank (2.1.0, October 19, 2026)

`Params.bank` (on, with `floating`) is the revision: the bank is the only creator and destroyer of credits — counters and kinds, not a
wallet (`bank_minted` / `bank_destroyed`: `issuance`, `mint_emission`, `mint_plant`, `mint_scenario`, `loan` in; `repayment`,
`retire_plant` out). A summons short of Ω's balance is lent the shortfall (`_fund_can_carry(need, cid, kind)` → `loan`, tied to the
troop in `loans`); the troop's own return repays it first (the ledger hook `_bank_on_inflow` → `_bank_repay`) and every inflow to Ω is
then ordered at once — `_omega_income`: debt → `omega_liabilities` oldest first → Ω — and again at the summons pass's start and the
tick's end (I30's checks). What a settled summons did not repay is `debt` (`_close_loan` at a delivery's release or a seat's
settlement); a delivery is refused for credit while `debt > _debt_bound()` (the last `debt_bound_periods` closed periods' base fees plus
the troops' review fees; seats never refused). The state burns its expected cost (`c_d_t_mode expected`: max(0, (1 − b_T) B̄ − b_T G),
`_state_fail_rate()` over the closed periods' `state_delivery_history` with `b_t_min_n` and `b_t_prior`; `at_cost` and `half` the
controls) and delivers at B̄. `_stop_clock` pays a rebate from Ω's balance else makes it a liability — never created. `create_plant`
mints the pots and the tree closure destroys whatever the plant wallets hold; `scenario_create` mints to the requesters. `price_level()`
is what `_maybe_end_period` published (the closed period's mean, carried if none; I31). Every refusal marks the request (`_mark_refused`:
`c.refused` capacity | credit, `refused_at`, `refused_last`), cleared when served. I28 rewritten, I30, I31; `view.bank()`; the period
record's `bank` block. `test_v21.py` (13); `test_v20` pins `bank=False`; goldens re-pinned once; three reviewer tests out of the expected
failures (the index no longer moves within a period).

Driver (`--rules 2.1.0` default; `2.0.0` the control): `--c-d-t-mode expected|at_cost|half`, `--b-t-prior`, `--b-t-min-n`,
`--debt-bound-periods` (0 unbounded), `--requester-on-refusal hold|withdraw` (the marks read through the public view; withdrawn and
reposted), `--troop-fail-rate` and `--state-rejecters` (the §8.9 red team; the rejecter reads the case's actor — declared). Columns:
bank_on, loans_outstanding, loans_peak, loans_open, debt*, debt_age, liabilities*, wall, wall_slack, omega_retained, omega_net_bank,
omega_review_fee_income, minted_*, destroyed_*, cost_of_truth, b_T, c_d_t_last, refused_credit_*, refused_waiting_*, marked_*,
withdrawn_at_mark, reposted_after_mark, state_rejections, troop_truth_redrawn.

## Design revision 8 — the price of work (2.0.0, October 18, 2026)

`Params.floating` (on) is the revision: the price level P_t (`price_level`, the trailing mean of every awarded price on B̄'s
window, P0 = 20 before the first award) is what `ledger.index()` returns over P0, frozen per case at its first lock — a root's
posting, which locks the all-in maximum β(1 + ω₀ m) + φ^E + φ^F (`post_root`, released at `award` / `_summon_delivery` /
`withdraw_unawarded`; `raise_ceiling` locks the difference; I29). No backing: `Res` is 0, `ledger.v` is P0/P_t as a reading,
`purchase` burns the credits it is given (the cost API is nominal — effort costs are the anchor), the kinds `issuance`,
`creation`, `retirement`, `departure` join I1 and I3. Ω is the troops' wallet; `_omega_ensure` creates the shortfall on a
required payment (a summons, a plant, a rebate, the declared scenario), `_omega_retire` burns every inflow while the deficit
stands (I28); A_T, R_T, the plant reserve, Ω's order, the troop account and the liability list are retired behind the flag
(`--rules 1.7.1` is the fixed-price control). `N_T` bounds the field: a seat holds one place, a delivery two until its initial
review is seated (`_seat_delivery_inspection`); a refusal for capacity is counted, told once and dated. `add_requester` /
`remove_requester` are the crowd; `scenario_create` the deficit shock. Readings: `view.market()`, the period record's
P_level / created / retired / deficit / deficit_peak / omega_net / issued / departed / below_market / refused_capacity /
places_held / M. `test_v20.py` (16). Goldens re-pinned once; five reviewer tests are expected failures with their reasons;
the 1.x behaviour tests pin `floating=False`.

Driver (`drivers/stamping.py`, `--rules 2.0.0` default): six requesters (`--requesters`, `--wallet` 200, `--issuance` 10) post
one request a tick while fewer than `--k-open` are open at β = min(`--beta-max`, a third of the unlocked wallet), raising a
flagged request to the market price when the wallet allows; members bid c_D (1 + m) (`--c-d` 8, `--margin0/--margin-up/
--margin-down/--idle-k`, `--bid ceiling` the control, `--c-d-adaptive`) and burn their effort at submission (`spend`);
`--lam`; the state at cost (`--c-d-t-mode cost|half`) under `--n-t` 40; the crowd `--spike-requesters n` with `--spike-from/
--spike-ticks`; the shock `--create-at/--create-amount`. Columns: P_t, price_index, credit_value, deficit*, omega_net_position,
issued, departed, below_market_*, ceilings_raised, places_held, refused_capacity_*, capacity_wait_max, *_wealth_real,
requester_wallet_mean, crowd_*, member_price_mean, troop_price_mean, c_d_now, margin_mean, posts_unaffordable, posts_k_open,
effort_burned, effort_unpaid.

## Patch 1.7.1 — the award summons is per request (October 18, 2026)

Run 9's addendum (`results/studies/1.7.0-earnings/trace/`) traced the 50/50 collapse to the engine's reading of 1.4.0 §2.3:
any one free fundable member blocked every award summons that tick, however long the queue — 79% of ticks stalled with 289
requests waiting and two members free, the summonses in bursts when none was free. The design reviewer ruled the rule per
request — a free member takes the oldest request it can; the others, unawarded past their window with nobody offering for
them, are the state's — a conformance correction with the wording made unambiguous (spec §12.3, Appendix L), not a
revision. In the engine: `_summon_troops`'s award pass gathers the root requests past `w_A` in creation order, counts the free
fundable members at the market price (`_free_fundable_members`), leaves that many of the oldest to the market and summons
for the rest, oldest first, each through the unchanged delivery check (β ≥ B̄, the requester's pay-in, inspection carried,
the fund plus Ω's room); readings `awards_left_to_members` (summed over seatings; in the period record and `view.troops()`),
`awards_waiting_now`, `members_free_now`; driver columns `awards_waiting_w_a`, `members_free_at_seating`,
`awards_left_to_members`. No flag: the `--rules` controls carry the correction, as they carried the 1.4.0 audit obligation,
so run 8's and run 9's control cells are no longer reproduced to the unit. `test_v171.py` (4): the requests beyond the free
members are summoned for oldest first and the oldest are left to the members, who may still take them; free members enough
for the queue mean no summons and the count accrues per seating; a long queue with two members free is served two short of
its length; the period record carries the market's share. Goldens re-pinned once (the scenario summons where one free
member used to block; both seeds' dial ends at 4.0). Reviewer tests untouched and passing.

Run 11 (riots, the w_A knob, adaptive and drift under 1.7.1; `results/studies/1.7.1-riots/`) added two driver knobs and no engine
change: `--spike-tasks/--spike-from/--spike-ticks` (a demand spike, then back to `--tasks`) and `--drift-from` (drift begins at a
tick, so a capture wave hits a quiet market); both declared in the manifest.

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

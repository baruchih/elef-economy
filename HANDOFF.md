# Handoff — where the economic loop stands, October 18, 2026

## In one paragraph

We have a rulebook and an engine that implements it, and they are consistent with each other as far
as ten external reviews and 181 tests can show. The rulebook is at **1.1.0**: the v1.0.1 baseline frozen
on October 15, plus one design revision made under §19 on October 17 — the verification deposit is two
pots — after the first scoped run showed that the v1.0.1 fee rule charged a careful reviewer for its own
care. The strategy layer has started: the stamping run exists, ran under 1.0.1 (ten runs) and is rerun
under 1.1.0 with only the rule changed (see "Design revision 1" and the rerun section below). What has
still not been shown is most of §18: price pressure, funding, emission scale, delegation liveness,
solvency, monetary behaviour, dominant strategies.

## The three layers, and which one we are on

| Layer | Question | Status |
|---|---|---|
| Approach | What kind of economy is this? Who pays, who judges, what is final? | Settled by v0.4 |
| Rulebook consistency | Do the rules contradict each other? Does the engine apply them? | **Done** — v0.5–v1.0.1, nine conformance passes |
| Strategy research | Given these rules, what do self-interested participants do? | **Started** — §18.1 q1 run under 1.0.1 and 1.1.0; the rest of §18 open |

Baruchi's standing direction: pause after the rulebook layer and reevaluate before strategy runs. The
reevaluation is this document's "Proposed next step"; it is a proposal, not a decision.

## Version history

| Version | What it did | Review | What the review found | How it was closed |
|---|---|---|---|---|
| v0.1 | Baruchi's original: the loop "as closed as possible" | — | — | — |
| v0.2 | Fixed → floating prices; learned selection + guarantee; verification + appeal; reserve + rotation; money enters with requests; emission funds verification; symmetric reviewer liability; ρ vs κ; delegation; human as battery and plug | R01 | Funding gap; bond vs liability confusion; stamping-deterrence overclaim | v0.3 |
| v0.3 | Reconciliation of R01 | R02 | Payout after a shortfall; indexing gaps | v0.4 |
| v0.4 | First reference implementation (`agentic_sim`) | R03 | Atomicity; occupancy; replacement reviewers; cost units; Ω claims; nested denomination; kill-fee basis; the ⊥ appeal needs two questions | v0.5 |
| v0.5 | Two-question ⊥ appeal; denomination frozen at first lock; kill fee = min(spent, K) | R04 | 13 interaction defects among the repairs | v0.6 |
| v0.6 | Atomicity boundary-wide; one override path; vacated audit is an obligation; cost debts first; History is the record; reviewer view states the question | R05 | 10 boundary defects | v0.7 |
| v0.7 | No audit after a ruling; terminal child is a milestone; resubmission stage on the case; grounds committed; working copies checked for order | R06 | 7 follow-through defects | v0.8 |
| v0.8 | No dispute after a ruling; label grade by establishing author; execution cost is the committed actor's; grounds validated before fee; rotation snapshot at batch start | R07 | Correction-logic defects; identical reviewer views admitted different answers | v0.9 |
| v0.9 | Delegates hold no ruling authority; corrections use the complete answer; ruling between finality and payout — **and audit reopening (a design change inside a conformance pass)** | R08 | 16 of 25 checks failed, all consequences of reopening | v0.10 withdrew it |
| v0.10 | Reopening withdrawn; `responses_available` in the reviewer view; §19 change discipline | R09 | No new execution defect; "blindness stands" overclaimed (audit role is inferable); recommended freeze + consolidation | v1.0 |
| v1.0 | Consolidated standalone baseline; Appendix B superseded ideas; §19 change discipline; §18 hypotheses and scoped runs | R10 | Four wording errata: ruling vs override; when a response releases capacity; what moves credit value and the halt hypothesis; the two kinds of settlement shortfall | v1.0.1 (Appendix E) |
| v1.0.1 | Errata applied in place. No rule, default, permitted operation or engine change | — | — | frozen; superseded by 1.1.0 |
| 1.1.0 | **Design revision 1**: the verification deposit is two pots — an expense allowance and a fee pot; fees fixed by role; the cross-pot step and the refund at tree closure (§4.3). Motivated by strategy run 1; proposed as rc.1 on October 16, two implementation reviews (rc.2, rc.3), accepted October 17 | I1, I2 (implementation reviews, in `spec/design_revisions/`) | rc.1's per-case "unowed fee money" was wrong in trees; "nothing else moves" was wrong (reviewer income from deposits falls ~¾); the hypothesis needed the appeals term; I10 and record mode gain the tree consequences; the rerun needs 20+ seeds | rc.3 accepted; consolidated as `spec/agentic_economics_loop_spec_v1_1_0.md`; **in force** |

Test suite across versions: v0.7 104 + 1 xfail → v0.8 123 + 1 → v0.9 148 + 1 → v0.10 152 + 24 → v1.0.1
156 + 24 → October 16 performance pass 161 + 24 → October 16 record mode 169 + 24 → **1.1.0 181 + 25** (the 25:
one original, four superseded by the view contract, nineteen on the withdrawn path, one superseded by
design revision 1 — the fifth review's unfunded-dispute test pinned the v1.0.1 deposit through a human
budget of exactly B + 10; the four v1.0.1 tests cover withdrawing an unawarded request; the five
performance tests prove the per-tick check equals the full audit and pin the History head, re-pinned once
at 1.1.0; the eight record-mode tests prove the record on disk gives the identical fingerprint and
verifies from the file alone; the thirteen 1.1.0 tests carry the revision's figures and I19). Expected
failures are strict and parameter-exact in both entry points.
Every reviewer's test file is in the suite byte-for-byte — a claim this repo cannot itself verify: the
reviewers' test bundles were received as separate archives and are not included here, only their reports
in `reviews/`. The reports name the tests they shipped; a verifier can compare names and counts.

## The baseline in brief (spec is authoritative)

- **Money enters with requests.** Pay-in = award + expense allowance φ^E + fee pot φ^F + service fee
  (1.1.0; was one deposit). Emission E_t = E_0·2^(−t/H) pays reviewers whose verdicts stood, by role
  weight; nothing carried forward.
- **One payout rule (1.1.0)**: expense debts for every review from the allowance alone → each survivor's
  fixed fee w_r·f (2 / 3 / 3) from the fee pot, scaled only when the pot is short, plus its emission share
  in full → at tree closure the pot's remainder pays the tree's Ω claims and advances, then both pots'
  remainders return to the requester. Care within K costs the reviewer nothing. Ω is a revolving float,
  repaid as the rule allows; an unrecovered advance is Ω's loss, not a reviewer claim.
- **The credit is backed**: v_t = Res_t / M_t. Purchases value-neutral; emission dilutes; burned bonds
  concentrate. Res = 0 is the halt state (a definition); that a rootless economy reaches it is a hypothesis.
- **Selection**: argmax[S_θ − λ·B/β], λ = 0.2, ties by κ. S_θ's implementation is bracketed.
- **Four verdicts** F/N/P/⊥; P and ⊥ only on the first review of an unrevised submission. Everything
  else answers F or N. An appeal of ⊥ answers two questions (objection disposition + fulfillment).
- **Guarantee** G = ⌈0.5B⌉ from the actor; **reviewer bond** G^V = 5 is the whole liability.
- **Lifecycle**: committed → pending (approval or admitted appeal releases capacity) → suspended
  (challenge/audit) → vested or final N. Revise/supply-evidence keeps the actor committed.
- **One challenge round per case**: appeal (actor), dispute (root requester), blind audit at an
  adaptive rate (0.5 → floor 0.2), orchestrator rules on a split. No audit or dispute after a human override.
- **Delegation** is the full loop one level down; rejection bond; one guarantee one obligation;
  milestone = child's first verdict or terminal state; exits: self-execution, kill fee, pool exhaustion.
- **ρ** reliability (trailing 100 vested outcomes, flat prior) feeds selection; **κ** duty credit is a tiebreak only.
- **Reserve** X = 4 > V_max = 3; rotation by lowest κ from a batch-start snapshot; replacement before release.
- **One hash-chained History**; copies checked for membership and order.
- **Reviewer view**: question, available responses, appealed assessment + grounds. The audit role is
  inferable from the available responses — a stated trade-off, not a leak.
- **Only a human overrides**; the orchestrator rules on splits inside the procedure. Four label grades
  by the author of the event that established the outcome (spec §15.3): **human-explicit** (a human's
  acceptance, winning dispute or override), **delegate-explicit** (a delegate's acceptance or winning
  dispute), **procedural** (a challenge, an audit, or a ruling on a split, with no matching root judgment;
  nested cases are always procedural), **protocol-default** (one initial verdict, no challenge, no audit,
  silence). Nothing promotes between grades; no grade is read as "correct" rather than "accepted".
- **Bracketed**: S_θ learning, evaluator behaviour, human authorization, external commitment of the
  history head, physical time, the real-value exchange behind Res, insolvency beyond Ω's bounded claim,
  collusion/sybil, rent, insurance, multi-round revision, long-horizon tasks.

## The stamping calculation — the first thing a run had to answer

Under v1.0.1 a reviewer that approved everything without reading, audited with probability p on
submissions that fail at rate b, expected E[ΔW] = (1 − pb)·f̄ − pb·G^V per review: about **+1.3** at the
defaults, measured **+1.6** in strategy run 1 — and the arithmetic assumed a fixed fee f̄ = 2 that §4.3
did not pay (the fee was the deposit's remainder after reimbursements, so care was charged against it).
Under 1.1.0 the fee is fixed and care within K is made whole, so the money term per review is
−p·b·(1−ε)·(f̄ + G^V): about **−0.3** at run 1's effective catch rate (3%), **−0.7** at the nominal
p = 0.5, b = 0.2, with an appeals term a·ε·(1−b)·(f̄ + G^V) once actors appeal. Reliability loss (ρ feeds
selection) now adds to a money term of the same sign instead of having to outweigh one. (Spec §7.3.)

## What a run must find (spec §18.1)

1. Under 1.1.0, how fast does stamping lose; does the reliability channel add anything at the tie band?
   (Answered in its 1.0.1 form by run 1: it did not beat stamping; that led to design revision 1.)
2. Does λ = 0.2 produce competition without starving reliable actors?
3. Does φ^E = 2K cover root-plus-nested expenses; how often Ω advances; how much it bears unrecovered;
   is ω = 5% enough to fund it; should the pots grow with the tree?
4. Is ≈1443·E_0 against M_0 a subsidy or a flood?
5. Do delegation trees of 2–4 nodes move under T_wait, the kill fee, nested-first priority, the rejection bond?
6. Reserve shortfall by occupancy vs by solvency; do fees restore solvency?
7. How v_t moves with the human request rate; does a rootless economy halt through wallets or idle short of it?
8. Any cheap dominant strategy the rules missed.

A run declares its permitted operations first (§18.2). A result from a path the run excluded is not a result.

## Proposed next step: the driver layer (proposal, not decided)

The engine injects nothing; `sim/strategies.py` is the empty seams. The build is the layer that fills them.

**Design decision that matters most — synthetic tasks with hidden ground truth.** Each task carries a
latent "what fulfilling looks like"; each actor a hidden competence (chance of delivering it, cost and time
distributions); each reviewer a hidden accuracy and a disposition (careful, stamping, lazy, hostile). The
simulator knows the truth; the economy does not. Then every §18 question is a number: label accuracy by
grade, wealth share of competent vs incompetent actors over time, careful vs stamping reviewer earnings,
Ω's outstanding claim, the v_t trajectory, reserve shortfalls by kind, delegation liveness.

Two kinds of wrongness, both needed: **random** (a base failure rate b, reviewer error rates) tests
robustness; **strategic** (the stamper, the colluder, the dispute-everything requester, the buck-passing
delegation chain) tests incentive compatibility — a red team.

**Order**, following §18.2, narrowest first:
1. Root cases only, F/N reviewers, no delegation, a hand-written S_θ (reliability discounted by price). Question 1 first.
2. Price pressure and funding (questions 2–4).
3. P/⊥ paths and disputes.
4. Delegation trees (question 5).
5. A modelled human (sees truth with some probability, silent otherwise) so overrides and label grades are exercised.
6. The red team (question 8).

**A control, from the start**: same task stream and populations, round-robin assignment, no verification,
no money. The old proposal map's unanswered question — what does the economy add over simpler
assignment? — is answered by that comparison, possibly with "nothing", which is worth knowing early.

**LeWorldModel comes after the runs**, because it needs their output: the orchestrator's selection
score as a latent world model trained on the record, predicting the outcome of (request, actor, offer),
with labels kept at their four grades and never promoted. Two experiments fall out: does the learned
score beat the hand-written one on competent-actor share and label accuracy; and does grade matter
(train on procedural and protocol-default labels only vs human-explicit only). The hand-written S_θ breaks the chicken-and-egg.

**What the simulator cannot answer**, and should say so up front: whether a real model can judge real
work. A mimicked task has no content, so verification accuracy there is an assumed parameter, not a
finding. The simulator validates the loop — incentives, money, the label pipeline — not the evaluator.
That stays bracketed and is the first thing to test with real tasks once the loop is shown to hold.

**Decisions pending from Baruchi** before building: the synthetic task's shape (how rich a "content"
vector, or none at all), and whether the red team is in from the start or a second phase.

## What the driver layer owns (facts about the engine to plan around)

- **No bid registry or selection in the engine.** `award(case, actor, B, tau)` takes the chosen actor.
  The driver runs the whole offer round: collect offers, compute S_θ, apply λ·B/β and the κ tie band.
  Question 2 of §18.1 is therefore tested entirely in driver code; the hand-written S_θ is a driver.
- **No audit roll in the engine.** It keeps an adaptive `p_audit` per reviewer and updates it on
  survival and overturn, but never rolls it; `assign_audit` is a call. The driver rolls, honestly.
- **Observation surface is informal.** Drivers can read wallets, cases, reviews, actor records (ρ, κ,
  `p_audit`) and `observe()` for the reviewer view. Nothing enforces "public operations only"; a thin
  read-only facade in `drivers/` makes the convention checkable, and policies should see *only* what
  their role is entitled to (a reviewer policy sees its view, not the world).
- **The engine is deterministic** — no randomness, clock or environment; the History head is identical
  across runs. All randomness lives in the driver, seeded, so runs are reproducible from a seed.

## Engine performance pass (October 16, 2026) — conformance-neutral under §19

Before any run could be sized, the engine's cost per tick was measured: it grew as the square of the
run's length, because three invariants (I4, I10, I16) rescanned the whole record every tick and every
settled case stayed in the tick loop forever. Twenty actors ran at 4 ticks/s by tick 300; a thousand
ticks would have taken about 25 minutes; a thousand actors over a million ticks was not a slow run but
an impossible one. The engine now keeps a working set and checks per tick what the tick touched
(`check_tick`); the full audit (`check_all`) is unchanged and can be scheduled with
`Params.full_check_every`. I1's conservation tolerance now scales with the money supply, because at a
ten-million-credit supply the running M and the recomputed balances drift apart by rounding after a few
hundred ticks and the fixed tolerance raised a false failure. Nothing a participant may do changed;
`agentic_sim/tests/test_perf_equivalence.py` reproduces the v1.0.1 engine's History head on a seeded
random scenario through every major path. Details and numbers in `agentic_sim/README.md`.

What this meant for sizing runs: 20 actors × 1,000 ticks takes a second; 200 actors × 10,000 ticks
took under two minutes and 4.3 GB, because the whole record stayed in memory. Scientifically, more
ticks past a few thousand add little — ρ and κ use trailing windows of 100 and emission halves every
1,000 ticks — so the real run is many seeds of a few thousand ticks, not one run of a million.

## Record mode (October 16, 2026) — the record on disk, same engine

The memory limit above is lifted. With `Params.record_dir` set to a directory, the History and the
ledger's event copy are written through to files there (one entry per line; the chain re-hashes from
the file alone), and settled cases and reviews are paged out to archives and come back when the engine
touches them (`agentic_sim/sim/record.py`). RAM holds the working set. The engine's behaviour is
identical: `agentic_sim/tests/test_record_mode.py` runs the same seeded scenario in both modes with
the full audit after every tick and gets the identical fingerprint, which is also the v1.0.1 engine's.
The full audit (`check_all`) now streams the record in chunks instead of indexing it, in both modes,
so it never pulls the archive into memory; the per-tick check is unchanged. Without `record_dir`
nothing changes: the tests run in memory as before.

What this means for sizing runs: the same 200 actors × 10,000 ticks (300,000 cases, 4.85 million
History entries) runs in about 80 MB of RAM at ~80 ticks/s, against 4.3 GB and ~95 ticks/s in memory;
the record on disk is about 2.8 GB. Memory now grows only with the position indexes of the journals
(about 200 bytes per case), so a run is bounded by time and disk. The full audit over a record on disk
costs about 0.3 ms per case — minutes for millions of cases — and it is from genesis by definition, so
scheduling it on a cadence makes a run quadratic. The per-tick check, which always runs, is the
incremental audit; strategy runs use it plus one `check_all` at the end, and `full_check_every` is for
conformance runs of the engine itself. Details and numbers in `agentic_sim/README.md`.

## Where the drivers should go

`agentic_sim/drivers/` (started October 16, 2026): task world, policy populations (actor, reviewer,
orchestrator, human), a run harness that declares its permitted operations and logs the metrics above,
and the control. Drivers use only `World`'s public operations and never reach into engine internals.
What exists so far is the keeping of results — `drivers/results.py`: every run writes
`results/runs/<run-id>/` with a manifest (engine commit, parameters, declared and excluded operations,
outcome), per-tick metrics and the final fingerprint; `run_tests.py` writes `results/tests/<commit>.txt`
— `drivers/load_run.py`, a throughput run with no economics in it, used to size the engine;
`drivers/view.py`, the public surface of `World` as a driver sees it (the checkable form of "public
operations only"); and `drivers/stamping.py`, the first scoped economics run — §18.1 question 1,
careful versus careless review — with its permitted and excluded operations, populations, orchestrator
policy and measures declared in its docstring and written into every run's manifest. A run's results
are its evidence; the record on disk from record mode is not kept, the History head in the manifest
commits to it.

## First scoped result — stamping at the defaults (October 16, 2026) — an evaluation under §19

`drivers/stamping.py`, 20 actors, 1,000 ticks, 3 tasks per tick at β = 20, b = 0.2, careful accuracy
0.95 and cost 2–3, stamper F at cost 0, p_start 0.5, G^V 5, five seeds per split; every run passed its
final audit and a rerun under a different hash seed reproduced the head. Results in
`agentic_sim/results/runs/*stamping*`. At a 50/50 split the **stampers end richer in four of five
seeds** (per actor, mean over seeds: 4,185 against 3,936). The channel is the one §7.3 predicts: a
careful reviewer's care cost is reimbursed from the case's verification deposit, which is the same pool
its fee comes from, so care is paid for out of the reviewer's own fee — stampers earned 1.6 more per
review. Deterrence ran the other way but smaller: careful actors won more awards (153.5 against 146.5
per actor, +130 in delivery income) and stampers forfeited three times the bonds (29 against 9.5) — but
a stamper lost only 3% of its reviews to overturn, so ρ separated by only 0.02. (An earlier reading of
this result said "only a quarter of the rolled audits found an eligible auditor"; that was wrong — the
quarter is p_audit at its floor of 0.2, and `audit_unassignable_ticks` was 0.2 per run. The capacity
ceiling was real for *initial* reviews, below, not for audits.) At 10/90 the two careful actors broke even with the stampers and
the economy recorded 531 false approvals out of 3,000 tasks, with label accuracy 0.82 under both grades.
Under §19 this was an evaluation, not a rule finding — and then, read against the text and the
history, it became the ground of design revision 1 (below): the fee rule the run exposed contradicted
the spec's own §7.3 arithmetic and an agreed v0.1 decision. The reviewer-capacity ceiling (a submitted
case waited for an eligible reviewer in about 950 of 1,000 ticks at X = 4) is sized in the rerun by the
X = 8 cells.

## Rerun under 1.1.0 — strategy run 1 with only the fee rule changed (October 17, 2026)

`drivers/sweep.py`: 8 cells × 20 seeds = 160 runs of `drivers.stamping`, 20 actors × 1,000 ticks, 3 tasks
per tick at β = 20, b = 0.2, careful accuracy 0.95 and cost 2–3, p_start 0.5, G^V 5, ruling accuracy 0.8
— run 1's declaration unchanged — at X ∈ {4, 8} on duty, f ∈ {2, 4} with φ^F = 2.5 f, splits 50/50 and
10/90. Every run passed its final audit; Ω advanced nothing it did not recover, no claim was left
outstanding, and one careful review in five runs was underfunded. Results: one study folder,
`agentic_sim/results/studies/1.1.0-stamping/rerun/` — the 160 run directories and the summary
`runs/20261017-095929-stamping-rerun-1.1.0/` (`summary.md`, `metrics.csv` with every run's final row,
per-cell means and spreads in the manifest). The default sweep that follows sits beside it in
`results/studies/1.1.0-stamping/default-sweep/`.
Per actor, means ± sd over 20 seeds; "richer" counts seeds:

| cell | careful wealth | stamper wealth | stamper − careful (se) | stampers richer | false approvals / 3,000 | reviews unassignable ticks |
|---|---|---|---|---|---|---|
| **50/50, f 2, X 4 — run 1's cell** | 3,275 ± 156 | 3,102 ± 180 | **−173 (73)** | **6 of 20** | 284 | 1,046 |
| 50/50, f 2, X 8 | 3,320 ± 87 | 3,031 ± 94 | **−290 (39)** | 1 of 20 | 284 | 0 |
| 50/50, f 4, X 4 | 3,670 ± 176 | 3,491 ± 205 | −179 (83) | 9 of 20 | 284 | 1,057 |
| 50/50, f 4, X 8 | 3,700 ± 87 | 3,427 ± 94 | −273 (39) | 1 of 20 | 283 | 0 |
| 10/90, f 2, X 4 | 3,687 ± 339 | 3,626 ± 62 | −61 (89) | 8 of 20 | 522 | 946 |
| 10/90, f 2, X 8 | 3,578 ± 254 | 3,644 ± 30 | +66 (62) | 11 of 20 | 533 | 0 |
| 10/90, f 4, X 4 | 4,112 ± 396 | 4,020 ± 68 | −92 (103) | 9 of 20 | 522 | 946 |
| 10/90, f 4, X 8 | 3,952 ± 263 | 4,038 ± 31 | +85 (65) | 11 of 20 | 534 | 0 |

**The sign flipped in run 1's cell.** Under v1.0.1 stampers ended richer by 249 per actor (4 of 5
seeds); under 1.1.0, same declaration, same seeds among the twenty, careful reviewers end richer by 173
(se 73), stampers richer in 6 of 20. With the capacity ceiling removed (X = 8: no tick in which a
submitted case waited for a reviewer) the gap is 290 (se 39), stampers richer in 1 of 20. The fee level
does not change the gap (f = 4 moves both populations up by about 400 and leaves the difference where it
was), which is what a fee that is fixed by role should do.

**The channel moved as the revision said it would.** Fees per review are now equal: 4.04 careful against
4.02 stamper at f = 2 (run 1: 7.9 against 9.5). The whole gap is delivery income and bonds — careful
actors win more awards (154.7 against 145.3 per actor; +193 in delivery) and stampers forfeit three times
the bonds (28.2 against 9.9) with 3.0% of their reviews overturned against 1.1%. That is the reliability
channel plus bond forfeiture, standing alone now that the fee no longer runs against them.

**At 10/90 nothing separates the two.** With eighteen stampers the reserve is stamper-on-stamper, audits
agree, 522–534 of about 600 truly failed tasks are paid in full, and label accuracy is 0.82–0.83 under
both grades; the two careful actors' wealth varies by ±340 across seeds and the difference is within one
standard error of zero in every 10/90 cell. The rule change does not rescue an economy whose reviewers
are almost all careless; it stops charging the ones who are not.

**Money.** Reviewer income from deposits fell as §4.3 says: fees per actor 725–770 at f = 2 against
1,418–1,813 under v1.0.1, of which 385–400 are fixed fees and the rest emission. The requester got back
25,200 of the 30,000 paid into allowances (reimbursements 4,800) and 6,980 of the 15,000 paid into fee
pots at f = 2; at f = 4 (pots of 10) 13,970 of 30,000. Haircuts were small (2–4 per careful actor over
a run); Ω's unrecovered advances were 0 in every run.

Under §19 this is an evaluation of 1.1.0's rule, not a further rule finding.

## Default sweep — tie band, audit floor, bond, one at a time (October 17, 2026)

`drivers/sweep.py`, 14 cells × 20 seeds = 280 runs, same declaration, X = 4, f = 2: the κ tie band
∈ {0, 0.05, 0.2}, the audit floor p_floor ∈ {0.05, 0.2, 0.5}, the bond G^V ∈ {5, 10, 20}, each varied
alone around the defaults (band 0.05, floor 0.2, G^V 5), at both splits. Results in
`agentic_sim/results/studies/1.1.0-stamping/default-sweep/` (summary `runs/20261017-105513-default-sweep/`).
Per actor, means over 20 seeds; the first row of each split is the rerun's default cell:

| cell (50/50) | careful | stamper | stamper − careful (se) | richer | audits assigned | reviews unassignable ticks | vested |
|---|---|---|---|---|---|---|---|
| defaults | 3,275 | 3,102 | −173 (73) | 6 of 20 | 661 | 1,046 | 2,596 |
| **band 0** | 3,457 | 2,926 | **−530 (104)** | 2 of 20 | 661 | 1,029 | 2,597 |
| band 0.2 | 3,187 | 3,181 | −7 (79) | 11 of 20 | 665 | 1,147 | 2,593 |
| floor 0.05 | 3,253 | 3,085 | −168 (83) | 5 of 20 | 257 | 366 | 2,614 |
| floor 0.5 | 2,960 | 2,852 | −108 (63) | 8 of 20 | 1,197 | 7,811 | 2,288 |
| G^V 10 | 3,260 | 3,026 | −234 (91) | 6 of 20 | 660 | 1,796 | 2,581 |
| G^V 20 | 3,146 | 2,825 | −320 (62) | 2 of 20 | 613 | 4,639 | 2,510 |

| cell (10/90) | careful | stamper | stamper − careful (se) | richer | false approvals | audits assigned | reviews unassignable ticks |
|---|---|---|---|---|---|---|---|
| defaults | 3,687 | 3,626 | −61 (89) | 8 of 20 | 522 | 688 | 946 |
| band 0 | 4,053 | 3,585 | −469 (215) | 7 of 20 | 518 | 681 | 916 |
| band 0.2 | 3,627 | 3,629 | +3 (90) | 9 of 20 | 521 | 683 | 933 |
| floor 0.05 | 3,556 | 3,598 | +41 (134) | 9 of 20 | 533 | 265 | 312 |
| floor 0.5 | 3,394 | 3,338 | −57 (81) | 12 of 20 | 456 | 1,307 | 7,956 |
| G^V 10 | 3,553 | 3,625 | +72 (118) | 10 of 20 | 522 | 678 | 1,614 |
| G^V 20 | 3,633 | 3,537 | −96 (91) | 7 of 20 | 499 | 661 | 4,803 |

**The tie band is the knob that carries the reliability channel.** With no band, selection is argmax ρ
and careful actors win 165 awards to the stampers' 135 at 50/50: a gap of 530 per actor, three times the
default's. At band 0.2 the κ tiebreak hands most awards to whoever has duty credit and the gap vanishes.
The ρ separation itself is only 0.02 (0.93 against 0.91), so a band of 0.05 already lets most stampers
through; the deterrent the rulebook relies on (§7.3, §11) works exactly as far as selection is allowed
to see ρ. At 10/90 the same holds in direction (−469) with two careful actors' worth of variance.

**The audit floor trades correctness for capacity, and capacity wins.** Raising the floor to 0.5 nearly
doubles the audits assigned and halves the stampers' lead in false approvals (284 → 206 at 50/50;
522 → 456 at 10/90), but the reserve of four cannot carry it: a submitted case waits for a reviewer in
7,800 review-ticks, awards go unfilled in 980 ticks, vesting falls by 12%, and both populations end
poorer. Lowering the floor to 0.05 costs 20 more false approvals and changes the wealth gap not at all —
at these catch rates the audit is not what separates the two; selection is.

**A larger bond punishes stampers and starves the reserve.** G^V 20 widens the gap to −320 (2 of 20)
and cuts false approvals (284 → 211), but reviews unassignable rise to 4,600 ticks because fewer actors
can fund the bond, stampers review 25% less (143 against 223) and careful actors forfeit five times the
default's bonds on their own 5% errors. At 10/90 the same bond lowers false approvals only to 499.

**What this says for the next runs.** Within the declared regime no default rescues the 10/90 economy:
the reserve is stamper-on-stamper and no knob changes who audits whom. The band is the cheap lever and
has no capacity cost; the floor and the bond both spend reviewer capacity, which at X = 4 is the binding
constraint — the X = 8 cells of the rerun are the control for that.

## Appeals run — the term stampers never pay (October 17, 2026)

`drivers/sweep.py`, 4 cells × 20 seeds = 80 runs, same declaration and defaults (X = 4, f = 2), with the
actor's response to an N now declared by `--appeal-policy`: **truthful** — appeal an N on work that is
truly fulfilled, accept otherwise; **always** — appeal every N. The court fee D = 2 is paid when the
actor can fund it (it always could). Appeal reviews go to whoever the reserve makes eligible, stampers
included, and answer by disposition; splits are ruled by the truth with probability 0.8. Results in
`agentic_sim/results/studies/1.1.0-stamping/appeals/` (summary `runs/20261017-111325-appeals/`).
Per actor, means over 20 seeds; the "none" rows are the rerun's default cells:

| cell | careful | stamper | stamper − careful (se) | richer | careful bonds lost | a = false N appealed and overturned | false approvals | vested |
|---|---|---|---|---|---|---|---|---|
| 50/50, none | 3,275 | 3,102 | −173 (73) | 6 of 20 | 9.9 | — | 284 | 2,596 |
| **50/50, truthful** | 3,269 | 3,129 | **−140 (120)** | 8 of 20 | 46.4 | **0.98** (65.6 of 66.6) | 248 | 2,606 |
| 50/50, always | 2,990 | 2,938 | −53 (69) | 9 of 20 | 108.9 | 0.98 | 325 | 2,367 |
| 10/90, none | 3,687 | 3,626 | −61 (89) | 8 of 20 | 14.0 | — | 522 | 2,881 |
| 10/90, truthful | 3,460 | 3,639 | **+179 (120)** | 13 of 20 | 52.8 | 0.98 | 509 | 2,875 |
| 10/90, always | 2,879 | 3,596 | **+717 (67)** | 19 of 20 | 483.1 | 0.98 | 535 | 2,784 |

**a is about 1, and the §7.3 condition then fails at the effective catch rate.** With truthful appeals,
98% of false rejections are appealed and overturned. The careful reviewer's own 5% error on the 80% of
work that is good is therefore paid in full — its bond, its fee, and the court fee — while a stamper's
false approvals are caught 3% of the time. §7.3's sign condition, pb > 0.04 a, needs an effective pb of
about 0.04; the run's is 0.03. The money gap at 50/50 shrinks from −173 to −140 and is no longer
distinguishable from zero (se 120); at 10/90 it turns against the careful reviewers (+179, 13 of 20),
whose ρ falls below the stampers' (0.96 against 0.97) because their errors are the ones that get
adjudicated. Careful reviewers forfeit five times the bonds they did without appeals (46 against 10).

**Frivolous appeals turn the appeal into a weapon in a stamper-majority reserve.** With every N appealed
at 10/90, the appeal panel is drawn from stampers and answers F: 147 of 155 true rejections are
overturned, each careful actor is overturned 96 times and forfeits 483 in bonds, ends with ρ 0.89
against 0.98, and the stampers end richer by 717 in 19 of 20 seeds. Only 30 of 3,000 tasks reach final N;
label accuracy under the procedural grade falls to 0.76. At 50/50 the same policy files 320 appeals and
wins 40% of the unfounded ones, the reserve spends 8,100 review-ticks waiting, awards go unfilled in 980
ticks and both populations end poorer.

**What this says.** Design revision 1 removed the fee penalty on care; the appeal path is the next
structural asymmetry: a careful reviewer's error is appealable by the party who knows the truth, a
stamper's error is found only by an audit at the floor rate, and the appeal panel is as careless as the
reserve. The run measured a ≈ 1, so the appeals term is the full ε(1−b)(f̄ + G^V) and the question moves
to the catch rate: the audit floor at X = 4 cannot be raised without starving the reserve (default sweep),
so either the reserve must be larger or the panel must be chosen by ρ. Under §19 these are evaluations and
design questions to write up, not patches.

## Requester-dispute run — truth enters with requesters (October 17, 2026)

`drivers/sweep.py`, 6 cells × 20 seeds = 120 runs, same declaration and defaults (X = 4, f = 2, no
appeals), with the human's response to a pending F declared by `--dispute-policy`: **truthful** — H
disputes every pending F on work that truly failed; **half** — the same with probability 0.5; **always** —
H disputes every pending F. H pays the court fee D = 2 each time and never ran short. The requester acts
once, before the audit roll; a dispute pre-empts the audit. Dispute reviews go to whoever the reserve
makes eligible and answer by disposition; splits are ruled by the truth with probability 0.8. Results in
`agentic_sim/results/studies/1.1.0-stamping/disputes/` (summary `runs/20261017-112415-disputes/`).
Per actor, means over 20 seeds; "none" rows are the rerun's default cells:

| cell | careful | stamper | stamper − careful (se) | richer | disputes filed / won | stamper overturned % | false approvals | vested | reviews unassignable ticks |
|---|---|---|---|---|---|---|---|---|---|
| 50/50, none | 3,275 | 3,102 | −173 (73) | 6 of 20 | — | 3.0 | 284 | 2,596 | 1,046 |
| **50/50, truthful** | 2,748 | 2,444 | **−304 (50)** | 2 of 20 | 299 / 215 | 16.9 | **83** | 2,155 | 7,794 |
| 50/50, half | 3,089 | 2,904 | −185 (46) | 3 of 20 | 184 / 109 | 9.4 | 229 | 2,450 | 7,098 |
| 50/50, always | 1,716 | 1,553 | −163 (79) | 5 of 20 | 1,274 / 110 | 8.6 | 47 | 1,153 | 11,567 |
| 10/90, none | 3,687 | 3,626 | −61 (89) | 8 of 20 | — | 0.8 | 522 | 2,881 | 946 |
| 10/90, truthful | 3,252 | 3,031 | −221 (108) | 11 of 20 | 458 / 78 | 4.3 | 376 | 2,377 | 8,296 |
| 10/90, half | 3,577 | 3,447 | −130 (73) | 8 of 20 | 258 / 38 | 2.4 | 468 | 2,729 | 7,318 |
| 10/90, always | 1,965 | 1,912 | −53 (149) | 13 of 20 | 1,319 / 42 | 2.3 | 206 | 1,265 | 11,891 |

**The dispute does to stampers what the appeal did to careful reviewers.** A requester who knows the
truth and disputes every false approval at 50/50 wins 72% of them, overturns 17% of the stampers'
reviews (33 per actor, bonds forfeited 167 against 33), cuts false approvals from 284 to 83, and widens
the careful lead to 304 per actor (2 of 20 seeds the other way). The human-explicit grade is correct in
every case it labels, by construction. This is the mirror image of the appeals run: there the party who
knew the truth was the actor and the exposed error was the careful reviewer's; here it is the requester
and the stampers'. Together the two runs say the rulebook's adjudication finds the error of whoever the
truth-holder chooses to challenge, at the rate the truth-holder chooses to challenge.

**At 10/90 the dispute panel is the stampers, and the requester loses.** H files 458 disputes and wins
78: the two dispute reviewers are drawn from a reserve that is nine-tenths stampers and say F, so 82% of
true disputes fail, false approvals stay at 376, and the procedural grade's accuracy falls to 0.59 — the
challenge path is now the least reliable label in the economy. The careful lead holds on the mean (−221)
but splits the seeds (11 of 20 the other way).

**Every dispute costs the reserve more than the audit it replaces.** A dispute is two reviews where an
audit was one, and with four on duty the economy pays for it in capacity: a submitted case waits for a
reviewer in 7,100–8,300 review-ticks under truthful or half disputes, awards go unfilled in about 970
ticks, vesting falls 6–17%, and both populations end poorer than with no disputes at all — the careful
reviewers by 500 per actor at 50/50. A requester who disputes everything (the "always" cells) files
1,300 disputes, loses 92% of them, pre-empts every audit, halves the economy's throughput and everyone's
wealth, and still ends with the fewest false approvals (47 at 50/50): correctness bought at the price of
the economy.

**What the four runs say together.** Under 1.1.0 the fee no longer penalises care; what decides the
careful–careless contest is who challenges whom and whether the reserve can carry the challenges. The
reliability channel works exactly as far as selection is allowed to see ρ (the tie band). Every path
that exposes an error — audits above the floor, appeals, disputes — draws two reviews from the same
small reserve, and at X = 4 that reserve is the binding constraint in every cell that uses them; the
X = 8 cells of the rerun are the only ones in which no case waited. The panel's composition is the
reserve's composition, so in a stamper-majority reserve appeals favour stampers and disputes fail. Under
§19 these are evaluations; the design questions they raise — reserve size against challenge load, a
panel chosen by ρ rather than by duty, and what a requester-dispute should cost relative to an audit —
are for a written proposal, not a patch. Spec §18.1 questions 1 and (in part) 6 are answered for this
declaration; 2, 3, 4, 5, 7, 8 are untouched.

## Two controls before review (October 17, 2026)

Both in `agentic_sim/results/studies/1.1.0-stamping/controls/`: `X8/` (appeals and disputes with eight on
duty, 20 seeds, 20 actors) and `scale200/` (200 actors, 40 on duty, 30 tasks per tick, 5 seeds). Same
declaration otherwise; truthful policies only.

| cell | careful | stamper | stamper − careful (se) | richer | stamper overturned % | false approvals | reviews unassignable ticks |
|---|---|---|---|---|---|---|---|
| 50/50, appeals, X 4 (above) | 3,269 | 3,129 | −140 (120) | 8 of 20 | 3.4 | 248 | 2,981 |
| **50/50, appeals, X 8** | 3,194 | 3,330 | **+136 (39)** | 15 of 20 | 2.7 | 276 | 0 |
| 10/90, appeals, X 8 | 3,291 | 3,693 | +403 (85) | 16 of 20 | 0.6 | 529 | 0 |
| 50/50, disputes, X 4 (above) | 2,748 | 2,444 | −304 (50) | 2 of 20 | 16.9 | 83 | 7,794 |
| **50/50, disputes, X 8** | 3,595 | 2,264 | **−1,331 (35)** | 0 of 20 | 14.2 | 131 | 0 |
| 10/90, disputes, X 8 | 3,661 | 3,545 | −116 (80) | 9 of 20 | 3.8 | 455 | 1 |
| 200 actors, 50/50, none | 2,942 | 2,793 | −149 (59) | 0 of 5 | 2.6 | 2,874 / 30,000 | 2,965 |
| 200 actors, 50/50, appeals | 2,868 | 3,012 | +144 (68) | 4 of 5 | 2.6 | 2,790 / 30,000 | 5,415 |
| 200 actors, 50/50, disputes | 2,451 | 2,275 | −176 (15) | 0 of 5 | 16.2 | 630 / 30,000 | 73,841 |

**Capacity was hiding the size of both challenge effects, not their direction — and in the appeals
case it was hiding a reversal.** With eight on duty no case waits for a reviewer, and the appeals cell
that read as "indistinguishable from zero" at X = 4 reads **+136 (se 39), stampers richer in 15 of 20**:
truthful appeals alone, with the fee penalty gone and the reserve unconstrained, hand the contest to the
stampers at 50/50. The mechanism is the one §7.3's appeals term names: 98% of the careful reviewers' false
rejections are adjudicated and lost, 3% of the stampers' false approvals are, so careful ρ ends below
stamper ρ (0.92 against 0.93) and selection follows. At 10/90 it is +403. The dispute cell moves the other
way by the same release: −1,331 (se 35), none of twenty seeds the other way — a requester who disputes
every false approval, with a reserve that can hear the disputes, takes 17% of the stampers' reviews and
most of their awards (112 against 188). At 10/90 the stamper panel still defeats the disputes (82 of 543
won) and the gap is −116.

**The 20-actor results scale.** At 200 actors with the same on-duty share the no-challenge cell gives
−149 (−173 at 20), the appeals cell +144 (+136 at X = 8), and the disputes cell −176 with the reserve
again saturated — 2,400 disputes are 4,800 reviews, cases waited 74,000 review-ticks, awards went
unfilled in 987 of 1,000 ticks. The reserve-share of 20% binds at 200 as it did at 20.

**What changes in the reading.** The appeals finding is stronger than the X = 4 run showed: under 1.1.0
at the defaults, when actors appeal truthfully and the reserve is not the bottleneck, stamping wins.
The two challenge paths pull in opposite directions with the same machinery — the appeal exposes the
careful reviewer, the dispute exposes the stamper — and which one is open in a given economy decides the
outcome. That sharpens the design questions for the review: the panel's composition (a panel chosen by ρ
would change both), the reserve's size against the challenge load, and the cost of a dispute against an
audit; and it adds one — whether a reviewer's appealable error and an auditable error should carry the
same bond when their rates of exposure differ by a factor of thirty.

The engine and its tests stay as they are; a driver that needs an engine change has found either a
conformance bug (fix + regression) or a design question (write it up, do not patch around it).

## Design revision 1 — the verification deposit is two pots (1.1.0, October 17, 2026)

The first change to the rulebook since the freeze, and the first use of §19's design-revision path. The
stamping result above was read against the text and the history: v0.1 R16–R17 had agreed "capped
expense reimbursement plus a fixed fee … for review work, not for the answer"; v0.3, repairing the
second review's shortfall finding, made the fee the deposit's remainder after reimbursements, and from
then on every credit of care reimbursed was a credit of fee lost — while §7.3 still reasoned with the
fixed fee. The revision was written as a release candidate (`spec/design_revisions/`), read on its own
through two implementation reviews — rc.1 computed "unowed fee money" per case, which in a tree would
have paid a root's expenses with money its nested case's reviewers were still owed (reviewer test
r4_07 is the shape); rc.1 said "nothing else moves" when reviewer income from deposits falls by about
three quarters in the common case; the hypothesis needed its appeals term; I10 and record mode gain the
tree consequences; the rerun needs twenty seeds or more — and accepted as rc.3. The consolidated text is
`spec/agentic_economics_loop_spec_v1_1_0.md` (§4.3 whole, §7.3, §10, I10/I12/I17/I19, §18.1, §20,
Appendices A, C, F); v1.0.1 moved to `spec/history/`. Versioning is semver from here: patch = wording,
minor = design revision, major = change of approach; a proposal is `-rc.N` and not in force.

Engine: the case pool holds the allowance and the fee pot; settlement follows §4.3 in order and reads
the root's pool for a nested case; the refund waits for tree closure; I19 is new; a root with open pots
stays resident. The suite's own figures were revised to §20 under 1.1.0 and the golden heads re-pinned
once; one reviewer test (r5_a, a budget of exactly B + 10) is superseded with the reason stated and its
principle re-asserted in `test_v11`; every other reviewer test passes unchanged. 181 + 25 in all four
modes. The rerun of strategy run 1 with only the rule changed is the section after the first result.

## Run 3 — the reviewer's list before a revision 2 (October 17, 2026)

The reviewer's reading of the 1.1.0 study (`uploads/run-02-1.1.0-study-and-review.md`, external) confirmed
the §4.3 implementation and asked for five things before a design revision 2 is proposed. Four are runs,
in `agentic_sim/results/studies/1.1.0-combined/` (560 runs, 20 seeds per cell, all audits passed); the
fifth is a test. One of the reviewer's classifications does not hold against the text and is answered
below. Everything here is under 1.1.0 as it stands.

**Conformance first: assignment is round-robin (§7.5), and the earlier sweeps used a seeded choice.**
§7.5 reads "Volunteers first; otherwise round-robin among eligible duty actors; otherwise wait." The
October 16–17 sweeps assigned initial, audit and appeal reviewers by a seeded random choice among the
eligible duty actors and declared that policy in every manifest (§18.2) — honest, but not the rule's. The
driver now defaults to round-robin and keeps `--assignment seeded` for reproducibility (the old heads
reproduce). The four headline cells re-run under round-robin (`rr-check/`):

| cell (50/50) | seeded (earlier) | round-robin | 
|---|---|---|
| none, X 4 | −173 (73) | −113 (66) |
| none, X 8 | −290 (39) | −265 (36) |
| truthful appeals, X 8 | +136 (39) | +90 (39) |
| truthful disputes, X 8 | −1,331 (35) | −1,370 (44) |

Every cell moved by less than its standard error and no direction changed, so the five earlier sweeps
stand as declared, with this note. The same §7.5 sentence settles the reviewer's first classification:
"a challenge panel chosen by ρ" is not an orchestrator policy runnable now — round-robin is a Rule — so it
is a design question for a revision 2 proposal and was not run.

**The combined regime (`combined/`): truthful appeals and truthful disputes at rate ∈ {0, 0.25, 0.5}, band 0,
X ∈ {4, 8}, both splits.** Stamper − careful wealth per actor (se), stampers richer of 20:

| dispute rate | 50/50, X 4 | 50/50, X 8 | 10/90, X 4 | 10/90, X 8 |
|---|---|---|---|---|
| 0 (appeals only) | +2 (87), 10 | **+200 (52), 16** | +1,336 (176), 19 | +1,794 (155), 20 |
| 0.25 | −77 (56), 8 | **−489 (70), 1** | +145 (168), 7 | +1,274 (171), 19 |
| 0.5 | −144 (36), 3 | **−919 (77), 0** | −141 (61), 7 | +1,270 (201), 18 |

The requester's attention is the swing variable. With the reserve unconstrained and selection pure argmax
ρ, appeals alone give the stampers +200; a requester who disputes one false approval in four turns it to
−489 and one in two to −919 — the break-even dispute rate at 50/50 is about 0.07. Band 0 amplifies
whatever ρ says, in both directions: at 10/90 the two careful actors' ρ ends below the stampers' (their
errors are the adjudicated ones), argmax then gives them 66 awards to the stampers' 159, and no dispute
rate in the sweep recovers it — disputes at 10/90 are heard by a stamper panel (23 of 135 won at X = 8)
and false approvals fall only from 521 to 487. At X = 4 every cell is capacity-damped (6,400–7,400
review-ticks waiting at the higher rates).

**The ε sweep (`epsilon/`): the careful reviewer's error rate at dispute rate 0.25, band 0.** 50/50, X 8:
ε 0.02 → −930 (58); 0.05 → −489 (70); 0.10 → +312 (63), stampers richer in 18 of 20. The reversal is
linear in ε as the reviewer predicted — about +155 per actor per point of ε — with break-even near ε ≈
0.08 at this dispute rate. At 10/90, X 8: +378, +1,274, +2,470; a careful reviewer with ε = 0.10 in a
stamper-majority reserve ends with 34 awards to the stampers' 163.

**Solvency (`solvency/`): G^V 20 confirmed as a q6 shortfall.** With the new counter — on-duty actors that
cannot fund the bond, summed over ticks — G^V 5 shows 9–12 such actor-ticks in 1,000; G^V 20 shows 291 at
both splits: on average 0.29 of the four duty slots is held by an actor who cannot be assigned, a case
waits for a reviewer in 4,500–4,700 review-ticks, awards go unfilled in 590–640 ticks, and vesting falls
4%. Stampers are the ones short — they review 136 times to the careful actors' 230 at 50/50, having lost
more bonds. The gap widens to −367 (70) at 50/50, but by starving the reserve, not by deterrence alone.

**The test (item 5).** The random scenario of `test_perf_equivalence` already repays Ω's advances from the
fee pot at closure (5 and 3 times in the two seeds, with 22 and 17 nested draws) under the per-tick audit;
`test_v11` gains a tree whose expenses exceed φ^E with Ω unable to advance, so claims arise in both the
nested case and the root and the pot's remainder settles them in queue order at closure. Suite 182 + 25.

**What this leaves for the revision 2 proposal.** With the fee penalty gone (1.1.0), the contest between
careful and careless review is decided by three things the runs have now measured: whether the party who
knows the truth challenges (break-even dispute rate ≈ 0.07 at 50/50), how often the careful reviewer errs
(break-even ε ≈ 0.08 at dispute rate 0.25), and who sits on the panel (a stamper-majority reserve is not
recovered by any dispute rate). The first two are the product's inputs; the third is the rule. Under §19
the questions for the proposal are: the panel's composition (§7.5's round-robin against a panel chosen by
ρ, or by a reliability floor); whether an appealable and an auditable error should carry the same bond;
the reserve's size against the challenge load (a default, X, with the measured capacity cost); and the
cost of a dispute against an audit (defaults D and X first).

## Design revision 2 — the loop's own clock (1.2.0, October 17, 2026)

The second use of §19's design-revision path. Run 3's reading was that three measured inputs decided the
careful–careless contest under 1.1.0 — whether the party who knows the truth challenges, how often the careful
reviewer errs, and who sits on the panel — and that the third was the rule's: a stamper-majority reserve
produces every signal the loop has, reliability included, so no remedy that leans on ρ can cure it. The design
discussion the same day added the assumption the baseline had left implicit — **humans do not intervene** —
which removes the one external oracle the loop leaned on. The revision gives the orchestrator truth of its own:
**planted work** whose fulfillment it knows by construction (§7.6), a **plant record** per actor adjudicated by
that truth and not by the panel, in two eligibility tiers (§11.2), and an **effort dial** that reads the
reserve's bad-plant approval rate once a period and moves the plant rate, the audit odds, the reserve's size
and the service fee with it — "the block-difficulty adjustment with negligence in place of block time" (§12.2).
A reserve that runs short of eligible actors runs short and says so; the loop does not seat the negligent to
make a number.

**Reviews.** Three release candidates, each read on its own (`spec/design_revisions/dr2_1.2.0-rc.*-review.md`).
rc.1: the plant actor was named in a view that carried the actor (§14) — the actor leaves the view; I9 and I21
could not both hold when eligible actors ran short — the reserve may run short and the gap is counted; a single
plant reliability let a reviewer approving half the bad plants stay eligible for ever — the record is defined on
the quantity the clock measures; newcomer plant-doubling cannot coexist with round-robin; the solvency figure
(29% of slots) was 7% of slot-ticks; Ω's working capital (45 per plant), the audit cap and the channels of the
hypothesis were unstated. rc.2: clearing the record on return would have readmitted every stamper with a clean
slate for ~50 reviews and kept panels captured at ~70% strength — the record persists; two rules for a
newcomer's audit odds; eligibility is a property at assignment, and a suspended actor leaves duty whether or not
a replacement exists. rc.3 adopted all of it; one leftover sentence was fixed in the accepted text
(`spec/design_revisions/dr2_the_loops_own_clock_1.2.0.md`, verbatim).

**Found at implementation — flagged for confirmation.** With the record persisting, "at the end of the
suspension it is readmitted only if its record passes, and otherwise remains suspended for a further T_susp"
makes every suspension permanent: the record is a trailing window of plant outcomes and a suspended actor
judges no plants, so a record that failed cannot pass later. That leaves T_susp inert and contradicts the
revision's §2.4 and its §8 run 2. The engine implements the smallest reading that gives T_susp its meaning:
readmission **on probation** — to duty, not to panels — until the actor's next plant re-checks the record, with a
still-failing record suspended again at once (§11.2 of the consolidated text, Appendix G, `World._rotate`). It is
the implementer's reading, marked as such in the text; confirming or revising it is the next design decision,
and the alternative is one branch of `_rotate`. The first smoke run shows its consequence: at the defaults a
returning stamper judges about one plant before it is out again, which is enough to hold F̂ just above F* and
pin m at m_max (below). **Confirmed** as the rule in force by patch 1.2.1 (October 17, 2026; the sentence of
design revision 3 rc.1's Appendix A), applied to `spec/agentic_economics_loop_spec_v1_2_1.md`; 1.2.0 to history.

**Engine (commit after `0ccf8bc`).** `create_plant` from two Ω-funded system wallets, the sealed marker and its
reveal, adjudication by truth, refusal of every challenge on a plant, the plant grade; the record, the two
tiers in every assignment and at rotation, suspension and probation; rotation filling to X_t or shrinking to
it, the eligibility shortfall; the dial once a period on adjudications with its clamps, the alarm and the
re-seat; the applied audit odds `min(1, m p_j)`; ω scaled; the view without the actor; I20 and I21; I9 and I13
amended; defaults p_start = p_cap = 1, Ω₀ = 300. `test_v12` (15) carries the revision's §6 figures and the
mechanism's properties; the equivalence scenario plants work and its goldens were re-pinned once. 197 passed,
26 expected failures in all three modes (the twenty-sixth: the third review's test 18, Ω's float pinned at 20).
The consolidated text is `spec/agentic_economics_loop_spec_v1_2_1.md` (§1, §2, §4.1, §7.1, §7.5–7.6, §8.3,
§11.2, §12 whole, §14, §15.3, §16, §17, §18.1, §20, Appendices A–D, G); 1.1.0 moved to `spec/history/`.

**Driver.** `drivers.stamping` supplies the plants the engine's rate calls for before each tick's assignments
(bad w.p. β_P, truth from its task world), rolls the effective odds, offers only tier-eligible reviewers, and
carries `--rules 1.1.0` (no plants, dial off, p_start = p_cap = 0.5, Ω float 20 — the 1.1.0 engine, declared),
`--pi0`, `--dial`, `--beta-p`, `--camouflage` (the red team) and the clock's columns. One smoke run at the
defaults (50/50, X₀ = 4, seed 1, no appeals or disputes), 1.2.0 against the 1.1.0 control: false approvals 53
against 291; stampers 9 of 10 suspended at the end, each suspended about seven times; the careful actors carry
the reviewing (506 reviews each against 77) and the stampers, free of duty, take the awards (193 against 107);
careful still richer, by 293 against 407 in the control; m pinned at 4, X_t 8, 930 plants, Ω net +5,720 after a
plant spend of 3,656. One seed, no conclusion — but the dynamic to watch in run 4 is already visible: suspension
frees the stampers for paid work, and the money contest then runs through delivery, not fees.

## Run 4 — the revision's §8 under 1.2.0 (October 17, 2026)

`agentic_sim/results/studies/1.2.0-clock/` (and `1.2.0-clock.zip` beside it): `drift/` (60 runs), `adaptive/`
(40), `tipping/` (120), `redteam/` (80) — 300 runs, 20 seeds per cell, 20 actors, every final audit passed;
engine 544ff19 (2708f64 adds only test records). Appeals truthful and no disputes throughout — the design
assumption's regime: the actor polices rejections, nobody polices approvals but the loop itself. The §6
reproduction is `test_v12`. "FA" is false approvals that vested; 1.1.0 cells are the control (`--rules 1.1.0`).

**Drift (run 2 of the revision's §8): the honest regime holds, at a capacity price.** Stampers rise from 50% to
90% in steps of 5% every 100 ticks over 1,500 ticks, 4,500 tasks posted.

| cell | FA | vested | stamper − careful (se) | stampers richer | m at end | alarms | eligibility shortfall (actor-ticks) | reviews waiting (review-ticks) | plants unfunded |
|---|---|---|---|---|---|---|---|---|---|
| 1.2.0, dial on | 83 | 2,518 | −2,213 (49) | 0 of 20 | 4.0 | 10.6 | 2,515 | 119,620 | 351 of 918 |
| 1.2.0, dial off (plants at π₀, m = 1) | 257 | 3,213 | −827 (69) | 0 of 20 | 1.0 | 0 | 33 | 52,528 | 0 |
| 1.1.0 control | 650 | 4,209 | +233 (186) | 12 of 20 | — | — | — | 2,283 | — |

Under 1.1.0 false approvals grow with the stamper share (80 at tick 300, 650 at 1,500) and the stampers end
richer in 12 of 20. With plants alone (dial off) they fall to 257; with the dial they fall to 83, and they stop
growing once the dial saturates: 66 at tick 600, 83 at 1,500. The dial reaches m = 2 at about tick 330 and m_max
at 395; the first alarm fires at about tick 450 (every run), and then roughly every period, because the only
actors judging plants are the two careful survivors and stampers returning on probation, so F̂ stays far above
F* (0.46–0.78 in the last periods). The price is capacity: on duty falls from 6 at tick 300 to about 3 from tick
900, against an X_t of 5–8; the eligibility shortfall accumulates 2,515 actor-ticks; a submitted case waits
for a reviewer 119,620 review-ticks in all (47× the control); vesting ends at 2,518 cases against 4,209; Ω
cannot fund 351 of the 918 plants the rate called for at m = 4 (Ω net still +1,603, the raised ω). Hypothesis 2
holds as stated — "honest and slow rather than captured and fast" — and the slow is measured.

**Adaptive dispositions (run 3).** Actors start 50/50; every 100 ticks each actor takes the richer disposition
by mean public wealth with probability 0.2.

| cell | stamper share at end | stampers richer | FA | m | alarms |
|---|---|---|---|---|---|
| 1.2.0 | 0.29 | 6 of 20 | 59 | 3.2 | 4.2 |
| 1.1.0 | 0.43 | 9 of 20 | 249 | — | — |

Both populations move toward careful under truthful appeals; 1.2.0 moves them further and faster. One
adaptation rule, one seed of starting shares: a direction, not an equilibrium.

**The tipping point (run 4) — and the finding of this run.** Fixed splits, truthful appeals, 1,000 ticks.

| split (stampers) | 1.2.0: stamper − careful (se), richer | 1.2.0 FA | 1.1.0: stamper − careful (se), richer | 1.1.0 FA | 1.2.0 reviews careful / stamper | 1.2.0 awards careful / stamper | 1.2.0 delivery income careful / stamper | 1.2.0 fees careful / stamper |
|---|---|---|---|---|---|---|---|---|
| 50% (red team, no camouflage) | −2 (51), 11 of 20 | 53 | — | — | 502 / 78 | 99 / 200 | — | — |
| 60% | **+215 (34), 19 of 20** | 67 | +22 (108), 9 of 20 | 306 | 636 / 82 | 64 / 207 | 1,063 / 3,311 | 2,106 / 277 |
| 70% | −10 (25), 8 of 20 | 89 | +43 (77), 9 of 20 | 379 | 787 / 91 | 37 / 195 | 654 / 3,142 | 2,612 / 309 |
| 80% | −902 (25), 0 of 20 | 121 | +223 (138), 13 of 20 | 442 | 799 / 100 | 33 / 143 | 626 / 2,373 | 2,915 / 354 |

Honesty holds at every split: false approvals fall four- to five-fold against 1.1.0, the stampers' â is
0.76–0.90 and they are suspended within their first handful of plants (run 1's "seat" channel works). But
the money contest at 50–70% is **not** what Hypothesis 1 predicted. The careful actors are the only eligible
reviewers, the dial sizes the reserve up (X_t 7–8), and they are therefore on duty almost all the time — 500 to
800 reviews each against 80–100 for a stamper — while the suspended stampers, free of duty, take the awards
(200 to 64 at 60/40) and the delivery income (3,311 to 1,063). The fee f = 2 per review does not replace the
award B = 20 per delivery: at 60/40 the stampers end richer in 19 of 20 seeds by 215 per actor, under the rule
whose purpose was to make stamping unprofitable. The ρ channel does not help, because selection is argmax ρ
among the *free* actors, and the careful are not free. What decides the contest under 1.2.0 is therefore not
the plant penalty (about 0.6 per review, as computed) but **who carries the reviewing load**, and the revision
loads it onto the honest minority and pays them the ordinary fee while Ω collects the raised security tax (Ω
net +5,898 at 60/40 against +3,106 under 1.1.0). Only at 80/20, where the stampers are too many for the market
to absorb and the reserve is short most of the time, do they lose again (−902).

**Red team (run 5).** A stamper that rejects 10% of its reviews at random: at 50/50 it buys time — plant
failures per stamper 5.9 against 7.2, suspensions 45 against 54, alarms 2.1 against 4.3 — and turns the wash
(−2) into +112 (se 74, 13 of 20), with false approvals still low (42) and false rejections up (26 against 18;
its random rejections are appealed and 133 of 138 appeals won). At 90/10 it changes nothing that matters
(−1,733 against −1,961; FA 154 against 165). Camouflage is a small edge, not a safety; the detection half of
the red team has nothing to detect by construction (the view test).

**Cost (run 6).** Ω's plant spend is 2,000–3,500 per 1,000 ticks at m ≈ 4 (the careful inspections' fees and
expenses; a stamper's failed plant costs Ω nothing), against ω income that rises with m to about four times
1.1.0's; Ω net is positive in every cell (+900 to +5,900 per run) and lowest where the reserve is shortest
(80/20, drift), because fewer awards mean less ω. The working capital binds before the income does: at m = 4
and π = 0.4 the rate calls for more plants than Ω's unlocked balance can carry at once — 17 to 663 unfunded per
run, worst where vesting is slow and plant pools stay open longest. X_t tracks demand (4.8 to 8.3) and is
undershot by the eligible pool wherever stampers exceed 60%.

**What this says for the next design decision.** Three things, in the order I would put them to the reviewer:

1. **The probation reading (above) needs a decision.** It is what makes F̂ stay high and the alarm fire every
   period in a captured market, and what gives the returning stamper its one plant before it is out again.
   The literal reading (permanent suspension) would make the clock quieter and the shortage larger. Neither
   is obviously right; the engine holds the first, and the alternative is one branch.
2. **The reviewing load is the contest.** Under 1.2.0 the honest minority is conscripted into the sized-up
   reserve and paid f = 2 a review while the stampers deliver at B = 20. Candidates, all design questions:
   the fee scaled with the dial as the tax is (f_t = f·m_t, funded from ω_t, which Ω now keeps); a reserve
   sized to the *eligible* pool rather than to demand; or the stampers' exclusion from duty extended to
   awards (a ρ or â floor for selection — which run 3 warned against for ρ, but â cannot be captured).
3. **Ω's working capital, not its income, caps the clock** at m_max; the float (300) carries one period at
   m = 1, and the rate at m = 4 is four times that with slower closures.

Untouched: §18.1 questions 2, 4, 5, 7, 10. The reviewer notes are
`agentic_sim/results/studies/1.2.0-clock-notes-for-reviewer.md`.

## Design revision 3 — inspection is membership (1.3.0, October 17, 2026)

The third use of §19's path, written the same day from run 4's finding and Baruchi's answer to it: "if you get
thrown out of inspection you are banned from receiving a new task; to get tasks back you have to prove you are
doing good inspection for a while." Suspension now suspends **market membership**: no new award while suspended
or on probation; the held commitment is finished by the ordinary rules. After T_susp the actor is a
**probationer** — initial reviews only, audit odds pinned at 1, re-suspended by any plant failure, readmitted
when its one trailing record passes θ_duty with n_min new plant outcomes judged (a full stamper: four rejected
bad plants, about fifty honest reviews; its panel seats return only once its approvals roll out of the window).
**At most half the eligible members are on duty**; probationers fill the initial seats first, members hold the
audit and challenge seats. The dial's **raised tax goes to a duty fund** paid to the settling reviews by role
weight as an uplift, instead of to Ω. **Plant capital counts the pots only** (15, not 45). Newcomers' odds are
pinned at 1 until their bad-plant record is determined (the 1.2.0 taper was passed by a third of stampers at
once). A duty levy — keep winning awards against a cash levy — was considered and rejected (Appendix B).
The slowness run 4 measured is deliberately **not** treated here; Baruchi has a direction for it, reserved.

**Reviews.** rc.1 (`spec/design_revisions/dr3_1.3.0-rc.1-review.md`): readmission stated two ways with the
worked example following the wrong one (0.17 against the persisting record's 0.5, and "panel-eligible at
once"); the cap as a standing per-tick predicate against mid-review completion, and its panel floor of two
against a cap of one at E_t = 2; reserve sizing on a population mean while probationers and newcomers are
audited at 1; no refill order for turns; the invariant and settlement consequences of netted plant capital
unstated; probation pays a stamper +1.2 a review (the award deters, not probation); the newcomer pin's
fresh-population worst case. rc.2 adopted all of it; one qualifier remained — the panel floor bounded by
availability, not membership — and the accepted text carries it in the reviewer's wording. Patch **1.2.1**
(the probation reading confirmed) was applied to the text in force the same day, before 1.3.0.

**Found at implementation — two readings, flagged for confirmation (§12.1, Appendix H).** (1) The members' cap
⌈E_t/2⌉ is 3 at six actors — below the X₀ = 4 of Appendix A's initialization and §20's worked example, so the
baseline's own worlds, and every reviewer test built on them, would violate the revision at tick 0 (the first
suite run failed on "C is not on verification duty" across the board). The engine lets the cap never fall below
the reserve's floor V_max + 1, as the panel floor yields to the cap; the difference from the literal text is
confined to memberships of four to seven, where the literal cap would leave two or three members free. One line
(`World._member_cap`). (2) An outgoing probationer whose turn ends with no free probationer stays, rather than
hand its seat to a member whom the next tick's "probationers first" would displace back. One branch of the
rotation. Both are the implementer's; the alternative to each is one edit. **Confirmed** as patch 1.3.1 (October 17, 2026; the sentences of design revision 4 rc.1's Appendix A), applied to `spec/agentic_economics_loop_spec_v1_4_0.md`; 1.3.0 to history.

**Engine (commit after `d8d3834`).** Membership on award with `member_at_award`; probation with the pin, the
re-check on any failure, readmission on the trailing record with the since-suspension counter; two kinds of
reserve seat with the cap at seating, the floor by availability, probationers displacing idle members from
initial seats, turns refilled by kind; the duty fund wallet credited at award and paid by role weight in each
settlement batch; plant capital on the pots alone with no escrow and no guarantee lock; I22, I23; I21 amended;
I15 exempting a plant's guarantee. `test_v13` (11); `test_v12` pinned to the 1.2.1 engine mode
(`Params(membership=False, duty_fund=False, net_plant_capital=False)`, the stamping driver's `--rules 1.2.0`);
goldens re-pinned once. 208 passed, 26 expected failures in all three modes. Consolidated text
`spec/agentic_economics_loop_spec_v1_4_0.md` (§2.1, §4.1, §5.2, §7.1, §7.6, §8.3, §10.4, §11.2, §12, §16, §17,
§18.1, §20, Appendices A–D, H); 1.2.1 to history.

**Driver.** Offers to members only; `--rules 1.3.0|1.2.0|1.1.0`, `--fund on|off`, `--m-max`, `--stamper-mode
reformer`; membership, probation, fund and readmission columns. One smoke run at 60/40, seed 1, truthful appeals:
careful 3,884 against stampers 1,966 (the 1.2.0 control: 3,095 against 3,096, a wash); false approvals 34 against
65; vested 1,887 against 2,410 — the gate flips the contest and costs the throughput Hypothesis 3 predicted;
the fund paid 4,542 to reviewers; awards went unfilled for want of members in 850 ticks; plain stampers were
never readmitted (they do not reform); reformers were readmitted 17 times (mean 162 ticks) and still ended at
2,214 against 4,009.

## Run 5 — the revision's §8 under 1.3.0 (October 17, 2026)

`agentic_sim/results/studies/1.3.0-membership/` (and `1.3.0-membership.zip` beside it): `tipping/` (80 runs),
`adaptive/` (60), `drift/` (80), `redteam/` (140: camouflage 80, reformer 60) — 360 runs, 20 seeds per cell,
20 actors, every final audit passed, engine 91a49e5. Appeals truthful and no disputes throughout. The §6
reproduction is `test_v13`. 1.2.0 figures below are run 4's (same seeds, same driver, `--rules 1.2.0`).

**The tipping point (run 2 of the revision's §8) — the sign flips at every split.**

| stampers | 1.3.0: stamper − careful (se), richer | 1.2.0 | 1.3.0 false approvals (of them by probationers) | 1.2.0 FA | vested 1.3.0 / 1.2.0 / 1.1.0 | awards unfilled for want of members (ticks of 1,000) | fund paid to reviewers |
|---|---|---|---|---|---|---|---|
| 50% | −2,132 (100), 0 of 20 | −2 (51) | 53 (7) | 53 | 1,924 / 2,399 / — | 816 | 4,099 |
| 60% | −2,397 (63), 0 of 20 | +215 (34), 19 of 20 | 69 (15) | 67 | 1,727 / 2,412 / 2,675 | 869 | 4,027 |
| 70% | −2,486 (37), 0 of 20 | −10 (25) | 90 (14) | 89 | 1,439 / 2,396 / 2,739 | 878 | 3,040 |
| 80% | −2,428 (36), 0 of 20 | −902 (25) | 113 (16) | 121 | 1,176 / 2,024 / 2,813 | 899 | 2,003 |

Hypothesis 1 holds, decisively: a stamper earns award income only until its first handful of plants and then
nothing, so the honest end richer by 2,100–2,500 per actor at every split, in 20 of 20 seeds. The channel is the
award — stampers' delivery income falls from 3,311 (1.2.0, 60/40) to 1,221, their awards from 207 to 74 — and
the fund adds 340–380 per careful actor. Honesty is unchanged (false approvals within a few of 1.2.0's);
probationers account for 7–16 of them per run (Hypothesis 5: their approvals are all audited, and what reaches a
customer is what an audit missed or no member was free to take). Plain stampers were never readmitted: they do
not reform. **The cost is the throughput Hypothesis 3 named and did not treat**: vesting falls 20–42% below 1.2.0
and 36–58% below 1.1.0, because awards go unfilled in 800–900 of 1,000 ticks for want of free members — at 60/40
eight members with half of them on duty cannot deliver three tasks a tick (Q11).

**Adaptive dispositions (run 3): an honest equilibrium, faster.** Actors start 50/50 and every 100 ticks take
the richer disposition with probability 0.2; 3,000 ticks.

| cell | stamper share at 500 / 1,000 / 2,000 / 3,000 ticks | reached ≤ 10% stampers | mean tick | vested | FA |
|---|---|---|---|---|---|
| 1.3.0, fund on | 0.21 / 0.15 / 0.04 / 0.01 | 20 of 20 | 865 | 7,148 | 91 |
| 1.3.0, fund off | 0.20 / 0.12 / 0.01 / 0.00 | 20 of 20 | 770 | 7,216 | 90 |
| 1.2.0 | 0.36 / 0.29 / 0.15 / 0.07 | 19 of 20 | 1,468 | 6,796 | 92 |

Hypothesis 2 holds: an actor whose income is zero switches faster than one whose income is merely lower; the
population reaches an honest state in about 800 ticks against about 1,500 under 1.2.0, and vesting recovers with
it (7,100–7,200 over 3,000 ticks, above 1.2.0's 6,796). Hypothesis 4 does not: the fund does not speed the
convergence (770 ticks without it, 865 with), because the gate decides the switch and the fund's uplift is small
beside the award. The fund's effect is distributional — 8,048 paid to reviewers over 3,000 ticks instead of
banked by Ω (Ω net 2,889 with the fund, 9,588 without).

**Drift (run 4): honest at both m_max, slower still.** Stampers 50% → 90% over 1,500 ticks.

| cell | FA (of them by probationers) | vested (1.2.0: 2,518; 1.1.0: 4,209) | stamper − careful | plants unfunded | fund paid |
|---|---|---|---|---|---|
| m_max 4, Ω₀ 300 | 97 (24) | 1,506 | −3,038 (120) | 49 | 3,087 |
| m_max 4, Ω₀ 100 | 91 (23) | 1,529 | −3,181 (156) | 119 | 3,215 |
| m_max 2, Ω₀ 300 | 158 (67) | 1,820 | −2,945 (203) | 0 | 1,627 |
| m_max 2, Ω₀ 100 | 152 (65) | 1,856 | −3,151 (213) | 34 | 1,676 |

Both settings keep the loop honest (1.1.0 control: 650) and both end with two members on duty, two
probationers, and member seats sized below one. m_max 2 costs about 60 more false approvals and gains about
300 vested cases; **two thirds of its false approvals are probationers'** (65 against 23 at m_max 4), because
the pinned audits need a panel-eligible member free to take them and at m_max 2 fewer are seated — the
probation safety of Hypothesis 5 binds on member availability before it binds on the cap. Ω₀ 100 against 300
changes only the unfunded plants (119 against 49 at m_max 4); on the 1.3.0 count of 15 per plant the smaller
float is nearly enough.

**Red team (run 6).** Camouflage (10% random rejections) under the gate: at 50/50 −1,997 (91) against
−2,132, false approvals 37 against 53, false rejections 25 against 16 — an edge of about 130 per actor, no
safety; at 90/10 −1,096 (173) against −1,321. The reformer — a stamper that reviews carefully on probation and
stamps again once readmitted — is readmitted about 20 times a run (mean cycle 150–170 ticks), reaches one or two
probationer false approvals per run, and ends 1,700–1,970 per actor poorer than the careful at 50/50, 60/40 and
90/10 (0 of 20 richer): the cycle's yield is the fee and uplift of about 40 probation reviews a run against the
awards lost in between.

**What run 5 leaves.** The gate does what it was for: the contest is decided at every split and the population
converges to honesty in under a thousand ticks. Three things for the next design decision, in order: (1) **the
slowness** — awards unfilled 80–90% of ticks at 60/40 and worse above; the shrinking of the market to its honest
core is now the cost, and the one Baruchi has reserved a direction for; (2) **probation safety binds on member
availability** — at m_max 2 two thirds of false approvals are probationers' whose pinned audits found no free
member; member seats are sized on demand but the members are busy delivering; (3) the two implementer's
readings above (the cap's floor; the outgoing probationer stays) need confirming or replacing. The reviewer
notes are `agentic_sim/results/studies/1.3.0-membership-notes-for-reviewer.md`. Untouched: §18.1 questions 2,
4, 5, 7, 10.

## Design revision 4 — the orchestrator's troops (1.4.0, October 17, 2026)

The fourth use of §19's path, the first to add a participant, and the remedy revision 3 reserved. Run 5's
two shortages — the audit nobody was free to take when a probationer approved, the award nobody was free to
accept when a customer posted — are one shortage: the market's only source of capacity was its own members.
Baruchi's answer: the orchestrator is like the government; it has **troops** — ELEF's own servers, honest by
construction, not paid as reviewers, used as few as possible and retracted as early as possible. The
revision: a **rolled audit is an obligation of the case** (the window does not close until an audit completes;
the drivers had dropped a roll that found no auditor since run 1 — a conformance correction as much as a
rule); a required seat unfilled for w_R ticks, or a root request unawarded for w_A with no free fundable
member, is taken by a troop **the engine summons** when the duty fund can carry its cost and bond, with Ω's
advance up to A_T; the troop's verdict and delivery are the driver's declared disposition (truth w.p. 1 − ε_T,
failure at b); the **fund is the troop's wallet** and carries troops first — costs and locks at summons, the
advance repaid, then uplift from above the troops' reserve R_T; a troop claims no emission or uplift, never
touches a plant, never audits a troop reviewer's approval of a troop's delivery (that seat waits for a member
and is counted), accepts every verdict on its own work **at the verdict** (the external reviewer's note at
acceptance), and is counted in public: troop-ticks, troop shortfall, cases held for the market's audit.
Patch **1.3.1** (the two run-5 readings confirmed) was applied first.

**Reviews.** rc.1 (`spec/design_revisions/dr4_1.4.0-rc.1-review.md`): "unverified by the market" let a
troop-reviewed troop delivery vest unaudited against its own §2.2 and I25; who summons and who answers was
unstated; the troop's cost was called a burn; the held case's fate was unsaid; why minor; w_R = d̄ = 2 where
reviews take one tick, B̄ = β in the drivers, no troop audits the state's own work. rc.2 adopted all of it and
the smaller points (the obligation as a conformance correction with the controls re-run, panels with troops,
A_T named, Hypothesis 4's size). The external reviewer: "Clean. Nothing to change in the text" — one note,
acceptance at the verdict — "accept rc.2, implement."

**Chosen at implementation (Appendix I).** A troop reviewer's approval of a member's work carries
min(1, m p_floor) — the odds a reviewer whose record stood would carry — since a troop has no p_j. A seat's
wait is counted in seating steps. A troop resumes its seat when its P or ⊥ is answered by a resubmission.
I25's pinned-approval clause is the driver's conformance, not an engine predicate: the engine cannot hold an
obligation an orchestrator never rolled, and the reviewer tests are such worlds — the engine does record the
obligation itself for the state's own work, where odds 1 is a rule and not a roll.

**Engine (commit after `0589ef2`).** `roll_audit`, `audit_odds`; troop ids aliased to the fund's wallet in the
ledger (I15 reconciles through the alias); `_summon_troops` at step 5 after the seating with the windows, the
free-reviewer and free-member tests, β ≥ B̄, the fund's carrying capacity and the advance; the troop's cost
as a purchase; emission and uplift exclusion; the fund's order; a troop's delivery final N at any verdict but
F; every reviewer lookup guarded; I24, I25; I9, I22, I23 amended. `test_v14` (10); the equivalence scenario
rolls as obligations and summons troops; goldens re-pinned once. 218 passed, 26 expected failures.
Consolidated text `spec/agentic_economics_loop_spec_v1_4_0.md` (§1, §2.1, §2.4, §4.4, §5.2, §7.1, §7.7, §8.3,
§10.4, §12.3, §16, §17, §18.1, §20, Appendices A–D, I); 1.3.1 to history.

**Driver.** Rolls on `audit_odds`, records the roll, never drops it; supplies troop verdicts and submissions;
`--rules 1.4.0|1.3.0|1.2.0|1.1.0` (the obligation holds in every mode), `--troops`, `--eps-t`, `--w-r`,
`--w-a`, `--c-t`, `--c-d-t`, `--a-t`; troop columns. One smoke run at 60/40, seed 1, truthful appeals: vested
2,321 (1.3.0 with the roll held: 1,887; 1.2.0 in run 4: 2,410); troops delivered 1,116 tasks (806 vested, 290
final N — b plus the careful reviewers' false rejections, accepted at the verdict) and took 1,444 review seats;
false approvals 35, of them 6 by troops and 6 by probationers; the fund paid 10,456 in uplift — and **refused
8,739 award summonses and 2,686 seat summonses for want of funds**: the uplift drains the fund down to R_T
every batch, and R_T is the peak capital of troops that were fundable, so the reserve cannot grow past what it
has already carried. The treasury, not the market's need, sets the state's share. One seed, no conclusion —
but the first thing run 6 will measure.

## Run 6 — the revision's §8 under 1.4.0 (October 17, 2026)

`agentic_sim/results/studies/1.4.0-troops/` (and `1.4.0-troops.zip`): `controls/` (160 runs: 1.2.0 and 1.3.0 with
the roll held at 50–80%), `tipping/` (80), `adaptive/` (40), `drift/` (40), `windows/` (180), `cost/` (120),
`float/` (40), `redteam/` (120: camouflage 80, reformer 40), `ruling/` (160, after the reviewer's reply) — 940 runs, 20 seeds per cell, 20 actors, every
final audit passed, engine f0779ac. Appeals truthful, no disputes. The §6 reproduction is `test_v14`.

**The controls with the roll held barely moved.** 1.2.0: false approvals 53 / 67 / 89 / 121 at 50–80% (run 4:
53 / 67 / 89 / 121); 1.3.0: 53 / 66 / 90 / 112 (run 5: 53 / 69 / 90 / 113), probationers' 7 / 12 / 14 / 15
(run 5: 7 / 15 / 14 / 16). The dropped roll was hiding almost nothing at m_max = 4; what it hid was the m_max = 2
drift of run 5 (65 of 97). Every comparison below is against these.

**The tipping point.**

| stampers | 1.4.0 vested / 1.3.0 / 1.2.0 | troop deliveries (vested) | state's share of vested work | FA 1.4.0 / 1.3.0 (probationers') | troop FA | stamper − careful 1.4.0 / 1.3.0 | members' awards 1.4.0 / 1.3.0 | careful fees + uplift | award summonses refused for funds (case-ticks) |
|---|---|---|---|---|---|---|---|---|---|
| 50% | 2,136 / 1,923 / 2,399 | 349 (257) | 12% | 42 / 53 (7 / 7) | 2 | −2,761 / −2,130 | 164 / 152 | 1,921 (545) | 7,243 |
| 60% | 2,237 / 1,719 / 2,412 | 828 (613) | 27% | 49 / 66 (7 / 12) | 4 | −3,196 / −2,386 | 147 / 153 | 2,549 (922) | 8,768 |
| 70% | 2,361 / 1,443 / 2,396 | 1,390 (1,033) | 44% | 69 / 90 (12 / 14) | 4 | −3,965 / −2,489 | 118 / 145 | 3,691 (1,666) | 4,888 |
| 80% | 2,376 / 1,173 / 2,024 | 1,784 (1,338) | 56% | 98 / 112 (13 / 15) | 5 | −5,094 / −2,426 | 73 / 137 | 5,392 (2,709) | 4,832 |

*Hypothesis 2 holds:* vesting recovers to the 1.2.0 control at 50–70% and above it at 80%, and the state's
share reads the capture — 12% of vested work at 50/50, 56% at 80/20. *Hypothesis 1 holds in rate, not in
count:* false approvals fall below the controls (troop reviewers at ε_T = 0.05 and no dropped audit), but the
probationers' count is unchanged at m_max = 4 because there was little to close there; in the m_max = 2 drift
(below) the count stays at 62 while throughput doubles, so the rate per vested case halves (3.6% → 1.7%) — the
residual is now the audit's 5% miss and the ruling's 20% error, not the missing auditor. *Hypothesis 4 holds
in sign and fails in its clause:* the gap widens by the uplift as predicted (545–2,709 per careful actor), but
members' awards are **not** unchanged — at 70–80% they fall by a fifth to a half (118 and 73 against 145 and
137), because every troop delivery needs an initial review and most need an audit, and that work keeps the
members on duty; careful wealth still rises (fees 5,392 against 1,602 at 80/20). *Hypothesis 5 fails:* the
fund refuses thousands of award summonses at every split (4,800–8,800 case-ticks a run) while paying 6,400–12,700
in uplift. The reserve R_T is the peak capital of troops that *were* fundable; the uplift drains the fund to it
every batch; so the fund can never carry more troops than it once did — a self-limiting reserve. The treasury,
not the market's need, sets the state's share. *Hypothesis 6 holds:* cases held for the market's audit live 6–16
ticks at most, and the held count at any tick is 0–1.

**Adaptive dispositions** (3,000 ticks): under 1.4.0 the stamper share reaches ≤ 10% at a mean tick of 900 in
20 of 20 (1.3.0 with the roll held: 870); troops are active about 0.9 at a time at ticks 500 and 1,000 and
**zero from tick 1,500** in every seed; vesting 7,203 against 7,138. *Hypothesis 3 holds:* the state retracts on
its own, within a few hundred ticks of the market turning honest.

**Drift** (50% → 90% over 1,500 ticks):

| m_max | FA (probationers', troops') | vested 1.4.0 / 1.3.0 / 1.2.0 / 1.1.0 | troop deliveries (vested) | troop audits | award summonses refused | fund paid out | stamper − careful |
|---|---|---|---|---|---|---|---|
| 2 | 157 (62, 8) | 3,621 / 1,856 / — / — | 2,527 (1,950) | 407 | 21,883 | 15,065 | −6,763 |
| 4 | 78 (22, 7) | 3,494 / 1,506 / 2,518 / 4,209 | 2,942 (2,206) | 407 | 10,197 | 22,334 | −10,595 |

Vesting doubles against 1.3.0 and reaches 85% of the 1.1.0 control's at m_max 4 with false approvals at an
eighth of its; the state delivers 55–60% of what vests at 90% stampers and says so. At m_max 2 the
probationers' 62 false approvals are 1.7% of vested work (run 5: 3.6%).

**Windows** (60/40, w_R × w_A): w_R decides the state's share of *reviewing* — 1,410–1,450 troop review seats a
run at w_R = 1 against 760–990 at w_R = 4 — with vesting almost flat (2,210–2,342) and false approvals
46–66; w_A barely matters (troop deliveries 700–1,030 across its range), because the fund, not the window,
limits deliveries. At w_R = 1 the troops take the market's ordinary slack, as the revision warned; the members'
awards rise (170 against 113–121) because troops carry the reviewing. w_R = 2, w_A = 2 is a reasonable middle.

**Cost and competence** (60/40): c^D_T = 20 makes a delivery a loss in expectation (0.8 × 0 − 0.2 × 30) and the
fund stops carrying — troop deliveries 209 against 828 at c^D_T = 10 and 950 at 5, award summonses refused
23,900, vesting back to 1,894 (the 1.3.0 level). ε_T = 0.10 doubles troops' false approvals (3–4 → 6–8) and
adds 20–30 false rejections; everything else within noise. **A_T** 300 against 100 at 80/20: refused award
summonses fall from 4,832 to 1,640 but troop deliveries do not move (1,805 against 1,784) — the advance is
not the binding constraint; the fund's inflow against its uplift is.

**Red team.** Camouflage under troops buys nothing (−2,882 against −2,761 at 50/50; −7,221 against −7,559 at
90/10). The reformer is readmitted 29 times a run at 60/40 and 55 at 90/10 and ends 2,375 and 3,953 poorer;
probationers' false approvals in the all-troop corner (90/10) are 4, troops' 6, held-for-market-audit age at
most 21 ticks, vesting 2,424 (1.3.0: 1,352).

**What run 6 leaves — three findings for the next decision, in order.**

1. **The fund's reserve is self-limiting.** R_T is the peak capital of fundable troops and the uplift drains
   the fund to it every batch, so the treasury can never carry more troops than it once did, however many the
   market needs; A_T does not help, and c^D_T = 20 collapses it. Candidates, all design questions: a reserve
   sized to the *unmet* demand (the refused summonses) rather than the met one; uplift paid only when troop
   shortfall was zero in the period; or the raised tax split between the fund's reserve and the uplift.
2. **Troops consume member capacity.** Every troop delivery is reviewed, and every troop-reviewed approval of a
   member's work is audited at the floor: at 70–80% the members review more and deliver less. The
   "no crowding out" clause of Hypothesis 4 should be restated — the honest keep their income, but it moves
   from awards to fees — or the troops' reviews should carry less audit load (a default: the odds a troop
   reviewer's approval carries).
3. **The roll held changed little at m_max 4; the residual probation leak is mostly the auditor's, not the
   ruling's.** The reviewer asked for the sweep before any default moved; it is below. Ruling accuracy
   0.80 → 0.95 removes three quarters of the wrong rulings and a sixth of the probationers' false approvals
   at drift, none at the tipping cells. What reaches a customer through a probationer is the auditor's own
   miss — a member whose record has not yet failed, or a troop at ε_T — more than the ruling's.

**The ruling sweep** (`ruling/`, 160 runs, same seeds; the r = 0.80 cells reproduce the figures above to
the unit, engine code unchanged at results commit e9a4f85):

| cell | ruling accuracy | vested | FA | probationers' FA | troops' FA | false rejections | rulings (wrong) |
|---|---|---|---|---|---|---|---|
| drift m_max 2 | 0.80 / 0.95 | 3,621 / 3,608 | 157 / 142 | 62 / 52 | 8 / 8 | 90 / 77 | 176 (34) / 173 (9) |
| drift m_max 4 | 0.80 / 0.95 | 3,494 / 3,521 | 78 / 68 | 22 / 16 | 7 / 6 | 126 / 105 | 168 (34) / 161 (9) |
| 60/40 | 0.80 / 0.95 | 2,237 / 2,315 | 49 / 49 | 7 / 9 | 4 / 3 | 46 / 43 | 96 (19) / 102 (5) |
| 80/20 | 0.80 / 0.95 | 2,376 / 2,374 | 98 / 94 | 13 / 13 | 5 / 5 | 74 / 68 | 103 (19) / 101 (5) |

The leak does not close. Wrong rulings fall from 34 to 9 a run at drift, but probationers' false approvals
fall by ten and six, and at the tipping cells not at all; false rejections fall by a similar count, since a
wrong ruling cuts both ways. So the ruling is a sixth of the probationers' leak where it is largest, and the
rest is the audit itself: the auditor of a pinned approval is whichever member or troop was free, and a
member whose record has not yet failed approves what the probationer approved. A default of 1 − ε_T for the
ruling is not warranted by this; what would be is a reading of who audits pinned approvals, a driver column
the runs do not yet carry.

The reviewer notes are `agentic_sim/results/studies/1.4.0-troops-notes-for-reviewer.md`. Untouched: §18.1
questions 2, 4, 5, 7, 10.

## Design revision 5 — the reserve is sized to the need (1.5.0, October 17, 2026)

The fifth use of §19's path and the smallest: one rule. Run 6 showed the troops doing what revision 4 said and
the fund starving them by its own rule — R_T, the peak capital troops *had* carried, was what every batch drained
the fund to, so the peak could never rise, and the fund refused 4,800–8,800 award summonses a run while paying
6,400–12,700 in uplift; A_T was not the constraint. The design reviewer proposed the reserve sized to the
*attempted* demand; rc.1 (`uploads/`, headed "Proposed") was reviewed (`spec/design_revisions/dr5_1.5.0-rc.1-review.md`,
six points: a peak does not fall mid-period though the text said it did, and the trailing-period reading had to
be settled; "refused" means refused for funds; a case's demand is its unfilled seats; the refused cost is the
carry check's own need; §6 understated how long a delivery's capital is held; the leak reading should attribute
by gate before auditor kind); rc.2 adopted all six (`dr5_1.5.0-rc.2-review.md`: implementable as it stands) and
Baruchi relayed acceptance: "accept rc.2, implement".

**The rule (§12.3, I23).** At each seating the troop demand D_s is the capital live troops hold plus the cost of
the summonses the fund could not carry at that seating — refused *for funds*, each case once per seating at the
amount the carry check refused, a case's demand its unfilled seats (a panel short of both, two). R_T is the peak
of D_s over the *current* period, starting at the period's first seating from the standing demand (every troop
still in the field), the previous period dropped. The uplift is paid, as before, only from the unlocked balance
above R_T. A peak holds: the stock falls as the backlog is served, the reserve does not until the period ends — one
period's retention, the dial's own lag, as a feature. Also: Hypothesis 4 of revision 4 restated (the honest keep
their income; its composition shifts from awards to fees, bounded by the duty cap), and a reading — how a
probationer's false approval reached the customer: the pinned audit upheld it, or rejected it and the ruling
overturned; on the upheld route the auditor's kind (troop; member never suspended; member suspended later than the
audit, inside its lag; member readmitted before it). Rejected and recorded: uplift only when the period's
shortfall was zero (sawtooths); a fixed reserve/uplift split (blind to need); a stock-tracking reserve (kept for
Q13); the ruling's default to 1 − ε_T (the sweep did not earn it).

**Implemented** (`spec/agentic_economics_loop_spec_v1_5_0.md`; 1.4.0 to history; rc.2 verbatim as
`spec/design_revisions/dr5_the_reserve_is_sized_to_the_need_1.5.0.md`; Appendix J; §18.1 Q13 continued, Q14 new).
Engine: `_summon_troops` accumulates the refused `need` inside its pass and reads it with the capital held at the
end — `troop_demand_held`, `troop_demand_refused`, `troop_demand_now`; `R_T` is `troop_demand_peak`, reset at the
period's end to the capital still held before the same tick's seating; the period record carries `demand_peak`,
`demand_peak_refused`, `demand_last`; I23 checks R_T ≥ capital held and ≥ D_s. `Params.reserve_demand=False` is the
1.4.0 reading (the larger of this and the previous period's peak capital carried — the engine's 1.4.0 reading, now
recorded in Appendix I as superseded), the declared control `--rules 1.4.0`. `test_v15` (7). Suite 225 + 26.
Goldens re-pinned once (the uplift paid changes where a refusal occurred; the period record carries new readings).
Driver: the demand per tick; the route-and-kind attribution after the run; `--decline-awards <share>` (careful actors
that offer for nothing — the 1.5.0 red team); `--rules 1.5.0|1.4.0|1.3.0|1.2.0|1.1.0`. For the record: the uplift check
compares the fund's *unlocked* balance against a reserve that counts capital held (costs purchased plus locks), so
the fund's total when uplift resumes is about R_T plus the locks then held — as under 1.4.0.

## Run 7 — the revision's §8 under 1.5.0 (October 17, 2026)

`agentic_sim/results/studies/1.5.0-reserve/` (and `1.5.0-reserve.zip`): `tipping/` (160: 1.5.0 and the 1.4.0 control
on this engine at 50–80%), `windows/` (60: w_A ∈ {1, 2, 5} at 60/40), `adaptive/` (40: 1.5.0 and 1.4.0 at 3,000 ticks),
`drift/` (80: m_max ∈ {2, 4} under both), `redteam/` (140: decliners 40, flood 20, reformer 40, camouflage 40),
`ramp/` (2: the §6 pair at 60/40 seed 1, logged every tick) — 482 runs, 20 seeds per cell, 20 actors, every final
audit passed, engine 01b75e2. Appeals truthful, no disputes. The 1.4.0 control on this engine reproduces run 6 to the
unit (vested 2,136 / 2,237 / 2,361 / 2,377; refusals 7,243 / 8,768 / 4,888 / 4,832), so `Params.reserve_demand=False` is
a faithful control.

**The rule does what it says, and the fund still does not carry the need.** The engine's reserve tracks the demand
(`test_v15`), and in every run R_T rose to thousands when requests queued — and the troops delivered no more.

| stampers | vested 1.5.0 / 1.4.0 | troop deliveries vested | award summonses refused (case-ticks) | uplift paid | R_T at the end | members' awards | FA (probationers') |
|---|---|---|---|---|---|---|---|
| 50% | 2,175 / 2,136 | 305 / 257 | 7,995 / 7,243 | 6,818 / 6,396 | 2,567 / 542 | 163 / 164 | 42 / 42 (6.4 / 6.8) |
| 60% | 2,186 / 2,237 | 545 / 613 | 11,211 / 8,768 | 8,504 / 8,602 | 2,766 / 941 | 153 / 147 | 47 / 49 (8.2 / 6.9) |
| 70% | 2,347 / 2,361 | 1,031 / 1,033 | 8,846 / 4,888 | 11,564 / 11,409 | 905 / 650 | 121 / 118 | 66 / 69 (9.8 / 11.6) |
| 80% | 2,375 / 2,377 | 1,331 / 1,338 | 5,777 / 4,832 | 12,556 / 12,738 | 712 / 751 | 74 / 73 | 96 / 98 (11.8 / 12.8) |

*Hypothesis 1 fails.* Refusals rise, deliveries do not, vesting is identical, the uplift paid is identical. **The §6
ramp** (60/40 seed 1, `ramp/`): the first refusal at tick 423 under both rules; the demand stock peaks at 3,568 (1.5.0;
the 1.4.0 run reads 5,452 — the readings run in both modes), not 270; troops in flight peak at 94 (1.4.0: 133), not
13; the uplift is paid in 393 of 1,000 ticks (1.4.0: 477); vested 2,274 against 2,321; troop deliveries 719 against
806; refused 12,801 against 8,739; the request backlog 133 against 49; reviews that found no reviewer 8,383 case-ticks
against 9,428. Per period under 1.5.0 the peak demand ran 1,500 → 3,568 → 2,988 → 3,396 → 2,820, R_T at the period's
end 0 / 1,140 / 0 / 944 / 440 / 0 / 2,000, and the uplift paid 117 / 599 / 296 / 3,135 / 1,152 / 3,146.

Three things the text did not see, each upstream of the reserve:

1. **The demand stock counts the queue.** A request has no expiry; at 50–60% the queue of open cases is ~300 and each
   waiting request is refused at every seating, so D_s is the queue's price — thousands — and R_T is a number the fund's
   inflow (3 of tax plus troop earnings a tick) can never reach in a period. The uplift stops, as designed; the fund
   carries all it can — 59–94 deliveries at once, 1,200–1,900 of capital against the §6 steady 270 — and the backlog
   still grows. §6's "one extra delivery a tick" assumed the flow; the engine met the stock.
2. **The reviewing seat is the cap.** On duty 4.5–5 (X_t ≈ 5), audits assigned 1,800–2,150, reviews that found no
   reviewer 7,300–11,400 case-ticks a run under both rules at every split. A troop's delivery waits for its initial
   review and then its pinned audit; its capital stays held; cash tied up in deliveries waiting for review is cash the
   fund cannot put into a review seat (seat refusals 290–530) or the next delivery. Vesting is pinned at 2.2–2.4 a tick
   by the market's reviewing capacity whoever delivers. Run 6's "troops consume member capacity" was this, seen from
   the other side.
3. **The boundary reset saw-tooths.** The peak restarts at the standing demand *at one seating*; when the in-flight
   cohort has just vested, the standing demand is near zero and the whole accumulated balance pays out in one batch
   (3,135 and 3,146 in two of the ramp's periods, at 60/40 where the fund was refusing nine summonses a tick). This is
   the sawtooth rc.2 rejected for the shortfall-zero rule, arriving by the reset instead. The 1.4.0 two-period reading
   damped it; one period does not.

**Windows** (60/40): w_A = 1 / 2 / 5 → vested 2,112 / 2,186 / 2,063; troop deliveries 432 / 545 / 373; summonses 598 /
732 / 507; refused 15,253 / 11,211 / 13,845. *Hypothesis 2 fails:* the window is not a knob while the review seat and
the cash tied in deliveries bind; a shorter window summons more and is refused more.

**Adaptive** (3,000 ticks): ≤ 10% stampers at a mean tick of 890 (1.4.0: 900), 20 of 20; troops active 0.05 / 0 /
0.05 / 0 at ticks 500 / 1,000 / 1,500 / 2,000 (1.4.0: 0.9 / 0.95 / 0 / 0); R_T 0–4 from tick 1,000 on; vested 7,187
against 7,203; false approvals 74 against 77. *Hypothesis 3 holds* — and under 1.5.0 the troops are gone sooner, since a
backlog peak stops the uplift and the fund's cash goes into the few deliveries, not the many.

**Drift** (50% → 90%): m_max 2: vested 3,566 / 3,621, false approvals 154 / 157 (probationers' 58 / 62, troops' 6 / 8),
troop deliveries 1,884 / 1,950, refused 40,071 / 21,883; m_max 4: 3,495 / 3,494, 81 / 78 (24 / 22), 2,190 / 2,206,
11,911 / 10,197. Same market, twice the refusals.

**Q14 — how a probationer's false approval reaches the customer** (the route-and-kind reading, both rules alike):

| cell | probationers' FA | audit upheld | audit rejected, ruling overturned | upheld by: troop / member never suspended / member suspended *later* / readmitted |
|---|---|---|---|---|
| drift m_max 2 | 58–62 | 51–56 | 6.5–6.8 (11%) | 3.4–3.9 / 3.4–9.6 / **42.6–44.0** / 0 |
| drift m_max 4 | 22–24 | 19–20 | 3.0–3.8 (15%) | 3.4–4.6 / 1.1–1.4 / **14.6** / 0 |
| 50–80% fixed | 6–13 | 6–12 | 0.6–1.4 (10–13%) | 0.1–0.7 / 1.8–2.5 / **3.2–9.1** / 0 |

*Hypothesis 4 holds in its first clause and fails in its second:* the member inside its detection lag — one whose
record fails *after* it audited — carries 73–80% of the upheld route under drift **and 55–75% at the fixed splits
too**. At a fixed split the lagging member is a stamper not yet caught by the plant record, not a careful actor turned;
the lag is the record's, not the drift's. A member in standing misses 2–3 a run; a troop under 1; the ruling 10–15%.
Readmitted members audited none of them.

**Red team.** *Decliners* (careful actors that offer for nothing, 60/40): a quarter of them (two actors) end 901
poorer than the careful who offer (3,461 against 4,362), troop deliveries 458 against 545 and refusals double
(23,820); half of them (four) end at 2,163 against 4,203, troop deliveries collapse to 17, vesting falls a quarter
(1,649), the backlog reaches 986 and the stampers get richer (1,817 against 1,389) — fewer awards, less tax, a fund
that cannot carry. Declining loses 20 an award and gains almost no uplift, as predicted; it also starves the state.
*A requester flood* (six tasks a tick): vested 2,642 (+21% on three a tick), refused 83,924, backlog 2,812, R_T 18,088,
uplift paid 6,912 (less than at three), reviews unassigned 64,547 case-ticks; stampers 2,647 (more awards for all),
careful 4,352 (less uplift). Not served and not an exploit: the review seat caps it, the reserve becomes the queue's
price, the uplift is throttled. *The reformer* is readmitted 28 (60/40) and 56 (90/10) times a run and ends 2,479 and
3,958 poorer than careful; probationers' false approvals 0.7 and 3.8. *Camouflage* 0.1 costs its user (1,287 against
1,417 at 50/50); held-for-market age reaches 53 at 90/10.

**What run 7 leaves — for the next decision, in order.**

1. **The queue, not the reserve, is the design question.** Demand measured on a never-expiring stock is unbounded,
   and a reserve sized to it is "retain everything" until a boundary. Candidates, all rules: a request unawarded for
   some T withdraws (the human's `withdraw` exists; §6.1 has no such deadline and the drivers never use it); or D_s
   counts the refused *flow* — cases first refused in this period — not the stock; or the refused component is capped
   at what the fund's period inflow could carry.
2. **The reviewing seat is the throughput cap** at every split under every rule since 1.3.0: X_t ≈ 5 on duty, the duty
   cap ⌈E_t/2⌉, and audits of every pinned and every troop approval. The 1.4.0 text left "whether the duty cap should
   loosen now that the floor is the state" open; the evidence now says the cap, not the fund, sets the market's size.
   The reserve rule is downstream of this and cannot fix it.
3. **The boundary reset.** Restart at the standing demand of one seating saw-tooths; the two-period reading damped it.
   A reset to max(standing demand, a fraction of the last peak), or a decayed peak — the "reserve that tracks the stock"
   rc.2 recorded and rejected — is the smaller fix, once 1 is settled.
4. **Q14 is answered and it is not the ruling and not the drift.** The leak through probation is the plant record's
   detection lag on the *auditor*: a pinned approval audited by a member whose record has not yet failed. Whether a
   pinned approval's auditor should itself have a determined record is now the question the text deferred.

The reviewer notes are `agentic_sim/results/studies/1.5.0-reserve-notes-for-reviewer.md`. Untouched: §18.1
questions 2, 4, 5, 7, 10.

## Design revision 6 — auto-scale (1.6.0, October 17, 2026)

The sixth use of §19's path and the largest since 1.3.0: five rules, each behind a flag so that run 8 can say which
did what. Run 7's finding was that the reviewing seat, not the treasury, caps the market — reviews that found no
reviewer 7,300–11,400 case-ticks a run, the open-case queue ~300, vesting pinned near the posting-rate ceiling whoever
delivered, twelve probationers idle while reviews waited — that the demand stock counted a never-expiring queue, that
the one-period reset saw-toothed, and that the probation leak was the plant record's detection lag on the auditor
(55–75% at fixed splits, 73–80% under drift). Baruchi's reading: a request on hold is a problem for the network's
rating — re-queue it with priority and have the orchestrator take some of the blame in money; and if ELEF controls the
network and the servers, allow auto-scale. The design reviewer's rc.1 was reviewed (`spec/design_revisions/
dr6_1.6.0-rc.1-review.md`: seven points — the determined-record panel rule refused every panel seat in a world that had
not planted, every reviewer test and the first period of every run; Ω's order named a plant cap the engine lacks and
would spend the honesty clock under stress; Hypothesis 1 asked for vesting above the 2.4 ceiling, the seat costs the
queue not the rate; the delivery check's advance; a clock with no verdict; withdrawal is of unawarded requests; the cold
start is every run's first period), rc.2 adopted all seven (`dr6_1.6.0-rc.2-review.md`: implementable as it stands),
and the design reviewer relayed acceptance: "accept rc.2, implement … the one-factor-at-a-time cells first, every
comparison against run 7 read from the second period on".

**The rules (§3.1, §6.1, §7.1, §10.4, §12.1, §12.3, I26).** *The service clock:* every root request is timed from
posting to its first verdict or its final without one, oldest first in every pass; past T_s = 8 the orchestrator owes
the requester r_s = ω₀B a tick, capped at B, from Ω when the clock stops or as Ω's liability; a request withdrawn before
award is owed nothing; the clock runs only while β ≥ B̄. *Auto-scale:* A_T removed — Ω backs the fund from its balance
above a plant reserve, in a stated order (the reserve; liabilities older than a period; inspection seats, then
deliveries; younger liabilities); review seats are summoned before deliveries; a delivery is summoned only when the fund
plus Ω's available advance can carry its own 20 and two review seats (36), drawing only its own shortfall. *Seat the
queue:* the reserve target is at least the reviews waiting, by kind, plus the period's initial rate, at every rotation;
probationers are seated as far as the queue needs. *A panel seat requires a determined record* (≥ n_min bad plants
seen), dormant until the world's first plant is adjudicated — so in every run the first period's panels are the
state's, and §8 reads from the second period on. *R_T over two periods* (the 1.4.0 reading restored). The members' duty
cap keeps its rule and its default is swept against ⌈2E_t/3⌉ and E_t for Baruchi's decision; Ω₀ 300 against 1,000;
θ_panel and the record window for the drift lag. Rejected and recorded: requests expire; members earn less while the
state scales; a rebate before anything was bought; lateness measured to the award.

**Implemented** (`spec/agentic_economics_loop_spec_v1_6_0.md`; 1.5.0 to history; rc.2 verbatim as
`spec/design_revisions/dr6_auto_scale_1.6.0.md`; Appendix K; I26; §18.1 Q11 restated, Q15 and Q16 new). Engine: the
clock in the summons pass with three stops (`_initial_verdict`, `_finalize_N`, and `_vest` for a human's override with
no initial verdict — the case the text's two stops did not name), the rebate transfer and the liability list serviced
oldest first before and after the pass, the I10 exemption for a liability serviced after vesting; `_omega_available()`
above `_plant_reserve()`; the pass in two loops with the priority check; the delivery check; `_reserve_target()` and
`_waiting_reviews()` by kind at every rotation; `panel_eligible` with determination behind `first_plant_adjudicated_at`;
`R_T` over two periods; `duty_cap_frac`. I9, I22, I23, I24 amended; I26 new. `test_v16` (11); suite 236 + 26; goldens
re-pinned once; reviewer tests untouched and passing; `test_v12`–`test_v15` pinned to their revisions' mode. Driver:
`--rules 1.6.0` with one flag per rule, `--duty-cap`, `--t-s`, `--plant-reserve`, `--beta-low/--beta-low-share`, the
rating and Ω columns.

**Three implementer's readings, flagged.** (1) *The plant reserve's horizon.* The text says π_t × initial rate ×
(φ^E+φ^F) × *the ticks remaining in the period*; a plant's pots return to Ω at its closure, so the clock's need at once
is a plant's life of plants. The literal horizon at 60/40 is about 360 — more than Ω₀ = 300 — and the state cannot
advance at all; the engine's default is a plant's life, W + T_review = 15 ticks (`plant_reserve_life`), and the literal
formula is kept as the declared cell `--plant-reserve period`, run in §8.1 beside the others. This is my own rc.1 point
2 adopted too literally, and the reviewer should rule on it. (2) *Reviews waiting by kind*, I9 per kind under the cap.
(3) *The 1.5.0 control* turns all five flags off with A_T binding and the one-period reset. A first smoke at 60/40 seed
1, for orientation only: on-time share 0.40, mean lateness 46, Ω's liabilities 28,000 against Ω's balance of 11, troop
deliveries 1,102 summoned and 827 vested (1.5.0: 719), reviews unassigned 7,557 case-ticks still, the queue 256 — the
seat is still short because the reserve can only seat eligible actors and after the stampers' suspensions there are
few, and because one idle member at the seating blocks every award summons however long the queue. Read with the sweeps.

## Run 8 — the revision's §8 under 1.6.0 (October 17, 2026)

`agentic_sim/results/studies/1.6.0-autoscale/` (and `1.6.0-autoscale.zip`): `ofat/` (140: the 1.5.0 control, each
rule alone, all five with the text's literal plant-reserve horizon, at 60/40), `tipping/` (80, logged every 20 ticks
for the ramp), `cap/` (80), `float/` (240: Ω₀ {300, 1,000} × T_s {5, 8, 12} at 60/40 and 80/20), `windows/` (40),
`drift/` (120: m_max {2, 4} × default / θ_panel 0.15 / window 12), `adaptive/` (20), `redteam/` (120) — 840 runs, 20
seeds per cell, 20 actors, every final audit passed, engine 195896a. Appeals truthful, no disputes. The 1.5.0 control
on this engine reproduces run 7's 60/40 cell to the unit. Every comparison is read from the second period on where it
matters (§2.4); the first period is the same in every cell: on time, panels the state's, Ω above 700.

**One factor at a time, 60/40, against the 1.5.0 control** (the cells the reviewer asked to read first):

| cell | vested | open cases | reviews unassigned (case-ticks) | troop deliveries | award summonses refused | FA (probationers') | members' awards | Ω at the end | Ω's liability | plants unfunded |
|---|---|---|---|---|---|---|---|---|---|---|
| 1.5.0 control | 2,186 | 298 | 11,423 | 545 | 11,211 | 47 (8.2) | 153 | 1,004 | — | 34 |
| clock alone | 2,151 | 320 | 6,777 | 514 | 8,184 | 46 (7.8) | 151 | 57 | 13,810 | 136 |
| Ω's backing alone | 2,284 | 152 | 8,874 | 691 | 4,054 | 47 (7.3) | 141 | 1,134 | — | 9 |
| seat the queue alone | 2,058 | 455 | 6,843 | 637 | 36,373 | 71 (6.4) | 161 | 971 | — | 0 |
| panel rule alone | 2,016 | 433 | 17,251 | 631 | 19,642 | **14 (5.0)** | 176 | 1,150 | — | 80 |
| two-period reserve alone | 2,189 | 288 | 11,082 | 550 | 9,082 | 51 (8.2) | 151 | 1,064 | — | 28 |
| all five, literal horizon | 2,259 | 92 | 7,760 | 1,010 | 12,330 | 12 (3.4) | 141 | 754 | 24,839 | 22 |
| all five (tipping 60/40) | 2,269 | 94 | 7,746 | 999 | 13,049 | 13 (3.6) | 151 | 94 | 19,778 | 81 |

*The panel rule is the honesty gain:* alone it cuts false approvals by 70% and the probationers' by 40%, with the queue
longer because undetermined members cannot fill panel seats and the fund-limited troops are slow to. *Ω's backing alone
is the capacity gain:* the queue halves, refusals fall by two thirds, troop deliveries rise a quarter, Ω stays above
1,000. *The clock alone bankrupts Ω:* liabilities 13,800 against a balance of 57, plants unfunded quadrupled. *Seat the
queue alone hurts:* more actors on duty, fewer free to deliver, three times the refusals, false approvals up by half.
*The two-period reserve alone is a wash.* Together, the five give the honesty of the panel rule and the queue of the
backing, and the clock's liability on top.

**The tipping point under 1.6.0** (1.5.0 in brackets):

| stampers | vested | open cases | reviews unassigned | on-time share | mean lateness | Ω's liability | Ω at the end (min) | plants unfunded | troop deliveries | FA (probationers') | lagging-auditor kind | members' awards | stamper wealth |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 50% | 2,178 (2,175) | 208 (313) | 6,238 (11,431) | 0.40 | 48 | 26,100 | 87 (41) | 151 | 671 (305) | 12 (3.5) [42 (6.4)] | 0 [3.6] | 162 (163) | 714 (1,417) |
| 60% | 2,269 (2,186) | 94 (298) | 7,746 (11,423) | 0.60 | 38 | 19,778 | 94 (48) | 81 | 999 (545) | 13 (3.6) [47 (8.2)] | 0 [4.3] | 151 (153) | 770 (1,389) |
| 70% | 2,293 (2,347) | 44 (55) | 5,976 (7,581) | 0.80 | 21 | 5,587 | 413 (347) | 14 | 1,302 (1,031) | 16 (3.5) [66 (9.8)] | 0 [6.7] | 118 (121) | 863 (1,347) |
| 80% | 2,282 (2,375) | 40 (41) | 5,875 (7,322) | 0.90 | 21 | 5,422 | 590 (550) | 13 | 1,590 (1,331) | 17 (6.5) [96 (11.8)] | 0 [7.7] | 52 (74) | 911 (1,394) |

*Hypothesis 4 holds in full:* the lagging-auditor kind is zero at every split (run 7: 3.6–9.1 of 6–12 upheld), and
false approvals fall by 72–82%. The stampers end 45% poorer than under 1.5.0. *Hypothesis 1 holds in part:* the queue
falls by a third to two thirds at 50–60% and reviews unassigned by 30–45% — not to a few hundred; vesting is at the
ceiling as predicted. *Hypothesis 2 is inverted:* the on-time share is 0.9 at 80/20 and 0.4–0.6 at 50–60%, with mean
lateness 38–48 ticks and Ω insolvent — liabilities 20,000–26,000 against a balance near 90, plants unfunded 80–150 a
run (the must-be-zero reading fails). At 80/20 the four members are all on duty by the cap's floor, the state delivers
everything, and from the fourth period on every request is on time; at 50–60% the half cap leaves members delivering
slowly and audits waiting. *The ramp (Hypothesis 5) is every run's first period:* on-time 1.00, 480–550 panel seats the
state's, no troop deliveries, Ω above 700, queue 35; the collapse comes in periods 2–3 as the stampers' records
determine and the market shrinks to its honest core; at 80/20 it recovers to on-time 1.00 by period 4, at 50–60% it
does not.

**The cap** (60/40 and 80/20; the half cap is the tipping cell):

| cell | open cases | reviews unassigned | on-time | lateness | Ω's liability | Ω at the end | troop deliveries | members' awards / delivery income / fees | careful wealth | FA |
|---|---|---|---|---|---|---|---|---|---|---|
| 60/40 half | 94 | 7,746 | 0.60 | 38 | 19,778 | 94 | 999 | 151 / 1,755 / 2,919 | 4,956 | 13 |
| 60/40 two thirds | 44 | 3,424 | 0.90 | 8 | 3,512 | 47 | 1,282 | 111 / 1,755 / 3,336 | 4,808 | 13 |
| 60/40 all | 50 | 3,335 | 0.80 | 13 | 6,809 | 30 | 1,382 | 94 / 1,498 / 3,356 | 4,614 | 13 |
| 80/20 half | 40 | 5,875 | 0.90 | 21 | 5,422 | 590 | 1,590 | 52 / 683 / 6,323 | 6,945 | 17 |
| 80/20 two thirds | 40 | 5,360 | 0.90 | 7 | 1,409 | 1,135 | 1,551 | 43 / 684 / 6,392 | 6,881 | 17 |
| 80/20 all | 39 | 5,520 | 0.90 | 8 | 1,335 | 957 | 1,768 | 40 / 640 / 6,675 | 7,128 | 17 |

*Hypothesis 6 holds, and the two-thirds cap is the answer to run 7's seat:* at 60/40 it halves the queue and reviews
unassigned, lifts the on-time share from 0.6 to 0.9, cuts mean lateness from 38 to 8 ticks and Ω's liability by four
fifths, with honesty unchanged and the careful members' wealth within 3% — their income moves from awards to fees, as
1.5.0's restated hypothesis said. At E_t the state delivers everything and the honest inspect only; the numbers are
beside each other for Baruchi's decision.

**Float and target.** At 60/40, Ω₀ = 1,000 does not help: liabilities 18,000–19,400 against 19,800–22,400 at 300, Ω
ends near 100–190 at both, plants unfunded 72–97 at both; T_s moves nothing. At 80/20, Ω₀ = 1,000 ends at 850–1,120 and
liabilities 3,700–5,300 (300: 350–740 and 4,800–6,500); on-time 0.8–0.9 at every T_s. *The float is not the limit at
50–60%:* Ω's income (ω₀B a member award, about 2 a tick) against plant costs and rebates is, and no float changes a
flow. **Windows:** w_A = 1 / 2 / 5 → on-time 0.40 / 0.60 / 0.50, liabilities 25,500 / 19,800 / 23,600; *Hypothesis 3
fails again* — the window is not a knob while Ω is insolvent.

**Drift** (50% → 90%; 1.5.0 in brackets):

| cell | vested | open cases | on-time | FA (probationers', troops') | upheld / overturned | upheld by: troop / standing / **lag** | Ω's liability | plants unfunded |
|---|---|---|---|---|---|---|---|---|
| m_max 2 | 3,512 (3,566) | 38 (108) | 0.80 | 64 (37, 3.5) [154 (58, 6)] | 31 / 5.9 | 6.0 / 5.8 / **18.9** [3.9 / 3.4 / 44.0] | 13,104 | 20 |
| m_max 4 | 3,458 (3,495) | 41 (69) | 0.80 | 34 (19, 3.4) [81 (24, 7)] | 15 / 3.8 | 4.0 / 1.2 / **9.8** [4.6 / 1.1 / 14.6] | 7,915 | 67 |
| m_max 2, window 12 | 3,509 | 39 | 0.80 | 60 (33, 3.0) | 27 / 5.6 | 6.6 / 6.2 / **14.3** | 13,087 | 20 |
| m_max 4, window 12 | 3,430 | 44 | 0.90 | 28 (15, 2.6) | 12 / 2.9 | 4.7 / 1.9 / **5.7** | 7,080 | 68 |
| m_max 2, θ_panel 0.15 | 3,513 | 38 | 0.80 | 65 (37, 3.3) | 31 / 6.5 | 6.3 / 3.5 / **21.0** | 12,909 | 23 |
| m_max 4, θ_panel 0.15 | 3,448 | 44 | 0.80 | 32 (17, 3.5) | 14 / 3.2 | 5.5 / 0.9 / **7.3** | 9,155 | 84 |

False approvals fall by more than half; the lagging auditor still carries about 60% of the upheld route under drift, as
the text predicted; the shorter record window cuts it by a quarter to 40%, the lower threshold does little at m_max 2.

**Adaptive** (3,000 ticks): ≤ 10% stampers at tick 735 (1.5.0: 890), troops zero from tick 500 at the latest, R_T zero
from 2,000, false approvals 48 (74), open late requests zero from 2,000 — *Hypothesis 7 holds* for everything that is a
flow. The one stock does not clear: Ω's liabilities, accrued at 22,000 in the stressed early periods, stand at 26,000 at
the end, paid down at about 1.4 a tick from Ω's income.

**Red team** (60/40). *The below-market poster* (a fifth of requests at β = 10): its clocks do not run and it is owed
nothing, as expected; its unserved requests clog the queue to 482 and cost everyone 13% of vesting. *The flood* (six
tasks a tick): not served (queue 1,380, on-time 0.2), not an exploit (rebates paid 740; liability 75,600 is the
reading). *The late withdrawer* (H withdraws unawarded requests after 12 ticks): gains nothing, as expected — and Ω's
liability falls from 19,800 to **830**, mean lateness from 38 to 3.5 ticks, the queue from 94 to 43, at the cost of 11%
of vesting (362 requests withdrawn). *The decliner* ends 209 poorer than the careful who offer (1.5.0: 901); *the
reformer* 3,146 poorer than careful; *camouflage* buys nothing.

**What run 8 leaves — for the next decision, in order.**

1. **The clock's liability is a stock the orchestrator cannot pay down, and it lives in the stale unawarded request.**
   Ω's income is about 2 a tick; a late request accrues 1 a tick up to 20; at 50–60% the liability reaches 20,000–26,000
   and no float, target or window changes it, while the withdrawer's cell shows what bounds it: a request that waits
   unawarded past 12 ticks is the lateness. The rc rejected expiry for turning customers away; the data say the queue
   that never expires is also what the clock prices. A rule that re-queues or withdraws an unawarded request after some
   T, with the clock's stop at that point, is the candidate — the design reviewer's and Baruchi's "re-queue with
   priority" read literally.
2. **The members' duty cap at two thirds** fixes the seat at 60/40 with honesty unchanged and careful wealth within 3%;
   a default, and Baruchi's product decision with the numbers beside it. The reserve-sizing rule alone made things worse.
3. **The plant reserve's horizon** — the implementer's reading (a plant's life) is in force; the text's literal horizon
   leaves Ω nothing to advance at Ω₀ = 300 (the `ofat/` literal cell shows the same honesty, a shorter queue, and the
   fund carrying the troops on its own earnings). The reviewer should rule.
4. **Plants unfunded for want of Ω are not zero** at 50–60% (80–150 a run) and under drift (20–84): the honesty clock
   is being starved by Ω's poverty, not by the advances — the reserve cannot hold back money Ω does not have. Ω's
   income rule (ω₀B per award) is upstream of every 1.6.0 rule.

The reviewer notes are `agentic_sim/results/studies/1.6.0-autoscale-notes-for-reviewer.md`. Untouched: §18.1
questions 2, 4, 5, 7, 10.

## Design revision 7 — the state's earnings (1.7.0, October 18, 2026)

The seventh use of §19's path, and the one Baruchi named: *why should an inspector profit from something a troop did? from
their perspective it's just like any other actor in the system.* Run 8's finding (above) was that the panel rule is the
honesty gain and Ω's backing the capacity gain, and that the clock's liability is a stock the orchestrator cannot pay
down — the troops' net at 60/40, 6,200–6,800 a run, went to the market's reviewers as uplift by 1.4.0's clause that
nothing a troop earns reaches Ω, while the same Ω carried the rebates on about 2 a tick and ended near zero at 50–60%
with liabilities of 20,000–26,000 and plants unfunded. The design reviewer's rc.1 was reviewed
(`spec/design_revisions/dr7_1.7.0-rc.1-review.md`: one decision — the ω₀ sweep moved the rebate r_s = ω₀B and the
surcharge with the fee; one piece of run-8 evidence the text lacked — the two-thirds cap at 60/40 triples plants unfunded,
81 → 272, so Hypothesis 1's plants-zero edge is tight; four figures — R_T was 952–3,494 at 60/40, not 270, and its job had
changed; a troop review seat's earnings; the surcharge about 7 a tick so uplift falls by two fifths), rc.2 adopted all
five with the smaller points (`dr7_1.7.0-rc.2-review.md`: implementable; R_T redefined as the two-period peak of capital
held with its purpose stated, r_s pinned at 1 for the sweep, Ω's record by source), and the design reviewer relayed
acceptance: "accept rc.2, implement … the three OFAT cells first, plants unfunded read first, every comparison from the
second period on, and the state's share read beside the refusals".

**The rules (§4.1, §10.4, §12.1, §12.2, §12.3, I23).** *Two accounts again:* the duty fund is 1.3.0's uplift fund —
the raised tax in and nothing else, its whole balance out as uplift at every batch, no reserve, no lock; the troops'
wallet is a separate troop account — Ω's advances and every troop's earnings in; costs, locks, forfeits, burns,
repayments out; at each batch the unlocked balance above R_T flows to Ω. *The clause withdrawn:* a troop is an actor of
the state and its earnings are the state's; the guards that stand in its place (members first at every seat, the windows,
cost at summons, no emission/uplift/ρ/κ to a troop, the state's share public) plus one reading, Ω's income by source.
*R_T is capital held:* the two-period peak of costs purchased plus locks, every troop in the field; the 1.5.0 refused
component withdrawn (its reason went with A_T); its purpose now the troops' in-flight capacity shielded from the liability
queue. *Ω pays its debts from its income:* the 1.6.0 order unchanged and funded; the plant reserve's horizon ruled a
plant's life. *The cap* ⌈2E_t/3⌉. *ω₀ swept {5, 10, 15}% with r_s pinned at 1.* Three 1.6.1 wording items folded in.
Rejected and recorded: the fund paying rebates before uplift (the right money, the wrong pocket); the account as a
pass-through; expiry or admission control now — the cannot-serve protocol held as 1.8.0's candidate if 50/50's liability
does not clear.

**Implemented** (`spec/agentic_economics_loop_spec_v1_7_0.md`; 1.6.0 to history; rc.2 verbatim as
`spec/design_revisions/dr7_the_states_earnings_1.7.0.md`; Appendix L; §18.1 Q13 and Q16 continued, Q17 new). Engine:
`Params.troop_account` (on) and `duty_cap_frac` 2/3; the wallet `TROOP_ACCT` with troop ids aliased to it and the carry
check, the advance, its repayment, the delivery check, the lock reconciliation and `fund_flow` following it; the batch
pays the duty fund's whole balance as uplift and then `_pay_troop_surplus` sends the troop account's unlocked balance
above `R_T` to Ω; `R_T` the two-period peak of capital held under the flag; Ω's record by source in the period record;
I23 amended (the uplift fund equals the raised tax received less the uplift paid and holds no lock; `R_T ≥ D_s` retired
with the component). `test_v17` (8); suite 244 + 26 in all three modes; goldens re-pinned once (both factors move the
scenario: the account and the cap); reviewer tests untouched and passing; `test_v13`–`test_v16` pinned to the merged
fund and the half cap. Driver: `--rules 1.7.0` with `--accounts`, `--duty-cap` by the rules, `--omega-rate`, `--r-s`;
the account, surplus and income columns; `--rules 1.6.0` is the control.

**Found at implementation — a figure, not a rule, and my own error to report.** rc.2 §1.5, §2.1 and §6 say a troop
*review seat* nets nothing (fee 2 or 3 against a cost of 3), adopting my rc.1 review's point 4. The engine has reimbursed
a troop reviewer's cost from the requester's expense allowance like any reviewer's since 1.4.0 — 1.4.0 §6 and `test_v14`
say so ("−3 cost, +3 reimbursed, +3 fee") — so a troop review seat nets its fee, +3 for an audit, and under 1.7.0 that is
the state's too. The surplus is larger than the text says (about 1,950 troop review seats a run at 60/40 earned their
fees beside the deliveries' net); no rule moves; the consolidated text states the seat's earnings correctly, the accepted
text is kept verbatim with the note in Appendix L, `test_v17` pins the figure. A smoke at 60/40 seed 1, for orientation
only: Ω's liability 0 (rebates 2,314 paid at the stop, 2,230 serviced), plants unfunded 0, Ω net +1,966, troop surplus to
Ω 6,415, troop deliveries 1,729 against the control's 1,102 (award summonses refused 459 against 17,493), careful wealth
4,284 against 5,088 (awards 116 against 158, the uplift gone), reviews unassigned 4,224 against 7,557. Read with run 9.

## Run 9 — the revision's §8 under 1.7.0 (October 18, 2026)

`agentic_sim/results/studies/1.7.0-earnings/` (and `1.7.0-earnings.zip`): `ofat/` (80: the 1.6.0 control, the accounts
alone, the cap alone, both, at 60/40, logged every 20 ticks), `tipping/` (160: 1.7.0 and the 1.6.0 two-thirds control at
50–80%, logged every 20 ticks), `take/` (120: ω₀ {5, 10, 15}% × {50/50, 60/40}, r_s pinned at 1), `adaptive/` (20),
`drift/` (40), `redteam/` (100) — 520 runs, 20 seeds per cell, 20 actors, every final audit passed, engine 003a238. The
1.6.0 control reproduces run 8 to the unit. Read from the second period on. The notes for the reviewer are
`agentic_sim/results/studies/1.7.0-earnings-notes-for-reviewer.md`; the figures below are the headline ones.

**One factor at a time, 60/40** (plants unfunded / Ω's liability / Ω at the end / on-time from the second period on /
queue / troop deliveries / award summonses refused): the 1.6.0 control 81 / 19,778 / 94 / 0.47 / 94 / 1,353 / 13,049;
the accounts alone under the half cap **124 / 16,694 / 347 / 0.28 / 718 / 560 / 33,638**; the cap alone 272 / 3,512 / 47
/ 0.83 / 44 / 1,723 / 1,979; **both 0.7 / 317 / 4,352 / 0.89 / 42 / 1,719 / 607**, troop surplus to Ω 6,029, careful
wealth 4,250 (uplift 795 against 1,291). Both together do what Hypothesis 1 says: plants unfunded zero in 17 of 20
seeds (2, 4 and 8 in three; one seed tipped), the liability a few hundred, Ω above 4,000 through the last period. **The
accounts alone are worse than the control:** under the merged fund the troops were financed by the surcharge whatever
Ω owed; under the two accounts every summons beyond the capital held is Ω's advance, and Ω pays debts older than a
period first — once the half cap lets lateness accrue, the debts take Ω's income, the state cannot summon, and the next
period is later still. R_T as capital held (461) shields the in-flight cohort and nothing more; the cap is what keeps
the loop from closing.

**Tipping** (1.7.0 against the 1.6.0 two-thirds control): at 60–80% solvent and on time — liability 317 / 0 / 226, Ω
4,352 / 7,967 / 9,215, plants unfunded 0.7 / 0.1 / 3.6, on-time 0.89 / 0.97 / 0.95 — with the state's share unchanged
within noise (1,719 vs 1,723; 1,859 vs 1,861; 2,132 vs 2,075) while refusals fall (Hypothesis 3 holds as the rc.2 review
framed it); the honest 12 / 18 / 25% poorer (uplift down two fifths to a half) and five to six times richer than a
stamper (Hypothesis 4); false approvals 11 / 14 / 14 / 16 against 13 / 13 / 14 / 17, the lag kind zero. **At 50/50 the
market collapses** — queue 609 (control 129), the state delivering 500 against 1,169, on-time 0.25, liability 20,643 —
by the same mechanism: Ω starts richer (1,852 against 708 at the end of the first period), the suspensions make the
market late from the third period, and from the fifth the old debts are paid before any advance (Ω 1,032 → 73 over
seven periods; troop deliveries per period 51 → 19 while the control's rise to 90–113). Hypothesis 2 is answered:
50/50's liability does not clear, and the two accounts close 1.6.0 §1.4's loop harder than the merged fund did.
Ω's income by source is a line, not a trend (surplus 5–9 a tick at 60/40 against a fee of 3; 10–11 at 80/20).

**The take:** at 60/40, 10% clears everything — liability 0, plants unfunded 0, Ω 7,836, careful wealth 5,066 (above the
control: the surcharge doubles too); at 50/50 fees do not carry the clock at any take swept (liability 20,643 / 13,169
/ 7,637, queue 609 / 342 / 178 at 5 / 10 / 15%). **Adaptive:** honest at tick 575 (735); the liability stock halves
(12,538 against 26,259) and clears in 5 seeds of 20, as before — no troops once honest, so no surplus (Hypothesis 5
fails); plants unfunded 396 (493). **Drift:** solvent (liability 779 / 0 against 13,104 / 7,915; plants unfunded 3.7 /
6.7 against 20 / 67); false approvals 32 (34) at m_max 4 and **80 (64) at m_max 2** — more state deliveries, more
pinned approvals inside the auditor's lag (71% / 59% of the upheld route). **Red team:** the late withdrawer now costs
and gains nothing (liability 0, on-time 0.95); the flood breaks Ω as before (liability 55,829 against 75,598) and the
state's take grows with volume it cannot serve (fee income 4,568 against 2,993, surplus 8,280 against 6,029) — Q17's
reading, not an exploit; the decliner loses 1,123 (209) and drags the market (queue 541); the reformer 2,881 poorer
(3,146) with the market collapsing around the readmitted reformers (troop deliveries 421); camouflage buys nothing.

**For the next decision, in order:** (1) the troops' working capital at 50/50 — advances before old debts under stress,
or a working-capital target above R_T, or the cannot-serve protocol that bounds the debt at the source (the take does
not do it: 15% at 50/50 leaves 7,600 owed); (2) the take at 60/40 as 10% if plants unfunded must be exactly zero in
every seed; (3) the liability stock that never clears once honest; (4) the honest 12–25% poorer — Baruchi's call; (5)
drift at m_max 2, false approvals 80 against 64, read with Q14 first. Also reported: my rc.1 review's point 4 (a troop
review seat "nets nothing") was wrong — the seat nets its fee, its cost reimbursed from the allowance since 1.4.0; the
accepted text carries the figure, Appendix L and `test_v17` correct it.

**Run 9 addendum — two evaluations the reviewer asked for, rules unchanged** (`trace/` 60 runs logged every 10 ticks,
`tsusp/` 120; engine d804628 — the driver gained the readings and `--t-susp`). *(1) The 50/50 collapse by period.* The
splits are identical through the second period and part at the third, when the stampers are suspended and ten members
remain at 50/50 against eight at 60/40: about five on duty at both, so five deliver at 50/50 against three, and one or
two are free at the seating step on most ticks. The engine reads 1.4.0 §12.3's "no member free to commit" per tick — one
free member blocks every award summons that tick — so at 50/50 the state is blocked on 79% of ticks with 289 requests
waiting and 2.0 members free (60/40: 54%, 14 waiting, 1.5 free, but the members are all committed often enough that the
state summons 21 deliveries per 10 ticks); the summonses come in bursts when none is free (the first at tick 288, 38 at
once; 70% of all troop deliveries in bursts of twenty or more), the queue grows a request a tick between them, and the
queue's age is the lateness. The 1.6.0 control at 50/50 stalls the same way (74%); the service paths diverge at tick
504 (range 320–690): a burst is bounded by what can be advanced that tick (Ω above the plant reserve under 1.7.0; the
surcharge-fed fund plus Ω under 1.6.0, whose bursts are larger — p90 43 against 23), the stall's rebates are paid in
cash by Ω under 1.7.0 and as a liability under 1.6.0, each burst sets R_T high so the account retains its earnings for
two periods, and from tick 396 (period 5) Ω's balance above the plant reserve goes to liabilities older than a period
before any advance — after which the control pulls ahead, 110–141 deliveries a period against 24–39. The collapse is the
stall; the two accounts decide how the bursts are financed. For the record: the other reading of the rule — summon for
the requests beyond the free fundable members — is the reviewer's to rule on; the same per-tick test is why 1.6.0's
Hypothesis 2 came out inverted in run 8. *(2) T_susp ∈ {0, 50, 100}.* At 0 a suspended stamper is a probationer at the
next rotation (460–570 suspensions a run); probationers carry the initial seats, fewer members sit on duty, more are
free to deliver — at 50/50 that helps (queue 173 against 609, on-time 0.70, liability 5,963, plants unfunded 0) and at
60/40 it breaks the market (queue 519 against 42, liability 13,497, troop deliveries 78), because the state is blocked
nearly always; honesty pays at both (false approvals 26 / 23 against 11 / 14, the probationers' 17 / 15 against 3;
stampers two and a half times richer on probation fees); audits by members up a third at 50/50. T_susp = 50 is between
on everything, better than 100 at 50/50 and worse at 60/40. No value is right at both splits and none repairs 50/50;
the lever is the same one the stall reads the other way. **The item for the decision is the summons test**, before the
working capital or the protocol.

## Maps

Two `_line` artifacts in project Agentic-OS (`c54120a6-aaff-40f7-8a9f-3667da542879`):

- **The economic loop — baseline v1.0** (`2c4dbe4e-a4fb-4b4d-b49b-b7c3e5090745`, revision 10): the
  ten-step flow, five side-flows (appeal, dispute, audit, delegation, override), twenty rules with
  equations, the open questions, a glossary, and a concept mapping the old proposal's open questions to
  what v1.0 decided. Text export in `docs/`.
- **Agentic Economics — Proposal (WIP)** (`440f5eaf-a538-4330-adc7-52b7e72b04bc`, revision 5): the
  October 14 open-questions map, kept as history.

## Working agreements that held across the whole effort

- Every review's tests are kept verbatim; the engine is fixed, never the test.
- A refused action changes nothing — asserted against whole-world snapshots.
- Conformance passes change *how*; design revisions change *what is permitted*, and are labelled.
- "Stated" means someone said it; the spec labels every rule as Rule / Consequence / Default /
  Hypothesis / Bracketed, and the map carries evidence on every statement.

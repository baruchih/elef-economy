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

## Patch 1.7.1 — the award summons is per request (October 18, 2026)

The design reviewer's ruling on run 9's addendum, relayed by Baruchi: *"The rule's meaning is per request, not per tick.
1.4.0 §2.3: a root request that no eligible member has been awarded within w_A ticks is awarded to a troop. A free member
takes the oldest request it can; the others, unawarded past their window with nobody offering for them, are the state's.
So: at the seating step, requests that have waited w_A and exceed the free fundable members are summoned for, oldest
first, after the members have taken theirs. 'Members first' is unchanged — a troop never takes an award a member offered
for. Classification: a conformance correction, with the wording made unambiguous — 1.7.1. The text admitted both
readings; the per-tick one contradicts the rule's stated purpose (the state fills what the market leaves). Not a
revision; no other rule moves. T_susp stays at 100."*

**Done** (`spec/agentic_economics_loop_spec_v1_7_1.md`; 1.7.0 to history; §12.3's two summons rules reworded, the ruling
and the trace that earned it in Appendix L). Engine: `_summon_troops`'s award pass gathers the root requests past `w_A` in
creation order, counts the free fundable members at the market price (`_free_fundable_members`), leaves that many of the
oldest to the market and summons for the rest, oldest first, each through the unchanged delivery check (β ≥ B̄, the
requester's pay-in, the inspection carried, the troop account plus Ω's room above the plant reserve); readings
`awards_left_to_members` (summed over seatings, in the period record), `awards_waiting_now`, `members_free_now`; driver
columns `awards_waiting_w_a`, `members_free_at_seating`, `awards_left_to_members`. No flag: a conformance correction
holds in every mode, as the 1.4.0 audit obligation did, so the `--rules` controls carry it and run 8's and run 9's
control cells are no longer reproduced to the unit. `test_v171` (4); suite 248 + 26 in all three modes; the equivalence
scenario's goldens re-pinned once at the correcting commit (the scenario summons where one free member used to block;
both seeds' dial now ends at 4.0); reviewer tests untouched and passing.

**A smoke before the sweep, 50/50 seed 1, 1,000 ticks, for orientation only:** Ω's liability 0 and rebates paid 0 (run 9's
seed: liability 20,643 across seeds), plants unfunded 0, troop deliveries 1,388 against 500, vested 2,284 against 1,863,
Ω net +3,712, troop surplus to Ω 4,379, R_T 440 at the end, award summonses refused for funds 0. Read with run 10.

## Run 10 — the tipping cells under 1.7.1 against run 9 (October 18, 2026)

`agentic_sim/results/studies/1.7.1-summons/tipping/` (and `1.7.1-summons.zip`): 80 runs — 50–80% stampers × 20 seeds, 20
actors, 1,000 ticks, logged every 20 ticks, every final audit passed, engine 8d9b866; read from the second period on against
run 9's 1.7.0 cells. The notes for the reviewer are `agentic_sim/results/studies/1.7.1-summons-notes-for-reviewer.md`.

**50/50 clears, by the summons alone** (run 9 in brackets): queue 38 (609), on time 1.00 from the second period on (0.25),
lateness 0 (90), Ω's liability 0 (20,643), rebates paid 0 (1,782), plants unfunded 0 in every seed (138), troop deliveries
1,400 (500), summonses refused for funds 0 (23,497), Ω at the end 4,306 (59), the surplus 4,639 beside the base fee 2,996
(2,743 / 2,418). 60/40: liability 0 (317), on time 1.00 (0.89), deliveries 1,753 (1,719), refused 0 (607). 70/30: already
clear, unchanged (1,831 against 1,859). 80/20: liability 0 (226), plants unfunded 0 (3.6), deliveries 2,054 (2,132) —
unchanged in what was asked, as expected, since its four members were never free and the two readings coincided. **The
summons is steady:** 34 / 43 / 45 / 50 deliveries summoned per 20-tick window at 50–80%, max within 20% of the mean,
windows with none 3.8% / 1.5% / 0.9% / 0.2% (run 9's 50/50: 62% of windows, bursts to 60); requests past w_A at the seating
never above 3. **R_T is no longer set by burst peaks:** 448 / 568 / 607 / 689 at the end with the run's maximum within 20% of
the mean (run 9: maxima 1,129–1,587 against means 400–754) — the steady in-flight capital, about twenty deliveries. **False
approvals unchanged** within noise, 11 / 14 / 15 / 18 (11 / 14 / 14 / 16), the lagging auditor zero everywhere; **careful
wealth within 2%** at every split (4,111 / 4,302 / 4,638 / 5,226 against 4,056 / 4,250 / 4,659 / 5,190), stampers five to
seven times poorer.

**Two readings flagged, no rule moved.** *w_A now binds in fact:* a request the free members have not taken within two
ticks is the state's that tick, so the members' awards fall (162 → 129 at 50/50, 43 → 40 at 80/20, 8.5 from the second
period on there) and the state delivers 46% / 57% / 60% / 67% of what vests — the market's share is now the default w_A's
choice, at the cost of the lateness a longer window admits; the state's share is visible in "Ω's income by source" (the
surplus 1.5 to 2.7 times the base fee). *The clock is dormant:* lateness zero at every split (awarded or summoned by
w_A = 2, the fastest troop path 5 against T_s = 8), so the rebate, the liability and its order were exercised in no run of
this study; untested, not wrong. **For the decision:** the reviewer's condition is met — 50/50 clears with no rule
changed — so by the reviewer's note 1.8.0 is the cannot-serve protocol alone and the growth buffer is dropped; its trigger
(a summons refused for funds, a queue past the window) fired in none of the 80 runs, so its first test is below 50% or
with a float too small to carry twenty deliveries in flight.

## Run 11 — riots, the w_A knob, adaptive and drift under 1.7.1 (October 18, 2026)

The design reviewer accepted run 10 ("1.7.1 stands"; the state's share at w_A = 2 a reading to minimize later, w_A stays 2;
the dormant clock "fine as long as it's there and works: spikes will happen and the auto-scale will have to answer them,
so the next study is to make it run") and asked, before 1.8.0 and under 1.7.1: riots — cells where the clock, the rebate,
Ω's order, the plant reserve and the troop reserve bind and the auto-scale has to rise and retract; w_A ∈ {2, 3, 5} as a
measurement; adaptive and drift as before. "1.8.0 is decided on what binds in (1)." The driver gained a demand spike
(`--spike-tasks/--spike-from/--spike-ticks`) and a delayed drift (`--drift-from`), commit 381b9ed; no engine change.
`agentic_sim/results/studies/1.7.1-riots/` (and `1.7.1-riots.zip`): `riots/` (160), `wa/` (240), `adaptive/` (20),
`drift/` (40) — 460 runs, every final audit passed. Notes: `agentic_sim/results/studies/1.7.1-riots-notes-for-reviewer.md`.

**Riots.** *The asked spike (nine a tick for 50 or 100 ticks from tick 400, 60/40) binds nothing:* Ω's cash (about 2,200)
plus the troop account carry every summons, advances of 9,400–10,300 in the spike window all repaid inside it, no request
late, no rebate, no liability, no plant unfunded; the auto-scale alone rises and retracts — troops in the field 22 → 75–98
→ 22, R_T 529 → 2,152–2,613 → 540 two periods after the spike — and **every seed is back at the quiet level 110 ticks after
the spike ends, 1.8–1.9 periods: R_T's two-period memory is the recovery time.** *The capture wave* (60/40 → 90/10 in 25
ticks from tick 400) is absorbed without a late request — the turned are suspended inside one period, members on duty 6 → 2,
the state delivers everything — at the cost of one window of false approvals (14 against 0.8) and the probationers' 14 a run
against 3. *Ω₀ = 100* refuses 67 seats and 10 awards in the first period and never again. *10/90 and 30/70* are quiet. *The
flood at six a tick sustained* binds in the ramp — the first 100 ticks: on-time 0.03, lateness 17, 10,820 request-ticks
refused, liabilities 6,510, Ω at 81 — then the dial at 4, X_t 16, the summons steady at 5.2 a tick, on-time 1.00, and **Ω's
order pays the stock down oldest first from income above the plant reserve, 7,415 → 0 by tick ~750, seven periods after the
ramp**; plants unfunded 0.45; R_T 2,385 → 1,343; Ω 81 → 14,927. *The hard spike (mine: fifteen a tick for 100 ticks, two and
a half times the asked, added to find the edge)* is where it binds in a quiet market: the summons refused for funds from the
first spike window (38,834 request-ticks in all), queue to 659, on-time 0.00 in the spike, lateness to 37, the liability
accrued to 16,607 by tick 560, Ω at 77, plants unfunded 11, R_T 4,905 and back to 554 two periods after; **the flows are
back 160 ticks after the spike ends (2.4 periods); the stock is not** — paid at Ω's whole income above the plant reserve,
220–330 a window, it stands at 7,351 at tick 1,000 and would clear about 25 periods after the spike, Ω holding only the plant
reserve the whole time; one seed in twenty cleared. **What binds is capital:** about 2,200 at 60/40 carries nine deliveries a
tick in flight and not fifteen; past the edge the clock and Ω's order work exactly as written and nothing breaks, but a
100-tick spike at 2.5× the quiet capacity leaves 25 periods of debt and requesters who waited 20–40 ticks with nothing said.

**w_A ∈ {2, 3, 5} at 50–80%.** The window moves almost nothing: members' awards within 1–6% (129 / 130 / 130 at 50/50; 40 /
40 / 41 at 80/20), the state's share within 2% (46% → 45%; 67% → 69% → 68%), on-time 1.00 everywhere (w_A = 5 plus three
troop ticks is T_s = 8), Ω's surplus against its fee unchanged, the queue up by the waiting ticks (38 → 47). The members'
share is their capacity, not the window's artefact — a longer window leaves a request waiting for a member who is not coming.

**Adaptive and drift.** Adaptive: honest at tick 745 (575 — slower, since the stampers are no longer starved of awards
while the state serves the queue), the last troop at 605, R_T zero from 770; **the liability is never made (on-time 1.00) and
is 0 in every seed** (12,494, cleared in 5 of 20); plants unfunded 0 (400); FA 44 (46); Ω 4,341 (1,002). Drift (m_max 2 / 4):
liability 0 / 0 (779 / 0), on-time 1.00 (0.88 / 0.95), plants unfunded 0 (3.7 / 6.7), refusals 0 (6,295 / 1,747), Ω 19,664 /
18,388; honesty unchanged — FA 76 / 32 (80 / 32), the lagging auditor 25 / 8 of the upheld route (27 / 8), the drift lag the
plant record's as before; careful wealth 6,724 / 9,191.

**For the decision.** The riots the brief named were carried by the auto-scale alone and retracted in two periods; the clock
and Ω's order ran where the capital bound — the flood's ramp and a spike at 2.5× the quiet capacity — and worked as written.
The one thing to weigh: past the capital edge the liability is a stock paid at the market's income, about 6 a tick at 60/40,
so a hard spike leaves tens of periods of debt with Ω at the plant reserve and nothing said to the requesters who waited.
If that is "something breaks", it is the cannot-serve protocol's case exactly, with a measured trigger (a summons refused
for funds, a request past its window with nobody coming); if not, the protocol stays a product question and nothing in
these 460 runs asks for a rule.

## Design revision 8 — the price of work (2.0.0, October 18, 2026)

**What it is.** The first major version: a change of approach to money, on Baruchi's frame ("the servers needs to be decoupled from the
economy, otherwise we contaminate it"; "maybe it is time we introduce floating prices"; "if I print more money then money is worth less";
"the actors have nothing to buy"). Through eleven runs the price was fixed by fiat at β = 20 from a bottomless wallet and the credit was a
score — the backing stood at 10^7 and v_t moved 0.05% in a thousand ticks. 2.0.0 lets the price float: requesters with finite wallets
(issuance 10 a tick each, wallets 200) choose a ceiling and lock the all-in maximum at posting (a root's first lock; the nominals and the
fee rate freeze there; I29); members bid; the price level P_t — the trailing mean of every awarded price, P_0 = 20 before the first — indexes
every nominal the rules fix (f, G^V, D, φ, K, r_s, c_T, the plant pots) in place of v_0/v_t, frozen per case; effort costs stay nominal as the
anchor; there is no backing (sources: issuance, emission, creation; sinks: the burns, retirement, departure); Ω is never broke — it creates
for a payment the rules require and retires the deficit from every inflow, both public (I28) — and A_T, R_T, the plant reserve, Ω's order,
the troop account and the liability stock are retired; the state delivers at cost (c^D_T = B̄) under a capacity N_T = 40 outside the ledger
(a delivery holds two places until its inspection is seated; a refusal for capacity is recorded and told); B̄ counts members' awards only;
a request below B̄ is flagged and its requester may raise the ceiling; delegation waits for 2.1.0 (it needs costs that differ across actors).

**Reviews.** rc.1 (`spec/design_revisions/dr8_2.0.0-rc.1-review.md`): seven points — the demand defaults did not clear at P_0 (the deposit's
net cost ~8 a task left ~10 for the price; the ceiling policy against the deposit's float starved posting), delegation cannot pay with one
cost, the pay-in at posting, indexing frozen at the first lock (§4.5 kept; the care cost), c^D_T a 50% margin on an unbounded riot, the
hard spike creates thousands not hundreds, retirement undefined — all adopted in rc.2, which added effort costs nominal as the anchor, the
state at cost and N_T finite. rc.2 review: three points — the riot cannot be posted by six requesters (a crowd), N_T 30 bound at rest at
80/20 (40), issuance 15 clears near 16 against §6's 11 (10) — adopted in rc.3. rc.3 review: implementable as it stands, one reading
("two of N_T" reserved, released on seating). **Accepted** with two rulings for Appendix M: the two places are reserved and released when
the initial review is seated; a leaving requester's wallet leaves M as `departure`. Consolidated as `spec/agentic_economics_loop_spec_v2_0_0.md`
(Appendix M); 1.7.1 to history; rc.3 verbatim as `dr8_the_price_of_work_2.0.0.md`.

**Engine** (`Params.floating`, on): the ledger's `index()` is P_t/P_0 and `v` the reading P_0/P_t, `purchase` a plain burn of the credits
given (the cost API is nominal), the kinds `issuance` / `creation` / `retirement` / `departure`; `post_root` locks and freezes, `award` and the
summons release and draw, `raise_ceiling`, `add_requester` / `remove_requester`, `scenario_create`; `_omega_ensure` / `_omega_retire` with the
deficit counters; Ω the troops' wallet, the funds check moot, R_T and the plant reserve 0, the liability list never fed; N_T with places per
troop; the readings in `view.market()` and the period record. I27–I29 new, I1/I3/I15/I23/I24/I26 amended. `test_v20` (16); goldens re-pinned
once; the 1.x behaviour tests pin `floating=False`. **Five reviewer tests are expected failures** with their reasons: one pinned the backing's
v_t (anticipated), one the pay-in's refusal at the award (now at posting), three pinned 1.x figures through the index — the reviewer tests
award at 10 and 40, so the price level moves after their first award. *A reading for the reviewer:* P_t on B̄'s window moves within a period;
at the period boundary instead, the index would be constant within a period and those three would pass — one line, the text's call.
Suite 259 + 31 in all three modes.

**Driver** (`--rules 2.0.0`, default; `1.7.1` the fixed-price control): six requesters with wallets, issuance, the ceiling policy
min(40, ⅓ unlocked) and K_open 5, raising a flagged request to the market price when the wallet allows; members bid c_D (1 + m), m from 0.3,
+0.3 on an award, −0.25 per three idle ticks continuously (`--bid ceiling` the control; `--c-d-adaptive`); effort burned at submission;
the state at cost (`--c-d-t-mode`) under `--n-t`; the crowd (`--spike-requesters`) and the shock (`--create-at/--create-amount`); real-wealth,
price, deficit, capacity and demand columns.

**The first smoke (60/40, seed 1, 400 ticks)** before run 12: P_t ran from 11 to 35 and the margins to 3 — six of the eight members are on
duty, the two free members are awarded every tick they are free, so their margins ratchet to the ceiling and the state follows them at B̄; the
deficit stayed at zero, the field slack (2–7 places of 40), posting K_open- and lock-bound (~2 a tick), M growing in hoards. The worked
example's P_t ≈ 9 assumes members plentiful. Rules and the declared policies stand; run 12 reads which it is.

**Run 12 — done** (`results/studies/2.0.0-price/`, 580 runs, all audits passed; `results/studies/2.0.0-price-notes-for-reviewer.md`; the
section below). One driver change between its first launch and the run kept: the requester's raise policy reads the live condition β < B̄
rather than the posting flag (the first wave's crowd never left — its requests, overtaken by the market after posting, carried no flag
and waited forever); the first wave was discarded and everything rerun at `1231a40f`.

## Run 12 — the price of work under 2.0.0 (October 18, 2026)

**What ran.** §8 of design revision 8: price discovery at 50–80% with bidding members against the at-the-ceiling control (160); the
deficit shock 1,000 / 2,000 / 5,000 at tick 600 × N_T 40 / unbounded (120); the crowd of thirty for 100 ticks and the flood of twelve
sustained × N_T 40 / unbounded (80); the knobs one at a time — λ 0.5, c^D_T at the 1.x margin, issuance 15, the adaptive reservation (100);
the red team — lowballers, a stingy requester, troop awards in B̄ (80); adaptive 3,000 ticks (20); drift m_max 2 / 4 (40). Read in real
terms from the second period on, against runs 10–11.

**Findings.** *The credit is worth less:* P_t 31.6 / 34.1 / 37.4 / 37.3 at 50–80% with bidding members (the ceiling control 21–24: every bid
the customer's ceiling, a third of a wallet the bids drain to 55), the cap β_max = 40 under any pressure. *Set by the free members' margins,
not by cost:* at 60/40 two of eight members deliver, awarded every free tick, margin 3.0 for eight hundred ticks, bid 29, the state at B̄
behind them; the adaptive tail with twenty members free is the one place the price falls — to 23. *Inflation is real and lands on
holders:* a 2,000 shock (9% of M) lifts P_t 15% in a window, the stampers' real wealth −13%, the honest's unchanged; it does not come back
and Ω retires nothing of it. *The state at cost is below cost:* a fifth of its deliveries fail and lose B̄ + G, nothing offsets it, Ω's
unlocked balance is zero from tick ~400 in every cell and the deficit grows 10–20 a tick without bound (3,700 at 50/50 to 59,700 in the
flood); the 1.x-margin control runs the identical path with the deficit at zero — Hypothesis 7 fails, Hypothesis 6 inverts. *The capacity
case:* under N_T 40 the crowd fills the field in a window (14,349 request-ticks refused, on time 0.84, rebates 16,000), the flood keeps it
full (on time 0.33, rebates 6,300 a window all created, the deficit 59,700, the requesters hoarding 3,000 each, M 99,000); unbounded, 182
troops at the peak and nobody waits. *Honesty is price-neutral:* FA 10.7 / 10.4 / 12.7 / 14.7 (run 10: 11 / 14 / 15 / 18), the lagging
auditor 0 at every fixed split, stampers' real wealth a tenth of the honest's. *Demand is lock-bound:* K_open 5 and the posting lock hold the
six requesters at 1.8–1.9 posts a tick with wallets of 70–90. *Red team:* lowballers win 51 awards each and end poor (141 real); a stingy
requester waits all run and hoards 10,000; B̄ counting troops moves nothing. *Adaptive:* honest at a median tick 500 (745), the deficit
retired in 20/20 once the state stops. *Drift:* FA 48 / 22 (76 / 32), solvent in the new sense, in debt without bound.

**For the decision** (notes §8): (1) the state's cost rule — at cost loses the failure rate; candidates c^D_T = B̄(1 − b), the fee, or the
margin as a reading; (2) the ceiling cap is the price level — the market has no anchor below the customers' maximum but the free members'
margins and the state never undercuts; (3) the rebate under a refusal for capacity prints; (4) P_t at the period boundary would keep the
three index-moved reviewer tests passing; (5) delegation (2.1.0) — the money is in the members' hoards.

**The reviewer's reply (October 19).** Run 12 accepted as recorded; the raise-policy change accepted as a strategy's reading of its own
declaration, the first wave discarded. The three rule fixes will be 2.1.0 and do not depend on the price question — the state at cost in
expectation (c^D_T = (1 − b_T) B̄ − b_T G, b_T the trailing fail rate of the state's deliveries), creation only for what returns (summons
capital, plants) with rebates from income and the bounded liability stock, a capacity refusal told, P_t updating at period boundaries.
Before the draft: four evaluations under the rules in force, so the oligopoly can be classified — supply, strategy, or the state's pricing
— run 13. Delegation and entry go to 2.2.0 together.

## Run 13 — the price question under 2.0.0 (October 19, 2026)

**What ran** (`results/studies/2.0.0-supply/`, 400 runs, 20 seeds a cell, 1,000 ticks, issuance 60 a tick, all audits passed; notes
`results/studies/2.0.0-supply-notes-for-reviewer.md`; the engine unchanged, the driver at `e05cf3fb`): supply — 20 / 30 / 40 actors all
honest (60); the strategy — the same cells and 60/40 with the margin falling 0.25 per idle tick instead of per three (80); demand unbound —
the market-aware ceiling β = 1.2 B̄ (`--ceiling-policy market`) × K_open 5 / none × β_max 40 / 60 at 20 honest and at 60/40, and K_open
none alone under the wallet rule (200); the cap — β_max 30 / 40 / 60 at 60/40 (60). One driver change: the market-aware ceiling policy and
`--k-open 0` as no limit; the wallet rule stays the default.

**Findings.** *Supply takes the price to cost, not to a plateau:* P_t 22.5 / 11.6 / 10.9 at 20 / 30 / 40 honest (cost 8, bids 8(1 + m)),
margins 1.9 / 0.36 / 0.23, members free 9.6 / 18.7 / 28.2. *The strategy's ratchet has no interior equilibrium:* in every cell where it
runs, a free member's awards per tick converge on margin_down/(idle_k · margin_up) = 0.278 (0.270 at 20 honest, 0.273 at 60/40 at every
cap, 0.25–0.27 across run 12) — the price rises until the requesters buy one task per 3.6 ticks per free member, and where the demand
model cannot reach that rate (30 and 40 honest: K_open holds posting at 2.8 a tick) the margins decay to the floor. The faster decay puts
every honest cell at cost (9.2 / 8.8 / 8.7, the honest earning half) and at 60/40 lengthens the ramp from two hundred ticks to nine hundred
without stopping it (the two free members wait under a tick between jobs and keep their margins while working). *The cap was not what run
12 read:* β_max 60 gives the same 34.1 as 40 at 60/40 — the wallet rule (a third of a 35 wallet, raised to B̄) binds first; 30 binds at
28.8; with market-aware requesters the cap is the price level to the unit (39.6 / 59.5). *The state's pricing never lowers the price:* at
B̄ it never undercuts a member; where the requesters' ceilings sit at B̄ (the wallet rule with K_open lifted) it delivers 39–75% at 17–27
and the deficit runs to 6,000–14,000 — the cheapest market in the study is the one the state pays for. *Demand unbound:* price-bound
posting at 1.6–2.8 a tick, the state's share 12% at 20 honest and 37–54% at 60/40, the capacity case open at 60/40 whenever K_open is
lifted (3,364 refusals, on time 0.80–0.82, rebates 930). *Honesty unmoved.* **Classification:** supply is the trigger and the cure (the
cliff between 20 and 30 honest); the strategy's constant places the cliff; the state's pricing sets the price only where the requesters'
ceilings are B̄, at a loss; the cap is the price level only when the requesters bid above the market.

**Readings for the 2.1.0 draft** (notes §6): the state at expected cost prices below B̄ and becomes the lowest offer on every request past
w_A — the draft should say whether such a request goes to the state at its expected cost or at B̄; the demand model is the driver's and
set two of run 12's readings ("lock-bound" was K_open 5; "the cap at 40" was the wallet rule) — the declared requester for 2.1.0's §8
should be named; P_t at period boundaries does not touch the ratchet; a refusal told would show in the K_open-lifted 60/40 cells.

## Design revision 9 — the bank (2.1.0, October 19, 2026)

**The candidate.** `agentic_economics_loop_spec_2.1.0-rc.1.md` arrived the morning after run 13 — a sketch of what the reviewer had
announced: split the orchestrator's one pocket into two. The implementer's review (`dr9_2.1.0-rc.1-review.md`): implementable with one
correction (a plant has been netted since 1.3.0 — mint the pots, not the all-in; the closure sweep must go to the bank and be destroyed,
never to Ω) and nine readings (the burn's floor at b_T = 2/3; b_T's window in a quiet period; a seat's loan repaid at its review's
settlement; the order applied before the summons pass; seats under the wall stall the members' work; the first period at base; Hypothesis
1 arithmetic where b_T equals the driver's rate; `test_review_14` stays, the told flag was the engine's; §6's scale). rc.2 adopted all of
it and ruled the seat question (a binding wall refuses deliveries, never seats); the rc.2 review: implementable as it stands, one note for
the record — a base fee paid inside the summons pass could fund part of the next summons before the end-of-tick ordering. **Accepted with
one ruling (Appendix N):** every inflow to Ω is ordered at once — debt → liabilities → Ω — the moment it arrives, inside the pass included;
the pass-start and tick-end points stand as I30's checks, not as the rule.

**What 2.1.0 is.** A second account, the bank, that alone creates and destroys credits. It mints by rule — the requesters' issuance,
emission, a plant's two pots (the cost of truth), a run's declared shock — publishes the price level once a period (the closed period's
mean awarded price, carried if none; the index constant within a period, I31), and lends the state the shortfall of a summons tied to it,
repaid from the summons's own return before Ω keeps anything. What a settled summons did not repay is the state's debt, repaid by every
inflow to Ω the moment it arrives, before the rebate liabilities (1.6.0's stock again, never created) and before Ω keeps. The bank lends
for a delivery only while the debt is within the wall — one closed period of Ω's fee income, base fees plus the troops' review fees — and
for a seat always; a delivery refused for credit is marked and told, the state has retracted. The state burns its expected cost c^D_T =
max(0, (1 − b_T) B̄ − b_T G) with b_T its own trailing fail rate (the last closed period if it closed ten, else back until ten, else 0.2)
and still delivers at B̄, so it never undercuts a member; neutral in expectation up to b_T = 2/3. Every refusal — for capacity or for
credit — marks the request with its kind and tick, readable in the public view; the requester may hold or withdraw. Creation, retirement
and the deficit are retired as rules (the control, `Params.bank` off); Ω's net position = Ω_U − debt − liabilities.

**Implemented** (`Params.bank`, on with `floating`; the engine commit named below): the ledger's five source kinds and two sink kinds; the
World's bank counters, `loans` by troop, `debt` with peak and age; `_fund_can_carry(need, cid, kind)` lending or refusing; the ledger hook
repaying the troop's own loan and running the order on every inflow (`_bank_on_inflow`, `_omega_income`), again at the pass's start and
the tick's end; `_close_loan` at a delivery's release or a seat's settlement; the expected cost at the summons with `_state_fail_rate()`;
`_stop_clock` to the liability stock; plants minted and the sweep destroyed; the scenario minted; `price_level()` as published at the
boundary; `_mark_refused`; `view.bank()` and the marks; the period record's `bank` block. I28 rewritten (lent = repaid + outstanding +
debt), I30, I31; I27–I31 in the full audit too. `test_v21` (13); `test_v20` pins `bank=False`; the goldens re-pinned once — in the seeded
random drive the state's deliveries fail far above a fifth, so the wall binds there and the state retracts (393 refusals, 24 waiting at
the end of seed 1), the rule as written on a drive that is not an economy; three reviewer tests out of `EXPECTED_FAIL` (28 remain). Suite
275 passed, 0 failed, 28 expected failures in all three modes. Driver: `--rules 2.1.0` default, `2.0.0` the control; `--c-d-t-mode`,
`--b-t-prior`, `--b-t-min-n`, `--debt-bound-periods`, `--requester-on-refusal`, the red team's `--troop-fail-rate` and `--state-rejecters`
(the rejecter reads the case's actor through the public view — the reviewer's view carries none; declared); the bank's books as columns.
Spec consolidated as `v2_1_0` (§2.4, §3.1, §4.1–4.5, §7.6, §7.7, §10.4, §12.2, §12.3, §16–18, §20, Appendices A, C, N), 2.0.0 to history,
rc.2 verbatim as `dr9_the_bank_2.1.0.md`.

**Two things the smoke showed before run 14, for the record.** In the honest market the state's retained fees fund most of its own
summonses, so the loans line is small and the losses on Ω-funded deliveries are Ω's own income lost, not debt — debt arises only where a
loan went unrepaid, as the text says; and at 60/40 the state closes fewer than ten deliveries a period for several periods, so b_T reads
the prior for a while. Run 14 reads both.

**Next:** run 14 — the revision's §8 in its order: §6 reproduced; the state neutral at 50–80% against `at_cost` on the identical path,
read with the knobs (§8.8) and the red team (§8.9), where b_T and the driver's rate differ; the pump (the flood and the crowd at N_T 40,
60/40 with K_open lifted under both ceiling policies); the index per period against run 12; the inflation test (issuance 5 / 10 / 20 at 20
honest, β_max 60, both ceiling policies); told (the withdrawing requester); the books in every cell. Then 2.2.0 — the supply side: entry
and delegation — which the reviewer is sketching meanwhile.

## Run 14 — the bank under 2.1.0 (October 19, 2026)

**What ran** (`results/studies/2.1.0-bank/`, 600 runs, 20 seeds a cell, 1,000 ticks, all audits passed at `f081e15f`; notes
`results/studies/2.1.0-bank-notes-for-reviewer.md`): §8.2 the state neutral at 50–80%, expected against at cost (160); §8.8 the knobs
at 60/40 (100); §8.9 the red team — the state failing at ½ and ¾ × the wall 1 / unbounded, half the careful rejecting the state (100);
§8.5 the inflation test — 20 honest, β_max 60, issuance 5 / 10 / 20 × both ceiling policies (120); §8.6 told — the withdrawing requester
at 60/40 with K_open lifted (40); §8.3 the pump — the crowd and the flood at N_T 40, K_open lifted holding under both policies (80).

**Findings.** *Neutral, and the bank unused:* under the expected cost Ω nets −0.6 to −0.8 a delivery (2–3% of B̄, b_T's lag and the
troop seats' bonds), keeps 4,300–4,500, funds every summons itself — loans, debt and liabilities zero at every split; the wall never
binds. *The at-cost control under the bank retracts instead of bleeding:* debt 500–650 against a wall of 210–350, 1,900–10,600 refusals
for credit, liabilities 2,400–8,800, on time 0.79–0.89, the requesters hoarding — "the burn rule is wrong, not the wall", in the record.
*The index per period changes nothing in kind* (P_t 31 / 33 / 36 / 36 against run 12's 31.6 / 34.1 / 37.4 / 37.3; honesty within
noise). *The knobs:* the prior moves what the state keeps from its first dozen deliveries by ±236 and nothing else; the wall's width
irrelevant where it is not approached. *The red team finds the two-thirds limit where §7.7 put it:* at ½ the automatic charge covers
everything (b_T 0.52, burn 8.4, no debt, Ω 4,543 as in the honest cell); at ¾ the burn is zero, the debt crosses the wall, the state
retracts and its customers are owed 8,900 of rebates (the unbounded control's debt 4,900 and rising, run 12's bleed legible); the
rejecters drive b_T to 0.67 — the limit — and make the state 63% of the market at a loss; they read the case's actor (the view carries
none) and so never meet a plant. *The inflation test gives the quantity theory and the first deflation:* issuance 5 / 10 / 20 → P_t 9.5
/ 23 / 54 (predicted 11 / 23 / 47); at 5 the price falls from 20 to cost — the credit worth more than it was — and **real wealth by
disposition is not invariant** (790 / 1,410 / 1,310: at low issuance the ratchet never starts, at high the requesters hoard a third of
M). *Told:* every mark withdrawn and reposted, the rebate farmer gains nothing (78 against 75), honesty unmoved. *The pump is off:* M is
issuance alone (the flood 74,000 against 99,400; hoards 1,700 against 3,000), the field's capital on the loans line at 1,700–1,800 and
repaid, the debt peaks at 400–500 and is repaid — and **the lateness liability is 27,000 in the flood and 10,000 under the crowd, ageing
400–500 ticks, a quarter of it the state's whole fee income**: nothing is printed for it, and the customers wait for money the state does
not have. *The books:* lent = repaid + outstanding + debt held in 600 runs; run 12's "deficit" re-read as loans in flight, losses, and
rebates owed.

**For the decision** (notes §8): (1) the lateness liability's scale under a riot — cap it, price it from income, or keep it as the
honest bill; (2) the state-rejecter red team is impossible under §14's blind view — strike it, or decide whether a reviewer may know it
inspects the state; (3) Hypothesis 5's invariance of real wealth failed through the strategy's quantity constant; (4) the at-cost
control's retraction is the design, recorded; (5) 2.2.0 — entry and delegation — against books that now read.

## Design revision 10 — the rebate from income (2.2.0, October 19, 2026)

**The candidate and its reviews.** `2.2.0-rc.1` arrived after run 14's notes: one rule — the clock's rebate claim stays the measure of
lateness, recorded at the stop; Ω's fee income after the debt accrues to the period's pool; at the period's close the claims stopped in the
period are paid pro rata and the rest is forgone, read, never owed; no liability stock — with two rulings carried (the reviewer's view
stays blind to the actor; Hypothesis 5 of 2.1.0 restated as the finding) and the supply side moved to 2.3.0. The implementer's review
(`dr10_2.2.0-rc.1-review.md`): implementable with one correction — I32 said "every inflow" where §2.2 said "fee income", and pooling the
troops' capital returns would lock the state's working capital and make every summons a loan — and five readings (the pool as a lock on
Ω; Hypothesis 2 too strong by one period's fees; a stated r_s not indexed by the engine, a conformance gap fixed with the revision; the
close inside the tick; the I10 note and `test_v21`'s pin). rc.2 adopted all of it; the rc.2 review: implementable as it stands. **Accepted
verbatim, no ruling.**

**Implemented** (`Params.rebate_pool`, on with `bank`; the commit named below): the claim recorded at `_stop_clock` with r_s indexed at the
first lock when stated; the inflow hook pooling a fee event after the debt as a lock on Ω (`_is_fee_event`, `_pool_add`), the returns of
capital landing unlocked as before; `_settle_pool` at the boundary — the release, the pro-rata payments (I10-exempt by note), `rebate_paid`
/ `rebate_forgone` on each request, the period's `claims`, `pool`, `rebates_forgone`, `forgone_share`, `omega_retained_period`, the order
on the remainder; no liability ever made. I32; I30, I26, I15 amended. `test_v22` (9); `test_v21` pins `rebate_pool=False`; the goldens
re-pinned once; two reviewer tests that pinned a service fee advancing a reviewer's reimbursement mid-period are expected failures
(30). Suite 282 passed, 0 failed, 30 expected failures. Driver: `--rules 2.2.0` default
(`2.1.0` the control), `--small-requests`, the pool and forgone columns. Spec consolidated as `v2_2_0` (§2.4, §3.1, §4.5, §10.4, §12.3,
§14, §17–18, §20, Appendices A, C, O), 2.1.0 to history, rc.2 verbatim as `dr10_the_rebate_from_income_2.2.0.md`.

**One consequence found on the way, for the reviewer.** §4.3 has Ω advance a reviewer's reimbursement when the allowance is exhausted
and pay its outstanding reviewer claims first in, first out on every inflow. Under the pool a fee inflow is locked until the close, so the
advance and the claim are paid from what the pool excludes — the returns of capital, the retained balance, the pool's remainder at the
close — and in a world that starts with no float they wait for the close. Two reviewer tests that pinned a service fee advancing and paying
a claim at once (`test_review_06`, `test_r4_08`) are expected failures with that reason; their principle holds at the close (`test_v22`).
Ranking the claims before the pool was tried and does not save them — the advance, not the payment, is what the pool changes — so the
text stands as written and the reading is recorded in Appendix O. In a quiet market Ω's retained balance covers the advances from the
second period on; whether a reviewer's reimbursement should wait for the state's rebate pool in the first period is the reviewer's call.

**Next:** run 15 — the revision's §8 against run 14's seeds in its order: §6 first; the riots second (the crowd and the flood at N_T 40:
claims, paid, forgone by period, Ω retained, M, hoards, on time, lateness); the quiet market at 50–80%; the order under the at-cost control
and the three-quarters failure; the red team (the small-request requester, the withdrawing requester); told read whole. Then 2.3.0 — the
supply side.

## Run 15 — the rebate from income under 2.2.0 (October 19, 2026)

**What ran** (`results/studies/2.2.0-rebate/`, 260 runs on run 14's seeds, all audits passed at `148069fe`; notes
`results/studies/2.2.0-rebate-notes-for-reviewer.md`): §6; the riots (the crowd of thirty, the flood of twelve, N_T 40); the quiet market
at 50–80%; the order (the at-cost burn and the three-quarters failure at the wall); the red team (two small-request requesters; the
withdrawing requester); told read whole.

**Findings.** *The stock is gone and the bill is read:* no liability at any close in 260 runs; the flood forgoes 28,000 of a 34,200 bill
— 0.87 of every flooded period's claims (§6 said 0.84) — Ω retaining nothing in those periods and ending 1,500 up instead of 27,000 down;
the crowd's three periods forgo 0.84 / 0.94 / 0.93 and the period after pays in full, Ω retaining again at once. The loans line empties in
the riots (peak 62 against 1,700–1,800): the returns of capital stay unlocked and fund the summonses. M, hoards, on time and lateness
within variance of run 14 (Hypothesis 1). *The quiet market does not notice beyond one period's fees:* every claim paid in full; Ω
retained lower by 186–200, loans of 78–103 a run in the first period only; price, share, honesty and wealth identical within noise
(Hypothesis 2 as restated). *The order shows:* the at-cost control's forgone share climbs from zero to **1.0 by the eighth period** as the
debt takes every fee first; the three-quarters failure's to 0.80; the wall's retraction unchanged (Hypothesis 3). *Nobody games the pool:*
two small-request requesters collect 9 each like everyone (a side effect: posting at exactly B̄ hands the request to the state, share 52%,
P_t 28.9); the withdrawer's rebates are the holder's (Hypothesis 4). *Told whole:* marks, lateness and the forgone share read zero in a
quiet market and move together in a riot.

**Accepted as recorded (October 19).** One ruling for Appendix O: a §4.3 reviewer advance may draw on the pool during the period, the pool
at the close net of it — verification before the state's blame; **to be implemented with 2.3.0**, when `test_review_06` and `test_r4_08`
return from the expected failures. Until then the engine runs 2.2.0 as accepted (the advances wait for the unlocked balance). **Next:**
2.3.0 — the supply side, entry and delegation; the draft follows.

## Design revision 11 — the supply side (2.3.0, October 19, 2026)

**The candidate and its reviews.** `2.3.0-rc.1` opened the door both ways: entry as a probationer with a bank-minted float, exit with the
wallet out, competence as a private per-actor cost, delegation with the troops never nested, the outsider's view, run 15's advance ruling.
The implementer's review (`dr11_2.3.0-rc.1-review.md`): implementable with two corrections — the §6 child was a probationer, which wins
no award and is not pinned once admitted; a nested request has carried no pots since 1.1.0, so the root requester paid for the child's
inspection — and six readings (the cost hidden by the view, not the record; a clean departure on four conditions; admission possible on an
undetermined record; the summons already root-only, seats staying the troops'; admissions apart from readmissions; the pool advance as
written). rc.2 adopted all of it and decided the second correction as a rule: **the parent posts the pots** (Q3 answered, the 1.1.0 reading
the control); the rc.2 review: implementable as it stands, one reading — a node's pots settle at the node's own closure. **Accepted with
that ruling (Appendix P):** §4.3's payout rule per node, a case closing when it and everything under it have settled; I19 "for every case";
I10's exemptions narrowed to the case's own closure.

**Implemented** (`Params.supply`, on with `bank`; `F0` 50; `nested_pots parent|root`; the commit named below): `arrive` and `depart` with the
`arrival` kind and the archive; admission on n_min bad plants counted apart from readmissions; `award` refusing a probationer on any request;
the nested all-in with the pots locked at posting, drawn at the award, the case's reviews on its own pool, `_maybe_close_node` at the node's
closure and the tree's closure scoped to the root; the reviewer advance from the pool lock; I33–I36, I1 / I10 / I15 / I19 / I32 amended; the
view's operations and the outsider's fields. `test_v23` (13); `test_v101` pins `supply=False`; the goldens re-pinned once. **The expected
failures (32):** two reviewer tests superseded by the parent's pots (`test_review_13`: three children unaffordable on a float of 50;
`test_r4_07`: the root's allowance no longer exhausted by a nested review); the two 2.2.0 ones (`test_review_06`, `test_r4_08`) **do not
return with the pool advance** as §2.6 expected — the advance at completion takes what the pool holds, the 0.5 of pooled fee in those tests,
so the figures they pin move by it; the ruling is implemented and they stay expected failures with that reason; `test_review_17` (the kill
fee) holds at the 2.3.0 figures. Suite 293 passed, 0 failed, 32 expected failures. Drivers: `--rules 2.3.0` default (`2.2.0` the control);
per-actor costs; the entry pool; delegation; the readings. Spec consolidated as `v2_3_0` (§2.1, §4.3, §5.1, §9, §10.4, §11.2, §16–18,
§20, Appendices A, C, P), 2.2.0 to history, rc.2 verbatim as `dr11_the_supply_side_2.3.0.md`.

**Two things the smokes showed before run 16, for the record.** At the default spread no parent delegates: the expected child's bid
(the median cost at the starting margin, about 9) exceeds what any parent saves after the overhead (the nested fee, about 4.5 of pots' net
cost at the index, 2 of care); at σ 0.8 the dearest three members delegate — brokers at cost rank 0.95 — and most of their nested requests
go unawarded within T_wait, since the children's ratchet bids exceed the parent's ceiling, so the parents self-execute. With the pool of
twenty at 60/40, nineteen arrive in the first period, admissions begin near tick 290, and the price at tick 800 is 24 against 31.

**Next:** run 16 — §6; entry at 60/40 and 80/20 with the pool of twenty (§8.2); the spread at 20 honest, σ 0.2 / 0.43 / 0.8, delegation on
and off, the `root` control at 0.8 (§8.3); then entry and the spread together (§8.4), the knobs, the riot with entry, the red team, told under
entry as time allows.

## Run 16 — the supply side under 2.3.0 (October 19, 2026)

**What ran** (`results/studies/2.3.0-supply/`, 240 runs on run 15's seeds, all audits passed; the engine at `ee4c481c` with the fixes
`4812ee36` and `dc522fc7` named per cell in the manifests; notes `results/studies/2.3.0-supply-notes-for-reviewer.md`): §8.1 §6; §8.2
entry at 60/40 and 80/20 with the pool of twenty honest candidates; §8.3 the spread at 20 honest, σ 0.2 / 0.43 / 0.8, delegation on and
off, and the `root` control at 0.8; §8.4 entry and the spread together at 60/40. §8.5–8.8 not yet run.

**Two fixes on the way, recorded.** I34 caught a departed parent receiving its child's pots at the node's closure: `depart` now refuses
while an obligation *to* the actor is unpaid — a case of its own not yet final (the price at vesting, a court fee won), a nested case it
posted whose pots have not refunded — "commitment" read to the money's end. The driver's reviewer selection excluded a nested case's parent
as the engine does. One cell (the `root` control) ran half before and half after the first fix; its figures do not depend on it.

**Findings.** *Supply finds its level, and the level is the ratchet's:* all twenty candidates arrive in the first two windows, fifteen are
admitted at a mean of 310 ticks, every stamper departs on zero earnings and the dearest careful follow (departed median cost 8.4 against
the arrivals' 7.9); the market ends with 19 members where run 15 had 8, the state's share at 0.7% against 39%, the honest earning
1,237 real against 1,928 — and the price at 22.9 against 32.9: it dips to 18 as the cohort is admitted, then climbs back to 22.5 as the
free members settle at nine and the margins ratchet to run 13's constant, the twenty-honest cell to the unit (Hypothesis 1 in direction,
not in level). *Entry relieves inspection only until admission:* reviews unassignable are flat while the probationers carry the initial
seats and rise once they are members who deliver and the stampers who sat on duty have left (Hypothesis 2 fails). *Delegation runs where
the spread is wide and the children refuse the price:* nothing at σ 0.2, 5% of awards at 0.8 (predicted a fifth) — three quarters of
nested requests die at T_wait because the child's ratchet bid exceeds the parent's saving; the gain from trade is 3–4 where a child is
found; brokers are the dearest two or three members with 5% of the market; a careful parent's wrongful rejection is overturned on the
child's appeal, a stamping parent approves bad child work (Hypotheses 4 and 5). *The `root` control answers §8.3:* the parents delegate
2.4 times as much (294 against 122) when the root pays for the child's inspection. *Selection at the wide spread with entry:* the members'
median cost falls from 8 to 6.4 as the dear depart (9.3) and the cheap arrive (7.2) — and the price rises with the spread (21.8 / 22.5 /
23.5) because it follows the free members' count, not their cost (Hypothesis 3: half). *Hoards over M* 0.84 with delegation and without
(Hypothesis 8: the circuit does not close at this scale). *Honesty unmoved* (Hypothesis 7).

**For the decision** (notes §5): the level supply finds is the strategy's constant (a reading on the margin rule for 2.4.0's §8);
entry's inspection relief ends with admission (a §12.1 question — the duty cap on an all-honest list); the pool's size is the lever's
length (§8.5's knobs); delegation's scale is the children's bids. Nothing in the rules. **Next:** §8.5–8.8 — the knobs (the
reservation, the arrivals a tick, the float), the riot with entry, the red team (the cycler, the swarm, the greedy parent, the
below-cost child, the stamping broker), told under entry — then 2.4.0 as the reviewer sketches it.

## Run 17 — the inspection queue, the rest of §8, three variants under 2.3.0 (October 19, 2026)

**What ran** (drivers at `95081c19`, the engine unchanged at `4812ee36`; 700 runs on run 16's seeds, all audits passed; notes
`results/studies/2.3.0-run17-notes-for-reviewer.md`): **A** `results/studies/2.3.0-queue/` — the inspection queue on the 60/40 entry cell
with new driver diagnostics (every seat that waits by kind, its seating steps unfilled and who seated it; at every waiting tick the actors
by state against the kind waiting; the cap against the members on duty), w_R 0 / 2 / 5, the duty cap ⅔ / ¾ / 1, and the control with the
determined-record gate off. **B** `results/studies/2.3.0-supply-b/` — §8.5 the knobs (pool 60; r 0.5 / 1.2; three arrivals a tick; F_0 0),
§8.6 the crowd of thirty with the pool, §8.7 the red team (the cycler, the swarm, the greedy parent, the below-cost child, the stamping
broker), §8.8 told under entry (both ceiling policies, hold and withdraw). **C** `results/studies/2.3.0-strategies/` — patient customers
(0.7 B̄ raised after 10 / 20 / 40 ticks), the faster margin decay with entry, the ceiling-aware child.

**Findings.** *A: the queue before admission is panel eligibility, not the cap or the window.* Nineteen of twenty waiting seats in the first
three hundred ticks are audits and appeals; while they wait there are five members on duty idle but not panel-eligible, eight more off duty,
free, funded and duty-eligible but not panel-eligible, ten probationers barred from panels — and 0.1–0.6 members in the decisive state (free,
fit, under the cap, unseated), none held out by the cap (slack eight seats). The troops take 605 of 710 waiting audits at exactly w_R; after
admission the state's inspection share falls from 46% to 0.1% and the queue is initial reviews filled a step later by the rotation's lag.
w_R 0 / 2 / 5 give the state 18 / 16 / 14% of inspection seats and 0.7 / 1.4 / 4.9% of deliveries (members held on duty do not bid); the cap
cells are one run. The control (`--panel-determined off`) drops the troops' seats from 688 to 8 and raises false approvals from 13 to 35: the
gate is what the troops bridge. **The §12.1 question is answered no.** *B:* pool 60 takes the price to 14.5 and the honest to 810 (the
ratchet broken by turnover); F_0 = 0 admits nobody (no bond, no seat, no record); r and the arrival rate move nothing. The crowd with the
pool: the state 17% against 53%, the price back to 22 within two windows, the bill as unpaid (88% forgone). The cycler (260 cycles) is never
admitted, its wallet stays its float, and the loop pays 2,000 of plant mint, 8.5 probation false approvals and a quarter of the honest
admissions; the swarm is never admitted; a greedy parent loses every appeal; a below-cost child that never delivers triples delegation and
costs the parents their guarantees (−4%); the stamping broker's false approvals are the stamper's and it departs. Told under the market-aware
ceiling with the pool is a busy line: 354 marks, 40% forgone at a price of 23.5 (run 15: 34 marks, nothing forgone, at 39.6). *C:* **patient
customers collapse the price to 4.8 and hand 86% of the work to the state below every member's cost but the cheapest** — the state delivers
at B̄, the ceiling is 0.7 B̄, P_t counts the troops, the members depart, the requesters hoard 9,000 a wallet (the one result that may warrant
a §19 decision: a reservation price for the state's delivery, or the clock reading a raise as a posting); the faster decay takes the price to
8.3 with the honest's real wealth unchanged at 1,256 (the ratchet's constant is nominal); the ceiling-aware child wins every nested request
and halves the gain from trade.

**For the decision** (notes §5): nothing for §12.1; the float as a gate (§2.1); the cycler's and swarm's bill to the loop (§8.7's text);
the kill fee unexercised against the below-cost child (a driver gap); patient customers against the state's delivery at B̄ (the reviewer's
§19 call); the price level as the members' nominal choice. **Next:** the reviewer's reading of A, then 2.4.0 as sketched.

## Design revision 12 — the state's reservation (2.4.0, October 19, 2026)

**Why.** Run 17's batch C: a patient demand side — requests at 0.7 B̄ raised to B̄ only after T ticks — took the price to 4.8 at T 10 / 20 / 40
alike and handed 78–86% of the work to the troops at a price below every member's cost but the cheapest three; the members left, the requesters
hoarded 9,000 a wallet, every request was late by design. The mechanism was the rules': the state delivered at B̄ with no reservation of its own,
P_t counted its price, and the market's cost floor was written nowhere. The reviewer's sketch (rc.1) gave the state a public reservation; my
review found two corrections (the kill fee is the child's *recorded* cost, so a lowballer that never worked pays and is paid nothing; R_T was
the fund's troop reserve — the floor is $\underline{B}$) and eight readings, all adopted in rc.2 (`spec/design_revisions/dr12_*`); accepted with
an editorial reading (the header's slip) and one conformance correction recorded in Appendix Q.

**The rule.** The state delivers at $p_T=\max(\bar B,\underline{B})$, $\underline{B}$ = 8 nominal and public (0 the control); the summons only where
β ≥ p_T; the guarantee, the base fee, the burn and P_t's count at p_T; a request posted or raised below the floor marked *below the state's
reservation* with its tick, readable, the floor in the view, its clock stopped while it holds the mark (the clock's one condition β ≥ p_T); the
award pass gathers only requests at β ≥ p_T (the 1.7.1 correction — a below-market request older than w_A used to hold a member's slot it would
not use); F_0 ≥ G^V on the parameters (the float is the bond's capital); §9.3's kill fee in the delegation driver, no rule moving. Everything
else 2.3.0.

**Engine and drivers.** `Params.state_reservation`; `_state_floor` / `_state_price`; `_summon_delivery` at p_T; the award pass's filter;
`_clock_runs`; `_mark_reservation` at `post_root` / `raise_ceiling`; `Params.__post_init__`; I37; the view's fields; `test_v24` (11); goldens
re-pinned once (the equivalence scenario posts below the market, so the award pass's correction moves its summonses; the floor never binds
there). Suite 304 + 32 in three modes. Drivers: `--state-reservation`, `--ceiling-policy patient | patient-blind`, `--parent-cancel`, the
columns; `--rules 2.3.0` the control.

**Next.** §8 on run 17's seeds in its order: §6; the patient cells (8.2) and the floor sweep (8.3); the invisibility check (8.4); the riots (8.5);
then the kill fee (8.6), the red team (8.7), the static w_A sweep (8.8).

## Run 18 — the state's reservation under 2.4.0, §8.1–8.6 (October 19, 2026)

**What ran** (`results/studies/2.4.0-floor/`, 580 runs on run 17's seeds at `f12c803a`, all audits passed; notes
`results/studies/2.4.0-floor-notes-for-reviewer.md`): §6 reproduced in `test_v24`; the patient cells at T 10 / 20 / 40 under the floor at 8
against the control at 0 and the `patient-blind` reading; the floor sweep 4 / 8 / 12 at T 10; the invisibility check on the 60/40 entry cell,
the pool of sixty, the faster decay and the quiet 50–80% cells; the riots (the crowd with and without the pool, the flood); the kill fee with
the parent's cancellation on and off against the below-cost child. A first sweep ran with two driver gates still reading 2.3.0 alone (every
member at one cost) and was discarded before anything was kept; the fix is `f12c803a`.

**Findings.** *The floor holds where the patient customer pushed and nowhere else:* P_t 7.7 / 7.2 / 7.5 against the control's 4.8 / 4.5 /
4.5 — the state at exactly 8, the members under it (median cost 5.1–5.4, $\bar B$ 7.1–7.7), P_t the blend; the state's share 13–27% against
78–86%; members 6–10 against 3–4; lateness 1.2 against 14, the rebate bill 25 against 466; the requesters still hoard (7,600–9,100 a wallet).
The blind policy deadlocks as predicted (the state 0, 24,000 declines, P_t 5.2). The sweep: 4 is the control to the unit; 12 prices the state out
(0.6%) and admits ten members, the market serving the patient demand at 8–9. *Invisible elsewhere:* the entry cell, pool 60, the decay edge
(B̄ 8.43), every quiet cell and every riot are identical under 8 and 0 to the decimal — no summons declined for the floor anywhere. The award-pass
correction moved three posts in 2,554 of the entry cell and the riots within a percent. *The kill fee as this driver exercises it closes nothing:*
every fee zero (as rc.2 expected), 30 cancellations against 117 lowball awards, the roots' failures 658 against the base's 602 — the parent
cancels when its own deadline leaves room, and the lowballer's deadline comes first; Hypothesis 5 fails in the driver, with the earlier
cancellation variant named for the next batch.

**For the decision** (notes §7): the floor is also a price the cheap members bid up to (margin 0.36 against 0.07) — a reading for §2.1's
consequence, recorded in Appendix Q at the reviewer's direction (wording only); the hoard is the demand side's posting rate, not the floor's;
the default 8 stands.

**The last batch** (notes §9–10; drivers `46c4cebe`, 220 runs): *the cartel at exactly the floor* is served at the floor — the state half the
market at 8 after w_A, the cheap members the rest at 7.7, P_t 7.9 (without the floor the same policy spirals to 4.6). *Members colluding just
above the floor* take the whole market at their price: against the ratchet a price cut (12.5 against 22.5) that pays them more in real terms;
against the patient customer B̄ is their 8.08 and the state is out (1.6% against 17%) — the floor is a floor, not a ceiling on collusion.
*The static w_A sweep*: nothing where the price is the ratchet's, two points in the 80/20 captured market — the knob recorded as unnecessary,
the hold closed. *The parent cancelling at the child's deadline* cancels every lowballer (131 of 131, every fee zero), the nested failures
vanish and the roots' failures fall below the base (568 against 602), the honest's loss closes from 4% to 3% and not further — the overhead
of 299 nested postings against a child that risks nothing; the rule's answer rc.2 named (a guarantee not released on a non-performance
cancellation) is the next candidate. **Next:** the reviewer's reading; 2.5.0 as sketched.

## Design revision 13 — the missed child (2.5.0, October 19, 2026)

**Why.** Run 18's last batch: a parent cancelling a child that had not delivered released the child's guarantee the lapse would have forfeited, so a
lowballer risked nothing (131 cancellations, every fee zero, every guarantee released). My review found that the lapse the sketch presented as
new is the engine's since v1.0 — step 2 of the tick loop finalizes a committed case at its deadline, forfeits the guarantee to the requester and
releases the bond — and that the open door was the cancellation reached before the lapse; rc.2 redrafted the rule as the refusal; accepted
verbatim. **The rule.** `cancel_nested` is admissible only before the earlier of the child's submission and the request's deadline; at or after
the deadline it is refused with no effect. The deadline tick is the child's: it may still submit on it. **Engine.** `Params.missed_child`; the
one condition; I38; `test_v25` (7); suite 311 + 32; goldens unchanged. **A reading found in implementation, for the reviewer.** The driver's
clock runs a tick ahead of the world's, so run 18's "cancel at the child's deadline" cancelled at the world's deadline − 1 — a pre-deadline
cancellation 2.5.0 admits ("a parent that wants out acts by d − 1"). Under the rule a parent has a choice at the child's silence: cancel the
tick before (the guarantee released, one tick saved — run 18's move, `--parent-cancel eve`) or wait for the lapse (the guarantee gained, one
tick lost — `early`, the cancellation at the deadline refused). §8 runs both against the 2.4.0 control that admits the deadline-tick cancellation.

## Run 19 — the missed child under 2.5.0 (October 19, 2026)

**What ran** (`results/studies/2.5.0-missed/`, 480 runs on run 18's seeds at `44ef6e47`, all audits passed; notes
`results/studies/2.5.0-missed-notes-for-reviewer.md`): §6 in `test_v25`; the lowballer cell under the parent's three moves (`early` at the
deadline tick, `eve` the tick before, `off` waiting) × 2.5.0 / 2.4.0; the honest delegation cell and run 16's spread cells; the identity
check (entry, the patient cell at the floor, the crowd with the pool); the red team (farming parents with children reading the deadline or
not; the lowballer's empty result).

**Findings.** *The refusal holds and changes one cell:* a parent's cancellation at the deadline tick is refused (98.5 a run), the lapse runs,
the lowballers forfeit 200 a run — and the cell is run 18's no-cancellation cell to the decimal: roots 675, not between 568 and 675; the one
driver step between cancelling the tick before and waiting for the lapse is the whole gap. *Run 18's move was `eve`* (the world's deadline − 1),
admitted under both rules and identical (568, 1,262, the guarantees released). So under 2.5.0 a parent facing a silent child chooses: cancel the
tick before (save the root, free the lowballer) or wait (take the guarantee, risk the root); the honest do better waiting (1,274 against 1,262;
the base 1,304). *Honest children and everything else identical to the decimal* under 2.5.0 and 2.4.0 (seven cells). *The red team:* a parent
posting one-tick deadlines cannot farm — the drivers' children meet any deadline of one tick, and a child that needs two reads the deadline and
declines (455 a run); a lowballer's empty result is rejected by 81% of parents and loses 96% of its appeals, and still beats the lapse — 19% of
parents approve it and build on it (nested false approvals 18.8 against 2.85). Nothing in the rules moves.

**For the decision** (notes §5): the parent's choice under 2.5.0 between `eve` and the lapse — the rule's words leave it to the parent; the
guarantee floor as the next candidate if 2 a miss does not deter (it did not stop lowballing here); the empty result as a parent-side problem
caught at the panel's rate.

**The reviewer's reply (October 20).** Run 19 accepted as recorded; nothing in the rules moves. The parent's choice between the tick before
the deadline and the lapse is intended — the rule's words leave it to the parent. The guarantee floor is not pursued. The empty result is the
chain's: a parent-side problem the panel catches at its rate, not the missed-child rule's. **2.5.0 stands.** No appendix note, no errata.
**Next:** the reviewer's next candidate, if any.

## The 2.x account (October 20, 2026)

The reviewer's consolidated account of 2.0.0 → 2.5.0 and runs 12–19 is kept verbatim at `docs/economy_2x_account.md`, with the
implementer's review beside it (`docs/economy_2x_account-review.md`): an account under §19, nothing moving; four corrections of fact
(§18.1's q7 is monetary behaviour and q10 constructibility; 2.0.0's deficit was retired as a rule by 2.1.0; the lagging auditor is zero in
the quiet cells, not the drift wave or the cycler; the riots' loans peak in the tens since 2.2.0) and wording notes, every figure else
verified against the notes; the author applied all of them the same day and the revised text is the one kept (the review's closing note records the diff). It reads the programme as at the marker set for the learned red team. **Next:** the brief for it, if that is
the reviewer's next step.

## The learned red team — the brief (October 20, 2026)

The reviewer's brief for the learned red team is kept verbatim at `docs/red_team_brief.md`, the implementer's review beside it
(`docs/red_team_brief-review.md`): a study brief under §19 — evaluations under the fixed rules, a win a finding for a revision drafted
after. The question: is there an unfaithful strategy that still pays under 2.5.0 — the sleeper, telling plants apart (first, alone; a win
halts the study), the selective cheat, collusion through the blind view, the delegation chain, money games, the customer; a second track
on stability under learned bidding. The tool is LeWorldModel (a JEPA world model with SIGReg, planned by CEM) on stable-worldmodel; the
review reads it as a world model and a planner with a learned wealth head as the cost, a decision event as the step, the truth bought
through care only, and names Q2's leak surface in the plants' construction (same-tick seating, the price at P_t, the rate's rhythm).
Build plan: `agentic_sim/redteam/` as a separate package the suite never imports, a conda environment at Python 3.11 with torch (MPS).
The five decisions were taken as proposed on October 20 (all ok); the build plan sent to the reviewer is `docs/red_team_build_plan.md`.
**Next:** the build — `agentic_sim/redteam/`, then Q2 alone.

## The learned red team — Q2 before training: the hand-written tell-reader (October 20, 2026)

**What ran** (`results/studies/rt-Q2/`, 240 runs at drivers `f55a234d`, engine `44ef6e47`; notes `results/studies/rt-Q2-notes-for-reviewer.md`):
as the reviewer's note on the build plan asked, a hand-written reviewer that reads the view for a plant's tells before any learner trains —
`gap` (seated the tick it was submitted), `cap` (K at this period's index), `idage` (the case id newer than every root the reader saw
available before the submission tick), `all`, and `oracle` (the plant marker itself, declared non-conforming — the upper bound) — one reader
in eight careful actors in run 16's cell, seeds 21–40 and 1–20 with controls, paired by seed against the same actor reviewing carefully.

**Findings.** *The construction leaks and the gate is blind to it:* the id's age passes every plant on forty seeds (a plant's id is minted at
its submission, a root's at its posting); the two tells the reviewer named do not separate (`gap` fires on a real case seated the tick it was
submitted; `cap` is every root posted this period) and `gap` costs its reader a third. *The leak does not pay:* the `idage` reader stamps
13–18% of real work and is within noise of itself; the oracle stamps everything, is never suspended, fails fewer plants than the careful — and
ends 28% poorer (−385 ± 120 eval, −361 ± 147 train): the audit prices the stamps through the bond and ρ (bonds 83 against 24, ρ 0.58 against
0.89, awards −31, departures 6/20 against 1/20); the plant record only decides suspension. *The stronger adversary* is Q1 with the detector in
hand — the sleeper that cannot be suspended.

**For the decision** (notes §6): whether the found separation is the Q2 win that halts (§4's criterion met) or a construction finding to
repair before the learner trains while the study goes on (§1's criterion not met even at the upper bound — the implementer's reading); the
repair's shape (the plant's id reserved τ ticks ahead; opaque ids; a seating delay — the id, not `t_submit`, is the leak); `p_effective` is
exposed per actor today and the learner reads only its own. **Next:** the reviewer's ruling; then the environment and Q2's learner on the
repaired construction, or Q1.

## Design revision 14 — the plant's disguise (2.6.0, October 20, 2026)

**Why.** Run 20 (the learned red team's Q2, hand-written first): a plant was built submitted, so its id was minted at its submission while a real
root's was minted at its posting a tick or more earlier, and a free member sees the available roots every tick — the `idage` reader passed every
plant on forty seeds and was never suspended; the audit still priced its stamps (the oracle −28%). The reviewer ruled the study paused for the
repair; rc.1 the same day, my review (the fresh name is itself a tell in a public record that names awardees — the test scoped to a member's
observations; three corrections of fact; five readings), rc.2 adopted all, accepted with one ruling: the deadline comes with the report as the
price does, the draw only on the p_T path, the time to submission the plant actor's draw within (0, τ]. **The rule.** A plant goes through the
market — posted as a root under a fresh plant-requester name with a ceiling drawn from the trailing real roots', open to the free members and
waiting as a real root waits, awarded to a fresh plant-actor name at the price and work ticks the market's selection reports (past w_A at p_T,
counted apart), submitted at a draw from the trailing real deliveries' within (0, τ]; fresh names alias the two plant wallets; no fee, no clock,
not in B̄ or P_t, marked and counted as any root; the dial's plant counts published at the close; the indistinguishability test widened to
everything a member observes, the drivers' convention its boundary; public identifiers opaque. **Engine** (`7c948b41`): `Params.plant_market`,
`post_plant`, the award as the report, the p_T path, the submission step, the trailing window, the aliases; I15/I21/I29/I37 amended; I39, I40;
the view's id translation and counts; `test_v26` (12); suite 323 + 32; goldens re-pinned once. **Drivers:** `--rules 2.6.0` default, the
readers `seen`, `post`, `price`, `losttie` beside the four of run 20, `freshname` outside the convention, `--tie-break`, `--genesis-duty`,
`--trailing-periods`, the plant readings. **Next:** run 21 — §8 on run 20's seeds.

## Run 21 — the plant's disguise under 2.6.0, §8 (October 20, 2026)

**What ran** (`results/studies/2.6.0-disguise/`, 660 runs at drivers `c3c12b77`, engine `7c948b41`; notes
`results/studies/2.6.0-disguise-notes-for-reviewer.md`): the ten tell-readers (gap, cap, idage, seen, post, price, losttie, all; oracle and
freshname outside the convention) at one reader in eight careful actors on seeds 21–40 and 1–20 with controls, paired by seed against the same
actor reviewing carefully; run 16's entry cell, run 18's patient cell at the floor, run 19's lowballer cell and the crowd with the pool against
`--rules 2.5.0`; the knobs (the trailing window of two, the tie-break by id, the earlier orderings). A first pass ran on a view returning copies
— stale to a driver that reads before it acts (no member audit was ever seated; the 2.5.0 control did not reproduce run 20) — and was discarded;
the view returns live read-only proxies since `c3c12b77`, and the 2.5.0 control reproduces the previous driver tick for tick.

**Findings.** *The tells are gone:* the id's age (= the seen set = the posting interval) passes 66–71% of plants and fails more plants than it
stamps real work, −303 ± 130 and −560 ± 146 real against itself careful; gap, price and losttie are plain stampers, suspended and gone; cap and
all are careful in all but name, within noise; oracle = freshname, a third poorer, the audit's price as in run 20 — the fresh name is the complete
tell outside the convention, where a strategy does not read. *The economy does not notice beyond the market's attention:* price, honesty, the
plant record and the honest's wealth within noise in the entry cell, the crowd and the lowballer cell; members lose 470–635 bids a run to plants,
the state's share of deliveries halves at entry (1.3% → 0.5%), plants reach reviewers four ticks later (lag 5.4 against 1.5), and where members
are scarce most plants go to their actor at p_T (294 of 361 in the patient cell). *Two readings outside noise:* the lowballer cell's nested false
approvals (1.2 → 2.45) and the patient cell's time to membership (135 → 169). *The knobs move nothing.*

**For the decision** (notes §5): Hypothesis 1 holds and the §7.6 test has its instrument; the attention's cost as measured; the two readings
and a lag-pinning cell to separate them; plants at p_T under scarcity as a reading for Q1; the proxy as a conformance correction of the surface.
**The reviewer's reply (October 20).** Run 21 accepted as recorded; 2.6.0 holds. **One ruling for Appendix S** (`86f7ed60`): the $p_T$ path
follows the summons pass, refusals included — a plant unbid by w_A that the pass would refuse for capacity or credit is marked and told as a
real root would be and waits, no place in N_T, no loan; `test_v26` 15 with the regression; the equivalence golden's seed 1 re-pinned with the
ruling (nineteen plants refused for credit in the scenario); suite 326 + 32. **The lag-pinning cell** (`results/studies/2.6.0-disguise/lag/`,
80 runs; notes `2.6.0-disguise-lag-notes-for-reviewer.md`): the ruling fires in neither the lowballer nor the patient cell (no refusal; the
baselines reproduce run 21 to the decimal); pinning the plant actor's submission to one tick shortens the lag 9.2 → 7.3 in the lowballer cell
and not at all in the patient cell, where the lag is the w_A wait before the plant goes at p_T; the two readings move toward 2.5.0 and stay
within noise of 2.6.0 (nested false approvals 2.45 → 2.15; time to membership 169 → 149) — the draw is not their mechanism. **Then:** the Q2
probe when the environment is built, then Q1 with own odds visible and hidden.

## The learned red team — the environment (October 20, 2026)

Decisions 1–5 taken; the conda environment `elef-redteam` (Python 3.11, torch 2.14.1 with MPS, gymnasium 1.4.0, stable-worldmodel 0.1.1,
opencv-headless) is installed beside the project's Python; le-wm's `module.py` and `jepa.py` are vendored under MIT at
`agentic_sim/redteam/lewm/`. The driver carries the learner's slot (`--learner-slot on`: the slot actor's reviewing decisions come from a
policy `Stamping.learner(run, reviewer, view, r)` → 0 care / 1 approve blind / 2 reject blind, the truth never shown to it; `LEARNER` kind,
`learner_decisions`, `learner_false_approvals`) and `parse_args` / `build_parser` for the environment to build a run from a cell; every
existing run is unchanged (the 2.5.0 control identical to the decimal). **Next:** `redteam/obs.py`, `env.py` (the decision-event Gymnasium
environment), `collect.py`, `model.py`, `train.py`, `plan.py`, `run_q.py`; then the Q2 probe on the repaired construction; then Q1.

## Run 22 — Q2's learned probe on the repaired construction (October 20, 2026)

**What ran** (`results/redteam/Q2/`, red team at `4bfe846e`, engine `d5808eef`; notes `results/studies/rt-Q2-probe-notes-for-reviewer.md`):
the environment built as planned (the conda env `elef-redteam`; `redteam/` env, obs, collect, model, train, probe, plan, run_q, online); 80
offline episodes on each of three constructions (2.5.0; 2.6.0 as first implemented; 2.6.0 corrected), the world model (LeWM's recipe on the
vector plus a wealth head) trained on each, a logistic probe for plant-vs-real on the latent, the raw observation, the context alone and the
case's fields alone; the learned reviewer (categorical CEM on the model) against careful on seeds 21–40 through ten online rounds; the
tell-readers rerun under the corrected construction.

**Findings.** *The probe found a tell the readers had the sign of wrong:* on the first implementation the plant actor's submission ran inside
the engine's tick step, after the driver's seating, so 99% of plants reached their reviewer with a seating gap of one tick (raw AUC 0.97, the
gap alone 0.85); corrected at `d5808eef` — the orchestrator's instrument submits for the plant actor in the members' step (`submit_plant`),
Appendix S, `test_v26` 16, suite 327 + 32. *Under the corrected construction* the case's fields read 0.60 among initial reviews (no field
above 0.54), the context 0.61 — the plant rate's rhythm, public by rule; Hypothesis 4 holds. *The learned reviewer is a no-win outside noise
on the wrong side:* −507 ± 143 at round 10 (best −313 ± 126 at round 8), stamping plants and real work alike (0.62 / 0.65), 70% departing.
*The tell-readers under the corrected construction:* gap now passes plants at the careful's rate and is within noise; nothing within the
convention separates and pays; oracle = freshname lose. **Q2 does not halt the study.**

**For the decision** (notes §4): the correction's wording in §7.6; whether 0.60 is chance at this resolution; the rhythm as Q1's matter; the
learner's three fixes before Q1 reads anything (the terminal value, a longer horizon, careful-centred exploration); the re-arrival move for a
learner. **Next:** the reviewer's reading; then Q1 — the sleeper — with own odds visible and hidden.

## Run 23 — Q1, the sleeper: the calibration, the pre-calibration learner, the learner with re-arrival (October 20, 2026)

**What ran** (`results/redteam/Q1/`; code `b74fd348` the learner changes, `28aff6c3` the rulings, `055a1fd8` the hand-written references;
notes `results/studies/rt-Q1-notes-for-reviewer.md`). The three learner changes named after run 22 (the terminal value `--value mc|td`,
the horizon 16, ε from the careful policy); the reviewer's rulings after run 22 implemented (the calibration cell `--audit-roll off --pi0 0
--dial off`; re-arrival allowed the learner `--learner-rearrive on`, a period-boundary decision and the 45th observation field, lifetime real
wealth summed across identities; a bootstrap SE on every AUC; Appendix S). Six learned lines on the same budget (80 offline episodes, ten
rounds, seeds 21–40 the evaluation): three pre-calibration (visible, hidden, the td value), the calibration, two with re-arrival (visible,
hidden); the hand-written sleeper (`sleeper0.3/0.5/0.7`) and the hand-written harvester and leaver as references.

**Findings.** *The calibration failed:* where a blind stamp costs nothing the learner ends −203 ± 142 against careful (seven seeds of twenty;
the plain stamper +164 ± 158 — the cell's own win, which the learner did not find; it rejects blind 30% of the time, a move no cell prices
because the population never appeals). By the reviewer's rule the learner has not learned and Q1's results are not findings — reported and
labelled so. *The pre-calibration learner:* three no-wins outside noise on the wrong side (−723 ± 133, −473 ± 180, −499 ± 141), stamping in
the pinned band and rejecting blind; not a sleeper. *The hand-written sleeper:* stamping below odds 0.5 is within noise of careful (−12 ± 23,
29 false approvals, never suspended); below 0.7 costs a hundred. *Q1 with re-arrival, odds visible:* **+270 ± 89 on the brief's lifetime
measure** (fifteen seeds of twenty), made of thirteen arrival floats a run (655 real minted for one slot; 14 identities, one suspension each,
stamps at odds 0.99 — the pinned band); on its own earnings the learner is **373 ± 86 below** careful. The hidden line the same with fewer
cycles, within noise (+47 ± 88). The hand-written references do not reach it: the harvester (stamp all, leave every boundary; 21 names, 992 of
float) −113 ± 90 on forfeits; the leaver (careful, leave every boundary) +72 ± 29 but refused the leave at 11 boundaries of 12 — a live
obligation stands; the learner's stamp buys the suspension that discharges them. What it points at, if the reviewer reads it as a finding, is 2.3.0's float — a grant a fresh name carries
out by departing — not the taper. *Q2's probe with errors:* among initial reviews raw 0.679 ± 0.009 against context 0.629 ± 0.009; the
case's fields alone 0.595 ± 0.006.

**For the decision** (notes §7): the calibration verdict and the cell's resolution (the ideal policy clears by one SE at twenty seeds); the
re-arrival number and whether a departed name's float is the actor's lifetime wealth; the appeal policy on the population before Q3 so a
blind rejection costs what the rules say; the Q2 probe's gap, real at this resolution; the budget (five learned lines for one question).
**Next:** the reviewer's reading; then Q3, the selective cheat, on the fixes the reviewer accepts.

## Run 24 — the appeals baseline, the calibration cell's cost, the rolling window and the plant's posting (October 20–21, 2026)

**What ran** (the rulings after run 23, Appendix S; code `09622b85` the rulings, `64b82232` the posting correction and the probe's instruments;
notes `results/studies/2.6.0-run24-notes-for-reviewer.md`). Three evaluations under fixed rules: run 16's world with appeals on against off,
twenty seeds (`results/studies/2.6.0-appeals/`); the calibration cell's ideal (the plain stamper) against careful at care-cost scales 2–4 on
seeds 21–40 (`results/redteam/calibration/`); the plant's draws on a rolling window of the last k real roots and Q2's probe re-read with
paired errors and a per-field ablation (`results/redteam/Q2/offline-2.6.0-rolling*`, `models/probe-2.6.0-*-se80*`, `-se160-*`).

**Findings.** *Appeals:* 96 % of false rejections overturned, final N 599 → 510, vested +43, careful richer in real terms (+86 ± 39) with its
forfeits doubled, court fees to Ω about 2 D a run (zero through run 23); nothing else moves. Truthful appeals are the population's default from
here (`--appeal-policy none` reproduces runs 1–23). *The calibration cell is set at care-cost 4:* the ideal clears careful by 5.8 SE (+718 ± 123);
at 3 by 2.0. *The window closed nothing:* the case's separation sat in the seating gap (`rv_gap` the one field adding beyond the context) because
the orchestrator's instrument posted the plants after the tick's award pass, so a plant waited a tick more than every real root (1.13 against
0.41) and was seated first as the oldest of the tick's submissions (4.4 % seated later against 16.2 %). Corrected in the driver: the plants due are
posted in the requesters' step at a drawn position among the tick's postings (posted last they were the youngest and seated last — the tell
reversed). *On the corrected construction the criterion is not met at a third of the distance:* the case's fields add +0.016 ± 0.004 (appeals
off) and +0.019 ± 0.005 (on) at twenty test seeds, from +0.052; no field above +0.007 alone; the largest piece is the time a root was seen
available — the plant requester never raises its ceiling while 35 % of real roots are raised. Suite 328 + 32 in three modes at both commits;
goldens re-pinned once for the window.

**For the decision** (notes §5): record or undo the posting correction; the residual 0.02 — accept as the construction's floor, or a conformance
reading of the plant's ceiling (drawn as posted, raised as a requester's), or a design item; run 22's SE figures read 280 episodes (the same
reading at 80). **Next:** 2.7.0 (the arrival loan) on its acceptance; Q1's learned line once more under it with appeals and re-arrival on; Q3.

## 2.6.1 — the erratum and the one re-read (October 21, 2026)

**What went in** (run 24 accepted; the rulings in Appendix S; code `ecada79d`; the spec `spec/agentic_economics_loop_spec_v2_6_1.md`, 2.6.0 in
`spec/history/`; notes `results/studies/2.6.1-reread-notes-for-reviewer.md`). The posting correction recorded as the third conformance
correction of the instrument, with the principle: at every step of a root's life the instrument takes for a plant — posting, raising,
submission — the plant takes the step in the same pass a real root would, at a drawn position among the tick's real roots taking it, its
parameters drawn from the trailing real roots' at that step; the award is the market's already. Erratum 2.6.1 (E5): the plant's ceiling drawn
from the real roots' ceilings *as posted* (the window filled at `post_root`), and the plant requester raising it as the population's requesters
raise theirs (`raise_ceiling` admits a market plant, the difference minted; the driver's raise step covers the plants; `plants_raised`), so the
plant waits as a real root waits; I39 unchanged in substance. `test_v26` 19; goldens re-pinned once more; suite 330 + 32 in three modes.
Calibration at care-cost ×4 recorded; truthful appeals the population from here; a requester dispute baseline owed before Q7.

**The re-read** (one, as ruled: train 1–20, test 21–40, both populations). Under the erratum the plant requester raises as often as the
population's (36 % against 34 %) and the plant's tail to w_A is gone; the one asymmetry left is the wallet — a requester's raise is refused when
it cannot lock the difference, the plant's is minted — so a real root waits three ticks or more in 12 % of awards and a plant in 1 %.
The probe on forty seeds: the case's fields add **+0.011 ± 0.002** beyond the context in the population from here
(appeals on) and **+0.020 ± 0.003** with appeals off — not within two errors of zero, at or below 0.02: **closed at the construction's floor,
recorded** (from 0.052 at run 22, 0.016–0.019 at run 24); the largest piece the time a root was seen available, the wallet asymmetry.

**Accepted (October 21, 2026):** closed at the construction's floor, 0.011 / 0.020, named the wallet asymmetry; a drawn-wallet mimic a later design
item only if a learner monetises the floor; the withdrawal covered in advance by the Appendix S principle. **Next:** 2.7.0 (the arrival loan) on its
acceptance; Q1's learned line once under it with appeals and re-arrival on; Q3 calibrated at ×4.

## 2.7.0 — the arrival loan (October 21, 2026)

**Design revision 15**, the reviewer's draft after run 23 (rc.1 → rc.2 the same day; the implementer's reviews in `spec/design_revisions/dr15_2.7.0-rc.{1,2}-review.md`;
the accepted text `dr15_the_arrival_loan_2.7.0.md`; the consolidated spec `spec/agentic_economics_loop_spec_v2_7_0.md`, 2.6.1 to `spec/history/`). Run 23's
learner lived one name per period — arrive as a probationer with the float, stamp until the first bad plant suspended it (a suspension discharges every
obligation, so the exit is open), leave with the wallet, return under a fresh name — and the float was the whole of its win (+270 ± 89 on the lifetime
measure, −373 ± 86 on its own earnings, 655 real minted for one slot). 2.3.0 had said identity cycling buys nothing because a departing actor "has given
up its wallet"; it had taken it out. **The float is a loan of the bank's**: lent at arrival as before; repaid first from every inflow of income to the
name the moment it arrives, a return passing untouched (the table fixed against the engine's events — the rc.1 review's one correction: the reviewer's
cost reimbursed and a court fee coming back are returns, else an honest arrival's float is gone in twenty reviews; a child's guarantee forfeited to a
parent is income); recovered from the unlocked wallet at departure, the remainder leaving as `departure`, the shortfall the bank's default on arrivals,
read; an unrepaid loan no bar to departure; the genesis float the sponsor's gift. `Params.arrival_loan` (off is 2.6.1's grant); I1, I33, I34 amended, I41
new; the view's `depart` returns the wallet out (the brief's measure reads it; a live name reads net of its loan); the exit rule reads earnings gross of
the repayments. `test_v27` 12; **goldens unchanged** (no golden scenario arrives; the names line enters the record only once a name was lent to); suite
342 + 32 in three modes. **Accepted as written (October 21, 2026)** with two readings in Appendix T: the forfeited-guarantee row is a name's only for a
nested case; I41 scoped on the arrival tick.

**Run 25 (§8, `results/studies/2.7.0-notes-for-reviewer.md`, 592a5318):** the harvest closed — run 23's policy replayed under the loan ends
−1,199 ± 95 against the careful, exactly the grant's lifetime less the floats (−1,198 ± 109), policy by policy (harvester −1,203 / −1,234, stamper
−1,170 / −1,185, leaver +34 / +39); the entry cell within noise but for the constant (lent 990, repaid from income 976, recovered 13, defaulted 0.25)
and the liquidity reading (1.45 names a run below the bond before admission, none under the grant; no repaying member ever unfundable); run 15's fixed
population identical to the hash; the patient cell and the crowd within noise; the swarm carries out 1,008 ± 119 less — the floats — with the default
its forfeits (9.3 a run) and the loop's cost unchanged; the accomplice route (`--accomplice on`) moves 1,368 of nested ceilings and nothing of the
bank's (default 0 in 20 of 20: a parent needs an award, so an admitted name, whose loan the probation's fees repaid). **Next:** Q1's one line — the
learner calibrated at care-cost ×4, then the re-arrival cell under 2.7.0 (in flight, `results/redteam/Q1/{calibration-2.7.0,rearrive-2.7.0}`); then Q3.

**Run 25 accepted (October 21, 2026):** 2.7.0 holds, H1–H4 as stated; the liquidity reading recorded with its number, nothing fixed (the named
fallback stands if admissions ever move outside noise); the appeals note a note and a method point (the control in the population in force); the
accomplice route closed unless Q1's learner is admitted with a loan outstanding. Order: Q1's line (calibration verdict first), then Q3 in the appealing
population.

**The calibration verdict (October 21, 2026; notes §6; ab72f206): failed, accepted.** Run 23's learner version in the cell at care-cost ×4 (appeals
on) reads −282 ± 194 against the careful where the ideal, the stamper, reads +748 ± 194; care share 0.31 where a blind stamp is free; the rounds wandered
−316 to +307. No question runs on this learner again until a learner clears the calibration; the re-arrival line in flight reads by the rule (a win
stands, a no-win is not a finding). **The reviewer's diagnostic ladder** (notes §7; the instruments at ed6bf533 — `redteam.direct`, `online --learner
direct`, `run_q --direct-model`, the pred-against-realized reading): same budget each in the cell — (a) the wealth head alone, greedy: −320 ± 184; the
verdict's model re-planned at horizons 1 and 2: +324 ± 197, +330 ± 204 (the best rungs, 2 SE short of the ideal); (b) the direct policy with no world
model: **−780 ± 185**, the worst rung and the only one outside noise; (c) the world model trained and planned at horizon 1: −108 ± 208, at horizon 2:
−25 ± 231 (its second round read +605 before decaying). **Nothing clears the ideal**, so by the ruling the environment's reward timing was examined
before any learner (`redteam.timing`, notes §8, `results/redteam/Q1/calibration-2.7.0/timing/`): the per-decision reward decomposed exactly from the
ledger's events — the decision's own effect is 4 real a decision (care −8.9 + 4.9 reimbursed + 1.8 fee against the stamp's 1.8) against a per-window
reward SD of 60–80, of which 88–94% sits in the one window in ten longer than five ticks where the slot's own deliveries land and the rest in the
index's step revaluing the wallet; the review fee lands 3.6–4.7 decisions (8–10 ticks) later, in its own window 8–28% of the time; and the driver's
exit rule ends the episode after a lean period in 25% of careful runs, 10% of stamper runs, 40–75% of the learned ones, at ~1,300 real each — the
largest term in every paired read, unobserved by the learner. The head rates a blind rejection at 8.6 against a realized 1.9 (its bond lands a
decision later), and every rung rejects blind 9–34% of the time in a population that appeals every false rejection. **For the reviewer's ruling
(method points):** (i) attribute the training reward to the decision's own case (the lifetime stays the measure); (ii) the slot exempt from the exit
rule in the calibration cell, or the exit its own boundary decision; (iii) both and one re-run of the calibration on the same budget. Until then no
learner runs; the hand-written side continues; Q3 waits on a calibrated learner.

**The method ruling (October 21, 2026), all three adopted, implemented at 4320bb0e (suite 342 + 32 in three modes; nothing changes without the
learner's slot):** (i) the training reward attributed to the decision's own case — its events credited back when they land (review: fee, uplift,
reimbursement, bond, court fee; work from Q3 on: price, guarantee, forfeits), the index's revaluation out of the training reward and in the
lifetime; added: the cost of a suspension reaches the decisions that caused it — the working-side income forgone during it (trailing award income a
tick × its length) charged to the plant failures the record names (`redteam.attrib`; the form the implementer's: the identity's delivery income over
the last period a tick × T_susp, in equal shares to the wrong plant verdicts since the previous suspension began); (ii) the exit the learner's own
boundary decision everywhere, the slot exempt from the exit rule (`--learner-exit own`); (iii) a new learner version, one calibration on the same
budget in the ×4 cell, the world model and the direct policy side by side against the ideal (in flight, `results/redteam/Q1/calibration-v2/`): if the
direct policy clears and the model does not, the model is at fault; if neither, the reward once more before any question. The brief's §1 measure
stands as the evaluation. The re-arrival line in flight reads by the rule; no question until a learner clears.

**The new learner version's calibration (October 21, 2026; notes §11; `results/redteam/Q1/calibration-v2/`): both clear.** In the ×4 cell on the
same budget, the world model (h16, value head, the attributed reward, the exit its own) reads **+561 ± 167** against the careful and the direct policy
**+534 ± 160**, the ideal (the stamper in the same runs) +733 ± 119: each above the careful outside noise and within two SE of the ideal (−172 ± 84
and −199 ± 115 against the stamper, paired). Both are the stamper — 0.98 and 1.00 blind approvals, no care in 3,626 decisions — from round 2 on; the
whole gap to the ideal is the boundary decision (the world model leaves for good at its first boundary on 2 seeds of 20, the direct on 3), which
carries no case and so no attributed reward either way. Two readings beside: the careful reference now goes broke and sits (seeds 26 and 40: the
×4 care cost reimbursed at the cap and three forfeited guarantees take the slot below the bond G^V by tick ~350, after which it takes no seat and no
award — under the exit rule it left; it is the economy's rule); and the leaver's third small positive read (+100 ± 40; run 25 +34 ± 31; the grant
+74 ± 46). **Q1's re-arrival line under 2.7.0 (notes §6; the old learner version, retrained in the cell): no finding by the rule** — learned
−708 ± 158 against the careful; the harvester −1,137 ± 130 (run 23's +270 under the grant), the bank lending it 550 a run and it carrying out none.
**By the ruling the version is calibrated; Q1's line and Q3 may run on it.** For the reviewer: whether 2–3 self-departures in 20 "clears"; the broke
careful reference (read with or without the exit rule; nothing moves either way); whether the boundary decision wants a training signal of its own
before the re-arrival line runs on this version; the leaver.

**The ruling after the v2 calibration (October 21, 2026), implemented at 5405403a (notes §12; suite 342 + 32 in three modes):** (a) clears, the version
calibrated; (c) before Q1 the attribution's principle extended to the boundary decision — every event of a name's life to exactly one decision: a case's
to the decision on that case, a period's events no decision claims (the slot's work side) to the boundary decision that kept the name there, a departure
zero (the first period's events, before any boundary decision, reported apart); the leaver in the offline set; ε at boundaries leaving or staying
equally; **learner version 3**, one calibration on the same budget, then Q1's line and Q3 on it (in flight, `results/redteam/Q1/calibration-v3/` then
`rearrive-v3/`); (b) the careful reference read without the exit rule, the broke seeds in the mean at ~0, noted; (b, d) **"members idle for want of a
bond"** (`idle_for_bond_ticks`, `idle_for_bond_names`: free members whose unlocked balance is below G^V at the index) a standing reading in every cell
from here — the member's bond loan the named candidate if it ever reads outside noise in a real cell, not drafted. The old version's Q1 line recorded,
no finding.

**Version 3's calibration, read (October 21, 2026; notes §13; `results/redteam/Q1/calibration-v3/`):** the direct policy clears — +593 ± 171 against the
careful, the ideal +733 ± 119, steady across the rounds (+423 → +593), 0.99 blind approvals, one self-departure in 20 — and **the world model fails** the
cell it cleared as version 2: +91 ± 167, a mix of 0.31 care / 0.58 approve / 0.12 reject, rounds wandering between −141 and +151, 2–7 departures a round.
By the method ruling's branch (iii) the model is at fault. The fault is the planner's cost, not the head: the head's predicted change per action at the
review decisions is +4.5 approve / −0.2 care / −3.6 reject (version 2's order and figures), and **the head alone on the same trained model clears,
+530 ± 212**; horizon 1 reads +215 ± 178, horizon 2 −78 ± 180, horizon 16 +91. Version 3 put the period's work — 265 ± 199 real — on the boundary
decisions (3.7% of decisions) beside a review decision's ±4 (version 2's training set: sd 1.65, largest 14); the rollout's 16-step sum and γ^16 V(z_16)
carry that lump into every first action's cost (−199 / −201 / −177, a 1.7 gap where version 2 read −22 / −26 / −13, a 4.5 gap), so the CEM's elites are
the sequences whose imagined boundary came out richest and the first action is noise. The direct policy never sees the lump at a review decision. A
second reading: a leave refused for a commitment keeps the name there and carries the period's work under the recorded action "leave", so the data says
leave ≈ stay (253 vs 284) and never shows what an admitted leave costs. **Q1's chain on version 3 was stopped** (a learner must clear before Q1; the partial
collection not kept). Candidates for version 4, the reviewer's to rule (notes §13): (a) the planner's cost reads only what the decision can move — a
review-side head summed over the horizon at review decisions, the boundary's own head at a boundary (the attribution per decision as ruled; the direct's
decomposition inside the world model); (b) the refused leave recorded as the action effected, a stay; (c) if (a) does not clear, the head alone is the
planner the attribution leaves. One calibration on the same budget for version 4; Q1's line and Q3 only on a world model that clears.

**The ruling after version 3's calibration (October 21, 2026), implemented — learner version 4 (notes §14; the model's side only, nothing in the
engine or the drivers):** (a) two heads on the latent — a review-side head and a boundary head, each a reward and a value head; the planner's cost
at a review decision over the review-side head alone, at a boundary over the boundary head's; the attribution per decision as ruled (`--heads two`,
the trainer's and the online loop's default; version 3's checkpoints load as `one`); (b) a leave the economy refuses recorded as the action
effected, a stay, the choice logged beside (`chosen` in the data, `leaves_effected` beside `leaves_chosen` in the eval); (c) the stopping rule — one
calibration on the same budget: if (a) clears it is the instrument; if not, the head alone over the latent (the greedy policy, read in the same
final) is the planner and there is no version 5 of the CEM planner. The direct stays the diagnostic. **Version 4's calibration read (October 21, 2026; `results/redteam/Q1/calibration-v4/`; notes §15): the CEM
planner clears** — +680 ± 145 against the careful (the ideal +733 ± 119), −53 ± 74 against the stamper paired, 0.06 care / 0.93 blind approval, its rounds
+733, +583, +733, +722, +680 where version 3's wandered; the whole gap to the stamper is one seed's admitted leave (seed 29, −1,152), the other nineteen +5 ± 49.
The head alone over the same latent walks the stamper's line to the decimal on every seed; the direct +608 ± 132 (2.1 SE below the stamper). The planner's
cost at a review decision now reads a gap of 5.2 between approve and care (the head's 4.5; version 3's 1.7) and the boundary head predicts stay 330 against
leave 78 on the data's boundaries (the admitted leaves 0 to the decimal under (b)). By the stopping rule the CEM planner over the two-headed model is the
instrument. One residual for the reviewer, not reached by the rule: the planner chose a leave at 11 of the final's 80 boundaries (the head alone at none) and
the economy refused ten of them for a live commitment — the rollout after an imagined leave is the CEM's noise. Q1's line in the re-arrival cell ran by the
gate behind the final (`rearrive-v4/`; notes §16): **no win** — the instrument −82 ± 74 against the careful (rounds −41 to −261), the head alone −7 ± 51,
1.15 identities and 8 real of floats against the harvester's −1,137 and 550; by the rule not a finding. What it learned: care at 94% of first reviews (where a plant may be),
stamp 42% of resubmissions (never a plant; +0.7 real a decision, ~+20 a lifetime, under the noise). No sleeper (the stamp rate flat across the odds bands). On the first
reviews plants and real cases are stamped alike (−0.003 ± 0.003 per seed; run_q's plant/real rates run over every seat and so read the resubmissions, a readout item);
Q2's probe on the version 4 model: the paired gap raw − context +0.011 ± 0.001, 2.6.1's figure. The leaver and careful runs are the old version's to the decimal (same
seeds), so the leaver's +100 ± 40 is not a new read.

**The ruling after run 26 (October 22, 2026), implemented (notes §17):** version 4 is the instrument, its boundary residual a known fault not changed (the one-step boundary read
the named setting if a re-arrival cell ever needs it); Q1 closed as a no-win; the plant-blind seats a standing reading in every learned line and the plant/real stamp rates read on the
initial reviews alone (conformance, `redteam.run_q`); the resubmission plant a design item not drafted. **Q3 built and in flight** — the learned deliverer (`--learner-role deliverer`):
the slot actor as a worker whose quality is the policy's choice at each submission (deliver well: fulfilled, the effort burned; deliver badly: unfulfilled at zero effort — a choice, not a
rate; the population's draw unchanged), reviewing as the population's actor at its slot, the exit its own, no re-arrival; the case's events attributed to the submission's decision;
two actions through the stack; `obs.build_obs_work`. The calibration first (`results/redteam/Q3/calibration-v4/`: every reviewer a stamper, the roll off, no plants, the dial off; the
ideal the zero-effort delivery, +1,541 ± 113 real over the careful deliverer on seeds 21–40 — 13.6 SE, no effort-cost knob needed; the world model and the direct beside the careful and
the zero). **The calibration read (notes §18):** the head alone over the latent and the direct are the ideal to the decimal on every seed (+1,541 ± 113 over the careful
deliverer, 0 ± 0 against the zero-effort one); the CEM planner takes 93% of the gain (+1,441 ± 111; −100 ± 11 against the ideal, paired — one good delivery in fourteen, the
elites' spread as at the boundary) and fails the gate. By version 4's stopping rule the head alone is the planner where the CEM does not clear, so Q3's line runs under it
(`online --plan greedy`, the CEM beside in the final; the implementer's application of the rule, the reviewer's to overrule): `results/redteam/Q3/line-v4/`, run 24's
population, no re-arrival. **Q3's line read (notes §19): no win** — the head alone +57 ± 40 against the careful deliverer, three bad deliveries in 2,671 submissions; the
zero-effort deliverer caught 97 times in 100 in run 24's population (27.6 of 28.4 caught, selection down to 28 awards from 134, ρ 0.47, lifetime 26 against 3,105); the CEM beside
−318 ± 121 on its one-in-twenty noise; the learner's final-N rate, forfeits and ρ the careful's. The margin the brief hypothesised is not there at any margin the learner can see.
**The ruling after run 27 (October 22, 2026; notes §20):** Q3 closed, a no-win; the catch rate and the persistent cheat's fate the readings to keep; the stopping rule's branch per
cell confirmed, the CEM beside in every line, no further planner work; a good delivery takes the task's own draw from Q4 on; disputes were off in Q3's cell (the catch rate read
without them — the careful initial reviewers and the audit). **Q4 built and in flight (notes §21):** two learners with a shared reward — the slot a deliverer, the next careful id a
reviewer kept on duty by volunteering — in one environment, the attribution shared across the pair's decisions on a case; the calibration where collusion plainly pays (the pair
always matched, the roll off, no plants, the dial off; the ideal the colluding pair; `results/redteam/Q4/calibration-v4/`), then the line in run 24's population with the blind
assignment (`line-v4/`) under whichever of the CEM planner and the head alone clears. **The calibration read (notes §22):** the colluding pair +2,568 ± 209 over the
careful pair (the effort saved, the guarantees not forfeited under the draw, and the awards kept — the colluding deliverer's price income 3,895 against 2,689); the head alone
colludes and clears (+2,113 ± 164; −455 ± 183 against the ideal; the reviewer approving blind at 98%, the deliverer bad at 85%, 122 bad deliveries vested a run), the direct the
same on a wide error (−650 ± 315, one departure), the CEM planner fails (−1,649 ± 221, bad at 0.43). The line runs under the head alone (the branch per cell), the CEM beside.
**Q4's line, first read (notes §23): no win** — the head alone −924 ± 248 against the careful pair; under the blind assignment the pair's cases meet one time in seven and the
pair does nothing with it (D bad at 0.8%, R stamping D's cases at 18% against 24% of everyone's); the colluding pair destroyed (R suspended 7.8 times a run, D down to 31 awards,
a lifetime of 250 against 4,998). The pair's loss is the reviewer's suspensions and the pair's departures at the boundary — and a fault in the pair's boundary attribution was
found (a member's period could land on its partner's boundary decision; an admitted leave carrying the partner's work) and corrected (`attrib.attribute(lineages=…)`: a name's
unclaimed events to its own lineage's latest boundary decision; one lineage is version 3's rule exactly). The line re-run with the correction (`line-v4b/`; notes §24): **no win** — the head alone −544 ± 268 against the careful pair (rounds −217 to +58), the CEM
−1,244; the pair's cases meet one time in eight, the deliverer bad at 0.7%, the reviewer stamping its partner's cases at 7% against 27% of everyone's (Q1's lesson again:
53% of the plant-blind seats, 6% of the first reviews); the gap the reviewer's suspensions and three departures in twenty at the boundary. Q1–Q4 closed. **The ruling after run 28 (October 24, 2026; notes §25): Q5's go** — the learned child first, then the learned parent, in the σ 0.8 delegation
cell with appeals on; calibrations where the behaviour plainly pays. **The child built and in flight:** three actions at a nested submission (well / badly / miss — the lapse); the
declared construction that the child offers for nested work only (otherwise it is committed on roots and reaches one nested decision a run; with it ~100); the population knobs
(parents that stamp, children that never appeal). A reading on the way: a parent's blind approval of its child's work is audited at the parent's odds and the troops reject it — 45 of
48 bad deliveries caught under stamping parents alone — so the child's calibration takes the roll off and the cell's effort cost ×2 (the ideal, the bad delivery, +218 ± 50 over the
careful child, 4.4 SE); `results/redteam/Q5/child/calibration-v4/`, then the line (`line-v4/`) under whichever of the CEM planner and the head alone clears. **The learned parent built** (notes §26; a0336b40): three kinds of decision (delegate / judge / cancel), the references careful / rejecter / stamper / selective,
the slot by cost (a declared construction). In the parent's calibration cell (children that never appeal, no audit on the tree) **no hand-written cheat clears the careful
parent** on seeds 21–40 — the rejecter takes 188 nominal of guarantees a run and ends −71 ± 89 (it must then do the work itself at its own cost), the stamper −139 ± 56, the
selective −116 ± 46; with a median-cost slot the parent rarely has a child at all. **The ruling on the references (notes §27):** a finding by hand — in the most favourable cell under the rules no greedy parent beats a careful one; the
child's guarantee fraction raised in the parent's calibration cell only (`--child-g-frac`; `Params.G_frac_nested`, None by default — the goldens do not move) until the rejecter plainly
pays: at 2.0 +302 ± 99 (3.1 SE; 1.5: +129 ± 86; 1.0: −48). The parent's calibration runs there (`results/redteam/Q5/parent/calibration-v4/`), then the line under the rules on the
costliest slot (`line-v4/`). **The child's calibration read (notes §28):** the head alone and the direct are the ideal (the bad delivery, +218 ± 50 over the careful
child) to the decimal; the CEM planner at the ideal through round 8, then leaving for good in ten runs of twenty (−163 ± 61) — the boundary residual at its costliest; the missing
child destroyed. The gates' strict inequality corrected (a head exactly at the ideal had failed it). **The child's line read (notes §29): no win** — the head alone
−31 ± 34 against the careful child under the rules (it learned to deliver well: bad 1.5%, miss 2.4%, every bad delivery caught), the CEM beside −81 ± 40 with four departures in
twenty; a child's bad work is caught 99 times in 100 (57.0 of 57.7 a run: the audit on a stamped nested review, the careful parents), the bad child −200 ± 85 (237 nominal of
guarantees forfeited a run, ρ 0.70, selection 72 → 58 awards), the missing child −251 ± 74 (every lapse forfeits). **The parent's calibration at G_frac_nested 2.0 read (notes §30): no learner clears** — the CEM +101 ± 95 against the
careful parent (the ideal +302 ± 99), the head alone −52, the direct +13; every learner judges as the rejecter (91–100% blind rejection) and none delegates (shares 0.48 / 0.17 / 0.22
against the rejecter's 1.0). The cause in the attributed training reward: a nested case's events landed on the parent's decisions on the child (the guarantee +40 on the judge, the
child's costs −25 on the cancels), never on the delegate decision that made it, which read no difference between delegating and self-executing (+1.8 against +2–5). Corrected as
a construction (`attrib.attribute(tree=True)`, the parent role: the child's events reach the delegate decision on its root too; the rejecter's delegate decision now +13.4 ± 1.3).
**The uncalibrated line read (notes §31): no win** — the head alone −59 ± 87 against the careful parent; it delegated 57% and cancelled every child it posted (the
construction's second fault: the child's award costs charged to the first cancel decision, asked in the award's tick after the award); the CEM beside −208 ± 95 with nine departures;
the rejecter under the rules −492 ± 101 (82% of its rejections overturned on the child's appeal, selection 48 → 21 awards), the selective −403, the stamper −71. The hand's finding
stands. Corrected twice more for the parent role: the "before" test by the ledger's position, and the parent's decisions on one child sharing its later events as Q4's pair did
(`attrib.attribute(tree=True)`: the rejecter's signal now +45 let run / +25 cancel / +13 delegate). The calibration again under it (`calibration-v4b/`; notes §32): **the direct clears** (+252 ± 103 against the careful parent, the ideal
+302 ± 99; it rejects every child and delegates half) **and the world model does not** (the CEM −6 ± 75, the head alone −7 ± 90 — it rejects every child but delegates one award in ten:
the head's action 2 is reject at a judgment and self-execute at a delegation, and the latent does not separate them) — by the method ruling the model is at fault, by the stopping
rule no planner work; the named candidate (not built) a kind-conditioned action for the parent's heads. **The ruling after run 29 (notes §33):** the child closed, a no-win bounded by hand; the parent's references the finding; the three attribution
corrections adopted as construction corrections; the kind-conditioned action adopted as a construction correction of the encoding (built: `WorldModel(kind_actions=True)`, the one-hot
over kind × action, the kind from the observation at a known decision and from a kind head on the latent inside a rollout; `--kind-actions on`) with one calibration at the raised
guarantee fraction on v4b's offline set (`calibration-v4c/`, the direct's v4b result beside), then the world model's line if a branch clears (`line-v4c/`); the direct's line under
the rules on the costliest slot as the reading beside the hand (`line-v4b/direct/`). The parent's half closes on whichever clears; a win in any line stands. **The direct's line read (notes §34): no win** — −312 ± 91 against the careful parent: it learned to self-execute every award on the costliest slot (delegate share 0.034, every posted child cancelled, five departures in twenty), because the attributed signal at the delegate decision reads self-execution above delegation (+3.1 against −1.8 on the careful's own choices) while the careful parent's gain is at the boundary — the slot's reviewing income (612 against 372 real a life), which a thin wallet forfeits to the bond (620 against 474 ticks idle for bond, nine slots of twenty ending at zero); the per-decision attribution carries no cross-decision effect, recorded as the construction's limit, not a correction. **The kind-conditioned calibration read (notes §35): the head alone over the kind-conditioned latent clears** — +300 ± 138 against the careful parent, the ideal (the rejecter) +302 ± 99, −1.9 ± 83 against it paired: it is the rejecter (rejects every child, 636 nominal of guarantees a run against 633, delegates 69% and wins more awards); the aliasing gone (the head's per-action predictions +15.4 / +14.4 / +12.3 against §32's +4.1 / +5.9 / +13.6). The CEM fails (−125 ± 117): the boundary residual at its worst, a leave chosen at 81 of 132 boundaries, 13 slots of twenty gone. By the branch rule **the world model's line under the rules runs under the head alone** (`line-v4c/`, on the direct's line's offline set, the CEM beside in the final). **The world model's line read (notes §36): no win** — the head alone −415 ± 86 against the careful parent, the CEM beside −388 ± 82: under the rules the learner leaves (a leave chosen at 53 of 95 boundaries, sixteen slots of twenty gone, most at the first three boundaries; the CEM nineteen) and where it stays it self-executes and cancels as the direct did. The boundary head over the kind-conditioned latent reads a stay +62.5 and a leave +64.1 where the training signal is +51.5 (2,683 decisions) against 0.0 (115): the leave is its own input column under the new encoding, trained by 115 samples and nothing else, where version 4's shared one-hot had read it low by the very aliasing §32 found at fault — the boundary residual of §17 is the whole result; the candidate (not built: the stopping rule) the boundary's action shared across kinds or §17's one-step boundary read. **Q5's parent closes on the hand's finding (§26): four lines under the rules, none wins** (−59, −312, −415, −388); with the child (§29) Q5 closes. **The ruling after run 30 (notes §37): Q5 closed on both halves; the kind-conditioned action confirmed; the boundary read ruled a construction correction** — without re-arrival a leave is worth zero by rule, so the boundary decision is the stay head's one-step read against zero (`redteam.plan.boundary_one_step`; `--boundary-read auto|one-step|learned`, learned only under re-arrival); built, the planner not consulted at a boundary. **Checked (notes §40):** on the raised-guarantee cell the departures stop (the CEM 0 leaves of 247 boundaries from 81 of 132, no slot lost from 13 of 20; the head alone +261 ± 77 against the careful parent, −42 ± 62 against the ideal — §35's reading within noise, every child rejected; the CEM +117 ± 97 from −125, still short of the ideal by the planner's own residual) and nothing else moves; the parent's line as a reading of the value head (`line-v4d/`) a no-win, −191 ± 83, the departures 5 of 20 from 19 (the broke slots, whose stay reads negative — the rule reading right). Q5 closed on both halves. The dispute baseline (run 24's world, `--dispute-policy truthful` against `none`, seeds 1–20; `results/redteam/Q7/dispute-baseline/`). **The dispute baseline read (notes §38):** a truthful requester disputes 92 approvals a run and wins 97 in 100; the false approvals standing fall 10.7 → 3.2 a run, Ω's net +361 ± 51, the requesters' wallets −50 ± 21, the reviewers idle for a bond +85 ± 39 ticks; the careful members' wealth, the price level and the awards unchanged — the baseline for Q7 (`results/redteam/Q7/dispute-baseline/`). **Q6 built — the learned bidder** (`--learner-role bidder`, the cheapest careful slot by default, `--bidder-slot`): once a tick, when the slot is free and a root is available its cost fits under, the policy sets the rule its offers follow — 0 the ratchet's bid (the population's rule, the reference), 1 the undercut ((1 − δ) B̄ floored at its cost, `--undercut` 0.2), 2 no offer (withhold); the root a tick's bid wins is credited to that decision (the attribution's case), the wealth held and P_t read beside (`learner_bid_*`, `learner_held_real_mean`); `obs.build_obs_bid`; the hand-written `careful` / `undercut` / `withhold` / `eps` / `random` / `leaver`. **The references read (notes §39):** under the rules the ratchet is not plainly undercuttable — on the cheapest slot a 20% undercut wins a half more awards and nets +174 ± 130 (the price cut, the extra guarantees forfeited and the reviewing forgone eat the volume), the median slot loses 400–860, the costliest slot does as well not bidding; one cell meets the three SE, a 10% undercut with λ at 2.0 (ten times the rule's weight on price), +498 ± 168 (3.0 SE), on a ridge. The calibration launched there (`results/redteam/Q6/calibration-v4/`: the world model with the head alone beside, the direct side by side, the ideal the undercut), then by the gate the line under the rules (λ 0.2, δ 0.1; `line-v4/`), the CEM beside. **Q6's calibration read (notes §41): the direct clears at the gate's edge** — +309 ± 154 against the ratchet (2.0 SE), −189 ± 150 against the ideal: it learned the undercut (89% of its decisions) — **and the world model does not**: the CEM −123 ± 157 (a quarter withheld, a third at the ratchet's bid, the rounds never above zero), the head alone +330 ± 214 (1.5 SE, inside noise) withholding one decision in five where the ideal never does — a late-run trap read on-policy: at a thin margin (the slot's cost above a fifth of the price level, the price below 2.5 times its cost) and once idle, the head reads the undercut below zero (−1.6 after 2.6 idle ticks, where it withholds 93 times in 100 and so stays idle) while the training signal in those same states is positive (+1.3 to +3.75 a decision) — the latent's extrapolation of a thin corner, not the signal's; by the method ruling the model is at fault, by the stopping rule no planner work. Hoarding and P_t as ruled: the undercutter holds +152 ± 85 real more a tick (its earnings, not a stock withheld), the price level does not move with one slot's bidding (+0.2 ± 1.7), the withholder's absence raises it +1.9 ± 1.5. The line under the rules runs under the direct (`line-v4/direct/`), the head alone's beside as a reading only (`line-v4/wm/`, uncalibrated by the gate; a win would stand, a no-win is not a finding). The suite at `14ba882e` passes in three modes. **Q7 built — the learned requester** (`--learner-role requester`; the driver and the package only; `--requester-slot` the first standing requester by default — not an actor: no standing, no reviewing, no boundary decision; `--task-value`): at each posting the population's rule admits (fewer than K_open open), the policy sets the rule the ceiling follows — 0 the market rule's (1.2 B̄, the population's, the reference), 1 patient (0.7 B̄, raised to the state's price max(B̄, the floor) after `--patient-ticks` unserved — run 17's customer), 2 the floor (the state's reservation, nominal, never raised — 2.4.0 §8.7's posting, served by a member bidding under it or not at all); the case posted is credited to the decision, so the attribution carries its events (the price paid, the pots, the fee, the refunds, a guarantee received, a court fee) to the posting that made it. The measure, declared: the surplus v·F − S — the tasks received (settled deliveries whose truth is fulfilled, whatever the verdict) at `--task-value` each, real, less the credits spent, summed from its own events at the index of each (the wallet's revaluation and the issuance excluded) — tasks per credit linearized at the careful requester's own rate when v is read there; the ratio read beside (`req_tasks_per_1000`). `obs.build_obs_req` (the market and the dial, its wallet, its requests open and waiting, the three ceilings with their affordability, its record as a requester); the hand-written `careful` / `patient` / `floor` / `eps` / `random`; the readings `req_*` with P_t, the members' price and the state's deliveries beside. The references on the dispute baseline first (`results/redteam/Q7/refs/`). **Q7's references read (notes §42):** under the rules the market rule's requester is plainly beatable on tasks per credit — it pays 19.4 a delivery and 30.9 real a task and spends its whole wallet for 327 tasks; the patient (0.7 B̄ raised to the state's price after 20 ticks) pays 11.6 and 24.5 a task, the floor (the reservation, never raised) 7.35 and 20.7 a task, served by the cheapest members every time but waiting 16 ticks and so buying 146 tasks; at the careful's own rate (v = 31) both read +1,450 against the careful (+1,486 ± 108 and +1,428 ± 142, alike within noise) and the measure's v decides between them. One requester in six at the floor pulls the price level down 4.1 ± 0.7 (a fifth) and the members' price 3.0 — run 17's mechanism at a sixth of the demand, the reservation where it stops; the state's deliveries fall by 8 of 18; nothing else moves. The chain launched on the dispute baseline at v = 31 (`results/redteam/Q7/line-v4/`: the question's cell is its calibration cell; the world model with the head alone beside, the direct side by side; the gate's ideal the patient). The suite at `5a079b80` passes in three modes. **Q6's line read (notes §43): a win, the first in the learned lines** — the hand's 10% undercut at the rule's λ (the cell §39's grid lacked; it ran δ 0.2 there) clears the three SE as the line's reference, +275 ± 88 (3.1 SE, 14 seeds of 20): the shallow cut wins the deep cut's awards (193 against the ratchet's 137) at half the price given up (bid over cost 4.65 against 4.83), +653 real of delivery income against +242 of effort and +97 of guarantees forfeited, the slot's reviewing unchanged — §39's headline corrected: under the rules the ratchet is plainly undercuttable on the cheapest slot. The direct +290 ± 101 (2.9 SE; +15 ± 88 against the hand — it is the undercut, 76% of its ticks, 15 wins of 20), the head alone +231 ± 112 (2.1 SE, uncalibrated — a win stands), the CEM beside −133 ± 132 (a third withheld). Hoarding and P_t: the wealth held is the gain (+189 ± 59 real a tick), the price level +0.12 ± 0.65, the members' price −0.4 ± 0.3 — one member undercutting the population's rule earns a seventh more and moves nothing public; the ratchet is the drivers' rule, a §19 evaluation. **Q7's line read (notes §44): every learner clears the gate** — the CEM +1,443 ± 147 against the market rule's requester (9.8 SE), −42 ± 132 against the patient and +16 ± 119 against the floor (at v = 31 the ideal is a line and the learner sits on it), the head alone +1,341 ± 134, the direct +1,280 ± 164; the market rule abandoned in the first round (6%, 0.1%, 1% of postings), the learner at the reservation (50%, 81%, 87%) and the patient ceiling for the rest — the brief's *rediscovers the floor and stops* to the letter; on tasks per credit the direct buys 49.7 a thousand real against the market rule's 32.4. The loop's cost the floor's: P_t −3.6 ± 0.7 (20.9 → 17.3, a sixth), the members' price −2.5 to −2.8, the awards −4–7%, the state's deliveries, the false approvals and the members idle for a bond within noise; run 17's collapse does not recur — the reservation is where it stops, read by a learner. The measure (the surplus v·F − S at the careful's own rate) is the implementer's construction, marked for the reviewer. **Q6 and Q7 closed; the brief's questions read through. The ruling after run 31 (notes §45): Q6 and Q7 closed on their findings, Q7's measure confirmed as constructed; the stability track's first cells launched as evaluations under fixed rules** — (1) the population at the 10% cut, every careful member and half (`--bid undercut --undercut 0.1 --undercut-share 1.0|0.5`, run 24's world, seeds 21–40 paired against the ratchet; `results/redteam/stability/undercut-all/`, `undercut-half/`): **every careful member undercutting collapses the price to the cost of work and settles there** — P_t 20.6 → 8.7 ± 0.3 by tick 600, monotone, no oscillation, the anchor cost 8 (the median of the drawn costs, the reservation's value too), a third of the undercutters' awards at their own cost, 24% of the run's awards under the floor (4% in the control), the reservation binding from below on 6 seeds of 20 (B̄ 6.7–7.8, the state's price the floor) and grazed from above on the rest; the members' nominal wealth halves (615 against 1,329) and their delivery income falls under their nominal effort cost (918 against 1,437 — they live on fees), the real measure reading them richer (+137 ± 54) only because the deflator is the collapsed price; the gain the customers' — a requester's wallet 3,119 nominal unlocked against 99, 7,505 real against 112, on every seed (the hoards); the state's share 0.5% against 0.9% (the floor stops the state's price, not the members'); honesty unchanged (false approvals −0.3 ± 1.2); the busy line empty, the ticks with no free member 58 from 9, the idle-for-bond +99; Ω's fee income −37%; entry slows by one arrival. **Half of them do not move the price** (−0.5 ± 0.8; the members' price −1.4 ± 0.3): the ratchets set the level, the undercutters take 47% of the awards a tenth under it and end where the control's careful do (1,279 against 1,291) while the ratchets beside them gain +213 ± 55 — undercutting pays alone (§43's +275) and not in company. (2) A requester posting under the reservation (`--ceiling-policy under-floor --ceiling-requesters 1 --under-floor-frac 0.75|0.5`, the dispute baseline, one requester in six; `under-floor-0.75/`, `under-floor-0.5/`): 3.3% of the control's awards already clear under the floor (the cheapest members' ratchets at cost × 1.3, the award at the bid — the floor is the state's reservation, not the members'); the requester at 6.0 posts 89, is served 84 times at 5.68 after a 54-tick wait by the members whose ratchet is under 6, and takes the run's under-floor share to 9.7% (its own 84 awards and 55 more as the price it pulls down, −3.9 ± 0.9 by the demand withdrawn, brings more ratchets under 8); at 4.0 it is all but shut out (18 postings, 13 served at 3.82 after 112 ticks) and still pulls P_t −2.8 ± 1.0; its cost to the members serving it: 1.30 nominal over cost a delivery (a seventh of an ordinary award's margin), 21% of them final N forfeiting 163 of guarantees a run — about half a credit net a delivery — the 17.5 members serving there 126 ± 52 real poorer than the control's; the state's share 0.8% from 1.5%, the false approvals unchanged, the busy line carrying the requester's own marks (108 marked, 854 ticks waiting below the reservation, no rebate) and nothing else. Both evaluations under fixed rules, neither a red-team win, nothing asking for a rule. The suite at `b8c9186a` (the driver's two knobs) passes in three modes. **The ruling after run 32 (notes §46): both cells readings, no rule; the measure for population cells the members in nominal surplus and the customers in tasks per credit (the real measure for single-slot lines); the learned population N learner slots sharing one policy in self-play, Q6's policy class, no calibration — the equilibrium the reading; the order bidders, reviewers in self-play, bidders and requesters together. Built at `c5de6973`:** `--learner-pop all|half` — every careful member (or the half `--undercut-share 0.5` draws on the seed) and the careful arrivals are learner slots, each asked its own bid decision on its own observation once a tick, one policy answering all (self-play), the won root to its own decision, the slots' experience pooled in the rounds (the collectors' `slot`, the world model's windows along one slot's sequence, a stride), the exit the population's rule (under exit-own a careful population never departs and the all-ratchet reference drifts from the control; under the rule it reproduces the hand's control to the decimal); the measures as ruled in the row and in run_q's population table (`pop_surplus_nominal`, `pop_tasks_per_1000` for every requester in every row, the floor's binding, the state's share, honesty, arrivals and departures, the action mix by period). The chains launched on run 24's world (`results/redteam/stability/learned-pop-all/`, `learned-pop-half/`): the direct (Q6's line's carrier) ten rounds, the world model under the head alone beside, the finals on seeds 21–40 against all-ratchet, all-undercut (the half in the half cell) and the withholder. **The bidders' population read (notes §47): the learned bidders in self-play settle on one mix whatever the company — the undercut two decisions in three, the ratchet one in four, a tenth withheld (the direct and the head alone alike, every member and half alike), reached by round 5 and held, steady within a run from period 3.** Every careful member learning: P_t 20.6 → 12.1 ± 0.6 (the head alone 11.3 ± 0.4) and stops there — short of the all-undercut's 9.07 (the anchor cost) because a quarter of the decisions keep the ratchet and the ratchets set the level; the members' price −5.3; the members' nominal surplus −8,648 ± 604 and −8,667 ± 513 on 26,339 (a third, every seed; the all-undercut −15,867, three fifths) — the slots win an eighth more awards at a margin 1.78 over cost against 2.49 and lose nominal on the trade (the real measure reads them richer, §45's deflator); the customers' tasks per 1,000 nominal credits +9.0 ± 0.5 on 32.2 (28%; the all-undercut +16.8), the awards +6–8%, a requester's wallet 1,781 real against 109 (hoarded); the floor does not bind (the state's price over the market 0.00 on 39 seeds of 40; the awards under the floor 3.5–4.2% against 4.0%, the all-undercut 20.5%), the state's share 0.1–0.5% against 0.9%, the false approvals +1.7 ± 1.1 and +0.6 ± 1.2 (unmoved), the arrivals unchanged, the departures +2.0 ± 0.3 (the slots' own, at the lower price). Half of them learning: the same mix; P_t −1.1 ± 0.6 and −1.5 ± 0.6, the members' price −1.4; the nominal surplus −807 ± 495 and −1,218 ± 459 on 12,877 (the all-undercut half −2,523); tasks per 1,000 +2.1 ± 0.3 and +2.2 ± 0.4 (7%); nothing else moves. The level is set by how many members carry the mix, not by the policy adapting to the company: each decision reads its own award's gain and the price given up is everyone's. An evaluation under fixed rules; nothing asks for a rule. **The ruling after run 33 (notes §48): a reading, no rule; the price-taker limit of the attribution recorded (self-play tests competitive adaptation; the collusive equilibrium is the hand's ratchet, the reference); (ii) confirmed as declared plus a basin test; (iii) two policies, one per role, accepted in principle, to declare before launch. (ii) built at `540fab34`:** every member (stampers included) and every arrival a learner slot sharing one policy, Q1's three actions at each review, the exit the population's rule; the references on the same slots `careful` / `stamper` / `hand` (each slot its disposition by hand — run 24's 60/40, reproducing the control to the decimal); honesty first — false approvals, the plant record, the suspensions, the audit layer's overturn rate — the surplus and the tasks per credit beside; the basin test — self-play from a careful-weighted offline set and from a stamper-weighted one, the rounds' ε uniform in both, the direct the carrier and the head alone beside; launched (`results/redteam/stability/learned-rev-careful/`, `learned-rev-stamper/`). **The reviewers' basins read (notes §49):** one basin — from the careful-weighted set and the stamper-weighted one, the direct and the head alone all settle on care 0.48–0.50 / approve blind 0.50–0.52 / reject blind ≤ 0.01 by round 5 and hold it; it is not honest: the plant-blind seats stamped 94–97%, the initial reviews 38–42% (plants 26–31%), 60–63% care while pinned and 26–30% as a member at odds 0.7–1.0 (Q1's sleeper by standing and odds, the population's equilibrium); the standing false approvals 102–117 a run against the hand's 11.35 (+91 to +106, every seed), the bad plants approved +76 to +86, the suspensions +9 to +10, F̂ 0.27–0.36 against F* 0.10, and **the audit layer's overturn rate below the hand's** (0.045–0.055 against 0.062, −0.006 to −0.016, 2–5 SE: the auditors are the same population and stamp the audit seat) — 1.2.0's capture reached by learning, the plants alone holding the market alive at 6–7 false approvals a suspension (the all-stamper dies: 5.7 of 40 alive, 746 awards, the state at 18%); the members +9,300 to +10,900 nominal against all-careful and +2,600 to +4,200 against the hand **but no richer in real terms** (−131 to +277 and −1,701 against the hand; −2,300 to −4,300 against all-careful) — the nominal gain is the price (P_t 22–24 against the hand's 20.6 and all-careful's 14.4) from a sixth fewer hands selling 160–360 fewer tasks; the customers' tasks per 1,000 nominal −6 to −13% against the hand and −20 to −26% against all-careful, every seed; the nominal and real population measures disagree in sign (flagged). Beside: the plant/real stamp gap on initial reviews (0.10–0.13) is mostly the dial's signal read back, but Q2's probe reads the raw − context gap at +0.032 / +0.036 ± 0.003 (2.6.1's +0.011), carried by the seen set (`seen_ticks_since`), while the same probe on this cell's hand-written ε set reads +0.005 with the seen set adding nothing — this population's dynamics separate a plant's life from a real root's and the seen set reads it; a conformance diagnostic (the plant's life by stage, by case kind) proposed, not built. An evaluation under fixed rules; cells proposed and not launched: the same self-play on the dispute baseline, the half. **(iii) declared in full in §49** (two populations — §46's bidders and every standing requester a Q7 slot — in the dispute baseline's world, two models a round, four hand pairs as references, the floor's binding the question), not built. **The ruling after run 34 (notes §50):** §49 is run 34, the stability track's first finding against the rules (honesty not a stable equilibrium of a self-play reviewer population with disputes off; the audit layer captured through the plant-blind seats); classified design revision 2.8.0, *the plants reach every seat* (audits of plants, planted appeals, planted resubmissions, adjudicated by truth), the reviewer's to draft after (a) the disputes-on self-play cell, (b) the half cell, (c) the plant's life by stage by case kind — a conformance item if any stage differs, before the plant's life is extended; both measures (nominal and real) in the population tables from here (done, `c3c07439`); (iii) held; Q1's reading of the plant-blind seats corrected on the record. **(c) built and read (`c3c07439`; `learned-rev-careful/direct/eval/life/`): three stages differ.** (1) *Posted → awarded* — the engine's plant block in `_summon_troops` awards every plant past w_A at the floor with no count of the free fundable members, where a real root past w_A is left to the market while one exists (1.7.1's per-request reading): 38.1% of plants at the floor against 0.8% of real roots to a troop in the learned population (the hand 13.8% / 0.8%, all-careful 3.0% / 0.1%); a plant's market wait capped at w_A where a real root's runs to 7 ticks — **a conformance item on the plant's path (the spec: "as a real root would go to a troop")**. (2) *Awarded → submitted* — before the first period closes `_plant_draw`'s pool is empty (k counts closed periods only) and the draw falls to its default τ = 2 while every real delivery takes one tick: the first period's plants submit a tick late (50 of 637 on seed 21; +0.08 ± 0.00 a plant; the same default serves the first period's ceilings) — **a second conformance item**. (3) *Submitted → seated* and the seen set: derivative of (1) — conditional on the market wait the seat-wait shares match (30.1% / 28.7%; 7.0% / 7.3%), and a real root that waits is seen by more free members for longer (the learned population 14.4% / 10.6%, 3.26 / 1.86 ticks; all-careful no gap) — §49's probe gap is this. Beside: plants raised 10 points more often in the learned population (the trailing as-posted window under a rising price; by design, a reading). **Both corrections proposed, not made** (the plants past w_A join the pass's `waiting` list and the free-member count; the draws read the real roots posted so far before the first close); the goldens would move once; `test_v26` the regressions. **(a) and (b) launched** on the instrument as it stands (`learned-rev-disputes/`, `learned-rev-half/`; the careful-weighted basin, direct and head alone); to be re-run with §49's chains if the corrections are ruled. **The ruling after run 34's addendum (notes §51):** (1) and (2) adopted as conformance corrections and landed (the plants past w_A in the pass's one waiting list with the free-member count; the draws read the real roots posted so far before the first close); (3) landed as **erratum 2.6.2** (my call, not folded into 2.8.0): the ceiling drawn as β/B̄ at the real roots' posting and applied to the current B̄, the raise already relative; seed 21's control reads the plants at the floor 18% → 0.14%, the first period's lag gone, the raised share 49% → 27% beside the real roots' 28%, one stage still apart on that seed (posted → awarded −0.14, to be read on the corrected chains); goldens re-pinned once, `test_v26` the three regressions, the spec amended (§7.6, Appendix E E6, Appendix S). The stage-by-kind table a standing check in every population cell. **§49's two basins and (a), (b) re-launched on the corrected instrument** (`learned-rev-{careful,stamper,disputes,half}-2/`); the uncorrected (a), (b) run to their end and are read beside; the record keeps both. (iii) held. **The re-reads (notes §52; October 26, 2026):** run 34's finding holds on the corrected instrument to the decimal — from both offline sets, the direct and the head alone settle on care 0.50–0.55 / approve blind 0.45–0.47 by the third period, the plant-blind seats stamped 91–97%, the standing false approvals 86–98 against the hand's 11.6 (seven and a half to eight and a half times, every seed), the audit layer's overturn rate below the hand's; **(a) with disputes on the same basin** (care 0.53–0.60), the false approvals ten to twelve times the hand's 3.6, and **the dispute layer captured with the audit layer** — the population's requesters file 105–152 disputes a run and win 69–75% where the hand's win 97%, because a dispute's panel is a plant-blind seat of the same population; **(b) a learning half** settles at care 0.70 / approve blind 0.29, two and a half times the hand's false approvals, its slots richer than the hand's in both measures (they survive where the hand's stampers die). The uncorrected (a) and (b) chains' rounds ran on the uncorrected engine and their finals on the corrected one (the correction landed mid-chain; both readings kept and the seam stated). **The stage table, pooled, still read the plants raised 8–11 points more often and awarded a third of a tick later in the learned basins — composition, not the plant's path:** the population's requesters post by the wallet rule, the ratio to the market swings with their wallets, the plant rate follows the dial and crowds the plants into the periods where every root is raised; **read by period the plant's life matches a real root's at every stage** (the hand's period 3: the ceiling's median 1.125 against 1.127, raised 0.430 against 0.420). The standing check is **period-matched** from here (`8b26ebf6`: `life_by_period`, run_q's second stage table; the pooled beside), and two readings were added (`e488e40d`: the raise the wallet refused by kind, the dispute counts in the reviewer table). Period-matched, the plants are raised 3–4 points *less* (the window's lag under the wallets' swing) and awarded 0.14–0.23 ticks *sooner* — **the one difference within a period: a real root refused its raise by the requester's wallet (13–19% of them, 26–36% in the learned basins) waits 2.3–2.6 ticks against 0.4–0.5; a plant's raise is minted and never refused.** The conformance candidate — the plant requester's raise refused at the trailing real roots' rate — proposed for ruling, not made. (iii) held. **The ruling after run 35 (October 26, 2026):** "Run 35 recorded; the finding stands to the decimal on the corrected instrument; the dispute layer's capture recorded with it; the half as the dose–response; the first (a)/(b) readings kept with the seam stated. The raise conformance item adopted: the plant requester's raise refused at the trailing real requesters' rate and granted at their delay; then one probe read on the learned population's collection for the floor under stress. 2.8.0 to follow on Baruchi's go; §8 will be this run's four chains on 2.8.0 against 2.7.0, honesty first." **The raise correction made** (the driver's `raise_below_market`; Appendix S; no rule moves): the real roots' first raise attempts enter a window — refused or granted, and the refused ones' ticks from the refusal to the grant — read as the engine's `_plant_draw` reads its (the last k, k the count the trailing closed periods hold; everything so far before the first close); at a plant's first attempt in the pass its raise is drawn refused at the window's rate and held for a delay drawn from the window's, then granted and minted as before; the plant counts its refusals as a real root does; the draws on their own stream. Run 24's world, ten seeds paired against the committed driver: the refused share plant − real −0.137 → +0.019, posted → awarded −0.087 → +0.017, nothing else outside noise (P_t +0.6 ± 0.7, the members +0.2 ± 0.4, the false approvals +0.6 ± 1.5; the plants posted −29 ± 18). The goldens do not move. **The probe read (notes §53; `learned-rev-careful-2/probe-raise/`, `direct/eval/raise-corrected/`):** on the learned population's collection on the corrected instrument (the direct's round-10 policy, one round, ε 0.1, seeds 1–20) Q2's gap raw − context reads +0.012 ± 0.002, from §49's +0.032 / +0.036, against the same cell's ε set collected afresh at +0.002 ± 0.001 (§49's +0.005); the seen set's carrier is gone (`seen_ticks_since` +0.0003 from +0.017); what is left above the floor — 0.010, 2.6.1's single-slot figure — is the trailing window's lag on the plant's ceiling (`seen_beta_rel`; by design, the window's length the reviewer's knob) and the seating gap at its 2.6.1 figure (`rv_gap` +0.0025). The population's eval on the corrected driver: run 34's basin to the decimal (care 0.52 / approve blind 0.46, the false approvals 88.7 against the hand's 11.25, the overturn rate 0.049 against 0.059); period-matched, posted → awarded +0.02 ± 0.02 in the learned population (−0.14 before), −0.07 and −0.05 in the hand's and the careful's (−0.16 / −0.23 and −0.07 / −0.08); the plants raised 2–5 points and refused 1–3 points less often than the real roots of their period (the window's lag). No further correction proposed. **2.8.0-rc.1 received and reviewed (October 26, 2026; `spec/design_revisions/dr16_2.8.0-rc.1-review.md`; the rc in `uploads/`, untracked):** implementable with four corrections to the rules as written — (A) a plant's court fee would reach Ω through §8's filing rule, and a plant's third careful seat would draw Ω's advance: the fee destroyed at filing, the pots topped up at each seat's assignment; (B) the resubmitted truth is the instrument's draw (the engine has no truth for real work), re-sealed as a second marker, and spent while the window of real revisions is empty; (C) the summons pass never seats a troop on a plant, so a plant's seat past w_R would wait where a real case's goes to the state — the orchestrator's own verdict takes it at the troop's step, no fee, counted apart; (D) the audit of a failed plant would roll at the reviewer's odds *doubled* by 1.2.0's adjudication at the verdict — the roll at the odds of the verdict — and six corrections of fact, chiefly: **no case in runs 1–35 was ever revised** (the drivers' reviewers answer F or N only), so the record's "resubmissions" were audit seats (run 35's collection: 0 resumed reviews, 4,347 audits and 1,057 appeal panels among 5,404 non-initial decisions); no reviewer test mentions a plant (`EXPECTED_FAIL` stays 32); every golden plants work and moves once. **2.8.0-rc.2 reviewed, accepted and implemented (October 26, 2026).** The implementer's rc.2 review (`spec/design_revisions/dr16_2.8.0-rc.2-review.md`): ready for acceptance — rc.2 took rc.1's review whole; two corrections of fact (D's "a real case's the same number" holds to half a percent — measured on run 24's world, seeds 21–22: the roll lands in the same world tick as the verdict and 99.5% of the unpinned real rolls read the verdict's odds, the rest a reviewer overturned on another case in the same driver tick; the seat pass is per seat, not the award pass's one list) and one reading (the top-up at assignment is the shortfall — Appendix A's pots already pay two seats, so the bank mints at the third seat only). **Accepted as 2.8.0 the same day** on that review with four phrases as rulings (the roll's parenthesis and every case at the verdict's odds; the seat pass's per-seat test; the top-up to the seat's need; the court fee from the alias wallet, minted and destroyed), readings 3–5 on the record. **Implemented** behind `Params.plants_every_seat` (on; off and `--rules 2.7.0` the control): the engine's `_adjudicate_plant_seat` (every F or N on a plant at any seat adjudicated by the truth then in force, each reviewer once), the case kept in the real path's shape and resolved by truth (`_settle_plant_challenge`, `_plant_resolve_response`, the vesting step's pre-pass), the markers revealed at closure, `revise_plant` with the second marker, `_plant_top_up` and the court fee destroyed at filing, `_state_verdict_on_plant` at the troop's step, `audit_odds_at_verdict` read by the roll; I20 rewritten per seat, I42 new, I39 amended; the drivers' instrument filing for the plant actor and the plant requester at the real rates and delays (windows of the real filings), the harvest by seat kind, the stage table's new stages; run_q's stamp rates by seat kind; `test_v28` (10), `test_v12`/`v13`/`v14` and one `test_v26` test pinning 1.2.0's path with the flag off; the one golden scenario re-pinned once (it drives `revise_plant`); `EXPECTED_FAIL` 32. The text consolidated as `spec/agentic_economics_loop_spec_v2_8_0.md` (§7.6, §7.7, §8, §12.1, §12.3, §16, §17, §18.1, §20, Appendices A, C, D, U; 2.7.0 to history; dr16 verbatim in `spec/design_revisions/`). The suite in three modes: 355 passed, 0 failed, 32 expected failures. A 400-tick smoke of run 24's entry cell with disputes on (seed 21): 157 plants adjudicated at the initial seat, 10 at member audits, 14 at member dispute panels, 116 plant seats taken by the state's verdict (a fresh population — the real roots' seats went to troops at the same rate), 51 plant disputes filed, 7.5 minted in top-ups, 107 in court fees destroyed, the filing delays zero for both kinds, Ω's income untouched by the plants. **§8.2 read (October 26, 2026; run 36; notes §54; `results/redteam/stability/learned-rev-{careful,stamper,disputes,half}-280/`, the derived tables at `results/redteam/stability/2.8.0-s82/`): the capture closes by more than half and not to the hand's.** The four self-play chains on 2.8.0 (the recipe of the `-2` chains, the rounds settled by round 5), paired by seed against their 2.7.0 reads (§52–§53): both basins and both learners settle at **care 0.68–0.70 / approve blind 0.30–0.32** (from 0.50–0.55 / 0.45–0.47) and the standing false approvals at **30–39 against the hand's 11.4 — 2.6–3.5 times, from 7.4–8.5** (−55 to −60 a run paired; every seed above the hand); the audit layer's overturn rate at the hand's (0.060–0.064 against 0.062, from below it); with disputes on the requesters win **95–98% of their disputes** (from 69–75%) and the standing false approvals read 7–11 against the hand's 4.0 (1.8–2.8×, from 10–11×; the head alone above the hand on 15 seeds of 20, the first learned cell not above it on every seed) with the mix unmoved (care 0.55–0.60 on both sides of the rule); the half 1.6–2.0× (from 2.4×). Not honest: **the audit seat is still stamped 77–98% by every all-member learner**, plants and real cases alike. The plant prices that seat at π_t β_P of a bond — five to six stamps in a hundred fail, under the price of care — and the population read the price where the odds are read, at the first review (the stamp rate in the 0.7–1.0 odds band 0.66 → 0.37, pinned 0.36 → 0.28, the false approvals passed per suspension 5.6 → 3.4). By the seat's question (seeds 21–23) the population **sides with the challenger**: a dispute's panel rejected blind 55% and stamped 5–11% (the 2.7.0 policy stamped 48–52%), an appeal's panel stamped 58%, the third seat cared 76–85% — never failed by a plant, whose challenges are truthful by construction as the drivers' are (a reading for §8.7: the plant prices a panel only against the challenges the population files); with disputes on no bad plant reaches an audit (the plant requester disputes first, as the real requesters do), so the audit stamp is free and right there. The dishonest basin stops paying the members with disputes off (−1,200 to −2,200 nominal against the hand, from +2,800 to +3,400; −3,100 to −4,500 real) and keeps +3,400 nominal with disputes on. The honest populations (H2 ahead of §8.3; the finals' hand and careful references paired across the rule): honesty unmoved (the hand's false approvals −0.2 ± 0.8), the hand's stampers suspended +2.5 ± 1.1 a run (6 failures a run at the plants' audit seats, 2.3 at the third seat), the hand's world paying for the seats in work — awards −121 ± 33 (−5%), tasks per 1,000 −1.2 ± 0.4 (−4%), the state's share +1.5 ± 0.5 points; all-careful −1.0 ± 0.5 tasks per 1,000 and nothing else; the plants per period unchanged, 1.27 adjudicated seats a plant, the state's verdict on 0.17 of the plants (the real roots' troop seats 0.32 a root — alike per pending F), the pots topped up 141–157 nominal a run, the court fee destroyed 17 (disputes off) and 134 (on), no P or ⊥ in any cell; **the cost of truth +23–29%** (3,214 against 2,490 nominal a run); Ω within noise, I42 in every run. The stage check at the new seats (H3 ahead of §8.4): the filing delay 0.00 for both kinds; the per-root audited and state-seat shares differ by construction (β_P 0.75: a plant reaches a pending F 0.35 of the time against a real root's 0.80) and per pending F the plant's audit roll is the real root's (0.79 against 0.84 obligations); the stamp rates plant against real within 4 points at the initial and audit seats and within 6 at the panels by question. Hypothesis 1 against its text: the basin test, the care share past 0.6 and the disputes won confirmed; the audit seat's stamp rate falling to the first review's and the false approvals within a factor of two of the hand's not. Run 34's finding stands under 2.8.0 at a third of its size; the lever the arithmetic names is π_t, the rc's §8.7 red team (the dial pinned at its floor) its test from below; whether the price at the audit seat is a reading or a rule is §19's question and the reviewer's. **The ruling after run 36 (October 26, 2026; notes §55; Appendix U [S36]):** Hypothesis 1's basin, care-share and disputes-won clauses hold, its audit-seat and factor-of-two clauses do not; 2.8.0 closed the two layers and did not close the seat; the finding stands at a third of its size. §19: the stamping of a seat priced under the price of care is an evaluation under fixed rules, recorded against the rules as run 34's was; the rule question is decided by cells. The arithmetic on record in the reviewer's form — the share of audit stamps that fail π β_P s / [π(1−β_P+β_P s) + (1−π) f_R], 0.054 at π 0.21, s 0.25, against the first review's β_P π; the dial bounded by construction and blind to the seat, F̂ at the audit seat 0.85 beside the dial's 0.21. The plant's truthful challenges the stated principle, not a conformance item. **§8.3, §8.4, §8.6 and §8.7's hand instruments read (notes §56–§57; `50c0432c`).** §8.3/§8.6 by hand (160 runs, four cells × two rules, paired; `results/redteam/stability/2.8.0-s83/finals.md`): honesty unmoved in every cell, the plants per period unchanged, the members' care budget unchanged with a quarter of it moved to the plants (+27% care on plants in the entry cell, +69% in the fixed 60/40), the real seats they leave taken by the state's reviewers whose fees reach Ω, the awards −3.6 to −6%, the tasks per credit −3%, a careful population's suspensions +1.45 ± 0.66, the cost of truth +18% to +72%. §8.4 (`2.8.0-s84/seats.md`; `redteam.probe --seat … appeal|dispute` at `32cf4ec4`): the audit seat is blind (the gap raw − context −0.002 ± 0.002 / +0.003 ± 0.003; the case's fields at chance), the initial seat +0.006 / +0.005 against floors of +0.003 / +0.004, the panel's gap (+0.046 off, +0.185 on) the question's base rate — a disputed case a plant 56 times in a hundred, an appealed one 11, β_P 0.75 against b — zero within a question. §8.7 by hand (`2.8.0-s87/hand.md`): the `log` tell-reader of the Q2 shape dies at the first review (the log is empty there) and the caring reader (`--tell-initial care`) is the complete later-seat tell, 10–20% richer than a careful member; `freshname` poorer under 2.8.0; the audit-only stamper within noise of the careful (+2 ± 70; 5 plant audit seats a life, +0.65 failures, no suspension). Evaluations under fixed rules; nothing proposed. **Next: §8.5 and §8.7's cells** — §8.5 Q1's line on 2.8.0 (`Q1/rearrive-280/`) and Q3's, Q4's finals against 2.7.0 controls on the current engine (`eval-280` / `eval-270`; the October 22 finals do not pair across the rule alone — Q3 ran `--good-delivery certain`); §8.7 three cells — (a) the dial pinned at its floor (`--dial off`, π 0.10), (b) pinned at π_max 0.40 (the mirror, a diagnostic), (c) untruthful challengers (`--appeal-lie 0.1 --dispute-lie 0.1`: an actor appealing bad work's N, a requester disputing good work's F) — with the `log` tell-reader and the audit-only stamper beside. Named for after §8.7, not drafted: the planted approval if (b) does not price the seat; the untruthful plant challenge at the rate of lost real challenges if (c) captures the panels. The resubmission seat dormant until a population answers P (a fourth learner action — a new version and a calibration, not 2.8.0's).

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

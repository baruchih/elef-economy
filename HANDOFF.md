# Handoff — where the economic loop stands, October 17, 2026

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
constraint — the X = 8 cells of the rerun are the control for that. Next, per the revision's §8: the
appeals run (which measures the a of §7.3, the term stampers never pay), then the requester-dispute run.

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

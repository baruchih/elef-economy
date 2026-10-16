# Handoff — where the economic loop stands, October 15, 2026

## In one paragraph

We have a rulebook and an engine that implements it, and they are consistent with each other as far
as ten external reviews and 167 tests can show. The rulebook is frozen at v1.0.1. What has **not** been
shown is what the rules do when participants are self-interested — whether careful review beats
stamping, whether price pressure starves reliable actors, whether the money behaves. That is the next
layer, and it is a simulator question: the engine is already the simulator of the *rules*; what it lacks
is *participants*. Nothing else is blocking.

## The three layers, and which one we are on

| Layer | Question | Status |
|---|---|---|
| Approach | What kind of economy is this? Who pays, who judges, what is final? | Settled by v0.4 |
| Rulebook consistency | Do the rules contradict each other? Does the engine apply them? | **Done** — v0.5–v1.0.1, nine conformance passes |
| Strategy research | Given these rules, what do self-interested participants do? | **Not started** — spec §18 |

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
| v1.0.1 | Errata applied in place. No rule, default, permitted operation or engine change | — | — | **frozen** |

Test suite across versions: v0.7 104 + 1 xfail → v0.8 123 + 1 → v0.9 148 + 1 → v0.10 152 + 24 → v1.0.1
156 + 24 → October 16 performance pass 161 + 24 → October 16 record mode 167 + 24 (the 24: one
original, four superseded by the view contract, nineteen on the withdrawn path; the four v1.0.1 tests
cover withdrawing an unawarded request, the one permitted operation no suite had exercised; the five
performance tests prove the per-tick check equals the full audit and the History head is unchanged; the
six record-mode tests prove the record on disk gives the identical fingerprint and verifies from the
file alone). Expected failures are strict and parameter-exact in both entry points.
Every reviewer's test file is in the suite byte-for-byte — a claim this repo cannot itself verify: the
reviewers' test bundles were received as separate archives and are not included here, only their reports
in `reviews/`. The reports name the tests they shipped; a verifier can compare names and counts.

## The baseline in brief (spec is authoritative)

- **Money enters with requests.** Pay-in = award + verification deposit + service fee. Emission
  E_t = E_0·2^(−t/H) pays reviewers whose verdicts stood, by role weight; nothing carried forward.
- **One payout rule**: entitlements → cost debts for every review → Ω advances → pro-rata haircut.
  Ω is a revolving float, repaid FIFO; an unrecovered advance is Ω's loss, not a reviewer claim.
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

## The stamping calculation — the first thing a run must answer

A reviewer that approves everything without reading, audited with probability p on submissions that
fail at rate b, expects E[ΔW] = (1 − pb)·f̄ − pb·G^V per review. At the defaults (p = 0.5, b = 0.2,
f̄ ≈ 2, G^V = 5) that is about **+1.3**, and still +0.6 at p = 1. Money alone does not make stamping
unprofitable. The rules rely on **reliability loss** (ρ feeds selection) as the deterrent. Whether that
is enough is unknown until it is run. (Spec §7.3.)

## What a run must find (spec §18.1)

1. Careful vs careless review once reliability loss is counted; at which (p, G^V, f̄) it stops.
2. Does λ = 0.2 produce competition without starving reliable actors?
3. Does φ = 2K cover root-plus-nested verification; how often Ω advances; how large its claim gets.
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
costs about 0.3 ms per case — minutes for millions of cases — which is what `full_check_every` should be
set with in mind. Details and numbers in `agentic_sim/README.md`.

## Where the drivers should go

`agentic_sim/drivers/` (new package): task world, policy populations (actor, reviewer, orchestrator,
human), a run harness that declares its permitted operations and logs the metrics above, and the
control. Drivers use only `World`'s public operations and never reach into engine internals. The engine
and its tests stay as they are; a driver that needs an engine change has found either a conformance bug
(fix + regression) or a design question (write it up, do not patch around it).

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

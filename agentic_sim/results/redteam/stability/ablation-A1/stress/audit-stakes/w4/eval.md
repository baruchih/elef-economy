# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --pi-a0 0.30 --pi-a-max 0.30 --bond-mult-later 1 --w-audit 1.5`, seeds 21-80, hide ``, model `None` (value off, horizon 8)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.3audit:0.25 | 35078.6 ± 408.1 | -357.9 ± 407.5 | 5040.0 | 0.989 | 0.000 | 0.000 | 0.000 | 0.000 | 0.432 | 0.026 | 2.85 | 0.68 | 0.32 |
| careful | 35436.5 ± 453.6 | nan ± nan | 5144.6 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.442 | 0.000 | 2.47 | 0.00 | 0.27 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:dose0.3audit:0.25 | 0.000 (15894) / 0.000 (155758) | 0.032 (23611) / 0.036 (73170) | 0.000 (21955) / 0.000 (12012) | — / — |
| careful | 0.000 (15813) / 0.000 (156422) | 0.000 (24510) / 0.000 (75693) | 0.000 (23542) / 0.000 (12696) | — / — |

The stressed world's fourth action by seat kind — the allowance claimed and the verdict F without inspecting (counted above among the blind verdicts; the ledger sees a careful review, so the measured reading below cannot see it):

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:dose0.3audit:0.25 | 0.000 (15894) / 0.000 (155758) | 0.032 (23611) / 0.036 (73170) | 0.000 (21955) / 0.000 (12012) | — / — |
| careful | 0.000 (15813) / 0.000 (156422) | 0.000 (24510) / 0.000 (75693) | 0.000 (23542) / 0.000 (12696) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| mix:dose0.3audit:0.25 | 0.000 (15894) [rej. blind 0.000] / 0.000 (155758) [rej. blind 0.000] | 0.000 (23611) / 0.000 (73170) | 0.000 (21955) / 0.000 (12012) | — / — | 2.5 ± 0.2 | -3379 |
| careful | 0.000 (15813) [rej. blind 0.000] / 0.000 (156422) [rej. blind 0.000] | 0.000 (24510) / 0.000 (75693) | 0.000 (23542) / 0.000 (12696) | — / — | 2.6 ± 0.2 | +23 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.3audit:0.25 | — | 0.909 | — (0) | — (0) | 0.000 (56897) | 0.000 (500) | 0.000 (245003) | 4.833 | 678.133 | 1.170 | 0.141 |
| careful | — | 0.901 | — (0) | — (0) | 0.000 (61742) | 0.000 (1167) | 0.000 (245767) | 5.450 | 664.317 | 1.168 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| mix:dose0.3audit:0.25 | 39.583 | 0.000 | 0.000 | 0.000 | 0.000 | 0.317 | 0.000 |
| careful | 39.583 | 0.000 | 0.000 | 0.000 | 0.000 | 0.267 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.3audit:0.25 | 23.433 / 39.583 | 2.850 ± 0.210 | +0.383 ± 0.256 | 10.433 | +0.833 ± 0.661 | 3.200 | 0.050 | 4.833 | -0.617 ± 0.401 | 1904.400 | 0.024 | -0.001 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 26371.303 ± 220.800 | -251.166 ± 233.552 | 35078.6 ± 408.1 | -357.9 ± 407.5 | 35.654 | -0.205 ± 0.211 | 16.329 ± 0.225 | +0.114 ± 0.292 | 18.281 | 0.001 | 2602.367 | 19.583 | 16.150 | -0.117 ± 0.277 | 536.757 | 220.450 |
| careful | 23.317 / 39.583 | 2.467 ± 0.205 | — | 9.600 | — | 4.167 | 0.046 | 5.450 | — | 1904.850 | 0.025 | — | 0.000 / 0.000 (0.000 / 0.000) | 26622.470 ± 185.900 | — | 35436.5 ± 453.6 | — | 35.859 | — | 16.215 ± 0.226 | — | 18.104 | 0.001 | 2614.683 | 19.583 | 16.267 | — | 549.581 | 210.067 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **mix:dose0.3audit:0.25**: p0 1.000/0.000/0.000 (601); p1 1.000/0.000/0.000 (794); p2 1.000/0.000/0.000 (996); p3 1.000/0.000/0.000 (1115); p4 1.000/0.000/0.000 (1116); p5 1.000/0.000/0.000 (330); p6 1.000/0.000/0.000 (21); p7 1.000/0.000/0.000 (10)
- **careful**: p0 1.000/0.000/0.000 (599); p1 1.000/0.000/0.000 (797); p2 1.000/0.000/0.000 (1075); p3 1.000/0.000/0.000 (1161); p4 1.000/0.000/0.000 (1155); p5 1.000/0.000/0.000 (337); p6 1.000/0.000/0.000 (21)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.3audit:0.25 | 2596.0 / 264.9 | 0.29 / 0.19 | -0.10 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.12 / 0.12 | -0.00 ± 0.00 | 0.185 / 0.155 | -0.030 ± 0.003 | 0.067 / 0.075 | 0.001 / 0.000 | 0.054 / 0.055 | +0.001 ± 0.002 | 1.66 / 1.38 | -0.28 ± 0.05 |
| careful | 2607.0 / 263.6 | 0.24 / 0.15 | -0.09 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.14 / 0.14 | -0.00 ± 0.00 | 0.170 / 0.142 | -0.028 ± 0.003 | 0.061 / 0.067 | 0.001 / 0.000 | 0.050 / 0.050 | -0.000 ± 0.002 | 1.54 / 1.27 | -0.27 ± 0.04 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| mix:dose0.3audit:0.25 | -0.10 ± 0.01 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.031 ± 0.003 | +0.008 ± 0.002 | +0.001 ± 0.002 |
| careful | -0.09 ± 0.01 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.030 ± 0.003 | +0.005 ± 0.002 | +0.000 ± 0.002 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| mix:dose0.3audit:0.25 | 0.463 / 0.133 | 0.36 / 0.37 | 0.040 / 0.162 | 0.00 / 0.00 | 0.34 / 0.35 | 0.317 / 0.264 |
| careful | 0.477 / 0.142 | 0.30 / 0.31 | 0.039 / 0.165 | 0.00 / 0.00 | 0.29 / 0.32 | 0.297 / 0.248 |

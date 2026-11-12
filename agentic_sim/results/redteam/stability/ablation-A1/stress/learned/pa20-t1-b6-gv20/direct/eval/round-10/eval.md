# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --pi-a0 0.20 --pi-a-max 0.20 --temptation 1 --gv 20 --bond-mult-later 1.5`, seeds 21-40, hide ``, model `None` (value off, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 28480.6 ± 827.5 | -506.2 ± 780.8 | 4251.6 | 0.827 | 0.027 | 0.032 | 0.084 | 0.106 | 0.333 | 0.313 | 16.05 | 61.25 | 0.15 |
| careful | 28986.8 ± 924.5 | nan ± nan | 4455.6 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.402 | 0.000 | 1.85 | 0.00 | 0.25 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| direct | 0.084 (9123) [rej. blind 0.005] / 0.106 (47624) [rej. blind 0.005] | 0.251 (4881) [rej. blind 0.055] / 0.322 (16939) [rej. blind 0.020] | 0.346 (3413) [rej. blind 0.300] / 0.325 (3052) [rej. blind 0.287] | — / — |
| careful | 0.000 (4864) / 0.000 (48384) | 0.000 (5093) / 0.000 (22300) | 0.000 (4851) / 0.000 (3619) | — / — |

The stressed world's fourth action by seat kind — the allowance claimed and the verdict F without inspecting (counted above among the blind verdicts; the ledger sees a careful review, so the measured reading below cannot see it):

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| direct | 0.062 (9123) / 0.080 (47624) | 0.160 (4881) / 0.248 (16939) | 0.044 (3413) / 0.029 (3052) | — / — |
| careful | 0.000 (4864) / 0.000 (48384) | 0.000 (5093) / 0.000 (22300) | 0.000 (4851) / 0.000 (3619) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| direct | 0.022 (9123) [rej. blind 0.006] / 0.027 (47624) [rej. blind 0.005] | 0.092 (4881) [rej. blind 0.055] / 0.077 (16939) [rej. blind 0.020] | 0.303 (3413) [rej. blind 0.300] / 0.296 (3052) [rej. blind 0.287] | — / — | 30.8 ± 1.9 | -9525 |
| careful | 0.000 (4864) / 0.000 (48384) [rej. blind 0.000] | 0.000 (5093) / 0.002 (22300) [rej. blind 0.000] | 0.000 (4851) / 0.001 (3619) | — / — | 41.8 ± 1.7 | +59 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 0.983 | 0.991 | — (0) | — (0) | 0.049 (1336) | 0.062 (1019) | 0.026 (82677) | 26.150 | 446.350 | 1.753 | 2.342 |
| careful | — | 0.908 | — (0) | — (0) | 0.000 (16684) | 0.000 (521) | 0.000 (71906) | 24.550 | 639.200 | 1.474 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| direct | 39.800 | 0.000 | 0.000 | 0.000 | 0.000 | 0.150 | 0.000 |
| careful | 39.800 | 0.000 | 0.000 | 0.000 | 0.000 | 0.250 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 26.250 / 39.800 | 16.050 ± 1.247 | +14.200 ± 1.341 | 43.850 | +34.800 ± 2.243 | 5.650 | 0.140 | 6.350 | +1.600 ± 0.783 | 1863.000 | 0.051 | +0.027 ± 0.002 | 0.000 / 0.000 (0.000 / 0.000) | 23445.933 ± 355.477 | -825.188 ± 380.669 | 28480.6 ± 827.5 | -506.2 ± 780.8 | 31.267 | -1.260 ± 0.428 | 19.060 ± 0.532 | +0.615 ± 0.604 | 20.894 | 0.020 | 2352.150 | 19.800 | 13.550 | +1.900 ± 0.873 | 95.142 | 1527.650 |
| careful | 28.150 / 39.800 | 1.850 ± 0.350 | — | 9.050 | — | 3.300 | 0.048 | 4.750 | — | 1773.400 | 0.024 | — | 0.000 / 0.000 (0.000 / 0.000) | 24271.120 ± 340.813 | — | 28986.8 ± 924.5 | — | 32.528 | — | 18.445 ± 0.674 | — | 20.975 | 0.024 | 2400.100 | 19.800 | 11.650 | — | 268.954 | 1561.150 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **direct**: p0 0.986/0.007/0.007 (528); p1 0.912/0.054/0.034 (473); p2 0.919/0.050/0.031 (480); p3 0.924/0.037/0.039 (410); p4 0.940/0.023/0.036 (394); p5 0.895/0.035/0.070 (396); p6 0.913/0.027/0.060 (340); p7 0.937/0.024/0.039 (293); p8 0.951/0.019/0.030 (213); p9 0.948/0.016/0.036 (128); p10 0.960/0.011/0.029 (70); p11 0.959/0.011/0.030 (42); p12 0.960/0.024/0.016 (6)
- **careful**: p0 1.000/0.000/0.000 (579); p1 1.000/0.000/0.000 (709); p2 1.000/0.000/0.000 (918); p3 1.000/0.000/0.000 (1026); p4 1.000/0.000/0.000 (1067); p5 1.000/0.000/0.000 (150); p6 1.000/0.000/0.000 (6)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 2381.2 / 456.1 | 1.00 / 0.88 | -0.12 ± 0.05 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.18 / 0.15 | -0.02 ± 0.01 | 0.408 / 0.384 | -0.024 ± 0.013 | 0.202 / 0.210 | 0.020 / 0.000 | 0.124 / 0.117 | -0.008 ± 0.004 | 2.81 / 2.46 | -0.34 ± 0.10 |
| careful | 2419.2 / 243.2 | 0.80 / 0.55 | -0.26 ± 0.04 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.29 / 0.28 | -0.02 ± 0.01 | 0.302 / 0.249 | -0.054 ± 0.006 | 0.128 / 0.125 | 0.024 / 0.000 | 0.087 / 0.070 | -0.018 ± 0.004 | 2.87 / 2.23 | -0.64 ± 0.15 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| direct | -0.08 ± 0.02 | +0.00 ± 0.00 | -0.03 ± 0.00 | -0.041 ± 0.006 | -0.006 ± 0.004 | -0.005 ± 0.002 |
| careful | -0.25 ± 0.04 | +0.00 ± 0.00 | -0.02 ± 0.01 | -0.052 ± 0.007 | -0.003 ± 0.004 | -0.017 ± 0.004 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| direct | 0.347 / 0.170 | 0.50 / 0.48 | 0.036 / 0.103 | 0.00 / 0.00 | 0.52 / 0.52 | 0.504 / 0.346 |
| careful | 0.450 / 0.144 | 0.32 / 0.31 | 0.039 / 0.168 | 0.00 / 0.00 | 0.33 / 0.27 | 0.327 / 0.337 |

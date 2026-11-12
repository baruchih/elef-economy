# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --pi-a0 0.20 --pi-a-max 0.20 --temptation 1 --gv 20 --bond-mult-later 1.5`, seeds 21-40, hide ``, model `None` (value off, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 27397.8 ± 693.0 | -1588.9 ± 1124.8 | 4284.0 | 0.840 | 0.035 | 0.024 | 0.086 | 0.110 | 0.350 | 0.257 | 18.50 | 68.75 | 0.30 |
| careful | 28986.8 ± 924.5 | nan ± nan | 4455.6 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.402 | 0.000 | 1.85 | 0.00 | 0.25 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| direct | 0.086 (9232) [rej. blind 0.002] / 0.110 (46447) [rej. blind 0.002] | 0.203 (5291) [rej. blind 0.029] / 0.261 (18015) [rej. blind 0.005] | 0.305 (3762) [rej. blind 0.260] / 0.270 (2933) [rej. blind 0.235] | — / — |
| careful | 0.000 (4864) / 0.000 (48384) | 0.000 (5093) / 0.000 (22300) | 0.000 (4851) / 0.000 (3619) | — / — |

The stressed world's fourth action by seat kind — the allowance claimed and the verdict F without inspecting (counted above among the blind verdicts; the ledger sees a careful review, so the measured reading below cannot see it):

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| direct | 0.052 (9232) / 0.077 (46447) | 0.133 (5291) / 0.202 (18015) | 0.040 (3762) / 0.026 (2933) | — / — |
| careful | 0.000 (4864) / 0.000 (48384) | 0.000 (5093) / 0.000 (22300) | 0.000 (4851) / 0.000 (3619) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| direct | 0.035 (9232) [rej. blind 0.002] / 0.034 (46447) [rej. blind 0.002] | 0.070 (5291) [rej. blind 0.029] / 0.059 (18015) [rej. blind 0.005] | 0.264 (3762) [rej. blind 0.260] / 0.244 (2933) [rej. blind 0.235] | — / — | 32.2 ± 1.5 | -8569 |
| careful | 0.000 (4864) / 0.000 (48384) [rej. blind 0.000] | 0.000 (5093) / 0.002 (22300) [rej. blind 0.000] | 0.000 (4851) / 0.001 (3619) | — / — | 41.8 ± 1.7 | +59 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 0.973 | 0.990 | — (0) | — (0) | 0.097 (1785) | 0.039 (1369) | 0.033 (82526) | 27.500 | 439.250 | 1.752 | 2.500 |
| careful | — | 0.908 | — (0) | — (0) | 0.000 (16684) | 0.000 (521) | 0.000 (71906) | 24.550 | 639.200 | 1.474 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| direct | 39.800 | 0.000 | 0.000 | 0.000 | 0.000 | 0.300 | 0.000 |
| careful | 39.800 | 0.000 | 0.000 | 0.000 | 0.000 | 0.250 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 26.500 / 39.800 | 18.500 ± 1.455 | +16.650 ± 1.600 | 44.300 | +35.250 ± 2.087 | 5.050 | 0.118 | 7.700 | +2.950 ± 0.709 | 1820.200 | 0.049 | +0.026 ± 0.002 | 0.000 / 0.000 (0.000 / 0.000) | 24058.678 ± 432.985 | -212.442 ± 411.353 | 27397.8 ± 693.0 | -1588.9 ± 1124.8 | 30.307 | -2.220 ± 0.519 | 20.193 ± 0.564 | +1.748 ± 1.005 | 21.646 | 0.033 | 2271.350 | 19.800 | 13.300 | +1.650 ± 0.796 | 52.504 | 1551.400 |
| careful | 28.150 / 39.800 | 1.850 ± 0.350 | — | 9.050 | — | 3.300 | 0.048 | 4.750 | — | 1773.400 | 0.024 | — | 0.000 / 0.000 (0.000 / 0.000) | 24271.120 ± 340.813 | — | 28986.8 ± 924.5 | — | 32.528 | — | 18.445 ± 0.674 | — | 20.975 | 0.024 | 2400.100 | 19.800 | 11.650 | — | 268.954 | 1561.150 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **direct**: p0 0.982/0.012/0.006 (530); p1 0.918/0.053/0.029 (457); p2 0.925/0.041/0.035 (501); p3 0.943/0.033/0.024 (445); p4 0.886/0.086/0.028 (408); p5 0.895/0.067/0.038 (373); p6 0.946/0.028/0.026 (313); p7 0.957/0.019/0.024 (293); p8 0.958/0.014/0.028 (244); p9 0.950/0.014/0.036 (174); p10 0.955/0.019/0.025 (93); p11 0.904/0.056/0.040 (25)
- **careful**: p0 1.000/0.000/0.000 (579); p1 1.000/0.000/0.000 (709); p2 1.000/0.000/0.000 (918); p3 1.000/0.000/0.000 (1026); p4 1.000/0.000/0.000 (1067); p5 1.000/0.000/0.000 (150); p6 1.000/0.000/0.000 (6)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 2322.3 / 461.6 | 1.24 / 1.06 | -0.18 ± 0.05 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.19 / 0.17 | -0.02 ± 0.00 | 0.436 / 0.416 | -0.020 ± 0.010 | 0.215 / 0.216 | 0.032 / 0.000 | 0.135 / 0.127 | -0.007 ± 0.005 | 3.33 / 2.91 | -0.43 ± 0.10 |
| careful | 2419.2 / 243.2 | 0.80 / 0.55 | -0.26 ± 0.04 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.29 / 0.28 | -0.02 ± 0.01 | 0.302 / 0.249 | -0.054 ± 0.006 | 0.128 / 0.125 | 0.024 / 0.000 | 0.087 / 0.070 | -0.018 ± 0.004 | 2.87 / 2.23 | -0.64 ± 0.15 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| direct | -0.11 ± 0.03 | +0.00 ± 0.00 | -0.03 ± 0.00 | -0.055 ± 0.006 | -0.020 ± 0.006 | +0.000 ± 0.004 |
| careful | -0.25 ± 0.04 | +0.00 ± 0.00 | -0.02 ± 0.01 | -0.052 ± 0.007 | -0.003 ± 0.004 | -0.017 ± 0.004 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| direct | 0.377 / 0.190 | 0.45 / 0.44 | 0.035 / 0.101 | 0.00 / 0.00 | 0.46 / 0.49 | 0.469 / 0.315 |
| careful | 0.450 / 0.144 | 0.32 / 0.31 | 0.039 / 0.168 | 0.00 / 0.00 | 0.33 / 0.27 | 0.327 / 0.337 |

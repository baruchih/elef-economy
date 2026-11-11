# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1 --pi-a0 0.10 --pi-a-max 0.10`, seeds 21-40, hide ``, model `None` (value off, horizon 8)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 30357.5 ± 509.8 | -5144.8 ± 728.9 | 3397.1 | 0.634 | 0.010 | 0.015 | 0.210 | 0.303 | 0.135 | 0.910 | 29.00 | 161.25 | 0.05 |
| careful | 35502.3 ± 852.9 | nan ± nan | 4637.9 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.384 | 0.000 | 2.55 | 0.00 | 0.30 |
| claimer | 9582.7 ± 171.7 | -25919.6 ± 875.8 | 1049.0 | 0.000 | 0.000 | 0.000 | 1.000 | 1.000 | 0.021 | 1.000 | 14.20 | 179.80 | 1.00 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| direct | 0.210 (13552) [rej. blind 0.002] / 0.303 (45205) [rej. blind 0.001] | 0.861 (1442) [rej. blind 0.074] / 0.958 (6235) [rej. blind 0.003] | 0.698 (583) [rej. blind 0.472] / 0.789 (924) [rej. blind 0.618] | — / — |
| careful | 0.000 (5284) / 0.000 (51900) | 0.000 (3178) / 0.000 (24974) | 0.000 (3248) / 0.000 (4174) | — / — |
| claimer | 1.000 (2986) / 1.000 (17556) | — / 1.000 (439) | — / — | — / — |

The stressed world's fourth action by seat kind — the allowance claimed and the verdict F without inspecting (counted above among the blind verdicts; the ledger sees a careful review, so the measured reading below cannot see it):

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| direct | 0.199 (13552) / 0.292 (45205) | 0.774 (1442) / 0.943 (6235) | 0.211 (583) / 0.157 (924) | — / — |
| careful | 0.000 (5284) / 0.000 (51900) | 0.000 (3178) / 0.000 (24974) | 0.000 (3248) / 0.000 (4174) | — / — |
| claimer | 1.000 (2986) / 1.000 (17556) | — / 1.000 (439) | — / — | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| direct | 0.011 (13552) [rej. blind 0.002] / 0.011 (45205) [rej. blind 0.001] | 0.087 (1442) [rej. blind 0.074] / 0.015 (6235) [rej. blind 0.003] | 0.487 (583) [rej. blind 0.472] / 0.632 (924) [rej. blind 0.618] | — / — | 0.5 ± 0.2 | -23170 |
| careful | 0.000 (5284) [rej. blind 0.000] / 0.000 (51900) [rej. blind 0.000] | 0.000 (3178) / 0.000 (24974) | 0.000 (3248) / 0.000 (4174) | — / — | 2.2 ± 0.3 | +7 |
| claimer | 0.000 (2986) / 0.000 (17556) | — / 0.000 (439) | — / — | — / — | 0.0 ± 0.0 | -20979 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 1.000 | 1.000 | — (0) | — (0) | 0.000 (22) | — (0) | 0.010 (67919) | 41.600 | 255.700 | 1.685 | 3.876 |
| careful | — | 0.910 | — (0) | — (0) | 0.000 (16686) | 0.000 (779) | 0.000 (75293) | 24.350 | 668.700 | 1.190 | 0.000 |
| claimer | — | 1.000 | — (0) | — (0) | — (0) | — (0) | 0.000 (20981) | 74.650 | 178.000 | 2.173 | 2.409 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| direct | 39.750 | 0.000 | 0.000 | 0.000 | 0.000 | 0.050 | 0.000 |
| careful | 39.750 | 0.000 | 0.000 | 0.000 | 0.000 | 0.300 | 0.000 |
| claimer | 39.850 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 18.700 / 39.750 | 29.000 ± 1.361 | +26.450 ± 1.424 | 123.400 | +113.300 ± 5.735 | 6.450 | 0.208 | 21.850 | +17.250 ± 0.672 | 1885.800 | 0.083 | +0.058 ± 0.002 | 0.000 / 0.000 (0.000 / 0.000) | 26792.275 ± 405.520 | +1857.625 ± 488.368 | 30357.5 ± 509.8 | -5144.8 ± 728.9 | 29.542 | -6.688 ± 0.481 | 21.167 ± 0.350 | +6.070 ± 0.570 | 20.110 | 0.037 | 2182.800 | 19.750 | 21.050 | +4.250 ± 0.602 | 62.920 | 82.100 |
| careful | 22.950 / 39.750 | 2.550 ± 0.438 | — | 10.100 | — | 3.250 | 0.053 | 4.600 | — | 1896.050 | 0.025 | — | 0.000 / 0.000 (0.000 / 0.000) | 24934.650 ± 445.425 | — | 35502.3 ± 852.9 | — | 36.230 | — | 15.098 ± 0.513 | — | 17.953 | 0.001 | 2599.400 | 19.750 | 16.800 | — | 689.070 | 188.600 |
| claimer | 5.850 / 39.850 | 14.200 ± 0.706 | +11.650 ± 0.674 | 111.850 | +101.750 ± 2.059 | 0.000 | 1.000 | 54.800 | +50.200 ± 1.893 | 877.600 | 0.192 | +0.167 ± 0.003 | 0.000 / 0.000 (0.000 / 0.000) | 7654.287 ± 133.917 | -17280.363 ± 518.037 | 9582.7 ± 171.7 | -25919.6 ± 875.8 | 26.418 | -9.812 ± 0.481 | 28.745 ± 0.671 | +13.647 ± 0.882 | 20.850 | 0.236 | 699.800 | 19.850 | 34.000 | +17.200 ± 0.760 | 5729.779 | 146.750 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **direct**: p0 0.987/0.012/0.001 (301); p1 0.935/0.035/0.031 (182); p2 0.952/0.022/0.026 (173); p3 0.921/0.044/0.035 (153); p4 0.930/0.027/0.043 (149); p5 0.946/0.016/0.037 (150); p6 0.971/0.008/0.022 (153); p7 0.964/0.006/0.031 (160); p8 0.969/0.007/0.024 (158); p9 0.981/0.004/0.015 (153); p10 0.980/0.003/0.017 (152); p11 0.976/0.003/0.021 (149); p12 0.971/0.008/0.021 (143); p13 0.971/0.001/0.028 (55); p14 0.981/0.013/0.006 (8)
- **careful**: p0 1.000/0.000/0.000 (605); p1 1.000/0.000/0.000 (751); p2 1.000/0.000/0.000 (913); p3 1.000/0.000/0.000 (1021); p4 1.000/0.000/0.000 (1014); p5 1.000/0.000/0.000 (292); p6 1.000/0.000/0.000 (40); p7 1.000/0.000/0.000 (2)
- **claimer**: p0 —/—/— (0); p1 —/—/— (0); p2 —/—/— (0); p3 —/—/— (0); p4 —/—/— (0); p5 —/—/— (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 2260.2 / 677.6 | 1.43 / 1.81 | +0.39 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.04 / 0.02 | -0.01 ± 0.00 | 0.538 / 0.614 | +0.077 ± 0.006 | 0.318 / 0.378 | 0.037 / 0.000 | 0.177 / 0.211 | +0.034 ± 0.002 | 3.04 / 3.29 | +0.24 ± 0.06 |
| careful | 2595.0 / 264.2 | 0.28 / 0.20 | -0.08 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.13 / 0.12 | -0.01 ± 0.00 | 0.170 / 0.144 | -0.025 ± 0.006 | 0.068 / 0.078 | 0.001 / 0.000 | 0.056 / 0.051 | -0.005 ± 0.004 | 1.75 / 1.49 | -0.26 ± 0.06 |
| claimer | 877.8 / 149.3 | 1.25 / 0.94 | -0.31 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.03 / 0.02 | -0.01 ± 0.00 | 0.290 / 0.264 | -0.026 ± 0.010 | 0.154 / 0.146 | 0.202 / 0.000 | 0.106 / 0.086 | -0.020 ± 0.005 | 3.72 / 2.68 | -1.04 ± 0.23 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| direct | +0.06 ± 0.01 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.045 ± 0.004 | -0.021 ± 0.004 | +0.009 ± 0.003 |
| careful | -0.08 ± 0.02 | +0.00 ± 0.00 | -0.01 ± 0.01 | -0.024 ± 0.005 | +0.011 ± 0.004 | -0.004 ± 0.004 |
| claimer | -0.81 ± 0.03 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.181 ± 0.013 | -0.119 ± 0.010 | -0.026 ± 0.005 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| direct | 0.137 / 0.069 | 0.58 / 0.61 | 0.027 / 0.073 | 0.00 / 0.00 | 0.54 / 0.56 | 0.820 / 0.613 |
| careful | 0.474 / 0.137 | 0.30 / 0.31 | 0.040 / 0.162 | 0.00 / 0.00 | 0.28 / 0.31 | 0.302 / 0.280 |
| claimer | 0.025 / 0.000 | 0.00 / — | 0.000 / 0.034 | — / 0.00 | — / — | 1.197 / 1.758 |

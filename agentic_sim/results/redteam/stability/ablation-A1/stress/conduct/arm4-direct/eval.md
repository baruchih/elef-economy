# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1 --arm 4`, seeds 21-60, hide ``, model `None` (value off, horizon 8)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:direct:0.25 | 28252.1 ± 452.4 | -2790.9 ± 657.0 | 3071.4 | 0.922 | 0.024 | 0.014 | 0.073 | 0.079 | 0.001 | 0.053 | 3.02 | 31.25 | 0.38 |
| mix:direct:0.75 | 28450.2 ± 375.1 | -2592.7 ± 523.0 | 3145.6 | 0.764 | 0.064 | 0.051 | 0.235 | 0.238 | 0.011 | 0.115 | 5.90 | 93.60 | 0.42 |
| careful | 31042.9 ± 550.2 | nan ± nan | 2927.0 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 2.48 | 0.00 | 0.17 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:direct:0.25 | 0.073 (18867) [rej. blind 0.014] / 0.079 (103912) [rej. blind 0.014] | — / 0.057 (70) | — / 0.000 (6) | — / — |
| mix:direct:0.75 | 0.235 (27320) [rej. blind 0.052] / 0.238 (97151) [rej. blind 0.051] | — / 0.117 (1218) [rej. blind 0.024] | — / 0.097 (134) [rej. blind 0.007] | — / — |
| careful | 0.000 (10900) / 0.000 (106176) | — / 0.000 (5) | — / — | — / — |

The stressed world's fourth action by seat kind — the allowance claimed and the verdict F without inspecting (counted above among the blind verdicts; the ledger sees a careful review, so the measured reading below cannot see it):

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:direct:0.25 | 0.035 (18867) / 0.040 (103912) | — / 0.029 (70) | — / 0.000 (6) | — / — |
| mix:direct:0.75 | 0.123 (27320) / 0.122 (97151) | — / 0.069 (1218) | — / 0.090 (134) | — / — |
| careful | 0.000 (10900) / 0.000 (106176) | — / 0.000 (5) | — / — | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| mix:direct:0.25 | 0.038 (18867) [rej. blind 0.014] / 0.039 (103912) [rej. blind 0.014] | — / 0.029 (70) | — / 0.000 (6) | — / — | 5.2 ± 0.4 | -4816 |
| mix:direct:0.75 | 0.113 (27320) [rej. blind 0.052] / 0.116 (97151) [rej. blind 0.051] | — / 0.048 (1218) [rej. blind 0.024] | — / 0.007 (134) [rej. blind 0.007] | — / — | 4.8 ± 0.4 | -15288 |
| careful | 0.000 (10900) [rej. blind 0.000] / 0.000 (106176) [rej. blind 0.000] | — / 0.000 (5) | — / — | — / — | 5.3 ± 0.4 | +39 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:direct:0.25 | 0.998 | 0.988 | — (0) | — (0) | 0.003 (2565) | 0.009 (2592) | 0.025 (117698) | 10.125 | 501.375 | 1.214 | 3.086 |
| mix:direct:0.75 | 1.000 | 1.000 | — (0) | — (0) | 0.000 (27) | 0.231 (39) | 0.063 (125757) | 17.050 | 377.600 | 1.288 | 5.490 |
| careful | — | 0.952 | — (0) | — (0) | 0.000 (11080) | 0.000 (1162) | 0.000 (104839) | 5.150 | 645.000 | 1.212 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| mix:direct:0.25 | 39.425 | 0.000 | 0.000 | 0.000 | 0.000 | 0.375 | 0.000 |
| mix:direct:0.75 | 39.675 | 0.000 | 0.000 | 0.000 | 0.000 | 0.425 | 0.000 |
| careful | 39.500 | 0.000 | 0.000 | 0.000 | 0.000 | 0.175 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:direct:0.25 | 18.050 / 39.425 | 3.025 ± 0.283 | +0.550 ± 0.427 | 36.700 | +26.750 ± 2.555 | 6.650 | 0.067 | 10.125 | +4.975 ± 0.659 | 1964.025 | 0.031 | +0.015 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 23790.143 ± 431.495 | +3801.124 ± 529.659 | 28252.1 ± 452.4 | -2790.9 ± 657.0 | 34.862 | -3.434 ± 0.480 | 19.687 ± 0.609 | +5.505 ± 0.733 | 17.935 | 0.002 | 2599.375 | 19.425 | 21.375 | +2.225 ± 0.388 | 308.274 | 280.975 |
| mix:direct:0.75 | 15.550 / 39.675 | 5.900 ± 0.318 | +3.425 ± 0.417 | 111.000 | +101.050 ± 2.840 | 14.175 | 0.201 | 17.050 | +11.900 ± 0.649 | 1866.800 | 0.062 | +0.045 ± 0.002 | 0.000 / 0.000 (0.000 / 0.000) | 26086.178 ± 244.359 | +6097.159 ± 398.212 | 28450.2 ± 375.1 | -2592.7 ± 523.0 | 31.750 | -6.546 ± 0.339 | 21.665 ± 0.352 | +7.484 ± 0.527 | 19.142 | 0.022 | 2385.600 | 19.675 | 24.125 | +4.975 ± 0.381 | 66.451 | 326.275 |
| careful | 20.350 / 39.500 | 2.475 ± 0.277 | — | 9.950 | — | 3.850 | 0.045 | 5.150 | — | 1929.600 | 0.017 | — | 0.000 / 0.000 (0.000 / 0.000) | 19989.020 ± 331.294 | — | 31042.9 ± 550.2 | — | 38.296 | — | 14.182 ± 0.367 | — | 16.518 | 0.000 | 2659.550 | 19.500 | 19.150 | — | 999.178 | 263.125 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **mix:direct:0.25**: p0 0.960/0.031/0.009 (540); p1 0.938/0.037/0.025 (452); p2 0.944/0.034/0.022 (364); p3 0.958/0.026/0.016 (316); p4 0.973/0.016/0.011 (289); p5 0.975/0.014/0.012 (245); p6 0.956/0.025/0.019 (186); p7 0.979/0.015/0.006 (150); p8 0.988/0.007/0.005 (132); p9 0.980/0.015/0.005 (115); p10 0.974/0.014/0.011 (80); p11 0.955/0.025/0.021 (52); p12 0.950/0.033/0.017 (22); p13 1.000/0.000/0.000 (6)
- **mix:direct:0.75**: p0 0.879/0.082/0.039 (513); p1 0.839/0.081/0.080 (309); p2 0.809/0.083/0.108 (214); p3 0.858/0.061/0.081 (166); p4 0.834/0.066/0.100 (160); p5 0.885/0.066/0.049 (157); p6 0.910/0.055/0.034 (156); p7 0.910/0.052/0.038 (159); p8 0.891/0.068/0.041 (162); p9 0.901/0.067/0.031 (169); p10 0.896/0.070/0.034 (163); p11 0.910/0.057/0.033 (159); p12 0.868/0.088/0.044 (133); p13 0.843/0.087/0.070 (90); p14 0.773/0.091/0.136 (46); p15 0.770/0.030/0.201 (8); p16 1.000/0.000/0.000 (0)
- **careful**: p0 1.000/0.000/0.000 (556); p1 1.000/0.000/0.000 (540); p2 1.000/0.000/0.000 (542); p3 1.000/0.000/0.000 (529); p4 1.000/0.000/0.000 (529); p5 1.000/0.000/0.000 (205); p6 1.000/0.000/0.000 (25); p7 1.000/0.000/0.000 (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:direct:0.25 | 2597.8 / 471.7 | 0.27 / 0.23 | -0.04 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.08 / 0.08 | -0.00 ± 0.00 | 0.163 / 0.137 | -0.026 ± 0.005 | 0.070 / 0.073 | 0.002 / 0.000 | 0.077 / 0.089 | +0.012 ± 0.002 | 1.83 / 1.62 | -0.20 ± 0.04 |
| mix:direct:0.75 | 2428.8 / 683.0 | 0.84 / 1.04 | +0.20 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.12 / 0.11 | -0.01 ± 0.00 | 0.357 / 0.390 | +0.033 ± 0.005 | 0.184 / 0.219 | 0.022 / 0.000 | 0.131 / 0.161 | +0.030 ± 0.003 | 3.01 / 3.17 | +0.15 ± 0.04 |
| careful | 2654.4 / 272.5 | 0.13 / 0.07 | -0.06 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.06 / 0.07 | +0.01 ± 0.00 | 0.101 / 0.081 | -0.020 ± 0.003 | 0.033 / 0.035 | 0.000 / 0.000 | 0.058 / 0.063 | +0.005 ± 0.003 | 1.38 / 1.29 | -0.09 ± 0.08 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| mix:direct:0.25 | -0.06 ± 0.01 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.034 ± 0.004 | -0.006 ± 0.002 | +0.000 ± 0.002 |
| mix:direct:0.75 | -0.01 ± 0.01 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.048 ± 0.003 | -0.013 ± 0.003 | -0.002 ± 0.002 |
| careful | -0.06 ± 0.01 | +0.00 ± 0.00 | +0.01 ± 0.00 | -0.018 ± 0.003 | +0.003 ± 0.002 | +0.004 ± 0.002 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| mix:direct:0.25 | 0.001 / 0.000 | 0.29 / — | 0.048 / 0.000 | 0.00 / — | — / — | 0.949 / 0.000 |
| mix:direct:0.75 | 0.012 / 0.000 | 0.36 / — | 0.068 / 0.000 | 0.00 / — | — / — | 1.011 / 0.000 |
| careful | 0.000 / 0.000 | 0.50 / — | 0.040 / 0.000 | 0.00 / — | — / — | 0.888 / 0.000 |

# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --pi0 0.40`, seeds 21-40, hide ``, model `results/redteam/stability/learned-rev-picap2-280/wm/models/wm-online-10.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | non-initial share | non-initial stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 28253.6 ± 323.6 | 3567.4 ± 741.2 | 3492.0 | 0.683 | 0.316 | 0.001 | 0.196 | 0.210 | 0.171 | 0.859 | 37.00 | 111.10 | 0.20 |
| careful | 24686.1 ± 683.2 | nan ± nan | 4591.1 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.236 | 0.000 | 14.80 | 0.00 | 0.30 |
| stamper | 3083.4 ± 92.9 | -21602.7 ± 676.9 | 516.8 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.024 | 1.000 | 6.30 | 72.85 | 1.00 |
| hand | 30505.4 ± 712.2 | 5819.3 ± 1059.9 | 4953.6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.326 | 0.000 | 10.45 | 0.00 | 0.60 |

The stamp rate by seat kind (2.8.0 §5), plant / real, with the decisions pooled over the seeds in parentheses — under 2.7.0 a plant reached the initial review alone; under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| greedy | 0.196 (16272) / 0.210 (41651) | 0.979 (1690) / 0.957 (8611) | 0.133 (475) / 0.241 (1141) | — / — |
| careful | 0.000 (19673) / 0.000 (50462) | 0.000 (1916) / 0.000 (14297) | 0.000 (806) / 0.000 (4667) | — / — |
| stamper | 1.000 (2782) / 1.000 (7300) | — / 1.000 (253) | — / — | — / — |
| hand | 0.000 (18714) / 0.000 (48094) | 0.000 (3251) / 0.000 (22872) | 0.000 (1222) / 0.000 (4919) | — / — |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 0.895 | 0.924 | 0.593 (27) | 0.765 (166) | 0.543 (786) | 0.370 (26799) | 0.276 (42062) | 40.800 | 123.250 | 1.898 | 2.723 |
| careful | — | 0.428 | 0.000 (51909) | 0.000 (14197) | 0.000 (5187) | 0.000 (2774) | 0.000 (17754) | 25.250 | 198.450 | 1.369 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (10335) | 63.950 | 75.250 | 1.900 | 1.139 |
| hand | — | 0.716 | 0.000 (4308) | 0.000 (22123) | 0.000 (19930) | 0.000 (17663) | 0.000 (35048) | 36.400 | 225.400 | 1.098 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| greedy | 39.950 | 0.000 | 0.000 | 0.000 | 0.000 | 0.200 | 0.000 |
| careful | 40.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.300 | 0.000 |
| stamper | 40.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| hand | 39.950 | 0.000 | 0.000 | 0.000 | 0.000 | 0.600 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 15.850 / 39.950 | 37.000 ± 1.624 | +22.200 ± 2.278 | 142.100 | +103.750 ± 2.099 | 8.600 | 0.289 | 20.850 | +15.600 ± 0.596 | 1562.550 | 0.048 | +0.023 ± 0.002 | 0.000 / 0.000 (0.000 / 0.000) | 31684.270 ± 441.316 | -1935.886 ± 637.953 | 28253.6 ± 323.6 | +3567.4 ± 741.2 | 27.250 | -6.253 ± 0.525 | 23.890 ± 0.219 | -7.630 ± 0.993 | 22.946 | 0.110 | 1859.450 | 19.950 | 24.100 | +1.600 ± 0.400 | 73.579 | 60.800 |
| careful | 17.500 / 40.000 | 14.800 ± 0.934 | — | 38.350 | — | 13.400 | 0.048 | 5.250 | — | 861.300 | 0.025 | — | 0.000 / 0.000 (0.000 / 0.000) | 33620.156 ± 571.920 | — | 24686.1 ± 683.2 | — | 33.504 | — | 31.520 ± 1.009 | — | 22.646 | 0.003 | 2522.650 | 20.000 | 22.500 | — | 189.461 | 92.150 |
| stamper | 5.900 / 40.000 | 6.300 ± 0.471 | -8.500 ± 1.118 | 103.500 | +65.150 ± 2.376 | 0.000 | 1.000 | 43.950 | +38.700 ± 2.268 | 365.050 | 0.185 | +0.160 ± 0.005 | 0.000 / 0.000 (0.000 / 0.000) | 2288.506 ± 141.032 | -31331.650 ± 556.014 | 3083.4 ± 92.9 | -21602.7 ± 676.9 | 28.295 | -5.208 ± 0.598 | 28.555 ± 0.909 | -2.965 ± 1.291 | 18.065 | 0.375 | 250.750 | 20.000 | 34.100 | +11.600 ± 0.712 | 8412.983 | 95.000 |
| hand | 18.850 / 39.950 | 10.450 ± 0.583 | -4.350 ± 1.168 | 82.050 | +43.700 ± 1.534 | 10.400 | 0.052 | 16.450 | +11.200 ± 0.746 | 1373.900 | 0.042 | +0.017 ± 0.002 | 0.000 / 0.000 (0.000 / 0.000) | 33461.762 ± 385.469 | -158.395 ± 544.646 | 30505.4 ± 712.2 | +5819.3 ± 1059.9 | 31.579 | -1.925 ± 0.489 | 24.011 ± 0.563 | -7.509 ± 1.220 | 21.002 | 0.021 | 2373.550 | 19.950 | 21.100 | -1.400 ± 0.387 | 62.180 | 154.100 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **greedy**: p0 0.849/0.151/0.000 (198); p1 0.586/0.413/0.001 (210); p2 0.586/0.414/0.001 (239); p3 0.555/0.437/0.008 (228); p4 0.676/0.318/0.005 (225); p5 0.715/0.285/0.000 (218); p6 0.716/0.284/0.000 (216); p7 0.751/0.249/0.000 (213); p8 0.699/0.301/0.000 (218); p9 0.718/0.282/0.000 (212); p10 0.691/0.309/0.000 (218); p11 0.666/0.334/0.000 (221); p12 0.666/0.334/0.000 (221); p13 0.674/0.326/0.000 (219); p14 0.677/0.323/0.000 (208); p15 0.705/0.295/0.000 (179); p16 0.777/0.223/0.000 (52)
- **careful**: p0 1.000/0.000/0.000 (195); p1 1.000/0.000/0.000 (255); p2 1.000/0.000/0.000 (275); p3 1.000/0.000/0.000 (284); p4 1.000/0.000/0.000 (260); p5 1.000/0.000/0.000 (232); p6 1.000/0.000/0.000 (229); p7 1.000/0.000/0.000 (229); p8 1.000/0.000/0.000 (230); p9 1.000/0.000/0.000 (231); p10 1.000/0.000/0.000 (225); p11 1.000/0.000/0.000 (225); p12 1.000/0.000/0.000 (234); p13 1.000/0.000/0.000 (229); p14 1.000/0.000/0.000 (224); p15 1.000/0.000/0.000 (228); p16 1.000/0.000/0.000 (224); p17 1.000/0.000/0.000 (227); p18 1.000/0.000/0.000 (221); p19 1.000/0.000/0.000 (110); p20 1.000/0.000/0.000 (24)
- **stamper**: p0 0.000/1.000/0.000 (194); p1 0.000/1.000/0.000 (179); p2 0.000/1.000/0.000 (129); p3 0.000/1.000/0.000 (10); p4 0.000/1.000/0.000 (3); p5 0.000/1.000/0.000 (1); p6 0.000/1.000/0.000 (0)
- **hand**: p0 —/—/— (0); p1 —/—/— (0); p2 —/—/— (0); p3 —/—/— (0); p4 —/—/— (0); p5 —/—/— (0); p6 —/—/— (0); p7 —/—/— (0); p8 —/—/— (0); p9 —/—/— (0); p10 —/—/— (0); p11 —/—/— (0); p12 —/—/— (0); p13 —/—/— (0); p14 —/—/— (0); p15 —/—/— (0); p16 —/—/— (0); p17 —/—/— (0); p18 —/—/— (0); p19 —/—/— (0); p20 —/—/— (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 2082.6 / 813.6 | 2.27 / 2.27 | +0.01 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.07 / 0.04 | -0.02 ± 0.00 | 0.645 / 0.621 | -0.024 ± 0.003 | 0.439 / 0.427 | 0.110 / 0.119 | 0.260 / 0.263 | +0.003 ± 0.004 | 3.97 / 3.91 | -0.05 ± 0.04 |
| careful | 2523.1 / 983.6 | 0.40 / 0.36 | -0.04 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.15 / 0.14 | -0.01 ± 0.00 | 0.148 / 0.129 | -0.019 ± 0.003 | 0.083 / 0.074 | 0.003 / 0.004 | 0.104 / 0.100 | -0.005 ± 0.003 | 2.25 / 2.08 | -0.16 ± 0.05 |
| stamper | 365.0 / 139.1 | 0.87 / 0.80 | -0.07 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.08 / 0.04 | -0.03 ± 0.01 | 0.030 / 0.016 | -0.013 ± 0.007 | 0.016 / 0.010 | 0.309 / 0.279 | 0.053 / 0.053 | -0.000 ± 0.004 | 1.76 / 1.59 | -0.17 ± 0.09 |
| hand | 2404.7 / 935.7 | 0.96 / 0.94 | -0.02 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.18 / 0.16 | -0.02 ± 0.00 | 0.439 / 0.410 | -0.029 ± 0.003 | 0.200 / 0.199 | 0.021 / 0.018 | 0.125 / 0.124 | -0.001 ± 0.002 | 2.70 / 2.63 | -0.06 ± 0.06 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| greedy | +0.00 ± 0.02 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.025 ± 0.003 | -0.013 ± 0.003 | +0.003 ± 0.004 |
| careful | -0.04 ± 0.02 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.019 ± 0.003 | -0.008 ± 0.002 | -0.004 ± 0.003 |
| stamper | -0.06 ± 0.03 | +0.00 ± 0.00 | -0.03 ± 0.00 | -0.011 ± 0.006 | -0.005 ± 0.003 | -0.001 ± 0.004 |
| hand | -0.02 ± 0.02 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.028 ± 0.003 | -0.000 ± 0.003 | -0.001 ± 0.003 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| greedy | 0.205 / 0.103 | 0.54 / 0.56 | 0.029 / 0.010 | 0.00 / 0.00 | 0.51 / 0.60 | 0.630 / 0.396 |
| careful | 0.282 / 0.097 | 0.12 / 0.14 | 0.041 / 0.013 | 0.00 / 0.00 | 0.05 / 0.09 | 0.070 / 0.029 |
| stamper | 0.035 / 0.000 | 0.00 / — | 0.000 / 0.000 | — / — | — / — | 1.181 / 1.725 |
| hand | 0.471 / 0.173 | 0.11 / 0.13 | 0.036 / 0.011 | 0.00 / 0.00 | 0.07 / 0.06 | 0.117 / 0.110 |

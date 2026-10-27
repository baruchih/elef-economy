# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --pi0 0.40`, seeds 21-40, hide ``, model `results/redteam/stability/learned-rev-picap2-280/wm/models/wm-online-5.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | non-initial share | non-initial stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 26523.6 ± 463.8 | 1837.5 ± 847.5 | 3426.3 | 0.688 | 0.311 | 0.002 | 0.186 | 0.193 | 0.189 | 0.833 | 35.30 | 101.95 | 0.15 |
| careful | 24686.1 ± 683.2 | nan ± nan | 4591.1 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.236 | 0.000 | 14.80 | 0.00 | 0.30 |
| stamper | 3083.4 ± 92.9 | -21602.7 ± 676.9 | 516.8 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.024 | 1.000 | 6.30 | 72.85 | 1.00 |

The stamp rate by seat kind (2.8.0 §5), plant / real, with the decisions pooled over the seeds in parentheses — under 2.7.0 a plant reached the initial review alone; under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| greedy | 0.186 (15619) / 0.193 (39945) | 0.949 (1808) / 0.929 (9615) | 0.084 (438) / 0.104 (1101) | — / — |
| careful | 0.000 (19673) / 0.000 (50462) | 0.000 (1916) / 0.000 (14297) | 0.000 (806) / 0.000 (4667) | — / — |
| stamper | 1.000 (2782) / 1.000 (7300) | — / 1.000 (253) | — / — | — / — |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 0.883 | 0.912 | — (0) | 0.722 (133) | 0.611 (265) | 0.359 (30501) | 0.268 (37627) | 43.450 | 76.150 | 2.679 | 2.346 |
| careful | — | 0.428 | 0.000 (51909) | 0.000 (14197) | 0.000 (5187) | 0.000 (2774) | 0.000 (17754) | 25.250 | 198.450 | 1.369 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (10335) | 63.950 | 75.250 | 1.900 | 1.139 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| greedy | 40.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.150 | 0.000 |
| careful | 40.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.300 | 0.000 |
| stamper | 40.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 14.400 / 40.000 | 35.300 ± 1.405 | +20.500 ± 1.652 | 134.400 | +96.050 ± 2.832 | 8.650 | 0.167 | 23.450 | +18.200 ± 0.655 | 1475.900 | 0.048 | +0.023 ± 0.002 | 0.000 / 0.000 (0.000 / 0.000) | 31931.325 ± 462.529 | -1688.831 ± 680.212 | 26523.6 ± 463.8 | +1837.5 ± 847.5 | 26.091 | -7.413 ± 0.510 | 25.675 ± 0.301 | -5.845 ± 1.061 | 24.368 | 0.180 | 1646.150 | 20.000 | 25.600 | +3.100 ± 0.422 | 78.288 | 47.550 |
| careful | 17.500 / 40.000 | 14.800 ± 0.934 | — | 38.350 | — | 13.400 | 0.048 | 5.250 | — | 861.300 | 0.025 | — | 0.000 / 0.000 (0.000 / 0.000) | 33620.156 ± 571.920 | — | 24686.1 ± 683.2 | — | 33.504 | — | 31.520 ± 1.009 | — | 22.646 | 0.003 | 2522.650 | 20.000 | 22.500 | — | 189.461 | 92.150 |
| stamper | 5.900 / 40.000 | 6.300 ± 0.471 | -8.500 ± 1.118 | 103.500 | +65.150 ± 2.376 | 0.000 | 1.000 | 43.950 | +38.700 ± 2.268 | 365.050 | 0.185 | +0.160 ± 0.005 | 0.000 / 0.000 (0.000 / 0.000) | 2288.506 ± 141.032 | -31331.650 ± 556.014 | 3083.4 ± 92.9 | -21602.7 ± 676.9 | 28.295 | -5.208 ± 0.598 | 28.555 ± 0.909 | -2.965 ± 1.291 | 18.065 | 0.375 | 250.750 | 20.000 | 34.100 | +11.600 ± 0.712 | 8412.983 | 95.000 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **greedy**: p0 0.782/0.218/0.000 (194); p1 0.530/0.468/0.002 (216); p2 0.467/0.531/0.002 (225); p3 0.665/0.333/0.002 (219); p4 0.723/0.277/0.000 (220); p5 0.722/0.278/0.000 (209); p6 0.774/0.225/0.001 (214); p7 0.755/0.245/0.001 (214); p8 0.728/0.270/0.001 (220); p9 0.713/0.285/0.002 (224); p10 0.682/0.311/0.006 (234); p11 0.682/0.315/0.003 (231); p12 0.697/0.299/0.003 (226); p13 0.706/0.294/0.000 (232); p14 0.694/0.306/0.000 (221); p15 0.715/0.285/0.000 (119); p16 0.606/0.394/0.000 (10)
- **careful**: p0 1.000/0.000/0.000 (195); p1 1.000/0.000/0.000 (255); p2 1.000/0.000/0.000 (275); p3 1.000/0.000/0.000 (284); p4 1.000/0.000/0.000 (260); p5 1.000/0.000/0.000 (232); p6 1.000/0.000/0.000 (229); p7 1.000/0.000/0.000 (229); p8 1.000/0.000/0.000 (230); p9 1.000/0.000/0.000 (231); p10 1.000/0.000/0.000 (225); p11 1.000/0.000/0.000 (225); p12 1.000/0.000/0.000 (234); p13 1.000/0.000/0.000 (229); p14 1.000/0.000/0.000 (224); p15 1.000/0.000/0.000 (228); p16 1.000/0.000/0.000 (224); p17 1.000/0.000/0.000 (227); p18 1.000/0.000/0.000 (221); p19 1.000/0.000/0.000 (110); p20 1.000/0.000/0.000 (24)
- **stamper**: p0 0.000/1.000/0.000 (194); p1 0.000/1.000/0.000 (179); p2 0.000/1.000/0.000 (129); p3 0.000/1.000/0.000 (10); p4 0.000/1.000/0.000 (3); p5 0.000/1.000/0.000 (1); p6 0.000/1.000/0.000 (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 1997.2 / 781.0 | 2.52 / 2.52 | -0.01 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.07 / 0.05 | -0.03 ± 0.00 | 0.680 / 0.657 | -0.023 ± 0.003 | 0.488 / 0.472 | 0.179 / 0.185 | 0.281 / 0.282 | +0.002 ± 0.004 | 4.19 / 4.18 | -0.01 ± 0.04 |
| careful | 2523.1 / 983.6 | 0.40 / 0.36 | -0.04 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.15 / 0.14 | -0.01 ± 0.00 | 0.148 / 0.129 | -0.019 ± 0.003 | 0.083 / 0.074 | 0.003 / 0.004 | 0.104 / 0.100 | -0.005 ± 0.003 | 2.25 / 2.08 | -0.16 ± 0.05 |
| stamper | 365.0 / 139.1 | 0.87 / 0.80 | -0.07 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.08 / 0.04 | -0.03 ± 0.01 | 0.030 / 0.016 | -0.013 ± 0.007 | 0.016 / 0.010 | 0.309 / 0.279 | 0.053 / 0.053 | -0.000 ± 0.004 | 1.76 / 1.59 | -0.17 ± 0.09 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| greedy | -0.01 ± 0.02 | +0.00 ± 0.00 | -0.03 ± 0.00 | -0.025 ± 0.003 | -0.018 ± 0.003 | +0.001 ± 0.004 |
| careful | -0.04 ± 0.02 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.019 ± 0.003 | -0.008 ± 0.002 | -0.004 ± 0.003 |
| stamper | -0.06 ± 0.03 | +0.00 ± 0.00 | -0.03 ± 0.00 | -0.011 ± 0.006 | -0.005 ± 0.003 | -0.001 ± 0.004 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| greedy | 0.238 / 0.115 | 0.48 / 0.52 | 0.024 / 0.011 | 0.00 / 0.00 | 0.49 / 0.41 | 0.574 / 0.370 |
| careful | 0.282 / 0.097 | 0.12 / 0.14 | 0.041 / 0.013 | 0.00 / 0.00 | 0.05 / 0.09 | 0.070 / 0.029 |
| stamper | 0.035 / 0.000 | 0.00 / — | 0.000 / 0.000 | — / — | — / — | 1.181 / 1.725 |

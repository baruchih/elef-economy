# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --pi0 0.40`, seeds 21-40, hide ``, model `None` (value off, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | non-initial share | non-initial stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 28042.5 ± 485.9 | 3356.3 ± 1007.1 | 3484.3 | 0.683 | 0.305 | 0.012 | 0.226 | 0.247 | 0.156 | 0.731 | 37.65 | 128.70 | 0.25 |
| careful | 24686.1 ± 683.2 | nan ± nan | 4591.1 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.236 | 0.000 | 14.80 | 0.00 | 0.30 |
| stamper | 3083.4 ± 92.9 | -21602.7 ± 676.9 | 516.8 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.024 | 1.000 | 6.30 | 72.85 | 1.00 |

The stamp rate by seat kind (2.8.0 §5), plant / real, with the decisions pooled over the seeds in parentheses — under 2.7.0 a plant reached the initial review alone; under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| direct | 0.226 (16542) / 0.247 (42306) | 0.823 (1507) / 0.850 (7442) | 0.117 (609) / 0.226 (1281) | — / — |
| careful | 0.000 (19673) / 0.000 (50462) | 0.000 (1916) / 0.000 (14297) | 0.000 (806) / 0.000 (4667) | — / — |
| stamper | 1.000 (2782) / 1.000 (7300) | — / 1.000 (253) | — / — | — / — |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 0.903 | 0.941 | 0.481 (260) | 0.686 (255) | 0.460 (389) | 0.398 (21454) | 0.259 (47329) | 39.450 | 157.200 | 1.775 | 3.262 |
| careful | — | 0.428 | 0.000 (51909) | 0.000 (14197) | 0.000 (5187) | 0.000 (2774) | 0.000 (17754) | 25.250 | 198.450 | 1.369 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (10335) | 63.950 | 75.250 | 1.900 | 1.139 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| direct | 39.950 | 0.000 | 0.000 | 0.000 | 0.000 | 0.250 | 0.000 |
| careful | 40.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.300 | 0.000 |
| stamper | 40.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 16.500 / 39.950 | 37.650 ± 1.450 | +22.850 ± 1.573 | 154.800 | +116.450 ± 4.423 | 12.600 | 0.245 | 19.500 | +14.250 ± 0.557 | 1609.600 | 0.057 | +0.032 ± 0.002 | 0.000 / 0.000 (0.000 / 0.000) | 31361.436 ± 431.275 | -2258.720 ± 564.638 | 28042.5 ± 485.9 | +3356.3 ± 1007.1 | 27.603 | -5.900 ± 0.620 | 23.962 ± 0.462 | -7.558 ± 1.218 | 22.679 | 0.081 | 1955.550 | 19.950 | 23.450 | +0.950 ± 0.613 | 70.020 | 51.650 |
| careful | 17.500 / 40.000 | 14.800 ± 0.934 | — | 38.350 | — | 13.400 | 0.048 | 5.250 | — | 861.300 | 0.025 | — | 0.000 / 0.000 (0.000 / 0.000) | 33620.156 ± 571.920 | — | 24686.1 ± 683.2 | — | 33.504 | — | 31.520 ± 1.009 | — | 22.646 | 0.003 | 2522.650 | 20.000 | 22.500 | — | 189.461 | 92.150 |
| stamper | 5.900 / 40.000 | 6.300 ± 0.471 | -8.500 ± 1.118 | 103.500 | +65.150 ± 2.376 | 0.000 | 1.000 | 43.950 | +38.700 ± 2.268 | 365.050 | 0.185 | +0.160 ± 0.005 | 0.000 / 0.000 (0.000 / 0.000) | 2288.506 ± 141.032 | -31331.650 ± 556.014 | 3083.4 ± 92.9 | -21602.7 ± 676.9 | 28.295 | -5.208 ± 0.598 | 28.555 ± 0.909 | -2.965 ± 1.291 | 18.065 | 0.375 | 250.750 | 20.000 | 34.100 | +11.600 ± 0.712 | 8412.983 | 95.000 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **direct**: p0 0.862/0.138/0.001 (196); p1 0.622/0.370/0.008 (215); p2 0.530/0.459/0.011 (224); p3 0.573/0.379/0.048 (236); p4 0.631/0.339/0.030 (230); p5 0.644/0.344/0.012 (219); p6 0.697/0.294/0.009 (215); p7 0.747/0.249/0.004 (204); p8 0.726/0.271/0.004 (208); p9 0.742/0.254/0.003 (202); p10 0.720/0.277/0.003 (203); p11 0.724/0.269/0.007 (202); p12 0.704/0.285/0.011 (201); p13 0.686/0.302/0.011 (206); p14 0.678/0.314/0.008 (203); p15 0.657/0.328/0.015 (188); p16 0.719/0.266/0.015 (99); p17 0.725/0.269/0.006 (32); p18 0.612/0.388/0.000 (2)
- **careful**: p0 1.000/0.000/0.000 (195); p1 1.000/0.000/0.000 (255); p2 1.000/0.000/0.000 (275); p3 1.000/0.000/0.000 (284); p4 1.000/0.000/0.000 (260); p5 1.000/0.000/0.000 (232); p6 1.000/0.000/0.000 (229); p7 1.000/0.000/0.000 (229); p8 1.000/0.000/0.000 (230); p9 1.000/0.000/0.000 (231); p10 1.000/0.000/0.000 (225); p11 1.000/0.000/0.000 (225); p12 1.000/0.000/0.000 (234); p13 1.000/0.000/0.000 (229); p14 1.000/0.000/0.000 (224); p15 1.000/0.000/0.000 (228); p16 1.000/0.000/0.000 (224); p17 1.000/0.000/0.000 (227); p18 1.000/0.000/0.000 (221); p19 1.000/0.000/0.000 (110); p20 1.000/0.000/0.000 (24)
- **stamper**: p0 0.000/1.000/0.000 (194); p1 0.000/1.000/0.000 (179); p2 0.000/1.000/0.000 (129); p3 0.000/1.000/0.000 (10); p4 0.000/1.000/0.000 (3); p5 0.000/1.000/0.000 (1); p6 0.000/1.000/0.000 (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 2115.3 / 827.1 | 2.04 / 2.12 | +0.08 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.06 / 0.04 | -0.02 ± 0.00 | 0.623 / 0.603 | -0.020 ± 0.003 | 0.411 / 0.402 | 0.081 / 0.089 | 0.236 / 0.239 | +0.002 ± 0.004 | 3.73 / 3.76 | +0.03 ± 0.04 |
| careful | 2523.1 / 983.6 | 0.40 / 0.36 | -0.04 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.15 / 0.14 | -0.01 ± 0.00 | 0.148 / 0.129 | -0.019 ± 0.003 | 0.083 / 0.074 | 0.003 / 0.004 | 0.104 / 0.100 | -0.005 ± 0.003 | 2.25 / 2.08 | -0.16 ± 0.05 |
| stamper | 365.0 / 139.1 | 0.87 / 0.80 | -0.07 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.08 / 0.04 | -0.03 ± 0.01 | 0.030 / 0.016 | -0.013 ± 0.007 | 0.016 / 0.010 | 0.309 / 0.279 | 0.053 / 0.053 | -0.000 ± 0.004 | 1.76 / 1.59 | -0.17 ± 0.09 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| direct | +0.08 ± 0.02 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.021 ± 0.003 | -0.010 ± 0.003 | +0.002 ± 0.004 |
| careful | -0.04 ± 0.02 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.019 ± 0.003 | -0.008 ± 0.002 | -0.004 ± 0.003 |
| stamper | -0.06 ± 0.03 | +0.00 ± 0.00 | -0.03 ± 0.00 | -0.011 ± 0.006 | -0.005 ± 0.003 | -0.001 ± 0.004 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| direct | 0.176 / 0.091 | 0.59 / 0.61 | 0.033 / 0.015 | 0.00 / 0.00 | 0.59 / 0.64 | 0.686 / 0.435 |
| careful | 0.282 / 0.097 | 0.12 / 0.14 | 0.041 / 0.013 | 0.00 / 0.00 | 0.05 / 0.09 | 0.070 / 0.029 |
| stamper | 0.035 / 0.000 | 0.00 / — | 0.000 / 0.000 | — / — | — / — | 1.181 / 1.725 |

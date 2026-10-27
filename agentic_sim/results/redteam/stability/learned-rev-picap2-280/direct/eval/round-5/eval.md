# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --pi0 0.40`, seeds 21-40, hide ``, model `None` (value off, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | non-initial share | non-initial stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 28252.8 ± 416.4 | 3566.6 ± 762.2 | 3601.2 | 0.695 | 0.290 | 0.015 | 0.227 | 0.246 | 0.176 | 0.611 | 35.50 | 119.05 | 0.10 |
| careful | 24686.1 ± 683.2 | nan ± nan | 4591.1 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.236 | 0.000 | 14.80 | 0.00 | 0.30 |
| stamper | 3083.4 ± 92.9 | -21602.7 ± 676.9 | 516.8 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.024 | 1.000 | 6.30 | 72.85 | 1.00 |

The stamp rate by seat kind (2.8.0 §5), plant / real, with the decisions pooled over the seeds in parentheses — under 2.7.0 a plant reached the initial review alone; under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| direct | 0.227 (16704) / 0.246 (42672) | 0.669 (1791) / 0.702 (8616) | 0.161 (703) / 0.237 (1537) | — / — |
| careful | 0.000 (19673) / 0.000 (50462) | 0.000 (1916) / 0.000 (14297) | 0.000 (806) / 0.000 (4667) | — / — |
| stamper | 1.000 (2782) / 1.000 (7300) | — / 1.000 (253) | — / — | — / — |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 0.902 | 0.940 | 0.514 (220) | 0.498 (229) | 0.568 (484) | 0.384 (22525) | 0.242 (48565) | 39.850 | 158.100 | 1.630 | 2.987 |
| careful | — | 0.428 | 0.000 (51909) | 0.000 (14197) | 0.000 (5187) | 0.000 (2774) | 0.000 (17754) | 25.250 | 198.450 | 1.369 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (10335) | 63.950 | 75.250 | 1.900 | 1.139 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| direct | 40.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.100 | 0.000 |
| careful | 40.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.300 | 0.000 |
| stamper | 40.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 16.750 / 40.000 | 35.500 ± 1.872 | +20.700 ± 2.260 | 152.400 | +114.050 ± 4.170 | 12.350 | 0.253 | 19.850 | +14.600 ± 0.591 | 1609.750 | 0.055 | +0.030 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 31123.413 ± 481.860 | -2496.743 ± 702.817 | 28252.8 ± 416.4 | +3566.6 ± 762.2 | 27.939 | -5.565 ± 0.477 | 23.538 ± 0.307 | -7.982 ± 0.922 | 22.291 | 0.082 | 1967.050 | 20.000 | 23.250 | +0.750 ± 0.354 | 69.061 | 53.500 |
| careful | 17.500 / 40.000 | 14.800 ± 0.934 | — | 38.350 | — | 13.400 | 0.048 | 5.250 | — | 861.300 | 0.025 | — | 0.000 / 0.000 (0.000 / 0.000) | 33620.156 ± 571.920 | — | 24686.1 ± 683.2 | — | 33.504 | — | 31.520 ± 1.009 | — | 22.646 | 0.003 | 2522.650 | 20.000 | 22.500 | — | 189.461 | 92.150 |
| stamper | 5.900 / 40.000 | 6.300 ± 0.471 | -8.500 ± 1.118 | 103.500 | +65.150 ± 2.376 | 0.000 | 1.000 | 43.950 | +38.700 ± 2.268 | 365.050 | 0.185 | +0.160 ± 0.005 | 0.000 / 0.000 (0.000 / 0.000) | 2288.506 ± 141.032 | -31331.650 ± 556.014 | 3083.4 ± 92.9 | -21602.7 ± 676.9 | 28.295 | -5.208 ± 0.598 | 28.555 ± 0.909 | -2.965 ± 1.291 | 18.065 | 0.375 | 250.750 | 20.000 | 34.100 | +11.600 ± 0.712 | 8412.983 | 95.000 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **direct**: p0 0.834/0.160/0.007 (200); p1 0.602/0.382/0.016 (212); p2 0.568/0.407/0.025 (231); p3 0.627/0.342/0.032 (242); p4 0.647/0.319/0.035 (238); p5 0.660/0.324/0.016 (229); p6 0.684/0.302/0.014 (214); p7 0.745/0.250/0.005 (211); p8 0.727/0.265/0.008 (204); p9 0.771/0.222/0.007 (196); p10 0.705/0.284/0.010 (208); p11 0.736/0.252/0.012 (205); p12 0.704/0.285/0.011 (207); p13 0.698/0.294/0.008 (217); p14 0.717/0.269/0.015 (217); p15 0.702/0.284/0.014 (215); p16 0.726/0.255/0.019 (136); p17 0.795/0.176/0.029 (19)
- **careful**: p0 1.000/0.000/0.000 (195); p1 1.000/0.000/0.000 (255); p2 1.000/0.000/0.000 (275); p3 1.000/0.000/0.000 (284); p4 1.000/0.000/0.000 (260); p5 1.000/0.000/0.000 (232); p6 1.000/0.000/0.000 (229); p7 1.000/0.000/0.000 (229); p8 1.000/0.000/0.000 (230); p9 1.000/0.000/0.000 (231); p10 1.000/0.000/0.000 (225); p11 1.000/0.000/0.000 (225); p12 1.000/0.000/0.000 (234); p13 1.000/0.000/0.000 (229); p14 1.000/0.000/0.000 (224); p15 1.000/0.000/0.000 (228); p16 1.000/0.000/0.000 (224); p17 1.000/0.000/0.000 (227); p18 1.000/0.000/0.000 (221); p19 1.000/0.000/0.000 (110); p20 1.000/0.000/0.000 (24)
- **stamper**: p0 0.000/1.000/0.000 (194); p1 0.000/1.000/0.000 (179); p2 0.000/1.000/0.000 (129); p3 0.000/1.000/0.000 (10); p4 0.000/1.000/0.000 (3); p5 0.000/1.000/0.000 (1); p6 0.000/1.000/0.000 (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 2133.6 / 835.2 | 2.08 / 2.13 | +0.05 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.06 / 0.04 | -0.02 ± 0.00 | 0.624 / 0.600 | -0.024 ± 0.003 | 0.403 / 0.390 | 0.082 / 0.089 | 0.239 / 0.238 | -0.001 ± 0.004 | 3.78 / 3.81 | +0.03 ± 0.04 |
| careful | 2523.1 / 983.6 | 0.40 / 0.36 | -0.04 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.15 / 0.14 | -0.01 ± 0.00 | 0.148 / 0.129 | -0.019 ± 0.003 | 0.083 / 0.074 | 0.003 / 0.004 | 0.104 / 0.100 | -0.005 ± 0.003 | 2.25 / 2.08 | -0.16 ± 0.05 |
| stamper | 365.0 / 139.1 | 0.87 / 0.80 | -0.07 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.08 / 0.04 | -0.03 ± 0.01 | 0.030 / 0.016 | -0.013 ± 0.007 | 0.016 / 0.010 | 0.309 / 0.279 | 0.053 / 0.053 | -0.000 ± 0.004 | 1.76 / 1.59 | -0.17 ± 0.09 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| direct | +0.05 ± 0.02 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.025 ± 0.003 | -0.014 ± 0.004 | -0.001 ± 0.004 |
| careful | -0.04 ± 0.02 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.019 ± 0.003 | -0.008 ± 0.002 | -0.004 ± 0.003 |
| stamper | -0.06 ± 0.03 | +0.00 ± 0.00 | -0.03 ± 0.00 | -0.011 ± 0.006 | -0.005 ± 0.003 | -0.001 ± 0.004 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| direct | 0.200 / 0.106 | 0.58 / 0.62 | 0.039 / 0.014 | 0.00 / 0.00 | 0.60 / 0.59 | 0.659 / 0.408 |
| careful | 0.282 / 0.097 | 0.12 / 0.14 | 0.041 / 0.013 | 0.00 / 0.00 | 0.05 / 0.09 | 0.070 / 0.029 |
| stamper | 0.035 / 0.000 | 0.00 / — | 0.000 / 0.000 | — / — | — / — | 1.181 / 1.725 |

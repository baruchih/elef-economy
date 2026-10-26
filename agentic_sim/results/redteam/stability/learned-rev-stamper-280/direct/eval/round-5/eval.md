# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule`, seeds 21-40, hide ``, model `None` (value off, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | non-initial share | non-initial stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 26425.7 ± 580.1 | -8743.5 ± 923.6 | 3235.2 | 0.661 | 0.327 | 0.012 | 0.271 | 0.289 | 0.116 | 0.750 | 36.75 | 158.30 | 0.15 |
| careful | 35169.1 ± 847.0 | nan ± nan | 4052.2 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.285 | 0.000 | 6.65 | 0.00 | 0.30 |
| stamper | 7002.0 ± 181.5 | -28167.1 ± 878.4 | 1063.8 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.021 | 1.000 | 14.20 | 182.10 | 1.00 |

The stamp rate by seat kind (2.8.0 §5), plant / real, with the decisions pooled over the seeds in parentheses — under 2.7.0 a plant reached the initial review alone; under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| direct | 0.271 (11747) / 0.289 (45427) | 0.811 (751) / 0.872 (5411) | 0.191 (309) / 0.246 (1059) | — / — |
| careful | 0.000 (5287) / 0.000 (52624) | 0.000 (642) / 0.000 (18617) | 0.000 (212) / 0.000 (3663) | — / — |
| stamper | 1.000 (3039) / 1.000 (17796) | — / 1.000 (440) | — / — | — / — |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 0.912 | 0.966 | 0.785 (792) | 0.735 (804) | 0.707 (908) | 0.409 (9475) | 0.293 (52725) | 43.050 | 344.200 | 1.649 | 3.677 |
| careful | — | 0.683 | 0.000 (25595) | 0.000 (5019) | 0.000 (4705) | 0.000 (979) | 0.000 (44747) | 24.950 | 697.400 | 1.149 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (21275) | 74.950 | 179.350 | 2.172 | 2.430 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| direct | 39.750 | 0.000 | 0.000 | 0.000 | 0.000 | 0.150 | 0.000 |
| careful | 39.700 | 0.000 | 0.000 | 0.000 | 0.000 | 0.300 | 0.000 |
| stamper | 40.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 17.350 / 39.750 | 36.750 ± 2.153 | +30.100 ± 2.391 | 124.500 | +114.300 ± 1.971 | 8.200 | 0.256 | 23.300 | +18.050 ± 0.829 | 1801.850 | 0.070 | +0.045 ± 0.002 | 0.000 / 0.000 (0.000 / 0.000) | 28077.563 ± 431.046 | +4761.026 ± 405.948 | 26425.7 ± 580.1 | -8743.5 ± 923.6 | 29.544 | -7.983 ± 0.358 | 23.106 ± 0.358 | +9.038 ± 0.530 | 21.455 | 0.048 | 2168.050 | 19.750 | 22.400 | +6.200 ± 0.468 | 70.971 | 116.350 |
| careful | 23.500 / 39.700 | 6.650 ± 0.568 | — | 10.200 | — | 3.300 | 0.054 | 5.250 | — | 1616.850 | 0.025 | — | 0.000 / 0.000 (0.000 / 0.000) | 23316.537 ± 373.976 | — | 35169.1 ± 847.0 | — | 37.527 | — | 14.069 ± 0.359 | — | 17.542 | 0.001 | 2634.850 | 19.700 | 16.200 | — | 949.449 | 211.850 |
| stamper | 3.850 / 40.000 | 14.200 ± 0.647 | +7.550 ± 0.872 | 113.550 | +103.350 ± 2.769 | 0.000 | 1.000 | 54.950 | +49.700 ± 2.549 | 889.800 | 0.192 | +0.166 ± 0.003 | 0.000 / 0.000 (0.000 / 0.000) | 9049.254 ± 151.120 | -14267.283 ± 352.384 | 7002.0 ± 181.5 | -28167.1 ± 878.4 | 26.601 | -10.926 ± 0.434 | 32.597 ± 0.855 | +18.528 ± 0.935 | 22.720 | 0.223 | 721.000 | 20.000 | 36.150 | +19.950 ± 0.972 | 5688.290 | 130.000 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **direct**: p0 0.851/0.148/0.001 (586); p1 0.506/0.485/0.008 (556); p2 0.548/0.445/0.007 (335); p3 0.660/0.326/0.014 (230); p4 0.568/0.402/0.030 (211); p5 0.625/0.355/0.019 (200); p6 0.700/0.284/0.016 (204); p7 0.689/0.295/0.016 (197); p8 0.704/0.285/0.011 (193); p9 0.713/0.274/0.013 (191); p10 0.719/0.259/0.022 (181); p11 0.638/0.343/0.019 (93); p12 0.622/0.350/0.029 (45); p13 0.579/0.404/0.018 (14)
- **careful**: p0 1.000/0.000/0.000 (594); p1 1.000/0.000/0.000 (705); p2 1.000/0.000/0.000 (830); p3 1.000/0.000/0.000 (911); p4 1.000/0.000/0.000 (773); p5 1.000/0.000/0.000 (239)
- **stamper**: p0 0.000/1.000/0.000 (561); p1 0.000/1.000/0.000 (305); p2 0.000/1.000/0.000 (170); p3 0.000/1.000/0.000 (24); p4 0.000/1.000/0.000 (3); p5 0.000/1.000/0.000 (1)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 2271.3 / 587.4 | 1.41 / 2.00 | +0.58 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.03 / 0.02 | -0.01 ± 0.00 | 0.497 / 0.607 | +0.109 ± 0.007 | 0.292 / 0.378 | 0.048 / 0.082 | 0.172 / 0.231 | +0.058 ± 0.006 | 3.25 / 3.60 | +0.36 ± 0.05 |
| careful | 2631.2 / 264.4 | 0.23 / 0.12 | -0.11 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.07 / 0.07 | +0.00 ± 0.00 | 0.162 / 0.128 | -0.034 ± 0.005 | 0.061 / 0.066 | 0.000 / 0.000 | 0.062 / 0.060 | -0.002 ± 0.004 | 1.48 / 1.24 | -0.24 ± 0.08 |
| stamper | 889.8 / 151.9 | 1.07 / 0.79 | -0.28 ± 0.04 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.03 / 0.02 | -0.01 ± 0.00 | 0.229 / 0.217 | -0.012 ± 0.008 | 0.128 / 0.128 | 0.189 / 0.270 | 0.098 / 0.068 | -0.030 ± 0.006 | 3.38 / 2.26 | -1.13 ± 0.27 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| direct | +0.07 ± 0.02 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.048 ± 0.004 | -0.024 ± 0.004 | +0.013 ± 0.005 |
| careful | -0.11 ± 0.02 | +0.00 ± 0.00 | +0.00 ± 0.00 | -0.037 ± 0.005 | +0.004 ± 0.003 | -0.002 ± 0.004 |
| stamper | -0.80 ± 0.04 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.163 ± 0.012 | -0.110 ± 0.009 | -0.041 ± 0.007 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| direct | 0.118 / 0.063 | 0.59 / 0.63 | 0.033 / 0.014 | 0.00 / 0.00 | 0.54 / 0.62 | 0.799 / 0.547 |
| careful | 0.351 / 0.120 | 0.36 / 0.42 | 0.040 / 0.012 | 0.00 / 0.00 | 0.29 / 0.39 | 0.313 / 0.130 |
| stamper | 0.025 / 0.000 | 0.00 / — | 0.000 / 0.000 | — / — | — / — | 1.196 / 1.717 |

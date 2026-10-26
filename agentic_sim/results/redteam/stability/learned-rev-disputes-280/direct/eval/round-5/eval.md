# Evaluation — cell `--entry-pool 20 --stampers 0.6 --dispute-policy truthful --learner-pop all --learner-role reviewer --learner-exit rule`, seeds 21-40, hide ``, model `None` (value off, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | non-initial share | non-initial stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 30018.0 ± 845.0 | -5973.0 ± 978.8 | 4237.6 | 0.562 | 0.385 | 0.053 | 0.285 | 0.289 | 0.306 | 0.783 | 11.95 | 144.05 | 0.05 |
| careful | 35991.0 ± 777.8 | nan ± nan | 4133.4 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.296 | 0.000 | 0.55 | 0.00 | 0.20 |
| stamper | 7029.9 ± 149.7 | -28961.1 ± 829.4 | 1086.0 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.026 | 1.000 | 8.70 | 192.80 | 1.00 |

The stamp rate by seat kind (2.8.0 §5), plant / real, with the decisions pooled over the seeds in parentheses — under 2.7.0 a plant reached the initial review alone; under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| direct | 0.285 (11733) / 0.289 (47063) | 0.860 (1604) / 0.852 (16755) | 0.617 (2866) / 0.614 (4731) | — / — |
| careful | 0.000 (5468) / 0.000 (52713) | 0.000 (602) / 0.000 (19391) | 0.000 (370) / 0.000 (4125) | — / — |
| stamper | 1.000 (3068) / 1.000 (18080) | — / 1.000 (375) | — / 1.000 (196) | — / — |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 0.854 | 0.941 | 0.751 (2014) | 0.713 (2025) | 0.576 (1008) | 0.545 (22904) | 0.295 (56801) | 39.950 | 403.600 | 1.395 | 3.606 |
| careful | — | 0.679 | 0.000 (25262) | 0.000 (6701) | 0.000 (4757) | 0.000 (1631) | 0.000 (44318) | 24.950 | 677.050 | 1.148 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (21719) | 76.600 | 180.650 | 2.118 | 2.517 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| direct | 39.800 | 0.000 | 0.000 | 0.000 | 0.000 | 0.050 | 0.000 |
| careful | 39.600 | 0.000 | 0.000 | 0.000 | 0.000 | 0.200 | 0.000 |
| stamper | 40.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 18.750 / 39.800 | 11.950 ± 0.872 | +11.400 ± 0.850 | 121.300 | +110.600 ± 4.495 | 10.650 | 0.352 | 20.150 | +14.800 ± 0.773 | 1693.950 | 0.009 | -0.004 ± 0.001 | 133.150 / 125.200 (133.150 / 125.200) | 31577.070 ± 473.203 | +8207.955 ± 555.011 | 30018.0 ± 845.0 | -5973.0 ± 978.8 | 30.778 | -6.948 ± 0.484 | 22.817 ± 0.657 | +9.105 ± 0.671 | 21.728 | 0.027 | 2303.350 | 19.800 | 21.050 | +4.100 ± 0.619 | 68.960 | 175.950 |
| careful | 22.650 / 39.600 | 0.550 ± 0.170 | — | 10.700 | — | 3.300 | 0.054 | 5.350 | — | 1591.500 | 0.013 | — | 25.750 / 25.150 (25.750 / 25.150) | 23369.114 ± 278.692 | — | 35991.0 ± 777.8 | — | 37.726 | — | 13.712 ± 0.314 | — | 17.430 | 0.001 | 2639.350 | 19.600 | 16.950 | — | 955.090 | 220.900 |
| stamper | 4.250 / 40.000 | 8.700 ± 0.585 | +8.150 ± 0.608 | 114.600 | +103.900 ± 1.987 | 0.000 | 1.000 | 56.600 | +51.250 ± 2.194 | 725.700 | 0.017 | +0.004 ± 0.001 | 178.550 / 170.050 (178.550 / 170.050) | 8356.862 ± 105.916 | -15012.252 ± 298.788 | 7029.9 ± 149.7 | -28961.1 ± 829.4 | 27.277 | -10.449 ± 0.391 | 30.331 ± 0.752 | +16.619 ± 0.866 | 22.470 | 0.248 | 708.100 | 20.000 | 35.750 | +18.800 ± 0.887 | 5752.771 | 182.750 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **direct**: p0 0.879/0.117/0.004 (601); p1 0.516/0.435/0.048 (644); p2 0.517/0.460/0.024 (392); p3 0.512/0.425/0.063 (314); p4 0.478/0.446/0.077 (302); p5 0.514/0.405/0.082 (295); p6 0.528/0.402/0.070 (294); p7 0.502/0.426/0.072 (298); p8 0.499/0.436/0.065 (292); p9 0.474/0.455/0.070 (285); p10 0.501/0.423/0.076 (263); p11 0.518/0.422/0.060 (183); p12 0.548/0.393/0.060 (74)
- **careful**: p0 1.000/0.000/0.000 (599); p1 1.000/0.000/0.000 (752); p2 1.000/0.000/0.000 (840); p3 1.000/0.000/0.000 (871); p4 1.000/0.000/0.000 (738); p5 1.000/0.000/0.000 (294); p6 1.000/0.000/0.000 (40)
- **stamper**: p0 0.000/1.000/0.000 (580); p1 0.000/1.000/0.000 (306); p2 0.000/1.000/0.000 (173); p3 0.000/1.000/0.000 (19); p4 0.000/1.000/0.000 (6); p5 0.000/1.000/0.000 (2)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 2353.2 / 586.6 | 1.20 / 1.54 | +0.34 ± 0.05 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.07 / 0.06 | -0.00 ± 0.00 | 0.473 / 0.547 | +0.075 ± 0.009 | 0.252 / 0.310 | 0.026 / 0.038 | 0.139 / 0.172 | +0.034 ± 0.005 | 2.96 / 3.19 | +0.23 ± 0.06 |
| careful | 2635.7 / 273.4 | 0.23 / 0.15 | -0.08 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.07 / 0.07 | +0.00 ± 0.00 | 0.155 / 0.130 | -0.025 ± 0.006 | 0.054 / 0.058 | 0.001 / 0.001 | 0.062 / 0.063 | +0.001 ± 0.003 | 1.52 / 1.33 | -0.19 ± 0.06 |
| stamper | 904.0 / 153.4 | 1.17 / 0.82 | -0.35 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.04 / 0.02 | -0.01 ± 0.00 | 0.268 / 0.270 | +0.002 ± 0.010 | 0.147 / 0.153 | 0.216 / 0.311 | 0.108 / 0.076 | -0.032 ± 0.004 | 3.52 / 2.18 | -1.35 ± 0.18 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| direct | +0.01 ± 0.02 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.052 ± 0.005 | -0.024 ± 0.006 | +0.006 ± 0.003 |
| careful | -0.07 ± 0.01 | +0.00 ± 0.00 | +0.00 ± 0.00 | -0.022 ± 0.004 | +0.005 ± 0.003 | +0.001 ± 0.003 |
| stamper | -0.84 ± 0.04 | +0.00 ± 0.00 | -0.03 ± 0.00 | -0.156 ± 0.015 | -0.109 ± 0.011 | -0.036 ± 0.004 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| direct | 0.352 / 0.135 | 0.44 / 0.41 | 0.103 / 0.224 | 0.00 / 0.00 | 0.45 / 0.42 | 0.495 / 0.293 |
| careful | 0.366 / 0.109 | 0.37 / 0.39 | 0.050 / 0.049 | 0.00 / 0.00 | 0.28 / 0.30 | 0.291 / 0.122 |
| stamper | 0.021 / 0.000 | 0.02 / — | 0.197 / 0.747 | 0.00 / 0.00 | 0.00 / — | 1.209 / 1.760 |

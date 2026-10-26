# Evaluation — cell `--entry-pool 20 --stampers 0.6 --dispute-policy truthful --learner-pop all --learner-role reviewer --learner-exit rule`, seeds 21-40, hide ``, model `None` (value off, horizon 8)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | non-initial share | non-initial stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 29402.4 ± 555.5 | -6588.6 ± 928.9 | 4425.2 | 0.553 | 0.394 | 0.053 | 0.256 | 0.273 | 0.332 | 0.812 | 11.20 | 144.90 | 0.25 |
| careful | 35991.0 ± 777.8 | nan ± nan | 4133.4 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.296 | 0.000 | 0.55 | 0.00 | 0.20 |
| stamper | 7029.9 ± 149.7 | -28961.1 ± 829.4 | 1086.0 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.026 | 1.000 | 8.70 | 192.80 | 1.00 |
| hand | 31127.8 ± 741.3 | -4863.1 ± 934.0 | 4442.9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.306 | 0.000 | 3.95 | 0.00 | 0.60 |

The stamp rate by seat kind (2.8.0 §5), plant / real, with the decisions pooled over the seeds in parentheses — under 2.7.0 a plant reached the initial review alone; under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| direct | 0.256 (12069) / 0.273 (47069) | 0.891 (1919) / 0.874 (18903) | 0.649 (3259) / 0.663 (5286) | — / — |
| careful | 0.000 (5468) / 0.000 (52713) | 0.000 (602) / 0.000 (19391) | 0.000 (370) / 0.000 (4125) | — / — |
| stamper | 1.000 (3068) / 1.000 (18080) | — / 1.000 (375) | — / 1.000 (196) | — / — |
| hand | 0.000 (12315) / 0.000 (49365) | 0.000 (1805) / 0.000 (19577) | 0.000 (1261) / 0.000 (4534) | — / — |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 0.855 | 0.934 | 0.733 (1791) | 0.648 (2122) | 0.581 (1416) | 0.536 (26269) | 0.306 (56907) | 39.200 | 378.000 | 1.415 | 3.696 |
| careful | — | 0.679 | 0.000 (25262) | 0.000 (6701) | 0.000 (4757) | 0.000 (1631) | 0.000 (44318) | 24.950 | 677.050 | 1.148 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (21719) | 76.600 | 180.650 | 2.118 | 2.517 |
| hand | — | 0.806 | 0.000 (5) | 0.000 (11770) | 0.000 (18886) | 0.000 (13761) | 0.000 (44435) | 35.100 | 340.250 | 1.442 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| direct | 39.800 | 0.000 | 0.000 | 0.000 | 0.000 | 0.250 | 0.000 |
| careful | 39.600 | 0.000 | 0.000 | 0.000 | 0.000 | 0.200 | 0.000 |
| stamper | 40.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| hand | 39.850 | 0.000 | 0.000 | 0.000 | 0.000 | 0.600 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 18.100 / 39.800 | 11.200 ± 0.839 | +10.650 ± 0.825 | 121.800 | +111.100 ± 3.961 | 8.500 | 0.345 | 19.400 | +14.050 ± 0.966 | 1694.600 | 0.007 | -0.006 ± 0.001 | 135.300 / 129.100 (135.300 / 129.100) | 32416.096 ± 449.306 | +9046.982 ± 483.980 | 29402.4 ± 555.5 | -6588.6 ± 928.9 | 30.731 | -6.994 ± 0.454 | 23.945 ± 0.493 | +10.234 ± 0.660 | 21.793 | 0.024 | 2310.100 | 19.800 | 21.700 | +4.750 ± 0.676 | 69.456 | 174.500 |
| careful | 22.650 / 39.600 | 0.550 ± 0.170 | — | 10.700 | — | 3.300 | 0.054 | 5.350 | — | 1591.500 | 0.013 | — | 25.750 / 25.150 (25.750 / 25.150) | 23369.114 ± 278.692 | — | 35991.0 ± 777.8 | — | 37.726 | — | 13.712 ± 0.314 | — | 17.430 | 0.001 | 2639.350 | 19.600 | 16.950 | — | 955.090 | 220.900 |
| stamper | 4.250 / 40.000 | 8.700 ± 0.585 | +8.150 ± 0.608 | 114.600 | +103.900 ± 1.987 | 0.000 | 1.000 | 56.600 | +51.250 ± 2.194 | 725.700 | 0.017 | +0.004 ± 0.001 | 178.550 / 170.050 (178.550 / 170.050) | 8356.862 ± 105.916 | -15012.252 ± 298.788 | 7029.9 ± 149.7 | -28961.1 ± 829.4 | 27.277 | -10.449 ± 0.391 | 30.331 ± 0.752 | +16.619 ± 0.866 | 22.470 | 0.248 | 708.100 | 20.000 | 35.750 | +18.800 ± 0.887 | 5752.771 | 182.750 |
| hand | 20.150 / 39.850 | 3.950 ± 0.420 | +3.400 ± 0.489 | 64.450 | +53.750 ± 1.640 | 6.600 | 0.051 | 15.250 | +9.900 ± 0.788 | 1566.450 | 0.013 | +0.000 ± 0.001 | 97.550 / 93.550 (97.550 / 93.550) | 28989.796 ± 350.301 | +5620.682 ± 445.223 | 31127.8 ± 741.3 | -4863.1 ± 934.0 | 32.427 | -5.299 ± 0.443 | 20.305 ± 0.551 | +6.593 ± 0.634 | 19.781 | 0.031 | 2402.750 | 19.850 | 19.700 | +2.750 ± 0.507 | 151.980 | 228.550 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **direct**: p0 0.836/0.150/0.014 (612); p1 0.553/0.419/0.029 (602); p2 0.541/0.422/0.038 (416); p3 0.546/0.404/0.051 (308); p4 0.542/0.394/0.064 (308); p5 0.484/0.437/0.080 (314); p6 0.492/0.434/0.074 (303); p7 0.479/0.450/0.072 (308); p8 0.461/0.460/0.079 (311); p9 0.477/0.451/0.072 (293); p10 0.466/0.464/0.069 (273); p11 0.446/0.485/0.069 (176); p12 0.463/0.455/0.082 (128); p13 0.483/0.439/0.078 (51); p14 0.501/0.423/0.076 (19); p15 0.385/0.564/0.051 (2)
- **careful**: p0 1.000/0.000/0.000 (599); p1 1.000/0.000/0.000 (752); p2 1.000/0.000/0.000 (840); p3 1.000/0.000/0.000 (871); p4 1.000/0.000/0.000 (738); p5 1.000/0.000/0.000 (294); p6 1.000/0.000/0.000 (40)
- **stamper**: p0 0.000/1.000/0.000 (580); p1 0.000/1.000/0.000 (306); p2 0.000/1.000/0.000 (173); p3 0.000/1.000/0.000 (19); p4 0.000/1.000/0.000 (6); p5 0.000/1.000/0.000 (2)
- **hand**: p0 —/—/— (0); p1 —/—/— (0); p2 —/—/— (0); p3 —/—/— (0); p4 —/—/— (0); p5 —/—/— (0); p6 —/—/— (0); p7 —/—/— (0); p8 —/—/— (0); p9 —/—/— (0); p10 —/—/— (0); p11 —/—/— (0); p12 —/—/— (0); p13 —/—/— (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 2353.4 / 603.5 | 1.20 / 1.53 | +0.33 ± 0.04 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.08 / 0.08 | +0.00 ± 0.00 | 0.456 / 0.525 | +0.069 ± 0.012 | 0.236 / 0.296 | 0.023 / 0.036 | 0.142 / 0.178 | +0.037 ± 0.005 | 2.99 / 3.22 | +0.23 ± 0.05 |
| careful | 2635.7 / 273.4 | 0.23 / 0.15 | -0.08 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.07 / 0.07 | +0.00 ± 0.00 | 0.155 / 0.130 | -0.025 ± 0.006 | 0.054 / 0.058 | 0.001 / 0.001 | 0.062 / 0.063 | +0.001 ± 0.003 | 1.52 / 1.33 | -0.19 ± 0.06 |
| stamper | 904.0 / 153.4 | 1.17 / 0.82 | -0.35 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.04 / 0.02 | -0.01 ± 0.00 | 0.268 / 0.270 | +0.002 ± 0.010 | 0.147 / 0.153 | 0.216 / 0.311 | 0.108 / 0.076 | -0.032 ± 0.004 | 3.52 / 2.18 | -1.35 ± 0.18 |
| hand | 2468.2 / 615.8 | 0.74 / 0.75 | +0.01 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.13 / 0.13 | +0.00 ± 0.00 | 0.320 / 0.324 | +0.004 ± 0.007 | 0.141 / 0.166 | 0.031 / 0.035 | 0.095 / 0.088 | -0.007 ± 0.003 | 2.54 / 2.48 | -0.07 ± 0.09 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| direct | -0.02 ± 0.02 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.050 ± 0.003 | -0.017 ± 0.005 | +0.004 ± 0.003 |
| careful | -0.07 ± 0.01 | +0.00 ± 0.00 | +0.00 ± 0.00 | -0.022 ± 0.004 | +0.005 ± 0.003 | +0.001 ± 0.003 |
| stamper | -0.84 ± 0.04 | +0.00 ± 0.00 | -0.03 ± 0.00 | -0.156 ± 0.015 | -0.109 ± 0.011 | -0.036 ± 0.004 |
| hand | -0.09 ± 0.02 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.045 ± 0.005 | -0.007 ± 0.003 | -0.008 ± 0.003 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| direct | 0.394 / 0.154 | 0.40 / 0.37 | 0.099 / 0.216 | 0.00 / 0.00 | 0.40 / 0.35 | 0.431 / 0.233 |
| careful | 0.366 / 0.109 | 0.37 / 0.39 | 0.050 / 0.049 | 0.00 / 0.00 | 0.28 / 0.30 | 0.291 / 0.122 |
| stamper | 0.021 / 0.000 | 0.02 / — | 0.197 / 0.747 | 0.00 / 0.00 | 0.00 / — | 1.209 / 1.760 |
| hand | 0.391 / 0.144 | 0.10 / 0.10 | 0.072 / 0.116 | 0.00 / 0.00 | 0.10 / 0.22 | 0.329 / 0.195 |

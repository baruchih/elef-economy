# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule`, seeds 21-40, hide ``, model `None` (value off, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | non-initial share | non-initial stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 27932.7 ± 449.1 | -7677.3 ± 723.2 | 3389.6 | 0.701 | 0.294 | 0.004 | 0.212 | 0.247 | 0.135 | 0.679 | 33.75 | 139.40 | 0.10 |
| careful | 35610.0 ± 690.2 | nan ± nan | 4142.1 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.300 | 0.000 | 6.10 | 0.00 | 0.30 |
| stamper | 7201.6 ± 143.3 | -28408.4 ± 730.6 | 1082.3 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.020 | 1.000 | 15.40 | 180.80 | 1.00 |

The stamp rate by seat kind (2.8.0 §5), plant / real, with the decisions pooled over the seeds in parentheses — under 2.7.0 a plant reached the initial review alone; under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| direct | 0.212 (12146) / 0.247 (46486) | 0.720 (1085) / 0.797 (6309) | 0.217 (626) / 0.238 (1139) | — / — |
| careful | 0.000 (5358) / 0.000 (52610) | 0.000 (945) / 0.000 (18926) | 0.000 (1365) / 0.000 (3638) | — / — |
| stamper | 1.000 (3123) / 1.000 (18084) | — / 1.000 (440) | — / — | — / — |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 0.916 | 0.958 | 0.778 (531) | 0.767 (437) | 0.717 (749) | 0.346 (13610) | 0.267 (52464) | 41.350 | 343.800 | 1.560 | 3.371 |
| careful | — | 0.683 | 0.000 (25992) | 0.000 (5627) | 0.000 (4615) | 0.000 (1110) | 0.000 (45498) | 25.300 | 722.750 | 1.157 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (21647) | 79.450 | 181.000 | 2.161 | 2.276 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| direct | 39.900 | 0.000 | 0.000 | 0.000 | 0.000 | 0.100 | 0.000 |
| careful | 39.650 | 0.000 | 0.000 | 0.000 | 0.000 | 0.300 | 0.000 |
| stamper | 40.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 18.750 / 39.900 | 33.750 ± 2.043 | +27.650 ± 2.079 | 111.400 | +100.950 ± 2.751 | 7.400 | 0.195 | 21.450 | +15.800 ± 0.780 | 1828.200 | 0.065 | +0.040 ± 0.002 | 0.000 / 0.000 (0.000 / 0.000) | 28296.846 ± 394.655 | +4578.033 ± 387.273 | 27932.7 ± 449.1 | -7677.3 ± 723.2 | 30.302 | -7.065 ± 0.448 | 21.867 ± 0.305 | +7.692 ± 0.479 | 20.902 | 0.018 | 2287.500 | 19.900 | 21.150 | +4.650 ± 0.372 | 65.944 | 97.250 |
| careful | 23.150 / 39.650 | 6.100 ± 0.355 | — | 10.450 | — | 3.400 | 0.055 | 5.650 | — | 1630.350 | 0.024 | — | 0.000 / 0.000 (0.000 / 0.000) | 23718.813 ± 303.512 | — | 35610.0 ± 690.2 | — | 37.367 | — | 14.175 ± 0.294 | — | 17.614 | 0.001 | 2633.550 | 19.650 | 16.500 | — | 903.473 | 232.300 |
| stamper | 2.900 / 40.000 | 15.400 ± 0.890 | +9.300 ± 0.924 | 118.450 | +108.000 ± 1.989 | 0.000 | 1.000 | 59.450 | +53.800 ± 1.773 | 904.200 | 0.187 | +0.162 ± 0.003 | 0.000 / 0.000 (0.000 / 0.000) | 9117.372 ± 129.526 | -14601.441 ± 268.742 | 7201.6 ± 143.3 | -28408.4 ± 730.6 | 26.578 | -10.788 ± 0.365 | 31.736 ± 0.665 | +17.561 ± 0.828 | 22.601 | 0.236 | 720.600 | 20.000 | 37.100 | +20.600 ± 0.525 | 5594.089 | 108.100 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **direct**: p0 0.842/0.158/0.000 (593); p1 0.509/0.484/0.007 (524); p2 0.600/0.396/0.004 (314); p3 0.721/0.275/0.004 (234); p4 0.706/0.291/0.003 (231); p5 0.667/0.329/0.005 (221); p6 0.698/0.299/0.003 (210); p7 0.717/0.279/0.004 (209); p8 0.751/0.246/0.003 (206); p9 0.770/0.228/0.002 (207); p10 0.777/0.218/0.005 (203); p11 0.751/0.237/0.012 (148); p12 0.670/0.320/0.010 (60); p13 0.749/0.249/0.002 (23); p14 0.887/0.113/0.000 (4)
- **careful**: p0 1.000/0.000/0.000 (590); p1 1.000/0.000/0.000 (737); p2 1.000/0.000/0.000 (863); p3 1.000/0.000/0.000 (903); p4 1.000/0.000/0.000 (771); p5 1.000/0.000/0.000 (264); p6 1.000/0.000/0.000 (14)
- **stamper**: p0 0.000/1.000/0.000 (562); p1 0.000/1.000/0.000 (304); p2 0.000/1.000/0.000 (182); p3 0.000/1.000/0.000 (30); p4 0.000/1.000/0.000 (3); p5 0.000/1.000/0.000 (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 2324.3 / 607.3 | 1.20 / 1.61 | +0.41 ± 0.04 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.04 / 0.02 | -0.01 ± 0.00 | 0.483 / 0.566 | +0.083 ± 0.008 | 0.266 / 0.332 | 0.018 / 0.000 | 0.158 / 0.197 | +0.038 ± 0.005 | 2.95 / 3.16 | +0.22 ± 0.05 |
| careful | 2630.5 / 267.9 | 0.23 / 0.14 | -0.09 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.06 / 0.07 | +0.00 ± 0.00 | 0.156 / 0.127 | -0.029 ± 0.005 | 0.055 / 0.063 | 0.001 / 0.000 | 0.062 / 0.062 | +0.000 ± 0.003 | 1.51 / 1.17 | -0.34 ± 0.09 |
| stamper | 904.2 / 156.2 | 1.06 / 0.79 | -0.26 ± 0.04 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.04 / 0.03 | -0.01 ± 0.00 | 0.236 / 0.238 | +0.002 ± 0.008 | 0.142 / 0.157 | 0.203 / 0.000 | 0.094 / 0.077 | -0.017 ± 0.006 | 3.35 / 2.14 | -1.21 ± 0.18 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| direct | +0.04 ± 0.02 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.052 ± 0.004 | -0.022 ± 0.004 | +0.006 ± 0.004 |
| careful | -0.08 ± 0.02 | +0.00 ± 0.00 | +0.00 ± 0.00 | -0.025 ± 0.005 | +0.009 ± 0.003 | +0.000 ± 0.003 |
| stamper | -0.77 ± 0.04 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.151 ± 0.012 | -0.100 ± 0.010 | -0.023 ± 0.006 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| direct | 0.133 / 0.080 | 0.61 / 0.64 | 0.032 / 0.086 | 0.00 / 0.00 | 0.62 / 0.64 | 0.766 / 0.567 |
| careful | 0.357 / 0.106 | 0.38 / 0.42 | 0.038 / 0.158 | 0.00 / 0.00 | 0.29 / 0.31 | 0.308 / 0.256 |
| stamper | 0.024 / 0.000 | 0.00 / — | 0.000 / 0.028 | — / 0.00 | — / — | 1.194 / 1.757 |

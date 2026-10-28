# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop half --learner-role reviewer --learner-exit rule`, seeds 21-40, hide ``, model `results/redteam/stability/learned-rev-half-290/wm/models/wm-online-10.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | non-initial share | non-initial stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 14917.1 ± 490.3 | -4243.1 ± 758.0 | 2029.8 | 0.817 | 0.183 | 0.000 | 0.071 | 0.068 | 0.274 | 0.491 | 16.00 | 24.40 | 0.10 |
| careful | 19160.2 ± 696.7 | nan ± nan | 2684.3 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.331 | 0.000 | 9.65 | 0.00 | 0.20 |
| stamper | 3827.8 ± 104.6 | -15332.4 ± 689.9 | 522.6 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.022 | 1.000 | 13.65 | 90.20 | 1.00 |

The stamp rate by seat kind (2.8.0 §5), plant / real, with the decisions pooled over the seeds in parentheses — under 2.7.0 a plant reached the initial review alone; under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| greedy | 0.071 (6147) / 0.068 (23310) | 0.594 (1125) / 0.612 (7756) | 0.026 (944) / 0.024 (1314) | — / — |
| careful | 0.000 (6457) / 0.000 (29437) | 0.000 (1311) / 0.000 (12477) | 0.000 (1444) / 0.000 (2560) | — / — |
| stamper | 1.000 (1435) / 1.000 (8782) | — / 1.000 (217) | — / 1.000 (18) | — / — |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 0.823 | 0.848 | 0.652 (66) | 0.210 (2119) | 0.188 (7701) | 0.228 (9142) | 0.161 (21568) | 20.100 | 140.200 | 2.945 | 1.214 |
| careful | — | 0.732 | 0.000 (672) | 0.000 (14272) | 0.000 (10247) | 0.000 (6255) | 0.000 (22240) | 12.100 | 211.900 | 2.286 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (10452) | 34.250 | 93.400 | 4.430 | 2.634 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| greedy | 20.300 | 0.000 | 0.000 | 0.000 | 0.000 | 0.100 | 0.000 |
| careful | 20.350 | 0.000 | 0.000 | 0.000 | 0.000 | 0.200 | 0.000 |
| stamper | 20.450 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 8.700 / 20.300 | 16.000 ± 1.124 | +6.350 ± 1.418 | 59.900 | +21.300 ± 2.292 | 6.600 | 0.044 | 17.400 | +8.900 ± 0.636 | 1630.900 | 0.045 | -0.001 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 15102.895 ± 536.544 | -1717.357 ± 481.803 | 14917.1 ± 490.3 | -4243.1 ± 758.0 | 31.114 | -3.908 ± 0.424 | 21.862 ± 0.353 | +2.213 ± 0.741 | 20.696 | 0.013 | 2365.550 | 19.750 | 20.700 | +1.450 ± 0.285 | 68.041 | 136.450 |
| careful | 12.700 / 20.350 | 9.650 ± 0.789 | — | 38.600 | — | 5.450 | 0.057 | 8.500 | — | 1577.850 | 0.046 | — | 0.000 / 0.000 (0.000 / 0.000) | 16820.252 ± 543.852 | — | 19160.2 ± 696.7 | — | 35.022 | — | 19.649 ± 0.781 | — | 18.475 | 0.002 | 2566.150 | 19.750 | 19.250 | — | 471.556 | 143.450 |
| stamper | 0.000 / 20.450 | 13.650 ± 0.883 | +4.000 ± 1.129 | 92.950 | +54.350 ± 2.256 | 4.700 | 0.040 | 32.500 | +24.000 ± 1.044 | 1554.050 | 0.091 | +0.046 ± 0.002 | 0.000 / 0.000 (0.000 / 0.000) | 3590.234 ± 112.689 | -13230.017 ± 528.376 | 3827.8 ± 104.6 | -15332.4 ± 689.9 | 27.935 | -7.087 ± 0.407 | 28.458 ± 0.383 | +8.808 ± 0.952 | 23.947 | 0.320 | 1455.350 | 20.000 | 29.000 | +9.750 ± 0.428 | 77.792 | 161.350 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **greedy**: p0 0.921/0.079/0.000 (288); p1 0.741/0.259/0.000 (199); p2 0.654/0.346/0.000 (107); p3 0.774/0.226/0.000 (124); p4 0.770/0.230/0.000 (143); p5 0.800/0.200/0.000 (146); p6 0.802/0.198/0.000 (151); p7 0.805/0.195/0.000 (143); p8 0.799/0.201/0.000 (160); p9 0.830/0.170/0.000 (159); p10 0.835/0.165/0.000 (171); p11 0.881/0.119/0.000 (142); p12 0.884/0.115/0.001 (82); p13 0.885/0.115/0.000 (14)
- **careful**: p0 1.000/0.000/0.000 (287); p1 1.000/0.000/0.000 (234); p2 1.000/0.000/0.000 (207); p3 1.000/0.000/0.000 (210); p4 1.000/0.000/0.000 (233); p5 1.000/0.000/0.000 (238); p6 1.000/0.000/0.000 (250); p7 1.000/0.000/0.000 (243); p8 1.000/0.000/0.000 (246); p9 1.000/0.000/0.000 (234); p10 1.000/0.000/0.000 (175); p11 1.000/0.000/0.000 (111); p12 1.000/0.000/0.000 (18)
- **stamper**: p0 0.000/1.000/0.000 (290); p1 0.000/1.000/0.000 (142); p2 0.000/1.000/0.000 (62); p3 0.000/1.000/0.000 (23); p4 0.000/1.000/0.000 (4); p5 0.000/1.000/0.000 (1)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 2378.9 / 622.8 | 1.06 / 1.21 | +0.15 ± 0.05 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.14 / 0.13 | -0.01 ± 0.00 | 0.439 / 0.465 | +0.027 ± 0.011 | 0.212 / 0.247 | 0.012 / 0.000 | 0.073 / 0.077 | +0.004 ± 0.003 | 2.87 / 2.99 | +0.13 ± 0.08 |
| careful | 2564.6 / 545.7 | 0.31 / 0.26 | -0.05 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.14 / 0.14 | +0.01 ± 0.00 | 0.163 / 0.153 | -0.010 ± 0.004 | 0.073 / 0.084 | 0.002 / 0.000 | 0.042 / 0.044 | +0.002 ± 0.002 | 1.73 / 1.55 | -0.18 ± 0.06 |
| stamper | 2101.3 / 538.9 | 1.99 / 2.20 | +0.21 ± 0.04 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.11 / 0.14 | +0.02 ± 0.00 | 0.556 / 0.620 | +0.064 ± 0.005 | 0.343 / 0.387 | 0.315 / 0.000 | 0.023 / 0.015 | -0.009 ± 0.002 | 3.22 / 2.94 | -0.28 ± 0.28 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| greedy | -0.02 ± 0.02 | +0.00 ± 0.00 | -0.03 ± 0.00 | -0.052 ± 0.005 | -0.012 ± 0.004 | -0.004 ± 0.003 |
| careful | -0.08 ± 0.02 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.034 ± 0.004 | -0.004 ± 0.002 | +0.002 ± 0.002 |
| stamper | -0.16 ± 0.03 | +0.00 ± 0.00 | +0.00 ± 0.00 | -0.054 ± 0.003 | -0.035 ± 0.005 | -0.005 ± 0.001 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| greedy | 0.421 / 0.188 | 0.18 / 0.20 | 0.035 / 0.086 | 0.00 / 0.00 | 0.15 / 0.15 | 0.312 / 0.177 |
| careful | 0.394 / 0.160 | 0.14 / 0.14 | 0.037 / 0.099 | 0.00 / 0.00 | 0.09 / 0.10 | 0.263 / 0.161 |
| stamper | 0.377 / 0.185 | 0.17 / 0.18 | 0.017 / 0.070 | 0.00 / 0.00 | 0.14 / 0.16 | 0.423 / 0.335 |

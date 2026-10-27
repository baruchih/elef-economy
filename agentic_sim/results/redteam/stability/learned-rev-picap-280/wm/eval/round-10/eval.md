# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --dial off --pi0 0.40`, seeds 21-40, hide ``, model `results/redteam/stability/learned-rev-picap-280/wm/models/wm-online-10.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | non-initial share | non-initial stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 20428.6 ± 300.8 | -3722.3 ± 857.0 | 3038.9 | 0.616 | 0.384 | 0.000 | 0.336 | 0.364 | 0.072 | 0.744 | 100.20 | 164.90 | 0.25 |
| careful | 24150.9 ± 731.9 | nan ± nan | 4587.1 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.229 | 0.000 | 14.55 | 0.00 | 0.45 |
| stamper | 2433.1 ± 84.8 | -21717.8 ± 720.2 | 498.4 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.025 | 1.000 | 6.20 | 73.60 | 1.00 |

The stamp rate by seat kind (2.8.0 §5), plant / real, with the decisions pooled over the seeds in parentheses — under 2.7.0 a plant reached the initial review alone; under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| greedy | 0.336 (15860) / 0.364 (40556) | 0.903 (569) / 0.872 (2978) | 0.128 (297) / 0.185 (518) | — / — |
| careful | 0.000 (19859) / 0.000 (50907) | 0.000 (1873) / 0.000 (13784) | 0.000 (758) / 0.000 (4562) | — / — |
| stamper | 1.000 (2685) / 1.000 (7030) | — / 1.000 (253) | — / — | — / — |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 0.456 | 0.668 | 0.611 (17038) | 0.391 (9962) | 0.428 (9822) | 0.067 (4418) | 0.230 (19538) | 46.650 | 107.900 | 3.966 | 3.535 |
| careful | — | 0.410 | 0.000 (54931) | 0.000 (12533) | 0.000 (4546) | 0.000 (2600) | 0.000 (17133) | 24.600 | 203.650 | 1.541 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (9968) | 61.350 | 76.700 | 1.889 | 1.200 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| greedy | 40.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.250 | 0.000 |
| careful | 39.950 | 0.000 | 0.000 | 0.000 | 0.000 | 0.450 | 0.000 |
| stamper | 40.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 11.850 / 40.000 | 100.200 ± 2.596 | +85.650 ± 2.494 | 218.700 | +181.300 ± 3.539 | 6.300 | 0.349 | 26.650 | +22.000 ± 0.821 | 1005.400 | 0.070 | +0.047 ± 0.003 | 0.000 / 0.000 (0.000 / 0.000) | 29554.324 ± 259.037 | -3043.276 ± 768.395 | 20428.6 ± 300.8 | -3722.3 ± 857.0 | 26.545 | -7.838 ± 0.623 | 31.329 ± 0.387 | +0.591 ± 0.949 | 27.394 | 0.190 | 1650.400 | 20.000 | 28.150 | +6.300 ± 0.385 | 83.665 | 75.750 |
| careful | 18.100 / 39.950 | 14.550 ± 0.793 | — | 37.400 | — | 11.750 | 0.048 | 4.650 | — | 833.500 | 0.024 | — | 0.000 / 0.000 (0.000 / 0.000) | 32597.600 ± 707.671 | — | 24150.9 ± 731.9 | — | 34.383 | — | 30.738 ± 0.838 | — | 22.062 | 0.002 | 2548.100 | 19.950 | 21.850 | — | 329.207 | 94.200 |
| stamper | 7.250 / 40.000 | 6.200 ± 0.479 | -8.350 ± 1.037 | 100.850 | +63.450 ± 1.455 | 0.000 | 1.000 | 41.350 | +36.700 ± 1.342 | 351.500 | 0.194 | +0.170 ± 0.004 | 0.000 / 0.000 (0.000 / 0.000) | 1412.272 ± 93.034 | -31185.328 ± 679.702 | 2433.1 ± 84.8 | -21717.8 ± 720.2 | 30.817 | -3.566 ± 0.650 | 28.681 ± 0.869 | -2.057 ± 1.254 | 17.814 | 0.368 | 246.150 | 20.000 | 32.750 | +10.900 ± 0.820 | 8643.959 | 91.750 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **greedy**: p0 0.884/0.116/0.000 (198); p1 0.544/0.455/0.000 (215); p2 0.461/0.539/0.000 (235); p3 0.444/0.556/0.000 (219); p4 0.537/0.463/0.000 (199); p5 0.672/0.328/0.000 (187); p6 0.660/0.339/0.000 (187); p7 0.676/0.324/0.000 (184); p8 0.680/0.320/0.001 (185); p9 0.633/0.364/0.003 (182); p10 0.615/0.385/0.000 (185); p11 0.615/0.385/0.000 (184); p12 0.643/0.357/0.000 (182); p13 0.608/0.392/0.000 (181); p14 0.629/0.371/0.001 (179); p15 0.630/0.370/0.001 (128); p16 0.681/0.319/0.000 (10)
- **careful**: p0 1.000/0.000/0.000 (195); p1 1.000/0.000/0.000 (247); p2 1.000/0.000/0.000 (279); p3 1.000/0.000/0.000 (285); p4 1.000/0.000/0.000 (258); p5 1.000/0.000/0.000 (233); p6 1.000/0.000/0.000 (228); p7 1.000/0.000/0.000 (228); p8 1.000/0.000/0.000 (222); p9 1.000/0.000/0.000 (224); p10 1.000/0.000/0.000 (222); p11 1.000/0.000/0.000 (223); p12 1.000/0.000/0.000 (226); p13 1.000/0.000/0.000 (227); p14 1.000/0.000/0.000 (222); p15 1.000/0.000/0.000 (220); p16 1.000/0.000/0.000 (226); p17 1.000/0.000/0.000 (230); p18 1.000/0.000/0.000 (216); p19 1.000/0.000/0.000 (152); p20 1.000/0.000/0.000 (26)
- **stamper**: p0 0.000/1.000/0.000 (194); p1 0.000/1.000/0.000 (181); p2 0.000/1.000/0.000 (116); p3 0.000/1.000/0.000 (2); p4 0.000/1.000/0.000 (2); p5 0.000/1.000/0.000 (2); p6 0.000/1.000/0.000 (1)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 2027.8 / 793.0 | 2.32 / 2.32 | -0.01 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.10 / 0.07 | -0.02 ± 0.00 | 0.625 / 0.599 | -0.026 ± 0.003 | 0.380 / 0.366 | 0.189 / 0.190 | 0.289 / 0.288 | -0.001 ± 0.005 | 4.19 / 4.17 | -0.02 ± 0.06 |
| careful | 2545.3 / 993.0 | 0.25 / 0.24 | -0.01 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.25 / 0.22 | -0.03 ± 0.00 | 0.100 / 0.085 | -0.015 ± 0.003 | 0.054 / 0.049 | 0.002 / 0.002 | 0.100 / 0.087 | -0.013 ± 0.002 | 2.01 / 1.93 | -0.07 ± 0.04 |
| stamper | 351.5 / 134.2 | 0.81 / 0.76 | -0.04 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.08 / 0.05 | -0.03 ± 0.00 | 0.004 / 0.001 | -0.003 ± 0.002 | 0.001 / 0.000 | 0.297 / 0.281 | 0.053 / 0.054 | +0.001 ± 0.005 | 1.74 / 1.61 | -0.13 ± 0.08 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| greedy | -0.01 ± 0.02 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.028 ± 0.002 | -0.016 ± 0.003 | -0.001 ± 0.005 |
| careful | -0.01 ± 0.01 | +0.00 ± 0.00 | -0.03 ± 0.00 | -0.015 ± 0.003 | -0.005 ± 0.001 | -0.012 ± 0.002 |
| stamper | -0.04 ± 0.02 | +0.00 ± 0.00 | -0.03 ± 0.00 | -0.003 ± 0.002 | -0.001 ± 0.001 | +0.000 ± 0.005 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| greedy | 0.072 / 0.036 | 0.58 / 0.65 | 0.018 / 0.008 | 0.00 / 0.00 | 0.53 / 0.53 | 0.497 / 0.333 |
| careful | 0.269 / 0.094 | 0.12 / 0.12 | 0.040 / 0.012 | 0.00 / 0.00 | 0.05 / 0.07 | 0.070 / 0.029 |
| stamper | 0.036 / 0.000 | 0.00 / — | 0.000 / 0.000 | — / — | — / — | 1.188 / 1.731 |

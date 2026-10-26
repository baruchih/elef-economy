# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --dial off --pi0 0.40`, seeds 21-40, hide ``, model `None` (value off, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | non-initial share | non-initial stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 21806.2 ± 342.4 | -2344.7 ± 872.9 | 3106.4 | 0.598 | 0.386 | 0.016 | 0.357 | 0.396 | 0.061 | 0.661 | 98.95 | 170.30 | 0.25 |
| careful | 24150.9 ± 731.9 | nan ± nan | 4587.1 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.229 | 0.000 | 14.55 | 0.00 | 0.45 |
| stamper | 2433.1 ± 84.8 | -21717.8 ± 720.2 | 498.4 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.025 | 1.000 | 6.20 | 73.60 | 1.00 |

The stamp rate by seat kind (2.8.0 §5), plant / real, with the decisions pooled over the seeds in parentheses — under 2.7.0 a plant reached the initial review alone; under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| direct | 0.357 (16398) / 0.396 (41959) | 0.788 (462) / 0.798 (2442) | 0.127 (307) / 0.250 (561) | — / — |
| careful | 0.000 (19859) / 0.000 (50907) | 0.000 (1873) / 0.000 (13784) | 0.000 (758) / 0.000 (4562) | — / — |
| stamper | 1.000 (2685) / 1.000 (7030) | — / 1.000 (253) | — / — | — / — |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 0.493 | 0.727 | 0.651 (14314) | 0.506 (8057) | 0.404 (11539) | 0.133 (4091) | 0.222 (24128) | 44.100 | 158.250 | 2.672 | 3.862 |
| careful | — | 0.410 | 0.000 (54931) | 0.000 (12533) | 0.000 (4546) | 0.000 (2600) | 0.000 (17133) | 24.600 | 203.650 | 1.541 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (9968) | 61.350 | 76.700 | 1.889 | 1.200 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| direct | 39.950 | 0.000 | 0.000 | 0.000 | 0.000 | 0.250 | 0.000 |
| careful | 39.950 | 0.000 | 0.000 | 0.000 | 0.000 | 0.450 | 0.000 |
| stamper | 40.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 13.500 / 39.950 | 98.950 ± 3.111 | +84.400 ± 3.235 | 227.950 | +190.550 ± 2.461 | 9.000 | 0.385 | 24.150 | +19.500 ± 0.671 | 1101.750 | 0.077 | +0.053 ± 0.002 | 0.000 / 0.000 (0.000 / 0.000) | 30560.345 ± 331.396 | -2037.255 ± 811.627 | 21806.2 ± 342.4 | -2344.7 ± 872.9 | 27.560 | -6.824 ± 0.591 | 30.425 ± 0.497 | -0.313 ± 1.012 | 26.504 | 0.106 | 1884.200 | 19.950 | 26.450 | +4.600 ± 0.483 | 97.114 | 85.000 |
| careful | 18.100 / 39.950 | 14.550 ± 0.793 | — | 37.400 | — | 11.750 | 0.048 | 4.650 | — | 833.500 | 0.024 | — | 0.000 / 0.000 (0.000 / 0.000) | 32597.600 ± 707.671 | — | 24150.9 ± 731.9 | — | 34.383 | — | 30.738 ± 0.838 | — | 22.062 | 0.002 | 2548.100 | 19.950 | 21.850 | — | 329.207 | 94.200 |
| stamper | 7.250 / 40.000 | 6.200 ± 0.479 | -8.350 ± 1.037 | 100.850 | +63.450 ± 1.455 | 0.000 | 1.000 | 41.350 | +36.700 ± 1.342 | 351.500 | 0.194 | +0.170 ± 0.004 | 0.000 / 0.000 (0.000 / 0.000) | 1412.272 ± 93.034 | -31185.328 ± 679.702 | 2433.1 ± 84.8 | -21717.8 ± 720.2 | 30.817 | -3.566 ± 0.650 | 28.681 ± 0.869 | -2.057 ± 1.254 | 17.814 | 0.368 | 246.150 | 20.000 | 32.750 | +10.900 ± 0.820 | 8643.959 | 91.750 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **direct**: p0 0.873/0.125/0.002 (200); p1 0.560/0.429/0.011 (215); p2 0.553/0.420/0.027 (225); p3 0.546/0.435/0.019 (223); p4 0.536/0.452/0.011 (205); p5 0.540/0.454/0.006 (192); p6 0.588/0.405/0.007 (183); p7 0.587/0.407/0.006 (181); p8 0.585/0.407/0.008 (179); p9 0.588/0.403/0.009 (177); p10 0.604/0.382/0.014 (180); p11 0.626/0.360/0.013 (178); p12 0.591/0.396/0.013 (182); p13 0.607/0.370/0.022 (178); p14 0.627/0.341/0.031 (178); p15 0.595/0.365/0.040 (159); p16 0.542/0.394/0.064 (67); p17 0.504/0.293/0.203 (6)
- **careful**: p0 1.000/0.000/0.000 (195); p1 1.000/0.000/0.000 (247); p2 1.000/0.000/0.000 (279); p3 1.000/0.000/0.000 (285); p4 1.000/0.000/0.000 (258); p5 1.000/0.000/0.000 (233); p6 1.000/0.000/0.000 (228); p7 1.000/0.000/0.000 (228); p8 1.000/0.000/0.000 (222); p9 1.000/0.000/0.000 (224); p10 1.000/0.000/0.000 (222); p11 1.000/0.000/0.000 (223); p12 1.000/0.000/0.000 (226); p13 1.000/0.000/0.000 (227); p14 1.000/0.000/0.000 (222); p15 1.000/0.000/0.000 (220); p16 1.000/0.000/0.000 (226); p17 1.000/0.000/0.000 (230); p18 1.000/0.000/0.000 (216); p19 1.000/0.000/0.000 (152); p20 1.000/0.000/0.000 (26)
- **stamper**: p0 0.000/1.000/0.000 (194); p1 0.000/1.000/0.000 (181); p2 0.000/1.000/0.000 (116); p3 0.000/1.000/0.000 (2); p4 0.000/1.000/0.000 (2); p5 0.000/1.000/0.000 (2); p6 0.000/1.000/0.000 (1)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 2097.9 / 819.9 | 2.04 / 2.08 | +0.04 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.09 / 0.06 | -0.03 ± 0.00 | 0.595 / 0.569 | -0.026 ± 0.003 | 0.331 / 0.319 | 0.105 / 0.109 | 0.263 / 0.259 | -0.005 ± 0.004 | 3.84 / 3.87 | +0.04 ± 0.04 |
| careful | 2545.3 / 993.0 | 0.25 / 0.24 | -0.01 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.25 / 0.22 | -0.03 ± 0.00 | 0.100 / 0.085 | -0.015 ± 0.003 | 0.054 / 0.049 | 0.002 / 0.002 | 0.100 / 0.087 | -0.013 ± 0.002 | 2.01 / 1.93 | -0.07 ± 0.04 |
| stamper | 351.5 / 134.2 | 0.81 / 0.76 | -0.04 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.08 / 0.05 | -0.03 ± 0.00 | 0.004 / 0.001 | -0.003 ± 0.002 | 0.001 / 0.000 | 0.297 / 0.281 | 0.053 / 0.054 | +0.001 ± 0.005 | 1.74 / 1.61 | -0.13 ± 0.08 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| direct | +0.03 ± 0.02 | +0.00 ± 0.00 | -0.03 ± 0.00 | -0.027 ± 0.003 | -0.013 ± 0.003 | -0.005 ± 0.004 |
| careful | -0.01 ± 0.01 | +0.00 ± 0.00 | -0.03 ± 0.00 | -0.015 ± 0.003 | -0.005 ± 0.001 | -0.012 ± 0.002 |
| stamper | -0.04 ± 0.02 | +0.00 ± 0.00 | -0.03 ± 0.00 | -0.003 ± 0.002 | -0.001 ± 0.001 | +0.000 ± 0.005 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| direct | 0.058 / 0.028 | 0.64 / 0.70 | 0.029 / 0.011 | 0.00 / 0.00 | 0.62 / 0.68 | 0.570 / 0.394 |
| careful | 0.269 / 0.094 | 0.12 / 0.12 | 0.040 / 0.012 | 0.00 / 0.00 | 0.05 / 0.07 | 0.070 / 0.029 |
| stamper | 0.036 / 0.000 | 0.00 / — | 0.000 / 0.000 | — / — | — / — | 1.188 / 1.731 |

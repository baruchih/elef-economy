# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --dispute-policy truthful --appeal-lie 0.1 --dispute-lie 0.1 --planted-approval off`, seeds 21-40, hide ``, model `None` (value off, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | non-initial share | non-initial stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 29421.7 ± 663.8 | -5457.0 ± 807.2 | 4375.0 | 0.668 | 0.308 | 0.024 | 0.204 | 0.216 | 0.318 | 0.589 | 13.00 | 119.70 | 0.20 |
| careful | 34878.7 ± 853.1 | nan ± nan | 4191.3 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.333 | 0.000 | 1.05 | 0.00 | 0.35 |
| stamper | 7124.2 ± 128.7 | -27754.4 ± 887.3 | 1076.4 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.029 | 1.000 | 9.25 | 187.75 | 1.00 |

The stamp rate by seat kind (2.8.0 §5), plant / real, with the decisions pooled over the seeds in parentheses — under 2.7.0 a plant reached the initial review alone; under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| direct | 0.204 (12291) / 0.216 (47373) | 0.867 (664) / 0.853 (15093) | 0.218 (4863) / 0.260 (7216) | — / — |
| careful | 0.000 (5154) / 0.000 (50746) | 0.000 (99) / 0.000 (16762) | 0.000 (2198) / 0.000 (8867) | — / — |
| stamper | 1.000 (3034) / 1.000 (17878) | — / 1.000 (343) | — / 1.000 (273) | — / — |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 0.877 | 0.925 | 0.461 (1827) | 0.491 (1431) | 0.516 (1647) | 0.381 (23443) | 0.265 (59152) | 37.300 | 374.800 | 1.515 | 3.209 |
| careful | — | 0.680 | 0.000 (26476) | 0.000 (5834) | 0.000 (4561) | 0.000 (1325) | 0.000 (45630) | 25.100 | 723.900 | 1.240 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (21528) | 74.200 | 176.100 | 2.207 | 2.530 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| direct | 39.700 | 0.000 | 0.000 | 0.000 | 0.000 | 0.200 | 0.000 |
| careful | 39.650 | 0.000 | 0.000 | 0.000 | 0.000 | 0.350 | 0.000 |
| stamper | 40.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 19.200 / 39.700 | 13.000 ± 0.909 | +11.950 ± 0.961 | 97.200 | +87.550 ± 4.148 | 9.300 | 0.196 | 17.600 | +12.150 ± 0.969 | 1523.800 | 0.008 | -0.005 ± 0.001 | 280.450 / 103.850 (107.600 / 99.050) | 29821.397 ± 470.803 | +5720.267 ± 652.207 | 29421.7 ± 663.8 | -5457.0 ± 807.2 | 30.972 | -4.195 ± 0.578 | 22.214 ± 0.506 | +7.427 ± 0.522 | 20.747 | 0.026 | 2315.800 | 19.700 | 20.500 | +5.300 ± 0.599 | 62.928 | 160.600 |
| careful | 24.450 / 39.650 | 1.050 ± 0.198 | — | 9.650 | — | 3.450 | 0.043 | 5.450 | — | 1425.450 | 0.013 | — | 222.700 / 28.800 (25.850 / 25.250) | 24101.129 ± 438.620 | — | 34878.7 ± 853.1 | — | 35.167 | — | 14.787 ± 0.443 | — | 18.563 | 0.007 | 2527.400 | 19.650 | 15.200 | — | 647.046 | 229.350 |
| stamper | 4.200 / 40.000 | 9.250 ± 0.656 | +8.200 ± 0.635 | 111.700 | +102.050 ± 1.558 | 0.000 | 1.000 | 54.200 | +48.750 ± 1.908 | 651.100 | 0.018 | +0.005 ± 0.001 | 245.550 / 166.300 (174.200 / 165.300) | 8391.745 ± 172.653 | -15709.385 ± 525.555 | 7124.2 ± 128.7 | -27754.4 ± 887.3 | 26.711 | -8.456 ± 0.577 | 30.190 ± 0.801 | +15.404 ± 0.969 | 22.785 | 0.256 | 694.100 | 20.000 | 35.800 | +20.600 ± 0.913 | 5688.227 | 169.400 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **direct**: p0 0.837/0.160/0.003 (614); p1 0.692/0.295/0.013 (569); p2 0.569/0.413/0.019 (400); p3 0.653/0.321/0.027 (299); p4 0.638/0.330/0.032 (297); p5 0.616/0.355/0.029 (297); p6 0.612/0.349/0.039 (301); p7 0.655/0.307/0.038 (294); p8 0.637/0.338/0.025 (292); p9 0.642/0.330/0.027 (288); p10 0.645/0.318/0.037 (281); p11 0.666/0.303/0.030 (243); p12 0.665/0.290/0.045 (158); p13 0.500/0.467/0.033 (36); p14 0.342/0.640/0.018 (6)
- **careful**: p0 1.000/0.000/0.000 (599); p1 1.000/0.000/0.000 (678); p2 1.000/0.000/0.000 (835); p3 1.000/0.000/0.000 (918); p4 1.000/0.000/0.000 (901); p5 1.000/0.000/0.000 (256); p6 1.000/0.000/0.000 (3)
- **stamper**: p0 0.000/1.000/0.000 (576); p1 0.000/1.000/0.000 (306); p2 0.000/1.000/0.000 (168); p3 0.000/1.000/0.000 (17); p4 0.000/1.000/0.000 (8); p5 0.000/1.000/0.000 (2)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 2368.7 / 614.5 | 1.09 / 1.23 | +0.14 ± 0.05 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.05 / 0.04 | -0.00 ± 0.00 | 0.463 / 0.499 | +0.036 ± 0.010 | 0.232 / 0.275 | 0.026 / 0.000 | 0.129 / 0.143 | +0.014 ± 0.006 | 2.82 / 2.81 | -0.01 ± 0.08 |
| careful | 2537.3 / 257.7 | 0.56 / 0.39 | -0.17 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.06 / 0.06 | -0.00 ± 0.00 | 0.257 / 0.212 | -0.045 ± 0.009 | 0.106 / 0.112 | 0.007 / 0.000 | 0.072 / 0.063 | -0.009 ± 0.005 | 2.25 / 1.94 | -0.31 ± 0.13 |
| stamper | 893.9 / 151.7 | 1.38 / 0.95 | -0.43 ± 0.04 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.03 / 0.02 | -0.01 ± 0.00 | 0.304 / 0.294 | -0.010 ± 0.008 | 0.173 / 0.172 | 0.223 / 0.000 | 0.114 / 0.080 | -0.034 ± 0.005 | 3.70 / 2.99 | -0.71 ± 0.41 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| direct | -0.04 ± 0.02 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.056 ± 0.004 | -0.019 ± 0.004 | -0.002 ± 0.004 |
| careful | -0.16 ± 0.03 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.047 ± 0.009 | +0.005 ± 0.005 | -0.009 ± 0.005 |
| stamper | -0.93 ± 0.05 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.174 ± 0.012 | -0.123 ± 0.011 | -0.042 ± 0.006 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| direct | 0.313 / 0.051 | 0.47 / 0.40 | 0.180 / 0.420 | 0.00 / 0.00 | 0.47 / 0.46 | 0.559 / 0.475 |
| careful | 0.328 / 0.019 | 0.38 / 0.53 | 0.145 / 0.412 | 0.00 / 0.00 | 0.31 / 0.32 | 0.382 / 0.428 |
| stamper | 0.019 / 0.000 | 0.01 / — | 0.271 / 0.999 | 0.00 / 0.00 | 0.00 / — | 1.279 / 1.999 |

# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop half --learner-role reviewer --learner-exit rule`, seeds 21-40, hide ``, model `None` (value off, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | non-initial share | non-initial stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 17070.5 ± 583.9 | -2405.5 ± 634.4 | 2364.1 | 0.763 | 0.230 | 0.006 | 0.112 | 0.121 | 0.282 | 0.540 | 20.45 | 41.30 | 0.25 |
| careful | 19476.0 ± 680.0 | nan ± nan | 2542.3 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.328 | 0.000 | 8.85 | 0.00 | 0.35 |
| stamper | 3754.7 ± 123.4 | -15721.3 ± 650.1 | 512.9 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.023 | 1.000 | 14.65 | 87.65 | 1.00 |

The stamp rate by seat kind (2.8.0 §5), plant / real, with the decisions pooled over the seeds in parentheses — under 2.7.0 a plant reached the initial review alone; under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| direct | 0.112 (7633) / 0.121 (26292) | 0.631 (1344) / 0.610 (9759) | 0.141 (462) / 0.193 (1791) | — / — |
| careful | 0.000 (6072) / 0.000 (28076) | 0.000 (1145) / 0.000 (12689) | 0.000 (431) / 0.000 (2433) | — / — |
| stamper | 1.000 (1432) / 1.000 (8590) | — / 1.000 (217) | — / 1.000 (18) | — / — |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 0.858 | 0.897 | 0.419 (43) | 0.597 (355) | 0.310 (4203) | 0.277 (15532) | 0.188 (27148) | 17.300 | 158.100 | 2.753 | 2.387 |
| careful | — | 0.740 | 0.000 (2430) | 0.000 (10779) | 0.000 (8620) | 0.000 (6625) | 0.000 (22392) | 12.650 | 230.700 | 2.206 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (10257) | 35.150 | 94.450 | 4.253 | 2.494 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| direct | 20.300 | 0.000 | 0.000 | 0.000 | 0.000 | 0.250 | 0.000 |
| careful | 20.400 | 0.000 | 0.000 | 0.000 | 0.000 | 0.350 | 0.000 |
| stamper | 20.450 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 10.150 / 20.300 | 20.450 ± 1.736 | +11.600 ± 1.953 | 73.750 | +36.000 ± 3.181 | 9.700 | 0.104 | 14.200 | +6.050 ± 0.587 | 1779.000 | 0.048 | +0.003 ± 0.002 | 0.000 / 0.000 (0.000 / 0.000) | 15763.332 ± 580.552 | -761.156 ± 575.247 | 17070.5 ± 583.9 | -2405.5 ± 634.4 | 32.291 | -2.253 ± 0.445 | 20.087 ± 0.440 | +1.399 ± 0.682 | 19.414 | 0.005 | 2470.650 | 19.750 | 19.850 | +0.500 ± 0.420 | 73.558 | 144.450 |
| careful | 12.050 / 20.400 | 8.850 ± 0.805 | — | 37.750 | — | 7.400 | 0.061 | 8.150 | — | 1604.000 | 0.044 | — | 0.000 / 0.000 (0.000 / 0.000) | 16524.488 ± 661.951 | — | 19476.0 ± 680.0 | — | 34.545 | — | 18.688 ± 0.714 | — | 18.626 | 0.005 | 2556.400 | 19.850 | 19.350 | — | 402.222 | 208.450 |
| stamper | 0.000 / 20.450 | 14.650 ± 0.916 | +5.800 ± 1.301 | 91.750 | +54.000 ± 2.342 | 4.650 | 0.056 | 33.350 | +25.200 ± 0.839 | 1526.100 | 0.091 | +0.047 ± 0.003 | 0.000 / 0.000 (0.000 / 0.000) | 3621.714 ± 145.480 | -12902.774 ± 684.362 | 3754.7 ± 123.4 | -15721.3 ± 650.1 | 27.726 | -6.819 ± 0.467 | 28.299 ± 0.366 | +9.611 ± 0.815 | 24.249 | 0.330 | 1421.100 | 20.000 | 29.150 | +9.800 ± 0.484 | 86.099 | 174.750 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **direct**: p0 0.898/0.101/0.001 (293); p1 0.615/0.379/0.006 (201); p2 0.794/0.201/0.005 (124); p3 0.765/0.226/0.009 (139); p4 0.776/0.218/0.006 (160); p5 0.795/0.195/0.010 (161); p6 0.793/0.202/0.005 (158); p7 0.778/0.214/0.008 (156); p8 0.737/0.255/0.008 (160); p9 0.732/0.261/0.007 (170); p10 0.755/0.240/0.005 (159); p11 0.705/0.289/0.006 (152); p12 0.730/0.258/0.012 (149); p13 0.722/0.273/0.005 (133); p14 0.752/0.237/0.011 (50); p15 1.000/0.000/0.000 (0)
- **careful**: p0 1.000/0.000/0.000 (301); p1 1.000/0.000/0.000 (256); p2 1.000/0.000/0.000 (217); p3 1.000/0.000/0.000 (210); p4 1.000/0.000/0.000 (219); p5 1.000/0.000/0.000 (228); p6 1.000/0.000/0.000 (218); p7 1.000/0.000/0.000 (200); p8 1.000/0.000/0.000 (197); p9 1.000/0.000/0.000 (170); p10 1.000/0.000/0.000 (155); p11 1.000/0.000/0.000 (112); p12 1.000/0.000/0.000 (60)
- **stamper**: p0 0.000/1.000/0.000 (295); p1 0.000/1.000/0.000 (139); p2 0.000/1.000/0.000 (56); p3 0.000/1.000/0.000 (20); p4 0.000/1.000/0.000 (3); p5 0.000/1.000/0.000 (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 2469.8 / 707.3 | 0.63 / 0.62 | -0.00 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.14 / 0.15 | +0.01 ± 0.00 | 0.338 / 0.343 | +0.005 ± 0.005 | 0.156 / 0.178 | 0.005 / 0.004 | 0.055 / 0.056 | +0.001 ± 0.003 | 2.23 / 2.34 | +0.11 ± 0.09 |
| careful | 2560.8 / 545.3 | 0.38 / 0.27 | -0.11 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.12 / 0.14 | +0.01 ± 0.00 | 0.177 / 0.158 | -0.019 ± 0.005 | 0.076 / 0.086 | 0.005 / 0.003 | 0.042 / 0.042 | +0.000 ± 0.002 | 1.95 / 1.62 | -0.33 ± 0.10 |
| stamper | 2078.2 / 520.5 | 2.05 / 2.20 | +0.16 ± 0.04 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.12 / 0.14 | +0.01 ± 0.00 | 0.559 / 0.617 | +0.058 ± 0.006 | 0.350 / 0.391 | 0.324 / 0.389 | 0.024 / 0.016 | -0.008 ± 0.002 | 3.36 / 2.76 | -0.60 ± 0.27 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| direct | -0.08 ± 0.01 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.052 ± 0.003 | -0.010 ± 0.003 | -0.002 ± 0.002 |
| careful | -0.13 ± 0.02 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.042 ± 0.005 | -0.007 ± 0.003 | +0.001 ± 0.002 |
| stamper | -0.19 ± 0.04 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.054 ± 0.004 | -0.035 ± 0.005 | -0.004 ± 0.002 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| direct | 0.461 / 0.225 | 0.16 / 0.17 | 0.037 / 0.014 | 0.00 / 0.00 | 0.15 / 0.11 | 0.306 / 0.118 |
| careful | 0.404 / 0.170 | 0.16 / 0.18 | 0.036 / 0.013 | 0.00 / 0.00 | 0.11 / 0.05 | 0.265 / 0.112 |
| stamper | 0.368 / 0.175 | 0.16 / 0.17 | 0.016 / 0.009 | 0.00 / 0.00 | 0.13 / 0.09 | 0.427 / 0.312 |

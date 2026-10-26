# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --dispute-policy truthful --appeal-lie 0.1 --dispute-lie 0.1`, seeds 21-40, hide ``, model `None` (value off, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | non-initial share | non-initial stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 30277.2 ± 757.5 | -5048.4 ± 1199.8 | 4298.7 | 0.632 | 0.350 | 0.017 | 0.217 | 0.249 | 0.297 | 0.667 | 18.45 | 156.35 | 0.20 |
| careful | 35325.6 ± 855.4 | nan ± nan | 4225.8 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.326 | 0.000 | 1.40 | 0.00 | 0.25 |
| stamper | 7257.2 ± 170.1 | -28068.4 ± 804.7 | 1083.2 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.028 | 1.000 | 8.20 | 181.65 | 1.00 |

The stamp rate by seat kind (2.8.0 §5), plant / real, with the decisions pooled over the seeds in parentheses — under 2.7.0 a plant reached the initial review alone; under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| direct | 0.217 (12798) / 0.249 (47666) | 0.812 (1695) / 0.805 (14663) | 0.325 (2327) / 0.451 (6825) | — / — |
| careful | 0.000 (5288) / 0.000 (51655) | 0.000 (556) / 0.000 (17297) | 0.000 (334) / 0.000 (9385) | — / — |
| stamper | 1.000 (3068) / 1.000 (17979) | — / 1.000 (343) | — / 1.000 (273) | — / — |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 0.898 | 0.934 | 0.589 (1174) | 0.611 (1338) | 0.479 (780) | 0.407 (22786) | 0.317 (59896) | 39.050 | 342.900 | 1.535 | 4.004 |
| careful | — | 0.677 | 0.000 (26259) | 0.000 (6465) | 0.000 (5104) | 0.000 (1482) | 0.000 (45205) | 24.350 | 694.900 | 1.197 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (21663) | 77.350 | 172.850 | 2.217 | 2.348 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| direct | 39.750 | 0.000 | 0.000 | 0.000 | 0.000 | 0.200 | 0.000 |
| careful | 39.500 | 0.000 | 0.000 | 0.000 | 0.000 | 0.250 | 0.000 |
| stamper | 39.950 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 19.550 / 39.750 | 18.450 ± 0.942 | +17.050 ± 0.972 | 114.800 | +104.900 ± 4.019 | 8.650 | 0.284 | 19.300 | +14.450 ± 1.009 | 1559.050 | 0.009 | -0.004 ± 0.001 | 301.050 / 123.850 (126.700 / 116.800) | 29409.295 ± 353.390 | +6290.791 ± 435.001 | 30277.2 ± 757.5 | -5048.4 ± 1199.8 | 31.092 | -5.177 ± 0.456 | 21.065 ± 0.541 | +7.164 ± 0.727 | 20.515 | 0.013 | 2360.450 | 19.750 | 20.200 | +4.400 ± 0.582 | 68.072 | 178.250 |
| careful | 23.700 / 39.500 | 1.400 ± 0.266 | — | 9.900 | — | 3.300 | 0.063 | 4.850 | — | 1432.650 | 0.013 | — | 216.400 / 26.850 (24.400 / 23.350) | 23118.504 ± 425.785 | — | 35325.6 ± 855.4 | — | 36.269 | — | 13.901 ± 0.358 | — | 17.763 | 0.002 | 2584.300 | 19.500 | 15.800 | — | 777.141 | 214.700 |
| stamper | 4.250 / 39.950 | 8.200 ± 0.691 | +6.800 ± 0.753 | 115.400 | +105.500 ± 2.733 | 0.000 | 1.000 | 57.400 | +52.550 ± 2.324 | 658.800 | 0.017 | +0.004 ± 0.001 | 243.050 / 162.100 (168.500 / 160.700) | 8453.892 ± 153.707 | -14664.613 ± 401.302 | 7257.2 ± 170.1 | -28068.4 ± 804.7 | 26.992 | -9.277 ± 0.544 | 29.830 ± 0.681 | +15.929 ± 0.820 | 22.472 | 0.259 | 694.950 | 19.950 | 35.700 | +19.900 ± 0.774 | 5671.578 | 146.650 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **direct**: p0 0.824/0.176/0.001 (607); p1 0.543/0.444/0.013 (510); p2 0.589/0.395/0.016 (345); p3 0.633/0.352/0.015 (291); p4 0.583/0.379/0.038 (300); p5 0.584/0.389/0.026 (297); p6 0.572/0.406/0.022 (294); p7 0.590/0.388/0.022 (296); p8 0.629/0.354/0.016 (277); p9 0.634/0.348/0.019 (273); p10 0.638/0.341/0.021 (264); p11 0.618/0.360/0.022 (218); p12 0.630/0.349/0.021 (154); p13 0.654/0.319/0.027 (106); p14 0.642/0.341/0.017 (59); p15 0.546/0.433/0.021 (7)
- **careful**: p0 1.000/0.000/0.000 (604); p1 1.000/0.000/0.000 (726); p2 1.000/0.000/0.000 (853); p3 1.000/0.000/0.000 (918); p4 1.000/0.000/0.000 (859); p5 1.000/0.000/0.000 (226); p6 1.000/0.000/0.000 (40)
- **stamper**: p0 0.000/1.000/0.000 (577); p1 0.000/1.000/0.000 (306); p2 0.000/1.000/0.000 (163); p3 0.000/1.000/0.000 (27); p4 0.000/1.000/0.000 (9); p5 0.000/1.000/0.000 (2)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 2383.3 / 639.9 | 1.04 / 1.19 | +0.15 ± 0.05 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.05 / 0.05 | -0.00 ± 0.00 | 0.460 / 0.487 | +0.027 ± 0.011 | 0.233 / 0.269 | 0.013 / 0.020 | 0.127 / 0.139 | +0.012 ± 0.005 | 2.71 / 2.74 | +0.03 ± 0.07 |
| careful | 2582.8 / 264.4 | 0.37 / 0.24 | -0.14 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.06 / 0.06 | -0.00 ± 0.00 | 0.221 / 0.182 | -0.039 ± 0.006 | 0.086 / 0.096 | 0.002 / 0.001 | 0.066 / 0.074 | +0.008 ± 0.004 | 1.91 / 1.52 | -0.39 ± 0.06 |
| stamper | 899.0 / 153.4 | 1.30 / 0.88 | -0.42 ± 0.05 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.04 / 0.02 | -0.01 ± 0.00 | 0.299 / 0.284 | -0.015 ± 0.010 | 0.173 / 0.172 | 0.226 / 0.315 | 0.110 / 0.078 | -0.032 ± 0.005 | 3.53 / 2.33 | -1.20 ± 0.21 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| direct | -0.01 ± 0.02 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.057 ± 0.004 | -0.018 ± 0.004 | -0.003 ± 0.003 |
| careful | -0.14 ± 0.02 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.040 ± 0.006 | +0.009 ± 0.004 | +0.008 ± 0.004 |
| stamper | -0.89 ± 0.04 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.171 ± 0.013 | -0.119 ± 0.011 | -0.040 ± 0.004 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| direct | 0.303 / 0.128 | 0.46 / 0.44 | 0.178 / 0.193 | 0.00 / 0.00 | 0.48 / 0.47 | 0.586 / 0.311 |
| careful | 0.333 / 0.106 | 0.37 / 0.40 | 0.143 / 0.049 | 0.00 / 0.00 | 0.31 / 0.30 | 0.358 / 0.133 |
| stamper | 0.019 / 0.000 | 0.01 / — | 0.267 / 0.753 | 0.00 / 0.00 | 0.00 / — | 1.272 / 1.766 |

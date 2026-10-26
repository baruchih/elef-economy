# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --dispute-policy truthful --appeal-lie 0.1 --dispute-lie 0.1`, seeds 21-40, hide ``, model `None` (value off, horizon 8)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | non-initial share | non-initial stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 30130.6 ± 715.7 | -5195.1 ± 939.6 | 4349.2 | 0.615 | 0.363 | 0.022 | 0.221 | 0.245 | 0.314 | 0.703 | 19.60 | 155.45 | 0.30 |
| careful | 35325.6 ± 855.4 | nan ± nan | 4225.8 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.326 | 0.000 | 1.40 | 0.00 | 0.25 |
| stamper | 7257.2 ± 170.1 | -28068.4 ± 804.7 | 1083.2 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.028 | 1.000 | 8.20 | 181.65 | 1.00 |
| hand | 30502.3 ± 640.9 | -4823.3 ± 1007.7 | 4549.1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.339 | 0.000 | 3.80 | 0.00 | 0.45 |

The stamp rate by seat kind (2.8.0 §5), plant / real, with the decisions pooled over the seeds in parentheses — under 2.7.0 a plant reached the initial review alone; under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| direct | 0.221 (12490) / 0.245 (47148) | 0.875 (1781) / 0.875 (15734) | 0.294 (2575) / 0.434 (7257) | — / — |
| careful | 0.000 (5288) / 0.000 (51655) | 0.000 (556) / 0.000 (17297) | 0.000 (334) / 0.000 (9385) | — / — |
| stamper | 1.000 (3068) / 1.000 (17979) | — / 1.000 (343) | — / 1.000 (273) | — / — |
| hand | 0.000 (11982) / 0.000 (48152) | 0.000 (1810) / 0.000 (17686) | 0.000 (1304) / 0.000 (10048) | — / — |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 0.882 | 0.943 | 0.682 (1401) | 0.718 (1177) | 0.659 (1165) | 0.468 (22875) | 0.304 (60367) | 38.700 | 359.100 | 1.525 | 4.017 |
| careful | — | 0.677 | 0.000 (26259) | 0.000 (6465) | 0.000 (5104) | 0.000 (1482) | 0.000 (45205) | 24.350 | 694.900 | 1.197 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (21663) | 77.350 | 172.850 | 2.217 | 2.348 |
| hand | — | 0.802 | 0.000 (73) | 0.000 (12376) | 0.000 (19108) | 0.000 (15045) | 0.000 (44380) | 37.550 | 354.850 | 1.384 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| direct | 39.850 | 0.000 | 0.000 | 0.000 | 0.000 | 0.300 | 0.000 |
| careful | 39.500 | 0.000 | 0.000 | 0.000 | 0.000 | 0.250 | 0.000 |
| stamper | 39.950 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| hand | 39.900 | 0.000 | 0.000 | 0.000 | 0.000 | 0.450 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 19.400 / 39.850 | 19.600 ± 1.075 | +18.200 ± 1.200 | 113.800 | +103.900 ± 3.431 | 9.100 | 0.267 | 18.850 | +14.000 ± 0.837 | 1543.600 | 0.008 | -0.004 ± 0.001 | 295.350 / 123.600 (124.100 / 116.100) | 30030.195 ± 401.134 | +6911.691 ± 463.755 | 30130.6 ± 715.7 | -5195.1 ± 939.6 | 30.725 | -5.544 ± 0.550 | 21.607 ± 0.450 | +7.706 ± 0.571 | 20.929 | 0.015 | 2331.850 | 19.850 | 20.450 | +4.650 ± 0.494 | 60.647 | 157.000 |
| careful | 23.700 / 39.500 | 1.400 ± 0.266 | — | 9.900 | — | 3.300 | 0.063 | 4.850 | — | 1432.650 | 0.013 | — | 216.400 / 26.850 (24.400 / 23.350) | 23118.504 ± 425.785 | — | 35325.6 ± 855.4 | — | 36.269 | — | 13.901 ± 0.358 | — | 17.763 | 0.002 | 2584.300 | 19.500 | 15.800 | — | 777.141 | 214.700 |
| stamper | 4.250 / 39.950 | 8.200 ± 0.691 | +6.800 ± 0.753 | 115.400 | +105.500 ± 2.733 | 0.000 | 1.000 | 57.400 | +52.550 ± 2.324 | 658.800 | 0.017 | +0.004 ± 0.001 | 243.050 / 162.100 (168.500 / 160.700) | 8453.892 ± 153.707 | -14664.613 ± 401.302 | 7257.2 ± 170.1 | -28068.4 ± 804.7 | 26.992 | -9.277 ± 0.544 | 29.830 ± 0.681 | +15.929 ± 0.820 | 22.472 | 0.259 | 694.950 | 19.950 | 35.700 | +19.900 ± 0.774 | 5671.578 | 146.650 |
| hand | 20.150 / 39.900 | 3.800 ± 0.445 | +2.400 ± 0.582 | 67.500 | +57.600 ± 1.816 | 6.100 | 0.053 | 17.650 | +12.800 ± 0.753 | 1391.150 | 0.012 | -0.001 ± 0.001 | 272.750 / 92.200 (92.000 / 89.100) | 28775.527 ± 329.146 | +5657.023 ± 384.259 | 30502.3 ± 640.9 | -4823.3 ± 1007.7 | 31.476 | -4.793 ± 0.553 | 20.333 ± 0.470 | +6.432 ± 0.699 | 19.987 | 0.047 | 2305.700 | 19.900 | 19.750 | +3.950 ± 0.655 | 59.516 | 218.050 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **direct**: p0 0.838/0.159/0.003 (609); p1 0.540/0.431/0.029 (566); p2 0.528/0.447/0.024 (362); p3 0.636/0.340/0.023 (268); p4 0.611/0.363/0.026 (304); p5 0.576/0.397/0.027 (299); p6 0.560/0.409/0.031 (302); p7 0.587/0.384/0.029 (302); p8 0.572/0.404/0.024 (314); p9 0.595/0.387/0.018 (296); p10 0.580/0.399/0.021 (283); p11 0.586/0.392/0.022 (229); p12 0.614/0.361/0.025 (129); p13 0.656/0.328/0.016 (69); p14 0.653/0.314/0.033 (15); p15 0.500/0.457/0.043 (2)
- **careful**: p0 1.000/0.000/0.000 (604); p1 1.000/0.000/0.000 (726); p2 1.000/0.000/0.000 (853); p3 1.000/0.000/0.000 (918); p4 1.000/0.000/0.000 (859); p5 1.000/0.000/0.000 (226); p6 1.000/0.000/0.000 (40)
- **stamper**: p0 0.000/1.000/0.000 (577); p1 0.000/1.000/0.000 (306); p2 0.000/1.000/0.000 (163); p3 0.000/1.000/0.000 (27); p4 0.000/1.000/0.000 (9); p5 0.000/1.000/0.000 (2)
- **hand**: p0 —/—/— (0); p1 —/—/— (0); p2 —/—/— (0); p3 —/—/— (0); p4 —/—/— (0); p5 —/—/— (0); p6 —/—/— (0); p7 —/—/— (0); p8 —/—/— (0); p9 —/—/— (0); p10 —/—/— (0); p11 —/—/— (0); p12 —/—/— (0); p13 —/—/— (0); p14 —/—/— (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 2357.4 / 624.5 | 1.12 / 1.30 | +0.18 ± 0.05 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.06 / 0.05 | -0.00 ± 0.00 | 0.477 / 0.526 | +0.050 ± 0.011 | 0.244 / 0.291 | 0.014 / 0.022 | 0.130 / 0.149 | +0.018 ± 0.005 | 2.88 / 2.86 | -0.02 ± 0.08 |
| careful | 2582.8 / 264.4 | 0.37 / 0.24 | -0.14 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.06 / 0.06 | -0.00 ± 0.00 | 0.221 / 0.182 | -0.039 ± 0.006 | 0.086 / 0.096 | 0.002 / 0.001 | 0.066 / 0.074 | +0.008 ± 0.004 | 1.91 / 1.52 | -0.39 ± 0.06 |
| stamper | 899.0 / 153.4 | 1.30 / 0.88 | -0.42 ± 0.05 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.04 / 0.02 | -0.01 ± 0.00 | 0.299 / 0.284 | -0.015 ± 0.010 | 0.173 / 0.172 | 0.226 / 0.315 | 0.110 / 0.078 | -0.032 ± 0.005 | 3.53 / 2.33 | -1.20 ± 0.21 |
| hand | 2407.6 / 599.1 | 0.98 / 1.02 | +0.04 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.12 / 0.12 | -0.00 ± 0.00 | 0.396 / 0.414 | +0.017 ± 0.007 | 0.176 / 0.202 | 0.047 / 0.054 | 0.111 / 0.108 | -0.003 ± 0.004 | 3.02 / 2.82 | -0.20 ± 0.08 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| direct | -0.01 ± 0.02 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.050 ± 0.005 | -0.019 ± 0.004 | +0.001 ± 0.004 |
| careful | -0.14 ± 0.02 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.040 ± 0.006 | +0.009 ± 0.004 | +0.008 ± 0.004 |
| stamper | -0.89 ± 0.04 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.171 ± 0.013 | -0.119 ± 0.011 | -0.040 ± 0.004 |
| hand | -0.09 ± 0.02 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.045 ± 0.004 | -0.010 ± 0.005 | -0.004 ± 0.004 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| direct | 0.327 / 0.141 | 0.43 / 0.40 | 0.180 / 0.196 | 0.00 / 0.00 | 0.43 / 0.41 | 0.554 / 0.272 |
| careful | 0.333 / 0.106 | 0.37 / 0.40 | 0.143 / 0.049 | 0.00 / 0.00 | 0.31 / 0.30 | 0.358 / 0.133 |
| stamper | 0.019 / 0.000 | 0.01 / — | 0.267 / 0.753 | 0.00 / 0.00 | 0.00 / — | 1.272 / 1.766 |
| hand | 0.362 / 0.149 | 0.13 / 0.13 | 0.160 / 0.123 | 0.00 / 0.00 | 0.12 / 0.22 | 0.357 / 0.195 |

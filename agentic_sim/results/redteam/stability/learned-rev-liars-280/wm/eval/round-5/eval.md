# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --dispute-policy truthful --appeal-lie 0.1 --dispute-lie 0.1`, seeds 21-40, hide ``, model `results/redteam/stability/learned-rev-liars-280/wm/models/wm-online-5.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | non-initial share | non-initial stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 30429.7 ± 538.3 | -4895.9 ± 786.9 | 4460.6 | 0.622 | 0.371 | 0.007 | 0.158 | 0.188 | 0.350 | 0.746 | 22.40 | 131.50 | 0.00 |
| careful | 35325.6 ± 855.4 | nan ± nan | 4225.8 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.326 | 0.000 | 1.40 | 0.00 | 0.25 |
| stamper | 7257.2 ± 170.1 | -28068.4 ± 804.7 | 1083.2 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.028 | 1.000 | 8.20 | 181.65 | 1.00 |

The stamp rate by seat kind (2.8.0 §5), plant / real, with the decisions pooled over the seeds in parentheses — under 2.7.0 a plant reached the initial review alone; under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| greedy | 0.158 (12833) / 0.188 (45192) | 0.955 (2051) / 0.958 (18303) | 0.235 (2626) / 0.384 (8208) | — / — |
| careful | 0.000 (5288) / 0.000 (51655) | 0.000 (556) / 0.000 (17297) | 0.000 (334) / 0.000 (9385) | — / — |
| stamper | 1.000 (3068) / 1.000 (17979) | — / 1.000 (343) | — / 1.000 (273) | — / — |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 0.866 | 0.910 | 0.762 (663) | 0.728 (1310) | 0.515 (2088) | 0.411 (34154) | 0.325 (50998) | 41.250 | 243.400 | 1.602 | 3.188 |
| careful | — | 0.677 | 0.000 (26259) | 0.000 (6465) | 0.000 (5104) | 0.000 (1482) | 0.000 (45205) | 24.350 | 694.900 | 1.197 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (21663) | 77.350 | 172.850 | 2.217 | 2.348 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| greedy | 39.800 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| careful | 39.500 | 0.000 | 0.000 | 0.000 | 0.000 | 0.250 | 0.000 |
| stamper | 39.950 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 17.950 / 39.800 | 22.400 ± 1.633 | +21.000 ± 1.603 | 94.550 | +84.650 ± 2.462 | 7.900 | 0.169 | 21.450 | +16.600 ± 0.550 | 1467.300 | 0.005 | -0.008 ± 0.001 | 263.400 / 97.800 (97.300 / 91.550) | 33140.393 ± 439.580 | +10021.888 ± 552.688 | 30429.7 ± 538.3 | -4895.9 ± 786.9 | 29.639 | -6.629 ± 0.525 | 23.315 ± 0.415 | +9.414 ± 0.530 | 21.801 | 0.025 | 2219.150 | 19.800 | 21.850 | +6.050 ± 0.564 | 70.549 | 164.950 |
| careful | 23.700 / 39.500 | 1.400 ± 0.266 | — | 9.900 | — | 3.300 | 0.063 | 4.850 | — | 1432.650 | 0.013 | — | 216.400 / 26.850 (24.400 / 23.350) | 23118.504 ± 425.785 | — | 35325.6 ± 855.4 | — | 36.269 | — | 13.901 ± 0.358 | — | 17.763 | 0.002 | 2584.300 | 19.500 | 15.800 | — | 777.141 | 214.700 |
| stamper | 4.250 / 39.950 | 8.200 ± 0.691 | +6.800 ± 0.753 | 115.400 | +105.500 ± 2.733 | 0.000 | 1.000 | 57.400 | +52.550 ± 2.324 | 658.800 | 0.017 | +0.004 ± 0.001 | 243.050 / 162.100 (168.500 / 160.700) | 8453.892 ± 153.707 | -14664.613 ± 401.302 | 7257.2 ± 170.1 | -28068.4 ± 804.7 | 26.992 | -9.277 ± 0.544 | 29.830 ± 0.681 | +15.929 ± 0.820 | 22.472 | 0.259 | 694.950 | 19.950 | 35.700 | +19.900 ± 0.774 | 5671.578 | 146.650 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **greedy**: p0 0.769/0.230/0.001 (608); p1 0.499/0.489/0.012 (482); p2 0.592/0.402/0.007 (318); p3 0.625/0.366/0.009 (302); p4 0.586/0.397/0.017 (316); p5 0.619/0.376/0.005 (308); p6 0.611/0.383/0.006 (311); p7 0.622/0.371/0.008 (318); p8 0.601/0.392/0.007 (316); p9 0.602/0.391/0.007 (318); p10 0.628/0.366/0.006 (304); p11 0.619/0.375/0.006 (278); p12 0.630/0.363/0.006 (195); p13 0.641/0.355/0.003 (61); p14 0.666/0.322/0.013 (16); p15 0.714/0.274/0.011 (9)
- **careful**: p0 1.000/0.000/0.000 (604); p1 1.000/0.000/0.000 (726); p2 1.000/0.000/0.000 (853); p3 1.000/0.000/0.000 (918); p4 1.000/0.000/0.000 (859); p5 1.000/0.000/0.000 (226); p6 1.000/0.000/0.000 (40)
- **stamper**: p0 0.000/1.000/0.000 (577); p1 0.000/1.000/0.000 (306); p2 0.000/1.000/0.000 (163); p3 0.000/1.000/0.000 (27); p4 0.000/1.000/0.000 (9); p5 0.000/1.000/0.000 (2)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 2259.6 / 641.6 | 1.50 / 1.88 | +0.38 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.09 / 0.08 | -0.00 ± 0.00 | 0.547 / 0.624 | +0.077 ± 0.005 | 0.308 / 0.369 | 0.024 / 0.031 | 0.177 / 0.214 | +0.037 ± 0.006 | 3.18 / 3.45 | +0.27 ± 0.05 |
| careful | 2582.8 / 264.4 | 0.37 / 0.24 | -0.14 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.06 / 0.06 | -0.00 ± 0.00 | 0.221 / 0.182 | -0.039 ± 0.006 | 0.086 / 0.096 | 0.002 / 0.001 | 0.066 / 0.074 | +0.008 ± 0.004 | 1.91 / 1.52 | -0.39 ± 0.06 |
| stamper | 899.0 / 153.4 | 1.30 / 0.88 | -0.42 ± 0.05 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.04 / 0.02 | -0.01 ± 0.00 | 0.299 / 0.284 | -0.015 ± 0.010 | 0.173 / 0.172 | 0.226 / 0.315 | 0.110 / 0.078 | -0.032 ± 0.005 | 3.53 / 2.33 | -1.20 ± 0.21 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| greedy | +0.03 ± 0.01 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.047 ± 0.003 | -0.025 ± 0.004 | +0.006 ± 0.004 |
| careful | -0.14 ± 0.02 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.040 ± 0.006 | +0.009 ± 0.004 | +0.008 ± 0.004 |
| stamper | -0.89 ± 0.04 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.171 ± 0.013 | -0.119 ± 0.011 | -0.040 ± 0.004 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| greedy | 0.398 / 0.157 | 0.30 / 0.26 | 0.163 / 0.159 | 0.00 / 0.00 | 0.31 / 0.29 | 0.409 / 0.172 |
| careful | 0.333 / 0.106 | 0.37 / 0.40 | 0.143 / 0.049 | 0.00 / 0.00 | 0.31 / 0.30 | 0.358 / 0.133 |
| stamper | 0.019 / 0.000 | 0.01 / — | 0.267 / 0.753 | 0.00 / 0.00 | 0.00 / — | 1.272 / 1.766 |

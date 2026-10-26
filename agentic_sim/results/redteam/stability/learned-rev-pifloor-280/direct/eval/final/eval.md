# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --dial off`, seeds 21-40, hide ``, model `None` (value off, horizon 8)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | non-initial share | non-initial stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 27705.3 ± 668.7 | -7104.0 ± 783.7 | 2867.4 | 0.565 | 0.431 | 0.004 | 0.393 | 0.412 | 0.060 | 0.835 | 72.50 | 225.65 | 0.15 |
| careful | 34809.2 ± 647.5 | nan ± nan | 4039.6 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.289 | 0.000 | 5.70 | 0.00 | 0.35 |
| stamper | 10017.9 ± 321.2 | -24791.4 ± 621.0 | 1874.0 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.012 | 1.000 | 23.05 | 345.40 | 0.85 |
| hand | 27934.0 ± 1036.9 | -6875.2 ± 1333.2 | 3446.8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.260 | 0.000 | 12.20 | 0.00 | 0.35 |

The stamp rate by seat kind (2.8.0 §5), plant / real, with the decisions pooled over the seeds in parentheses — under 2.7.0 a plant reached the initial review alone; under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| direct | 0.393 (4859) / 0.412 (49057) | 0.903 (134) / 0.945 (2681) | 0.323 (96) / 0.343 (522) | — / — |
| careful | 0.000 (5180) / 0.000 (52256) | 0.000 (575) / 0.000 (18957) | 0.000 (192) / 0.000 (3631) | — / — |
| stamper | 1.000 (3324) / 1.000 (33716) | — / 1.000 (440) | — / — | — / — |
| hand | 0.000 (4595) / 0.000 (46439) | 0.000 (623) / 0.000 (14345) | 0.000 (293) / 0.000 (2640) | — / — |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 0.737 | 0.945 | 0.834 (6549) | 0.805 (1634) | 0.669 (4208) | 0.516 (698) | 0.334 (44260) | 50.150 | 613.150 | 1.632 | 4.500 |
| careful | — | 0.665 | 0.000 (26978) | 0.000 (5546) | 0.000 (4306) | 0.000 (1030) | 0.000 (42931) | 24.850 | 661.650 | 1.211 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (37480) | 86.350 | 352.150 | 2.152 | 4.000 |
| hand | — | 0.761 | 0.000 (16496) | 0.000 (3409) | 0.000 (2965) | 0.000 (652) | 0.000 (45413) | 36.900 | 722.400 | 1.343 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| direct | 39.700 | 0.000 | 0.000 | 0.000 | 0.000 | 0.150 | 0.000 |
| careful | 39.600 | 0.000 | 0.000 | 0.000 | 0.000 | 0.350 | 0.000 |
| stamper | 40.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.850 | 0.000 |
| hand | 39.950 | 0.000 | 0.000 | 0.000 | 0.000 | 0.350 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 22.250 / 39.700 | 72.500 ± 3.602 | +66.800 ± 3.630 | 77.100 | +66.850 ± 1.857 | 1.950 | 0.533 | 30.450 | +25.200 ± 0.970 | 1812.550 | 0.090 | +0.065 ± 0.003 | 0.000 / 0.000 (0.000 / 0.000) | 25456.126 ± 578.383 | +2225.412 ± 514.478 | 27705.3 ± 668.7 | -7104.0 ± 783.7 | 32.421 | -5.351 ± 0.415 | 19.909 ± 0.526 | +5.912 ± 0.562 | 20.786 | 0.001 | 2454.650 | 19.700 | 17.450 | +0.000 ± 0.594 | 179.539 | 105.500 |
| careful | 22.150 / 39.600 | 5.700 ± 0.607 | — | 10.250 | — | 2.850 | 0.046 | 5.250 | — | 1578.650 | 0.025 | — | 0.000 / 0.000 (0.000 / 0.000) | 23230.713 ± 394.109 | — | 34809.2 ± 647.5 | — | 37.772 | — | 13.997 ± 0.283 | — | 17.491 | 0.001 | 2618.250 | 19.600 | 17.450 | — | 1033.546 | 228.900 |
| stamper | 7.750 / 40.000 | 23.050 ± 1.258 | +17.350 ± 1.346 | 124.900 | +114.650 ± 1.667 | 0.000 | 1.000 | 66.350 | +61.100 ± 1.347 | 1683.550 | 0.198 | +0.172 ± 0.003 | 0.000 / 0.000 (0.000 / 0.000) | 14114.807 ± 394.301 | -9115.907 ± 566.436 | 10017.9 ± 321.2 | -24791.4 ± 621.0 | 25.385 | -12.387 ± 0.282 | 32.823 ± 0.595 | +18.826 ± 0.567 | 25.271 | 0.406 | 1023.150 | 20.000 | 32.250 | +14.800 ± 0.854 | 1348.683 | 145.950 |
| hand | 23.950 / 39.950 | 12.200 ± 0.780 | +6.500 ± 1.022 | 51.250 | +41.000 ± 1.892 | 2.100 | 0.128 | 16.950 | +11.700 ± 1.036 | 1714.800 | 0.081 | +0.056 ± 0.002 | 0.000 / 0.000 (0.000 / 0.000) | 26825.087 ± 399.676 | +3594.374 ± 340.909 | 27934.0 ± 1036.9 | -6875.2 ± 1333.2 | 30.928 | -6.844 ± 0.674 | 20.827 ± 0.956 | +6.830 ± 1.039 | 22.744 | 0.050 | 2218.250 | 19.950 | 16.000 | -1.450 ± 0.766 | 237.074 | 262.100 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **direct**: p0 0.826/0.173/0.000 (600); p1 0.464/0.532/0.004 (577); p2 0.569/0.429/0.002 (536); p3 0.486/0.510/0.003 (552); p4 0.460/0.533/0.007 (564); p5 0.548/0.378/0.074 (38)
- **careful**: p0 1.000/0.000/0.000 (594); p1 1.000/0.000/0.000 (748); p2 1.000/0.000/0.000 (870); p3 1.000/0.000/0.000 (896); p4 1.000/0.000/0.000 (772); p5 1.000/0.000/0.000 (158)
- **stamper**: p0 0.000/1.000/0.000 (561); p1 0.000/1.000/0.000 (454); p2 0.000/1.000/0.000 (388); p3 0.000/1.000/0.000 (356); p4 0.000/1.000/0.000 (117)
- **hand**: p0 —/—/— (0); p1 —/—/— (0); p2 —/—/— (0); p3 —/—/— (0); p4 —/—/— (0); p5 —/—/— (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 2452.8 / 242.9 | 0.51 / 0.45 | -0.06 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.02 / 0.01 | -0.01 ± 0.00 | 0.317 / 0.273 | -0.043 ± 0.007 | 0.130 / 0.135 | 0.001 / 0.001 | 0.100 / 0.109 | +0.009 ± 0.003 | 1.88 / 1.72 | -0.15 ± 0.08 |
| careful | 2612.8 / 259.0 | 0.18 / 0.10 | -0.08 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.15 / 0.15 | -0.01 ± 0.00 | 0.130 / 0.101 | -0.029 ± 0.006 | 0.045 / 0.052 | 0.000 / 0.000 | 0.064 / 0.071 | +0.007 ± 0.004 | 1.53 / 1.27 | -0.25 ± 0.07 |
| stamper | 1685.8 / 166.2 | 1.67 / 1.21 | -0.46 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.03 / 0.02 | -0.01 ± 0.00 | 0.502 / 0.400 | -0.103 ± 0.005 | 0.324 / 0.273 | 0.393 / 0.354 | 0.110 / 0.093 | -0.017 ± 0.004 | 4.12 / 2.92 | -1.20 ± 0.26 |
| hand | 2321.9 / 229.8 | 1.34 / 1.14 | -0.20 ± 0.04 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.10 / 0.09 | -0.01 ± 0.01 | 0.399 / 0.342 | -0.057 ± 0.007 | 0.178 / 0.173 | 0.050 / 0.046 | 0.100 / 0.090 | -0.010 ± 0.003 | 3.37 / 3.17 | -0.20 ± 0.14 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| direct | -0.06 ± 0.03 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.044 ± 0.007 | +0.004 ± 0.005 | +0.009 ± 0.003 |
| careful | -0.08 ± 0.02 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.029 ± 0.006 | +0.007 ± 0.003 | +0.007 ± 0.004 |
| stamper | -0.46 ± 0.03 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.103 ± 0.005 | -0.052 ± 0.008 | -0.017 ± 0.004 |
| hand | -0.20 ± 0.04 | +0.00 ± 0.00 | -0.01 ± 0.01 | -0.058 ± 0.007 | -0.005 ± 0.005 | -0.010 ± 0.003 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| direct | 0.054 / 0.028 | 0.61 / 0.80 | 0.026 / 0.008 | 0.00 / 0.00 | 0.58 / 0.62 | 0.817 / 0.642 |
| careful | 0.361 / 0.110 | 0.36 / 0.38 | 0.038 / 0.011 | 0.00 / 0.00 | 0.26 / 0.16 | 0.288 / 0.123 |
| stamper | 0.013 / 0.000 | 0.00 / — | 0.000 / 0.000 | — / — | — / — | 1.213 / 1.725 |
| hand | 0.303 / 0.134 | 0.41 / 0.46 | 0.028 / 0.009 | 0.00 / 0.00 | 0.37 / 0.33 | 0.525 / 0.469 |

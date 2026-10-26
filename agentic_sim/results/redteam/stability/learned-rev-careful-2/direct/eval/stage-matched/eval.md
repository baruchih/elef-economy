# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule`, seeds 21-40, hide ``, model `None` (value off, horizon 8)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the plant-blind seats — a revised submission or a panel, where no plant is received — are read apart: their share of the review decisions and the stamp rate on them.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | blind-seat share | blind-seat stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 30514.5 ± 651.5 | -4836.2 ± 966.6 | 3716.5 | 0.513 | 0.470 | 0.016 | 0.306 | 0.377 | 0.229 | 0.914 | 98.10 | 256.45 | 0.15 |
| hand | 32145.9 ± 593.0 | -3204.8 ± 834.8 | 4447.5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.295 | 0.000 | 11.60 | 0.00 | 0.60 |
| careful | 35350.7 ± 821.3 | nan ± nan | 4122.6 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.292 | 0.000 | 6.30 | 0.00 | 0.45 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 0.858 | 0.952 | 0.820 (1464) | 0.860 (1780) | 0.783 (1416) | 0.661 (20332) | 0.361 (49338) | 45.600 | 314.650 | 1.634 | 5.624 |
| hand | — | 0.803 | 0.000 (113) | 0.000 (11603) | 0.000 (18496) | 0.000 (15352) | 0.000 (43386) | 33.850 | 344.800 | 1.254 | 0.000 |
| careful | — | 0.668 | 0.000 (27448) | 0.000 (5667) | 0.000 (4419) | 0.000 (1173) | 0.000 (43745) | 23.750 | 700.250 | 1.094 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| direct | 39.800 | 0.000 | 0.000 | 0.000 | 0.000 | 0.150 | 0.000 |
| hand | 39.850 | 0.000 | 0.000 | 0.000 | 0.000 | 0.600 | 0.000 |
| careful | 39.600 | 0.000 | 0.000 | 0.000 | 0.000 | 0.450 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 16.650 / 39.800 | 98.100 ± 5.063 | +91.800 ± 5.422 | 145.350 | +136.350 ± 5.344 | 8.400 | 0.287 | 25.800 | +21.650 ± 0.944 | 1797.950 | 0.049 | +0.025 ± 0.004 | 0.000 / 0.000 (0.000 / 0.000) | 32605.033 ± 583.658 | +9993.196 ± 681.425 | 30514.5 ± 651.5 | -4836.2 ± 966.6 | 29.528 | -9.039 ± 0.458 | 23.033 ± 0.655 | +9.334 ± 0.788 | 21.343 | 0.034 | 2187.000 | 19.800 | 23.150 | +5.700 ± 0.553 | 72.888 | 108.550 |
| hand | 19.500 / 39.850 | 11.600 ± 0.666 | +5.300 ± 0.941 | 62.250 | +53.250 ± 2.040 | 6.900 | 0.047 | 14.000 | +9.850 ± 0.933 | 1678.600 | 0.060 | +0.036 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 29714.546 ± 438.122 | +7102.709 ± 376.361 | 32145.9 ± 593.0 | -3204.8 ± 834.8 | 32.740 | -5.828 ± 0.318 | 20.386 ± 0.371 | +6.687 ± 0.456 | 19.478 | 0.010 | 2486.700 | 19.850 | 20.350 | +2.900 ± 0.369 | 86.726 | 150.900 |
| careful | 22.150 / 39.600 | 6.300 ± 0.649 | — | 9.000 | — | 2.600 | 0.044 | 4.150 | — | 1595.100 | 0.024 | — | 0.000 / 0.000 (0.000 / 0.000) | 22611.837 ± 296.550 | — | 35350.7 ± 821.3 | — | 38.567 | — | 13.699 ± 0.397 | — | 16.874 | 0.000 | 2654.200 | 19.600 | 17.450 | — | 1103.486 | 220.800 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **direct**: p0 0.796/0.204/0.000 (608); p1 0.324/0.653/0.023 (551); p2 0.410/0.568/0.022 (335); p3 0.503/0.477/0.020 (252); p4 0.461/0.518/0.021 (259); p5 0.481/0.497/0.022 (251); p6 0.495/0.480/0.026 (241); p7 0.511/0.474/0.015 (240); p8 0.485/0.508/0.008 (239); p9 0.522/0.475/0.003 (232); p10 0.502/0.481/0.017 (226); p11 0.492/0.483/0.025 (162); p12 0.531/0.439/0.031 (83); p13 0.564/0.412/0.024 (31); p14 0.288/0.616/0.096 (6)
- **hand**: p0 —/—/— (0); p1 —/—/— (0); p2 —/—/— (0); p3 —/—/— (0); p4 —/—/— (0); p5 —/—/— (0); p6 —/—/— (0); p7 —/—/— (0); p8 —/—/— (0); p9 —/—/— (0); p10 —/—/— (0); p11 —/—/— (0); p12 —/—/— (0); p13 —/—/— (0); p14 —/—/— (0)
- **careful**: p0 1.000/0.000/0.000 (622); p1 1.000/0.000/0.000 (758); p2 1.000/0.000/0.000 (860); p3 1.000/0.000/0.000 (866); p4 1.000/0.000/0.000 (750); p5 1.000/0.000/0.000 (254); p6 1.000/0.000/0.000 (12)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling the requester's wallet refused to raise at least once (never a plant's: its raise is minted — §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 2253.9 / 611.5 | 1.34 / 1.68 | +0.34 ± 0.06 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.07 / 0.07 | +0.01 ± 0.00 | 0.458 / 0.565 | +0.107 ± 0.009 | 0.265 / 0.000 | 0.034 / 0.063 | 0.162 / 0.197 | +0.035 ± 0.006 | 3.24 / 3.43 | +0.19 ± 0.08 |
| hand | 2502.1 / 631.4 | 0.54 / 0.45 | -0.09 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.14 / 0.16 | +0.02 ± 0.00 | 0.310 / 0.325 | +0.015 ± 0.005 | 0.128 / 0.000 | 0.010 / 0.013 | 0.089 / 0.078 | -0.011 ± 0.003 | 2.22 / 2.11 | -0.11 ± 0.08 |
| careful | 2649.1 / 267.9 | 0.14 / 0.07 | -0.07 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.07 / 0.07 | +0.00 ± 0.00 | 0.119 / 0.122 | +0.003 ± 0.003 | 0.038 / 0.000 | 0.000 / 0.000 | 0.060 / 0.059 | -0.001 ± 0.003 | 1.33 / 1.15 | -0.18 ± 0.05 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| direct | -0.14 ± 0.05 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.044 ± 0.004 | -0.360 ± 0.023 | -0.004 ± 0.005 |
| hand | -0.16 ± 0.02 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.027 ± 0.003 | -0.149 ± 0.014 | -0.011 ± 0.003 |
| careful | -0.07 ± 0.02 | +0.00 ± 0.00 | +0.00 ± 0.00 | +0.001 ± 0.003 | -0.039 ± 0.007 | -0.001 ± 0.003 |

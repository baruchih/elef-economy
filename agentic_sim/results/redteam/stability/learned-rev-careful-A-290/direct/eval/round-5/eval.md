# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --planted-lie off`, seeds 21-40, hide ``, model `None` (value off, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | non-initial share | non-initial stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 28234.5 ± 539.2 | -8160.0 ± 683.1 | 3548.2 | 0.730 | 0.260 | 0.011 | 0.201 | 0.218 | 0.144 | 0.604 | 26.50 | 114.40 | 0.05 |
| careful | 36394.5 ± 672.3 | nan ± nan | 4082.5 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.297 | 0.000 | 6.55 | 0.00 | 0.50 |
| stamper | 6949.2 ± 182.7 | -29445.3 ± 715.0 | 1082.4 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.020 | 1.000 | 14.90 | 183.85 | 1.00 |

The stamp rate by seat kind (2.8.0 §5), plant / real, with the decisions pooled over the seeds in parentheses — under 2.7.0 a plant reached the initial review alone; under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| direct | 0.201 (13849) / 0.218 (46921) | 0.664 (1524) / 0.727 (6582) | 0.123 (845) / 0.207 (1243) | — / — |
| careful | 0.000 (5288) / 0.000 (52128) | 0.000 (1186) / 0.000 (18613) | 0.000 (787) / 0.000 (3648) | — / — |
| stamper | 1.000 (3131) / 1.000 (18077) | — / 1.000 (440) | — / — | — / — |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 0.928 | 0.956 | 0.673 (49) | 0.683 (218) | 0.608 (316) | 0.334 (16402) | 0.233 (53979) | 39.550 | 274.700 | 1.610 | 2.893 |
| careful | — | 0.679 | 0.000 (25511) | 0.000 (5997) | 0.000 (4476) | 0.000 (1099) | 0.000 (44567) | 25.000 | 712.900 | 1.154 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (21648) | 77.150 | 179.100 | 2.187 | 2.383 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| direct | 39.850 | 0.000 | 0.000 | 0.000 | 0.000 | 0.050 | 0.000 |
| careful | 39.650 | 0.000 | 0.000 | 0.000 | 0.000 | 0.500 | 0.000 |
| stamper | 40.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 18.550 / 39.850 | 26.500 ± 1.360 | +19.950 ± 1.260 | 121.350 | +111.600 ± 3.660 | 9.650 | 0.218 | 19.700 | +14.350 ± 0.853 | 1804.500 | 0.059 | +0.035 ± 0.002 | 0.000 / 0.000 (0.000 / 0.000) | 28336.263 ± 351.006 | +4449.490 ± 424.056 | 28234.5 ± 539.2 | -8160.0 ± 683.1 | 30.567 | -6.552 ± 0.378 | 21.817 ± 0.391 | +8.032 ± 0.383 | 20.334 | 0.025 | 2294.800 | 19.850 | 21.300 | +4.500 ± 0.560 | 71.621 | 108.250 |
| careful | 22.850 / 39.650 | 6.550 ± 0.521 | — | 9.750 | — | 3.600 | 0.050 | 5.350 | — | 1609.600 | 0.024 | — | 0.000 / 0.000 (0.000 / 0.000) | 23886.773 ± 334.972 | — | 36394.5 ± 672.3 | — | 37.118 | — | 13.784 ± 0.259 | — | 17.787 | 0.001 | 2609.350 | 19.650 | 16.800 | — | 894.930 | 193.150 |
| stamper | 3.750 / 40.000 | 14.900 ± 1.090 | +8.350 ± 1.195 | 115.600 | +105.850 ± 2.486 | 0.000 | 1.000 | 57.150 | +51.800 ± 2.295 | 903.900 | 0.191 | +0.167 ± 0.003 | 0.000 / 0.000 (0.000 / 0.000) | 9080.821 ± 214.040 | -14805.952 ± 389.991 | 6949.2 ± 182.7 | -29445.3 ± 715.0 | 26.326 | -10.792 ± 0.499 | 33.101 ± 0.810 | +19.317 ± 0.895 | 22.927 | 0.239 | 717.950 | 20.000 | 36.250 | +19.450 ± 0.947 | 5556.698 | 136.250 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **direct**: p0 0.774/0.226/0.000 (580); p1 0.624/0.366/0.010 (374); p2 0.675/0.312/0.012 (246); p3 0.644/0.343/0.013 (241); p4 0.680/0.310/0.010 (230); p5 0.681/0.309/0.010 (232); p6 0.727/0.254/0.020 (218); p7 0.743/0.244/0.013 (220); p8 0.773/0.212/0.015 (206); p9 0.772/0.216/0.012 (212); p10 0.811/0.177/0.012 (199); p11 0.803/0.185/0.012 (193); p12 0.784/0.204/0.012 (187); p13 0.781/0.213/0.006 (133); p14 0.786/0.203/0.011 (70); p15 0.754/0.246/0.000 (7)
- **careful**: p0 1.000/0.000/0.000 (599); p1 1.000/0.000/0.000 (727); p2 1.000/0.000/0.000 (853); p3 1.000/0.000/0.000 (902); p4 1.000/0.000/0.000 (767); p5 1.000/0.000/0.000 (217); p6 1.000/0.000/0.000 (17)
- **stamper**: p0 0.000/1.000/0.000 (561); p1 0.000/1.000/0.000 (305); p2 0.000/1.000/0.000 (169); p3 0.000/1.000/0.000 (40); p4 0.000/1.000/0.000 (6); p5 0.000/1.000/0.000 (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 2346.1 / 692.5 | 1.18 / 1.54 | +0.36 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.04 / 0.02 | -0.01 ± 0.00 | 0.485 / 0.564 | +0.079 ± 0.009 | 0.274 / 0.331 | 0.025 / 0.000 | 0.161 / 0.189 | +0.028 ± 0.004 | 2.81 / 3.13 | +0.32 ± 0.04 |
| careful | 2606.4 / 264.4 | 0.29 / 0.19 | -0.10 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.07 / 0.07 | -0.00 ± 0.00 | 0.174 / 0.138 | -0.036 ± 0.005 | 0.065 / 0.074 | 0.001 / 0.000 | 0.063 / 0.060 | -0.003 ± 0.004 | 1.61 / 1.36 | -0.26 ± 0.08 |
| stamper | 903.9 / 156.6 | 1.11 / 0.80 | -0.31 ± 0.04 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.04 / 0.02 | -0.01 ± 0.00 | 0.233 / 0.235 | +0.002 ± 0.012 | 0.137 / 0.151 | 0.205 / 0.000 | 0.100 / 0.072 | -0.028 ± 0.005 | 3.62 / 2.14 | -1.48 ± 0.28 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| direct | +0.06 ± 0.01 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.043 ± 0.003 | -0.019 ± 0.004 | +0.004 ± 0.003 |
| careful | -0.09 ± 0.02 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.033 ± 0.005 | +0.010 ± 0.004 | -0.003 ± 0.004 |
| stamper | -0.83 ± 0.05 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.146 ± 0.016 | -0.094 ± 0.011 | -0.037 ± 0.005 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| direct | 0.139 / 0.082 | 0.61 / 0.64 | 0.035 / 0.014 | 0.00 / 0.00 | 0.67 / 0.67 | 0.744 / 0.616 |
| careful | 0.355 / 0.116 | 0.38 / 0.44 | 0.040 / 0.013 | 0.00 / 0.00 | 0.31 / 0.33 | 0.312 / 0.225 |
| stamper | 0.024 / 0.000 | 0.00 / — | 0.000 / 0.000 | — / — | — / — | 1.197 / 1.947 |

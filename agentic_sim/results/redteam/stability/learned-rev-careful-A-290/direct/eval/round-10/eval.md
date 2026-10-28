# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --planted-lie off`, seeds 21-40, hide ``, model `None` (value off, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | non-initial share | non-initial stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 28818.6 ± 686.6 | -7575.8 ± 733.3 | 3433.6 | 0.717 | 0.274 | 0.009 | 0.197 | 0.235 | 0.125 | 0.668 | 26.70 | 121.85 | 0.15 |
| careful | 36394.5 ± 672.3 | nan ± nan | 4082.5 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.297 | 0.000 | 6.55 | 0.00 | 0.50 |
| stamper | 6949.2 ± 182.7 | -29445.3 ± 715.0 | 1082.4 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.020 | 1.000 | 14.90 | 183.85 | 1.00 |

The stamp rate by seat kind (2.8.0 §5), plant / real, with the decisions pooled over the seeds in parentheses — under 2.7.0 a plant reached the initial review alone; under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| direct | 0.197 (13051) / 0.235 (47043) | 0.764 (1273) / 0.789 (5595) | 0.140 (665) / 0.238 (1045) | — / — |
| careful | 0.000 (5288) / 0.000 (52128) | 0.000 (1186) / 0.000 (18613) | 0.000 (787) / 0.000 (3648) | — / — |
| stamper | 1.000 (3131) / 1.000 (18077) | — / 1.000 (440) | — / — | — / — |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 0.925 | 0.955 | 0.615 (161) | 0.615 (455) | 0.665 (480) | 0.330 (15203) | 0.249 (52373) | 38.950 | 328.300 | 1.594 | 3.128 |
| careful | — | 0.679 | 0.000 (25511) | 0.000 (5997) | 0.000 (4476) | 0.000 (1099) | 0.000 (44567) | 25.000 | 712.900 | 1.154 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (21648) | 77.150 | 179.100 | 2.187 | 2.383 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| direct | 39.800 | 0.000 | 0.000 | 0.000 | 0.000 | 0.150 | 0.000 |
| careful | 39.650 | 0.000 | 0.000 | 0.000 | 0.000 | 0.500 | 0.000 |
| stamper | 40.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 19.500 / 39.800 | 26.700 ± 1.499 | +20.150 ± 1.541 | 108.750 | +99.000 ± 2.511 | 9.150 | 0.197 | 19.150 | +13.800 ± 0.860 | 1819.550 | 0.063 | +0.039 ± 0.003 | 0.000 / 0.000 (0.000 / 0.000) | 28031.182 ± 434.295 | +4144.409 ± 469.536 | 28818.6 ± 686.6 | -7575.8 ± 733.3 | 30.603 | -6.515 ± 0.444 | 21.206 ± 0.532 | +7.422 ± 0.600 | 20.525 | 0.019 | 2315.650 | 19.800 | 20.300 | +3.500 ± 0.675 | 63.318 | 154.050 |
| careful | 22.850 / 39.650 | 6.550 ± 0.521 | — | 9.750 | — | 3.600 | 0.050 | 5.350 | — | 1609.600 | 0.024 | — | 0.000 / 0.000 (0.000 / 0.000) | 23886.773 ± 334.972 | — | 36394.5 ± 672.3 | — | 37.118 | — | 13.784 ± 0.259 | — | 17.787 | 0.001 | 2609.350 | 19.650 | 16.800 | — | 894.930 | 193.150 |
| stamper | 3.750 / 40.000 | 14.900 ± 1.090 | +8.350 ± 1.195 | 115.600 | +105.850 ± 2.486 | 0.000 | 1.000 | 57.150 | +51.800 ± 2.295 | 903.900 | 0.191 | +0.167 ± 0.003 | 0.000 / 0.000 (0.000 / 0.000) | 9080.821 ± 214.040 | -14805.952 ± 389.991 | 6949.2 ± 182.7 | -29445.3 ± 715.0 | 26.326 | -10.792 ± 0.499 | 33.101 ± 0.810 | +19.317 ± 0.895 | 22.927 | 0.239 | 717.950 | 20.000 | 36.250 | +19.450 ± 0.947 | 5556.698 | 136.250 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **direct**: p0 0.777/0.223/0.001 (589); p1 0.570/0.408/0.021 (429); p2 0.659/0.332/0.010 (283); p3 0.672/0.309/0.019 (229); p4 0.684/0.308/0.008 (219); p5 0.738/0.253/0.009 (212); p6 0.752/0.241/0.006 (217); p7 0.748/0.248/0.004 (208); p8 0.749/0.247/0.005 (211); p9 0.776/0.221/0.003 (199); p10 0.771/0.224/0.005 (198); p11 0.759/0.230/0.012 (193); p12 0.751/0.244/0.006 (141); p13 0.753/0.227/0.020 (83); p14 0.793/0.195/0.012 (21)
- **careful**: p0 1.000/0.000/0.000 (599); p1 1.000/0.000/0.000 (727); p2 1.000/0.000/0.000 (853); p3 1.000/0.000/0.000 (902); p4 1.000/0.000/0.000 (767); p5 1.000/0.000/0.000 (217); p6 1.000/0.000/0.000 (17)
- **stamper**: p0 0.000/1.000/0.000 (561); p1 0.000/1.000/0.000 (305); p2 0.000/1.000/0.000 (169); p3 0.000/1.000/0.000 (40); p4 0.000/1.000/0.000 (6); p5 0.000/1.000/0.000 (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 2352.2 / 652.5 | 1.09 / 1.41 | +0.31 ± 0.04 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.03 / 0.02 | -0.01 ± 0.00 | 0.468 / 0.538 | +0.070 ± 0.011 | 0.263 / 0.321 | 0.019 / 0.000 | 0.150 / 0.188 | +0.038 ± 0.005 | 2.70 / 2.89 | +0.19 ± 0.06 |
| careful | 2606.4 / 264.4 | 0.29 / 0.19 | -0.10 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.07 / 0.07 | -0.00 ± 0.00 | 0.174 / 0.138 | -0.036 ± 0.005 | 0.065 / 0.074 | 0.001 / 0.000 | 0.063 / 0.060 | -0.003 ± 0.004 | 1.61 / 1.36 | -0.26 ± 0.08 |
| stamper | 903.9 / 156.6 | 1.11 / 0.80 | -0.31 ± 0.04 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.04 / 0.02 | -0.01 ± 0.00 | 0.233 / 0.235 | +0.002 ± 0.012 | 0.137 / 0.151 | 0.205 / 0.000 | 0.100 / 0.072 | -0.028 ± 0.005 | 3.62 / 2.14 | -1.48 ± 0.28 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| direct | +0.04 ± 0.02 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.054 ± 0.005 | -0.021 ± 0.004 | +0.014 ± 0.004 |
| careful | -0.09 ± 0.02 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.033 ± 0.005 | +0.010 ± 0.004 | -0.003 ± 0.004 |
| stamper | -0.83 ± 0.05 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.146 ± 0.016 | -0.094 ± 0.011 | -0.037 ± 0.005 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| direct | 0.118 / 0.068 | 0.59 / 0.64 | 0.035 / 0.014 | 0.00 / 0.00 | 0.67 / 0.54 | 0.778 / 0.658 |
| careful | 0.355 / 0.116 | 0.38 / 0.44 | 0.040 / 0.013 | 0.00 / 0.00 | 0.31 / 0.33 | 0.312 / 0.225 |
| stamper | 0.024 / 0.000 | 0.00 / — | 0.000 / 0.000 | — / — | — / — | 1.197 / 1.947 |

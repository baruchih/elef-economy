# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --planted-lie off`, seeds 21-40, hide ``, model `results/redteam/stability/learned-rev-careful-A-290/wm/models/wm-online-10.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | non-initial share | non-initial stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 26859.1 ± 400.9 | -9535.4 ± 611.3 | 3296.1 | 0.723 | 0.277 | 0.000 | 0.168 | 0.211 | 0.137 | 0.753 | 24.65 | 109.25 | 0.05 |
| careful | 36394.5 ± 672.3 | nan ± nan | 4082.5 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.297 | 0.000 | 6.55 | 0.00 | 0.50 |
| stamper | 6949.2 ± 182.7 | -29445.3 ± 715.0 | 1082.4 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.020 | 1.000 | 14.90 | 183.85 | 1.00 |

The stamp rate by seat kind (2.8.0 §5), plant / real, with the decisions pooled over the seeds in parentheses — under 2.7.0 a plant reached the initial review alone; under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| greedy | 0.168 (11970) / 0.211 (44911) | 0.925 (1369) / 0.868 (6215) | 0.073 (519) / 0.115 (938) | — / — |
| careful | 0.000 (5288) / 0.000 (52128) | 0.000 (1186) / 0.000 (18613) | 0.000 (787) / 0.000 (3648) | — / — |
| stamper | 1.000 (3131) / 1.000 (18077) | — / 1.000 (440) | — / — | — / — |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 0.898 | 0.940 | 0.564 (353) | 0.709 (443) | 0.551 (960) | 0.340 (18072) | 0.240 (46094) | 44.950 | 285.000 | 1.726 | 2.430 |
| careful | — | 0.679 | 0.000 (25511) | 0.000 (5997) | 0.000 (4476) | 0.000 (1099) | 0.000 (44567) | 25.000 | 712.900 | 1.154 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (21648) | 77.150 | 179.100 | 2.187 | 2.383 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| greedy | 39.800 | 0.000 | 0.000 | 0.000 | 0.000 | 0.050 | 0.000 |
| careful | 39.650 | 0.000 | 0.000 | 0.000 | 0.000 | 0.500 | 0.000 |
| stamper | 40.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 17.400 / 39.800 | 24.650 ± 1.082 | +18.100 ± 1.289 | 94.550 | +84.800 ± 2.741 | 5.850 | 0.160 | 25.150 | +19.800 ± 0.835 | 1731.300 | 0.059 | +0.035 ± 0.002 | 0.000 / 0.000 (0.000 / 0.000) | 28907.843 ± 414.701 | +5021.070 ± 354.467 | 26859.1 ± 400.9 | -9535.4 ± 611.3 | 29.462 | -7.656 ± 0.363 | 23.177 ± 0.224 | +9.393 ± 0.330 | 21.585 | 0.048 | 2143.800 | 19.800 | 22.400 | +5.600 ± 0.432 | 67.026 | 140.000 |
| careful | 22.850 / 39.650 | 6.550 ± 0.521 | — | 9.750 | — | 3.600 | 0.050 | 5.350 | — | 1609.600 | 0.024 | — | 0.000 / 0.000 (0.000 / 0.000) | 23886.773 ± 334.972 | — | 36394.5 ± 672.3 | — | 37.118 | — | 13.784 ± 0.259 | — | 17.787 | 0.001 | 2609.350 | 19.650 | 16.800 | — | 894.930 | 193.150 |
| stamper | 3.750 / 40.000 | 14.900 ± 1.090 | +8.350 ± 1.195 | 115.600 | +105.850 ± 2.486 | 0.000 | 1.000 | 57.150 | +51.800 ± 2.295 | 903.900 | 0.191 | +0.167 ± 0.003 | 0.000 / 0.000 (0.000 / 0.000) | 9080.821 ± 214.040 | -14805.952 ± 389.991 | 6949.2 ± 182.7 | -29445.3 ± 715.0 | 26.326 | -10.792 ± 0.499 | 33.101 ± 0.810 | +19.317 ± 0.895 | 22.927 | 0.239 | 717.950 | 20.000 | 36.250 | +19.450 ± 0.947 | 5556.698 | 136.250 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **greedy**: p0 0.874/0.126/0.000 (591); p1 0.448/0.551/0.001 (461); p2 0.617/0.383/0.000 (298); p3 0.678/0.322/0.000 (231); p4 0.725/0.275/0.000 (218); p5 0.730/0.270/0.000 (218); p6 0.788/0.212/0.000 (212); p7 0.815/0.185/0.000 (210); p8 0.783/0.217/0.000 (218); p9 0.752/0.248/0.000 (219); p10 0.805/0.195/0.000 (203); p11 0.770/0.230/0.000 (141); p12 0.729/0.271/0.000 (65); p13 0.735/0.265/0.000 (12)
- **careful**: p0 1.000/0.000/0.000 (599); p1 1.000/0.000/0.000 (727); p2 1.000/0.000/0.000 (853); p3 1.000/0.000/0.000 (902); p4 1.000/0.000/0.000 (767); p5 1.000/0.000/0.000 (217); p6 1.000/0.000/0.000 (17)
- **stamper**: p0 0.000/1.000/0.000 (561); p1 0.000/1.000/0.000 (305); p2 0.000/1.000/0.000 (169); p3 0.000/1.000/0.000 (40); p4 0.000/1.000/0.000 (6); p5 0.000/1.000/0.000 (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 2245.6 / 598.5 | 1.57 / 2.16 | +0.59 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.04 / 0.03 | -0.01 ± 0.00 | 0.533 / 0.628 | +0.096 ± 0.006 | 0.314 / 0.391 | 0.048 / 0.000 | 0.193 / 0.248 | +0.055 ± 0.004 | 3.38 / 3.79 | +0.41 ± 0.03 |
| careful | 2606.4 / 264.4 | 0.29 / 0.19 | -0.10 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.07 / 0.07 | -0.00 ± 0.00 | 0.174 / 0.138 | -0.036 ± 0.005 | 0.065 / 0.074 | 0.001 / 0.000 | 0.063 / 0.060 | -0.003 ± 0.004 | 1.61 / 1.36 | -0.26 ± 0.08 |
| stamper | 903.9 / 156.6 | 1.11 / 0.80 | -0.31 ± 0.04 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.04 / 0.02 | -0.01 ± 0.00 | 0.233 / 0.235 | +0.002 ± 0.012 | 0.137 / 0.151 | 0.205 / 0.000 | 0.100 / 0.072 | -0.028 ± 0.005 | 3.62 / 2.14 | -1.48 ± 0.28 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| greedy | +0.09 ± 0.02 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.047 ± 0.003 | -0.025 ± 0.003 | +0.011 ± 0.004 |
| careful | -0.09 ± 0.02 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.033 ± 0.005 | +0.010 ± 0.004 | -0.003 ± 0.004 |
| stamper | -0.83 ± 0.05 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.146 ± 0.016 | -0.094 ± 0.011 | -0.037 ± 0.005 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| greedy | 0.136 / 0.077 | 0.55 / 0.55 | 0.028 / 0.010 | 0.00 / 0.00 | 0.47 / 0.83 | 0.741 / 0.601 |
| careful | 0.355 / 0.116 | 0.38 / 0.44 | 0.040 / 0.013 | 0.00 / 0.00 | 0.31 / 0.33 | 0.312 / 0.225 |
| stamper | 0.024 / 0.000 | 0.00 / — | 0.000 / 0.000 | — / — | — / — | 1.197 / 1.947 |

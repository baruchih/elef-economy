# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --planted-lie off`, seeds 21-40, hide ``, model `results/redteam/stability/learned-rev-careful-A-290/wm/models/wm-online-5.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | non-initial share | non-initial stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 26766.9 ± 374.8 | -9627.6 ± 636.5 | 3337.6 | 0.722 | 0.278 | 0.000 | 0.159 | 0.201 | 0.150 | 0.760 | 26.70 | 107.30 | 0.05 |
| careful | 36394.5 ± 672.3 | nan ± nan | 4082.5 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.297 | 0.000 | 6.55 | 0.00 | 0.50 |
| stamper | 6949.2 ± 182.7 | -29445.3 ± 715.0 | 1082.4 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.020 | 1.000 | 14.90 | 183.85 | 1.00 |

The stamp rate by seat kind (2.8.0 §5), plant / real, with the decisions pooled over the seeds in parentheses — under 2.7.0 a plant reached the initial review alone; under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| greedy | 0.159 (12251) / 0.201 (44501) | 0.874 (1558) / 0.879 (6918) | 0.080 (522) / 0.116 (1001) | — / — |
| careful | 0.000 (5288) / 0.000 (52128) | 0.000 (1186) / 0.000 (18613) | 0.000 (787) / 0.000 (3648) | — / — |
| stamper | 1.000 (3131) / 1.000 (18077) | — / 1.000 (440) | — / — | — / — |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 0.897 | 0.934 | 0.701 (137) | 0.719 (270) | 0.556 (516) | 0.336 (21361) | 0.241 (44467) | 42.900 | 254.250 | 1.728 | 2.501 |
| careful | — | 0.679 | 0.000 (25511) | 0.000 (5997) | 0.000 (4476) | 0.000 (1099) | 0.000 (44567) | 25.000 | 712.900 | 1.154 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (21648) | 77.150 | 179.100 | 2.187 | 2.383 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| greedy | 39.700 | 0.000 | 0.000 | 0.000 | 0.000 | 0.050 | 0.000 |
| careful | 39.650 | 0.000 | 0.000 | 0.000 | 0.000 | 0.500 | 0.000 |
| stamper | 40.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 17.250 / 39.700 | 26.700 ± 1.543 | +20.150 ± 1.494 | 91.850 | +82.100 ± 1.945 | 7.350 | 0.194 | 23.200 | +17.850 ± 0.792 | 1688.850 | 0.057 | +0.033 ± 0.003 | 0.000 / 0.000 (0.000 / 0.000) | 29541.108 ± 327.016 | +5654.335 ± 436.861 | 26766.9 ± 374.8 | -9627.6 ± 636.5 | 29.053 | -8.065 ± 0.427 | 23.708 ± 0.243 | +9.924 ± 0.370 | 21.883 | 0.050 | 2119.800 | 19.700 | 22.450 | +5.650 ± 0.372 | 72.018 | 139.700 |
| careful | 22.850 / 39.650 | 6.550 ± 0.521 | — | 9.750 | — | 3.600 | 0.050 | 5.350 | — | 1609.600 | 0.024 | — | 0.000 / 0.000 (0.000 / 0.000) | 23886.773 ± 334.972 | — | 36394.5 ± 672.3 | — | 37.118 | — | 13.784 ± 0.259 | — | 17.787 | 0.001 | 2609.350 | 19.650 | 16.800 | — | 894.930 | 193.150 |
| stamper | 3.750 / 40.000 | 14.900 ± 1.090 | +8.350 ± 1.195 | 115.600 | +105.850 ± 2.486 | 0.000 | 1.000 | 57.150 | +51.800 ± 2.295 | 903.900 | 0.191 | +0.167 ± 0.003 | 0.000 / 0.000 (0.000 / 0.000) | 9080.821 ± 214.040 | -14805.952 ± 389.991 | 6949.2 ± 182.7 | -29445.3 ± 715.0 | 26.326 | -10.792 ± 0.499 | 33.101 ± 0.810 | +19.317 ± 0.895 | 22.927 | 0.239 | 717.950 | 20.000 | 36.250 | +19.450 ± 0.947 | 5556.698 | 136.250 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **greedy**: p0 0.836/0.164/0.000 (588); p1 0.438/0.562/0.000 (409); p2 0.647/0.352/0.001 (262); p3 0.734/0.263/0.003 (236); p4 0.732/0.267/0.001 (236); p5 0.769/0.231/0.000 (218); p6 0.790/0.210/0.000 (225); p7 0.766/0.234/0.000 (225); p8 0.775/0.225/0.000 (225); p9 0.755/0.245/0.000 (227); p10 0.740/0.260/0.000 (205); p11 0.775/0.225/0.000 (153); p12 0.705/0.295/0.000 (104); p13 0.754/0.246/0.000 (27)
- **careful**: p0 1.000/0.000/0.000 (599); p1 1.000/0.000/0.000 (727); p2 1.000/0.000/0.000 (853); p3 1.000/0.000/0.000 (902); p4 1.000/0.000/0.000 (767); p5 1.000/0.000/0.000 (217); p6 1.000/0.000/0.000 (17)
- **stamper**: p0 0.000/1.000/0.000 (561); p1 0.000/1.000/0.000 (305); p2 0.000/1.000/0.000 (169); p3 0.000/1.000/0.000 (40); p4 0.000/1.000/0.000 (6); p5 0.000/1.000/0.000 (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 2225.1 / 612.5 | 1.65 / 2.19 | +0.54 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.05 / 0.04 | -0.01 ± 0.00 | 0.549 / 0.650 | +0.100 ± 0.006 | 0.338 / 0.412 | 0.050 / 0.000 | 0.207 / 0.253 | +0.046 ± 0.005 | 3.41 / 3.65 | +0.24 ± 0.04 |
| careful | 2606.4 / 264.4 | 0.29 / 0.19 | -0.10 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.07 / 0.07 | -0.00 ± 0.00 | 0.174 / 0.138 | -0.036 ± 0.005 | 0.065 / 0.074 | 0.001 / 0.000 | 0.063 / 0.060 | -0.003 ± 0.004 | 1.61 / 1.36 | -0.26 ± 0.08 |
| stamper | 903.9 / 156.6 | 1.11 / 0.80 | -0.31 ± 0.04 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.04 / 0.02 | -0.01 ± 0.00 | 0.233 / 0.235 | +0.002 ± 0.012 | 0.137 / 0.151 | 0.205 / 0.000 | 0.100 / 0.072 | -0.028 ± 0.005 | 3.62 / 2.14 | -1.48 ± 0.28 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| greedy | +0.08 ± 0.02 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.044 ± 0.003 | -0.028 ± 0.004 | +0.003 ± 0.005 |
| careful | -0.09 ± 0.02 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.033 ± 0.005 | +0.010 ± 0.004 | -0.003 ± 0.004 |
| stamper | -0.83 ± 0.05 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.146 ± 0.016 | -0.094 ± 0.011 | -0.037 ± 0.005 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| greedy | 0.154 / 0.087 | 0.52 / 0.56 | 0.030 / 0.012 | 0.00 / 0.00 | 0.50 / 0.41 | 0.708 / 0.568 |
| careful | 0.355 / 0.116 | 0.38 / 0.44 | 0.040 / 0.013 | 0.00 / 0.00 | 0.31 / 0.33 | 0.312 / 0.225 |
| stamper | 0.024 / 0.000 | 0.00 / — | 0.000 / 0.000 | — / — | — / — | 1.197 / 1.947 |

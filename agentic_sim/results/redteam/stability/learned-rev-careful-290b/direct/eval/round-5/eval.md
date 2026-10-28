# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule`, seeds 21-40, hide ``, model `None` (value off, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | non-initial share | non-initial stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 28697.1 ± 642.4 | -6912.9 ± 826.2 | 3321.9 | 0.692 | 0.297 | 0.011 | 0.227 | 0.267 | 0.125 | 0.649 | 30.45 | 137.80 | 0.05 |
| careful | 35610.0 ± 690.2 | nan ± nan | 4142.1 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.300 | 0.000 | 6.10 | 0.00 | 0.30 |
| stamper | 7201.6 ± 143.3 | -28408.4 ± 730.6 | 1082.3 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.020 | 1.000 | 15.40 | 180.80 | 1.00 |

The stamp rate by seat kind (2.8.0 §5), plant / real, with the decisions pooled over the seeds in parentheses — under 2.7.0 a plant reached the initial review alone; under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| direct | 0.227 (11828) / 0.267 (46282) | 0.704 (915) / 0.759 (5724) | 0.219 (549) / 0.262 (1141) | — / — |
| careful | 0.000 (5358) / 0.000 (52610) | 0.000 (945) / 0.000 (18926) | 0.000 (1365) / 0.000 (3638) | — / — |
| stamper | 1.000 (3123) / 1.000 (18084) | — / 1.000 (440) | — / — | — / — |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 0.919 | 0.958 | 0.700 (686) | 0.679 (324) | 0.752 (577) | 0.347 (12764) | 0.272 (52088) | 42.000 | 351.850 | 1.662 | 3.281 |
| careful | — | 0.683 | 0.000 (25992) | 0.000 (5627) | 0.000 (4615) | 0.000 (1110) | 0.000 (45498) | 25.300 | 722.750 | 1.157 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (21647) | 79.450 | 181.000 | 2.161 | 2.276 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| direct | 39.850 | 0.000 | 0.000 | 0.000 | 0.000 | 0.050 | 0.000 |
| careful | 39.650 | 0.000 | 0.000 | 0.000 | 0.000 | 0.300 | 0.000 |
| stamper | 40.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 19.100 / 39.850 | 30.450 ± 1.607 | +24.350 ± 1.758 | 109.800 | +99.350 ± 2.180 | 8.600 | 0.191 | 22.150 | +16.500 ± 1.070 | 1805.850 | 0.066 | +0.042 ± 0.002 | 0.000 / 0.000 (0.000 / 0.000) | 28003.189 ± 373.817 | +4284.376 ± 417.018 | 28697.1 ± 642.4 | -6912.9 ± 826.2 | 30.158 | -7.209 ± 0.460 | 21.064 ± 0.469 | +6.889 ± 0.613 | 21.092 | 0.026 | 2261.000 | 19.850 | 20.750 | +4.250 ± 0.491 | 59.005 | 120.450 |
| careful | 23.150 / 39.650 | 6.100 ± 0.355 | — | 10.450 | — | 3.400 | 0.055 | 5.650 | — | 1630.350 | 0.024 | — | 0.000 / 0.000 (0.000 / 0.000) | 23718.813 ± 303.512 | — | 35610.0 ± 690.2 | — | 37.367 | — | 14.175 ± 0.294 | — | 17.614 | 0.001 | 2633.550 | 19.650 | 16.500 | — | 903.473 | 232.300 |
| stamper | 2.900 / 40.000 | 15.400 ± 0.890 | +9.300 ± 0.924 | 118.450 | +108.000 ± 1.989 | 0.000 | 1.000 | 59.450 | +53.800 ± 1.773 | 904.200 | 0.187 | +0.162 ± 0.003 | 0.000 / 0.000 (0.000 / 0.000) | 9117.372 ± 129.526 | -14601.441 ± 268.742 | 7201.6 ± 143.3 | -28408.4 ± 730.6 | 26.578 | -10.788 ± 0.365 | 31.736 ± 0.665 | +17.561 ± 0.828 | 22.601 | 0.236 | 720.600 | 20.000 | 37.100 | +20.600 ± 0.525 | 5594.089 | 108.100 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **direct**: p0 0.849/0.150/0.001 (591); p1 0.457/0.523/0.019 (529); p2 0.575/0.413/0.012 (309); p3 0.765/0.230/0.005 (224); p4 0.672/0.307/0.020 (224); p5 0.660/0.327/0.013 (215); p6 0.720/0.264/0.016 (205); p7 0.728/0.255/0.017 (208); p8 0.729/0.257/0.014 (214); p9 0.801/0.194/0.005 (204); p10 0.739/0.252/0.008 (200); p11 0.746/0.245/0.009 (142); p12 0.735/0.248/0.017 (47); p13 0.687/0.313/0.000 (9)
- **careful**: p0 1.000/0.000/0.000 (590); p1 1.000/0.000/0.000 (737); p2 1.000/0.000/0.000 (863); p3 1.000/0.000/0.000 (903); p4 1.000/0.000/0.000 (771); p5 1.000/0.000/0.000 (264); p6 1.000/0.000/0.000 (14)
- **stamper**: p0 0.000/1.000/0.000 (562); p1 0.000/1.000/0.000 (304); p2 0.000/1.000/0.000 (182); p3 0.000/1.000/0.000 (30); p4 0.000/1.000/0.000 (3); p5 0.000/1.000/0.000 (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 2314.1 / 591.4 | 1.24 / 1.61 | +0.38 ± 0.07 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.03 / 0.02 | -0.01 ± 0.00 | 0.477 / 0.560 | +0.083 ± 0.011 | 0.271 / 0.341 | 0.026 / 0.000 | 0.158 / 0.190 | +0.032 ± 0.006 | 2.91 / 3.11 | +0.20 ± 0.08 |
| careful | 2630.5 / 267.9 | 0.23 / 0.14 | -0.09 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.06 / 0.07 | +0.00 ± 0.00 | 0.156 / 0.127 | -0.029 ± 0.005 | 0.055 / 0.063 | 0.001 / 0.000 | 0.062 / 0.062 | +0.000 ± 0.003 | 1.51 / 1.17 | -0.34 ± 0.09 |
| stamper | 904.2 / 156.2 | 1.06 / 0.79 | -0.26 ± 0.04 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.04 / 0.03 | -0.01 ± 0.00 | 0.236 / 0.238 | +0.002 ± 0.008 | 0.142 / 0.157 | 0.203 / 0.000 | 0.094 / 0.077 | -0.017 ± 0.006 | 3.35 / 2.14 | -1.21 ± 0.18 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| direct | +0.04 ± 0.03 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.050 ± 0.004 | -0.019 ± 0.005 | +0.001 ± 0.005 |
| careful | -0.08 ± 0.02 | +0.00 ± 0.00 | +0.00 ± 0.00 | -0.025 ± 0.005 | +0.009 ± 0.003 | +0.000 ± 0.003 |
| stamper | -0.77 ± 0.04 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.151 ± 0.012 | -0.100 ± 0.010 | -0.023 ± 0.006 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| direct | 0.121 / 0.069 | 0.61 / 0.62 | 0.036 / 0.091 | 0.00 / 0.00 | 0.60 / 0.57 | 0.786 / 0.601 |
| careful | 0.357 / 0.106 | 0.38 / 0.42 | 0.038 / 0.158 | 0.00 / 0.00 | 0.29 / 0.31 | 0.308 / 0.256 |
| stamper | 0.024 / 0.000 | 0.00 / — | 0.000 / 0.028 | — / 0.00 | — / — | 1.194 / 1.757 |

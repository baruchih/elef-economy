# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule`, seeds 21-40, hide ``, model `results/redteam/stability/learned-rev-careful-290/wm/models/wm-online-10.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | non-initial share | non-initial stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 26836.3 ± 421.5 | -8692.8 ± 783.9 | 3334.2 | 0.724 | 0.275 | 0.001 | 0.169 | 0.202 | 0.145 | 0.758 | 30.60 | 109.30 | 0.15 |
| careful | 35529.1 ± 774.7 | nan ± nan | 4189.1 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.309 | 0.000 | 7.30 | 0.00 | 0.35 |
| stamper | 7349.8 ± 172.2 | -28179.3 ± 811.2 | 1057.0 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.021 | 1.000 | 16.30 | 179.80 | 1.00 |

The stamp rate by seat kind (2.8.0 §5), plant / real, with the decisions pooled over the seeds in parentheses — under 2.7.0 a plant reached the initial review alone; under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| greedy | 0.169 (12383) / 0.202 (44647) | 0.891 (1340) / 0.904 (6571) | 0.136 (817) / 0.083 (925) | — / — |
| careful | 0.000 (5335) / 0.000 (52552) | 0.000 (1230) / 0.000 (19185) | 0.000 (1824) / 0.000 (3657) | — / — |
| stamper | 1.000 (3000) / 1.000 (17701) | — / 1.000 (440) | — / — | — / — |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 0.895 | 0.938 | 0.791 (153) | 0.761 (452) | 0.705 (610) | 0.326 (19631) | 0.242 (45837) | 43.500 | 243.800 | 1.752 | 2.513 |
| careful | — | 0.675 | 0.000 (26530) | 0.000 (6574) | 0.000 (4265) | 0.000 (1116) | 0.000 (45298) | 24.600 | 720.300 | 1.174 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (21141) | 72.450 | 179.000 | 2.197 | 2.482 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| greedy | 39.800 | 0.000 | 0.000 | 0.000 | 0.000 | 0.150 | 0.000 |
| careful | 39.700 | 0.000 | 0.000 | 0.000 | 0.000 | 0.350 | 0.000 |
| stamper | 40.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 17.350 / 39.800 | 30.600 ± 2.184 | +23.300 ± 2.058 | 96.500 | +87.300 ± 2.325 | 6.850 | 0.182 | 23.700 | +18.800 ± 0.875 | 1695.600 | 0.054 | +0.029 ± 0.002 | 0.000 / 0.000 (0.000 / 0.000) | 29254.123 ± 332.463 | +6144.228 ± 437.987 | 26836.3 ± 421.5 | -8692.8 ± 783.9 | 29.048 | -8.709 ± 0.407 | 23.483 ± 0.241 | +9.744 ± 0.260 | 21.836 | 0.056 | 2113.800 | 19.800 | 22.450 | +6.200 ± 0.439 | 64.378 | 144.800 |
| careful | 23.450 / 39.700 | 7.300 ± 0.508 | — | 9.200 | — | 2.650 | 0.042 | 4.900 | — | 1624.750 | 0.025 | — | 0.000 / 0.000 (0.000 / 0.000) | 23109.895 ± 390.187 | — | 35529.1 ± 774.7 | — | 37.756 | — | 13.739 ± 0.211 | — | 17.387 | 0.001 | 2632.400 | 19.700 | 16.250 | — | 999.731 | 185.000 |
| stamper | 3.950 / 40.000 | 16.300 ± 0.987 | +9.000 ± 1.326 | 111.250 | +102.050 ± 1.755 | 0.000 | 1.000 | 52.450 | +47.550 ± 1.370 | 885.100 | 0.189 | +0.164 ± 0.003 | 0.000 / 0.000 (0.000 / 0.000) | 9235.727 ± 182.151 | -13874.168 ± 409.826 | 7349.8 ± 172.2 | -28179.3 ± 811.2 | 26.772 | -10.984 ± 0.470 | 31.455 ± 0.755 | +17.716 ± 0.875 | 22.777 | 0.201 | 737.650 | 20.000 | 36.050 | +19.800 ± 0.928 | 5739.536 | 113.600 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **greedy**: p0 0.851/0.149/0.000 (579); p1 0.510/0.488/0.002 (429); p2 0.579/0.421/0.000 (267); p3 0.697/0.303/0.000 (222); p4 0.777/0.223/0.000 (222); p5 0.765/0.235/0.000 (222); p6 0.791/0.208/0.002 (219); p7 0.749/0.250/0.000 (228); p8 0.793/0.207/0.000 (216); p9 0.762/0.237/0.000 (219); p10 0.710/0.289/0.001 (217); p11 0.724/0.272/0.004 (188); p12 0.766/0.233/0.001 (95); p13 0.433/0.567/0.000 (11)
- **careful**: p0 1.000/0.000/0.000 (591); p1 1.000/0.000/0.000 (732); p2 1.000/0.000/0.000 (856); p3 1.000/0.000/0.000 (918); p4 1.000/0.000/0.000 (805); p5 1.000/0.000/0.000 (280); p6 1.000/0.000/0.000 (6)
- **stamper**: p0 0.000/1.000/0.000 (561); p1 0.000/1.000/0.000 (306); p2 0.000/1.000/0.000 (168); p3 0.000/1.000/0.000 (18); p4 0.000/1.000/0.000 (3); p5 0.000/1.000/0.000 (1)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 2232.3 / 619.1 | 1.66 / 2.16 | +0.50 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.04 / 0.04 | -0.01 ± 0.00 | 0.550 / 0.641 | +0.091 ± 0.008 | 0.337 / 0.404 | 0.056 / 0.000 | 0.203 / 0.239 | +0.036 ± 0.004 | 3.39 / 3.68 | +0.30 ± 0.05 |
| careful | 2627.6 / 266.8 | 0.23 / 0.14 | -0.09 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.07 / 0.06 | -0.00 ± 0.00 | 0.155 / 0.126 | -0.029 ± 0.005 | 0.059 / 0.065 | 0.000 / 0.000 | 0.061 / 0.064 | +0.003 ± 0.004 | 1.52 / 1.27 | -0.25 ± 0.10 |
| stamper | 885.0 / 150.0 | 1.05 / 0.72 | -0.33 ± 0.04 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.03 / 0.02 | -0.01 ± 0.00 | 0.237 / 0.225 | -0.012 ± 0.009 | 0.133 / 0.129 | 0.167 / 0.000 | 0.103 / 0.078 | -0.025 ± 0.006 | 3.54 / 2.00 | -1.54 ± 0.19 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| greedy | +0.04 ± 0.02 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.051 ± 0.004 | -0.030 ± 0.003 | -0.004 ± 0.005 |
| careful | -0.09 ± 0.02 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.031 ± 0.005 | +0.006 ± 0.003 | +0.003 ± 0.004 |
| stamper | -0.86 ± 0.04 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.174 ± 0.012 | -0.123 ± 0.010 | -0.037 ± 0.006 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| greedy | 0.146 / 0.072 | 0.55 / 0.56 | 0.029 / 0.098 | 0.00 / 0.00 | 0.57 / 0.62 | 0.715 / 0.714 |
| careful | 0.363 / 0.103 | 0.40 / 0.40 | 0.040 / 0.162 | 0.00 / 0.00 | 0.30 / 0.28 | 0.304 / 0.324 |
| stamper | 0.025 / 0.000 | 0.00 / — | 0.000 / 0.045 | — / 0.00 | — / — | 1.195 / 1.993 |

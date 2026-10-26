# Evaluation — cell `--entry-pool 20 --stampers 0.6 --dispute-policy truthful --learner-pop all --learner-role reviewer --learner-exit rule`, seeds 21-40, hide ``, model `results/redteam/stability/learned-rev-disputes-280/wm/models/wm-online-5.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | non-initial share | non-initial stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 28950.0 ± 471.8 | -7041.0 ± 698.0 | 4016.7 | 0.586 | 0.392 | 0.022 | 0.228 | 0.244 | 0.291 | 0.841 | 8.30 | 122.55 | 0.15 |
| careful | 35991.0 ± 777.8 | nan ± nan | 4133.4 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.296 | 0.000 | 0.55 | 0.00 | 0.20 |
| stamper | 7029.9 ± 149.7 | -28961.1 ± 829.4 | 1086.0 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.026 | 1.000 | 8.70 | 192.80 | 1.00 |

The stamp rate by seat kind (2.8.0 §5), plant / real, with the decisions pooled over the seeds in parentheses — under 2.7.0 a plant reached the initial review alone; under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| greedy | 0.228 (11179) / 0.244 (45787) | 0.941 (1563) / 0.939 (16100) | 0.411 (2349) / 0.627 (3355) | — / — |
| careful | 0.000 (5468) / 0.000 (52713) | 0.000 (602) / 0.000 (19391) | 0.000 (370) / 0.000 (4125) | — / — |
| stamper | 1.000 (3068) / 1.000 (18080) | — / 1.000 (375) | — / 1.000 (196) | — / — |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 0.827 | 0.931 | 0.835 (2791) | 0.807 (1851) | 0.770 (1029) | 0.475 (24721) | 0.305 (49941) | 45.250 | 373.200 | 1.477 | 2.708 |
| careful | — | 0.679 | 0.000 (25262) | 0.000 (6701) | 0.000 (4757) | 0.000 (1631) | 0.000 (44318) | 24.950 | 677.050 | 1.148 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (21719) | 76.600 | 180.650 | 2.118 | 2.517 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| greedy | 39.850 | 0.000 | 0.000 | 0.000 | 0.000 | 0.150 | 0.000 |
| careful | 39.600 | 0.000 | 0.000 | 0.000 | 0.000 | 0.200 | 0.000 |
| stamper | 40.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 17.800 / 39.850 | 8.300 ± 0.459 | +7.750 ± 0.486 | 109.300 | +98.600 ± 2.982 | 6.550 | 0.256 | 25.400 | +20.050 ± 1.014 | 1664.850 | 0.008 | -0.005 ± 0.001 | 121.350 / 117.200 (121.350 / 117.200) | 32229.848 ± 415.446 | +8860.734 ± 477.934 | 28950.0 ± 471.8 | -7041.0 ± 698.0 | 29.991 | -7.735 ± 0.339 | 23.806 ± 0.374 | +10.095 ± 0.514 | 22.452 | 0.025 | 2242.600 | 19.850 | 22.050 | +5.100 ± 0.486 | 72.203 | 200.200 |
| careful | 22.650 / 39.600 | 0.550 ± 0.170 | — | 10.700 | — | 3.300 | 0.054 | 5.350 | — | 1591.500 | 0.013 | — | 25.750 / 25.150 (25.750 / 25.150) | 23369.114 ± 278.692 | — | 35991.0 ± 777.8 | — | 37.726 | — | 13.712 ± 0.314 | — | 17.430 | 0.001 | 2639.350 | 19.600 | 16.950 | — | 955.090 | 220.900 |
| stamper | 4.250 / 40.000 | 8.700 ± 0.585 | +8.150 ± 0.608 | 114.600 | +103.900 ± 1.987 | 0.000 | 1.000 | 56.600 | +51.250 ± 2.194 | 725.700 | 0.017 | +0.004 ± 0.001 | 178.550 / 170.050 (178.550 / 170.050) | 8356.862 ± 105.916 | -15012.252 ± 298.788 | 7029.9 ± 149.7 | -28961.1 ± 829.4 | 27.277 | -10.449 ± 0.391 | 30.331 ± 0.752 | +16.619 ± 0.866 | 22.470 | 0.248 | 708.100 | 20.000 | 35.750 | +18.800 ± 0.887 | 5752.771 | 182.750 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **greedy**: p0 0.927/0.071/0.001 (604); p1 0.416/0.555/0.029 (682); p2 0.398/0.568/0.035 (424); p3 0.633/0.350/0.017 (279); p4 0.555/0.434/0.011 (273); p5 0.597/0.387/0.016 (283); p6 0.583/0.395/0.022 (284); p7 0.611/0.372/0.018 (275); p8 0.583/0.390/0.027 (283); p9 0.554/0.414/0.032 (288); p10 0.529/0.432/0.039 (246); p11 0.523/0.445/0.032 (79); p12 0.468/0.468/0.064 (15); p13 0.586/0.414/0.000 (1)
- **careful**: p0 1.000/0.000/0.000 (599); p1 1.000/0.000/0.000 (752); p2 1.000/0.000/0.000 (840); p3 1.000/0.000/0.000 (871); p4 1.000/0.000/0.000 (738); p5 1.000/0.000/0.000 (294); p6 1.000/0.000/0.000 (40)
- **stamper**: p0 0.000/1.000/0.000 (580); p1 0.000/1.000/0.000 (306); p2 0.000/1.000/0.000 (173); p3 0.000/1.000/0.000 (19); p4 0.000/1.000/0.000 (6); p5 0.000/1.000/0.000 (2)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 2289.3 / 559.0 | 1.45 / 1.90 | +0.45 ± 0.05 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.07 / 0.07 | +0.00 ± 0.00 | 0.491 / 0.600 | +0.109 ± 0.010 | 0.277 / 0.364 | 0.024 / 0.039 | 0.164 / 0.212 | +0.048 ± 0.006 | 3.35 / 3.59 | +0.24 ± 0.06 |
| careful | 2635.7 / 273.4 | 0.23 / 0.15 | -0.08 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.07 / 0.07 | +0.00 ± 0.00 | 0.155 / 0.130 | -0.025 ± 0.006 | 0.054 / 0.058 | 0.001 / 0.001 | 0.062 / 0.063 | +0.001 ± 0.003 | 1.52 / 1.33 | -0.19 ± 0.06 |
| stamper | 904.0 / 153.4 | 1.17 / 0.82 | -0.35 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.04 / 0.02 | -0.01 ± 0.00 | 0.268 / 0.270 | +0.002 ± 0.010 | 0.147 / 0.153 | 0.216 / 0.311 | 0.108 / 0.076 | -0.032 ± 0.004 | 3.52 / 2.18 | -1.35 ± 0.18 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| greedy | +0.00 ± 0.02 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.049 ± 0.005 | -0.029 ± 0.004 | +0.006 ± 0.004 |
| careful | -0.07 ± 0.01 | +0.00 ± 0.00 | +0.00 ± 0.00 | -0.022 ± 0.004 | +0.005 ± 0.003 | +0.001 ± 0.003 |
| stamper | -0.84 ± 0.04 | +0.00 ± 0.00 | -0.03 ± 0.00 | -0.156 ± 0.015 | -0.109 ± 0.011 | -0.036 ± 0.004 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| greedy | 0.347 / 0.137 | 0.47 / 0.40 | 0.086 / 0.207 | 0.00 / 0.00 | 0.48 / 0.42 | 0.498 / 0.293 |
| careful | 0.366 / 0.109 | 0.37 / 0.39 | 0.050 / 0.049 | 0.00 / 0.00 | 0.28 / 0.30 | 0.291 / 0.122 |
| stamper | 0.021 / 0.000 | 0.02 / — | 0.197 / 0.747 | 0.00 / 0.00 | 0.00 / — | 1.209 / 1.760 |

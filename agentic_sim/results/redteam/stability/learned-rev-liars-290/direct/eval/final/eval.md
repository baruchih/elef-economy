# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --dispute-policy truthful --appeal-lie 0.1 --dispute-lie 0.1`, seeds 21-40, hide ``, model `None` (value off, horizon 8)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | non-initial share | non-initial stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 29350.4 ± 505.3 | -5082.7 ± 1011.2 | 4291.0 | 0.642 | 0.333 | 0.025 | 0.246 | 0.262 | 0.311 | 0.580 | 12.95 | 139.60 | 0.20 |
| careful | 34433.1 ± 972.8 | nan ± nan | 4326.4 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.346 | 0.000 | 2.00 | 0.00 | 0.25 |
| stamper | 7001.5 ± 128.9 | -27431.6 ± 925.2 | 1077.1 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.029 | 1.000 | 8.20 | 189.15 | 1.00 |
| hand | 31265.2 ± 835.2 | -3167.8 ± 1128.9 | 4743.1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.364 | 0.000 | 4.15 | 0.00 | 0.45 |

The stamp rate by seat kind (2.8.0 §5), plant / real, with the decisions pooled over the seeds in parentheses — under 2.7.0 a plant reached the initial review alone; under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| direct | 0.246 (12321) / 0.262 (46830) | 0.832 (559) / 0.872 (13967) | 0.165 (5497) / 0.288 (6646) | — / — |
| careful | 0.000 (5351) / 0.000 (51202) | 0.000 (141) / 0.000 (17274) | 0.000 (3309) / 0.000 (9251) | — / — |
| stamper | 1.000 (3041) / 1.000 (17881) | — / 1.000 (344) | 1.000 (2) / 1.000 (274) | — / — |
| hand | 0.000 (12104) / 0.000 (48237) | 0.000 (917) / 0.000 (17803) | 0.000 (5786) / 0.000 (10016) | — / — |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 0.885 | 0.938 | 0.709 (1036) | 0.621 (1279) | 0.532 (1671) | 0.409 (22328) | 0.287 (59506) | 36.850 | 347.650 | 1.607 | 3.788 |
| careful | — | 0.672 | 0.000 (25918) | 0.000 (8346) | 0.000 (5321) | 0.000 (1714) | 0.000 (45229) | 26.000 | 704.500 | 1.232 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (21542) | 76.500 | 173.600 | 2.225 | 2.473 |
| hand | — | 0.805 | 0.000 (35) | 0.000 (12033) | 0.000 (20285) | 0.000 (16298) | 0.000 (46212) | 36.250 | 364.650 | 1.377 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| direct | 39.800 | 0.000 | 0.000 | 0.000 | 0.000 | 0.200 | 0.000 |
| careful | 39.700 | 0.000 | 0.000 | 0.000 | 0.000 | 0.250 | 0.000 |
| stamper | 39.950 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| hand | 39.850 | 0.000 | 0.000 | 0.000 | 0.000 | 0.450 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 19.200 / 39.800 | 12.950 ± 0.659 | +10.950 ± 0.742 | 117.150 | +105.800 ± 4.064 | 9.850 | 0.246 | 17.050 | +10.750 ± 0.807 | 1528.250 | 0.008 | -0.005 ± 0.001 | 293.350 / 123.150 (124.750 / 118.850) | 30051.637 ± 342.973 | +5840.630 ± 433.861 | 29350.4 ± 505.3 | -5082.7 ± 1011.2 | 30.633 | -4.856 ± 0.357 | 22.303 ± 0.480 | +7.057 ± 0.679 | 20.916 | 0.021 | 2299.850 | 19.800 | 20.600 | +4.850 ± 0.685 | 61.246 | 173.600 |
| careful | 23.950 / 39.700 | 2.000 ± 0.348 | — | 11.350 | — | 3.400 | 0.059 | 6.300 | — | 1441.850 | 0.013 | — | 217.550 / 30.050 (27.100 / 26.400) | 24211.007 ± 488.723 | — | 34433.1 ± 972.8 | — | 35.488 | — | 15.246 ± 0.533 | — | 18.244 | 0.002 | 2560.450 | 19.700 | 15.750 | — | 645.706 | 271.850 |
| stamper | 4.750 / 39.950 | 8.200 ± 0.738 | +6.200 ± 0.800 | 113.200 | +101.850 ± 2.516 | 0.000 | 1.000 | 56.550 | +50.250 ± 2.216 | 647.800 | 0.018 | +0.004 ± 0.001 | 249.500 / 169.500 (175.400 / 167.750) | 8183.485 ± 154.156 | -16027.522 ± 453.696 | 7001.5 ± 128.9 | -27431.6 ± 925.2 | 26.453 | -9.035 ± 0.392 | 29.962 ± 0.585 | +14.716 ± 0.855 | 22.899 | 0.288 | 665.700 | 19.950 | 35.200 | +19.450 ± 0.942 | 5658.933 | 170.000 |
| hand | 20.450 / 39.850 | 4.150 ± 0.488 | +2.150 ± 0.554 | 66.800 | +55.450 ± 1.887 | 6.850 | 0.049 | 16.400 | +10.100 ± 0.628 | 1398.750 | 0.013 | -0.001 ± 0.001 | 270.450 / 93.300 (92.800 / 89.950) | 29260.598 ± 326.415 | +5049.591 ± 480.148 | 31265.2 ± 835.2 | -3167.8 ± 1128.9 | 31.657 | -3.831 ± 0.473 | 20.226 ± 0.484 | +4.979 ± 0.829 | 19.828 | 0.048 | 2308.650 | 19.850 | 19.400 | +3.650 ± 0.625 | 93.754 | 162.550 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **direct**: p0 0.837/0.156/0.006 (604); p1 0.579/0.398/0.022 (533); p2 0.569/0.414/0.017 (386); p3 0.695/0.284/0.020 (285); p4 0.634/0.330/0.036 (310); p5 0.577/0.386/0.036 (316); p6 0.597/0.371/0.031 (300); p7 0.603/0.372/0.026 (306); p8 0.613/0.352/0.036 (290); p9 0.623/0.352/0.025 (289); p10 0.609/0.367/0.024 (283); p11 0.645/0.329/0.026 (220); p12 0.627/0.330/0.043 (127); p13 0.656/0.301/0.043 (42); p14 0.200/0.600/0.200 (0)
- **careful**: p0 1.000/0.000/0.000 (628); p1 1.000/0.000/0.000 (676); p2 1.000/0.000/0.000 (838); p3 1.000/0.000/0.000 (955); p4 1.000/0.000/0.000 (891); p5 1.000/0.000/0.000 (312); p6 1.000/0.000/0.000 (26)
- **stamper**: p0 0.000/1.000/0.000 (574); p1 0.000/1.000/0.000 (306); p2 0.000/1.000/0.000 (158); p3 0.000/1.000/0.000 (28); p4 0.000/1.000/0.000 (8); p5 0.000/1.000/0.000 (2)
- **hand**: p0 —/—/— (0); p1 —/—/— (0); p2 —/—/— (0); p3 —/—/— (0); p4 —/—/— (0); p5 —/—/— (0); p6 —/—/— (0); p7 —/—/— (0); p8 —/—/— (0); p9 —/—/— (0); p10 —/—/— (0); p11 —/—/— (0); p12 —/—/— (0); p13 —/—/— (0); p14 —/—/— (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 2341.5 / 616.0 | 1.18 / 1.34 | +0.16 ± 0.05 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.05 / 0.04 | -0.01 ± 0.00 | 0.464 / 0.514 | +0.050 ± 0.009 | 0.230 / 0.278 | 0.020 / 0.000 | 0.137 / 0.152 | +0.015 ± 0.004 | 3.00 / 3.00 | +0.00 ± 0.08 |
| careful | 2560.1 / 267.6 | 0.44 / 0.29 | -0.15 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.07 / 0.07 | -0.00 ± 0.00 | 0.233 / 0.197 | -0.036 ± 0.006 | 0.093 / 0.104 | 0.002 / 0.000 | 0.070 / 0.068 | -0.003 ± 0.003 | 2.03 / 1.66 | -0.37 ± 0.10 |
| stamper | 894.0 / 152.1 | 1.44 / 1.06 | -0.38 ± 0.04 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.03 / 0.02 | -0.01 ± 0.00 | 0.313 / 0.307 | -0.005 ± 0.010 | 0.184 / 0.193 | 0.255 / 0.000 | 0.114 / 0.070 | -0.044 ± 0.005 | 3.93 / 3.00 | -0.93 ± 0.29 |
| hand | 2411.8 / 605.2 | 0.98 / 0.97 | -0.01 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.11 / 0.11 | -0.01 ± 0.00 | 0.379 / 0.394 | +0.015 ± 0.006 | 0.171 / 0.193 | 0.048 / 0.000 | 0.113 / 0.109 | -0.003 ± 0.003 | 2.80 / 2.78 | -0.02 ± 0.07 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| direct | -0.03 ± 0.02 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.051 ± 0.005 | -0.020 ± 0.006 | -0.001 ± 0.003 |
| careful | -0.14 ± 0.02 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.036 ± 0.006 | +0.011 ± 0.003 | -0.003 ± 0.003 |
| stamper | -0.86 ± 0.05 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.163 ± 0.015 | -0.111 ± 0.011 | -0.048 ± 0.006 |
| hand | -0.12 ± 0.02 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.046 ± 0.004 | -0.014 ± 0.004 | -0.004 ± 0.003 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| direct | 0.294 / 0.045 | 0.51 / 0.42 | 0.184 / 0.516 | 0.00 / 0.00 | 0.51 / 0.50 | 0.605 / 0.626 |
| careful | 0.335 / 0.026 | 0.39 / 0.55 | 0.144 / 0.523 | 0.00 / 0.00 | 0.32 / 0.30 | 0.367 / 0.484 |
| stamper | 0.019 / 0.000 | 0.01 / — | 0.275 / 1.047 | 0.00 / 0.00 | 0.00 / — | 1.282 / 2.167 |
| hand | 0.364 / 0.075 | 0.13 / 0.10 | 0.159 / 0.382 | 0.00 / 0.00 | 0.12 / 0.14 | 0.358 / 0.317 |

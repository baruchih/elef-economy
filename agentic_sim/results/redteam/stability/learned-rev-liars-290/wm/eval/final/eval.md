# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --dispute-policy truthful --appeal-lie 0.1 --dispute-lie 0.1`, seeds 21-40, hide ``, model `results/redteam/stability/learned-rev-liars-290/wm/models/wm-online-10.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | non-initial share | non-initial stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 28463.6 ± 557.5 | -5969.5 ± 963.6 | 4162.1 | 0.676 | 0.319 | 0.005 | 0.175 | 0.197 | 0.322 | 0.599 | 11.95 | 103.30 | 0.10 |
| careful | 34433.1 ± 972.8 | nan ± nan | 4326.4 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.346 | 0.000 | 2.00 | 0.00 | 0.25 |
| stamper | 7001.5 ± 128.9 | -27431.6 ± 925.2 | 1077.1 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.029 | 1.000 | 8.20 | 189.15 | 1.00 |
| hand | 31265.2 ± 835.2 | -3167.8 ± 1128.9 | 4743.1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.364 | 0.000 | 4.15 | 0.00 | 0.45 |

The stamp rate by seat kind (2.8.0 §5), plant / real, with the decisions pooled over the seeds in parentheses — under 2.7.0 a plant reached the initial review alone; under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| greedy | 0.175 (11730) / 0.197 (44738) | 0.967 (738) / 0.949 (14657) | 0.087 (5178) / 0.156 (6200) | — / — |
| careful | 0.000 (5351) / 0.000 (51202) | 0.000 (141) / 0.000 (17274) | 0.000 (3309) / 0.000 (9251) | — / — |
| stamper | 1.000 (3041) / 1.000 (17881) | — / 1.000 (344) | 1.000 (2) / 1.000 (274) | — / — |
| hand | 0.000 (12104) / 0.000 (48237) | 0.000 (917) / 0.000 (17803) | 0.000 (5786) / 0.000 (10016) | — / — |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 0.865 | 0.920 | 0.844 (694) | 0.745 (1202) | 0.631 (1153) | 0.357 (30016) | 0.270 (50176) | 42.400 | 293.300 | 1.676 | 2.436 |
| careful | — | 0.672 | 0.000 (25918) | 0.000 (8346) | 0.000 (5321) | 0.000 (1714) | 0.000 (45229) | 26.000 | 704.500 | 1.232 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (21542) | 76.500 | 173.600 | 2.225 | 2.473 |
| hand | — | 0.805 | 0.000 (35) | 0.000 (12033) | 0.000 (20285) | 0.000 (16298) | 0.000 (46212) | 36.250 | 364.650 | 1.377 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| greedy | 39.750 | 0.000 | 0.000 | 0.000 | 0.000 | 0.100 | 0.000 |
| careful | 39.700 | 0.000 | 0.000 | 0.000 | 0.000 | 0.250 | 0.000 |
| stamper | 39.950 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| hand | 39.850 | 0.000 | 0.000 | 0.000 | 0.000 | 0.450 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 17.850 / 39.750 | 11.950 ± 0.816 | +9.950 ± 0.890 | 94.750 | +83.400 ± 3.400 | 6.200 | 0.175 | 22.650 | +16.350 ± 0.634 | 1458.150 | 0.008 | -0.005 ± 0.001 | 263.650 / 98.050 (97.750 / 93.350) | 31441.503 ± 473.264 | +7230.496 ± 449.784 | 28463.6 ± 557.5 | -5969.5 ± 963.6 | 29.393 | -6.096 ± 0.382 | 23.713 ± 0.358 | +8.466 ± 0.724 | 22.052 | 0.037 | 2164.700 | 19.750 | 21.900 | +6.150 ± 0.650 | 73.245 | 156.000 |
| careful | 23.950 / 39.700 | 2.000 ± 0.348 | — | 11.350 | — | 3.400 | 0.059 | 6.300 | — | 1441.850 | 0.013 | — | 217.550 / 30.050 (27.100 / 26.400) | 24211.007 ± 488.723 | — | 34433.1 ± 972.8 | — | 35.488 | — | 15.246 ± 0.533 | — | 18.244 | 0.002 | 2560.450 | 19.700 | 15.750 | — | 645.706 | 271.850 |
| stamper | 4.750 / 39.950 | 8.200 ± 0.738 | +6.200 ± 0.800 | 113.200 | +101.850 ± 2.516 | 0.000 | 1.000 | 56.550 | +50.250 ± 2.216 | 647.800 | 0.018 | +0.004 ± 0.001 | 249.500 / 169.500 (175.400 / 167.750) | 8183.485 ± 154.156 | -16027.522 ± 453.696 | 7001.5 ± 128.9 | -27431.6 ± 925.2 | 26.453 | -9.035 ± 0.392 | 29.962 ± 0.585 | +14.716 ± 0.855 | 22.899 | 0.288 | 665.700 | 19.950 | 35.200 | +19.450 ± 0.942 | 5658.933 | 170.000 |
| hand | 20.450 / 39.850 | 4.150 ± 0.488 | +2.150 ± 0.554 | 66.800 | +55.450 ± 1.887 | 6.850 | 0.049 | 16.400 | +10.100 ± 0.628 | 1398.750 | 0.013 | -0.001 ± 0.001 | 270.450 / 93.300 (92.800 / 89.950) | 29260.598 ± 326.415 | +5049.591 ± 480.148 | 31265.2 ± 835.2 | -3167.8 ± 1128.9 | 31.657 | -3.831 ± 0.473 | 20.226 ± 0.484 | +4.979 ± 0.829 | 19.828 | 0.048 | 2308.650 | 19.850 | 19.400 | +3.650 ± 0.625 | 93.754 | 162.550 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **greedy**: p0 0.895/0.105/0.000 (595); p1 0.526/0.472/0.002 (525); p2 0.570/0.428/0.002 (367); p3 0.676/0.323/0.001 (291); p4 0.650/0.344/0.006 (305); p5 0.654/0.340/0.006 (309); p6 0.652/0.340/0.008 (309); p7 0.679/0.313/0.008 (299); p8 0.670/0.322/0.008 (310); p9 0.695/0.296/0.009 (309); p10 0.690/0.301/0.008 (257); p11 0.682/0.309/0.010 (168); p12 0.710/0.281/0.010 (94); p13 0.668/0.328/0.004 (23)
- **careful**: p0 1.000/0.000/0.000 (628); p1 1.000/0.000/0.000 (676); p2 1.000/0.000/0.000 (838); p3 1.000/0.000/0.000 (955); p4 1.000/0.000/0.000 (891); p5 1.000/0.000/0.000 (312); p6 1.000/0.000/0.000 (26)
- **stamper**: p0 0.000/1.000/0.000 (574); p1 0.000/1.000/0.000 (306); p2 0.000/1.000/0.000 (158); p3 0.000/1.000/0.000 (28); p4 0.000/1.000/0.000 (8); p5 0.000/1.000/0.000 (2)
- **hand**: p0 —/—/— (0); p1 —/—/— (0); p2 —/—/— (0); p3 —/—/— (0); p4 —/—/— (0); p5 —/—/— (0); p6 —/—/— (0); p7 —/—/— (0); p8 —/—/— (0); p9 —/—/— (0); p10 —/—/— (0); p11 —/—/— (0); p12 —/—/— (0); p13 —/—/— (0); p14 —/—/— (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 2236.9 / 586.5 | 1.67 / 2.17 | +0.50 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.06 / 0.06 | -0.01 ± 0.00 | 0.562 / 0.646 | +0.084 ± 0.006 | 0.311 / 0.385 | 0.037 / 0.000 | 0.191 / 0.231 | +0.040 ± 0.005 | 3.42 / 3.71 | +0.29 ± 0.06 |
| careful | 2560.1 / 267.6 | 0.44 / 0.29 | -0.15 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.07 / 0.07 | -0.00 ± 0.00 | 0.233 / 0.197 | -0.036 ± 0.006 | 0.093 / 0.104 | 0.002 / 0.000 | 0.070 / 0.068 | -0.003 ± 0.003 | 2.03 / 1.66 | -0.37 ± 0.10 |
| stamper | 894.0 / 152.1 | 1.44 / 1.06 | -0.38 ± 0.04 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.03 / 0.02 | -0.01 ± 0.00 | 0.313 / 0.307 | -0.005 ± 0.010 | 0.184 / 0.193 | 0.255 / 0.000 | 0.114 / 0.070 | -0.044 ± 0.005 | 3.93 / 3.00 | -0.93 ± 0.29 |
| hand | 2411.8 / 605.2 | 0.98 / 0.97 | -0.01 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.11 / 0.11 | -0.01 ± 0.00 | 0.379 / 0.394 | +0.015 ± 0.006 | 0.171 / 0.193 | 0.048 / 0.000 | 0.113 / 0.109 | -0.003 ± 0.003 | 2.80 / 2.78 | -0.02 ± 0.07 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| greedy | +0.08 ± 0.03 | +0.00 ± 0.00 | -0.03 ± 0.00 | -0.044 ± 0.002 | -0.025 ± 0.005 | -0.001 ± 0.005 |
| careful | -0.14 ± 0.02 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.036 ± 0.006 | +0.011 ± 0.003 | -0.003 ± 0.003 |
| stamper | -0.86 ± 0.05 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.163 ± 0.015 | -0.111 ± 0.011 | -0.048 ± 0.006 |
| hand | -0.12 ± 0.02 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.046 ± 0.004 | -0.014 ± 0.004 | -0.004 ± 0.003 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| greedy | 0.323 / 0.061 | 0.39 / 0.35 | 0.164 / 0.433 | 0.00 / 0.00 | 0.38 / 0.35 | 0.538 / 0.469 |
| careful | 0.335 / 0.026 | 0.39 / 0.55 | 0.144 / 0.523 | 0.00 / 0.00 | 0.32 / 0.30 | 0.367 / 0.484 |
| stamper | 0.019 / 0.000 | 0.01 / — | 0.275 / 1.047 | 0.00 / 0.00 | 0.00 / — | 1.282 / 2.167 |
| hand | 0.364 / 0.075 | 0.13 / 0.10 | 0.159 / 0.382 | 0.00 / 0.00 | 0.12 / 0.14 | 0.358 / 0.317 |

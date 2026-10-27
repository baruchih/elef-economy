# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --dispute-policy truthful --appeal-lie 0.1 --dispute-lie 0.1`, seeds 21-40, hide ``, model `results/redteam/stability/learned-rev-liars-290/wm/models/wm-online-5.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | non-initial share | non-initial stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 28121.1 ± 598.1 | -6312.0 ± 813.9 | 4155.9 | 0.682 | 0.310 | 0.007 | 0.181 | 0.196 | 0.320 | 0.583 | 8.60 | 96.55 | 0.05 |
| careful | 34433.1 ± 972.8 | nan ± nan | 4326.4 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.346 | 0.000 | 2.00 | 0.00 | 0.25 |
| stamper | 7001.5 ± 128.9 | -27431.6 ± 925.2 | 1077.1 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.029 | 1.000 | 8.20 | 189.15 | 1.00 |

The stamp rate by seat kind (2.8.0 §5), plant / real, with the decisions pooled over the seeds in parentheses — under 2.7.0 a plant reached the initial review alone; under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| greedy | 0.181 (12241) / 0.196 (44253) | 0.958 (692) / 0.933 (14504) | 0.106 (5541) / 0.127 (5886) | — / — |
| careful | 0.000 (5351) / 0.000 (51202) | 0.000 (141) / 0.000 (17274) | 0.000 (3309) / 0.000 (9251) | — / — |
| stamper | 1.000 (3041) / 1.000 (17881) | — / 1.000 (344) | 1.000 (2) / 1.000 (274) | — / — |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 0.882 | 0.920 | 0.660 (297) | 0.668 (987) | 0.565 (964) | 0.355 (30694) | 0.269 (50175) | 41.800 | 265.450 | 1.693 | 2.310 |
| careful | — | 0.672 | 0.000 (25918) | 0.000 (8346) | 0.000 (5321) | 0.000 (1714) | 0.000 (45229) | 26.000 | 704.500 | 1.232 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (21542) | 76.500 | 173.600 | 2.225 | 2.473 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| greedy | 39.750 | 0.000 | 0.000 | 0.000 | 0.000 | 0.050 | 0.000 |
| careful | 39.700 | 0.000 | 0.000 | 0.000 | 0.000 | 0.250 | 0.000 |
| stamper | 39.950 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 17.150 / 39.750 | 8.600 ± 0.651 | +6.600 ± 0.769 | 101.300 | +89.950 ± 3.109 | 6.350 | 0.156 | 22.050 | +15.750 ± 0.721 | 1452.500 | 0.008 | -0.005 ± 0.001 | 256.300 / 99.900 (98.800 / 95.750) | 31511.741 ± 638.696 | +7300.733 ± 560.522 | 28121.1 ± 598.1 | -6312.0 ± 813.9 | 29.001 | -6.488 ± 0.342 | 24.000 ± 0.292 | +8.753 ± 0.607 | 22.237 | 0.050 | 2110.450 | 19.750 | 22.600 | +6.850 ± 0.577 | 75.267 | 171.200 |
| careful | 23.950 / 39.700 | 2.000 ± 0.348 | — | 11.350 | — | 3.400 | 0.059 | 6.300 | — | 1441.850 | 0.013 | — | 217.550 / 30.050 (27.100 / 26.400) | 24211.007 ± 488.723 | — | 34433.1 ± 972.8 | — | 35.488 | — | 15.246 ± 0.533 | — | 18.244 | 0.002 | 2560.450 | 19.700 | 15.750 | — | 645.706 | 271.850 |
| stamper | 4.750 / 39.950 | 8.200 ± 0.738 | +6.200 ± 0.800 | 113.200 | +101.850 ± 2.516 | 0.000 | 1.000 | 56.550 | +50.250 ± 2.216 | 647.800 | 0.018 | +0.004 ± 0.001 | 249.500 / 169.500 (175.400 / 167.750) | 8183.485 ± 154.156 | -16027.522 ± 453.696 | 7001.5 ± 128.9 | -27431.6 ± 925.2 | 26.453 | -9.035 ± 0.392 | 29.962 ± 0.585 | +14.716 ± 0.855 | 22.899 | 0.288 | 665.700 | 19.950 | 35.200 | +19.450 ± 0.942 | 5658.933 | 170.000 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **greedy**: p0 0.866/0.134/0.000 (590); p1 0.580/0.417/0.002 (462); p2 0.581/0.417/0.002 (321); p3 0.685/0.312/0.004 (288); p4 0.637/0.354/0.008 (307); p5 0.641/0.353/0.006 (309); p6 0.624/0.365/0.011 (302); p7 0.656/0.336/0.008 (298); p8 0.670/0.319/0.011 (302); p9 0.696/0.288/0.015 (293); p10 0.707/0.279/0.014 (291); p11 0.725/0.262/0.013 (222); p12 0.705/0.278/0.016 (135); p13 0.734/0.249/0.017 (35)
- **careful**: p0 1.000/0.000/0.000 (628); p1 1.000/0.000/0.000 (676); p2 1.000/0.000/0.000 (838); p3 1.000/0.000/0.000 (955); p4 1.000/0.000/0.000 (891); p5 1.000/0.000/0.000 (312); p6 1.000/0.000/0.000 (26)
- **stamper**: p0 0.000/1.000/0.000 (574); p1 0.000/1.000/0.000 (306); p2 0.000/1.000/0.000 (158); p3 0.000/1.000/0.000 (28); p4 0.000/1.000/0.000 (8); p5 0.000/1.000/0.000 (2)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 2212.7 / 612.0 | 1.81 / 2.27 | +0.46 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.06 / 0.06 | -0.00 ± 0.00 | 0.571 / 0.658 | +0.087 ± 0.004 | 0.335 / 0.408 | 0.050 / 0.000 | 0.205 / 0.255 | +0.050 ± 0.004 | 3.55 / 3.79 | +0.24 ± 0.04 |
| careful | 2560.1 / 267.6 | 0.44 / 0.29 | -0.15 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.07 / 0.07 | -0.00 ± 0.00 | 0.233 / 0.197 | -0.036 ± 0.006 | 0.093 / 0.104 | 0.002 / 0.000 | 0.070 / 0.068 | -0.003 ± 0.003 | 2.03 / 1.66 | -0.37 ± 0.10 |
| stamper | 894.0 / 152.1 | 1.44 / 1.06 | -0.38 ± 0.04 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.03 / 0.02 | -0.01 ± 0.00 | 0.313 / 0.307 | -0.005 ± 0.010 | 0.184 / 0.193 | 0.255 / 0.000 | 0.114 / 0.070 | -0.044 ± 0.005 | 3.93 / 3.00 | -0.93 ± 0.29 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| greedy | +0.02 ± 0.02 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.047 ± 0.004 | -0.028 ± 0.004 | +0.009 ± 0.004 |
| careful | -0.14 ± 0.02 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.036 ± 0.006 | +0.011 ± 0.003 | -0.003 ± 0.003 |
| stamper | -0.86 ± 0.05 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.163 ± 0.015 | -0.111 ± 0.011 | -0.048 ± 0.006 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| greedy | 0.323 / 0.056 | 0.39 / 0.38 | 0.160 / 0.452 | 0.00 / 0.00 | 0.40 / 0.37 | 0.539 / 0.499 |
| careful | 0.335 / 0.026 | 0.39 / 0.55 | 0.144 / 0.523 | 0.00 / 0.00 | 0.32 / 0.30 | 0.367 / 0.484 |
| stamper | 0.019 / 0.000 | 0.01 / — | 0.275 / 1.047 | 0.00 / 0.00 | 0.00 / — | 1.282 / 2.167 |

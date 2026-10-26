# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop half --learner-role reviewer --learner-exit rule`, seeds 21-40, hide ``, model `results/redteam/stability/learned-rev-half-280/wm/models/wm-online-10.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | non-initial share | non-initial stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 16686.9 ± 678.8 | -2789.1 ± 779.5 | 2212.8 | 0.811 | 0.189 | 0.000 | 0.074 | 0.087 | 0.295 | 0.430 | 18.40 | 29.15 | 0.10 |
| careful | 19476.0 ± 680.0 | nan ± nan | 2542.3 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.328 | 0.000 | 8.85 | 0.00 | 0.35 |
| stamper | 3754.7 ± 123.4 | -15721.3 ± 650.1 | 512.9 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.023 | 1.000 | 14.65 | 87.65 | 1.00 |
| hand | 16051.0 ± 730.8 | -3425.0 ± 637.5 | 2252.1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.316 | 0.000 | 11.40 | 0.00 | 0.60 |

The stamp rate by seat kind (2.8.0 §5), plant / real, with the decisions pooled over the seeds in parentheses — under 2.7.0 a plant reached the initial review alone; under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| greedy | 0.074 (6523) / 0.087 (24657) | 0.458 (1136) / 0.490 (9785) | 0.174 (384) / 0.134 (1770) | — / — |
| careful | 0.000 (6072) / 0.000 (28076) | 0.000 (1145) / 0.000 (12689) | 0.000 (431) / 0.000 (2433) | — / — |
| stamper | 1.000 (1432) / 1.000 (8590) | — / 1.000 (217) | — / 1.000 (18) | — / — |
| hand | 0.000 (6234) / 0.000 (24577) | 0.000 (1277) / 0.000 (10496) | 0.000 (423) / 0.000 (2035) | — / — |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 0.814 | 0.848 | 0.964 (55) | 0.335 (1868) | 0.188 (8858) | 0.199 (10748) | 0.166 (22726) | 19.050 | 145.550 | 2.813 | 1.530 |
| careful | — | 0.740 | 0.000 (2430) | 0.000 (10779) | 0.000 (8620) | 0.000 (6625) | 0.000 (22392) | 12.650 | 230.700 | 2.206 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (10257) | 35.150 | 94.450 | 4.253 | 2.494 |
| hand | — | 0.811 | 0.000 (24) | 0.000 (5413) | 0.000 (9611) | 0.000 (7805) | 0.000 (22189) | 18.650 | 184.050 | 2.625 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| greedy | 20.350 | 0.000 | 0.000 | 0.000 | 0.000 | 0.100 | 0.000 |
| careful | 20.400 | 0.000 | 0.000 | 0.000 | 0.000 | 0.350 | 0.000 |
| stamper | 20.450 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| hand | 20.350 | 0.000 | 0.000 | 0.000 | 0.000 | 0.600 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 9.500 / 20.350 | 18.400 ± 1.055 | +9.550 ± 1.489 | 60.500 | +22.750 ± 2.413 | 7.900 | 0.092 | 16.000 | +7.850 ± 0.971 | 1690.300 | 0.047 | +0.003 ± 0.002 | 0.000 / 0.000 (0.000 / 0.000) | 15852.072 ± 630.603 | -672.415 ± 534.054 | 16686.9 ± 678.8 | -2789.1 ± 779.5 | 32.261 | -2.284 ± 0.452 | 20.799 ± 0.459 | +2.112 ± 0.841 | 19.733 | 0.007 | 2453.250 | 19.850 | 20.250 | +0.900 ± 0.376 | 72.321 | 164.050 |
| careful | 12.050 / 20.400 | 8.850 ± 0.805 | — | 37.750 | — | 7.400 | 0.061 | 8.150 | — | 1604.000 | 0.044 | — | 0.000 / 0.000 (0.000 / 0.000) | 16524.488 ± 661.951 | — | 19476.0 ± 680.0 | — | 34.545 | — | 18.688 ± 0.714 | — | 18.626 | 0.005 | 2556.400 | 19.850 | 19.350 | — | 402.222 | 208.450 |
| stamper | 0.000 / 20.450 | 14.650 ± 0.916 | +5.800 ± 1.301 | 91.750 | +54.000 ± 2.342 | 4.650 | 0.056 | 33.350 | +25.200 ± 0.839 | 1526.100 | 0.091 | +0.047 ± 0.003 | 0.000 / 0.000 (0.000 / 0.000) | 3621.714 ± 145.480 | -12902.774 ± 684.362 | 3754.7 ± 123.4 | -15721.3 ± 650.1 | 27.726 | -6.819 ± 0.467 | 28.299 ± 0.366 | +9.611 ± 0.815 | 24.249 | 0.330 | 1421.100 | 20.000 | 29.150 | +9.800 ± 0.484 | 86.099 | 174.750 |
| hand | 10.250 / 20.350 | 11.400 ± 0.741 | +2.550 ± 1.080 | 65.950 | +28.200 ± 2.843 | 7.250 | 0.055 | 16.500 | +8.350 ± 0.982 | 1638.350 | 0.062 | +0.017 ± 0.002 | 0.000 / 0.000 (0.000 / 0.000) | 15418.576 ± 511.616 | -1105.911 ± 520.255 | 16051.0 ± 730.8 | -3425.0 ± 637.5 | 31.511 | -3.034 ± 0.585 | 21.146 ± 0.555 | +2.458 ± 0.978 | 20.493 | 0.025 | 2365.950 | 19.900 | 20.150 | +0.800 ± 0.479 | 64.918 | 193.700 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **greedy**: p0 0.911/0.089/0.000 (293); p1 0.686/0.314/0.000 (181); p2 0.695/0.305/0.000 (128); p3 0.791/0.209/0.000 (124); p4 0.822/0.178/0.000 (167); p5 0.815/0.185/0.000 (144); p6 0.802/0.198/0.000 (160); p7 0.841/0.159/0.000 (151); p8 0.847/0.153/0.000 (166); p9 0.829/0.171/0.000 (164); p10 0.817/0.183/0.000 (179); p11 0.784/0.216/0.000 (164); p12 0.842/0.158/0.000 (125); p13 0.834/0.166/0.000 (49); p14 0.857/0.143/0.000 (17)
- **careful**: p0 1.000/0.000/0.000 (301); p1 1.000/0.000/0.000 (256); p2 1.000/0.000/0.000 (217); p3 1.000/0.000/0.000 (210); p4 1.000/0.000/0.000 (219); p5 1.000/0.000/0.000 (228); p6 1.000/0.000/0.000 (218); p7 1.000/0.000/0.000 (200); p8 1.000/0.000/0.000 (197); p9 1.000/0.000/0.000 (170); p10 1.000/0.000/0.000 (155); p11 1.000/0.000/0.000 (112); p12 1.000/0.000/0.000 (60)
- **stamper**: p0 0.000/1.000/0.000 (295); p1 0.000/1.000/0.000 (139); p2 0.000/1.000/0.000 (56); p3 0.000/1.000/0.000 (20); p4 0.000/1.000/0.000 (3); p5 0.000/1.000/0.000 (0)
- **hand**: p0 —/—/— (0); p1 —/—/— (0); p2 —/—/— (0); p3 —/—/— (0); p4 —/—/— (0); p5 —/—/— (0); p6 —/—/— (0); p7 —/—/— (0); p8 —/—/— (0); p9 —/—/— (0); p10 —/—/— (0); p11 —/—/— (0); p12 —/—/— (0); p13 —/—/— (0); p14 —/—/— (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 2455.8 / 654.5 | 0.68 / 0.73 | +0.05 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.14 / 0.14 | -0.00 ± 0.00 | 0.385 / 0.393 | +0.009 ± 0.007 | 0.174 / 0.195 | 0.007 / 0.006 | 0.054 / 0.058 | +0.003 ± 0.003 | 2.23 / 2.27 | +0.03 ± 0.06 |
| careful | 2560.8 / 545.3 | 0.38 / 0.27 | -0.11 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.12 / 0.14 | +0.01 ± 0.00 | 0.177 / 0.158 | -0.019 ± 0.005 | 0.076 / 0.086 | 0.005 / 0.003 | 0.042 / 0.042 | +0.000 ± 0.002 | 1.95 / 1.62 | -0.33 ± 0.10 |
| stamper | 2078.2 / 520.5 | 2.05 / 2.20 | +0.16 ± 0.04 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.12 / 0.14 | +0.01 ± 0.00 | 0.559 / 0.617 | +0.058 ± 0.006 | 0.350 / 0.391 | 0.324 / 0.389 | 0.024 / 0.016 | -0.008 ± 0.002 | 3.36 / 2.76 | -0.60 ± 0.27 |
| hand | 2412.9 / 610.2 | 0.91 / 0.91 | +0.00 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.14 / 0.14 | -0.00 ± 0.00 | 0.375 / 0.380 | +0.005 ± 0.005 | 0.167 / 0.186 | 0.025 / 0.028 | 0.052 / 0.051 | -0.002 ± 0.002 | 2.72 / 2.54 | -0.19 ± 0.12 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| greedy | -0.05 ± 0.01 | +0.00 ± 0.00 | -0.03 ± 0.00 | -0.052 ± 0.004 | -0.013 ± 0.003 | -0.000 ± 0.002 |
| careful | -0.13 ± 0.02 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.042 ± 0.005 | -0.007 ± 0.003 | +0.001 ± 0.002 |
| stamper | -0.19 ± 0.04 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.054 ± 0.004 | -0.035 ± 0.005 | -0.004 ± 0.002 |
| hand | -0.12 ± 0.02 | +0.00 ± 0.00 | -0.03 ± 0.00 | -0.052 ± 0.004 | -0.013 ± 0.003 | -0.002 ± 0.002 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| greedy | 0.433 / 0.195 | 0.13 / 0.14 | 0.035 / 0.012 | 0.00 / 0.00 | 0.10 / 0.17 | 0.301 / 0.129 |
| careful | 0.404 / 0.170 | 0.16 / 0.18 | 0.036 / 0.013 | 0.00 / 0.00 | 0.11 / 0.05 | 0.265 / 0.112 |
| stamper | 0.368 / 0.175 | 0.16 / 0.17 | 0.016 / 0.009 | 0.00 / 0.00 | 0.13 / 0.09 | 0.427 / 0.312 |
| hand | 0.407 / 0.196 | 0.11 / 0.14 | 0.033 / 0.012 | 0.00 / 0.00 | 0.07 / 0.10 | 0.323 / 0.174 |

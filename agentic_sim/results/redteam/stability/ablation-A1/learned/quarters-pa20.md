# The frozen policy in a 1,000-tick run, read by quarter — `pa20` (D2, the economy reviewer's addendum 4; `quarters.py`)

Cell: `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --pi-a0 0.20 --pi-a-max 0.20`; seeds 21-40. Means over the seeds (± SE where shown). A quarter is 250 ticks; the seats by the quarter of the seat's assignment, the standing false approvals by the quarter of their vesting, the fees by the quarter of their payment, the snapshots at the first decision at or after the boundary (the members alive and the tiers at that moment; the cost of truth cumulative there). The audit and panel seats are on members' real deliveries (the plants' beside); a member's seat inspected (care spent) or blind (none spent, a verdict of either sign).

## direct (20 seeds; the standing false approvals a run 4.5 ± 0.4, care 0.954, m^A at the end 1.43)

**The dials by close** (mean over the seeds that reached the close): 

| close | t | m_t | π_t | m^A | π^A | m^La | m^Ld | planted approvals adjudicated at a member's audit seat | F̂^A read (n) |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 189 | 1.05 | 0.105 | 1.07 | 0.200 | 1.00 | 1.00 | 2.6 | 0.17 (2) |
| 1 | 379 | 1.05 | 0.105 | 1.22 | 0.200 | 1.00 | 1.00 | 22.1 | 0.09 (16) |
| 2 | 567 | 1.09 | 0.109 | 1.49 | 0.200 | 1.00 | 1.00 | 53.1 | 0.09 (20) |
| 3 | 745 | 1.15 | 0.115 | 1.47 | 0.200 | 1.05 | 1.00 | 63.3 | 0.06 (20) |
| 4 | 912 | 1.26 | 0.126 | 1.46 | 0.200 | 1.05 | 1.00 | 61.2 | 0.06 (20) |
| 5 | 977 | 1.78 | 0.178 | 1.60 | 0.200 | 1.17 | 1.00 | 47.4 | 0.06 (5) |

**By quarter**:

| quarter | members alive | duty-ineligible / panel-ineligible of them | probationers / suspended | audit seats on members' work: member inspected / member blind / state | the member's share of them | member blind rate | audit seats on plants: member (blind) / state | panel seats: member inspected / blind / state | standing false approvals vested: member-confirmed / state-confirmed / never audited / other | roots vested | review fees: members / the state | cost of truth (cumulative at the boundary; the quarter's) | m^A / π^A at the boundary |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Q1 (t 0–250) | 18.1 | 0.0 / 17.2 | 18.8 / 0.4 | 32 / 23 / 459 | **0.11** | **0.422** | 7 (2) / 0 | 3 / 5 / 68 | **0.1 ± 0.1** / 0.3 ± 0.1 / 0.0 ± 0.0 / 0.1 | 505 | 1510 / 1427 | 476 (476) | 1.07 / 0.200 |
| Q2 (t 250–500) | 20.8 | 0.0 / 14.6 | 14.7 / 0.7 | 232 / 20 / 208 | **0.55** | **0.079** | 56 (7) / 0 | 28 / 14 / 38 | **0.5 ± 0.1** / 0.2 ± 0.1 / 0.1 ± 0.0 / 0.0 | 470 | 2267 / 686 | 1237 (761) | 1.25 / 0.200 |
| Q3 (t 500–750) | 26.9 | 0.0 / 12.2 | 2.7 / 0.8 | 423 / 14 / 52 | **0.89** | **0.032** | 102 (4) / 0 | 58 / 14 / 13 | **1.1 ± 0.3** / 0.0 ± 0.0 / 0.1 ± 0.1 / 0.1 | 510 | 3256 / 193 | 2546 (1309) | 1.46 / 0.200 |
| Q4 (t 750–1000) | 23.1 | 0.0 / 6.7 | 0.1 / 0.0 | 449 / 9 / 8 | **0.98** | **0.021** | 111 (2) / 0 | 74 / 8 / 4 | **0.5 ± 0.1** / 0.0 ± 0.0 / 1.3 ± 0.3 / 0.1 | 525 | 3219 / 37 | 4000 (1453) | 1.43 / 0.200 |

**The quarter's price** (the system's overhead per task vested in the quarter: the care spent on real and planted cases, the state's seats' cost, the cost of truth and the plants' awarded price, by the quarter of each; the standing false approvals vested in the quarter over the bad deliveries vested in it, per thousand; the bad deliveries here are a member's real roots vested unfulfilled, the false approvals among them those vested approved — every unfulfilled root that vests is a false approval, so the two counts coincide; the leak per thousand bad deliveries is read on the bad deliveries settled in the quarter at every outcome — the driver's `bad_deliveries` by the quarter of the settlement — and the false approvals among them):

| quarter | roots vested | care on real / on plants | the state's seats' cost | the cost of truth (the quarter's) | the plants' price | system overhead a vested task | standing false approvals vested | per thousand tasks vested | bad deliveries settled / false approvals among them | leak per thousand bad deliveries |
|---|---|---|---|---|---|---|---|---|---|---|
| Q1 | 505 | 1742 / 180 | 1542 | 476 | 1682 | **11.14** | 0.6 ± 0.2 | 1.2 | 133 / 0.6 | **4.5** |
| Q2 | 470 | 2162 / 335 | 739 | 761 | 2607 | **14.04** | 0.7 ± 0.2 | 1.5 | 127 / 0.7 | **5.5** |
| Q3 | 510 | 2824 / 597 | 227 | 1309 | 2419 | **14.46** | 1.3 ± 0.3 | 2.5 | 132 / 1.3 | **9.9** |
| Q4 | 525 | 2951 / 699 | 39 | 1453 | 2782 | **15.11** | 1.9 ± 0.4 | 3.5 | 135 / 1.9 | **13.7** |
| the run (the quarters summed) | 2010 | 9679 / 1812 | 2546 | 4000 | 9490 | **13.70** | 4.4 | 2.2 | 528 / 4.4 | **8.4** |

**The whole run.** Review seats a run by who sat and the seat (plants included): member audit 1480, member initial 2881, member panel 465, plant alias initial 239, state audit 731, state initial 3, state panel 124 — the state's share of the review seats **0.151** (858 of 5684). The review fees a run by who sat and the seat kind: member audit 3941, member initial 5109, member panel 1202, state audit 2043, state initial 5, state panel 295 — the members' 10252 in all, the state's 2343. Ω's net 4892.9 ± 64.2; the tasks vested 2013.7 ± 12.7 a run, bad deliveries 527.6 ± 6.7, the standing false approvals 4.5 ± 0.4 — the leak 0.0022 per vested task (the row's), 0.008 per bad delivery; the system's overhead a vested task 13.68, the customers' 12.58; the state's review cost 2546, unreimbursed 0; the cost of truth 4000.

## greedy (20 seeds; the standing false approvals a run 3.1 ± 0.4, care 0.981, m^A at the end 1.03)

**The dials by close** (mean over the seeds that reached the close): 

| close | t | m_t | π_t | m^A | π^A | m^La | m^Ld | planted approvals adjudicated at a member's audit seat | F̂^A read (n) |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 188 | 1.02 | 0.102 | 1.00 | 0.200 | 1.00 | 1.00 | 1.7 | — (0) |
| 1 | 383 | 1.08 | 0.108 | 1.08 | 0.200 | 1.00 | 1.00 | 35.0 | 0.07 (20) |
| 2 | 569 | 1.17 | 0.117 | 1.07 | 0.200 | 1.00 | 1.00 | 57.0 | 0.05 (20) |
| 3 | 752 | 1.18 | 0.118 | 1.05 | 0.200 | 1.02 | 1.00 | 65.0 | 0.04 (20) |
| 4 | 930 | 1.15 | 0.115 | 1.03 | 0.200 | 1.09 | 1.05 | 62.9 | 0.05 (20) |
| 5 | 705 | 3.24 | 0.324 | 1.00 | 0.200 | 1.00 | 1.00 | 19.0 | 0.00 (1) |
| 6 | 785 | 2.92 | 0.292 | 1.00 | 0.200 | 1.00 | 1.00 | 22.0 | 0.05 (1) |
| 7 | 877 | 2.62 | 0.262 | 1.00 | 0.200 | 1.00 | 1.00 | 29.0 | 0.00 (1) |
| 8 | 972 | 2.36 | 0.236 | 1.00 | 0.200 | 1.00 | 1.00 | 30.0 | 0.00 (1) |

**By quarter**:

| quarter | members alive | duty-ineligible / panel-ineligible of them | probationers / suspended | audit seats on members' work: member inspected / member blind / state | the member's share of them | member blind rate | audit seats on plants: member (blind) / state | panel seats: member inspected / blind / state | standing false approvals vested: member-confirmed / state-confirmed / never audited / other | roots vested | review fees: members / the state | cost of truth (cumulative at the boundary; the quarter's) | m^A / π^A at the boundary |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Q1 (t 0–250) | 18.4 | 0.0 / 16.9 | 18.9 / 0.1 | 49 / 16 / 444 | **0.13** | **0.245** | 10 (0) / 0 | 8 / 1 / 72 | **0.2 ± 0.1** / 0.2 ± 0.1 / 0.1 ± 0.0 / 0.1 | 501 | 1529 / 1396 | 524 (524) | 1.00 / 0.200 |
| Q2 (t 250–500) | 20.6 | 0.0 / 14.1 | 13.6 / 1.1 | 303 / 6 / 159 | **0.66** | **0.019** | 69 (2) / 0 | 42 / 6 / 30 | **0.2 ± 0.1** / 0.0 ± 0.0 / 0.2 ± 0.2 / 0.1 | 482 | 2514 / 530 | 1470 (946) | 1.08 / 0.200 |
| Q3 (t 500–750) | 26.6 | 0.0 / 10.3 | 2.0 / 0.7 | 434 / 3 / 43 | **0.91** | **0.006** | 103 (1) / 0 | 66 / 3 / 14 | **0.3 ± 0.1** / 0.1 ± 0.0 / 0.1 ± 0.1 / 0.1 | 510 | 3255 / 160 | 2854 (1384) | 1.07 / 0.200 |
| Q4 (t 750–1000) | 22.8 | 0.0 / 4.7 | 0.0 / 0.0 | 434 / 4 / 3 | **0.99** | **0.010** | 104 (1) / 0 | 73 / 5 / 2 | **0.5 ± 0.2** / 0.0 ± 0.0 / 0.8 ± 0.2 / 0.1 | 518 | 3058 / 14 | 4208 (1355) | 1.03 / 0.200 |

**The quarter's price** (the system's overhead per task vested in the quarter: the care spent on real and planted cases, the state's seats' cost, the cost of truth and the plants' awarded price, by the quarter of each; the standing false approvals vested in the quarter over the bad deliveries vested in it, per thousand; the bad deliveries here are a member's real roots vested unfulfilled, the false approvals among them those vested approved — every unfulfilled root that vests is a false approval, so the two counts coincide; the leak per thousand bad deliveries is read on the bad deliveries settled in the quarter at every outcome — the driver's `bad_deliveries` by the quarter of the settlement — and the false approvals among them):

| quarter | roots vested | care on real / on plants | the state's seats' cost | the cost of truth (the quarter's) | the plants' price | system overhead a vested task | standing false approvals vested | per thousand tasks vested | bad deliveries settled / false approvals among them | leak per thousand bad deliveries |
|---|---|---|---|---|---|---|---|---|---|---|
| Q1 | 501 | 1801 / 193 | 1515 | 524 | 1684 | **11.41** | 0.6 ± 0.2 | 1.1 | 134 / 0.6 | **4.1** |
| Q2 | 482 | 2371 / 440 | 563 | 946 | 2863 | **14.92** | 0.6 ± 0.2 | 1.1 | 124 / 0.6 | **4.4** |
| Q3 | 510 | 2871 / 664 | 185 | 1384 | 2384 | **14.68** | 0.6 ± 0.2 | 1.1 | 126 / 0.6 | **4.4** |
| Q4 | 518 | 2912 / 685 | 17 | 1355 | 2664 | **14.74** | 1.4 ± 0.3 | 2.7 | 130 / 1.4 | **10.7** |
| the run (the quarters summed) | 2011 | 9955 / 1983 | 2279 | 4208 | 9596 | **13.94** | 3.0 | 1.5 | 515 / 3.0 | **5.9** |

**The whole run.** Review seats a run by who sat and the seat (plants included): member audit 1538, member initial 2856, member panel 479, plant alias initial 249, state audit 652, state initial 3, state panel 118 — the state's share of the review seats **0.137** (774 of 5647). The review fees a run by who sat and the seat kind: member audit 4053, member initial 5065, member panel 1237, state audit 1815, state initial 5, state panel 280 — the members' 10355 in all, the state's 2100. Ω's net 4550.2 ± 75.2; the tasks vested 2017.7 ± 19.5 a run, bad deliveries 514.8 ± 8.1, the standing false approvals 3.1 ± 0.4 — the leak 0.0016 per vested task (the row's), 0.006 per bad delivery; the system's overhead a vested task 13.94, the customers' 12.44; the state's review cost 2279, unreimbursed 0; the cost of truth 4208.

## hand (20 seeds; the standing false approvals a run 8.1 ± 0.7, care 0.000, m^A at the end 1.11)

**The dials by close** (mean over the seeds that reached the close): 

| close | t | m_t | π_t | m^A | π^A | m^La | m^Ld | planted approvals adjudicated at a member's audit seat | F̂^A read (n) |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 196 | 2.00 | 0.200 | 1.00 | 0.200 | 1.00 | 1.00 | 0.1 | — (0) |
| 1 | 314 | 4.00 | 0.400 | 1.00 | 0.200 | 1.00 | 1.00 | 7.0 | 0.05 (5) |
| 2 | 382 | 3.98 | 0.398 | 1.02 | 0.200 | 1.00 | 1.00 | 12.3 | 0.04 (17) |
| 3 | 442 | 3.77 | 0.377 | 1.06 | 0.200 | 1.00 | 1.00 | 16.6 | 0.04 (20) |
| 4 | 497 | 3.68 | 0.368 | 1.06 | 0.200 | 1.00 | 1.00 | 20.4 | 0.04 (20) |
| 5 | 554 | 3.53 | 0.353 | 1.03 | 0.200 | 1.06 | 1.00 | 22.4 | 0.02 (20) |
| 6 | 614 | 3.20 | 0.320 | 1.04 | 0.200 | 1.06 | 1.00 | 22.4 | 0.04 (20) |
| 7 | 682 | 2.93 | 0.293 | 1.10 | 0.200 | 1.11 | 1.00 | 25.8 | 0.06 (20) |
| 8 | 755 | 2.64 | 0.264 | 1.12 | 0.200 | 1.16 | 1.04 | 27.4 | 0.05 (20) |
| 9 | 838 | 2.44 | 0.244 | 1.14 | 0.200 | 1.28 | 1.09 | 31.2 | 0.05 (20) |
| 10 | 928 | 2.23 | 0.223 | 1.13 | 0.200 | 1.36 | 1.09 | 32.6 | 0.04 (20) |
| 11 | 966 | 2.47 | 0.247 | 1.12 | 0.200 | 1.46 | 1.14 | 32.7 | 0.07 (6) |

**By quarter**:

| quarter | members alive | duty-ineligible / panel-ineligible of them | probationers / suspended | audit seats on members' work: member inspected / member blind / state | the member's share of them | member blind rate | audit seats on plants: member (blind) / state | panel seats: member inspected / blind / state | standing false approvals vested: member-confirmed / state-confirmed / never audited / other | roots vested | review fees: members / the state | cost of truth (cumulative at the boundary; the quarter's) | m^A / π^A at the boundary |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Q1 (t 0–250) | 15.7 | 0.0 / 15.1 | 19.1 / 2.4 | 20 / 12 / 505 | **0.06** | **0.388** | 2 (0) / 0 | 4 / 1 / 99 | **2.0 ± 0.3** / 2.9 ± 0.4 / 0.0 ± 0.0 / 0.6 | 475 | 1252 / 1647 | 408 (408) | 1.00 / 0.200 |
| Q2 (t 250–500) | 21.6 | 0.0 / 5.0 | 0.8 / 1.7 | 265 / 0 / 114 | **0.70** | **0.000** | 96 (0) / 0 | 46 / 0 / 23 | **0.8 ± 0.2** / 0.6 ± 0.2 / 0.0 ± 0.0 / 0.1 | 365 | 2644 / 535 | 2165 (1757) | 1.06 / 0.200 |
| Q3 (t 500–750) | 21.2 | 0.0 / 3.8 | 0.0 / 0.0 | 472 / 0 / 2 | **1.00** | **0.000** | 144 (0) / 0 | 76 / 0 / 1 | **0.1 ± 0.1** / 0.0 ± 0.0 / 0.0 ± 0.0 / 0.1 | 485 | 3633 / 22 | 4427 (2263) | 1.08 / 0.200 |
| Q4 (t 750–1000) | 20.9 | 0.0 / 2.5 | 0.0 / 0.0 | 457 / 2 / 2 | **1.00** | **0.004** | 128 (1) / 0 | 76 / 0 / 2 | **0.6 ± 0.2** / 0.0 ± 0.0 / 0.0 ± 0.0 / 0.1 | 476 | 3497 / 26 | 6334 (1907) | 1.11 / 0.200 |

**The quarter's price** (the system's overhead per task vested in the quarter: the care spent on real and planted cases, the state's seats' cost, the cost of truth and the plants' awarded price, by the quarter of each; the standing false approvals vested in the quarter over the bad deliveries vested in it, per thousand; the bad deliveries here are a member's real roots vested unfulfilled, the false approvals among them those vested approved — every unfulfilled root that vests is a false approval, so the two counts coincide; the leak per thousand bad deliveries is read on the bad deliveries settled in the quarter at every outcome — the driver's `bad_deliveries` by the quarter of the settlement — and the false approvals among them):

| quarter | roots vested | care on real / on plants | the state's seats' cost | the cost of truth (the quarter's) | the plants' price | system overhead a vested task | standing false approvals vested | per thousand tasks vested | bad deliveries settled / false approvals among them | leak per thousand bad deliveries |
|---|---|---|---|---|---|---|---|---|---|---|
| Q1 | 475 | 905 / 106 | 1820 | 408 | 1947 | **10.91** | 5.5 ± 0.5 | 11.6 | 124 / 5.5 | **44.5** |
| Q2 | 365 | 1977 / 813 | 613 | 1757 | 5159 | **28.24** | 1.4 ± 0.3 | 3.8 | 99 / 1.4 | **14.1** |
| Q3 | 485 | 2894 / 1174 | 31 | 2263 | 5543 | **24.54** | 0.2 ± 0.1 | 0.4 | 125 / 0.2 | **1.6** |
| Q4 | 476 | 2839 / 986 | 38 | 1907 | 4731 | **22.05** | 0.7 ± 0.2 | 1.4 | 124 / 0.7 | **5.3** |
| the run (the quarters summed) | 1802 | 8616 / 3079 | 2502 | 6334 | 17379 | **21.04** | 7.8 | 4.3 | 471 / 7.8 | **16.4** |

**The whole run.** Review seats a run by who sat and the seat (plants included): member audit 1624, member initial 2963, member panel 542, plant alias initial 249, state audit 665, state initial 21, state panel 128 — the state's share of the review seats **0.137** (814 of 5942). The review fees a run by who sat and the seat kind: member audit 4399, member initial 5207, member panel 1419, state audit 1884, state initial 38, state panel 308 — the members' 11025 in all, the state's 2230. Ω's net 4672.5 ± 57.5; the tasks vested 1865.4 ± 15.7 a run, bad deliveries 471.2 ± 7.2, the standing false approvals 8.1 ± 0.7 — the leak 0.0043 per vested task (the row's), 0.017 per bad delivery; the system's overhead a vested task 20.35, the customers' 14.71; the state's review cost 2501, unreimbursed 0; the cost of truth 6334.

## careful (20 seeds; the standing false approvals a run 2.4 ± 0.3, care 1.000, m^A at the end 1.00)

**The dials by close** (mean over the seeds that reached the close): 

| close | t | m_t | π_t | m^A | π^A | m^La | m^Ld | planted approvals adjudicated at a member's audit seat | F̂^A read (n) |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 189 | 1.01 | 0.101 | 1.00 | 0.200 | 1.00 | 1.00 | 1.9 | 0.00 (1) |
| 1 | 385 | 1.01 | 0.101 | 1.03 | 0.200 | 1.00 | 1.00 | 33.2 | 0.06 (19) |
| 2 | 578 | 1.01 | 0.101 | 1.04 | 0.200 | 1.00 | 1.00 | 59.5 | 0.06 (20) |
| 3 | 765 | 1.06 | 0.106 | 1.01 | 0.200 | 1.00 | 1.00 | 66.7 | 0.05 (20) |
| 4 | 945 | 1.03 | 0.103 | 1.00 | 0.200 | 1.01 | 1.15 | 65.0 | 0.05 (20) |

**By quarter**:

| quarter | members alive | duty-ineligible / panel-ineligible of them | probationers / suspended | audit seats on members' work: member inspected / member blind / state | the member's share of them | member blind rate | audit seats on plants: member (blind) / state | panel seats: member inspected / blind / state | standing false approvals vested: member-confirmed / state-confirmed / never audited / other | roots vested | review fees: members / the state | cost of truth (cumulative at the boundary; the quarter's) | m^A / π^A at the boundary |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Q1 (t 0–250) | 18.4 | 0.0 / 17.2 | 18.7 / 0.2 | 65 / 0 / 441 | **0.13** | **0.000** | 10 (0) / 0 | 10 / 0 / 73 | **0.0 ± 0.0** / 0.1 ± 0.1 / 0.0 ± 0.0 / 0.0 | 504 | 1538 / 1388 | 495 (495) | 1.00 / 0.200 |
| Q2 (t 250–500) | 21.4 | 0.0 / 14.8 | 13.7 / 1.1 | 309 / 0 / 166 | **0.65** | **0.000** | 70 (0) / 0 | 44 / 0 / 33 | **0.1 ± 0.1** / 0.1 ± 0.1 / 0.1 ± 0.1 / 0.1 | 491 | 2478 / 550 | 1462 (968) | 1.03 / 0.200 |
| Q3 (t 500–750) | 28.6 | 0.0 / 12.8 | 2.8 / 0.5 | 436 / 0 / 54 | **0.89** | **0.000** | 100 (0) / 0 | 69 / 0 / 16 | **0.1 ± 0.1** / 0.1 ± 0.1 / 0.2 ± 0.1 / 0.2 | 523 | 3201 / 191 | 2834 (1372) | 1.04 / 0.200 |
| Q4 (t 750–1000) | 24.0 | 0.0 / 5.7 | 0.0 / 0.0 | 441 / 2 / 7 | **0.98** | **0.004** | 104 (1) / 0 | 83 / 0 / 4 | **0.1 ± 0.1** / 0.0 ± 0.0 / 0.9 ± 0.2 / 0.1 | 527 | 3039 / 29 | 4221 (1388) | 1.00 / 0.200 |

**The quarter's price** (the system's overhead per task vested in the quarter: the care spent on real and planted cases, the state's seats' cost, the cost of truth and the plants' awarded price, by the quarter of each; the standing false approvals vested in the quarter over the bad deliveries vested in it, per thousand; the bad deliveries here are a member's real roots vested unfulfilled, the false approvals among them those vested approved — every unfulfilled root that vests is a false approval, so the two counts coincide; the leak per thousand bad deliveries is read on the bad deliveries settled in the quarter at every outcome — the driver's `bad_deliveries` by the quarter of the settlement — and the false approvals among them):

| quarter | roots vested | care on real / on plants | the state's seats' cost | the cost of truth (the quarter's) | the plants' price | system overhead a vested task | standing false approvals vested | per thousand tasks vested | bad deliveries settled / false approvals among them | leak per thousand bad deliveries |
|---|---|---|---|---|---|---|---|---|---|---|
| Q1 | 504 | 1841 / 195 | 1508 | 495 | 1704 | **11.40** | 0.1 ± 0.1 | 0.2 | 131 / 0.1 | **0.8** |
| Q2 | 491 | 2425 / 474 | 579 | 968 | 2597 | **14.35** | 0.5 ± 0.1 | 0.9 | 120 / 0.5 | **3.8** |
| Q3 | 523 | 2911 / 660 | 213 | 1372 | 2154 | **13.98** | 0.7 ± 0.2 | 1.3 | 133 / 0.7 | **5.3** |
| Q4 | 527 | 2980 / 703 | 31 | 1388 | 2413 | **14.25** | 1.1 ± 0.2 | 2.2 | 133 / 1.1 | **8.6** |
| the run (the quarters summed) | 2045 | 10157 / 2033 | 2332 | 4221 | 8868 | **13.50** | 2.4 | 1.2 | 518 / 2.4 | **4.6** |

**The whole run.** Review seats a run by who sat and the seat (plants included): member audit 1536, member initial 2871, member panel 476, plant alias initial 249, state audit 669, state initial 2, state panel 126 — the state's share of the review seats **0.140** (797 of 5680). The review fees a run by who sat and the seat kind: member audit 3984, member initial 5061, member panel 1212, state audit 1857, state initial 4, state panel 296 — the members' 10256 in all, the state's 2157. Ω's net 4555.8 ± 81.0; the tasks vested 2046.4 ± 9.2 a run, bad deliveries 517.8 ± 5.1, the standing false approvals 2.4 ± 0.3 — the leak 0.0012 per vested task (the row's), 0.005 per bad delivery; the system's overhead a vested task 13.49, the customers' 12.26; the state's review cost 2331, unreimbursed 0; the cost of truth 4221.


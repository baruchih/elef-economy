# The frozen policy in a 1,000-tick run, read by quarter — `pa10` (D2, the economy reviewer's addendum 4; `quarters.py`)

Cell: `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --pi-a0 0.10 --pi-a-max 0.10`; seeds 21-40. Means over the seeds (± SE where shown). A quarter is 250 ticks; the seats by the quarter of the seat's assignment, the standing false approvals by the quarter of their vesting, the fees by the quarter of their payment, the snapshots at the first decision at or after the boundary (the members alive and the tiers at that moment; the cost of truth cumulative there). The audit and panel seats are on members' real deliveries (the plants' beside); a member's seat inspected (care spent) or blind (none spent, a verdict of either sign).

## direct (20 seeds; the standing false approvals a run 5.5 ± 0.7, care 0.936, m^A at the end 4.68)

**The dials by close** (mean over the seeds that reached the close): 

| close | t | m_t | π_t | m^A | π^A | m^La | m^Ld | planted approvals adjudicated at a member's audit seat | F̂^A read (n) |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 189 | 1.02 | 0.102 | 1.00 | 0.100 | 1.00 | 1.00 | 0.8 | — (0) |
| 1 | 383 | 1.03 | 0.103 | 1.49 | 0.100 | 1.00 | 1.00 | 11.6 | 0.28 (13) |
| 2 | 574 | 1.09 | 0.109 | 2.47 | 0.100 | 1.00 | 1.00 | 24.7 | 0.19 (20) |
| 3 | 754 | 1.10 | 0.110 | 3.65 | 0.100 | 1.19 | 1.00 | 30.4 | 0.16 (20) |
| 4 | 935 | 1.11 | 0.111 | 4.44 | 0.100 | 1.29 | 1.00 | 33.6 | 0.11 (20) |
| 5 | 831 | 1.84 | 0.184 | 4.17 | 0.100 | 1.00 | 1.00 | 20.0 | 0.15 (1) |
| 6 | 936 | 1.66 | 0.166 | 7.58 | 0.100 | 1.00 | 1.00 | 22.0 | 0.18 (1) |

**By quarter**:

| quarter | members alive | duty-ineligible / panel-ineligible of them | probationers / suspended | audit seats on members' work: member inspected / member blind / state | the member's share of them | member blind rate | audit seats on plants: member (blind) / state | panel seats: member inspected / blind / state | standing false approvals vested: member-confirmed / state-confirmed / never audited / other | roots vested | review fees: members / the state | cost of truth (cumulative at the boundary; the quarter's) | m^A / π^A at the boundary |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Q1 (t 0–250) | 18.1 | 0.0 / 16.9 | 18.9 / 0.3 | 28 / 29 / 452 | **0.11** | **0.512** | 4 (1) / 0 | 5 / 2 / 75 | **0.2 ± 0.1** / 0.1 ± 0.1 / 0.0 ± 0.0 / 0.1 | 504 | 1482 / 1427 | 442 (442) | 1.00 / 0.100 |
| Q2 (t 250–500) | 20.1 | 0.0 / 15.4 | 15.6 / 0.7 | 171 / 67 / 232 | **0.51** | **0.281** | 29 (7) / 0 | 23 / 12 / 45 | **1.1 ± 0.2** / 0.1 ± 0.1 / 0.1 ± 0.1 / 0.1 | 480 | 2065 / 752 | 917 (475) | 1.49 / 0.100 |
| Q3 (t 500–750) | 24.9 | 0.0 / 12.6 | 5.3 / 0.6 | 359 / 48 / 84 | **0.83** | **0.118** | 55 (7) / 0 | 51 / 8 / 19 | **0.8 ± 0.2** / 0.2 ± 0.1 / 0.6 ± 0.2 / 0.1 | 512 | 2874 / 300 | 1737 (820) | 2.68 / 0.100 |
| Q4 (t 750–1000) | 23.0 | 0.0 / 6.3 | 0.1 / 0.1 | 426 / 32 / 10 | **0.98** | **0.069** | 61 (4) / 0 | 73 / 8 / 5 | **0.9 ± 0.3** / 0.0 ± 0.0 / 1.0 ± 0.3 / 0.0 | 524 | 2943 / 46 | 2641 (904) | 4.68 / 0.100 |

**The whole run.** Review seats a run by who sat and the seat (plants included): member audit 1308, member initial 2867, member panel 321, plant alias initial 115, state audit 779, state initial 1, state panel 146 — the state's share of the review seats **0.171** (926 of 5422). The review fees a run by who sat and the seat kind: member audit 3456, member initial 5109, member panel 800, state audit 2177, state initial 2, state panel 345 — the members' 9365 in all, the state's 2525. Ω's net 5046.1 ± 95.0; the tasks vested 2021.6 ± 10.4 a run, bad deliveries 518.5 ± 5.4, the standing false approvals 5.5 ± 0.7 — the leak 0.0027 per vested task (the row's), 0.011 per bad delivery; the system's overhead a vested task 11.40, the customers' 12.40; the state's review cost 2754, unreimbursed 0; the cost of truth 2641.

## greedy (20 seeds; the standing false approvals a run 4.0 ± 0.4, care 0.974, m^A at the end 2.13)

**The dials by close** (mean over the seeds that reached the close): 

| close | t | m_t | π_t | m^A | π^A | m^La | m^Ld | planted approvals adjudicated at a member's audit seat | F̂^A read (n) |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 189 | 1.04 | 0.104 | 1.00 | 0.100 | 1.00 | 1.00 | 1.6 | 0.09 (1) |
| 1 | 381 | 1.03 | 0.103 | 1.33 | 0.100 | 1.00 | 1.00 | 14.4 | 0.15 (14) |
| 2 | 575 | 1.08 | 0.108 | 1.61 | 0.100 | 1.00 | 1.00 | 23.1 | 0.13 (19) |
| 3 | 758 | 1.08 | 0.108 | 1.80 | 0.100 | 1.06 | 1.00 | 32.2 | 0.09 (20) |
| 4 | 940 | 1.09 | 0.109 | 2.13 | 0.100 | 1.06 | 1.07 | 33.3 | 0.12 (20) |
| 5 | 721 | 1.63 | 0.163 | 1.89 | 0.100 | 1.00 | 1.00 | 20.0 | 0.10 (1) |
| 6 | 835 | 1.47 | 0.147 | 1.71 | 0.100 | 1.00 | 1.00 | 22.0 | 0.00 (1) |
| 7 | 972 | 1.32 | 0.132 | 2.05 | 0.100 | 1.00 | 1.00 | 25.0 | 0.12 (1) |

**By quarter**:

| quarter | members alive | duty-ineligible / panel-ineligible of them | probationers / suspended | audit seats on members' work: member inspected / member blind / state | the member's share of them | member blind rate | audit seats on plants: member (blind) / state | panel seats: member inspected / blind / state | standing false approvals vested: member-confirmed / state-confirmed / never audited / other | roots vested | review fees: members / the state | cost of truth (cumulative at the boundary; the quarter's) | m^A / π^A at the boundary |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Q1 (t 0–250) | 17.8 | 0.0 / 16.6 | 19.1 / 0.1 | 52 / 21 / 435 | **0.14** | **0.283** | 6 (1) / 0 | 10 / 1 / 69 | **0.2 ± 0.1** / 0.2 ± 0.1 / 0.0 ± 0.0 / 0.0 | 504 | 1545 / 1370 | 485 (485) | 1.00 / 0.100 |
| Q2 (t 250–500) | 19.4 | 0.0 / 13.7 | 15.4 / 0.7 | 216 / 23 / 216 | **0.53** | **0.096** | 29 (2) / 0 | 33 / 1 / 39 | **0.7 ± 0.2** / 0.1 ± 0.1 / 0.0 ± 0.0 / 0.1 | 470 | 2066 / 699 | 1008 (523) | 1.33 / 0.100 |
| Q3 (t 500–750) | 26.4 | 0.0 / 11.1 | 4.5 / 0.9 | 400 / 15 / 63 | **0.87** | **0.037** | 54 (2) / 0 | 60 / 1 / 16 | **0.2 ± 0.1** / 0.1 ± 0.0 / 0.3 ± 0.1 / 0.0 | 503 | 2892 / 234 | 1818 (810) | 1.61 / 0.100 |
| Q4 (t 750–1000) | 23.9 | 0.0 / 6.2 | 0.2 / 0.1 | 416 / 37 / 9 | **0.98** | **0.081** | 61 (5) / 0 | 78 / 1 / 4 | **0.9 ± 0.3** / 0.0 ± 0.0 / 1.1 ± 0.3 / 0.0 | 522 | 2840 / 36 | 2745 (928) | 2.13 / 0.100 |

**The whole run.** Review seats a run by who sat and the seat (plants included): member audit 1332, member initial 2835, member panel 327, plant alias initial 117, state audit 726, state initial 2, state panel 129 — the state's share of the review seats **0.160** (857 of 5351). The review fees a run by who sat and the seat kind: member audit 3479, member initial 5056, member panel 809, state audit 2029, state initial 3, state panel 306 — the members' 9344 in all, the state's 2339. Ω's net 4736.5 ± 107.9; the tasks vested 2003.9 ± 15.4 a run, bad deliveries 518.5 ± 7.3, the standing false approvals 4.0 ± 0.4 — the leak 0.0020 per vested task (the row's), 0.008 per bad delivery; the system's overhead a vested task 11.59, the customers' 12.42; the state's review cost 2569, unreimbursed 0; the cost of truth 2745.

## hand (20 seeds; the standing false approvals a run 7.7 ± 0.7, care 0.000, m^A at the end 1.51)

**The dials by close** (mean over the seeds that reached the close): 

| close | t | m_t | π_t | m^A | π^A | m^La | m^Ld | planted approvals adjudicated at a member's audit seat | F̂^A read (n) |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 195 | 2.00 | 0.200 | 1.00 | 0.100 | 1.00 | 1.00 | 0.7 | — (0) |
| 1 | 312 | 4.00 | 0.400 | 1.00 | 0.100 | 1.00 | 1.00 | 3.4 | 0.09 (2) |
| 2 | 383 | 4.00 | 0.400 | 1.02 | 0.100 | 1.00 | 1.00 | 6.0 | 0.06 (5) |
| 3 | 443 | 3.92 | 0.392 | 1.05 | 0.100 | 1.00 | 1.00 | 7.4 | 0.06 (16) |
| 4 | 498 | 3.69 | 0.369 | 1.07 | 0.100 | 1.00 | 1.00 | 9.6 | 0.07 (12) |
| 5 | 553 | 3.53 | 0.353 | 1.23 | 0.100 | 1.05 | 1.00 | 11.1 | 0.06 (19) |
| 6 | 612 | 3.20 | 0.320 | 1.40 | 0.100 | 1.05 | 1.00 | 11.2 | 0.07 (17) |
| 7 | 678 | 2.96 | 0.296 | 1.42 | 0.100 | 1.04 | 1.00 | 12.3 | 0.04 (20) |
| 8 | 752 | 2.82 | 0.282 | 1.70 | 0.100 | 1.04 | 1.00 | 13.7 | 0.05 (20) |
| 9 | 830 | 2.59 | 0.259 | 1.59 | 0.100 | 1.06 | 1.00 | 14.2 | 0.03 (19) |
| 10 | 917 | 2.44 | 0.244 | 1.60 | 0.100 | 1.06 | 1.00 | 15.6 | 0.06 (20) |
| 11 | 938 | 2.78 | 0.278 | 1.55 | 0.100 | 1.05 | 1.00 | 14.9 | 0.02 (9) |
| 12 | 951 | 3.43 | 0.343 | 1.80 | 0.100 | 1.00 | 1.00 | 11.0 | 0.09 (3) |
| 13 | 959 | 3.15 | 0.315 | 2.22 | 0.100 | 1.00 | 1.00 | 11.0 | 0.09 (1) |

**By quarter**:

| quarter | members alive | duty-ineligible / panel-ineligible of them | probationers / suspended | audit seats on members' work: member inspected / member blind / state | the member's share of them | member blind rate | audit seats on plants: member (blind) / state | panel seats: member inspected / blind / state | standing false approvals vested: member-confirmed / state-confirmed / never audited / other | roots vested | review fees: members / the state | cost of truth (cumulative at the boundary; the quarter's) | m^A / π^A at the boundary |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Q1 (t 0–250) | 16.4 | 0.0 / 15.8 | 19.1 / 1.6 | 28 / 12 / 502 | **0.07** | **0.311** | 3 (0) / 0 | 7 / 1 / 99 | **2.1 ± 0.4** / 2.9 ± 0.3 / 0.0 ± 0.0 / 0.5 | 482 | 1302 / 1623 | 412 (412) | 1.00 / 0.100 |
| Q2 (t 250–500) | 20.6 | 0.0 / 5.1 | 1.7 / 1.4 | 246 / 0 / 124 | **0.67** | **0.000** | 65 (0) / 0 | 42 / 0 / 30 | **0.5 ± 0.2** / 0.7 ± 0.2 / 0.0 ± 0.0 / 0.2 | 359 | 2380 / 585 | 1792 (1381) | 1.04 / 0.100 |
| Q3 (t 500–750) | 20.8 | 0.0 / 3.5 | 0.0 / 0.0 | 473 / 0 / 3 | **0.99** | **0.000** | 101 (0) / 0 | 77 / 0 / 2 | **0.2 ± 0.1** / 0.0 ± 0.0 / 0.0 ± 0.0 / 0.1 | 489 | 3401 / 26 | 3594 (1802) | 1.54 / 0.100 |
| Q4 (t 750–1000) | 20.2 | 0.0 / 2.8 | 0.0 / 0.0 | 452 / 2 / 2 | **1.00** | **0.005** | 84 (0) / 0 | 74 / 0 / 1 | **0.2 ± 0.1** / 0.0 ± 0.0 / 0.0 ± 0.0 / 0.0 | 469 | 3248 / 23 | 5100 (1506) | 1.51 / 0.100 |

**The whole run.** Review seats a run by who sat and the seat (plants included): member audit 1490, member initial 2972, member panel 420, plant alias initial 122, state audit 674, state initial 17, state panel 135 — the state's share of the review seats **0.145** (827 of 5709). The review fees a run by who sat and the seat kind: member audit 4017, member initial 5229, member panel 1085, state audit 1900, state initial 31, state panel 326 — the members' 10330 in all, the state's 2257. Ω's net 4652.5 ± 47.6; the tasks vested 1862.0 ± 14.5 a run, bad deliveries 467.5 ± 6.5, the standing false approvals 7.7 ± 0.7 — the leak 0.0041 per vested task (the row's), 0.016 per bad delivery; the system's overhead a vested task 18.25, the customers' 14.78; the state's review cost 2544, unreimbursed 0; the cost of truth 5100.

## careful (20 seeds; the standing false approvals a run 2.5 ± 0.4, care 1.000, m^A at the end 1.05)

**The dials by close** (mean over the seeds that reached the close): 

| close | t | m_t | π_t | m^A | π^A | m^La | m^Ld | planted approvals adjudicated at a member's audit seat | F̂^A read (n) |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 189 | 1.01 | 0.101 | 1.00 | 0.100 | 1.00 | 1.00 | 1.8 | 0.00 (1) |
| 1 | 383 | 1.05 | 0.105 | 1.00 | 0.100 | 1.00 | 1.00 | 15.7 | 0.06 (17) |
| 2 | 571 | 1.06 | 0.106 | 1.03 | 0.100 | 1.03 | 1.00 | 27.5 | 0.05 (20) |
| 3 | 755 | 1.05 | 0.105 | 1.02 | 0.100 | 1.10 | 1.00 | 33.7 | 0.05 (20) |
| 4 | 938 | 1.06 | 0.106 | 1.04 | 0.100 | 1.14 | 1.05 | 32.8 | 0.04 (20) |
| 5 | 844 | 1.32 | 0.132 | 1.00 | 0.100 | 2.00 | 1.00 | 23.0 | 0.00 (1) |
| 6 | 991 | 1.65 | 0.165 | 1.25 | 0.100 | 1.80 | 1.00 | 24.0 | 0.12 (1) |

**By quarter**:

| quarter | members alive | duty-ineligible / panel-ineligible of them | probationers / suspended | audit seats on members' work: member inspected / member blind / state | the member's share of them | member blind rate | audit seats on plants: member (blind) / state | panel seats: member inspected / blind / state | standing false approvals vested: member-confirmed / state-confirmed / never audited / other | roots vested | review fees: members / the state | cost of truth (cumulative at the boundary; the quarter's) | m^A / π^A at the boundary |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Q1 (t 0–250) | 18.3 | 0.0 / 17.1 | 18.6 / 0.3 | 72 / 0 / 436 | **0.14** | **0.000** | 7 (0) / 0 | 11 / 0 / 71 | **0.1 ± 0.0** / 0.2 ± 0.1 / 0.0 ± 0.0 / 0.0 | 503 | 1536 / 1366 | 460 (460) | 1.00 / 0.100 |
| Q2 (t 250–500) | 21.0 | 0.0 / 13.7 | 13.8 / 0.8 | 288 / 0 / 184 | **0.61** | **0.000** | 36 (0) / 0 | 44 / 0 / 34 | **0.1 ± 0.1** / 0.1 ± 0.1 / 0.1 ± 0.0 / 0.1 | 487 | 2271 / 597 | 1087 (627) | 1.00 / 0.100 |
| Q3 (t 500–750) | 27.6 | 0.0 / 10.1 | 2.6 / 0.5 | 447 / 0 / 38 | **0.92** | **0.000** | 59 (0) / 0 | 75 / 0 / 11 | **0.4 ± 0.2** / 0.0 ± 0.0 / 0.5 ± 0.2 / 0.0 | 517 | 3007 / 142 | 2043 (955) | 1.02 / 0.100 |
| Q4 (t 750–1000) | 22.9 | 0.0 / 5.0 | 0.1 / 0.0 | 441 / 2 / 3 | **0.99** | **0.004** | 58 (0) / 0 | 78 / 0 / 3 | **0.1 ± 0.1** / 0.0 ± 0.0 / 0.8 ± 0.2 / 0.1 | 525 | 2778 / 17 | 2954 (911) | 1.05 / 0.100 |

**The whole run.** Review seats a run by who sat and the seat (plants included): member audit 1409, member initial 2862, member panel 372, plant alias initial 124, state audit 663, state initial 2, state panel 119 — the state's share of the review seats **0.144** (784 of 5427). The review fees a run by who sat and the seat kind: member audit 3630, member initial 5049, member panel 914, state audit 1840, state initial 3, state panel 278 — the members' 9593 in all, the state's 2122. Ω's net 4485.0 ± 88.8; the tasks vested 2034.7 ± 13.1 a run, bad deliveries 517.0 ± 6.4, the standing false approvals 2.5 ± 0.4 — the leak 0.0013 per vested task (the row's), 0.005 per bad delivery; the system's overhead a vested task 11.69, the customers' 12.30; the state's review cost 2309, unreimbursed 0; the cost of truth 2954.


# The frozen policy in a 1,000-tick run, read by quarter — `run42-1000` (D2, the economy reviewer's addendum 4; `quarters.py`)

Cell: `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule`; seeds 21-40. Means over the seeds (± SE where shown). A quarter is 250 ticks; the seats by the quarter of the seat's assignment, the standing false approvals by the quarter of their vesting, the fees by the quarter of their payment, the snapshots at the first decision at or after the boundary (the members alive and the tiers at that moment; the cost of truth cumulative there). The audit and panel seats are on members' real deliveries (the plants' beside); a member's seat inspected (care spent) or blind (none spent, a verdict of either sign).

## direct (20 seeds; the standing false approvals a run 16.3 ± 1.2, care 0.825, m^A at the end 4.77)

**The dials by close** (mean over the seeds that reached the close): 

| close | t | m_t | π_t | m^A | π^A | m^La | m^Ld | planted approvals adjudicated at a member's audit seat | F̂^A read (n) |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 188 | 1.00 | 0.100 | 1.00 | 0.020 | 1.00 | 1.00 | 0.2 | — (0) |
| 1 | 385 | 1.01 | 0.101 | 1.00 | 0.020 | 1.00 | 1.00 | 2.5 | — (0) |
| 2 | 576 | 1.07 | 0.107 | 1.15 | 0.023 | 1.10 | 1.00 | 5.1 | 0.37 (3) |
| 3 | 758 | 1.18 | 0.118 | 2.30 | 0.046 | 1.30 | 1.00 | 6.8 | 0.54 (20) |
| 4 | 926 | 1.15 | 0.115 | 4.37 | 0.087 | 1.44 | 1.00 | 13.6 | 0.44 (18) |
| 5 | 952 | 1.83 | 0.183 | 5.33 | 0.107 | 1.74 | 1.00 | 12.0 | 0.31 (3) |

**By quarter**:

| quarter | members alive | duty-ineligible / panel-ineligible of them | probationers / suspended | audit seats on members' work: member inspected / member blind / state | the member's share of them | member blind rate | audit seats on plants: member (blind) / state | panel seats: member inspected / blind / state | standing false approvals vested: member-confirmed / state-confirmed / never audited / other | roots vested | review fees: members / the state | cost of truth (cumulative at the boundary; the quarter's) | m^A / π^A at the boundary |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Q1 (t 0–250) | 18.2 | 0.0 / 17.3 | 18.9 / 0.3 | 9 / 49 / 450 | **0.11** | **0.848** | 1 (1) / 0 | 4 / 3 / 73 | **0.5 ± 0.2** / 0.1 ± 0.1 / 0.0 ± 0.0 / 0.2 | 505 | 1491 / 1410 | 404 (404) | 1.00 / 0.020 |
| Q2 (t 250–500) | 20.4 | 0.0 / 15.2 | 15.2 / 0.7 | 78 / 183 / 213 | **0.55** | **0.702** | 12 (7) / 0 | 20 / 8 / 37 | **3.5 ± 0.5** / 0.2 ± 0.1 / 0.2 ± 0.1 / 0.1 | 491 | 2062 / 682 | 746 (342) | 1.00 / 0.020 |
| Q3 (t 500–750) | 26.9 | 0.0 / 16.0 | 4.3 / 1.1 | 158 / 232 / 108 | **0.78** | **0.595** | 22 (12) / 0 | 44 / 5 / 21 | **4.7 ± 0.6** / 0.2 ± 0.1 / 0.6 ± 0.2 / 0.1 | 525 | 2622 / 363 | 1192 (446) | 1.30 / 0.026 |
| Q4 (t 750–1000) | 23.2 | 0.0 / 10.8 | 0.1 / 0.0 | 286 / 157 / 28 | **0.94** | **0.355** | 42 (14) / 0 | 66 / 5 / 8 | **4.5 ± 0.5** / 0.0 ± 0.0 / 1.2 ± 0.3 / 0.1 | 531 | 2667 / 89 | 1897 (706) | 4.77 / 0.095 |

**The whole run.** Review seats a run by who sat and the seat (plants included): member audit 1230, member initial 2878, member panel 226, plant alias initial 40, state audit 801, state initial 1, state panel 139 — the state's share of the review seats **0.178** (941 of 5275). The review fees a run by who sat and the seat kind: member audit 3203, member initial 5105, member panel 533, state audit 2217, state initial 2, state panel 325 — the members' 8842 in all, the state's 2545. Ω's net 4973.9 ± 65.3; the tasks vested 2053.2 ± 10.3 a run, bad deliveries 519.3 ± 5.5, the standing false approvals 16.3 ± 1.2 — the leak 0.0079 per vested task (the row's), 0.031 per bad delivery; the system's overhead a vested task 9.35, the customers' 11.53; the state's review cost 2758, unreimbursed 0; the cost of truth 1897.

## greedy (20 seeds; the standing false approvals a run 9.9 ± 0.6, care 0.878, m^A at the end 3.81)

**The dials by close** (mean over the seeds that reached the close): 

| close | t | m_t | π_t | m^A | π^A | m^La | m^Ld | planted approvals adjudicated at a member's audit seat | F̂^A read (n) |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 189 | 1.08 | 0.108 | 1.00 | 0.020 | 1.00 | 1.00 | 0.2 | — (0) |
| 1 | 376 | 1.09 | 0.109 | 1.00 | 0.020 | 1.00 | 1.00 | 2.4 | — (0) |
| 2 | 561 | 1.14 | 0.114 | 1.15 | 0.023 | 1.00 | 1.00 | 4.7 | 0.47 (3) |
| 3 | 737 | 1.15 | 0.115 | 2.10 | 0.042 | 1.02 | 1.00 | 6.5 | 0.59 (16) |
| 4 | 910 | 1.17 | 0.117 | 3.74 | 0.075 | 1.13 | 1.00 | 12.7 | 0.37 (17) |
| 5 | 789 | 1.76 | 0.176 | 1.27 | 0.025 | 1.41 | 1.00 | 5.0 | 0.15 (1) |
| 6 | 765 | 1.69 | 0.169 | 1.54 | 0.031 | 1.64 | 1.00 | 6.0 | — (0) |
| 7 | 879 | 1.52 | 0.152 | 2.37 | 0.047 | 1.64 | 1.00 | 7.0 | 0.15 (1) |

**By quarter**:

| quarter | members alive | duty-ineligible / panel-ineligible of them | probationers / suspended | audit seats on members' work: member inspected / member blind / state | the member's share of them | member blind rate | audit seats on plants: member (blind) / state | panel seats: member inspected / blind / state | standing false approvals vested: member-confirmed / state-confirmed / never audited / other | roots vested | review fees: members / the state | cost of truth (cumulative at the boundary; the quarter's) | m^A / π^A at the boundary |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Q1 (t 0–250) | 18.1 | 0.0 / 17.3 | 18.8 / 0.3 | 25 / 35 / 447 | **0.12** | **0.585** | 2 (1) / 0 | 8 / 0 / 73 | **0.5 ± 0.2** / 0.2 ± 0.1 / 0.0 ± 0.0 / 0.1 | 506 | 1498 / 1395 | 390 (390) | 1.00 / 0.020 |
| Q2 (t 250–500) | 20.4 | 0.0 / 15.1 | 14.4 / 0.6 | 141 / 119 / 209 | **0.55** | **0.456** | 13 (6) / 0 | 32 / 0 / 39 | **1.8 ± 0.3** / 0.2 ± 0.1 / 0.1 ± 0.1 / 0.0 | 489 | 2079 / 671 | 763 (373) | 1.00 / 0.020 |
| Q3 (t 500–750) | 25.1 | 0.0 / 14.1 | 5.4 / 0.6 | 205 / 181 / 102 | **0.79** | **0.469** | 22 (11) / 0 | 49 / 0 / 24 | **2.2 ± 0.3** / 0.0 ± 0.0 / 0.1 ± 0.1 / 0.1 | 522 | 2599 / 352 | 1285 (522) | 1.33 / 0.027 |
| Q4 (t 750–1000) | 23.3 | 0.0 / 11.2 | 0.2 / 0.1 | 299 / 132 / 42 | **0.91** | **0.306** | 38 (12) / 0 | 63 / 1 / 11 | **4.0 ± 0.6** / 0.1 ± 0.0 / 0.7 ± 0.2 / 0.1 | 529 | 2625 / 141 | 1937 (652) | 3.81 / 0.076 |

**The whole run.** Review seats a run by who sat and the seat (plants included): member audit 1212, member initial 2886, member panel 218, plant alias initial 36, state audit 804, state initial 1, state panel 147 — the state's share of the review seats **0.181** (951 of 5268). The review fees a run by who sat and the seat kind: member audit 3148, member initial 5143, member panel 510, state audit 2210, state initial 1, state panel 347 — the members' 8801 in all, the state's 2559. Ω's net 4985.9 ± 115.7; the tasks vested 2049.6 ± 14.8 a run, bad deliveries 524.4 ± 6.9, the standing false approvals 9.9 ± 0.6 — the leak 0.0048 per vested task (the row's), 0.019 per bad delivery; the system's overhead a vested task 9.79, the customers' 11.86; the state's review cost 2805, unreimbursed 0; the cost of truth 1937.

## hand (20 seeds; the standing false approvals a run 7.2 ± 0.7, care 0.000, m^A at the end 1.13)

**The dials by close** (mean over the seeds that reached the close): 

| close | t | m_t | π_t | m^A | π^A | m^La | m^Ld | planted approvals adjudicated at a member's audit seat | F̂^A read (n) |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 195 | 2.00 | 0.200 | 1.00 | 0.020 | 1.00 | 1.00 | 0.1 | — (0) |
| 1 | 312 | 3.98 | 0.398 | 1.00 | 0.020 | 1.00 | 1.00 | 1.1 | — (0) |
| 2 | 378 | 3.98 | 0.398 | 1.00 | 0.020 | 1.00 | 1.00 | 0.9 | — (0) |
| 3 | 437 | 3.88 | 0.388 | 1.00 | 0.020 | 1.00 | 1.00 | 1.6 | — (0) |
| 4 | 490 | 3.61 | 0.361 | 1.00 | 0.020 | 1.10 | 1.00 | 2.0 | — (0) |
| 5 | 548 | 3.41 | 0.341 | 1.00 | 0.020 | 1.10 | 1.00 | 2.4 | 0.04 (5) |
| 6 | 609 | 3.12 | 0.312 | 1.05 | 0.021 | 1.08 | 1.00 | 2.1 | 0.03 (9) |
| 7 | 677 | 2.83 | 0.283 | 1.05 | 0.021 | 1.07 | 1.00 | 2.8 | 0.04 (6) |
| 8 | 752 | 2.60 | 0.260 | 1.04 | 0.021 | 1.09 | 1.00 | 3.1 | 0.09 (1) |
| 9 | 834 | 2.38 | 0.238 | 1.09 | 0.022 | 1.12 | 1.10 | 3.2 | 0.07 (7) |
| 10 | 914 | 2.22 | 0.222 | 1.15 | 0.023 | 1.12 | 1.17 | 3.6 | 0.03 (10) |
| 11 | 965 | 2.12 | 0.212 | 1.16 | 0.023 | 1.13 | 1.20 | 4.0 | — (0) |

**By quarter**:

| quarter | members alive | duty-ineligible / panel-ineligible of them | probationers / suspended | audit seats on members' work: member inspected / member blind / state | the member's share of them | member blind rate | audit seats on plants: member (blind) / state | panel seats: member inspected / blind / state | standing false approvals vested: member-confirmed / state-confirmed / never audited / other | roots vested | review fees: members / the state | cost of truth (cumulative at the boundary; the quarter's) | m^A / π^A at the boundary |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Q1 (t 0–250) | 16.6 | 0.0 / 15.6 | 18.7 / 1.9 | 41 / 13 / 486 | **0.10** | **0.237** | 2 (0) / 0 | 10 / 1 / 91 | **2.4 ± 0.4** / 2.4 ± 0.3 / 0.0 ± 0.0 / 0.6 | 484 | 1341 / 1566 | 432 (432) | 1.00 / 0.020 |
| Q2 (t 250–500) | 20.9 | 0.0 / 4.7 | 1.4 / 0.9 | 274 / 0 / 126 | **0.69** | **0.000** | 49 (0) / 0 | 48 / 0 / 27 | **0.3 ± 0.1** / 0.5 ± 0.2 / 0.0 ± 0.0 / 0.2 | 390 | 2421 / 546 | 1615 (1184) | 1.00 / 0.020 |
| Q3 (t 500–750) | 20.9 | 0.0 / 3.5 | 0.0 / 0.0 | 478 / 0 / 3 | **0.99** | **0.000** | 60 (0) / 0 | 78 / 0 / 1 | **0.4 ± 0.1** / 0.0 ± 0.0 / 0.0 ± 0.0 / 0.0 | 494 | 3160 / 19 | 2992 (1377) | 1.04 / 0.021 |
| Q4 (t 750–1000) | 20.6 | 0.0 / 1.9 | 0.0 / 0.0 | 470 / 2 / 2 | **1.00** | **0.003** | 45 (0) / 0 | 83 / 0 / 1 | **0.2 ± 0.1** / 0.0 ± 0.0 / 0.0 ± 0.0 / 0.0 | 490 | 3071 / 16 | 4034 (1042) | 1.13 / 0.023 |

**The whole run.** Review seats a run by who sat and the seat (plants included): member audit 1451, member initial 3008, member panel 355, plant alias initial 27, state audit 649, state initial 13, state panel 123 — the state's share of the review seats **0.140** (785 of 5599). The review fees a run by who sat and the seat kind: member audit 3851, member initial 5259, member panel 882, state audit 1828, state initial 23, state panel 296 — the members' 9993 in all, the state's 2148. Ω's net 4569.0 ± 70.5; the tasks vested 1906.1 ± 14.6 a run, bad deliveries 466.4 ± 6.5, the standing false approvals 7.2 ± 0.7 — the leak 0.0038 per vested task (the row's), 0.015 per bad delivery; the system's overhead a vested task 15.81, the customers' 14.40; the state's review cost 2398, unreimbursed 0; the cost of truth 4034.

## careful (20 seeds; the standing false approvals a run 2.6 ± 0.4, care 1.000, m^A at the end 1.12)

**The dials by close** (mean over the seeds that reached the close): 

| close | t | m_t | π_t | m^A | π^A | m^La | m^Ld | planted approvals adjudicated at a member's audit seat | F̂^A read (n) |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 189 | 1.01 | 0.101 | 1.00 | 0.020 | 1.00 | 1.00 | 0.2 | — (0) |
| 1 | 385 | 1.03 | 0.103 | 1.00 | 0.020 | 1.00 | 1.00 | 2.9 | — (0) |
| 2 | 577 | 1.04 | 0.104 | 1.05 | 0.021 | 1.00 | 1.00 | 5.4 | 0.06 (5) |
| 3 | 763 | 1.05 | 0.105 | 1.12 | 0.022 | 1.09 | 1.00 | 7.2 | 0.05 (16) |
| 4 | 944 | 1.07 | 0.107 | 1.12 | 0.022 | 1.11 | 1.00 | 7.3 | 0.05 (6) |
| 5 | 995 | 1.32 | 0.132 | 1.00 | 0.020 | 1.00 | 1.00 | 5.0 | — (0) |

**By quarter**:

| quarter | members alive | duty-ineligible / panel-ineligible of them | probationers / suspended | audit seats on members' work: member inspected / member blind / state | the member's share of them | member blind rate | audit seats on plants: member (blind) / state | panel seats: member inspected / blind / state | standing false approvals vested: member-confirmed / state-confirmed / never audited / other | roots vested | review fees: members / the state | cost of truth (cumulative at the boundary; the quarter's) | m^A / π^A at the boundary |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Q1 (t 0–250) | 17.4 | 0.0 / 16.4 | 19.1 / 0.2 | 65 / 0 / 437 | **0.13** | **0.000** | 2 (0) / 0 | 11 / 0 / 72 | **0.0 ± 0.0** / 0.2 ± 0.1 / 0.0 ± 0.0 / 0.1 | 498 | 1500 / 1381 | 415 (415) | 1.00 / 0.020 |
| Q2 (t 250–500) | 19.2 | 0.0 / 12.3 | 14.7 / 0.8 | 274 / 0 / 173 | **0.61** | **0.000** | 12 (0) / 0 | 41 / 0 / 35 | **0.2 ± 0.1** / 0.1 ± 0.1 / 0.1 ± 0.1 / 0.1 | 463 | 2075 / 584 | 778 (362) | 1.00 / 0.020 |
| Q3 (t 500–750) | 25.4 | 0.0 / 8.9 | 5.2 / 0.5 | 428 / 0 / 48 | **0.90** | **0.000** | 21 (0) / 0 | 65 / 0 / 14 | **0.4 ± 0.2** / 0.0 ± 0.0 / 0.1 ± 0.0 / 0.0 | 505 | 2749 / 193 | 1306 (529) | 1.05 / 0.021 |
| Q4 (t 750–1000) | 23.3 | 0.0 / 4.8 | 0.0 / 0.1 | 449 / 2 / 6 | **0.99** | **0.004** | 25 (0) / 0 | 81 / 0 / 3 | **0.5 ± 0.2** / 0.0 ± 0.0 / 0.9 ± 0.3 / 0.0 | 524 | 2646 / 25 | 1924 (617) | 1.12 / 0.022 |

**The whole run.** Review seats a run by who sat and the seat (plants included): member audit 1282, member initial 2831, member panel 273, plant alias initial 25, state audit 677, state initial 1, state panel 124 — the state's share of the review seats **0.155** (803 of 5189). The review fees a run by who sat and the seat kind: member audit 3304, member initial 5019, member panel 646, state audit 1884, state initial 3, state panel 296 — the members' 8969 in all, the state's 2183. Ω's net 4617.0 ± 131.4; the tasks vested 2007.5 ± 21.9 a run, bad deliveries 511.2 ± 7.6, the standing false approvals 2.6 ± 0.4 — the leak 0.0013 per vested task (the row's), 0.005 per bad delivery; the system's overhead a vested task 10.27, the customers' 12.44; the state's review cost 2396, unreimbursed 0; the cost of truth 1924.


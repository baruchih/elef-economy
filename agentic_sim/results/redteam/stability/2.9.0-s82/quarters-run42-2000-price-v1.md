# The frozen policy in a 2,000-tick run, read by quarter — `run42-2000-price` (D2, the economy reviewer's addendum 4; `quarters.py`)

Cell: `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule`; seeds 21-40. Means over the seeds (± SE where shown). A quarter is 500 ticks; the seats by the quarter of the seat's assignment, the standing false approvals by the quarter of their vesting, the fees by the quarter of their payment, the snapshots at the first decision at or after the boundary (the members alive and the tiers at that moment; the cost of truth cumulative there). The audit and panel seats are on members' real deliveries (the plants' beside); a member's seat inspected (care spent) or blind (none spent, a verdict of either sign).

## greedy (20 seeds; the standing false approvals a run 22.5 ± 1.5, care 0.908, m^A at the end 8.33)

**The dials by close** (mean over the seeds that reached the close): 

| close | t | m_t | π_t | m^A | π^A | m^La | m^Ld | planted approvals adjudicated at a member's audit seat | F̂^A read (n) |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 189 | 1.06 | 0.106 | 1.00 | 0.020 | 1.00 | 1.00 | 0.2 | — (0) |
| 1 | 379 | 1.05 | 0.105 | 1.00 | 0.020 | 1.00 | 1.00 | 2.7 | — (0) |
| 2 | 567 | 1.03 | 0.103 | 1.15 | 0.023 | 1.00 | 1.00 | 4.8 | 0.29 (3) |
| 3 | 751 | 1.02 | 0.102 | 2.29 | 0.046 | 1.05 | 1.00 | 7.1 | 0.60 (20) |
| 4 | 937 | 1.11 | 0.111 | 4.51 | 0.090 | 1.19 | 1.00 | 15.1 | 0.36 (20) |
| 5 | 1118 | 1.41 | 0.141 | 7.14 | 0.143 | 1.28 | 1.00 | 28.7 | 0.18 (20) |
| 6 | 1270 | 1.82 | 0.182 | 11.00 | 0.220 | 1.49 | 1.05 | 38.7 | 0.18 (20) |
| 7 | 1382 | 2.15 | 0.215 | 11.16 | 0.223 | 1.58 | 1.05 | 44.2 | 0.08 (20) |
| 8 | 1482 | 2.68 | 0.268 | 10.41 | 0.208 | 1.50 | 1.05 | 43.0 | 0.07 (19) |
| 9 | 1571 | 2.93 | 0.293 | 9.99 | 0.200 | 1.50 | 1.05 | 33.0 | 0.05 (20) |
| 10 | 1654 | 3.01 | 0.301 | 10.36 | 0.207 | 1.45 | 1.05 | 28.2 | 0.06 (20) |
| 11 | 1718 | 2.94 | 0.294 | 9.51 | 0.190 | 1.41 | 1.05 | 27.8 | 0.04 (19) |
| 12 | 1796 | 2.94 | 0.294 | 9.06 | 0.181 | 1.48 | 1.04 | 26.2 | 0.06 (17) |
| 13 | 1854 | 2.73 | 0.273 | 8.45 | 0.169 | 1.34 | 1.10 | 25.1 | 0.04 (15) |
| 14 | 1910 | 2.60 | 0.260 | 7.27 | 0.145 | 1.17 | 1.13 | 23.1 | 0.02 (11) |
| 15 | 1939 | 2.81 | 0.281 | 6.35 | 0.127 | 1.04 | 1.00 | 18.6 | 0.04 (5) |
| 16 | 1972 | 2.38 | 0.238 | 8.24 | 0.165 | 1.21 | 1.00 | 27.5 | 0.07 (2) |

**By quarter**:

| quarter | members alive | duty-ineligible / panel-ineligible of them | probationers / suspended | audit seats on members' work: member inspected / member blind / state | the member's share of them | member blind rate | audit seats on plants: member (blind) / state | panel seats: member inspected / blind / state | standing false approvals vested: member-confirmed / state-confirmed / never audited / other | roots vested | review fees: members / the state | cost of truth (cumulative at the boundary; the quarter's) | m^A / π^A at the boundary |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Q1 (t 0–500) | 20.0 | 0.0 / 15.2 | 14.8 / 0.8 | 158 / 171 / 647 | **0.34** | **0.520** | 15 (7) / 0 | 40 / 1 / 110 | **2.1 ± 0.4** / 0.6 ± 0.2 / 0.2 ± 0.1 / 0.0 | 995 | 3577 / 2043 | 767 (767) | 1.00 / 0.020 |
| Q2 (t 500–1000) | 22.9 | 0.0 / 10.3 | 0.1 / 0.1 | 491 / 355 / 111 | **0.88** | **0.419** | 60 (21) / 0 | 113 / 2 / 25 | **7.0 ± 0.8** / 0.1 ± 0.1 / 1.2 ± 0.2 / 0.4 | 1058 | 5290 / 379 | 1924 (1157) | 4.71 / 0.094 |
| Q3 (t 1000–1500) | 20.7 | 0.0 / 10.2 | 0.0 / 0.0 | 848 / 75 / 50 | **0.95** | **0.081** | 205 (12) / 0 | 155 / 6 / 12 | **6.5 ± 0.8** / 0.2 ± 0.1 / 1.4 ± 0.4 / 1.1 | 1035 | 6138 / 149 | 4948 (3024) | 10.93 / 0.219 |
| Q4 (t 1500–2000) | 19.9 | 0.0 / 3.6 | 0.0 / 0.0 | 833 / 3 / 29 | **0.97** | **0.003** | 238 (1) / 0 | 141 / 0 / 9 | **0.9 ± 0.2** / 0.1 ± 0.0 / 0.3 ± 0.2 / 0.2 | 902 | 6712 / 139 | 8520 (3573) | 8.33 / 0.167 |

**The quarter's price** (the system's overhead per task vested in the quarter: the care spent on real and planted cases, the state's seats' cost, the cost of truth and the plants' awarded price, by the quarter of each; the standing false approvals vested in the quarter over the bad deliveries vested in it, per thousand; the bad deliveries here are a member's real roots vested unfulfilled, the false approvals among them those vested approved — every unfulfilled root that vests is a false approval, so the two counts coincide and the quarter's leak per bad delivery is read against the whole run's `leak_bad`, which counts the bad deliveries at every outcome):

| quarter | roots vested | care on real / on plants | the state's seats' cost | the cost of truth (the quarter's) | the plants' price | system overhead a vested task | standing false approvals vested | leak per vested task |
|---|---|---|---|---|---|---|---|---|
| Q1 | 995 | 3682 / 371 | 2231 | 767 | 3097 | **10.20** | 3.0 ± 0.5 | 3.0 per thousand |
| Q2 | 1058 | 4736 / 555 | 415 | 1157 | 2470 | **8.83** | 8.8 ± 1.1 | 8.3 per thousand |
| Q3 | 1035 | 5318 / 1384 | 175 | 3024 | 8422 | **17.71** | 9.2 ± 1.0 | 8.9 per thousand |
| Q4 | 902 | 5192 / 1844 | 205 | 3573 | 11707 | **24.97** | 1.6 ± 0.4 | 1.7 per thousand |
| the run (the quarters summed) | 3989 | 18928 / 4154 | 3025 | 8520 | 25696 | **15.12** | 22.5 | 5.6 per thousand |

**The whole run.** Review seats a run by who sat and the seat (plants included): member audit 3455, member initial 5778, member panel 938, plant alias initial 351, state audit 840, state initial 19, state panel 156 — the state's share of the review seats **0.091** (1015 of 11185). The review fees a run by who sat and the seat kind: member audit 9117, member initial 10216, member panel 2385, state audit 2307, state initial 33, state panel 370 — the members' 21717 in all, the state's 2710. Ω's net 8030.6 ± 115.3; the tasks vested 3996.0 ± 17.2 a run, bad deliveries 1011.2 ± 11.3, the standing false approvals 22.5 ± 1.5 — the leak 0.0056 per vested task (the row's), 0.022 per bad delivery; the system's overhead a vested task 15.11, the customers' 12.61; the state's review cost 3022, unreimbursed 0; the cost of truth 8520.

## hand (20 seeds; the standing false approvals a run 11.8 ± 0.7, care 0.000, m^A at the end 1.19)

**The dials by close** (mean over the seeds that reached the close): 

| close | t | m_t | π_t | m^A | π^A | m^La | m^Ld | planted approvals adjudicated at a member's audit seat | F̂^A read (n) |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 195 | 2.00 | 0.200 | 1.00 | 0.020 | 1.00 | 1.00 | 0.1 | — (0) |
| 1 | 313 | 4.00 | 0.400 | 1.00 | 0.020 | 1.00 | 1.00 | 0.8 | — (0) |
| 2 | 380 | 3.98 | 0.398 | 1.00 | 0.020 | 1.00 | 1.00 | 0.9 | — (0) |
| 3 | 438 | 3.90 | 0.390 | 1.00 | 0.020 | 1.00 | 1.00 | 1.6 | — (0) |
| 4 | 490 | 3.76 | 0.376 | 1.00 | 0.020 | 1.00 | 1.00 | 1.9 | 0.00 (1) |
| 5 | 544 | 3.45 | 0.345 | 1.00 | 0.020 | 1.03 | 1.00 | 2.2 | — (0) |
| 6 | 604 | 3.19 | 0.319 | 1.13 | 0.023 | 1.06 | 1.00 | 2.2 | 0.08 (10) |
| 7 | 670 | 2.94 | 0.294 | 1.13 | 0.023 | 1.11 | 1.00 | 2.8 | 0.07 (8) |
| 8 | 743 | 2.79 | 0.279 | 1.10 | 0.022 | 1.20 | 1.00 | 3.1 | 0.02 (4) |
| 9 | 822 | 2.63 | 0.263 | 1.10 | 0.022 | 1.17 | 1.00 | 3.1 | 0.00 (3) |
| 10 | 906 | 2.41 | 0.241 | 1.09 | 0.022 | 1.25 | 1.00 | 3.6 | 0.00 (7) |
| 11 | 998 | 2.21 | 0.221 | 1.11 | 0.022 | 1.23 | 1.00 | 3.6 | 0.05 (9) |
| 12 | 1099 | 1.99 | 0.199 | 1.09 | 0.022 | 1.36 | 1.00 | 4.0 | 0.05 (6) |
| 13 | 1212 | 1.85 | 0.185 | 1.09 | 0.022 | 1.39 | 1.05 | 4.3 | 0.05 (6) |
| 14 | 1335 | 1.69 | 0.169 | 1.13 | 0.023 | 1.35 | 1.05 | 4.5 | 0.04 (9) |
| 15 | 1470 | 1.63 | 0.163 | 1.13 | 0.023 | 1.39 | 1.05 | 5.0 | 0.04 (8) |
| 16 | 1612 | 1.61 | 0.161 | 1.17 | 0.023 | 1.39 | 1.05 | 5.2 | 0.05 (9) |
| 17 | 1706 | 1.50 | 0.150 | 1.20 | 0.024 | 1.42 | 1.00 | 5.4 | 0.07 (7) |
| 18 | 1783 | 1.52 | 0.152 | 1.28 | 0.026 | 1.50 | 1.00 | 5.8 | 0.07 (6) |
| 19 | 1799 | 1.73 | 0.173 | 1.38 | 0.028 | 1.63 | 1.00 | 6.0 | 0.04 (4) |
| 20 | 1818 | 1.54 | 0.154 | 1.41 | 0.028 | 1.40 | 1.17 | 6.2 | 0.00 (2) |
| 21 | 1844 | 2.05 | 0.205 | 1.73 | 0.035 | 1.44 | 1.00 | 7.0 | 0.11 (1) |
| 22 | 1952 | 1.84 | 0.184 | 1.67 | 0.033 | 1.44 | 1.50 | 6.0 | 0.00 (1) |

**By quarter**:

| quarter | members alive | duty-ineligible / panel-ineligible of them | probationers / suspended | audit seats on members' work: member inspected / member blind / state | the member's share of them | member blind rate | audit seats on plants: member (blind) / state | panel seats: member inspected / blind / state | standing false approvals vested: member-confirmed / state-confirmed / never audited / other | roots vested | review fees: members / the state | cost of truth (cumulative at the boundary; the quarter's) | m^A / π^A at the boundary |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Q1 (t 0–500) | 21.2 | 0.0 / 4.8 | 0.9 / 1.6 | 298 / 13 / 633 | **0.33** | **0.041** | 50 (0) / 0 | 50 / 1 / 123 | **2.5 ± 0.4** / 3.5 ± 0.4 / 0.0 ± 0.0 / 1.2 | 875 | 3701 / 2186 | 1597 (1597) | 1.00 / 0.020 |
| Q2 (t 500–1000) | 20.1 | 0.0 / 2.3 | 0.0 / 0.0 | 942 / 0 / 5 | **0.99** | **0.000** | 112 (0) / 0 | 154 / 0 / 3 | **0.8 ± 0.2** / 0.0 ± 0.0 / 0.0 ± 0.0 / 0.4 | 971 | 6242 / 41 | 4168 (2571) | 1.11 / 0.022 |
| Q3 (t 1000–1500) | 19.6 | 0.0 / 0.8 | 0.0 / 0.0 | 880 / 0 / 2 | **1.00** | **0.000** | 71 (0) / 0 | 149 / 0 / 1 | **0.6 ± 0.2** / 0.0 ± 0.0 / 0.6 ± 0.2 / 0.2 | 950 | 5923 / 31 | 5911 (1743) | 1.13 / 0.023 |
| Q4 (t 1500–2000) | 19.2 | 0.0 / 0.7 | 0.0 / 0.0 | 806 / 2 / 2 | **1.00** | **0.002** | 57 (0) / 0 | 139 / 0 / 2 | **0.6 ± 0.2** / 0.1 ± 0.0 / 1.3 ± 0.3 / 0.0 | 934 | 5577 / 35 | 7319 (1408) | 1.19 / 0.024 |

**The quarter's price** (the system's overhead per task vested in the quarter: the care spent on real and planted cases, the state's seats' cost, the cost of truth and the plants' awarded price, by the quarter of each; the standing false approvals vested in the quarter over the bad deliveries vested in it, per thousand; the bad deliveries here are a member's real roots vested unfulfilled, the false approvals among them those vested approved — every unfulfilled root that vests is a false approval, so the two counts coincide and the quarter's leak per bad delivery is read against the whole run's `leak_bad`, which counts the bad deliveries at every outcome):

| quarter | roots vested | care on real / on plants | the state's seats' cost | the cost of truth (the quarter's) | the plants' price | system overhead a vested task | standing false approvals vested | leak per vested task |
|---|---|---|---|---|---|---|---|---|
| Q1 | 875 | 2940 / 716 | 2433 | 1597 | 6052 | **15.70** | 7.2 ± 0.6 | 8.3 per thousand |
| Q2 | 971 | 5792 / 1388 | 54 | 2571 | 7090 | **17.39** | 1.1 ± 0.3 | 1.2 per thousand |
| Q3 | 950 | 5549 / 922 | 47 | 1743 | 4914 | **13.87** | 1.4 ± 0.3 | 1.5 per thousand |
| Q4 | 934 | 5301 / 750 | 56 | 1408 | 4181 | **12.52** | 1.9 ± 0.3 | 2.0 per thousand |
| the run (the quarters summed) | 3730 | 19581 / 3775 | 2589 | 7319 | 22236 | **14.88** | 11.7 | 3.1 per thousand |

**The whole run.** Review seats a run by who sat and the seat (plants included): member audit 3249, member initial 5753, member panel 786, plant alias initial 66, state audit 673, state initial 38, state panel 132 — the state's share of the review seats **0.079** (843 of 10631). The review fees a run by who sat and the seat kind: member audit 9002, member initial 10434, member panel 2008, state audit 1902, state initial 71, state panel 320 — the members' 21444 in all, the state's 2293. Ω's net 7431.6 ± 59.1; the tasks vested 3776.3 ± 31.1 a run, bad deliveries 953.9 ± 10.9, the standing false approvals 11.8 ± 0.7 — the leak 0.0031 per vested task (the row's), 0.012 per bad delivery; the system's overhead a vested task 14.72, the customers' 13.98; the state's review cost 2589, unreimbursed 0; the cost of truth 7319.

## careful (20 seeds; the standing false approvals a run 8.6 ± 0.8, care 1.000, m^A at the end 1.26)

**The dials by close** (mean over the seeds that reached the close): 

| close | t | m_t | π_t | m^A | π^A | m^La | m^Ld | planted approvals adjudicated at a member's audit seat | F̂^A read (n) |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 189 | 1.03 | 0.103 | 1.00 | 0.020 | 1.00 | 1.00 | 0.1 | — (0) |
| 1 | 380 | 1.04 | 0.104 | 1.00 | 0.020 | 1.00 | 1.00 | 3.0 | — (0) |
| 2 | 567 | 1.02 | 0.102 | 1.04 | 0.021 | 1.00 | 1.00 | 5.5 | 0.04 (8) |
| 3 | 753 | 1.07 | 0.107 | 1.12 | 0.022 | 1.05 | 1.00 | 7.2 | 0.05 (12) |
| 4 | 933 | 1.06 | 0.106 | 1.16 | 0.023 | 1.11 | 1.03 | 7.2 | 0.06 (10) |
| 5 | 1113 | 1.05 | 0.105 | 1.21 | 0.024 | 1.09 | 1.09 | 7.0 | 0.06 (11) |
| 6 | 1295 | 1.02 | 0.102 | 1.23 | 0.025 | 1.09 | 1.09 | 7.3 | 0.04 (12) |
| 7 | 1482 | 1.01 | 0.101 | 1.19 | 0.024 | 1.09 | 1.09 | 7.5 | 0.03 (12) |
| 8 | 1673 | 1.02 | 0.102 | 1.26 | 0.025 | 1.13 | 1.10 | 7.5 | 0.07 (11) |
| 9 | 1861 | 1.03 | 0.103 | 1.27 | 0.025 | 1.11 | 1.10 | 7.6 | 0.03 (14) |
| 10 | 1922 | 1.04 | 0.104 | 1.17 | 0.023 | 1.14 | 1.38 | 7.5 | 0.00 (2) |

**By quarter**:

| quarter | members alive | duty-ineligible / panel-ineligible of them | probationers / suspended | audit seats on members' work: member inspected / member blind / state | the member's share of them | member blind rate | audit seats on plants: member (blind) / state | panel seats: member inspected / blind / state | standing false approvals vested: member-confirmed / state-confirmed / never audited / other | roots vested | review fees: members / the state | cost of truth (cumulative at the boundary; the quarter's) | m^A / π^A at the boundary |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Q1 (t 0–500) | 20.8 | 0.0 / 13.3 | 14.6 / 0.6 | 353 / 0 / 627 | **0.36** | **0.000** | 15 (0) / 0 | 52 / 0 / 106 | **0.2 ± 0.1** / 0.3 ± 0.1 / 0.1 ± 0.0 / 0.1 | 989 | 3667 / 1996 | 812 (812) | 1.00 / 0.020 |
| Q2 (t 500–1000) | 23.1 | 0.0 / 4.2 | 0.1 / 0.1 | 889 / 0 / 41 | **0.96** | **0.000** | 47 (0) / 0 | 156 / 0 / 13 | **0.6 ± 0.2** / 0.1 ± 0.0 / 1.1 ± 0.2 / 0.3 | 1050 | 5401 / 154 | 2011 (1199) | 1.16 / 0.023 |
| Q3 (t 1000–1500) | 20.9 | 0.0 / 3.5 | 0.0 / 0.0 | 831 / 0 / 1 | **1.00** | **0.000** | 46 (0) / 0 | 152 / 0 / 1 | **0.5 ± 0.2** / 0.1 ± 0.0 / 2.1 ± 0.3 / 0.1 | 1053 | 4887 / 5 | 3201 (1190) | 1.21 / 0.024 |
| Q4 (t 1500–2000) | 20.4 | 0.0 / 2.6 | 0.0 / 0.0 | 806 / 1 / 1 | **1.00** | **0.002** | 45 (0) / 0 | 150 / 0 / 1 | **0.7 ± 0.2** / 0.0 ± 0.0 / 2.3 ± 0.3 / 0.1 | 1017 | 5405 / 12 | 4380 (1179) | 1.26 / 0.025 |

**The quarter's price** (the system's overhead per task vested in the quarter: the care spent on real and planted cases, the state's seats' cost, the cost of truth and the plants' awarded price, by the quarter of each; the standing false approvals vested in the quarter over the bad deliveries vested in it, per thousand; the bad deliveries here are a member's real roots vested unfulfilled, the false approvals among them those vested approved — every unfulfilled root that vests is a false approval, so the two counts coincide and the quarter's leak per bad delivery is read against the whole run's `leak_bad`, which counts the bad deliveries at every outcome):

| quarter | roots vested | care on real / on plants | the state's seats' cost | the cost of truth (the quarter's) | the plants' price | system overhead a vested task | standing false approvals vested | leak per vested task |
|---|---|---|---|---|---|---|---|---|
| Q1 | 989 | 4228 / 398 | 2158 | 812 | 2991 | **10.70** | 0.7 ± 0.2 | 0.7 per thousand |
| Q2 | 1050 | 5938 / 618 | 167 | 1199 | 2246 | **9.68** | 2.0 ± 0.3 | 1.9 per thousand |
| Q3 | 1053 | 5778 / 622 | 7 | 1190 | 2925 | **9.99** | 2.9 ± 0.4 | 2.7 per thousand |
| Q4 | 1017 | 5593 / 602 | 18 | 1179 | 3756 | **10.96** | 3.0 ± 0.3 | 3.0 per thousand |
| the run (the quarters summed) | 4110 | 21536 / 2240 | 2350 | 4380 | 11918 | **10.32** | 8.6 | 2.1 per thousand |

**The whole run.** Review seats a run by who sat and the seat (plants included): member audit 3035, member initial 5758, member panel 720, plant alias initial 66, state audit 674, state initial 4, state panel 122 — the state's share of the review seats **0.078** (800 of 10314). The review fees a run by who sat and the seat kind: member audit 7611, member initial 10054, member panel 1695, state audit 1871, state initial 8, state panel 288 — the members' 19360 in all, the state's 2167. Ω's net 7368.0 ± 118.2; the tasks vested 4115.6 ± 23.4 a run, bad deliveries 1054.3 ± 8.6, the standing false approvals 8.6 ± 0.8 — the leak 0.0021 per vested task (the row's), 0.008 per bad delivery; the system's overhead a vested task 10.31, the customers' 11.74; the state's review cost 2349, unreimbursed 0; the cost of truth 4380.


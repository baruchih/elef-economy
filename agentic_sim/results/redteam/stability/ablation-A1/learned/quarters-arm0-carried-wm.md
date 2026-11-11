# The frozen policy in a 1,000-tick run, read by quarter — `arm0-carried-wm` (D2, the economy reviewer's addendum 4; `quarters.py`)

Cell: `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --dial-start 2.598085,14.111864,6.329700,1.732815`; seeds 21-40. Means over the seeds (± SE where shown). A quarter is 250 ticks; the seats by the quarter of the seat's assignment, the standing false approvals by the quarter of their vesting, the fees by the quarter of their payment, the snapshots at the first decision at or after the boundary (the members alive and the tiers at that moment; the cost of truth cumulative there). The audit and panel seats are on members' real deliveries (the plants' beside); a member's seat inspected (care spent) or blind (none spent, a verdict of either sign).

## greedy (20 seeds; the standing false approvals a run 3.3 ± 0.4, care 0.987, m^A at the end 8.55)

**The dials by close** (mean over the seeds that reached the close): 

| close | t | m_t | π_t | m^A | π^A | m^La | m^Ld | planted approvals adjudicated at a member's audit seat | F̂^A read (n) |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 72 | 2.46 | 0.246 | 14.11 | 0.282 | 6.33 | 1.73 | 0.9 | — (0) |
| 1 | 152 | 2.23 | 0.223 | 13.28 | 0.266 | 6.33 | 1.73 | 19.0 | 0.05 (18) |
| 2 | 245 | 2.27 | 0.227 | 12.45 | 0.249 | 6.09 | 1.73 | 38.6 | 0.05 (20) |
| 3 | 336 | 2.12 | 0.212 | 11.57 | 0.231 | 5.88 | 1.73 | 42.4 | 0.05 (20) |
| 4 | 432 | 1.92 | 0.192 | 11.05 | 0.221 | 5.51 | 1.72 | 44.1 | 0.05 (20) |
| 5 | 537 | 1.78 | 0.178 | 10.57 | 0.211 | 5.11 | 1.78 | 44.9 | 0.04 (20) |
| 6 | 653 | 1.75 | 0.175 | 10.16 | 0.203 | 4.75 | 1.75 | 45.5 | 0.06 (20) |
| 7 | 777 | 1.58 | 0.158 | 9.38 | 0.188 | 4.50 | 1.74 | 45.8 | 0.05 (20) |
| 8 | 850 | 1.70 | 0.170 | 9.06 | 0.181 | 4.25 | 1.72 | 42.5 | 0.04 (13) |
| 9 | 785 | 2.05 | 0.205 | 9.33 | 0.187 | 4.29 | 1.53 | 35.2 | 0.07 (5) |
| 10 | 784 | 2.21 | 0.221 | 8.52 | 0.170 | 4.13 | 1.56 | 30.0 | 0.03 (3) |
| 11 | 878 | 1.99 | 0.199 | 7.67 | 0.153 | 3.73 | 1.56 | 29.3 | 0.03 (3) |
| 12 | 967 | 1.82 | 0.182 | 6.15 | 0.123 | 2.95 | 1.57 | 28.0 | 0.00 (2) |

**By quarter**:

| quarter | members alive | duty-ineligible / panel-ineligible of them | probationers / suspended | audit seats on members' work: member inspected / member blind / state | the member's share of them | member blind rate | audit seats on plants: member (blind) / state | panel seats: member inspected / blind / state | standing false approvals vested: member-confirmed / state-confirmed / never audited / other | roots vested | review fees: members / the state | cost of truth (cumulative at the boundary; the quarter's) | m^A / π^A at the boundary |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Q1 (t 0–250) | 22.4 | 0.0 / 13.1 | 10.2 / 0.9 | 238 / 5 / 255 | **0.49** | **0.020** | 77 (2) / 0 | 30 / 9 / 41 | **0.3 ± 0.1** / 0.2 ± 0.1 / 0.0 ± 0.0 / 0.0 | 486 | 2493 / 763 | 1723 (1723) | 12.99 / 0.260 |
| Q2 (t 250–500) | 23.3 | 0.0 / 5.7 | 0.0 / 0.1 | 487 / 2 / 10 | **0.98** | **0.003** | 150 (1) / 0 | 76 / 4 / 4 | **0.4 ± 0.1** / 0.0 ± 0.0 / 0.1 ± 0.1 / 0.1 | 516 | 3723 / 50 | 3982 (2259) | 10.66 / 0.213 |
| Q3 (t 500–750) | 22.3 | 0.0 / 4.3 | 0.0 / 0.0 | 465 / 1 / 1 | **1.00** | **0.003** | 124 (0) / 0 | 80 / 3 / 1 | **0.5 ± 0.1** / 0.0 ± 0.0 / 0.6 ± 0.2 / 0.0 | 514 | 3444 / 9 | 5924 (1941) | 9.85 / 0.197 |
| Q4 (t 750–1000) | 21.8 | 0.0 / 4.0 | 0.0 / 0.0 | 443 / 3 / 1 | **1.00** | **0.007** | 103 (1) / 0 | 77 / 2 / 1 | **0.5 ± 0.2** / 0.0 ± 0.0 / 0.6 ± 0.2 / 0.1 | 511 | 3377 / 12 | 7553 (1630) | 8.55 / 0.171 |

**The quarter's price** (the system's overhead per task vested in the quarter: the care spent on real and planted cases, the state's seats' cost, the cost of truth and the plants' awarded price, by the quarter of each; the standing false approvals vested in the quarter over the bad deliveries vested in it, per thousand; the bad deliveries here are a member's real roots vested unfulfilled, the false approvals among them those vested approved — every unfulfilled root that vests is a false approval, so the two counts coincide; the leak per thousand bad deliveries is read on the bad deliveries settled in the quarter at every outcome — the driver's `bad_deliveries` by the quarter of the settlement — and the false approvals among them):

| quarter | roots vested | care on real / on plants | the state's seats' cost | the cost of truth (the quarter's) | the plants' price | system overhead a vested task | standing false approvals vested | per thousand tasks vested | bad deliveries settled / false approvals among them | leak per thousand bad deliveries |
|---|---|---|---|---|---|---|---|---|---|---|
| Q1 | 486 | 2286 / 698 | 819 | 1723 | 4761 | **21.18** | 0.6 ± 0.2 | 1.2 | 131 / 0.6 | **4.6** |
| Q2 | 516 | 3059 / 1122 | 53 | 2259 | 3878 | **20.10** | 0.6 ± 0.1 | 1.2 | 138 / 0.6 | **4.3** |
| Q3 | 514 | 2987 / 954 | 13 | 1941 | 4033 | **19.33** | 1.0 ± 0.2 | 1.9 | 129 / 1.0 | **7.7** |
| Q4 | 511 | 2906 / 830 | 16 | 1630 | 3553 | **17.48** | 1.1 ± 0.2 | 2.2 | 128 / 1.1 | **8.6** |
| the run (the quarters summed) | 2027 | 11238 / 3605 | 902 | 7553 | 16226 | **19.50** | 3.3 | 1.6 | 527 / 3.3 | **6.3** |

**The whole run.** Review seats a run by who sat and the seat (plants included): member audit 2098, member initial 3094, member panel 828, plant alias initial 358, state audit 269, state initial 9, state panel 47 — the state's share of the review seats **0.051** (325 of 6344). The review fees a run by who sat and the seat kind: member audit 5483, member initial 5388, member panel 2166, state audit 713, state initial 16, state panel 106 — the members' 13037 in all, the state's 835. Ω's net 3406.2 ± 49.8; the tasks vested 2028.1 ± 12.4 a run, bad deliveries 527.1 ± 7.1, the standing false approvals 3.3 ± 0.4 — the leak 0.0016 per vested task (the row's), 0.006 per bad delivery; the system's overhead a vested task 19.53, the customers' 13.18; the state's review cost 901, unreimbursed 0; the cost of truth 7553.

## careful (20 seeds; the standing false approvals a run 2.4 ± 0.4, care 1.000, m^A at the end 8.40)

**The dials by close** (mean over the seeds that reached the close): 

| close | t | m_t | π_t | m^A | π^A | m^La | m^Ld | planted approvals adjudicated at a member's audit seat | F̂^A read (n) |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 73 | 2.42 | 0.242 | 14.11 | 0.282 | 6.33 | 1.73 | 1.9 | — (0) |
| 1 | 155 | 2.32 | 0.232 | 13.24 | 0.265 | 6.43 | 1.73 | 25.2 | 0.04 (17) |
| 2 | 246 | 2.16 | 0.216 | 12.00 | 0.240 | 5.93 | 1.73 | 38.6 | 0.04 (20) |
| 3 | 339 | 2.01 | 0.201 | 11.55 | 0.231 | 5.64 | 1.73 | 43.0 | 0.06 (20) |
| 4 | 439 | 1.88 | 0.188 | 11.35 | 0.227 | 5.38 | 1.72 | 45.6 | 0.06 (20) |
| 5 | 547 | 1.70 | 0.170 | 10.48 | 0.210 | 5.06 | 1.71 | 46.2 | 0.06 (20) |
| 6 | 666 | 1.59 | 0.159 | 9.83 | 0.197 | 4.75 | 1.68 | 46.9 | 0.05 (20) |
| 7 | 797 | 1.47 | 0.147 | 9.08 | 0.182 | 4.61 | 1.62 | 47.2 | 0.06 (20) |
| 8 | 810 | 1.81 | 0.181 | 7.95 | 0.159 | 5.06 | 1.62 | 34.4 | 0.07 (9) |
| 9 | 827 | 2.04 | 0.204 | 7.95 | 0.159 | 5.73 | 1.63 | 32.4 | 0.05 (5) |
| 10 | 847 | 2.15 | 0.215 | 7.11 | 0.142 | 5.23 | 1.62 | 29.3 | 0.06 (3) |
| 11 | 899 | 2.11 | 0.211 | 5.64 | 0.113 | 5.57 | 1.65 | 22.5 | 0.03 (2) |
| 12 | 958 | 1.57 | 0.157 | 6.17 | 0.123 | 5.25 | 1.73 | 31.0 | 0.03 (1) |

**By quarter**:

| quarter | members alive | duty-ineligible / panel-ineligible of them | probationers / suspended | audit seats on members' work: member inspected / member blind / state | the member's share of them | member blind rate | audit seats on plants: member (blind) / state | panel seats: member inspected / blind / state | standing false approvals vested: member-confirmed / state-confirmed / never audited / other | roots vested | review fees: members / the state | cost of truth (cumulative at the boundary; the quarter's) | m^A / π^A at the boundary |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Q1 (t 0–250) | 22.1 | 0.0 / 12.1 | 9.3 / 0.8 | 268 / 0 / 225 | **0.54** | **0.000** | 87 (0) / 0 | 40 / 0 / 41 | **0.1 ± 0.0** / 0.1 ± 0.0 / 0.0 ± 0.0 / 0.1 | 486 | 2572 / 696 | 1864 (1864) | 12.46 / 0.249 |
| Q2 (t 250–500) | 23.4 | 0.0 / 4.7 | 0.1 / 0.1 | 489 / 0 / 7 | **0.98** | **0.000** | 146 (0) / 0 | 79 / 0 / 3 | **0.2 ± 0.1** / 0.0 ± 0.0 / 0.1 ± 0.1 / 0.1 | 516 | 3700 / 37 | 4079 (2215) | 11.06 / 0.221 |
| Q3 (t 500–750) | 22.5 | 0.0 / 4.0 | 0.0 / 0.0 | 472 / 0 / 1 | **1.00** | **0.000** | 122 (0) / 0 | 79 / 0 / 1 | **0.3 ± 0.1** / 0.0 ± 0.0 / 0.3 ± 0.1 / 0.1 | 519 | 3372 / 9 | 5978 (1899) | 9.35 / 0.187 |
| Q4 (t 750–1000) | 21.8 | 0.0 / 3.5 | 0.0 / 0.0 | 445 / 2 / 1 | **1.00** | **0.004** | 100 (0) / 0 | 74 / 0 / 1 | **0.3 ± 0.1** / 0.0 ± 0.0 / 0.5 ± 0.1 / 0.1 | 512 | 3251 / 9 | 7587 (1609) | 8.40 / 0.168 |

**The quarter's price** (the system's overhead per task vested in the quarter: the care spent on real and planted cases, the state's seats' cost, the cost of truth and the plants' awarded price, by the quarter of each; the standing false approvals vested in the quarter over the bad deliveries vested in it, per thousand; the bad deliveries here are a member's real roots vested unfulfilled, the false approvals among them those vested approved — every unfulfilled root that vests is a false approval, so the two counts coincide; the leak per thousand bad deliveries is read on the bad deliveries settled in the quarter at every outcome — the driver's `bad_deliveries` by the quarter of the settlement — and the false approvals among them):

| quarter | roots vested | care on real / on plants | the state's seats' cost | the cost of truth (the quarter's) | the plants' price | system overhead a vested task | standing false approvals vested | per thousand tasks vested | bad deliveries settled / false approvals among them | leak per thousand bad deliveries |
|---|---|---|---|---|---|---|---|---|---|---|
| Q1 | 486 | 2380 / 808 | 754 | 1864 | 4895 | **22.03** | 0.1 ± 0.1 | 0.3 | 129 / 0.1 | **1.2** |
| Q2 | 516 | 3053 / 1114 | 41 | 2215 | 3860 | **19.92** | 0.5 ± 0.2 | 0.9 | 134 / 0.5 | **3.4** |
| Q3 | 519 | 3016 / 951 | 11 | 1899 | 3731 | **18.52** | 0.8 ± 0.2 | 1.6 | 132 / 0.8 | **6.5** |
| Q4 | 512 | 2923 / 808 | 13 | 1609 | 3398 | **17.09** | 0.9 ± 0.2 | 1.8 | 133 / 0.9 | **6.8** |
| the run (the quarters summed) | 2033 | 11372 / 3681 | 819 | 7587 | 15885 | **19.35** | 2.4 | 1.2 | 527 / 2.4 | **4.5** |

**The whole run.** Review seats a run by who sat and the seat (plants included): member audit 2132, member initial 3085, member panel 811, plant alias initial 360, state audit 237, state initial 9, state panel 46 — the state's share of the review seats **0.046** (292 of 6319). The review fees a run by who sat and the seat kind: member audit 5455, member initial 5332, member panel 2109, state audit 629, state initial 15, state panel 106 — the members' 12895 in all, the state's 751. Ω's net 3252.3 ± 46.8; the tasks vested 2036.5 ± 10.2 a run, bad deliveries 527.2 ± 6.9, the standing false approvals 2.4 ± 0.4 — the leak 0.0012 per vested task (the row's), 0.004 per bad delivery; the system's overhead a vested task 19.34, the customers' 12.97; the state's review cost 819, unreimbursed 0; the cost of truth 7587.


# The frozen policy in a 1,000-tick run, read by quarter — `arm4` (D2, the economy reviewer's addendum 4; `quarters.py`)

Cell: `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --arm 4`; seeds 21-40. Means over the seeds (± SE where shown). A quarter is 250 ticks; the seats by the quarter of the seat's assignment, the standing false approvals by the quarter of their vesting, the fees by the quarter of their payment, the snapshots at the first decision at or after the boundary (the members alive and the tiers at that moment; the cost of truth cumulative there). The audit and panel seats are on members' real deliveries (the plants' beside); a member's seat inspected (care spent) or blind (none spent, a verdict of either sign).

## direct (20 seeds; the standing false approvals a run 5.2 ± 0.7, care 0.975, m^A at the end 1.00)

**The dials by close** (mean over the seeds that reached the close): 

| close | t | m_t | π_t | m^A | π^A | m^La | m^Ld | planted approvals adjudicated at a member's audit seat | F̂^A read (n) |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 187 | 1.01 | 0.101 | 1.00 | 0.020 | 1.00 | 1.00 | 0.0 | — (0) |
| 1 | 376 | 1.16 | 0.116 | 1.00 | 0.020 | 1.00 | 1.00 | 0.0 | — (0) |
| 2 | 550 | 1.19 | 0.119 | 1.00 | 0.020 | 1.00 | 1.00 | 0.0 | — (0) |
| 3 | 715 | 1.33 | 0.133 | 1.00 | 0.020 | 1.00 | 1.00 | 0.0 | — (0) |
| 4 | 875 | 1.32 | 0.132 | 1.00 | 0.020 | 1.00 | 1.00 | 0.0 | — (0) |
| 5 | 866 | 1.81 | 0.181 | 1.00 | 0.020 | 1.00 | 1.00 | 0.0 | — (0) |
| 6 | 916 | 2.25 | 0.225 | 1.00 | 0.020 | 1.00 | 1.00 | 0.0 | — (0) |
| 7 | 922 | 2.18 | 0.218 | 1.00 | 0.020 | 1.00 | 1.00 | 0.0 | — (0) |

**By quarter**:

| quarter | members alive | duty-ineligible / panel-ineligible of them | probationers / suspended | audit seats on members' work: member inspected / member blind / state | the member's share of them | member blind rate | audit seats on plants: member (blind) / state | panel seats: member inspected / blind / state | standing false approvals vested: member-confirmed / state-confirmed / never audited / other | roots vested | review fees: members / the state | cost of truth (cumulative at the boundary; the quarter's) | m^A / π^A at the boundary |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Q1 (t 0–250) | 16.9 | 0.0 / 16.0 | 17.2 / 0.8 | 0 / 0 / 517 | **0.00** | **0.000** | 0 (0) / 0 | 0 / 0 / 0 | **0.0 ± 0.0** / 0.5 ± 0.1 / 0.0 ± 0.0 / 0.1 | 512 | 1328 / 1456 | 393 (393) | 1.00 / 0.020 |
| Q2 (t 250–500) | 20.6 | 0.0 / 12.3 | 11.5 / 0.5 | 0 / 0 / 493 | **0.00** | **0.000** | 0 (0) / 0 | 0 / 0 / 0 | **0.0 ± 0.0** / 0.3 ± 0.1 / 0.0 ± 0.0 / 0.0 | 511 | 1248 / 1349 | 667 (274) | 1.00 / 0.020 |
| Q3 (t 500–750) | 22.6 | 0.0 / 7.2 | 1.6 / 0.2 | 0 / 0 / 499 | **0.00** | **0.000** | 0 (0) / 0 | 0 / 0 / 0 | **0.0 ± 0.0** / 0.4 ± 0.1 / 0.7 ± 0.2 / 0.1 | 532 | 1273 / 1289 | 1014 (347) | 1.00 / 0.020 |
| Q4 (t 750–1000) | 19.6 | 0.0 / 4.5 | 0.0 / 0.0 | 0 / 0 / 473 | **0.00** | **0.000** | 0 (0) / 0 | 0 / 0 / 0 | **0.0 ± 0.0** / 0.6 ± 0.2 / 2.6 ± 0.6 / 0.1 | 535 | 1182 / 1067 | 1387 (373) | 1.00 / 0.020 |

**The whole run.** Review seats a run by who sat and the seat (plants included): member audit 0, member initial 2957, state audit 1984, state deciding 454, state initial 0, state panel 0 — the state's share of the review seats **0.452** (2438 of 5395). The review fees a run by who sat and the seat kind: member audit 0, member initial 5031, state audit 5160, state initial 0, state panel 0 — the members' 5031 in all, the state's 5160. Ω's net 7447.6 ± 58.1; the tasks vested 2090.6 ± 7.5 a run, bad deliveries 535.8 ± 7.0, the standing false approvals 5.2 ± 0.7 — the leak 0.0025 per vested task (the row's), 0.010 per bad delivery; the system's overhead a vested task 9.68, the customers' 11.87; the state's review cost 6416, unreimbursed 169; the cost of truth 1387.

## greedy (20 seeds; the standing false approvals a run 3.1 ± 0.5, care 0.995, m^A at the end 1.00)

**The dials by close** (mean over the seeds that reached the close): 

| close | t | m_t | π_t | m^A | π^A | m^La | m^Ld | planted approvals adjudicated at a member's audit seat | F̂^A read (n) |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 187 | 1.06 | 0.106 | 1.00 | 0.020 | 1.00 | 1.00 | 0.0 | — (0) |
| 1 | 375 | 1.05 | 0.105 | 1.00 | 0.020 | 1.00 | 1.00 | 0.0 | — (0) |
| 2 | 559 | 1.05 | 0.105 | 1.00 | 0.020 | 1.00 | 1.00 | 0.0 | — (0) |
| 3 | 740 | 1.03 | 0.103 | 1.00 | 0.020 | 1.00 | 1.00 | 0.0 | — (0) |
| 4 | 922 | 1.09 | 0.109 | 1.00 | 0.020 | 1.00 | 1.00 | 0.0 | — (0) |
| 5 | 914 | 1.29 | 0.129 | 1.00 | 0.020 | 1.00 | 1.00 | 0.0 | — (0) |
| 6 | 976 | 1.41 | 0.141 | 1.00 | 0.020 | 1.00 | 1.00 | 0.0 | — (0) |

**By quarter**:

| quarter | members alive | duty-ineligible / panel-ineligible of them | probationers / suspended | audit seats on members' work: member inspected / member blind / state | the member's share of them | member blind rate | audit seats on plants: member (blind) / state | panel seats: member inspected / blind / state | standing false approvals vested: member-confirmed / state-confirmed / never audited / other | roots vested | review fees: members / the state | cost of truth (cumulative at the boundary; the quarter's) | m^A / π^A at the boundary |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Q1 (t 0–250) | 16.2 | 0.0 / 15.1 | 16.8 / 0.5 | 0 / 0 / 515 | **0.00** | **0.000** | 0 (0) / 0 | 0 / 0 / 0 | **0.0 ± 0.0** / 0.3 ± 0.1 / 0.0 ± 0.0 / 0.0 | 509 | 1327 / 1446 | 374 (374) | 1.00 / 0.020 |
| Q2 (t 250–500) | 20.0 | 0.0 / 10.9 | 11.2 / 0.6 | 0 / 0 / 485 | **0.00** | **0.000** | 0 (0) / 0 | 0 / 0 / 0 | **0.0 ± 0.0** / 0.1 ± 0.1 / 0.2 ± 0.1 / 0.1 | 507 | 1254 / 1327 | 655 (281) | 1.00 / 0.020 |
| Q3 (t 500–750) | 23.4 | 0.0 / 6.8 | 3.0 / 0.3 | 0 / 0 / 485 | **0.00** | **0.000** | 0 (0) / 0 | 0 / 0 / 0 | **0.0 ± 0.0** / 0.3 ± 0.1 / 0.4 ± 0.2 / 0.0 | 531 | 1274 / 1272 | 954 (299) | 1.00 / 0.020 |
| Q4 (t 750–1000) | 19.9 | 0.0 / 4.9 | 0.0 / 0.0 | 0 / 0 / 455 | **0.00** | **0.000** | 0 (0) / 0 | 0 / 0 / 0 | **0.0 ± 0.0** / 0.4 ± 0.1 / 1.2 ± 0.2 / 0.0 | 536 | 1173 / 1012 | 1266 (312) | 1.00 / 0.020 |

**The whole run.** Review seats a run by who sat and the seat (plants included): member initial 2928, state audit 1940, state deciding 431 — the state's share of the review seats **0.447** (2371 of 5299). The review fees a run by who sat and the seat kind: member initial 5029, state audit 5056 — the members' 5029 in all, the state's 5056. Ω's net 7326.9 ± 72.1; the tasks vested 2084.1 ± 10.1 a run, bad deliveries 540.2 ± 4.5, the standing false approvals 3.1 ± 0.5 — the leak 0.0015 per vested task (the row's), 0.006 per bad delivery; the system's overhead a vested task 9.41, the customers' 11.77; the state's review cost 6277, unreimbursed 167; the cost of truth 1266.

## hand (20 seeds; the standing false approvals a run 4.5 ± 0.5, care 0.000, m^A at the end 1.00)

**The dials by close** (mean over the seeds that reached the close): 

| close | t | m_t | π_t | m^A | π^A | m^La | m^Ld | planted approvals adjudicated at a member's audit seat | F̂^A read (n) |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 190 | 1.98 | 0.198 | 1.00 | 0.020 | 1.00 | 1.00 | 0.0 | — (0) |
| 1 | 298 | 3.86 | 0.386 | 1.00 | 0.020 | 1.00 | 1.00 | 0.0 | — (0) |
| 2 | 357 | 3.98 | 0.398 | 1.00 | 0.020 | 1.00 | 1.00 | 0.0 | — (0) |
| 3 | 408 | 3.90 | 0.390 | 1.00 | 0.020 | 1.00 | 1.00 | 0.0 | — (0) |
| 4 | 457 | 3.73 | 0.373 | 1.00 | 0.020 | 1.00 | 1.00 | 0.0 | — (0) |
| 5 | 511 | 3.45 | 0.345 | 1.00 | 0.020 | 1.00 | 1.00 | 0.0 | — (0) |
| 6 | 570 | 3.16 | 0.316 | 1.00 | 0.020 | 1.00 | 1.00 | 0.0 | — (0) |
| 7 | 635 | 2.85 | 0.285 | 1.00 | 0.020 | 1.00 | 1.00 | 0.0 | — (0) |
| 8 | 706 | 2.61 | 0.261 | 1.00 | 0.020 | 1.00 | 1.00 | 0.0 | — (0) |
| 9 | 786 | 2.43 | 0.243 | 1.00 | 0.020 | 1.00 | 1.00 | 0.0 | — (0) |
| 10 | 874 | 2.25 | 0.225 | 1.00 | 0.020 | 1.00 | 1.00 | 0.0 | — (0) |
| 11 | 927 | 2.29 | 0.229 | 1.00 | 0.020 | 1.00 | 1.00 | 0.0 | — (0) |
| 12 | 953 | 2.61 | 0.261 | 1.00 | 0.020 | 1.00 | 1.00 | 0.0 | — (0) |
| 13 | 996 | 2.24 | 0.224 | 1.00 | 0.020 | 1.00 | 1.00 | 0.0 | — (0) |

**By quarter**:

| quarter | members alive | duty-ineligible / panel-ineligible of them | probationers / suspended | audit seats on members' work: member inspected / member blind / state | the member's share of them | member blind rate | audit seats on plants: member (blind) / state | panel seats: member inspected / blind / state | standing false approvals vested: member-confirmed / state-confirmed / never audited / other | roots vested | review fees: members / the state | cost of truth (cumulative at the boundary; the quarter's) | m^A / π^A at the boundary |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Q1 (t 0–250) | 16.1 | 0.0 / 14.8 | 16.8 / 1.3 | 0 / 0 / 543 | **0.00** | **0.000** | 0 (0) / 0 | 0 / 0 / 0 | **0.0 ± 0.0** / 2.0 ± 0.4 / 0.0 ± 0.0 / 0.2 | 498 | 1244 / 1551 | 500 (500) | 1.00 / 0.020 |
| Q2 (t 250–500) | 18.9 | 0.0 / 3.1 | 0.0 / 0.5 | 0 / 0 / 488 | **0.00** | **0.000** | 0 (0) / 0 | 0 / 0 / 0 | **0.0 ± 0.0** / 1.6 ± 0.3 / 0.0 ± 0.0 / 0.1 | 489 | 1436 / 1323 | 1339 (839) | 1.00 / 0.020 |
| Q3 (t 500–750) | 18.2 | 0.0 / 3.1 | 0.0 / 0.0 | 0 / 0 / 485 | **0.00** | **0.000** | 0 (0) / 0 | 0 / 0 / 0 | **0.0 ± 0.0** / 0.5 ± 0.2 / 0.0 ± 0.0 / 0.0 | 502 | 1446 / 1297 | 2075 (736) | 1.00 / 0.020 |
| Q4 (t 750–1000) | 17.9 | 0.0 / 3.2 | 0.0 / 0.0 | 0 / 0 / 470 | **0.00** | **0.000** | 0 (0) / 0 | 0 / 0 / 0 | **0.0 ± 0.0** / 0.1 ± 0.1 / 0.0 ± 0.0 / 0.0 | 488 | 1363 / 1316 | 2685 (610) | 1.00 / 0.020 |

**The whole run.** Review seats a run by who sat and the seat (plants included): member audit 3, member initial 3137, member panel 0, state audit 1990, state deciding 447, state initial 1, state panel 0 — the state's share of the review seats **0.437** (2439 of 5580). The review fees a run by who sat and the seat kind: member audit 8, member initial 5480, member panel 1, state audit 5485, state initial 2, state panel 1 — the members' 5489 in all, the state's 5487. Ω's net 7884.2 ± 21.6; the tasks vested 1983.6 ± 11.8 a run, bad deliveries 502.6 ± 5.2, the standing false approvals 4.5 ± 0.5 — the leak 0.0023 per vested task (the row's), 0.009 per bad delivery; the system's overhead a vested task 14.43, the customers' 14.07; the state's review cost 6803, unreimbursed 145; the cost of truth 2685.

## careful (20 seeds; the standing false approvals a run 3.0 ± 0.4, care 1.000, m^A at the end 1.00)

**The dials by close** (mean over the seeds that reached the close): 

| close | t | m_t | π_t | m^A | π^A | m^La | m^Ld | planted approvals adjudicated at a member's audit seat | F̂^A read (n) |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 187 | 1.01 | 0.101 | 1.00 | 0.020 | 1.00 | 1.00 | 0.0 | — (0) |
| 1 | 378 | 1.00 | 0.100 | 1.00 | 0.020 | 1.00 | 1.00 | 0.0 | — (0) |
| 2 | 567 | 1.06 | 0.106 | 1.00 | 0.020 | 1.00 | 1.00 | 0.0 | — (0) |
| 3 | 749 | 1.07 | 0.107 | 1.00 | 0.020 | 1.00 | 1.00 | 0.0 | — (0) |
| 4 | 928 | 1.05 | 0.105 | 1.00 | 0.020 | 1.00 | 1.00 | 0.0 | — (0) |
| 5 | 869 | 1.52 | 0.152 | 1.00 | 0.020 | 1.00 | 1.00 | 0.0 | — (0) |
| 6 | 995 | 1.37 | 0.137 | 1.00 | 0.020 | 1.00 | 1.00 | 0.0 | — (0) |

**By quarter**:

| quarter | members alive | duty-ineligible / panel-ineligible of them | probationers / suspended | audit seats on members' work: member inspected / member blind / state | the member's share of them | member blind rate | audit seats on plants: member (blind) / state | panel seats: member inspected / blind / state | standing false approvals vested: member-confirmed / state-confirmed / never audited / other | roots vested | review fees: members / the state | cost of truth (cumulative at the boundary; the quarter's) | m^A / π^A at the boundary |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Q1 (t 0–250) | 17.0 | 0.0 / 15.8 | 17.4 / 0.6 | 0 / 0 / 516 | **0.00** | **0.000** | 0 (0) / 0 | 0 / 0 / 0 | **0.0 ± 0.0** / 0.2 ± 0.1 / 0.0 ± 0.0 / 0.0 | 513 | 1326 / 1451 | 358 (358) | 1.00 / 0.020 |
| Q2 (t 250–500) | 20.8 | 0.0 / 12.2 | 11.5 / 0.3 | 0 / 0 / 495 | **0.00** | **0.000** | 0 (0) / 0 | 0 / 0 / 0 | **0.0 ± 0.0** / 0.3 ± 0.1 / 0.1 ± 0.1 / 0.0 | 519 | 1264 / 1343 | 649 (290) | 1.00 / 0.020 |
| Q3 (t 500–750) | 23.6 | 0.0 / 6.4 | 2.0 / 0.5 | 0 / 0 / 492 | **0.00** | **0.000** | 0 (0) / 0 | 0 / 0 / 0 | **0.0 ± 0.0** / 0.3 ± 0.1 / 0.2 ± 0.1 / 0.0 | 536 | 1265 / 1272 | 977 (328) | 1.00 / 0.020 |
| Q4 (t 750–1000) | 20.2 | 0.0 / 3.5 | 0.0 / 0.1 | 0 / 0 / 442 | **0.00** | **0.000** | 0 (0) / 0 | 0 / 0 / 0 | **0.0 ± 0.0** / 0.3 ± 0.1 / 1.4 ± 0.2 / 0.0 | 537 | 1165 / 963 | 1255 (278) | 1.00 / 0.020 |

**The whole run.** Review seats a run by who sat and the seat (plants included): member audit 0, member initial 2936, state audit 1946, state deciding 431 — the state's share of the review seats **0.447** (2377 of 5313). The review fees a run by who sat and the seat kind: member audit 0, member initial 5019, state audit 5028 — the members' 5019 in all, the state's 5028. Ω's net 7241.4 ± 56.7; the tasks vested 2103.8 ± 5.7 a run, bad deliveries 529.5 ± 5.6, the standing false approvals 3.0 ± 0.4 — the leak 0.0014 per vested task (the row's), 0.006 per bad delivery; the system's overhead a vested task 9.25, the customers' 11.58; the state's review cost 6196, unreimbursed 168; the cost of truth 1255.


# The frozen policy in a 1,000-tick run, read by quarter — `arm2` (D2, the economy reviewer's addendum 4; `quarters.py`)

Cell: `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --arm 2`; seeds 21-40. Means over the seeds (± SE where shown). A quarter is 250 ticks; the seats by the quarter of the seat's assignment, the standing false approvals by the quarter of their vesting, the fees by the quarter of their payment, the snapshots at the first decision at or after the boundary (the members alive and the tiers at that moment; the cost of truth cumulative there). The audit and panel seats are on members' real deliveries (the plants' beside); a member's seat inspected (care spent) or blind (none spent, a verdict of either sign).

## direct (20 seeds; the standing false approvals a run 4.5 ± 0.6, care 0.975, m^A at the end 1.00)

**The dials by close** (mean over the seeds that reached the close): 

| close | t | m_t | π_t | m^A | π^A | m^La | m^Ld | planted approvals adjudicated at a member's audit seat | F̂^A read (n) |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 187 | 1.01 | 0.101 | 1.00 | 0.020 | 1.00 | 1.00 | 0.0 | — (0) |
| 1 | 381 | 1.02 | 0.102 | 1.00 | 0.020 | 1.00 | 1.00 | 0.0 | — (0) |
| 2 | 572 | 1.03 | 0.103 | 1.00 | 0.020 | 1.00 | 1.00 | 0.0 | — (0) |
| 3 | 756 | 1.16 | 0.116 | 1.00 | 0.020 | 1.23 | 1.00 | 0.0 | — (0) |
| 4 | 930 | 1.37 | 0.137 | 1.00 | 0.020 | 1.29 | 1.00 | 0.0 | — (0) |
| 5 | 918 | 3.36 | 0.336 | 1.00 | 0.020 | 1.32 | 1.00 | 0.0 | — (0) |
| 6 | 890 | 3.24 | 0.324 | 1.00 | 0.020 | 1.00 | 1.00 | 0.0 | — (0) |
| 7 | 948 | 4.00 | 0.400 | 1.00 | 0.020 | 1.00 | 1.00 | 0.0 | — (0) |
| 8 | 997 | 4.00 | 0.400 | 1.00 | 0.020 | 1.00 | 1.00 | 0.0 | — (0) |

**By quarter**:

| quarter | members alive | duty-ineligible / panel-ineligible of them | probationers / suspended | audit seats on members' work: member inspected / member blind / state | the member's share of them | member blind rate | audit seats on plants: member (blind) / state | panel seats: member inspected / blind / state | standing false approvals vested: member-confirmed / state-confirmed / never audited / other | roots vested | review fees: members / the state | cost of truth (cumulative at the boundary; the quarter's) | m^A / π^A at the boundary |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Q1 (t 0–250) | 16.1 | 0.0 / 15.1 | 17.5 / 0.7 | 0 / 0 / 514 | **0.00** | **0.000** | 0 (0) / 0 | 1 / 2 / 52 | **0.0 ± 0.0** / 0.3 ± 0.1 / 0.0 ± 0.0 / 0.0 | 512 | 1329 / 1568 | 390 (390) | 1.00 / 0.020 |
| Q2 (t 250–500) | 20.1 | 0.0 / 12.6 | 11.6 / 0.8 | 0 / 0 / 477 | **0.00** | **0.000** | 0 (0) / 0 | 10 / 2 / 41 | **0.0 ± 0.0** / 0.3 ± 0.1 / 0.1 ± 0.1 / 0.0 | 495 | 1252 / 1409 | 646 (256) | 1.00 / 0.020 |
| Q3 (t 500–750) | 25.0 | 0.0 / 9.3 | 1.7 / 0.3 | 0 / 0 / 490 | **0.00** | **0.000** | 0 (0) / 0 | 26 / 4 / 23 | **0.0 ± 0.0** / 0.6 ± 0.2 / 0.5 ± 0.2 / 0.1 | 528 | 1362 / 1368 | 1006 (360) | 1.00 / 0.020 |
| Q4 (t 750–1000) | 20.4 | 0.0 / 5.8 | 0.1 / 0.1 | 0 / 0 / 464 | **0.00** | **0.000** | 0 (0) / 0 | 48 / 3 / 4 | **0.0 ± 0.0** / 0.5 ± 0.2 / 2.2 ± 0.6 / 0.0 | 532 | 1340 / 1067 | 1451 (445) | 1.00 / 0.020 |

**The quarter's price** (the system's overhead per task vested in the quarter: the care spent on real and planted cases, the state's seats' cost, the cost of truth and the plants' awarded price, by the quarter of each; the standing false approvals vested in the quarter over the bad deliveries vested in it, per thousand; the bad deliveries here are a member's real roots vested unfulfilled, the false approvals among them those vested approved — every unfulfilled root that vests is a false approval, so the two counts coincide; the leak per thousand bad deliveries is read on the bad deliveries settled in the quarter at every outcome — the driver's `bad_deliveries` by the quarter of the settlement — and the false approvals among them):

| quarter | roots vested | care on real / on plants | the state's seats' cost | the cost of truth (the quarter's) | the plants' price | system overhead a vested task | standing false approvals vested | per thousand tasks vested | bad deliveries settled / false approvals among them | leak per thousand bad deliveries |
|---|---|---|---|---|---|---|---|---|---|---|
| Q1 | 512 | 1664 / 164 | 1966 | 390 | 1410 | **10.92** | 0.3 ± 0.1 | 0.6 | 132 / 0.3 | **2.3** |
| Q2 | 495 | 1558 / 160 | 1801 | 256 | 1338 | **10.33** | 0.5 ± 0.1 | 0.9 | 125 / 0.5 | **3.6** |
| Q3 | 528 | 1687 / 185 | 1728 | 360 | 925 | **9.25** | 1.1 ± 0.3 | 2.2 | 133 / 1.1 | **8.6** |
| Q4 | 532 | 1720 / 244 | 1319 | 445 | 1244 | **9.35** | 2.6 ± 0.6 | 5.0 | 132 / 2.6 | **20.1** |
| the run (the quarters summed) | 2067 | 6629 / 753 | 6815 | 1451 | 4917 | **9.95** | 4.5 | 2.2 | 522 / 4.5 | **8.7** |

**The whole run.** Review seats a run by who sat and the seat (plants included): member audit 0, member initial 2901, member panel 136, state audit 1947, state deciding 443, state initial 0, state panel 120 — the state's share of the review seats **0.453** (2510 of 5546). The review fees a run by who sat and the seat kind: member audit 1, member initial 4986, member panel 297, state audit 5128, state initial 0, state panel 284 — the members' 5284 in all, the state's 5413. Ω's net 7240.9 ± 65.0; the tasks vested 2069.1 ± 11.5 a run, bad deliveries 522.0 ± 4.5, the standing false approvals 4.5 ± 0.6 — the leak 0.0022 per vested task (the row's), 0.009 per bad delivery; the system's overhead a vested task 9.93, the customers' 12.17; the state's review cost 6766, unreimbursed 591; the cost of truth 1451.

## greedy (20 seeds; the standing false approvals a run 3.3 ± 0.4, care 0.997, m^A at the end 1.00)

**The dials by close** (mean over the seeds that reached the close): 

| close | t | m_t | π_t | m^A | π^A | m^La | m^Ld | planted approvals adjudicated at a member's audit seat | F̂^A read (n) |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 187 | 1.00 | 0.100 | 1.00 | 0.020 | 1.00 | 1.00 | 0.0 | — (0) |
| 1 | 379 | 1.00 | 0.100 | 1.00 | 0.020 | 1.00 | 1.00 | 0.0 | — (0) |
| 2 | 568 | 1.05 | 0.105 | 1.00 | 0.020 | 1.00 | 1.00 | 0.0 | — (0) |
| 3 | 748 | 1.07 | 0.107 | 1.00 | 0.020 | 1.09 | 1.00 | 0.0 | — (0) |
| 4 | 929 | 1.08 | 0.108 | 1.00 | 0.020 | 1.13 | 1.00 | 0.0 | — (0) |
| 5 | 912 | 2.00 | 0.200 | 1.00 | 0.020 | 1.00 | 1.00 | 0.0 | — (0) |

**By quarter**:

| quarter | members alive | duty-ineligible / panel-ineligible of them | probationers / suspended | audit seats on members' work: member inspected / member blind / state | the member's share of them | member blind rate | audit seats on plants: member (blind) / state | panel seats: member inspected / blind / state | standing false approvals vested: member-confirmed / state-confirmed / never audited / other | roots vested | review fees: members / the state | cost of truth (cumulative at the boundary; the quarter's) | m^A / π^A at the boundary |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Q1 (t 0–250) | 17.1 | 0.0 / 15.7 | 17.4 / 0.2 | 0 / 0 / 518 | **0.00** | **0.000** | 0 (0) / 0 | 3 / 0 / 49 | **0.0 ± 0.0** / 0.1 ± 0.1 / 0.0 ± 0.0 / 0.0 | 514 | 1335 / 1557 | 395 (395) | 1.00 / 0.020 |
| Q2 (t 250–500) | 21.2 | 0.0 / 12.4 | 11.4 / 0.8 | 0 / 0 / 496 | **0.00** | **0.000** | 0 (0) / 0 | 12 / 0 / 42 | **0.0 ± 0.0** / 0.2 ± 0.1 / 0.1 ± 0.1 / 0.1 | 520 | 1299 / 1430 | 686 (291) | 1.00 / 0.020 |
| Q3 (t 500–750) | 24.0 | 0.0 / 7.0 | 2.3 / 0.3 | 0 / 0 / 495 | **0.00** | **0.000** | 0 (0) / 0 | 32 / 0 / 20 | **0.0 ± 0.0** / 0.5 ± 0.2 / 0.2 ± 0.1 / 0.0 | 535 | 1366 / 1331 | 1049 (362) | 1.00 / 0.020 |
| Q4 (t 750–1000) | 20.0 | 0.0 / 4.2 | 0.1 / 0.0 | 0 / 0 / 451 | **0.00** | **0.000** | 0 (0) / 0 | 48 / 0 / 4 | **0.0 ± 0.0** / 0.6 ± 0.2 / 1.6 ± 0.3 / 0.0 | 534 | 1312 / 1004 | 1485 (437) | 1.00 / 0.020 |

**The quarter's price** (the system's overhead per task vested in the quarter: the care spent on real and planted cases, the state's seats' cost, the cost of truth and the plants' awarded price, by the quarter of each; the standing false approvals vested in the quarter over the bad deliveries vested in it, per thousand; the bad deliveries here are a member's real roots vested unfulfilled, the false approvals among them those vested approved — every unfulfilled root that vests is a false approval, so the two counts coincide; the leak per thousand bad deliveries is read on the bad deliveries settled in the quarter at every outcome — the driver's `bad_deliveries` by the quarter of the settlement — and the false approvals among them):

| quarter | roots vested | care on real / on plants | the state's seats' cost | the cost of truth (the quarter's) | the plants' price | system overhead a vested task | standing false approvals vested | per thousand tasks vested | bad deliveries settled / false approvals among them | leak per thousand bad deliveries |
|---|---|---|---|---|---|---|---|---|---|---|
| Q1 | 514 | 1691 / 166 | 1940 | 395 | 1349 | **10.78** | 0.1 ± 0.1 | 0.2 | 135 / 0.1 | **0.7** |
| Q2 | 520 | 1664 / 173 | 1809 | 291 | 1334 | **10.13** | 0.4 ± 0.1 | 0.8 | 132 / 0.4 | **3.0** |
| Q3 | 535 | 1755 / 202 | 1623 | 362 | 917 | **9.08** | 0.7 ± 0.2 | 1.3 | 136 / 0.7 | **5.1** |
| Q4 | 534 | 1786 / 235 | 1228 | 437 | 1063 | **8.89** | 2.1 ± 0.3 | 3.9 | 132 / 2.1 | **15.9** |
| the run (the quarters summed) | 2103 | 6896 / 776 | 6600 | 1485 | 4663 | **9.71** | 3.3 | 1.6 | 535 / 3.3 | **6.2** |

**The whole run.** Review seats a run by who sat and the seat (plants included): member initial 2942, member panel 136, state audit 1960, state deciding 436, state panel 115 — the state's share of the review seats **0.449** (2511 of 5588). The review fees a run by who sat and the seat kind: member initial 5016, member panel 296, state audit 5056, state panel 267 — the members' 5312 in all, the state's 5322. Ω's net 7096.3 ± 50.2; the tasks vested 2103.4 ± 5.3 a run, bad deliveries 535.1 ± 5.1, the standing false approvals 3.3 ± 0.4 — the leak 0.0016 per vested task (the row's), 0.006 per bad delivery; the system's overhead a vested task 9.69, the customers' 11.89; the state's review cost 6553, unreimbursed 612; the cost of truth 1485.

## hand (20 seeds; the standing false approvals a run 3.8 ± 0.4, care 0.000, m^A at the end 1.00)

**The dials by close** (mean over the seeds that reached the close): 

| close | t | m_t | π_t | m^A | π^A | m^La | m^Ld | planted approvals adjudicated at a member's audit seat | F̂^A read (n) |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 191 | 1.98 | 0.198 | 1.00 | 0.020 | 1.00 | 1.00 | 0.0 | — (0) |
| 1 | 298 | 3.84 | 0.384 | 1.00 | 0.020 | 1.00 | 1.00 | 0.0 | — (0) |
| 2 | 358 | 3.91 | 0.391 | 1.00 | 0.020 | 1.00 | 1.00 | 0.0 | — (0) |
| 3 | 409 | 3.93 | 0.393 | 1.00 | 0.020 | 1.00 | 1.00 | 0.0 | — (0) |
| 4 | 459 | 3.83 | 0.383 | 1.00 | 0.020 | 1.07 | 1.00 | 0.0 | — (0) |
| 5 | 512 | 3.57 | 0.357 | 1.00 | 0.020 | 1.12 | 1.00 | 0.0 | — (0) |
| 6 | 568 | 3.31 | 0.331 | 1.00 | 0.020 | 1.13 | 1.00 | 0.0 | — (0) |
| 7 | 631 | 3.09 | 0.309 | 1.00 | 0.020 | 1.12 | 1.00 | 0.0 | — (0) |
| 8 | 699 | 2.88 | 0.288 | 1.00 | 0.020 | 1.15 | 1.00 | 0.0 | — (0) |
| 9 | 773 | 2.63 | 0.263 | 1.00 | 0.020 | 1.21 | 1.00 | 0.0 | — (0) |
| 10 | 853 | 2.50 | 0.250 | 1.00 | 0.020 | 1.18 | 1.00 | 0.0 | — (0) |
| 11 | 907 | 2.44 | 0.244 | 1.00 | 0.020 | 1.23 | 1.00 | 0.0 | — (0) |
| 12 | 945 | 2.59 | 0.259 | 1.00 | 0.020 | 1.47 | 1.00 | 0.0 | — (0) |
| 13 | 986 | 2.84 | 0.284 | 1.00 | 0.020 | 1.49 | 1.00 | 0.0 | — (0) |

**By quarter**:

| quarter | members alive | duty-ineligible / panel-ineligible of them | probationers / suspended | audit seats on members' work: member inspected / member blind / state | the member's share of them | member blind rate | audit seats on plants: member (blind) / state | panel seats: member inspected / blind / state | standing false approvals vested: member-confirmed / state-confirmed / never audited / other | roots vested | review fees: members / the state | cost of truth (cumulative at the boundary; the quarter's) | m^A / π^A at the boundary |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Q1 (t 0–250) | 16.4 | 0.0 / 14.6 | 16.4 / 1.1 | 0 / 0 / 544 | **0.00** | **0.000** | 0 (0) / 0 | 2 / 1 / 31 | **0.0 ± 0.0** / 2.0 ± 0.4 / 0.0 ± 0.0 / 0.1 | 497 | 1247 / 1640 | 487 (487) | 1.00 / 0.020 |
| Q2 (t 250–500) | 19.6 | 0.0 / 2.8 | 0.1 / 0.7 | 0 / 0 / 488 | **0.00** | **0.000** | 0 (0) / 0 | 30 / 0 / 13 | **0.0 ± 0.0** / 0.9 ± 0.2 / 0.0 ± 0.0 / 0.1 | 488 | 1543 / 1340 | 1456 (970) | 1.00 / 0.020 |
| Q3 (t 500–750) | 18.6 | 0.0 / 2.8 | 0.0 / 0.0 | 0 / 0 / 485 | **0.00** | **0.000** | 0 (0) / 0 | 46 / 0 / 1 | **0.0 ± 0.0** / 0.3 ± 0.1 / 0.0 ± 0.0 / 0.0 | 498 | 1625 / 1259 | 2446 (989) | 1.00 / 0.020 |
| Q4 (t 750–1000) | 18.2 | 0.0 / 2.1 | 0.0 / 0.0 | 0 / 0 / 469 | **0.00** | **0.000** | 0 (0) / 0 | 48 / 0 / 1 | **0.0 ± 0.0** / 0.2 ± 0.2 / 0.0 ± 0.0 / 0.1 | 487 | 1562 / 1295 | 3214 (768) | 1.00 / 0.020 |

**The quarter's price** (the system's overhead per task vested in the quarter: the care spent on real and planted cases, the state's seats' cost, the cost of truth and the plants' awarded price, by the quarter of each; the standing false approvals vested in the quarter over the bad deliveries vested in it, per thousand; the bad deliveries here are a member's real roots vested unfulfilled, the false approvals among them those vested approved — every unfulfilled root that vests is a false approval, so the two counts coincide; the leak per thousand bad deliveries is read on the bad deliveries settled in the quarter at every outcome — the driver's `bad_deliveries` by the quarter of the settlement — and the false approvals among them):

| quarter | roots vested | care on real / on plants | the state's seats' cost | the cost of truth (the quarter's) | the plants' price | system overhead a vested task | standing false approvals vested | per thousand tasks vested | bad deliveries settled / false approvals among them | leak per thousand bad deliveries |
|---|---|---|---|---|---|---|---|---|---|---|
| Q1 | 497 | 1172 / 141 | 2073 | 487 | 1844 | **11.50** | 2.2 ± 0.4 | 4.4 | 129 / 2.2 | **17.1** |
| Q2 | 488 | 1452 / 524 | 1673 | 970 | 3682 | **17.03** | 1.0 ± 0.2 | 2.1 | 125 / 1.0 | **8.0** |
| Q3 | 498 | 1680 / 578 | 1543 | 989 | 3682 | **17.01** | 0.3 ± 0.1 | 0.6 | 122 / 0.3 | **2.5** |
| Q4 | 487 | 1657 / 448 | 1620 | 768 | 2948 | **15.29** | 0.2 ± 0.2 | 0.5 | 121 / 0.2 | **2.1** |
| the run (the quarters summed) | 1970 | 5962 / 1692 | 6910 | 3214 | 12157 | **15.20** | 3.8 | 1.9 | 497 / 3.8 | **7.5** |

**The whole run.** Review seats a run by who sat and the seat (plants included): member audit 8, member initial 3153, member panel 208, state audit 1992, state deciding 441, state initial 1, state panel 47 — the state's share of the review seats **0.424** (2481 of 5850). The review fees a run by who sat and the seat kind: member audit 22, member initial 5457, member panel 498, state audit 5417, state initial 2, state panel 115 — the members' 5977 in all, the state's 5534. Ω's net 7556.9 ± 37.5; the tasks vested 1982.5 ± 18.1 a run, bad deliveries 497.1 ± 8.5, the standing false approvals 3.8 ± 0.4 — the leak 0.0019 per vested task (the row's), 0.007 per bad delivery; the system's overhead a vested task 15.09, the customers' 14.28; the state's review cost 6848, unreimbursed 487; the cost of truth 3214.

## careful (20 seeds; the standing false approvals a run 2.5 ± 0.4, care 1.000, m^A at the end 1.00)

**The dials by close** (mean over the seeds that reached the close): 

| close | t | m_t | π_t | m^A | π^A | m^La | m^Ld | planted approvals adjudicated at a member's audit seat | F̂^A read (n) |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 187 | 1.00 | 0.100 | 1.00 | 0.020 | 1.00 | 1.00 | 0.0 | — (0) |
| 1 | 378 | 1.01 | 0.101 | 1.00 | 0.020 | 1.00 | 1.00 | 0.0 | — (0) |
| 2 | 566 | 1.04 | 0.104 | 1.00 | 0.020 | 1.00 | 1.00 | 0.0 | — (0) |
| 3 | 748 | 1.03 | 0.103 | 1.00 | 0.020 | 1.10 | 1.00 | 0.0 | — (0) |
| 4 | 931 | 1.02 | 0.102 | 1.00 | 0.020 | 1.14 | 1.00 | 0.0 | — (0) |

**By quarter**:

| quarter | members alive | duty-ineligible / panel-ineligible of them | probationers / suspended | audit seats on members' work: member inspected / member blind / state | the member's share of them | member blind rate | audit seats on plants: member (blind) / state | panel seats: member inspected / blind / state | standing false approvals vested: member-confirmed / state-confirmed / never audited / other | roots vested | review fees: members / the state | cost of truth (cumulative at the boundary; the quarter's) | m^A / π^A at the boundary |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Q1 (t 0–250) | 17.0 | 0.0 / 15.8 | 17.6 / 0.2 | 0 / 0 / 518 | **0.00** | **0.000** | 0 (0) / 0 | 3 / 0 / 50 | **0.0 ± 0.0** / 0.2 ± 0.1 / 0.0 ± 0.0 / 0.0 | 514 | 1336 / 1559 | 385 (385) | 1.00 / 0.020 |
| Q2 (t 250–500) | 21.3 | 0.0 / 12.2 | 11.7 / 0.6 | 0 / 0 / 497 | **0.00** | **0.000** | 0 (0) / 0 | 12 / 0 / 42 | **0.0 ± 0.0** / 0.3 ± 0.1 / 0.1 ± 0.0 / 0.1 | 521 | 1311 / 1438 | 691 (306) | 1.00 / 0.020 |
| Q3 (t 500–750) | 24.1 | 0.0 / 7.0 | 2.0 / 0.4 | 0 / 0 / 493 | **0.00** | **0.000** | 0 (0) / 0 | 32 / 0 / 20 | **0.0 ± 0.0** / 0.2 ± 0.1 / 0.3 ± 0.1 / 0.0 | 535 | 1363 / 1330 | 1057 (366) | 1.00 / 0.020 |
| Q4 (t 750–1000) | 20.4 | 0.0 / 3.6 | 0.0 / 0.0 | 0 / 0 / 443 | **0.00** | **0.000** | 0 (0) / 0 | 49 / 0 / 2 | **0.0 ± 0.0** / 0.3 ± 0.1 / 0.9 ± 0.3 / 0.0 | 533 | 1314 / 980 | 1472 (415) | 1.00 / 0.020 |

**The quarter's price** (the system's overhead per task vested in the quarter: the care spent on real and planted cases, the state's seats' cost, the cost of truth and the plants' awarded price, by the quarter of each; the standing false approvals vested in the quarter over the bad deliveries vested in it, per thousand; the bad deliveries here are a member's real roots vested unfulfilled, the false approvals among them those vested approved — every unfulfilled root that vests is a false approval, so the two counts coincide; the leak per thousand bad deliveries is read on the bad deliveries settled in the quarter at every outcome — the driver's `bad_deliveries` by the quarter of the settlement — and the false approvals among them):

| quarter | roots vested | care on real / on plants | the state's seats' cost | the cost of truth (the quarter's) | the plants' price | system overhead a vested task | standing false approvals vested | per thousand tasks vested | bad deliveries settled / false approvals among them | leak per thousand bad deliveries |
|---|---|---|---|---|---|---|---|---|---|---|
| Q1 | 514 | 1695 / 165 | 1941 | 385 | 1376 | **10.82** | 0.2 ± 0.1 | 0.5 | 136 / 0.2 | **1.8** |
| Q2 | 521 | 1672 / 176 | 1815 | 306 | 1333 | **10.17** | 0.4 ± 0.1 | 0.8 | 132 / 0.4 | **3.0** |
| Q3 | 535 | 1761 / 199 | 1611 | 366 | 905 | **9.04** | 0.6 ± 0.2 | 1.0 | 134 / 0.6 | **4.1** |
| Q4 | 533 | 1804 / 226 | 1192 | 415 | 1016 | **8.73** | 1.2 ± 0.3 | 2.3 | 135 / 1.2 | **9.3** |
| the run (the quarters summed) | 2104 | 6932 / 766 | 6559 | 1472 | 4630 | **9.68** | 2.5 | 1.2 | 537 / 2.5 | **4.6** |

**The whole run.** Review seats a run by who sat and the seat (plants included): member initial 2943, member panel 135, state audit 1951, state deciding 427, state panel 113 — the state's share of the review seats **0.447** (2490 of 5568). The review fees a run by who sat and the seat kind: member initial 5033, member panel 291, state audit 5042, state panel 264 — the members' 5324 in all, the state's 5306. Ω's net 7095.0 ± 53.0; the tasks vested 2104.2 ± 5.1 a run, bad deliveries 537.1 ± 5.1, the standing false approvals 2.5 ± 0.4 — the leak 0.0012 per vested task (the row's), 0.005 per bad delivery; the system's overhead a vested task 9.66, the customers' 11.88; the state's review cost 6514, unreimbursed 606; the cost of truth 1472.


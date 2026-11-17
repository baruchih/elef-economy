# Addendum 22: the record's readings and the six reads without training (November 17, 2026; a20/launch.sh at eca3d5ee3)

Loaded: cw3 100, r9 100, r15 (a18) 100, r15 (rerun) 100, r17 120, r18 100, r19 100; r20 120, r21 120, r22 100, r23 100, r24 100, r25 100 episodes.


## 0. The rerun against the record

Read 15's world (conduct M at 0.5 on 1 slot in 4, world 3's cell, seeds 21–120) run again whole at eca3d5ee3 — the harness of 906fc5ac4 plus the `--theta-duty` passthrough at its default — for the probation spells, which a18/r15 (f16e1ffee) did not export; checked against a18/r15 on every row column and every per-slot key the record carries, before it is read:

- **read 15 (conduct M at 0.5 on 1 slot in 4)**: 100 seeds, 39879 row columns and 336554 per-slot keys over 3958 slots compared with the record's — **0 differences**.

## AB5.1. Three figures that differ between the notes — the like-for-like base

- **read 9**: the gap like for like on K3's base (the careful's income in good standing less the conduct's rate over the careful's good ticks, the ruling of November 16) 63 ± 14; the same difference on the conduct's good ticks (the careful's rate over the conduct's good ticks, less the conduct's income) 65 ± 14. The level saving like for like as a ratio of the seeds' means: with each seed's numerator and denominator on the careful's good ticks (§117's form) 0.38 ± 0.06; on the conduct's own good ticks (§118's form) 0.40 ± 0.07; the mean of the seeds' ratios 0.47 ± 0.07 (the same per seed either way).
- **read 15**: the gap like for like on K3's base (the careful's income in good standing less the conduct's rate over the careful's good ticks, the ruling of November 16) 284 ± 14; the same difference on the conduct's good ticks (the careful's rate over the conduct's good ticks, less the conduct's income) 195 ± 10. The level saving like for like as a ratio of the seeds' means: with each seed's numerator and denominator on the careful's good ticks (§117's form) 1.80 ± 0.07; on the conduct's own good ticks (§118's form) 1.79 ± 0.07; the mean of the seeds' ratios 1.85 ± 0.07 (the same per seed either way).

What moved is the base of the like-for-like comparison, not the data. Per seed the two forms are the same ratio (the K3 gap plus the benefit's denominator, scaled by the conduct's good ticks over the careful's, is the careful's rate on the conduct's good ticks less the conduct's income); as a ratio of the seeds' means they weight the seeds differently — §117 by the care scaled to the careful's ticks, §118 by the care as measured — and the figures differ by a hundredth or two, a third of the error. **The figures of record from here**: for the gap like for like, K3's base as ruled (read 9's 63 ± 14); for the level saving like for like, §118's form (0.40 ± 0.07 for read 9, 1.79 ± 0.07 for read 15), the numerator and the denominator both on the conduct's own good ticks, which is the quantity the identity x = q · T* was confirmed on. §118's Z3.3 column headed 'the gap like for like' (65 ± 14) is the gap on the conduct's good ticks — the numerator of the level saving — and is relabelled so by erratum; the gain like for like there, 108 ± 15, is 0.9 of the care less what the claims spared less that gap, and with K3's gap in its place it reads 109 ± 16 (the same quantity on the careful's good ticks; both stand, each on its base).

## AB5.2. The way back from a member's suspension, as built

A spell on the way back begins when the hundred ticks off duty end (the probation's start) and ends in a readmission (`since_susp ≥ 4` outcomes of either kind with the record passing θ_duty), in another suspension (a wrong planted verdict on probation), at the slot's departure, or open at the run's end. The whole way is counted from the tick of the suspension that began it (the slot's suspension log) to the readmission. Read 15's world holds the most; the others beside.

| spells | n | ended: member / suspended / departed / open | **to membership (from the probation's start): ticks, reviews** | the whole way from the suspension to the readmission: ticks | to a suspension: ticks, reviews | every spell: ticks, reviews |
|---|---|---|---|---|---|---|
| read 15's world (M at 0.5 on 1 in 4; the rerun) | 65 | 0.37 / 0.14 / 0.49 / 0.00 | **67 ± 11 ticks, 24.2 ± 2.5 reviews** (medians 46, 22) | **168 ± 11** (median 147) | 58 ± 23 ticks, 12.6 ± 3.9 reviews | 54 ± 7 ticks, 12.9 ± 1.7 reviews |
| world 3's all-careful (cw3) | 2 | 1.00 / 0.00 / 0.00 / 0.00 | **54 ± 12 ticks, 40.5 ± 13.5 reviews** (medians 54, 40) | **156 ± 12** (median 156) | nan ticks, nan reviews | 54 ± 12 ticks, 40.5 ± 13.5 reviews |
| read 9's world (M at 0.1 on 1 in 4) | 5 | 0.60 / 0.20 / 0.20 / 0.00 | **63 ± 25 ticks, 41.0 ± 15.6 reviews** (medians 38, 28) | **164 ± 25** (median 139) | 20 ticks, 10.0 reviews | 46 ± 17 ticks, 26.8 ± 12.3 reviews |
| read 18's world (M at 0.1 on every slot) | 16 | 0.56 / 0.06 / 0.38 / 0.00 | **55 ± 10 ticks, 20.3 ± 3.5 reviews** (medians 44, 17) | **156 ± 10** (median 145) | 28 ticks, 11.0 reviews | 70 ± 15 ticks, 15.4 ± 2.8 reviews |
| read 19's world (M at 0.2 on 1 in 4) | 19 | 0.37 / 0.21 / 0.42 / 0.00 | **104 ± 29 ticks, 27.7 ± 3.6 reviews** (medians 95, 31) | **205 ± 29** (median 196) | 43 ± 19 ticks, 16.5 ± 6.9 reviews | 62 ± 14 ticks, 16.6 ± 3.0 reviews |
| read 20's world (all-careful, θ_duty 0.34) | 60 | 0.42 / 0.20 / 0.17 / 0.22 | **118 ± 15 ticks, 68.5 ± 8.7 reviews** (medians 91, 47) | **219 ± 15** (median 192) | 25 ± 5 ticks, 14.4 ± 2.3 reviews | 86 ± 10 ticks, 42.2 ± 5.3 reviews |
| read 21's world (G at 1.0, θ_duty 0.34) | 163 | 0.47 / 0.15 / 0.25 / 0.13 | **75 ± 7 ticks, 43.1 ± 3.5 reviews** (medians 56, 36) | **176 ± 7** (median 158) | 57 ± 15 ticks, 25.1 ± 7.1 reviews | 73 ± 5 ticks, 32.0 ± 2.4 reviews |
| read 22's world (M at 0.1, θ_duty 0.34) | 74 | 0.49 / 0.15 / 0.28 / 0.08 | **86 ± 10 ticks, 42.1 ± 4.7 reviews** (medians 64, 31) | **187 ± 10** (median 166) | 54 ± 14 ticks, 20.8 ± 4.9 reviews | 77 ± 7 ticks, 30.1 ± 3.2 reviews |
| read 23's world (all-careful, θ_duty 0.20) | 632 | 0.26 / 0.15 / 0.41 / 0.18 | **130 ± 7 ticks, 52.3 ± 2.4 reviews** (medians 109, 43) | **231 ± 7** (median 210) | 90 ± 10 ticks, 32.4 ± 3.6 reviews | 113 ± 3 ticks, 32.4 ± 1.2 reviews |
| read 24's world (M at 0.1, θ_duty 0.20) | 812 | 0.28 / 0.15 / 0.40 / 0.17 | **103 ± 5 ticks, 43.2 ± 1.7 reviews** (medians 80, 35) | **204 ± 5** (median 181) | 83 ± 7 ticks, 32.3 ± 2.8 reviews | 102 ± 3 ticks, 30.3 ± 1.0 reviews |
| read 25's world (case-keyed M at 0.1 on every slot) | 19 | 0.47 / 0.16 / 0.37 / 0.00 | **112 ± 27 ticks, 26.9 ± 2.5 reviews** (medians 121, 29) | **213 ± 27** (median 222) | 30 ± 14 ticks, 8.7 ± 2.7 reviews | 85 ± 16 ticks, 17.4 ± 2.7 reviews |

Read 15's world by group:

| spells | n | ended: member / suspended / departed / open | **to membership (from the probation's start): ticks, reviews** | the whole way from the suspension to the readmission: ticks | to a suspension: ticks, reviews | every spell: ticks, reviews |
|---|---|---|---|---|---|---|
| the conduct's slots (M at 0.5) | 63 | 0.37 / 0.13 / 0.51 / 0.00 | **63 ± 11 ticks, 23.2 ± 2.3 reviews** (medians 45, 22) | **164 ± 11** (median 146) | 54 ± 25 ticks, 13.4 ± 4.3 reviews | 52 ± 7 ticks, 12.4 ± 1.6 reviews |
| the careful slots beside | 2 | 0.50 / 0.50 / 0.00 / 0.00 | **161 ticks, 49.0 reviews** (medians 161, 49) | **262** (median 262) | 92 ticks, 6.0 reviews | 126 ± 34 ticks, 27.5 ± 21.5 reviews |

An arrival's probation in the same worlds, for the comparison Z3.6 made:

| spells | n | ended: member / suspended / departed / open | **to membership (from the probation's start): ticks, reviews** | the whole way from the suspension to the readmission: ticks | to a suspension: ticks, reviews | every spell: ticks, reviews |
|---|---|---|---|---|---|---|
| read 15's world (M at 0.5 on 1 in 4; the rerun) | 2102 | 0.77 / 0.23 / 0.00 / 0.00 | **428 ± 4 ticks, 42.1 ± 0.5 reviews** (medians 432, 39) |  | 317 ± 9 ticks, 27.6 ± 0.9 reviews | 403 ± 4 ticks, 38.9 ± 0.5 reviews |
| world 3's all-careful (cw3) | 2208 | 0.78 / 0.22 / 0.00 / 0.00 | **488 ± 5 ticks, 53.4 ± 0.7 reviews** (medians 530, 51) |  | 374 ± 10 ticks, 36.0 ± 1.2 reviews | 462 ± 4 ticks, 49.5 ± 0.6 reviews |
| read 9's world (M at 0.1 on 1 in 4) | 2224 | 0.78 / 0.22 / 0.00 / 0.00 | **489 ± 5 ticks, 52.4 ± 0.7 reviews** (medians 521, 49) |  | 369 ± 10 ticks, 34.5 ± 1.2 reviews | 463 ± 5 ticks, 48.5 ± 0.6 reviews |
| read 18's world (M at 0.1 on every slot) | 2137 | 0.76 / 0.24 / 0.00 / 0.00 | **466 ± 4 ticks, 44.0 ± 0.5 reviews** (medians 484, 41) |  | 359 ± 9 ticks, 29.7 ± 0.9 reviews | 441 ± 4 ticks, 40.6 ± 0.5 reviews |
| read 19's world (M at 0.2 on 1 in 4) | 2157 | 0.78 / 0.22 / 0.00 / 0.00 | **495 ± 5 ticks, 51.7 ± 0.6 reviews** (medians 520, 49) |  | 347 ± 10 ticks, 31.4 ± 1.1 reviews | 462 ± 4 ticks, 47.2 ± 0.6 reviews |
| read 20's world (all-careful, θ_duty 0.34) | 2660 | 0.77 / 0.23 / 0.00 / 0.00 | **490 ± 4 ticks, 53.9 ± 0.6 reviews** (medians 530, 51) |  | 364 ± 9 ticks, 34.6 ± 1.1 reviews | 462 ± 4 ticks, 49.5 ± 0.6 reviews |
| read 21's world (G at 1.0, θ_duty 0.34) | 2656 | 0.77 / 0.23 / 0.00 / 0.00 | **491 ± 5 ticks, 53.0 ± 0.6 reviews** (medians 527, 50) |  | 365 ± 9 ticks, 34.3 ± 1.0 reviews | 462 ± 4 ticks, 48.7 ± 0.5 reviews |
| read 22's world (M at 0.1, θ_duty 0.34) | 2244 | 0.77 / 0.23 / 0.00 / 0.00 | **491 ± 5 ticks, 52.2 ± 0.7 reviews** (medians 531, 49) |  | 364 ± 10 ticks, 34.9 ± 1.2 reviews | 462 ± 5 ticks, 48.3 ± 0.6 reviews |
| read 23's world (all-careful, θ_duty 0.20) | 2211 | 0.71 / 0.24 / 0.00 / 0.06 | **570 ± 5 ticks, 56.7 ± 0.7 reviews** (medians 592, 53) |  | 406 ± 11 ticks, 37.5 ± 1.2 reviews | 539 ± 5 ticks, 52.8 ± 0.6 reviews |
| read 24's world (M at 0.1, θ_duty 0.20) | 2244 | 0.71 / 0.24 / 0.00 / 0.05 | **558 ± 5 ticks, 54.4 ± 0.6 reviews** (medians 574, 51) |  | 373 ± 10 ticks, 33.7 ± 1.0 reviews | 517 ± 5 ticks, 50.0 ± 0.6 reviews |
| read 25's world (case-keyed M at 0.1 on every slot) | 2081 | 0.76 / 0.24 / 0.00 / 0.00 | **462 ± 4 ticks, 43.9 ± 0.5 reviews** (medians 468, 40) |  | 324 ± 9 ticks, 27.2 ± 0.9 reviews | 429 ± 4 ticks, 39.9 ± 0.5 reviews |

## AB4.5 and AB4.7 from the record

- **AB4.5.** The planted cases are 0.140 ± 0.001 of a careful member's reviews as a member over every seat in world 3's all-careful (0.115 ± 0.000 the bad ones), so 27.5 reviews as a member hold 3.9 planted cases of both kinds and 3.2 bad ones. By the rule the first suspension of a member that claims at every review falls at its fourth planted bad case where its window starts empty (the record is read from n_min = 4 bad plants on; four wrong of four is 5/6), and at the fifth wrong one where the window holds the four right verdicts of a probation (five wrong beside four right is 6/11, the fourth 5/10 is not above 0.5).

**AB4.7 — the split of read 9's loss from the flows by seat** (a19/rerun/r9 at 906fc5ac4: the conduct's slots and the careful beside them, a mean a slot by seed, the difference careful − conduct ± its SE over the seeds; every flow real at its tick and tallied to the seat of the review it belongs to; the bond on the planted cases is the wrong planted verdicts as a member times the bond G^V = 5 at the run's closing index, the bond on real work the rest of the bonds lost at member seats).

| | the conduct's slot | the careful beside | **careful − conduct** |
|---|---|---|---|
| the lifetime of record (wallet + benefit) | 819 | 928 | **+109 ± 22** |
| the benefit (what the claims spared) | 21.2 | 0.0 | **-21.2 ± 0.6** |
| ticks in good standing | 531 | 552 | **+21 ± 13** |
| income in good standing (K3) | 550 | 660 | **+110 ± 18** |
| reviews as a member (every seat) | 75.4 | 92.2 | **+16.7 ± 2.4** |
| … at the first review | 46.7 | 44.8 | **-1.9 ± 1.4** |
| … at the audit seat | 24.1 | 39.6 | **+15.6 ± 1.6** |
| … at the third seat | 2.0 | 3.2 | **+1.3 ± 0.1** |
| … at an appeal panel | 2.5 | 4.2 | **+1.7 ± 0.2** |
| … at a dispute panel | 0.2 | 0.3 | **+0.1 ± 0.0** |
| **income beyond the care at member seats (fee + emission + uplift), real** | 297 | 379 | **+82 ± 10** |
| … at the first review | 169.8 | 166.3 | **-3.4 ± 5.4** |
| … at the audit seat | 108.0 | 179.1 | **+71.1 ± 7.4** |
| … at the third seat | 8.1 | 15.0 | **+6.9 ± 0.7** |
| … at an appeal panel | 10.2 | 17.4 | **+7.2 ± 0.7** |
| … at a dispute panel | 0.9 | 1.3 | **+0.4 ± 0.1** |
| the care spent and claimed at member seats | 215 | 262 | **+46 ± 7** |
| the care reimbursed at member seats | 215 | 262 | **+46 ± 7** |
| **bonds lost at member seats, real (all)** | 24.9 | 22.8 | **-2.1 ± 0.8** |
| … at the first review | 15.7 | 11.2 | **-4.4 ± 0.5** |
| … at the audit seat | 6.7 | 9.7 | **+3.0 ± 0.5** |
| … at the third seat | 1.6 | 0.8 | **-0.8 ± 0.1** |
| … at an appeal panel | 0.9 | 1.1 | **+0.2 ± 0.1** |
| … at a dispute panel | 0.1 | 0.1 | **+0.0 ± 0.0** |
| … on the planted cases (wrong planted verdicts × G^V at the closing index; an upper estimate, the bond is 5 real at P_0 and more as P_t falls) | 8.7 | 4.4 | **-4.3 ± 0.3** |
| … on real work (the rest; a lower estimate) | 16.2 | 18.4 | **+2.2 ± 0.6** |
| wrong planted verdicts as a member | 1.31 | 0.66 | **-0.65 ± 0.05** |
| wrong first approvals of real bad work / of which overturned | 1.45 | 0.64 | **-0.81 ± 0.06** |
| … overturned | 1.30 | 0.56 | **-0.74 ± 0.05** |
| court fees at member seats (net) | 0.0 | 0.0 | **+0.0 ± 0.0** |

So of the 109 real a careful slot ends ahead of the conduct's of record (the 109 of §116; with the 21.2 the claims spared, 131 before the saving), the seats carry 82 real of income beyond the care that the conduct does not earn (71 of it at the audit seat, 14 at the panels, -3 at the first review), the bonds -2.1 real in all — the conduct loses 4.3 more on its planted cases (an upper estimate at the closing index; at least -3.3 at P_0) and 4.4 more at the first review, where its 0.74 more overturned approvals of real bad work sit, while the careful loses 2.3 more at the audit seat and the panels it holds and the conduct does not (a careful auditor's own one error in twenty on a real case, overturned when challenged) — and the rest is the work side and the ticks out of good standing (21 fewer good ticks). The reviewer's 75 real in seats, under 4 in bonds on real work and 'more than half of what the conduct loses is what its failed planted cases cost it' are read against these figures in the notes.

## Reads 20 and 23. The all-careful population with the suspension's threshold moved — against world 3's all-careful by seed (seeds 21–120, the seeds the record holds)

The row V3.1 gave for an all-careful population (a slot's lifetime of record, with the reservation, and its income in good standing — the like-for-like figure for a population with no conduct beside it), for all slots, the founders and the arrivals; then the suspensions, the spells, the admissions and the world's side, each cell − world 3 paired by seed.


**read 20: θ_duty 0.34 (the second failure)** (120 seeds; paired on the 100 the record holds)

| slots | measure | seeds | world 3's cell | the cell | **cell − world 3, paired** | SE from nothing |
|---|---|---|---|---|---|---|
| every slot | lifetime of record | 100 | 902 | 899 | **-3 ± 5** | -0.6 |
| every slot | with the reservation | 100 | 1029 | 1025 | **-5 ± 5** | -0.9 |
| every slot | income in good standing | 100 | 626 | 624 | **-1 ± 2** | -0.7 |
| every slot | good ticks a slot | 100 | 550 | 548 | **-3 ± 1** | -2.4 |
| every slot | suspensions a slot | 100 | 0.13 | 0.15 | **+0.02 ± 0.00** | 6.1 |
| every slot | slots suspended at least once (share) | 100 | 0.120 | 0.135 | **+0.016 ± 0.003** | 5.4 |
| every slot | … as a member | 100 | 0.001 | 0.019 | **+0.018 ± 0.002** | 9.0 |
| every slot | … on probation | 100 | 0.119 | 0.121 | **+0.002 ± 0.002** | 1.2 |
| every slot | arrivals admitted within the run (share) | 100 | 0.879 | 0.878 | **-0.002 ± 0.003** | -0.5 |
| the founders | lifetime of record | 100 | 1096 | 1090 | **-6 ± 8** | -0.8 |
| the founders | with the reservation | 100 | 1276 | 1268 | **-7 ± 8** | -1.0 |
| the founders | income in good standing | 100 | 831 | 830 | **-1 ± 3** | -0.5 |
| the founders | good ticks a slot | 100 | 776 | 774 | **-2 ± 2** | -1.0 |
| the founders | suspensions a slot | 100 | 0.00 | 0.03 | **+0.03 ± 0.00** | 6.4 |
| the founders | slots suspended at least once (share) | 100 | 0.001 | 0.025 | **+0.024 ± 0.004** | 6.8 |
| the founders | … as a member | 100 | 0.001 | 0.025 | **+0.024 ± 0.004** | 6.8 |
| the founders | … on probation | 100 | 0.000 | 0.004 | **+0.004 ± 0.001** | 2.9 |
| the arrivals | lifetime of record | 100 | 704 | 703 | **-0 ± 5** | -0.0 |
| the arrivals | with the reservation | 100 | 777 | 776 | **-2 ± 4** | -0.4 |
| the arrivals | income in good standing | 100 | 415 | 414 | **-1 ± 4** | -0.3 |
| the arrivals | good ticks a slot | 100 | 319 | 315 | **-3 ± 2** | -1.6 |
| the arrivals | suspensions a slot | 100 | 0.25 | 0.27 | **+0.02 ± 0.01** | 2.7 |
| the arrivals | slots suspended at least once (share) | 100 | 0.241 | 0.248 | **+0.007 ± 0.004** | 1.5 |
| the arrivals | … as a member | 100 | 0.000 | 0.012 | **+0.012 ± 0.003** | 4.9 |
| the arrivals | … on probation | 100 | 0.241 | 0.242 | **+0.001 ± 0.004** | 0.2 |
| the arrivals | arrivals admitted within the run (share) | 100 | 0.879 | 0.878 | **-0.002 ± 0.003** | -0.5 |
| the world | | | | | | |
| the world | standing false approvals a run | 100 | 2.5 | 2.5 | **+0.0 ± 0.1** | 0.4 |
| the world | the leak, ‰ of bad deliveries | 100 | 4.8 | 4.8 | **+0.1 ± 0.2** | 0.3 |
| the world | the system overhead a vested task | 100 | 11.88 | 11.92 | **+0.04 ± 0.02** | 2.0 |
| the world | the cost of truth a run | 100 | 2968 | 2978 | **+10 ± 10** | 1.0 |
| the world | departures a run | 100 | 16.7 | 16.6 | **-0.1 ± 0.1** | -0.7 |
| the world | arrivals a run | 100 | 19.5 | 19.5 | **-0.0 ± 0.0** | -1.0 |
| the world | P_t at the end | 100 | 14.8 | 14.9 | **+0.1 ± 0.1** | 1.0 |

(The suspension log and the spells are matched a tick apart — a spell closes at the standing step of the tick after the suspension is logged; 0 probation spells end at a tick the log does not hold.)

**The careful slots that take a wrong planted verdict as a member, from that failure on** — read 20: θ_duty 0.34 (the second failure) against world 3's cell by seed (the slots' first failure to the exit: the income of record with the benefit, with the reservation, and like for like as the cell's failed slots' good-standing income less world 3's failed slots' rate over the cell's good ticks from the failure; a mean over a seed's failed slots, then over the seeds):

| | world 3's cell | the cell | **cell − world 3, paired** | SE |
|---|---|---|---|---|
| failed slots a seed (as members) | 16.3 | 15.8 | **-0.5 ± 0.2** | -2.2 |
| from the first failure: of record | 409 | 417 | **+8 ± 6** | 1.4 |
| … with the reservation | 459 | 469 | **+10 ± 6** | 1.8 |
| … like for like (the cell's good income less world 3's rate over the cell's good ticks) | | | **+4 ± 4** | 1.1 |
| good ticks from the failure | 355 | 354 | **-1 ± 4** | -0.3 |
| ticks from the failure to the exit | 362 | 367 | **+5 ± 4** | 1.1 |
| ticks without the earned seats | 163 | 166 | **+3 ± 3** | 0.7 |
| share whose seats returned | 0.70 | 0.69 | **-0.01 ± 0.01** | -1.3 |
| further wrong planted verdicts | 0.52 | 0.50 | **-0.01 ± 0.02** | -0.9 |
| suspensions from the failure on | 0.00 | 0.05 | **+0.05 ± 0.01** | 8.0 |
| departed share | 0.25 | 0.26 | **+0.01 ± 0.01** | 1.1 |

**read 23: θ_duty 0.20 (the first failure)** (100 seeds; paired on the 100 the record holds)

| slots | measure | seeds | world 3's cell | the cell | **cell − world 3, paired** | SE from nothing |
|---|---|---|---|---|---|---|
| every slot | lifetime of record | 100 | 902 | 823 | **-79 ± 12** | -6.8 |
| every slot | with the reservation | 100 | 1029 | 938 | **-91 ± 11** | -8.3 |
| every slot | income in good standing | 100 | 626 | 608 | **-17 ± 4** | -4.1 |
| every slot | good ticks a slot | 100 | 550 | 484 | **-67 ± 4** | -16.0 |
| every slot | suspensions a slot | 100 | 0.13 | 0.38 | **+0.26 ± 0.01** | 24.9 |
| every slot | slots suspended at least once (share) | 100 | 0.120 | 0.331 | **+0.211 ± 0.009** | 23.5 |
| every slot | … as a member | 100 | 0.001 | 0.221 | **+0.220 ± 0.007** | 32.5 |
| every slot | … on probation | 100 | 0.119 | 0.140 | **+0.021 ± 0.006** | 3.4 |
| every slot | arrivals admitted within the run (share) | 100 | 0.879 | 0.801 | **-0.079 ± 0.014** | -5.5 |
| the founders | lifetime of record | 100 | 1096 | 1085 | **-12 ± 18** | -0.7 |
| the founders | with the reservation | 100 | 1276 | 1244 | **-32 ± 16** | -1.9 |
| the founders | income in good standing | 100 | 831 | 904 | **+73 ± 10** | 7.0 |
| the founders | good ticks a slot | 100 | 776 | 747 | **-29 ± 5** | -5.5 |
| the founders | suspensions a slot | 100 | 0.00 | 0.31 | **+0.31 ± 0.01** | 24.1 |
| the founders | slots suspended at least once (share) | 100 | 0.001 | 0.279 | **+0.278 ± 0.012** | 23.9 |
| the founders | … as a member | 100 | 0.001 | 0.279 | **+0.278 ± 0.012** | 23.9 |
| the founders | … on probation | 100 | 0.000 | 0.022 | **+0.022 ± 0.003** | 7.2 |
| the arrivals | lifetime of record | 100 | 704 | 558 | **-146 ± 14** | -10.1 |
| the arrivals | with the reservation | 100 | 777 | 627 | **-150 ± 14** | -10.5 |
| the arrivals | income in good standing | 100 | 415 | 308 | **-107 ± 13** | -8.3 |
| the arrivals | good ticks a slot | 100 | 319 | 215 | **-104 ± 7** | -14.5 |
| the arrivals | suspensions a slot | 100 | 0.25 | 0.45 | **+0.20 ± 0.02** | 12.2 |
| the arrivals | slots suspended at least once (share) | 100 | 0.241 | 0.384 | **+0.143 ± 0.014** | 10.6 |
| the arrivals | … as a member | 100 | 0.000 | 0.163 | **+0.163 ± 0.009** | 18.0 |
| the arrivals | … on probation | 100 | 0.241 | 0.260 | **+0.019 ± 0.012** | 1.5 |
| the arrivals | arrivals admitted within the run (share) | 100 | 0.879 | 0.801 | **-0.079 ± 0.014** | -5.5 |
| the world | | | | | | |
| the world | standing false approvals a run | 100 | 2.5 | 1.9 | **-0.6 ± 0.2** | -3.4 |
| the world | the leak, ‰ of bad deliveries | 100 | 4.8 | 3.9 | **-0.9 ± 0.3** | -2.7 |
| the world | the system overhead a vested task | 100 | 11.88 | 12.43 | **+0.56 ± 0.04** | 12.8 |
| the world | the cost of truth a run | 100 | 2968 | 2776 | **-192 ± 31** | -6.3 |
| the world | departures a run | 100 | 16.7 | 15.7 | **-1.0 ± 0.2** | -4.4 |
| the world | arrivals a run | 100 | 19.5 | 19.6 | **+0.1 ± 0.0** | 3.1 |
| the world | P_t at the end | 100 | 14.8 | 18.0 | **+3.2 ± 0.3** | 9.6 |

(The suspension log and the spells are matched a tick apart — a spell closes at the standing step of the tick after the suspension is logged; 0 probation spells end at a tick the log does not hold.)

**The careful slots that take a wrong planted verdict as a member, from that failure on** — read 23: θ_duty 0.20 (the first failure) against world 3's cell by seed (the slots' first failure to the exit: the income of record with the benefit, with the reservation, and like for like as the cell's failed slots' good-standing income less world 3's failed slots' rate over the cell's good ticks from the failure; a mean over a seed's failed slots, then over the seeds):

| | world 3's cell | the cell | **cell − world 3, paired** | SE |
|---|---|---|---|---|
| failed slots a seed (as members) | 16.3 | 15.8 | **-0.6 ± 0.4** | -1.4 |
| from the first failure: of record | 409 | 341 | **-68 ± 12** | -5.8 |
| … with the reservation | 459 | 439 | **-20 ± 11** | -1.8 |
| … like for like (the cell's good income less world 3's rate over the cell's good ticks) | | | **+62 ± 6** | 10.5 |
| good ticks from the failure | 355 | 206 | **-150 ± 7** | -21.1 |
| ticks from the failure to the exit | 362 | 309 | **-53 ± 7** | -7.4 |
| ticks without the earned seats | 163 | 138 | **-25 ± 5** | -5.0 |
| share whose seats returned | 0.70 | 0.61 | **-0.09 ± 0.02** | -6.0 |
| further wrong planted verdicts | 0.52 | 0.42 | **-0.10 ± 0.03** | -3.7 |
| suspensions from the failure on | 0.00 | 0.32 | **+0.32 ± 0.01** | 23.4 |
| departed share | 0.25 | 0.40 | **+0.15 ± 0.01** | 10.4 |

## Read 21. Conduct G at 1.0 on 1 slot in 4 in the cell of the second failure (θ_duty 0.34), seeds 21–140 — read as read 17 was, and against read 17 by seed

| read | seeds | failed slots a seed: conduct / careful | **from the first failure: of record** (level at) | **with the reservation** (level at) | **like for like** (level at) | the conduct's claims after the first failure a slot (seats held / lost at the claim) | further wrong planted verdicts a slot: conduct / careful | ticks without the earned seats: conduct / careful (share whose seats returned) | suspensions from the failure on a failed slot: conduct / careful; departed share: conduct / careful | ticks from the first failure to the exit: conduct / careful |
|---|---|---|---|---|---|---|---|---|---|---|
| read 17: conduct G at 1.0, world 3's cell (120 seeds) | 120 | 5.6 / 16.5 | **+26 ± 21** (1.6) | **-22 ± 19** (0.5) | **-44 ± 17** (0.4) | 15.6 (0.0 / 15.6) | 1.68 / 0.49 | 152 / 164 (0.46 / 0.63) | 0.23 / 0.01; 0.54 / 0.31 | 297 / 340 |
| **read 21: conduct G at 1.0, θ_duty 0.34 (120 seeds)** | 120 | 5.4 / 16.4 | **+33 ± 22** (2.0) | **-11 ± 20** (0.6) | **-36 ± 17** (0.2) | 10.7 (0.0 / 10.7) | 1.18 / 0.48 | 155 / 164 (0.46 / 0.61) | 0.43 / 0.06; 0.48 / 0.33 | 298 / 335 |

Over the whole life (the careful slots beside, of the same world and seed; the cell's all-careful for the careful group's contrast):

| world / read | seeds | **of record** | temptation | **with the reservation** | temptation | **like for like** | temptation |
|---|---|---|---|---|---|---|---|
| read 17: G at 1.0, world 3's cell | 100 | **+21 ± 27** (0.8) | 1.8 ± 1.0 | **-10 ± 24** (-0.4) | 0.6 ± 0.9 | **-28 ± 15** (-1.8) | 0.0 ± 0.5 |
| **read 21: G at 1.0, θ_duty 0.34** | 120 | **+8 ± 26** (0.3) | 1.5 ± 1.5 | **-16 ± 23** (-0.7) | 0.1 ± 1.4 | **-37 ± 14** (-2.6) | -1.0 ± 0.8 |


| world / read | conduct's slots: claims (as a member / on probation); benefit; suspensions; audit seats; good ticks | careful slots: suspensions; audit seats; good ticks | **lost for each claim: of record / with the reservation / like for like** | careful group − all-careful of the cell; FA; leak ‰; overhead (all-careful of the cell) |
|---|---|---|---|---|
| read 17 | 8.9 (8.9 / 0.0); 26.2; 0.26; 35.1; 513 | 0.12; 38.2; 553 | **2.4 ± 3.0 / -1.1 ± 2.7 / -3.2 ± 1.8** | -11 ± 10; 3.0; 6; 12.7 (2.5; 5; 11.9) |
| **read 21** | 5.9 (5.9 / 0.0); 17.2; 0.36; 36.0; 507 | 0.16; 37.1; 545 | **1.3 ± 4.5 / -2.7 ± 4.0 / -6.3 ± 2.5** | -6 ± 10; 2.7; 5; 12.4 (2.5; 5; 11.9) |


| contrast | seeds | lifetime | first | second | **second − first, paired** | SE from nothing |
|---|---|---|---|---|---|---|
| read 21 against read 17 (G at 1.0: θ_duty 0.34 less world 3's cell), over the life | 100 | of record | +21 | +22 | **+0 ± 13** | 0.0 |
| read 21 against read 17 (G at 1.0: θ_duty 0.34 less world 3's cell), over the life | 100 | with the reservation | -10 | -2 | **+8 ± 11** | 0.8 |
| read 21 against read 17 (G at 1.0: θ_duty 0.34 less world 3's cell), over the life | 100 | like for like | -28 | -28 | **+0 ± 10** | 0.0 |
| … from the first failure on (the failed slots) | 120 | of record | +26 | +33 | **+7 ± 12** | 0.6 |
| … from the first failure on (the failed slots) | 120 | with the reservation | -22 | -11 | **+10 ± 12** | 0.8 |
| … from the first failure on (the failed slots) | 119 | like for like | -37 | -36 | **+1 ± 13** | 0.0 |

| read | failed slots | suspended after the failure (share) | ticks from the first failure to the first suspension: mean / median | claims in them a suspended slot: mean / median | claims a never-suspended failed slot |
|---|---|---|---|---|---|
| 17: G at 1.0, world 3's cell | 670 | 146 (0.22) | 279 / 241 | 25.9 / 24 | 8.8 |
| **21: G at 1.0, θ_duty 0.34** | 653 | 222 (0.34) | 208 / 158 | 14.2 / 10 | 6.0 |

## Reads 22 and 24. Conduct M at 0.1 on 1 slot in 4 in the two cells — read as reads 9 and 19 were, and against read 9 by seed

| world / read | seeds | **of record** | temptation | **with the reservation** | temptation | **like for like** | temptation |
|---|---|---|---|---|---|---|---|
| read 9: M at 0.1, world 3's cell (θ_duty 0.50) | 100 | **+109 ± 22** (4.9) | 6.2 ± 1.1 | **+90 ± 19** (4.8) | 5.2 ± 1.0 | **+63 ± 14** (4.6) | 3.8 ± 0.7 |
| **read 22: M at 0.1, θ_duty 0.34** | 100 | **+128 ± 21** (6.1) | 7.4 ± 1.2 | **+94 ± 18** (5.1) | 5.7 ± 1.0 | **+60 ± 13** (4.6) | 3.8 ± 0.6 |
| **read 24: M at 0.1, θ_duty 0.20** | 100 | **+149 ± 20** (7.3) | 11.5 ± 1.6 | **+102 ± 17** (6.0) | 8.2 ± 1.3 | **+21 ± 13** (1.6) | 2.2 ± 0.8 |
| read 19: M at 0.2, world 3's cell | 100 | **+200 ± 18** (11.2) | 6.2 ± 0.5 | **+173 ± 16** (11.1) | 5.5 ± 0.5 | **+149 ± 13** (11.8) | 4.6 ± 0.3 |


| world / read | conduct's slots: claims (as a member / on probation); benefit; suspensions; audit seats; good ticks | careful slots: suspensions; audit seats; good ticks | **lost for each claim: of record / with the reservation / like for like** | careful group − all-careful of the cell; FA; leak ‰; overhead (all-careful of the cell) |
|---|---|---|---|---|
| read 9 | 7.5 (7.5 / 0.0); 21.2; 0.13; 24.1; 531 | 0.13; 39.6; 552 | **14.7 ± 3.2 / 12.1 ± 2.7 / 8.4 ± 1.9** | +26 ± 10; 3.8; 7; 12.0 (2.5; 5; 11.9) |
| **read 22** | 7.1 (7.1 / 0.0); 20.0; 0.23; 23.0; 507 | 0.15; 39.8; 550 | **18.2 ± 3.3 / 13.2 ± 2.8 / 8.5 ± 1.9** | +27 ± 9; 3.6; 7; 12.1 (2.5; 5; 11.9) |
| **read 24** | 5.6 (5.6 / 0.0); 14.2; 0.70; 21.4; 398 | 0.40; 37.0; 489 | **26.8 ± 4.2 / 18.3 ± 3.4 / 3.7 ± 2.4** | +7 ± 15; 2.6; 5; 12.8 (1.9; 4; 12.4) |
| read 19 | 13.6 (13.6 / 0.0); 38.4; 0.14; 13.9; 517 | 0.13; 43.5; 550 | **14.7 ± 1.5 / 12.8 ± 1.3 / 11.0 ± 1.0** | +25 ± 10; 3.9; 7; 12.6 (2.5; 5; 11.9) |

| read | seeds | **the level saving, the ratio of the seeds' means: of record / with the reservation / like for like** | the mean of the seeds' ratios | the identity's q · T* | claims as a member over member reviews | member reviews a slot; claims as a member |
|---|---|---|---|---|---|---|
| read 9 | 100 | **0.61 ± 0.11 / 0.52 ± 0.09 / 0.40 ± 0.07** | 0.83 ± 0.13 / 0.69 ± 0.10 / 0.47 ± 0.07 | 0.62 / 0.52 / 0.38 | 0.099 | 75.4; 7.5 |
| **read 22** | 100 | **0.74 ± 0.12 / 0.56 ± 0.10 / 0.37 ± 0.06** | 1.01 ± 0.15 / 0.77 ± 0.12 / 0.44 ± 0.07 | 0.74 / 0.57 / 0.38 | 0.099 | 71.2; 7.1 |
| **read 24** | 100 | **1.14 ± 0.16 / 0.81 ± 0.13 / 0.22 ± 0.07** | 1.57 ± 0.20 / 1.12 ± 0.17 / 0.27 ± 0.08 | 1.15 / 0.82 / 0.22 | 0.099 | 56.1; 5.6 |
| read 19 | 100 | **1.23 ± 0.11 / 1.09 ± 0.09 / 0.91 ± 0.07** | 1.41 ± 0.11 / 1.24 ± 0.09 / 0.96 ± 0.07 | 1.24 / 1.10 / 0.93 | 0.199 | 68.3; 13.6 |

**W3's three counts and the suspensions** (a mean a slot):

| count | read 9: conduct / careful beside | **read 22: conduct / careful** | **read 24: conduct / careful** | read 19: conduct / careful |
|---|---|---|---|---|
| reviews as a member in a life | 75.4 / 92.2 | 71.2 / 91.9 | 56.1 / 79.7 | 68.3 / 97.9 |
| … at the first review | 46.7 / 44.8 | 43.8 / 44.3 | 30.9 / 35.6 | 51.7 / 45.9 |
| … at the audit seat | 24.1 / 39.6 | 23.0 / 39.8 | 21.4 / 37.0 | 13.9 / 43.5 |
| reviews on probation | 27.1 / 27.4 | 27.8 / 28.1 | 37.0 / 33.8 | 25.7 / 26.0 |
| good ticks a slot | 531 / 552 | 507 / 550 | 398 / 489 | 517 / 550 |
| planted bad cases met as a member | 8.3 / 11.0 | 7.7 / 11.0 | 6.4 / 9.7 | 7.2 / 12.6 |
| wrong planted verdicts as a member | 1.31 / 0.66 | 1.25 / 0.66 | 1.00 / 0.59 | 1.81 / 0.78 |
| … on probation | 0.13 / 0.13 | 0.13 / 0.13 | 0.17 / 0.17 | 0.11 / 0.13 |
| slots reaching a wrong planted verdict as a member (share) | 0.65 / 0.44 | 0.65 / 0.44 | 0.64 / 0.43 | 0.72 / 0.47 |
| **slots suspended at least once (share)** | 0.13 / 0.12 | 0.21 / 0.13 | 0.59 / 0.34 | 0.13 / 0.12 |
| suspensions a slot | 0.13 / 0.13 | 0.23 / 0.15 | 0.70 / 0.40 | 0.14 / 0.13 |
| reviews of real tasks as a member before the first suspension, over the slots suspended | 3.5 / 0.2 | 18.1 / 5.8 | 36.5 / 34.1 | 11.7 / 0.0 |
| wrong first approvals of real bad work in a life | 1.45 / 0.64 | 1.48 / 0.66 | 1.18 / 0.62 | 2.42 / 0.66 |
| … of which stay paid | 0.15 / 0.08 | 0.15 / 0.07 | 0.08 / 0.06 | 0.20 / 0.06 |
| the conduct's wrong first approvals over the careful beside's | 2.27 ± 0.11 | 2.23 ± 0.10 | 1.91 ± 0.08 | 3.64 ± 0.13 |


| contrast | seeds | lifetime | first | second | **second − first, paired** | SE from nothing |
|---|---|---|---|---|---|---|
| read 22 against read 9 (M at 0.1: θ_duty 0.34 less world 3's cell), the gap careful − conduct over the life | 100 | of record | +109 | +128 | **+19 ± 14** | 1.4 |
| read 22 against read 9 (M at 0.1: θ_duty 0.34 less world 3's cell), the gap careful − conduct over the life | 100 | with the reservation | +90 | +94 | **+4 ± 10** | 0.4 |
| read 22 against read 9 (M at 0.1: θ_duty 0.34 less world 3's cell), the gap careful − conduct over the life | 100 | like for like | +63 | +60 | **-3 ± 8** | -0.3 |
| read 24 against read 9 (M at 0.1: θ_duty 0.20 less world 3's cell) | 100 | of record | +109 | +149 | **+40 ± 22** | 1.8 |
| read 24 against read 9 (M at 0.1: θ_duty 0.20 less world 3's cell) | 100 | with the reservation | +90 | +102 | **+12 ± 18** | 0.7 |
| read 24 against read 9 (M at 0.1: θ_duty 0.20 less world 3's cell) | 100 | like for like | +63 | +21 | **-42 ± 15** | -2.9 |
| read 24 against read 22 (θ_duty 0.20 less 0.34) | 100 | of record | +128 | +149 | **+21 ± 22** | 0.9 |
| read 24 against read 22 (θ_duty 0.20 less 0.34) | 100 | with the reservation | +94 | +102 | **+8 ± 17** | 0.5 |
| read 24 against read 22 (θ_duty 0.20 less 0.34) | 100 | like for like | +60 | +21 | **-40 ± 15** | -2.7 |

## AB4.6. Across the three thresholds: what the careful lose, and where the level saving stands

| θ_duty | the careful population's slot: cell − world 3 of record (paired by seed) | … with the reservation | … income in good standing | the careful failed member from its failure on: cell − world 3 | conduct M at 0.1 on 1 in 4: behind the careful beside, of record | its level saving of record (ratio of means) | its slots suspended at least once |
|---|---|---|---|---|---|---|---|
| 0.50 (of record) | 0 (the record) | 0 | 0 | 0 | 109 ± 22 | 0.61 ± 0.11 | 0.13 / careful 0.12 |
| 0.34 | -3 ± 5 | -5 ± 5 | -1 ± 2 | +8 ± 6 | 128 ± 21 | 0.74 ± 0.12 | 0.21 / careful 0.13 |
| 0.20 | -79 ± 12 | -91 ± 11 | -17 ± 4 | -68 ± 12 | 149 ± 20 | 1.14 ± 0.16 | 0.59 / careful 0.34 |

The reviewer's relation (AB4.6): a cheaper model stops paying where its extra failures (0.95 q a test beyond the careful's 0.05) cost what it saves, so at the line the careful lose, by their own failures, 0.05 ÷ (0.95 q) of what the model would save. It is a relation between the cost of a failure and the line, not a read; the rows above are the measured pairs it is set against.

## Read 25. Conduct M at 0.1 with its claims set by the case, on every slot — world 3's cell, seeds 21–120, read as read 18 was, and against read 18 by seed

Every slot of the world follows the conduct: as a member a claim where the case's hash falls under the dose (the same cases for every slot of the seed, at every seat), careful at the others and on probation. Each row a seed: the all-careful's slot less the population's; then the population against read 18's by seed.

| read | seeds | slots a seed: population / all-careful | **all-careful − population, of record** (SE from nothing) | temptation | **with the reservation** | temptation | like for like (reported) | the population's slot: of record / with the reservation | suspended at least once (share): population / all-careful | member reviews a slot: population / all-careful | audit seats a slot: population / all-careful |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 18: M at 0.1 on every slot (claims drawn at each review) | 100 | 39.6 / 39.5 | **+13 ± 10** (1.3) | 1.5 ± 0.4 | **-13 ± 11** (-1.2) | 0.5 ± 0.4 | -129 ± 9 | 889 / 1042 | 0.13 / 0.12 | 97.3 / 87.9 | 36.2 / 35.8 |
| **25: M at 0.1 on every slot, the claims set by the case** | 100 | 39.5 / 39.5 | **+3 ± 9** (0.3) | 1.1 ± 0.3 | **-33 ± 10** (-3.4) | -0.1 ± 0.3 | -142 ± 10 | 899 / 1062 | 0.13 / 0.12 | 97.4 / 87.9 | 35.6 / 35.8 |

| read | what the claims spared a slot | the care on all its reviews as a member | claims a slot | **the population's level saving, the ratio of the seeds' means: of record / with the reservation / like for like** | the mean of the seeds' ratios | wrong first approvals of real bad work a slot (paid) |
|---|---|---|---|---|---|---|
| 18 | 27.9 ± 0.4 | 278 ± 4 | 9.8 ± 0.1 | **0.15 ± 0.04 / 0.05 ± 0.04 / -0.35 ± 0.03** | 0.16 ± 0.04 / 0.08 ± 0.04 / -0.33 ± 0.03 | 1.51 (0.19) |
| **25** | 29.8 ± 0.5 | 281 ± 4 | 10.3 ± 0.2 | **0.12 ± 0.03 / -0.01 ± 0.03 / -0.38 ± 0.03** | 0.12 ± 0.03 / 0.01 ± 0.03 / -0.36 ± 0.03 | 1.51 (0.65) |

**The world's side, paired by seed** (the population's less the all-careful's):

| measure | read 18 | read 25 | the all-careful | **read 18 − all-careful** | **read 25 − all-careful** | **read 25 − read 18** (SE from nothing) |
|---|---|---|---|---|---|---|
| standing false approvals a run | 7.4 | 25.7 | 2.5 | +4.9 ± 0.3 | +23.2 ± 0.6 | **+18.3 ± 0.7** (25.3) |
| the leak, ‰ of bad deliveries | 14.6 | 50.6 | 4.8 | +9.9 ± 0.7 | +45.9 ± 1.2 | **+36.0 ± 1.4** (26.0) |
| the system overhead a vested task | 14.44 | 14.32 | 11.88 | +2.56 ± 0.23 | +2.44 ± 0.24 | **-0.12 ± 0.32** (-0.4) |
| the cost of truth a run | 4219 | 4161 | 2968 | +1251 ± 118 | +1193 ± 109 | **-58 ± 155** (-0.4) |
| departures a run | 18.1 | 18.2 | 16.7 | +1.4 ± 0.2 | +1.5 ± 0.2 | **+0.1 ± 0.2** (0.2) |
| arrivals a run | 19.6 | 19.5 | 19.5 | +0.1 ± 0.1 | +0.1 ± 0.1 | **-0.1 ± 0.1** (-0.9) |
| P_t at the end | 17.7 | 17.5 | 14.8 | +2.9 ± 0.3 | +2.7 ± 0.3 | **-0.2 ± 0.4** (-0.5) |

**The members' side, read 25 against read 18 by seed** (the population's slot):

| measure | read 18 | read 25 | **read 25 − read 18** (SE) |
|---|---|---|---|
| the slot's lifetime of record | 889 | 899 | **+11 ± 10** (1.1) |
| … with the reservation | 1042 | 1062 | **+19 ± 11** (1.7) |
| … income in good standing | 707 | 720 | **+13 ± 10** (1.2) |
| good ticks a slot | 537 | 539 | **+2 ± 3** (0.6) |
| slots suspended at least once (share) | 0.132 | 0.129 | **-0.003 ± 0.006** (-0.4) |
| suspensions a slot | 0.139 | 0.135 | **-0.004 ± 0.007** (-0.5) |
| member reviews a slot | 97.3 | 97.4 | **+0.1 ± 1.7** (0.1) |
| audit seats a slot | 36.2 | 35.6 | **-0.7 ± 0.7** (-1.0) |
| claims a slot | 9.8 | 10.3 | **+0.5 ± 0.2** (2.5) |
| what the claims spared | 27.9 | 29.8 | **+1.8 ± 0.7** (2.7) |
| wrong first approvals of real bad work a slot | 1.51 | 1.51 | **-0.00 ± 0.03** (-0.1) |
| … that stay paid | 0.19 | 0.65 | **+0.46 ± 0.02** (25.2) |

| population, as a member | wrong first approvals of real bad work over the real bad work reviewed first | planted bad share of the first reviews |
|---|---|---|
| read 18 | 0.148 ± 0.002 | 0.124 ± 0.004 |
| read 25 | 0.146 ± 0.002 | 0.129 ± 0.004 |
| the all-careful | 0.050 ± 0.001 | 0.069 ± 0.001 |

## Against the expectations stated before the run (AB6, AB7)

- MET — read 20: suspensions a slot 0.13 to 0.19: 0.15.
- MET — read 20: 12 to 17 slots in 100 suspended at least once: 13.
- MET — read 20: arrivals admitted within the run 86 to 89 in 100: 88.
- MET — read 20: a slot's lifetime of record between 25 under world 3's and 10 over at the point value: -3 ± 5 by seed.
- MET — read 20: a leak of 4.0 to 5.6 in a thousand: 4.7.
- MET — read 21: between 7 and 12 claims a failed slot (read 17's 15.6): 10.7.
- MISSED — read 21: suspensions a failed slot from the failure on 0.60 to 0.90 for the conduct: 0.43.
- MISSED — read 21: … 0.22 to 0.32 for the careful failed slots: 0.06.
- MISSED — read 21: the conduct behind the careful failed slots by 40 to 160 real of record from the first failure on: +33 ± 22.
- MET — read 21: with the reservation between 20 ahead and 90 behind (the sign not called): -11 ± 20.
- MISSED — read 21: by seed worse off than read 17's conduct by 20 to 140 real of record (the gap from the failure on, read 21 less read 17): +7 ± 12.
- MET — read 22: 18 to 28 of the conduct's slots in 100 suspended at least once: 21.
- MET — read 22: 12 to 17 of the careful beside: 13.
- MET — read 22: behind by 110 to 180 real of record: +128 ± 21.
- MET — read 22: a level saving of 0.65 to 0.95 of record: 0.74 ± 0.12.
- MET — read 23: suspensions a slot 0.36 to 0.56: 0.38.
- MET — read 23: 30 to 45 slots in 100 suspended at least once: 33.
- MISSED — read 23: good ticks a slot 410 to 480 (world 3's 550): 484 (550).
- MET — read 23: arrivals admitted within the run 74 to 85 in 100: 80.
- MISSED — read 23: the way back from a member's suspension to a readmission 350 to 520 ticks from the suspension: 231 (n = 165).
- MET — read 23: a slot's lifetime of record between level with world 3's and 80 under it: -79 ± 12 by seed.
- MISSED — read 23: a careful member that fails ends 80 to 250 real lower from the failure on than in world 3's cell: -68 ± 12 (cell − world 3).
- MET — read 23: a leak no more than 1 in a thousand above world 3's: -0.9 ± 0.3.
- MET — read 23: an overhead of 11.9 to 13.6: 12.43.
- MET — read 24: 50 to 70 of the conduct's slots in 100 suspended at least once: 59.
- MET — read 24: 30 to 45 of the careful beside: 34.
- MISSED — read 24: between 38 and 56 reviews as a member in a life (read 9's 75.4): 56.1.
- MET — read 24: behind by 80 to 220 real of record: +149 ± 20.
- MET — read 24: a level saving of 0.8 to 1.6 of record (the side of 0.9 not called): 1.14 ± 0.16.
- MET — read 25: the leak 40 to 120 in a thousand bad deliveries (read 18's 14.6): 50.6.
- MET — read 25: the standing false approvals 20 to 60 a run (read 18's 7.4): 25.7.
- MET — read 25: a slot within 30 real of read 18's of record: +11 ± 10 by seed.
- MET — read 25: as many slots suspended as read 18, within 4 in 100: -0.3 ± 0.6.

**25 of 33 met.**

## Refuted, or shown, each apart

- *With the suspension at the second failure, a claim costs something while the earned seats are lost*: shown if read 21's conduct is behind the careful failed slots by two standard errors of record, from the first failure on; refuted if it is within one standard error of nothing, or ahead. It is +33 ± 22 (1.5 SE). **Neither.**
- *The suspension at the second failure costs the careful nothing that a read can see*: refuted if read 20's slot ends below world 3's by two standard errors of record, by seed; shown if it is within one standard error of it, or above. Cell − world 3 is -3 ± 5 (-0.6 SE). **Shown.**
- *The suspension at the second failure holds a model that spares nine tenths at a dose of 0.1*: shown if read 22's level saving is above 0.9 by two standard errors of record; refuted if it is under 0.9 at the point value. It is 0.74 ± 0.12 (-1.4 SE from 0.9). **Refuted.**
- *The suspension at the first failure, with the way back as built, holds that model at that dose*: the same condition on read 24. It is 1.14 ± 0.16 (+1.5 SE from 0.9). **Neither.**
- *The suspension at the first failure, with the way back as built, costs the careful population a part of its lifetime*: shown if read 23's slot ends below world 3's by two standard errors of record, by seed; refuted if it is within one standard error of it, or above. Cell − world 3 is -79 ± 12 (-6.8 SE). **Shown.**
- *When every member misses the same deliveries, the buyers get several times what read 18 has*: shown if the leak is at least twice read 18's at the point value and above it by two standard errors, by seed; refuted if it is within two standard errors of read 18's. The leak is 50.6 against read 18's 14.6 (3.46 times), above it by +36.0 ± 1.4 by seed (26.0 SE). **Shown.**

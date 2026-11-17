# Addenda 18–19: the record's three readings and the three reads without training (November 17, 2026; a18/launch.sh at f16e1ffee)

## The reruns at f16e1ffee against the record (W3's counts and W2's tallies need per-slot readings the record does not carry; the worlds of reads 2, 4, 9 and 11 and the all-careful of worlds 3 and 4 run again whole — nothing collected anew)

| world | seeds shared | row columns differing | per-slot keys of the record differing (slots compared) |
|---|---|---|---|
| read 2: conduct M at 0.1, world 4's cell | 100 | 0 | 0 (3960) |
| read 4: conduct M at 0.3, world 4's cell | 60 | 0 | 0 (2375) |
| read 9: conduct M at 0.1, world 3's cell | 100 | 0 | 0 (3959) |
| read 11: conduct M at 0.1 on 3 slots in 4, world 4's cell | 60 | 0 | 0 (2374) |
| the all-careful of world 3: arm 1, the weight of record (21–120) | 100 | 0 | 0 (3947) |
| the all-careful of world 4: arm 1, the weight doubled (21–120) | 100 | 0 | 0 (3960) |

## Y3.2. A claim's cost by the state of the earned seats — the failed slots' gap from the first failure on against their claims with the seats held and with them lost (reads 12, 13 and 14)

The gap is the careful failed slots' lifetime from the first failure on less the conduct's failed slots' (positive: the conduct behind), on the three lifetimes; the claims are the conduct's per failed slot after the first failure, split by the engine's `panel_eligible` at the claim (held / lost). Conduct F at 0.3 (240 seeds), conduct G at 0.3 (240; no claim with the seats held by construction) and conduct F at 1.0 (120) pooled. By the seeds: each seed's means, one row a seed and read, least squares of the gap on the two claim counts; by the slots: each failed conduct slot against the careful failed slots' mean of its seed. The fit with no intercept is the reviewer's form (a cost for each claim in each state); the fit with an intercept reads what a marked record loses with no claim at all. Standard errors homoskedastic.

| fit | lifetime | rows | **a claim with the seats held, no intercept** | **a claim with the seats lost, no intercept** | intercept | held, with the intercept | lost, with the intercept | R² (with the intercept) |
|---|---|---|---|---|---|---|---|---|
| by the seeds, the three reads pooled | of record | 600 | **2.4 ± 2.4** | **4.4 ± 0.7** | +60 ± 13 | -1.1 ± 2.5 | 1.9 ± 0.9 | 0.01 |
| by the seeds, the three reads pooled | with the reservation | 600 | **4.5 ± 2.2** | **2.0 ± 0.7** | +35 ± 12 | 2.4 ± 2.3 | 0.6 ± 0.8 | 0.00 |
| by the seeds, the three reads pooled | like for like | 598 | **-1.3 ± 1.7** | **3.4 ± 0.5** | +34 ± 9 | -3.3 ± 1.8 | 2.0 ± 0.6 | 0.02 |
| by the seeds, reads 12 and 14 (the reviewer's pair) | of record | 360 | **1.0 ± 2.2** | **5.1 ± 0.7** | +193 ± 17 | -15.9 ± 2.4 | 0.0 ± 0.7 | 0.11 |
| by the seeds, reads 12 and 14 (the reviewer's pair) | with the reservation | 360 | **3.4 ± 1.9** | **2.5 ± 0.6** | +116 ± 16 | -6.8 ± 2.3 | -0.5 ± 0.7 | 0.03 |
| by the seeds, reads 12 and 14 (the reviewer's pair) | like for like | 359 | **-0.6 ± 1.6** | **3.0 ± 0.5** | +129 ± 13 | -12.0 ± 1.8 | -0.3 ± 0.6 | 0.11 |
| by the seeds, reads 12 and 13 | of record | 480 | **3.3 ± 2.9** | **3.4 ± 1.4** | +93 ± 18 | -0.2 ± 2.9 | -5.4 ± 2.2 | 0.01 |
| by the seeds, reads 12 and 13 | with the reservation | 480 | **5.6 ± 2.6** | **1.2 ± 1.3** | +59 ± 17 | 3.4 ± 2.6 | -4.4 ± 2.0 | 0.01 |
| by the seeds, reads 12 and 13 | like for like | 478 | **-3.4 ± 1.9** | **7.2 ± 0.9** | -7 ± 13 | -3.1 ± 2.0 | 7.9 ± 1.5 | 0.05 |
| by the seeds, read 13 alone (the lost state alone) | of record | 240 | — | **0.9 ± 2.1** | +30 ± 26 | — | -2.5 ± 3.7 | 0.00 |
| by the seeds, read 13 alone (the lost state alone) | with the reservation | 240 | — | **-0.7 ± 1.9** | +24 ± 24 | — | -3.5 ± 3.4 | 0.00 |
| by the seeds, read 13 alone (the lost state alone) | like for like | 239 | — | **5.0 ± 1.5** | -52 ± 18 | — | 10.9 ± 2.5 | 0.07 |
| by the slots, the three reads pooled | of record | 3207 | **-2.3 ± 1.0** | **-0.4 ± 0.4** | +145 ± 8 | -7.4 ± 1.0 | -4.3 ± 0.4 | 0.06 |
| by the slots, the three reads pooled | with the reservation | 3207 | **1.0 ± 0.9** | **-0.4 ± 0.3** | +80 ± 7 | -1.9 ± 0.9 | -2.5 ± 0.4 | 0.02 |
| by the slots, the three reads pooled | like for like | 2815 | **-6.3 ± 0.8** | **2.3 ± 0.3** | +57 ± 7 | -8.3 ± 0.8 | 0.8 ± 0.3 | 0.04 |
| by the slots, reads 12 and 14 (the reviewer's pair) | of record | 1944 | **-3.1 ± 0.9** | **0.5 ± 0.3** | +264 ± 8 | -13.7 ± 0.8 | -5.4 ± 0.3 | 0.24 |
| by the slots, reads 12 and 14 (the reviewer's pair) | with the reservation | 1944 | **0.4 ± 0.8** | **0.2 ± 0.3** | +154 ± 8 | -5.8 ± 0.8 | -3.2 ± 0.3 | 0.07 |
| by the slots, reads 12 and 14 (the reviewer's pair) | like for like | 1704 | **-5.9 ± 0.7** | **2.0 ± 0.3** | +128 ± 9 | -11.1 ± 0.8 | -0.8 ± 0.3 | 0.11 |
| by the slots, reads 12 and 13 | of record | 2527 | **-4.9 ± 1.3** | **-4.5 ± 0.7** | +168 ± 9 | -11.7 ± 1.3 | -12.9 ± 0.8 | 0.13 |
| by the slots, reads 12 and 13 | with the reservation | 2527 | **-1.5 ± 1.2** | **-2.9 ± 0.6** | +100 ± 9 | -5.5 ± 1.2 | -7.8 ± 0.8 | 0.05 |
| by the slots, reads 12 and 13 | like for like | 2215 | **-6.4 ± 0.9** | **4.9 ± 0.5** | +32 ± 8 | -7.7 ± 0.9 | 3.3 ± 0.6 | 0.04 |
| by the slots, read 13 alone (the lost state alone) | of record | 1263 | — | **-5.7 ± 1.1** | +62 ± 14 | — | -9.2 ± 1.4 | 0.03 |
| by the slots, read 13 alone (the lost state alone) | with the reservation | 1263 | — | **-3.8 ± 1.1** | +28 ± 13 | — | -5.4 ± 1.3 | 0.01 |
| by the slots, read 13 alone (the lost state alone) | like for like | 1111 | — | **4.4 ± 0.8** | -18 ± 11 | — | 5.4 ± 1.0 | 0.03 |

**The two states cannot be parted by a fit over the slots or the seeds within the reads.** Within a read a failed slot's claim counts measure how long it lived after its failure as much as its conduct — a slot that made more claims stayed longer and earned more from the failure on — so with an intercept the slopes read negative (reads 12 and 14 by the slots: −14 a held claim, −5 a lost one, of record) and without one they read the blend of that selection and the reads' designs. What parts the states is the design: conduct G makes no claim with the seats held. So the costs are read from the reads' means, as the reviewer's (R) did, with their errors from a bootstrap over the seeds (2,000 draws):

| lifetime | **a claim held, from reads 12 and 14** | **a claim lost, from reads 12 and 14** | a claim lost, read 13's own | a claim held, read 12 with read 13's lost | a claim held, read 14 with read 13's lost |
|---|---|---|---|---|---|
| of record | **14.1 ± 4.5** | **3.9 ± 1.3** | 2.6 ± 2.6 | 16.4 ± 5.5 | 21.0 ± 14.6 |
| with the reservation | **12.8 ± 3.8** | **1.3 ± 1.1** | 0.6 ± 2.4 | 14.0 ± 4.9 | 16.6 ± 13.2 |
| like for like | **16.2 ± 3.4** | **-0.4 ± 1.0** | 2.2 ± 1.8 | 11.6 ± 3.8 | 2.5 ± 9.9 |

The means behind them: of record — read 12 95 on 4.5 held / 8.1 lost a failed slot, read 13 15 on 5.9 lost, read 14 168 on 4.9 / 25.7; with the reservation — read 12 69 on 4.5 held / 8.1 lost a failed slot, read 13 4 on 5.9 lost, read 14 96 on 4.9 / 25.7; like for like — read 12 70 on 4.5 held / 8.1 lost a failed slot, read 13 13 on 5.9 lost, read 14 67 on 4.9 / 25.7.
- read 12: across its failed slots the claims after the failure and the ticks from the failure to the exit are correlated at +0.64 (1264 slots) — the survival the within-read fits read.
- read 13: across its failed slots the claims after the failure and the ticks from the failure to the exit are correlated at +0.56 (1263 slots) — the survival the within-read fits read.
- read 14: across its failed slots the claims after the failure and the ticks from the failure to the exit are correlated at +0.51 (680 slots) — the survival the within-read fits read.

## W2. The level saving — the identity as the engine counts what a claim spares, and the level savings from the tallies

**The identity holds as the engine counts.** A careful review's cost is drawn uniform on {2, 3} credits (times the calibration knob, 1 in every run of record) at every seat alike — `_care_cost` reads no seat — and the claim buys and is reimbursed exactly that draw, as the careful review would have been (an underfunded review pays what the wallet can buy, for both alike); the private benefit is the cost claimed times the temptation, real at the claim's tick; so at a temptation of 1 what a claim spares is the cost of care of that review and nothing else — not the fee, not the bond, not the verdict's consequence — and over a life the claims spare the conduct a share of the cost of care on all its reviews as a member equal to the share of those reviews it claimed, q in expectation (the coin is a review's own, independent of the cost's draw). The level saving is therefore x = q · T* up to the coin's noise, with T* the level temptation read as §112–§115 read it. What the identity does not carry: a claim on good work gives the right verdict where the careful's own review errs one time in twenty, so a conduct's claims improve its record a little relative to the careful's at that seat; that is in the loss, not in the saving. The tallies' figure below is the exact one: by seed, the careful slots' lifetime less the conduct's plus what the claims spared, over the care the conduct spent and claimed as a member (its member reviews' care, real); like for like the careful's income in good standing scaled to the conduct's good ticks less the conduct's own, over the same.

| read | seeds | **level saving from the tallies, the mean of the seeds' ratios: of record** | **with the reservation** | **like for like** | the tallies as a ratio of the seeds' means: of record / with the reservation / like for like | the identity's q·T*: of record / with the reservation / like for like (the reviewer's) | claims as a member over member reviews (q) | the cost the claims spared over the member care (q) | member reviews a slot; claims as a member |
|---|---|---|---|---|---|---|---|---|---|
| read 9: conduct M at 0.1, world 3's cell | 100 | **0.83 ± 0.13** | **0.69 ± 0.10** | **0.47 ± 0.07** | 0.61 ± 0.11 / 0.52 ± 0.09 / 0.38 ± 0.06 | 0.62 / 0.52 / 0.38 (0.62 / 0.52 / 0.38) | 0.099 ± 0.001 | 0.098 ± 0.001 | 75.4; 7.5 |
| read 2: conduct M at 0.1, world 4's cell | 100 | **0.95 ± 0.13** | **0.80 ± 0.11** | **0.58 ± 0.07** | 0.75 ± 0.12 / 0.65 ± 0.10 / 0.52 ± 0.07 | 0.76 / 0.66 / 0.52 (0.76 / 0.66 / 0.52) | 0.099 ± 0.001 | 0.099 ± 0.001 | 75.3; 7.4 |
| read 1: conduct M at 0.1, world 1's cell (the pin) | 100 | (the record carries no tallies) | | | | 0.55 / 0.51 / 0.44 (0.55 / 0.51 / 0.44) | | | |
| read 3: conduct M at 0.1, world 6's cell (arm 4) | 100 | (the record carries no tallies) | | | | 0.03 / 0.10 / 0.20 (0.03 / 0.10 / 0.20) | | | |
| read 11: conduct M at 0.1 on 3 slots in 4, world 4's cell | 60 | **0.80 ± 0.20** | **0.78 ± 0.17** | **0.79 ± 0.15** | 0.70 ± 0.17 / 0.69 ± 0.15 / 0.72 ± 0.13 | 0.69 / 0.68 / 0.71 (0.69 / 0.68 / 0.71) | 0.101 ± 0.001 | 0.101 ± 0.001 | 87.1; 8.8 |
| read 4: conduct M at 0.3, world 4's cell | 60 | **3.06 ± 0.24** | **2.45 ± 0.17** | **1.69 ± 0.09** | 2.67 ± 0.19 / 2.18 ± 0.15 / 1.63 ± 0.09 | 2.66 / 2.18 / 1.64 (2.67 / 2.19 / 1.65) | 0.300 ± 0.002 | 0.301 ± 0.002 | 62.0; 18.6 |
| read 15: conduct M at 0.5, world 3's cell | 100 | **3.62 ± 0.19** | **2.70 ± 0.13** | **1.85 ± 0.07** | 3.29 ± 0.16 / 2.52 ± 0.11 / 1.80 ± 0.07 | 3.30 / 2.53 / 1.83 | 0.499 ± 0.002 | 0.500 ± 0.002 | 54.1; 27.0 |
| read 16: conduct M at 1.0, world 3's cell | 100 | **10.38 ± 0.39** | **6.63 ± 0.26** | **2.84 ± 0.09** | 9.59 ± 0.39 / 6.15 ± 0.25 / 2.75 ± 0.09 | 9.59 / 6.15 / 2.82 | 1.000 ± 0.000 | 1.000 ± 0.000 | 28.1; 28.1 |

The first three columns are what W2 asked — by seed, the share, as a mean with its error; the fourth is the same tallies as a ratio of the seeds' means, the form the level temptation has taken since §112, which the identity's q·T* must match (and does, to the coin: the claims' share of the member reviews reads q to three figures). The mean of the seeds' ratios runs a fifth to a third above it on every read because a seed's loss and its claims are negatively correlated — the conduct's slots that live longest claim most and lose least — so the seeds with few claims carry large ratios; it is the honest answer to the question as put, and the ratio of means the one to set against the identity.

## W3. Three counts from the worlds on record (reads 2, 4, 9 and 11 run again whole at f16e1ffee; the conduct's slots, the careful slots beside them in the same world and seeds, and the all-careful population of the same world and seeds; the mean for a slot, ± the standard error over the seeds)

### W3.1. The reviews made as a member in a life, by seat, and the planted cases among them by kind

The engine's seat kinds: a first review of an unrevised submission (initial), the same reviewer resumed on a revision (resumed; none in these populations), the audit seat, the third seat (an audit-role challenge's), the appeal panel and the dispute panel. Reviews given on probation are beside; a review in neither standing (`down`: a seat completed by a slot whose standing had just changed) is counted apart.

| read | group | **member reviews a slot** | initial | audit | third | appeal | dispute | resumed | planted among them: bad / good | … at the initial seat: bad / good | … at the audit seat: bad / good | … at the panels (third, appeal, dispute): bad / good | reviews on probation a slot | down |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| read 9: conduct M at 0.1, world 3's cell | the conduct's slots | **75.4 ± 1.9** | 46.7 ± 1.2 | 24.1 ± 1.2 | 2.0 ± 0.1 | 2.5 ± 0.1 | 0.2 ± 0.0 | 0.0 | 8.3 ± 0.3 / 1.9 ± 0.1 | 3.6 / 1.1 | 2.2 / 0.5 | 2.5 / 0.3 | 27.1 ± 1.1 | 0.0 |
|  | the careful slots beside | **92.2 ± 1.1** | 44.8 ± 0.6 | 39.6 ± 0.6 | 3.2 ± 0.1 | 4.2 ± 0.1 | 0.3 ± 0.0 | 0.0 | 11.0 ± 0.2 / 2.5 ± 0.1 | 3.3 / 1.1 | 3.6 / 1.0 | 4.1 / 0.4 | 27.4 ± 0.4 | 0.0 |
|  | the all-careful population | **87.9 ± 0.7** | 44.9 ± 0.4 | 35.8 ± 0.3 | 3.0 ± 0.0 | 4.0 ± 0.1 | 0.3 ± 0.0 | 0.0 | 10.1 ± 0.1 / 2.3 ± 0.0 | 3.1 / 1.0 | 3.3 / 0.8 | 3.7 / 0.4 | 27.7 ± 0.3 | 0.0 |
| read 2: conduct M at 0.1, world 4's cell | the conduct's slots | **75.3 ± 1.6** | 46.8 ± 1.1 | 24.0 ± 0.9 | 1.9 ± 0.1 | 2.5 ± 0.1 | 0.2 ± 0.0 | 0.0 | 8.0 ± 0.2 / 1.9 ± 0.1 | 3.4 / 1.1 | 2.2 / 0.6 | 2.4 / 0.2 | 26.4 ± 1.2 | 0.0 |
|  | the careful slots beside | **90.9 ± 1.1** | 44.7 ± 0.6 | 38.6 ± 0.6 | 3.2 ± 0.1 | 4.1 ± 0.1 | 0.3 ± 0.0 | 0.0 | 10.8 ± 0.2 / 2.4 ± 0.1 | 3.2 / 1.1 | 3.6 / 0.9 | 4.0 / 0.4 | 27.2 ± 0.4 | 0.0 |
|  | the all-careful population | **87.6 ± 0.8** | 44.7 ± 0.5 | 35.7 ± 0.4 | 2.9 ± 0.0 | 4.0 ± 0.1 | 0.3 ± 0.0 | 0.0 | 10.1 ± 0.1 / 2.2 ± 0.0 | 3.1 / 1.0 | 3.2 / 0.8 | 3.8 / 0.4 | 27.5 ± 0.3 | 0.0 |
| read 4: conduct M at 0.3, world 4's cell | the conduct's slots | **62.0 ± 2.2** | 51.6 ± 1.9 | 8.7 ± 0.6 | 0.7 ± 0.1 | 0.9 ± 0.1 | 0.1 ± 0.0 | 0.0 | 7.6 ± 0.5 / 2.2 ± 0.2 | 5.8 / 1.8 | 0.9 / 0.3 | 0.9 / 0.1 | 23.1 ± 1.4 | 0.0 |
|  | the careful slots beside | **109.0 ± 1.8** | 51.1 ± 1.0 | 48.1 ± 0.9 | 4.4 ± 0.1 | 5.1 ± 0.1 | 0.3 ± 0.0 | 0.0 | 15.9 ± 0.6 / 4.5 ± 0.3 | 5.5 / 1.8 | 4.8 / 2.0 | 5.6 / 0.6 | 23.2 ± 0.6 | 0.0 |
|  | the all-careful population | **87.1 ± 1.1** | 45.1 ± 0.6 | 34.9 ± 0.5 | 2.9 ± 0.1 | 4.0 ± 0.1 | 0.3 ± 0.0 | 0.0 | 10.0 ± 0.2 / 2.2 ± 0.0 | 3.1 / 1.0 | 3.2 / 0.8 | 3.7 / 0.4 | 27.1 ± 0.4 | 0.0 |
| read 11: conduct M at 0.1 on 3 slots in 4, world 4's cell | the conduct's slots | **87.1 ± 1.6** | 50.4 ± 0.9 | 30.8 ± 0.8 | 2.5 ± 0.1 | 3.2 ± 0.1 | 0.2 ± 0.0 | 0.0 | 11.0 ± 0.4 / 3.1 ± 0.2 | 4.7 / 1.6 | 3.0 / 1.1 | 3.3 / 0.4 | 24.7 ± 0.6 | 0.0 |
|  | the careful slots beside | **104.2 ± 3.6** | 44.8 ± 1.4 | 49.9 ± 2.6 | 4.1 ± 0.2 | 5.1 ± 0.3 | 0.3 ± 0.0 | 0.0 | 14.4 ± 0.7 / 3.5 ± 0.2 | 4.2 / 1.3 | 4.9 / 1.6 | 5.3 / 0.5 | 24.4 ± 1.2 | 0.0 |
|  | the all-careful population | **87.1 ± 1.1** | 45.1 ± 0.6 | 34.9 ± 0.5 | 2.9 ± 0.1 | 4.0 ± 0.1 | 0.3 ± 0.0 | 0.0 | 10.0 ± 0.2 / 2.2 ± 0.0 | 3.1 / 1.0 | 3.2 / 0.8 | 3.7 / 0.4 | 27.1 ± 0.4 | 0.0 |

### W3.2. From admission: the reviews of real tasks made as a member before the earned seats are first lost (the first wrong planted verdict on the record, by the driver's clock — the plant's closure) and before the first suspension; the shares of the slots that reach each

Over every slot the count is censored at the exit (a slot that never fails counts all its real member reviews); over the slots that reach the event it is the count before it. A failure on probation (an arrival's, before admission) puts the record's mark on before any member review, so such a slot reaches the first with 0.

| read | group | **real reviews as a member before the seats are first lost: every slot / the slots that reach it** | share that reach a failure | **real reviews as a member before the first suspension: every slot / the slots that reach it** | share that reach a suspension | member reviews of every kind before the first suspension, the slots that reach it |
|---|---|---|---|---|---|---|
| read 9: conduct M at 0.1, world 3's cell | the conduct's slots | **33.3 ± 1.0 / 29.5 ± 1.0** | 0.75 ± 0.01 | **63.1 ± 1.7 / 3.5 ± 1.5** | 0.13 ± 0.01 | 3.9 ± 1.6 |
|  | the careful slots beside | **51.7 ± 0.8 / 43.6 ± 0.9** | 0.54 ± 0.01 | **76.2 ± 0.9 / 0.2 ± 0.2** | 0.12 ± 0.00 | 0.3 ± 0.2 |
|  | the all-careful population | **51.1 ± 0.6 / 41.5 ± 0.9** | 0.52 ± 0.01 | **73.3 ± 0.6 / 0.2 ± 0.1** | 0.12 ± 0.00 | 0.2 ± 0.2 |
| read 2: conduct M at 0.1, world 4's cell | the conduct's slots | **33.7 ± 0.9 / 30.6 ± 1.3** | 0.74 ± 0.02 | **63.3 ± 1.4 / 2.8 ± 1.0** | 0.13 ± 0.01 | 3.2 ± 1.1 |
|  | the careful slots beside | **50.6 ± 0.7 / 41.7 ± 0.8** | 0.56 ± 0.01 | **75.4 ± 0.8 / 0.0 ± 0.0** | 0.12 ± 0.01 | 0.0 ± 0.0 |
|  | the all-careful population | **50.8 ± 0.6 / 42.5 ± 0.8** | 0.52 ± 0.01 | **72.8 ± 0.7 / 0.2 ± 0.2** | 0.12 ± 0.01 | 0.2 ± 0.2 |
| read 4: conduct M at 0.3, world 4's cell | the conduct's slots | **19.6 ± 0.9 / 18.6 ± 0.9** | 0.86 ± 0.01 | **50.6 ± 1.7 / 20.2 ± 3.1** | 0.21 ± 0.02 | 23.4 ± 3.5 |
|  | the careful slots beside | **51.2 ± 1.2 / 44.4 ± 1.2** | 0.65 ± 0.01 | **86.4 ± 1.0 / 0.4 ± 0.4** | 0.12 ± 0.01 | 0.4 ± 0.4 |
|  | the all-careful population | **50.3 ± 0.8 / 41.1 ± 1.0** | 0.54 ± 0.01 | **72.3 ± 0.9 / 0.4 ± 0.3** | 0.13 ± 0.01 | 0.4 ± 0.3 |
| read 11: conduct M at 0.1 on 3 slots in 4, world 4's cell | the conduct's slots | **33.9 ± 0.8 / 32.5 ± 0.8** | 0.80 ± 0.01 | **71.5 ± 1.2 / 1.3 ± 0.5** | 0.12 ± 0.01 | 1.5 ± 0.5 |
|  | the careful slots beside | **51.6 ± 1.9 / 45.6 ± 2.5** | 0.66 ± 0.02 | **84.6 ± 2.9 / 0.0 ± 0.0** | 0.12 ± 0.01 | 0.0 ± 0.0 |
|  | the all-careful population | **50.3 ± 0.8 / 41.1 ± 1.0** | 0.54 ± 0.01 | **72.3 ± 0.9 / 0.4 ± 0.3** | 0.13 ± 0.01 | 0.4 ± 0.3 |

### W3.3. The wrong approvals of real bad work given in a life as a first reviewer, and how many were paid

A first review's F on real work whose truth is unfulfilled; paid where the review vested and its fee reached the slot, overturned where its bond was forfeited (an audit's or a panel's overturn), open where the case had not settled by the run's end.

| read | group | **wrong first approvals of real bad work a slot** | **paid** | overturned | open at the end | paid share of the settled | ratio to the careful slots beside (the conduct's) |
|---|---|---|---|---|---|---|---|
| read 9: conduct M at 0.1, world 3's cell | the conduct's slots | **1.45 ± 0.05** | **0.15 ± 0.01** | 1.30 ± 0.05 | 0.00 ± 0.00 | 0.10 | 2.27 ± 0.11 |
|  | the careful slots beside | **0.64 ± 0.02** | **0.08 ± 0.01** | 0.56 ± 0.01 | 0.00 ± 0.00 | 0.12 |  |
|  | the all-careful population | **0.66 ± 0.01** | **0.06 ± 0.00** | 0.59 ± 0.01 | 0.00 ± 0.00 | 0.10 |  |
| read 2: conduct M at 0.1, world 4's cell | the conduct's slots | **1.48 ± 0.05** | **0.14 ± 0.01** | 1.33 ± 0.05 | 0.02 ± 0.00 | 0.10 | 2.28 ± 0.10 |
|  | the careful slots beside | **0.65 ± 0.02** | **0.07 ± 0.00** | 0.58 ± 0.01 | 0.00 ± 0.00 | 0.11 |  |
|  | the all-careful population | **0.68 ± 0.01** | **0.06 ± 0.00** | 0.61 ± 0.01 | 0.00 ± 0.00 | 0.09 |  |
| read 4: conduct M at 0.3, world 4's cell | the conduct's slots | **3.15 ± 0.12** | **0.23 ± 0.02** | 2.92 ± 0.12 | 0.00 ± 0.00 | 0.07 | 5.12 ± 0.26 |
|  | the careful slots beside | **0.62 ± 0.02** | **0.06 ± 0.01** | 0.56 ± 0.02 | 0.00 ± 0.00 | 0.10 |  |
|  | the all-careful population | **0.68 ± 0.02** | **0.06 ± 0.00** | 0.62 ± 0.02 | 0.00 ± 0.00 | 0.09 |  |
| read 11: conduct M at 0.1 on 3 slots in 4, world 4's cell | the conduct's slots | **1.46 ± 0.03** | **0.18 ± 0.01** | 1.28 ± 0.03 | 0.01 ± 0.00 | 0.12 | 2.34 ± 0.15 |
|  | the careful slots beside | **0.62 ± 0.04** | **0.07 ± 0.01** | 0.55 ± 0.03 | 0.00 ± 0.00 | 0.12 |  |
|  | the all-careful population | **0.68 ± 0.02** | **0.06 ± 0.00** | 0.62 ± 0.02 | 0.00 ± 0.00 | 0.09 |  |

## W4. Reads 15 and 16 — conduct M at 0.5 and at 1.0 in world 3's cell on seeds 21–120 (read 9, conduct M at 0.1, beside): the three lifetimes with their level temptations (read as P4 and Q4 were)

The conduct on 1 slot in 4; the gap is the careful slots beside less the conduct's (positive: the conduct behind), of record (the wallet's real wealth at the exit plus the benefit), with the reservation (0.8 real a tick from a departure to the run's end), like for like (the careful's good-standing income less the conduct's good-standing rate times the careful's good ticks); the level temptation 1 + gap / what the claims spared. Beside: the all-careful population of the same seeds.

| world / read | seeds | **of record** | temptation | **with the reservation** | temptation | **like for like** | temptation |
|---|---|---|---|---|---|---|---|
| read 9: conduct M at 0.1, world 3's cell | 100 | **+109 ± 22** (4.9) | 6.2 ± 1.1 | **+90 ± 19** (4.8) | 5.2 ± 1.0 | **+63 ± 14** (4.6) | 3.8 ± 0.7 |
| read 15: conduct M at 0.5, world 3's cell | 100 | **+420 ± 17** (24.6) | 6.6 ± 0.3 | **+304 ± 14** (22.0) | 5.1 ± 0.2 | **+284 ± 14** (20.3) | 3.7 ± 0.1 |
| read 16: conduct M at 1.0, world 3's cell | 100 | **+649 ± 16** (40.9) | 9.6 ± 0.4 | **+389 ± 12** (32.5) | 6.1 ± 0.3 | **+354 ± 15** (22.9) | 2.8 ± 0.1 |

### Both groups a slot, the lifetime lost for each claim, and the honest side

| world / read | conduct's slots: claims (as a member / on probation); benefit; suspensions; audit seats; good ticks | careful slots: suspensions; audit seats; good ticks | **lost for each claim: of record / with the reservation / like for like** | careful group − all-careful; FA; leak ‰; overhead (all-careful) |
|---|---|---|---|---|
| read 9: conduct M at 0.1, world 3's cell | 7.5 (7.5 / 0.0); 21.2; 0.13; 24.1; 531 | 0.13; 39.6; 552 | **14.7 ± 3.2 / 12.1 ± 2.7 / 8.4 ± 1.9** | +26 ± 10; 3.8; 7; 12.0 (2.5; 5; 11.9) |
| read 15: conduct M at 0.5, world 3's cell | 27.0 (27.0 / 0.0); 75.0; 0.44; 4.1; 400 | 0.13; 52.0; 569 | **15.6 ± 0.8 / 11.3 ± 0.6 / 10.5 ± 0.6** | +68 ± 13; 4.3; 9; 15.8 (2.5; 5; 11.9) |
| read 16: conduct M at 1.0, world 3's cell | 28.1 (28.1 / 0.0); 75.6; 0.78; 1.6; 233 | 0.13; 54.0; 601 | **23.1 ± 1.0 / 13.9 ± 0.7 / 12.6 ± 0.7** | +114 ± 12; 4.1; 8; 17.7 (2.5; 5; 11.9) |

### W3's three counts for reads 15 and 16 (read 9's rerun beside)

| read | group | **member reviews a slot** | initial | audit | third | appeal | dispute | resumed | planted among them: bad / good | … at the initial seat: bad / good | … at the audit seat: bad / good | … at the panels (third, appeal, dispute): bad / good | reviews on probation a slot | down |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| read 9: conduct M at 0.1, world 3's cell | the conduct's slots | **75.4 ± 1.9** | 46.7 ± 1.2 | 24.1 ± 1.2 | 2.0 ± 0.1 | 2.5 ± 0.1 | 0.2 ± 0.0 | 0.0 | 8.3 ± 0.3 / 1.9 ± 0.1 | 3.6 / 1.1 | 2.2 / 0.5 | 2.5 / 0.3 | 27.1 ± 1.1 | 0.0 |
|  | the careful slots beside | **92.2 ± 1.1** | 44.8 ± 0.6 | 39.6 ± 0.6 | 3.2 ± 0.1 | 4.2 ± 0.1 | 0.3 ± 0.0 | 0.0 | 11.0 ± 0.2 / 2.5 ± 0.1 | 3.3 / 1.1 | 3.6 / 1.0 | 4.1 / 0.4 | 27.4 ± 0.4 | 0.0 |
|  | the all-careful population | **87.9 ± 0.7** | 44.9 ± 0.4 | 35.8 ± 0.3 | 3.0 ± 0.0 | 4.0 ± 0.1 | 0.3 ± 0.0 | 0.0 | 10.1 ± 0.1 / 2.3 ± 0.0 | 3.1 / 1.0 | 3.3 / 0.8 | 3.7 / 0.4 | 27.7 ± 0.3 | 0.0 |
| read 15: conduct M at 0.5, world 3's cell | the conduct's slots | **54.1 ± 1.2** | 49.3 ± 1.0 | 4.1 ± 0.3 | 0.3 ± 0.0 | 0.4 ± 0.0 | 0.0 ± 0.0 | 0.0 | 6.9 ± 0.3 / 2.2 ± 0.1 | 6.1 / 2.0 | 0.4 / 0.1 | 0.4 / 0.0 | 21.7 ± 1.0 | 0.0 |
|  | the careful slots beside | **119.5 ± 1.8** | 56.6 ± 1.0 | 52.0 ± 0.7 | 5.2 ± 0.1 | 5.3 ± 0.1 | 0.4 ± 0.0 | 0.0 | 19.7 ± 0.6 / 6.0 ± 0.3 | 7.6 / 2.5 | 5.5 / 2.7 | 6.5 / 0.8 | 20.6 ± 0.5 | 0.0 |
|  | the all-careful population | **87.9 ± 0.7** | 44.9 ± 0.4 | 35.8 ± 0.3 | 3.0 ± 0.0 | 4.0 ± 0.1 | 0.3 ± 0.0 | 0.0 | 10.1 ± 0.1 / 2.3 ± 0.0 | 3.1 / 1.0 | 3.3 / 0.8 | 3.7 / 0.4 | 27.7 ± 0.3 | 0.0 |
| read 16: conduct M at 1.0, world 3's cell | the conduct's slots | **28.1 ± 0.6** | 26.2 ± 0.6 | 1.6 ± 0.1 | 0.1 ± 0.0 | 0.1 ± 0.0 | 0.0 ± 0.0 | 0.0 | 3.3 ± 0.1 / 1.1 ± 0.0 | 3.0 / 1.0 | 0.1 / 0.1 | 0.1 / 0.0 | 18.4 ± 1.1 | 0.0 |
|  | the careful slots beside | **136.6 ± 1.7** | 70.7 ± 1.0 | 54.0 ± 0.6 | 5.3 ± 0.1 | 6.1 ± 0.1 | 0.4 ± 0.0 | 0.0 | 23.4 ± 0.5 / 8.2 ± 0.2 | 11.0 / 3.7 | 5.5 / 3.5 | 6.8 / 0.9 | 16.3 ± 0.3 | 0.0 |
|  | the all-careful population | **87.9 ± 0.7** | 44.9 ± 0.4 | 35.8 ± 0.3 | 3.0 ± 0.0 | 4.0 ± 0.1 | 0.3 ± 0.0 | 0.0 | 10.1 ± 0.1 / 2.3 ± 0.0 | 3.1 / 1.0 | 3.3 / 0.8 | 3.7 / 0.4 | 27.7 ± 0.3 | 0.0 |

| read | group | **real reviews as a member before the seats are first lost: every slot / the slots that reach it** | share that reach a failure | **real reviews as a member before the first suspension: every slot / the slots that reach it** | share that reach a suspension | member reviews of every kind before the first suspension, the slots that reach it | **wrong first approvals of real bad work a slot: given / paid / overturned** | ratio to the careful beside |
|---|---|---|---|---|---|---|---|---|
| read 9: conduct M at 0.1, world 3's cell | the conduct's slots | **33.3 ± 1.0 / 29.5 ± 1.0** | 0.75 ± 0.01 | **63.1 ± 1.7 / 3.5 ± 1.5** | 0.13 ± 0.01 | 3.9 ± 1.6 | **1.45 ± 0.05 / 0.15 ± 0.01 / 1.30 ± 0.05** | 2.27 ± 0.11 |
|  | the careful slots beside | **51.7 ± 0.8 / 43.6 ± 0.9** | 0.54 ± 0.01 | **76.2 ± 0.9 / 0.2 ± 0.2** | 0.12 ± 0.00 | 0.3 ± 0.2 | **0.64 ± 0.02 / 0.08 ± 0.01 / 0.56 ± 0.01** |  |
|  | the all-careful population | **51.1 ± 0.6 / 41.5 ± 0.9** | 0.52 ± 0.01 | **73.3 ± 0.6 / 0.2 ± 0.1** | 0.12 ± 0.00 | 0.2 ± 0.2 | **0.66 ± 0.01 / 0.06 ± 0.00 / 0.59 ± 0.01** |  |
| read 15: conduct M at 0.5, world 3's cell | the conduct's slots | **14.3 ± 0.5 / 13.5 ± 0.5** | 0.93 ± 0.01 | **42.8 ± 1.0 / 35.8 ± 1.8** | 0.41 ± 0.02 | 43.4 ± 2.2 | **4.59 ± 0.10 / 0.29 ± 0.02 / 4.30 ± 0.10** | 7.27 ± 0.24 |
|  | the careful slots beside | **51.8 ± 0.8 / 49.1 ± 1.0** | 0.70 ± 0.01 | **92.1 ± 1.1 / 1.1 ± 0.4** | 0.12 ± 0.01 | 1.3 ± 0.5 | **0.63 ± 0.02 / 0.05 ± 0.00 / 0.58 ± 0.01** |  |
|  | the all-careful population | **51.1 ± 0.6 / 41.5 ± 0.9** | 0.52 ± 0.01 | **73.3 ± 0.6 / 0.2 ± 0.1** | 0.12 ± 0.00 | 0.2 ± 0.2 | **0.66 ± 0.01 / 0.06 ± 0.00 / 0.59 ± 0.01** |  |
| read 16: conduct M at 1.0, world 3's cell | the conduct's slots | **8.8 ± 0.3 / 8.6 ± 0.3** | 0.97 ± 0.01 | **23.0 ± 0.6 / 23.1 ± 0.8** | 0.74 ± 0.02 | 27.9 ± 0.9 | **4.55 ± 0.11 / 0.27 ± 0.02 / 4.28 ± 0.11** | 6.50 ± 0.21 |
|  | the careful slots beside | **48.6 ± 0.8 / 46.3 ± 0.9** | 0.77 ± 0.01 | **103.6 ± 1.2 / 0.8 ± 0.4** | 0.12 ± 0.01 | 1.1 ± 0.5 | **0.70 ± 0.01 / 0.05 ± 0.00 / 0.65 ± 0.01** |  |
|  | the all-careful population | **51.1 ± 0.6 / 41.5 ± 0.9** | 0.52 ± 0.01 | **73.3 ± 0.6 / 0.2 ± 0.1** | 0.12 ± 0.00 | 0.2 ± 0.2 | **0.66 ± 0.01 / 0.06 ± 0.00 / 0.59 ± 0.01** |  |

**Read 16's hundredth.** Of the conduct's slots that make a hundred reviews as a member or more — **0 slots over the hundred seeds** (0.00 a seed of 9.8 conduct slots) — 0 were suspended before their hundredth member review, 0 at some point. The set is empty because a claim at every member review stops a slot well short of a hundred: over the 981 conduct slots the member reviews in a life are 27.6 a slot, the most 96, 8 in 100 reach fifty; counting the reviews on probation too 44.8 a slot, the most 186, 4 in 100 reach a hundred. Over the conduct's slots that reach a suspension (731 slots, 75 in 100) the first comes after 27.5 ± 0.6 reviews as a member (median 29; the real-task reviews among them in the table above). The 250 slots never suspended made 25.3 member reviews (the most 82): 1 alive at the run's end and 249 departed under the exit rule, 216 of them with a wrong planted verdict on the record (the seats lost, no suspension yet).
- read 15: conduct M at 0.5, world 3's cell: 153 conduct slots with a hundred member reviews or more, 10 suspended before the hundredth (7 in 100), 61 ever; the first suspension after 46.0 member reviews over the 412 slots that reach one.
- read 9: conduct M at 0.1, world 3's cell: 279 conduct slots with a hundred member reviews or more, 2 suspended before the hundredth (1 in 100), 3 ever; the first suspension after 3.7 member reviews over the 122 slots that reach one.

## Read 17. Conduct G at 1.0 in world 3's cell on seeds 21–140 — careful until its first wrong planted verdict, then a claim at every decision where its earned seats are lost, careful where they are held, on probation and after a suspension (read as read 13 was; reads 13 and 14 beside)

### From the first failure on — among the slots that ever had a wrong planted verdict, the conduct's failed slots less the careful failed slots of the same world and seeds

| read | seeds | failed slots a seed: F / careful | **from the first failure: of record** (level at) | **with the reservation** (level at) | **like for like** (level at) | F's claims after the first failure a slot (seats held / lost at the claim) | further wrong planted verdicts a slot: F / careful | ticks without the earned seats: F / careful (share whose seats returned) | suspensions a slot: F / careful; departed share: F / careful | ticks from the first failure to the exit: F / careful |
|---|---|---|---|---|---|---|---|---|---|---|
| read 13: conduct G at 0.3 (240 seeds) | 240 | 5.3 / 15.9 | **+15 ± 15** (1.9) | **+4 ± 14** (1.2) | **+13 ± 11** (1.7) | 5.9 (0.0 / 5.9) | 0.87 / 0.45 | 185 / 176 (0.50 / 0.60) | 0.26 / 0.26; 0.40 / 0.33 | 338 / 347 |
| read 14: conduct F at 1.0 (120 seeds) | 120 | 5.7 / 17.2 | **+168 ± 13** (2.9) | **+96 ± 14** (2.1) | **+67 ± 12** (1.5) | 30.6 (4.9 / 25.7) | 3.20 / 0.59 | 150 / 158 (0.46 / 0.65) | 0.51 / 0.20; 0.69 / 0.29 | 266 / 337 |
| **read 17: conduct G at 1.0 (120 seeds)** | 120 | 5.6 / 16.5 | **+26 ± 21** (1.6) | **-22 ± 19** (0.5) | **-44 ± 17** (0.4) | 15.6 (0.0 / 15.6) | 1.68 / 0.49 | 152 / 164 (0.46 / 0.63) | 0.45 / 0.22; 0.54 / 0.31 | 297 / 340 |

### Over the life — the conduct's slots less the careful beside (every slot, failed or not)

| world / read | seeds | **of record** | temptation | **with the reservation** | temptation | **like for like** | temptation |
|---|---|---|---|---|---|---|---|
| read 13: conduct G at 0.3 | 240 | **-7 ± 18** (-0.4) | 0.3 ± 1.9 | **-12 ± 16** (-0.7) | -0.2 ± 1.6 | **-1 ± 11** (-0.1) | 0.9 ± 1.1 |
| read 14: conduct F at 1.0 | 120 | **+85 ± 21** (4.0) | 2.6 ± 0.4 | **+41 ± 19** (2.2) | 1.8 ± 0.4 | **+27 ± 13** (2.1) | 1.5 ± 0.2 |
| **read 17: conduct G at 1.0** | 120 | **+6 ± 24** (0.3) | 1.2 ± 0.9 | **-24 ± 22** (-1.1) | 0.1 ± 0.8 | **-36 ± 14** (-2.6) | -0.3 ± 0.5 |

### Paired on the shared seeds (second − first; a positive figure: the second further behind)

| contrast | seeds | lifetime | first | second | **second − first, paired** | SE from nothing |
|---|---|---|---|---|---|---|
| read 17 (G at 1.0) against read 14 (F at 1.0), over the life | 120 | of record | +85 | +6 | **-78 ± 13** | -6.0 |
| read 17 (G at 1.0) against read 14 (F at 1.0), over the life | 120 | with the reservation | +41 | -24 | **-65 ± 11** | -5.9 |
| read 17 (G at 1.0) against read 14 (F at 1.0), over the life | 120 | like for like | +27 | -36 | **-64 ± 10** | -6.5 |
| read 17 (G at 1.0) against read 14 (F at 1.0), from the first failure on | 120 | of record | +168 | +26 | **-142 ± 17** | -8.2 |
| read 17 (G at 1.0) against read 14 (F at 1.0), from the first failure on | 120 | with the reservation | +96 | -22 | **-118 ± 17** | -6.8 |
| read 17 (G at 1.0) against read 14 (F at 1.0), from the first failure on | 120 | like for like | +67 | -44 | **-111 ± 15** | -7.6 |
| read 17 (G at 1.0) against read 13 (G at 0.3), from the first failure on | 120 | of record | -17 | +26 | **+42 ± 19** | 2.2 |
| read 17 (G at 1.0) against read 13 (G at 0.3), from the first failure on | 120 | with the reservation | -26 | -22 | **+5 ± 17** | 0.3 |
| read 17 (G at 1.0) against read 13 (G at 0.3), from the first failure on | 120 | like for like | -10 | -44 | **-33 ± 16** | -2.1 |

**Read 17's figures for the expectations.** Claims a failed slot 15.6 (held 0.0 / lost 15.6; read 13's 5.9); from the first failure on behind by +26 ± 21 of record, -22 ± 19 with the reservation, -44 ± 17 like for like; for each claim 1.6 ± 1.3 / -1.4 ± 1.2 / -2.8 ± 1.1 real; level at 1.6 ± 0.5 / 0.5 ± 0.4 / 0.4 ± 0.2; suspensions a failed slot 0.45 (the careful failed slots' 0.22; read 13's 0.26, read 14's 0.51); further failures 1.68 against 0.49; ticks without the seats 152 against 164; departed 0.54 against 0.31.

### Y3.3. The level saving on a marked record by the identity (q · the level temptation; the reviewer's figures in parentheses)

| read | over the life: of record / with the reservation / like for like | from the first failure on: of record / with the reservation / like for like |
|---|---|---|
| read 12: conduct F at 0.3 | 1.10 / 0.95 / 0.89 (1.11 / 0.96 / 0.90) | 1.06 / 0.85 / 0.80 (1.05 / 0.84 / 0.81) |
| read 13: conduct G at 0.3 | 0.09 / -0.07 / 0.27 | 0.56 / 0.36 / 0.51 (0.57 / 0.36 / 0.51) |
| read 14: conduct F at 1.0 | 2.60 / 1.78 / 1.46 | 2.85 / 2.06 / 1.47 (2.9 / 2.1 / 1.5) |
| read 17: conduct G at 1.0 | 1.25 / 0.07 / -0.27 | 1.56 / 0.53 / 0.36 |

For conduct G the identity's q is the dose while the seats are lost, not the share of all member reviews claimed — G claims none with the seats held — so its 'level saving' is the share of the care on its reviews with the seats lost, as the reviewer's 0.57 / 0.36 / 0.51 read it.

## Against the expectations stated before the run, and the refutations or showings

- MET — W2: the identity holds as the engine counts (one care draw at every seat, the claim sparing that draw and nothing else); the tallies' level savings of read 9 as a ratio of the seeds' means are 0.61 / 0.52 / 0.38 against the identity's 0.62 / 0.52 / 0.38 (within the 0.1 asked); the mean of the seeds' ratios 0.83 / 0.69 / 0.47 is above both, for the reason given in W2.
- MET — W3: a conduct slot of read 9 makes 75.4 reviews as a member in a life (60 to 90 expected).
- MET — W3: 13 in 100 of read 9's conduct slots are suspended at least once (10 to 40 expected).
- MET — W3: a conduct slot of read 9 gives 2.27 times a careful slot's wrong approvals of real bad work (1.5 to 4 expected).
- MET — read 15: conduct M at 0.5, world 3's cell: behind on every lifetime, +420 ± 17 / +304 ± 14 / +284 ± 14 (250 to 700 of record expected).
- MET — read 15: conduct M at 0.5, world 3's cell: the level saving from the tallies 3.62 / 2.70 / 1.85 (above 1.0 on every lifetime expected); by the identity 3.30 / 2.53 / 1.83.
- MET — read 15: conduct M at 0.5, world 3's cell: 41 in 100 of the conduct's slots suspended at least once (30 to 80 expected).
- MET — read 16: conduct M at 1.0, world 3's cell: behind on every lifetime, +649 ± 16 / +389 ± 12 / +354 ± 15 (400 to 900 of record expected).
- MET — read 16: conduct M at 1.0, world 3's cell: the level saving from the tallies 10.38 / 6.63 / 2.84 (above 1.5 on every lifetime expected); by the identity 9.59 / 6.15 / 2.82.
- MISSED — read 16: over the slots that reach a suspension the first comes after 27.5 reviews as a member (30 to 90 expected).
- EMPTY — read 16: no conduct slot makes a hundred reviews as a member (the expectation's set is empty; every slot is stopped, departs or reaches the run's end before its hundredth).
- MET — read 17: 15.6 claims a failed slot (15 to 30 expected).
- MET — read 17: from the first failure on behind at the point value by +26 ± 21 of record (20 to 120 expected).
- MET — read 17: for each claim 1.6 ± 1.3 real of record lost (1 to 5 expected).
- MET — read 17: level at a temptation of 1.6 ± 0.5 of record from the first failure on (1.3 to 2.7 expected).
- MET — read 17: suspensions a failed slot 0.45 (above read 13's 0.26 and no higher than read 14's 0.51 expected).
- MET — read 17: from the first failure on G at 1.0 loses less than F at 1.0 by seed — G less F -142 ± 17 of record on 120 seeds (less expected).
- (the sign with the reservation, which the reviewer did not know: -22 ± 19)

### Refuted, or shown, each apart

- "A cheaper model pays in the design as ruled when it misses one bad delivery in ten": shown if the level saving of read 9 is under 0.9 at the point value on the lifetime of record — by the identity 0.62, by the tallies 0.83 ± 0.13: **SHOWN**.
- "It does not pay when it misses half or more": refuted if the level saving of read 15 or of read 16 is under 0.9 on any lifetime — read 15 3.62 / 2.70 / 1.85, read 16 10.38 / 6.63 / 2.84 from the tallies (the identity 3.30 / 2.53 / 1.83 and 9.59 / 6.15 / 2.82): **NOT REFUTED**.
- "A member that misses everything is stopped within a hundred reviews": refuted if in read 16, among the conduct's slots that make a hundred reviews as a member or more, fewer than 9 in 10 were suspended before their hundredth — no conduct slot makes a hundred reviews as a member, so the condition's set is empty: **NOT REFUTED** (and, read on the slots as they are, every one is stopped before a hundred: the member reviews in a life and the suspensions' timing above).
- "A skip costs something while the earned seats are lost": refuted if in read 17, from the first failure on, conduct G at 1.0 is within two standard errors of nothing on the lifetime of record — +26 ± 21 (1.2 SE): **REFUTED**.
- "Skipping everything while the earned seats are lost pays": shown if in read 17, from the first failure on, conduct G at 1.0 is ahead by two standard errors of record or with the reservation counted, or level at a temptation under 1 on both — of record +26 ± 21 (level at 1.6), with the reservation -22 ± 19 (level at 0.5): **NOT SHOWN**.

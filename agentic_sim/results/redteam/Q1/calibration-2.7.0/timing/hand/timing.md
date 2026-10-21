# The reward's timing — cell `--entry-pool 20 --stampers 0.6 --pi0 0 --dial off --audit-roll off --care-cost 4`, seeds 21-40

Per decision window (real at the window's closing index): the reward the environment paid, its reviewing side (what the decision caused: the care cost, its reimbursement, the review fee, the bond lost), its working side (the slot actor's other life: the delivery price, the effort cost, a guarantee lost, its own court fee, the emission share, the uplift) and the revaluation of the wealth held by the index's move, mean and SD across windows; the decomposition is exact (the residual is the check); the lag from a review decision to its own case's consequences.

| policy | windows | ticks/window mean / median / p90 | one-tick windows | reward mean | reward SD | review side mean | SD | work side mean | SD | revaluation mean | SD | other | residual |abs| | corr |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| careful | 1495 | 13.2 / 1 / 9 | 0.68 | 13.84 | 63.92 | -2.39 | 4.60 | 16.22 | 53.79 | -0.15 | 26.42 | 0.00 | 0.16 | 0.997 |
| stamper | 1841 | 10.7 / 1 / 3 | 0.66 | 19.36 | 81.33 | 1.83 | 4.33 | 19.08 | 67.43 | -1.63 | 45.63 | 0.00 | 0.08 | 0.999 |

## The long windows (more than five ticks between decisions: the slot off duty, its work landing)

| policy | share of windows | reward mean (long) | SD | reward mean (short) | SD | share of the reward's variance |
|---|---|---|---|---|---|---|
| careful | 0.11 | 136.91 | 136.78 | -0.91 | 17.64 | 0.88 |
| stamper | 0.09 | 184.98 | 209.20 | 3.38 | 12.29 | 0.94 |

## By source (mean per window, SD, share of windows carrying it)

| policy | care_cost | reimbursement | review_fee | bond_lost | delivery_price | effort_cost | guarantee_lost | court_fee | emission | uplift | revaluation | other |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| careful | -8.90 ± 2.7 (0.99) | 4.92 ± 0.6 (0.99) | 1.79 ± 3.7 (0.41) | -0.19 ± 0.9 (0.04) | 25.79 ± 86.4 (0.20) | -10.30 ± 37.1 (0.10) | -1.82 ± 7.3 (0.08) | 0.00 ± 0.0 (0.00) | 2.55 ± 5.6 (0.41) | 0.00 ± 0.0 (0.00) | -0.15 ± 26.4 (0.04) | 0.00 ± 0.0 (0.00) |
| stamper | 0.00 ± 0.0 (0.00) | 0.00 ± 0.0 (0.00) | 1.84 ± 4.3 (0.36) | -0.00 ± 0.1 (0.00) | 27.95 ± 100.0 (0.16) | -9.73 ± 37.0 (0.08) | -1.93 ± 8.1 (0.07) | -0.00 ± 0.0 (0.00) | 2.79 ± 7.0 (0.36) | 0.00 ± 0.0 (0.00) | -1.63 ± 45.6 (0.04) | 0.00 ± 0.0 (0.00) |

## By the action taken in the window

| policy | action | n | reward | review side | work side | care cost | reimbursement | review fee | bond lost |
|---|---|---|---|---|---|---|---|---|---|
| careful | care | 1495 | 13.84 | -2.39 | 16.22 | -8.90 | 4.92 | 1.79 | -0.19 |
| stamper | approve_blind | 1841 | 19.36 | 1.83 | 19.08 | 0.00 | 0.00 | 1.84 | -0.00 |

## The lag from a review decision to its own case's consequences

| policy | source | n | lag (decisions) | lag (ticks) | in own window | one later | two or more later |
|---|---|---|---|---|---|---|---|
| careful | care_cost | 1484 | 0.00 | 0.0 | 1.00 | 0.00 | 0.00 |
| careful | reimbursement | 1486 | 0.00 | 0.0 | 1.00 | 0.00 | 0.00 |
| careful | review_fee | 1430 | 3.60 | 7.9 | 0.28 | 0.07 | 0.65 |
| careful | bond_lost | 111 | 0.95 | 2.1 | 0.14 | 0.77 | 0.09 |
| stamper | review_fee | 1824 | 4.73 | 9.9 | 0.08 | 0.08 | 0.83 |
| stamper | bond_lost | 1 | 2.00 | 2.0 | 0.00 | 0.00 | 1.00 |

## Unclassified events (kind:note, summed real)

- careful: none
- stamper: none

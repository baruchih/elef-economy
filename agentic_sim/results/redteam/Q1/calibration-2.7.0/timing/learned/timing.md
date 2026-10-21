# The reward's timing — cell `--entry-pool 20 --stampers 0.6 --pi0 0 --dial off --audit-roll off --care-cost 4`, seeds 21-40

Per decision window (real at the window's closing index): the reward the environment paid, its reviewing side (what the decision caused: the care cost, its reimbursement, the review fee, the bond lost), its working side (the slot actor's other life: the delivery price, the effort cost, a guarantee lost, its own court fee, the emission share, the uplift) and the revaluation of the wealth held by the index's move, mean and SD across windows; the decomposition is exact (the residual is the check); the lag from a review decision to its own case's consequences.

| policy | windows | ticks/window mean / median / p90 | one-tick windows | reward mean | reward SD | review side mean | SD | work side mean | SD | revaluation mean | SD | other | residual |abs| | corr |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 1527 | 12.9 / 1 / 4 | 0.70 | 9.85 | 52.83 | -0.57 | 4.77 | 10.77 | 42.97 | -0.59 | 27.50 | 0.00 | 0.25 | 0.996 |
| direct | 955 | 20.7 / 1 / 7 | 0.72 | 5.34 | 29.03 | -0.71 | 4.52 | 5.82 | 23.36 | -0.20 | 11.98 | 0.00 | 0.42 | 0.991 |

## The long windows (more than five ticks between decisions: the slot off duty, its work landing)

| policy | share of windows | reward mean (long) | SD | reward mean (short) | SD | share of the reward's variance |
|---|---|---|---|---|---|---|
| learned | 0.09 | 99.62 | 138.71 | 0.72 | 15.04 | 0.90 |
| direct | 0.10 | 46.84 | 77.76 | 0.59 | 5.86 | 0.94 |

## By source (mean per window, SD, share of windows carrying it)

| policy | care_cost | reimbursement | review_fee | bond_lost | delivery_price | effort_cost | guarantee_lost | court_fee | emission | uplift | revaluation | other |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | -2.88 ± 4.7 (0.30) | 1.51 ± 2.3 (0.30) | 1.57 ± 3.6 (0.36) | -0.77 ± 2.1 (0.14) | 17.65 ± 71.7 (0.14) | -7.63 ± 31.4 (0.08) | -1.60 ± 8.0 (0.06) | -0.00 ± 0.1 (0.00) | 2.34 ± 5.7 (0.36) | 0.00 ± 0.0 (0.00) | -0.59 ± 27.5 (0.04) | 0.00 ± 0.0 (0.00) |
| direct | -1.51 ± 3.2 (0.19) | 0.97 ± 2.0 (0.19) | 1.31 ± 3.2 (0.33) | -1.48 ± 2.6 (0.26) | 9.19 ± 44.0 (0.12) | -4.68 ± 24.0 (0.06) | -0.83 ± 4.8 (0.05) | 0.00 ± 0.0 (0.00) | 2.15 ± 5.6 (0.33) | 0.00 ± 0.0 (0.00) | -0.20 ± 12.0 (0.04) | 0.00 ± 0.0 (0.00) |

## By the action taken in the window

| policy | action | n | reward | review side | work side | care cost | reimbursement | review fee | bond lost |
|---|---|---|---|---|---|---|---|---|---|
| learned | care | 468 | 10.51 | -3.16 | 13.12 | -9.38 | 4.92 | 1.76 | -0.46 |
| learned | approve_blind | 795 | 12.10 | 1.40 | 11.62 | 0.00 | 0.00 | 1.69 | -0.29 |
| learned | reject_blind | 264 | 1.93 | -1.91 | 4.02 | 0.00 | 0.00 | 0.86 | -2.77 |
| direct | care | 186 | 9.21 | -2.90 | 9.75 | -7.78 | 5.00 | 1.30 | -1.42 |
| direct | approve_blind | 417 | 6.56 | 1.14 | 5.37 | 0.00 | 0.00 | 1.71 | -0.57 |
| direct | reject_blind | 352 | 1.84 | -1.74 | 4.29 | 0.00 | 0.00 | 0.85 | -2.59 |

## The lag from a review decision to its own case's consequences

| policy | source | n | lag (decisions) | lag (ticks) | in own window | one later | two or more later |
|---|---|---|---|---|---|---|---|
| learned | care_cost | 463 | 0.00 | 0.0 | 1.00 | 0.00 | 0.00 |
| learned | reimbursement | 463 | 0.00 | 0.0 | 1.00 | 0.00 | 0.00 |
| learned | review_fee | 1283 | 4.31 | 8.9 | 0.17 | 0.07 | 0.75 |
| learned | bond_lost | 460 | 0.89 | 2.1 | 0.19 | 0.73 | 0.08 |
| direct | care_cost | 186 | 0.00 | 0.0 | 1.00 | 0.00 | 0.00 |
| direct | reimbursement | 186 | 0.00 | 0.0 | 1.00 | 0.00 | 0.00 |
| direct | review_fee | 665 | 3.83 | 8.2 | 0.25 | 0.08 | 0.67 |
| direct | bond_lost | 565 | 0.93 | 2.1 | 0.16 | 0.75 | 0.09 |

## Unclassified events (kind:note, summed real)

- learned: none
- direct: none

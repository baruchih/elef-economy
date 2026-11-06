# The label recompute on `results/redteam/stability/learned-rev-careful-2/relabel/direct-offline` (seeds 1-20; 1028482 decisions, 1028482 at review seats)

The pooled label (the construction the chain trained on) and the own-name label on the same decisions, by seat and by the action taken: the mean credit, and the pooled purse's part — pooled minus own — per decision.

| seat | decisions | label changed (share) | mean pooled | mean own | care: n / pooled / own / pooled − own | approve blind: n / pooled / own / pooled − own | reject blind: n / pooled / own / pooled − own | plant: n / pooled / own | real: n / pooled / own |
|---|---|---|---|---|---|---|---|---|---|
| initial | 753469 | 0.742 | 3.82 | 3.19 | 492502 / 4.09 / 4.17 / -0.08 | 206398 / 3.97 / 1.90 / 2.07 | 54569 / 0.74 / -0.73 / 1.47 | 156060 / 1.52 / 1.52 | 597409 / 4.42 / 3.63 |
| audit | 222700 | 0.997 | 20.06 | 5.41 | 55975 / 17.52 / 4.87 / 12.65 | 156597 / 22.18 / 6.03 / 16.16 | 10128 / 1.27 / -1.24 / 2.51 | 0 / — / — | 222700 / 20.06 / 5.41 |
| panel | 52313 | 0.998 | 5.58 | 4.25 | 30904 / 5.57 / 4.75 / 0.82 | 17385 / 7.47 / 4.19 / 3.29 | 4024 / -2.49 / 0.75 / -3.24 | 0 / — / — | 52313 / 5.58 / 4.25 |

The argmax by seat on the same observations: the action mix (care / approve blind / reject blind) each model chooses over every decision at the seat, and the share of decisions whose argmax differs between two models — own-name against the pooled refit (the label rule's effect), own-name against the stored model, the pooled refit against the stored model (the same labels and torch seed: zero where the fit is deterministic, or the data differ from the stored model's), and a second pooled refit on another torch seed against the first (two fits of the same labels: the refit's own noise, the floor any difference must clear).

| seat | decisions | direct own: mix | direct pooled refit: mix | direct pooled refit (seed 1): mix | direct stored: mix | direct own vs direct pooled refit | direct own vs direct stored | direct pooled refit vs direct stored | direct pooled refit (seed 1) vs direct pooled refit |
|---|---|---|---|---|---|---|---|---|---|
| initial | 753469 | 0.963 / 0.028 / 0.009 | 0.613 / 0.361 / 0.026 | 0.603 / 0.371 / 0.026 | 0.613 / 0.361 / 0.026 | 0.379 | 0.379 | 0.000 | 0.234 |
| audit | 222700 | 0.086 / 0.914 / 0.000 | 0.043 / 0.956 / 0.000 | 0.028 / 0.972 / 0.000 | 0.043 / 0.956 / 0.000 | 0.105 | 0.105 | 0.000 | 0.059 |
| panel | 52313 | 0.505 / 0.356 / 0.139 | 0.484 / 0.490 / 0.027 | 0.485 / 0.482 / 0.033 | 0.484 / 0.490 / 0.027 | 0.530 | 0.530 | 0.000 | 0.354 |
| all review | 1028482 | 0.750 / 0.236 / 0.014 | 0.483 / 0.497 / 0.020 | 0.473 / 0.507 / 0.020 | 0.483 / 0.497 / 0.020 | 0.327 | 0.327 | 0.000 | 0.202 |

The same mix on the plants alone and on the real cases alone at each seat:

| seat | direct own: plant / real | direct pooled refit: plant / real | direct pooled refit (seed 1): plant / real | direct stored: plant / real |
|---|---|---|---|---|
| initial | 0.976 / 0.013 / 0.012 — 0.960 / 0.032 / 0.008 | 0.684 / 0.282 / 0.034 — 0.594 / 0.382 / 0.024 | 0.679 / 0.289 / 0.032 — 0.584 / 0.392 / 0.024 | 0.684 / 0.282 / 0.034 — 0.594 / 0.382 / 0.024 |
| audit | — — 0.086 / 0.914 / 0.000 | — — 0.043 / 0.956 / 0.000 | — — 0.028 / 0.972 / 0.000 | — — 0.043 / 0.956 / 0.000 |
| panel | — — 0.505 / 0.356 / 0.139 | — — 0.484 / 0.490 / 0.027 | — — 0.485 / 0.482 / 0.033 | — — 0.484 / 0.490 / 0.027 |

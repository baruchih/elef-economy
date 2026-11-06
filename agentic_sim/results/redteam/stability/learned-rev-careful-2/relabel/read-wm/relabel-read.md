# The label recompute on `results/redteam/stability/learned-rev-careful-2/relabel/wm-offline` (seeds 1-20; 1002450 decisions, 1002450 at review seats)

The pooled label (the construction the chain trained on) and the own-name label on the same decisions, by seat and by the action taken: the mean credit, and the pooled purse's part — pooled minus own — per decision.

| seat | decisions | label changed (share) | mean pooled | mean own | care: n / pooled / own / pooled − own | approve blind: n / pooled / own / pooled − own | reject blind: n / pooled / own / pooled − own | plant: n / pooled / own | real: n / pooled / own |
|---|---|---|---|---|---|---|---|---|---|
| initial | 748081 | 0.735 | 4.00 | 3.32 | 520959 / 4.16 / 4.21 / -0.04 | 184152 / 4.22 / 1.72 / 2.50 | 42970 / 1.00 / -0.62 / 1.63 | 157685 / 1.65 / 1.65 | 590396 / 4.62 / 3.76 |
| audit | 209253 | 0.996 | 20.10 | 5.41 | 48852 / 17.71 / 4.84 / 12.86 | 150734 / 22.06 / 6.02 / 16.04 | 9667 / 1.59 / -1.32 / 2.92 | 0 / — / — | 209253 / 20.10 / 5.41 |
| panel | 45116 | 0.998 | 5.69 | 4.21 | 26256 / 5.93 / 4.65 / 1.28 | 15674 / 7.00 / 4.06 / 2.93 | 3186 / -2.70 / 1.29 / -3.99 | 0 / — / — | 45116 / 5.69 / 4.21 |

The argmax by seat on the same observations: the action mix (care / approve blind / reject blind) each model chooses over every decision at the seat, and the share of decisions whose argmax differs between two models — own-name against the pooled refit (the label rule's effect), own-name against the stored model, the pooled refit against the stored model (the same labels and torch seed: zero where the fit is deterministic, or the data differ from the stored model's), and a second pooled refit on another torch seed against the first (two fits of the same labels: the refit's own noise, the floor any difference must clear).

| seat | decisions | direct own: mix | direct pooled refit: mix | direct pooled refit (seed 1): mix | direct stored: mix | wm own: mix | wm pooled refit: mix | wm pooled refit (seed 1): mix | wm stored: mix | direct own vs direct pooled refit | direct own vs direct stored | direct pooled refit vs direct stored | direct pooled refit (seed 1) vs direct pooled refit | wm own vs wm pooled refit | wm own vs wm stored | wm pooled refit vs wm stored | wm pooled refit (seed 1) vs wm pooled refit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| initial | 748081 | 0.958 / 0.033 / 0.009 | 0.596 / 0.374 / 0.030 | 0.594 / 0.376 / 0.030 | 0.608 / 0.365 / 0.026 | 0.989 / 0.010 / 0.002 | 0.651 / 0.346 / 0.003 | 0.649 / 0.342 / 0.009 | 0.651 / 0.346 / 0.003 | 0.388 | 0.380 | 0.310 | 0.252 | 0.345 | 0.345 | 0.000 | 0.199 |
| audit | 209253 | 0.105 / 0.894 / 0.000 | 0.056 / 0.944 / 0.000 | 0.067 / 0.933 / 0.000 | 0.045 / 0.955 / 0.000 | 0.119 / 0.881 / 0.000 | 0.008 / 0.992 / 0.000 | 0.005 / 0.995 / 0.000 | 0.008 / 0.992 / 0.000 | 0.122 | 0.128 | 0.077 | 0.090 | 0.118 | 0.118 | 0.000 | 0.008 |
| panel | 45116 | 0.392 / 0.447 / 0.160 | 0.405 / 0.561 / 0.034 | 0.407 / 0.574 / 0.019 | 0.505 / 0.468 / 0.027 | 0.577 / 0.356 / 0.067 | 0.283 / 0.717 / 0.001 | 0.359 / 0.639 / 0.002 | 0.283 / 0.717 / 0.001 | 0.531 | 0.536 | 0.454 | 0.357 | 0.525 | 0.525 | 0.000 | 0.373 |
| all review | 1002450 | 0.755 / 0.232 / 0.014 | 0.475 / 0.501 / 0.024 | 0.476 / 0.501 / 0.023 | 0.486 / 0.493 / 0.021 | 0.789 / 0.207 / 0.004 | 0.500 / 0.498 / 0.002 | 0.502 / 0.491 / 0.007 | 0.500 / 0.498 / 0.002 | 0.339 | 0.334 | 0.268 | 0.223 | 0.306 | 0.306 | 0.000 | 0.167 |

The same mix on the plants alone and on the real cases alone at each seat:

| seat | direct own: plant / real | direct pooled refit: plant / real | direct pooled refit (seed 1): plant / real | direct stored: plant / real | wm own: plant / real | wm pooled refit: plant / real | wm pooled refit (seed 1): plant / real | wm stored: plant / real |
|---|---|---|---|---|---|---|---|---|
| initial | 0.976 / 0.012 / 0.012 — 0.953 / 0.039 / 0.008 | 0.675 / 0.288 / 0.037 — 0.575 / 0.397 / 0.028 | 0.663 / 0.297 / 0.040 — 0.576 / 0.397 / 0.027 | 0.680 / 0.286 / 0.034 — 0.589 / 0.386 / 0.024 | 0.993 / 0.004 / 0.002 — 0.987 / 0.011 / 0.001 | 0.710 / 0.287 / 0.004 — 0.635 / 0.362 / 0.003 | 0.694 / 0.294 / 0.012 — 0.637 / 0.354 / 0.008 | 0.710 / 0.287 / 0.004 — 0.635 / 0.362 / 0.003 |
| audit | — — 0.105 / 0.894 / 0.000 | — — 0.056 / 0.944 / 0.000 | — — 0.067 / 0.933 / 0.000 | — — 0.045 / 0.955 / 0.000 | — — 0.119 / 0.881 / 0.000 | — — 0.008 / 0.992 / 0.000 | — — 0.005 / 0.995 / 0.000 | — — 0.008 / 0.992 / 0.000 |
| panel | — — 0.392 / 0.447 / 0.160 | — — 0.405 / 0.561 / 0.034 | — — 0.407 / 0.574 / 0.019 | — — 0.505 / 0.468 / 0.027 | — — 0.577 / 0.356 / 0.067 | — — 0.283 / 0.717 / 0.001 | — — 0.359 / 0.639 / 0.002 | — — 0.283 / 0.717 / 0.001 |

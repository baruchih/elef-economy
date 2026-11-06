# The label recompute on `results/redteam/stability/learned-rev-careful-290b/relabel/wm-offline` (seeds 1-20; 889499 decisions, 889499 at review seats)

The pooled label (the construction the chain trained on) and the own-name label on the same decisions, by seat and by the action taken: the mean credit, and the pooled purse's part — pooled minus own — per decision.

| seat | decisions | label changed (share) | mean pooled | mean own | care: n / pooled / own / pooled − own | approve blind: n / pooled / own / pooled − own | reject blind: n / pooled / own / pooled − own | plant: n / pooled / own | real: n / pooled / own |
|---|---|---|---|---|---|---|---|---|---|
| initial | 738672 | 0.742 | 6.41 | 3.76 | 546923 / 6.58 / 4.57 / 2.01 | 150348 / 6.80 / 1.94 / 4.86 | 41401 / 2.73 / -0.28 / 3.01 | 147117 / 2.10 / 2.38 | 591555 / 7.48 / 4.11 |
| audit | 115872 | 0.953 | 17.17 | 4.78 | 49210 / 15.98 / 4.68 / 11.30 | 62285 / 19.21 / 5.29 / 13.92 | 4377 / 1.51 / -1.31 / 2.82 | 13633 / 3.07 / 1.76 | 102239 / 19.05 / 5.18 |
| panel | 34955 | 0.905 | 4.82 | 4.17 | 28548 / 5.43 / 4.66 / 0.77 | 4611 / 4.03 / 2.00 / 2.03 | 1796 / -2.98 / 2.01 / -4.99 | 10592 / 6.06 / 3.88 | 24363 / 4.28 / 4.30 |

The argmax by seat on the same observations: the action mix (care / approve blind / reject blind) each model chooses over every decision at the seat, and the share of decisions whose argmax differs between two models — own-name against the pooled refit (the label rule's effect), own-name against the stored model, the pooled refit against the stored model (the same labels and torch seed: zero where the fit is deterministic, or the data differ from the stored model's), and a second pooled refit on another torch seed against the first (two fits of the same labels: the refit's own noise, the floor any difference must clear).

| seat | decisions | direct own: mix | direct pooled refit: mix | direct pooled refit (seed 1): mix | direct stored: mix | wm own: mix | wm pooled refit: mix | wm pooled refit (seed 1): mix | wm stored: mix | direct own vs direct pooled refit | direct own vs direct stored | direct pooled refit vs direct stored | direct pooled refit (seed 1) vs direct pooled refit | wm own vs wm pooled refit | wm own vs wm stored | wm pooled refit vs wm stored | wm pooled refit (seed 1) vs wm pooled refit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| initial | 738672 | 0.972 / 0.020 / 0.008 | 0.690 / 0.289 / 0.021 | 0.701 / 0.279 / 0.020 | 0.707 / 0.279 / 0.014 | 0.997 / 0.002 / 0.001 | 0.767 / 0.232 / 0.001 | 0.730 / 0.269 / 0.001 | 0.767 / 0.232 / 0.001 | 0.315 | 0.301 | 0.282 | 0.221 | 0.233 | 0.233 | 0.000 | 0.139 |
| audit | 115872 | 0.600 / 0.399 / 0.001 | 0.227 / 0.772 / 0.000 | 0.207 / 0.792 / 0.001 | 0.235 / 0.765 / 0.000 | 0.659 / 0.341 / 0.000 | 0.121 / 0.879 / 0.000 | 0.100 / 0.900 / 0.000 | 0.121 / 0.879 / 0.000 | 0.559 | 0.551 | 0.308 | 0.257 | 0.605 | 0.605 | 0.000 | 0.131 |
| panel | 34955 | 0.720 / 0.091 / 0.188 | 0.697 / 0.253 / 0.049 | 0.672 / 0.294 / 0.034 | 0.657 / 0.308 / 0.035 | 0.961 / 0.007 / 0.031 | 0.661 / 0.337 / 0.002 | 0.651 / 0.347 / 0.002 | 0.661 / 0.337 / 0.002 | 0.434 | 0.496 | 0.403 | 0.333 | 0.360 | 0.360 | 0.000 | 0.314 |
| all review | 889499 | 0.914 / 0.072 / 0.014 | 0.630 / 0.351 / 0.019 | 0.636 / 0.347 / 0.018 | 0.644 / 0.343 / 0.013 | 0.952 / 0.047 / 0.002 | 0.679 / 0.321 / 0.000 | 0.645 / 0.354 / 0.001 | 0.679 / 0.321 / 0.000 | 0.352 | 0.341 | 0.290 | 0.230 | 0.286 | 0.286 | 0.000 | 0.145 |

The same mix on the plants alone and on the real cases alone at each seat:

| seat | direct own: plant / real | direct pooled refit: plant / real | direct pooled refit (seed 1): plant / real | direct stored: plant / real | wm own: plant / real | wm pooled refit: plant / real | wm pooled refit (seed 1): plant / real | wm stored: plant / real |
|---|---|---|---|---|---|---|---|---|
| initial | 0.971 / 0.018 / 0.012 — 0.972 / 0.021 / 0.007 | 0.728 / 0.244 / 0.027 — 0.680 / 0.301 / 0.019 | 0.740 / 0.235 / 0.025 — 0.691 / 0.290 / 0.018 | 0.751 / 0.232 / 0.017 — 0.697 / 0.290 / 0.013 | 0.998 / 0.001 / 0.001 — 0.997 / 0.002 / 0.001 | 0.817 / 0.183 / 0.001 — 0.755 / 0.245 / 0.000 | 0.789 / 0.210 / 0.001 — 0.715 / 0.284 / 0.001 | 0.817 / 0.183 / 0.001 — 0.755 / 0.245 / 0.000 |
| audit | 0.724 / 0.274 / 0.002 — 0.584 / 0.416 / 0.001 | 0.254 / 0.744 / 0.001 — 0.224 / 0.776 / 0.000 | 0.235 / 0.760 / 0.006 — 0.204 / 0.796 / 0.000 | 0.246 / 0.754 / 0.000 — 0.233 / 0.767 / 0.000 | 0.760 / 0.240 / 0.000 — 0.645 / 0.355 / 0.000 | 0.112 / 0.888 / 0.000 — 0.122 / 0.878 / 0.000 | 0.104 / 0.896 / 0.000 — 0.099 / 0.901 / 0.000 | 0.112 / 0.888 / 0.000 — 0.122 / 0.878 / 0.000 |
| panel | 0.729 / 0.107 / 0.164 — 0.716 / 0.085 / 0.199 | 0.707 / 0.244 / 0.050 — 0.693 / 0.258 / 0.049 | 0.695 / 0.269 / 0.036 — 0.663 / 0.305 / 0.033 | 0.668 / 0.296 / 0.035 — 0.651 / 0.313 / 0.035 | 0.969 / 0.008 / 0.023 — 0.958 / 0.006 / 0.035 | 0.647 / 0.352 / 0.000 — 0.667 / 0.331 / 0.002 | 0.657 / 0.343 / 0.000 — 0.648 / 0.349 / 0.002 | 0.647 / 0.352 / 0.000 — 0.667 / 0.331 / 0.002 |

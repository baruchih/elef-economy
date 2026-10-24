# Evaluation (Q5, the learned child) — cell `--entry-pool 20 --stampers 0.6 --delegation on --c-d-sigma 0.8 --child-prefers-nested on`, seeds 21-40, model `results/redteam/Q5/child/line-v4/models/wm-online-10.pt` (value mc, horizon 16)

| policy | lifetime real wealth | paired − careful | work decisions | bad share | miss share | nested awards | bad approved | bad caught | misses lapsed | good final N | bad approved rate | slot final-N rate | population final-N rate | guarantees forfeited (nominal) | effort saved (nominal) | slot ρ | awards | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 721.5 ± 24.1 | -31.2 ± 34.1 | 69.8 | 0.015 | 0.024 | 69.900 | 0.000 | 1.300 | 1.350 | 14.300 | 0.000 | 0.230 | 0.213 | 72.200 | 6.717 | 0.901 | 69.900 | 0.00 |
| learned | 672.1 ± 38.8 | -80.6 ± 40.3 | 71.8 | 0.174 | 0.032 | 71.800 | 0.150 | 8.650 | 2.500 | 11.950 | 0.017 | 0.299 | 0.214 | 93.800 | 47.462 | 0.886 | 71.800 | 0.20 |
| careful | 752.6 ± 36.2 | nan ± nan | 71.5 | 0.000 | 0.000 | 71.600 | 0.000 | 0.000 | 0.000 | 14.350 | — | 0.203 | 0.211 | 62.150 | 0.000 | 0.905 | 71.600 | 0.00 |
| zero | 553.2 ± 66.5 | -199.5 ± 84.9 | 57.7 | 1.000 | 0.000 | 57.700 | 0.650 | 57.000 | 0.000 | 0.000 | 0.011 | 0.989 | 0.228 | 237.100 | 315.259 | 0.703 | 57.700 | 0.00 |
| miss | 501.3 ± 59.4 | -251.3 ± 74.1 | 50.2 | 0.000 | 1.000 | 50.300 | 0.000 | 0.000 | 50.250 | 0.000 | — | — | 0.227 | 204.950 | 0.000 | 0.704 | 50.300 | 0.00 |

The boundary decisions (the exit the learner's own): leaves chosen and effected, the share of episodes whose learner had departed at the end.

| policy | boundary decisions | leaves chosen | leaves effected | departed |
|---|---|---|---|---|
| greedy | 10.950 | 0.000 | 0.000 | 0.000 |
| learned | 10.800 | 0.450 | 0.200 | 0.200 |
| careful | 11.050 | 0.000 | 0.000 | 0.000 |
| zero | 11.300 | 0.000 | 0.000 | 0.000 |
| miss | 11.100 | 0.000 | 0.000 | 0.000 |

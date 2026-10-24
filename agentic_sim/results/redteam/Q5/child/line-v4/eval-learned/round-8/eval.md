# Evaluation (Q5, the learned child) — cell `--entry-pool 20 --stampers 0.6 --delegation on --c-d-sigma 0.8 --child-prefers-nested on`, seeds 21-40, model `results/redteam/Q5/child/line-v4/models/wm-online-8.pt` (value mc, horizon 16)

| policy | lifetime real wealth | paired − careful | work decisions | bad share | miss share | nested awards | bad approved | bad caught | misses lapsed | good final N | bad approved rate | slot final-N rate | population final-N rate | guarantees forfeited (nominal) | effort saved (nominal) | slot ρ | awards | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 673.8 ± 29.7 | -78.9 ± 38.6 | 61.4 | 0.020 | 0.024 | 61.450 | 0.000 | 1.550 | 1.400 | 12.300 | 0.000 | 0.234 | 0.209 | 62.400 | 8.013 | 0.910 | 61.450 | 0.05 |
| careful | 752.6 ± 36.2 | nan ± nan | 71.5 | 0.000 | 0.000 | 71.600 | 0.000 | 0.000 | 0.000 | 14.350 | — | 0.203 | 0.211 | 62.150 | 0.000 | 0.905 | 71.600 | 0.00 |

The boundary decisions (the exit the learner's own): leaves chosen and effected, the share of episodes whose learner had departed at the end.

| policy | boundary decisions | leaves chosen | leaves effected | departed |
|---|---|---|---|---|
| greedy | 10.600 | 0.050 | 0.050 | 0.050 |
| careful | 11.050 | 0.000 | 0.000 | 0.000 |

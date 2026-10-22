# Evaluation (Q3, the learned deliverer) — cell `--entry-pool 20 --stampers 0.6`, seeds 21-40, model `results/redteam/Q3/line-v4/models/wm-online-10.pt` (value mc, horizon 16)

| policy | lifetime real wealth | paired − careful | work decisions | bad share | bad approved | bad caught | good final N | bad approved rate | slot final-N rate | population final-N rate | guarantees forfeited (nominal) | effort saved (nominal) | slot ρ | awards | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 3161.7 ± 134.0 | 56.8 ± 39.5 | 133.6 | 0.001 | 0.100 | 0.050 | 1.750 | 0.667 | 0.014 | 0.197 | 22.250 | 0.742 | 0.959 | 133.600 | 0.00 |
| careful | 3104.9 ± 135.0 | nan ± nan | 133.6 | 0.000 | 0.000 | 0.000 | 1.850 | — | 0.014 | 0.196 | 22.250 | 0.000 | 0.958 | 133.650 | 0.00 |

The boundary decisions (the exit the learner's own): leaves chosen and effected, the share of episodes whose learner had departed at the end.

| policy | boundary decisions | leaves chosen | leaves effected | departed |
|---|---|---|---|---|
| greedy | 12.050 | 0.200 | 0.000 | 0.000 |
| careful | 12.050 | 0.000 | 0.000 | 0.000 |

# Evaluation (Q3, the learned deliverer) — cell `--entry-pool 20 --stampers 0.6`, seeds 21-40, model `results/redteam/Q3/line-v4/models/wm-online-6.pt` (value mc, horizon 16)

| policy | lifetime real wealth | paired − careful | work decisions | bad share | bad approved | bad caught | good final N | bad approved rate | slot final-N rate | population final-N rate | guarantees forfeited (nominal) | effort saved (nominal) | slot ρ | awards | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 3133.1 ± 133.4 | 28.2 ± 28.2 | 133.8 | 0.000 | 0.050 | 0.000 | 1.850 | 1.000 | 0.014 | 0.196 | 22.700 | 0.262 | 0.957 | 133.800 | 0.00 |
| careful | 3104.9 ± 135.0 | nan ± nan | 133.6 | 0.000 | 0.000 | 0.000 | 1.850 | — | 0.014 | 0.196 | 22.250 | 0.000 | 0.958 | 133.650 | 0.00 |

The boundary decisions (the exit the learner's own): leaves chosen and effected, the share of episodes whose learner had departed at the end.

| policy | boundary decisions | leaves chosen | leaves effected | departed |
|---|---|---|---|---|
| greedy | 12.050 | 0.350 | 0.000 | 0.000 |
| careful | 12.050 | 0.000 | 0.000 | 0.000 |

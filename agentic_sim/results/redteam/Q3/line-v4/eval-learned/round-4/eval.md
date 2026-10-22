# Evaluation (Q3, the learned deliverer) — cell `--entry-pool 20 --stampers 0.6`, seeds 21-40, model `results/redteam/Q3/line-v4/models/wm-online-4.pt` (value mc, horizon 16)

| policy | lifetime real wealth | paired − careful | work decisions | bad share | bad approved | bad caught | good final N | bad approved rate | slot final-N rate | population final-N rate | guarantees forfeited (nominal) | effort saved (nominal) | slot ρ | awards | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 3067.1 ± 151.2 | -37.8 ± 48.9 | 128.9 | 0.000 | 0.000 | 0.000 | 1.800 | — | 0.014 | 0.196 | 21.750 | 0.000 | 0.959 | 129.050 | 0.10 |
| careful | 3104.9 ± 135.0 | nan ± nan | 133.6 | 0.000 | 0.000 | 0.000 | 1.850 | — | 0.014 | 0.196 | 22.250 | 0.000 | 0.958 | 133.650 | 0.00 |

The boundary decisions (the exit the learner's own): leaves chosen and effected, the share of episodes whose learner had departed at the end.

| policy | boundary decisions | leaves chosen | leaves effected | departed |
|---|---|---|---|---|
| greedy | 11.450 | 0.500 | 0.100 | 0.100 |
| careful | 12.050 | 0.000 | 0.000 | 0.000 |

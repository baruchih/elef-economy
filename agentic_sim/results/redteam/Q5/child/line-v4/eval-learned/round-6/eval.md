# Evaluation (Q5, the learned child) — cell `--entry-pool 20 --stampers 0.6 --delegation on --c-d-sigma 0.8 --child-prefers-nested on`, seeds 21-40, model `results/redteam/Q5/child/line-v4/models/wm-online-6.pt` (value mc, horizon 16)

| policy | lifetime real wealth | paired − careful | work decisions | bad share | miss share | nested awards | bad approved | bad caught | misses lapsed | good final N | bad approved rate | slot final-N rate | population final-N rate | guarantees forfeited (nominal) | effort saved (nominal) | slot ρ | awards | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 662.4 ± 44.5 | -90.2 ± 44.8 | 66.0 | 0.057 | 0.001 | 66.100 | 0.100 | 4.450 | 0.100 | 13.100 | 0.022 | 0.268 | 0.212 | 72.400 | 21.374 | 0.906 | 66.100 | 0.10 |
| careful | 752.6 ± 36.2 | nan ± nan | 71.5 | 0.000 | 0.000 | 71.600 | 0.000 | 0.000 | 0.000 | 14.350 | — | 0.203 | 0.211 | 62.150 | 0.000 | 0.905 | 71.600 | 0.00 |

The boundary decisions (the exit the learner's own): leaves chosen and effected, the share of episodes whose learner had departed at the end.

| policy | boundary decisions | leaves chosen | leaves effected | departed |
|---|---|---|---|---|
| greedy | 10.350 | 0.150 | 0.100 | 0.100 |
| careful | 11.050 | 0.000 | 0.000 | 0.000 |

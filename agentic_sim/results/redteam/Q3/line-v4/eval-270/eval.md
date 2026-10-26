# Evaluation (Q3, the learned deliverer) — cell `--entry-pool 20 --stampers 0.6 --rules 2.7.0`, seeds 21-40, model `results/redteam/Q3/line-v4/models/wm-online-10.pt` (value mc, horizon 16)

| policy | lifetime real wealth | paired − careful | work decisions | bad share | miss share | nested awards | bad approved | bad caught | misses lapsed | good final N | bad approved rate | slot final-N rate | population final-N rate | guarantees forfeited (nominal) | effort saved (nominal) | slot ρ | awards | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 1599.1 ± 104.3 | -9.2 ± 13.0 | 130.2 | 0.001 | 0.000 | 0.000 | 0.050 | 0.050 | 0.000 | 26.600 | 0.500 | 0.207 | 0.205 | 284.500 | 0.480 | 0.888 | 130.250 | 0.00 |
| learned | 1302.5 ± 87.0 | -305.7 ± 83.7 | 122.6 | 0.107 | 0.000 | 0.000 | 0.200 | 12.550 | 0.000 | 23.500 | 0.016 | 0.297 | 0.214 | 358.800 | 98.174 | 0.875 | 122.800 | 0.00 |
| careful | 1608.3 ± 106.6 | nan ± nan | 130.2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 26.050 | — | 0.202 | 0.206 | 281.150 | 0.000 | 0.895 | 130.350 | 0.00 |
| zero | 97.1 ± 68.6 | -1511.2 ± 111.0 | 30.7 | 1.000 | 0.000 | 0.000 | 1.000 | 29.650 | 0.000 | 0.000 | 0.033 | 0.967 | 0.217 | 199.250 | 226.046 | 0.487 | 30.700 | 0.00 |

The boundary decisions (the exit the learner's own): leaves chosen and effected, the share of episodes whose learner had departed at the end; the boundary read ({br}: the stay head's one-step read against zero — its mean and the boundaries it read negative — or learned).

| policy | boundary decisions | leaves chosen | leaves effected | departed | stay read (mean) | stay read < 0 |
|---|---|---|---|---|---|---|
| greedy | 12.050 | 0.100 | 0.000 | 0.000 | 79.447 | 0.100 |
| learned | 11.900 | 0.050 | 0.000 | 0.000 | 70.648 | 0.050 |
| careful | 12.100 | 0.000 | 0.000 | 0.000 | — | — |
| zero | 12.100 | 0.000 | 0.000 | 0.000 | — | — |

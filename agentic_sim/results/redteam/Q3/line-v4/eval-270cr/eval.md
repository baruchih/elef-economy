# Evaluation (Q3, the learned deliverer) — cell `--entry-pool 20 --stampers 0.6 --rules 2.7.0`, seeds 21-40, model `results/redteam/Q3/line-v4/models/wm-online-10.pt` (value mc, horizon 16)

| policy | lifetime real wealth | paired − careful | work decisions | bad share | miss share | nested awards | bad approved | bad caught | misses lapsed | good final N | bad approved rate | slot final-N rate | population final-N rate | guarantees forfeited (nominal) | effort saved (nominal) | slot ρ | awards | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 1687.3 ± 110.2 | -77.1 ± 76.6 | 120.5 | 0.001 | 0.000 | 0.000 | 0.050 | 0.050 | 0.000 | 25.650 | 0.500 | 0.215 | 0.211 | 271.050 | 0.480 | 0.884 | 120.600 | 0.05 |
| learned | 1477.6 ± 102.1 | -286.9 ± 88.1 | 123.3 | 0.089 | 0.000 | 0.000 | 0.100 | 11.000 | 0.000 | 22.500 | 0.009 | 0.274 | 0.213 | 334.100 | 82.721 | 0.877 | 123.450 | 0.00 |
| careful | 1764.4 ± 125.8 | nan ± nan | 124.5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 26.250 | — | 0.213 | 0.211 | 278.700 | 0.000 | 0.891 | 124.650 | 0.00 |
| zero | 47.5 ± 37.9 | -1716.9 ± 132.7 | 34.9 | 1.000 | 0.000 | 0.000 | 1.050 | 33.800 | 0.000 | 0.000 | 0.030 | 0.970 | 0.220 | 259.900 | 262.254 | 0.482 | 34.850 | 0.00 |

The boundary decisions (the exit the learner's own): leaves chosen and effected, the share of episodes whose learner had departed at the end; the boundary read ({br}: the stay head's one-step read against zero — its mean and the boundaries it read negative — or learned).

| policy | boundary decisions | leaves chosen | leaves effected | departed | stay read (mean) | stay read < 0 |
|---|---|---|---|---|---|---|
| greedy | 11.750 | 0.350 | 0.050 | 0.050 | 55.573 | 0.350 |
| learned | 11.800 | 0.100 | 0.000 | 0.000 | 55.562 | 0.100 |
| careful | 12.150 | 0.000 | 0.000 | 0.000 | — | — |
| zero | 11.750 | 0.000 | 0.000 | 0.000 | — | — |

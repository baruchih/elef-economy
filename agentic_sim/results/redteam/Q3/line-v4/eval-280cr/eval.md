# Evaluation (Q3, the learned deliverer) — cell `--entry-pool 20 --stampers 0.6 --rules 2.8.0`, seeds 21-40, model `results/redteam/Q3/line-v4/models/wm-online-10.pt` (value mc, horizon 16)

| policy | lifetime real wealth | paired − careful | work decisions | bad share | miss share | nested awards | bad approved | bad caught | misses lapsed | good final N | bad approved rate | slot final-N rate | population final-N rate | guarantees forfeited (nominal) | effort saved (nominal) | slot ρ | awards | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 1566.8 ± 109.8 | -77.5 ± 98.5 | 126.8 | 0.001 | 0.000 | 0.000 | 0.050 | 0.050 | 0.000 | 27.600 | 0.500 | 0.220 | 0.208 | 292.800 | 0.480 | 0.883 | 126.900 | 0.00 |
| learned | 1491.0 ± 112.2 | -153.2 ± 116.2 | 120.2 | 0.071 | 0.000 | 0.000 | 0.100 | 8.650 | 0.000 | 23.850 | 0.011 | 0.272 | 0.212 | 332.300 | 68.954 | 0.886 | 120.300 | 0.05 |
| careful | 1644.3 ± 134.0 | nan ± nan | 125.5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 26.850 | — | 0.216 | 0.208 | 288.700 | 0.000 | 0.889 | 125.600 | 0.00 |
| zero | 50.0 ± 38.9 | -1594.3 ± 135.3 | 28.4 | 1.000 | 0.000 | 0.000 | 0.850 | 27.500 | 0.000 | 0.000 | 0.030 | 0.970 | 0.217 | 192.050 | 199.757 | 0.480 | 28.400 | 0.00 |

The boundary decisions (the exit the learner's own): leaves chosen and effected, the share of episodes whose learner had departed at the end; the boundary read ({br}: the stay head's one-step read against zero — its mean and the boundaries it read negative — or learned).

| policy | boundary decisions | leaves chosen | leaves effected | departed | stay read (mean) | stay read < 0 |
|---|---|---|---|---|---|---|
| greedy | 11.600 | 0.100 | 0.000 | 0.000 | 58.725 | 0.100 |
| learned | 11.250 | 0.150 | 0.050 | 0.050 | 50.481 | 0.150 |
| careful | 11.600 | 0.000 | 0.000 | 0.000 | — | — |
| zero | 11.500 | 0.000 | 0.000 | 0.000 | — | — |

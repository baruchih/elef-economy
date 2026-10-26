# Evaluation (Q3, the learned deliverer) — cell `--entry-pool 20 --stampers 0.6`, seeds 21-40, model `results/redteam/Q3/line-v4/models/wm-online-10.pt` (value mc, horizon 16)

| policy | lifetime real wealth | paired − careful | work decisions | bad share | miss share | nested awards | bad approved | bad caught | misses lapsed | good final N | bad approved rate | slot final-N rate | population final-N rate | guarantees forfeited (nominal) | effort saved (nominal) | slot ρ | awards | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 1701.2 ± 106.4 | 22.8 ± 40.7 | 127.0 | 0.001 | 0.000 | 0.000 | 0.050 | 0.050 | 0.000 | 25.700 | 0.500 | 0.205 | 0.208 | 281.850 | 0.480 | 0.884 | 127.100 | 0.00 |
| learned | 1505.5 ± 114.0 | -172.9 ± 96.1 | 122.7 | 0.066 | 0.000 | 0.000 | 0.150 | 7.950 | 0.000 | 25.150 | 0.019 | 0.274 | 0.216 | 346.050 | 61.080 | 0.875 | 122.700 | 0.00 |
| careful | 1678.4 ± 107.2 | nan ± nan | 126.8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 26.050 | — | 0.208 | 0.208 | 282.400 | 0.000 | 0.887 | 126.800 | 0.00 |
| zero | 10.8 ± 6.9 | -1667.7 ± 108.6 | 32.8 | 1.000 | 0.000 | 0.000 | 1.200 | 31.550 | 0.000 | 0.000 | 0.037 | 0.963 | 0.216 | 259.150 | 253.710 | 0.469 | 32.800 | 0.00 |

The boundary decisions (the exit the learner's own): leaves chosen and effected, the share of episodes whose learner had departed at the end; the boundary read ({br}: the stay head's one-step read against zero — its mean and the boundaries it read negative — or learned).

| policy | boundary decisions | leaves chosen | leaves effected | departed | stay read (mean) | stay read < 0 |
|---|---|---|---|---|---|---|
| greedy | 11.700 | 0.350 | 0.000 | 0.000 | 61.514 | 0.350 |
| learned | 11.900 | 0.450 | 0.000 | 0.000 | 54.322 | 0.450 |
| careful | 11.700 | 0.000 | 0.000 | 0.000 | — | — |
| zero | 11.650 | 0.000 | 0.000 | 0.000 | — | — |

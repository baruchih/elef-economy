# Evaluation (Q3, the learned deliverer) — cell `--entry-pool 20 --stampers 0.6`, seeds 21-40, model `results/redteam/Q3/line-v4/models/wm-online-10.pt` (value mc, horizon 16)

| policy | lifetime real wealth | paired − careful | work decisions | bad share | miss share | nested awards | bad approved | bad caught | misses lapsed | good final N | bad approved rate | slot final-N rate | population final-N rate | guarantees forfeited (nominal) | effort saved (nominal) | slot ρ | awards | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 1755.2 ± 107.7 | 35.5 ± 29.0 | 123.0 | 0.001 | 0.000 | 0.000 | 0.050 | 0.050 | 0.000 | 25.250 | 0.500 | 0.208 | 0.208 | 267.050 | 0.480 | 0.898 | 123.100 | 0.05 |
| learned | 1519.1 ± 134.8 | -200.6 ± 104.2 | 112.5 | 0.087 | 0.000 | 0.000 | 0.150 | 9.400 | 0.000 | 20.900 | 0.016 | 0.271 | 0.213 | 310.700 | 75.277 | 0.872 | 112.450 | 0.05 |
| careful | 1719.7 ± 106.7 | nan ± nan | 124.3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 25.750 | — | 0.209 | 0.207 | 273.050 | 0.000 | 0.898 | 124.350 | 0.00 |
| zero | 9.2 ± 8.4 | -1710.5 ± 110.4 | 28.2 | 1.000 | 0.000 | 0.000 | 0.900 | 27.350 | 0.000 | 0.000 | 0.032 | 0.968 | 0.220 | 210.100 | 224.007 | 0.458 | 28.250 | 0.00 |

The boundary decisions (the exit the learner's own): leaves chosen and effected, the share of episodes whose learner had departed at the end; the boundary read ({br}: the stay head's one-step read against zero — its mean and the boundaries it read negative — or learned).

| policy | boundary decisions | leaves chosen | leaves effected | departed | stay read (mean) | stay read < 0 |
|---|---|---|---|---|---|---|
| greedy | 11.550 | 0.150 | 0.050 | 0.050 | 53.615 | 0.150 |
| learned | 11.250 | 0.500 | 0.050 | 0.050 | 52.606 | 0.500 |
| careful | 11.350 | 0.000 | 0.000 | 0.000 | — | — |
| zero | 11.400 | 0.000 | 0.000 | 0.000 | — | — |

# Evaluation (Q5, the learned child) — cell `--entry-pool 20 --stampers 0.6 --delegation on --c-d-sigma 0.8 --child-prefers-nested on --parent-judge stamp --audit-roll off --effort-cost 2`, seeds 21-40, model `None` (value off, horizon 8)

| policy | lifetime real wealth | paired − careful | work decisions | bad share | miss share | nested awards | bad approved | bad caught | misses lapsed | good final N | bad approved rate | slot final-N rate | population final-N rate | guarantees forfeited (nominal) | effort saved (nominal) | slot ρ | awards | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 963.9 ± 66.0 | 225.6 ± 50.5 | 48.4 | 1.000 | 0.000 | 48.400 | 48.100 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 | 0.185 | 0.000 | 451.334 | 0.956 | 48.400 | 0.00 |
| careful | 738.3 ± 49.3 | nan ± nan | 59.5 | 0.000 | 0.000 | 59.550 | 0.000 | 0.000 | 0.000 | 0.000 | — | 0.000 | 0.172 | 0.000 | 0.000 | 0.961 | 59.550 | 0.00 |
| zero | 956.6 ± 63.2 | 218.3 ± 49.7 | 48.6 | 1.000 | 0.000 | 48.600 | 48.300 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 | 0.185 | 0.000 | 452.628 | 0.956 | 48.600 | 0.00 |

The boundary decisions (the exit the learner's own): leaves chosen and effected, the share of episodes whose learner had departed at the end.

| policy | boundary decisions | leaves chosen | leaves effected | departed |
|---|---|---|---|---|
| direct | 10.750 | 0.000 | 0.000 | 0.000 |
| careful | 11.000 | 0.000 | 0.000 | 0.000 |
| zero | 10.750 | 0.000 | 0.000 | 0.000 |

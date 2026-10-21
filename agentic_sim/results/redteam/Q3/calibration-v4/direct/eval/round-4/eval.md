# Evaluation (Q3, the learned deliverer) — cell `--entry-pool 20 --stampers 1.0 --entry-stampers 1.0 --pi0 0 --dial off --audit-roll off`, seeds 21-40, model `None` (value off, horizon 16)

| policy | lifetime real wealth | paired − careful | work decisions | bad share | bad approved | bad caught | good final N | bad approved rate | slot final-N rate | population final-N rate | guarantees forfeited (nominal) | effort saved (nominal) | slot ρ | awards | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 3503.5 ± 156.9 | 1541.2 ± 113.2 | 136.8 | 1.000 | 135.000 | 0.000 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 1089.908 | 0.990 | 136.800 | 0.00 |
| careful | 1962.4 ± 154.3 | nan ± nan | 136.8 | 0.000 | 0.000 | 0.000 | 0.000 | — | 0.000 | 0.000 | 0.000 | 0.000 | 0.990 | 136.800 | 0.00 |
| zero | 3503.5 ± 156.9 | 1541.2 ± 113.2 | 136.8 | 1.000 | 135.000 | 0.000 | 0.000 | 1.000 | 0.000 | 0.000 | 0.000 | 1089.908 | 0.990 | 136.800 | 0.00 |

The boundary decisions (the exit the learner's own): leaves chosen and effected, the share of episodes whose learner had departed at the end.

| policy | boundary decisions | leaves chosen | leaves effected | departed |
|---|---|---|---|---|
| direct | 4.000 | 0.000 | 0.000 | 0.000 |
| careful | 4.000 | 0.000 | 0.000 | 0.000 |
| zero | 4.000 | 0.000 | 0.000 | 0.000 |

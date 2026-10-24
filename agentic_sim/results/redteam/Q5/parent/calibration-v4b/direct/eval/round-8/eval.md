# Evaluation (Q5, the learned parent) — cell `--entry-pool 20 --stampers 0.6 --delegation on --c-d-sigma 0.8 --parent-slot costliest --child-appeal none --audit-roll off --child-g-frac 2.0`, seeds 21-40, model `None` (value off, horizon 16)

| policy | lifetime real | paired − careful | delegate decisions | delegate share | judge decisions | judge care / stamp / reject | cancel decisions | cancel share | children settled | guarantees taken (nominal) | child lapses | rejections overturned | kill fees | bad stamped / good rejected | slot ρ | awards | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 939.6 ± 105.9 | 229.6 ± 107.3 | 65.700 | 0.510 | 22.350 | 0.000 / 0.000 / 1.000 | 22.650 | 0.014 | 22.350 | 504.800 | 0.000 | 0.000 | 0.000 | 0.000 / 18.000 | 0.893 | 65.800 | 0.00 |
| careful | 710.0 ± 67.1 | nan ± nan | 57.150 | 0.867 | 21.300 | 1.000 / 0.000 / 0.000 | 21.300 | 0.000 | 21.300 | 129.950 | 0.000 | 0.000 | 0.000 | 0.000 / 0.000 | 0.900 | 57.400 | 0.00 |
| rejecter | 1012.2 ± 88.7 | 302.2 ± 98.8 | 53.900 | 1.000 | 27.750 | 0.000 / 0.000 / 1.000 | 27.750 | 0.000 | 27.750 | 632.600 | 0.000 | 0.000 | 0.000 | 0.000 / 22.400 | 0.912 | 53.900 | 0.00 |

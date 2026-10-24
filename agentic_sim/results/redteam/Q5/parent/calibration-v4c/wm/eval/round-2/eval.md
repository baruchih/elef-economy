# Evaluation (Q5, the learned parent) — cell `--entry-pool 20 --stampers 0.6 --delegation on --c-d-sigma 0.8 --parent-slot costliest --child-appeal none --audit-roll off --child-g-frac 2.0`, seeds 21-40, model `results/redteam/Q5/parent/calibration-v4c/wm/models/wm-online-2.pt` (value mc, horizon 16)

| policy | lifetime real | paired − careful | delegate decisions | delegate share | judge decisions | judge care / stamp / reject | cancel decisions | cancel share | children settled | guarantees taken (nominal) | child lapses | rejections overturned | kill fees | bad stamped / good rejected | slot ρ | awards | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 640.9 ± 118.9 | -69.1 ± 101.6 | 43.700 | 0.701 | 11.600 | 0.079 / 0.284 / 0.637 | 12.800 | 0.084 | 11.600 | 171.450 | 0.000 | 0.000 | 0.000 | 0.650 / 6.150 | 0.905 | 44.850 | 0.70 |
| careful | 710.0 ± 67.1 | nan ± nan | 57.150 | 0.867 | 21.300 | 1.000 / 0.000 / 0.000 | 21.300 | 0.000 | 21.300 | 129.950 | 0.000 | 0.000 | 0.000 | 0.000 / 0.000 | 0.900 | 57.400 | 0.00 |
| rejecter | 1012.2 ± 88.7 | 302.2 ± 98.8 | 53.900 | 1.000 | 27.750 | 0.000 / 0.000 / 1.000 | 27.750 | 0.000 | 27.750 | 632.600 | 0.000 | 0.000 | 0.000 | 0.000 / 22.400 | 0.912 | 53.900 | 0.00 |

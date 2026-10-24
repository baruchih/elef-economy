# Evaluation (Q5, the learned parent) — cell `--entry-pool 20 --stampers 0.6 --delegation on --c-d-sigma 0.8 --parent-slot costliest --child-appeal none --audit-roll off --child-g-frac 2.0`, seeds 21-40, model `results/redteam/Q5/parent/calibration-v4b/wm/models/wm-online-10.pt` (value mc, horizon 16)

| policy | lifetime real | paired − careful | delegate decisions | delegate share | judge decisions | judge care / stamp / reject | cancel decisions | cancel share | children settled | guarantees taken (nominal) | child lapses | rejections overturned | kill fees | bad stamped / good rejected | slot ρ | awards | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 703.7 ± 80.9 | -6.3 ± 74.8 | 63.500 | 0.397 | 11.000 | 0.210 / 0.007 / 0.784 | 12.600 | 0.197 | 11.000 | 206.750 | 0.000 | 0.000 | 0.000 | 0.000 / 6.700 | 0.901 | 65.900 | 0.05 |
| greedy | 702.9 ± 94.0 | -7.1 ± 90.4 | 74.200 | 0.097 | 6.050 | 0.004 / 0.000 / 0.996 | 6.100 | 0.003 | 6.050 | 113.150 | 0.000 | 0.000 | 0.000 | 0.000 / 5.000 | 0.899 | 74.600 | 0.00 |
| careful | 710.0 ± 67.1 | nan ± nan | 57.150 | 0.867 | 21.300 | 1.000 / 0.000 / 0.000 | 21.300 | 0.000 | 21.300 | 129.950 | 0.000 | 0.000 | 0.000 | 0.000 / 0.000 | 0.900 | 57.400 | 0.00 |
| rejecter | 1012.2 ± 88.7 | 302.2 ± 98.8 | 53.900 | 1.000 | 27.750 | 0.000 / 0.000 / 1.000 | 27.750 | 0.000 | 27.750 | 632.600 | 0.000 | 0.000 | 0.000 | 0.000 / 22.400 | 0.912 | 53.900 | 0.00 |
| selective | 968.4 ± 106.2 | 258.4 ± 109.2 | 54.900 | 1.000 | 28.600 | 0.049 / 0.000 / 0.951 | 28.600 | 0.000 | 28.600 | 697.250 | 0.000 | 0.000 | 0.000 | 0.000 / 21.750 | 0.893 | 54.950 | 0.00 |

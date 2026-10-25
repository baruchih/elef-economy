# Evaluation (Q5, the learned parent) — cell `--entry-pool 20 --stampers 0.6 --delegation on --c-d-sigma 0.8 --parent-slot costliest`, seeds 21-40, model `results/redteam/Q5/parent/line-v4d/models/wm-online-10.pt` (value mc, horizon 16)

| policy | lifetime real | paired − careful | delegate decisions | delegate share | judge decisions | judge care / stamp / reject | cancel decisions | cancel share | children settled | guarantees taken (nominal) | child lapses | rejections overturned | kill fees | bad stamped / good rejected | slot ρ | awards | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 511.9 ± 83.1 | -190.8 ± 82.7 | 43.950 | 0.670 | 7.750 | 0.351 / 0.543 / 0.106 | 11.300 | 0.390 | 7.750 | 9.050 | 0.000 | 0.750 | 0.000 | 0.450 / 0.750 | 0.913 | 43.950 | 0.25 |
| greedy | 402.0 ± 86.0 | -300.7 ± 113.3 | 53.850 | 0.186 | 0.000 | — / — / — | 5.050 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 / 0.000 | 0.911 | 53.950 | 0.40 |
| careful | 702.7 ± 111.0 | nan ± nan | 48.200 | 0.866 | 18.050 | 1.000 / 0.000 / 0.000 | 18.050 | 0.000 | 18.050 | 26.950 | 0.000 | 0.000 | 0.000 | 0.000 / 0.000 | 0.888 | 48.250 | 0.00 |
| rejecter | 211.3 ± 71.3 | -491.5 ± 100.6 | 20.650 | 1.000 | 4.700 | 0.000 / 0.000 / 1.000 | 4.700 | 0.000 | 4.650 | 4.400 | 0.000 | 3.850 | 0.000 | 0.000 / 4.000 | 0.807 | 20.800 | 0.00 |
| stamper | 631.8 ± 66.3 | -70.9 ± 101.4 | 41.400 | 1.000 | 12.050 | 0.000 / 1.000 / 0.000 | 12.050 | 0.000 | 12.050 | 15.450 | 0.000 | 0.000 | 0.000 | 2.700 / 0.000 | 0.894 | 41.500 | 0.00 |
| selective | 300.0 ± 63.8 | -402.7 ± 99.6 | 28.800 | 1.000 | 8.050 | 0.336 / 0.000 / 0.664 | 8.050 | 0.000 | 8.050 | 8.500 | 0.000 | 4.450 | 0.000 | 0.000 / 4.500 | 0.834 | 28.850 | 0.00 |

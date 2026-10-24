# Evaluation (Q5, the learned parent) — cell `--entry-pool 20 --stampers 0.6 --delegation on --c-d-sigma 0.8 --parent-slot costliest`, seeds 21-40, model `results/redteam/Q5/parent/line-v4/models/wm-online-10.pt` (value mc, horizon 16)

| policy | lifetime real | paired − careful | delegate decisions | delegate share | judge decisions | judge care / stamp / reject | cancel decisions | cancel share | children settled | guarantees taken (nominal) | child lapses | rejections overturned | kill fees | bad stamped / good rejected | slot ρ | awards | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 494.5 ± 90.6 | -208.3 ± 95.1 | 47.100 | 0.517 | 1.750 | 0.367 / 0.534 / 0.099 | 7.950 | 0.776 | 1.750 | 3.600 | 0.000 | 0.200 | 0.000 | 0.200 / 0.250 | 0.917 | 47.200 | 0.45 |
| greedy | 643.5 ± 65.7 | -59.3 ± 87.3 | 61.550 | 0.567 | 0.000 | — / — / — | 12.650 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 / 0.000 | 0.911 | 61.600 | 0.05 |
| careful | 702.7 ± 111.0 | nan ± nan | 48.200 | 0.866 | 18.050 | 1.000 / 0.000 / 0.000 | 18.050 | 0.000 | 18.050 | 26.950 | 0.000 | 0.000 | 0.000 | 0.000 / 0.000 | 0.888 | 48.250 | 0.00 |
| rejecter | 211.3 ± 71.3 | -491.5 ± 100.6 | 20.650 | 1.000 | 4.700 | 0.000 / 0.000 / 1.000 | 4.700 | 0.000 | 4.650 | 4.400 | 0.000 | 3.850 | 0.000 | 0.000 / 4.000 | 0.807 | 20.800 | 0.00 |
| stamper | 631.8 ± 66.3 | -70.9 ± 101.4 | 41.400 | 1.000 | 12.050 | 0.000 / 1.000 / 0.000 | 12.050 | 0.000 | 12.050 | 15.450 | 0.000 | 0.000 | 0.000 | 2.700 / 0.000 | 0.894 | 41.500 | 0.00 |
| selective | 300.0 ± 63.8 | -402.7 ± 99.6 | 28.800 | 1.000 | 8.050 | 0.336 / 0.000 / 0.664 | 8.050 | 0.000 | 8.050 | 8.500 | 0.000 | 4.450 | 0.000 | 0.000 / 4.500 | 0.834 | 28.850 | 0.00 |

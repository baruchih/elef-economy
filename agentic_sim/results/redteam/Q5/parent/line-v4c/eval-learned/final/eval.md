# Evaluation (Q5, the learned parent) — cell `--entry-pool 20 --stampers 0.6 --delegation on --c-d-sigma 0.8 --parent-slot costliest`, seeds 21-40, model `results/redteam/Q5/parent/line-v4c/models/wm-online-10.pt` (value mc, horizon 16)

| policy | lifetime real | paired − careful | delegate decisions | delegate share | judge decisions | judge care / stamp / reject | cancel decisions | cancel share | children settled | guarantees taken (nominal) | child lapses | rejections overturned | kill fees | bad stamped / good rejected | slot ρ | awards | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 315.0 ± 88.6 | -387.7 ± 82.3 | 35.800 | 0.271 | 2.500 | 0.308 / 0.470 / 0.222 | 3.850 | 0.451 | 2.500 | 3.150 | 0.000 | 0.100 | 0.000 | 0.250 / 0.100 | 0.912 | 35.850 | 0.95 |
| greedy | 287.5 ± 73.2 | -415.2 ± 85.5 | 39.500 | 0.420 | 0.000 | — / — / — | 3.800 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 / 0.000 | 0.897 | 39.500 | 0.80 |
| careful | 702.7 ± 111.0 | nan ± nan | 48.200 | 0.866 | 18.050 | 1.000 / 0.000 / 0.000 | 18.050 | 0.000 | 18.050 | 26.950 | 0.000 | 0.000 | 0.000 | 0.000 / 0.000 | 0.888 | 48.250 | 0.00 |
| rejecter | 211.3 ± 71.3 | -491.5 ± 100.6 | 20.650 | 1.000 | 4.700 | 0.000 / 0.000 / 1.000 | 4.700 | 0.000 | 4.650 | 4.400 | 0.000 | 3.850 | 0.000 | 0.000 / 4.000 | 0.807 | 20.800 | 0.00 |
| stamper | 631.8 ± 66.3 | -70.9 ± 101.4 | 41.400 | 1.000 | 12.050 | 0.000 / 1.000 / 0.000 | 12.050 | 0.000 | 12.050 | 15.450 | 0.000 | 0.000 | 0.000 | 2.700 / 0.000 | 0.894 | 41.500 | 0.00 |
| selective | 300.0 ± 63.8 | -402.7 ± 99.6 | 28.800 | 1.000 | 8.050 | 0.336 / 0.000 / 0.664 | 8.050 | 0.000 | 8.050 | 8.500 | 0.000 | 4.450 | 0.000 | 0.000 / 4.500 | 0.834 | 28.850 | 0.00 |

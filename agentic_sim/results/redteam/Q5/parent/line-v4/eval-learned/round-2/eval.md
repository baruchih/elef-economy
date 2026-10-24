# Evaluation (Q5, the learned parent) — cell `--entry-pool 20 --stampers 0.6 --delegation on --c-d-sigma 0.8 --parent-slot costliest`, seeds 21-40, model `results/redteam/Q5/parent/line-v4/models/wm-online-2.pt` (value mc, horizon 16)

| policy | lifetime real | paired − careful | delegate decisions | delegate share | judge decisions | judge care / stamp / reject | cancel decisions | cancel share | children settled | guarantees taken (nominal) | child lapses | rejections overturned | kill fees | bad stamped / good rejected | slot ρ | awards | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 602.3 ± 64.3 | -100.5 ± 100.6 | 60.700 | 0.628 | 0.000 | — / — / — | 14.650 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 / 0.000 | 0.916 | 60.800 | 0.10 |
| careful | 702.7 ± 111.0 | nan ± nan | 48.200 | 0.866 | 18.050 | 1.000 / 0.000 / 0.000 | 18.050 | 0.000 | 18.050 | 26.950 | 0.000 | 0.000 | 0.000 | 0.000 / 0.000 | 0.888 | 48.250 | 0.00 |

# Evaluation (Q5, the learned parent) — cell `--entry-pool 20 --stampers 0.6 --delegation on --c-d-sigma 0.8 --parent-slot costliest`, seeds 21-40, model `results/redteam/Q5/parent/line-v4d/models/wm-online-4.pt` (value mc, horizon 16)

| policy | lifetime real | paired − careful | delegate decisions | delegate share | judge decisions | judge care / stamp / reject | cancel decisions | cancel share | children settled | guarantees taken (nominal) | child lapses | rejections overturned | kill fees | bad stamped / good rejected | slot ρ | awards | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 444.8 ± 85.6 | -258.0 ± 78.7 | 48.250 | 0.587 | 3.650 | 0.248 / 0.752 / 0.000 | 10.500 | 0.659 | 3.650 | 4.500 | 0.000 | 0.000 | 0.000 | 0.700 / 0.000 | 0.900 | 48.300 | 0.20 |
| careful | 702.7 ± 111.0 | nan ± nan | 48.200 | 0.866 | 18.050 | 1.000 / 0.000 / 0.000 | 18.050 | 0.000 | 18.050 | 26.950 | 0.000 | 0.000 | 0.000 | 0.000 / 0.000 | 0.888 | 48.250 | 0.00 |

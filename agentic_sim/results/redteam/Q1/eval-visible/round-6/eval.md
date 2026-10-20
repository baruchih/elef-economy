# Evaluation — cell `--entry-pool 20 --stampers 0.6`, seeds 21-40, hide ``, model `results/redteam/Q1/models/visible/wm-online-6.pt` (value mc, horizon 16)

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate | real stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 691.8 ± 101.6 | -615.9 ± 147.5 | 72.8 | 0.133 | 0.372 | 0.495 | 0.827 | 0.854 | 10.85 | 4.90 | 0.90 |
| careful | 1307.7 ± 123.2 | nan ± nan | 150.9 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 12.15 | 0.00 | 0.15 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 0.992 | 0.980 | — (0) | 0.600 (30) | 0.159 (44) | 0.453 (75) | 0.449 (1306) | 0.800 | 0.000 | — | 6.125 |
| careful | — | 0.789 | — (0) | 0.000 (511) | 0.000 (875) | 0.000 (419) | 0.000 (1213) | 0.000 | 0.000 | — | — |

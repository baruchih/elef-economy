# Evaluation — cell `--entry-pool 20 --stampers 0.6`, seeds 21-40, hide ``, model `results/redteam/Q1/models/visible-td/wm-online-8.pt` (value td, horizon 16)

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate | real stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 727.1 ± 118.0 | -580.6 ± 163.7 | 85.0 | 0.386 | 0.174 | 0.439 | 0.678 | 0.604 | 11.10 | 3.25 | 0.70 |
| careful | 1307.7 ± 123.2 | nan ± nan | 150.9 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 12.15 | 0.00 | 0.15 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 0.964 | 0.935 | — (0) | 0.106 (160) | 0.012 (171) | 0.108 (139) | 0.232 (1229) | 0.400 | 0.000 | — | 8.125 |
| careful | — | 0.789 | — (0) | 0.000 (511) | 0.000 (875) | 0.000 (419) | 0.000 (1213) | 0.000 | 0.000 | — | — |

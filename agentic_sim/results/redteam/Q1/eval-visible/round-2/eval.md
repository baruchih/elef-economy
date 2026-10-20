# Evaluation — cell `--entry-pool 20 --stampers 0.6`, seeds 21-40, hide ``, model `results/redteam/Q1/models/visible/wm-online-2.pt` (value mc, horizon 16)

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate | real stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 759.7 ± 87.3 | -548.0 ± 153.9 | 68.0 | 0.350 | 0.383 | 0.267 | 0.692 | 0.671 | 12.15 | 4.10 | 0.95 |
| careful | 1307.7 ± 123.2 | nan ± nan | 150.9 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 12.15 | 0.00 | 0.15 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 0.971 | 0.978 | 0.000 (3) | 1.000 (6) | 0.688 (80) | 0.355 (124) | 0.450 (1148) | 0.700 | 0.000 | — | 5.857 |
| careful | — | 0.789 | — (0) | 0.000 (511) | 0.000 (875) | 0.000 (419) | 0.000 (1213) | 0.000 | 0.000 | — | — |

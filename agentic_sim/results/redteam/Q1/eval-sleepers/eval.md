# Evaluation — cell `--entry-pool 20 --stampers 0.6`, seeds 21-40, hide ``, model `None` (value off, horizon 8)

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate | real stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|
| careful | 1307.7 ± 123.2 | nan ± nan | 150.9 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 12.15 | 0.00 | 0.15 |
| stamper | 269.5 ± 55.5 | -1038.2 ± 121.1 | 31.8 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 10.65 | 6.10 | 1.00 |
| sleeper0.3 | 1307.7 ± 123.2 | 0.0 ± 0.0 | 150.9 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 12.15 | 0.00 | 0.15 |
| sleeper0.5 | 1295.3 ± 119.4 | -12.3 ± 22.9 | 153.7 | 0.909 | 0.091 | 0.000 | 0.080 | 0.106 | 12.45 | 1.45 | 0.15 |
| sleeper0.7 | 1207.4 ± 109.8 | -100.3 ± 40.4 | 143.5 | 0.830 | 0.170 | 0.000 | 0.221 | 0.193 | 13.30 | 3.85 | 0.25 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| careful | — | 0.789 | — (0) | 0.000 (511) | 0.000 (875) | 0.000 (419) | 0.000 (1213) | 0.000 | 0.000 | — | — |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (636) | 0.700 | 0.000 | — | 8.714 |
| sleeper0.3 | — | 0.789 | — (0) | 0.000 (511) | 0.000 (875) | 0.000 (419) | 0.000 (1213) | 0.000 | 0.000 | — | — |
| sleeper0.5 | 0.446 | 0.855 | — (0) | 1.000 (314) | 0.000 (845) | 0.000 (645) | 0.000 (1270) | 0.000 | 0.000 | — | — |
| sleeper0.7 | 0.577 | 0.961 | — (0) | 1.000 (87) | 1.000 (483) | 0.000 (516) | 0.000 (1784) | 0.000 | 0.000 | — | — |

# Evaluation — cell `--entry-pool 20 --stampers 0.6`, seeds 21-40, hide ``, model `results/redteam/Q1/models/visible/wm-online-10.pt` (value mc, horizon 16)

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate | real stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 584.9 ± 72.1 | -722.8 ± 133.3 | 48.2 | 0.084 | 0.336 | 0.580 | 0.923 | 0.906 | 11.90 | 2.90 | 0.95 |
| greedy | 693.7 ± 86.2 | -614.0 ± 125.8 | 72.8 | 0.298 | 0.198 | 0.504 | 0.640 | 0.725 | 12.55 | 2.20 | 0.85 |
| careful | 1307.7 ± 123.2 | nan ± nan | 150.9 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 12.15 | 0.00 | 0.15 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 1.000 | 0.989 | — (0) | 0.000 (30) | 0.000 (9) | 0.263 (19) | 0.389 (906) | 0.850 | 0.000 | — | 3.412 |
| greedy | 0.980 | 0.951 | — (0) | 0.031 (64) | 0.057 (158) | 0.165 (97) | 0.233 (1138) | 0.600 | 0.000 | — | 3.667 |
| careful | — | 0.789 | — (0) | 0.000 (511) | 0.000 (875) | 0.000 (419) | 0.000 (1213) | 0.000 | 0.000 | — | — |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| learned | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.950 | 0.000 |
| greedy | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.850 | 0.000 |
| careful | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.150 | 0.000 |

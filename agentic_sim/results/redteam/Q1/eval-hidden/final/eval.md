# Evaluation — cell `--entry-pool 20 --stampers 0.6`, seeds 21-40, hide `own_p_eff`, model `results/redteam/Q1/models/hidden/wm-online-10.pt` (value mc, horizon 16)

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate | real stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 834.4 ± 127.4 | -473.3 ± 180.0 | 93.6 | 0.352 | 0.230 | 0.417 | 0.582 | 0.599 | 11.00 | 3.30 | 0.75 |
| greedy | 875.3 ± 113.5 | -432.4 ± 155.4 | 103.3 | 0.375 | 0.209 | 0.416 | 0.611 | 0.656 | 12.50 | 2.80 | 0.60 |
| careful | 1307.7 ± 123.2 | nan ± nan | 150.9 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 12.15 | 0.00 | 0.15 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 0.942 | 0.938 | — (0) | 0.217 (83) | 0.142 (289) | 0.195 (220) | 0.247 (1280) | 0.450 | 0.000 | — | 7.333 |
| greedy | 0.950 | 0.918 | 0.231 (13) | 0.190 (126) | 0.110 (336) | 0.237 (270) | 0.265 (1322) | 0.250 | 0.000 | — | 11.200 |
| careful | — | 0.789 | — (0) | 0.000 (511) | 0.000 (875) | 0.000 (419) | 0.000 (1213) | 0.000 | 0.000 | — | — |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| learned | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.750 | 0.000 |
| greedy | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.600 | 0.000 |
| careful | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.150 | 0.000 |

# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-rearrive on`, seeds 21-40, hide ``, model `results/redteam/Q1/rearrive-2.7.0/models/wm-online-8.pt` (value mc, horizon 16)

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate | real stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 1149.7 ± 98.0 | -507.8 ± 89.6 | 179.7 | 0.664 | 0.221 | 0.116 | 0.352 | 0.337 | 12.15 | 5.35 | 0.75 |
| careful | 1657.5 ± 101.4 | nan ± nan | 190.5 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 11.05 | 0.00 | 0.25 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 0.954 | 0.928 | 0.452 (31) | 0.125 (192) | 0.169 (225) | 0.167 (239) | 0.232 (2906) | 5.700 | 0.600 | — | 0.939 |
| careful | — | 0.789 | — (0) | 0.000 (486) | 0.000 (787) | 0.000 (898) | 0.000 (1639) | 0.300 | 0.250 | — | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| learned | 4.600 | 3.600 | 0.750 | 2.500 | 180.000 | 0.000 | 12.500 |
| careful | 1.250 | 0.250 | 0.000 | 0.000 | 12.500 | 0.000 | 12.150 |

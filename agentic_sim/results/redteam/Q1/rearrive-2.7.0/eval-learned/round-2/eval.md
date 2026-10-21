# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-rearrive on`, seeds 21-40, hide ``, model `results/redteam/Q1/rearrive-2.7.0/models/wm-online-2.pt` (value mc, horizon 16)

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate | real stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 807.2 ± 78.7 | -850.4 ± 83.2 | 145.5 | 0.413 | 0.323 | 0.264 | 0.584 | 0.570 | 11.80 | 6.55 | 0.95 |
| careful | 1657.5 ± 101.4 | nan ± nan | 190.5 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 11.05 | 0.00 | 0.25 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 0.997 | 0.995 | — (0) | — (0) | 0.156 (32) | 0.029 (34) | 0.318 (2844) | 9.750 | 0.950 | 228.833 | 0.672 |
| careful | — | 0.789 | — (0) | 0.000 (486) | 0.000 (787) | 0.000 (898) | 0.000 (1639) | 0.300 | 0.250 | — | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| learned | 6.550 | 5.550 | 0.850 | 3.550 | 277.500 | 0.000 | 12.200 |
| careful | 1.250 | 0.250 | 0.000 | 0.000 | 12.500 | 0.000 | 12.150 |

# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-rearrive on`, seeds 21-40, hide ``, model `None` (value off, horizon 8)

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate | real stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|
| careful | 1438.2 ± 88.1 | nan ± nan | 171.2 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 11.90 | 0.00 | 0.15 |
| stamper | 790.7 ± 38.5 | -647.5 ± 85.2 | 92.8 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 10.75 | 16.95 | 1.00 |
| harvester | 1325.6 ± 37.9 | -112.6 ± 89.9 | 95.5 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 10.85 | 16.00 | 1.00 |
| leaver | 1510.2 ± 88.3 | 72.0 ± 29.4 | 174.3 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 11.30 | 0.00 | 0.50 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| careful | — | 0.749 | — (0) | 0.000 (654) | 0.000 (960) | 0.000 (475) | 0.000 (1335) | 0.350 | 0.150 | — | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (1855) | 19.850 | 0.000 | — | 0.854 |
| harvester | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (1909) | 21.350 | 0.000 | — | 0.749 |
| leaver | — | 0.782 | — (0) | 0.000 (470) | 0.000 (956) | 0.000 (505) | 0.000 (1555) | 1.250 | 0.550 | 273.000 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| careful | 1.250 | 0.250 | 0.000 | 0.000 | 12.500 | 0.000 | 11.700 |
| stamper | 10.400 | 9.400 | 0.000 | 0.000 | 470.000 | 0.000 | 12.100 |
| harvester | 20.850 | 19.850 | 10.350 | 2.150 | 992.500 | 0.000 | 12.500 |
| leaver | 2.400 | 1.400 | 1.050 | 10.750 | 70.000 | 0.000 | 11.800 |

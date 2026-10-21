# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-rearrive on`, seeds 21-40, hide ``, model `results/redteam/Q1/rearrive-visible/models/wm-online-10.pt` (value mc, horizon 16)

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate | real stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 458.7 ± 62.6 | -1198.8 ± 95.2 | 150.4 | 0.248 | 0.384 | 0.368 | 0.758 | 0.728 | 11.30 | 8.55 | 0.95 |
| harvester | 454.1 ± 60.7 | -1203.4 ± 113.7 | 89.2 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 11.80 | 15.20 | 1.00 |
| leaver | 1691.4 ± 84.8 | 33.9 ± 30.7 | 192.9 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 11.00 | 0.00 | 0.40 |
| stamper | 487.4 ± 66.2 | -1170.1 ± 116.7 | 88.0 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 11.75 | 14.95 | 1.00 |
| careful | 1657.5 ± 101.4 | nan ± nan | 190.5 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 11.05 | 0.00 | 0.25 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 0.987 | 0.981 | 0.373 (67) | 0.000 (19) | 0.000 (31) | 0.154 (65) | 0.376 (2827) | 14.100 | 0.400 | 188.000 | 0.606 |
| harvester | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (1784) | 22.100 | 0.000 | — | 0.688 |
| leaver | — | 0.808 | — (0) | 0.000 (466) | 0.000 (726) | 0.000 (802) | 0.000 (1865) | 0.850 | 0.450 | 346.000 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (1761) | 21.000 | 0.000 | — | 0.712 |
| careful | — | 0.789 | — (0) | 0.000 (486) | 0.000 (787) | 0.000 (898) | 0.000 (1639) | 0.300 | 0.250 | — | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| learned | 15.400 | 14.400 | 7.450 | 2.100 | 720.000 | 0.000 | 12.250 |
| harvester | 21.650 | 20.650 | 10.700 | 1.750 | 1032.500 | 0.000 | 12.450 |
| leaver | 2.000 | 1.000 | 0.700 | 11.350 | 50.000 | 0.000 | 12.050 |
| stamper | 11.050 | 10.050 | 0.000 | 0.000 | 502.500 | 0.000 | 12.500 |
| careful | 1.250 | 0.250 | 0.000 | 0.000 | 12.500 | 0.000 | 12.150 |

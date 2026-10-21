# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-rearrive on --arrival-loan off`, seeds 21-40, hide ``, model `results/redteam/Q1/rearrive-visible/models/wm-online-10.pt` (value mc, horizon 16)

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate | real stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 1367.3 ± 55.9 | -343.4 ± 114.5 | 136.1 | 0.301 | 0.380 | 0.319 | 0.754 | 0.668 | 10.00 | 6.85 | 1.00 |
| harvester | 1481.3 ± 48.2 | -229.4 ± 115.7 | 88.8 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 10.60 | 14.65 | 1.00 |
| leaver | 1784.9 ± 110.9 | 74.2 ± 45.6 | 192.4 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 11.70 | 0.00 | 0.40 |
| stamper | 993.4 ± 51.4 | -717.3 ± 115.2 | 89.2 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 11.25 | 14.70 | 1.00 |
| careful | 1710.7 ± 108.8 | nan ± nan | 191.7 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 11.00 | 0.00 | 0.25 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 0.983 | 0.974 | 0.473 (55) | 0.188 (16) | 0.000 (52) | 0.171 (41) | 0.381 (2557) | 17.950 | 0.350 | — | 0.382 |
| harvester | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (1775) | 21.650 | 0.000 | — | 0.677 |
| leaver | — | 0.792 | — (0) | 0.000 (419) | 0.000 (954) | 0.000 (751) | 0.000 (1724) | 0.900 | 0.400 | — | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (1784) | 20.200 | 0.000 | — | 0.728 |
| careful | — | 0.793 | — (0) | 0.000 (478) | 0.000 (897) | 0.000 (784) | 0.000 (1674) | 0.500 | 0.250 | — | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| learned | 18.450 | 17.450 | 9.000 | 2.150 | 872.500 | 0.000 | 13.000 |
| harvester | 21.450 | 20.450 | 10.450 | 1.850 | 1022.500 | 0.000 | 12.300 |
| leaver | 2.050 | 1.050 | 0.650 | 11.550 | 52.500 | 0.000 | 12.200 |
| stamper | 10.700 | 9.700 | 0.000 | 0.000 | 485.000 | 0.000 | 12.300 |
| careful | 1.350 | 0.350 | 0.000 | 0.000 | 17.500 | 0.000 | 12.150 |

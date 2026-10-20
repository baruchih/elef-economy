# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-rearrive on`, seeds 21-40, hide ``, model `results/redteam/Q1/rearrive-visible/models/wm-online-10.pt` (value mc, horizon 16)

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate | real stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 1708.1 ± 80.9 | 269.8 ± 88.6 | 140.8 | 0.212 | 0.408 | 0.380 | 0.769 | 0.781 | 11.65 | 8.50 | 0.95 |
| greedy | 1543.5 ± 73.5 | 105.3 ± 87.9 | 135.1 | 0.155 | 0.370 | 0.474 | 0.854 | 0.804 | 10.50 | 6.75 | 0.85 |
| careful | 1438.2 ± 88.1 | nan ± nan | 171.2 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 11.90 | 0.00 | 0.15 |
| sleeper0.5 | 1402.9 ± 84.0 | -35.3 ± 28.7 | 174.3 | 0.886 | 0.114 | 0.000 | 0.088 | 0.116 | 12.25 | 2.20 | 0.15 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 0.990 | 0.979 | — (0) | 0.000 (19) | 0.237 (38) | 0.237 (156) | 0.409 (2602) | 13.900 | 0.450 | — | 0.612 |
| greedy | 0.971 | 0.942 | — (0) | 0.000 (114) | 0.190 (211) | 0.188 (191) | 0.383 (2185) | 13.500 | 0.150 | — | 0.500 |
| careful | — | 0.749 | — (0) | 0.000 (654) | 0.000 (960) | 0.000 (475) | 0.000 (1335) | 0.350 | 0.150 | — | 0.000 |
| sleeper0.5 | 0.446 | 0.834 | — (0) | 1.000 (390) | 0.000 (951) | 0.000 (736) | 0.000 (1410) | 0.350 | 0.150 | — | 6.286 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| learned | 14.100 | 13.100 | 6.900 | 1.600 | 655.000 | 0.000 | 12.500 |
| greedy | 13.700 | 12.700 | 6.750 | 3.200 | 635.000 | 0.000 | 12.350 |
| careful | 1.250 | 0.250 | 0.000 | 0.000 | 12.500 | 0.000 | 11.700 |
| sleeper0.5 | 1.250 | 0.250 | 0.000 | 0.000 | 12.500 | 0.000 | 11.650 |

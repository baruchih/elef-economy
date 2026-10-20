# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-rearrive on`, seeds 21-40, hide ``, model `results/redteam/Q1/rearrive-visible/models/wm-online-6.pt` (value mc, horizon 16)

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate | real stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 1380.9 ± 66.3 | -57.3 ± 93.2 | 161.4 | 0.387 | 0.254 | 0.360 | 0.631 | 0.604 | 11.20 | 6.55 | 0.75 |
| careful | 1438.2 ± 88.1 | nan ± nan | 171.2 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 11.90 | 0.00 | 0.15 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 0.920 | 0.931 | — (0) | 0.104 (125) | 0.247 (288) | 0.135 (208) | 0.266 (2608) | 7.500 | 0.450 | — | 0.873 |
| careful | — | 0.749 | — (0) | 0.000 (654) | 0.000 (960) | 0.000 (475) | 0.000 (1335) | 0.350 | 0.150 | — | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| learned | 7.750 | 6.750 | 3.550 | 3.150 | 337.500 | 0.000 | 11.850 |
| careful | 1.250 | 0.250 | 0.000 | 0.000 | 12.500 | 0.000 | 11.700 |

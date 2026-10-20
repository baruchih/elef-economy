# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-rearrive on`, seeds 21-40, hide `own_p_eff`, model `results/redteam/Q1/rearrive-hidden/models/wm-online-8.pt` (value mc, horizon 16)

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate | real stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 1373.7 ± 59.6 | -64.6 ± 91.1 | 146.6 | 0.282 | 0.385 | 0.333 | 0.708 | 0.708 | 11.90 | 7.80 | 0.90 |
| careful | 1438.2 ± 88.1 | nan ± nan | 171.2 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 11.90 | 0.00 | 0.15 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 0.972 | 0.962 | — (0) | 0.146 (41) | 0.293 (157) | 0.285 (172) | 0.393 (2561) | 10.700 | 0.550 | 278.667 | 0.729 |
| careful | — | 0.749 | — (0) | 0.000 (654) | 0.000 (960) | 0.000 (475) | 0.000 (1335) | 0.350 | 0.150 | — | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| learned | 10.800 | 9.800 | 5.100 | 3.100 | 490.000 | 0.000 | 12.100 |
| careful | 1.250 | 0.250 | 0.000 | 0.000 | 12.500 | 0.000 | 11.700 |

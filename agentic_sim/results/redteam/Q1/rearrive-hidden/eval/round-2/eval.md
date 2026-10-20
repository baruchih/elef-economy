# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-rearrive on`, seeds 21-40, hide `own_p_eff`, model `results/redteam/Q1/rearrive-hidden/models/wm-online-2.pt` (value mc, horizon 16)

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate | real stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 1492.0 ± 97.0 | 53.7 ± 76.9 | 152.7 | 0.328 | 0.321 | 0.351 | 0.667 | 0.667 | 11.10 | 6.10 | 0.95 |
| careful | 1438.2 ± 88.1 | nan ± nan | 171.2 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 11.90 | 0.00 | 0.15 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 0.950 | 0.955 | — (0) | 0.451 (91) | 0.162 (167) | 0.181 (193) | 0.324 (2603) | 9.100 | 0.750 | 303.500 | 0.670 |
| careful | — | 0.749 | — (0) | 0.000 (654) | 0.000 (960) | 0.000 (475) | 0.000 (1335) | 0.350 | 0.150 | — | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| learned | 9.400 | 8.400 | 4.400 | 3.700 | 420.000 | 0.000 | 12.250 |
| careful | 1.250 | 0.250 | 0.000 | 0.000 | 12.500 | 0.000 | 11.700 |

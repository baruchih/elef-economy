# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-rearrive on`, seeds 21-40, hide ``, model `results/redteam/Q1/rearrive-v4/models/wm-online-6.pt` (value mc, horizon 16)

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate | real stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 1341.5 ± 102.6 | -261.3 ± 84.7 | 184.0 | 0.758 | 0.170 | 0.073 | 0.144 | 0.277 | 11.95 | 1.75 | 0.15 |
| careful | 1602.9 ± 117.0 | nan ± nan | 179.8 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 11.20 | 0.00 | 0.00 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 0.768 | 0.840 | — (0) | 0.220 (391) | 0.216 (741) | 0.292 (528) | 0.128 (2020) | 0.200 | 0.150 | — | 8.750 |
| careful | — | 0.793 | — (0) | 0.000 (474) | 0.000 (781) | 0.000 (830) | 0.000 (1512) | 0.000 | 0.000 | — | — |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| learned | 1.150 | 0.150 | 0.150 | 0.250 | 7.500 | 0.000 | 12.200 |
| careful | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 12.000 |

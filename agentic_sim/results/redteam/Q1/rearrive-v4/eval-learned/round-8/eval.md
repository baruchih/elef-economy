# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-rearrive on`, seeds 21-40, hide ``, model `results/redteam/Q1/rearrive-v4/models/wm-online-8.pt` (value mc, horizon 16)

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate | real stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 1513.6 ± 105.6 | -89.3 ± 68.1 | 178.4 | 0.777 | 0.217 | 0.006 | 0.054 | 0.267 | 11.55 | 2.00 | 0.05 |
| careful | 1602.9 ± 117.0 | nan ± nan | 179.8 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 11.20 | 0.00 | 0.00 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 0.774 | 0.815 | — (0) | 0.188 (432) | 0.295 (814) | 0.325 (701) | 0.157 (1621) | 0.050 | 0.050 | — | 40.000 |
| careful | — | 0.793 | — (0) | 0.000 (474) | 0.000 (781) | 0.000 (830) | 0.000 (1512) | 0.000 | 0.000 | — | — |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| learned | 1.050 | 0.050 | 0.050 | 0.100 | 2.500 | 0.000 | 12.050 |
| careful | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 12.000 |

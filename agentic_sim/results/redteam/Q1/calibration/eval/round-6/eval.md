# Evaluation — cell `--entry-pool 20 --stampers 0.6 --pi0 0 --dial off --audit-roll off`, seeds 21-40, hide ``, model `results/redteam/Q1/calibration/models/wm-online-6.pt` (value mc, horizon 16)

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate | real stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 1264.9 ± 139.3 | -185.3 ± 156.3 | 67.2 | 0.119 | 0.324 | 0.557 | 0.000 | 0.860 | 172.90 | 4.75 | 0.15 |
| careful | 1450.2 ± 120.4 | nan ± nan | 79.5 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 171.75 | 0.00 | 0.05 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 1.000 | 1.000 | — (0) | — (0) | — (0) | — (0) | 0.359 (1343) | 0.000 | 0.000 | — | — |
| careful | — | 1.000 | — (0) | — (0) | — (0) | — (0) | 0.000 (1591) | 0.000 | 0.000 | — | — |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| learned | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.150 | 0.000 |
| careful | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.050 | 0.000 |

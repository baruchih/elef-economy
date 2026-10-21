# Evaluation — cell `--entry-pool 20 --stampers 0.6 --pi0 0 --dial off --audit-roll off --care-cost 4`, seeds 21-40, hide ``, model `results/redteam/Q1/calibration-2.7.0/models/wm-online-10.pt` (value mc, horizon 1)

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate | real stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 1403.9 ± 154.9 | nan ± nan | 87.4 | 0.329 | 0.579 | 0.092 | 0.000 | 0.700 | 198.90 | 10.00 | 0.15 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 1.000 | 1.000 | — (0) | — (0) | — (0) | — (0) | 0.593 (1748) | 0.000 | 0.000 | — | — |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| learned | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.150 | 0.000 |

# Evaluation — cell `--entry-pool 20 --stampers 0.6 --pi0 0 --dial off --audit-roll off --care-cost 4`, seeds 21-40, hide ``, model `results/redteam/Q1/calibration-2.7.0-h1/models/wm-online-4.pt` (value mc, horizon 1)

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate | real stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 555.2 ± 147.5 | -525.1 ± 208.9 | 49.3 | 0.152 | 0.469 | 0.379 | 0.000 | 0.764 | 190.20 | 4.85 | 0.65 |
| careful | 1080.4 ± 158.1 | nan ± nan | 74.8 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 197.45 | 0.00 | 0.25 |
| stamper | 1828.0 ± 151.9 | 747.6 ± 193.6 | 92.0 | 0.000 | 1.000 | 0.000 | 0.000 | 1.000 | 203.50 | 16.70 | 0.10 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 1.000 | 1.000 | — (0) | — (0) | — (0) | — (0) | 0.538 (986) | 0.000 | 0.000 | — | — |
| careful | — | 1.000 | — (0) | — (0) | — (0) | — (0) | 0.000 (1495) | 0.000 | 0.000 | — | — |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (1841) | 0.000 | 0.000 | — | — |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| learned | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.650 | 0.000 |
| careful | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.250 | 0.000 |
| stamper | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.100 | 0.000 |

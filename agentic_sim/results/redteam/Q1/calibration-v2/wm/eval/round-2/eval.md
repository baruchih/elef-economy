# Evaluation — cell `--entry-pool 20 --stampers 0.6 --pi0 0 --dial off --audit-roll off --care-cost 4`, seeds 21-40, hide ``, model `results/redteam/Q1/calibration-v2/wm/models/wm-online-2.pt` (value mc, horizon 16)

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate | real stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 1704.5 ± 156.6 | 496.0 ± 181.9 | 85.5 | 0.000 | 1.000 | 0.000 | 0.000 | 1.000 | 203.95 | 15.05 | 0.20 |
| careful | 1208.5 ± 143.3 | nan ± nan | 85.7 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 197.20 | 0.00 | 0.00 |
| stamper | 1941.3 ± 102.7 | 732.8 ± 119.4 | 100.1 | 0.000 | 1.000 | 0.000 | 0.000 | 1.000 | 205.25 | 18.10 | 0.00 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (1711) | 0.000 | 0.000 | — | — |
| careful | — | 1.000 | — (0) | — (0) | — (0) | — (0) | 0.000 (1714) | 0.000 | 0.000 | — | — |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (2002) | 0.000 | 0.000 | — | — |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| learned | 1.000 | 0.000 | 0.200 | 2.850 | 0.000 | 0.200 | 3.500 |
| careful | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 4.000 |
| stamper | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 4.000 |

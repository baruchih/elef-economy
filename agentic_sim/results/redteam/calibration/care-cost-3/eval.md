# Evaluation — cell `--entry-pool 20 --stampers 0.6 --pi0 0 --dial off --audit-roll off --care-cost 3`, seeds 21-40, hide ``, model `None` (value off, horizon 8)

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate | real stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|
| careful | 1331.8 ± 129.9 | nan ± nan | 77.8 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 169.85 | 0.00 | 0.15 |
| stamper | 1696.9 ± 133.5 | 365.1 ± 180.4 | 84.8 | 0.000 | 1.000 | 0.000 | 0.000 | 1.000 | 180.00 | 15.15 | 0.05 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| careful | — | 1.000 | — (0) | — (0) | — (0) | — (0) | 0.000 (1555) | 0.000 | 0.000 | — | — |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (1696) | 0.000 | 0.000 | — | — |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| careful | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.150 | 0.000 |
| stamper | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.050 | 0.000 |

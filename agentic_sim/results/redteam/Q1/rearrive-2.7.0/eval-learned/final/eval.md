# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-rearrive on`, seeds 21-40, hide ``, model `results/redteam/Q1/rearrive-2.7.0/models/wm-online-10.pt` (value mc, horizon 16)

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate | real stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 894.4 ± 88.0 | -708.5 ± 157.5 | 204.4 | 0.471 | 0.260 | 0.269 | 0.509 | 0.532 | 11.50 | 6.60 | 0.85 |
| careful | 1602.9 ± 117.0 | nan ± nan | 179.8 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 11.20 | 0.00 | 0.00 |
| harvester | 466.1 ± 60.4 | -1136.8 ± 129.5 | 93.3 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 11.80 | 15.60 | 1.00 |
| leaver | 1702.5 ± 97.3 | 99.7 ± 39.7 | 193.7 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 10.70 | 0.00 | 0.40 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 0.939 | 0.925 | 0.304 (23) | 0.215 (246) | 0.199 (286) | 0.184 (245) | 0.272 (3289) | 3.700 | 1.000 | 322.500 | 1.784 |
| careful | — | 0.793 | — (0) | 0.000 (474) | 0.000 (781) | 0.000 (830) | 0.000 (1512) | 0.000 | 0.000 | — | — |
| harvester | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (1866) | 22.500 | 0.000 | — | 0.693 |
| leaver | — | 0.800 | — (0) | 0.000 (477) | 0.000 (763) | 0.000 (812) | 0.000 (1821) | 1.100 | 0.500 | 401.000 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| learned | 3.000 | 2.000 | 2.000 | 3.150 | 100.000 | 0.000 | 12.350 |
| careful | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 12.000 |
| harvester | 12.000 | 11.000 | 11.000 | 1.700 | 550.000 | 0.000 | 12.700 |
| leaver | 1.800 | 0.800 | 0.800 | 11.350 | 40.000 | 0.000 | 12.150 |

# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-rearrive on`, seeds 21-40, hide ``, model `results/redteam/Q1/rearrive-280/models/wm-online-6.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | non-initial share | non-initial stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 1650.0 ± 127.4 | -28.5 ± 102.5 | 188.8 | 0.849 | 0.143 | 0.008 | 0.053 | 0.063 | 0.304 | 0.368 | 12.80 | 1.20 | 0.00 |
| careful | 1678.4 ± 107.2 | nan ± nan | 200.7 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.385 | 0.000 | 11.75 | 0.00 | 0.00 |

The stamp rate by seat kind (2.8.0 §5), plant / real, with the decisions pooled over the seeds in parentheses — under 2.7.0 a plant reached the initial review alone; under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| learned | 0.053 (567) / 0.063 (2060) | 0.355 (93) / 0.366 (872) | 0.281 (32) / 0.404 (151) | — / — |
| careful | 0.000 (500) / 0.000 (1968) | 0.000 (143) / 0.000 (1158) | 0.000 (49) / 0.000 (195) | — / — |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 0.737 | 0.814 | — (0) | 0.153 (563) | 0.236 (622) | 0.195 (791) | 0.091 (1799) | 0.000 | 0.000 | — | — |
| careful | — | 0.777 | — (0) | 0.000 (542) | 0.000 (994) | 0.000 (882) | 0.000 (1595) | 0.000 | 0.000 | — | — |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| learned | 1.000 | 0.000 | 0.000 | 0.050 | 0.000 | 0.000 | 11.900 |
| careful | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 11.700 |

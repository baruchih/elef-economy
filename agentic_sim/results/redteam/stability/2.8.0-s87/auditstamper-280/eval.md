# Evaluation — cell `--entry-pool 20 --stampers 0.6`, seeds 21-40, hide ``, model `None` (value off, horizon 8)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | non-initial share | non-initial stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| careful | 1678.4 ± 107.2 | nan ± nan | 200.7 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.385 | 0.000 | 11.75 | 0.00 | 0.00 |
| auditstamper | 1680.7 ± 86.6 | 2.3 ± 70.1 | 192.5 | 0.753 | 0.247 | 0.000 | 0.000 | 0.000 | 0.314 | 0.814 | 11.55 | 1.85 | 0.00 |
| stamper | 437.3 ± 58.7 | -1241.1 ± 111.1 | 64.0 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.034 | 1.000 | 11.70 | 11.10 | 0.00 |

The stamp rate by seat kind (2.8.0 §5), plant / real, with the decisions pooled over the seeds in parentheses — under 2.7.0 a plant reached the initial review alone; under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| careful | 0.000 (500) / 0.000 (1968) | 0.000 (143) / 0.000 (1158) | 0.000 (49) / 0.000 (195) | — / — |
| auditstamper | 0.000 (562) / 0.000 (2078) | 1.000 (99) / 1.000 (886) | 0.000 (35) / 0.000 (190) | — / — |
| stamper | 1.000 (233) / 1.000 (1004) | — / 1.000 (39) | — / 1.000 (4) | — / — |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| careful | — | 0.777 | — (0) | 0.000 (542) | 0.000 (994) | 0.000 (882) | 0.000 (1595) | 0.000 | 0.000 | — | — |
| auditstamper | 0.714 | 0.784 | — (0) | 0.356 (601) | 0.299 (1037) | 0.273 (652) | 0.181 (1560) | 0.000 | 0.000 | — | — |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (1280) | 6.500 | 0.000 | — | 1.708 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| careful | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 11.700 |
| auditstamper | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 11.700 |
| stamper | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 12.000 |

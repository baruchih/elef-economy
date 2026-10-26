# Evaluation — cell `--entry-pool 20 --stampers 0.6 --rules 2.7.0`, seeds 21-40, hide ``, model `None` (value off, horizon 8)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | non-initial share | non-initial stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| careful | 1608.3 ± 106.6 | nan ± nan | 185.0 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.311 | 0.000 | 11.30 | 0.00 | 0.00 |
| auditstamper | 1676.4 ± 88.4 | 68.1 ± 78.5 | 187.1 | 0.720 | 0.280 | 0.000 | 0.000 | 0.000 | 0.339 | 0.838 | 12.10 | 1.50 | 0.00 |
| stamper | 364.2 ± 39.6 | -1244.0 ± 118.5 | 68.5 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.031 | 1.000 | 11.90 | 12.05 | 0.00 |

The stamp rate by seat kind (2.8.0 §5), plant / real, with the decisions pooled over the seeds in parentheses — under 2.7.0 a plant reached the initial review alone; under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| careful | 0.000 (547) / 0.000 (2001) | — / 0.000 (954) | — / 0.000 (198) | — / — |
| auditstamper | 0.000 (521) / 0.000 (1952) | — / 1.000 (1062) | — / 0.000 (206) | — / — |
| stamper | 1.000 (248) / 1.000 (1080) | — / 1.000 (39) | — / 1.000 (4) | — / — |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| careful | — | 0.786 | — (0) | 0.000 (543) | 0.000 (844) | 0.000 (649) | 0.000 (1664) | 0.000 | 0.000 | — | — |
| auditstamper | 0.734 | 0.775 | — (0) | 0.269 (551) | 0.285 (927) | 0.394 (764) | 0.233 (1499) | 0.000 | 0.000 | — | — |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (1371) | 6.250 | 0.000 | — | 1.928 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| careful | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 12.100 |
| auditstamper | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 11.800 |
| stamper | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 12.000 |

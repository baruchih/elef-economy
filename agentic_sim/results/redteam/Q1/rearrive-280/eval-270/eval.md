# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-rearrive on --rules 2.7.0`, seeds 21-40, hide ``, model `results/redteam/Q1/rearrive-280/models/wm-online-10.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | non-initial share | non-initial stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 1697.7 ± 115.7 | 89.5 ± 90.8 | 193.1 | 0.875 | 0.122 | 0.003 | 0.057 | 0.061 | 0.289 | 0.313 | 12.00 | 2.75 | 0.05 |
| greedy | 1617.0 ± 104.5 | 8.7 ± 79.4 | 189.8 | 0.838 | 0.162 | 0.000 | 0.092 | 0.079 | 0.228 | 0.428 | 11.95 | 2.20 | 0.15 |
| careful | 1608.3 ± 106.6 | nan ± nan | 185.0 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.311 | 0.000 | 11.30 | 0.00 | 0.00 |
| harvester | 431.3 ± 50.1 | -1177.0 ± 129.4 | 90.0 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.024 | 1.000 | 12.25 | 14.40 | 1.00 |
| leaver | 1692.8 ± 97.1 | 84.5 ± 40.8 | 190.9 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.273 | 0.000 | 11.90 | 0.00 | 0.50 |
| stamper | 364.2 ± 39.6 | -1244.0 ± 118.5 | 68.5 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.031 | 1.000 | 11.90 | 12.05 | 0.00 |

The stamp rate by seat kind (2.8.0 §5), plant / real, with the decisions pooled over the seeds in parentheses — under 2.7.0 a plant reached the initial review alone; under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| learned | 0.057 (599) / 0.061 (2148) | — / 0.346 (920) | — / 0.159 (195) | — / — |
| greedy | 0.092 (653) / 0.079 (2276) | — / 0.484 (728) | — / 0.137 (139) | — / — |
| careful | 0.000 (547) / 0.000 (2001) | — / 0.000 (954) | — / 0.000 (198) | — / — |
| harvester | 1.000 (364) / 1.000 (1394) | — / 1.000 (39) | — / 1.000 (4) | — / — |
| leaver | 0.000 (602) / 0.000 (2175) | — / 0.000 (859) | — / 0.000 (183) | — / — |
| stamper | 1.000 (248) / 1.000 (1080) | — / 1.000 (39) | — / 1.000 (4) | — / — |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 0.834 | 0.794 | 0.140 (43) | 0.110 (490) | 0.115 (879) | 0.207 (634) | 0.116 (1816) | 0.250 | 0.050 | — | 11.000 |
| greedy | 0.797 | 0.805 | 0.000 (12) | 0.119 (487) | 0.209 (818) | 0.152 (574) | 0.154 (1905) | 0.150 | 0.150 | — | 14.667 |
| careful | — | 0.786 | — (0) | 0.000 (543) | 0.000 (844) | 0.000 (649) | 0.000 (1664) | 0.000 | 0.000 | — | — |
| harvester | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (1801) | 21.400 | 0.000 | — | 0.673 |
| leaver | — | 0.822 | — (0) | 0.000 (474) | 0.000 (744) | 0.000 (533) | 0.000 (2068) | 1.100 | 0.650 | 136.750 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (1371) | 6.250 | 0.000 | — | 1.928 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| learned | 1.100 | 0.100 | 0.100 | 0.300 | 5.000 | 0.000 | 12.200 |
| greedy | 1.150 | 0.150 | 0.150 | 0.400 | 7.500 | 0.000 | 12.300 |
| careful | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 12.100 |
| harvester | 11.350 | 10.350 | 10.350 | 2.300 | 517.500 | 0.000 | 12.650 |
| leaver | 1.950 | 0.950 | 0.950 | 11.100 | 47.500 | 0.000 | 12.050 |
| stamper | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 12.000 |

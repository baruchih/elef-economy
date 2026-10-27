# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-rearrive on`, seeds 21-40, hide ``, model `results/redteam/Q1/rearrive-280/models/wm-online-10.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | non-initial share | non-initial stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 1466.8 ± 123.1 | -211.6 ± 119.5 | 176.2 | 0.831 | 0.165 | 0.004 | 0.077 | 0.083 | 0.211 | 0.350 | 12.05 | 2.10 | 0.00 |
| greedy | 1589.1 ± 109.0 | -89.4 ± 95.0 | 189.9 | 0.816 | 0.184 | 0.000 | 0.108 | 0.097 | 0.280 | 0.399 | 11.45 | 2.95 | 0.00 |
| careful | 1678.4 ± 107.2 | nan ± nan | 200.7 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.385 | 0.000 | 11.75 | 0.00 | 0.00 |
| harvester | 463.3 ± 61.2 | -1215.1 ± 116.1 | 90.0 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.024 | 1.000 | 11.45 | 14.25 | 1.00 |
| leaver | 1670.0 ± 115.5 | -8.4 ± 32.4 | 202.9 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.402 | 0.000 | 11.65 | 0.00 | 0.50 |
| stamper | 437.3 ± 58.7 | -1241.1 ± 111.1 | 64.0 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.034 | 1.000 | 11.70 | 11.10 | 0.00 |

The stamp rate by seat kind (2.8.0 §5), plant / real, with the decisions pooled over the seeds in parentheses — under 2.7.0 a plant reached the initial review alone; under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| learned | 0.077 (594) / 0.083 (2186) | 0.426 (47) / 0.382 (574) | 0.267 (15) / 0.159 (107) | — / — |
| greedy | 0.108 (623) / 0.097 (2113) | 0.418 (98) / 0.465 (779) | 0.095 (42) / 0.118 (144) | — / — |
| careful | 0.000 (500) / 0.000 (1968) | 0.000 (143) / 0.000 (1158) | 0.000 (49) / 0.000 (195) | — / — |
| harvester | 1.000 (363) / 1.000 (1395) | — / 1.000 (39) | — / 1.000 (4) | — / — |
| leaver | 0.000 (502) / 0.000 (1923) | 0.000 (149) / 0.000 (1217) | 0.000 (53) / 0.000 (214) | — / — |
| stamper | 1.000 (233) / 1.000 (1004) | — / 1.000 (39) | — / 1.000 (4) | — / — |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 0.854 | 0.834 | — (0) | 0.109 (448) | 0.139 (638) | 0.117 (563) | 0.142 (1874) | 0.100 | 0.050 | — | 21.000 |
| greedy | 0.810 | 0.820 | — (0) | 0.142 (367) | 0.209 (871) | 0.154 (700) | 0.190 (1861) | 0.050 | 0.000 | — | 59.000 |
| careful | — | 0.777 | — (0) | 0.000 (542) | 0.000 (994) | 0.000 (882) | 0.000 (1595) | 0.000 | 0.000 | — | — |
| harvester | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (1801) | 20.900 | 0.000 | — | 0.682 |
| leaver | — | 0.800 | — (0) | 0.000 (544) | 0.000 (818) | 0.000 (876) | 0.000 (1820) | 1.300 | 0.550 | 281.000 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (1280) | 6.500 | 0.000 | — | 1.708 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| learned | 1.000 | 0.000 | 0.000 | 0.600 | 0.000 | 0.000 | 11.800 |
| greedy | 1.000 | 0.000 | 0.000 | 0.500 | 0.000 | 0.000 | 12.000 |
| careful | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 11.700 |
| harvester | 11.100 | 10.100 | 10.100 | 2.000 | 505.000 | 0.000 | 12.100 |
| leaver | 2.050 | 1.050 | 1.050 | 10.500 | 52.500 | 0.000 | 11.550 |
| stamper | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 12.000 |

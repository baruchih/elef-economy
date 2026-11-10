# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-rearrive on`, seeds 21-40, hide ``, model `results/redteam/Q1/rearrive-280/models/wm-online-10.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 1494.6 ± 121.0 | -225.1 ± 119.5 | 190.4 | 0.844 | 0.148 | 0.009 | 0.067 | 0.080 | 0.268 | 0.289 | 8.25 | 1.95 | 0.05 |
| greedy | 1539.4 ± 100.5 | -180.3 ± 114.4 | 198.0 | 0.820 | 0.180 | 0.000 | 0.107 | 0.112 | 0.262 | 0.388 | 8.90 | 3.60 | 0.20 |
| careful | 1719.7 ± 106.7 | nan ± nan | 214.2 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.396 | 0.000 | 7.50 | 0.00 | 0.00 |
| harvester | 424.7 ± 55.8 | -1295.0 ± 114.6 | 93.3 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.023 | 1.000 | 9.00 | 14.70 | 1.00 |
| leaver | 1583.9 ± 105.1 | -135.8 ± 71.9 | 208.2 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.361 | 0.000 | 7.90 | 0.00 | 0.45 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| learned | 0.067 (567) [rej. blind 0.012] / 0.080 (2220) [rej. blind 0.006] | 0.362 (80) / 0.306 (761) [rej. blind 0.013] | 0.237 (76) [rej. blind 0.066] / 0.143 (105) [rej. blind 0.019] | — / — |
| greedy | 0.107 (619) / 0.112 (2302) | 0.395 (86) / 0.428 (766) | 0.293 (82) / 0.162 (105) | — / — |
| careful | 0.000 (553) / 0.000 (2036) | 0.000 (136) / 0.000 (1244) | 0.000 (98) / 0.000 (218) | — / — |
| harvester | 1.000 (377) / 1.000 (1447) | — / 1.000 (39) | — / 1.000 (4) | — / — |
| leaver | 0.000 (570) / 0.000 (2091) | 0.000 (121) / 0.000 (1110) | 0.000 (82) / 0.000 (190) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| learned | 0.067 (567) [rej. blind 0.012] / 0.080 (2220) [rej. blind 0.006] | 0.362 (80) / 0.306 (761) [rej. blind 0.013] | 0.237 (76) [rej. blind 0.066] / 0.143 (105) [rej. blind 0.019] | — / — | 1.4 ± 0.4 | +0 |
| greedy | 0.108 (619) [rej. blind 0.002] / 0.113 (2302) | 0.395 (86) / 0.428 (766) | 0.293 (82) / 0.162 (105) | — / — | 1.4 ± 0.4 | +2 |
| careful | 0.000 (553) / 0.000 (2036) | 0.000 (136) / 0.000 (1244) | 0.000 (98) / 0.000 (218) | — / — | 1.1 ± 0.4 | +0 |
| harvester | 1.000 (377) / 1.000 (1447) | — / 1.000 (39) | — / 1.000 (4) | — / — | 1.4 ± 0.4 | +0 |
| leaver | 0.002 (570) / 0.000 (2091) | 0.000 (121) / 0.000 (1110) | 0.000 (82) / 0.000 (190) | — / — | 1.1 ± 0.4 | +1 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 1.000 | 1.000 | — (0) | — (0) | — (0) | 0.000 (21) | 0.125 (3788) | 0.150 | 0.100 | — | 13.000 |
| greedy | 0.998 | 0.998 | — (0) | — (0) | 0.316 (19) | 0.027 (37) | 0.184 (3904) | 0.700 | 0.200 | — | 5.143 |
| careful | — | 0.999 | — (0) | — (0) | 0.000 (4) | 0.000 (50) | 0.000 (4231) | 0.050 | 0.050 | — | 0.000 |
| harvester | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (1867) | 21.150 | 0.000 | — | 0.695 |
| leaver | — | 0.999 | — (0) | — (0) | 0.000 (4) | 0.000 (35) | 0.000 (4125) | 1.050 | 0.500 | 106.000 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| learned | 1.050 | 0.050 | 0.050 | 0.750 | 2.500 | 0.000 | 11.250 |
| greedy | 1.300 | 0.300 | 0.300 | 0.500 | 15.000 | 0.000 | 11.700 |
| careful | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 11.350 |
| harvester | 11.200 | 10.200 | 10.200 | 1.850 | 510.000 | 0.000 | 12.050 |
| leaver | 2.000 | 1.000 | 1.000 | 10.300 | 50.000 | 0.000 | 11.300 |

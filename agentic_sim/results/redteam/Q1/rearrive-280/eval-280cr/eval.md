# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-rearrive on --rules 2.8.0`, seeds 21-40, hide ``, model `results/redteam/Q1/rearrive-280/models/wm-online-10.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 1593.3 ± 140.1 | -50.9 ± 109.6 | 187.0 | 0.828 | 0.168 | 0.003 | 0.066 | 0.068 | 0.295 | 0.310 | 7.50 | 1.45 | 0.05 |
| greedy | 1594.4 ± 101.3 | -49.8 ± 109.9 | 187.2 | 0.871 | 0.129 | 0.000 | 0.099 | 0.075 | 0.243 | 0.301 | 8.65 | 1.75 | 0.15 |
| careful | 1644.3 ± 134.0 | nan ± nan | 200.6 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.364 | 0.000 | 7.80 | 0.00 | 0.00 |
| harvester | 509.4 ± 76.8 | -1134.9 ± 125.1 | 87.4 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.025 | 1.000 | 8.40 | 13.60 | 1.00 |
| leaver | 1671.8 ± 113.5 | 27.5 ± 58.7 | 204.2 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.330 | 0.000 | 7.95 | 0.00 | 0.50 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| learned | 0.066 (528) [rej. blind 0.006] / 0.068 (2107) [rej. blind 0.004] | 0.315 (73) / 0.330 (871) | 0.071 (28) / 0.226 (133) | — / — |
| greedy | 0.099 (609) [rej. blind 0.002] / 0.075 (2227) [rej. blind 0.000] | 0.392 (79) / 0.312 (695) | 0.125 (24) / 0.200 (110) | — / — |
| careful | 0.000 (542) / 0.000 (2011) | 0.000 (121) / 0.000 (1078) | 0.000 (40) / 0.000 (220) | — / — |
| harvester | 1.000 (329) / 1.000 (1376) | — / 1.000 (39) | — / 1.000 (4) | — / — |
| leaver | 0.000 (599) / 0.000 (2139) | 0.000 (106) / 0.000 (1028) | 0.000 (37) / 0.000 (175) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| learned | 0.066 (528) [rej. blind 0.006] / 0.068 (2107) [rej. blind 0.004] | 0.315 (73) / 0.330 (871) | 0.071 (28) / 0.226 (133) | — / — | 1.2 ± 0.3 | +0 |
| greedy | 0.099 (609) [rej. blind 0.002] / 0.076 (2227) [rej. blind 0.000] | 0.392 (79) / 0.312 (695) | 0.125 (24) / 0.200 (110) | — / — | 1.4 ± 0.4 | +1 |
| careful | 0.000 (542) / 0.000 (2011) | 0.000 (121) / 0.000 (1078) | 0.000 (40) / 0.000 (220) | — / — | 0.9 ± 0.2 | +0 |
| harvester | 1.000 (329) / 1.000 (1376) | — / 1.000 (39) | — / 1.000 (4) | — / — | 1.6 ± 0.4 | +0 |
| leaver | 0.000 (599) / 0.000 (2139) [rej. blind 0.000] | 0.000 (106) / 0.000 (1028) | 0.000 (37) / 0.000 (175) | — / — | 1.0 ± 0.2 | +1 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 1.000 | 0.999 | — (0) | — (0) | — (0) | 0.042 (48) | 0.137 (3692) | 0.100 | 0.100 | — | 14.500 |
| greedy | 1.000 | 0.999 | — (0) | — (0) | — (0) | 0.038 (52) | 0.135 (3692) | 0.600 | 0.150 | — | 2.917 |
| careful | — | 1.000 | — (0) | — (0) | — (0) | 0.000 (28) | 0.000 (3984) | 0.000 | 0.000 | — | — |
| harvester | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (1748) | 19.150 | 0.000 | — | 0.710 |
| leaver | — | 1.000 | — (0) | — (0) | — (0) | 0.000 (12) | 0.000 (4072) | 1.250 | 0.700 | 198.167 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| learned | 1.050 | 0.050 | 0.050 | 0.300 | 2.500 | 0.000 | 11.450 |
| greedy | 1.200 | 0.200 | 0.200 | 0.250 | 10.000 | 0.000 | 11.750 |
| careful | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 11.600 |
| harvester | 10.350 | 9.350 | 9.350 | 2.350 | 467.500 | 0.000 | 11.700 |
| leaver | 2.000 | 1.000 | 1.000 | 10.750 | 50.000 | 0.000 | 11.750 |

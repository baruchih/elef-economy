# Evaluation — cell `--entry-pool 20 --stampers 0 --learner-slot on --learner-rearrive on --temptation 1 --bond-mult-later 1 --pi-a0 0.10 --pi-a-max 0.10`, seeds 21-40, hide ``, model `None` (value off, horizon 8)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| claimreturner | 674.9 ± 87.8 | -530.2 ± 127.5 | 94.9 | 0.000 | 0.000 | 0.000 | 1.000 | 1.000 | 0.012 | 1.000 | 3.65 | 17.75 | 0.85 |
| claimer | 644.3 ± 89.0 | -560.8 ± 126.4 | 82.7 | 0.000 | 0.000 | 0.000 | 1.000 | 1.000 | 0.014 | 1.000 | 3.50 | 14.90 | 0.00 |
| careful | 1205.0 ± 178.5 | nan ± nan | 119.8 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.320 | 0.000 | 2.75 | 0.00 | 0.00 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| claimreturner | 1.000 (178) / 1.000 (1697) | — / 1.000 (22) | — / 1.000 (1) | — / — |
| claimer | 1.000 (162) / 1.000 (1469) | — / 1.000 (22) | — / 1.000 (1) | — / — |
| careful | 0.000 (143) / 0.000 (1485) | 0.000 (71) / 0.000 (549) | 0.000 (59) / 0.000 (88) | — / — |

The stressed world's fourth action by seat kind — the allowance claimed and the verdict F without inspecting (counted above among the blind verdicts; the ledger sees a careful review, so the measured reading below cannot see it):

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| claimreturner | 1.000 (178) / 1.000 (1697) | — / 1.000 (22) | — / 1.000 (1) | — / — |
| claimer | 1.000 (162) / 1.000 (1469) | — / 1.000 (22) | — / 1.000 (1) | — / — |
| careful | 0.000 (143) / 0.000 (1485) | 0.000 (71) / 0.000 (549) | 0.000 (59) / 0.000 (88) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| claimreturner | 0.022 (178) / 0.026 (1697) | — / 0.000 (22) | — / 0.000 (1) | — / — | 2.0 ± 0.4 | -1850 |
| claimer | 0.000 (162) / 0.000 (1469) | — / 0.000 (22) | — / 0.000 (1) | — / — | 2.0 ± 0.4 | -1654 |
| careful | 0.000 (143) / 0.000 (1485) | 0.000 (71) / 0.000 (549) | 0.000 (59) / 0.000 (88) | — / — | 2.2 ± 0.3 | +0 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| claimreturner | — | 1.000 | — (0) | — (0) | — (0) | — (0) | 0.000 (1898) | 3.700 | 0.000 | — | 4.797 |
| claimer | — | 1.000 | — (0) | — (0) | — (0) | — (0) | 0.000 (1654) | 3.150 | 0.000 | — | 4.730 |
| careful | — | 0.925 | — (0) | — (0) | 0.000 (418) | 0.000 (63) | 0.000 (1914) | 0.000 | 0.000 | — | — |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| claimreturner | 2.550 | 1.550 | 1.550 | 0.300 | 77.500 | 0.000 | 5.400 |
| claimer | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 5.450 |
| careful | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 5.100 |

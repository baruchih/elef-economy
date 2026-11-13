# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --pi-a0 0.10 --pi-a-max 0.10 --bond-mult-later 1 --w-audit 1.5`, seeds 21-80, hide ``, model `None` (value off, horizon 8)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.3audit:0.25 | 35048.8 ± 454.2 | -333.7 ± 445.0 | 4595.5 | 0.984 | 0.000 | 0.000 | 0.000 | 0.000 | 0.378 | 0.043 | 3.33 | 0.78 | 0.32 |
| careful | 35382.5 ± 455.9 | nan ± nan | 4620.9 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.382 | 0.000 | 2.58 | 0.00 | 0.28 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:dose0.3audit:0.25 | 0.000 (16107) / 0.000 (155405) | 0.055 (9535) / 0.053 (74092) | 0.000 (9071) / 0.000 (11520) | — / — |
| careful | 0.000 (15961) / 0.000 (155290) | 0.000 (9589) / 0.000 (74537) | 0.000 (9713) / 0.000 (12163) | — / — |

The stressed world's fourth action by seat kind — the allowance claimed and the verdict F without inspecting (counted above among the blind verdicts; the ledger sees a careful review, so the measured reading below cannot see it):

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:dose0.3audit:0.25 | 0.000 (16107) / 0.000 (155405) | 0.055 (9535) / 0.053 (74092) | 0.000 (9071) / 0.000 (11520) | — / — |
| careful | 0.000 (15961) / 0.000 (155290) | 0.000 (9589) / 0.000 (74537) | 0.000 (9713) / 0.000 (12163) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| mix:dose0.3audit:0.25 | 0.000 (16107) [rej. blind 0.000] / 0.000 (155405) [rej. blind 0.000] | 0.000 (9535) / 0.000 (74092) | 0.000 (9071) / 0.000 (11520) | — / — | 2.6 ± 0.3 | -4419 |
| careful | 0.000 (15961) [rej. blind 0.000] / 0.000 (155290) [rej. blind 0.000] | 0.000 (9589) / 0.000 (74537) | 0.000 (9713) / 0.000 (12163) | — / — | 2.8 ± 0.3 | +26 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.3audit:0.25 | — | 0.917 | — (0) | — (0) | 0.000 (45690) | 0.000 (3197) | 0.000 (226843) | 5.233 | 694.200 | 1.173 | 0.150 |
| careful | — | 0.912 | — (0) | — (0) | 0.000 (49195) | 0.000 (2233) | 0.000 (225825) | 4.800 | 674.017 | 1.180 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| mix:dose0.3audit:0.25 | 39.683 | 0.000 | 0.000 | 0.000 | 0.000 | 0.317 | 0.000 |
| careful | 39.717 | 0.000 | 0.000 | 0.000 | 0.000 | 0.283 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.3audit:0.25 | 22.867 / 39.683 | 3.333 ± 0.250 | +0.750 ± 0.319 | 10.617 | -0.150 ± 0.629 | 3.217 | 0.051 | 5.233 | +0.433 ± 0.363 | 1903.150 | 0.023 | -0.002 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 25335.334 ± 233.976 | +269.364 ± 239.053 | 35048.8 ± 454.2 | -333.7 ± 445.0 | 35.717 | -0.256 ± 0.222 | 15.675 ± 0.241 | +0.499 ± 0.325 | 18.194 | 0.002 | 2592.683 | 19.683 | 16.817 | +0.367 ± 0.274 | 583.292 | 220.867 |
| careful | 23.267 / 39.717 | 2.583 ± 0.208 | — | 10.767 | — | 3.233 | 0.060 | 4.800 | — | 1894.300 | 0.024 | — | 0.000 / 0.000 (0.000 / 0.000) | 25065.970 ± 246.254 | — | 35382.5 ± 455.9 | — | 35.973 | — | 15.176 ± 0.235 | — | 18.079 | 0.002 | 2591.900 | 19.717 | 16.450 | — | 638.886 | 213.750 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **mix:dose0.3audit:0.25**: p0 1.000/0.000/0.000 (597); p1 1.000/0.000/0.000 (735); p2 1.000/0.000/0.000 (889); p3 1.000/0.000/0.000 (964); p4 1.000/0.000/0.000 (966); p5 1.000/0.000/0.000 (314); p6 1.000/0.000/0.000 (47); p7 1.000/0.000/0.000 (7); p8 1.000/0.000/0.000 (3)
- **careful**: p0 1.000/0.000/0.000 (603); p1 1.000/0.000/0.000 (730); p2 1.000/0.000/0.000 (912); p3 1.000/0.000/0.000 (1009); p4 1.000/0.000/0.000 (1008); p5 1.000/0.000/0.000 (300); p6 1.000/0.000/0.000 (54); p7 1.000/0.000/0.000 (4)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.3audit:0.25 | 2590.1 / 268.4 | 0.32 / 0.19 | -0.12 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.12 / 0.13 | +0.01 ± 0.00 | 0.190 / 0.155 | -0.036 ± 0.003 | 0.075 / 0.080 | 0.002 / 0.000 | 0.056 / 0.054 | -0.002 ± 0.002 | 1.80 / 1.40 | -0.40 ± 0.06 |
| careful | 2588.2 / 266.0 | 0.31 / 0.21 | -0.10 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.13 / 0.13 | -0.00 ± 0.00 | 0.177 / 0.148 | -0.029 ± 0.003 | 0.072 / 0.082 | 0.001 / 0.000 | 0.057 / 0.051 | -0.005 ± 0.002 | 1.82 / 1.46 | -0.36 ± 0.05 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| mix:dose0.3audit:0.25 | -0.12 ± 0.01 | +0.00 ± 0.00 | +0.00 ± 0.00 | -0.033 ± 0.003 | +0.007 ± 0.002 | -0.001 ± 0.002 |
| careful | -0.10 ± 0.01 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.030 ± 0.003 | +0.009 ± 0.002 | -0.005 ± 0.002 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| mix:dose0.3audit:0.25 | 0.470 / 0.139 | 0.32 / 0.33 | 0.039 / 0.158 | 0.00 / 0.00 | 0.29 / 0.34 | 0.312 / 0.256 |
| careful | 0.473 / 0.141 | 0.30 / 0.31 | 0.040 / 0.162 | 0.00 / 0.00 | 0.29 / 0.33 | 0.305 / 0.256 |

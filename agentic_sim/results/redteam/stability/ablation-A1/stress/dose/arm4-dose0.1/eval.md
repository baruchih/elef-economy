# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1 --arm 4`, seeds 21-60, hide ``, model `None` (value off, horizon 8)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 30151.1 ± 479.5 | -891.8 ± 483.3 | 2929.8 | 0.977 | 0.000 | 0.000 | 0.022 | 0.023 | 0.000 | 0.000 | 3.73 | 12.12 | 0.35 |
| careful | 31042.9 ± 550.2 | nan ± nan | 2927.0 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 2.48 | 0.00 | 0.17 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:dose0.1:0.25 | 0.022 (11282) / 0.023 (105901) | — / 0.000 (10) | — / — | — / — |
| careful | 0.000 (10900) / 0.000 (106176) | — / 0.000 (5) | — / — | — / — |

The stressed world's fourth action by seat kind — the allowance claimed and the verdict F without inspecting (counted above among the blind verdicts; the ledger sees a careful review, so the measured reading below cannot see it):

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:dose0.1:0.25 | 0.022 (11282) / 0.023 (105901) | — / 0.000 (10) | — / — | — / — |
| careful | 0.000 (10900) / 0.000 (106176) | — / 0.000 (5) | — / — | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 0.000 (11282) [rej. blind 0.000] / 0.000 (105901) [rej. blind 0.000] | — / 0.000 (10) | — / — | — / — | 5.7 ± 0.4 | -2617 |
| careful | 0.000 (10900) [rej. blind 0.000] / 0.000 (106176) [rej. blind 0.000] | — / 0.000 (5) | — / — | — / — | 5.3 ± 0.4 | +39 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | — | 0.957 | — (0) | — (0) | 0.000 (9840) | 0.000 (1918) | 0.000 (105435) | 5.850 | 640.400 | 1.197 | 2.073 |
| careful | — | 0.952 | — (0) | — (0) | 0.000 (11080) | 0.000 (1162) | 0.000 (104839) | 5.150 | 645.000 | 1.212 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 39.425 | 0.000 | 0.000 | 0.000 | 0.000 | 0.350 | 0.000 |
| careful | 39.500 | 0.000 | 0.000 | 0.000 | 0.000 | 0.175 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 19.750 / 39.425 | 3.725 ± 0.399 | +1.250 ± 0.434 | 14.375 | +4.425 ± 0.932 | 2.825 | 0.071 | 5.850 | +0.700 ± 0.544 | 1947.950 | 0.023 | +0.006 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 20119.563 ± 284.364 | +130.544 ± 385.263 | 30151.1 ± 479.5 | -891.8 ± 483.3 | 37.748 | -0.548 ± 0.374 | 14.805 ± 0.297 | +0.623 ± 0.427 | 16.799 | 0.000 | 2652.100 | 19.425 | 19.675 | +0.525 ± 0.306 | 895.289 | 249.350 |
| careful | 20.350 / 39.500 | 2.475 ± 0.277 | — | 9.950 | — | 3.850 | 0.045 | 5.150 | — | 1929.600 | 0.017 | — | 0.000 / 0.000 (0.000 / 0.000) | 19989.020 ± 331.294 | — | 31042.9 ± 550.2 | — | 38.296 | — | 14.182 ± 0.367 | — | 16.518 | 0.000 | 2659.550 | 19.500 | 19.150 | — | 999.178 | 263.125 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **mix:dose0.1:0.25**: p0 1.000/0.000/0.000 (544); p1 1.000/0.000/0.000 (515); p2 1.000/0.000/0.000 (519); p3 1.000/0.000/0.000 (499); p4 1.000/0.000/0.000 (496); p5 1.000/0.000/0.000 (239); p6 1.000/0.000/0.000 (44); p7 1.000/0.000/0.000 (8)
- **careful**: p0 1.000/0.000/0.000 (556); p1 1.000/0.000/0.000 (540); p2 1.000/0.000/0.000 (542); p3 1.000/0.000/0.000 (529); p4 1.000/0.000/0.000 (529); p5 1.000/0.000/0.000 (205); p6 1.000/0.000/0.000 (25); p7 1.000/0.000/0.000 (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 2647.5 / 282.1 | 0.15 / 0.08 | -0.07 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.06 / 0.06 | +0.01 ± 0.00 | 0.102 / 0.079 | -0.024 ± 0.004 | 0.037 / 0.040 | 0.000 / 0.000 | 0.059 / 0.064 | +0.004 ± 0.002 | 1.41 / 1.21 | -0.19 ± 0.05 |
| careful | 2654.4 / 272.5 | 0.13 / 0.07 | -0.06 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.06 / 0.07 | +0.01 ± 0.00 | 0.101 / 0.081 | -0.020 ± 0.003 | 0.033 / 0.035 | 0.000 / 0.000 | 0.058 / 0.063 | +0.005 ± 0.003 | 1.38 / 1.29 | -0.09 ± 0.08 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | -0.07 ± 0.01 | +0.00 ± 0.00 | +0.01 ± 0.00 | -0.022 ± 0.004 | +0.004 ± 0.002 | +0.003 ± 0.002 |
| careful | -0.06 ± 0.01 | +0.00 ± 0.00 | +0.01 ± 0.00 | -0.018 ± 0.003 | +0.003 ± 0.002 | +0.004 ± 0.002 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 0.000 / 0.000 | 0.28 / — | 0.039 / 0.000 | 0.00 / — | — / — | 0.900 / 0.000 |
| careful | 0.000 / 0.000 | 0.50 / — | 0.040 / 0.000 | 0.00 / — | — / — | 0.888 / 0.000 |

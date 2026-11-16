# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1 --arm 1 --pi-a0 0.10 --pi-a-max 0.10 --w-audit 3`, seeds 81-120, hide ``, model `None` (value off, horizon 8)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:doseM0.1:0.25 | 36180.9 ± 584.4 | -166.6 ± 589.6 | 4535.1 | 0.985 | 0.000 | 0.000 | 0.017 | 0.014 | 0.370 | 0.014 | 3.40 | 7.05 | 0.17 |
| careful | 36347.5 ± 769.0 | nan ± nan | 4610.8 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.379 | 0.000 | 2.62 | 0.00 | 0.25 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:doseM0.1:0.25 | 0.017 (10773) / 0.014 (103526) | 0.016 (6495) / 0.015 (49754) | 0.011 (6345) / 0.014 (4513) | — / — |
| careful | 0.000 (10421) / 0.000 (104150) | 0.000 (6553) / 0.000 (51785) | 0.000 (6747) / 0.000 (4775) | — / — |

The stressed world's fourth action by seat kind — the allowance claimed and the verdict F without inspecting (counted above among the blind verdicts; the ledger sees a careful review, so the measured reading below cannot see it):

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:doseM0.1:0.25 | 0.017 (10773) / 0.014 (103526) | 0.016 (6495) / 0.015 (49754) | 0.011 (6345) / 0.014 (4513) | — / — |
| careful | 0.000 (10421) / 0.000 (104150) | 0.000 (6553) / 0.000 (51785) | 0.000 (6747) / 0.000 (4775) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| mix:doseM0.1:0.25 | 0.000 (10773) [rej. blind 0.000] / 0.000 (103526) [rej. blind 0.000] | 0.000 (6495) / 0.000 (49754) | 0.000 (6345) / 0.000 (4513) | — / — | 3.4 ± 0.3 | -2610 |
| careful | 0.000 (10421) [rej. blind 0.000] / 0.000 (104150) [rej. blind 0.000] | 0.000 (6553) / 0.000 (51785) | 0.000 (6747) / 0.000 (4775) | — / — | 3.7 ± 0.4 | +31 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:doseM0.1:0.25 | — | 0.920 | — (0) | — (0) | 0.000 (29211) | 0.000 (2163) | 0.000 (150032) | 5.200 | 677.475 | 1.164 | 1.356 |
| careful | — | 0.910 | — (0) | — (0) | 0.000 (33827) | 0.000 (317) | 0.000 (150287) | 4.525 | 685.975 | 1.132 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| mix:doseM0.1:0.25 | 39.625 | 0.000 | 0.000 | 0.000 | 0.000 | 0.175 | 0.000 |
| careful | 39.575 | 0.000 | 0.000 | 0.000 | 0.000 | 0.250 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:doseM0.1:0.25 | 22.425 / 39.625 | 3.400 ± 0.258 | +0.775 ± 0.362 | 12.975 | +3.900 ± 0.826 | 3.025 | 0.074 | 5.200 | +0.675 ± 0.376 | 1910.725 | 0.017 | +0.002 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 25138.777 ± 269.607 | -37.748 ± 341.688 | 36180.9 ± 584.4 | -166.6 ± 589.6 | 36.100 | -0.073 ± 0.328 | 15.085 ± 0.305 | +0.071 ± 0.396 | 17.509 | 0.001 | 2593.650 | 19.625 | 17.200 | +0.650 ± 0.299 | 667.680 | 243.450 |
| careful | 23.025 / 39.575 | 2.625 ± 0.292 | — | 9.075 | — | 3.200 | 0.049 | 4.525 | — | 1887.075 | 0.015 | — | 0.000 / 0.000 (0.000 / 0.000) | 25176.525 ± 271.124 | — | 36347.5 ± 769.0 | — | 36.173 | — | 15.014 ± 0.350 | — | 17.590 | 0.002 | 2604.975 | 19.575 | 16.550 | — | 690.797 | 281.025 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **mix:doseM0.1:0.25**: p0 1.000/0.000/0.000 (597); p1 1.000/0.000/0.000 (720); p2 1.000/0.000/0.000 (860); p3 1.000/0.000/0.000 (971); p4 1.000/0.000/0.000 (965); p5 1.000/0.000/0.000 (315); p6 1.000/0.000/0.000 (36); p7 1.000/0.000/0.000 (6)
- **careful**: p0 1.000/0.000/0.000 (611); p1 1.000/0.000/0.000 (791); p2 1.000/0.000/0.000 (925); p3 1.000/0.000/0.000 (1013); p4 1.000/0.000/0.000 (1003); p5 1.000/0.000/0.000 (267)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:doseM0.1:0.25 | 2588.2 / 269.3 | 0.26 / 0.16 | -0.10 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.12 / 0.11 | -0.00 ± 0.00 | 0.178 / 0.143 | -0.035 ± 0.004 | 0.073 / 0.081 | 0.001 / 0.000 | 0.055 / 0.057 | +0.001 ± 0.003 | 1.62 / 1.33 | -0.29 ± 0.06 |
| careful | 2603.8 / 260.5 | 0.26 / 0.17 | -0.08 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.12 / 0.11 | -0.01 ± 0.00 | 0.162 / 0.135 | -0.027 ± 0.004 | 0.064 / 0.070 | 0.002 / 0.000 | 0.053 / 0.051 | -0.002 ± 0.002 | 1.64 / 1.35 | -0.29 ± 0.09 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| mix:doseM0.1:0.25 | -0.10 ± 0.01 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.035 ± 0.004 | +0.007 ± 0.002 | +0.002 ± 0.003 |
| careful | -0.08 ± 0.01 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.027 ± 0.004 | +0.006 ± 0.002 | -0.002 ± 0.002 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| mix:doseM0.1:0.25 | 0.474 / 0.148 | 0.31 / 0.32 | 0.039 / 0.158 | 0.00 / 0.00 | 0.29 / 0.34 | 0.472 / 0.261 |
| careful | 0.491 / 0.142 | 0.30 / 0.32 | 0.038 / 0.164 | 0.00 / 0.00 | 0.29 / 0.31 | 0.436 / 0.230 |

# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --arm 4 --temptation 1 --gv 10 --bond-mult-later 1`, seeds 21-40, hide ``, model `None` (value off, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 29363.1 ± 525.9 | -321.5 ± 677.3 | 3150.8 | 0.887 | 0.013 | 0.001 | 0.090 | 0.117 | 0.001 | 1.000 | 4.90 | 58.65 | 0.45 |
| careful | 29684.6 ± 609.8 | nan ± nan | 2897.3 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 2.90 | 0.00 | 0.60 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| direct | 0.090 (12697) [rej. blind 0.002] / 0.117 (50273) [rej. blind 0.000] | — / 1.000 (42) [rej. blind 0.095] | — / 1.000 (4) [rej. blind 1.000] | — / — |
| careful | 0.000 (5277) / 0.000 (52668) | — / 0.000 (1) | — / — | — / — |

The stressed world's fourth action by seat kind — the allowance claimed and the verdict F without inspecting (counted above among the blind verdicts; the ledger sees a careful review, so the measured reading below cannot see it):

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| direct | 0.076 (12697) / 0.104 (50273) | — / 0.595 (42) | — / 0.000 (4) | — / — |
| careful | 0.000 (5277) / 0.000 (52668) | — / 0.000 (1) | — / — | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| direct | 0.020 (12697) [rej. blind 0.006] / 0.028 (50273) [rej. blind 0.003] | — / 0.405 (42) [rej. blind 0.095] | — / 1.000 (4) [rej. blind 1.000] | — / — | 50.1 ± 1.3 | -5395 |
| careful | 0.011 (5277) [rej. blind 0.009] / 0.014 (52668) [rej. blind 0.003] | — / 0.000 (1) | — / — | — / — | 53.3 ± 1.5 | +787 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 0.998 | 0.999 | — (0) | — (0) | 0.030 (100) | 0.007 (148) | 0.013 (62768) | 32.700 | 403.400 | 1.240 | 1.794 |
| careful | — | 0.946 | — (0) | — (0) | 0.000 (6401) | — (0) | 0.000 (51545) | 24.450 | 653.600 | 1.191 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| direct | 39.850 | 0.000 | 0.000 | 0.000 | 0.000 | 0.450 | 0.000 |
| careful | 39.650 | 0.000 | 0.000 | 0.000 | 0.000 | 0.600 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 17.800 / 39.850 | 4.900 ± 0.435 | +2.000 ± 0.417 | 63.050 | +54.150 ± 1.736 | 7.250 | 0.103 | 12.850 | +8.050 ± 0.639 | 1983.800 | 0.043 | +0.025 ± 0.002 | 0.000 / 0.000 (0.000 / 0.000) | 25094.147 ± 397.157 | +5811.876 ± 486.246 | 29363.1 ± 525.9 | -321.5 ± 677.3 | 32.838 | -5.089 ± 0.484 | 20.116 ± 0.502 | +5.950 ± 0.679 | 18.466 | 0.004 | 2511.150 | 19.850 | 22.050 | +2.500 ± 0.380 | 58.716 | 892.750 |
| careful | 20.100 / 39.650 | 2.900 ± 0.390 | — | 8.900 | — | 3.350 | 0.046 | 4.800 | — | 1902.800 | 0.018 | — | 0.000 / 0.000 (0.000 / 0.000) | 19282.271 ± 424.603 | — | 29684.6 ± 609.8 | — | 37.927 | — | 14.167 ± 0.344 | — | 16.820 | 0.001 | 2638.000 | 19.650 | 19.550 | — | 1013.908 | 686.050 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **direct**: p0 0.993/0.006/0.000 (504); p1 0.971/0.026/0.003 (337); p2 0.967/0.032/0.001 (261); p3 0.979/0.020/0.001 (200); p4 0.974/0.026/0.001 (173); p5 0.996/0.002/0.002 (161); p6 0.981/0.018/0.001 (169); p7 0.987/0.012/0.000 (167); p8 0.990/0.009/0.001 (169); p9 0.995/0.005/0.000 (176); p10 0.994/0.006/0.001 (181); p11 0.997/0.002/0.001 (164); p12 0.986/0.014/0.000 (95); p13 0.984/0.016/0.000 (59); p14 0.988/0.004/0.008 (25)
- **careful**: p0 1.000/0.000/0.000 (557); p1 1.000/0.000/0.000 (534); p2 1.000/0.000/0.000 (542); p3 1.000/0.000/0.000 (541); p4 1.000/0.000/0.000 (547); p5 1.000/0.000/0.000 (175); p6 1.000/0.000/0.000 (2)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 2513.7 / 634.9 | 0.48 / 0.42 | -0.06 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.16 / 0.12 | -0.04 ± 0.01 | 0.263 / 0.245 | -0.018 ± 0.009 | 0.123 / 0.136 | 0.004 / 0.000 | 0.093 / 0.108 | +0.015 ± 0.005 | 2.31 / 2.04 | -0.27 ± 0.08 |
| careful | 2633.4 / 263.9 | 0.18 / 0.10 | -0.09 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.11 / 0.12 | +0.01 ± 0.00 | 0.111 / 0.090 | -0.021 ± 0.005 | 0.041 / 0.044 | 0.001 / 0.000 | 0.060 / 0.067 | +0.007 ± 0.003 | 1.56 / 1.34 | -0.23 ± 0.07 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| direct | -0.08 ± 0.02 | +0.00 ± 0.00 | -0.02 ± 0.01 | -0.044 ± 0.005 | -0.010 ± 0.004 | -0.003 ± 0.004 |
| careful | -0.09 ± 0.02 | +0.00 ± 0.00 | +0.01 ± 0.00 | -0.023 ± 0.005 | +0.003 ± 0.003 | +0.007 ± 0.003 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| direct | 0.001 / 0.000 | 0.37 / — | 0.034 / 0.000 | 0.00 / — | — / — | 0.966 / 0.000 |
| careful | 0.000 / 0.000 | 0.00 / — | 0.038 / 0.000 | 0.00 / — | — / — | 0.883 / 0.000 |

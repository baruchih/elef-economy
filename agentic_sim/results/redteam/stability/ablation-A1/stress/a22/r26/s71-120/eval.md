# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1 --arm 1 --pi-a0 0.10 --pi-a-max 0.10 --w-audit 1.5`, seeds 71-120, hide ``, model `None` (value off, horizon 8)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:caseM0.2:1.0 | 33682.4 ± 403.1 | nan ± nan | 3912.6 | 0.823 | 0.000 | 0.000 | 0.173 | 0.157 | 0.188 | 0.247 | 24.00 | 98.58 | 0.34 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:caseM0.2:1.0 | 0.173 (33960) / 0.157 (124960) | 0.349 (5797) / 0.241 (26046) | 0.207 (3341) / 0.066 (1526) | — / — |

The stressed world's fourth action by seat kind — the allowance claimed and the verdict F without inspecting (counted above among the blind verdicts; the ledger sees a careful review, so the measured reading below cannot see it):

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:caseM0.2:1.0 | 0.173 (33960) / 0.157 (124960) | 0.349 (5797) / 0.241 (26046) | 0.207 (3341) / 0.066 (1526) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| mix:caseM0.2:1.0 | 0.000 (33960) [rej. blind 0.000] / 0.000 (124960) [rej. blind 0.000] | 0.000 (5797) / 0.000 (26046) | 0.000 (3341) / 0.000 (1526) | — / — | 1.4 ± 0.2 | -34568 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:caseM0.2:1.0 | — | 0.998 | — (0) | — (0) | 0.000 (755) | 0.000 (1511) | 0.000 (193364) | 6.960 | 418.520 | 1.327 | 14.164 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| mix:caseM0.2:1.0 | 39.640 | 0.000 | 0.000 | 0.000 | 0.000 | 0.340 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:caseM0.2:1.0 | 21.060 / 39.640 | 24.000 ± 1.310 | — | 108.900 | — | 6.900 | 0.245 | 6.960 | — | 1994.440 | 0.041 | — | 0.000 / 0.000 (0.000 / 0.000) | 26598.671 ± 260.454 | — | 33682.4 ± 403.1 | — | 32.629 | — | 19.038 ± 0.319 | — | 18.000 | 0.004 | 2494.480 | 19.640 | 18.580 | — | 64.345 | 163.680 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **mix:caseM0.2:1.0**: p0 1.000/0.000/0.000 (502); p1 1.000/0.000/0.000 (364); p2 1.000/0.000/0.000 (319); p3 1.000/0.000/0.000 (298); p4 1.000/0.000/0.000 (267); p5 1.000/0.000/0.000 (219); p6 1.000/0.000/0.000 (200); p7 1.000/0.000/0.000 (180); p8 1.000/0.000/0.000 (156); p9 1.000/0.000/0.000 (155); p10 1.000/0.000/0.000 (140); p11 1.000/0.000/0.000 (131); p12 1.000/0.000/0.000 (112); p13 1.000/0.000/0.000 (98); p14 1.000/0.000/0.000 (66); p15 1.000/0.000/0.000 (11); p16 1.000/0.000/0.000 (1)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:caseM0.2:1.0 | 2499.2 / 679.2 | 0.57 / 0.61 | +0.04 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.04 / 0.04 | -0.01 ± 0.00 | 0.307 / 0.295 | -0.012 ± 0.005 | 0.149 / 0.164 | 0.004 / 0.000 | 0.107 / 0.118 | +0.010 ± 0.002 | 2.10 / 2.09 | -0.01 ± 0.05 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| mix:caseM0.2:1.0 | -0.04 ± 0.01 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.047 ± 0.002 | -0.009 ± 0.002 | +0.001 ± 0.002 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| mix:caseM0.2:1.0 | 0.208 / 0.103 | 0.57 / 0.63 | 0.033 / 0.082 | 0.00 / 0.00 | 0.56 / 0.67 | 0.818 / 0.514 |

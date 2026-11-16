# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1 --arm 4`, seeds 61-120, hide ``, model `None` (value off, horizon 8)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 30483.1 ± 486.5 | -291.3 ± 418.8 | 2941.6 | 0.977 | 0.000 | 0.000 | 0.024 | 0.023 | 0.000 | 0.115 | 3.13 | 12.22 | 0.30 |
| careful | 30774.5 ± 395.3 | nan ± nan | 2911.5 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 2.28 | 0.00 | 0.35 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:dose0.1:0.25 | 0.024 (17579) / 0.023 (158892) | — / 0.115 (26) | — / — | — / — |
| careful | 0.000 (16090) / 0.000 (158565) | — / 0.000 (34) | — / 0.000 (1) | — / — |

The stressed world's fourth action by seat kind — the allowance claimed and the verdict F without inspecting (counted above among the blind verdicts; the ledger sees a careful review, so the measured reading below cannot see it):

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:dose0.1:0.25 | 0.024 (17579) / 0.023 (158892) | — / 0.115 (26) | — / — | — / — |
| careful | 0.000 (16090) / 0.000 (158565) | — / 0.000 (34) | — / 0.000 (1) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 0.001 (17579) [rej. blind 0.001] / 0.000 (158892) [rej. blind 0.000] | — / 0.000 (26) | — / — | — / — | 5.6 ± 0.4 | -3986 |
| careful | 0.001 (16090) [rej. blind 0.001] / 0.000 (158565) [rej. blind 0.000] | — / 0.000 (34) | — / 0.000 (1) | — / — | 5.8 ± 0.4 | +79 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | — | 0.959 | — (0) | — (0) | 0.000 (14534) | 0.000 (2494) | 0.000 (159469) | 6.650 | 619.650 | 1.195 | 1.837 |
| careful | — | 0.951 | — (0) | — (0) | 0.000 (17204) | 0.000 (694) | 0.000 (156792) | 4.983 | 681.617 | 1.175 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 39.333 | 0.000 | 0.000 | 0.000 | 0.000 | 0.300 | 0.000 |
| careful | 39.450 | 0.000 | 0.000 | 0.000 | 0.000 | 0.350 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 19.750 / 39.333 | 3.133 ± 0.231 | +0.850 ± 0.296 | 15.283 | +5.267 ± 0.917 | 3.950 | 0.062 | 6.650 | +1.667 ± 0.371 | 1953.317 | 0.023 | +0.006 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 19831.832 ± 272.541 | -186.616 ± 291.855 | 30483.1 ± 486.5 | -291.3 ± 418.8 | 38.001 | +0.095 ± 0.290 | 14.489 ± 0.300 | +0.318 ± 0.317 | 16.628 | 0.001 | 2651.567 | 19.333 | 19.583 | +0.833 ± 0.288 | 949.821 | 293.367 |
| careful | 20.700 / 39.450 | 2.283 ± 0.170 | — | 10.017 | — | 3.317 | 0.045 | 4.983 | — | 1915.583 | 0.017 | — | 0.000 / 0.000 (0.000 / 0.000) | 20018.448 ± 215.534 | — | 30774.5 ± 395.3 | — | 37.906 | — | 14.172 ± 0.165 | — | 16.770 | 0.002 | 2644.117 | 19.450 | 18.750 | — | 960.636 | 320.217 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **mix:dose0.1:0.25**: p0 1.000/0.000/0.000 (543); p1 1.000/0.000/0.000 (518); p2 1.000/0.000/0.000 (491); p3 1.000/0.000/0.000 (490); p4 1.000/0.000/0.000 (479); p5 1.000/0.000/0.000 (265); p6 1.000/0.000/0.000 (56); p7 1.000/0.000/0.000 (18); p8 1.000/0.000/0.000 (8); p9 1.000/0.000/0.000 (7)
- **careful**: p0 1.000/0.000/0.000 (557); p1 1.000/0.000/0.000 (537); p2 1.000/0.000/0.000 (536); p3 1.000/0.000/0.000 (541); p4 1.000/0.000/0.000 (534); p5 1.000/0.000/0.000 (203); p6 1.000/0.000/0.000 (4)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 2648.2 / 293.0 | 0.14 / 0.08 | -0.07 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.06 / 0.07 | +0.01 ± 0.00 | 0.101 / 0.080 | -0.021 ± 0.003 | 0.035 / 0.037 | 0.001 / 0.000 | 0.061 / 0.069 | +0.009 ± 0.002 | 1.39 / 1.23 | -0.16 ± 0.04 |
| careful | 2642.8 / 268.2 | 0.18 / 0.10 | -0.08 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.06 / 0.07 | +0.01 ± 0.00 | 0.120 / 0.101 | -0.019 ± 0.003 | 0.042 / 0.046 | 0.002 / 0.000 | 0.059 / 0.064 | +0.005 ± 0.002 | 1.53 / 1.24 | -0.28 ± 0.07 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | -0.07 ± 0.01 | +0.00 ± 0.00 | +0.01 ± 0.00 | -0.021 ± 0.003 | +0.002 ± 0.002 | +0.008 ± 0.002 |
| careful | -0.08 ± 0.01 | +0.00 ± 0.00 | +0.01 ± 0.00 | -0.019 ± 0.003 | +0.004 ± 0.002 | +0.005 ± 0.002 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 0.000 / 0.000 | 0.74 / — | 0.039 / 0.000 | 0.00 / — | — / — | 0.903 / 0.000 |
| careful | 0.000 / 0.000 | 0.52 / — | 0.040 / 0.000 | 0.00 / — | — / — | 0.888 / 0.000 |

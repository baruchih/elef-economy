# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1 --arm 1 --pi-a0 0.10 --pi-a-max 0.10 --w-audit 3`, seeds 21-80, hide ``, model `None` (value off, horizon 8)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 35311.8 ± 479.5 | 227.4 ± 528.4 | 4584.6 | 0.979 | 0.000 | 0.000 | 0.025 | 0.025 | 0.371 | 0.015 | 3.82 | 13.78 | 0.35 |
| careful | 35084.4 ± 469.0 | nan ± nan | 4523.7 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.368 | 0.000 | 2.42 | 0.00 | 0.37 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:dose0.1:0.25 | 0.025 (17507) / 0.025 (155405) | 0.015 (10182) / 0.015 (75115) | 0.014 (9869) / 0.016 (6999) | — / — |
| careful | 0.000 (15893) / 0.000 (155552) | 0.000 (9419) / 0.000 (73480) | 0.000 (9742) / 0.000 (7337) | — / — |

The stressed world's fourth action by seat kind — the allowance claimed and the verdict F without inspecting (counted above among the blind verdicts; the ledger sees a careful review, so the measured reading below cannot see it):

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:dose0.1:0.25 | 0.025 (17507) / 0.025 (155405) | 0.015 (10182) / 0.015 (75115) | 0.014 (9869) / 0.016 (6999) | — / — |
| careful | 0.000 (15893) / 0.000 (155552) | 0.000 (9419) / 0.000 (73480) | 0.000 (9742) / 0.000 (7337) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 0.000 (17507) [rej. blind 0.000] / 0.000 (155405) [rej. blind 0.000] | 0.000 (10182) / 0.000 (75115) | 0.000 (9869) / 0.000 (6999) | — / — | 3.2 ± 0.3 | -5867 |
| careful | 0.000 (15893) [rej. blind 0.000] / 0.000 (155552) [rej. blind 0.000] | 0.000 (9419) / 0.000 (73480) | 0.000 (9742) / 0.000 (7337) | — / — | 2.9 ± 0.2 | +28 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | — | 0.930 | — (0) | — (0) | 0.000 (37572) | 0.000 (9301) | 0.000 (228204) | 6.800 | 641.067 | 1.185 | 2.027 |
| careful | — | 0.917 | — (0) | — (0) | 0.000 (45788) | 0.000 (2057) | 0.000 (223578) | 5.367 | 662.867 | 1.199 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 39.650 | 0.000 | 0.000 | 0.000 | 0.000 | 0.350 | 0.000 |
| careful | 39.617 | 0.000 | 0.000 | 0.000 | 0.000 | 0.367 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 22.450 / 39.650 | 3.817 ± 0.249 | +1.400 ± 0.303 | 16.183 | +5.550 ± 0.904 | 4.183 | 0.079 | 6.800 | +1.433 ± 0.409 | 1917.617 | 0.021 | +0.006 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 25169.435 ± 226.965 | +462.214 ± 275.581 | 35311.8 ± 479.5 | +227.4 ± 528.4 | 35.674 | -0.439 ± 0.256 | 15.546 ± 0.257 | +0.244 ± 0.321 | 17.677 | 0.001 | 2594.300 | 19.650 | 17.200 | +0.467 ± 0.291 | 593.799 | 246.333 |
| careful | 22.883 / 39.617 | 2.417 ± 0.192 | — | 10.633 | — | 3.517 | 0.052 | 5.367 | — | 1890.783 | 0.015 | — | 0.000 / 0.000 (0.000 / 0.000) | 24707.221 ± 217.118 | — | 35084.4 ± 469.0 | — | 36.113 | — | 15.302 ± 0.265 | — | 17.547 | 0.001 | 2597.683 | 19.617 | 16.733 | — | 680.375 | 235.883 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **mix:dose0.1:0.25**: p0 1.000/0.000/0.000 (582); p1 1.000/0.000/0.000 (675); p2 1.000/0.000/0.000 (823); p3 1.000/0.000/0.000 (895); p4 1.000/0.000/0.000 (875); p5 1.000/0.000/0.000 (452); p6 1.000/0.000/0.000 (129); p7 1.000/0.000/0.000 (43); p8 1.000/0.000/0.000 (11); p9 1.000/0.000/0.000 (1)
- **careful**: p0 1.000/0.000/0.000 (588); p1 1.000/0.000/0.000 (729); p2 1.000/0.000/0.000 (890); p3 1.000/0.000/0.000 (981); p4 1.000/0.000/0.000 (994); p5 1.000/0.000/0.000 (321); p6 1.000/0.000/0.000 (22)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 2590.1 / 291.8 | 0.28 / 0.20 | -0.08 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.12 / 0.12 | +0.00 ± 0.00 | 0.181 / 0.147 | -0.035 ± 0.003 | 0.072 / 0.079 | 0.001 / 0.000 | 0.058 / 0.056 | -0.002 ± 0.002 | 1.66 / 1.39 | -0.27 ± 0.06 |
| careful | 2592.5 / 264.9 | 0.26 / 0.17 | -0.10 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.12 / 0.11 | -0.00 ± 0.00 | 0.175 / 0.141 | -0.033 ± 0.003 | 0.072 / 0.079 | 0.001 / 0.000 | 0.056 / 0.058 | +0.002 ± 0.002 | 1.66 / 1.33 | -0.34 ± 0.06 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | -0.08 ± 0.01 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.036 ± 0.003 | +0.005 ± 0.002 | -0.001 ± 0.002 |
| careful | -0.10 ± 0.01 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.034 ± 0.003 | +0.006 ± 0.002 | +0.002 ± 0.002 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 0.477 / 0.158 | 0.29 / 0.31 | 0.039 / 0.152 | 0.00 / 0.00 | 0.28 / 0.30 | 0.477 / 0.248 |
| careful | 0.466 / 0.138 | 0.28 / 0.32 | 0.041 / 0.166 | 0.00 / 0.00 | 0.27 / 0.31 | 0.473 / 0.257 |

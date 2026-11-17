# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1 --arm 1 --pi-a0 0.10 --pi-a-max 0.10 --w-audit 1.5`, seeds 96-120, hide ``, model `None` (value off, horizon 8)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:doseM0.1:1.0 | 36360.2 ± 689.3 | nan ± nan | 4693.6 | 0.919 | 0.000 | 0.000 | 0.074 | 0.070 | 0.365 | 0.100 | 8.44 | 42.08 | 0.40 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:doseM0.1:1.0 | 0.074 (10823) / 0.070 (63723) | 0.096 (5356) / 0.100 (30462) | 0.101 (4522) / 0.104 (2454) | — / — |

The stressed world's fourth action by seat kind — the allowance claimed and the verdict F without inspecting (counted above among the blind verdicts; the ledger sees a careful review, so the measured reading below cannot see it):

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:doseM0.1:1.0 | 0.074 (10823) / 0.070 (63723) | 0.096 (5356) / 0.100 (30462) | 0.101 (4522) / 0.104 (2454) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| mix:doseM0.1:1.0 | 0.000 (10823) [rej. blind 0.000] / 0.000 (63723) [rej. blind 0.000] | 0.000 (5356) / 0.000 (30462) | 0.000 (4522) / 0.000 (2454) | — / — | 2.5 ± 0.3 | -9561 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:doseM0.1:1.0 | — | 0.973 | — (0) | — (0) | 0.000 (5956) | 0.000 (3211) | 0.000 (108173) | 5.280 | 577.440 | 1.224 | 7.970 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| mix:doseM0.1:1.0 | 39.600 | 0.000 | 0.000 | 0.000 | 0.000 | 0.400 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:doseM0.1:1.0 | 21.640 / 39.600 | 8.440 ± 0.817 | — | 39.600 | — | 4.960 | 0.141 | 5.280 | — | 1970.360 | 0.029 | — | 0.000 / 0.000 (0.000 / 0.000) | 27175.119 ± 485.622 | — | 36360.2 ± 689.3 | — | 34.333 | — | 17.040 ± 0.553 | — | 18.004 | 0.004 | 2547.960 | 19.600 | 17.960 | — | 331.624 | 208.680 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **mix:doseM0.1:1.0**: p0 1.000/0.000/0.000 (559); p1 1.000/0.000/0.000 (564); p2 1.000/0.000/0.000 (586); p3 1.000/0.000/0.000 (642); p4 1.000/0.000/0.000 (620); p5 1.000/0.000/0.000 (410); p6 1.000/0.000/0.000 (251); p7 1.000/0.000/0.000 (194); p8 1.000/0.000/0.000 (151); p9 1.000/0.000/0.000 (137); p10 1.000/0.000/0.000 (104); p11 1.000/0.000/0.000 (67); p12 1.000/0.000/0.000 (23); p13 1.000/0.000/0.000 (2)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:doseM0.1:1.0 | 2548.9 / 432.9 | 0.38 / 0.28 | -0.10 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.11 / 0.12 | +0.00 ± 0.00 | 0.224 / 0.192 | -0.032 ± 0.006 | 0.097 / 0.102 | 0.003 / 0.000 | 0.067 / 0.065 | -0.002 ± 0.003 | 1.90 / 1.76 | -0.14 ± 0.06 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| mix:doseM0.1:1.0 | -0.08 ± 0.01 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.036 ± 0.005 | +0.000 ± 0.003 | -0.000 ± 0.003 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| mix:doseM0.1:1.0 | 0.471 / 0.208 | 0.33 / 0.32 | 0.036 / 0.125 | 0.00 / 0.00 | 0.33 / 0.35 | 0.519 / 0.227 |

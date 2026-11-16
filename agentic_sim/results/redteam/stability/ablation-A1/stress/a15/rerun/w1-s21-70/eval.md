# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1 --pi-a0 0.10 --pi-a-max 0.10 --w-audit 1.5`, seeds 21-70, hide ``, model `None` (value off, horizon 8)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 34756.7 ± 506.5 | -968.0 ± 511.2 | 4712.1 | 0.979 | 0.000 | 0.000 | 0.024 | 0.025 | 0.387 | 0.015 | 3.62 | 13.58 | 0.28 |
| careful | 35724.7 ± 498.2 | nan ± nan | 4614.9 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.383 | 0.000 | 2.60 | 0.00 | 0.26 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:dose0.1:0.25 | 0.024 (15053) / 0.025 (129292) | 0.015 (8740) / 0.014 (63720) | 0.014 (8612) / 0.016 (10189) | — / — |
| careful | 0.000 (13210) / 0.000 (129198) | 0.000 (7987) / 0.000 (62142) | 0.000 (8027) / 0.000 (10182) | — / — |

The stressed world's fourth action by seat kind — the allowance claimed and the verdict F without inspecting (counted above among the blind verdicts; the ledger sees a careful review, so the measured reading below cannot see it):

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:dose0.1:0.25 | 0.024 (15053) / 0.025 (129292) | 0.015 (8740) / 0.014 (63720) | 0.014 (8612) / 0.016 (10189) | — / — |
| careful | 0.000 (13210) / 0.000 (129198) | 0.000 (7987) / 0.000 (62142) | 0.000 (8027) / 0.000 (10182) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 0.000 (15053) [rej. blind 0.000] / 0.000 (129292) [rej. blind 0.000] | 0.000 (8740) / 0.000 (63720) | 0.000 (8612) / 0.000 (10189) | — / — | 2.6 ± 0.3 | -4913 |
| careful | 0.000 (13210) [rej. blind 0.000] / 0.000 (129198) [rej. blind 0.000] | 0.000 (7987) / 0.000 (62142) | 0.000 (8027) / 0.000 (10182) | — / — | 2.8 ± 0.3 | +21 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | — | 0.927 | — (0) | — (0) | 0.000 (32716) | 0.000 (10896) | 0.000 (191994) | 6.360 | 624.920 | 1.207 | 2.135 |
| careful | — | 0.911 | — (0) | — (0) | 0.000 (41143) | 0.000 (1674) | 0.000 (187929) | 4.720 | 677.480 | 1.183 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 39.680 | 0.000 | 0.000 | 0.000 | 0.000 | 0.280 | 0.000 |
| careful | 39.680 | 0.000 | 0.000 | 0.000 | 0.000 | 0.260 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 22.940 / 39.680 | 3.620 ± 0.293 | +1.020 ± 0.364 | 16.580 | +5.800 ± 1.081 | 3.780 | 0.076 | 6.360 | +1.640 ± 0.402 | 1927.060 | 0.029 | +0.005 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 25850.593 ± 356.039 | +832.141 ± 378.386 | 34756.7 ± 506.5 | -968.0 ± 511.2 | 35.627 | -0.398 ± 0.291 | 16.357 ± 0.385 | +1.376 ± 0.396 | 18.085 | 0.001 | 2591.480 | 19.680 | 16.740 | +0.440 ± 0.325 | 534.131 | 225.980 |
| careful | 23.380 / 39.680 | 2.600 ± 0.241 | — | 10.780 | — | 3.100 | 0.061 | 4.720 | — | 1890.420 | 0.024 | — | 0.000 / 0.000 (0.000 / 0.000) | 25018.452 ± 249.982 | — | 35724.7 ± 498.2 | — | 36.025 | — | 14.981 ± 0.253 | — | 18.044 | 0.002 | 2586.940 | 19.680 | 16.300 | — | 666.885 | 213.580 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **mix:dose0.1:0.25**: p0 1.000/0.000/0.000 (580); p1 1.000/0.000/0.000 (689); p2 1.000/0.000/0.000 (816); p3 1.000/0.000/0.000 (887); p4 1.000/0.000/0.000 (885); p5 1.000/0.000/0.000 (478); p6 1.000/0.000/0.000 (198); p7 1.000/0.000/0.000 (54); p8 1.000/0.000/0.000 (20); p9 1.000/0.000/0.000 (5)
- **careful**: p0 1.000/0.000/0.000 (605); p1 1.000/0.000/0.000 (737); p2 1.000/0.000/0.000 (919); p3 1.000/0.000/0.000 (1014); p4 1.000/0.000/0.000 (1010); p5 1.000/0.000/0.000 (290); p6 1.000/0.000/0.000 (34); p7 1.000/0.000/0.000 (5)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 2585.8 / 301.1 | 0.28 / 0.16 | -0.12 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.13 / 0.13 | +0.01 ± 0.00 | 0.180 / 0.143 | -0.037 ± 0.004 | 0.073 / 0.077 | 0.001 / 0.000 | 0.056 / 0.049 | -0.008 ± 0.002 | 1.68 / 1.36 | -0.33 ± 0.05 |
| careful | 2584.0 / 264.2 | 0.32 / 0.22 | -0.10 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.13 / 0.12 | -0.00 ± 0.00 | 0.180 / 0.150 | -0.029 ± 0.004 | 0.074 / 0.085 | 0.002 / 0.000 | 0.057 / 0.051 | -0.006 ± 0.002 | 1.87 / 1.46 | -0.40 ± 0.06 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | -0.11 ± 0.01 | +0.00 ± 0.00 | +0.00 ± 0.00 | -0.036 ± 0.004 | +0.003 ± 0.003 | -0.007 ± 0.002 |
| careful | -0.10 ± 0.01 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.030 ± 0.004 | +0.010 ± 0.002 | -0.005 ± 0.002 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 0.486 / 0.161 | 0.29 / 0.28 | 0.038 / 0.151 | 0.00 / 0.00 | 0.28 / 0.30 | 0.306 / 0.236 |
| careful | 0.474 / 0.142 | 0.30 / 0.31 | 0.040 / 0.161 | 0.00 / 0.00 | 0.29 / 0.33 | 0.304 / 0.254 |

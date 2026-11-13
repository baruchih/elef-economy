# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --pi-a0 0.10 --pi-a-max 0.10 --bond-mult-later 1 --w-audit 1.5`, seeds 21-80, hide ``, model `None` (value off, horizon 8)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose1audit:0.25 | 34651.2 ± 421.4 | -731.3 ± 444.8 | 4532.0 | 0.979 | 0.000 | 0.000 | 0.000 | 0.000 | 0.368 | 0.057 | 3.55 | 1.08 | 0.32 |
| careful | 35382.5 ± 455.9 | nan ± nan | 4620.9 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.382 | 0.000 | 2.58 | 0.00 | 0.28 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:dose1audit:0.25 | 0.000 (16020) / 0.000 (155944) | 0.070 (9061) / 0.072 (71062) | 0.000 (8577) / 0.000 (11254) | — / — |
| careful | 0.000 (15961) / 0.000 (155290) | 0.000 (9589) / 0.000 (74537) | 0.000 (9713) / 0.000 (12163) | — / — |

The stressed world's fourth action by seat kind — the allowance claimed and the verdict F without inspecting (counted above among the blind verdicts; the ledger sees a careful review, so the measured reading below cannot see it):

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:dose1audit:0.25 | 0.000 (16020) / 0.000 (155944) | 0.070 (9061) / 0.072 (71062) | 0.000 (8577) / 0.000 (11254) | — / — |
| careful | 0.000 (15961) / 0.000 (155290) | 0.000 (9589) / 0.000 (74537) | 0.000 (9713) / 0.000 (12163) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| mix:dose1audit:0.25 | 0.000 (16020) [rej. blind 0.000] / 0.000 (155944) [rej. blind 0.000] | 0.000 (9061) / 0.000 (71062) | 0.000 (8577) / 0.000 (11254) | — / — | 2.8 ± 0.3 | -5721 |
| careful | 0.000 (15961) [rej. blind 0.000] / 0.000 (155290) [rej. blind 0.000] | 0.000 (9589) / 0.000 (74537) | 0.000 (9713) / 0.000 (12163) | — / — | 2.8 ± 0.3 | +26 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose1audit:0.25 | — | 0.918 | — (0) | — (0) | 0.000 (44614) | 0.000 (3044) | 0.000 (224260) | 4.983 | 688.833 | 1.180 | 0.217 |
| careful | — | 0.912 | — (0) | — (0) | 0.000 (49195) | 0.000 (2233) | 0.000 (225825) | 4.800 | 674.017 | 1.180 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| mix:dose1audit:0.25 | 39.667 | 0.000 | 0.000 | 0.000 | 0.000 | 0.317 | 0.000 |
| careful | 39.717 | 0.000 | 0.000 | 0.000 | 0.000 | 0.283 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose1audit:0.25 | 23.000 / 39.667 | 3.550 ± 0.242 | +0.967 ± 0.280 | 9.950 | -0.817 ± 0.700 | 3.417 | 0.049 | 4.983 | +0.183 ± 0.335 | 1906.167 | 0.023 | -0.001 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 24846.966 ± 216.265 | -219.004 ± 218.453 | 34651.2 ± 421.4 | -731.3 ± 444.8 | 35.833 | -0.140 ± 0.235 | 15.535 ± 0.211 | +0.359 ± 0.281 | 18.101 | 0.002 | 2601.133 | 19.667 | 16.667 | +0.217 ± 0.295 | 593.990 | 232.667 |
| careful | 23.267 / 39.717 | 2.583 ± 0.208 | — | 10.767 | — | 3.233 | 0.060 | 4.800 | — | 1894.300 | 0.024 | — | 0.000 / 0.000 (0.000 / 0.000) | 25065.970 ± 246.254 | — | 35382.5 ± 455.9 | — | 35.973 | — | 15.176 ± 0.235 | — | 18.079 | 0.002 | 2591.900 | 19.717 | 16.450 | — | 638.886 | 213.750 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **mix:dose1audit:0.25**: p0 1.000/0.000/0.000 (586); p1 1.000/0.000/0.000 (717); p2 1.000/0.000/0.000 (865); p3 1.000/0.000/0.000 (946); p4 1.000/0.000/0.000 (960); p5 1.000/0.000/0.000 (289); p6 1.000/0.000/0.000 (52); p7 1.000/0.000/0.000 (21)
- **careful**: p0 1.000/0.000/0.000 (603); p1 1.000/0.000/0.000 (730); p2 1.000/0.000/0.000 (912); p3 1.000/0.000/0.000 (1009); p4 1.000/0.000/0.000 (1008); p5 1.000/0.000/0.000 (300); p6 1.000/0.000/0.000 (54); p7 1.000/0.000/0.000 (4)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose1audit:0.25 | 2599.1 / 267.0 | 0.31 / 0.20 | -0.10 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.11 / 0.11 | -0.00 ± 0.00 | 0.188 / 0.152 | -0.036 ± 0.003 | 0.074 / 0.082 | 0.002 / 0.000 | 0.058 / 0.058 | -0.000 ± 0.002 | 1.74 / 1.46 | -0.29 ± 0.04 |
| careful | 2588.2 / 266.0 | 0.31 / 0.21 | -0.10 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.13 / 0.13 | -0.00 ± 0.00 | 0.177 / 0.148 | -0.029 ± 0.003 | 0.072 / 0.082 | 0.001 / 0.000 | 0.057 / 0.051 | -0.005 ± 0.002 | 1.82 / 1.46 | -0.36 ± 0.05 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| mix:dose1audit:0.25 | -0.10 ± 0.01 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.035 ± 0.003 | +0.008 ± 0.002 | +0.000 ± 0.002 |
| careful | -0.10 ± 0.01 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.030 ± 0.003 | +0.009 ± 0.002 | -0.005 ± 0.002 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| mix:dose1audit:0.25 | 0.449 / 0.131 | 0.35 / 0.38 | 0.040 / 0.163 | 0.00 / 0.00 | 0.34 / 0.37 | 0.337 / 0.283 |
| careful | 0.473 / 0.141 | 0.30 / 0.31 | 0.040 / 0.162 | 0.00 / 0.00 | 0.29 / 0.33 | 0.305 / 0.256 |

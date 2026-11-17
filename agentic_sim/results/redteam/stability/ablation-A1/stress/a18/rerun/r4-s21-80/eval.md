# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1 --arm 1 --pi-a0 0.10 --pi-a-max 0.10 --w-audit 3`, seeds 21-80, hide ``, model `None` (value off, horizon 8)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:doseM0.3:0.25 | 35207.5 ± 437.6 | nan ± nan | 4753.5 | 0.960 | 0.000 | 0.000 | 0.059 | 0.053 | 0.379 | 0.018 | 4.15 | 27.62 | 0.37 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:doseM0.3:0.25 | 0.059 (23638) / 0.053 (153510) | 0.018 (12612) / 0.018 (77041) | 0.015 (11502) / 0.019 (6907) | — / — |

The stressed world's fourth action by seat kind — the allowance claimed and the verdict F without inspecting (counted above among the blind verdicts; the ledger sees a careful review, so the measured reading below cannot see it):

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:doseM0.3:0.25 | 0.059 (23638) / 0.053 (153510) | 0.018 (12612) / 0.018 (77041) | 0.015 (11502) / 0.019 (6907) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| mix:doseM0.3:0.25 | 0.000 (23638) / 0.000 (153510) [rej. blind 0.000] | 0.000 (12612) / 0.000 (77041) [rej. blind 0.000] | 0.000 (11502) / 0.000 (6907) | — / — | 3.3 ± 0.4 | -11395 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:doseM0.3:0.25 | — | 0.955 | — (0) | — (0) | 0.000 (23809) | 0.000 (9916) | 0.000 (251485) | 5.967 | 577.800 | 1.213 | 4.628 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| mix:doseM0.3:0.25 | 39.583 | 0.000 | 0.000 | 0.000 | 0.000 | 0.367 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:doseM0.3:0.25 | 21.400 / 39.583 | 4.150 ± 0.298 | — | 32.417 | — | 4.483 | 0.122 | 5.967 | — | 1941.450 | 0.026 | — | 0.000 / 0.000 (0.000 / 0.000) | 27039.153 ± 339.981 | — | 35207.5 ± 437.6 | — | 34.684 | — | 17.133 ± 0.358 | — | 17.880 | 0.001 | 2565.017 | 19.583 | 18.183 | — | 400.646 | 225.183 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **mix:doseM0.3:0.25**: p0 1.000/0.000/0.000 (559); p1 1.000/0.000/0.000 (591); p2 1.000/0.000/0.000 (695); p3 1.000/0.000/0.000 (742); p4 1.000/0.000/0.000 (726); p5 1.000/0.000/0.000 (445); p6 1.000/0.000/0.000 (228); p7 1.000/0.000/0.000 (171); p8 1.000/0.000/0.000 (124); p9 1.000/0.000/0.000 (91); p10 1.000/0.000/0.000 (76); p11 1.000/0.000/0.000 (55); p12 1.000/0.000/0.000 (37); p13 1.000/0.000/0.000 (15); p14 1.000/0.000/0.000 (9)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:doseM0.3:0.25 | 2558.5 / 394.0 | 0.35 / 0.29 | -0.06 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.13 / 0.13 | +0.01 ± 0.00 | 0.218 / 0.194 | -0.023 ± 0.005 | 0.093 / 0.104 | 0.001 / 0.000 | 0.065 / 0.065 | +0.000 ± 0.002 | 1.81 / 1.65 | -0.16 ± 0.05 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| mix:doseM0.3:0.25 | -0.08 ± 0.01 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.038 ± 0.003 | -0.000 ± 0.002 | -0.001 ± 0.002 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| mix:doseM0.3:0.25 | 0.494 / 0.197 | 0.27 / 0.28 | 0.038 / 0.129 | 0.00 / 0.00 | 0.26 / 0.27 | 0.478 / 0.213 |

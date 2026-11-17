# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1 --arm 1 --pi-a0 0.10 --pi-a-max 0.10 --w-audit 1.5`, seeds 21-70, hide ``, model `None` (value off, horizon 8)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:doseM1.0:0.25 | 33588.2 ± 384.7 | nan ± nan | 4982.2 | 0.946 | 0.000 | 0.000 | 0.069 | 0.085 | 0.397 | 0.009 | 4.14 | 42.36 | 0.48 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:doseM1.0:0.25 | 0.069 (28598) / 0.085 (121697) | 0.006 (13528) / 0.010 (67705) | 0.007 (11526) / 0.010 (6056) | — / — |

The stressed world's fourth action by seat kind — the allowance claimed and the verdict F without inspecting (counted above among the blind verdicts; the ledger sees a careful review, so the measured reading below cannot see it):

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:doseM1.0:0.25 | 0.069 (28598) / 0.085 (121697) | 0.006 (13528) / 0.010 (67705) | 0.007 (11526) / 0.010 (6056) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| mix:doseM1.0:0.25 | 0.000 (28598) [rej. blind 0.000] / 0.000 (121697) [rej. blind 0.000] | 0.000 (13528) / 0.000 (67705) | 0.000 (11526) / 0.000 (6056) | — / — | 2.4 ± 0.3 | -13267 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:doseM1.0:0.25 | — | 0.992 | — (0) | — (0) | 0.000 (2763) | 0.000 (4843) | 0.000 (241504) | 11.520 | 420.420 | 1.228 | 3.677 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| mix:doseM1.0:0.25 | 39.660 | 0.000 | 0.000 | 0.000 | 0.000 | 0.480 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:doseM1.0:0.25 | 19.520 / 39.660 | 4.140 ± 0.301 | — | 49.880 | — | 6.640 | 0.052 | 11.520 | — | 1906.520 | 0.033 | — | 0.000 / 0.000 (0.000 / 0.000) | 30433.897 ± 277.784 | — | 33588.2 ± 384.7 | — | 32.029 | — | 20.614 ± 0.343 | — | 19.088 | 0.008 | 2435.140 | 19.660 | 20.140 | — | 89.019 | 181.480 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **mix:doseM1.0:0.25**: p0 1.000/0.000/0.000 (482); p1 1.000/0.000/0.000 (436); p2 1.000/0.000/0.000 (400); p3 1.000/0.000/0.000 (407); p4 1.000/0.000/0.000 (411); p5 1.000/0.000/0.000 (374); p6 1.000/0.000/0.000 (350); p7 1.000/0.000/0.000 (338); p8 1.000/0.000/0.000 (346); p9 1.000/0.000/0.000 (364); p10 1.000/0.000/0.000 (352); p11 1.000/0.000/0.000 (290); p12 1.000/0.000/0.000 (149); p13 1.000/0.000/0.000 (17); p14 1.000/0.000/0.000 (1)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:doseM1.0:0.25 | 2433.9 / 572.0 | 0.80 / 0.79 | -0.01 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.15 / 0.16 | +0.01 ± 0.00 | 0.365 / 0.348 | -0.017 ± 0.004 | 0.175 / 0.187 | 0.007 / 0.000 | 0.098 / 0.101 | +0.003 ± 0.002 | 2.67 / 2.75 | +0.08 ± 0.04 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| mix:doseM1.0:0.25 | -0.09 ± 0.01 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.056 ± 0.003 | -0.011 ± 0.002 | -0.001 ± 0.002 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| mix:doseM1.0:0.25 | 0.546 / 0.237 | 0.16 / 0.15 | 0.035 / 0.092 | 0.00 / 0.00 | 0.14 / 0.17 | 0.447 / 0.149 |

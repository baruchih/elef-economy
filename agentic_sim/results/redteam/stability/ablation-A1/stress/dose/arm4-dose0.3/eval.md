# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1 --arm 4`, seeds 21-40, hide ``, model `None` (value off, horizon 8)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.3:0.25 | 29845.9 ± 805.3 | -775.4 ± 914.5 | 3045.4 | 0.946 | 0.000 | 0.000 | 0.051 | 0.055 | 0.000 | 0.000 | 4.15 | 29.95 | 0.20 |
| careful | 30621.3 ± 651.3 | nan ± nan | 2932.8 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 3.05 | 0.00 | 0.20 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:dose0.3:0.25 | 0.051 (8568) / 0.055 (52338) | — / 0.000 (2) | — / — | — / — |
| careful | 0.000 (5405) / 0.000 (53247) | — / 0.000 (3) | — / — | — / — |

The stressed world's fourth action by seat kind — the allowance claimed and the verdict F without inspecting (counted above among the blind verdicts; the ledger sees a careful review, so the measured reading below cannot see it):

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:dose0.3:0.25 | 0.051 (8568) / 0.055 (52338) | — / 0.000 (2) | — / — | — / — |
| careful | 0.000 (5405) / 0.000 (53247) | — / 0.000 (3) | — / — | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| mix:dose0.3:0.25 | 0.001 (8568) [rej. blind 0.000] / 0.000 (52338) [rej. blind 0.000] | — / 0.000 (2) | — / — | — / — | 5.4 ± 0.5 | -3277 |
| careful | 0.000 (5405) [rej. blind 0.000] / 0.000 (53247) [rej. blind 0.000] | — / 0.000 (3) | — / — | — / — | 5.0 ± 0.4 | +17 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.3:0.25 | — | 0.979 | — (0) | — (0) | 0.000 (2402) | 0.000 (1547) | 0.000 (56959) | 9.950 | 531.000 | 1.181 | 3.010 |
| careful | — | 0.949 | — (0) | — (0) | 0.000 (5868) | 0.000 (476) | 0.000 (52311) | 4.550 | 640.150 | 1.213 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| mix:dose0.3:0.25 | 39.300 | 0.000 | 0.000 | 0.000 | 0.000 | 0.200 | 0.000 |
| careful | 39.350 | 0.000 | 0.000 | 0.000 | 0.000 | 0.200 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.3:0.25 | 18.700 / 39.300 | 4.150 ± 0.399 | +1.100 ± 0.615 | 32.250 | +22.900 ± 2.988 | 5.250 | 0.084 | 9.950 | +5.400 ± 0.803 | 1980.000 | 0.030 | +0.013 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 23354.819 ± 459.470 | +3717.523 ± 639.021 | 29845.9 ± 805.3 | -775.4 ± 914.5 | 35.155 | -3.524 ± 0.469 | 18.203 ± 0.783 | +4.106 ± 0.933 | 17.811 | 0.000 | 2621.750 | 19.300 | 20.600 | +1.550 ± 0.605 | 357.274 | 218.550 |
| careful | 20.300 / 39.350 | 3.050 ± 0.373 | — | 9.350 | — | 3.250 | 0.040 | 4.550 | — | 1929.250 | 0.017 | — | 0.000 / 0.000 (0.000 / 0.000) | 19637.296 ± 470.320 | — | 30621.3 ± 651.3 | — | 38.679 | — | 14.096 ± 0.426 | — | 16.293 | 0.000 | 2667.600 | 19.350 | 19.050 | — | 1064.197 | 240.650 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **mix:dose0.3:0.25**: p0 1.000/0.000/0.000 (514); p1 1.000/0.000/0.000 (417); p2 1.000/0.000/0.000 (390); p3 1.000/0.000/0.000 (361); p4 1.000/0.000/0.000 (312); p5 1.000/0.000/0.000 (286); p6 1.000/0.000/0.000 (193); p7 1.000/0.000/0.000 (126); p8 1.000/0.000/0.000 (91); p9 1.000/0.000/0.000 (74); p10 1.000/0.000/0.000 (64); p11 1.000/0.000/0.000 (36); p12 1.000/0.000/0.000 (17); p13 1.000/0.000/0.000 (0)
- **careful**: p0 1.000/0.000/0.000 (556); p1 1.000/0.000/0.000 (548); p2 1.000/0.000/0.000 (548); p3 1.000/0.000/0.000 (538); p4 1.000/0.000/0.000 (532); p5 1.000/0.000/0.000 (192); p6 1.000/0.000/0.000 (20); p7 1.000/0.000/0.000 (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.3:0.25 | 2616.9 / 428.4 | 0.22 / 0.16 | -0.06 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.07 / 0.07 | +0.00 ± 0.00 | 0.157 / 0.134 | -0.024 ± 0.008 | 0.064 / 0.067 | 0.000 / 0.000 | 0.071 / 0.084 | +0.013 ± 0.004 | 1.67 / 1.44 | -0.23 ± 0.08 |
| careful | 2662.3 / 270.2 | 0.10 / 0.06 | -0.04 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.06 / 0.07 | +0.01 ± 0.00 | 0.082 / 0.064 | -0.018 ± 0.005 | 0.024 / 0.024 | 0.000 / 0.000 | 0.059 / 0.062 | +0.004 ± 0.003 | 1.30 / 1.34 | +0.03 ± 0.14 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| mix:dose0.3:0.25 | -0.07 ± 0.02 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.033 ± 0.007 | -0.004 ± 0.003 | +0.005 ± 0.003 |
| careful | -0.04 ± 0.01 | +0.00 ± 0.00 | +0.01 ± 0.00 | -0.016 ± 0.004 | -0.000 ± 0.002 | +0.004 ± 0.003 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| mix:dose0.3:0.25 | 0.000 / 0.000 | 0.00 / — | 0.038 / 0.000 | 0.00 / — | — / — | 0.929 / 0.000 |
| careful | 0.000 / 0.000 | 0.75 / — | 0.039 / 0.000 | 0.00 / — | — / — | 0.885 / 0.000 |

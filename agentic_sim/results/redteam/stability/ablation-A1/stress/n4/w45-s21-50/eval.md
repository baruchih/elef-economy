# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1 --arm 1 --pi-a0 0.10 --pi-a-max 0.10 --w-audit 3`, seeds 21-50, hide ``, model `None` (value off, horizon 8)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 36186.1 ± 732.2 | 501.2 ± 915.0 | 4581.2 | 0.979 | 0.000 | 0.000 | 0.024 | 0.024 | 0.372 | 0.015 | 3.83 | 13.13 | 0.30 |
| mix:dose0.3:0.25 | 35280.0 ± 535.3 | -404.8 ± 702.6 | 4847.9 | 0.959 | 0.000 | 0.000 | 0.061 | 0.062 | 0.381 | 0.006 | 3.97 | 30.73 | 0.43 |
| careful | 35684.8 ± 702.8 | nan ± nan | 4544.9 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.372 | 0.000 | 2.67 | 0.00 | 0.37 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:dose0.1:0.25 | 0.024 (8787) / 0.024 (77557) | 0.017 (5068) / 0.015 (37544) | 0.015 (4933) / 0.016 (3546) | — / — |
| mix:dose0.3:0.25 | 0.061 (13349) / 0.062 (76669) | 0.004 (6799) / 0.007 (39109) | 0.004 (6159) / 0.008 (3353) | — / — |
| careful | 0.000 (7894) / 0.000 (77795) | 0.000 (4783) / 0.000 (37232) | 0.000 (4896) / 0.000 (3746) | — / — |

The stressed world's fourth action by seat kind — the allowance claimed and the verdict F without inspecting (counted above among the blind verdicts; the ledger sees a careful review, so the measured reading below cannot see it):

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:dose0.1:0.25 | 0.024 (8787) / 0.024 (77557) | 0.017 (5068) / 0.015 (37544) | 0.015 (4933) / 0.016 (3546) | — / — |
| mix:dose0.3:0.25 | 0.061 (13349) / 0.062 (76669) | 0.004 (6799) / 0.007 (39109) | 0.004 (6159) / 0.008 (3353) | — / — |
| careful | 0.000 (7894) / 0.000 (77795) | 0.000 (4783) / 0.000 (37232) | 0.000 (4896) / 0.000 (3746) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 0.000 (8787) / 0.000 (77557) | 0.000 (5068) / 0.000 (37544) | 0.000 (4933) / 0.000 (3546) | — / — | 2.9 ± 0.4 | -2839 |
| mix:dose0.3:0.25 | 0.000 (13349) / 0.000 (76669) [rej. blind 0.000] | 0.000 (6799) / 0.000 (39109) | 0.000 (6159) / 0.000 (3353) | — / — | 2.7 ± 0.4 | -5907 |
| careful | 0.000 (7894) [rej. blind 0.000] / 0.000 (77795) [rej. blind 0.000] | 0.000 (4783) / 0.000 (37232) | 0.000 (4896) / 0.000 (3746) | — / — | 2.7 ± 0.3 | +12 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | — | 0.931 | — (0) | — (0) | 0.000 (18631) | 0.000 (4324) | 0.000 (114480) | 6.467 | 630.533 | 1.189 | 2.031 |
| mix:dose0.3:0.25 | — | 0.962 | — (0) | — (0) | 0.000 (9683) | 0.000 (4616) | 0.000 (131139) | 9.567 | 510.067 | 1.281 | 3.213 |
| careful | — | 0.916 | — (0) | — (0) | 0.000 (22987) | 0.000 (735) | 0.000 (112624) | 5.533 | 670.967 | 1.195 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 39.600 | 0.000 | 0.000 | 0.000 | 0.000 | 0.300 | 0.000 |
| mix:dose0.3:0.25 | 39.600 | 0.000 | 0.000 | 0.000 | 0.000 | 0.433 | 0.000 |
| careful | 39.533 | 0.000 | 0.000 | 0.000 | 0.000 | 0.367 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 22.267 / 39.600 | 3.833 ± 0.300 | +1.167 ± 0.346 | 16.267 | +5.833 ± 1.303 | 3.533 | 0.076 | 6.467 | +0.933 ± 0.581 | 1912.100 | 0.020 | +0.005 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 25443.250 ± 361.955 | +649.969 ± 406.191 | 36186.1 ± 732.2 | +501.2 ± 915.0 | 35.583 | -0.616 ± 0.345 | 15.329 ± 0.424 | +0.264 ± 0.550 | 17.710 | 0.001 | 2589.267 | 19.600 | 17.333 | +0.700 ± 0.407 | 589.767 | 264.467 |
| mix:dose0.3:0.25 | 21.333 / 39.600 | 3.967 ± 0.316 | +1.300 ± 0.418 | 36.500 | +26.067 ± 4.158 | 5.300 | 0.096 | 9.567 | +4.033 ± 0.624 | 1956.200 | 0.028 | +0.013 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 27645.099 ± 560.270 | +2851.819 ± 704.856 | 35280.0 ± 535.3 | -404.8 ± 702.6 | 34.441 | -1.758 ± 0.484 | 17.276 ± 0.365 | +2.211 ± 0.621 | 17.870 | 0.001 | 2563.300 | 19.600 | 18.267 | +1.633 ± 0.466 | 317.464 | 195.000 |
| careful | 22.900 / 39.533 | 2.667 ± 0.241 | — | 10.433 | — | 3.533 | 0.051 | 5.533 | — | 1891.533 | 0.015 | — | 0.000 / 0.000 (0.000 / 0.000) | 24793.280 ± 271.953 | — | 35684.8 ± 702.8 | — | 36.200 | — | 15.065 ± 0.377 | — | 17.471 | 0.001 | 2598.300 | 19.533 | 16.633 | — | 704.363 | 284.733 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **mix:dose0.1:0.25**: p0 1.000/0.000/0.000 (583); p1 1.000/0.000/0.000 (676); p2 1.000/0.000/0.000 (837); p3 1.000/0.000/0.000 (891); p4 1.000/0.000/0.000 (858); p5 1.000/0.000/0.000 (457); p6 1.000/0.000/0.000 (142); p7 1.000/0.000/0.000 (25); p8 1.000/0.000/0.000 (16); p9 1.000/0.000/0.000 (1)
- **mix:dose0.3:0.25**: p0 1.000/0.000/0.000 (542); p1 1.000/0.000/0.000 (575); p2 1.000/0.000/0.000 (650); p3 1.000/0.000/0.000 (665); p4 1.000/0.000/0.000 (649); p5 1.000/0.000/0.000 (398); p6 1.000/0.000/0.000 (266); p7 1.000/0.000/0.000 (228); p8 1.000/0.000/0.000 (159); p9 1.000/0.000/0.000 (149); p10 1.000/0.000/0.000 (143); p11 1.000/0.000/0.000 (108); p12 1.000/0.000/0.000 (82); p13 1.000/0.000/0.000 (30); p14 1.000/0.000/0.000 (7)
- **careful**: p0 1.000/0.000/0.000 (589); p1 1.000/0.000/0.000 (724); p2 1.000/0.000/0.000 (906); p3 1.000/0.000/0.000 (1006); p4 1.000/0.000/0.000 (1007); p5 1.000/0.000/0.000 (297); p6 1.000/0.000/0.000 (15)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 2585.2 / 292.9 | 0.30 / 0.21 | -0.09 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.12 / 0.13 | +0.00 ± 0.00 | 0.189 / 0.153 | -0.036 ± 0.004 | 0.073 / 0.078 | 0.001 / 0.000 | 0.059 / 0.056 | -0.002 ± 0.002 | 1.70 / 1.42 | -0.28 ± 0.09 |
| mix:dose0.3:0.25 | 2555.6 / 445.0 | 0.34 / 0.31 | -0.03 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.13 / 0.14 | +0.01 ± 0.00 | 0.235 / 0.220 | -0.015 ± 0.007 | 0.097 / 0.107 | 0.001 / 0.000 | 0.067 / 0.065 | -0.002 ± 0.003 | 1.79 / 1.70 | -0.09 ± 0.06 |
| careful | 2593.2 / 263.1 | 0.27 / 0.17 | -0.10 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.12 / 0.11 | -0.00 ± 0.00 | 0.172 / 0.141 | -0.032 ± 0.004 | 0.069 / 0.074 | 0.001 / 0.000 | 0.055 / 0.057 | +0.001 ± 0.002 | 1.71 / 1.34 | -0.37 ± 0.10 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | -0.09 ± 0.01 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.039 ± 0.004 | +0.002 ± 0.002 | -0.002 ± 0.003 |
| mix:dose0.3:0.25 | -0.05 ± 0.01 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.033 ± 0.005 | -0.000 ± 0.003 | -0.003 ± 0.003 |
| careful | -0.10 ± 0.02 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.035 ± 0.005 | +0.004 ± 0.002 | +0.001 ± 0.002 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 0.477 / 0.156 | 0.29 / 0.31 | 0.039 / 0.151 | 0.00 / 0.00 | 0.28 / 0.30 | 0.477 / 0.245 |
| mix:dose0.3:0.25 | 0.503 / 0.201 | 0.24 / 0.22 | 0.037 / 0.116 | 0.00 / 0.00 | 0.23 / 0.24 | 0.478 / 0.194 |
| careful | 0.472 / 0.142 | 0.29 / 0.33 | 0.041 / 0.165 | 0.00 / 0.00 | 0.28 / 0.31 | 0.467 / 0.252 |

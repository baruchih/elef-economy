# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --dispute-policy truthful --appeal-lie 0.1 --dispute-lie 0.1`, seeds 21-40, hide ``, model `None` (value off, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 34702.3 ± 746.8 | -1204.8 ± 803.5 | 4560.4 | 0.758 | 0.237 | 0.005 | 0.018 | 0.014 | 0.371 | 0.633 | 2.35 | 8.35 | 0.30 |
| careful | 35907.1 ± 773.7 | nan ± nan | 4458.9 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.376 | 0.000 | 1.50 | 0.00 | 0.25 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| direct | 0.018 (5544) [rej. blind 0.004] / 0.014 (51872) [rej. blind 0.002] | 0.954 (130) / 0.944 (21935) [rej. blind 0.001] | 0.031 (3138) [rej. blind 0.020] / 0.053 (8590) [rej. blind 0.032] | — / — |
| careful | 0.000 (5147) / 0.000 (50490) | 0.000 (122) / 0.000 (21520) | 0.000 (2814) / 0.000 (9085) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| direct | 0.018 (5544) [rej. blind 0.005] / 0.014 (51872) [rej. blind 0.002] | 0.954 (130) / 0.944 (21935) [rej. blind 0.001] | 0.031 (3138) [rej. blind 0.020] / 0.053 (8590) [rej. blind 0.032] | — / — | 3.2 ± 0.6 | +14 |
| careful | 0.000 (5147) [rej. blind 0.000] / 0.000 (50490) [rej. blind 0.000] | 0.000 (122) / 0.000 (21520) | 0.000 (2814) / 0.000 (9085) | — / — | 2.5 ± 0.5 | +5 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 0.779 | 0.925 | — (0) | — (0) | 0.483 (20246) | 0.332 (2092) | 0.163 (68871) | 6.100 | 707.650 | 1.207 | 1.369 |
| careful | — | 0.925 | — (0) | — (0) | 0.000 (13499) | 0.000 (722) | 0.000 (74957) | 5.350 | 707.050 | 1.229 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| direct | 39.650 | 0.000 | 0.000 | 0.000 | 0.000 | 0.300 | 0.000 |
| careful | 39.600 | 0.000 | 0.000 | 0.000 | 0.000 | 0.250 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 23.750 / 39.650 | 2.350 ± 0.310 | +0.850 ± 0.418 | 13.350 | +4.100 ± 1.374 | 3.400 | 0.070 | 6.100 | +0.750 ± 0.824 | 1680.650 | 0.007 | -0.006 ± 0.001 | 224.650 / 35.450 (32.350 / 31.600) | 25513.148 ± 288.612 | +974.465 ± 483.509 | 34702.3 ± 746.8 | -1204.8 ± 803.5 | 36.198 | +1.526 ± 0.653 | 15.734 ± 0.373 | +1.122 ± 0.335 | 18.456 | 0.003 | 2592.200 | 19.650 | 15.900 | +0.600 ± 0.489 | 710.649 | 191.600 |
| careful | 24.300 / 39.600 | 1.500 ± 0.235 | — | 9.250 | — | 2.800 | 0.054 | 5.350 | — | 1657.400 | 0.013 | — | 209.300 / 28.550 (25.600 / 25.050) | 24538.683 ± 434.133 | — | 35907.1 ± 773.7 | — | 34.672 | — | 14.612 ± 0.282 | — | 18.491 | 0.007 | 2513.700 | 19.600 | 15.300 | — | 545.685 | 275.150 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **direct**: p0 0.948/0.049/0.003 (596); p1 0.797/0.197/0.006 (738); p2 0.724/0.273/0.004 (867); p3 0.694/0.303/0.004 (976); p4 0.704/0.290/0.006 (930); p5 0.738/0.246/0.015 (358); p6 0.772/0.220/0.008 (97)
- **careful**: p0 1.000/0.000/0.000 (603); p1 1.000/0.000/0.000 (715); p2 1.000/0.000/0.000 (846); p3 1.000/0.000/0.000 (989); p4 1.000/0.000/0.000 (1014); p5 1.000/0.000/0.000 (262); p6 1.000/0.000/0.000 (31)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 2593.6 / 277.2 | 0.34 / 0.24 | -0.09 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.08 / 0.08 | +0.00 ± 0.00 | 0.201 / 0.166 | -0.035 ± 0.006 | 0.069 / 0.075 | 0.003 / 0.000 | 0.062 / 0.059 | -0.004 ± 0.002 | 1.74 / 1.61 | -0.13 ± 0.10 |
| careful | 2524.5 / 257.4 | 0.57 / 0.39 | -0.18 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.08 / 0.08 | -0.00 ± 0.00 | 0.259 / 0.218 | -0.041 ± 0.005 | 0.114 / 0.124 | 0.007 / 0.000 | 0.070 / 0.063 | -0.008 ± 0.003 | 2.29 / 1.83 | -0.47 ± 0.13 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| direct | -0.09 ± 0.02 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.033 ± 0.005 | +0.006 ± 0.004 | -0.004 ± 0.003 |
| careful | -0.17 ± 0.03 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.041 ± 0.005 | +0.009 ± 0.004 | -0.007 ± 0.003 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| direct | 0.417 / 0.021 | 0.34 / 0.31 | 0.145 / 0.415 | 0.00 / 0.00 | 0.32 / 0.34 | 0.372 / 0.404 |
| careful | 0.420 / 0.022 | 0.32 / 0.40 | 0.139 / 0.398 | 0.00 / 0.00 | 0.31 / 0.32 | 0.375 / 0.402 |

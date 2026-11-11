# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --dispute-policy truthful --dispute-rate 0.1`, seeds 21-40, hide ``, model `/Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/ablation-A1/detection/retrain-d0.1/wm/models/wm-online-20.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 34804.3 ± 787.9 | 413.3 ± 977.8 | 4223.1 | 0.810 | 0.188 | 0.002 | 0.002 | 0.002 | 0.317 | 0.597 | 11.40 | 10.10 | 0.50 |
| careful | 34391.0 ± 812.7 | nan ± nan | 4563.9 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.366 | 0.000 | 2.55 | 0.00 | 0.35 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| greedy | 0.002 (5309) / 0.002 (52390) | 0.603 (1233) [rej. blind 0.002] / 0.675 (21716) [rej. blind 0.000] | 0.164 (1144) [rej. blind 0.051] / 0.139 (2669) [rej. blind 0.027] | — / — |
| careful | 0.000 (5261) / 0.000 (52569) | 0.000 (1211) / 0.000 (26220) | 0.000 (1708) / 0.000 (4310) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| greedy | 0.002 (5309) / 0.002 (52390) | 0.603 (1233) [rej. blind 0.002] / 0.675 (21716) [rej. blind 0.000] | 0.164 (1144) [rej. blind 0.051] / 0.139 (2669) [rej. blind 0.027] | — / — | 1.9 ± 0.4 | +1 |
| careful | 0.000 (5261) / 0.000 (52569) [rej. blind 0.000] | 0.000 (1211) / 0.000 (26220) | 0.000 (1708) / 0.000 (4310) | — / — | 3.1 ± 0.5 | +13 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 0.756 | 0.942 | — (0) | — (0) | 0.494 (16010) | 0.441 (392) | 0.115 (68059) | 24.350 | 733.650 | 1.205 | 0.415 |
| careful | — | 0.908 | — (0) | — (0) | 0.000 (16977) | 0.000 (156) | 0.000 (74146) | 25.350 | 691.450 | 1.136 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| greedy | 39.700 | 0.000 | 0.000 | 0.000 | 0.000 | 0.500 | 0.000 |
| careful | 39.850 | 0.000 | 0.000 | 0.000 | 0.000 | 0.350 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 23.950 / 39.700 | 11.400 ± 0.694 | +8.850 ± 0.744 | 9.950 | +0.050 ± 0.966 | 3.200 | 0.058 | 4.650 | -0.850 ± 0.563 | 1926.050 | 0.015 | -0.008 ± 0.001 | 2.550 / 2.250 (2.550 / 2.250) | 25247.166 ± 363.128 | +868.504 ± 451.558 | 34804.3 ± 787.9 | +413.3 ± 977.8 | 36.570 | +0.019 ± 0.426 | 15.477 ± 0.348 | +0.067 ± 0.574 | 18.280 | 0.001 | 2623.100 | 19.700 | 15.750 | -1.700 ± 0.641 | 719.871 | 203.000 |
| careful | 22.400 / 39.850 | 2.550 ± 0.359 | — | 9.900 | — | 3.450 | 0.050 | 5.500 | — | 1905.400 | 0.023 | — | 3.600 / 3.500 (3.600 / 3.500) | 24378.662 ± 301.908 | — | 34391.0 ± 812.7 | — | 36.551 | — | 15.410 ± 0.507 | — | 17.739 | 0.001 | 2632.950 | 19.850 | 17.450 | — | 694.584 | 239.500 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **greedy**: p0 0.962/0.038/0.000 (581); p1 0.836/0.162/0.002 (694); p2 0.757/0.242/0.001 (795); p3 0.726/0.272/0.002 (897); p4 0.780/0.218/0.002 (923); p5 0.920/0.078/0.002 (312); p6 0.964/0.036/0.000 (22)
- **careful**: p0 1.000/0.000/0.000 (608); p1 1.000/0.000/0.000 (797); p2 1.000/0.000/0.000 (924); p3 1.000/0.000/0.000 (971); p4 1.000/0.000/0.000 (974); p5 1.000/0.000/0.000 (290)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 2619.5 / 265.4 | 0.27 / 0.20 | -0.08 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.06 / 0.06 | -0.00 ± 0.00 | 0.164 / 0.140 | -0.024 ± 0.005 | 0.055 / 0.063 | 0.001 / 0.000 | 0.059 / 0.058 | -0.001 ± 0.004 | 1.68 / 1.37 | -0.31 ± 0.13 |
| careful | 2628.4 / 263.1 | 0.22 / 0.12 | -0.10 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.10 / 0.10 | +0.00 ± 0.00 | 0.155 / 0.123 | -0.032 ± 0.006 | 0.060 / 0.063 | 0.001 / 0.000 | 0.052 / 0.050 | -0.003 ± 0.003 | 1.60 / 1.24 | -0.36 ± 0.12 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| greedy | -0.07 ± 0.02 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.026 ± 0.005 | +0.007 ± 0.003 | -0.001 ± 0.004 |
| careful | -0.09 ± 0.02 | +0.00 ± 0.00 | +0.00 ± 0.00 | -0.030 ± 0.006 | +0.005 ± 0.004 | -0.002 ± 0.003 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| greedy | 0.409 / 0.124 | 0.47 / 0.46 | 0.041 / 0.187 | 0.00 / 0.00 | 0.46 / 0.50 | 0.384 / 0.345 |
| careful | 0.493 / 0.140 | 0.29 / 0.29 | 0.040 / 0.183 | 0.00 / 0.00 | 0.28 / 0.26 | 0.275 / 0.235 |

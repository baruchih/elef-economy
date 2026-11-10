# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --dispute-policy truthful --dispute-rate 0.1`, seeds 21-40, hide ``, model `None` (value off, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 35341.1 ± 805.0 | 950.1 ± 977.8 | 4289.0 | 0.814 | 0.181 | 0.005 | 0.025 | 0.033 | 0.332 | 0.496 | 15.20 | 29.85 | 0.50 |
| careful | 34391.0 ± 812.7 | nan ± nan | 4563.9 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.366 | 0.000 | 2.55 | 0.00 | 0.35 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| direct | 0.025 (5409) [rej. blind 0.000] / 0.033 (51928) [rej. blind 0.000] | 0.478 (1359) [rej. blind 0.004] / 0.570 (22749) [rej. blind 0.001] | 0.125 (1277) [rej. blind 0.062] / 0.114 (3058) [rej. blind 0.090] | — / — |
| careful | 0.000 (5261) / 0.000 (52569) | 0.000 (1211) / 0.000 (26220) | 0.000 (1708) / 0.000 (4310) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| direct | 0.025 (5409) [rej. blind 0.000] / 0.033 (51928) [rej. blind 0.000] | 0.478 (1359) [rej. blind 0.004] / 0.570 (22749) [rej. blind 0.001] | 0.125 (1277) [rej. blind 0.062] / 0.114 (3058) [rej. blind 0.090] | — / — | 3.1 ± 0.5 | +14 |
| careful | 0.000 (5261) / 0.000 (52569) [rej. blind 0.000] | 0.000 (1211) / 0.000 (26220) | 0.000 (1708) / 0.000 (4310) | — / — | 3.1 ± 0.5 | +13 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 0.790 | 0.939 | — (0) | — (0) | 0.439 (14811) | 0.227 (1592) | 0.125 (69377) | 24.100 | 726.450 | 1.173 | 1.239 |
| careful | — | 0.908 | — (0) | — (0) | 0.000 (16977) | 0.000 (156) | 0.000 (74146) | 25.350 | 691.450 | 1.136 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| direct | 39.550 | 0.000 | 0.000 | 0.000 | 0.000 | 0.500 | 0.000 |
| careful | 39.850 | 0.000 | 0.000 | 0.000 | 0.000 | 0.350 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 22.700 / 39.550 | 15.200 ± 1.374 | +12.650 ± 1.550 | 13.300 | +3.400 ± 1.037 | 3.150 | 0.099 | 4.550 | -0.950 ± 0.467 | 1927.550 | 0.024 | +0.000 ± 0.001 | 3.600 / 3.400 (3.600 / 3.400) | 25916.233 ± 340.143 | +1537.571 ± 307.282 | 35341.1 ± 805.0 | +950.1 ± 977.8 | 35.863 | -0.688 ± 0.375 | 15.684 ± 0.438 | +0.274 ± 0.676 | 18.685 | 0.002 | 2597.950 | 19.550 | 16.850 | -0.600 ± 0.578 | 599.702 | 231.350 |
| careful | 22.400 / 39.850 | 2.550 ± 0.359 | — | 9.900 | — | 3.450 | 0.050 | 5.500 | — | 1905.400 | 0.023 | — | 3.600 / 3.500 (3.600 / 3.500) | 24378.662 ± 301.908 | — | 34391.0 ± 812.7 | — | 36.551 | — | 15.410 ± 0.507 | — | 17.739 | 0.001 | 2632.950 | 19.850 | 17.450 | — | 694.584 | 239.500 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **direct**: p0 0.930/0.069/0.001 (608); p1 0.817/0.174/0.009 (693); p2 0.755/0.239/0.006 (816); p3 0.763/0.234/0.004 (881); p4 0.807/0.190/0.004 (918); p5 0.886/0.109/0.004 (339); p6 0.894/0.092/0.013 (34)
- **careful**: p0 1.000/0.000/0.000 (608); p1 1.000/0.000/0.000 (797); p2 1.000/0.000/0.000 (924); p3 1.000/0.000/0.000 (971); p4 1.000/0.000/0.000 (974); p5 1.000/0.000/0.000 (290)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 2596.4 / 270.4 | 0.32 / 0.19 | -0.12 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.08 / 0.08 | +0.00 ± 0.00 | 0.183 / 0.142 | -0.042 ± 0.006 | 0.067 / 0.068 | 0.002 / 0.000 | 0.063 / 0.059 | -0.004 ± 0.003 | 1.76 / 1.45 | -0.30 ± 0.08 |
| careful | 2628.4 / 263.1 | 0.22 / 0.12 | -0.10 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.10 / 0.10 | +0.00 ± 0.00 | 0.155 / 0.123 | -0.032 ± 0.006 | 0.060 / 0.063 | 0.001 / 0.000 | 0.052 / 0.050 | -0.003 ± 0.003 | 1.60 / 1.24 | -0.36 ± 0.12 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| direct | -0.11 ± 0.02 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.037 ± 0.005 | +0.002 ± 0.003 | -0.003 ± 0.003 |
| careful | -0.09 ± 0.02 | +0.00 ± 0.00 | +0.00 ± 0.00 | -0.030 ± 0.006 | +0.005 ± 0.004 | -0.002 ± 0.003 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| direct | 0.432 / 0.136 | 0.41 / 0.39 | 0.040 / 0.175 | 0.00 / 0.00 | 0.43 / 0.46 | 0.367 / 0.306 |
| careful | 0.493 / 0.140 | 0.29 / 0.29 | 0.040 / 0.183 | 0.00 / 0.00 | 0.28 / 0.26 | 0.275 / 0.235 |

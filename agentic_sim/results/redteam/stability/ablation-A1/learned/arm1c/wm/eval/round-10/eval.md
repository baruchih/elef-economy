# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --arm 1c`, seeds 21-40, hide ``, model `/Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/ablation-A1/learned/arm1c/wm/models/wm-online-10.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 35204.2 ± 841.2 | -208.1 ± 777.6 | 4323.5 | 0.913 | 0.087 | 0.000 | 0.002 | 0.003 | 0.329 | 0.260 | 7.20 | 6.25 | 0.40 |
| careful | 35412.4 ± 510.2 | nan ± nan | 4475.4 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.352 | 0.000 | 2.55 | 0.00 | 0.15 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| greedy | 0.002 (5405) / 0.003 (52621) | 0.234 (1416) / 0.290 (23291) | 0.089 (1630) / 0.084 (2107) | — / — |
| careful | 0.000 (5474) / 0.000 (52508) | 0.000 (1403) / 0.000 (26048) | 0.000 (1632) / 0.000 (2444) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| greedy | 0.002 (5405) / 0.003 (52621) [rej. blind 0.000] | 0.234 (1416) / 0.290 (23291) | 0.089 (1630) / 0.084 (2107) | — / — | 1.8 ± 0.3 | +4 |
| careful | 0.000 (5474) [rej. blind 0.000] / 0.000 (52508) [rej. blind 0.000] | 0.000 (1403) / 0.000 (26048) | 0.000 (1632) / 0.000 (2444) | — / — | 2.2 ± 0.4 | +7 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 0.837 | 0.922 | — (0) | — (0) | 0.165 (15115) | 0.194 (757) | 0.069 (70598) | 24.650 | 689.350 | 1.179 | 0.254 |
| careful | — | 0.919 | — (0) | — (0) | 0.000 (13929) | 0.000 (1960) | 0.000 (73620) | 24.300 | 674.350 | 1.145 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| greedy | 39.650 | 0.000 | 0.000 | 0.000 | 0.000 | 0.400 | 0.000 |
| careful | 39.500 | 0.000 | 0.000 | 0.000 | 0.000 | 0.150 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 22.200 / 39.650 | 7.200 ± 0.738 | +4.650 ± 0.944 | 11.500 | +0.650 ± 1.238 | 3.350 | 0.046 | 5.000 | +0.200 ± 0.601 | 1917.900 | 0.012 | -0.003 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 24410.390 ± 420.812 | +122.569 ± 450.965 | 35204.2 ± 841.2 | -208.1 ± 777.6 | 36.828 | +0.003 ± 0.356 | 14.825 ± 0.280 | +0.192 ± 0.410 | 17.496 | 0.001 | 2635.550 | 19.650 | 17.450 | +0.950 ± 0.380 | 750.399 | 161.650 |
| careful | 23.000 / 39.500 | 2.550 ± 0.456 | — | 10.850 | — | 3.400 | 0.058 | 4.800 | — | 1914.300 | 0.015 | — | 0.000 / 0.000 (0.000 / 0.000) | 24287.821 ± 342.951 | — | 35412.4 ± 510.2 | — | 36.825 | — | 14.633 ± 0.314 | — | 17.175 | 0.001 | 2629.050 | 19.500 | 16.500 | — | 780.602 | 176.350 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **greedy**: p0 0.968/0.032/0.000 (589); p1 0.906/0.094/0.000 (688); p2 0.860/0.140/0.000 (842); p3 0.872/0.128/0.000 (891); p4 0.957/0.043/0.000 (933); p5 0.957/0.043/0.000 (342); p6 0.826/0.174/0.000 (37)
- **careful**: p0 1.000/0.000/0.000 (597); p1 1.000/0.000/0.000 (719); p2 1.000/0.000/0.000 (879); p3 1.000/0.000/0.000 (930); p4 1.000/0.000/0.000 (922); p5 1.000/0.000/0.000 (334); p6 1.000/0.000/0.000 (71); p7 1.000/0.000/0.000 (23)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 2631.1 / 270.2 | 0.19 / 0.14 | -0.06 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.08 / 0.08 | +0.00 ± 0.00 | 0.132 / 0.116 | -0.017 ± 0.005 | 0.041 / 0.047 | 0.001 / 0.000 | 0.058 / 0.052 | -0.007 ± 0.003 | 1.47 / 1.39 | -0.08 ± 0.06 |
| careful | 2625.4 / 273.7 | 0.20 / 0.11 | -0.09 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.09 / 0.09 | -0.00 ± 0.00 | 0.145 / 0.117 | -0.028 ± 0.005 | 0.050 / 0.056 | 0.001 / 0.000 | 0.054 / 0.059 | +0.005 ± 0.003 | 1.47 / 1.20 | -0.27 ± 0.10 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| greedy | -0.06 ± 0.02 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.018 ± 0.005 | +0.006 ± 0.003 | -0.007 ± 0.003 |
| careful | -0.08 ± 0.02 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.030 ± 0.005 | +0.005 ± 0.003 | +0.005 ± 0.003 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| greedy | 0.437 / 0.127 | 0.37 / 0.39 | 0.038 / 0.173 | 0.00 / 0.00 | 0.36 / 0.37 | 0.480 / 0.283 |
| careful | 0.490 / 0.156 | 0.29 / 0.29 | 0.038 / 0.160 | 0.00 / 0.00 | 0.25 / 0.29 | 0.439 / 0.242 |

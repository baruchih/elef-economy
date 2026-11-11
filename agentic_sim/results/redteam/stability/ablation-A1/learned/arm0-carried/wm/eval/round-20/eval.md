# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --dial-start 2.598085,14.111864,6.329700,1.732815`, seeds 21-40, hide ``, model `/Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/ablation-A1/learned/arm0-carried/wm/models/wm-online-20.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 34885.6 ± 667.0 | -871.2 ± 1102.0 | 6013.9 | 0.987 | 0.002 | 0.011 | 0.001 | 0.001 | 0.486 | 0.026 | 3.30 | 0.50 | 0.20 |
| careful | 35756.8 ± 761.0 | nan ± nan | 6021.9 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.488 | 0.000 | 2.35 | 0.00 | 0.25 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| greedy | 0.001 (9850) / 0.001 (51972) | 0.006 (9063) [rej. blind 0.003] / 0.006 (32860) | 0.086 (10931) [rej. blind 0.085] / 0.063 (5603) [rej. blind 0.063] | — / — |
| careful | 0.000 (9628) / 0.000 (52016) | 0.000 (9093) / 0.000 (33495) | 0.000 (10746) / 0.000 (5460) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| greedy | 0.001 (9850) / 0.001 (51972) | 0.006 (9063) [rej. blind 0.003] / 0.006 (32860) | 0.086 (10931) [rej. blind 0.085] / 0.063 (5603) [rej. blind 0.063] | — / — | 2.9 ± 0.5 | +1 |
| careful | 0.000 (9628) [rej. blind 0.000] / 0.000 (52016) [rej. blind 0.000] | 0.000 (9093) / 0.000 (33495) | 0.000 (10746) / 0.000 (5460) | — / — | 2.5 ± 0.4 | +10 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 0.974 | 0.952 | — (0) | — (0) | 0.002 (9069) | 0.000 (15895) | 0.003 (95315) | 24.900 | 327.100 | 1.131 | 0.020 |
| careful | — | 0.948 | — (0) | — (0) | 0.000 (10249) | 0.000 (15477) | 0.000 (94712) | 24.950 | 317.250 | 1.203 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| greedy | 39.900 | 0.000 | 0.000 | 0.000 | 0.000 | 0.200 | 0.000 |
| careful | 39.750 | 0.000 | 0.000 | 0.000 | 0.000 | 0.250 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 21.750 / 39.900 | 3.300 ± 0.385 | +0.950 ± 0.380 | 18.550 | +0.400 ± 1.880 | 7.150 | 0.050 | 5.000 | -0.200 ± 0.777 | 1897.050 | 0.029 | +0.005 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 31318.122 ± 623.239 | +514.017 ± 895.021 | 34885.6 ± 667.0 | -871.2 ± 1102.0 | 34.806 | -0.368 ± 0.625 | 19.640 ± 0.542 | +0.840 ± 0.979 | 18.363 | 0.001 | 2610.500 | 19.900 | 18.150 | +0.150 ± 0.372 | 295.381 | 125.950 |
| careful | 21.750 / 39.750 | 2.350 ± 0.357 | — | 18.150 | — | 5.550 | 0.043 | 5.200 | — | 1896.100 | 0.025 | — | 0.000 / 0.000 (0.000 / 0.000) | 30804.105 ± 547.429 | — | 35756.8 ± 761.0 | — | 35.173 | — | 18.800 ± 0.604 | — | 18.045 | 0.002 | 2609.650 | 19.750 | 18.000 | — | 399.449 | 108.000 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **greedy**: p0 0.983/0.016/0.001 (268); p1 0.970/0.000/0.030 (391); p2 0.954/0.005/0.041 (553); p3 0.990/0.001/0.009 (598); p4 0.995/0.000/0.005 (655); p5 0.986/0.003/0.010 (691); p6 0.990/0.001/0.009 (742); p7 0.992/0.003/0.005 (775); p8 0.995/0.000/0.005 (749); p9 0.997/0.000/0.003 (267); p10 0.999/0.000/0.001 (132); p11 0.995/0.000/0.005 (88); p12 1.000/0.000/0.000 (87); p13 1.000/0.000/0.000 (18)
- **careful**: p0 1.000/0.000/0.000 (277); p1 1.000/0.000/0.000 (435); p2 1.000/0.000/0.000 (544); p3 1.000/0.000/0.000 (612); p4 1.000/0.000/0.000 (668); p5 1.000/0.000/0.000 (704); p6 1.000/0.000/0.000 (758); p7 1.000/0.000/0.000 (811); p8 1.000/0.000/0.000 (707); p9 1.000/0.000/0.000 (249); p10 1.000/0.000/0.000 (122); p11 1.000/0.000/0.000 (74); p12 1.000/0.000/0.000 (47); p13 1.000/0.000/0.000 (12)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 2598.6 / 492.5 | 0.24 / 0.21 | -0.03 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.18 / 0.17 | -0.02 ± 0.00 | 0.188 / 0.153 | -0.035 ± 0.010 | 0.083 / 0.079 | 0.001 / 0.000 | 0.056 / 0.055 | -0.001 ± 0.002 | 1.56 / 1.44 | -0.11 ± 0.03 |
| careful | 2600.8 / 481.4 | 0.21 / 0.17 | -0.04 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.20 / 0.18 | -0.02 ± 0.00 | 0.147 / 0.126 | -0.021 ± 0.009 | 0.063 / 0.066 | 0.002 / 0.000 | 0.052 / 0.054 | +0.002 ± 0.002 | 1.63 / 1.41 | -0.21 ± 0.05 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| greedy | -0.03 ± 0.01 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.029 ± 0.006 | -0.001 ± 0.003 | +0.000 ± 0.002 |
| careful | -0.06 ± 0.01 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.025 ± 0.005 | +0.001 ± 0.003 | +0.003 ± 0.002 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| greedy | 0.625 / 0.197 | 0.14 / 0.18 | 0.040 / 0.253 | 0.00 / 0.00 | 0.13 / 0.15 | 0.122 / 0.167 |
| careful | 0.636 / 0.199 | 0.12 / 0.15 | 0.038 / 0.246 | 0.00 / 0.00 | 0.12 / 0.15 | 0.109 / 0.165 |

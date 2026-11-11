# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --dial-start 2.528710,12.314131,4.855057,1.503601`, seeds 21-40, hide ``, model `/Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/ablation-A1/learned/arm0-carried/wm/models/wm-online-15.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 35175.2 ± 663.6 | 1023.6 ± 795.6 | 6019.7 | 0.990 | 0.002 | 0.008 | 0.000 | 0.000 | 0.487 | 0.021 | 2.55 | 0.20 | 0.20 |
| careful | 34151.6 ± 841.4 | nan ± nan | 5897.4 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.481 | 0.000 | 3.15 | 0.00 | 0.30 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| greedy | 0.000 (9305) / 0.000 (52398) | 0.007 (8962) [rej. blind 0.001] / 0.005 (33454) | 0.069 (10655) [rej. blind 0.069] / 0.044 (5620) [rej. blind 0.043] | — / — |
| careful | 0.000 (9202) / 0.000 (52063) | 0.000 (8197) / 0.000 (32830) | 0.000 (10012) / 0.000 (5643) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| greedy | 0.000 (9305) / 0.000 (52398) [rej. blind 0.000] | 0.007 (8962) [rej. blind 0.001] / 0.005 (33454) | 0.069 (10655) [rej. blind 0.069] / 0.044 (5620) [rej. blind 0.043] | — / — | 3.1 ± 0.4 | +7 |
| careful | 0.000 (9202) / 0.000 (52063) | 0.000 (8197) [rej. blind 0.000] / 0.000 (32830) | 0.000 (10012) / 0.000 (5643) | — / — | 2.9 ± 0.4 | +6 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 0.922 | 0.944 | — (0) | — (0) | 0.005 (10606) | 0.002 (16742) | 0.002 (93046) | 24.500 | 333.050 | 1.120 | 0.008 |
| careful | — | 0.941 | — (0) | — (0) | 0.000 (11704) | 0.000 (15406) | 0.000 (90837) | 25.150 | 327.400 | 1.128 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| greedy | 39.700 | 0.000 | 0.000 | 0.000 | 0.000 | 0.200 | 0.000 |
| careful | 39.750 | 0.000 | 0.000 | 0.000 | 0.000 | 0.300 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 22.200 / 39.700 | 2.550 ± 0.400 | -0.600 ± 0.582 | 17.550 | +0.250 ± 1.586 | 5.200 | 0.060 | 4.800 | -0.600 ± 0.450 | 1903.400 | 0.027 | +0.004 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 29445.724 ± 675.639 | -806.673 ± 1017.672 | 35175.2 ± 663.6 | +1023.6 ± 795.6 | 36.181 | +0.760 ± 0.866 | 18.223 ± 0.604 | -1.361 ± 1.009 | 17.565 | 0.001 | 2630.500 | 19.700 | 17.500 | -0.500 ± 0.438 | 559.552 | 126.600 |
| careful | 21.750 / 39.750 | 3.150 ± 0.472 | — | 17.300 | — | 4.450 | 0.036 | 5.400 | — | 1879.200 | 0.024 | — | 0.000 / 0.000 (0.000 / 0.000) | 30252.398 ± 667.906 | — | 34151.6 ± 841.4 | — | 35.421 | — | 19.584 ± 0.759 | — | 18.015 | 0.001 | 2614.750 | 19.750 | 18.000 | — | 433.354 | 113.400 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **greedy**: p0 0.996/0.003/0.002 (279); p1 0.987/0.000/0.013 (439); p2 0.975/0.002/0.022 (580); p3 0.993/0.001/0.006 (643); p4 0.990/0.001/0.009 (706); p5 0.985/0.004/0.011 (725); p6 0.989/0.003/0.008 (781); p7 0.993/0.003/0.004 (844); p8 0.995/0.002/0.003 (661); p9 0.997/0.002/0.001 (207); p10 1.000/0.000/0.000 (96); p11 1.000/0.000/0.000 (37); p12 1.000/0.000/0.000 (22)
- **careful**: p0 1.000/0.000/0.000 (278); p1 1.000/0.000/0.000 (422); p2 1.000/0.000/0.000 (586); p3 1.000/0.000/0.000 (665); p4 1.000/0.000/0.000 (709); p5 1.000/0.000/0.000 (722); p6 1.000/0.000/0.000 (784); p7 1.000/0.000/0.000 (815); p8 1.000/0.000/0.000 (670); p9 1.000/0.000/0.000 (105); p10 1.000/0.000/0.000 (57); p11 1.000/0.000/0.000 (58); p12 1.000/0.000/0.000 (26)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 2619.9 / 465.2 | 0.17 / 0.14 | -0.02 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.19 / 0.17 | -0.02 ± 0.00 | 0.142 / 0.112 | -0.030 ± 0.010 | 0.053 / 0.048 | 0.001 / 0.000 | 0.054 / 0.050 | -0.005 ± 0.003 | 1.46 / 1.48 | +0.02 ± 0.08 |
| careful | 2603.2 / 460.1 | 0.19 / 0.15 | -0.04 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.19 / 0.17 | -0.02 ± 0.00 | 0.140 / 0.114 | -0.026 ± 0.009 | 0.064 / 0.061 | 0.001 / 0.000 | 0.058 / 0.058 | -0.000 ± 0.003 | 1.55 / 1.38 | -0.17 ± 0.06 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| greedy | -0.03 ± 0.01 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.027 ± 0.006 | -0.004 ± 0.002 | -0.003 ± 0.003 |
| careful | -0.05 ± 0.01 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.024 ± 0.005 | -0.001 ± 0.003 | +0.001 ± 0.003 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| greedy | 0.631 / 0.197 | 0.12 / 0.16 | 0.040 / 0.253 | 0.00 / 0.00 | 0.13 / 0.14 | 0.113 / 0.169 |
| careful | 0.623 / 0.191 | 0.12 / 0.16 | 0.040 / 0.255 | 0.00 / 0.00 | 0.11 / 0.14 | 0.116 / 0.178 |

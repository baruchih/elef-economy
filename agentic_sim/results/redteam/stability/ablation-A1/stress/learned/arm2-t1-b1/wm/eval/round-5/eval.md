# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --arm 2 --temptation 1 --bond-mult-later 1`, seeds 21-40, hide ``, model `/Users/baruchi-admin/projects/elef-economy-stress/agentic_sim/results/redteam/stability/ablation-A1/stress/learned/arm2-t1-b1/wm/models/wm-online-5.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 27905.6 ± 379.3 | -2252.3 ± 594.4 | 3020.6 | 0.746 | 0.000 | 0.000 | 0.139 | 0.251 | 0.083 | 0.554 | 9.40 | 112.10 | 0.15 |
| careful | 30157.8 ± 752.6 | nan ± nan | 3074.6 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.044 | 0.000 | 2.45 | 0.00 | 0.40 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| greedy | 0.139 (12182) / 0.251 (43235) | — / 1.000 (2187) | 0.261 (1375) / 0.156 (1433) | — / — |
| careful | 0.000 (5352) / 0.000 (53450) | — / — | 0.000 (763) / 0.000 (1927) | — / — |

The stressed world's fourth action by seat kind — the allowance claimed and the verdict F without inspecting (counted above among the blind verdicts; the ledger sees a careful review, so the measured reading below cannot see it):

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| greedy | 0.139 (12182) / 0.251 (43235) | — / 1.000 (2187) | 0.261 (1375) / 0.156 (1433) | — / — |
| careful | 0.000 (5352) / 0.000 (53450) | — / — | 0.000 (763) / 0.000 (1927) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| greedy | 0.002 (12182) [rej. blind 0.000] / 0.004 (43235) [rej. blind 0.000] | — / 0.000 (2187) | 0.000 (1375) / 0.000 (1433) | — / — | 4.0 ± 0.5 | -15128 |
| careful | 0.000 (5352) [rej. blind 0.000] / 0.000 (53450) [rej. blind 0.000] | — / — | 0.000 (763) / 0.000 (1927) | — / — | 3.6 ± 0.4 | +18 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | — | 1.000 | — (0) | — (0) | — (0) | — (0) | 0.000 (60412) | 51.150 | 217.400 | 1.689 | 2.192 |
| careful | — | 0.944 | — (0) | — (0) | 0.000 (7087) | — (0) | 0.000 (54405) | 24.400 | 670.250 | 1.139 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| greedy | 39.650 | 0.000 | 0.000 | 0.000 | 0.000 | 0.150 | 0.000 |
| careful | 39.600 | 0.000 | 0.000 | 0.000 | 0.000 | 0.400 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 14.450 / 39.650 | 9.400 ± 0.769 | +6.950 ± 0.872 | 84.900 | +75.150 ± 2.073 | 6.350 | 0.122 | 31.500 | +26.700 ± 0.856 | 1783.800 | 0.070 | +0.053 ± 0.002 | 0.000 / 0.000 (0.000 / 0.000) | 27207.140 ± 386.882 | +7748.508 ± 337.992 | 27905.6 ± 379.3 | -2252.3 ± 594.4 | 28.347 | -9.858 ± 0.342 | 22.717 ± 0.266 | +8.540 ± 0.465 | 21.095 | 0.078 | 2011.050 | 19.650 | 25.200 | +6.000 ± 0.363 | 68.876 | 222.000 |
| careful | 20.400 / 39.600 | 2.450 ± 0.352 | — | 9.750 | — | 2.500 | 0.043 | 4.800 | — | 1933.250 | 0.017 | — | 0.000 / 0.000 (0.000 / 0.000) | 19458.632 ± 328.789 | — | 30157.8 ± 752.6 | — | 38.206 | — | 14.177 ± 0.384 | — | 16.393 | 0.000 | 2677.450 | 19.600 | 19.200 | — | 952.026 | 234.400 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **greedy**: p0 1.000/0.000/0.000 (232); p1 1.000/0.000/0.000 (161); p2 1.000/0.000/0.000 (160); p3 1.000/0.000/0.000 (178); p4 1.000/0.000/0.000 (187); p5 1.000/0.000/0.000 (196); p6 1.000/0.000/0.000 (198); p7 1.000/0.000/0.000 (181); p8 1.000/0.000/0.000 (190); p9 1.000/0.000/0.000 (188); p10 1.000/0.000/0.000 (181); p11 1.000/0.000/0.000 (155); p12 1.000/0.000/0.000 (47); p13 1.000/0.000/0.000 (1)
- **careful**: p0 1.000/0.000/0.000 (559); p1 1.000/0.000/0.000 (560); p2 1.000/0.000/0.000 (568); p3 1.000/0.000/0.000 (572); p4 1.000/0.000/0.000 (595); p5 1.000/0.000/0.000 (220)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 2161.8 / 609.1 | 1.85 / 2.38 | +0.53 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.14 / 0.12 | -0.02 ± 0.00 | 0.559 / 0.656 | +0.097 ± 0.005 | 0.361 / 0.430 | 0.076 / 0.000 | 0.244 / 0.299 | +0.054 ± 0.006 | 3.93 / 4.09 | +0.16 ± 0.04 |
| careful | 2672.5 / 267.6 | 0.08 / 0.03 | -0.05 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.06 / 0.07 | +0.01 ± 0.00 | 0.082 / 0.071 | -0.011 ± 0.004 | 0.022 / 0.024 | 0.000 / 0.000 | 0.056 / 0.055 | -0.001 ± 0.002 | 1.30 / 1.20 | -0.10 ± 0.06 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| greedy | +0.06 ± 0.02 | +0.00 ± 0.00 | -0.03 ± 0.00 | -0.040 ± 0.004 | -0.033 ± 0.004 | -0.003 ± 0.006 |
| careful | -0.05 ± 0.01 | +0.00 ± 0.00 | +0.01 ± 0.00 | -0.012 ± 0.004 | +0.002 ± 0.002 | -0.001 ± 0.002 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| greedy | 0.048 / 0.000 | 0.36 / — | 0.026 / 0.084 | 0.00 / 0.00 | 0.15 / 0.15 | 0.975 / 0.056 |
| careful | 0.000 / 0.000 | — / — | 0.039 / 0.157 | 0.00 / 0.00 | 0.14 / 0.13 | 0.924 / 0.174 |

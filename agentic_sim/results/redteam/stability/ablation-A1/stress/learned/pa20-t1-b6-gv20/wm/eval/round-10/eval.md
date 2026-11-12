# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --pi-a0 0.20 --pi-a-max 0.20 --temptation 1 --gv 20 --bond-mult-later 1.5`, seeds 21-40, hide ``, model `/Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/ablation-A1/stress/learned/pa20-t1-b6-gv20/wm/models/wm-online-10.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 22999.1 ± 635.0 | -5987.7 ± 878.3 | 4168.9 | 0.897 | 0.001 | 0.018 | 0.044 | 0.087 | 0.404 | 0.137 | 8.95 | 40.60 | 0.20 |
| careful | 28986.8 ± 924.5 | nan ± nan | 4455.6 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.402 | 0.000 | 1.85 | 0.00 | 0.25 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| greedy | 0.044 (7540) [rej. blind 0.002] / 0.087 (42121) [rej. blind 0.006] | 0.099 (5401) [rej. blind 0.018] / 0.136 (20652) [rej. blind 0.001] | 0.199 (4517) [rej. blind 0.174] / 0.122 (3147) [rej. blind 0.117] | — / — |
| careful | 0.000 (4864) / 0.000 (48384) | 0.000 (5093) / 0.000 (22300) | 0.000 (4851) / 0.000 (3619) | — / — |

The stressed world's fourth action by seat kind — the allowance claimed and the verdict F without inspecting (counted above among the blind verdicts; the ledger sees a careful review, so the measured reading below cannot see it):

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| greedy | 0.041 (7540) / 0.081 (42121) | 0.078 (5401) / 0.132 (20652) | 0.025 (4517) / 0.004 (3147) | — / — |
| careful | 0.000 (4864) / 0.000 (48384) | 0.000 (5093) / 0.000 (22300) | 0.000 (4851) / 0.000 (3619) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| greedy | 0.003 (7540) [rej. blind 0.002] / 0.006 (42121) [rej. blind 0.006] | 0.021 (5401) [rej. blind 0.018] / 0.005 (20652) [rej. blind 0.001] | 0.174 (4517) [rej. blind 0.174] / 0.118 (3147) [rej. blind 0.117] | — / — | 14.7 ± 0.9 | -6925 |
| careful | 0.000 (4864) / 0.000 (48384) [rej. blind 0.000] | 0.000 (5093) / 0.002 (22300) [rej. blind 0.000] | 0.000 (4851) / 0.001 (3619) | — / — | 41.8 ± 1.7 | +59 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 0.962 | 0.975 | — (0) | — (0) | 0.000 (1349) | 0.002 (8884) | 0.001 (73145) | 30.050 | 152.100 | 2.863 | 1.351 |
| careful | — | 0.908 | — (0) | — (0) | 0.000 (16684) | 0.000 (521) | 0.000 (71906) | 24.550 | 639.200 | 1.474 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| greedy | 39.900 | 0.000 | 0.000 | 0.000 | 0.000 | 0.200 | 0.000 |
| careful | 39.800 | 0.000 | 0.000 | 0.000 | 0.000 | 0.250 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 30.600 / 39.900 | 8.950 ± 0.958 | +7.100 ± 1.026 | 25.550 | +16.500 ± 1.663 | 4.200 | 0.052 | 10.150 | +5.400 ± 0.881 | 1625.850 | 0.044 | +0.020 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 26912.367 ± 428.858 | +2641.246 ± 441.814 | 22999.1 ± 635.0 | -5987.7 ± 878.3 | 27.873 | -4.655 ± 0.503 | 26.343 ± 0.514 | +7.898 ± 0.764 | 24.723 | 0.085 | 1965.850 | 19.900 | 9.300 | -2.350 ± 0.799 | 78.362 | 1274.150 |
| careful | 28.150 / 39.800 | 1.850 ± 0.350 | — | 9.050 | — | 3.300 | 0.048 | 4.750 | — | 1773.400 | 0.024 | — | 0.000 / 0.000 (0.000 / 0.000) | 24271.120 ± 340.813 | — | 28986.8 ± 924.5 | — | 32.528 | — | 18.445 ± 0.674 | — | 20.975 | 0.024 | 2400.100 | 19.800 | 11.650 | — | 268.954 | 1561.150 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **greedy**: p0 0.966/0.001/0.033 (419); p1 0.965/0.005/0.030 (350); p2 0.974/0.001/0.026 (465); p3 0.975/0.002/0.023 (535); p4 0.983/0.001/0.016 (580); p5 0.985/0.000/0.014 (605); p6 0.990/0.000/0.010 (388); p7 0.986/0.000/0.014 (254); p8 0.990/0.000/0.010 (158); p9 0.992/0.000/0.008 (64)
- **careful**: p0 1.000/0.000/0.000 (579); p1 1.000/0.000/0.000 (709); p2 1.000/0.000/0.000 (918); p3 1.000/0.000/0.000 (1026); p4 1.000/0.000/0.000 (1067); p5 1.000/0.000/0.000 (150); p6 1.000/0.000/0.000 (6)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 2106.1 / 377.0 | 2.15 / 2.19 | +0.04 ± 0.05 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.18 / 0.14 | -0.04 ± 0.01 | 0.590 / 0.595 | +0.005 ± 0.011 | 0.351 / 0.369 | 0.082 / 0.000 | 0.236 / 0.239 | +0.003 ± 0.006 | 4.04 / 3.99 | -0.05 ± 0.04 |
| careful | 2419.2 / 243.2 | 0.80 / 0.55 | -0.26 ± 0.04 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.29 / 0.28 | -0.02 ± 0.01 | 0.302 / 0.249 | -0.054 ± 0.006 | 0.128 / 0.125 | 0.024 / 0.000 | 0.087 / 0.070 | -0.018 ± 0.004 | 2.87 / 2.23 | -0.64 ± 0.15 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| greedy | -0.23 ± 0.04 | +0.00 ± 0.00 | -0.03 ± 0.01 | -0.079 ± 0.006 | -0.038 ± 0.007 | -0.017 ± 0.006 |
| careful | -0.25 ± 0.04 | +0.00 ± 0.00 | -0.02 ± 0.01 | -0.052 ± 0.007 | -0.003 ± 0.004 | -0.017 ± 0.004 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| greedy | 0.474 / 0.173 | 0.23 / 0.18 | 0.035 / 0.106 | 0.00 / 0.00 | 0.21 / 0.21 | 0.340 / 0.262 |
| careful | 0.450 / 0.144 | 0.32 / 0.31 | 0.039 / 0.168 | 0.00 / 0.00 | 0.33 / 0.27 | 0.327 / 0.337 |

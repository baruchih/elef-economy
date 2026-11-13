# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1 --arm 4`, seeds 21-40, hide ``, model `/Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/ablation-A1/stress/learned/horizon/arm4-t1-b1-mc/wm-ret/models/wm-online-10.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 30449.2 ± 542.8 | -172.1 ± 794.3 | 3230.3 | 0.775 | 0.051 | 0.002 | 0.248 | 0.218 | 0.002 | 0.433 | 7.65 | 107.45 | 0.40 |
| careful | 30621.3 ± 651.3 | nan ± nan | 2932.8 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 3.05 | 0.00 | 0.20 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| greedy | 0.248 (14045) [rej. blind 0.002] / 0.218 (50434) [rej. blind 0.002] | — / 0.424 (118) | — / 0.556 (9) | — / — |
| careful | 0.000 (5405) / 0.000 (53247) | — / 0.000 (3) | — / — | — / — |

The stressed world's fourth action by seat kind — the allowance claimed and the verdict F without inspecting (counted above among the blind verdicts; the ledger sees a careful review, so the measured reading below cannot see it):

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| greedy | 0.198 (14045) / 0.164 (50434) | — / 0.364 (118) | — / 0.444 (9) | — / — |
| careful | 0.000 (5405) / 0.000 (53247) | — / 0.000 (3) | — / — | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| greedy | 0.050 (14045) [rej. blind 0.002] / 0.054 (50434) [rej. blind 0.002] | — / 0.059 (118) | — / 0.111 (9) | — / — | 4.9 ± 0.5 | -11080 |
| careful | 0.000 (5405) [rej. blind 0.000] / 0.000 (53247) [rej. blind 0.000] | — / 0.000 (3) | — / — | — / — | 5.0 ± 0.4 | +17 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 1.000 | 1.000 | — (0) | — (0) | 0.000 (14) | 0.000 (28) | 0.051 (64564) | 13.550 | 380.400 | 1.369 | 7.930 |
| careful | — | 0.949 | — (0) | — (0) | 0.000 (5868) | 0.000 (476) | 0.000 (52311) | 4.550 | 640.150 | 1.213 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| greedy | 39.600 | 0.000 | 0.000 | 0.000 | 0.000 | 0.400 | 0.000 |
| careful | 39.350 | 0.000 | 0.000 | 0.000 | 0.000 | 0.200 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 17.050 / 39.600 | 7.650 ± 0.708 | +4.600 ± 0.869 | 147.850 | +138.500 ± 4.519 | 6.400 | 0.535 | 13.550 | +9.000 ± 0.923 | 2042.700 | 0.062 | +0.045 ± 0.002 | 0.000 / 0.000 (0.000 / 0.000) | 24931.380 ± 399.803 | +5294.085 ± 516.006 | 30449.2 ± 542.8 | -172.1 ± 794.3 | 32.923 | -5.755 ± 0.413 | 19.379 ± 0.486 | +5.283 ± 0.708 | 18.074 | 0.005 | 2514.950 | 19.600 | 22.550 | +3.500 ± 0.622 | 62.829 | 200.350 |
| careful | 20.300 / 39.350 | 3.050 ± 0.373 | — | 9.350 | — | 3.250 | 0.040 | 4.550 | — | 1929.250 | 0.017 | — | 0.000 / 0.000 (0.000 / 0.000) | 19637.296 ± 470.320 | — | 30621.3 ± 651.3 | — | 38.679 | — | 14.096 ± 0.426 | — | 16.293 | 0.000 | 2667.600 | 19.350 | 19.050 | — | 1064.197 | 240.650 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **greedy**: p0 0.936/0.059/0.005 (521); p1 0.917/0.079/0.005 (342); p2 0.947/0.052/0.001 (243); p3 0.982/0.017/0.002 (198); p4 0.933/0.065/0.003 (176); p5 0.931/0.068/0.001 (161); p6 0.973/0.027/0.000 (154); p7 0.964/0.036/0.000 (140); p8 0.948/0.052/0.000 (140); p9 0.955/0.043/0.002 (131); p10 0.935/0.064/0.001 (135); p11 0.911/0.088/0.001 (115); p12 0.900/0.097/0.003 (111); p13 0.866/0.134/0.000 (70); p14 0.804/0.196/0.000 (34); p15 0.790/0.210/0.000 (5)
- **careful**: p0 1.000/0.000/0.000 (556); p1 1.000/0.000/0.000 (548); p2 1.000/0.000/0.000 (548); p3 1.000/0.000/0.000 (538); p4 1.000/0.000/0.000 (532); p5 1.000/0.000/0.000 (192); p6 1.000/0.000/0.000 (20); p7 1.000/0.000/0.000 (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 2521.7 / 702.2 | 0.49 / 0.57 | +0.07 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.11 / 0.10 | -0.01 ± 0.00 | 0.260 / 0.277 | +0.017 ± 0.006 | 0.118 / 0.142 | 0.005 / 0.000 | 0.101 / 0.118 | +0.016 ± 0.004 | 2.37 / 2.40 | +0.04 ± 0.04 |
| careful | 2662.3 / 270.2 | 0.10 / 0.06 | -0.04 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.06 / 0.07 | +0.01 ± 0.00 | 0.082 / 0.064 | -0.018 ± 0.005 | 0.024 / 0.024 | 0.000 / 0.000 | 0.059 / 0.062 | +0.004 ± 0.003 | 1.30 / 1.34 | +0.03 ± 0.14 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| greedy | -0.03 ± 0.01 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.040 ± 0.004 | -0.007 ± 0.004 | -0.005 ± 0.004 |
| careful | -0.04 ± 0.01 | +0.00 ± 0.00 | +0.01 ± 0.00 | -0.016 ± 0.004 | -0.000 ± 0.002 | +0.004 ± 0.003 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| greedy | 0.002 / 0.000 | 0.39 / — | 0.032 / 0.000 | 0.00 / — | — / — | 0.996 / 0.000 |
| careful | 0.000 / 0.000 | 0.75 / — | 0.039 / 0.000 | 0.00 / — | — / — | 0.885 / 0.000 |

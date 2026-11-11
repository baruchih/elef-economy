# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --arm 4 --temptation 1 --bond-mult-later 1`, seeds 21-40, hide ``, model `/Users/baruchi-admin/projects/elef-economy-stress/agentic_sim/results/redteam/stability/ablation-A1/stress/learned/arm4-t1-b1/wm/models/wm-online-5.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 26837.9 ± 645.0 | -3783.4 ± 870.4 | 2879.0 | 0.796 | 0.000 | 0.000 | 0.109 | 0.201 | 0.026 | 0.997 | 7.35 | 93.60 | 0.15 |
| careful | 30621.3 ± 651.3 | nan ± nan | 2932.8 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 3.05 | 0.00 | 0.20 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| greedy | 0.109 (11157) / 0.201 (44947) | — / 1.000 (1467) | — / 0.444 (9) [rej. blind 0.444] | — / — |
| careful | 0.000 (5405) / 0.000 (53247) | — / 0.000 (3) | — / — | — / — |

The stressed world's fourth action by seat kind — the allowance claimed and the verdict F without inspecting (counted above among the blind verdicts; the ledger sees a careful review, so the measured reading below cannot see it):

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| greedy | 0.109 (11157) / 0.201 (44947) | — / 1.000 (1467) | — / 0.000 (9) | — / — |
| careful | 0.000 (5405) / 0.000 (53247) | — / 0.000 (3) | — / — | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| greedy | 0.002 (11157) [rej. blind 0.000] / 0.004 (44947) [rej. blind 0.000] | — / 0.000 (1467) | — / 0.444 (9) [rej. blind 0.444] | — / — | 3.2 ± 0.5 | -11507 |
| careful | 0.000 (5405) [rej. blind 0.000] / 0.000 (53247) [rej. blind 0.000] | — / 0.000 (3) | — / — | — / — | 5.0 ± 0.4 | +17 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 1.000 | 1.000 | — (0) | — (0) | — (0) | 0.000 (442) | 0.000 (57138) | 50.800 | 234.550 | 1.563 | 1.843 |
| careful | — | 0.949 | — (0) | — (0) | 0.000 (5868) | 0.000 (476) | 0.000 (52311) | 23.900 | 640.150 | 1.213 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| greedy | 39.750 | 0.000 | 0.000 | 0.000 | 0.000 | 0.150 | 0.000 |
| careful | 39.350 | 0.000 | 0.000 | 0.000 | 0.000 | 0.200 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 15.250 / 39.750 | 7.350 ± 0.805 | +4.300 ± 0.726 | 63.400 | +54.050 ± 2.410 | 5.700 | 0.073 | 31.050 | +26.500 ± 0.643 | 1824.250 | 0.062 | +0.044 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 26600.798 ± 457.540 | +6963.503 ± 497.112 | 26837.9 ± 645.0 | -3783.4 ± 870.4 | 29.430 | -9.248 ± 0.460 | 23.064 ± 0.551 | +8.967 ± 0.632 | 20.891 | 0.049 | 2152.850 | 19.750 | 24.500 | +5.450 ± 0.587 | 71.150 | 207.600 |
| careful | 20.300 / 39.350 | 3.050 ± 0.373 | — | 9.350 | — | 3.250 | 0.040 | 4.550 | — | 1929.250 | 0.017 | — | 0.000 / 0.000 (0.000 / 0.000) | 19637.296 ± 470.320 | — | 30621.3 ± 651.3 | — | 38.679 | — | 14.096 ± 0.426 | — | 16.293 | 0.000 | 2667.600 | 19.350 | 19.050 | — | 1064.197 | 240.650 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **greedy**: p0 1.000/0.000/0.000 (242); p1 1.000/0.000/0.000 (163); p2 1.000/0.000/0.000 (175); p3 1.000/0.000/0.000 (184); p4 1.000/0.000/0.000 (197); p5 1.000/0.000/0.000 (207); p6 1.000/0.000/0.000 (214); p7 1.000/0.000/0.000 (222); p8 1.000/0.000/0.000 (229); p9 1.000/0.000/0.000 (230); p10 1.000/0.000/0.000 (139); p11 0.999/0.000/0.001 (58); p12 1.000/0.000/0.000 (28); p13 1.000/0.000/0.000 (6)
- **careful**: p0 1.000/0.000/0.000 (556); p1 1.000/0.000/0.000 (548); p2 1.000/0.000/0.000 (548); p3 1.000/0.000/0.000 (538); p4 1.000/0.000/0.000 (532); p5 1.000/0.000/0.000 (192); p6 1.000/0.000/0.000 (20); p7 1.000/0.000/0.000 (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 2247.3 / 557.9 | 1.59 / 1.96 | +0.37 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.12 / 0.10 | -0.02 ± 0.00 | 0.523 / 0.585 | +0.061 ± 0.005 | 0.308 / 0.352 | 0.048 / 0.000 | 0.219 / 0.264 | +0.045 ± 0.004 | 3.65 / 3.84 | +0.19 ± 0.04 |
| careful | 2662.3 / 270.2 | 0.10 / 0.06 | -0.04 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.06 / 0.07 | +0.01 ± 0.00 | 0.082 / 0.064 | -0.018 ± 0.005 | 0.024 / 0.024 | 0.000 / 0.000 | 0.059 / 0.062 | +0.004 ± 0.003 | 1.30 / 1.34 | +0.03 ± 0.14 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| greedy | +0.03 ± 0.02 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.045 ± 0.003 | -0.026 ± 0.003 | +0.004 ± 0.004 |
| careful | -0.04 ± 0.01 | +0.00 ± 0.00 | +0.01 ± 0.00 | -0.016 ± 0.004 | -0.000 ± 0.002 | +0.004 ± 0.003 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| greedy | 0.033 / 0.000 | 0.24 / — | 0.030 / 0.000 | 0.00 / — | — / — | 0.955 / 0.000 |
| careful | 0.000 / 0.000 | 0.75 / — | 0.039 / 0.000 | 0.00 / — | — / — | 0.885 / 0.000 |

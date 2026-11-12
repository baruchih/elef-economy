# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1 --arm 4`, seeds 21-40, hide ``, model `None` (value off, horizon 8)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 28693.7 ± 590.4 | -1927.5 ± 766.6 | 2978.7 | 0.746 | 0.015 | 0.002 | 0.156 | 0.266 | 0.017 | 0.997 | 8.45 | 121.35 | 0.05 |
| careful | 30621.3 ± 651.3 | nan ± nan | 2932.8 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 3.05 | 0.00 | 0.20 |
| claimer | 10316.6 ± 207.0 | -20304.6 ± 782.6 | 1007.3 | 0.000 | 0.000 | 0.000 | 1.000 | 1.000 | 0.000 | — | 8.80 | 172.40 | 1.00 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| direct | 0.156 (13265) [rej. blind 0.002] / 0.266 (45302) [rej. blind 0.001] | — / 0.998 (989) [rej. blind 0.004] | — / 0.944 (18) [rej. blind 0.833] | — / — |
| careful | 0.000 (5405) / 0.000 (53247) | — / 0.000 (3) | — / — | — / — |
| claimer | 1.000 (2754) / 1.000 (17392) | — / — | — / — | — / — |

The stressed world's fourth action by seat kind — the allowance claimed and the verdict F without inspecting (counted above among the blind verdicts; the ledger sees a careful review, so the measured reading below cannot see it):

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| direct | 0.137 (13265) / 0.251 (45302) | — / 0.987 (989) | — / 0.000 (18) | — / — |
| careful | 0.000 (5405) / 0.000 (53247) | — / 0.000 (3) | — / — | — / — |
| claimer | 1.000 (2754) / 1.000 (17392) | — / — | — / — | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| direct | 0.021 (13265) [rej. blind 0.003] / 0.018 (45302) [rej. blind 0.001] | — / 0.011 (989) [rej. blind 0.004] | — / 0.944 (18) [rej. blind 0.833] | — / — | 6.5 ± 0.8 | -13969 |
| careful | 0.000 (5405) [rej. blind 0.000] / 0.000 (53247) [rej. blind 0.000] | — / 0.000 (3) | — / — | — / — | 5.0 ± 0.4 | +17 |
| claimer | 0.009 (2754) / 0.012 (17392) | — / — | — / — | — / — | 0.0 ± 0.0 | -19911 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 1.000 | 1.000 | — (0) | — (0) | — (0) | — (0) | 0.015 (59574) | 27.050 | 262.950 | 1.410 | 4.486 |
| careful | — | 0.949 | — (0) | — (0) | 0.000 (5868) | 0.000 (476) | 0.000 (52311) | 4.550 | 640.150 | 1.213 | 0.000 |
| claimer | — | 1.000 | — (0) | — (0) | — (0) | — (0) | 0.000 (20146) | 55.800 | 227.700 | 1.503 | 3.090 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| direct | 39.450 | 0.000 | 0.000 | 0.000 | 0.000 | 0.050 | 0.000 |
| careful | 39.350 | 0.000 | 0.000 | 0.000 | 0.000 | 0.200 | 0.000 |
| claimer | 39.850 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 15.400 / 39.450 | 8.450 ± 0.609 | +5.400 ± 0.550 | 97.450 | +88.100 ± 2.833 | 7.500 | 0.158 | 27.050 | +22.500 ± 0.890 | 1863.800 | 0.073 | +0.056 ± 0.002 | 0.000 / 0.000 (0.000 / 0.000) | 26395.458 ± 384.147 | +6758.162 ± 406.895 | 28693.7 ± 590.4 | -1927.5 ± 766.6 | 29.664 | -9.015 ± 0.511 | 21.421 ± 0.445 | +7.325 ± 0.637 | 20.101 | 0.035 | 2199.300 | 19.450 | 24.050 | +5.000 ± 0.492 | 61.730 | 223.100 |
| careful | 20.300 / 39.350 | 3.050 ± 0.373 | — | 9.350 | — | 3.250 | 0.040 | 4.550 | — | 1929.250 | 0.017 | — | 0.000 / 0.000 (0.000 / 0.000) | 19637.296 ± 470.320 | — | 30621.3 ± 651.3 | — | 38.679 | — | 14.096 ± 0.426 | — | 16.293 | 0.000 | 2667.600 | 19.350 | 19.050 | — | 1064.197 | 240.650 |
| claimer | 3.400 / 39.850 | 8.800 ± 0.635 | +5.750 ± 0.718 | 105.000 | +95.650 ± 2.196 | 0.000 | 1.000 | 55.800 | +51.250 ± 2.051 | 869.650 | 0.193 | +0.175 ± 0.003 | 0.000 / 0.000 (0.000 / 0.000) | 7024.830 ± 123.369 | -12612.466 ± 485.721 | 10316.6 ± 207.0 | -20304.6 ± 782.6 | 29.162 | -9.516 ± 0.390 | 25.121 ± 0.622 | +11.025 ± 0.819 | 18.876 | 0.178 | 747.350 | 19.850 | 36.450 | +17.400 ± 0.622 | 6178.506 | 488.950 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **direct**: p0 0.976/0.023/0.001 (249); p1 0.972/0.027/0.001 (189); p2 0.935/0.058/0.007 (160); p3 0.937/0.058/0.004 (155); p4 0.962/0.035/0.003 (161); p5 0.980/0.018/0.002 (159); p6 0.989/0.010/0.001 (162); p7 0.993/0.005/0.002 (165); p8 0.997/0.002/0.001 (173); p9 0.998/0.001/0.001 (172); p10 0.996/0.001/0.002 (171); p11 0.993/0.005/0.002 (166); p12 0.989/0.009/0.002 (117); p13 0.993/0.003/0.003 (62); p14 1.000/0.000/0.000 (10)
- **careful**: p0 1.000/0.000/0.000 (556); p1 1.000/0.000/0.000 (548); p2 1.000/0.000/0.000 (548); p3 1.000/0.000/0.000 (538); p4 1.000/0.000/0.000 (532); p5 1.000/0.000/0.000 (192); p6 1.000/0.000/0.000 (20); p7 1.000/0.000/0.000 (0)
- **claimer**: p0 —/—/— (0); p1 —/—/— (0); p2 —/—/— (0); p3 —/—/— (0); p4 —/—/— (0); p5 —/—/— (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 2265.1 / 663.2 | 1.46 / 1.88 | +0.42 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.13 / 0.12 | -0.01 ± 0.00 | 0.532 / 0.612 | +0.080 ± 0.006 | 0.313 / 0.373 | 0.035 / 0.000 | 0.206 / 0.261 | +0.055 ± 0.004 | 3.47 / 3.66 | +0.19 ± 0.03 |
| careful | 2662.3 / 270.2 | 0.10 / 0.06 | -0.04 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.06 / 0.07 | +0.01 ± 0.00 | 0.082 / 0.064 | -0.018 ± 0.005 | 0.024 / 0.024 | 0.000 / 0.000 | 0.059 / 0.062 | +0.004 ± 0.003 | 1.30 / 1.34 | +0.03 ± 0.14 |
| claimer | 869.6 / 137.7 | 0.78 / 0.64 | -0.14 ± 0.05 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.13 / 0.13 | -0.00 ± 0.01 | 0.213 / 0.175 | -0.038 ± 0.008 | 0.076 / 0.063 | 0.140 / 0.000 | 0.070 / 0.067 | -0.004 ± 0.007 | 3.97 / 3.17 | -0.80 ± 0.31 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| direct | +0.06 ± 0.02 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.045 ± 0.003 | -0.023 ± 0.004 | +0.009 ± 0.004 |
| careful | -0.04 ± 0.01 | +0.00 ± 0.00 | +0.01 ± 0.00 | -0.016 ± 0.004 | -0.000 ± 0.002 | +0.004 ± 0.003 |
| claimer | -0.55 ± 0.06 | +0.00 ± 0.00 | -0.00 ± 0.01 | -0.147 ± 0.009 | -0.076 ± 0.007 | -0.023 ± 0.008 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| direct | 0.022 / 0.000 | 0.32 / — | 0.030 / 0.000 | 0.00 / — | — / — | 0.991 / 0.000 |
| careful | 0.000 / 0.000 | 0.75 / — | 0.039 / 0.000 | 0.00 / — | — / — | 0.885 / 0.000 |
| claimer | 0.000 / 0.000 | — / — | 0.000 / 0.000 | — / — | — / — | 1.269 / 0.000 |

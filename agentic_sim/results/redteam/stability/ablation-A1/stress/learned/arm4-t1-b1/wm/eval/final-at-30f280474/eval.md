# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --arm 4 --temptation 1 --bond-mult-later 1`, seeds 21-40, hide ``, model `/Users/baruchi-admin/projects/elef-economy-stress/agentic_sim/results/redteam/stability/ablation-A1/stress/learned/arm4-t1-b1/wm/models/wm-online-10.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 26705.9 ± 354.5 | -3915.3 ± 770.9 | 2831.7 | 0.780 | 0.000 | 0.000 | 0.115 | 0.218 | 0.030 | 1.000 | 7.55 | 93.75 | 0.15 |
| careful | 30621.3 ± 651.3 | nan ± nan | 2932.8 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 3.05 | 0.00 | 0.20 |
| stamper | 7483.2 ± 167.2 | -23138.0 ± 700.6 | 1040.5 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.000 | — | 9.10 | 182.90 | 1.00 |
| claimer | 10316.6 ± 207.0 | -20304.6 ± 782.6 | 1007.3 | 0.000 | 0.000 | 0.000 | 1.000 | 1.000 | 0.000 | — | 8.80 | 172.40 | 1.00 |
| hand | 30001.4 ± 569.0 | -619.9 ± 542.8 | 3137.3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.001 | 0.000 | 4.50 | 0.00 | 0.50 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| greedy | 0.115 (11319) / 0.218 (43640) | — / 1.000 (1667) | — / 1.000 (8) [rej. blind 1.000] | — / — |
| careful | 0.000 (5405) / 0.000 (53247) | — / 0.000 (3) | — / — | — / — |
| stamper | 1.000 (2914) / 1.000 (17895) | — / — | — / — | — / — |
| claimer | 1.000 (2754) / 1.000 (17392) | — / — | — / — | — / — |
| hand | 0.000 (12429) / 0.000 (50248) | — / 0.000 (60) | — / 0.000 (9) | — / — |

The stressed world's fourth action by seat kind — the allowance claimed and the verdict F without inspecting (counted above among the blind verdicts; the ledger sees a careful review, so the measured reading below cannot see it):

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| greedy | 0.115 (11319) / 0.218 (43640) | — / 1.000 (1667) | — / 0.000 (8) | — / — |
| careful | 0.000 (5405) / 0.000 (53247) | — / 0.000 (3) | — / — | — / — |
| stamper | 0.000 (2914) / 0.000 (17895) | — / — | — / — | — / — |
| claimer | 1.000 (2754) / 1.000 (17392) | — / — | — / — | — / — |
| hand | 0.000 (12429) / 0.000 (50248) | — / 0.000 (60) | — / 0.000 (9) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| greedy | 0.002 (11319) / 0.005 (43640) [rej. blind 0.000] | — / 0.000 (1667) | — / 1.000 (8) [rej. blind 1.000] | — / — | 3.1 ± 0.4 | -12243 |
| careful | 0.000 (5405) [rej. blind 0.000] / 0.000 (53247) [rej. blind 0.000] | — / 0.000 (3) | — / — | — / — | 5.0 ± 0.4 | +17 |
| stamper | 1.000 (2914) / 1.000 (17895) | — / — | — / — | — / — | 0.0 ± 0.0 | +0 |
| claimer | 0.009 (2754) / 0.012 (17392) | — / — | — / — | — / — | 0.0 ± 0.0 | -19911 |
| hand | 0.068 (12429) [rej. blind 0.000] / 0.103 (50248) [rej. blind 0.000] | — / 0.000 (60) | — / 0.000 (9) | — / — | 3.4 ± 0.5 | +6027 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 1.000 | 1.000 | — (0) | — (0) | — (0) | 0.000 (107) | 0.000 (56527) | 31.100 | 214.200 | 1.717 | 3.014 |
| careful | — | 0.949 | — (0) | — (0) | 0.000 (5868) | 0.000 (476) | 0.000 (52311) | 4.550 | 640.150 | 1.213 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (20809) | 58.350 | 223.400 | 1.595 | 3.135 |
| claimer | — | 1.000 | — (0) | — (0) | — (0) | — (0) | 0.000 (20146) | 55.800 | 227.700 | 1.503 | 3.090 |
| hand | — | 0.999 | — (0) | — (0) | — (0) | 0.000 (824) | 0.000 (61922) | 12.650 | 352.650 | 1.148 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| greedy | 39.750 | 0.000 | 0.000 | 0.000 | 0.000 | 0.150 | 0.000 |
| careful | 39.350 | 0.000 | 0.000 | 0.000 | 0.000 | 0.200 | 0.000 |
| stamper | 39.900 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| claimer | 39.850 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| hand | 39.750 | 0.000 | 0.000 | 0.000 | 0.000 | 0.500 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 14.650 / 39.750 | 7.550 ± 0.647 | +4.500 ± 0.727 | 67.050 | +57.700 ± 2.293 | 6.300 | 0.085 | 31.100 | +26.550 ± 0.958 | 1773.650 | 0.063 | +0.045 ± 0.002 | 0.000 / 0.000 (0.000 / 0.000) | 27180.215 ± 320.147 | +7542.919 ± 506.107 | 26705.9 ± 354.5 | -3915.3 ± 770.9 | 28.584 | -10.095 ± 0.372 | 23.510 ± 0.269 | +9.414 ± 0.554 | 21.423 | 0.057 | 2071.450 | 19.750 | 25.100 | +6.050 ± 0.366 | 71.254 | 183.400 |
| careful | 20.300 / 39.350 | 3.050 ± 0.373 | — | 9.350 | — | 3.250 | 0.040 | 4.550 | — | 1929.250 | 0.017 | — | 0.000 / 0.000 (0.000 / 0.000) | 19637.296 ± 470.320 | — | 30621.3 ± 651.3 | — | 38.679 | — | 14.096 ± 0.426 | — | 16.293 | 0.000 | 2667.600 | 19.350 | 19.050 | — | 1064.197 | 240.650 |
| stamper | 1.900 / 39.900 | 9.100 ± 0.962 | +6.050 ± 1.109 | 108.600 | +99.250 ± 2.255 | 0.000 | 1.000 | 58.350 | +53.800 ± 1.741 | 894.950 | 0.199 | +0.181 ± 0.004 | 0.000 / 0.000 (0.000 / 0.000) | 8347.449 ± 141.503 | -11289.846 ± 474.883 | 7483.2 ± 167.2 | -23138.0 ± 700.6 | 28.872 | -9.807 ± 0.390 | 29.581 ± 0.749 | +15.485 ± 0.865 | 21.154 | 0.176 | 769.900 | 19.900 | 38.000 | +18.950 ± 0.531 | 6051.272 | 427.050 |
| claimer | 3.400 / 39.850 | 8.800 ± 0.635 | +5.750 ± 0.718 | 105.000 | +95.650 ± 2.196 | 0.000 | 1.000 | 55.800 | +51.250 ± 2.051 | 869.650 | 0.193 | +0.175 ± 0.003 | 0.000 / 0.000 (0.000 / 0.000) | 7024.830 ± 123.369 | -12612.466 ± 485.721 | 10316.6 ± 207.0 | -20304.6 ± 782.6 | 29.162 | -9.516 ± 0.390 | 25.121 ± 0.622 | +11.025 ± 0.819 | 18.876 | 0.178 | 747.350 | 19.850 | 36.450 | +17.400 ± 0.622 | 6178.506 | 488.950 |
| hand | 17.850 / 39.750 | 4.500 ± 0.505 | +1.450 ± 0.609 | 55.050 | +45.700 ± 1.785 | 7.450 | 0.059 | 12.650 | +8.100 ± 0.830 | 1975.550 | 0.041 | +0.023 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 26205.847 ± 374.724 | +6568.551 ± 477.404 | 30001.4 ± 569.0 | -619.9 ± 542.8 | 32.763 | -5.916 ± 0.387 | 19.423 ± 0.318 | +5.327 ± 0.522 | 18.728 | 0.003 | 2510.450 | 19.750 | 21.900 | +2.850 ± 0.365 | 50.407 | 467.250 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **greedy**: p0 1.000/0.000/0.000 (229); p1 0.999/0.000/0.001 (162); p2 1.000/0.000/0.000 (170); p3 0.999/0.000/0.001 (176); p4 1.000/0.000/0.000 (185); p5 1.000/0.000/0.000 (192); p6 1.000/0.000/0.000 (199); p7 1.000/0.000/0.000 (204); p8 1.000/0.000/0.000 (210); p9 1.000/0.000/0.000 (216); p10 1.000/0.000/0.000 (165); p11 1.000/0.000/0.000 (75); p12 1.000/0.000/0.000 (21); p13 1.000/0.000/0.000 (3)
- **careful**: p0 1.000/0.000/0.000 (556); p1 1.000/0.000/0.000 (548); p2 1.000/0.000/0.000 (548); p3 1.000/0.000/0.000 (538); p4 1.000/0.000/0.000 (532); p5 1.000/0.000/0.000 (192); p6 1.000/0.000/0.000 (20); p7 1.000/0.000/0.000 (0)
- **stamper**: p0 0.000/1.000/0.000 (556); p1 0.000/1.000/0.000 (309); p2 0.000/1.000/0.000 (155); p3 0.000/1.000/0.000 (17); p4 0.000/1.000/0.000 (3)
- **claimer**: p0 —/—/— (0); p1 —/—/— (0); p2 —/—/— (0); p3 —/—/— (0); p4 —/—/— (0); p5 —/—/— (0)
- **hand**: p0 —/—/— (0); p1 —/—/— (0); p2 —/—/— (0); p3 —/—/— (0); p4 —/—/— (0); p5 —/—/— (0); p6 —/—/— (0); p7 —/—/— (0); p8 —/—/— (0); p9 —/—/— (0); p10 —/—/— (0); p11 —/—/— (0); p12 —/—/— (0); p13 —/—/— (0); p14 —/—/— (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 2182.0 / 566.0 | 1.89 / 2.32 | +0.43 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.12 / 0.10 | -0.02 ± 0.00 | 0.550 / 0.625 | +0.075 ± 0.006 | 0.340 / 0.395 | 0.056 / 0.000 | 0.242 / 0.289 | +0.047 ± 0.005 | 4.03 / 4.26 | +0.22 ± 0.05 |
| careful | 2662.3 / 270.2 | 0.10 / 0.06 | -0.04 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.06 / 0.07 | +0.01 ± 0.00 | 0.082 / 0.064 | -0.018 ± 0.005 | 0.024 / 0.024 | 0.000 / 0.000 | 0.059 / 0.062 | +0.004 ± 0.003 | 1.30 / 1.34 | +0.03 ± 0.14 |
| stamper | 894.8 / 145.7 | 0.72 / 0.56 | -0.15 ± 0.04 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.13 / 0.13 | -0.00 ± 0.01 | 0.164 / 0.142 | -0.022 ± 0.008 | 0.079 / 0.073 | 0.140 / 0.000 | 0.074 / 0.054 | -0.020 ± 0.004 | 3.78 / 2.27 | -1.51 ± 0.22 |
| claimer | 869.6 / 137.7 | 0.78 / 0.64 | -0.14 ± 0.05 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.13 / 0.13 | -0.00 ± 0.01 | 0.213 / 0.175 | -0.038 ± 0.008 | 0.076 / 0.063 | 0.140 / 0.000 | 0.070 / 0.067 | -0.004 ± 0.007 | 3.97 / 3.17 | -0.80 ± 0.31 |
| hand | 2512.4 / 621.5 | 0.58 / 0.57 | -0.02 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.11 / 0.09 | -0.02 ± 0.00 | 0.353 / 0.336 | -0.017 ± 0.007 | 0.148 / 0.157 | 0.003 / 0.000 | 0.108 / 0.116 | +0.008 ± 0.003 | 2.36 / 2.19 | -0.16 ± 0.08 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| greedy | -0.00 ± 0.02 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.049 ± 0.003 | -0.033 ± 0.003 | -0.002 ± 0.005 |
| careful | -0.04 ± 0.01 | +0.00 ± 0.00 | +0.01 ± 0.00 | -0.016 ± 0.004 | -0.000 ± 0.002 | +0.004 ± 0.003 |
| stamper | -0.60 ± 0.05 | +0.00 ± 0.00 | -0.00 ± 0.01 | -0.134 ± 0.014 | -0.078 ± 0.008 | -0.041 ± 0.005 |
| claimer | -0.55 ± 0.06 | +0.00 ± 0.00 | -0.00 ± 0.01 | -0.147 ± 0.009 | -0.076 ± 0.007 | -0.023 ± 0.008 |
| hand | -0.05 ± 0.02 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.046 ± 0.004 | -0.005 ± 0.003 | -0.001 ± 0.003 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| greedy | 0.037 / 0.000 | 0.28 / — | 0.029 / 0.000 | 0.00 / — | — / — | 0.956 / 0.000 |
| careful | 0.000 / 0.000 | 0.75 / — | 0.039 / 0.000 | 0.00 / — | — / — | 0.885 / 0.000 |
| stamper | 0.000 / 0.000 | — / — | 0.000 / 0.000 | — / — | — / — | 1.282 / 0.000 |
| claimer | 0.000 / 0.000 | — / — | 0.000 / 0.000 | — / — | — / — | 1.269 / 0.000 |
| hand | 0.001 / 0.000 | 0.55 / — | 0.035 / 0.000 | 0.00 / — | — / — | 0.962 / 0.000 |

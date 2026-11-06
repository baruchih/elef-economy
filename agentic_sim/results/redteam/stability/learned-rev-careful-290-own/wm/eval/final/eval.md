# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule`, seeds 21-40, hide ``, model `results/redteam/stability/learned-rev-careful-290-own/wm/models/wm-online-10.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 35326.8 ± 785.7 | -283.1 ± 722.1 | 3913.8 | 0.845 | 0.155 | 0.000 | 0.012 | 0.013 | 0.263 | 0.555 | 18.50 | 15.60 | 0.45 |
| careful | 35610.0 ± 690.2 | nan ± nan | 4142.1 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.300 | 0.000 | 6.10 | 0.00 | 0.30 |
| stamper | 7201.6 ± 143.3 | -28408.4 ± 730.6 | 1082.3 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.020 | 1.000 | 15.40 | 180.80 | 1.00 |
| hand | 32157.7 ± 597.4 | -3452.3 ± 702.9 | 4519.8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.328 | 0.000 | 10.45 | 0.00 | 0.55 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| greedy | 0.012 (5451) / 0.013 (52269) | 0.634 (870) / 0.658 (16324) | 0.085 (925) / 0.011 (2437) | — / — |
| careful | 0.000 (5358) / 0.000 (52610) | 0.000 (945) / 0.000 (18926) | 0.000 (1365) / 0.000 (3638) | — / — |
| stamper | 1.000 (3123) / 1.000 (18084) | — / 1.000 (440) | — / — | — / — |
| hand | 0.000 (12392) / 0.000 (48324) | 0.000 (2646) / 0.000 (20477) | 0.000 (2555) / 0.000 (4001) | — / — |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 0.386 | 0.762 | 0.337 (23094) | 0.195 (4791) | 0.363 (4367) | 0.185 (947) | 0.037 (45077) | 23.950 | 738.600 | 1.181 | 0.651 |
| careful | — | 0.683 | 0.000 (25992) | 0.000 (5627) | 0.000 (4615) | 0.000 (1110) | 0.000 (45498) | 25.300 | 722.750 | 1.157 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (21647) | 79.450 | 181.000 | 2.161 | 2.276 |
| hand | — | 0.817 | 0.000 (206) | 0.000 (9733) | 0.000 (17840) | 0.000 (17400) | 0.000 (45216) | 36.950 | 363.350 | 1.351 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| greedy | 39.650 | 0.000 | 0.000 | 0.000 | 0.000 | 0.450 | 0.000 |
| careful | 39.650 | 0.000 | 0.000 | 0.000 | 0.000 | 0.300 | 0.000 |
| stamper | 40.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| hand | 39.850 | 0.000 | 0.000 | 0.000 | 0.000 | 0.550 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 23.350 / 39.650 | 18.500 ± 1.144 | +12.400 ± 1.299 | 12.300 | +1.850 ± 1.079 | 3.350 | 0.065 | 4.300 | -1.350 ± 0.704 | 1641.000 | 0.016 | -0.009 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 24544.599 ± 346.263 | +825.786 ± 392.538 | 35326.8 ± 785.7 | -283.1 ± 722.1 | 37.277 | -0.089 ± 0.403 | 14.769 ± 0.373 | +0.594 ± 0.451 | 18.004 | 0.001 | 2617.350 | 19.650 | 16.300 | -0.200 ± 0.506 | 908.826 | 196.250 |
| careful | 23.150 / 39.650 | 6.100 ± 0.355 | — | 10.450 | — | 3.400 | 0.055 | 5.650 | — | 1630.350 | 0.024 | — | 0.000 / 0.000 (0.000 / 0.000) | 23718.813 ± 303.512 | — | 35610.0 ± 690.2 | — | 37.367 | — | 14.175 ± 0.294 | — | 17.614 | 0.001 | 2633.550 | 19.650 | 16.500 | — | 903.473 | 232.300 |
| stamper | 2.900 / 40.000 | 15.400 ± 0.890 | +9.300 ± 0.924 | 118.450 | +108.000 ± 1.989 | 0.000 | 1.000 | 59.450 | +53.800 ± 1.773 | 904.200 | 0.187 | +0.162 ± 0.003 | 0.000 / 0.000 (0.000 / 0.000) | 9117.372 ± 129.526 | -14601.441 ± 268.742 | 7201.6 ± 143.3 | -28408.4 ± 730.6 | 26.578 | -10.788 ± 0.365 | 31.736 ± 0.665 | +17.561 ± 0.828 | 22.601 | 0.236 | 720.600 | 20.000 | 37.100 | +20.600 ± 0.525 | 5594.089 | 108.100 |
| hand | 20.050 / 39.850 | 10.450 ± 0.822 | +4.350 ± 0.907 | 67.200 | +56.750 ± 1.142 | 7.700 | 0.043 | 17.100 | +11.450 ± 0.806 | 1654.800 | 0.060 | +0.036 ± 0.002 | 0.000 / 0.000 (0.000 / 0.000) | 30204.240 ± 351.394 | +6485.426 ± 328.387 | 32157.7 ± 597.4 | -3452.3 ± 702.9 | 31.742 | -5.625 ± 0.365 | 20.038 ± 0.392 | +5.863 ± 0.402 | 20.099 | 0.030 | 2356.200 | 19.850 | 19.800 | +3.300 ± 0.454 | 76.458 | 156.650 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **greedy**: p0 0.956/0.044/0.000 (595); p1 0.878/0.122/0.000 (662); p2 0.790/0.210/0.000 (786); p3 0.745/0.255/0.000 (785); p4 0.847/0.153/0.000 (762); p5 0.942/0.058/0.000 (311); p6 0.914/0.086/0.000 (12)
- **careful**: p0 1.000/0.000/0.000 (590); p1 1.000/0.000/0.000 (737); p2 1.000/0.000/0.000 (863); p3 1.000/0.000/0.000 (903); p4 1.000/0.000/0.000 (771); p5 1.000/0.000/0.000 (264); p6 1.000/0.000/0.000 (14)
- **stamper**: p0 0.000/1.000/0.000 (562); p1 0.000/1.000/0.000 (304); p2 0.000/1.000/0.000 (182); p3 0.000/1.000/0.000 (30); p4 0.000/1.000/0.000 (3); p5 0.000/1.000/0.000 (0)
- **hand**: p0 —/—/— (0); p1 —/—/— (0); p2 —/—/— (0); p3 —/—/— (0); p4 —/—/— (0); p5 —/—/— (0); p6 —/—/— (0); p7 —/—/— (0); p8 —/—/— (0); p9 —/—/— (0); p10 —/—/— (0); p11 —/—/— (0); p12 —/—/— (0); p13 —/—/— (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 2613.4 / 272.6 | 0.24 / 0.14 | -0.10 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.05 / 0.05 | +0.00 ± 0.00 | 0.170 / 0.135 | -0.035 ± 0.006 | 0.060 / 0.064 | 0.001 / 0.000 | 0.064 / 0.064 | +0.000 ± 0.005 | 1.57 / 1.39 | -0.18 ± 0.10 |
| careful | 2630.5 / 267.9 | 0.23 / 0.14 | -0.09 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.06 / 0.07 | +0.00 ± 0.00 | 0.156 / 0.127 | -0.029 ± 0.005 | 0.055 / 0.063 | 0.001 / 0.000 | 0.062 / 0.062 | +0.000 ± 0.003 | 1.51 / 1.17 | -0.34 ± 0.09 |
| stamper | 904.2 / 156.2 | 1.06 / 0.79 | -0.26 ± 0.04 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.04 / 0.03 | -0.01 ± 0.00 | 0.236 / 0.238 | +0.002 ± 0.008 | 0.142 / 0.157 | 0.203 / 0.000 | 0.094 / 0.077 | -0.017 ± 0.006 | 3.35 / 2.14 | -1.21 ± 0.18 |
| hand | 2416.2 / 619.6 | 0.83 / 0.85 | +0.01 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.14 / 0.13 | -0.00 ± 0.00 | 0.398 / 0.404 | +0.007 ± 0.006 | 0.178 / 0.202 | 0.030 / 0.000 | 0.100 / 0.094 | -0.006 ± 0.004 | 2.65 / 2.47 | -0.18 ± 0.08 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| greedy | -0.10 ± 0.02 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.034 ± 0.006 | +0.004 ± 0.004 | +0.001 ± 0.005 |
| careful | -0.08 ± 0.02 | +0.00 ± 0.00 | +0.00 ± 0.00 | -0.025 ± 0.005 | +0.009 ± 0.003 | +0.000 ± 0.003 |
| stamper | -0.77 ± 0.04 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.151 ± 0.012 | -0.100 ± 0.010 | -0.023 ± 0.006 |
| hand | -0.11 ± 0.01 | +0.00 ± 0.00 | -0.03 ± 0.00 | -0.056 ± 0.003 | -0.012 ± 0.004 | -0.007 ± 0.003 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| greedy | 0.310 / 0.087 | 0.47 / 0.54 | 0.039 / 0.160 | 0.00 / 0.00 | 0.39 / 0.43 | 0.376 / 0.314 |
| careful | 0.357 / 0.106 | 0.38 / 0.42 | 0.038 / 0.158 | 0.00 / 0.00 | 0.29 / 0.31 | 0.308 / 0.256 |
| stamper | 0.024 / 0.000 | 0.00 / — | 0.000 / 0.028 | — / 0.00 | — / — | 1.194 / 1.757 |
| hand | 0.417 / 0.178 | 0.14 / 0.17 | 0.033 / 0.086 | 0.00 / 0.00 | 0.11 / 0.10 | 0.316 / 0.209 |

# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --arm 1c`, seeds 21-40, hide ``, model `None` (value off, horizon 8)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 36322.2 ± 865.4 | 909.8 ± 787.0 | 4300.1 | 0.882 | 0.118 | 0.001 | 0.023 | 0.026 | 0.328 | 0.310 | 12.20 | 22.00 | 0.30 |
| careful | 35412.4 ± 510.2 | nan ± nan | 4475.4 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.352 | 0.000 | 2.55 | 0.00 | 0.15 |
| stamper | 7133.5 ± 223.0 | -28278.8 ± 587.9 | 1077.8 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.020 | 1.000 | 14.80 | 187.50 | 1.00 |
| hand | 33026.1 ± 711.9 | -2386.2 ± 875.6 | 4697.2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.362 | 0.000 | 7.10 | 0.00 | 0.55 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| direct | 0.023 (5607) [rej. blind 0.000] / 0.026 (52181) [rej. blind 0.000] | 0.275 (1554) [rej. blind 0.001] / 0.348 (23226) | 0.107 (1427) [rej. blind 0.018] / 0.047 (2007) [rej. blind 0.004] | — / — |
| careful | 0.000 (5474) / 0.000 (52508) | 0.000 (1403) / 0.000 (26048) | 0.000 (1632) / 0.000 (2444) | — / — |
| stamper | 1.000 (3070) / 1.000 (18047) | — / 1.000 (440) | — / — | — / — |
| hand | 0.000 (12053) / 0.000 (47916) | 0.000 (3233) / 0.000 (25652) | 0.000 (2662) / 0.000 (2428) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| direct | 0.023 (5607) [rej. blind 0.000] / 0.026 (52181) [rej. blind 0.000] | 0.275 (1554) [rej. blind 0.001] / 0.348 (23226) | 0.107 (1427) [rej. blind 0.018] / 0.047 (2007) [rej. blind 0.004] | — / — | 1.9 ± 0.5 | +6 |
| careful | 0.000 (5474) [rej. blind 0.000] / 0.000 (52508) [rej. blind 0.000] | 0.000 (1403) / 0.000 (26048) | 0.000 (1632) / 0.000 (2444) | — / — | 2.2 ± 0.4 | +7 |
| stamper | 1.000 (3070) / 1.000 (18047) | — / 1.000 (440) | — / — | — / — | 0.0 ± 0.0 | +0 |
| hand | 0.099 (12053) / 0.149 (47916) | 0.000 (3233) / 0.009 (25652) | 0.000 (2662) / 0.005 (2428) | — / — | 1.2 ± 0.3 | +8562 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 0.842 | 0.939 | — (0) | — (0) | 0.264 (12534) | 0.119 (2105) | 0.092 (71363) | 7.000 | 700.750 | 1.187 | 3.143 |
| careful | — | 0.919 | — (0) | — (0) | 0.000 (13929) | 0.000 (1960) | 0.000 (73620) | 4.800 | 674.350 | 1.145 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (21557) | 52.800 | 196.900 | 1.948 | 3.551 |
| hand | — | 0.999 | — (0) | — (0) | 0.000 (62) | 0.000 (649) | 0.000 (93233) | 16.600 | 359.250 | 1.295 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| direct | 39.600 | 0.000 | 0.000 | 0.000 | 0.000 | 0.300 | 0.000 |
| careful | 39.500 | 0.000 | 0.000 | 0.000 | 0.000 | 0.150 | 0.000 |
| stamper | 40.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| hand | 39.800 | 0.000 | 0.000 | 0.000 | 0.000 | 0.550 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 22.850 / 39.600 | 12.200 ± 1.321 | +9.650 ± 1.455 | 15.100 | +4.250 ± 1.453 | 3.350 | 0.069 | 7.000 | +2.200 ± 0.720 | 1943.850 | 0.017 | +0.001 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 25511.775 ± 317.790 | +1223.955 ± 373.887 | 36322.2 ± 865.4 | +909.8 ± 787.0 | 36.070 | -0.755 ± 0.422 | 14.984 ± 0.410 | +0.351 ± 0.459 | 17.902 | 0.000 | 2614.550 | 19.600 | 16.750 | +0.250 ± 0.435 | 623.884 | 155.500 |
| careful | 23.000 / 39.500 | 2.550 ± 0.456 | — | 10.850 | — | 3.400 | 0.058 | 4.800 | — | 1914.300 | 0.015 | — | 0.000 / 0.000 (0.000 / 0.000) | 24287.821 ± 342.951 | — | 35412.4 ± 510.2 | — | 36.825 | — | 14.633 ± 0.314 | — | 17.175 | 0.001 | 2629.050 | 19.500 | 16.500 | — | 780.602 | 176.350 |
| stamper | 2.800 / 40.000 | 14.800 ± 0.934 | +12.250 ± 1.102 | 111.800 | +100.950 ± 2.288 | 0.000 | 1.000 | 52.800 | +48.000 ± 2.070 | 902.300 | 0.191 | +0.175 ± 0.003 | 0.000 / 0.000 (0.000 / 0.000) | 9113.711 ± 139.999 | -15174.110 ± 330.399 | 7133.5 ± 223.0 | -28278.8 ± 587.9 | 27.260 | -9.565 ± 0.383 | 32.579 ± 1.032 | +17.945 ± 1.021 | 22.064 | 0.188 | 763.400 | 20.000 | 37.200 | +20.700 ± 0.811 | 5758.952 | 133.850 |
| hand | 19.850 / 39.800 | 7.100 ± 0.571 | +4.550 ± 0.756 | 66.000 | +55.150 ± 1.592 | 6.300 | 0.048 | 16.600 | +11.800 ± 0.851 | 1910.550 | 0.046 | +0.031 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 30729.560 ± 321.946 | +6441.739 ± 363.710 | 33026.1 ± 711.9 | -2386.2 ± 875.6 | 31.320 | -5.505 ± 0.295 | 20.230 ± 0.495 | +5.596 ± 0.610 | 19.713 | 0.020 | 2365.800 | 19.800 | 19.950 | +3.450 ± 0.432 | 52.847 | 181.100 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **direct**: p0 0.951/0.048/0.001 (591); p1 0.864/0.136/0.000 (681); p2 0.824/0.176/0.000 (827); p3 0.825/0.175/0.000 (836); p4 0.931/0.069/0.001 (860); p5 0.924/0.074/0.002 (429); p6 0.935/0.058/0.007 (76)
- **careful**: p0 1.000/0.000/0.000 (597); p1 1.000/0.000/0.000 (719); p2 1.000/0.000/0.000 (879); p3 1.000/0.000/0.000 (930); p4 1.000/0.000/0.000 (922); p5 1.000/0.000/0.000 (334); p6 1.000/0.000/0.000 (71); p7 1.000/0.000/0.000 (23)
- **stamper**: p0 0.000/1.000/0.000 (571); p1 0.000/1.000/0.000 (306); p2 0.000/1.000/0.000 (174); p3 0.000/1.000/0.000 (21); p4 0.000/1.000/0.000 (5); p5 0.000/1.000/0.000 (1)
- **hand**: p0 —/—/— (0); p1 —/—/— (0); p2 —/—/— (0); p3 —/—/— (0); p4 —/—/— (0); p5 —/—/— (0); p6 —/—/— (0); p7 —/—/— (0); p8 —/—/— (0); p9 —/—/— (0); p10 —/—/— (0); p11 —/—/— (0); p12 —/—/— (0); p13 —/—/— (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 2609.1 / 280.4 | 0.22 / 0.13 | -0.09 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.08 / 0.08 | +0.00 ± 0.00 | 0.165 / 0.135 | -0.030 ± 0.006 | 0.059 / 0.058 | 0.000 / 0.000 | 0.057 / 0.052 | -0.005 ± 0.003 | 1.49 / 1.28 | -0.21 ± 0.06 |
| careful | 2625.4 / 273.7 | 0.20 / 0.11 | -0.09 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.09 / 0.09 | -0.00 ± 0.00 | 0.145 / 0.117 | -0.028 ± 0.005 | 0.050 / 0.056 | 0.001 / 0.000 | 0.054 / 0.059 | +0.005 ± 0.003 | 1.47 / 1.20 | -0.27 ± 0.10 |
| stamper | 902.4 / 153.5 | 0.93 / 0.77 | -0.15 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.03 / 0.02 | -0.01 ± 0.00 | 0.219 / 0.208 | -0.011 ± 0.008 | 0.127 / 0.125 | 0.153 / 0.000 | 0.104 / 0.080 | -0.024 ± 0.007 | 2.96 / 1.92 | -1.04 ± 0.23 |
| hand | 2395.8 / 602.6 | 0.94 / 0.96 | +0.02 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.15 / 0.15 | -0.00 ± 0.00 | 0.408 / 0.408 | -0.000 ± 0.007 | 0.196 / 0.215 | 0.020 / 0.000 | 0.111 / 0.109 | -0.003 ± 0.004 | 2.71 / 2.66 | -0.04 ± 0.09 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| direct | -0.07 ± 0.02 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.020 ± 0.006 | +0.002 ± 0.003 | -0.005 ± 0.003 |
| careful | -0.08 ± 0.02 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.030 ± 0.005 | +0.005 ± 0.003 | +0.005 ± 0.003 |
| stamper | -0.71 ± 0.05 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.167 ± 0.012 | -0.111 ± 0.010 | -0.035 ± 0.007 |
| hand | -0.12 ± 0.02 | +0.00 ± 0.00 | -0.03 ± 0.00 | -0.061 ± 0.005 | -0.016 ± 0.004 | -0.005 ± 0.004 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| direct | 0.439 / 0.139 | 0.38 / 0.40 | 0.039 / 0.153 | 0.00 / 0.00 | 0.37 / 0.43 | 0.505 / 0.290 |
| careful | 0.490 / 0.156 | 0.29 / 0.29 | 0.038 / 0.160 | 0.00 / 0.00 | 0.25 / 0.29 | 0.439 / 0.237 |
| stamper | 0.024 / 0.000 | 0.00 / — | 0.000 / 0.030 | — / 0.00 | — / — | 1.236 / 1.734 |
| hand | 0.525 / 0.221 | 0.11 / 0.13 | 0.033 / 0.084 | 0.00 / 0.00 | 0.09 / 0.11 | 0.480 / 0.218 |

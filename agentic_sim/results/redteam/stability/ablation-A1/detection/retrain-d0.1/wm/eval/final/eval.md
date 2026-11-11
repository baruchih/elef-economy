# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --dispute-policy truthful --dispute-rate 0.1`, seeds 21-40, hide ``, model `/Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/ablation-A1/detection/retrain-d0.1/wm/models/wm-online-20.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 34804.3 ± 787.9 | 413.3 ± 977.8 | 4223.1 | 0.810 | 0.188 | 0.002 | 0.002 | 0.002 | 0.317 | 0.597 | 11.40 | 10.10 | 0.50 |
| careful | 34391.0 ± 812.7 | nan ± nan | 4563.9 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.366 | 0.000 | 2.55 | 0.00 | 0.35 |
| stamper | 6812.9 ± 146.0 | -27578.1 ± 860.3 | 1066.8 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.022 | 1.000 | 14.20 | 185.45 | 1.00 |
| hand | 32073.1 ± 585.1 | -2317.9 ± 899.7 | 4728.3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.373 | 0.000 | 7.10 | 0.00 | 0.50 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| greedy | 0.002 (5309) / 0.002 (52390) | 0.603 (1233) [rej. blind 0.002] / 0.675 (21716) [rej. blind 0.000] | 0.164 (1144) [rej. blind 0.051] / 0.139 (2669) [rej. blind 0.027] | — / — |
| careful | 0.000 (5261) / 0.000 (52569) | 0.000 (1211) / 0.000 (26220) | 0.000 (1708) / 0.000 (4310) | — / — |
| stamper | 1.000 (3034) / 1.000 (17841) | — / 1.000 (446) | — / 1.000 (14) | — / — |
| hand | 0.000 (11850) / 0.000 (47399) | 0.000 (3033) / 0.000 (25219) | 0.000 (2910) / 0.000 (4155) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| greedy | 0.002 (5309) / 0.002 (52390) | 0.603 (1233) [rej. blind 0.002] / 0.675 (21716) [rej. blind 0.000] | 0.164 (1144) [rej. blind 0.051] / 0.139 (2669) [rej. blind 0.027] | — / — | 1.9 ± 0.4 | +1 |
| careful | 0.000 (5261) / 0.000 (52569) [rej. blind 0.000] | 0.000 (1211) / 0.000 (26220) | 0.000 (1708) / 0.000 (4310) | — / — | 3.1 ± 0.5 | +13 |
| stamper | 1.000 (3034) / 1.000 (17841) | — / 1.000 (446) | — / 1.000 (14) | — / — | 0.0 ± 0.0 | +0 |
| hand | 0.104 (11850) / 0.154 (47399) | 0.000 (3033) / 0.009 (25219) | 0.000 (2910) / 0.008 (4155) | — / — | 0.9 ± 0.2 | +8785 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 0.756 | 0.942 | — (0) | — (0) | 0.494 (16010) | 0.441 (392) | 0.115 (68059) | 24.350 | 733.650 | 1.205 | 0.415 |
| careful | — | 0.908 | — (0) | — (0) | 0.000 (16977) | 0.000 (156) | 0.000 (74146) | 25.350 | 691.450 | 1.136 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (21335) | 77.350 | 178.850 | 2.150 | 2.398 |
| hand | — | 1.000 | — (0) | — (0) | 0.000 (12) | 0.000 (756) | 0.000 (93798) | 36.900 | 356.250 | 1.349 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| greedy | 39.700 | 0.000 | 0.000 | 0.000 | 0.000 | 0.500 | 0.000 |
| careful | 39.850 | 0.000 | 0.000 | 0.000 | 0.000 | 0.350 | 0.000 |
| stamper | 39.950 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| hand | 39.900 | 0.000 | 0.000 | 0.000 | 0.000 | 0.500 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 23.950 / 39.700 | 11.400 ± 0.694 | +8.850 ± 0.744 | 9.950 | +0.050 ± 0.966 | 3.200 | 0.058 | 4.650 | -0.850 ± 0.563 | 1926.050 | 0.015 | -0.008 ± 0.001 | 2.550 / 2.250 (2.550 / 2.250) | 25247.166 ± 363.128 | +868.504 ± 451.558 | 34804.3 ± 787.9 | +413.3 ± 977.8 | 36.570 | +0.019 ± 0.426 | 15.477 ± 0.348 | +0.067 ± 0.574 | 18.280 | 0.001 | 2623.100 | 19.700 | 15.750 | -1.700 ± 0.641 | 719.871 | 203.000 |
| careful | 22.400 / 39.850 | 2.550 ± 0.359 | — | 9.900 | — | 3.450 | 0.050 | 5.500 | — | 1905.400 | 0.023 | — | 3.600 / 3.500 (3.600 / 3.500) | 24378.662 ± 301.908 | — | 34391.0 ± 812.7 | — | 36.551 | — | 15.410 ± 0.507 | — | 17.739 | 0.001 | 2632.950 | 19.850 | 17.450 | — | 694.584 | 239.500 |
| stamper | 4.400 / 39.950 | 14.200 ± 0.698 | +11.650 ± 0.762 | 115.650 | +105.750 ± 2.466 | 0.000 | 1.000 | 57.400 | +51.900 ± 2.499 | 875.950 | 0.181 | +0.158 ± 0.003 | 15.950 / 15.400 (15.950 / 15.400) | 8729.991 ± 156.518 | -15648.671 ± 312.694 | 6812.9 ± 146.0 | -27578.1 ± 860.3 | 26.718 | -9.833 ± 0.436 | 32.649 ± 0.721 | +17.239 ± 0.940 | 22.598 | 0.240 | 708.200 | 19.950 | 35.550 | +18.100 ± 0.891 | 5714.789 | 131.200 |
| hand | 20.000 / 39.900 | 7.100 ± 0.528 | +4.550 ± 0.709 | 67.450 | +57.550 ± 0.958 | 7.400 | 0.061 | 17.000 | +11.500 ± 0.819 | 1895.750 | 0.052 | +0.029 ± 0.002 | 8.650 / 8.450 (8.650 / 8.450) | 30131.308 ± 428.831 | +5752.646 ± 452.739 | 32073.1 ± 585.1 | -2317.9 ± 899.7 | 31.152 | -5.399 ± 0.427 | 20.140 ± 0.479 | +4.730 ± 0.757 | 20.141 | 0.034 | 2308.250 | 19.900 | 19.900 | +2.450 ± 0.559 | 54.272 | 148.450 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **greedy**: p0 0.962/0.038/0.000 (581); p1 0.836/0.162/0.002 (694); p2 0.757/0.242/0.001 (795); p3 0.726/0.272/0.002 (897); p4 0.780/0.218/0.002 (923); p5 0.920/0.078/0.002 (312); p6 0.964/0.036/0.000 (22)
- **careful**: p0 1.000/0.000/0.000 (608); p1 1.000/0.000/0.000 (797); p2 1.000/0.000/0.000 (924); p3 1.000/0.000/0.000 (971); p4 1.000/0.000/0.000 (974); p5 1.000/0.000/0.000 (290)
- **stamper**: p0 0.000/1.000/0.000 (564); p1 0.000/1.000/0.000 (305); p2 0.000/1.000/0.000 (164); p3 0.000/1.000/0.000 (24); p4 0.000/1.000/0.000 (8); p5 0.000/1.000/0.000 (2)
- **hand**: p0 —/—/— (0); p1 —/—/— (0); p2 —/—/— (0); p3 —/—/— (0); p4 —/—/— (0); p5 —/—/— (0); p6 —/—/— (0); p7 —/—/— (0); p8 —/—/— (0); p9 —/—/— (0); p10 —/—/— (0); p11 —/—/— (0); p12 —/—/— (0); p13 —/—/— (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 2619.5 / 265.4 | 0.27 / 0.20 | -0.08 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.06 / 0.06 | -0.00 ± 0.00 | 0.164 / 0.140 | -0.024 ± 0.005 | 0.055 / 0.063 | 0.001 / 0.000 | 0.059 / 0.058 | -0.001 ± 0.004 | 1.68 / 1.37 | -0.31 ± 0.13 |
| careful | 2628.4 / 263.1 | 0.22 / 0.12 | -0.10 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.10 / 0.10 | +0.00 ± 0.00 | 0.155 / 0.123 | -0.032 ± 0.006 | 0.060 / 0.063 | 0.001 / 0.000 | 0.052 / 0.050 | -0.003 ± 0.003 | 1.60 / 1.24 | -0.36 ± 0.12 |
| stamper | 892.0 / 151.7 | 1.06 / 0.77 | -0.29 ± 0.04 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.04 / 0.03 | -0.01 ± 0.00 | 0.227 / 0.221 | -0.007 ± 0.010 | 0.127 / 0.137 | 0.205 / 0.000 | 0.095 / 0.063 | -0.033 ± 0.004 | 3.40 / 2.03 | -1.36 ± 0.29 |
| hand | 2369.9 / 592.5 | 1.04 / 1.12 | +0.09 ± 0.04 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.15 / 0.15 | -0.00 ± 0.00 | 0.439 / 0.449 | +0.010 ± 0.007 | 0.207 / 0.233 | 0.035 / 0.000 | 0.111 / 0.116 | +0.005 ± 0.004 | 3.01 / 3.06 | +0.05 ± 0.12 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| greedy | -0.07 ± 0.02 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.026 ± 0.005 | +0.007 ± 0.003 | -0.001 ± 0.004 |
| careful | -0.09 ± 0.02 | +0.00 ± 0.00 | +0.00 ± 0.00 | -0.030 ± 0.006 | +0.005 ± 0.004 | -0.002 ± 0.003 |
| stamper | -0.80 ± 0.05 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.143 ± 0.014 | -0.086 ± 0.010 | -0.039 ± 0.005 |
| hand | -0.06 ± 0.03 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.057 ± 0.004 | -0.010 ± 0.003 | +0.002 ± 0.004 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| greedy | 0.409 / 0.124 | 0.47 / 0.46 | 0.041 / 0.187 | 0.00 / 0.00 | 0.46 / 0.50 | 0.384 / 0.345 |
| careful | 0.493 / 0.140 | 0.29 / 0.29 | 0.040 / 0.183 | 0.00 / 0.00 | 0.28 / 0.26 | 0.275 / 0.235 |
| stamper | 0.025 / 0.000 | 0.00 / — | 0.018 / 0.129 | 0.00 / 0.00 | 0.14 / — | 1.199 / 1.789 |
| hand | 0.521 / 0.210 | 0.12 / 0.15 | 0.035 / 0.108 | 0.00 / 0.00 | 0.12 / 0.14 | 0.330 / 0.228 |

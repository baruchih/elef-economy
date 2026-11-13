# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1 --pi-a0 0.10 --pi-a-max 0.10`, seeds 21-40, hide ``, model `/Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/ablation-A1/stress/learned/horizon/pa10-t1-b1-mc/wm-ret/models/wm-online-10.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 29833.5 ± 366.0 | -5668.7 ± 800.8 | 3977.2 | 0.758 | 0.049 | 0.027 | 0.243 | 0.236 | 0.222 | 0.254 | 14.95 | 113.25 | 0.30 |
| careful | 35502.3 ± 852.9 | nan ± nan | 4637.9 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.384 | 0.000 | 2.55 | 0.00 | 0.30 |
| stamper | 6932.3 ± 121.2 | -28570.0 ± 843.3 | 1075.2 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.020 | 1.000 | 15.65 | 181.55 | 1.00 |
| claimer | 9582.7 ± 171.7 | -25919.6 ± 875.8 | 1049.0 | 0.000 | 0.000 | 0.000 | 1.000 | 1.000 | 0.021 | 1.000 | 14.20 | 179.80 | 1.00 |
| hand | 32158.8 ± 656.4 | -3343.5 ± 690.8 | 4875.9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.391 | 0.000 | 7.65 | 0.00 | 0.50 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| greedy | 0.243 (14133) [rej. blind 0.028] / 0.236 (47714) [rej. blind 0.024] | 0.242 (2769) [rej. blind 0.033] / 0.275 (10341) [rej. blind 0.028] | 0.213 (1986) [rej. blind 0.045] / 0.216 (2602) [rej. blind 0.042] | — / — |
| careful | 0.000 (5284) / 0.000 (51900) | 0.000 (3178) / 0.000 (24974) | 0.000 (3248) / 0.000 (4174) | — / — |
| stamper | 1.000 (3109) / 1.000 (17956) | — / 1.000 (440) | — / — | — / — |
| claimer | 1.000 (2986) / 1.000 (17556) | — / 1.000 (439) | — / — | — / — |
| hand | 0.000 (12036) / 0.000 (47342) | 0.000 (5048) / 0.000 (24706) | 0.000 (4294) / 0.000 (4092) | — / — |

The stressed world's fourth action by seat kind — the allowance claimed and the verdict F without inspecting (counted above among the blind verdicts; the ledger sees a careful review, so the measured reading below cannot see it):

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| greedy | 0.161 (14133) / 0.163 (47714) | 0.178 (2769) / 0.196 (10341) | 0.135 (1986) / 0.136 (2602) | — / — |
| careful | 0.000 (5284) / 0.000 (51900) | 0.000 (3178) / 0.000 (24974) | 0.000 (3248) / 0.000 (4174) | — / — |
| stamper | 0.000 (3109) / 0.000 (17956) | — / 0.000 (440) | — / — | — / — |
| claimer | 1.000 (2986) / 1.000 (17556) | — / 1.000 (439) | — / — | — / — |
| hand | 0.000 (12036) / 0.000 (47342) | 0.000 (5048) / 0.000 (24706) | 0.000 (4294) / 0.000 (4092) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| greedy | 0.082 (14133) [rej. blind 0.028] / 0.073 (47714) [rej. blind 0.024] | 0.064 (2769) [rej. blind 0.033] / 0.079 (10341) [rej. blind 0.028] | 0.078 (1986) [rej. blind 0.045] / 0.080 (2602) [rej. blind 0.042] | — / — | 1.4 ± 0.3 | -13192 |
| careful | 0.000 (5284) [rej. blind 0.000] / 0.000 (51900) [rej. blind 0.000] | 0.000 (3178) / 0.000 (24974) | 0.000 (3248) / 0.000 (4174) | — / — | 2.2 ± 0.3 | +7 |
| stamper | 1.000 (3109) / 1.000 (17956) | — / 1.000 (440) | — / — | — / — | 0.0 ± 0.0 | +0 |
| claimer | 0.000 (2986) / 0.000 (17556) | — / 0.000 (439) | — / — | — / — | 0.0 ± 0.0 | -20979 |
| hand | 0.100 (12036) / 0.157 (47342) | 0.000 (5048) / 0.010 (24706) | 0.000 (4294) / 0.005 (4092) | — / — | 0.7 ± 0.2 | +8898 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 1.000 | 1.000 | — (0) | — (0) | — (0) | 0.286 (14) | 0.049 (79531) | 17.250 | 318.650 | 1.477 | 6.565 |
| careful | — | 0.910 | — (0) | — (0) | 0.000 (16686) | 0.000 (779) | 0.000 (75293) | 4.600 | 668.700 | 1.190 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (21505) | 58.750 | 177.550 | 2.177 | 3.090 |
| claimer | — | 1.000 | — (0) | — (0) | — (0) | — (0) | 0.000 (20981) | 54.800 | 178.000 | 2.173 | 3.281 |
| hand | — | 0.999 | — (0) | — (0) | 0.000 (61) | 0.000 (525) | 0.000 (96932) | 16.700 | 355.300 | 1.426 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| greedy | 39.750 | 0.000 | 0.000 | 0.000 | 0.000 | 0.300 | 0.000 |
| careful | 39.750 | 0.000 | 0.000 | 0.000 | 0.000 | 0.300 | 0.000 |
| stamper | 40.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| claimer | 39.850 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| hand | 39.800 | 0.000 | 0.000 | 0.000 | 0.000 | 0.500 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 17.650 / 39.750 | 14.950 ± 1.144 | +12.400 ± 1.153 | 133.450 | +123.350 ± 3.958 | 12.400 | 0.191 | 17.250 | +12.650 ± 0.947 | 1891.500 | 0.067 | +0.041 ± 0.002 | 0.000 / 0.000 (0.000 / 0.000) | 27318.982 ± 241.644 | +2384.332 ± 504.700 | 29833.5 ± 366.0 | -5668.7 ± 800.8 | 31.129 | -5.101 ± 0.449 | 21.747 ± 0.246 | +6.650 ± 0.575 | 19.331 | 0.026 | 2330.000 | 19.750 | 22.100 | +5.300 ± 0.417 | 68.263 | 171.000 |
| careful | 22.950 / 39.750 | 2.550 ± 0.438 | — | 10.100 | — | 3.250 | 0.053 | 4.600 | — | 1896.050 | 0.025 | — | 0.000 / 0.000 (0.000 / 0.000) | 24934.650 ± 445.425 | — | 35502.3 ± 852.9 | — | 36.230 | — | 15.098 ± 0.513 | — | 17.953 | 0.001 | 2599.400 | 19.750 | 16.800 | — | 689.070 | 188.600 |
| stamper | 4.250 / 40.000 | 15.650 ± 0.895 | +13.100 ± 0.771 | 117.200 | +107.100 ± 2.883 | 0.000 | 1.000 | 58.750 | +54.150 ± 2.500 | 897.700 | 0.189 | +0.164 ± 0.004 | 0.000 / 0.000 (0.000 / 0.000) | 9091.606 ± 197.532 | -15843.044 ± 466.104 | 6932.3 ± 121.2 | -28570.0 ± 843.3 | 26.326 | -9.904 ± 0.472 | 33.112 ± 0.588 | +18.014 ± 0.831 | 22.849 | 0.237 | 713.750 | 20.000 | 35.750 | +18.950 ± 0.832 | 5586.993 | 128.750 |
| claimer | 5.850 / 39.850 | 14.200 ± 0.706 | +11.650 ± 0.674 | 111.850 | +101.750 ± 2.059 | 0.000 | 1.000 | 54.800 | +50.200 ± 1.893 | 877.600 | 0.192 | +0.167 ± 0.003 | 0.000 / 0.000 (0.000 / 0.000) | 7654.287 ± 133.917 | -17280.363 ± 518.037 | 9582.7 ± 171.7 | -25919.6 ± 875.8 | 26.418 | -9.812 ± 0.481 | 28.745 ± 0.671 | +13.647 ± 0.882 | 20.850 | 0.236 | 699.800 | 19.850 | 34.000 | +17.200 ± 0.760 | 5729.779 | 146.750 |
| hand | 20.250 / 39.800 | 7.650 ± 0.658 | +5.100 ± 0.849 | 66.350 | +56.250 ± 1.332 | 6.500 | 0.050 | 16.700 | +12.100 ± 0.764 | 1893.800 | 0.058 | +0.033 ± 0.002 | 0.000 / 0.000 (0.000 / 0.000) | 30737.749 ± 417.993 | +5803.099 ± 558.949 | 32158.8 ± 656.4 | -3343.5 ± 690.8 | 30.961 | -5.269 ± 0.456 | 20.486 ± 0.457 | +5.388 ± 0.668 | 20.249 | 0.036 | 2305.100 | 19.800 | 19.550 | +2.750 ± 0.502 | 49.328 | 172.800 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **greedy**: p0 0.939/0.047/0.013 (457); p1 0.892/0.093/0.015 (306); p2 0.815/0.138/0.047 (241); p3 0.942/0.023/0.035 (202); p4 0.943/0.021/0.036 (208); p5 0.896/0.078/0.027 (202); p6 0.919/0.062/0.019 (202); p7 0.904/0.067/0.029 (191); p8 0.885/0.073/0.042 (201); p9 0.885/0.062/0.052 (193); p10 0.912/0.048/0.040 (213); p11 0.936/0.038/0.027 (232); p12 0.952/0.020/0.028 (228); p13 0.904/0.032/0.065 (177); p14 0.874/0.069/0.056 (59); p15 0.891/0.109/0.000 (6)
- **careful**: p0 1.000/0.000/0.000 (605); p1 1.000/0.000/0.000 (751); p2 1.000/0.000/0.000 (913); p3 1.000/0.000/0.000 (1021); p4 1.000/0.000/0.000 (1014); p5 1.000/0.000/0.000 (292); p6 1.000/0.000/0.000 (40); p7 1.000/0.000/0.000 (2)
- **stamper**: p0 0.000/1.000/0.000 (561); p1 0.000/1.000/0.000 (305); p2 0.000/1.000/0.000 (171); p3 0.000/1.000/0.000 (27); p4 0.000/1.000/0.000 (10); p5 0.000/1.000/0.000 (3)
- **claimer**: p0 —/—/— (0); p1 —/—/— (0); p2 —/—/— (0); p3 —/—/— (0); p4 —/—/— (0); p5 —/—/— (0)
- **hand**: p0 —/—/— (0); p1 —/—/— (0); p2 —/—/— (0); p3 —/—/— (0); p4 —/—/— (0); p5 —/—/— (0); p6 —/—/— (0); p7 —/—/— (0); p8 —/—/— (0); p9 —/—/— (0); p10 —/—/— (0); p11 —/—/— (0); p12 —/—/— (0); p13 —/—/— (0); p14 —/—/— (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 2385.7 / 706.6 | 1.07 / 1.24 | +0.17 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.04 / 0.03 | -0.01 ± 0.00 | 0.425 / 0.456 | +0.031 ± 0.008 | 0.223 / 0.255 | 0.026 / 0.000 | 0.139 / 0.152 | +0.013 ± 0.003 | 2.90 / 3.04 | +0.14 ± 0.05 |
| careful | 2595.0 / 264.2 | 0.28 / 0.20 | -0.08 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.13 / 0.12 | -0.01 ± 0.00 | 0.170 / 0.144 | -0.025 ± 0.006 | 0.068 / 0.078 | 0.001 / 0.000 | 0.056 / 0.051 | -0.005 ± 0.004 | 1.75 / 1.49 | -0.26 ± 0.06 |
| stamper | 897.8 / 155.4 | 1.08 / 0.80 | -0.28 ± 0.05 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.03 / 0.02 | -0.01 ± 0.00 | 0.237 / 0.239 | +0.002 ± 0.011 | 0.130 / 0.142 | 0.204 / 0.000 | 0.099 / 0.081 | -0.019 ± 0.005 | 3.46 / 2.36 | -1.10 ± 0.20 |
| claimer | 877.8 / 149.3 | 1.25 / 0.94 | -0.31 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.03 / 0.02 | -0.01 ± 0.00 | 0.290 / 0.264 | -0.026 ± 0.010 | 0.154 / 0.146 | 0.202 / 0.000 | 0.106 / 0.086 | -0.020 ± 0.005 | 3.72 / 2.68 | -1.04 ± 0.23 |
| hand | 2367.1 / 601.8 | 1.05 / 1.07 | +0.03 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.15 / 0.16 | +0.00 ± 0.00 | 0.445 / 0.459 | +0.015 ± 0.007 | 0.211 / 0.234 | 0.036 / 0.000 | 0.105 / 0.100 | -0.005 ± 0.004 | 3.02 / 2.87 | -0.16 ± 0.10 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| greedy | -0.00 ± 0.02 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.044 ± 0.004 | -0.013 ± 0.003 | -0.001 ± 0.003 |
| careful | -0.08 ± 0.02 | +0.00 ± 0.00 | -0.01 ± 0.01 | -0.024 ± 0.005 | +0.011 ± 0.004 | -0.004 ± 0.004 |
| stamper | -0.77 ± 0.06 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.148 ± 0.017 | -0.096 ± 0.012 | -0.028 ± 0.006 |
| claimer | -0.81 ± 0.03 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.181 ± 0.013 | -0.119 ± 0.010 | -0.026 ± 0.005 |
| hand | -0.12 ± 0.02 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.055 ± 0.005 | -0.017 ± 0.003 | -0.007 ± 0.003 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| greedy | 0.215 / 0.128 | 0.58 / 0.64 | 0.046 / 0.096 | 0.00 / 0.00 | 0.59 / 0.58 | 0.698 / 0.544 |
| careful | 0.474 / 0.137 | 0.30 / 0.31 | 0.040 / 0.162 | 0.00 / 0.00 | 0.28 / 0.31 | 0.302 / 0.249 |
| stamper | 0.025 / 0.000 | 0.00 / — | 0.000 / 0.035 | — / 0.00 | — / — | 1.195 / 1.769 |
| claimer | 0.025 / 0.000 | 0.00 / — | 0.000 / 0.034 | — / 0.00 | — / — | 1.197 / 1.758 |
| hand | 0.509 / 0.214 | 0.12 / 0.13 | 0.033 / 0.085 | 0.00 / 0.00 | 0.11 / 0.13 | 0.343 / 0.228 |

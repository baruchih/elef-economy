# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --pi-a0 0.10 --pi-a-max 0.10`, seeds 21-40, hide ``, model `None` (value off, horizon 8)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 33416.7 ± 777.9 | -2085.5 ± 840.8 | 4490.4 | 0.936 | 0.052 | 0.012 | 0.011 | 0.012 | 0.362 | 0.158 | 5.50 | 8.20 | 0.40 |
| careful | 35502.3 ± 852.9 | nan ± nan | 4637.9 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.384 | 0.000 | 2.55 | 0.00 | 0.30 |
| stamper | 6932.3 ± 121.2 | -28570.0 ± 843.3 | 1075.2 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.020 | 1.000 | 15.65 | 181.55 | 1.00 |
| hand | 32158.8 ± 656.4 | -3343.5 ± 690.8 | 4875.9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.391 | 0.000 | 7.65 | 0.00 | 0.50 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| direct | 0.011 (5362) [rej. blind 0.000] / 0.012 (51927) [rej. blind 0.000] | 0.127 (2971) [rej. blind 0.022] / 0.151 (23147) [rej. blind 0.002] | 0.240 (2754) [rej. blind 0.168] / 0.165 (3648) [rej. blind 0.147] | — / — |
| careful | 0.000 (5284) / 0.000 (51900) | 0.000 (3178) / 0.000 (24974) | 0.000 (3248) / 0.000 (4174) | — / — |
| stamper | 1.000 (3109) / 1.000 (17956) | — / 1.000 (440) | — / — | — / — |
| hand | 0.000 (12036) / 0.000 (47342) | 0.000 (5048) / 0.000 (24706) | 0.000 (4294) / 0.000 (4092) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| direct | 0.011 (5362) [rej. blind 0.001] / 0.012 (51927) [rej. blind 0.000] | 0.127 (2971) [rej. blind 0.022] / 0.151 (23147) [rej. blind 0.002] | 0.240 (2754) [rej. blind 0.168] / 0.165 (3648) [rej. blind 0.147] | — / — | 2.2 ± 0.4 | +14 |
| careful | 0.000 (5284) [rej. blind 0.000] / 0.000 (51900) [rej. blind 0.000] | 0.000 (3178) / 0.000 (24974) | 0.000 (3248) / 0.000 (4174) | — / — | 2.2 ± 0.3 | +7 |
| stamper | 1.000 (3109) / 1.000 (17956) | — / 1.000 (440) | — / — | — / — | 0.0 ± 0.0 | +0 |
| hand | 0.100 (12036) / 0.157 (47342) | 0.000 (5048) / 0.010 (24706) | 0.000 (4294) / 0.005 (4092) | — / — | 0.7 ± 0.2 | +8898 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 0.861 | 0.925 | — (0) | — (0) | 0.092 (14296) | 0.033 (698) | 0.045 (74815) | 24.500 | 723.700 | 1.178 | 0.335 |
| careful | — | 0.910 | — (0) | — (0) | 0.000 (16686) | 0.000 (779) | 0.000 (75293) | 24.350 | 668.700 | 1.190 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (21505) | 78.750 | 177.550 | 2.177 | 2.305 |
| hand | — | 0.999 | — (0) | — (0) | 0.000 (61) | 0.000 (525) | 0.000 (96932) | 36.500 | 355.300 | 1.426 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| direct | 39.650 | 0.000 | 0.000 | 0.000 | 0.000 | 0.400 | 0.000 |
| careful | 39.750 | 0.000 | 0.000 | 0.000 | 0.000 | 0.300 | 0.000 |
| stamper | 40.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| hand | 39.800 | 0.000 | 0.000 | 0.000 | 0.000 | 0.500 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 23.250 / 39.650 | 5.500 ± 0.655 | +2.950 ± 0.526 | 11.600 | +1.500 ± 1.423 | 4.000 | 0.057 | 4.850 | +0.250 ± 0.699 | 1921.050 | 0.032 | +0.007 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 25485.851 ± 330.142 | +551.201 ± 523.701 | 33416.7 ± 777.9 | -2085.5 ± 840.8 | 35.283 | -0.947 ± 0.503 | 16.433 ± 0.348 | +1.336 ± 0.597 | 18.861 | 0.001 | 2600.750 | 19.650 | 16.400 | -0.400 ± 0.568 | 452.364 | 193.700 |
| careful | 22.950 / 39.750 | 2.550 ± 0.438 | — | 10.100 | — | 3.250 | 0.053 | 4.600 | — | 1896.050 | 0.025 | — | 0.000 / 0.000 (0.000 / 0.000) | 24934.650 ± 445.425 | — | 35502.3 ± 852.9 | — | 36.230 | — | 15.098 ± 0.513 | — | 17.953 | 0.001 | 2599.400 | 19.750 | 16.800 | — | 689.070 | 188.600 |
| stamper | 4.250 / 40.000 | 15.650 ± 0.895 | +13.100 ± 0.771 | 117.200 | +107.100 ± 2.883 | 0.000 | 1.000 | 58.750 | +54.150 ± 2.500 | 897.700 | 0.189 | +0.164 ± 0.004 | 0.000 / 0.000 (0.000 / 0.000) | 9091.606 ± 197.532 | -15843.044 ± 466.104 | 6932.3 ± 121.2 | -28570.0 ± 843.3 | 26.326 | -9.904 ± 0.472 | 33.112 ± 0.588 | +18.014 ± 0.831 | 22.849 | 0.237 | 713.750 | 20.000 | 35.750 | +18.950 ± 0.832 | 5586.993 | 128.750 |
| hand | 20.250 / 39.800 | 7.650 ± 0.658 | +5.100 ± 0.849 | 66.350 | +56.250 ± 1.332 | 6.500 | 0.050 | 16.700 | +12.100 ± 0.764 | 1893.800 | 0.058 | +0.033 ± 0.002 | 0.000 / 0.000 (0.000 / 0.000) | 30737.749 ± 417.993 | +5803.099 ± 558.949 | 32158.8 ± 656.4 | -3343.5 ± 690.8 | 30.961 | -5.269 ± 0.456 | 20.486 ± 0.457 | +5.388 ± 0.668 | 20.249 | 0.036 | 2305.100 | 19.800 | 19.550 | +2.750 ± 0.502 | 49.328 | 172.800 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **direct**: p0 0.959/0.039/0.002 (589); p1 0.902/0.080/0.018 (695); p2 0.908/0.073/0.019 (875); p3 0.939/0.049/0.012 (959); p4 0.955/0.036/0.009 (1011); p5 0.965/0.021/0.014 (311); p6 0.969/0.031/0.000 (32); p7 0.959/0.038/0.003 (18)
- **careful**: p0 1.000/0.000/0.000 (605); p1 1.000/0.000/0.000 (751); p2 1.000/0.000/0.000 (913); p3 1.000/0.000/0.000 (1021); p4 1.000/0.000/0.000 (1014); p5 1.000/0.000/0.000 (292); p6 1.000/0.000/0.000 (40); p7 1.000/0.000/0.000 (2)
- **stamper**: p0 0.000/1.000/0.000 (561); p1 0.000/1.000/0.000 (305); p2 0.000/1.000/0.000 (171); p3 0.000/1.000/0.000 (27); p4 0.000/1.000/0.000 (10); p5 0.000/1.000/0.000 (3)
- **hand**: p0 —/—/— (0); p1 —/—/— (0); p2 —/—/— (0); p3 —/—/— (0); p4 —/—/— (0); p5 —/—/— (0); p6 —/—/— (0); p7 —/—/— (0); p8 —/—/— (0); p9 —/—/— (0); p10 —/—/— (0); p11 —/—/— (0); p12 —/—/— (0); p13 —/—/— (0); p14 —/—/— (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 2596.3 / 268.1 | 0.32 / 0.24 | -0.08 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.11 / 0.11 | -0.00 ± 0.00 | 0.213 / 0.183 | -0.030 ± 0.004 | 0.079 / 0.086 | 0.001 / 0.000 | 0.058 / 0.061 | +0.003 ± 0.004 | 1.75 / 1.57 | -0.17 ± 0.09 |
| careful | 2595.0 / 264.2 | 0.28 / 0.20 | -0.08 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.13 / 0.12 | -0.01 ± 0.00 | 0.170 / 0.144 | -0.025 ± 0.006 | 0.068 / 0.078 | 0.001 / 0.000 | 0.056 / 0.051 | -0.005 ± 0.004 | 1.75 / 1.49 | -0.26 ± 0.06 |
| stamper | 897.8 / 155.4 | 1.08 / 0.80 | -0.28 ± 0.05 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.03 / 0.02 | -0.01 ± 0.00 | 0.237 / 0.239 | +0.002 ± 0.011 | 0.130 / 0.142 | 0.204 / 0.000 | 0.099 / 0.081 | -0.019 ± 0.005 | 3.46 / 2.36 | -1.10 ± 0.20 |
| hand | 2367.1 / 601.8 | 1.05 / 1.07 | +0.03 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.15 / 0.16 | +0.00 ± 0.00 | 0.445 / 0.459 | +0.015 ± 0.007 | 0.211 / 0.234 | 0.036 / 0.000 | 0.105 / 0.100 | -0.005 ± 0.004 | 3.02 / 2.87 | -0.16 ± 0.10 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| direct | -0.08 ± 0.02 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.030 ± 0.004 | +0.006 ± 0.004 | +0.004 ± 0.004 |
| careful | -0.08 ± 0.02 | +0.00 ± 0.00 | -0.01 ± 0.01 | -0.024 ± 0.005 | +0.011 ± 0.004 | -0.004 ± 0.004 |
| stamper | -0.77 ± 0.06 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.148 ± 0.017 | -0.096 ± 0.012 | -0.028 ± 0.006 |
| hand | -0.12 ± 0.02 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.055 ± 0.005 | -0.017 ± 0.003 | -0.007 ± 0.003 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| direct | 0.439 / 0.130 | 0.35 / 0.35 | 0.040 / 0.164 | 0.00 / 0.00 | 0.34 / 0.42 | 0.357 / 0.316 |
| careful | 0.474 / 0.137 | 0.30 / 0.31 | 0.040 / 0.162 | 0.00 / 0.00 | 0.28 / 0.31 | 0.302 / 0.280 |
| stamper | 0.025 / 0.000 | 0.00 / — | 0.000 / 0.035 | — / 0.00 | — / — | 1.195 / 1.769 |
| hand | 0.509 / 0.214 | 0.12 / 0.13 | 0.033 / 0.085 | 0.00 / 0.00 | 0.11 / 0.13 | 0.343 / 0.237 |

# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule`, seeds 21-40, hide ``, model `None` (value off, horizon 8)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the plant-blind seats — a revised submission or a panel, where no plant is received — are read apart: their share of the review decisions and the stamp rate on them.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | blind-seat share | blind-seat stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 28840.5 ± 580.1 | -6652.6 ± 1184.4 | 3647.0 | 0.520 | 0.463 | 0.018 | 0.334 | 0.367 | 0.219 | 0.914 | 88.65 | 237.20 | 0.35 |
| careful | 35493.1 ± 953.9 | nan ± nan | 4109.2 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.290 | 0.000 | 6.50 | 0.00 | 0.45 |
| hand | 31815.8 ± 548.8 | -3677.3 ± 1033.7 | 4361.4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.293 | 0.000 | 11.25 | 0.00 | 0.65 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 0.860 | 0.956 | 0.824 (1514) | 0.860 (1852) | 0.844 (1163) | 0.659 (18450) | 0.357 (49961) | 47.200 | 319.150 | 1.606 | 5.025 |
| careful | — | 0.667 | 0.000 (27265) | 0.000 (5849) | 0.000 (4627) | 0.000 (1174) | 0.000 (43269) | 24.250 | 690.100 | 1.112 | 0.000 |
| hand | — | 0.805 | 0.000 (113) | 0.000 (11389) | 0.000 (17707) | 0.000 (15366) | 0.000 (42653) | 33.300 | 344.900 | 1.251 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| direct | 39.850 | 0.000 | 0.000 | 0.000 | 0.000 | 0.350 | 0.000 |
| careful | 39.600 | 0.000 | 0.000 | 0.000 | 0.000 | 0.450 | 0.000 |
| hand | 39.850 | 0.000 | 0.000 | 0.000 | 0.000 | 0.650 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 15.500 / 39.850 | 88.650 ± 4.424 | +82.150 ± 4.654 | 154.200 | +144.950 ± 4.684 | 8.700 | 0.321 | 27.350 | +22.700 ± 0.765 | 1784.650 | 0.049 | +0.026 ± 0.003 | 0.000 / 0.000 (0.000 / 0.000) | 31901.832 ± 432.462 | +9380.196 ± 491.901 | 28840.5 ± 580.1 | -6652.6 ± 1184.4 | 29.419 | -9.291 ± 0.510 | 23.910 ± 0.350 | +10.263 ± 0.631 | 21.451 | 0.055 | 2124.950 | 19.850 | 24.350 | +7.250 ± 0.486 | 77.309 | 109.150 |
| careful | 22.500 / 39.600 | 6.500 ± 0.651 | — | 9.250 | — | 3.850 | 0.036 | 4.650 | — | 1593.650 | 0.023 | — | 0.000 / 0.000 (0.000 / 0.000) | 22521.636 ± 353.580 | — | 35493.1 ± 953.9 | — | 38.710 | — | 13.648 ± 0.434 | — | 16.769 | 0.000 | 2652.600 | 19.600 | 17.100 | — | 1125.419 | 201.700 |
| hand | 19.250 / 39.850 | 11.250 ± 0.537 | +4.750 ± 0.973 | 60.900 | +51.650 ± 1.899 | 6.850 | 0.044 | 13.450 | +8.800 ± 1.060 | 1654.500 | 0.059 | +0.036 ± 0.002 | 0.000 / 0.000 (0.000 / 0.000) | 30318.582 ± 421.599 | +7796.946 ± 413.233 | 31815.8 ± 548.8 | -3677.3 ± 1033.7 | 32.310 | -6.399 ± 0.371 | 21.092 ± 0.413 | +7.444 ± 0.613 | 19.846 | 0.013 | 2441.850 | 19.850 | 20.600 | +3.500 ± 0.545 | 75.737 | 150.100 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **direct**: p0 0.796/0.204/0.000 (608); p1 0.325/0.651/0.024 (555); p2 0.410/0.570/0.021 (336); p3 0.495/0.481/0.024 (246); p4 0.492/0.482/0.026 (253); p5 0.467/0.521/0.012 (250); p6 0.498/0.490/0.012 (243); p7 0.515/0.472/0.013 (232); p8 0.528/0.457/0.014 (231); p9 0.525/0.460/0.015 (230); p10 0.507/0.464/0.029 (210); p11 0.534/0.426/0.040 (144); p12 0.514/0.454/0.032 (78); p13 0.633/0.326/0.040 (31); p14 0.214/0.750/0.036 (1)
- **careful**: p0 1.000/0.000/0.000 (622); p1 1.000/0.000/0.000 (750); p2 1.000/0.000/0.000 (843); p3 1.000/0.000/0.000 (869); p4 1.000/0.000/0.000 (734); p5 1.000/0.000/0.000 (274); p6 1.000/0.000/0.000 (18)
- **hand**: p0 —/—/— (0); p1 —/—/— (0); p2 —/—/— (0); p3 —/—/— (0); p4 —/—/— (0); p5 —/—/— (0); p6 —/—/— (0); p7 —/—/— (0); p8 —/—/— (0); p9 —/—/— (0); p10 —/—/— (0); p11 —/—/— (0); p12 —/—/— (0); p13 —/—/— (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling the requester's wallet refused to raise at least once (never a plant's: its raise is minted — §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 2239.4 / 608.0 | 1.44 / 1.99 | +0.55 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.07 / 0.06 | -0.00 ± 0.00 | 0.475 / 0.584 | +0.109 ± 0.007 | 0.279 / 0.352 | 0.054 / 0.086 | 0.171 / 0.209 | +0.039 ± 0.005 | 3.48 / 3.83 | +0.36 ± 0.04 |
| careful | 2647.7 / 269.5 | 0.14 / 0.09 | -0.05 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.07 / 0.07 | +0.01 ± 0.00 | 0.118 / 0.096 | -0.023 ± 0.003 | 0.040 / 0.044 | 0.000 / 0.000 | 0.060 / 0.061 | +0.000 ± 0.003 | 1.33 / 1.18 | -0.15 ± 0.06 |
| hand | 2462.1 / 620.9 | 0.68 / 0.71 | +0.03 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.15 / 0.15 | +0.01 ± 0.00 | 0.343 / 0.345 | +0.002 ± 0.006 | 0.154 / 0.172 | 0.013 / 0.016 | 0.099 / 0.103 | +0.004 ± 0.003 | 2.45 / 2.48 | +0.03 ± 0.09 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| direct | +0.02 ± 0.02 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.050 ± 0.004 | -0.028 ± 0.004 | -0.004 ± 0.004 |
| careful | -0.05 ± 0.01 | +0.00 ± 0.00 | +0.01 ± 0.00 | -0.024 ± 0.004 | +0.004 ± 0.002 | +0.001 ± 0.002 |
| hand | -0.07 ± 0.02 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.047 ± 0.005 | -0.008 ± 0.003 | +0.002 ± 0.002 |

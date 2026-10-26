# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop half --learner-role reviewer --learner-exit rule`, seeds 21-40, hide ``, model `results/redteam/stability/learned-rev-half-2/wm/models/wm-online-5.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the plant-blind seats — a revised submission or a panel, where no plant is received — are read apart: their share of the review decisions and the stamp rate on them.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | blind-seat share | blind-seat stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 16180.2 ± 407.9 | -3148.1 ± 855.5 | 2134.2 | 0.727 | 0.273 | 0.000 | 0.074 | 0.086 | 0.278 | 0.770 | 23.70 | 36.70 | 0.10 |
| careful | 19328.3 ± 736.1 | nan ± nan | 2499.2 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.295 | 0.000 | 8.95 | 0.00 | 0.35 |
| stamper | 3903.7 ± 144.4 | -15424.6 ± 762.0 | 518.5 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.023 | 1.000 | 15.00 | 87.25 | 1.00 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 0.781 | 0.849 | 1.000 (5) | 0.433 (2122) | 0.316 (9675) | 0.356 (10341) | 0.197 (20540) | 19.550 | 150.250 | 2.642 | 1.877 |
| careful | — | 0.735 | 0.000 (2042) | 0.000 (12029) | 0.000 (8320) | 0.000 (6503) | 0.000 (21089) | 12.800 | 221.050 | 2.156 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (10369) | 34.150 | 101.250 | 3.805 | 2.555 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| greedy | 20.350 | 0.000 | 0.000 | 0.000 | 0.000 | 0.100 | 0.000 |
| careful | 20.300 | 0.000 | 0.000 | 0.000 | 0.000 | 0.350 | 0.000 |
| stamper | 20.400 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 9.450 / 20.350 | 23.700 ± 1.401 | +14.750 ± 1.581 | 62.600 | +26.450 ± 2.300 | 7.600 | 0.098 | 17.050 | +8.600 ± 1.014 | 1660.800 | 0.040 | -0.004 ± 0.002 | 16376.105 ± 464.887 | +110.207 ± 502.832 | 16180.2 ± 407.9 | -3148.1 ± 855.5 | 31.711 | -3.510 ± 0.563 | 21.900 ± 0.426 | +3.207 ± 0.893 | 20.273 | 0.009 | 2412.600 | 19.850 | 21.150 | +1.550 ± 0.400 | 63.628 | 151.150 |
| careful | 12.100 / 20.300 | 8.950 ± 0.686 | — | 36.150 | — | 7.700 | 0.046 | 8.450 | — | 1565.700 | 0.044 | — | 16265.899 ± 638.614 | — | 19328.3 ± 736.1 | — | 35.221 | — | 18.694 ± 0.823 | — | 18.362 | 0.005 | 2566.500 | 19.800 | 19.600 | — | 524.255 | 200.550 |
| stamper | 0.000 / 20.400 | 15.000 ± 1.039 | +6.050 ± 1.221 | 93.300 | +57.150 ± 2.321 | 6.000 | 0.061 | 31.900 | +23.450 ± 1.017 | 1542.700 | 0.092 | +0.048 ± 0.003 | 3489.421 ± 146.045 | -12776.478 ± 609.566 | 3903.7 ± 144.4 | -15424.6 ± 762.0 | 28.031 | -7.190 ± 0.545 | 28.627 ± 0.309 | +9.933 ± 0.842 | 23.865 | 0.261 | 1597.600 | 19.950 | 28.450 | +8.850 ± 0.504 | 91.373 | 166.200 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **greedy**: p0 0.877/0.123/0.000 (288); p1 0.654/0.346/0.000 (190); p2 0.657/0.343/0.000 (116); p3 0.681/0.319/0.000 (146); p4 0.708/0.292/0.000 (139); p5 0.706/0.294/0.000 (147); p6 0.732/0.268/0.000 (150); p7 0.728/0.271/0.000 (155); p8 0.792/0.208/0.000 (167); p9 0.710/0.290/0.000 (164); p10 0.725/0.275/0.000 (165); p11 0.654/0.346/0.000 (159); p12 0.675/0.325/0.000 (112); p13 0.653/0.347/0.000 (37); p14 1.000/0.000/0.000 (0)
- **careful**: p0 1.000/0.000/0.000 (304); p1 1.000/0.000/0.000 (217); p2 1.000/0.000/0.000 (181); p3 1.000/0.000/0.000 (211); p4 1.000/0.000/0.000 (210); p5 1.000/0.000/0.000 (212); p6 1.000/0.000/0.000 (225); p7 1.000/0.000/0.000 (197); p8 1.000/0.000/0.000 (205); p9 1.000/0.000/0.000 (188); p10 1.000/0.000/0.000 (180); p11 1.000/0.000/0.000 (130); p12 1.000/0.000/0.000 (37); p13 1.000/0.000/0.000 (3)
- **stamper**: p0 0.000/1.000/0.000 (293); p1 0.000/1.000/0.000 (143); p2 0.000/1.000/0.000 (55); p3 0.000/1.000/0.000 (21); p4 0.000/1.000/0.000 (3); p5 0.000/1.000/0.000 (1); p6 0.000/1.000/0.000 (0); p7 0.000/1.000/0.000 (0); p8 0.000/1.000/0.000 (1)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 2418.3 / 647.8 | 0.85 / 0.78 | -0.07 ± 0.04 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.14 / 0.17 | +0.03 ± 0.00 | 0.404 / 0.432 | +0.028 ± 0.006 | 0.008 / 0.009 | 0.064 / 0.062 | -0.003 ± 0.003 | 2.67 / 2.57 | -0.10 ± 0.08 |
| careful | 2572.1 / 548.2 | 0.34 / 0.21 | -0.13 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.13 / 0.14 | +0.01 ± 0.00 | 0.179 / 0.190 | +0.011 ± 0.005 | 0.005 / 0.004 | 0.044 / 0.041 | -0.003 ± 0.002 | 1.85 / 1.56 | -0.29 ± 0.10 |
| stamper | 2120.0 / 546.5 | 1.99 / 1.86 | -0.12 ± 0.06 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.13 / 0.20 | +0.07 ± 0.01 | 0.543 / 0.605 | +0.062 ± 0.005 | 0.256 / 0.376 | 0.023 / 0.015 | -0.008 ± 0.002 | 2.95 / 2.41 | -0.54 ± 0.27 |

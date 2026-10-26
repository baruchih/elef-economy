# Evaluation — cell `--entry-pool 20 --stampers 0.6 --dispute-policy truthful --learner-pop all --learner-role reviewer --learner-exit rule`, seeds 21-40, hide ``, model `None` (value off, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the plant-blind seats — a revised submission or a panel, where no plant is received — are read apart: their share of the review decisions and the stamp rate on them.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | blind-seat share | blind-seat stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 30507.2 ± 660.3 | -4179.1 ± 1145.3 | 4209.4 | 0.515 | 0.470 | 0.015 | 0.228 | 0.331 | 0.292 | 0.907 | 50.75 | 279.85 | 0.15 |
| careful | 34686.3 ± 943.9 | nan ± nan | 4064.8 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.283 | 0.000 | 0.50 | 0.00 | 0.25 |
| stamper | 7060.1 ± 175.9 | -27626.2 ± 969.6 | 1033.5 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.027 | 1.000 | 8.90 | 180.65 | 1.00 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 0.877 | 0.953 | 0.879 (1362) | 0.778 (1803) | 0.714 (685) | 0.633 (22360) | 0.384 (57979) | 40.800 | 352.400 | 1.413 | 6.859 |
| careful | — | 0.687 | 0.000 (25012) | 0.000 (5498) | 0.000 (4685) | 0.000 (1032) | 0.000 (45068) | 25.350 | 702.200 | 1.153 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (20671) | 69.050 | 189.900 | 1.963 | 2.616 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| direct | 39.850 | 0.000 | 0.000 | 0.000 | 0.000 | 0.150 | 0.000 |
| careful | 39.650 | 0.000 | 0.000 | 0.000 | 0.000 | 0.250 | 0.000 |
| stamper | 39.900 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 17.900 / 39.850 | 50.750 ± 2.510 | +50.250 ± 2.515 | 121.500 | +110.400 ± 4.700 | 8.550 | 0.233 | 20.950 | +15.250 ± 1.172 | 1715.700 | 0.007 | -0.006 ± 0.001 | 32533.749 ± 427.571 | +9836.965 ± 527.020 | 30507.2 ± 660.3 | -4179.1 ± 1145.3 | 30.691 | -7.047 ± 0.510 | 23.076 ± 0.546 | +9.080 ± 0.825 | 21.280 | 0.010 | 2339.950 | 19.850 | 21.950 | +4.950 ± 0.550 | 68.102 | 133.450 |
| careful | 22.650 / 39.650 | 0.500 ± 0.136 | — | 11.100 | — | 3.400 | 0.057 | 5.700 | — | 1603.650 | 0.013 | — | 22696.783 ± 320.852 | — | 34686.3 ± 943.9 | — | 37.739 | — | 13.996 ± 0.428 | — | 17.483 | 0.000 | 2651.850 | 19.650 | 17.000 | — | 949.702 | 203.800 |
| stamper | 4.200 / 39.900 | 8.900 ± 0.801 | +8.400 ± 0.809 | 107.000 | +95.900 ± 1.624 | 0.000 | 1.000 | 49.150 | +43.450 ± 1.354 | 695.450 | 0.015 | +0.003 ± 0.001 | 8299.708 ± 190.343 | -14397.076 ± 322.265 | 7060.1 ± 175.9 | -27626.2 ± 969.6 | 27.923 | -9.816 ± 0.449 | 30.178 ± 0.809 | +16.182 ± 1.001 | 22.365 | 0.181 | 738.650 | 19.900 | 35.700 | +18.700 ± 0.629 | 6025.482 | 147.550 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **direct**: p0 0.848/0.151/0.002 (592); p1 0.485/0.496/0.018 (615); p2 0.466/0.500/0.034 (374); p3 0.526/0.456/0.018 (283); p4 0.481/0.503/0.016 (282); p5 0.434/0.546/0.020 (287); p6 0.423/0.563/0.015 (283); p7 0.444/0.543/0.013 (285); p8 0.415/0.571/0.014 (279); p9 0.441/0.547/0.012 (270); p10 0.431/0.554/0.015 (264); p11 0.480/0.510/0.010 (187); p12 0.475/0.517/0.009 (116); p13 0.525/0.468/0.008 (65); p14 0.472/0.518/0.010 (26); p15 0.526/0.474/0.000 (1)
- **careful**: p0 1.000/0.000/0.000 (603); p1 1.000/0.000/0.000 (719); p2 1.000/0.000/0.000 (833); p3 1.000/0.000/0.000 (871); p4 1.000/0.000/0.000 (774); p5 1.000/0.000/0.000 (265)
- **stamper**: p0 0.000/1.000/0.000 (580); p1 0.000/1.000/0.000 (302); p2 0.000/1.000/0.000 (144); p3 0.000/1.000/0.000 (7); p4 0.000/1.000/0.000 (1)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 2353.6 / 625.2 | 1.10 / 0.55 | -0.55 ± 0.05 | 1.00 / 1.08 | +0.08 ± 0.00 | 0.06 / 0.10 | +0.04 ± 0.01 | 0.434 / 0.515 | +0.081 ± 0.013 | 0.009 / 0.314 | 0.131 / 0.095 | -0.036 ± 0.005 | 3.00 / 1.85 | -1.15 ± 0.12 |
| careful | 2646.2 / 266.6 | 0.20 / 0.06 | -0.14 ± 0.03 | 1.00 / 1.19 | +0.19 ± 0.00 | 0.07 / 0.07 | +0.01 ± 0.00 | 0.144 / 0.134 | -0.009 ± 0.004 | 0.000 / 0.025 | 0.062 / 0.068 | +0.007 ± 0.003 | 1.48 / 1.47 | -0.01 ± 0.08 |
| stamper | 863.0 / 142.2 | 1.08 / 0.48 | -0.60 ± 0.05 | 1.00 / 1.35 | +0.35 ± 0.01 | 0.03 / 0.28 | +0.25 ± 0.03 | 0.241 / 0.249 | +0.008 ± 0.008 | 0.144 / 0.321 | 0.110 / 0.080 | -0.030 ± 0.006 | 3.44 / 1.85 | -1.59 ± 0.14 |

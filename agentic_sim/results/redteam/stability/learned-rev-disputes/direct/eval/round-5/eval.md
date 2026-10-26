# Evaluation — cell `--entry-pool 20 --stampers 0.6 --dispute-policy truthful --learner-pop all --learner-role reviewer --learner-exit rule`, seeds 21-40, hide ``, model `None` (value off, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the plant-blind seats — a revised submission or a panel, where no plant is received — are read apart: their share of the review decisions and the stamp rate on them.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | blind-seat share | blind-seat stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 31939.7 ± 745.3 | -2746.6 ± 694.9 | 4324.4 | 0.540 | 0.443 | 0.017 | 0.221 | 0.315 | 0.300 | 0.845 | 40.15 | 260.90 | 0.00 |
| careful | 34686.3 ± 943.9 | nan ± nan | 4064.8 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.283 | 0.000 | 0.50 | 0.00 | 0.25 |
| stamper | 7060.1 ± 175.9 | -27626.2 ± 969.6 | 1033.5 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.027 | 1.000 | 8.90 | 180.65 | 1.00 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 0.869 | 0.945 | 0.795 (1980) | 0.741 (1447) | 0.676 (1343) | 0.594 (23099) | 0.359 (58619) | 40.800 | 359.700 | 1.390 | 6.395 |
| careful | — | 0.687 | 0.000 (25012) | 0.000 (5498) | 0.000 (4685) | 0.000 (1032) | 0.000 (45068) | 25.350 | 702.200 | 1.153 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (20671) | 69.050 | 189.900 | 1.963 | 2.616 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| direct | 39.950 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| careful | 39.650 | 0.000 | 0.000 | 0.000 | 0.000 | 0.250 | 0.000 |
| stamper | 39.900 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 18.700 / 39.950 | 40.150 ± 2.275 | +39.650 ± 2.338 | 118.150 | +107.050 ± 3.416 | 7.300 | 0.272 | 20.850 | +15.150 ± 0.907 | 1737.900 | 0.007 | -0.006 ± 0.001 | 32297.402 ± 501.251 | +9600.618 ± 518.450 | 31939.7 ± 745.3 | -2746.6 ± 694.9 | 31.123 | -6.616 ± 0.482 | 21.720 ± 0.474 | +7.724 ± 0.541 | 21.015 | 0.004 | 2389.050 | 19.950 | 21.250 | +4.250 ± 0.435 | 62.622 | 152.650 |
| careful | 22.650 / 39.650 | 0.500 ± 0.136 | — | 11.100 | — | 3.400 | 0.057 | 5.700 | — | 1603.650 | 0.013 | — | 22696.783 ± 320.852 | — | 34686.3 ± 943.9 | — | 37.739 | — | 13.996 ± 0.428 | — | 17.483 | 0.000 | 2651.850 | 19.650 | 17.000 | — | 949.702 | 203.800 |
| stamper | 4.200 / 39.900 | 8.900 ± 0.801 | +8.400 ± 0.809 | 107.000 | +95.900 ± 1.624 | 0.000 | 1.000 | 49.150 | +43.450 ± 1.354 | 695.450 | 0.015 | +0.003 ± 0.001 | 8299.708 ± 190.343 | -14397.076 ± 322.265 | 7060.1 ± 175.9 | -27626.2 ± 969.6 | 27.923 | -9.816 ± 0.449 | 30.178 ± 0.809 | +16.182 ± 1.001 | 22.365 | 0.181 | 738.650 | 19.900 | 35.700 | +18.700 ± 0.629 | 6025.482 | 147.550 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **direct**: p0 0.819/0.176/0.004 (618); p1 0.451/0.529/0.020 (628); p2 0.516/0.456/0.028 (360); p3 0.552/0.429/0.018 (276); p4 0.516/0.469/0.015 (280); p5 0.467/0.505/0.028 (284); p6 0.468/0.510/0.022 (283); p7 0.458/0.520/0.022 (287); p8 0.470/0.512/0.018 (278); p9 0.494/0.492/0.014 (277); p10 0.512/0.477/0.011 (266); p11 0.532/0.457/0.011 (230); p12 0.541/0.451/0.008 (126); p13 0.557/0.434/0.009 (82); p14 0.498/0.493/0.008 (42); p15 0.658/0.332/0.011 (9)
- **careful**: p0 1.000/0.000/0.000 (603); p1 1.000/0.000/0.000 (719); p2 1.000/0.000/0.000 (833); p3 1.000/0.000/0.000 (871); p4 1.000/0.000/0.000 (774); p5 1.000/0.000/0.000 (265)
- **stamper**: p0 0.000/1.000/0.000 (580); p1 0.000/1.000/0.000 (302); p2 0.000/1.000/0.000 (144); p3 0.000/1.000/0.000 (7); p4 0.000/1.000/0.000 (1)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 2389.0 / 638.8 | 0.92 / 0.49 | -0.42 ± 0.06 | 1.00 / 1.08 | +0.08 ± 0.00 | 0.06 / 0.09 | +0.03 ± 0.01 | 0.433 / 0.529 | +0.095 ± 0.009 | 0.003 / 0.249 | 0.118 / 0.094 | -0.024 ± 0.004 | 2.63 / 1.78 | -0.85 ± 0.11 |
| careful | 2646.2 / 266.6 | 0.20 / 0.06 | -0.14 ± 0.03 | 1.00 / 1.19 | +0.19 ± 0.00 | 0.07 / 0.07 | +0.01 ± 0.00 | 0.144 / 0.134 | -0.009 ± 0.004 | 0.000 / 0.025 | 0.062 / 0.068 | +0.007 ± 0.003 | 1.48 / 1.47 | -0.01 ± 0.08 |
| stamper | 863.0 / 142.2 | 1.08 / 0.48 | -0.60 ± 0.05 | 1.00 / 1.35 | +0.35 ± 0.01 | 0.03 / 0.28 | +0.25 ± 0.03 | 0.241 / 0.249 | +0.008 ± 0.008 | 0.144 / 0.321 | 0.110 / 0.080 | -0.030 ± 0.006 | 3.44 / 1.85 | -1.59 ± 0.14 |

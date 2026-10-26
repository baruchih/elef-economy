# Evaluation — cell `--entry-pool 20 --stampers 0.6 --dispute-policy truthful --learner-pop all --learner-role reviewer --learner-exit rule`, seeds 21-40, hide ``, model `results/redteam/stability/learned-rev-disputes/wm/models/wm-online-10.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the plant-blind seats — a revised submission or a panel, where no plant is received — are read apart: their share of the review decisions and the stamp rate on them.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | blind-seat share | blind-seat stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 29905.7 ± 828.7 | -4780.7 ± 1118.4 | 4070.6 | 0.527 | 0.471 | 0.002 | 0.210 | 0.307 | 0.294 | 0.923 | 64.30 | 296.10 | 0.20 |
| careful | 34686.3 ± 943.9 | nan ± nan | 4064.8 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.283 | 0.000 | 0.50 | 0.00 | 0.25 |
| stamper | 7060.1 ± 175.9 | -27626.2 ± 969.6 | 1033.5 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.027 | 1.000 | 8.90 | 180.65 | 1.00 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 0.850 | 0.934 | 0.894 (1747) | 0.858 (1791) | 0.677 (1601) | 0.583 (26557) | 0.377 (49716) | 45.400 | 335.450 | 1.447 | 6.522 |
| careful | — | 0.687 | 0.000 (25012) | 0.000 (5498) | 0.000 (4685) | 0.000 (1032) | 0.000 (45068) | 25.350 | 702.200 | 1.153 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (20671) | 69.050 | 189.900 | 1.963 | 2.616 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| greedy | 39.700 | 0.000 | 0.000 | 0.000 | 0.000 | 0.200 | 0.000 |
| careful | 39.650 | 0.000 | 0.000 | 0.000 | 0.000 | 0.250 | 0.000 |
| stamper | 39.900 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 16.400 / 39.700 | 64.300 ± 3.379 | +63.800 ± 3.393 | 112.050 | +100.950 ± 5.723 | 4.700 | 0.170 | 25.700 | +20.000 ± 1.203 | 1654.550 | 0.007 | -0.006 ± 0.001 | 33552.446 ± 475.099 | +10855.663 ± 513.682 | 29905.7 ± 828.7 | -4780.7 ± 1118.4 | 29.819 | -7.919 ± 0.536 | 24.320 ± 0.700 | +10.324 ± 0.710 | 21.921 | 0.029 | 2225.700 | 19.700 | 23.300 | +6.300 ± 0.539 | 69.372 | 128.150 |
| careful | 22.650 / 39.650 | 0.500 ± 0.136 | — | 11.100 | — | 3.400 | 0.057 | 5.700 | — | 1603.650 | 0.013 | — | 22696.783 ± 320.852 | — | 34686.3 ± 943.9 | — | 37.739 | — | 13.996 ± 0.428 | — | 17.483 | 0.000 | 2651.850 | 19.650 | 17.000 | — | 949.702 | 203.800 |
| stamper | 4.200 / 39.900 | 8.900 ± 0.801 | +8.400 ± 0.809 | 107.000 | +95.900 ± 1.624 | 0.000 | 1.000 | 49.150 | +43.450 ± 1.354 | 695.450 | 0.015 | +0.003 ± 0.001 | 8299.708 ± 190.343 | -14397.076 ± 322.265 | 7060.1 ± 175.9 | -27626.2 ± 969.6 | 27.923 | -9.816 ± 0.449 | 30.178 ± 0.809 | +16.182 ± 1.001 | 22.365 | 0.181 | 738.650 | 19.900 | 35.700 | +18.700 ± 0.629 | 6025.482 | 147.550 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **greedy**: p0 0.818/0.182/0.000 (619); p1 0.409/0.584/0.007 (640); p2 0.429/0.571/0.001 (386); p3 0.500/0.499/0.000 (272); p4 0.420/0.580/0.001 (283); p5 0.525/0.474/0.001 (276); p6 0.494/0.505/0.001 (278); p7 0.502/0.496/0.002 (273); p8 0.510/0.489/0.001 (269); p9 0.493/0.506/0.002 (277); p10 0.526/0.474/0.001 (220); p11 0.510/0.488/0.002 (108); p12 0.527/0.471/0.002 (63); p13 0.511/0.481/0.008 (54); p14 0.587/0.411/0.003 (40); p15 0.491/0.509/0.000 (11)
- **careful**: p0 1.000/0.000/0.000 (603); p1 1.000/0.000/0.000 (719); p2 1.000/0.000/0.000 (833); p3 1.000/0.000/0.000 (871); p4 1.000/0.000/0.000 (774); p5 1.000/0.000/0.000 (265)
- **stamper**: p0 0.000/1.000/0.000 (580); p1 0.000/1.000/0.000 (302); p2 0.000/1.000/0.000 (144); p3 0.000/1.000/0.000 (7); p4 0.000/1.000/0.000 (1)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 2279.3 / 593.6 | 1.41 / 0.66 | -0.75 ± 0.10 | 1.00 / 1.09 | +0.09 ± 0.00 | 0.06 / 0.12 | +0.06 ± 0.01 | 0.448 / 0.558 | +0.111 ± 0.010 | 0.028 / 0.437 | 0.163 / 0.111 | -0.053 ± 0.009 | 3.50 / 2.00 | -1.51 ± 0.17 |
| careful | 2646.2 / 266.6 | 0.20 / 0.06 | -0.14 ± 0.03 | 1.00 / 1.19 | +0.19 ± 0.00 | 0.07 / 0.07 | +0.01 ± 0.00 | 0.144 / 0.134 | -0.009 ± 0.004 | 0.000 / 0.025 | 0.062 / 0.068 | +0.007 ± 0.003 | 1.48 / 1.47 | -0.01 ± 0.08 |
| stamper | 863.0 / 142.2 | 1.08 / 0.48 | -0.60 ± 0.05 | 1.00 / 1.35 | +0.35 ± 0.01 | 0.03 / 0.28 | +0.25 ± 0.03 | 0.241 / 0.249 | +0.008 ± 0.008 | 0.144 / 0.321 | 0.110 / 0.080 | -0.030 ± 0.006 | 3.44 / 1.85 | -1.59 ± 0.14 |

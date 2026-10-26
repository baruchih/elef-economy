# Evaluation — cell `--entry-pool 20 --stampers 0.6 --dispute-policy truthful --learner-pop all --learner-role reviewer --learner-exit rule`, seeds 21-40, hide ``, model `results/redteam/stability/learned-rev-disputes-2/wm/models/wm-online-5.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the plant-blind seats — a revised submission or a panel, where no plant is received — are read apart: their share of the review decisions and the stamp rate on them.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | blind-seat share | blind-seat stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 31214.5 ± 537.4 | -2230.0 ± 907.4 | 4192.2 | 0.546 | 0.454 | 0.001 | 0.223 | 0.241 | 0.299 | 0.965 | 60.70 | 244.45 | 0.15 |
| careful | 33444.4 ± 894.0 | nan ± nan | 4101.7 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.285 | 0.000 | 0.40 | 0.00 | 0.25 |
| stamper | 7125.9 ± 112.8 | -26318.5 ± 968.0 | 1053.0 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.027 | 1.000 | 8.15 | 186.30 | 1.00 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 0.846 | 0.926 | 0.902 (692) | 0.925 (1470) | 0.790 (1865) | 0.554 (34176) | 0.344 (45642) | 43.350 | 292.950 | 1.436 | 5.639 |
| careful | — | 0.687 | 0.000 (24146) | 0.000 (6755) | 0.000 (4661) | 0.000 (1443) | 0.000 (45029) | 24.950 | 696.200 | 1.133 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (21060) | 72.100 | 199.700 | 1.874 | 2.584 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| greedy | 39.800 | 0.000 | 0.000 | 0.000 | 0.000 | 0.150 | 0.000 |
| careful | 39.700 | 0.000 | 0.000 | 0.000 | 0.000 | 0.250 | 0.000 |
| stamper | 39.900 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 16.850 / 39.800 | 60.700 ± 3.608 | +60.300 ± 3.639 | 123.500 | +112.850 ± 3.070 | 6.350 | 0.276 | 23.550 | +18.300 ± 0.968 | 1631.050 | 0.005 | -0.008 ± 0.001 | 33883.074 ± 475.927 | +11457.614 ± 559.582 | 31214.5 ± 537.4 | -2230.0 ± 907.4 | 30.031 | -8.050 ± 0.420 | 23.310 ± 0.276 | +8.950 ± 0.420 | 21.591 | 0.022 | 2259.300 | 19.800 | 22.950 | +6.050 ± 0.540 | 70.644 | 147.750 |
| careful | 22.800 / 39.700 | 0.400 ± 0.134 | — | 10.650 | — | 3.700 | 0.048 | 5.250 | — | 1598.100 | 0.013 | — | 22425.460 ± 528.637 | — | 33444.4 ± 894.0 | — | 38.081 | — | 14.360 ± 0.339 | — | 17.273 | 0.001 | 2660.500 | 19.700 | 16.900 | — | 985.796 | 198.850 |
| stamper | 5.500 / 39.900 | 8.150 ± 0.612 | +7.750 ± 0.619 | 109.750 | +99.100 ± 2.159 | 0.000 | 1.000 | 52.200 | +46.950 ± 1.751 | 704.200 | 0.016 | +0.003 ± 0.001 | 8280.104 ± 185.330 | -14145.356 ± 564.796 | 7125.9 ± 112.8 | -26318.5 ± 968.0 | 27.799 | -10.282 ± 0.500 | 29.430 ± 0.708 | +15.069 ± 0.889 | 22.363 | 0.202 | 730.600 | 19.900 | 34.400 | +17.500 ± 0.872 | 5961.570 | 192.700 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **greedy**: p0 0.800/0.199/0.000 (598); p1 0.410/0.588/0.002 (529); p2 0.557/0.442/0.001 (330); p3 0.502/0.496/0.002 (314); p4 0.491/0.509/0.000 (287); p5 0.509/0.490/0.001 (281); p6 0.521/0.479/0.000 (276); p7 0.517/0.482/0.001 (276); p8 0.528/0.472/0.000 (276); p9 0.528/0.472/0.000 (270); p10 0.514/0.485/0.001 (273); p11 0.532/0.468/0.000 (231); p12 0.483/0.516/0.000 (163); p13 0.526/0.474/0.000 (71); p14 0.548/0.452/0.000 (17)
- **careful**: p0 1.000/0.000/0.000 (599); p1 1.000/0.000/0.000 (731); p2 1.000/0.000/0.000 (840); p3 1.000/0.000/0.000 (866); p4 1.000/0.000/0.000 (743); p5 1.000/0.000/0.000 (280); p6 1.000/0.000/0.000 (43)
- **stamper**: p0 0.000/1.000/0.000 (580); p1 0.000/1.000/0.000 (306); p2 0.000/1.000/0.000 (150); p3 0.000/1.000/0.000 (8); p4 0.000/1.000/0.000 (7); p5 0.000/1.000/0.000 (3)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 2295.6 / 643.0 | 1.34 / 1.60 | +0.25 ± 0.04 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.10 / 0.12 | +0.02 ± 0.00 | 0.491 / 0.584 | +0.093 ± 0.008 | 0.021 / 0.036 | 0.167 / 0.197 | +0.029 ± 0.005 | 3.17 / 3.41 | +0.24 ± 0.05 |
| careful | 2657.3 / 273.4 | 0.17 / 0.08 | -0.09 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.07 / 0.08 | +0.01 ± 0.00 | 0.130 / 0.126 | -0.004 ± 0.004 | 0.001 / 0.001 | 0.061 / 0.067 | +0.006 ± 0.003 | 1.41 / 1.25 | -0.16 ± 0.09 |
| stamper | 876.6 / 147.8 | 1.10 / 0.56 | -0.53 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.02 / 0.24 | +0.21 ± 0.03 | 0.255 / 0.236 | -0.019 ± 0.009 | 0.166 / 0.264 | 0.112 / 0.081 | -0.031 ± 0.006 | 3.35 / 1.94 | -1.40 ± 0.15 |

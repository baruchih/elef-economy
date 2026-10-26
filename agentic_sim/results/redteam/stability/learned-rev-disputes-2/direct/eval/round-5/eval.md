# Evaluation — cell `--entry-pool 20 --stampers 0.6 --dispute-policy truthful --learner-pop all --learner-role reviewer --learner-exit rule`, seeds 21-40, hide ``, model `None` (value off, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the plant-blind seats — a revised submission or a panel, where no plant is received — are read apart: their share of the review decisions and the stamp rate on them.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | blind-seat share | blind-seat stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 32250.2 ± 658.8 | -1194.3 ± 763.2 | 4354.9 | 0.563 | 0.412 | 0.026 | 0.256 | 0.289 | 0.294 | 0.814 | 32.15 | 219.35 | 0.25 |
| careful | 33444.4 ± 894.0 | nan ± nan | 4101.7 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.285 | 0.000 | 0.40 | 0.00 | 0.25 |
| stamper | 7125.9 ± 112.8 | -26318.5 ± 968.0 | 1053.0 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.027 | 1.000 | 8.15 | 186.30 | 1.00 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 0.879 | 0.952 | 0.648 (1303) | 0.770 (1530) | 0.673 (1107) | 0.607 (21569) | 0.326 (61590) | 38.750 | 353.500 | 1.358 | 5.661 |
| careful | — | 0.687 | 0.000 (24146) | 0.000 (6755) | 0.000 (4661) | 0.000 (1443) | 0.000 (45029) | 24.950 | 696.200 | 1.133 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (21060) | 72.100 | 199.700 | 1.874 | 2.584 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| direct | 39.800 | 0.000 | 0.000 | 0.000 | 0.000 | 0.250 | 0.000 |
| careful | 39.700 | 0.000 | 0.000 | 0.000 | 0.000 | 0.250 | 0.000 |
| stamper | 39.900 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 19.000 / 39.800 | 32.150 ± 1.929 | +31.750 ± 1.952 | 131.300 | +120.650 ± 3.047 | 11.600 | 0.299 | 18.950 | +13.700 ± 0.673 | 1744.450 | 0.007 | -0.006 ± 0.001 | 31533.038 ± 325.455 | +9107.578 ± 431.102 | 32250.2 ± 658.8 | -1194.3 ± 763.2 | 31.699 | -6.382 ± 0.433 | 21.082 ± 0.416 | +6.722 ± 0.453 | 20.525 | 0.007 | 2409.300 | 19.800 | 20.800 | +3.900 ± 0.507 | 63.309 | 164.050 |
| careful | 22.800 / 39.700 | 0.400 ± 0.134 | — | 10.650 | — | 3.700 | 0.048 | 5.250 | — | 1598.100 | 0.013 | — | 22425.460 ± 528.637 | — | 33444.4 ± 894.0 | — | 38.081 | — | 14.360 ± 0.339 | — | 17.273 | 0.001 | 2660.500 | 19.700 | 16.900 | — | 985.796 | 198.850 |
| stamper | 5.500 / 39.900 | 8.150 ± 0.612 | +7.750 ± 0.619 | 109.750 | +99.100 ± 2.159 | 0.000 | 1.000 | 52.200 | +46.950 ± 1.751 | 704.200 | 0.016 | +0.003 ± 0.001 | 8280.104 ± 185.330 | -14145.356 ± 564.796 | 7125.9 ± 112.8 | -26318.5 ± 968.0 | 27.799 | -10.282 ± 0.500 | 29.430 ± 0.708 | +15.069 ± 0.889 | 22.363 | 0.202 | 730.600 | 19.900 | 34.400 | +17.500 ± 0.872 | 5961.570 | 192.700 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **direct**: p0 0.834/0.159/0.007 (599); p1 0.562/0.403/0.035 (585); p2 0.504/0.453/0.043 (406); p3 0.528/0.425/0.047 (287); p4 0.478/0.481/0.042 (280); p5 0.507/0.461/0.032 (282); p6 0.510/0.462/0.028 (275); p7 0.533/0.447/0.020 (272); p8 0.489/0.491/0.020 (271); p9 0.507/0.472/0.020 (270); p10 0.509/0.474/0.017 (272); p11 0.523/0.464/0.013 (242); p12 0.544/0.443/0.013 (160); p13 0.500/0.489/0.011 (102); p14 0.498/0.495/0.007 (42); p15 0.707/0.282/0.011 (9)
- **careful**: p0 1.000/0.000/0.000 (599); p1 1.000/0.000/0.000 (731); p2 1.000/0.000/0.000 (840); p3 1.000/0.000/0.000 (866); p4 1.000/0.000/0.000 (743); p5 1.000/0.000/0.000 (280); p6 1.000/0.000/0.000 (43)
- **stamper**: p0 0.000/1.000/0.000 (580); p1 0.000/1.000/0.000 (306); p2 0.000/1.000/0.000 (150); p3 0.000/1.000/0.000 (8); p4 0.000/1.000/0.000 (7); p5 0.000/1.000/0.000 (3)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 2419.8 / 655.6 | 0.83 / 0.91 | +0.08 ± 0.04 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.08 / 0.09 | +0.01 ± 0.00 | 0.414 / 0.495 | +0.081 ± 0.009 | 0.007 / 0.011 | 0.113 / 0.119 | +0.007 ± 0.004 | 2.53 / 2.53 | +0.01 ± 0.06 |
| careful | 2657.3 / 273.4 | 0.17 / 0.08 | -0.09 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.07 / 0.08 | +0.01 ± 0.00 | 0.130 / 0.126 | -0.004 ± 0.004 | 0.001 / 0.001 | 0.061 / 0.067 | +0.006 ± 0.003 | 1.41 / 1.25 | -0.16 ± 0.09 |
| stamper | 876.6 / 147.8 | 1.10 / 0.56 | -0.53 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.02 / 0.24 | +0.21 ± 0.03 | 0.255 / 0.236 | -0.019 ± 0.009 | 0.166 / 0.264 | 0.112 / 0.081 | -0.031 ± 0.006 | 3.35 / 1.94 | -1.40 ± 0.15 |

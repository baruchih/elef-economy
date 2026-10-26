# Evaluation — cell `--entry-pool 20 --stampers 0.6 --dispute-policy truthful --learner-pop all --learner-role reviewer --learner-exit rule`, seeds 21-40, hide ``, model `None` (value off, horizon 8)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the plant-blind seats — a revised submission or a panel, where no plant is received — are read apart: their share of the review decisions and the stamp rate on them.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | blind-seat share | blind-seat stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 31112.1 ± 839.8 | -2332.3 ± 1342.1 | 4267.9 | 0.530 | 0.456 | 0.014 | 0.282 | 0.303 | 0.283 | 0.906 | 42.55 | 252.40 | 0.15 |
| careful | 33444.4 ± 894.0 | nan ± nan | 4101.7 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.285 | 0.000 | 0.40 | 0.00 | 0.25 |
| stamper | 7125.9 ± 112.8 | -26318.5 ± 968.0 | 1053.0 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.027 | 1.000 | 8.15 | 186.30 | 1.00 |
| hand | 32105.8 ± 614.4 | -1338.6 ± 964.9 | 4304.7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.284 | 0.000 | 3.55 | 0.00 | 0.45 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 0.884 | 0.957 | 0.850 (1203) | 0.765 (1691) | 0.724 (1214) | 0.643 (20590) | 0.371 (60661) | 39.250 | 340.950 | 1.322 | 6.431 |
| careful | — | 0.687 | 0.000 (24146) | 0.000 (6755) | 0.000 (4661) | 0.000 (1443) | 0.000 (45029) | 24.950 | 696.200 | 1.133 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (21060) | 72.100 | 199.700 | 1.874 | 2.584 |
| hand | — | 0.807 | 0.000 (75) | 0.000 (12084) | 0.000 (16204) | 0.000 (14686) | 0.000 (43045) | 35.850 | 354.500 | 1.322 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| direct | 39.700 | 0.000 | 0.000 | 0.000 | 0.000 | 0.150 | 0.000 |
| careful | 39.700 | 0.000 | 0.000 | 0.000 | 0.000 | 0.250 | 0.000 |
| stamper | 39.900 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| hand | 39.850 | 0.000 | 0.000 | 0.000 | 0.000 | 0.450 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 18.500 / 39.700 | 42.550 ± 2.111 | +42.150 ± 2.150 | 154.550 | +143.900 ± 3.253 | 9.000 | 0.309 | 19.550 | +14.300 ± 1.201 | 1762.750 | 0.007 | -0.006 ± 0.001 | 31628.401 ± 532.754 | +9202.941 ± 643.707 | 31112.1 ± 839.8 | -2332.3 ± 1342.1 | 31.399 | -6.682 ± 0.418 | 21.977 ± 0.509 | +7.616 ± 0.714 | 20.607 | 0.011 | 2378.600 | 19.700 | 21.200 | +4.300 ± 0.696 | 64.737 | 107.000 |
| careful | 22.800 / 39.700 | 0.400 ± 0.134 | — | 10.650 | — | 3.700 | 0.048 | 5.250 | — | 1598.100 | 0.013 | — | 22425.460 ± 528.637 | — | 33444.4 ± 894.0 | — | 38.081 | — | 14.360 ± 0.339 | — | 17.273 | 0.001 | 2660.500 | 19.700 | 16.900 | — | 985.796 | 198.850 |
| stamper | 5.500 / 39.900 | 8.150 ± 0.612 | +7.750 ± 0.619 | 109.750 | +99.100 ± 2.159 | 0.000 | 1.000 | 52.200 | +46.950 ± 1.751 | 704.200 | 0.016 | +0.003 ± 0.001 | 8280.104 ± 185.330 | -14145.356 ± 564.796 | 7125.9 ± 112.8 | -26318.5 ± 968.0 | 27.799 | -10.282 ± 0.500 | 29.430 ± 0.708 | +15.069 ± 0.889 | 22.363 | 0.202 | 730.600 | 19.900 | 34.400 | +17.500 ± 0.872 | 5961.570 | 192.700 |
| hand | 19.800 / 39.850 | 3.550 ± 0.359 | +3.150 ± 0.335 | 65.750 | +55.100 ± 1.231 | 7.650 | 0.051 | 16.000 | +10.750 ± 0.688 | 1566.750 | 0.013 | +0.000 ± 0.001 | 29348.109 ± 401.843 | +6922.649 ± 466.210 | 32105.8 ± 614.4 | -1338.6 ± 964.9 | 32.443 | -5.638 ± 0.401 | 19.687 ± 0.403 | +5.327 ± 0.594 | 19.775 | 0.023 | 2419.950 | 19.850 | 20.050 | +3.150 ± 0.534 | 118.326 | 226.900 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **direct**: p0 0.822/0.176/0.001 (609); p1 0.529/0.452/0.019 (563); p2 0.494/0.487/0.020 (375); p3 0.533/0.455/0.013 (289); p4 0.462/0.521/0.017 (286); p5 0.444/0.534/0.021 (280); p6 0.436/0.553/0.011 (273); p7 0.433/0.553/0.014 (269); p8 0.424/0.561/0.015 (268); p9 0.442/0.541/0.017 (257); p10 0.470/0.510/0.020 (251); p11 0.507/0.481/0.012 (205); p12 0.507/0.479/0.014 (153); p13 0.546/0.445/0.009 (116); p14 0.527/0.463/0.010 (64); p15 0.686/0.314/0.000 (8)
- **careful**: p0 1.000/0.000/0.000 (599); p1 1.000/0.000/0.000 (731); p2 1.000/0.000/0.000 (840); p3 1.000/0.000/0.000 (866); p4 1.000/0.000/0.000 (743); p5 1.000/0.000/0.000 (280); p6 1.000/0.000/0.000 (43)
- **stamper**: p0 0.000/1.000/0.000 (580); p1 0.000/1.000/0.000 (306); p2 0.000/1.000/0.000 (150); p3 0.000/1.000/0.000 (8); p4 0.000/1.000/0.000 (7); p5 0.000/1.000/0.000 (3)
- **hand**: p0 —/—/— (0); p1 —/—/— (0); p2 —/—/— (0); p3 —/—/— (0); p4 —/—/— (0); p5 —/—/— (0); p6 —/—/— (0); p7 —/—/— (0); p8 —/—/— (0); p9 —/—/— (0); p10 —/—/— (0); p11 —/—/— (0); p12 —/—/— (0); p13 —/—/— (0); p14 —/—/— (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 2396.8 / 662.7 | 0.84 / 0.98 | +0.14 ± 0.05 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.07 / 0.07 | +0.00 ± 0.00 | 0.376 / 0.453 | +0.077 ± 0.013 | 0.011 / 0.022 | 0.116 / 0.125 | +0.009 ± 0.004 | 2.57 / 2.73 | +0.15 ± 0.08 |
| careful | 2657.3 / 273.4 | 0.17 / 0.08 | -0.09 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.07 / 0.08 | +0.01 ± 0.00 | 0.130 / 0.126 | -0.004 ± 0.004 | 0.001 / 0.001 | 0.061 / 0.067 | +0.006 ± 0.003 | 1.41 / 1.25 | -0.16 ± 0.09 |
| stamper | 876.6 / 147.8 | 1.10 / 0.56 | -0.53 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.02 / 0.24 | +0.21 ± 0.03 | 0.255 / 0.236 | -0.019 ± 0.009 | 0.166 / 0.264 | 0.112 / 0.081 | -0.031 ± 0.006 | 3.35 / 1.94 | -1.40 ± 0.15 |
| hand | 2465.1 / 617.6 | 0.74 / 0.62 | -0.13 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.13 / 0.15 | +0.02 ± 0.00 | 0.353 / 0.380 | +0.026 ± 0.006 | 0.022 / 0.031 | 0.099 / 0.088 | -0.011 ± 0.002 | 2.55 / 2.34 | -0.21 ± 0.05 |

# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule`, seeds 21-40, hide ``, model `None` (value off, horizon 8)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the plant-blind seats — a revised submission or a panel, where no plant is received — are read apart: their share of the review decisions and the stamp rate on them.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | blind-seat share | blind-seat stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 31663.4 ± 759.3 | -2741.5 ± 1122.5 | 3797.8 | 0.482 | 0.508 | 0.010 | 0.306 | 0.410 | 0.233 | 0.954 | 107.95 | 295.15 | 0.25 |
| careful | 34404.9 ± 785.9 | nan ± nan | 4035.3 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.280 | 0.000 | 7.70 | 0.00 | 0.35 |
| stamper | 6865.0 ± 189.0 | -27539.8 ± 832.1 | 1040.8 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.022 | 1.000 | 16.10 | 174.25 | 1.00 |
| hand | 31794.9 ± 488.5 | -2610.0 ± 749.5 | 4344.6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.289 | 0.000 | 11.35 | 0.00 | 0.55 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 0.874 | 0.962 | 0.848 (999) | 0.883 (1350) | 0.841 (1144) | 0.740 (21335) | 0.390 (51129) | 44.350 | 347.950 | 1.476 | 6.655 |
| careful | — | 0.685 | 0.000 (25159) | 0.000 (5535) | 0.000 (4467) | 0.000 (1292) | 0.000 (44254) | 25.100 | 699.850 | 1.167 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (20815) | 72.200 | 191.150 | 1.970 | 2.413 |
| hand | — | 0.820 | — (0) | 0.000 (9001) | 0.000 (17318) | 0.000 (16563) | 0.000 (44010) | 34.650 | 341.000 | 1.297 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| direct | 39.800 | 0.000 | 0.000 | 0.000 | 0.000 | 0.250 | 0.000 |
| careful | 39.550 | 0.000 | 0.000 | 0.000 | 0.000 | 0.350 | 0.000 |
| stamper | 39.950 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| hand | 39.850 | 0.000 | 0.000 | 0.000 | 0.000 | 0.550 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | nominal surplus | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 17.300 / 39.800 | 107.950 ± 5.710 | +100.250 ± 5.332 | 147.500 | +136.900 ± 4.605 | 7.150 | 0.314 | 24.550 | +19.000 ± 1.000 | 1868.500 | 0.053 | +0.029 ± 0.003 | 32402.700 ± 458.170 | +9301.892 ± 743.095 | 30.177 | -7.627 ± 0.557 | 22.092 ± 0.425 | +7.727 ± 0.832 | 20.916 | 0.012 | 2286.300 | 19.800 | 22.500 | +5.650 ± 0.525 | 65.802 | 132.450 |
| careful | 22.700 / 39.550 | 7.700 ± 0.692 | — | 10.600 | — | 3.650 | 0.041 | 5.550 | — | 1612.300 | 0.025 | — | 23100.809 ± 490.604 | — | 37.804 | — | 14.364 ± 0.567 | — | 17.402 | 0.001 | 2639.700 | 19.550 | 16.850 | — | 962.459 | 213.900 |
| stamper | 5.700 / 39.950 | 16.100 ± 0.644 | +8.400 ± 0.838 | 110.400 | +99.800 ± 1.977 | 0.000 | 1.000 | 52.250 | +46.700 ± 1.898 | 869.850 | 0.186 | +0.161 ± 0.003 | 8881.524 ± 176.410 | -14219.284 ± 488.247 | 27.241 | -10.563 ± 0.428 | 32.990 ± 0.777 | +18.625 ± 1.002 | 22.327 | 0.179 | 745.600 | 19.950 | 34.250 | +17.400 ± 0.913 | 5871.487 | 118.750 |
| hand | 19.400 / 39.850 | 11.350 ± 0.755 | +3.650 ± 0.933 | 65.000 | +54.400 ± 1.358 | 7.450 | 0.063 | 14.800 | +9.250 ± 0.900 | 1672.900 | 0.062 | +0.037 ± 0.002 | 29779.643 ± 450.422 | +6678.835 ± 729.139 | 32.178 | -5.626 ± 0.547 | 20.562 ± 0.450 | +6.198 ± 0.742 | 19.879 | 0.009 | 2448.750 | 19.850 | 20.450 | +3.600 ± 0.461 | 108.558 | 179.200 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **direct**: p0 0.819/0.180/0.002 (599); p1 0.343/0.634/0.023 (564); p2 0.461/0.528/0.010 (338); p3 0.510/0.484/0.006 (263); p4 0.450/0.534/0.016 (273); p5 0.385/0.601/0.014 (256); p6 0.380/0.612/0.008 (251); p7 0.398/0.596/0.006 (253); p8 0.429/0.566/0.005 (247); p9 0.440/0.556/0.004 (240); p10 0.448/0.543/0.009 (241); p11 0.409/0.572/0.020 (178); p12 0.390/0.599/0.011 (52); p13 0.427/0.569/0.004 (37); p14 0.479/0.504/0.017 (6)
- **careful**: p0 1.000/0.000/0.000 (601); p1 1.000/0.000/0.000 (702); p2 1.000/0.000/0.000 (824); p3 1.000/0.000/0.000 (849); p4 1.000/0.000/0.000 (764); p5 1.000/0.000/0.000 (266); p6 1.000/0.000/0.000 (31)
- **stamper**: p0 0.000/1.000/0.000 (562); p1 0.000/1.000/0.000 (303); p2 0.000/1.000/0.000 (153); p3 0.000/1.000/0.000 (16); p4 0.000/1.000/0.000 (6); p5 0.000/1.000/0.000 (1)
- **hand**: p0 —/—/— (0); p1 —/—/— (0); p2 —/—/— (0); p3 —/—/— (0); p4 —/—/— (0); p5 —/—/— (0); p6 —/—/— (0); p7 —/—/— (0); p8 —/—/— (0); p9 —/—/— (0); p10 —/—/— (0); p11 —/—/— (0); p12 —/—/— (0); p13 —/—/— (0); p14 —/—/— (0)

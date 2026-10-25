# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule`, seeds 21-40, hide ``, model `results/redteam/stability/learned-rev-careful/wm/models/wm-online-10.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the plant-blind seats — a revised submission or a panel, where no plant is received — are read apart: their share of the review decisions and the stamp rate on them.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | blind-seat share | blind-seat stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 31495.9 ± 503.1 | -2909.0 ± 914.2 | 3771.1 | 0.497 | 0.499 | 0.004 | 0.279 | 0.375 | 0.243 | 0.966 | 102.40 | 260.65 | 0.10 |
| careful | 34404.9 ± 785.9 | nan ± nan | 4035.3 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.280 | 0.000 | 7.70 | 0.00 | 0.35 |
| stamper | 6865.0 ± 189.0 | -27539.8 ± 832.1 | 1040.8 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.022 | 1.000 | 16.10 | 174.25 | 1.00 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 0.877 | 0.956 | 0.976 (165) | 0.931 (1043) | 0.895 (458) | 0.702 (26591) | 0.369 (47165) | 43.500 | 240.500 | 1.580 | 5.992 |
| careful | — | 0.685 | 0.000 (25159) | 0.000 (5535) | 0.000 (4467) | 0.000 (1292) | 0.000 (44254) | 25.100 | 699.850 | 1.167 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (20815) | 72.200 | 191.150 | 1.970 | 2.413 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| greedy | 39.850 | 0.000 | 0.000 | 0.000 | 0.000 | 0.100 | 0.000 |
| careful | 39.550 | 0.000 | 0.000 | 0.000 | 0.000 | 0.350 | 0.000 |
| stamper | 39.950 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | nominal surplus | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 16.800 / 39.850 | 102.400 ± 3.513 | +94.700 ± 3.448 | 150.900 | +140.300 ± 3.473 | 6.900 | 0.305 | 23.650 | +18.100 ± 0.680 | 1762.100 | 0.045 | +0.020 ± 0.003 | 33950.408 ± 470.006 | +10849.599 ± 628.793 | 28.867 | -8.937 ± 0.510 | 23.015 ± 0.411 | +8.650 ± 0.681 | 21.627 | 0.018 | 2173.150 | 19.850 | 23.050 | +6.200 ± 0.495 | 72.844 | 151.450 |
| careful | 22.700 / 39.550 | 7.700 ± 0.692 | — | 10.600 | — | 3.650 | 0.041 | 5.550 | — | 1612.300 | 0.025 | — | 23100.809 ± 490.604 | — | 37.804 | — | 14.364 ± 0.567 | — | 17.402 | 0.001 | 2639.700 | 19.550 | 16.850 | — | 962.459 | 213.900 |
| stamper | 5.700 / 39.950 | 16.100 ± 0.644 | +8.400 ± 0.838 | 110.400 | +99.800 ± 1.977 | 0.000 | 1.000 | 52.250 | +46.700 ± 1.898 | 869.850 | 0.186 | +0.161 ± 0.003 | 8881.524 ± 176.410 | -14219.284 ± 488.247 | 27.241 | -10.563 ± 0.428 | 32.990 ± 0.777 | +18.625 ± 1.002 | 22.327 | 0.179 | 745.600 | 19.950 | 34.250 | +17.400 ± 0.913 | 5871.487 | 118.750 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **greedy**: p0 0.769/0.231/0.000 (596); p1 0.353/0.641/0.006 (408); p2 0.487/0.488/0.025 (278); p3 0.469/0.521/0.010 (269); p4 0.416/0.583/0.001 (269); p5 0.416/0.582/0.002 (259); p6 0.473/0.527/0.000 (245); p7 0.476/0.524/0.000 (235); p8 0.496/0.504/0.000 (244); p9 0.476/0.520/0.004 (244); p10 0.483/0.517/0.000 (240); p11 0.449/0.551/0.000 (235); p12 0.417/0.583/0.000 (162); p13 0.469/0.531/0.000 (64); p14 0.543/0.457/0.000 (13); p15 0.224/0.776/0.000 (9)
- **careful**: p0 1.000/0.000/0.000 (601); p1 1.000/0.000/0.000 (702); p2 1.000/0.000/0.000 (824); p3 1.000/0.000/0.000 (849); p4 1.000/0.000/0.000 (764); p5 1.000/0.000/0.000 (266); p6 1.000/0.000/0.000 (31)
- **stamper**: p0 0.000/1.000/0.000 (562); p1 0.000/1.000/0.000 (303); p2 0.000/1.000/0.000 (153); p3 0.000/1.000/0.000 (16); p4 0.000/1.000/0.000 (6); p5 0.000/1.000/0.000 (1)

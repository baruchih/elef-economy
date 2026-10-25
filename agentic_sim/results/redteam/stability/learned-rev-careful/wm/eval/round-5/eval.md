# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule`, seeds 21-40, hide ``, model `results/redteam/stability/learned-rev-careful/wm/models/wm-online-5.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the plant-blind seats — a revised submission or a panel, where no plant is received — are read apart: their share of the review decisions and the stamp rate on them.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | blind-seat share | blind-seat stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 27310.1 ± 597.9 | -7094.8 ± 1037.5 | 3553.8 | 0.517 | 0.482 | 0.000 | 0.268 | 0.365 | 0.223 | 0.969 | 93.90 | 251.10 | 0.40 |
| careful | 34404.9 ± 785.9 | nan ± nan | 4035.3 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.280 | 0.000 | 7.70 | 0.00 | 0.35 |
| stamper | 6865.0 ± 189.0 | -27539.8 ± 832.1 | 1040.8 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.022 | 1.000 | 16.10 | 174.25 | 1.00 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 0.874 | 0.947 | 0.962 (952) | 0.941 (802) | 0.866 (580) | 0.623 (23954) | 0.385 (44787) | 48.450 | 266.050 | 1.984 | 5.183 |
| careful | — | 0.685 | 0.000 (25159) | 0.000 (5535) | 0.000 (4467) | 0.000 (1292) | 0.000 (44254) | 25.100 | 699.850 | 1.167 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (20815) | 72.200 | 191.150 | 1.970 | 2.413 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| greedy | 39.800 | 0.000 | 0.000 | 0.000 | 0.000 | 0.400 | 0.000 |
| careful | 39.550 | 0.000 | 0.000 | 0.000 | 0.000 | 0.350 | 0.000 |
| stamper | 39.950 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | nominal surplus | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 14.000 / 39.800 | 93.900 ± 3.290 | +86.200 ± 3.235 | 140.050 | +129.450 ± 4.314 | 5.150 | 0.179 | 28.650 | +23.100 ± 1.397 | 1734.900 | 0.050 | +0.025 ± 0.003 | 32168.951 ± 502.891 | +9068.142 ± 761.879 | 28.332 | -9.472 ± 0.508 | 25.638 ± 0.448 | +11.273 ± 0.839 | 21.967 | 0.086 | 1982.050 | 19.800 | 25.800 | +8.950 ± 0.679 | 84.471 | 135.650 |
| careful | 22.700 / 39.550 | 7.700 ± 0.692 | — | 10.600 | — | 3.650 | 0.041 | 5.550 | — | 1612.300 | 0.025 | — | 23100.809 ± 490.604 | — | 37.804 | — | 14.364 ± 0.567 | — | 17.402 | 0.001 | 2639.700 | 19.550 | 16.850 | — | 962.459 | 213.900 |
| stamper | 5.700 / 39.950 | 16.100 ± 0.644 | +8.400 ± 0.838 | 110.400 | +99.800 ± 1.977 | 0.000 | 1.000 | 52.250 | +46.700 ± 1.898 | 869.850 | 0.186 | +0.161 ± 0.003 | 8881.524 ± 176.410 | -14219.284 ± 488.247 | 27.241 | -10.563 ± 0.428 | 32.990 ± 0.777 | +18.625 ± 1.002 | 22.327 | 0.179 | 745.600 | 19.950 | 34.250 | +17.400 ± 0.913 | 5871.487 | 118.750 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **greedy**: p0 0.793/0.207/0.000 (593); p1 0.337/0.663/0.000 (467); p2 0.424/0.574/0.002 (298); p3 0.453/0.546/0.000 (257); p4 0.467/0.533/0.000 (259); p5 0.462/0.538/0.000 (252); p6 0.451/0.548/0.000 (250); p7 0.474/0.526/0.000 (246); p8 0.483/0.516/0.001 (240); p9 0.508/0.492/0.000 (231); p10 0.546/0.454/0.000 (212); p11 0.581/0.419/0.000 (161); p12 0.631/0.369/0.000 (85); p13 0.655/0.345/0.000 (3)
- **careful**: p0 1.000/0.000/0.000 (601); p1 1.000/0.000/0.000 (702); p2 1.000/0.000/0.000 (824); p3 1.000/0.000/0.000 (849); p4 1.000/0.000/0.000 (764); p5 1.000/0.000/0.000 (266); p6 1.000/0.000/0.000 (31)
- **stamper**: p0 0.000/1.000/0.000 (562); p1 0.000/1.000/0.000 (303); p2 0.000/1.000/0.000 (153); p3 0.000/1.000/0.000 (16); p4 0.000/1.000/0.000 (6); p5 0.000/1.000/0.000 (1)

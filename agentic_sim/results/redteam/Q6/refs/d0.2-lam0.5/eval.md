# Evaluation (Q6, the learned bidder) — cell `--entry-pool 20 --stampers 0.6 --lam 0.5`, seeds 21-40, model `None` (value off, horizon 8)

The bidder's lifetime real wealth paired against the careful (the ratchet); its rule by tick (the ratchet's bid / at cost / no offer), the awards its bids won and the bid over cost at them, the offers lost, the wealth it held (real, a tick), the price level and the members' mean price at the close (hoarding and P_t beside).

| policy | lifetime real | paired − careful | bid decisions | ratchet / undercut / withhold | awards won | of slot awards | bid / cost | offers lost | held (real) | slot ρ | slot cost | delivery income | effort burned | P_t close | members' price | awarded (all) | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| careful | 2185.5 ± 99.1 | nan ± nan | 437.950 | 1.000 / 0.000 / 0.000 | 136.950 | 136.950 | 4.952 | 629.650 | 1098.281 | 0.899 | 4.122 | 1990.008 | 1064.720 | 19.324 | 18.600 | 2515.100 | 0.000 |
| undercut | 2215.1 ± 98.5 | 29.7 ± 148.3 | 306.000 | 0.000 / 1.000 / 0.000 | 211.350 | 211.350 | 3.953 | 319.600 | 1075.476 | 0.870 | 4.122 | 2461.872 | 1342.486 | 19.121 | 18.432 | 2502.750 | 0.000 |
| withhold | 934.0 ± 45.0 | -1251.5 ± 119.7 | 713.800 | 0.000 / 0.000 / 1.000 | 0.000 | 0.000 | — | 0.000 | 468.378 | 0.945 | 4.122 | 0.000 | 513.800 | 21.008 | 20.220 | 2398.950 | 0.000 |

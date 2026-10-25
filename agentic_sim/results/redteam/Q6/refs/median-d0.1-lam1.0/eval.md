# Evaluation (Q6, the learned bidder) — cell `--entry-pool 20 --stampers 0.6 --lam 1.0 --undercut 0.1 --bidder-slot median`, seeds 21-40, model `None` (value off, horizon 8)

The bidder's lifetime real wealth paired against the careful (the ratchet); its rule by tick (the ratchet's bid / at cost / no offer), the awards its bids won and the bid over cost at them, the offers lost, the wealth it held (real, a tick), the price level and the members' mean price at the close (hoarding and P_t beside).

| policy | lifetime real | paired − careful | bid decisions | ratchet / undercut / withhold | awards won | of slot awards | bid / cost | offers lost | held (real) | slot ρ | slot cost | delivery income | effort burned | P_t close | members' price | awarded (all) | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| careful | 1595.2 ± 126.2 | nan ± nan | 451.600 | 1.000 / 0.000 / 0.000 | 128.000 | 128.000 | 2.194 | 740.050 | 773.897 | 0.892 | 8.936 | 1896.672 | 1623.476 | 18.173 | 18.027 | 2513.100 | 0.000 |
| undercut | 1209.3 ± 120.6 | -385.9 ± 151.6 | 378.000 | 0.000 / 1.000 / 0.000 | 181.750 | 181.750 | 1.738 | 318.650 | 583.187 | 0.848 | 8.936 | 2248.146 | 2047.859 | 18.081 | 17.348 | 2561.700 | 0.000 |
| withhold | 984.4 ± 76.9 | -610.8 ± 151.1 | 705.400 | 0.000 / 0.000 / 1.000 | 0.000 | 0.000 | — | 0.000 | 485.588 | 0.945 | 8.936 | 0.000 | 531.400 | 20.744 | 19.816 | 2440.200 | 0.000 |

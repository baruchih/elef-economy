# Evaluation (Q6, the learned bidder) — cell `--entry-pool 20 --stampers 0.6 --undercut 0.2 --bidder-slot median`, seeds 21-40, model `None` (value off, horizon 8)

The bidder's lifetime real wealth paired against the careful (the ratchet); its rule by tick (the ratchet's bid / at cost / no offer), the awards its bids won and the bid over cost at them, the offers lost, the wealth it held (real, a tick), the price level and the members' mean price at the close (hoarding and P_t beside).

| policy | lifetime real | paired − careful | bid decisions | ratchet / undercut / withhold | awards won | of slot awards | bid / cost | offers lost | held (real) | slot ρ | slot cost | delivery income | effort burned | P_t close | members' price | awarded (all) | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| careful | 1585.0 ± 69.0 | nan ± nan | 457.600 | 1.000 / 0.000 / 0.000 | 127.300 | 127.300 | 2.531 | 545.400 | 869.524 | 0.884 | 8.936 | 2195.936 | 1611.608 | 20.777 | 19.930 | 2451.050 | 0.000 |
| undercut | 1033.0 ± 86.3 | -552.0 ± 97.9 | 380.400 | 0.000 / 1.000 / 0.000 | 178.800 | 178.800 | 1.733 | 478.750 | 510.175 | 0.869 | 8.936 | 2147.499 | 2026.781 | 20.354 | 19.281 | 2515.250 | 0.000 |
| withhold | 889.2 ± 30.6 | -695.8 ± 69.1 | 719.450 | 0.000 / 0.000 / 1.000 | 0.000 | 0.000 | — | 0.000 | 452.490 | 0.944 | 8.936 | 0.000 | 501.700 | 21.405 | 20.658 | 2360.050 | 0.000 |

# Evaluation (Q6, the learned bidder) — cell `--entry-pool 20 --stampers 0.6 --undercut 0.1`, seeds 21-40, model `None` (value off, horizon 8)

The bidder's lifetime real wealth paired against the careful (the ratchet); its rule by tick (the ratchet's bid / at cost / no offer), the awards its bids won and the bid over cost at them, the offers lost, the wealth it held (real, a tick), the price level and the members' mean price at the close (hoarding and P_t beside).

| policy | lifetime real | paired − careful | bid decisions | ratchet / undercut / withhold | awards won | of slot awards | bid / cost | offers lost | held (real) | slot ρ | slot cost | delivery income | effort burned | P_t close | members' price | awarded (all) | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 2282.9 ± 77.3 | 290.3 ± 101.2 | 351.150 | 0.170 / 0.757 / 0.073 | 188.850 | 188.850 | 4.729 | 410.600 | 1174.106 | 0.861 | 4.122 | 2644.512 | 1246.764 | 20.661 | 19.435 | 2506.850 | 0.000 |
| careful | 1992.5 ± 66.3 | nan ± nan | 445.050 | 1.000 / 0.000 / 0.000 | 137.450 | 137.450 | 4.828 | 539.500 | 985.357 | 0.894 | 4.122 | 2003.841 | 1028.554 | 20.540 | 19.843 | 2448.750 | 0.000 |
| undercut | 2267.7 ± 75.1 | 275.2 ± 87.7 | 343.700 | 0.000 / 1.000 / 0.000 | 192.650 | 192.650 | 4.649 | 497.550 | 1167.574 | 0.866 | 4.122 | 2657.309 | 1270.991 | 20.693 | 19.549 | 2490.400 | 0.000 |
| withhold | 859.7 ± 31.4 | -1132.8 ± 76.5 | 730.000 | 0.000 / 0.000 / 1.000 | 0.000 | 0.000 | — | 0.000 | 420.616 | 0.951 | 4.122 | 0.000 | 482.950 | 20.457 | 20.144 | 2447.750 | 0.000 |

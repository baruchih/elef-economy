# Evaluation (Q6, the learned bidder) — cell `--entry-pool 20 --stampers 0.6`, seeds 21-40, model `None` (value off, horizon 8)

The bidder's lifetime real wealth paired against the careful (the ratchet); its rule by tick (the ratchet's bid / at cost / no offer), the awards its bids won and the bid over cost at them, the offers lost, the wealth it held (real, a tick), the price level and the members' mean price at the close (hoarding and P_t beside).

| policy | lifetime real | paired − careful | bid decisions | ratchet / undercut / withhold | awards won | of slot awards | bid / cost | offers lost | held (real) | slot ρ | slot cost | delivery income | effort burned | P_t close | members' price | awarded (all) | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| careful | 1992.5 ± 66.3 | nan ± nan | 445.050 | 1.000 / 0.000 / 0.000 | 137.450 | 137.450 | 4.828 | 539.500 | 985.357 | 0.894 | 4.122 | 2003.841 | 1028.554 | 20.540 | 19.843 | 2448.750 | 0.000 |
| undercut | 2166.0 ± 118.7 | 173.5 ± 130.0 | 323.550 | 0.000 / 1.000 / 0.000 | 194.150 | 194.150 | 4.122 | 432.250 | 1084.237 | 0.867 | 4.122 | 2371.790 | 1299.592 | 20.230 | 19.413 | 2491.950 | 0.000 |
| withhold | 859.7 ± 31.4 | -1132.8 ± 76.5 | 730.000 | 0.000 / 0.000 / 1.000 | 0.000 | 0.000 | — | 0.000 | 420.616 | 0.951 | 4.122 | 0.000 | 482.950 | 20.457 | 20.144 | 2447.750 | 0.000 |

# Evaluation (Q6, the learned bidder) — cell `--entry-pool 20 --stampers 0.6 --lam 2.0 --undercut 0.2 --bidder-slot median`, seeds 21-40, model `None` (value off, horizon 8)

The bidder's lifetime real wealth paired against the careful (the ratchet); its rule by tick (the ratchet's bid / at cost / no offer), the awards its bids won and the bid over cost at them, the offers lost, the wealth it held (real, a tick), the price level and the members' mean price at the close (hoarding and P_t beside).

| policy | lifetime real | paired − careful | bid decisions | ratchet / undercut / withhold | awards won | of slot awards | bid / cost | offers lost | held (real) | slot ρ | slot cost | delivery income | effort burned | P_t close | members' price | awarded (all) | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| careful | 1655.8 ± 143.8 | nan ± nan | 469.300 | 1.000 / 0.000 / 0.000 | 120.700 | 120.700 | 1.968 | 752.600 | 860.526 | 0.879 | 8.936 | 1704.960 | 1596.031 | 16.768 | 16.779 | 2558.700 | 0.000 |
| undercut | 794.1 ± 157.7 | -861.7 ± 183.0 | 504.800 | 0.000 / 1.000 / 0.000 | 157.750 | 157.750 | 1.432 | 62.100 | 394.176 | 0.820 | 8.936 | 1647.361 | 1613.781 | 18.454 | 17.803 | 2500.500 | 0.000 |
| withhold | 890.2 ± 38.8 | -765.6 ± 153.9 | 713.600 | 0.000 / 0.000 / 1.000 | 0.000 | 0.000 | — | 0.000 | 429.976 | 0.942 | 8.936 | 0.000 | 496.150 | 20.039 | 19.578 | 2431.150 | 0.000 |

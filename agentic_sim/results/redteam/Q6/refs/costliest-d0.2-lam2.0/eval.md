# Evaluation (Q6, the learned bidder) — cell `--entry-pool 20 --stampers 0.6 --lam 2.0 --undercut 0.2 --bidder-slot costliest`, seeds 21-40, model `None` (value off, horizon 8)

The bidder's lifetime real wealth paired against the careful (the ratchet); its rule by tick (the ratchet's bid / at cost / no offer), the awards its bids won and the bid over cost at them, the offers lost, the wealth it held (real, a tick), the price level and the members' mean price at the close (hoarding and P_t beside).

| policy | lifetime real | paired − careful | bid decisions | ratchet / undercut / withhold | awards won | of slot awards | bid / cost | offers lost | held (real) | slot ρ | slot cost | delivery income | effort burned | P_t close | members' price | awarded (all) | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| careful | 893.6 ± 111.5 | nan ± nan | 573.550 | 1.000 / 0.000 / 0.000 | 83.750 | 83.750 | 1.382 | 970.500 | 422.571 | 0.868 | 15.511 | 1344.851 | 1626.006 | 17.573 | 17.187 | 2551.500 | 0.000 |
| undercut | 216.2 ± 69.7 | -677.4 ± 117.3 | 644.750 | 0.000 / 1.000 / 0.000 | 92.650 | 92.650 | 1.040 | 362.200 | 122.028 | 0.820 | 15.511 | 1198.022 | 1630.146 | 18.031 | 17.425 | 2544.500 | 0.000 |
| withhold | 1023.1 ± 50.3 | 129.5 ± 116.1 | 706.350 | 0.000 / 0.000 / 1.000 | 0.000 | 0.000 | — | 0.000 | 493.539 | 0.944 | 15.511 | 0.000 | 505.850 | 18.033 | 18.542 | 2458.300 | 0.000 |

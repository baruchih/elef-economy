# Evaluation (Q6, the learned bidder) — cell `--entry-pool 20 --stampers 0.6 --undercut 0.1 --lam 2.0`, seeds 21-40, model `None` (value off, horizon 16)

The bidder's lifetime real wealth paired against the careful (the ratchet); its rule by tick (the ratchet's bid / at cost / no offer), the awards its bids won and the bid over cost at them, the offers lost, the wealth it held (real, a tick), the price level and the members' mean price at the close (hoarding and P_t beside).

| policy | lifetime real | paired − careful | bid decisions | ratchet / undercut / withhold | awards won | of slot awards | bid / cost | offers lost | held (real) | slot ρ | slot cost | delivery income | effort burned | P_t close | members' price | awarded (all) | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 2944.4 ± 151.5 | 643.0 ± 188.2 | 300.150 | 0.113 / 0.845 / 0.042 | 218.950 | 218.950 | 4.115 | 212.800 | 1381.929 | 0.858 | 4.122 | 2656.541 | 1332.341 | 14.888 | 16.565 | 2541.500 | 0.000 |
| careful | 2301.4 ± 117.9 | nan ± nan | 441.000 | 1.000 / 0.000 / 0.000 | 136.500 | 136.500 | 4.707 | 765.750 | 1163.074 | 0.888 | 4.122 | 1872.892 | 1059.432 | 17.444 | 17.117 | 2550.000 | 0.000 |
| undercut | 2799.1 ± 134.6 | 497.6 ± 168.2 | 270.950 | 0.000 / 1.000 / 0.000 | 228.200 | 228.200 | 4.233 | 154.250 | 1314.751 | 0.863 | 4.122 | 2859.202 | 1415.773 | 17.688 | 17.668 | 2499.550 | 0.000 |

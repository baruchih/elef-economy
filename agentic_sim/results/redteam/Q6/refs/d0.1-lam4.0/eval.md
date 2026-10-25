# Evaluation (Q6, the learned bidder) — cell `--entry-pool 20 --stampers 0.6 --lam 4.0 --undercut 0.1`, seeds 21-40, model `None` (value off, horizon 8)

The bidder's lifetime real wealth paired against the careful (the ratchet); its rule by tick (the ratchet's bid / at cost / no offer), the awards its bids won and the bid over cost at them, the offers lost, the wealth it held (real, a tick), the price level and the members' mean price at the close (hoarding and P_t beside).

| policy | lifetime real | paired − careful | bid decisions | ratchet / undercut / withhold | awards won | of slot awards | bid / cost | offers lost | held (real) | slot ρ | slot cost | delivery income | effort burned | P_t close | members' price | awarded (all) | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| careful | 2493.1 ± 139.5 | nan ± nan | 441.250 | 1.000 / 0.000 / 0.000 | 135.800 | 135.800 | 4.600 | 762.400 | 1223.676 | 0.891 | 4.122 | 1835.773 | 1044.928 | 15.963 | 16.590 | 2513.950 | 0.000 |
| undercut | 2456.0 ± 120.2 | -37.2 ± 196.2 | 258.850 | 0.000 / 1.000 / 0.000 | 240.550 | 240.550 | 4.216 | 72.600 | 1202.702 | 0.851 | 4.122 | 2893.169 | 1445.144 | 18.733 | 17.384 | 2528.100 | 0.000 |
| withhold | 1056.8 ± 60.1 | -1436.3 ± 152.7 | 718.750 | 0.000 / 0.000 / 1.000 | 0.000 | 0.000 | — | 0.000 | 518.135 | 0.942 | 4.122 | 0.000 | 509.600 | 17.689 | 18.438 | 2462.700 | 0.000 |

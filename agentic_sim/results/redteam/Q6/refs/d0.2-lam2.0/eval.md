# Evaluation (Q6, the learned bidder) — cell `--entry-pool 20 --stampers 0.6 --lam 2.0`, seeds 21-40, model `None` (value off, horizon 8)

The bidder's lifetime real wealth paired against the careful (the ratchet); its rule by tick (the ratchet's bid / at cost / no offer), the awards its bids won and the bid over cost at them, the offers lost, the wealth it held (real, a tick), the price level and the members' mean price at the close (hoarding and P_t beside).

| policy | lifetime real | paired − careful | bid decisions | ratchet / undercut / withhold | awards won | of slot awards | bid / cost | offers lost | held (real) | slot ρ | slot cost | delivery income | effort burned | P_t close | members' price | awarded (all) | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| careful | 2301.4 ± 117.9 | nan ± nan | 441.000 | 1.000 / 0.000 / 0.000 | 136.500 | 136.500 | 4.707 | 765.750 | 1163.074 | 0.888 | 4.122 | 1872.892 | 1059.432 | 17.444 | 17.117 | 2550.000 | 0.000 |
| undercut | 2236.4 ± 152.0 | -65.0 ± 152.9 | 256.550 | 0.000 / 1.000 / 0.000 | 239.250 | 239.250 | 3.577 | 70.300 | 1102.592 | 0.853 | 4.122 | 2506.458 | 1446.385 | 18.622 | 16.993 | 2547.550 | 0.000 |
| withhold | 963.5 ± 48.9 | -1337.9 ± 131.8 | 715.500 | 0.000 / 0.000 / 1.000 | 0.000 | 0.000 | — | 0.000 | 479.232 | 0.940 | 4.122 | 0.000 | 508.100 | 19.365 | 19.175 | 2423.250 | 0.000 |

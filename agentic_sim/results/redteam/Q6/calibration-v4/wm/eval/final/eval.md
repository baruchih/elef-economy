# Evaluation (Q6, the learned bidder) — cell `--entry-pool 20 --stampers 0.6 --undercut 0.1 --lam 2.0`, seeds 21-40, model `results/redteam/Q6/calibration-v4/wm/models/wm-online-10.pt` (value mc, horizon 16)

The bidder's lifetime real wealth paired against the careful (the ratchet); its rule by tick (the ratchet's bid / at cost / no offer), the awards its bids won and the bid over cost at them, the offers lost, the wealth it held (real, a tick), the price level and the members' mean price at the close (hoarding and P_t beside).

| policy | lifetime real | paired − careful | bid decisions | ratchet / undercut / withhold | awards won | of slot awards | bid / cost | offers lost | held (real) | slot ρ | slot cost | delivery income | effort burned | P_t close | members' price | awarded (all) | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 2178.6 ± 131.4 | -122.9 ± 157.4 | 383.900 | 0.299 / 0.453 / 0.247 | 171.450 | 171.450 | 4.184 | 263.900 | 1155.967 | 0.885 | 4.122 | 2117.108 | 1195.479 | 18.633 | 16.884 | 2572.500 | 0.000 |
| greedy | 2631.8 ± 176.5 | 330.4 ± 213.6 | 325.400 | 0.082 / 0.726 / 0.192 | 194.100 | 194.100 | 4.198 | 205.150 | 1301.737 | 0.872 | 4.122 | 2376.589 | 1297.609 | 17.304 | 16.953 | 2556.600 | 0.050 |
| careful | 2301.4 ± 117.9 | nan ± nan | 441.000 | 1.000 / 0.000 / 0.000 | 136.500 | 136.500 | 4.707 | 765.750 | 1163.074 | 0.888 | 4.122 | 1872.892 | 1059.432 | 17.444 | 17.117 | 2550.000 | 0.000 |
| undercut | 2799.1 ± 134.6 | 497.6 ± 168.2 | 270.950 | 0.000 / 1.000 / 0.000 | 228.200 | 228.200 | 4.233 | 154.250 | 1314.751 | 0.863 | 4.122 | 2859.202 | 1415.773 | 17.688 | 17.668 | 2499.550 | 0.000 |
| withhold | 963.5 ± 48.9 | -1337.9 ± 131.8 | 715.500 | 0.000 / 0.000 / 1.000 | 0.000 | 0.000 | — | 0.000 | 479.232 | 0.940 | 4.122 | 0.000 | 508.100 | 19.365 | 19.175 | 2423.250 | 0.000 |

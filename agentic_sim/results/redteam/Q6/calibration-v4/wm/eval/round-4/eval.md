# Evaluation (Q6, the learned bidder) — cell `--entry-pool 20 --stampers 0.6 --undercut 0.1 --lam 2.0`, seeds 21-40, model `results/redteam/Q6/calibration-v4/wm/models/wm-online-4.pt` (value mc, horizon 16)

The bidder's lifetime real wealth paired against the careful (the ratchet); its rule by tick (the ratchet's bid / at cost / no offer), the awards its bids won and the bid over cost at them, the offers lost, the wealth it held (real, a tick), the price level and the members' mean price at the close (hoarding and P_t beside).

| policy | lifetime real | paired − careful | bid decisions | ratchet / undercut / withhold | awards won | of slot awards | bid / cost | offers lost | held (real) | slot ρ | slot cost | delivery income | effort burned | P_t close | members' price | awarded (all) | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 2208.3 ± 162.6 | -93.1 ± 141.0 | 336.000 | 0.322 / 0.485 / 0.193 | 171.700 | 171.700 | 4.271 | 208.700 | 1117.811 | 0.874 | 4.122 | 2152.391 | 1144.211 | 18.233 | 17.140 | 2564.600 | 0.100 |
| careful | 2301.4 ± 117.9 | nan ± nan | 441.000 | 1.000 / 0.000 / 0.000 | 136.500 | 136.500 | 4.707 | 765.750 | 1163.074 | 0.888 | 4.122 | 1872.892 | 1059.432 | 17.444 | 17.117 | 2550.000 | 0.000 |
| undercut | 2799.1 ± 134.6 | 497.6 ± 168.2 | 270.950 | 0.000 / 1.000 / 0.000 | 228.200 | 228.200 | 4.233 | 154.250 | 1314.751 | 0.863 | 4.122 | 2859.202 | 1415.773 | 17.688 | 17.668 | 2499.550 | 0.000 |

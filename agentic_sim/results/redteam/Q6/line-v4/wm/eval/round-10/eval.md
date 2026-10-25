# Evaluation (Q6, the learned bidder) — cell `--entry-pool 20 --stampers 0.6 --undercut 0.1`, seeds 21-40, model `results/redteam/Q6/line-v4/wm/models/wm-online-10.pt` (value mc, horizon 16)

The bidder's lifetime real wealth paired against the careful (the ratchet); its rule by tick (the ratchet's bid / at cost / no offer), the awards its bids won and the bid over cost at them, the offers lost, the wealth it held (real, a tick), the price level and the members' mean price at the close (hoarding and P_t beside).

| policy | lifetime real | paired − careful | bid decisions | ratchet / undercut / withhold | awards won | of slot awards | bid / cost | offers lost | held (real) | slot ρ | slot cost | delivery income | effort burned | P_t close | members' price | awarded (all) | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 2223.8 ± 105.8 | 231.2 ± 111.6 | 340.900 | 0.148 / 0.728 / 0.125 | 175.200 | 175.200 | 4.789 | 364.450 | 1153.817 | 0.866 | 4.122 | 2477.008 | 1174.510 | 19.740 | 19.484 | 2461.700 | 0.100 |
| careful | 1992.5 ± 66.3 | nan ± nan | 445.050 | 1.000 / 0.000 / 0.000 | 137.450 | 137.450 | 4.828 | 539.500 | 985.357 | 0.894 | 4.122 | 2003.841 | 1028.554 | 20.540 | 19.843 | 2448.750 | 0.000 |

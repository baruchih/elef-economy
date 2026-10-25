# Evaluation (Q6, the learned bidder) — cell `--entry-pool 20 --stampers 0.6 --lam 1.0 --undercut 0.1`, seeds 21-40, model `None` (value off, horizon 8)

The bidder's lifetime real wealth paired against the careful (the ratchet); its rule by tick (the ratchet's bid / at cost / no offer), the awards its bids won and the bid over cost at them, the offers lost, the wealth it held (real, a tick), the price level and the members' mean price at the close (hoarding and P_t beside).

| policy | lifetime real | paired − careful | bid decisions | ratchet / undercut / withhold | awards won | of slot awards | bid / cost | offers lost | held (real) | slot ρ | slot cost | delivery income | effort burned | P_t close | members' price | awarded (all) | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| careful | 2394.4 ± 135.3 | nan ± nan | 444.000 | 1.000 / 0.000 / 0.000 | 137.950 | 137.950 | 4.864 | 694.100 | 1207.654 | 0.896 | 4.122 | 2019.234 | 1044.794 | 17.866 | 17.750 | 2529.050 | 0.000 |
| undercut | 2470.1 ± 151.6 | 75.7 ± 213.6 | 306.100 | 0.000 / 1.000 / 0.000 | 211.500 | 211.500 | 4.149 | 317.450 | 1197.177 | 0.867 | 4.122 | 2602.876 | 1341.322 | 18.196 | 17.384 | 2554.650 | 0.000 |
| withhold | 992.9 ± 60.5 | -1401.5 ± 146.3 | 716.300 | 0.000 / 0.000 / 1.000 | 0.000 | 0.000 | — | 0.000 | 503.088 | 0.935 | 4.122 | 0.000 | 513.100 | 19.588 | 18.959 | 2468.150 | 0.000 |

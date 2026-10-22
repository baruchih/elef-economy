# Evaluation (Q4, the pair) — cell `--entry-pool 20 --stampers 0.6`, seeds 21-40, model `results/redteam/Q4/line-v4b/models/wm-online-6.pt` (value mc, horizon 16)

The pair's lifetime real wealth (the deliverer's and the reviewer's, as one), paired against the careful pair; the deliverer's bad share and what became of its bad work; the reviewer's verdicts (care / approve blind / reject blind) over all its reviews, and on the deliverer's cases apart (matched in the calibration, blind in the line).

| policy | pair lifetime real | paired − careful | D real | R real | work decisions | bad share | bad approved / caught | R care / approve / reject | R reviews | D's cases R took (matched / waited / unmatched) | R on D's cases: care / stamp / reject | bad stamped (vested / caught) | forfeited | R suspensions | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 4631.3 ± 158.5 | -366.2 ± 167.2 | 1315.144 | 3316.201 | 138.200 | 0.006 | 0.100 / 0.700 | 0.693 / 0.307 / 0.001 | 779.750 | 18.150 (0.000 / 0.000 / 0.000) | 16.050 / 2.050 / 0.000 | 0.300 (0.000 / 0.000) | 296.850 | 0.100 | 0.00 |
| careful | 4997.5 ± 139.1 | nan ± nan | 1386.294 | 3611.243 | 130.100 | 0.000 | 0.000 / 0.000 | 1.000 / 0.000 / 0.000 | 811.050 | 18.350 (0.000 / 0.000 / 0.000) | 18.350 / 0.000 / 0.000 | 0.000 (0.000 / 0.000) | 276.500 | 0.000 | 0.00 |

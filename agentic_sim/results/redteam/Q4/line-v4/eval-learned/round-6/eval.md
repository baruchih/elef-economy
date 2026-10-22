# Evaluation (Q4, the pair) — cell `--entry-pool 20 --stampers 0.6`, seeds 21-40, model `results/redteam/Q4/line-v4/models/wm-online-6.pt` (value mc, horizon 16)

The pair's lifetime real wealth (the deliverer's and the reviewer's, as one), paired against the careful pair; the deliverer's bad share and what became of its bad work; the reviewer's verdicts (care / approve blind / reject blind) over all its reviews, and on the deliverer's cases apart (matched in the calibration, blind in the line).

| policy | pair lifetime real | paired − careful | D real | R real | work decisions | bad share | bad approved / caught | R care / approve / reject | R reviews | D's cases R took (matched / waited / unmatched) | R on D's cases: care / stamp / reject | bad stamped (vested / caught) | forfeited | R suspensions | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 4675.6 ± 216.3 | -322.0 ± 233.0 | 1434.881 | 3240.696 | 129.050 | 0.009 | 0.000 / 1.050 | 0.697 / 0.303 / 0.000 | 750.350 | 17.650 (0.000 / 0.000 / 0.000) | 16.300 / 1.350 / 0.000 | 0.150 (0.000 / 0.000) | 266.750 | 0.200 | 0.10 |
| careful | 4997.5 ± 139.1 | nan ± nan | 1386.294 | 3611.243 | 130.100 | 0.000 | 0.000 / 0.000 | 1.000 / 0.000 / 0.000 | 811.050 | 18.350 (0.000 / 0.000 / 0.000) | 18.350 / 0.000 / 0.000 | 0.000 (0.000 / 0.000) | 276.500 | 0.000 | 0.00 |

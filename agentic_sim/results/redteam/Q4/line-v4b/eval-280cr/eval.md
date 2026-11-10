# Evaluation (Q4, the pair) — cell `--entry-pool 20 --stampers 0.6 --rules 2.8.0`, seeds 21-40, model `results/redteam/Q4/line-v4b/models/wm-online-10.pt` (value mc, horizon 16)

The pair's lifetime real wealth (the deliverer's and the reviewer's, as one), paired against the careful pair; the deliverer's bad share and what became of its bad work; the reviewer's verdicts (care / approve blind / reject blind) over all its reviews, and on the deliverer's cases apart (matched in the calibration, blind in the line).

| policy | pair lifetime real | paired − careful | D real | R real | work decisions | bad share | bad approved / caught | R care / approve / reject | R reviews | D's cases R took (matched / waited / unmatched) | R on D's cases: care / stamp / reject | bad stamped (vested / caught) | forfeited | R suspensions | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 4092.1 ± 247.0 | -934.3 ± 296.9 | 1451.662 | 2640.426 | 119.450 | 0.009 | 0.100 / 1.050 | 0.779 / 0.220 / 0.002 | 637.900 | 15.350 (0.000 / 0.000 / 0.000) | 13.650 / 1.700 / 0.000 | 0.300 (0.000 / 0.050) | 282.650 | 0.050 | 0.10 |
| learned | 3535.4 ± 281.6 | -1490.9 ± 305.1 | 1281.151 | 2254.296 | 110.100 | 0.065 | 0.350 / 3.800 | 0.730 / 0.167 / 0.103 | 574.700 | 12.650 (0.000 / 0.000 / 0.000) | 10.100 / 1.400 / 1.150 | 0.350 (0.050 / 0.000) | 257.400 | 0.650 | 0.15 |
| careful | 5026.4 ± 204.7 | nan ± nan | 1437.742 | 3588.653 | 118.950 | 0.000 | 0.000 / 0.000 | 1.000 / 0.000 / 0.000 | 807.200 | 14.950 (0.000 / 0.000 / 0.000) | 14.950 / 0.000 / 0.000 | 0.000 (0.000 / 0.000) | 252.950 | 0.000 | 0.00 |
| collude | 336.5 ± 48.3 | -4689.9 ± 209.0 | 61.289 | 275.217 | 36.800 | 1.000 | 1.350 / 35.400 | 0.000 / 1.000 / 0.000 | 100.500 | 1.850 (0.000 / 0.000 / 0.000) | 0.000 / 1.850 / 0.000 | 1.850 (0.150 / 1.700) | 281.800 | 7.350 | 0.00 |

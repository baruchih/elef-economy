# Evaluation (Q4, the pair) — cell `--entry-pool 20 --stampers 0.6 --rules 2.7.0`, seeds 21-40, model `results/redteam/Q4/line-v4b/models/wm-online-10.pt` (value mc, horizon 16)

The pair's lifetime real wealth (the deliverer's and the reviewer's, as one), paired against the careful pair; the deliverer's bad share and what became of its bad work; the reviewer's verdicts (care / approve blind / reject blind) over all its reviews, and on the deliverer's cases apart (matched in the calibration, blind in the line).

| policy | pair lifetime real | paired − careful | D real | R real | work decisions | bad share | bad approved / caught | R care / approve / reject | R reviews | D's cases R took (matched / waited / unmatched) | R on D's cases: care / stamp / reject | bad stamped (vested / caught) | forfeited | R suspensions | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 4411.2 ± 224.6 | -663.2 ± 246.1 | 1401.926 | 3009.230 | 127.750 | 0.010 | 0.150 / 0.950 | 0.726 / 0.273 / 0.001 | 668.250 | 14.800 (0.000 / 0.000 / 0.000) | 13.500 / 1.250 / 0.000 | 0.200 (0.000 / 0.000) | 282.250 | 0.300 | 0.05 |
| learned | 3808.1 ± 188.2 | -1266.3 ± 200.3 | 1420.144 | 2387.946 | 126.100 | 0.033 | 0.350 / 3.700 | 0.666 / 0.251 / 0.083 | 629.900 | 16.000 (0.000 / 0.000 / 0.000) | 12.200 / 2.200 / 1.600 | 0.500 (0.050 / 0.000) | 297.600 | 0.350 | 0.00 |
| careful | 5074.3 ± 122.2 | nan ± nan | 1317.297 | 3757.052 | 122.600 | 0.000 | 0.000 / 0.000 | 1.000 / 0.000 / 0.000 | 831.950 | 14.850 (0.000 / 0.000 / 0.000) | 14.850 / 0.000 / 0.000 | 0.000 (0.000 / 0.000) | 270.900 | 0.000 | 0.00 |
| collude | 288.5 ± 46.6 | -4785.8 ± 126.0 | 52.557 | 235.957 | 34.750 | 1.000 | 0.900 / 33.850 | 0.000 / 1.000 / 0.000 | 96.500 | 1.700 (0.000 / 0.000 / 0.000) | 0.000 / 1.700 / 0.000 | 1.700 (0.050 / 1.650) | 248.600 | 7.700 | 0.00 |

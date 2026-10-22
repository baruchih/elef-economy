# Evaluation (Q4, the pair) — cell `--entry-pool 20 --stampers 0.6`, seeds 21-40, model `results/redteam/Q4/line-v4/models/wm-online-10.pt` (value mc, horizon 16)

The pair's lifetime real wealth (the deliverer's and the reviewer's, as one), paired against the careful pair; the deliverer's bad share and what became of its bad work; the reviewer's verdicts (care / approve blind / reject blind) over all its reviews, and on the deliverer's cases apart (matched in the calibration, blind in the line).

| policy | pair lifetime real | paired − careful | D real | R real | work decisions | bad share | bad approved / caught | R care / approve / reject | R reviews | D's cases R took (matched / waited / unmatched) | R on D's cases: care / stamp / reject | bad stamped (vested / caught) | forfeited | R suspensions | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 3526.4 ± 241.7 | -1471.1 ± 229.7 | 1230.055 | 2296.355 | 110.250 | 0.086 | 0.100 / 8.300 | 0.688 / 0.229 / 0.083 | 595.650 | 13.450 (0.000 / 0.000 / 0.000) | 10.550 / 1.900 / 0.950 | 0.100 (0.050 / 0.050) | 279.350 | 0.400 | 0.25 |
| greedy | 4073.1 ± 263.8 | -924.4 ± 248.3 | 1332.884 | 2740.217 | 118.350 | 0.008 | 0.000 / 0.950 | 0.763 / 0.236 / 0.001 | 647.200 | 16.400 (0.000 / 0.000 / 0.000) | 13.450 / 2.850 / 0.050 | 0.650 (0.000 / 0.000) | 257.150 | 0.350 | 0.25 |
| careful | 4997.5 ± 139.1 | nan ± nan | 1386.294 | 3611.243 | 130.100 | 0.000 | 0.000 / 0.000 | 1.000 / 0.000 / 0.000 | 811.050 | 18.350 (0.000 / 0.000 / 0.000) | 18.350 / 0.000 / 0.000 | 0.000 (0.000 / 0.000) | 276.500 | 0.000 | 0.00 |
| collude | 249.5 ± 22.6 | -4748.0 ± 143.5 | 6.681 | 242.825 | 30.750 | 1.000 | 1.700 / 29.050 | 0.000 / 1.000 / 0.000 | 94.700 | 1.050 (0.000 / 0.000 / 0.000) | 0.000 / 1.050 / 0.000 | 1.050 (0.200 / 0.850) | 212.150 | 7.750 | 0.00 |

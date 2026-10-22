# Evaluation (Q4, the pair) — cell `--entry-pool 20 --stampers 0.6`, seeds 21-40, model `results/redteam/Q4/line-v4b/models/wm-online-10.pt` (value mc, horizon 16)

The pair's lifetime real wealth (the deliverer's and the reviewer's, as one), paired against the careful pair; the deliverer's bad share and what became of its bad work; the reviewer's verdicts (care / approve blind / reject blind) over all its reviews, and on the deliverer's cases apart (matched in the calibration, blind in the line).

| policy | pair lifetime real | paired − careful | D real | R real | work decisions | bad share | bad approved / caught | R care / approve / reject | R reviews | D's cases R took (matched / waited / unmatched) | R on D's cases: care / stamp / reject | bad stamped (vested / caught) | forfeited | R suspensions | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 4453.3 ± 225.3 | -544.3 ± 267.9 | 1427.984 | 3025.267 | 129.950 | 0.007 | 0.100 / 0.500 | 0.728 / 0.271 / 0.001 | 695.450 | 16.900 (0.000 / 0.000 / 0.000) | 15.650 / 1.150 / 0.100 | 0.150 (0.000 / 0.000) | 280.750 | 0.150 | 0.05 |
| learned | 3753.7 ± 201.9 | -1243.8 ± 244.7 | 1316.165 | 2437.570 | 128.600 | 0.027 | 0.300 / 3.000 | 0.724 / 0.217 / 0.060 | 627.500 | 16.100 (0.000 / 0.000 / 0.000) | 13.100 / 1.800 / 1.200 | 0.250 (0.050 / 0.000) | 286.900 | 0.450 | 0.00 |
| careful | 4997.5 ± 139.1 | nan ± nan | 1386.294 | 3611.243 | 130.100 | 0.000 | 0.000 / 0.000 | 1.000 / 0.000 / 0.000 | 811.050 | 18.350 (0.000 / 0.000 / 0.000) | 18.350 / 0.000 / 0.000 | 0.000 (0.000 / 0.000) | 276.500 | 0.000 | 0.00 |
| collude | 249.5 ± 22.6 | -4748.0 ± 143.5 | 6.681 | 242.825 | 30.750 | 1.000 | 1.700 / 29.050 | 0.000 / 1.000 / 0.000 | 94.700 | 1.050 (0.000 / 0.000 / 0.000) | 0.000 / 1.050 / 0.000 | 1.050 (0.200 / 0.850) | 212.150 | 7.750 | 0.00 |

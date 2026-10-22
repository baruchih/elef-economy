# Evaluation (Q4, the pair) — cell `--entry-pool 20 --stampers 0.6 --pi0 0 --dial off --audit-roll off --match-pair on`, seeds 21-40, model `results/redteam/Q4/calibration-v4/wm/models/wm-online-6.pt` (value mc, horizon 16)

The pair's lifetime real wealth (the deliverer's and the reviewer's, as one), paired against the careful pair; the deliverer's bad share and what became of its bad work; the reviewer's verdicts (care / approve blind / reject blind) over all its reviews, and on the deliverer's cases apart (matched in the calibration, blind in the line).

| policy | pair lifetime real | paired − careful | D real | R real | work decisions | bad share | bad approved / caught | R care / approve / reject | R reviews | D's cases R took (matched / waited / unmatched) | R on D's cases: care / stamp / reject | bad stamped (vested / caught) | forfeited | R suspensions | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| learned | 4745.9 ± 198.8 | 990.6 ± 263.8 | 2582.387 | 2163.535 | 148.050 | 0.347 | 44.700 / 6.750 | 0.111 / 0.802 / 0.087 | 677.300 | 143.550 (143.550 / 41.000 / 2.900) | 12.350 / 120.850 / 10.150 | 59.400 (44.300 / 0.000) | 147.300 | 0.000 | 0.05 |
| careful | 3755.3 ± 135.8 | nan ± nan | 1550.350 | 2204.946 | 148.200 | 0.000 | 0.000 / 0.000 | 1.000 / 0.000 / 0.000 | 683.500 | 143.650 (143.650 / 43.300 / 3.500) | 143.600 / 0.000 / 0.000 | 0.000 (0.000 / 0.000) | 370.850 | 0.000 | 0.00 |
| collude | 6322.9 ± 162.6 | 2567.6 ± 208.9 | 3617.086 | 2705.773 | 150.900 | 1.000 | 146.500 / 2.700 | 0.000 / 1.000 / 0.000 | 684.300 | 147.150 (147.150 / 40.600 / 2.200) | 0.000 / 147.050 / 0.000 | 147.050 (145.550 / 0.000) | 27.850 | 0.000 | 0.00 |

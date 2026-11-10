# Evaluation (Q4, the pair) — cell `--entry-pool 20 --stampers 0.6 --rules 2.7.0 --p-floor 0.2 --p-halve-every 5`, seeds 21-40, model `results/redteam/Q4/line-v4b/models/wm-online-10.pt` (value mc, horizon 16)

The pair's lifetime real wealth (the deliverer's and the reviewer's, as one), paired against the careful pair; the deliverer's bad share and what became of its bad work; the reviewer's verdicts (care / approve blind / reject blind) over all its reviews, and on the deliverer's cases apart (matched in the calibration, blind in the line).

| policy | pair lifetime real | paired − careful | D real | R real | work decisions | bad share | bad approved / caught | R care / approve / reject | R reviews | D's cases R took (matched / waited / unmatched) | R on D's cases: care / stamp / reject | bad stamped (vested / caught) | forfeited | R suspensions | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 4562.8 ± 160.6 | nan ± nan | 1292.737 | 3270.047 | 128.000 | 0.010 | 0.100 / 0.700 | 0.728 / 0.272 / 0.000 | 758.350 | 18.550 (0.000 / 0.000 / 0.000) | 16.750 / 1.750 / 0.000 | 0.500 (0.000 / 0.000) | 287.850 | 0.100 | 0.05 |

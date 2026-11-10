# Evaluation (Q4, the pair) — cell `--entry-pool 20 --stampers 0.6 --rules 2.8.0 --p-floor 0.2 --p-halve-every 5`, seeds 21-40, model `results/redteam/Q4/line-v4b/models/wm-online-10.pt` (value mc, horizon 16)

The pair's lifetime real wealth (the deliverer's and the reviewer's, as one), paired against the careful pair; the deliverer's bad share and what became of its bad work; the reviewer's verdicts (care / approve blind / reject blind) over all its reviews, and on the deliverer's cases apart (matched in the calibration, blind in the line).

| policy | pair lifetime real | paired − careful | D real | R real | work decisions | bad share | bad approved / caught | R care / approve / reject | R reviews | D's cases R took (matched / waited / unmatched) | R on D's cases: care / stamp / reject | bad stamped (vested / caught) | forfeited | R suspensions | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 3889.5 ± 297.3 | nan ± nan | 1419.228 | 2470.300 | 111.850 | 0.018 | 0.100 / 0.700 | 0.731 / 0.268 / 0.001 | 561.650 | 13.100 (0.000 / 0.000 / 0.000) | 11.550 / 1.550 / 0.000 | 0.200 (0.000 / 0.000) | 225.450 | 0.300 | 0.20 |

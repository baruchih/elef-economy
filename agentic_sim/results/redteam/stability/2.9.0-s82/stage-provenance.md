# The plant kind's state-seat stage on record — before and after the driver's correction (30f280474)

Produced by `2.9.0-s82/restage_read.py` over the evaluations of record and their re-reads (`restage.py`, `restage.sh`) and the pairings produced again (`restage_pair.sh`). The column: the plant kind's `state seats` in a stage table (`life_plant_state_seats`: the state's verdicts on a plant after a member's first seat, per plant so seated; the period-matched table's plant row `state_seats`). Before the correction a planted approval's state seats were filed under it with no seated count; after, a planted approval is skipped (its stages are the `pa_*` readings'). The real kind's `state seats per real root` never carried one and is unchanged. The re-read found two further columns of the plant kind that the planted approvals had joined, in the cells where disputes are on alone: a planted approval there is disputed first (§68), and its dispute was filed under the plant kind's `filed share` (`life_plant_filing_share`) and its panel's wait under `panel wait` (`life_plant_panel_wait`); section 2b lists them. No other summary figure of any re-read differs from the record but the four suspension-count keys of the driver's log, corrected at 4df18f1bc (notes §109) and counted apart.


## 1. The notes

One place quotes the column: §108's seam paragraph (`results/studies/2.7.0-notes-for-reviewer.md`), which states the correction with the figures before and after for the G3 cell and seed 21's hand run. No other section quotes the plant kind's state-seat stage; the `state seats per real root` rows in §83, §84 and §88's tables are the real kind's.


## 2. The evaluations' stage tables (`eval.md`, `eval.json`)

| evaluation | policy | before | after | other keys moved | note |
|---|---|---|---|---|---|
| ablation-A1/detection/arm2/frozen-d0.1 | direct | 0.190 | 0.190 | 0 | re-read |
| ablation-A1/detection/arm2/frozen-d0.1 | careful | 0.178 | 0.178 | 0 | re-read |
| ablation-A1/detection/arm2/frozen-d0.1 | hand | 0.059 | 0.059 | 0 | re-read |
| ablation-A1/detection/arm2/frozen-d0.25 | direct | 0.199 | 0.199 | 0 | re-read |
| ablation-A1/detection/arm2/frozen-d0.25 | careful | 0.193 | 0.193 | 0 | re-read |
| ablation-A1/detection/arm2/frozen-d0.25 | hand | 0.080 | 0.080 | 0 | re-read |
| ablation-A1/detection/arm2/frozen-wm-d0.1 | greedy | 0.175 | 0.175 | 0 | re-read |
| ablation-A1/detection/arm2/frozen-wm-d0.1 | careful | 0.178 | 0.178 | 0 | re-read |
| ablation-A1/detection/arm2/frozen-wm-d0.25 | greedy | 0.189 | 0.189 | 0 | re-read |
| ablation-A1/detection/arm2/frozen-wm-d0.25 | careful | 0.193 | 0.193 | 0 | re-read |
| ablation-A1/detection/frozen-d0.1 | direct | 0.314 | 0.302 | 2 (life_plant_filing_share, life_plant_panel_wait) | re-read |
| ablation-A1/detection/frozen-d0.1 | careful | 0.235 | 0.227 | 2 (life_plant_filing_share, life_plant_panel_wait) | re-read |
| ablation-A1/detection/frozen-d0.1 | hand | 0.228 | 0.226 | 2 (life_plant_filing_share, life_plant_panel_wait) | re-read |
| ablation-A1/detection/frozen-d0.25 | direct | 0.346 | 0.324 | 2 (life_plant_filing_share, life_plant_panel_wait) | re-read |
| ablation-A1/detection/frozen-d0.25 | careful | 0.262 | 0.245 | 2 (life_plant_filing_share, life_plant_panel_wait) | re-read |
| ablation-A1/detection/frozen-d0.25 | hand | 0.216 | 0.214 | 2 (life_plant_filing_share, life_plant_panel_wait) | re-read |
| ablation-A1/detection/frozen2-d0.1 | direct | 0.314 | 0.302 | 2 (life_plant_filing_share, life_plant_panel_wait) | re-read |
| ablation-A1/detection/frozen2-d0.1 | careful | 0.235 | 0.227 | 2 (life_plant_filing_share, life_plant_panel_wait) | re-read |
| ablation-A1/detection/frozen2-d0.1 | hand | 0.228 | 0.226 | 2 (life_plant_filing_share, life_plant_panel_wait) | re-read |
| ablation-A1/detection/frozen2-d0.25 | direct | 0.346 | 0.324 | 2 (life_plant_filing_share, life_plant_panel_wait) | re-read |
| ablation-A1/detection/frozen2-d0.25 | careful | 0.262 | 0.245 | 2 (life_plant_filing_share, life_plant_panel_wait) | re-read |
| ablation-A1/detection/frozen2-d0.25 | hand | 0.216 | 0.214 | 2 (life_plant_filing_share, life_plant_panel_wait) | re-read |
| ablation-A1/detection/retrain-d0.1/direct/eval/final | direct | 0.301 | 0.289 | 2 (life_plant_filing_share, life_plant_panel_wait) | re-read |
| ablation-A1/detection/retrain-d0.1/direct/eval/final | careful | 0.235 | 0.227 | 2 (life_plant_filing_share, life_plant_panel_wait) | re-read |
| ablation-A1/detection/retrain-d0.1/direct/eval/final | stamper | 1.789 | 1.789 | 0 | re-read |
| ablation-A1/detection/retrain-d0.1/direct/eval/final | hand | 0.228 | 0.226 | 2 (life_plant_filing_share, life_plant_panel_wait) | re-read |
| ablation-A1/detection/retrain-d0.1/wm/eval/final | greedy | 0.345 | 0.335 | 2 (life_plant_filing_share, life_plant_panel_wait) | re-read |
| ablation-A1/detection/retrain-d0.1/wm/eval/final | careful | 0.235 | 0.227 | 2 (life_plant_filing_share, life_plant_panel_wait) | re-read |
| ablation-A1/detection/retrain-d0.1/wm/eval/final | stamper | 1.789 | 1.789 | 0 | re-read |
| ablation-A1/detection/retrain-d0.1/wm/eval/final | hand | 0.228 | 0.226 | 2 (life_plant_filing_share, life_plant_panel_wait) | re-read |
| ablation-A1/detection/retrain-d0.25/direct/eval/final | direct | 0.317 | 0.297 | 2 (life_plant_filing_share, life_plant_panel_wait) | re-read |
| ablation-A1/detection/retrain-d0.25/direct/eval/final | careful | 0.262 | 0.245 | 2 (life_plant_filing_share, life_plant_panel_wait) | re-read |
| ablation-A1/detection/retrain-d0.25/direct/eval/final | stamper | 1.824 | 1.824 | 0 | re-read |
| ablation-A1/detection/retrain-d0.25/direct/eval/final | hand | 0.216 | 0.214 | 2 (life_plant_filing_share, life_plant_panel_wait) | re-read |
| ablation-A1/detection/retrain-d0.25/wm/eval/final | greedy | 0.310 | 0.294 | 2 (life_plant_filing_share, life_plant_panel_wait) | re-read |
| ablation-A1/detection/retrain-d0.25/wm/eval/final | careful | 0.262 | 0.245 | 2 (life_plant_filing_share, life_plant_panel_wait) | re-read |
| ablation-A1/detection/retrain-d0.25/wm/eval/final | stamper | 1.824 | 1.824 | 0 | re-read |
| ablation-A1/detection/retrain-d0.25/wm/eval/final | hand | 0.216 | 0.214 | 2 (life_plant_filing_share, life_plant_panel_wait) | re-read |
| ablation-A1/learned/arm0-carried/direct/eval/final | direct | 0.134 | 0.130 | 0 | re-read |
| ablation-A1/learned/arm0-carried/direct/eval/final | careful | 0.134 | 0.129 | 0 | re-read |
| ablation-A1/learned/arm0-carried/direct/eval/final | stamper | 1.741 | 1.741 | 0 | re-read |
| ablation-A1/learned/arm0-carried/direct/eval/final | hand | 0.214 | 0.206 | 0 | re-read |
| ablation-A1/learned/arm0-carried/wm/eval/final | greedy | 0.167 | 0.160 | 0 | re-read |
| ablation-A1/learned/arm0-carried/wm/eval/final | careful | 0.165 | 0.155 | 0 | re-read |
| ablation-A1/learned/arm0-carried/wm/eval/final | stamper | 1.757 | 1.757 | 0 | re-read |
| ablation-A1/learned/arm0-carried/wm/eval/final | hand | 0.220 | 0.214 | 0 | re-read |
| ablation-A1/learned/arm1c/direct/eval/final | direct | 0.295 | 0.290 | 0 | re-read |
| ablation-A1/learned/arm1c/direct/eval/final | careful | 0.242 | 0.237 | 0 | re-read |
| ablation-A1/learned/arm1c/direct/eval/final | stamper | 1.734 | 1.734 | 0 | re-read |
| ablation-A1/learned/arm1c/direct/eval/final | hand | 0.219 | 0.218 | 0 | re-read |
| ablation-A1/learned/arm1c/wm/eval/final | greedy | 0.283 | 0.278 | 0 | re-read |
| ablation-A1/learned/arm1c/wm/eval/final | careful | 0.242 | 0.237 | 0 | re-read |
| ablation-A1/learned/arm1c/wm/eval/final | stamper | 1.734 | 1.734 | 0 | re-read |
| ablation-A1/learned/arm1c/wm/eval/final | hand | 0.219 | 0.218 | 0 | re-read |
| ablation-A1/learned/arm2-stamper/direct/eval/final | direct | 0.176 | 0.176 | 0 | re-read |
| ablation-A1/learned/arm2-stamper/direct/eval/final | careful | 0.174 | 0.174 | 0 | re-read |
| ablation-A1/learned/arm2-stamper/direct/eval/final | stamper | 0.064 | 0.064 | 0 | re-read |
| ablation-A1/learned/arm2-stamper/direct/eval/final | hand | 0.042 | 0.042 | 0 | re-read |
| ablation-A1/learned/arm2-stamper/wm/eval/final | greedy | 0.172 | 0.172 | 0 | re-read |
| ablation-A1/learned/arm2-stamper/wm/eval/final | careful | 0.174 | 0.174 | 0 | re-read |
| ablation-A1/learned/arm2-stamper/wm/eval/final | stamper | 0.064 | 0.064 | 0 | re-read |
| ablation-A1/learned/arm2-stamper/wm/eval/final | hand | 0.042 | 0.042 | 0 | re-read |
| ablation-A1/learned/arm2/direct/eval/final | direct | 0.195 | 0.195 | 0 | re-read |
| ablation-A1/learned/arm2/direct/eval/final | careful | 0.174 | 0.174 | 0 | re-read |
| ablation-A1/learned/arm2/direct/eval/final | stamper | 0.064 | 0.064 | 0 | re-read |
| ablation-A1/learned/arm2/direct/eval/final | hand | 0.042 | 0.042 | 0 | re-read |
| ablation-A1/learned/arm2/wm/eval/final | greedy | 0.172 | 0.172 | 0 | re-read |
| ablation-A1/learned/arm2/wm/eval/final | careful | 0.174 | 0.174 | 0 | re-read |
| ablation-A1/learned/arm2/wm/eval/final | stamper | 0.064 | 0.064 | 0 | re-read |
| ablation-A1/learned/arm2/wm/eval/final | hand | 0.042 | 0.042 | 0 | re-read |
| ablation-A1/learned/arm4-stamper/direct/eval/final | direct | 0.000 | 0.000 | 0 | re-read |
| ablation-A1/learned/arm4-stamper/direct/eval/final | careful | 0.000 | 0.000 | 0 | re-read |
| ablation-A1/learned/arm4-stamper/direct/eval/final | stamper | 0.000 | 0.000 | 0 | re-read |
| ablation-A1/learned/arm4-stamper/direct/eval/final | hand | 0.000 | 0.000 | 0 | re-read |
| ablation-A1/learned/arm4-stamper/wm/eval/final | greedy | 0.000 | 0.000 | 0 | re-read |
| ablation-A1/learned/arm4-stamper/wm/eval/final | careful | 0.000 | 0.000 | 0 | re-read |
| ablation-A1/learned/arm4-stamper/wm/eval/final | stamper | 0.000 | 0.000 | 0 | re-read |
| ablation-A1/learned/arm4-stamper/wm/eval/final | hand | 0.000 | 0.000 | 0 | re-read |
| ablation-A1/learned/arm4/direct/eval/final | direct | 0.000 | 0.000 | 0 | re-read |
| ablation-A1/learned/arm4/direct/eval/final | careful | 0.000 | 0.000 | 0 | re-read |
| ablation-A1/learned/arm4/direct/eval/final | stamper | 0.000 | 0.000 | 0 | re-read |
| ablation-A1/learned/arm4/direct/eval/final | hand | 0.000 | 0.000 | 0 | re-read |
| ablation-A1/learned/arm4/wm/eval/final | greedy | 0.000 | 0.000 | 0 | re-read |
| ablation-A1/learned/arm4/wm/eval/final | careful | 0.000 | 0.000 | 0 | re-read |
| ablation-A1/learned/arm4/wm/eval/final | stamper | 0.000 | 0.000 | 0 | re-read |
| ablation-A1/learned/arm4/wm/eval/final | hand | 0.000 | 0.000 | 0 | re-read |
| ablation-A1/learned/pa10-stamper/direct/eval/final | direct | 0.285 | 0.255 | 0 | re-read |
| ablation-A1/learned/pa10-stamper/direct/eval/final | careful | 0.280 | 0.249 | 0 | re-read |
| ablation-A1/learned/pa10-stamper/direct/eval/final | stamper | 1.769 | 1.769 | 0 | re-read |
| ablation-A1/learned/pa10-stamper/direct/eval/final | hand | 0.237 | 0.228 | 0 | re-read |
| ablation-A1/learned/pa10-stamper/wm/eval/final | greedy | 0.293 | 0.259 | 0 | re-read |
| ablation-A1/learned/pa10-stamper/wm/eval/final | careful | 0.280 | 0.249 | 0 | re-read |
| ablation-A1/learned/pa10-stamper/wm/eval/final | stamper | 1.769 | 1.769 | 0 | re-read |
| ablation-A1/learned/pa10-stamper/wm/eval/final | hand | 0.237 | 0.228 | 0 | re-read |
| ablation-A1/learned/pa10/direct/eval/final | direct | 0.316 | 0.288 | 0 | re-read |
| ablation-A1/learned/pa10/direct/eval/final | careful | 0.280 | 0.249 | 0 | re-read |
| ablation-A1/learned/pa10/direct/eval/final | stamper | 1.769 | 1.769 | 0 | re-read |
| ablation-A1/learned/pa10/direct/eval/final | hand | 0.237 | 0.228 | 0 | re-read |
| ablation-A1/learned/pa10/wm/eval/final | greedy | 0.310 | 0.278 | 0 | re-read |
| ablation-A1/learned/pa10/wm/eval/final | careful | 0.280 | 0.249 | 0 | re-read |
| ablation-A1/learned/pa10/wm/eval/final | stamper | 1.769 | 1.769 | 0 | re-read |
| ablation-A1/learned/pa10/wm/eval/final | hand | 0.237 | 0.228 | 0 | re-read |
| ablation-A1/learned/pa20/direct/eval/final | direct | 0.300 | 0.261 | 0 | re-read |
| ablation-A1/learned/pa20/direct/eval/final | careful | 0.315 | 0.260 | 0 | re-read |
| ablation-A1/learned/pa20/direct/eval/final | stamper | 1.757 | 1.757 | 0 | re-read |
| ablation-A1/learned/pa20/direct/eval/final | hand | 0.238 | 0.226 | 0 | re-read |
| ablation-A1/learned/pa20/wm/eval/final | greedy | 0.283 | 0.242 | 0 | re-read |
| ablation-A1/learned/pa20/wm/eval/final | careful | 0.315 | 0.260 | 0 | re-read |
| ablation-A1/learned/pa20/wm/eval/final | stamper | 1.757 | 1.757 | 0 | re-read |
| ablation-A1/learned/pa20/wm/eval/final | hand | 0.238 | 0.226 | 0 | re-read |
| ablation-A1/stress/entry/arm4-direct-s0.1 | mix:direct:0.1 | 0.000 | 0.000 | 0 | re-read |
| ablation-A1/stress/entry/arm4-direct-s0.25 | mix:direct:0.25 | 0.000 | 0.000 | 0 | re-read |
| ablation-A1/stress/entry/arm4-direct-s0.75 | mix:direct:0.75 | 0.000 | 0.000 | 0 | re-read |
| ablation-A1/stress/entry/arm4-wm-s0.1 | mix:greedy:0.1 | 0.000 | 0.000 | 0 | re-read |
| ablation-A1/stress/entry/arm4-wm-s0.25 | mix:greedy:0.25 | 0.000 | 0.000 | 0 | re-read |
| ablation-A1/stress/entry/arm4-wm-s0.75 | mix:greedy:0.75 | 0.000 | 0.000 | 0 | re-read |
| ablation-A1/stress/entry/pa10-direct-s0.1 | mix:direct:0.1 | 0.210 | 0.210 | 0 | re-read |
| ablation-A1/stress/entry/pa10-direct-s0.25 | mix:direct:0.25 | 0.159 | 0.159 | 0 | re-read |
| ablation-A1/stress/entry/pa10-direct-s0.75 | mix:direct:0.75 | 0.279 | 0.279 | 0 | re-read |
| ablation-A1/stress/entry/pa10-wm-s0.1 | mix:greedy:0.1 | 0.191 | 0.191 | 0 | re-read |
| ablation-A1/stress/entry/pa10-wm-s0.25 | mix:greedy:0.25 | 0.159 | 0.159 | 0 | re-read |
| ablation-A1/stress/entry/pa10-wm-s0.75 | mix:greedy:0.75 | 0.248 | 0.248 | 0 | re-read |
| ablation-A1/stress/f41/arm2-direct | mix:direct | 0.047 | 0.047 | 0 | re-read |
| ablation-A1/stress/f41/arm2-wm | mix:greedy | 0.042 | 0.042 | 0 | re-read |
| ablation-A1/stress/f41/arm4-direct | mix:direct | 0.000 | 0.000 | 0 | re-read |
| ablation-A1/stress/f41/arm4-wm | mix:greedy | 0.000 | 0.000 | 0 | re-read |
| ablation-A1/stress/f41/pa10-direct | mix:direct | 0.151 | 0.145 | 0 | re-read |
| ablation-A1/stress/f41/pa10-wm | mix:greedy | 0.167 | 0.160 | 0 | re-read |
| ablation-A1/stress/learned/arm2-t1-b1/direct/eval/final-r7 | direct | 0.089 | 0.089 | 0 | re-read |
| ablation-A1/stress/learned/arm2-t1-b1/direct/eval/final-r7 | careful | 0.174 | 0.174 | 0 | re-read |
| ablation-A1/stress/learned/arm2-t1-b1/direct/eval/final-r7 | claimer | 0.061 | 0.061 | 0 | re-read |
| ablation-A1/stress/learned/arm2-t1-b1/direct/eval/final-r7b | direct | 0.089 | 0.089 | 0 | re-read |
| ablation-A1/stress/learned/arm2-t1-b1/direct/eval/final | direct | 0.089 | 0.089 | 0 | re-read |
| ablation-A1/stress/learned/arm2-t1-b1/direct/eval/final | careful | 0.174 | 0.174 | 0 | re-read |
| ablation-A1/stress/learned/arm2-t1-b1/direct/eval/final | stamper | 0.064 | 0.064 | 0 | re-read |
| ablation-A1/stress/learned/arm2-t1-b1/direct/eval/final | claimer | 0.061 | 0.061 | 0 | re-read |
| ablation-A1/stress/learned/arm2-t1-b1/direct/eval/final | hand | 0.042 | 0.042 | 0 | re-read |
| ablation-A1/stress/learned/arm2-t1-b1/wm/eval/final-r7 | greedy | 0.052 | 0.052 | 0 | re-read |
| ablation-A1/stress/learned/arm2-t1-b1/wm/eval/final-r7 | careful | 0.174 | 0.174 | 0 | re-read |
| ablation-A1/stress/learned/arm2-t1-b1/wm/eval/final-r7b | greedy | 0.052 | 0.052 | 0 | re-read |
| ablation-A1/stress/learned/arm2-t1-b1/wm/eval/final | greedy | 0.052 | 0.052 | 0 | re-read |
| ablation-A1/stress/learned/arm2-t1-b1/wm/eval/final | careful | 0.174 | 0.174 | 0 | re-read |
| ablation-A1/stress/learned/arm2-t1-b1/wm/eval/final | stamper | 0.064 | 0.064 | 0 | re-read |
| ablation-A1/stress/learned/arm2-t1-b1/wm/eval/final | claimer | 0.061 | 0.061 | 0 | re-read |
| ablation-A1/stress/learned/arm2-t1-b1/wm/eval/final | hand | 0.042 | 0.042 | 0 | re-read |
| ablation-A1/stress/learned/arm4-t1-b1-gv10/direct/eval/final | direct | 0.000 | 0.000 | 0 | re-read |
| ablation-A1/stress/learned/arm4-t1-b1-gv10/direct/eval/final | careful | 0.000 | 0.000 | 0 | re-read |
| ablation-A1/stress/learned/arm4-t1-b1-gv10/direct/eval/final | stamper | 0.000 | 0.000 | 0 | re-read |
| ablation-A1/stress/learned/arm4-t1-b1-gv10/direct/eval/final | claimer | 0.000 | 0.000 | 0 | re-read |
| ablation-A1/stress/learned/arm4-t1-b1-gv10/direct/eval/final | hand | 0.000 | 0.000 | 0 | re-read |
| ablation-A1/stress/learned/arm4-t1-b1-gv10/wm/eval/final | greedy | 0.000 | 0.000 | 0 | re-read |
| ablation-A1/stress/learned/arm4-t1-b1-gv10/wm/eval/final | careful | 0.000 | 0.000 | 0 | re-read |
| ablation-A1/stress/learned/arm4-t1-b1-gv10/wm/eval/final | stamper | 0.000 | 0.000 | 0 | re-read |
| ablation-A1/stress/learned/arm4-t1-b1-gv10/wm/eval/final | claimer | 0.000 | 0.000 | 0 | re-read |
| ablation-A1/stress/learned/arm4-t1-b1-gv10/wm/eval/final | hand | 0.000 | 0.000 | 0 | re-read |
| ablation-A1/stress/learned/arm4-t1-b1/direct/eval/final-r7 | direct | 0.000 | 0.000 | 0 | re-read |
| ablation-A1/stress/learned/arm4-t1-b1/direct/eval/final-r7 | careful | 0.000 | 0.000 | 0 | re-read |
| ablation-A1/stress/learned/arm4-t1-b1/direct/eval/final-r7 | claimer | 0.000 | 0.000 | 0 | re-read |
| ablation-A1/stress/learned/arm4-t1-b1/direct/eval/final-r7b | direct | 0.000 | 0.000 | 0 | re-read |
| ablation-A1/stress/learned/arm4-t1-b1/direct/eval/final | direct | 0.000 | 0.000 | 0 | re-read |
| ablation-A1/stress/learned/arm4-t1-b1/direct/eval/final | careful | 0.000 | 0.000 | 0 | re-read |
| ablation-A1/stress/learned/arm4-t1-b1/direct/eval/final | stamper | 0.000 | 0.000 | 0 | re-read |
| ablation-A1/stress/learned/arm4-t1-b1/direct/eval/final | claimer | 0.000 | 0.000 | 0 | re-read |
| ablation-A1/stress/learned/arm4-t1-b1/direct/eval/final | hand | 0.000 | 0.000 | 0 | re-read |
| ablation-A1/stress/learned/arm4-t1-b1/wm/eval/final-r7 | greedy | 0.000 | 0.000 | 0 | re-read |
| ablation-A1/stress/learned/arm4-t1-b1/wm/eval/final-r7 | careful | 0.000 | 0.000 | 0 | re-read |
| ablation-A1/stress/learned/arm4-t1-b1/wm/eval/final-r7b | greedy | 0.000 | 0.000 | 0 | re-read |
| ablation-A1/stress/learned/arm4-t1-b1/wm/eval/final | greedy | 0.000 | 0.000 | 0 | re-read |
| ablation-A1/stress/learned/arm4-t1-b1/wm/eval/final | careful | 0.000 | 0.000 | 0 | re-read |
| ablation-A1/stress/learned/arm4-t1-b1/wm/eval/final | stamper | 0.000 | 0.000 | 0 | re-read |
| ablation-A1/stress/learned/arm4-t1-b1/wm/eval/final | claimer | 0.000 | 0.000 | 0 | re-read |
| ablation-A1/stress/learned/arm4-t1-b1/wm/eval/final | hand | 0.000 | 0.000 | 0 | re-read |
| ablation-A1/stress/learned/pa10-t1-b1/direct/eval/final-r7 | direct | 0.613 | 0.601 | 0 | re-read |
| ablation-A1/stress/learned/pa10-t1-b1/direct/eval/final-r7 | careful | 0.280 | 0.249 | 0 | re-read |
| ablation-A1/stress/learned/pa10-t1-b1/direct/eval/final-r7 | claimer | 1.758 | 1.758 | 0 | re-read |
| ablation-A1/stress/learned/pa10-t1-b1/direct/eval/final-r7b | direct | 0.613 | 0.601 | 0 | re-read |
| ablation-A1/stress/learned/pa10-t1-b1/direct/eval/final | direct | 0.613 | 0.601 | 0 | re-read |
| ablation-A1/stress/learned/pa10-t1-b1/direct/eval/final | careful | 0.280 | 0.249 | 0 | re-read |
| ablation-A1/stress/learned/pa10-t1-b1/direct/eval/final | stamper | 1.769 | 1.769 | 0 | re-read |
| ablation-A1/stress/learned/pa10-t1-b1/direct/eval/final | claimer | 1.758 | 1.758 | 0 | re-read |
| ablation-A1/stress/learned/pa10-t1-b1/direct/eval/final | hand | 0.237 | 0.228 | 0 | re-read |
| ablation-A1/stress/learned/pa10-t1-b1/wm/eval/final-r7 | greedy | 0.533 | 0.526 | 0 | re-read |
| ablation-A1/stress/learned/pa10-t1-b1/wm/eval/final-r7 | careful | 0.280 | 0.249 | 0 | re-read |
| ablation-A1/stress/learned/pa10-t1-b1/wm/eval/final-r7b | greedy | 0.533 | 0.526 | 0 | re-read |
| ablation-A1/stress/learned/pa10-t1-b1/wm/eval/final | greedy | 0.533 | 0.526 | 0 | re-read |
| ablation-A1/stress/learned/pa10-t1-b1/wm/eval/final | careful | 0.280 | 0.249 | 0 | re-read |
| ablation-A1/stress/learned/pa10-t1-b1/wm/eval/final | stamper | 1.769 | 1.769 | 0 | re-read |
| ablation-A1/stress/learned/pa10-t1-b1/wm/eval/final | claimer | 1.758 | 1.758 | 0 | re-read |
| ablation-A1/stress/learned/pa10-t1-b1/wm/eval/final | hand | 0.237 | 0.228 | 0 | re-read |
| ablation-A1/stress/learned/pa20-t1-b6-gv20/direct/eval/final | direct | 0.307 | 0.307 | 0 | re-read |
| ablation-A1/stress/learned/pa20-t1-b6-gv20/direct/eval/final | careful | 0.278 | 0.278 | 0 | re-read |
| ablation-A1/stress/learned/pa20-t1-b6-gv20/direct/eval/final | stamper | 1.750 | 1.750 | 0 | re-read |
| ablation-A1/stress/learned/pa20-t1-b6-gv20/direct/eval/final | claimer | 1.769 | 1.769 | 0 | re-read |
| ablation-A1/stress/learned/pa20-t1-b6-gv20/direct/eval/final | hand | 0.207 | 0.207 | 0 | re-read |
| ablation-A1/stress/learned/pa20-t1-b6-gv20/wm/eval/final | greedy | 0.230 | 0.230 | 0 | re-read |
| ablation-A1/stress/learned/pa20-t1-b6-gv20/wm/eval/final | careful | 0.278 | 0.278 | 0 | re-read |
| ablation-A1/stress/learned/pa20-t1-b6-gv20/wm/eval/final | stamper | 1.750 | 1.750 | 0 | re-read |
| ablation-A1/stress/learned/pa20-t1-b6-gv20/wm/eval/final | claimer | 1.769 | 1.769 | 0 | re-read |
| ablation-A1/stress/learned/pa20-t1-b6-gv20/wm/eval/final | hand | 0.207 | 0.207 | 0 | re-read |
| ablation-A1/stress/payoff/honest/arm2-t1-b1-gv10 | careful | 0.181 | 0.181 | 0 | re-read |
| ablation-A1/stress/payoff/honest/arm2-t1-b1-gv20 | careful | 0.169 | 0.169 | 0 | re-read |
| ablation-A1/stress/payoff/honest/arm2-t2-b1-gv10 | careful | 0.181 | 0.181 | 0 | re-read |
| ablation-A1/stress/payoff/honest/arm2-t2-b1-gv20 | careful | 0.169 | 0.169 | 0 | re-read |
| ablation-A1/stress/payoff/honest/arm4-t1-b1-gv10 | careful | 0.000 | 0.000 | 0 | re-read |
| ablation-A1/stress/payoff/honest/arm4-t1-b1-gv20 | careful | 0.000 | 0.000 | 0 | re-read |
| ablation-A1/stress/payoff/honest/arm4-t2-b1-gv10 | careful | 0.000 | 0.000 | 0 | re-read |
| ablation-A1/stress/payoff/honest/arm4-t2-b1-gv20 | careful | 0.000 | 0.000 | 0 | re-read |
| ablation-A1/stress/payoff/honest/pa10-t1-b1-gv10 | careful | 0.282 | 0.258 | 0 | re-read |
| ablation-A1/stress/payoff/honest/pa10-t1-b1-gv20 | careful | 0.331 | 0.301 | 0 | re-read |
| ablation-A1/stress/payoff/honest/pa10-t1-b1 | careful | 0.293 | 0.262 | 0 | re-read |
| ablation-A1/stress/payoff/honest/pa10-t1-b6-w3 | careful | 0.310 | 0.285 | 0 | re-read |
| ablation-A1/stress/payoff/honest/pa10-t1-b6 | careful | 0.289 | 0.270 | 0 | re-read |
| ablation-A1/stress/payoff/honest/pa10-t1-b8-w3 | careful | 0.309 | 0.287 | 0 | re-read |
| ablation-A1/stress/payoff/honest/pa10-t1-b8 | careful | 0.308 | 0.287 | 0 | re-read |
| ablation-A1/stress/payoff/honest/pa10-t2-b1-gv10 | careful | 0.282 | 0.258 | 0 | re-read |
| ablation-A1/stress/payoff/honest/pa10-t2-b1-gv20 | careful | 0.331 | 0.301 | 0 | re-read |
| ablation-A1/stress/payoff/honest/pa10-t2-b6-w3 | careful | 0.310 | 0.285 | 0 | re-read |
| ablation-A1/stress/payoff/honest/pa10-t2-b6 | careful | 0.289 | 0.270 | 0 | re-read |
| ablation-A1/stress/payoff/honest/pa10-t2-b8-w3 | careful | 0.309 | 0.287 | 0 | re-read |
| ablation-A1/stress/payoff/honest/pa10-t2-b8 | careful | 0.308 | 0.287 | 0 | re-read |
| ablation-A1/stress/payoff/honest/pa20-t1-b1 | careful | 0.322 | 0.269 | 0 | re-read |
| ablation-A1/stress/payoff/honest/pa20-t1-b2-w3 | careful | 0.236 | 0.236 | 0 | re-read |
| ablation-A1/stress/payoff/honest/pa20-t1-b2 | careful | 0.239 | 0.239 | 0 | re-read |
| ablation-A1/stress/payoff/honest/pa20-t1-b4-w3 | careful | 0.249 | 0.249 | 0 | re-read |
| ablation-A1/stress/payoff/honest/pa20-t1-b4 | careful | 0.354 | 0.312 | 0 | re-read |
| ablation-A1/stress/payoff/honest/pa20-t1-b6-w3 | careful | 0.336 | 0.283 | 0 | re-read |
| ablation-A1/stress/payoff/honest/pa20-t1-b6 | careful | 0.326 | 0.281 | 0 | re-read |
| ablation-A1/stress/payoff/honest/pa20-t1-b8-w3 | careful | 0.362 | 0.319 | 0 | re-read |
| ablation-A1/stress/payoff/honest/pa20-t1-b8 | careful | 0.358 | 0.319 | 0 | re-read |
| ablation-A1/stress/payoff/honest/pa20-t2-b1 | careful | 0.322 | 0.269 | 0 | re-read |
| ablation-A1/stress/payoff/honest/pa20-t2-b4 | careful | 0.354 | 0.312 | 0 | re-read |
| ablation-A1/stress/payoff/honest/pa20-t2-b6-w3 | careful | 0.336 | 0.283 | 0 | re-read |
| ablation-A1/stress/payoff/honest/pa20-t2-b6 | careful | 0.326 | 0.281 | 0 | re-read |
| ablation-A1/stress/payoff/honest/pa20-t2-b8-w3 | careful | 0.362 | 0.319 | 0 | re-read |
| ablation-A1/stress/payoff/honest/pa20-t2-b8 | careful | 0.358 | 0.319 | 0 | re-read |
| ablation-A1/stress/payoff/honest/pa30-t1-b1-w3 | careful | 0.234 | 0.234 | 0 | re-read |
| ablation-A1/stress/payoff/honest/pa30-t1-b1 | careful | 0.241 | 0.241 | 0 | re-read |
| ablation-A1/stress/payoff/honest/pa30-t1-b2-w3 | careful | 0.230 | 0.230 | 0 | re-read |
| ablation-A1/stress/payoff/honest/pa30-t1-b2 | careful | 0.259 | 0.259 | 0 | re-read |
| ablation-A1/stress/payoff/honest/pa30-t1-b4-w3 | careful | 0.276 | 0.276 | 0 | re-read |
| ablation-A1/stress/payoff/honest/pa30-t1-b4 | careful | 0.275 | 0.275 | 0 | re-read |
| cr-finals/hand-old-defaults-290-cr | careful | 0.267 | 0.258 | 0 | re-read |
| cr-finals/hand-old-defaults-290-cr | hand | 0.205 | 0.203 | 0 | re-read |
| cr-finals/hand-old-defaults-liars-cr | careful | 0.454 | 0.417 | 2 (life_plant_filing_share, life_plant_panel_wait) | re-read |
| cr-finals/hand-old-defaults-liars-cr | hand | 0.285 | 0.278 | 2 (life_plant_filing_share, life_plant_panel_wait) | re-read |
| learned-rev-careful-290-own/direct/eval/final-2000 | direct | 0.592 | 0.552 | 0 | re-read |
| learned-rev-careful-290-own/direct/eval/final-2000 | careful | 0.127 | 0.124 | 0 | re-read |
| learned-rev-careful-290-own/direct/eval/final-2000 | hand | 0.140 | 0.139 | 0 | re-read |
| learned-rev-careful-290-own/direct/eval/final-cr | direct | 0.298 | 0.291 | 0 | re-read |
| learned-rev-careful-290-own/direct/eval/final-cr | careful | 0.268 | 0.261 | 0 | re-read |
| learned-rev-careful-290-own/direct/eval/final-cr | stamper | 1.746 | 1.746 | 0 | re-read |
| learned-rev-careful-290-own/direct/eval/final-cr | hand | 0.216 | 0.214 | 0 | re-read |
| learned-rev-careful-290-own/direct/eval/final | direct | 0.285 | ≥ 0.058 (bound) | — | the macOS episode, not re-run |
| learned-rev-careful-290-own/direct/eval/final | careful | 0.256 | ≥ 0.048 (bound) | — | the macOS episode, not re-run |
| learned-rev-careful-290-own/direct/eval/final | stamper | 1.757 | ≥ 1.757 (bound) | — | the macOS episode, not re-run |
| learned-rev-careful-290-own/direct/eval/final | hand | 0.209 | ≥ 0.112 (bound) | — | the macOS episode, not re-run |
| learned-rev-careful-290-own/probe-seats/evals/round-11 | direct | 0.299 | 0.293 | 0 | re-read |
| learned-rev-careful-290-own/probe-seats/evals/round-11 | careful | 0.268 | 0.261 | 0 | re-read |
| learned-rev-careful-290-own/wm/eval/final-2000 | greedy | 0.142 | 0.138 | 0 | re-read |
| learned-rev-careful-290-own/wm/eval/final-2000 | careful | 0.127 | 0.124 | 0 | re-read |
| learned-rev-careful-290-own/wm/eval/final-2000 | hand | 0.140 | 0.139 | 0 | re-read |
| learned-rev-careful-290-own/wm/eval/final-cr | greedy | 0.316 | 0.312 | 0 | re-read |
| learned-rev-careful-290-own/wm/eval/final-cr | careful | 0.268 | 0.261 | 0 | re-read |
| learned-rev-careful-290-own/wm/eval/final-cr | stamper | 1.746 | 1.746 | 0 | re-read |
| learned-rev-careful-290-own/wm/eval/final-cr | hand | 0.216 | 0.214 | 0 | re-read |
| learned-rev-careful-290-own/wm/eval/final | greedy | 0.314 | ≥ 0.099 (bound) | — | the macOS episode, not re-run |
| learned-rev-careful-290-own/wm/eval/final | careful | 0.256 | ≥ 0.048 (bound) | — | the macOS episode, not re-run |
| learned-rev-careful-290-own/wm/eval/final | stamper | 1.757 | ≥ 1.757 (bound) | — | the macOS episode, not re-run |
| learned-rev-careful-290-own/wm/eval/final | hand | 0.209 | ≥ 0.112 (bound) | — | the macOS episode, not re-run |
| learned-rev-careful-290/direct/eval/final | direct | 0.781 | ≥ 0.353 (bound) | — | the macOS episode, not re-run |
| learned-rev-careful-290/direct/eval/final | careful | 0.324 | ≥ 0.000 (bound) | — | the macOS episode, not re-run |
| learned-rev-careful-290/direct/eval/final | stamper | 1.993 | ≥ 1.635 (bound) | — | the macOS episode, not re-run |
| learned-rev-careful-290/direct/eval/final | hand | 0.257 | ≥ 0.014 (bound) | — | the macOS episode, not re-run |
| learned-rev-careful-290/wm/eval/final | greedy | 0.714 | ≥ 0.282 (bound) | — | the macOS episode, not re-run |
| learned-rev-careful-290/wm/eval/final | careful | 0.324 | ≥ 0.000 (bound) | — | the macOS episode, not re-run |
| learned-rev-careful-290/wm/eval/final | stamper | 1.993 | ≥ 1.635 (bound) | — | the macOS episode, not re-run |
| learned-rev-careful-290/wm/eval/final | hand | 0.257 | ≥ 0.014 (bound) | — | the macOS episode, not re-run |
| learned-rev-careful-290b/direct/eval/final | direct | 0.567 | ≥ 0.540 (bound) | — | the macOS episode, not re-run |
| learned-rev-careful-290b/direct/eval/final | careful | 0.256 | ≥ 0.048 (bound) | — | the macOS episode, not re-run |
| learned-rev-careful-290b/direct/eval/final | stamper | 1.757 | ≥ 1.757 (bound) | — | the macOS episode, not re-run |
| learned-rev-careful-290b/direct/eval/final | hand | 0.209 | ≥ 0.112 (bound) | — | the macOS episode, not re-run |
| learned-rev-careful-290b/wm/eval/final | greedy | 0.506 | ≥ 0.477 (bound) | — | the macOS episode, not re-run |
| learned-rev-careful-290b/wm/eval/final | careful | 0.256 | ≥ 0.048 (bound) | — | the macOS episode, not re-run |
| learned-rev-careful-290b/wm/eval/final | stamper | 1.757 | ≥ 1.757 (bound) | — | the macOS episode, not re-run |
| learned-rev-careful-290b/wm/eval/final | hand | 0.209 | ≥ 0.112 (bound) | — | the macOS episode, not re-run |
| learned-rev-careful-A-290/direct/eval/final | direct | 0.408 | ≥ 0.376 (bound) | — | the macOS episode, not re-run |
| learned-rev-careful-A-290/direct/eval/final | careful | 0.137 | ≥ 0.000 (bound) | — | the macOS episode, not re-run |
| learned-rev-careful-A-290/direct/eval/final | stamper | 1.721 | ≥ 1.721 (bound) | — | the macOS episode, not re-run |
| learned-rev-careful-A-290/direct/eval/final | hand | 0.177 | ≥ 0.078 (bound) | — | the macOS episode, not re-run |
| learned-rev-careful-A-290/wm/eval/final | greedy | 0.375 | ≥ 0.340 (bound) | — | the macOS episode, not re-run |
| learned-rev-careful-A-290/wm/eval/final | careful | 0.137 | ≥ 0.000 (bound) | — | the macOS episode, not re-run |
| learned-rev-careful-A-290/wm/eval/final | stamper | 1.721 | ≥ 1.721 (bound) | — | the macOS episode, not re-run |
| learned-rev-careful-A-290/wm/eval/final | hand | 0.177 | ≥ 0.078 (bound) | — | the macOS episode, not re-run |
| learned-rev-half-290-own/direct/eval/final | direct | 0.161 | 0.159 | 0 | re-read |
| learned-rev-half-290-own/direct/eval/final | careful | 0.160 | 0.158 | 0 | re-read |
| learned-rev-half-290-own/direct/eval/final | stamper | 0.353 | 0.352 | 0 | re-read |
| learned-rev-half-290-own/direct/eval/final | hand | 0.216 | 0.214 | 0 | re-read |
| learned-rev-half-290-own/wm/eval/final | greedy | 0.168 | 0.166 | 0 | re-read |
| learned-rev-half-290-own/wm/eval/final | careful | 0.160 | 0.158 | 0 | re-read |
| learned-rev-half-290-own/wm/eval/final | stamper | 0.353 | 0.352 | 0 | re-read |
| learned-rev-half-290-own/wm/eval/final | hand | 0.216 | 0.214 | 0 | re-read |
| learned-rev-half-290/direct/eval/final | direct | 0.173 | ≥ 0.000 (bound) | — | the macOS episode, not re-run |
| learned-rev-half-290/direct/eval/final | careful | 0.161 | ≥ 0.046 (bound) | — | the macOS episode, not re-run |
| learned-rev-half-290/direct/eval/final | stamper | 0.335 | ≥ 0.243 (bound) | — | the macOS episode, not re-run |
| learned-rev-half-290/direct/eval/final | hand | 0.209 | ≥ 0.112 (bound) | — | the macOS episode, not re-run |
| learned-rev-half-290/wm/eval/final | greedy | 0.177 | ≥ 0.017 (bound) | — | the macOS episode, not re-run |
| learned-rev-half-290/wm/eval/final | careful | 0.161 | ≥ 0.046 (bound) | — | the macOS episode, not re-run |
| learned-rev-half-290/wm/eval/final | stamper | 0.335 | ≥ 0.243 (bound) | — | the macOS episode, not re-run |
| learned-rev-half-290/wm/eval/final | hand | 0.209 | ≥ 0.112 (bound) | — | the macOS episode, not re-run |
| learned-rev-liars-290-own/direct/eval/final-cr | direct | 0.406 | 0.369 | 2 (life_plant_filing_share, life_plant_panel_wait) | re-read |
| learned-rev-liars-290-own/direct/eval/final-cr | careful | 0.446 | 0.402 | 2 (life_plant_filing_share, life_plant_panel_wait) | re-read |
| learned-rev-liars-290-own/direct/eval/final-cr | stamper | 1.998 | 1.998 | 0 | re-read |
| learned-rev-liars-290-own/direct/eval/final-cr | hand | 0.293 | 0.285 | 2 (life_plant_filing_share, life_plant_panel_wait) | re-read |
| learned-rev-liars-290-own/direct/eval/final | direct | 0.417 | ≥ 0.231 (bound) | — | the macOS episode, not re-run |
| learned-rev-liars-290-own/direct/eval/final | careful | 0.464 | ≥ 0.271 (bound) | — | the macOS episode, not re-run |
| learned-rev-liars-290-own/direct/eval/final | stamper | 1.999 | ≥ 1.999 (bound) | — | the macOS episode, not re-run |
| learned-rev-liars-290-own/direct/eval/final | hand | 0.273 | ≥ 0.187 (bound) | — | the macOS episode, not re-run |
| learned-rev-liars-290-own/probe-seats/evals/round-11 | direct | 0.443 | 0.404 | 2 (life_plant_filing_share, life_plant_panel_wait) | re-read |
| learned-rev-liars-290-own/probe-seats/evals/round-11 | careful | 0.446 | 0.402 | 2 (life_plant_filing_share, life_plant_panel_wait) | re-read |
| learned-rev-liars-290-own/wm/eval/final-cr | greedy | 0.415 | 0.376 | 2 (life_plant_filing_share, life_plant_panel_wait) | re-read |
| learned-rev-liars-290-own/wm/eval/final-cr | careful | 0.446 | 0.402 | 2 (life_plant_filing_share, life_plant_panel_wait) | re-read |
| learned-rev-liars-290-own/wm/eval/final-cr | stamper | 1.998 | 1.998 | 0 | re-read |
| learned-rev-liars-290-own/wm/eval/final-cr | hand | 0.293 | 0.285 | 2 (life_plant_filing_share, life_plant_panel_wait) | re-read |
| learned-rev-liars-290-own/wm/eval/final | greedy | 0.404 | ≥ 0.213 (bound) | — | the macOS episode, not re-run |
| learned-rev-liars-290-own/wm/eval/final | careful | 0.464 | ≥ 0.271 (bound) | — | the macOS episode, not re-run |
| learned-rev-liars-290-own/wm/eval/final | stamper | 1.999 | ≥ 1.999 (bound) | — | the macOS episode, not re-run |
| learned-rev-liars-290-own/wm/eval/final | hand | 0.273 | ≥ 0.187 (bound) | — | the macOS episode, not re-run |
| learned-rev-liars-290/direct/eval/final | direct | 0.626 | ≥ 0.444 (bound) | — | the macOS episode, not re-run |
| learned-rev-liars-290/direct/eval/final | careful | 0.484 | ≥ 0.047 (bound) | — | the macOS episode, not re-run |
| learned-rev-liars-290/direct/eval/final | stamper | 2.167 | ≥ 1.812 (bound) | — | the macOS episode, not re-run |
| learned-rev-liars-290/direct/eval/final | hand | 0.317 | ≥ 0.128 (bound) | — | the macOS episode, not re-run |
| learned-rev-liars-290/wm/eval/final | greedy | 0.469 | ≥ 0.284 (bound) | — | the macOS episode, not re-run |
| learned-rev-liars-290/wm/eval/final | careful | 0.484 | ≥ 0.047 (bound) | — | the macOS episode, not re-run |
| learned-rev-liars-290/wm/eval/final | stamper | 2.167 | ≥ 1.812 (bound) | — | the macOS episode, not re-run |
| learned-rev-liars-290/wm/eval/final | hand | 0.317 | ≥ 0.128 (bound) | — | the macOS episode, not re-run |
| learned-rev-liars-290b/direct/eval/final | direct | 0.599 | ≥ 0.535 (bound) | — | the macOS episode, not re-run |
| learned-rev-liars-290b/direct/eval/final | careful | 0.464 | ≥ 0.271 (bound) | — | the macOS episode, not re-run |
| learned-rev-liars-290b/direct/eval/final | stamper | 1.999 | ≥ 1.999 (bound) | — | the macOS episode, not re-run |
| learned-rev-liars-290b/direct/eval/final | hand | 0.273 | ≥ 0.187 (bound) | — | the macOS episode, not re-run |
| learned-rev-liars-290b/wm/eval/final | greedy | 0.569 | ≥ 0.508 (bound) | — | the macOS episode, not re-run |
| learned-rev-liars-290b/wm/eval/final | careful | 0.464 | ≥ 0.271 (bound) | — | the macOS episode, not re-run |
| learned-rev-liars-290b/wm/eval/final | stamper | 1.999 | ≥ 1.999 (bound) | — | the macOS episode, not re-run |
| learned-rev-liars-290b/wm/eval/final | hand | 0.273 | ≥ 0.187 (bound) | — | the macOS episode, not re-run |
| learned-rev-picap-290-own/direct/eval/final | direct | 0.048 | 0.048 | 0 | re-read |
| learned-rev-picap-290-own/direct/eval/final | careful | 0.045 | 0.045 | 0 | re-read |
| learned-rev-picap-290-own/direct/eval/final | stamper | 1.748 | 1.748 | 0 | re-read |
| learned-rev-picap-290-own/direct/eval/final | hand | 0.126 | 0.125 | 0 | re-read |
| learned-rev-picap-290-own/wm/eval/final | greedy | 0.042 | 0.042 | 0 | re-read |
| learned-rev-picap-290-own/wm/eval/final | careful | 0.045 | 0.045 | 0 | re-read |
| learned-rev-picap-290-own/wm/eval/final | stamper | 1.748 | 1.748 | 0 | re-read |
| learned-rev-picap-290-own/wm/eval/final | hand | 0.126 | 0.125 | 0 | re-read |
| learned-rev-pifloor-290-own/direct/eval/final | direct | 0.349 | 0.344 | 0 | re-read |
| learned-rev-pifloor-290-own/direct/eval/final | careful | 0.272 | 0.265 | 0 | re-read |
| learned-rev-pifloor-290-own/direct/eval/final | stamper | 1.762 | 1.762 | 0 | re-read |
| learned-rev-pifloor-290-own/direct/eval/final | hand | 0.688 | 0.671 | 0 | re-read |
| learned-rev-pifloor-290-own/wm/eval/final | greedy | 0.354 | 0.351 | 0 | re-read |
| learned-rev-pifloor-290-own/wm/eval/final | careful | 0.272 | 0.265 | 0 | re-read |
| learned-rev-pifloor-290-own/wm/eval/final | stamper | 1.762 | 1.762 | 0 | re-read |
| learned-rev-pifloor-290-own/wm/eval/final | hand | 0.688 | 0.671 | 0 | re-read |
| learned-rev-stamper-290-own/direct/eval/final-cr | direct | 0.300 | 0.294 | 0 | re-read |
| learned-rev-stamper-290-own/direct/eval/final-cr | careful | 0.268 | 0.261 | 0 | re-read |
| learned-rev-stamper-290-own/direct/eval/final-cr | stamper | 1.746 | 1.746 | 0 | re-read |
| learned-rev-stamper-290-own/direct/eval/final-cr | hand | 0.216 | 0.214 | 0 | re-read |
| learned-rev-stamper-290-own/direct/eval/final | direct | 0.293 | ≥ 0.053 (bound) | — | the macOS episode, not re-run |
| learned-rev-stamper-290-own/direct/eval/final | careful | 0.256 | ≥ 0.048 (bound) | — | the macOS episode, not re-run |
| learned-rev-stamper-290-own/direct/eval/final | stamper | 1.757 | ≥ 1.757 (bound) | — | the macOS episode, not re-run |
| learned-rev-stamper-290-own/direct/eval/final | hand | 0.209 | ≥ 0.112 (bound) | — | the macOS episode, not re-run |
| learned-rev-stamper-290-own/wm/eval/final-cr | greedy | 0.307 | 0.305 | 0 | re-read |
| learned-rev-stamper-290-own/wm/eval/final-cr | careful | 0.268 | 0.261 | 0 | re-read |
| learned-rev-stamper-290-own/wm/eval/final-cr | stamper | 1.746 | 1.746 | 0 | re-read |
| learned-rev-stamper-290-own/wm/eval/final-cr | hand | 0.216 | 0.214 | 0 | re-read |
| learned-rev-stamper-290-own/wm/eval/final | greedy | 0.277 | ≥ 0.065 (bound) | — | the macOS episode, not re-run |
| learned-rev-stamper-290-own/wm/eval/final | careful | 0.256 | ≥ 0.048 (bound) | — | the macOS episode, not re-run |
| learned-rev-stamper-290-own/wm/eval/final | stamper | 1.757 | ≥ 1.757 (bound) | — | the macOS episode, not re-run |
| learned-rev-stamper-290-own/wm/eval/final | hand | 0.209 | ≥ 0.112 (bound) | — | the macOS episode, not re-run |
| learned-rev-stamper-290/direct/eval/final | direct | 0.819 | ≥ 0.384 (bound) | — | the macOS episode, not re-run |
| learned-rev-stamper-290/direct/eval/final | careful | 0.324 | ≥ 0.000 (bound) | — | the macOS episode, not re-run |
| learned-rev-stamper-290/direct/eval/final | stamper | 1.993 | ≥ 1.635 (bound) | — | the macOS episode, not re-run |
| learned-rev-stamper-290/direct/eval/final | hand | 0.257 | ≥ 0.014 (bound) | — | the macOS episode, not re-run |
| learned-rev-stamper-290/wm/eval/final | greedy | 0.772 | ≥ 0.351 (bound) | — | the macOS episode, not re-run |
| learned-rev-stamper-290/wm/eval/final | careful | 0.324 | ≥ 0.000 (bound) | — | the macOS episode, not re-run |
| learned-rev-stamper-290/wm/eval/final | stamper | 1.993 | ≥ 1.635 (bound) | — | the macOS episode, not re-run |
| learned-rev-stamper-290/wm/eval/final | hand | 0.257 | ≥ 0.014 (bound) | — | the macOS episode, not re-run |

303 policy columns re-read (34 with another key moved), 80 bounded.


### 2b. The plant kind's filed share and panel wait where they moved (the cells with disputes on)

| evaluation | policy | filed share before | after | panel wait before | after |
|---|---|---|---|---|---|
| ablation-A1/detection/frozen-d0.1 | direct | 0.188 | 0.176 | 0.425 | 0.430 |
| ablation-A1/detection/frozen-d0.1 | careful | 0.183 | 0.170 | 0.264 | 0.267 |
| ablation-A1/detection/frozen-d0.1 | hand | 0.108 | 0.105 | 0.136 | 0.137 |
| ablation-A1/detection/frozen-d0.25 | direct | 0.204 | 0.177 | 0.482 | 0.491 |
| ablation-A1/detection/frozen-d0.25 | careful | 0.199 | 0.173 | 0.311 | 0.315 |
| ablation-A1/detection/frozen-d0.25 | hand | 0.139 | 0.129 | 0.108 | 0.112 |
| ablation-A1/detection/frozen2-d0.1 | direct | 0.188 | 0.176 | 0.425 | 0.430 |
| ablation-A1/detection/frozen2-d0.1 | careful | 0.183 | 0.170 | 0.264 | 0.267 |
| ablation-A1/detection/frozen2-d0.1 | hand | 0.108 | 0.105 | 0.136 | 0.137 |
| ablation-A1/detection/frozen2-d0.25 | direct | 0.204 | 0.177 | 0.482 | 0.491 |
| ablation-A1/detection/frozen2-d0.25 | careful | 0.199 | 0.173 | 0.311 | 0.315 |
| ablation-A1/detection/frozen2-d0.25 | hand | 0.139 | 0.129 | 0.108 | 0.112 |
| ablation-A1/detection/retrain-d0.1/direct/eval/final | direct | 0.193 | 0.180 | 0.418 | 0.414 |
| ablation-A1/detection/retrain-d0.1/direct/eval/final | careful | 0.183 | 0.170 | 0.264 | 0.267 |
| ablation-A1/detection/retrain-d0.1/direct/eval/final | hand | 0.108 | 0.105 | 0.136 | 0.137 |
| ablation-A1/detection/retrain-d0.1/wm/eval/final | greedy | 0.187 | 0.178 | 0.499 | 0.506 |
| ablation-A1/detection/retrain-d0.1/wm/eval/final | careful | 0.183 | 0.170 | 0.264 | 0.267 |
| ablation-A1/detection/retrain-d0.1/wm/eval/final | hand | 0.108 | 0.105 | 0.136 | 0.137 |
| ablation-A1/detection/retrain-d0.25/direct/eval/final | direct | 0.218 | 0.186 | 0.405 | 0.427 |
| ablation-A1/detection/retrain-d0.25/direct/eval/final | careful | 0.199 | 0.173 | 0.311 | 0.315 |
| ablation-A1/detection/retrain-d0.25/direct/eval/final | hand | 0.139 | 0.129 | 0.108 | 0.112 |
| ablation-A1/detection/retrain-d0.25/wm/eval/final | greedy | 0.214 | 0.185 | 0.411 | 0.431 |
| ablation-A1/detection/retrain-d0.25/wm/eval/final | careful | 0.199 | 0.173 | 0.311 | 0.315 |
| ablation-A1/detection/retrain-d0.25/wm/eval/final | hand | 0.139 | 0.129 | 0.108 | 0.112 |
| cr-finals/hand-old-defaults-liars-cr | careful | 0.464 | 0.401 | 0.344 | 0.348 |
| cr-finals/hand-old-defaults-liars-cr | hand | 0.354 | 0.326 | 0.146 | 0.146 |
| learned-rev-liars-290-own/direct/eval/final-cr | direct | 0.479 | 0.402 | 0.276 | 0.277 |
| learned-rev-liars-290-own/direct/eval/final-cr | careful | 0.480 | 0.398 | 0.324 | 0.325 |
| learned-rev-liars-290-own/direct/eval/final-cr | hand | 0.358 | 0.321 | 0.142 | 0.151 |
| learned-rev-liars-290-own/probe-seats/evals/round-11 | direct | 0.492 | 0.415 | 0.329 | 0.339 |
| learned-rev-liars-290-own/probe-seats/evals/round-11 | careful | 0.480 | 0.398 | 0.324 | 0.325 |
| learned-rev-liars-290-own/wm/eval/final-cr | greedy | 0.477 | 0.396 | 0.297 | 0.307 |
| learned-rev-liars-290-own/wm/eval/final-cr | careful | 0.480 | 0.398 | 0.324 | 0.325 |
| learned-rev-liars-290-own/wm/eval/final-cr | hand | 0.358 | 0.321 | 0.142 | 0.151 |

34 policy columns; in every other re-read both are the record's to the decimal. The bounded finals of the liar chains of §68–§70 (`learned-rev-liars-290/`, `-290b/`, `-B-290/`) carried the planted approvals' disputes in the same way; their filed share is bounded as the state seats are, by the planted approvals closed a run over the plants seated.


## 3. The pairings (every row of a pairing of record against the pairing produced again over the re-reads)

A pairing's rows are aligned by their label; a cell is *changed* where the record carried a figure and the re-pairing carries a different one, and *newly read* where the record carried none (`nan`, `—`) — the re-reads were made with today's `run_q`, whose evaluation writes readings (the leak, the overhead, the false penalties) the evaluations of record predate, so a base side re-read carries figures its record lacked; those are not the correction's and are counted apart.


### 2.9.0-s82/finals-paired-ablations.md — not re-paired (a side made before the corrected emission, or the reader's); the rows of record:

- `| state seats per plant | 0.408 | 0.375 | 0.177 | 0.137 | 0.404 | 0.433 | 0.174 | 0.130 |`
- `| state seats per plant | +0.004 ± 0.020 | -0.058 ± 0.021 | +0.003 ± 0.008 | +0.007 ± 0.007 |`
- `| state seats per plant | +0.231 ± 0.016 | +0.198 ± 0.020 | -0.040 ± 0.010 |`
- `| state seats per plant | 0.480 | 0.370 | 0.285 | 0.428 | 0.272 | 0.226 | 0.195 | 0.133 |`
- `| state seats per plant | +0.208 ± 0.029 | +0.144 ± 0.017 | +0.090 ± 0.011 | +0.295 ± 0.016 |`
- `| state seats per plant | +0.195 ± 0.026 | +0.085 ± 0.017 | +0.143 ± 0.019 |`

### 2.9.0-s82/finals-paired-b-vs-290.md — not re-paired (a side made before the corrected emission, or the reader's); the rows of record:

- `| state seats per plant | 0.567 | 0.506 | 0.209 | 0.256 | 0.781 | 0.714 | 0.257 | 0.324 |`
- `| state seats per plant | -0.213 ± 0.023 | -0.208 ± 0.018 | -0.048 ± 0.013 | -0.068 ± 0.014 |`
- `| state seats per plant | +0.359 ± 0.011 | +0.298 ± 0.017 | +0.047 ± 0.013 |`
- `| state seats per plant | 0.599 | 0.569 | 0.273 | 0.464 | 0.626 | 0.469 | 0.317 | 0.484 |`
- `| state seats per plant | -0.027 ± 0.036 | +0.100 ± 0.037 | -0.044 ± 0.013 | -0.020 ± 0.019 |`
- `| state seats per plant | +0.326 ± 0.017 | +0.296 ± 0.026 | +0.190 ± 0.016 |`

### 2.9.0-s82/finals-paired-b.md — not re-paired (a side made before the corrected emission, or the reader's); the rows of record:

- `| state seats per plant | 0.567 | 0.506 | 0.209 | 0.256 | 0.404 | 0.433 | 0.174 | 0.130 |`
- `| state seats per plant | +0.164 ± 0.014 | +0.074 ± 0.015 | +0.035 ± 0.012 | +0.126 ± 0.013 |`
- `| state seats per plant | +0.359 ± 0.011 | +0.298 ± 0.017 | +0.047 ± 0.013 |`
- `| state seats per plant | 0.599 | 0.569 | 0.273 | 0.464 | 0.272 | 0.226 | 0.195 | 0.133 |`
- `| state seats per plant | +0.327 ± 0.020 | +0.343 ± 0.029 | +0.078 ± 0.010 | +0.331 ± 0.012 |`
- `| state seats per plant | +0.326 ± 0.017 | +0.296 ± 0.026 | +0.190 ± 0.016 |`

### 2.9.0-s82/finals-paired-half.md — not re-paired (a side made before the corrected emission, or the reader's); the rows of record:

- `| state seats per plant | 0.173 | 0.177 | 0.209 | 0.161 | 0.109 | 0.129 | 0.174 | 0.112 |`
- `| state seats per plant | +0.064 ± 0.007 | +0.049 ± 0.011 | +0.035 ± 0.012 | +0.049 ± 0.009 |`
- `| state seats per plant | -0.036 ± 0.008 | -0.032 ± 0.010 | -0.048 ± 0.012 |`

### 2.9.0-s82/finals-paired-own-liars.md — not re-paired (a side made before the corrected emission, or the reader's); the rows of record:

- `| state seats per plant | 0.417 | 0.404 | 0.273 | 0.464 | 0.599 | 0.569 | 0.273 | 0.464 |`
- `| state seats per plant | -0.183 ± 0.018 | -0.166 ± 0.033 | +0.000 ± 0.000 | +0.000 ± 0.000 |`
- `| state seats per plant | +0.144 ± 0.012 | +0.130 ± 0.013 | +0.190 ± 0.016 |`

### 2.9.0-s82/finals-paired-own-stamper.md — not re-paired (a side made before the corrected emission, or the reader's); the rows of record:

- `| state seats per plant | 0.293 | 0.277 | 0.209 | 0.256 | 0.819 | 0.772 | 0.257 | 0.324 |`
- `| state seats per plant | -0.525 ± 0.017 | -0.495 ± 0.020 | -0.048 ± 0.013 | -0.068 ± 0.014 |`
- `| state seats per plant | +0.085 ± 0.015 | +0.069 ± 0.015 | +0.047 ± 0.013 |`

### 2.9.0-s82/finals-paired-own.md — not re-paired (a side made before the corrected emission, or the reader's); the rows of record:

- `| state seats per plant | 0.285 | 0.314 | 0.209 | 0.256 | 0.567 | 0.506 | 0.209 | 0.256 |`
- `| state seats per plant | -0.282 ± 0.011 | -0.193 ± 0.014 | +0.000 ± 0.000 | +0.000 ± 0.000 |`
- `| state seats per plant | +0.077 ± 0.012 | +0.105 ± 0.015 | +0.047 ± 0.013 |`

### 2.9.0-s82/finals-paired.md — not re-paired (a side made before the corrected emission, or the reader's); the rows of record:

- `| state seats per plant | 0.781 | 0.714 | 0.257 | 0.324 | 0.404 | 0.433 | 0.174 | 0.130 |`
- `| state seats per plant | +0.377 ± 0.019 | +0.282 ± 0.016 | +0.083 ± 0.012 | +0.194 ± 0.014 |`
- `| state seats per plant | +0.524 ± 0.021 | +0.458 ± 0.017 | +0.067 ± 0.010 |`
- `| state seats per plant | 0.626 | 0.469 | 0.317 | 0.484 | 0.272 | 0.226 | 0.195 | 0.133 |`
- `| state seats per plant | +0.354 ± 0.036 | +0.243 ± 0.028 | +0.122 ± 0.014 | +0.351 ± 0.016 |`
- `| state seats per plant | +0.309 ± 0.035 | +0.152 ± 0.030 | +0.167 ± 0.022 |`

### 2.9.0-s87-own/finals-paired-half-vs-run42.md — re-paired as `finals-paired-half-vs-run42-at-30f280474.md`; 7 rows changed, 20 rows newly read where the record had none

- before: `| state seats per plant | 0.161 | 0.168 | 0.216 | 0.160 | 0.298 | 0.316 | 0.216 | 0.268 |`
  after:  `| state seats per plant | 0.159 | 0.166 | 0.214 | 0.158 | 0.291 | 0.312 | 0.214 | 0.261 |`
- before: `| state seats per plant | -0.136 ± 0.013 | -0.148 ± 0.019 | +0.000 ± 0.000 | -0.108 ± 0.017 |`
  after:  `| state seats per plant | -0.132 ± 0.013 | -0.146 ± 0.019 | +0.000 ± 0.000 | -0.102 ± 0.017 |`
- before: `| state seats per plant | -0.055 ± 0.009 | -0.048 ± 0.012 | -0.057 ± 0.011 |`
  after:  `| state seats per plant | -0.055 ± 0.009 | -0.048 ± 0.012 | -0.056 ± 0.011 |`
- before: `| the half direct | 0.543 / 0.213 | 0.14 / 0.15 | 0.038 / 0.096 | 0.00 / 0.00 | 0.12 / 0.12 | 0.280 / 0.161 | -0.416 ± 0.005 | -0.010 ± 0.003 | +0.057 ± 0.003 |`
  after:  `| the half direct | 0.543 / 0.213 | 0.14 / 0.15 | 0.038 / 0.096 | 0.00 / 0.00 | 0.12 / 0.12 | 0.280 / 0.159 | -0.416 ± 0.005 | -0.011 ± 0.004 | +0.057 ± 0.003 |`
- before: `| the half head alone | 0.537 / 0.207 | 0.11 / 0.13 | 0.036 / 0.095 | 0.00 / 0.00 | 0.11 / 0.11 | 0.283 / 0.168 | -0.414 ± 0.006 | -0.011 ± 0.003 | +0.058 ± 0.004 |`
  after:  `| the half head alone | 0.537 / 0.207 | 0.11 / 0.13 | 0.036 / 0.095 | 0.00 / 0.00 | 0.11 / 0.11 | 0.283 / 0.166 | -0.414 ± 0.006 | -0.012 ± 0.003 | +0.058 ± 0.004 |`
- before: `| the half hand | 0.525 / 0.214 | 0.11 / 0.14 | 0.035 / 0.085 | 0.00 / 0.00 | 0.09 / 0.11 | 0.321 / 0.216 | -0.398 ± 0.008 | +0.012 ± 0.004 | +0.048 ± 0.002 |`
  after:  `| the half hand | 0.525 / 0.214 | 0.11 / 0.14 | 0.035 / 0.085 | 0.00 / 0.00 | 0.09 / 0.11 | 0.321 / 0.214 | -0.398 ± 0.008 | +0.010 ± 0.004 | +0.048 ± 0.002 |`
- before: `| the half careful | 0.544 / 0.210 | 0.11 / 0.12 | 0.038 / 0.095 | 0.00 / 0.00 | 0.11 / 0.11 | 0.273 / 0.160 | -0.418 ± 0.005 | -0.007 ± 0.003 | +0.056 ± 0.004 |`
  after:  `| the half careful | 0.544 / 0.210 | 0.11 / 0.12 | 0.038 / 0.095 | 0.00 / 0.00 | 0.11 / 0.11 | 0.273 / 0.158 | -0.418 ± 0.005 | -0.008 ± 0.003 | +0.056 ± 0.004 |`

### 2.9.0-s87-own/finals-paired-half.md — re-paired as `finals-paired-half-at-30f280474.md`; 7 rows changed, 0 rows newly read where the record had none

- before: `| state seats per plant | 0.161 | 0.168 | 0.216 | 0.160 | 0.173 | 0.177 | 0.209 | 0.161 |`
  after:  `| state seats per plant | 0.159 | 0.166 | 0.214 | 0.158 | 0.173 | 0.177 | 0.209 | 0.161 |`
- before: `| state seats per plant | -0.012 ± 0.010 | -0.009 ± 0.009 | +0.007 ± 0.011 | -0.001 ± 0.009 |`
  after:  `| state seats per plant | -0.013 ± 0.010 | -0.011 ± 0.009 | +0.006 ± 0.012 | -0.002 ± 0.009 |`
- before: `| state seats per plant | -0.055 ± 0.009 | -0.048 ± 0.012 | -0.057 ± 0.011 |`
  after:  `| state seats per plant | -0.055 ± 0.009 | -0.048 ± 0.012 | -0.056 ± 0.011 |`
- before: `| own money direct | 0.543 / 0.213 | 0.14 / 0.15 | 0.038 / 0.096 | 0.00 / 0.00 | 0.12 / 0.12 | 0.280 / 0.161 | -0.416 ± 0.005 | -0.010 ± 0.003 | +0.057 ± 0.003 |`
  after:  `| own money direct | 0.543 / 0.213 | 0.14 / 0.15 | 0.038 / 0.096 | 0.00 / 0.00 | 0.12 / 0.12 | 0.280 / 0.159 | -0.416 ± 0.005 | -0.011 ± 0.004 | +0.057 ± 0.003 |`
- before: `| own money head alone | 0.537 / 0.207 | 0.11 / 0.13 | 0.036 / 0.095 | 0.00 / 0.00 | 0.11 / 0.11 | 0.283 / 0.168 | -0.414 ± 0.006 | -0.011 ± 0.003 | +0.058 ± 0.004 |`
  after:  `| own money head alone | 0.537 / 0.207 | 0.11 / 0.13 | 0.036 / 0.095 | 0.00 / 0.00 | 0.11 / 0.11 | 0.283 / 0.166 | -0.414 ± 0.006 | -0.012 ± 0.003 | +0.058 ± 0.004 |`
- before: `| own money hand | 0.525 / 0.214 | 0.11 / 0.14 | 0.035 / 0.085 | 0.00 / 0.00 | 0.09 / 0.11 | 0.321 / 0.216 | -0.398 ± 0.008 | +0.012 ± 0.004 | +0.048 ± 0.002 |`
  after:  `| own money hand | 0.525 / 0.214 | 0.11 / 0.14 | 0.035 / 0.085 | 0.00 / 0.00 | 0.09 / 0.11 | 0.321 / 0.214 | -0.398 ± 0.008 | +0.010 ± 0.004 | +0.048 ± 0.002 |`
- before: `| own money careful | 0.544 / 0.210 | 0.11 / 0.12 | 0.038 / 0.095 | 0.00 / 0.00 | 0.11 / 0.11 | 0.273 / 0.160 | -0.418 ± 0.005 | -0.007 ± 0.003 | +0.056 ± 0.004 |`
  after:  `| own money careful | 0.544 / 0.210 | 0.11 / 0.12 | 0.038 / 0.095 | 0.00 / 0.00 | 0.11 / 0.11 | 0.273 / 0.158 | -0.418 ± 0.005 | -0.008 ± 0.003 | +0.056 ± 0.004 |`

### 2.9.0-s87-own/finals-paired-pins.md — re-paired as `finals-paired-pins-at-30f280474.md`; 11 rows changed, 40 rows newly read where the record had none

- before: `| state seats per plant | 0.349 | 0.354 | 0.688 | 0.272 | 0.298 | 0.316 | 0.216 | 0.268 |`
  after:  `| state seats per plant | 0.344 | 0.351 | 0.671 | 0.265 | 0.291 | 0.312 | 0.214 | 0.261 |`
- before: `| state seats per plant | +0.052 ± 0.019 | +0.038 ± 0.023 | +0.472 ± 0.028 | +0.004 ± 0.006 |`
  after:  `| state seats per plant | +0.053 ± 0.019 | +0.039 ± 0.023 | +0.456 ± 0.028 | +0.004 ± 0.006 |`
- before: `| state seats per plant | -0.339 ± 0.031 | -0.334 ± 0.033 | -0.416 ± 0.031 |`
  after:  `| state seats per plant | -0.327 ± 0.032 | -0.320 ± 0.034 | -0.406 ± 0.031 |`
- before: `| pinned direct | 0.412 / 0.127 | 0.47 / 0.49 | 0.039 / 0.164 | 0.00 / 0.00 | 0.49 / 0.52 | 0.397 / 0.349 | -0.286 ± 0.010 | -0.047 ± 0.008 | +0.125 ± 0.004 |`
  after:  `| pinned direct | 0.412 / 0.127 | 0.47 / 0.49 | 0.039 / 0.164 | 0.00 / 0.00 | 0.49 / 0.52 | 0.397 / 0.344 | -0.286 ± 0.010 | -0.052 ± 0.008 | +0.125 ± 0.004 |`
- before: `| pinned head alone | 0.374 / 0.099 | 0.47 / 0.49 | 0.038 / 0.162 | 0.00 / 0.00 | 0.47 / 0.50 | 0.428 / 0.354 | -0.275 ± 0.010 | -0.073 ± 0.009 | +0.125 ± 0.005 |`
  after:  `| pinned head alone | 0.374 / 0.099 | 0.47 / 0.49 | 0.038 / 0.162 | 0.00 / 0.00 | 0.47 / 0.50 | 0.428 / 0.351 | -0.275 ± 0.010 | -0.077 ± 0.009 | +0.125 ± 0.005 |`
- before: `| pinned hand | 0.351 / 0.141 | 0.40 / 0.38 | 0.027 / 0.144 | 0.00 / 0.00 | 0.39 / 0.42 | 0.566 / 0.688 | -0.212 ± 0.012 | +0.124 ± 0.011 | +0.117 ± 0.005 |`
  after:  `| pinned hand | 0.351 / 0.141 | 0.40 / 0.38 | 0.027 / 0.144 | 0.00 / 0.00 | 0.39 / 0.42 | 0.566 / 0.671 | -0.212 ± 0.012 | +0.106 ± 0.011 | +0.117 ± 0.005 |`
- before: `| pinned careful | 0.467 / 0.128 | 0.30 / 0.31 | 0.038 / 0.165 | 0.00 / 0.00 | 0.29 / 0.33 | 0.311 / 0.272 | -0.340 ± 0.009 | -0.039 ± 0.007 | +0.127 ± 0.004 |`
  after:  `| pinned careful | 0.467 / 0.128 | 0.30 / 0.31 | 0.038 / 0.165 | 0.00 / 0.00 | 0.29 / 0.33 | 0.311 / 0.265 | -0.340 ± 0.009 | -0.046 ± 0.007 | +0.127 ± 0.004 |`
- before: `| state seats per plant | 0.048 | 0.042 | 0.126 | 0.045 | 0.298 | 0.316 | 0.216 | 0.268 |`
  after:  `| state seats per plant | 0.048 | 0.042 | 0.125 | 0.045 | 0.291 | 0.312 | 0.214 | 0.261 |`
- before: `| state seats per plant | -0.249 ± 0.012 | -0.274 ± 0.018 | -0.090 ± 0.012 | -0.223 ± 0.015 |`
  after:  `| state seats per plant | -0.243 ± 0.012 | -0.270 ± 0.017 | -0.089 ± 0.012 | -0.216 ± 0.015 |`
- before: `| state seats per plant | -0.077 ± 0.007 | -0.083 ± 0.008 | -0.081 ± 0.006 |`
  after:  `| state seats per plant | -0.077 ± 0.007 | -0.084 ± 0.008 | -0.081 ± 0.006 |`
- before: `| pinned hand | 0.659 / 0.233 | 0.10 / 0.12 | 0.036 / 0.076 | 0.00 / 0.00 | 0.07 / 0.11 | 0.120 / 0.126 | -0.427 ± 0.005 | +0.006 ± 0.003 | +0.040 ± 0.002 |`
  after:  `| pinned hand | 0.659 / 0.233 | 0.10 / 0.12 | 0.036 / 0.076 | 0.00 / 0.00 | 0.07 / 0.11 | 0.120 / 0.125 | -0.427 ± 0.005 | +0.006 ± 0.003 | +0.040 ± 0.002 |`

### ablation-A1/detection/retrain-d0.1/finals-paired-vs-frozen.md — re-paired as `finals-paired-vs-frozen-at-30f280474.md`; 7 rows changed, 0 rows newly read where the record had none

- before: `| state seats per plant | 0.301 | 0.345 | 0.228 | 0.235 | 0.314 | — | 0.228 | 0.235 |`
  after:  `| state seats per plant | 0.289 | 0.335 | 0.226 | 0.227 | 0.302 | — | 0.226 | 0.227 |`
- before: `| state seats per plant | -0.013 ± 0.022 | — | +0.000 ± 0.000 | +0.000 ± 0.000 |`
  after:  `| state seats per plant | -0.013 ± 0.021 | — | +0.000 ± 0.000 | +0.000 ± 0.000 |`
- before: `| state seats per plant | +0.073 ± 0.020 | +0.117 ± 0.015 | +0.007 ± 0.014 |`
  after:  `| state seats per plant | +0.063 ± 0.019 | +0.109 ± 0.015 | +0.001 ± 0.014 |`
- before: `| C5 retrained at 0.1 direct | 0.441 / 0.123 | 0.43 / 0.42 | 0.041 / 0.193 | 0.00 / 0.00 | 0.41 / 0.42 | 0.346 / 0.301 | -0.324 ± 0.007 | -0.038 ± 0.010 | +0.153 ± 0.007 |`
  after:  `| C5 retrained at 0.1 direct | 0.441 / 0.123 | 0.43 / 0.42 | 0.041 / 0.180 | 0.00 / 0.00 | 0.41 / 0.41 | 0.346 / 0.289 | -0.324 ± 0.007 | -0.050 ± 0.009 | +0.139 ± 0.006 |`
- before: `| C5 retrained at 0.1 head alone | 0.409 / 0.124 | 0.47 / 0.46 | 0.041 / 0.187 | 0.00 / 0.00 | 0.46 / 0.50 | 0.384 / 0.345 | -0.288 ± 0.009 | -0.036 ± 0.008 | +0.147 ± 0.005 |`
  after:  `| C5 retrained at 0.1 head alone | 0.409 / 0.124 | 0.47 / 0.46 | 0.041 / 0.178 | 0.00 / 0.00 | 0.46 / 0.51 | 0.384 / 0.335 | -0.288 ± 0.009 | -0.045 ± 0.008 | +0.137 ± 0.004 |`
- before: `| C5 retrained at 0.1 hand | 0.521 / 0.210 | 0.12 / 0.15 | 0.035 / 0.108 | 0.00 / 0.00 | 0.12 / 0.14 | 0.330 / 0.228 | -0.404 ± 0.004 | +0.025 ± 0.004 | +0.071 ± 0.002 |`
  after:  `| C5 retrained at 0.1 hand | 0.521 / 0.210 | 0.12 / 0.15 | 0.035 / 0.105 | 0.00 / 0.00 | 0.12 / 0.14 | 0.330 / 0.226 | -0.404 ± 0.004 | +0.022 ± 0.004 | +0.068 ± 0.002 |`
- before: `| C5 retrained at 0.1 careful | 0.493 / 0.140 | 0.29 / 0.29 | 0.040 / 0.183 | 0.00 / 0.00 | 0.28 / 0.26 | 0.275 / 0.235 | -0.355 ± 0.009 | -0.037 ± 0.007 | +0.143 ± 0.005 |`
  after:  `| C5 retrained at 0.1 careful | 0.493 / 0.140 | 0.29 / 0.29 | 0.040 / 0.170 | 0.00 / 0.00 | 0.28 / 0.27 | 0.275 / 0.227 | -0.355 ± 0.009 | -0.045 ± 0.006 | +0.130 ± 0.005 |`

### ablation-A1/detection/retrain-d0.25/finals-paired-vs-frozen.md — re-paired as `finals-paired-vs-frozen-at-30f280474.md`; 7 rows changed, 0 rows newly read where the record had none

- before: `| state seats per plant | 0.317 | 0.310 | 0.216 | 0.262 | 0.346 | — | 0.216 | 0.262 |`
  after:  `| state seats per plant | 0.297 | 0.294 | 0.214 | 0.245 | 0.324 | — | 0.214 | 0.245 |`
- before: `| state seats per plant | -0.028 ± 0.015 | — | +0.000 ± 0.000 | +0.000 ± 0.000 |`
  after:  `| state seats per plant | -0.028 ± 0.014 | — | +0.000 ± 0.000 | +0.000 ± 0.000 |`
- before: `| state seats per plant | +0.101 ± 0.017 | +0.095 ± 0.015 | +0.046 ± 0.010 |`
  after:  `| state seats per plant | +0.083 ± 0.016 | +0.081 ± 0.015 | +0.032 ± 0.010 |`
- before: `| C5 retrained at 0.25 direct | 0.434 / 0.120 | 0.44 / 0.42 | 0.042 / 0.218 | 0.00 / 0.00 | 0.39 / 0.41 | 0.350 / 0.317 | -0.318 ± 0.007 | -0.028 ± 0.012 | +0.176 ± 0.007 |`
  after:  `| C5 retrained at 0.25 direct | 0.434 / 0.120 | 0.44 / 0.42 | 0.042 / 0.186 | 0.00 / 0.00 | 0.39 / 0.43 | 0.350 / 0.297 | -0.318 ± 0.007 | -0.048 ± 0.010 | +0.144 ± 0.006 |`
- before: `| C5 retrained at 0.25 head alone | 0.446 / 0.124 | 0.39 / 0.43 | 0.043 / 0.214 | 0.00 / 0.00 | 0.40 / 0.41 | 0.335 / 0.310 | -0.328 ± 0.009 | -0.018 ± 0.008 | +0.171 ± 0.007 |`
  after:  `| C5 retrained at 0.25 head alone | 0.446 / 0.124 | 0.39 / 0.43 | 0.043 / 0.185 | 0.00 / 0.00 | 0.40 / 0.43 | 0.335 / 0.294 | -0.328 ± 0.009 | -0.034 ± 0.007 | +0.142 ± 0.006 |`
- before: `| C5 retrained at 0.25 hand | 0.527 / 0.194 | 0.10 / 0.14 | 0.041 / 0.139 | 0.00 / 0.00 | 0.10 / 0.11 | 0.317 / 0.216 | -0.427 ± 0.006 | +0.025 ± 0.003 | +0.098 ± 0.003 |`
  after:  `| C5 retrained at 0.25 hand | 0.527 / 0.194 | 0.10 / 0.14 | 0.041 / 0.129 | 0.00 / 0.00 | 0.10 / 0.11 | 0.317 / 0.214 | -0.427 ± 0.006 | +0.023 ± 0.003 | +0.088 ± 0.003 |`
- before: `| C5 retrained at 0.25 careful | 0.477 / 0.127 | 0.30 / 0.29 | 0.043 / 0.199 | 0.00 / 0.00 | 0.29 / 0.31 | 0.298 / 0.262 | -0.350 ± 0.007 | -0.035 ± 0.007 | +0.156 ± 0.004 |`
  after:  `| C5 retrained at 0.25 careful | 0.477 / 0.127 | 0.30 / 0.29 | 0.043 / 0.173 | 0.00 / 0.00 | 0.29 / 0.32 | 0.298 / 0.245 | -0.350 ± 0.007 | -0.052 ± 0.007 | +0.130 ± 0.004 |`

### ablation-A1/learned/finals-paired-arm0-carried.md — re-paired as `finals-paired-arm0-carried-at-30f280474.md`; 7 rows changed, 20 rows newly read where the record had none

- before: `| state seats per plant | 0.134 | 0.167 | 0.214 | 0.134 | 0.298 | 0.316 | 0.216 | 0.268 |`
  after:  `| state seats per plant | 0.130 | 0.160 | 0.206 | 0.129 | 0.291 | 0.312 | 0.214 | 0.261 |`
- before: `| state seats per plant | -0.163 ± 0.016 | -0.149 ± 0.020 | -0.002 ± 0.014 | -0.134 ± 0.016 |`
  after:  `| state seats per plant | -0.161 ± 0.016 | -0.152 ± 0.019 | -0.008 ± 0.014 | -0.131 ± 0.016 |`
- before: `| state seats per plant | -0.080 ± 0.012 | -0.047 ± 0.011 | -0.080 ± 0.012 |`
  after:  `| state seats per plant | -0.077 ± 0.011 | -0.046 ± 0.010 | -0.077 ± 0.012 |`
- before: `| arm 0 carried direct | 0.661 / 0.213 | 0.11 / 0.15 | 0.039 / 0.214 | 0.00 / 0.00 | 0.11 / 0.14 | 0.100 / 0.134 | -0.433 ± 0.005 | +0.010 ± 0.004 | +0.174 ± 0.009 |`
  after:  `| arm 0 carried direct | 0.661 / 0.213 | 0.11 / 0.15 | 0.039 / 0.214 | 0.00 / 0.00 | 0.11 / 0.14 | 0.100 / 0.130 | -0.433 ± 0.005 | +0.005 ± 0.004 | +0.174 ± 0.009 |`
- before: `| arm 0 carried head alone | 0.625 / 0.197 | 0.14 / 0.18 | 0.040 / 0.253 | 0.00 / 0.00 | 0.13 / 0.15 | 0.122 / 0.167 | -0.406 ± 0.008 | +0.010 ± 0.006 | +0.213 ± 0.008 |`
  after:  `| arm 0 carried head alone | 0.625 / 0.197 | 0.14 / 0.18 | 0.040 / 0.253 | 0.00 / 0.00 | 0.13 / 0.15 | 0.122 / 0.160 | -0.406 ± 0.008 | +0.003 ± 0.005 | +0.213 ± 0.008 |`
- before: `| arm 0 carried hand | 0.653 / 0.220 | 0.09 / 0.13 | 0.036 / 0.158 | 0.00 / 0.00 | 0.07 / 0.10 | 0.144 / 0.214 | -0.418 ± 0.005 | +0.044 ± 0.003 | +0.123 ± 0.004 |`
  after:  `| arm 0 carried hand | 0.653 / 0.220 | 0.09 / 0.13 | 0.036 / 0.158 | 0.00 / 0.00 | 0.07 / 0.10 | 0.144 / 0.206 | -0.418 ± 0.005 | +0.036 ± 0.003 | +0.123 ± 0.004 |`
- before: `| arm 0 carried careful | 0.660 / 0.207 | 0.12 / 0.15 | 0.039 / 0.227 | 0.00 / 0.00 | 0.12 / 0.12 | 0.094 / 0.134 | -0.434 ± 0.006 | +0.008 ± 0.005 | +0.188 ± 0.008 |`
  after:  `| arm 0 carried careful | 0.660 / 0.207 | 0.12 / 0.15 | 0.039 / 0.227 | 0.00 / 0.00 | 0.12 / 0.12 | 0.094 / 0.129 | -0.434 ± 0.006 | +0.004 ± 0.004 | +0.188 ± 0.008 |`

### ablation-A1/learned/finals-paired-arm1c.md — re-paired as `finals-paired-arm1c-at-30f280474.md`; 7 rows changed, 20 rows newly read where the record had none

- before: `| state seats per plant | 0.295 | 0.283 | 0.219 | 0.242 | 0.298 | 0.316 | 0.216 | 0.268 |`
  after:  `| state seats per plant | 0.290 | 0.278 | 0.218 | 0.237 | 0.291 | 0.312 | 0.214 | 0.261 |`
- before: `| state seats per plant | -0.002 ± 0.018 | -0.033 ± 0.024 | +0.003 ± 0.012 | -0.026 ± 0.017 |`
  after:  `| state seats per plant | -0.002 ± 0.017 | -0.034 ± 0.024 | +0.004 ± 0.013 | -0.023 ± 0.017 |`
- before: `| state seats per plant | +0.076 ± 0.017 | +0.064 ± 0.017 | +0.023 ± 0.012 |`
  after:  `| state seats per plant | +0.071 ± 0.017 | +0.060 ± 0.017 | +0.019 ± 0.013 |`
- before: `| arm1c direct | 0.439 / 0.139 | 0.38 / 0.40 | 0.039 / 0.153 | 0.00 / 0.00 | 0.37 / 0.43 | 0.505 / 0.295 | -0.316 ± 0.010 | -0.191 ± 0.008 | +0.114 ± 0.005 |`
  after:  `| arm1c direct | 0.439 / 0.139 | 0.38 / 0.40 | 0.039 / 0.153 | 0.00 / 0.00 | 0.37 / 0.43 | 0.505 / 0.290 | -0.316 ± 0.010 | -0.197 ± 0.007 | +0.114 ± 0.005 |`
- before: `| arm1c head alone | 0.437 / 0.127 | 0.37 / 0.39 | 0.038 / 0.173 | 0.00 / 0.00 | 0.36 / 0.37 | 0.480 / 0.283 | -0.313 ± 0.008 | -0.193 ± 0.009 | +0.134 ± 0.009 |`
  after:  `| arm1c head alone | 0.437 / 0.127 | 0.37 / 0.39 | 0.038 / 0.173 | 0.00 / 0.00 | 0.36 / 0.37 | 0.480 / 0.278 | -0.313 ± 0.008 | -0.198 ± 0.009 | +0.134 ± 0.009 |`
- before: `| arm1c hand | 0.525 / 0.221 | 0.11 / 0.13 | 0.033 / 0.084 | 0.00 / 0.00 | 0.09 / 0.11 | 0.480 / 0.219 | -0.395 ± 0.006 | -0.148 ± 0.004 | +0.049 ± 0.002 |`
  after:  `| arm1c hand | 0.525 / 0.221 | 0.11 / 0.13 | 0.033 / 0.084 | 0.00 / 0.00 | 0.09 / 0.11 | 0.480 / 0.218 | -0.395 ± 0.006 | -0.149 ± 0.004 | +0.049 ± 0.002 |`
- before: `| arm1c careful | 0.490 / 0.156 | 0.29 / 0.29 | 0.038 / 0.160 | 0.00 / 0.00 | 0.25 / 0.29 | 0.439 / 0.242 | -0.340 ± 0.009 | -0.191 ± 0.008 | +0.122 ± 0.005 |`
  after:  `| arm1c careful | 0.490 / 0.156 | 0.29 / 0.29 | 0.038 / 0.160 | 0.00 / 0.00 | 0.25 / 0.29 | 0.439 / 0.237 | -0.340 ± 0.009 | -0.195 ± 0.008 | +0.122 ± 0.005 |`

### ablation-A1/learned/finals-paired-arm2-stamper-run42.md — re-paired as `finals-paired-arm2-stamper-run42-at-30f280474.md`; 2 rows changed, 20 rows newly read where the record had none

- before: `| state seats per plant | 0.176 | 0.172 | 0.042 | 0.174 | 0.298 | 0.316 | 0.216 | 0.268 |`
  after:  `| state seats per plant | 0.176 | 0.172 | 0.042 | 0.174 | 0.291 | 0.312 | 0.214 | 0.261 |`
- before: `| state seats per plant | -0.122 ± 0.011 | -0.144 ± 0.018 | -0.174 ± 0.008 | -0.094 ± 0.016 |`
  after:  `| state seats per plant | -0.115 ± 0.011 | -0.140 ± 0.018 | -0.173 ± 0.008 | -0.087 ± 0.016 |`

### ablation-A1/learned/finals-paired-arm2-stamper.md — re-paired as `finals-paired-arm2-stamper-at-30f280474.md`; 0 rows changed, 0 rows newly read where the record had none


### ablation-A1/learned/finals-paired-arm2.md — re-paired as `finals-paired-arm2-at-30f280474.md`; 2 rows changed, 20 rows newly read where the record had none

- before: `| state seats per plant | 0.195 | 0.172 | 0.042 | 0.174 | 0.298 | 0.316 | 0.216 | 0.268 |`
  after:  `| state seats per plant | 0.195 | 0.172 | 0.042 | 0.174 | 0.291 | 0.312 | 0.214 | 0.261 |`
- before: `| state seats per plant | -0.103 ± 0.014 | -0.144 ± 0.019 | -0.174 ± 0.008 | -0.094 ± 0.016 |`
  after:  `| state seats per plant | -0.097 ± 0.014 | -0.139 ± 0.019 | -0.173 ± 0.008 | -0.087 ± 0.016 |`

### ablation-A1/learned/finals-paired-arm4-stamper-run42.md — re-paired as `finals-paired-arm4-stamper-run42-at-30f280474.md`; 2 rows changed, 20 rows newly read where the record had none

- before: `| state seats per plant | 0.000 | 0.000 | 0.000 | 0.000 | 0.298 | 0.316 | 0.216 | 0.268 |`
  after:  `| state seats per plant | 0.000 | 0.000 | 0.000 | 0.000 | 0.291 | 0.312 | 0.214 | 0.261 |`
- before: `| state seats per plant | -0.298 ± 0.012 | -0.316 ± 0.018 | -0.216 ± 0.009 | -0.268 ± 0.015 |`
  after:  `| state seats per plant | -0.291 ± 0.012 | -0.312 ± 0.017 | -0.214 ± 0.009 | -0.261 ± 0.014 |`

### ablation-A1/learned/finals-paired-arm4-stamper.md — re-paired as `finals-paired-arm4-stamper-at-30f280474.md`; 0 rows changed, 0 rows newly read where the record had none


### ablation-A1/learned/finals-paired-arm4.md — re-paired as `finals-paired-arm4-at-30f280474.md`; 2 rows changed, 20 rows newly read where the record had none

- before: `| state seats per plant | 0.000 | 0.000 | 0.000 | 0.000 | 0.298 | 0.316 | 0.216 | 0.268 |`
  after:  `| state seats per plant | 0.000 | 0.000 | 0.000 | 0.000 | 0.291 | 0.312 | 0.214 | 0.261 |`
- before: `| state seats per plant | -0.298 ± 0.012 | -0.316 ± 0.018 | -0.216 ± 0.009 | -0.268 ± 0.015 |`
  after:  `| state seats per plant | -0.291 ± 0.012 | -0.312 ± 0.017 | -0.214 ± 0.009 | -0.261 ± 0.014 |`

### ablation-A1/learned/finals-paired-pa10-stamper-run42.md — re-paired as `finals-paired-pa10-stamper-run42-at-30f280474.md`; 7 rows changed, 20 rows newly read where the record had none

- before: `| state seats per plant | 0.285 | 0.293 | 0.237 | 0.280 | 0.298 | 0.316 | 0.216 | 0.268 |`
  after:  `| state seats per plant | 0.255 | 0.259 | 0.228 | 0.249 | 0.291 | 0.312 | 0.214 | 0.261 |`
- before: `| state seats per plant | -0.012 ± 0.017 | -0.023 ± 0.017 | +0.021 ± 0.012 | +0.012 ± 0.020 |`
  after:  `| state seats per plant | -0.037 ± 0.014 | -0.053 ± 0.017 | +0.014 ± 0.012 | -0.011 ± 0.017 |`
- before: `| state seats per plant | +0.049 ± 0.013 | +0.057 ± 0.013 | +0.043 ± 0.015 |`
  after:  `| state seats per plant | +0.027 ± 0.012 | +0.031 ± 0.011 | +0.021 ± 0.013 |`
- before: `| pin stamper start direct | 0.459 / 0.133 | 0.32 / 0.32 | 0.039 / 0.159 | 0.00 / 0.00 | 0.32 / 0.29 | 0.323 / 0.285 | -0.331 ± 0.007 | -0.032 ± 0.010 | +0.120 ± 0.005 |`
  after:  `| pin stamper start direct | 0.459 / 0.133 | 0.32 / 0.32 | 0.039 / 0.159 | 0.00 / 0.00 | 0.32 / 0.29 | 0.323 / 0.255 | -0.331 ± 0.007 | -0.063 ± 0.008 | +0.120 ± 0.005 |`
- before: `| pin stamper start head alone | 0.467 / 0.132 | 0.34 / 0.33 | 0.040 / 0.156 | 0.00 / 0.00 | 0.32 / 0.36 | 0.313 / 0.293 | -0.338 ± 0.009 | -0.016 ± 0.011 | +0.116 ± 0.004 |`
  after:  `| pin stamper start head alone | 0.467 / 0.132 | 0.34 / 0.33 | 0.040 / 0.156 | 0.00 / 0.00 | 0.32 / 0.36 | 0.313 / 0.259 | -0.338 ± 0.009 | -0.051 ± 0.008 | +0.116 ± 0.004 |`
- before: `| pin stamper start hand | 0.509 / 0.214 | 0.12 / 0.13 | 0.033 / 0.085 | 0.00 / 0.00 | 0.11 / 0.13 | 0.343 / 0.237 | -0.389 ± 0.007 | +0.022 ± 0.004 | +0.050 ± 0.003 |`
  after:  `| pin stamper start hand | 0.509 / 0.214 | 0.12 / 0.13 | 0.033 / 0.085 | 0.00 / 0.00 | 0.11 / 0.13 | 0.343 / 0.228 | -0.389 ± 0.007 | +0.014 ± 0.003 | +0.050 ± 0.003 |`
- before: `| pin stamper start careful | 0.474 / 0.137 | 0.30 / 0.31 | 0.040 / 0.162 | 0.00 / 0.00 | 0.28 / 0.31 | 0.302 / 0.280 | -0.341 ± 0.010 | -0.019 ± 0.010 | +0.123 ± 0.005 |`
  after:  `| pin stamper start careful | 0.474 / 0.137 | 0.30 / 0.31 | 0.040 / 0.162 | 0.00 / 0.00 | 0.28 / 0.31 | 0.302 / 0.249 | -0.341 ± 0.010 | -0.050 ± 0.009 | +0.123 ± 0.005 |`

### ablation-A1/learned/finals-paired-pa10-stamper.md — re-paired as `finals-paired-pa10-stamper-at-30f280474.md`; 7 rows changed, 0 rows newly read where the record had none

- before: `| state seats per plant | 0.285 | 0.293 | 0.237 | 0.280 | 0.316 | 0.310 | 0.237 | 0.280 |`
  after:  `| state seats per plant | 0.255 | 0.259 | 0.228 | 0.249 | 0.288 | 0.278 | 0.228 | 0.249 |`
- before: `| state seats per plant | -0.031 ± 0.021 | -0.016 ± 0.019 | +0.000 ± 0.000 | +0.000 ± 0.000 |`
  after:  `| state seats per plant | -0.033 ± 0.018 | -0.019 ± 0.016 | +0.000 ± 0.000 | +0.000 ± 0.000 |`
- before: `| state seats per plant | +0.049 ± 0.013 | +0.057 ± 0.013 | +0.043 ± 0.015 |`
  after:  `| state seats per plant | +0.027 ± 0.012 | +0.031 ± 0.011 | +0.021 ± 0.013 |`
- before: `| pin stamper start direct | 0.459 / 0.133 | 0.32 / 0.32 | 0.039 / 0.159 | 0.00 / 0.00 | 0.32 / 0.29 | 0.323 / 0.285 | -0.331 ± 0.007 | -0.032 ± 0.010 | +0.120 ± 0.005 |`
  after:  `| pin stamper start direct | 0.459 / 0.133 | 0.32 / 0.32 | 0.039 / 0.159 | 0.00 / 0.00 | 0.32 / 0.29 | 0.323 / 0.255 | -0.331 ± 0.007 | -0.063 ± 0.008 | +0.120 ± 0.005 |`
- before: `| pin stamper start head alone | 0.467 / 0.132 | 0.34 / 0.33 | 0.040 / 0.156 | 0.00 / 0.00 | 0.32 / 0.36 | 0.313 / 0.293 | -0.338 ± 0.009 | -0.016 ± 0.011 | +0.116 ± 0.004 |`
  after:  `| pin stamper start head alone | 0.467 / 0.132 | 0.34 / 0.33 | 0.040 / 0.156 | 0.00 / 0.00 | 0.32 / 0.36 | 0.313 / 0.259 | -0.338 ± 0.009 | -0.051 ± 0.008 | +0.116 ± 0.004 |`
- before: `| pin stamper start hand | 0.509 / 0.214 | 0.12 / 0.13 | 0.033 / 0.085 | 0.00 / 0.00 | 0.11 / 0.13 | 0.343 / 0.237 | -0.389 ± 0.007 | +0.022 ± 0.004 | +0.050 ± 0.003 |`
  after:  `| pin stamper start hand | 0.509 / 0.214 | 0.12 / 0.13 | 0.033 / 0.085 | 0.00 / 0.00 | 0.11 / 0.13 | 0.343 / 0.228 | -0.389 ± 0.007 | +0.014 ± 0.003 | +0.050 ± 0.003 |`
- before: `| pin stamper start careful | 0.474 / 0.137 | 0.30 / 0.31 | 0.040 / 0.162 | 0.00 / 0.00 | 0.28 / 0.31 | 0.302 / 0.280 | -0.341 ± 0.010 | -0.019 ± 0.010 | +0.123 ± 0.005 |`
  after:  `| pin stamper start careful | 0.474 / 0.137 | 0.30 / 0.31 | 0.040 / 0.162 | 0.00 / 0.00 | 0.28 / 0.31 | 0.302 / 0.249 | -0.341 ± 0.010 | -0.050 ± 0.009 | +0.123 ± 0.005 |`

### ablation-A1/learned/finals-paired-pa10.md — re-paired as `finals-paired-pa10-at-30f280474.md`; 7 rows changed, 20 rows newly read where the record had none

- before: `| state seats per plant | 0.316 | 0.310 | 0.237 | 0.280 | 0.298 | 0.316 | 0.216 | 0.268 |`
  after:  `| state seats per plant | 0.288 | 0.278 | 0.228 | 0.249 | 0.291 | 0.312 | 0.214 | 0.261 |`
- before: `| state seats per plant | +0.018 ± 0.022 | -0.006 ± 0.019 | +0.021 ± 0.012 | +0.012 ± 0.020 |`
  after:  `| state seats per plant | -0.003 ± 0.020 | -0.034 ± 0.019 | +0.014 ± 0.012 | -0.011 ± 0.017 |`
- before: `| state seats per plant | +0.079 ± 0.014 | +0.073 ± 0.013 | +0.043 ± 0.015 |`
  after:  `| state seats per plant | +0.060 ± 0.012 | +0.050 ± 0.012 | +0.021 ± 0.013 |`
- before: `| pa10 direct | 0.439 / 0.130 | 0.35 / 0.35 | 0.040 / 0.164 | 0.00 / 0.00 | 0.34 / 0.42 | 0.357 / 0.316 | -0.316 ± 0.010 | -0.032 ± 0.008 | +0.124 ± 0.006 |`
  after:  `| pa10 direct | 0.439 / 0.130 | 0.35 / 0.35 | 0.040 / 0.164 | 0.00 / 0.00 | 0.34 / 0.42 | 0.357 / 0.288 | -0.316 ± 0.010 | -0.060 ± 0.007 | +0.124 ± 0.006 |`
- before: `| pa10 head alone | 0.453 / 0.129 | 0.32 / 0.33 | 0.039 / 0.161 | 0.00 / 0.00 | 0.31 / 0.33 | 0.334 / 0.310 | -0.328 ± 0.011 | -0.019 ± 0.013 | +0.122 ± 0.005 |`
  after:  `| pa10 head alone | 0.453 / 0.129 | 0.32 / 0.33 | 0.039 / 0.161 | 0.00 / 0.00 | 0.31 / 0.33 | 0.334 / 0.278 | -0.328 ± 0.011 | -0.051 ± 0.011 | +0.122 ± 0.005 |`
- before: `| pa10 hand | 0.509 / 0.214 | 0.12 / 0.13 | 0.033 / 0.085 | 0.00 / 0.00 | 0.11 / 0.13 | 0.343 / 0.237 | -0.389 ± 0.007 | +0.022 ± 0.004 | +0.050 ± 0.003 |`
  after:  `| pa10 hand | 0.509 / 0.214 | 0.12 / 0.13 | 0.033 / 0.085 | 0.00 / 0.00 | 0.11 / 0.13 | 0.343 / 0.228 | -0.389 ± 0.007 | +0.014 ± 0.003 | +0.050 ± 0.003 |`
- before: `| pa10 careful | 0.474 / 0.137 | 0.30 / 0.31 | 0.040 / 0.162 | 0.00 / 0.00 | 0.28 / 0.31 | 0.302 / 0.280 | -0.341 ± 0.010 | -0.019 ± 0.010 | +0.123 ± 0.005 |`
  after:  `| pa10 careful | 0.474 / 0.137 | 0.30 / 0.31 | 0.040 / 0.162 | 0.00 / 0.00 | 0.28 / 0.31 | 0.302 / 0.249 | -0.341 ± 0.010 | -0.050 ± 0.009 | +0.123 ± 0.005 |`

### ablation-A1/learned/finals-paired-pa20-run42.md — re-paired as `finals-paired-pa20-run42-at-30f280474.md`; 7 rows changed, 20 rows newly read where the record had none

- before: `| state seats per plant | 0.300 | 0.283 | 0.238 | 0.315 | 0.298 | 0.316 | 0.216 | 0.268 |`
  after:  `| state seats per plant | 0.261 | 0.242 | 0.226 | 0.260 | 0.291 | 0.312 | 0.214 | 0.261 |`
- before: `| state seats per plant | +0.002 ± 0.018 | -0.033 ± 0.026 | +0.022 ± 0.013 | +0.047 ± 0.016 |`
  after:  `| state seats per plant | -0.031 ± 0.015 | -0.070 ± 0.025 | +0.012 ± 0.013 | -0.001 ± 0.013 |`
- before: `| state seats per plant | +0.062 ± 0.014 | +0.045 ± 0.016 | +0.077 ± 0.016 |`
  after:  `| state seats per plant | +0.035 ± 0.011 | +0.016 ± 0.014 | +0.034 ± 0.012 |`
- before: `| π^A pinned at 0.20 direct | 0.455 / 0.146 | 0.32 / 0.31 | 0.038 / 0.149 | 0.00 / 0.00 | 0.29 / 0.32 | 0.329 / 0.300 | -0.321 ± 0.006 | -0.013 ± 0.010 | +0.110 ± 0.005 |`
  after:  `| π^A pinned at 0.20 direct | 0.455 / 0.146 | 0.32 / 0.31 | 0.038 / 0.149 | 0.00 / 0.00 | 0.29 / 0.32 | 0.329 / 0.261 | -0.321 ± 0.006 | -0.052 ± 0.006 | +0.110 ± 0.005 |`
- before: `| π^A pinned at 0.20 head alone | 0.478 / 0.147 | 0.30 / 0.31 | 0.038 / 0.154 | 0.00 / 0.00 | 0.29 / 0.31 | 0.300 / 0.283 | -0.340 ± 0.007 | -0.007 ± 0.010 | +0.116 ± 0.006 |`
  after:  `| π^A pinned at 0.20 head alone | 0.478 / 0.147 | 0.30 / 0.31 | 0.038 / 0.154 | 0.00 / 0.00 | 0.29 / 0.31 | 0.300 / 0.242 | -0.340 ± 0.007 | -0.047 ± 0.008 | +0.116 ± 0.006 |`
- before: `| π^A pinned at 0.20 hand | 0.514 / 0.208 | 0.11 / 0.14 | 0.032 / 0.087 | 0.00 / 0.00 | 0.10 / 0.10 | 0.335 / 0.238 | -0.402 ± 0.006 | +0.032 ± 0.004 | +0.053 ± 0.002 |`
  after:  `| π^A pinned at 0.20 hand | 0.514 / 0.208 | 0.11 / 0.14 | 0.032 / 0.087 | 0.00 / 0.00 | 0.10 / 0.10 | 0.335 / 0.226 | -0.402 ± 0.006 | +0.020 ± 0.003 | +0.053 ± 0.002 |`
- before: `| π^A pinned at 0.20 careful | 0.474 / 0.143 | 0.34 / 0.36 | 0.041 / 0.158 | 0.00 / 0.00 | 0.32 / 0.35 | 0.305 / 0.315 | -0.335 ± 0.006 | +0.013 ± 0.010 | +0.117 ± 0.005 |`
  after:  `| π^A pinned at 0.20 careful | 0.474 / 0.143 | 0.34 / 0.36 | 0.041 / 0.158 | 0.00 / 0.00 | 0.32 / 0.35 | 0.305 / 0.260 | -0.335 ± 0.006 | -0.042 ± 0.007 | +0.117 ± 0.005 |`

### ablation-A1/learned/finals-paired-pa20.md — re-paired as `finals-paired-pa20-at-30f280474.md`; 7 rows changed, 0 rows newly read where the record had none

- before: `| state seats per plant | 0.300 | 0.283 | 0.238 | 0.315 | 0.316 | 0.310 | 0.237 | 0.280 |`
  after:  `| state seats per plant | 0.261 | 0.242 | 0.226 | 0.260 | 0.288 | 0.278 | 0.228 | 0.249 |`
- before: `| state seats per plant | -0.016 ± 0.019 | -0.027 ± 0.022 | +0.001 ± 0.010 | +0.035 ± 0.013 |`
  after:  `| state seats per plant | -0.028 ± 0.014 | -0.035 ± 0.019 | -0.002 ± 0.010 | +0.011 ± 0.012 |`
- before: `| state seats per plant | +0.062 ± 0.014 | +0.045 ± 0.016 | +0.077 ± 0.016 |`
  after:  `| state seats per plant | +0.035 ± 0.011 | +0.016 ± 0.014 | +0.034 ± 0.012 |`
- before: `| π^A pinned at 0.20 direct | 0.455 / 0.146 | 0.32 / 0.31 | 0.038 / 0.149 | 0.00 / 0.00 | 0.29 / 0.32 | 0.329 / 0.300 | -0.321 ± 0.006 | -0.013 ± 0.010 | +0.110 ± 0.005 |`
  after:  `| π^A pinned at 0.20 direct | 0.455 / 0.146 | 0.32 / 0.31 | 0.038 / 0.149 | 0.00 / 0.00 | 0.29 / 0.32 | 0.329 / 0.261 | -0.321 ± 0.006 | -0.052 ± 0.006 | +0.110 ± 0.005 |`
- before: `| π^A pinned at 0.20 head alone | 0.478 / 0.147 | 0.30 / 0.31 | 0.038 / 0.154 | 0.00 / 0.00 | 0.29 / 0.31 | 0.300 / 0.283 | -0.340 ± 0.007 | -0.007 ± 0.010 | +0.116 ± 0.006 |`
  after:  `| π^A pinned at 0.20 head alone | 0.478 / 0.147 | 0.30 / 0.31 | 0.038 / 0.154 | 0.00 / 0.00 | 0.29 / 0.31 | 0.300 / 0.242 | -0.340 ± 0.007 | -0.047 ± 0.008 | +0.116 ± 0.006 |`
- before: `| π^A pinned at 0.20 hand | 0.514 / 0.208 | 0.11 / 0.14 | 0.032 / 0.087 | 0.00 / 0.00 | 0.10 / 0.10 | 0.335 / 0.238 | -0.402 ± 0.006 | +0.032 ± 0.004 | +0.053 ± 0.002 |`
  after:  `| π^A pinned at 0.20 hand | 0.514 / 0.208 | 0.11 / 0.14 | 0.032 / 0.087 | 0.00 / 0.00 | 0.10 / 0.10 | 0.335 / 0.226 | -0.402 ± 0.006 | +0.020 ± 0.003 | +0.053 ± 0.002 |`
- before: `| π^A pinned at 0.20 careful | 0.474 / 0.143 | 0.34 / 0.36 | 0.041 / 0.158 | 0.00 / 0.00 | 0.32 / 0.35 | 0.305 / 0.315 | -0.335 ± 0.006 | +0.013 ± 0.010 | +0.117 ± 0.005 |`
  after:  `| π^A pinned at 0.20 careful | 0.474 / 0.143 | 0.34 / 0.36 | 0.041 / 0.158 | 0.00 / 0.00 | 0.32 / 0.35 | 0.305 / 0.260 | -0.335 ± 0.006 | -0.042 ± 0.007 | +0.117 ± 0.005 |`

### ablation-A1/stress/learned/finals-paired-arm2-t1-b1.md — re-paired as `finals-paired-arm2-t1-b1-at-30f280474.md`; 0 rows changed, 0 rows newly read where the record had none


### ablation-A1/stress/learned/finals-paired-arm4-t1-b1-gv10-unstressed.md — re-paired as `finals-paired-arm4-t1-b1-gv10-unstressed-at-30f280474.md`; 0 rows changed, 0 rows newly read where the record had none


### ablation-A1/stress/learned/finals-paired-arm4-t1-b1-gv10.md — re-paired as `finals-paired-arm4-t1-b1-gv10-at-30f280474.md`; 0 rows changed, 0 rows newly read where the record had none


### ablation-A1/stress/learned/finals-paired-arm4-t1-b1.md — re-paired as `finals-paired-arm4-t1-b1-at-30f280474.md`; 0 rows changed, 0 rows newly read where the record had none


### ablation-A1/stress/learned/finals-paired-pa10-t1-b1.md — re-paired as `finals-paired-pa10-t1-b1-at-30f280474.md`; 7 rows changed, 0 rows newly read where the record had none

- before: `| state seats per plant | 0.613 | 0.533 | 0.237 | 0.280 | 0.316 | 0.310 | 0.237 | 0.280 |`
  after:  `| state seats per plant | 0.601 | 0.526 | 0.228 | 0.249 | 0.288 | 0.278 | 0.228 | 0.249 |`
- before: `| state seats per plant | +0.298 ± 0.024 | +0.223 ± 0.016 | +0.000 ± 0.000 | +0.000 ± 0.000 |`
  after:  `| state seats per plant | +0.313 ± 0.024 | +0.248 ± 0.014 | +0.000 ± 0.000 | +0.000 ± 0.000 |`
- before: `| state seats per plant | +0.377 ± 0.019 | +0.296 ± 0.010 | +0.043 ± 0.015 |`
  after:  `| state seats per plant | +0.373 ± 0.020 | +0.298 ± 0.011 | +0.021 ± 0.013 |`
- before: `| the 0.10 pin, stressed (x 1, bond x1) direct | 0.137 / 0.069 | 0.58 / 0.61 | 0.027 / 0.073 | 0.00 / 0.00 | 0.54 / 0.56 | 0.820 / 0.613 | -0.091 ± 0.006 | -0.161 ± 0.008 | +0.044 ± 0.002 |`
  after:  `| the 0.10 pin, stressed (x 1, bond x1) direct | 0.137 / 0.069 | 0.58 / 0.61 | 0.027 / 0.073 | 0.00 / 0.00 | 0.54 / 0.56 | 0.820 / 0.601 | -0.091 ± 0.006 | -0.174 ± 0.008 | +0.044 ± 0.002 |`
- before: `| the 0.10 pin, stressed (x 1, bond x1) head alone | 0.165 / 0.080 | 0.53 / 0.56 | 0.027 / 0.076 | 0.00 / 0.00 | 0.57 / 0.64 | 0.764 / 0.533 | -0.119 ± 0.005 | -0.163 ± 0.006 | +0.047 ± 0.002 |`
  after:  `| the 0.10 pin, stressed (x 1, bond x1) head alone | 0.165 / 0.080 | 0.53 / 0.56 | 0.027 / 0.076 | 0.00 / 0.00 | 0.57 / 0.64 | 0.764 / 0.526 | -0.119 ± 0.005 | -0.171 ± 0.006 | +0.047 ± 0.002 |`
- before: `| the 0.10 pin, stressed (x 1, bond x1) hand | 0.509 / 0.214 | 0.12 / 0.13 | 0.033 / 0.085 | 0.00 / 0.00 | 0.11 / 0.13 | 0.343 / 0.237 | -0.389 ± 0.007 | +0.022 ± 0.004 | +0.050 ± 0.003 |`
  after:  `| the 0.10 pin, stressed (x 1, bond x1) hand | 0.509 / 0.214 | 0.12 / 0.13 | 0.033 / 0.085 | 0.00 / 0.00 | 0.11 / 0.13 | 0.343 / 0.228 | -0.389 ± 0.007 | +0.014 ± 0.003 | +0.050 ± 0.003 |`
- before: `| the 0.10 pin, stressed (x 1, bond x1) careful | 0.474 / 0.137 | 0.30 / 0.31 | 0.040 / 0.162 | 0.00 / 0.00 | 0.28 / 0.31 | 0.302 / 0.280 | -0.341 ± 0.010 | -0.019 ± 0.010 | +0.123 ± 0.005 |`
  after:  `| the 0.10 pin, stressed (x 1, bond x1) careful | 0.474 / 0.137 | 0.30 / 0.31 | 0.040 / 0.162 | 0.00 / 0.00 | 0.28 / 0.31 | 0.302 / 0.249 | -0.341 ± 0.010 | -0.050 ± 0.009 | +0.123 ± 0.005 |`

### ablation-A1/stress/learned/finals-paired-pa20-t1-b6-gv20-stressed.md — re-paired as `finals-paired-pa20-t1-b6-gv20-stressed-at-30f280474.md`; 2 rows changed, 0 rows newly read where the record had none

- before: `| state seats per plant | 0.307 | 0.230 | 0.207 | 0.278 | 0.613 | 0.533 | 0.237 | 0.280 |`
  after:  `| state seats per plant | 0.307 | 0.230 | 0.207 | 0.278 | 0.601 | 0.526 | 0.228 | 0.249 |`
- before: `| state seats per plant | -0.306 ± 0.023 | -0.303 ± 0.011 | -0.030 ± 0.011 | -0.001 ± 0.015 |`
  after:  `| state seats per plant | -0.294 ± 0.024 | -0.295 ± 0.012 | -0.022 ± 0.012 | +0.029 ± 0.014 |`

### ablation-A1/stress/learned/finals-paired-pa20-t1-b6-gv20.md — re-paired as `finals-paired-pa20-t1-b6-gv20-at-30f280474.md`; 2 rows changed, 0 rows newly read where the record had none

- before: `| state seats per plant | 0.307 | 0.230 | 0.207 | 0.278 | 0.300 | 0.283 | 0.238 | 0.315 |`
  after:  `| state seats per plant | 0.307 | 0.230 | 0.207 | 0.278 | 0.261 | 0.242 | 0.226 | 0.260 |`
- before: `| state seats per plant | +0.008 ± 0.024 | -0.053 ± 0.018 | -0.031 ± 0.011 | -0.036 ± 0.014 |`
  after:  `| state seats per plant | +0.047 ± 0.020 | -0.012 ± 0.017 | -0.019 ± 0.011 | +0.018 ± 0.014 |`

### cr-finals/paired-290-vs-270-own-cr.md — re-paired as `paired-290-vs-270-own-cr-at-30f280474.md`; 12 rows changed, 0 rows newly read where the record had none

- before: `| state seats per plant | 0.298 | 0.316 | 0.216 | 0.268 | nan | nan | nan | nan |`
  after:  `| state seats per plant | 0.291 | 0.312 | 0.214 | 0.261 | nan | nan | nan | nan |`
- before: `| state seats per plant | +0.082 ± 0.015 | +0.100 ± 0.019 | +0.052 ± 0.016 |`
  after:  `| state seats per plant | +0.077 ± 0.015 | +0.098 ± 0.019 | +0.046 ± 0.016 |`
- before: `| 2.9.0 direct | 0.436 / 0.137 | 0.42 / 0.44 | 0.039 / 0.165 | 0.00 / 0.00 | 0.41 / 0.43 | 0.360 / 0.298 | -0.311 ± 0.006 | -0.049 ± 0.008 | +0.125 ± 0.006 |`
  after:  `| 2.9.0 direct | 0.436 / 0.137 | 0.42 / 0.44 | 0.039 / 0.165 | 0.00 / 0.00 | 0.41 / 0.43 | 0.360 / 0.291 | -0.311 ± 0.006 | -0.055 ± 0.008 | +0.125 ± 0.006 |`
- before: `| 2.9.0 head alone | 0.429 / 0.138 | 0.44 / 0.45 | 0.039 / 0.154 | 0.00 / 0.00 | 0.46 / 0.50 | 0.366 / 0.316 | -0.299 ± 0.011 | -0.040 ± 0.007 | +0.115 ± 0.004 |`
  after:  `| 2.9.0 head alone | 0.429 / 0.138 | 0.44 / 0.45 | 0.039 / 0.154 | 0.00 / 0.00 | 0.46 / 0.50 | 0.366 / 0.312 | -0.299 ± 0.011 | -0.044 ± 0.007 | +0.115 ± 0.004 |`
- before: `| 2.9.0 hand | 0.525 / 0.214 | 0.11 / 0.14 | 0.035 / 0.085 | 0.00 / 0.00 | 0.09 / 0.11 | 0.321 / 0.216 | -0.398 ± 0.008 | +0.012 ± 0.004 | +0.048 ± 0.002 |`
  after:  `| 2.9.0 hand | 0.525 / 0.214 | 0.11 / 0.14 | 0.035 / 0.085 | 0.00 / 0.00 | 0.09 / 0.11 | 0.321 / 0.214 | -0.398 ± 0.008 | +0.010 ± 0.004 | +0.048 ± 0.002 |`
- before: `| 2.9.0 careful | 0.468 / 0.130 | 0.31 / 0.33 | 0.039 / 0.164 | 0.00 / 0.00 | 0.29 / 0.31 | 0.313 / 0.268 | -0.343 ± 0.008 | -0.040 ± 0.008 | +0.125 ± 0.004 |`
  after:  `| 2.9.0 careful | 0.468 / 0.130 | 0.31 / 0.33 | 0.039 / 0.164 | 0.00 / 0.00 | 0.29 / 0.31 | 0.313 / 0.261 | -0.343 ± 0.008 | -0.047 ± 0.007 | +0.125 ± 0.004 |`
- before: `| state seats per plant | 0.300 | 0.307 | 0.216 | 0.268 | nan | nan | nan | nan |`
  after:  `| state seats per plant | 0.294 | 0.305 | 0.214 | 0.261 | nan | nan | nan | nan |`
- before: `| state seats per plant | +0.084 ± 0.022 | +0.091 ± 0.015 | +0.052 ± 0.016 |`
  after:  `| state seats per plant | +0.080 ± 0.022 | +0.091 ± 0.015 | +0.046 ± 0.016 |`
- before: `| 2.9.0 direct | 0.437 / 0.132 | 0.43 / 0.45 | 0.038 / 0.163 | 0.00 / 0.00 | 0.45 / 0.41 | 0.356 / 0.300 | -0.314 ± 0.010 | -0.046 ± 0.009 | +0.124 ± 0.006 |`
  after:  `| 2.9.0 direct | 0.437 / 0.132 | 0.43 / 0.45 | 0.038 / 0.163 | 0.00 / 0.00 | 0.45 / 0.41 | 0.356 / 0.294 | -0.314 ± 0.010 | -0.051 ± 0.009 | +0.124 ± 0.006 |`
- before: `| 2.9.0 head alone | 0.416 / 0.139 | 0.43 / 0.43 | 0.038 / 0.152 | 0.00 / 0.00 | 0.42 / 0.42 | 0.389 / 0.307 | -0.305 ± 0.010 | -0.048 ± 0.009 | +0.114 ± 0.005 |`
  after:  `| 2.9.0 head alone | 0.416 / 0.139 | 0.43 / 0.43 | 0.038 / 0.152 | 0.00 / 0.00 | 0.42 / 0.42 | 0.389 / 0.305 | -0.305 ± 0.010 | -0.050 ± 0.009 | +0.114 ± 0.005 |`
- before: `| 2.9.0 hand | 0.525 / 0.214 | 0.11 / 0.14 | 0.035 / 0.085 | 0.00 / 0.00 | 0.09 / 0.11 | 0.321 / 0.216 | -0.398 ± 0.008 | +0.012 ± 0.004 | +0.048 ± 0.002 |`
  after:  `| 2.9.0 hand | 0.525 / 0.214 | 0.11 / 0.14 | 0.035 / 0.085 | 0.00 / 0.00 | 0.09 / 0.11 | 0.321 / 0.214 | -0.398 ± 0.008 | +0.010 ± 0.004 | +0.048 ± 0.002 |`
- before: `| 2.9.0 careful | 0.468 / 0.130 | 0.31 / 0.33 | 0.039 / 0.164 | 0.00 / 0.00 | 0.29 / 0.31 | 0.313 / 0.268 | -0.343 ± 0.008 | -0.040 ± 0.008 | +0.125 ± 0.004 |`
  after:  `| 2.9.0 careful | 0.468 / 0.130 | 0.31 / 0.33 | 0.039 / 0.164 | 0.00 / 0.00 | 0.29 / 0.31 | 0.313 / 0.261 | -0.343 ± 0.008 | -0.047 ± 0.007 | +0.125 ± 0.004 |`

### cr-finals/seam-290-own.md — re-paired as `seam-290-own-at-30f280474.md`; 21 rows changed, 0 rows newly read where the record had none

- before: `| state seats per plant | 0.298 | 0.316 | 0.216 | 0.268 | 0.285 | 0.314 | 0.209 | 0.256 |`
  after:  `| state seats per plant | 0.291 | 0.312 | 0.214 | 0.261 | 0.285 | 0.314 | 0.209 | 0.256 |`
- before: `| state seats per plant | +0.012 ± 0.016 | +0.002 ± 0.015 | +0.007 ± 0.011 | +0.012 ± 0.013 |`
  after:  `| state seats per plant | +0.006 ± 0.015 | -0.002 ± 0.015 | +0.006 ± 0.012 | +0.005 ± 0.012 |`
- before: `| state seats per plant | +0.082 ± 0.015 | +0.100 ± 0.019 | +0.052 ± 0.016 |`
  after:  `| state seats per plant | +0.077 ± 0.015 | +0.098 ± 0.019 | +0.046 ± 0.016 |`
- before: `| corrected direct | 0.436 / 0.137 | 0.42 / 0.44 | 0.039 / 0.165 | 0.00 / 0.00 | 0.41 / 0.43 | 0.360 / 0.298 | -0.311 ± 0.006 | -0.049 ± 0.008 | +0.125 ± 0.006 |`
  after:  `| corrected direct | 0.436 / 0.137 | 0.42 / 0.44 | 0.039 / 0.165 | 0.00 / 0.00 | 0.41 / 0.43 | 0.360 / 0.291 | -0.311 ± 0.006 | -0.055 ± 0.008 | +0.125 ± 0.006 |`
- before: `| corrected head alone | 0.429 / 0.138 | 0.44 / 0.45 | 0.039 / 0.154 | 0.00 / 0.00 | 0.46 / 0.50 | 0.366 / 0.316 | -0.299 ± 0.011 | -0.040 ± 0.007 | +0.115 ± 0.004 |`
  after:  `| corrected head alone | 0.429 / 0.138 | 0.44 / 0.45 | 0.039 / 0.154 | 0.00 / 0.00 | 0.46 / 0.50 | 0.366 / 0.312 | -0.299 ± 0.011 | -0.044 ± 0.007 | +0.115 ± 0.004 |`
- before: `| corrected hand | 0.525 / 0.214 | 0.11 / 0.14 | 0.035 / 0.085 | 0.00 / 0.00 | 0.09 / 0.11 | 0.321 / 0.216 | -0.398 ± 0.008 | +0.012 ± 0.004 | +0.048 ± 0.002 |`
  after:  `| corrected hand | 0.525 / 0.214 | 0.11 / 0.14 | 0.035 / 0.085 | 0.00 / 0.00 | 0.09 / 0.11 | 0.321 / 0.214 | -0.398 ± 0.008 | +0.010 ± 0.004 | +0.048 ± 0.002 |`
- before: `| corrected careful | 0.468 / 0.130 | 0.31 / 0.33 | 0.039 / 0.164 | 0.00 / 0.00 | 0.29 / 0.31 | 0.313 / 0.268 | -0.343 ± 0.008 | -0.040 ± 0.008 | +0.125 ± 0.004 |`
  after:  `| corrected careful | 0.468 / 0.130 | 0.31 / 0.33 | 0.039 / 0.164 | 0.00 / 0.00 | 0.29 / 0.31 | 0.313 / 0.261 | -0.343 ± 0.008 | -0.047 ± 0.007 | +0.125 ± 0.004 |`
- before: `| state seats per plant | 0.300 | 0.307 | 0.216 | 0.268 | 0.293 | 0.277 | 0.209 | 0.256 |`
  after:  `| state seats per plant | 0.294 | 0.305 | 0.214 | 0.261 | 0.293 | 0.277 | 0.209 | 0.256 |`
- before: `| state seats per plant | +0.006 ± 0.016 | +0.030 ± 0.017 | +0.007 ± 0.011 | +0.012 ± 0.013 |`
  after:  `| state seats per plant | +0.001 ± 0.016 | +0.028 ± 0.016 | +0.006 ± 0.012 | +0.005 ± 0.012 |`
- before: `| state seats per plant | +0.084 ± 0.022 | +0.091 ± 0.015 | +0.052 ± 0.016 |`
  after:  `| state seats per plant | +0.080 ± 0.022 | +0.091 ± 0.015 | +0.046 ± 0.016 |`
- before: `| corrected direct | 0.437 / 0.132 | 0.43 / 0.45 | 0.038 / 0.163 | 0.00 / 0.00 | 0.45 / 0.41 | 0.356 / 0.300 | -0.314 ± 0.010 | -0.046 ± 0.009 | +0.124 ± 0.006 |`
  after:  `| corrected direct | 0.437 / 0.132 | 0.43 / 0.45 | 0.038 / 0.163 | 0.00 / 0.00 | 0.45 / 0.41 | 0.356 / 0.294 | -0.314 ± 0.010 | -0.051 ± 0.009 | +0.124 ± 0.006 |`
- before: `| corrected head alone | 0.416 / 0.139 | 0.43 / 0.43 | 0.038 / 0.152 | 0.00 / 0.00 | 0.42 / 0.42 | 0.389 / 0.307 | -0.305 ± 0.010 | -0.048 ± 0.009 | +0.114 ± 0.005 |`
  after:  `| corrected head alone | 0.416 / 0.139 | 0.43 / 0.43 | 0.038 / 0.152 | 0.00 / 0.00 | 0.42 / 0.42 | 0.389 / 0.305 | -0.305 ± 0.010 | -0.050 ± 0.009 | +0.114 ± 0.005 |`
- before: `| corrected hand | 0.525 / 0.214 | 0.11 / 0.14 | 0.035 / 0.085 | 0.00 / 0.00 | 0.09 / 0.11 | 0.321 / 0.216 | -0.398 ± 0.008 | +0.012 ± 0.004 | +0.048 ± 0.002 |`
  after:  `| corrected hand | 0.525 / 0.214 | 0.11 / 0.14 | 0.035 / 0.085 | 0.00 / 0.00 | 0.09 / 0.11 | 0.321 / 0.214 | -0.398 ± 0.008 | +0.010 ± 0.004 | +0.048 ± 0.002 |`
- before: `| corrected careful | 0.468 / 0.130 | 0.31 / 0.33 | 0.039 / 0.164 | 0.00 / 0.00 | 0.29 / 0.31 | 0.313 / 0.268 | -0.343 ± 0.008 | -0.040 ± 0.008 | +0.125 ± 0.004 |`
  after:  `| corrected careful | 0.468 / 0.130 | 0.31 / 0.33 | 0.039 / 0.164 | 0.00 / 0.00 | 0.29 / 0.31 | 0.313 / 0.261 | -0.343 ± 0.008 | -0.047 ± 0.007 | +0.125 ± 0.004 |`
- before: `| state seats per plant | 0.406 | 0.415 | 0.293 | 0.446 | 0.417 | 0.404 | 0.273 | 0.464 |`
  after:  `| state seats per plant | 0.369 | 0.376 | 0.285 | 0.402 | 0.417 | 0.404 | 0.273 | 0.464 |`
- before: `| state seats per plant | -0.011 ± 0.016 | +0.012 ± 0.016 | +0.020 ± 0.008 | -0.017 ± 0.014 |`
  after:  `| state seats per plant | -0.048 ± 0.016 | -0.028 ± 0.014 | +0.012 ± 0.008 | -0.062 ± 0.013 |`
- before: `| state seats per plant | +0.113 ± 0.016 | +0.122 ± 0.019 | +0.153 ± 0.018 |`
  after:  `| state seats per plant | +0.083 ± 0.015 | +0.090 ± 0.018 | +0.116 ± 0.016 |`
- before: `| corrected direct | 0.420 / 0.022 | 0.33 / 0.24 | 0.144 / 0.479 | 0.00 / 0.00 | 0.30 / 0.28 | 0.358 / 0.406 | -0.408 ± 0.009 | +0.066 ± 0.008 | +0.334 ± 0.009 |`
  after:  `| corrected direct | 0.420 / 0.022 | 0.33 / 0.24 | 0.144 / 0.402 | 0.00 / 0.00 | 0.30 / 0.28 | 0.358 / 0.369 | -0.408 ± 0.009 | +0.028 ± 0.008 | +0.257 ± 0.008 |`
- before: `| corrected head alone | 0.429 / 0.025 | 0.32 / 0.32 | 0.143 / 0.477 | 0.00 / 0.00 | 0.29 / 0.30 | 0.337 / 0.415 | -0.411 ± 0.007 | +0.088 ± 0.011 | +0.334 ± 0.010 |`
  after:  `| corrected head alone | 0.429 / 0.025 | 0.32 / 0.32 | 0.143 / 0.396 | 0.00 / 0.00 | 0.29 / 0.31 | 0.337 / 0.376 | -0.411 ± 0.007 | +0.048 ± 0.009 | +0.253 ± 0.009 |`
- before: `| corrected hand | 0.468 / 0.101 | 0.11 / 0.09 | 0.159 / 0.358 | 0.00 / 0.00 | 0.12 / 0.14 | 0.363 / 0.293 | -0.451 ± 0.008 | +0.068 ± 0.005 | +0.206 ± 0.005 |`
  after:  `| corrected hand | 0.468 / 0.101 | 0.11 / 0.09 | 0.159 / 0.321 | 0.00 / 0.00 | 0.12 / 0.15 | 0.363 / 0.285 | -0.451 ± 0.008 | +0.061 ± 0.005 | +0.170 ± 0.004 |`
- before: `| corrected careful | 0.420 / 0.022 | 0.32 / 0.40 | 0.139 / 0.480 | 0.00 / 0.00 | 0.31 / 0.32 | 0.375 / 0.446 | -0.403 ± 0.009 | +0.078 ± 0.010 | +0.340 ± 0.009 |`
  after:  `| corrected careful | 0.420 / 0.022 | 0.32 / 0.40 | 0.139 / 0.398 | 0.00 / 0.00 | 0.31 / 0.32 | 0.375 / 0.402 | -0.403 ± 0.009 | +0.034 ± 0.009 | +0.259 ± 0.009 |`

27 pairings re-paired: 140 rows changed, 240 rows newly read where the record had none.


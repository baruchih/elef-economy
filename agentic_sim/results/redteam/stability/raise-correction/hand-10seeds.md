# The raise correction on run 24's world (`--entry-pool 20 --stampers 0.6`), seeds 21–30, paired: the committed driver (d5989614) against the corrected (b1f07ee6)

The runs are under `results/runs/*old-raise-s<seed>` / `*new-raise-s<seed>` (not committed); the last row of each `metrics.csv`. Paired Δ = corrected − committed, SE over the ten seeds.

| reading | committed | corrected | paired Δ | SE |
|---|---|---|---|---|
| `P_t` | 20.301 | 20.930 | +0.629 | 0.746 |
| `false_approvals` | 11.400 | 12.000 | +0.600 | 1.470 |
| `careful_members` | 19.400 | 19.600 | +0.200 | 0.359 |
| `careful_wealth` | 1337.002 | 1320.237 | -16.765 | 53.125 |
| `awarded` | 2465.000 | 2468.400 | +3.400 | 27.140 |
| `troop_deliveries` | 34.400 | 32.600 | -1.800 | 5.120 |
| `plants_posted` | 639.600 | 610.800 | -28.800 | 17.712 |
| `plants_raised` | 312.500 | 261.400 | -51.100 | 66.012 |
| `plant_raises_refused` | nan | 92.000 | +nan | nan |
| `plant_raise_delay_mean` | nan | 1.476 | +nan | nan |
| `raise_refusal_rate_window` | nan | 0.384 | +nan | nan |
| `life_real_raise_refused_share` | 0.137 | 0.131 | -0.007 | 0.035 |
| `life_plant_raise_refused_share` | 0.000 | 0.149 | +0.149 | 0.023 |
| `life_real_raised_share` | 0.322 | 0.295 | -0.026 | 0.070 |
| `life_plant_raised_share` | 0.334 | 0.302 | -0.032 | 0.075 |
| `life_real_post_award` | 0.580 | 0.563 | -0.017 | 0.117 |
| `life_plant_post_award` | 0.493 | 0.581 | +0.087 | 0.122 |
| `life_real_award_submit` | 1.000 | 1.000 | +0.000 | 0.000 |
| `life_plant_award_submit` | 1.000 | 1.000 | +0.000 | 0.000 |
| `life_real_submit_seat` | 0.139 | 0.141 | +0.002 | 0.009 |
| `life_plant_submit_seat` | 0.159 | 0.145 | -0.014 | 0.012 |

plant − real, the raise refused share: committed -0.1372, corrected +0.0186

plant − real, posted → awarded: committed -0.0869, corrected +0.0172

Per seed, P_t committed / corrected: 21: 19.7 / 23.7, 22: 22.5 / 20.8, 23: 19.2 / 20.5, 24: 18.0 / 22.0, 25: 19.7 / 20.4, 26: 21.2 / 18.7, 27: 20.2 / 22.3, 28: 19.6 / 18.4, 29: 18.9 / 20.1, 30: 24.1 / 22.4

Per seed, members committed / corrected: 21: 19 / 18, 22: 19 / 20, 23: 20 / 20, 24: 20 / 20, 25: 20 / 19, 26: 19 / 21, 27: 20 / 19, 28: 20 / 20, 29: 20 / 20, 30: 17 / 19

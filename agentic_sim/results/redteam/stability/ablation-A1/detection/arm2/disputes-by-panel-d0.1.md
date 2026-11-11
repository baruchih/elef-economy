# The customers' truthful disputes by the panel's make-up, and the state's panel seats by cause — detection 0.1, the direct's policy results/redteam/stability/ablation-A1/learned/arm2/direct/models/direct-online-10.pt and the careful, cell --entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --dispute-policy truthful --dispute-rate 0.1 --arm 2, seeds 21–40

| policy | make-up | disputes a run | won a run | **won share (pooled)** |
|---|---|---|---|---|
| direct | two members | 1.00 ± 0.19 | 0.25 ± 0.12 | 0.250 (20) |
| direct | one member, one of the state's | 1.00 ± 0.24 | 0.90 ± 0.24 | 0.900 (20) |
| direct | two of the state's | 1.75 ± 0.37 | 1.75 ± 0.37 | 1.000 (35) |
| careful | two members | 0.75 ± 0.12 | 0.70 ± 0.13 | 0.933 (15) |
| careful | one member, one of the state's | 0.50 ± 0.20 | 0.45 ± 0.17 | 0.900 (10) |
| careful | two of the state's | 1.30 ± 0.15 | 1.30 ± 0.15 | 1.000 (26) |

| policy | member panel seats | state panel seats (audit + appeal) | state audits | panel seats unfilled at the driver's seating (ticks) | … a free member kept off the tier | … no member free | member-periods panel-ineligible |
|---|---|---|---|---|---|---|---|
| direct | 132.65 ± 4.34 | 2088.45 ± 9.19 | 1966.20 ± 7.59 | 179.75 ± 5.38 | 179.65 ± 5.35 | 0.10 ± 0.07 | 63.45 ± 1.90 |
| careful | 143.20 ± 5.43 | 2056.65 ± 7.74 | 1943.10 ± 7.25 | 166.70 ± 4.59 | 166.40 ± 4.57 | 0.30 ± 0.15 | 61.45 ± 1.31 |

The joint of the two verdicts on the customers' truthful disputes, by make-up (pooled): both confirm the standing F / split / both reject, against the product of the single-seat F rate p on the same panels (p², 2p(1−p), (1−p)²):

| policy | make-up | panels | single-seat F rate p | both confirm (observed / p²) | split (observed / 2p(1−p)) | both reject (observed / (1−p)²) |
|---|---|---|---|---|---|---|
| direct | two members | 20 | 0.875 | 0.750 / 0.766 | 0.250 / 0.219 | 0.000 / 0.016 |
| direct | one member, one of the state's | 20 | 0.475 | 0.100 / 0.226 | 0.750 / 0.499 | 0.150 / 0.276 |
| direct | two of the state's | 35 | 0.043 | 0.000 / 0.002 | 0.086 / 0.082 | 0.914 / 0.916 |
| careful | two members | 15 | 0.033 | 0.000 / 0.001 | 0.067 / 0.064 | 0.933 / 0.934 |
| careful | one member, one of the state's | 10 | 0.200 | 0.100 / 0.040 | 0.200 / 0.320 | 0.700 / 0.640 |
| careful | two of the state's | 26 | 0.019 | 0.000 / 0.000 | 0.038 / 0.038 | 0.962 / 0.962 |

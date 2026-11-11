# The customers' truthful disputes by the panel's make-up, and the state's panel seats by cause — detection 0.25, the direct's policy results/redteam/stability/ablation-A1/learned/arm2/direct/models/direct-online-10.pt and the careful, cell --entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --dispute-policy truthful --dispute-rate 0.25 --arm 2, seeds 21–40

| policy | make-up | disputes a run | won a run | **won share (pooled)** |
|---|---|---|---|---|
| direct | two members | 3.70 ± 0.48 | 0.95 ± 0.29 | 0.257 (74) |
| direct | one member, one of the state's | 1.75 ± 0.31 | 1.75 ± 0.31 | 1.000 (35) |
| direct | two of the state's | 3.25 ± 0.43 | 3.25 ± 0.43 | 1.000 (65) |
| careful | two members | 3.05 ± 0.34 | 3.05 ± 0.34 | 1.000 (61) |
| careful | one member, one of the state's | 1.75 ± 0.25 | 1.65 ± 0.25 | 0.943 (35) |
| careful | two of the state's | 3.40 ± 0.38 | 3.40 ± 0.38 | 1.000 (68) |

| policy | member panel seats | state panel seats (audit + appeal) | state audits | panel seats unfilled at the driver's seating (ticks) | … a free member kept off the tier | … no member free | member-periods panel-ineligible |
|---|---|---|---|---|---|---|---|
| direct | 153.00 ± 7.57 | 2089.70 ± 8.66 | 1964.60 ± 7.93 | 188.00 ± 4.83 | 187.60 ± 4.81 | 0.40 ± 0.20 | 68.40 ± 2.97 |
| careful | 154.50 ± 5.51 | 2044.30 ± 9.37 | 1926.10 ± 8.09 | 175.45 ± 3.95 | 175.15 ± 4.02 | 0.30 ± 0.16 | 60.20 ± 1.65 |

The joint of the two verdicts on the customers' truthful disputes, by make-up (pooled): both confirm the standing F / split / both reject, against the product of the single-seat F rate p on the same panels (p², 2p(1−p), (1−p)²):

| policy | make-up | panels | single-seat F rate p | both confirm (observed / p²) | split (observed / 2p(1−p)) | both reject (observed / (1−p)²) |
|---|---|---|---|---|---|---|
| direct | two members | 74 | 0.845 | 0.743 / 0.713 | 0.203 / 0.263 | 0.054 / 0.024 |
| direct | one member, one of the state's | 35 | 0.429 | 0.000 / 0.184 | 0.857 / 0.490 | 0.143 / 0.327 |
| direct | two of the state's | 65 | 0.038 | 0.000 / 0.001 | 0.077 / 0.074 | 0.923 / 0.925 |
| careful | two members | 61 | 0.082 | 0.000 / 0.007 | 0.164 / 0.150 | 0.836 / 0.843 |
| careful | one member, one of the state's | 35 | 0.071 | 0.057 / 0.005 | 0.029 / 0.133 | 0.914 / 0.862 |
| careful | two of the state's | 68 | 0.059 | 0.000 / 0.003 | 0.118 / 0.111 | 0.882 / 0.886 |

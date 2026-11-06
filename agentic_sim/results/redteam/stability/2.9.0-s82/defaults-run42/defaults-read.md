# The defaults read on run 42's population by channel (the third ruling's 3): run 42's trained policies (the direct's `direct-online-10.pt`, the head alone's `wm-online-10.pt`, trained at the defaults) and the hand on seeds 21–40, one default moved per cell, no retraining. Columns: the standing false approvals a run (mean ± SE over the seeds), the member-confirmed audit, the state-confirmed audit, the never-audited channel, its share, the mean odds at the verdict of the never-audited, and the audits bought a run on every real root by who sat. The full channel tables beside (fa-channels-<cell>.md).

| cell | policy | standing false approvals | member confirmed | state confirmed | never audited | never-audited share | odds at verdict, never audited | audits a run, a member sat | audits a run, the state sat |
|---|---|---|---|---|---|---|---|---|---|
| defaults (p_floor 0.2, halve every 5) | direct | 28.7 ± 2.3 | 10.2 ± 1.1 | 0.6 ± 0.2 | 17.6 ± 1.7 | 0.615 | 0.284 | 860.0 ± 17.3 | 794.4 ± 20.2 |
| defaults (p_floor 0.2, halve every 5) | head alone | 18.5 ± 1.1 | 9.1 ± 0.6 | 0.6 ± 0.1 | 8.7 ± 1.0 | 0.468 | 0.266 | 816.8 ± 12.8 | 830.3 ± 15.2 |
| defaults (p_floor 0.2, halve every 5) | hand | 10.1 ± 0.8 | 2.9 ± 0.4 | 2.7 ± 0.4 | 3.5 ± 0.3 | 0.351 | 0.562 | 1004.0 ± 29.2 | 604.0 ± 15.1 |
| p_floor 0.35 | direct | 22.9 ± 1.7 | 11.6 ± 0.8 | 0.5 ± 0.2 | 10.8 ± 1.3 | 0.468 | 0.433 | 954.4 ± 14.8 | 792.3 ± 21.6 |
| p_floor 0.35 | head alone | 16.2 ± 1.1 | 9.6 ± 0.8 | 0.7 ± 0.2 | 5.8 ± 0.7 | 0.357 | 0.413 | 943.1 ± 14.5 | 791.2 ± 13.6 |
| p_floor 0.35 | hand | 7.5 ± 0.8 | 3.3 ± 0.4 | 2.6 ± 0.3 | 0.8 ± 0.3 | 0.099 | 0.800 | 1256.2 ± 25.4 | 593.5 ± 13.4 |
| p_floor 0.5 | direct | 20.6 ± 1.5 | 12.6 ± 0.8 | 0.4 ± 0.1 | 7.5 ± 0.9 | 0.363 | 0.538 | 1041.7 ± 24.4 | 794.2 ± 20.2 |
| p_floor 0.5 | head alone | 13.4 ± 1.0 | 9.0 ± 1.0 | 0.3 ± 0.1 | 4.0 ± 0.5 | 0.295 | 0.516 | 1019.0 ± 28.1 | 784.6 ± 23.2 |
| p_floor 0.5 | hand | 7.4 ± 0.7 | 3.8 ± 0.5 | 2.7 ± 0.3 | 0.0 ± 0.0 | 0.000 | nan | 1267.5 ± 24.3 | 600.0 ± 13.8 |
| halve every 10 | direct | 22.9 ± 2.3 | 11.7 ± 1.3 | 0.5 ± 0.1 | 10.4 ± 1.4 | 0.455 | 0.348 | 991.6 ± 19.9 | 784.0 ± 23.3 |
| halve every 10 | head alone | 16.9 ± 1.6 | 8.7 ± 1.0 | 0.7 ± 0.1 | 7.2 ± 0.9 | 0.430 | 0.314 | 929.8 ± 23.9 | 830.4 ± 22.7 |
| halve every 10 | hand | 8.5 ± 0.6 | 3.4 ± 0.4 | 2.6 ± 0.3 | 1.5 ± 0.3 | 0.176 | 0.592 | 1088.8 ± 26.4 | 600.5 ± 12.7 |
| halve every 20 | direct | 17.9 ± 1.5 | 12.3 ± 1.3 | 0.6 ± 0.2 | 4.7 ± 0.6 | 0.262 | 0.421 | 1105.8 ± 21.2 | 821.5 ± 23.1 |
| halve every 20 | head alone | 11.7 ± 0.9 | 8.6 ± 0.9 | 0.5 ± 0.2 | 2.4 ± 0.3 | 0.206 | 0.358 | 1130.6 ± 31.5 | 787.6 ± 32.4 |
| halve every 20 | hand | 7.3 ± 0.7 | 3.4 ± 0.5 | 2.6 ± 0.3 | 0.6 ± 0.2 | 0.082 | 0.594 | 1230.0 ± 22.7 | 599.5 ± 12.9 |
| p_floor 0.5, halve every 20 | direct | 14.7 ± 0.9 | 12.2 ± 0.8 | 0.6 ± 0.2 | 1.8 ± 0.4 | 0.119 | 0.553 | 1145.0 ± 25.7 | 810.7 ± 23.5 |
| p_floor 0.5, halve every 20 | head alone | 12.2 ± 1.3 | 9.8 ± 1.0 | 0.7 ± 0.2 | 1.3 ± 0.4 | 0.106 | 0.543 | 1166.5 ± 35.0 | 789.4 ± 31.4 |
| p_floor 0.5, halve every 20 | hand | 7.6 ± 0.7 | 3.8 ± 0.5 | 2.7 ± 0.3 | 0.0 ± 0.0 | 0.000 | nan | 1269.5 ± 23.4 | 596.9 ± 13.1 |

Paired against the hand on the same seeds (policy − hand): the total, the member-confirmed audit, the never-audited channel.

| cell | policy | total | member confirmed | never audited |
|---|---|---|---|---|
| defaults (p_floor 0.2, halve every 5) | direct − hand | 18.6 ± 2.7 | 7.3 ± 1.3 | 14.1 ± 1.9 |
| defaults (p_floor 0.2, halve every 5) | head alone − hand | 8.4 ± 1.5 | 6.2 ± 0.9 | 5.1 ± 1.1 |
| p_floor 0.35 | direct − hand | 15.4 ± 1.8 | 8.2 ± 0.9 | 10.0 ± 1.3 |
| p_floor 0.35 | head alone − hand | 8.7 ± 1.5 | 6.3 ± 1.0 | 5.0 ± 0.7 |
| p_floor 0.5 | direct − hand | 13.2 ± 1.6 | 8.8 ± 1.0 | 7.5 ± 0.9 |
| p_floor 0.5 | head alone − hand | 6.0 ± 1.5 | 5.2 ± 1.1 | 4.0 ± 0.5 |
| halve every 10 | direct − hand | 14.4 ± 2.2 | 8.3 ± 1.2 | 8.9 ± 1.4 |
| halve every 10 | head alone − hand | 8.3 ± 1.8 | 5.2 ± 1.0 | 5.8 ± 0.9 |
| halve every 20 | direct − hand | 10.6 ± 1.7 | 9.0 ± 1.4 | 4.1 ± 0.7 |
| halve every 20 | head alone − hand | 4.3 ± 1.1 | 5.2 ± 0.9 | 1.8 ± 0.4 |
| p_floor 0.5, halve every 20 | direct − hand | 7.0 ± 0.9 | 8.3 ± 0.9 | 1.8 ± 0.4 |
| p_floor 0.5, halve every 20 | head alone − hand | 4.7 ± 1.5 | 6.0 ± 1.2 | 1.3 ± 0.4 |

# §8.6: the review fees by seat and by who sat — --entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule; seeds 21–30; the finals' direct (/Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/learned-rev-careful-290b/direct/models/direct-online-10.pt) and head alone (/Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/learned-rev-careful-290b/wm/models/wm-online-10.pt), the hand beside. Nominal credits a run, means ± SE over the seeds. A seat's fee is the fixed fee paid from the fee pot at settlement (`feepot_out … review fee`); who sat: a member, the state (a troop), the plant alias (never paid — a check). Beside: the duty uplift paid, the court fees the state won, the bonds burned.

| who sat | seat | case kind | direct | head alone | hand | direct (seats) | head alone (seats) | hand (seats) |
|---|---|---|---|---|---|---|---|---|
| member | appeal | plant | 14 ± 3 | 21 ± 2 | 85 ± 7 | 4.8 | 7.1 | 28.4 |
| member | appeal | real | 167 ± 20 | 159 ± 11 | 697 ± 35 | 60.5 | 56.1 | 259.0 |
| member | audit | plant | 80 ± 8 | 95 ± 9 | 250 ± 17 | 26.8 | 31.6 | 83.4 |
| member | audit | real | 914 ± 93 | 1053 ± 70 | 2845 ± 93 | 313.6 | 353.9 | 1002.8 |
| member | initial | plant | 279 ± 8 | 280 ± 8 | 292 ± 12 | 139.3 | 140.0 | 145.9 |
| member | initial | real | 4768 ± 43 | 4806 ± 58 | 5087 ± 56 | 2442.2 | 2428.7 | 2600.4 |
| state | appeal | real | 619 ± 21 | 584 ± 27 | 304 ± 16 | 237.5 | 217.9 | 116.4 |
| state | audit | real | 4197 ± 64 | 3854 ± 94 | 1834 ± 62 | 1462.3 | 1316.9 | 624.8 |
| state | initial | real | 2 ± 0 | 3 ± 1 | 11 ± 3 | 0.8 | 1.6 | 5.4 |

Totals by who sat (review fees a run):

| who sat | direct | head alone | hand |
|---|---|---|---|
| member | 6222 ± 162 | 6414 ± 142 | 9256 ± 186 |
| state | 4818 ± 79 | 4441 ± 119 | 2149 ± 75 |
| plant alias | 0 ± 0 | 0 ± 0 | 0 ± 0 |

The members' panel income (appeal + dispute seats, real and plant) and the state's audit-seat income:

| reading | direct | head alone | hand |
|---|---|---|---|
| members' panel fees | 181 ± 21 | 180 ± 11 | 782 ± 34 |
| members' audit-seat fees | 994 ± 100 | 1147 ± 78 | 3095 ± 109 |
| state's audit-seat fees | 4197 ± 64 | 3854 ± 94 | 1834 ± 62 |
| state's panel fees | 619 ± 21 | 584 ± 27 | 304 ± 16 |
| state's initial-seat fees | 2 ± 0 | 3 ± 1 | 11 ± 3 |

Beside:

| flow | to / from | direct | head alone | hand |
|---|---|---|---|---|
| bond burned | member | 1610 ± 25 | 1513 ± 34 | 1449 ± 36 |
| bond burned | state | 384 ± 19 | 363 ± 19 | 165 ± 10 |
| court fee won | member | 138 ± 6 | 143 ± 4 | 154 ± 6 |
| members' audits of real approvals (the base), a run | member | 302 ± 31 | 338 ± 23 | 958 ± 32 |
| service fee to Ω | state | 2442 ± 17 | 2441 ± 14 | 2456 ± 18 |
| uplift | member | 4074 ± 186 | 4549 ± 226 | 3860 ± 130 |

The dial per seat's path by period (seed: real member audits of real approvals | m^A | π^A | pool A [hit, adj] | pa adjudicated | confirmed):

- direct seed 21: 41 | 1.0 | 0.02 | [0, 0] | 0 | 0; 25 | 1.0 | 0.02 | [1, 1] | 1 | 1; 22 | 1.0 | 0.02 | [1, 1] | 0 | 0; 49 | 1.0 | 0.02 | [2, 2] | 1 | 1; 50 | 1.0 | 0.02 | [2, 2] | 0 | 0; 23 | 1.0 | 0.02 | [2, 3] | 1 | 0; 17 | 1.0 | 0.02 | [2, 3] | 0 | 0; 8 | 1.0 | 0.02 | [2, 3] | 0 | 0; 52 | 1.0 | 0.02 | [3, 4] | 1 | 1; 22 | 1.0 | 0.02 | [3, 5] | 1 | 0; 2 | 1.0 | 0.02 | [3, 5] | 0 | 0
- direct seed 22: 21 | 1.0 | 0.02 | [0, 0] | 0 | 0; 52 | 1.0 | 0.02 | [0, 1] | 1 | 0; 22 | 1.0 | 0.02 | [0, 1] | 0 | 0; 20 | 1.0 | 0.02 | [1, 2] | 1 | 1; 33 | 1.0 | 0.02 | [1, 2] | 0 | 0; 28 | 1.0 | 0.02 | [2, 3] | 1 | 1; 24 | 1.0 | 0.02 | [2, 3] | 0 | 0; 21 | 1.0 | 0.02 | [2, 3] | 0 | 0; 19 | 1.0 | 0.02 | [2, 3] | 0 | 0; 4 | 1.0 | 0.02 | [2, 3] | 0 | 0; 0 | 1.0 | 0.02 | [2, 3] | 0 | 0
- direct seed 23: 20 | 1.0 | 0.02 | [0, 0] | 0 | 0; 37 | 1.0 | 0.02 | [0, 1] | 1 | 0; 101 | 1.0 | 0.02 | [2, 3] | 2 | 2; 67 | 1.0 | 0.02 | [3, 4] | 1 | 1; 47 | 1.0 | 0.02 | [4, 5] | 1 | 1; 13 | 1.0 | 0.02 | [4, 5] | 0 | 0; 11 | 1.0 | 0.02 | [4, 5] | 0 | 0; 44 | 1.0 | 0.02 | [4, 6] | 1 | 0; 0 | 1.0 | 0.02 | [4, 6] | 0 | 0; 0 | 1.0 | 0.02 | [4, 6] | 0 | 0; 0 | 1.0 | 0.02 | [4, 6] | 0 | 0; 15 | 1.0 | 0.02 | [5, 7] | 1 | 1
- head alone seed 21: 25 | 1.0 | 0.02 | [0, 0] | 0 | 0; 22 | 1.0 | 0.02 | [0, 0] | 0 | 0; 54 | 1.0 | 0.02 | [1, 1] | 1 | 1; 54 | 1.0 | 0.02 | [1, 2] | 1 | 0; 33 | 1.0 | 0.02 | [1, 3] | 1 | 0; 16 | 1.0 | 0.02 | [2, 4] | 1 | 1; 23 | 1.0 | 0.02 | [2, 4] | 0 | 0; 31 | 1.0 | 0.02 | [3, 5] | 1 | 1; 41 | 1.0 | 0.02 | [3, 5] | 0 | 0; 6 | 1.0 | 0.02 | [4, 6] | 1 | 1; 26 | 1.0 | 0.02 | [4, 6] | 0 | 0; 30 | 1.0 | 0.02 | [5, 7] | 1 | 1; 29 | 1.0 | 0.02 | [5, 7] | 0 | 0
- head alone seed 22: 15 | 1.0 | 0.02 | [0, 0] | 0 | 0; 13 | 1.0 | 0.02 | [0, 0] | 0 | 0; 26 | 1.0 | 0.02 | [0, 0] | 0 | 0; 16 | 1.0 | 0.02 | [0, 0] | 0 | 0; 54 | 1.0 | 0.02 | [1, 1] | 1 | 1; 35 | 1.0 | 0.02 | [1, 2] | 1 | 0; 31 | 1.0 | 0.02 | [1, 2] | 0 | 0; 45 | 1.0 | 0.02 | [1, 3] | 1 | 0; 24 | 1.0 | 0.02 | [1, 3] | 0 | 0; 53 | 1.0 | 0.02 | [2, 4] | 1 | 1; 48 | 1.0 | 0.02 | [2, 4] | 0 | 0
- head alone seed 23: 16 | 1.0 | 0.02 | [0, 0] | 0 | 0; 38 | 1.0 | 0.02 | [1, 1] | 1 | 1; 39 | 1.0 | 0.02 | [1, 1] | 0 | 0; 18 | 1.0 | 0.02 | [2, 2] | 1 | 1; 22 | 1.0 | 0.02 | [2, 2] | 0 | 0; 32 | 1.0 | 0.02 | [2, 3] | 1 | 0; 24 | 1.0 | 0.02 | [2, 3] | 0 | 0; 6 | 1.0 | 0.02 | [2, 3] | 0 | 0; 44 | 1.0 | 0.02 | [3, 4] | 1 | 1; 40 | 1.0 | 0.02 | [3, 4] | 0 | 0
- hand seed 21: 20 | 1.0 | 0.02 | [0, 0] | 0 | 0; 6 | 1.0 | 0.02 | [0, 0] | 0 | 0; 52 | 1.0 | 0.02 | [0, 1] | 1 | 0; 71 | 1.0 | 0.02 | [0, 2] | 1 | 0; 81 | 1.0 | 0.02 | [1, 4] | 2 | 1; 90 | 1.0 | 0.02 | [1, 6] | 2 | 0; 92 | 1.0 | 0.02 | [1, 8] | 2 | 0; 106 | 1.0 | 0.02 | [0, 0] | 2 | 0; 93 | 1.0 | 0.02 | [1, 2] | 2 | 1; 107 | 1.0 | 0.02 | [1, 4] | 2 | 0; 105 | 1.0 | 0.02 | [1, 6] | 2 | 0
- hand seed 22: 18 | 1.0 | 0.02 | [0, 0] | 0 | 0; 10 | 1.0 | 0.02 | [0, 0] | 0 | 0; 70 | 1.0 | 0.02 | [0, 1] | 1 | 0; 88 | 1.0 | 0.02 | [0, 3] | 2 | 0; 84 | 1.0 | 0.02 | [0, 5] | 2 | 0; 99 | 1.0 | 0.02 | [0, 7] | 2 | 0; 97 | 1.0 | 0.02 | [0, 9] | 2 | 0; 109 | 1.0 | 0.02 | [0, 0] | 2 | 0; 98 | 1.0 | 0.02 | [0, 2] | 2 | 0; 99 | 1.0 | 0.02 | [1, 4] | 2 | 1; 98 | 1.0 | 0.02 | [1, 6] | 2 | 0
- hand seed 23: 19 | 1.0 | 0.02 | [0, 0] | 0 | 0; 34 | 1.0 | 0.02 | [0, 0] | 0 | 0; 60 | 1.0 | 0.02 | [0, 1] | 1 | 0; 76 | 1.0 | 0.02 | [0, 2] | 1 | 0; 95 | 1.0 | 0.02 | [0, 4] | 2 | 0; 90 | 1.0 | 0.02 | [0, 6] | 2 | 0; 82 | 1.0 | 0.02 | [0, 7] | 1 | 0; 90 | 1.0 | 0.02 | [0, 9] | 2 | 0; 89 | 1.0 | 0.02 | [0, 0] | 2 | 0; 105 | 1.0 | 0.02 | [0, 2] | 2 | 0; 100 | 1.0 | 0.02 | [0, 4] | 2 | 0; 101 | 1.0 | 0.02 | [0, 6] | 2 | 0; 92 | 1.0 | 0.02 | [0, 8] | 2 | 0

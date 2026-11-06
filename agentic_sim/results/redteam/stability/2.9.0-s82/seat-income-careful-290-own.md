# §8.6: the review fees by seat and by who sat — --entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule; seeds 21–30; the finals' direct (/Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/learned-rev-careful-290-own/direct/models/direct-online-10.pt) and head alone (/Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/learned-rev-careful-290-own/wm/models/wm-online-10.pt), the hand beside. Nominal credits a run, means ± SE over the seeds. A seat's fee is the fixed fee paid from the fee pot at settlement (`feepot_out … review fee`); who sat: a member, the state (a troop), the plant alias (never paid — a check). Beside: the duty uplift paid, the court fees the state won, the bonds burned.

| who sat | seat | case kind | direct | head alone | hand | direct (seats) | head alone (seats) | hand (seats) |
|---|---|---|---|---|---|---|---|---|
| member | appeal | plant | 40 ± 4 | 35 ± 3 | 85 ± 7 | 13.3 | 11.8 | 28.4 |
| member | appeal | real | 407 ± 21 | 358 ± 18 | 697 ± 35 | 158.0 | 139.9 | 259.0 |
| member | audit | plant | 65 ± 5 | 52 ± 2 | 250 ± 17 | 21.8 | 17.2 | 83.4 |
| member | audit | real | 2370 ± 57 | 2222 ± 43 | 2845 ± 93 | 855.5 | 801.0 | 1002.8 |
| member | initial | plant | 130 ± 10 | 124 ± 5 | 292 ± 12 | 65.2 | 61.8 | 145.9 |
| member | initial | real | 5045 ± 19 | 5115 ± 22 | 5087 ± 56 | 2617.3 | 2651.4 | 2600.4 |
| state | appeal | real | 345 ± 15 | 366 ± 6 | 304 ± 16 | 134.7 | 145.0 | 116.4 |
| state | audit | real | 2162 ± 67 | 2375 ± 46 | 1834 ± 62 | 753.2 | 825.9 | 624.8 |
| state | initial | real | 1 ± 0 | 1 ± 0 | 11 ± 3 | 0.6 | 0.3 | 5.4 |

Totals by who sat (review fees a run):

| who sat | direct | head alone | hand |
|---|---|---|---|
| member | 8058 ± 71 | 7905 ± 53 | 9256 ± 186 |
| state | 2508 ± 76 | 2741 ± 50 | 2149 ± 75 |
| plant alias | 0 ± 0 | 0 ± 0 | 0 ± 0 |

The members' panel income (appeal + dispute seats, real and plant) and the state's audit-seat income:

| reading | direct | head alone | hand |
|---|---|---|---|
| members' panel fees | 447 ± 22 | 393 ± 18 | 782 ± 34 |
| members' audit-seat fees | 2436 ± 56 | 2273 ± 44 | 3095 ± 109 |
| state's audit-seat fees | 2162 ± 67 | 2375 ± 46 | 1834 ± 62 |
| state's panel fees | 345 ± 15 | 366 ± 6 | 304 ± 16 |
| state's initial-seat fees | 1 ± 0 | 1 ± 0 | 11 ± 3 |

Beside:

| flow | to / from | direct | head alone | hand |
|---|---|---|---|---|
| bond burned | member | 780 ± 26 | 664 ± 20 | 1449 ± 36 |
| bond burned | state | 172 ± 13 | 207 ± 12 | 165 ± 10 |
| court fee won | member | 192 ± 4 | 195 ± 4 | 154 ± 6 |
| members' audits of real approvals (the base), a run | member | 816 ± 28 | 770 ± 19 | 958 ± 32 |
| service fee to Ω | state | 2402 ± 43 | 2363 ± 39 | 2456 ± 18 |
| uplift | member | 231 ± 127 | 89 ± 41 | 3860 ± 130 |

The dial per seat's path by period (seed: real member audits of real approvals | m^A | π^A | pool A [hit, adj] | pa adjudicated | confirmed):

- direct seed 21: 20 | 1.0 | 0.02 | [0, 0] | 0 | 0; 79 | 1.0 | 0.02 | [1, 1] | 1 | 1; 224 | 1.0 | 0.02 | [4, 6] | 5 | 3; 290 | 2.0 | 0.04 | [0, 0] | 6 | 3; 227 | 2.0 | 0.04 | [7, 9] | 9 | 7
- direct seed 22: 75 | 1.0 | 0.02 | [0, 1] | 1 | 0; 129 | 1.0 | 0.02 | [3, 4] | 3 | 3; 133 | 1.0 | 0.02 | [5, 6] | 2 | 2; 264 | 2.0 | 0.04 | [0, 0] | 5 | 1; 194 | 2.0 | 0.04 | [4, 8] | 8 | 4
- direct seed 23: 28 | 1.0 | 0.02 | [0, 0] | 0 | 0; 87 | 1.0 | 0.02 | [2, 2] | 2 | 2; 176 | 1.0 | 0.02 | [4, 5] | 3 | 2; 271 | 2.0 | 0.04 | [0, 0] | 6 | 3; 244 | 2.0 | 0.04 | [2, 9] | 9 | 2
- head alone seed 21: 17 | 1.0 | 0.02 | [0, 0] | 0 | 0; 84 | 1.0 | 0.02 | [0, 1] | 1 | 0; 245 | 1.0 | 0.02 | [2, 6] | 5 | 2; 282 | 2.0 | 0.04 | [0, 0] | 6 | 4; 128 | 2.0 | 0.04 | [1, 5] | 5 | 1
- head alone seed 22: 15 | 1.0 | 0.02 | [0, 0] | 0 | 0; 87 | 1.0 | 0.02 | [1, 1] | 1 | 1; 153 | 1.0 | 0.02 | [2, 4] | 3 | 1; 252 | 1.0 | 0.02 | [7, 9] | 5 | 5; 294 | 2.0 | 0.04 | [0, 0] | 5 | 2
- head alone seed 23: 68 | 1.0 | 0.02 | [1, 1] | 1 | 1; 55 | 1.0 | 0.02 | [1, 2] | 1 | 0; 181 | 1.0 | 0.02 | [5, 6] | 4 | 4; 167 | 1.0 | 0.02 | [8, 9] | 3 | 3; 160 | 2.0 | 0.04 | [0, 0] | 3 | 3; 99 | 2.0 | 0.04 | [2, 4] | 4 | 2
- hand seed 21: 20 | 1.0 | 0.02 | [0, 0] | 0 | 0; 6 | 1.0 | 0.02 | [0, 0] | 0 | 0; 52 | 1.0 | 0.02 | [0, 1] | 1 | 0; 71 | 1.0 | 0.02 | [0, 2] | 1 | 0; 81 | 1.0 | 0.02 | [1, 4] | 2 | 1; 90 | 1.0 | 0.02 | [1, 6] | 2 | 0; 92 | 1.0 | 0.02 | [1, 8] | 2 | 0; 106 | 1.0 | 0.02 | [0, 0] | 2 | 0; 93 | 1.0 | 0.02 | [1, 2] | 2 | 1; 107 | 1.0 | 0.02 | [1, 4] | 2 | 0; 105 | 1.0 | 0.02 | [1, 6] | 2 | 0
- hand seed 22: 18 | 1.0 | 0.02 | [0, 0] | 0 | 0; 10 | 1.0 | 0.02 | [0, 0] | 0 | 0; 70 | 1.0 | 0.02 | [0, 1] | 1 | 0; 88 | 1.0 | 0.02 | [0, 3] | 2 | 0; 84 | 1.0 | 0.02 | [0, 5] | 2 | 0; 99 | 1.0 | 0.02 | [0, 7] | 2 | 0; 97 | 1.0 | 0.02 | [0, 9] | 2 | 0; 109 | 1.0 | 0.02 | [0, 0] | 2 | 0; 98 | 1.0 | 0.02 | [0, 2] | 2 | 0; 99 | 1.0 | 0.02 | [1, 4] | 2 | 1; 98 | 1.0 | 0.02 | [1, 6] | 2 | 0
- hand seed 23: 19 | 1.0 | 0.02 | [0, 0] | 0 | 0; 34 | 1.0 | 0.02 | [0, 0] | 0 | 0; 60 | 1.0 | 0.02 | [0, 1] | 1 | 0; 76 | 1.0 | 0.02 | [0, 2] | 1 | 0; 95 | 1.0 | 0.02 | [0, 4] | 2 | 0; 90 | 1.0 | 0.02 | [0, 6] | 2 | 0; 82 | 1.0 | 0.02 | [0, 7] | 1 | 0; 90 | 1.0 | 0.02 | [0, 9] | 2 | 0; 89 | 1.0 | 0.02 | [0, 0] | 2 | 0; 105 | 1.0 | 0.02 | [0, 2] | 2 | 0; 100 | 1.0 | 0.02 | [0, 4] | 2 | 0; 101 | 1.0 | 0.02 | [0, 6] | 2 | 0; 92 | 1.0 | 0.02 | [0, 8] | 2 | 0

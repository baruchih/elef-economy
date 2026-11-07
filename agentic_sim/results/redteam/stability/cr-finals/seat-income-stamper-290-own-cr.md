# §8.6: the review fees by seat and by who sat — --entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule; seeds 21–40; the finals' direct (/Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/learned-rev-stamper-290-own/direct/models/direct-online-10.pt) and head alone (/Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/learned-rev-stamper-290-own/wm/models/wm-online-10.pt), the hand beside. Nominal credits a run, means ± SE over the seeds. A seat's fee is the fixed fee paid from the fee pot at settlement (`feepot_out … review fee`); who sat: a member, the state (a troop), the plant alias (never paid — a check). Beside: the duty uplift paid, the court fees the state won, the bonds burned.

| who sat | seat | case kind | direct | head alone | hand | direct (seats) | head alone (seats) | hand (seats) |
|---|---|---|---|---|---|---|---|---|
| member | appeal | plant | 39 ± 4 | 39 ± 3 | 83 ± 5 | 12.9 | 13.1 | 27.6 |
| member | appeal | real | 504 ± 17 | 433 ± 18 | 799 ± 22 | 194.0 | 169.2 | 300.2 |
| member | audit | plant | 89 ± 12 | 96 ± 5 | 292 ± 9 | 29.6 | 31.9 | 97.4 |
| member | audit | real | 3152 ± 84 | 2924 ± 72 | 3559 ± 64 | 1151.3 | 1083.5 | 1279.5 |
| member | initial | plant | 130 ± 8 | 143 ± 6 | 280 ± 6 | 65.1 | 71.6 | 139.9 |
| member | initial | real | 5014 ± 36 | 4995 ± 26 | 4979 ± 32 | 2640.7 | 2648.2 | 2588.1 |
| state | appeal | real | 325 ± 12 | 355 ± 13 | 296 ± 13 | 128.6 | 141.2 | 113.8 |
| state | audit | real | 2184 ± 74 | 2358 ± 84 | 1828 ± 51 | 764.6 | 828.0 | 625.7 |
| state | initial | real | 2 ± 1 | 1 ± 0 | 23 ± 3 | 0.8 | 0.7 | 12.1 |

Totals by who sat (review fees a run):

| who sat | direct | head alone | hand |
|---|---|---|---|
| member | 8928 ± 133 | 8630 ± 98 | 9993 ± 103 |
| state | 2510 ± 84 | 2714 ± 94 | 2148 ± 61 |
| plant alias | 0 ± 0 | 0 ± 0 | 0 ± 0 |

The members' panel income (appeal + dispute seats, real and plant) and the state's audit-seat income:

| reading | direct | head alone | hand |
|---|---|---|---|
| members' panel fees | 543 ± 20 | 472 ± 18 | 882 ± 23 |
| members' audit-seat fees | 3241 ± 89 | 3019 ± 72 | 3851 ± 66 |
| state's audit-seat fees | 2184 ± 74 | 2358 ± 84 | 1828 ± 51 |
| state's panel fees | 325 ± 12 | 355 ± 13 | 296 ± 13 |
| state's initial-seat fees | 2 ± 1 | 1 ± 0 | 23 ± 3 |

Beside:

| flow | to / from | direct | head alone | hand |
|---|---|---|---|---|
| bond burned | member | 863 ± 25 | 822 ± 17 | 1501 ± 29 |
| bond burned | state | 179 ± 11 | 208 ± 12 | 167 ± 7 |
| court fee won | member | 190 ± 4 | 187 ± 4 | 163 ± 5 |
| members' audits of real approvals (the base), a run | member | 1068 ± 29 | 996 ± 31 | 1216 ± 31 |
| service fee to Ω | state | 2407 ± 33 | 2394 ± 24 | 2401 ± 9 |
| uplift | member | 182 ± 133 | 318 ± 65 | 3626 ± 65 |

The dial per seat's path by period (seed: real member audits of real approvals | m^A | π^A | pool A [hit, adj] | pa adjudicated | confirmed):

- direct seed 21: 20 | 1.0 | 0.02 | [0, 0] | 0 | 0; 114 | 1.0 | 0.02 | [0, 1] | 1 | 0; 249 | 1.0 | 0.02 | [2, 6] | 5 | 2; 319 | 1.666667 | 0.033333 | [0, 0] | 6 | 0; 340 | 3.333333 | 0.066667 | [0, 0] | 12 | 11
- direct seed 22: 72 | 1.0 | 0.02 | [0, 1] | 1 | 0; 138 | 1.0 | 0.02 | [2, 4] | 3 | 2; 291 | 1.0 | 0.02 | [4, 9] | 5 | 2; 321 | 2.0 | 0.04 | [0, 0] | 7 | 3; 335 | 3.076923 | 0.061538 | [0, 0] | 13 | 2
- direct seed 23: 109 | 1.0 | 0.02 | [0, 2] | 2 | 0; 187 | 1.0 | 0.02 | [2, 5] | 3 | 2; 217 | 2.0 | 0.04 | [0, 0] | 5 | 2; 309 | 4.0 | 0.08 | [0, 0] | 12 | 8; 288 | 8.0 | 0.16 | [0, 0] | 22 | 13
- head alone seed 21: 20 | 1.0 | 0.02 | [0, 0] | 0 | 0; 106 | 1.0 | 0.02 | [1, 2] | 2 | 1; 275 | 1.0 | 0.02 | [4, 8] | 6 | 3; 206 | 2.0 | 0.04 | [0, 0] | 4 | 3; 246 | 2.0 | 0.04 | [8, 9] | 9 | 8
- head alone seed 22: 15 | 1.0 | 0.02 | [0, 0] | 0 | 0; 92 | 1.0 | 0.02 | [2, 2] | 2 | 2; 130 | 1.0 | 0.02 | [4, 4] | 2 | 2; 330 | 2.0 | 0.04 | [0, 0] | 7 | 3; 326 | 4.0 | 0.08 | [0, 0] | 13 | 6
- head alone seed 23: 17 | 1.0 | 0.02 | [0, 0] | 0 | 0; 91 | 1.0 | 0.02 | [1, 2] | 2 | 1; 233 | 1.0 | 0.02 | [5, 6] | 4 | 4; 193 | 2.0 | 0.04 | [0, 0] | 4 | 3; 286 | 4.0 | 0.08 | [0, 0] | 11 | 7
- hand seed 21: 20 | 1.0 | 0.02 | [0, 0] | 0 | 0; 0 | 1.0 | 0.02 | [0, 0] | 0 | 0; 37 | 1.0 | 0.02 | [0, 0] | 0 | 0; 61 | 1.0 | 0.02 | [0, 2] | 2 | 0; 89 | 1.0 | 0.02 | [0, 3] | 1 | 0; 108 | 1.0 | 0.02 | [0, 6] | 3 | 0; 127 | 1.0 | 0.02 | [0, 8] | 2 | 0; 137 | 1.0 | 0.02 | [0, 0] | 3 | 0; 150 | 1.0 | 0.02 | [0, 3] | 3 | 0; 161 | 1.0 | 0.02 | [0, 6] | 3 | 0
- hand seed 22: 18 | 1.0 | 0.02 | [0, 0] | 0 | 0; 18 | 1.0 | 0.02 | [0, 0] | 0 | 0; 61 | 1.0 | 0.02 | [0, 1] | 1 | 0; 80 | 1.0 | 0.02 | [0, 3] | 2 | 0; 102 | 1.0 | 0.02 | [0, 5] | 2 | 0; 136 | 1.0 | 0.02 | [0, 8] | 3 | 0; 138 | 1.0 | 0.02 | [0, 0] | 2 | 0; 139 | 1.0 | 0.02 | [0, 3] | 3 | 0; 161 | 1.0 | 0.02 | [1, 6] | 3 | 1; 177 | 1.0 | 0.02 | [0, 0] | 4 | 0; 197 | 1.0 | 0.02 | [0, 4] | 4 | 0
- hand seed 23: 19 | 1.0 | 0.02 | [0, 0] | 0 | 0; 11 | 1.0 | 0.02 | [0, 0] | 0 | 0; 62 | 1.0 | 0.02 | [0, 1] | 1 | 0; 88 | 1.0 | 0.02 | [0, 3] | 2 | 0; 96 | 1.0 | 0.02 | [0, 5] | 2 | 0; 108 | 1.0 | 0.02 | [1, 7] | 2 | 1; 120 | 1.0 | 0.02 | [1, 9] | 2 | 0; 136 | 1.0 | 0.02 | [0, 0] | 3 | 0; 143 | 1.0 | 0.02 | [1, 3] | 3 | 1; 162 | 1.0 | 0.02 | [1, 6] | 3 | 0; 190 | 2.0 | 0.04 | [0, 0] | 4 | 1; 192 | 2.0 | 0.04 | [0, 7] | 7 | 0

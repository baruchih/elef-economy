# §8.6: the review fees by seat and by who sat — --entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule; seeds 21–40; the finals' direct (/Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/learned-rev-careful-290-own/direct/models/direct-online-10.pt) and head alone (/Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/learned-rev-careful-290-own/wm/models/wm-online-10.pt), the hand beside. Nominal credits a run, means ± SE over the seeds. A seat's fee is the fixed fee paid from the fee pot at settlement (`feepot_out … review fee`); who sat: a member, the state (a troop), the plant alias (never paid — a check). Beside: the duty uplift paid, the court fees the state won, the bonds burned.

| who sat | seat | case kind | direct | head alone | hand | direct (seats) | head alone (seats) | hand (seats) |
|---|---|---|---|---|---|---|---|---|
| member | appeal | plant | 34 ± 2 | 36 ± 3 | 83 ± 5 | 11.5 | 12.1 | 27.6 |
| member | appeal | real | 499 ± 19 | 474 ± 26 | 799 ± 22 | 193.8 | 183.8 | 300.2 |
| member | audit | plant | 89 ± 5 | 87 ± 7 | 292 ± 9 | 29.7 | 29.1 | 97.4 |
| member | audit | real | 3114 ± 63 | 3061 ± 95 | 3559 ± 64 | 1144.4 | 1121.0 | 1279.5 |
| member | initial | plant | 129 ± 4 | 136 ± 7 | 280 ± 6 | 64.7 | 67.8 | 139.9 |
| member | initial | real | 4976 ± 20 | 5007 ± 24 | 4979 ± 32 | 2627.7 | 2638.4 | 2588.1 |
| state | appeal | real | 325 ± 10 | 347 ± 17 | 296 ± 13 | 128.3 | 136.3 | 113.8 |
| state | audit | real | 2217 ± 65 | 2210 ± 92 | 1828 ± 51 | 776.0 | 771.6 | 625.7 |
| state | initial | real | 2 ± 0 | 1 ± 0 | 23 ± 3 | 1.2 | 0.8 | 12.1 |

Totals by who sat (review fees a run):

| who sat | direct | head alone | hand |
|---|---|---|---|
| member | 8842 ± 83 | 8801 ± 135 | 9993 ± 103 |
| state | 2545 ± 70 | 2559 ± 107 | 2148 ± 61 |
| plant alias | 0 ± 0 | 0 ± 0 | 0 ± 0 |

The members' panel income (appeal + dispute seats, real and plant) and the state's audit-seat income:

| reading | direct | head alone | hand |
|---|---|---|---|
| members' panel fees | 533 ± 20 | 510 ± 29 | 882 ± 23 |
| members' audit-seat fees | 3203 ± 64 | 3148 ± 97 | 3851 ± 66 |
| state's audit-seat fees | 2217 ± 65 | 2210 ± 92 | 1828 ± 51 |
| state's panel fees | 325 ± 10 | 347 ± 17 | 296 ± 13 |
| state's initial-seat fees | 2 ± 0 | 1 ± 0 | 23 ± 3 |

Beside:

| flow | to / from | direct | head alone | hand |
|---|---|---|---|---|
| bond burned | member | 847 ± 20 | 841 ± 18 | 1501 ± 29 |
| bond burned | state | 169 ± 11 | 204 ± 11 | 167 ± 7 |
| court fee won | member | 193 ± 5 | 196 ± 5 | 163 ± 5 |
| members' audits of real approvals (the base), a run | member | 1055 ± 20 | 1020 ± 40 | 1216 ± 31 |
| service fee to Ω | state | 2380 ± 22 | 2415 ± 24 | 2401 ± 9 |
| uplift | member | 114 ± 40 | 184 ± 87 | 3626 ± 65 |

The dial per seat's path by period (seed: real member audits of real approvals | m^A | π^A | pool A [hit, adj] | pa adjudicated | confirmed):

- direct seed 21: 20 | 1.0 | 0.02 | [0, 0] | 0 | 0; 69 | 1.0 | 0.02 | [1, 1] | 1 | 1; 255 | 1.0 | 0.02 | [4, 6] | 5 | 3; 300 | 2.0 | 0.04 | [0, 0] | 6 | 2; 282 | 4.0 | 0.08 | [0, 0] | 11 | 5
- direct seed 22: 77 | 1.0 | 0.02 | [0, 1] | 1 | 0; 194 | 1.0 | 0.02 | [0, 5] | 4 | 0; 275 | 2.0 | 0.04 | [0, 0] | 5 | 3; 352 | 4.0 | 0.08 | [0, 0] | 14 | 6; 251 | 8.0 | 0.16 | [0, 0] | 20 | 9
- direct seed 23: 47 | 1.0 | 0.02 | [0, 0] | 0 | 0; 70 | 1.0 | 0.02 | [2, 2] | 2 | 2; 206 | 1.0 | 0.02 | [5, 6] | 4 | 3; 307 | 2.0 | 0.04 | [0, 0] | 6 | 5; 324 | 4.0 | 0.08 | [0, 0] | 13 | 6
- head alone seed 21: 17 | 1.0 | 0.02 | [0, 0] | 0 | 0; 155 | 1.0 | 0.02 | [3, 3] | 3 | 3; 273 | 1.0 | 0.02 | [4, 8] | 5 | 1; 308 | 2.0 | 0.04 | [0, 0] | 7 | 4; 350 | 4.0 | 0.08 | [0, 0] | 13 | 6
- head alone seed 22: 15 | 1.0 | 0.02 | [0, 0] | 0 | 0; 66 | 1.0 | 0.02 | [1, 1] | 1 | 1; 236 | 1.0 | 0.02 | [4, 6] | 5 | 3; 246 | 2.0 | 0.04 | [0, 0] | 5 | 4; 194 | 2.0 | 0.04 | [2, 7] | 7 | 2
- head alone seed 23: 73 | 1.0 | 0.02 | [0, 1] | 1 | 0; 35 | 1.0 | 0.02 | [1, 2] | 1 | 1; 185 | 1.0 | 0.02 | [1, 5] | 3 | 0; 254 | 1.0 | 0.02 | [4, 9] | 4 | 3; 295 | 2.0 | 0.04 | [0, 0] | 6 | 3
- hand seed 21: 20 | 1.0 | 0.02 | [0, 0] | 0 | 0; 0 | 1.0 | 0.02 | [0, 0] | 0 | 0; 37 | 1.0 | 0.02 | [0, 0] | 0 | 0; 61 | 1.0 | 0.02 | [0, 2] | 2 | 0; 89 | 1.0 | 0.02 | [0, 3] | 1 | 0; 108 | 1.0 | 0.02 | [0, 6] | 3 | 0; 127 | 1.0 | 0.02 | [0, 8] | 2 | 0; 137 | 1.0 | 0.02 | [0, 0] | 3 | 0; 150 | 1.0 | 0.02 | [0, 3] | 3 | 0; 161 | 1.0 | 0.02 | [0, 6] | 3 | 0
- hand seed 22: 18 | 1.0 | 0.02 | [0, 0] | 0 | 0; 18 | 1.0 | 0.02 | [0, 0] | 0 | 0; 61 | 1.0 | 0.02 | [0, 1] | 1 | 0; 80 | 1.0 | 0.02 | [0, 3] | 2 | 0; 102 | 1.0 | 0.02 | [0, 5] | 2 | 0; 136 | 1.0 | 0.02 | [0, 8] | 3 | 0; 138 | 1.0 | 0.02 | [0, 0] | 2 | 0; 139 | 1.0 | 0.02 | [0, 3] | 3 | 0; 161 | 1.0 | 0.02 | [1, 6] | 3 | 1; 177 | 1.0 | 0.02 | [0, 0] | 4 | 0; 197 | 1.0 | 0.02 | [0, 4] | 4 | 0
- hand seed 23: 19 | 1.0 | 0.02 | [0, 0] | 0 | 0; 11 | 1.0 | 0.02 | [0, 0] | 0 | 0; 62 | 1.0 | 0.02 | [0, 1] | 1 | 0; 88 | 1.0 | 0.02 | [0, 3] | 2 | 0; 96 | 1.0 | 0.02 | [0, 5] | 2 | 0; 108 | 1.0 | 0.02 | [1, 7] | 2 | 1; 120 | 1.0 | 0.02 | [1, 9] | 2 | 0; 136 | 1.0 | 0.02 | [0, 0] | 3 | 0; 143 | 1.0 | 0.02 | [1, 3] | 3 | 1; 162 | 1.0 | 0.02 | [1, 6] | 3 | 0; 190 | 2.0 | 0.04 | [0, 0] | 4 | 1; 192 | 2.0 | 0.04 | [0, 7] | 7 | 0

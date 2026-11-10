# The per-seat dial's path by period — `liars` (the economy reviewer's question after §88; `dial_path.py`)

Cell: `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --dispute-policy truthful --appeal-lie 0.1 --dispute-lie 0.1`; seeds 21-40; 1000 ticks (a period 200 ticks: five closed periods and nothing closes the sixth). A run's dial starts at the floor (m^A 1, π^A = π^A_0 0.02 at genesis) and nothing carries between runs. m^A steps at a period's close on a reading of at least ten pooled adjudications of planted approvals at a member's audit seat (Appendix V, `seat_dial_min_adj` 10): `adj` is the period's own count, `pool` what the pool carries forward after the close (confirmed / adjudicated), `F̂^A` the reading where one was taken (mean over the seeds that read one; the count of seeds reading). The planted approvals posted in the period are at π^A per real approval audited by a member in the period (`base`); the partial sixth period's counts are shown for the record.

## direct (20 seeds)

| period | m^A before → after | seeds stepping (↑ / ↓) | π^A after | planted approvals posted | base (members' audits of real approvals) | adj at a member's audit seat | confirmed | pool carried | F̂^A read (n) |
|---|---|---|---|---|---|---|---|---|---|
| p0 (t 0–192) | 1.00 → 1.00 | 0 / 0 of 20 | 0.020 | 0.1 | 29 | 0.0 | 0.0 | 0.0 / 0.0 | — (0) |
| p1 (t 192–392) | 1.00 → 1.00 | 0 / 0 of 20 | 0.020 | 3.0 | 144 | 0.0 | 0.0 | 0.0 / 0.0 | — (0) |
| p2 (t 392–592) | 1.00 → 1.00 | 0 / 0 of 20 | 0.020 | 4.7 | 240 | 0.0 | 0.0 | 0.0 / 0.0 | — (0) |
| p3 (t 592–783) | 1.00 → 1.00 | 0 / 0 of 20 | 0.020 | 5.8 | 285 | 0.0 | 0.0 | 0.0 / 0.0 | — (0) |
| p4 (t 783–915) | 1.00 → 1.00 | 0 / 0 of 20 | 0.020 | 5.0 | 261 | 0.0 | 0.0 | 0.0 / 0.0 | — (0) |
| p5 (t 886–975) | 1.00 → 1.00 | 0 / 0 of 6 | 0.020 | 4.3 | 199 | 0.0 | 0.0 | 0.0 / 0.0 | — (0) |
| p6 (t 879–969) | 1.00 → 1.00 | 0 / 0 of 1 | 0.020 | 4.0 | 161 | 0.0 | 0.0 | 0.0 / 0.0 | — (0) |
| p7 partial (t 915–1000) | 1.00 (no close) | — | 0.020 | 1.2 | 66 | 0.0 | 0.0 | 0.0 / 0.0 | — |

m^A at the run's end: mean 1.00, min 1.00, max 1.00; seeds whose m^A left 1 within the run: 0 of 20; adjudications a closed period, mean over the seeds and periods 0.0 against the ten a step needs; readings taken a run 0.0 of 7 closes.

Every seed's path (m^A after each close; the adjudications at a member's audit seat by period in brackets; F̂^A where read):

- seed 21: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0] ; planted approvals a run 20, audited 0, confirmed 0
- seed 22: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0] ; planted approvals a run 16, audited 0, confirmed 0
- seed 23: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0] ; planted approvals a run 22, audited 0, confirmed 0
- seed 24: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0, 0] ; planted approvals a run 23, audited 0, confirmed 0
- seed 25: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0] ; planted approvals a run 18, audited 0, confirmed 0
- seed 26: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0, 0] ; planted approvals a run 22, audited 0, confirmed 0
- seed 27: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0] ; planted approvals a run 22, audited 0, confirmed 0
- seed 28: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0, 0] ; planted approvals a run 27, audited 0, confirmed 0
- seed 29: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0, 0, 0] ; planted approvals a run 24, audited 0, confirmed 0
- seed 30: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0] ; planted approvals a run 20, audited 0, confirmed 0
- seed 31: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0, 0] ; planted approvals a run 21, audited 0, confirmed 0
- seed 32: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0] ; planted approvals a run 23, audited 0, confirmed 0
- seed 33: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0] ; planted approvals a run 19, audited 0, confirmed 0
- seed 34: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0] ; planted approvals a run 23, audited 0, confirmed 0
- seed 35: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0] ; planted approvals a run 20, audited 0, confirmed 0
- seed 36: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0, 0] ; planted approvals a run 20, audited 0, confirmed 0
- seed 37: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0] ; planted approvals a run 23, audited 0, confirmed 0
- seed 38: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0] ; planted approvals a run 23, audited 0, confirmed 0
- seed 39: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0] ; planted approvals a run 18, audited 0, confirmed 0
- seed 40: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0] ; planted approvals a run 22, audited 0, confirmed 0

## greedy (20 seeds)

| period | m^A before → after | seeds stepping (↑ / ↓) | π^A after | planted approvals posted | base (members' audits of real approvals) | adj at a member's audit seat | confirmed | pool carried | F̂^A read (n) |
|---|---|---|---|---|---|---|---|---|---|
| p0 (t 0–188) | 1.00 → 1.00 | 0 / 0 of 20 | 0.020 | 0.5 | 49 | 0.1 | 0.1 | 0.1 / 0.1 | — (0) |
| p1 (t 188–388) | 1.00 → 1.00 | 0 / 0 of 20 | 0.020 | 3.1 | 154 | 0.1 | 0.1 | 0.1 / 0.1 | — (0) |
| p2 (t 388–573) | 1.00 → 1.00 | 0 / 0 of 20 | 0.020 | 4.6 | 238 | 0.0 | 0.0 | 0.1 / 0.1 | — (0) |
| p3 (t 573–765) | 1.00 → 1.00 | 0 / 0 of 20 | 0.020 | 5.8 | 280 | 0.0 | 0.0 | 0.1 / 0.1 | — (0) |
| p4 (t 765–955) | 1.00 → 1.00 | 0 / 0 of 20 | 0.020 | 5.3 | 274 | 0.0 | 0.0 | 0.1 / 0.1 | — (0) |
| p5 (t 639–744) | 1.00 → 1.00 | 0 / 0 of 2 | 0.020 | 4.0 | 204 | 0.0 | 0.0 | 0.0 / 0.0 | — (0) |
| p6 (t 744–860) | 1.00 → 1.00 | 0 / 0 of 2 | 0.020 | 3.5 | 183 | 0.0 | 0.0 | 0.0 / 0.0 | — (0) |
| p7 (t 860–989) | 1.00 → 1.00 | 0 / 0 of 1 | 0.020 | 4.0 | 209 | 0.0 | 0.0 | 0.0 / 0.0 | — (0) |
| p8 partial (t 955–1000) | 1.00 (no close) | — | 0.020 | 1.6 | 73 | 0.0 | 0.0 | 0.1 / 0.1 | — |

m^A at the run's end: mean 1.00, min 1.00, max 1.00; seeds whose m^A left 1 within the run: 0 of 20; adjudications a closed period, mean over the seeds and periods 0.0 against the ten a step needs; readings taken a run 0.0 of 8 closes.

Every seed's path (m^A after each close; the adjudications at a member's audit seat by period in brackets; F̂^A where read):

- seed 21: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0] ; planted approvals a run 24, audited 0, confirmed 0
- seed 22: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [1, 1, 0, 0, 0] ; planted approvals a run 22, audited 2, confirmed 2
- seed 23: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0] ; planted approvals a run 24, audited 0, confirmed 0
- seed 24: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0] ; planted approvals a run 21, audited 0, confirmed 0
- seed 25: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0] ; planted approvals a run 20, audited 0, confirmed 0
- seed 26: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0] ; planted approvals a run 24, audited 0, confirmed 0
- seed 27: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0] ; planted approvals a run 22, audited 0, confirmed 0
- seed 28: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0] ; planted approvals a run 21, audited 0, confirmed 0
- seed 29: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0, 0, 0, 0] ; planted approvals a run 23, audited 0, confirmed 0
- seed 30: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0] ; planted approvals a run 17, audited 0, confirmed 0
- seed 31: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0] ; planted approvals a run 25, audited 0, confirmed 0
- seed 32: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0] ; planted approvals a run 21, audited 0, confirmed 0
- seed 33: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0] ; planted approvals a run 23, audited 0, confirmed 0
- seed 34: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0, 0, 0] ; planted approvals a run 23, audited 0, confirmed 0
- seed 35: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0] ; planted approvals a run 20, audited 0, confirmed 0
- seed 36: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0] ; planted approvals a run 24, audited 0, confirmed 0
- seed 37: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0] ; planted approvals a run 21, audited 0, confirmed 0
- seed 38: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0] ; planted approvals a run 19, audited 0, confirmed 0
- seed 39: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0] ; planted approvals a run 22, audited 0, confirmed 0
- seed 40: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0] ; planted approvals a run 21, audited 0, confirmed 0

## hand (20 seeds)

| period | m^A before → after | seeds stepping (↑ / ↓) | π^A after | planted approvals posted | base (members' audits of real approvals) | adj at a member's audit seat | confirmed | pool carried | F̂^A read (n) |
|---|---|---|---|---|---|---|---|---|---|
| p0 (t 0–190) | 1.00 → 1.00 | 0 / 0 of 20 | 0.020 | 0.1 | 22 | 0.0 | 0.0 | 0.0 / 0.0 | — (0) |
| p1 (t 190–302) | 1.00 → 1.00 | 0 / 0 of 20 | 0.020 | 0.8 | 52 | 0.0 | 0.0 | 0.0 / 0.0 | — (0) |
| p2 (t 302–364) | 1.00 → 1.00 | 0 / 0 of 20 | 0.020 | 1.3 | 58 | 0.0 | 0.0 | 0.0 / 0.0 | — (0) |
| p3 (t 364–429) | 1.00 → 1.00 | 0 / 0 of 20 | 0.020 | 1.4 | 74 | 0.0 | 0.0 | 0.0 / 0.0 | — (0) |
| p4 (t 429–482) | 1.00 → 1.00 | 0 / 0 of 20 | 0.020 | 1.6 | 83 | 0.0 | 0.0 | 0.0 / 0.0 | — (0) |
| p5 (t 482–545) | 1.00 → 1.00 | 0 / 0 of 20 | 0.020 | 1.9 | 96 | 0.0 | 0.0 | 0.0 / 0.0 | — (0) |
| p6 (t 545–617) | 1.00 → 1.00 | 0 / 0 of 20 | 0.020 | 2.1 | 107 | 0.0 | 0.0 | 0.0 / 0.0 | — (0) |
| p7 (t 617–697) | 1.00 → 1.00 | 0 / 0 of 20 | 0.020 | 2.2 | 113 | 0.0 | 0.0 | 0.0 / 0.0 | — (0) |
| p8 (t 697–786) | 1.00 → 1.00 | 0 / 0 of 20 | 0.020 | 2.4 | 119 | 0.0 | 0.0 | 0.0 / 0.0 | — (0) |
| p9 (t 786–884) | 1.00 → 1.00 | 0 / 0 of 20 | 0.020 | 2.8 | 132 | 0.0 | 0.0 | 0.0 / 0.0 | — (0) |
| p10 (t 884–996) | 1.00 → 1.00 | 0 / 0 of 19 | 0.020 | 2.7 | 143 | 0.0 | 0.0 | 0.0 / 0.0 | — (0) |
| p11 (t 836–919) | 1.00 → 1.00 | 0 / 0 of 8 | 0.020 | 2.9 | 134 | 0.0 | 0.0 | 0.0 / 0.0 | — (0) |
| p12 (t 880–941) | 1.00 → 1.00 | 0 / 0 of 2 | 0.020 | 2.5 | 120 | 0.0 | 0.0 | 0.0 / 0.0 | — (0) |
| p13 partial (t 996–1000) | 1.00 (no close) | — | 0.020 | 1.6 | 76 | 0.0 | 0.0 | 0.0 / 0.0 | — |

m^A at the run's end: mean 1.00, min 1.00, max 1.00; seeds whose m^A left 1 within the run: 0 of 20; adjudications a closed period, mean over the seeds and periods 0.0 against the ten a step needs; readings taken a run 0.0 of 13 closes.

Every seed's path (m^A after each close; the adjudications at a member's audit seat by period in brackets; F̂^A where read):

- seed 21: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ; planted approvals a run 23, audited 0, confirmed 0
- seed 22: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ; planted approvals a run 21, audited 0, confirmed 0
- seed 23: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ; planted approvals a run 22, audited 0, confirmed 0
- seed 24: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ; planted approvals a run 23, audited 0, confirmed 0
- seed 25: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ; planted approvals a run 23, audited 0, confirmed 0
- seed 26: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ; planted approvals a run 23, audited 0, confirmed 0
- seed 27: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ; planted approvals a run 24, audited 0, confirmed 0
- seed 28: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ; planted approvals a run 22, audited 0, confirmed 0
- seed 29: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ; planted approvals a run 21, audited 0, confirmed 0
- seed 30: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ; planted approvals a run 22, audited 0, confirmed 0
- seed 31: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ; planted approvals a run 22, audited 0, confirmed 0
- seed 32: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ; planted approvals a run 21, audited 0, confirmed 0
- seed 33: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ; planted approvals a run 21, audited 0, confirmed 0
- seed 34: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ; planted approvals a run 22, audited 0, confirmed 0
- seed 35: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ; planted approvals a run 22, audited 0, confirmed 0
- seed 36: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ; planted approvals a run 20, audited 0, confirmed 0
- seed 37: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ; planted approvals a run 23, audited 0, confirmed 0
- seed 38: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ; planted approvals a run 22, audited 0, confirmed 0
- seed 39: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ; planted approvals a run 25, audited 0, confirmed 0
- seed 40: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ; planted approvals a run 22, audited 0, confirmed 0


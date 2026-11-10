# The per-seat dial's path by period — `run42` (the economy reviewer's question after §88; `dial_path.py`)

Cell: `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule`; seeds 21-40; 1000 ticks (a period 200 ticks: five closed periods and nothing closes the sixth). A run's dial starts at the floor (m^A 1, π^A = π^A_0 0.02 at genesis) and nothing carries between runs. m^A steps at a period's close on a reading of at least ten pooled adjudications of planted approvals at a member's audit seat (Appendix V, `seat_dial_min_adj` 10): `adj` is the period's own count, `pool` what the pool carries forward after the close (confirmed / adjudicated), `F̂^A` the reading where one was taken (mean over the seeds that read one; the count of seeds reading). The planted approvals posted in the period are at π^A per real approval audited by a member in the period (`base`); the partial sixth period's counts are shown for the record.

## direct (20 seeds)

| period | m^A before → after | seeds stepping (↑ / ↓) | π^A after | planted approvals posted | base (members' audits of real approvals) | adj at a member's audit seat | confirmed | pool carried | F̂^A read (n) |
|---|---|---|---|---|---|---|---|---|---|
| p0 (t 0–184) | 1.00 → 1.00 | 0 / 0 of 20 | 0.020 | 0.2 | 34 | 0.2 | 0.1 | 0.1 / 0.2 | — (0) |
| p1 (t 184–384) | 1.00 → 1.00 | 0 / 0 of 20 | 0.020 | 2.6 | 132 | 2.5 | 1.1 | 1.1 / 2.8 | — (0) |
| p2 (t 384–557) | 1.00 → 1.15 | 3 / 0 of 20 | 0.023 | 5.2 | 262 | 5.1 | 2.8 | 3.4 / 6.3 | 0.37 (3) |
| p3 (t 557–750) | 1.15 → 2.30 | 20 / 0 of 20 | 0.046 | 6.7 | 292 | 6.8 | 3.6 | 0.0 / 0.0 | 0.54 (20) |
| p4 (t 750–937) | 2.30 → 4.37 | 18 / 0 of 20 | 0.087 | 13.8 | 299 | 13.6 | 5.8 | 0.3 / 0.8 | 0.44 (18) |
| p5 (t 829–976) | 2.67 → 5.33 | 3 / 0 of 3 | 0.107 | 12.7 | 230 | 12.0 | 3.0 | 0.0 / 0.0 | 0.31 (3) |
| p6 partial (t 937–1000) | 4.77 (no close) | — | 0.095 | 9.3 | 96 | 9.3 | 2.5 | 0.0 / 0.0 | — |

m^A at the run's end: mean 4.77, min 3.33, max 8.00; seeds whose m^A left 1 within the run: 20 of 20 (first at period p2–p3, median p3); adjudications a closed period, mean over the seeds and periods 5.8 against the ten a step needs; readings taken a run 2.2 of 6 closes.

Every seed's path (m^A after each close; the adjudications at a member's audit seat by period in brackets; F̂^A where read):

- seed 21: 1.00 → 1.00 → 1.00 → 2.00 → 4.00 [0, 1, 5, 6, 11] p3 F̂^A 0.50, p4 F̂^A 0.45; planted approvals a run 32, audited 32, confirmed 13
- seed 22: 1.00 → 1.00 → 2.00 → 4.00 → 8.00 [1, 4, 5, 14, 20] p2 F̂^A 0.30, p3 F̂^A 0.43, p4 F̂^A 0.45; planted approvals a run 70, audited 69, confirmed 24
- seed 23: 1.00 → 1.00 → 1.00 → 2.00 → 4.00 [0, 2, 4, 6, 13] p3 F̂^A 0.83, p4 F̂^A 0.46; planted approvals a run 29, audited 28, confirmed 17
- seed 24: 1.00 → 1.00 → 1.00 → 2.00 → 4.00 [0, 3, 5, 7, 14] p3 F̂^A 0.47, p4 F̂^A 0.36; planted approvals a run 33, audited 31, confirmed 13
- seed 25: 1.00 → 1.00 → 1.00 → 2.00 → 4.00 [0, 2, 5, 6, 12] p3 F̂^A 0.77, p4 F̂^A 0.50; planted approvals a run 30, audited 30, confirmed 17
- seed 26: 1.00 → 1.00 → 1.00 → 2.00 → 4.00 → 8.00 [1, 2, 4, 4, 11, 19] p3 F̂^A 0.55, p4 F̂^A 0.64, p5 F̂^A 0.21; planted approvals a run 50, audited 49, confirmed 19
- seed 27: 1.00 → 1.00 → 1.00 → 2.00 → 4.00 [1, 1, 7, 6, 15] p3 F̂^A 0.53, p4 F̂^A 0.33; planted approvals a run 34, audited 33, confirmed 13
- seed 28: 1.00 → 1.00 → 1.00 → 2.00 → 4.00 [0, 3, 4, 7, 14] p3 F̂^A 0.50, p4 F̂^A 0.21; planted approvals a run 35, audited 33, confirmed 13
- seed 29: 1.00 → 1.00 → 1.00 → 2.00 → 4.00 [0, 2, 5, 6, 10] p3 F̂^A 0.85, p4 F̂^A 0.50; planted approvals a run 40, audited 39, confirmed 22
- seed 30: 1.00 → 1.00 → 1.00 → 2.00 → 3.33 [0, 2, 5, 7, 12] p3 F̂^A 0.43, p4 F̂^A 0.17; planted approvals a run 34, audited 34, confirmed 9
- seed 31: 1.00 → 1.00 → 2.00 → 4.00 → 8.00 [0, 4, 6, 11, 23] p2 F̂^A 0.40, p3 F̂^A 0.64, p4 F̂^A 0.35; planted approvals a run 69, audited 68, confirmed 25
- seed 32: 1.00 → 1.00 → 1.00 → 2.00 → 2.00 → 4.00 [0, 2, 5, 6, 8, 7] p3 F̂^A 0.62, p5 F̂^A 0.33; planted approvals a run 36, audited 36, confirmed 14
- seed 33: 1.00 → 1.00 → 2.00 → 4.00 → 8.00 [0, 4, 6, 13, 25] p2 F̂^A 0.40, p3 F̂^A 0.46, p4 F̂^A 0.28; planted approvals a run 63, audited 62, confirmed 21
- seed 34: 1.00 → 1.00 → 1.00 → 2.00 → 4.00 [0, 2, 6, 6, 14] p3 F̂^A 0.36, p4 F̂^A 0.50; planted approvals a run 33, audited 33, confirmed 14
- seed 35: 1.00 → 1.00 → 1.00 → 2.00 → 4.00 [0, 4, 2, 4, 11] p3 F̂^A 0.50, p4 F̂^A 0.45; planted approvals a run 31, audited 29, confirmed 14
- seed 36: 1.00 → 1.00 → 1.00 → 2.00 → 4.00 [0, 3, 6, 7, 12] p3 F̂^A 0.44, p4 F̂^A 0.50; planted approvals a run 32, audited 31, confirmed 14
- seed 37: 1.00 → 1.00 → 1.00 → 2.00 → 4.00 [0, 3, 6, 6, 11] p3 F̂^A 0.53, p4 F̂^A 0.55; planted approvals a run 34, audited 34, confirmed 15
- seed 38: 1.00 → 1.00 → 1.00 → 2.00 → 2.00 → 4.00 [0, 3, 5, 3, 8, 10] p3 F̂^A 0.64, p5 F̂^A 0.39; planted approvals a run 41, audited 40, confirmed 16
- seed 39: 1.00 → 1.00 → 1.00 → 2.00 → 4.00 [1, 0, 6, 5, 13] p3 F̂^A 0.33, p4 F̂^A 0.54; planted approvals a run 32, audited 31, confirmed 13
- seed 40: 1.00 → 1.00 → 1.00 → 2.00 → 4.00 [0, 4, 5, 5, 14] p3 F̂^A 0.50, p4 F̂^A 0.71; planted approvals a run 37, audited 36, confirmed 17

## greedy (20 seeds)

| period | m^A before → after | seeds stepping (↑ / ↓) | π^A after | planted approvals posted | base (members' audits of real approvals) | adj at a member's audit seat | confirmed | pool carried | F̂^A read (n) |
|---|---|---|---|---|---|---|---|---|---|
| p0 (t 0–194) | 1.00 → 1.00 | 0 / 0 of 20 | 0.020 | 0.2 | 37 | 0.2 | 0.1 | 0.1 / 0.2 | — (0) |
| p1 (t 194–388) | 1.00 → 1.00 | 0 / 0 of 20 | 0.020 | 2.5 | 125 | 2.4 | 1.4 | 1.4 / 2.6 | — (0) |
| p2 (t 388–577) | 1.00 → 1.15 | 3 / 0 of 20 | 0.023 | 4.8 | 243 | 4.7 | 2.4 | 3.0 / 5.7 | 0.47 (3) |
| p3 (t 577–767) | 1.15 → 2.10 | 16 / 0 of 20 | 0.042 | 6.5 | 274 | 6.5 | 3.6 | 0.4 / 1.5 | 0.59 (16) |
| p4 (t 767–961) | 2.10 → 3.74 | 15 / 1 of 20 | 0.075 | 12.8 | 295 | 12.7 | 4.5 | 0.3 / 1.1 | 0.37 (17) |
| p5 (t 569–659) | 1.00 → 1.27 | 1 / 0 of 2 | 0.025 | 4.5 | 236 | 5.0 | 2.0 | 1.0 / 3.0 | 0.15 (1) |
| p6 (t 659–765) | 1.54 → 1.54 | 0 / 0 of 1 | 0.031 | 7.0 | 206 | 6.0 | 2.0 | 2.0 / 6.0 | — (0) |
| p7 (t 765–879) | 1.54 → 2.37 | 1 / 0 of 1 | 0.047 | 7.0 | 228 | 7.0 | 0.0 | 0.0 / 0.0 | 0.15 (1) |
| p8 partial (t 961–1000) | 3.81 (no close) | — | 0.076 | 8.1 | 116 | 7.8 | 2.1 | 0.4 / 1.0 | — |

m^A at the run's end: mean 3.81, min 1.00, max 8.00; seeds whose m^A left 1 within the run: 19 of 20 (first at period p2–p5, median p3); adjudications a closed period, mean over the seeds and periods 5.3 against the ten a step needs; readings taken a run 1.9 of 8 closes.

Every seed's path (m^A after each close; the adjudications at a member's audit seat by period in brackets; F̂^A where read):

- seed 21: 1.00 → 1.00 → 1.00 → 2.00 → 4.00 [0, 3, 5, 7, 13] p3 F̂^A 0.53, p4 F̂^A 0.46; planted approvals a run 35, audited 33, confirmed 18
- seed 22: 1.00 → 1.00 → 1.00 → 2.00 → 2.00 [0, 1, 5, 5, 7] p3 F̂^A 0.73; planted approvals a run 25, audited 25, confirmed 12
- seed 23: 1.00 → 1.00 → 1.00 → 1.00 → 2.00 [1, 1, 3, 4, 6] p4 F̂^A 0.47; planted approvals a run 18, audited 17, confirmed 7
- seed 24: 1.00 → 1.00 → 1.00 → 2.00 → 1.80 [0, 3, 5, 7, 14] p3 F̂^A 0.47, p4 F̂^A 0.07; planted approvals a run 33, audited 32, confirmed 9
- seed 25: 1.00 → 1.00 → 1.00 → 1.00 → 2.00 [0, 1, 3, 2, 5] p4 F̂^A 0.73; planted approvals a run 15, audited 14, confirmed 8
- seed 26: 1.00 → 1.00 → 1.00 → 2.00 → 4.00 [0, 2, 6, 6, 14] p3 F̂^A 0.57, p4 F̂^A 0.43; planted approvals a run 37, audited 35, confirmed 17
- seed 27: 1.00 → 1.00 → 1.00 → 2.00 → 2.00 [0, 4, 4, 4, 7] p3 F̂^A 0.75; planted approvals a run 27, audited 26, confirmed 17
- seed 28: 1.00 → 1.00 → 1.00 → 2.00 → 3.08 [0, 0, 5, 5, 13] p3 F̂^A 0.60, p4 F̂^A 0.15; planted approvals a run 28, audited 26, confirmed 8
- seed 29: 1.00 → 1.00 → 1.00 → 2.00 → 4.00 [0, 3, 6, 6, 13] p3 F̂^A 0.73, p4 F̂^A 0.54; planted approvals a run 34, audited 33, confirmed 19
- seed 30: 1.00 → 1.00 → 1.00 → 2.00 → 4.00 [0, 2, 4, 6, 13] p3 F̂^A 0.33, p4 F̂^A 0.46; planted approvals a run 34, audited 33, confirmed 11
- seed 31: 1.00 → 1.00 → 1.00 → 2.00 → 4.00 [1, 4, 4, 7, 12] p3 F̂^A 0.56, p4 F̂^A 0.50; planted approvals a run 41, audited 41, confirmed 15
- seed 32: 1.00 → 1.00 → 2.00 → 4.00 → 8.00 [0, 5, 6, 14, 25] p2 F̂^A 0.45, p3 F̂^A 0.79, p4 F̂^A 0.44; planted approvals a run 64, audited 61, confirmed 34
- seed 33: 1.00 → 1.00 → 1.00 → 2.00 → 4.00 [2, 2, 3, 6, 14] p3 F̂^A 0.46, p4 F̂^A 0.36; planted approvals a run 34, audited 33, confirmed 11
- seed 34: 1.00 → 1.00 → 1.00 → 2.00 → 4.00 [0, 2, 6, 6, 12] p3 F̂^A 0.71, p4 F̂^A 0.25; planted approvals a run 34, audited 33, confirmed 13
- seed 35: 1.00 → 1.00 → 1.00 → 2.00 → 4.00 [0, 2, 4, 5, 11] p3 F̂^A 0.82, p4 F̂^A 0.45; planted approvals a run 41, audited 40, confirmed 16
- seed 36: 1.00 → 1.00 → 1.00 → 2.00 → 4.00 [0, 2, 6, 7, 13] p3 F̂^A 0.33, p4 F̂^A 0.31; planted approvals a run 34, audited 33, confirmed 9
- seed 37: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.54 → 1.54 → 2.37 [0, 1, 3, 2, 3, 4, 6, 7] p5 F̂^A 0.15, p7 F̂^A 0.15; planted approvals a run 36, audited 36, confirmed 7
- seed 38: 1.00 → 1.00 → 2.00 → 4.00 → 8.00 [0, 4, 6, 13, 26] p2 F̂^A 0.30, p3 F̂^A 0.69, p4 F̂^A 0.23; planted approvals a run 66, audited 64, confirmed 23
- seed 39: 1.00 → 1.00 → 2.00 → 4.00 → 8.00 [1, 4, 7, 13, 27] p2 F̂^A 0.67, p3 F̂^A 0.38, p4 F̂^A 0.30; planted approvals a run 62, audited 61, confirmed 23
- seed 40: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 1, 3, 5, 5, 6] p4 F̂^A 0.07; planted approvals a run 23, audited 23, confirmed 3

## hand (20 seeds)

| period | m^A before → after | seeds stepping (↑ / ↓) | π^A after | planted approvals posted | base (members' audits of real approvals) | adj at a member's audit seat | confirmed | pool carried | F̂^A read (n) |
|---|---|---|---|---|---|---|---|---|---|
| p0 (t 0–200) | 1.00 → 1.00 | 0 / 0 of 20 | 0.020 | 0.2 | 33 | 0.1 | 0.0 | 0.0 / 0.1 | — (0) |
| p1 (t 200–329) | 1.00 → 1.00 | 0 / 0 of 20 | 0.020 | 1.1 | 53 | 1.1 | 0.0 | 0.0 / 1.2 | — (0) |
| p2 (t 329–398) | 1.00 → 1.00 | 0 / 0 of 20 | 0.020 | 1.2 | 57 | 0.9 | 0.1 | 0.1 / 2.1 | — (0) |
| p3 (t 398–470) | 1.00 → 1.00 | 0 / 0 of 20 | 0.020 | 1.6 | 84 | 1.6 | 0.1 | 0.1 / 3.8 | — (0) |
| p4 (t 470–532) | 1.00 → 1.00 | 0 / 0 of 20 | 0.020 | 1.9 | 98 | 2.0 | 0.0 | 0.1 / 5.8 | — (0) |
| p5 (t 532–587) | 1.00 → 1.00 | 0 / 0 of 20 | 0.020 | 2.2 | 113 | 2.4 | 0.2 | 0.2 / 5.5 | 0.04 (5) |
| p6 (t 587–654) | 1.00 → 1.05 | 1 / 0 of 20 | 0.021 | 2.5 | 118 | 2.1 | 0.0 | 0.1 / 3.1 | 0.03 (9) |
| p7 (t 654–729) | 1.05 → 1.05 | 0 / 0 of 20 | 0.021 | 2.6 | 128 | 2.8 | 0.2 | 0.1 / 2.5 | 0.04 (6) |
| p8 (t 729–815) | 1.05 → 1.04 | 0 / 1 of 20 | 0.021 | 3.0 | 142 | 3.1 | 0.2 | 0.3 / 5.0 | 0.09 (1) |
| p9 (t 815–905) | 1.04 → 1.09 | 1 / 0 of 20 | 0.022 | 3.2 | 154 | 3.2 | 0.1 | 0.1 / 4.5 | 0.07 (7) |
| p10 (t 871–972) | 1.10 → 1.15 | 1 / 1 of 18 | 0.023 | 3.7 | 169 | 3.6 | 0.2 | 0.1 / 2.4 | 0.03 (10) |
| p11 (t 900–997) | 1.16 → 1.16 | 0 / 0 of 10 | 0.023 | 4.0 | 167 | 4.0 | 0.0 | 0.1 / 4.6 | — (0) |
| p12 partial (t 905–1000) | 1.13 (no close) | — | 0.023 | 1.7 | 78 | 1.8 | 0.2 | 0.1 / 4.5 | — |

m^A at the run's end: mean 1.13, min 1.00, max 2.00; seeds whose m^A left 1 within the run: 3 of 20 (first at period p6–p10, median p9); adjudications a closed period, mean over the seeds and periods 2.2 against the ten a step needs; readings taken a run 1.9 of 12 closes.

Every seed's path (m^A after each close; the adjudications at a member's audit seat by period in brackets; F̂^A where read):

- seed 21: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 2, 1, 3, 2, 3, 3, 3] p7 F̂^A 0.00; planted approvals a run 21, audited 20, confirmed 0
- seed 22: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 1, 2, 2, 3, 2, 3, 3, 4, 4] p6 F̂^A 0.00, p9 F̂^A 0.10; planted approvals a run 25, audited 24, confirmed 1
- seed 23: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 2.00 → 2.00 [0, 0, 1, 2, 2, 2, 2, 3, 3, 3, 4, 7] p7 F̂^A 0.08, p10 F̂^A 0.20; planted approvals a run 30, audited 29, confirmed 3
- seed 24: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 1, 1, 2, 2, 2, 3, 3, 3, 3] p7 F̂^A 0.09; planted approvals a run 23, audited 23, confirmed 2
- seed 25: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 0, 1, 2, 3, 3, 3, 3, 4, 4] p7 F̂^A 0.08, p10 F̂^A 0.00; planted approvals a run 23, audited 23, confirmed 1
- seed 26: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4] p6 F̂^A 0.10, p10 F̂^A 0.00; planted approvals a run 25, audited 25, confirmed 1
- seed 27: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 3, 2, 2, 2, 2, 3, 2, 3, 4] p5 F̂^A 0.00, p9 F̂^A 0.08; planted approvals a run 26, audited 26, confirmed 1
- seed 28: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 2.00 → 2.00 → 1.82 → 1.82 → 1.64 → 1.64 [0, 2, 1, 1, 2, 2, 2, 5, 6, 5, 5, 5] p6 F̂^A 0.20, p8 F̂^A 0.09, p10 F̂^A 0.00; planted approvals a run 40, audited 40, confirmed 3
- seed 29: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [1, 2, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4] p5 F̂^A 0.10, p9 F̂^A 0.00; planted approvals a run 28, audited 28, confirmed 1
- seed 30: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 1, 1, 1, 3, 2, 2, 2, 3, 2, 3, 3] p6 F̂^A 0.00, p10 F̂^A 0.00; planted approvals a run 26, audited 26, confirmed 0
- seed 31: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 1, 1, 1, 2, 2, 3, 2, 3, 3, 2, 3] p6 F̂^A 0.00, p10 F̂^A 0.10; planted approvals a run 25, audited 25, confirmed 1
- seed 32: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 1, 1, 2, 2, 2, 2, 3, 2, 3, 3, 3] p6 F̂^A 0.00, p10 F̂^A 0.00; planted approvals a run 26, audited 26, confirmed 0
- seed 33: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 2, 1, 2, 3, 2, 3, 4, 4, 3] p6 F̂^A 0.00, p9 F̂^A 0.00; planted approvals a run 25, audited 24, confirmed 0
- seed 34: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 2.00 → 2.00 [1, 1, 0, 2, 2, 3, 2, 3, 4, 3, 8] p6 F̂^A 0.00, p9 F̂^A 0.20; planted approvals a run 33, audited 32, confirmed 4
- seed 35: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 2, 2, 2, 2, 3, 2, 2, 2, 3, 2, 3] p5 F̂^A 0.00, p10 F̂^A 0.00; planted approvals a run 27, audited 27, confirmed 0
- seed 36: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4] p5 F̂^A 0.00, p9 F̂^A 0.00; planted approvals a run 28, audited 28, confirmed 1
- seed 37: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 1, 0, 2, 2, 2, 2, 2, 3, 3, 4] p7 F̂^A 0.00, p10 F̂^A 0.00; planted approvals a run 22, audited 22, confirmed 0
- seed 38: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [1, 2, 0, 2, 2, 3, 2, 3, 3, 3, 4] p5 F̂^A 0.10, p9 F̂^A 0.09; planted approvals a run 28, audited 27, confirmed 2
- seed 39: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 2, 0, 2, 2, 2, 2, 3, 2, 3, 3, 4] p6 F̂^A 0.00, p10 F̂^A 0.00; planted approvals a run 27, audited 27, confirmed 0
- seed 40: 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 → 1.00 [0, 0, 1, 1, 2, 2, 2, 2, 3, 3, 3] p7 F̂^A 0.00; planted approvals a run 22, audited 22, confirmed 1


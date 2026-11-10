# The per-seat dial's path by period — `run42-quick` (the economy reviewer's question after §88; `dial_path.py`)

Cell: `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule`; seeds 21-23; 1000 ticks (a period 200 ticks: five closed periods and nothing closes the sixth). A run's dial starts at the floor (m^A 1, π^A = π^A_0 0.02 at genesis) and nothing carries between runs. m^A steps at a period's close on a reading of at least ten pooled adjudications of planted approvals at a member's audit seat (Appendix V, `seat_dial_min_adj` 10): `adj` is the period's own count, `pool` what the pool carries forward after the close (confirmed / adjudicated), `F̂^A` the reading where one was taken (mean over the seeds that read one; the count of seeds reading). The planted approvals posted in the period are at π^A per real approval audited by a member in the period (`base`); the partial sixth period's counts are shown for the record.

## direct (3 seeds)

| period | m^A before → after | seeds stepping (↑ / ↓) | π^A after | planted approvals posted | base (members' audits of real approvals) | adj at a member's audit seat | confirmed | pool carried | F̂^A read (n) |
|---|---|---|---|---|---|---|---|---|---|
| p0 (t 0–184) | 1.00 → 1.00 | 0 / 0 of 3 | 0.020 | 0.3 | 48 | 0.3 | 0.0 | 0.0 / 0.3 | — (0) |
| p1 (t 184–384) | 1.00 → 1.00 | 0 / 0 of 3 | 0.020 | 2.3 | 111 | 2.3 | 1.0 | 1.0 / 2.7 | — (0) |
| p2 (t 384–557) | 1.00 → 1.33 | 1 / 0 of 3 | 0.027 | 4.7 | 245 | 4.7 | 3.0 | 3.0 / 4.0 | 0.30 (1) |
| p3 (t 557–750) | 1.33 → 2.67 | 3 / 0 of 3 | 0.053 | 8.7 | 320 | 8.7 | 4.3 | 0.0 / 0.0 | 0.59 (3) |
| p4 (t 750–937) | 2.67 → 5.33 | 3 / 0 of 3 | 0.107 | 15.0 | 286 | 14.7 | 6.7 | 0.0 / 0.0 | 0.46 (3) |
| p5 partial (t 937–1000) | 5.33 (no close) | — | 0.107 | 12.7 | 107 | 12.7 | 3.3 | 0.0 / 0.0 | — |

m^A at the run's end: mean 5.33, min 4.00, max 8.00; seeds whose m^A left 1 within the run: 3 of 3 (first at period p2–p3, median p3); adjudications a closed period, mean over the seeds and periods 6.1 against the ten a step needs; readings taken a run 2.3 of 5 closes.

Every seed's path (m^A after each close; the adjudications at a member's audit seat by period in brackets; F̂^A where read):

- seed 21: 1.00 → 1.00 → 1.00 → 2.00 → 4.00 [0, 1, 5, 6, 11] p3 F̂^A 0.50, p4 F̂^A 0.45; planted approvals a run 32, audited 32, confirmed 13
- seed 22: 1.00 → 1.00 → 2.00 → 4.00 → 8.00 [1, 4, 5, 14, 20] p2 F̂^A 0.30, p3 F̂^A 0.43, p4 F̂^A 0.45; planted approvals a run 70, audited 69, confirmed 24
- seed 23: 1.00 → 1.00 → 1.00 → 2.00 → 4.00 [0, 2, 4, 6, 13] p3 F̂^A 0.83, p4 F̂^A 0.46; planted approvals a run 29, audited 28, confirmed 17


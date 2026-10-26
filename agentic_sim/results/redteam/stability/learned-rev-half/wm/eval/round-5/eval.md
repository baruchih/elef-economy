# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop half --learner-role reviewer --learner-exit rule`, seeds 21-40, hide ``, model `results/redteam/stability/learned-rev-half/wm/models/wm-online-5.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the plant-blind seats — a revised submission or a panel, where no plant is received — are read apart: their share of the review decisions and the stamp rate on them.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | blind-seat share | blind-seat stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 16097.1 ± 608.0 | -3115.3 ± 756.4 | 2144.6 | 0.732 | 0.268 | 0.000 | 0.079 | 0.103 | 0.295 | 0.676 | 23.80 | 40.55 | 0.15 |
| careful | 19212.4 ± 633.3 | nan ± nan | 2593.3 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.296 | 0.000 | 9.00 | 0.00 | 0.45 |
| stamper | 3621.3 ± 110.9 | -15591.1 ± 617.6 | 501.6 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.024 | 1.000 | 14.40 | 87.05 | 1.00 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 0.774 | 0.834 | 0.730 (259) | 0.436 (2850) | 0.272 (9227) | 0.313 (10481) | 0.214 (20074) | 19.900 | 138.100 | 2.791 | 2.038 |
| careful | — | 0.736 | 0.000 (1566) | 0.000 (12785) | 0.000 (8783) | 0.000 (6467) | 0.000 (22266) | 13.150 | 212.850 | 2.209 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (10033) | 34.050 | 96.800 | 4.040 | 2.557 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| greedy | 20.300 | 0.000 | 0.000 | 0.000 | 0.000 | 0.150 | 0.000 |
| careful | 20.300 | 0.000 | 0.000 | 0.000 | 0.000 | 0.450 | 0.000 |
| stamper | 20.450 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 9.250 / 20.300 | 23.800 ± 2.164 | +14.800 ± 2.057 | 61.450 | +23.450 ± 2.498 | 7.350 | 0.073 | 16.500 | +7.000 ± 0.788 | 1679.750 | 0.044 | +0.001 ± 0.002 | 15768.279 ± 473.581 | -1611.349 ± 667.582 | 16097.1 ± 608.0 | -3115.3 ± 756.4 | 32.220 | -2.035 ± 0.439 | 21.355 ± 0.560 | +1.545 ± 0.919 | 19.913 | 0.004 | 2467.950 | 19.800 | 20.800 | +0.650 ± 0.393 | 60.355 | 161.700 |
| careful | 12.350 / 20.300 | 9.000 ± 0.923 | — | 38.000 | — | 7.450 | 0.059 | 9.500 | — | 1592.550 | 0.043 | — | 17379.628 ± 720.044 | — | 19212.4 ± 633.3 | — | 34.255 | — | 19.810 ± 0.824 | — | 18.941 | 0.001 | 2571.000 | 19.750 | 20.150 | — | 284.377 | 181.750 |
| stamper | 0.000 / 20.450 | 14.400 ± 1.075 | +5.400 ± 1.519 | 91.450 | +53.450 ± 2.722 | 4.700 | 0.047 | 32.250 | +22.750 ± 1.066 | 1512.550 | 0.091 | +0.048 ± 0.002 | 3317.654 ± 132.825 | -14061.974 ± 706.689 | 3621.3 ± 110.9 | -15591.1 ± 617.6 | 27.661 | -6.594 ± 0.404 | 29.316 ± 0.219 | +9.506 ± 0.753 | 24.428 | 0.237 | 1618.450 | 20.000 | 28.500 | +8.350 ± 0.477 | 96.601 | 140.500 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **greedy**: p0 0.875/0.125/0.000 (298); p1 0.484/0.516/0.000 (204); p2 0.678/0.322/0.000 (118); p3 0.799/0.201/0.000 (136); p4 0.755/0.245/0.000 (145); p5 0.747/0.253/0.000 (136); p6 0.733/0.267/0.000 (159); p7 0.748/0.252/0.000 (142); p8 0.742/0.258/0.000 (173); p9 0.713/0.287/0.000 (158); p10 0.727/0.273/0.000 (161); p11 0.737/0.263/0.000 (144); p12 0.698/0.302/0.000 (119); p13 0.768/0.232/0.000 (49); p14 0.541/0.459/0.000 (2)
- **careful**: p0 1.000/0.000/0.000 (302); p1 1.000/0.000/0.000 (248); p2 1.000/0.000/0.000 (198); p3 1.000/0.000/0.000 (190); p4 1.000/0.000/0.000 (230); p5 1.000/0.000/0.000 (205); p6 1.000/0.000/0.000 (243); p7 1.000/0.000/0.000 (236); p8 1.000/0.000/0.000 (221); p9 1.000/0.000/0.000 (187); p10 1.000/0.000/0.000 (154); p11 1.000/0.000/0.000 (116); p12 1.000/0.000/0.000 (54); p13 1.000/0.000/0.000 (11); p14 1.000/0.000/0.000 (0)
- **stamper**: p0 0.000/1.000/0.000 (296); p1 0.000/1.000/0.000 (131); p2 0.000/1.000/0.000 (56); p3 0.000/1.000/0.000 (18); p4 0.000/1.000/0.000 (1); p5 0.000/1.000/0.000 (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 2465.1 / 654.0 | 0.66 / 0.29 | -0.37 ± 0.07 | 1.00 / 1.08 | +0.08 ± 0.00 | 0.13 / 0.18 | +0.05 ± 0.01 | 0.347 / 0.377 | +0.030 ± 0.008 | 0.003 / 0.139 | 0.053 / 0.036 | -0.017 ± 0.004 | 2.40 / 1.67 | -0.72 ± 0.13 |
| careful | 2565.7 / 545.0 | 0.34 / 0.11 | -0.22 ± 0.03 | 1.00 / 1.10 | +0.10 ± 0.00 | 0.13 / 0.15 | +0.02 ± 0.00 | 0.216 / 0.202 | -0.014 ± 0.006 | 0.001 / 0.046 | 0.046 / 0.040 | -0.006 ± 0.003 | 1.81 / 1.43 | -0.38 ± 0.11 |
| stamper | 2087.3 / 532.0 | 2.27 / 0.92 | -1.35 ± 0.03 | 1.00 / 1.09 | +0.09 ± 0.00 | 0.11 / 0.20 | +0.09 ± 0.01 | 0.526 / 0.591 | +0.065 ± 0.006 | 0.233 / 0.618 | 0.022 / 0.013 | -0.009 ± 0.001 | 3.17 / 1.87 | -1.30 ± 0.21 |

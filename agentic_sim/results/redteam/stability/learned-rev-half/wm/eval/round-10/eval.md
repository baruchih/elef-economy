# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop half --learner-role reviewer --learner-exit rule`, seeds 21-40, hide ``, model `results/redteam/stability/learned-rev-half/wm/models/wm-online-10.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the plant-blind seats — a revised submission or a panel, where no plant is received — are read apart: their share of the review decisions and the stamp rate on them.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | blind-seat share | blind-seat stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 16510.0 ± 622.5 | -2702.4 ± 672.2 | 2149.9 | 0.698 | 0.302 | 0.000 | 0.087 | 0.100 | 0.279 | 0.831 | 25.15 | 44.35 | 0.10 |
| careful | 19212.4 ± 633.3 | nan ± nan | 2593.3 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.296 | 0.000 | 9.00 | 0.00 | 0.45 |
| stamper | 3621.3 ± 110.9 | -15591.1 ± 617.6 | 501.6 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.024 | 1.000 | 14.40 | 87.05 | 1.00 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 0.772 | 0.860 | 0.728 (235) | 0.583 (1879) | 0.373 (8390) | 0.366 (11856) | 0.206 (20638) | 20.000 | 148.550 | 2.697 | 2.217 |
| careful | — | 0.736 | 0.000 (1566) | 0.000 (12785) | 0.000 (8783) | 0.000 (6467) | 0.000 (22266) | 13.150 | 212.850 | 2.209 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (10033) | 34.050 | 96.800 | 4.040 | 2.557 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| greedy | 20.350 | 0.000 | 0.000 | 0.000 | 0.000 | 0.100 | 0.000 |
| careful | 20.300 | 0.000 | 0.000 | 0.000 | 0.000 | 0.450 | 0.000 |
| stamper | 20.450 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 9.150 / 20.350 | 25.150 ± 1.736 | +16.150 ± 2.238 | 64.400 | +26.400 ± 2.359 | 8.650 | 0.095 | 17.350 | +7.850 ± 0.723 | 1679.550 | 0.040 | -0.003 ± 0.001 | 16217.070 ± 663.207 | -1162.558 ± 762.193 | 16510.0 ± 622.5 | -2702.4 ± 672.2 | 32.090 | -2.165 ± 0.438 | 21.127 ± 0.634 | +1.316 ± 1.064 | 20.067 | 0.011 | 2435.500 | 19.800 | 20.950 | +0.800 ± 0.560 | 96.686 | 192.850 |
| careful | 12.350 / 20.300 | 9.000 ± 0.923 | — | 38.000 | — | 7.450 | 0.059 | 9.500 | — | 1592.550 | 0.043 | — | 17379.628 ± 720.044 | — | 19212.4 ± 633.3 | — | 34.255 | — | 19.810 ± 0.824 | — | 18.941 | 0.001 | 2571.000 | 19.750 | 20.150 | — | 284.377 | 181.750 |
| stamper | 0.000 / 20.450 | 14.400 ± 1.075 | +5.400 ± 1.519 | 91.450 | +53.450 ± 2.722 | 4.700 | 0.047 | 32.250 | +22.750 ± 1.066 | 1512.550 | 0.091 | +0.048 ± 0.002 | 3317.654 ± 132.825 | -14061.974 ± 706.689 | 3621.3 ± 110.9 | -15591.1 ± 617.6 | 27.661 | -6.594 ± 0.404 | 29.316 ± 0.219 | +9.506 ± 0.753 | 24.428 | 0.237 | 1618.450 | 20.000 | 28.500 | +8.350 ± 0.477 | 96.601 | 140.500 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **greedy**: p0 0.921/0.079/0.000 (300); p1 0.539/0.461/0.000 (209); p2 0.666/0.334/0.000 (119); p3 0.694/0.306/0.000 (141); p4 0.666/0.334/0.000 (147); p5 0.710/0.290/0.000 (131); p6 0.705/0.295/0.000 (155); p7 0.692/0.308/0.000 (149); p8 0.671/0.329/0.000 (153); p9 0.684/0.316/0.000 (159); p10 0.659/0.341/0.000 (162); p11 0.668/0.332/0.000 (133); p12 0.645/0.355/0.000 (118); p13 0.631/0.369/0.000 (66); p14 0.724/0.276/0.000 (8)
- **careful**: p0 1.000/0.000/0.000 (302); p1 1.000/0.000/0.000 (248); p2 1.000/0.000/0.000 (198); p3 1.000/0.000/0.000 (190); p4 1.000/0.000/0.000 (230); p5 1.000/0.000/0.000 (205); p6 1.000/0.000/0.000 (243); p7 1.000/0.000/0.000 (236); p8 1.000/0.000/0.000 (221); p9 1.000/0.000/0.000 (187); p10 1.000/0.000/0.000 (154); p11 1.000/0.000/0.000 (116); p12 1.000/0.000/0.000 (54); p13 1.000/0.000/0.000 (11); p14 1.000/0.000/0.000 (0)
- **stamper**: p0 0.000/1.000/0.000 (296); p1 0.000/1.000/0.000 (131); p2 0.000/1.000/0.000 (56); p3 0.000/1.000/0.000 (18); p4 0.000/1.000/0.000 (1); p5 0.000/1.000/0.000 (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 2449.0 / 660.5 | 0.78 / 0.33 | -0.45 ± 0.10 | 1.00 / 1.08 | +0.08 ± 0.00 | 0.13 / 0.18 | +0.05 ± 0.01 | 0.345 / 0.381 | +0.036 ± 0.010 | 0.011 / 0.171 | 0.062 / 0.039 | -0.023 ± 0.005 | 2.50 / 1.78 | -0.72 ± 0.18 |
| careful | 2565.7 / 545.0 | 0.34 / 0.11 | -0.22 ± 0.03 | 1.00 / 1.10 | +0.10 ± 0.00 | 0.13 / 0.15 | +0.02 ± 0.00 | 0.216 / 0.202 | -0.014 ± 0.006 | 0.001 / 0.046 | 0.046 / 0.040 | -0.006 ± 0.003 | 1.81 / 1.43 | -0.38 ± 0.11 |
| stamper | 2087.3 / 532.0 | 2.27 / 0.92 | -1.35 ± 0.03 | 1.00 / 1.09 | +0.09 ± 0.00 | 0.11 / 0.20 | +0.09 ± 0.01 | 0.526 / 0.591 | +0.065 ± 0.006 | 0.233 / 0.618 | 0.022 / 0.013 | -0.009 ± 0.001 | 3.17 / 1.87 | -1.30 ± 0.21 |

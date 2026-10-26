# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule`, seeds 21-40, hide ``, model `results/redteam/stability/learned-rev-stamper-2/wm/models/wm-online-10.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the plant-blind seats — a revised submission or a panel, where no plant is received — are read apart: their share of the review decisions and the stamp rate on them.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | blind-seat share | blind-seat stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 29950.4 ± 361.2 | -5400.3 ± 814.4 | 3680.4 | 0.553 | 0.447 | 0.000 | 0.266 | 0.306 | 0.227 | 0.957 | 86.10 | 222.85 | 0.20 |
| careful | 35350.7 ± 821.3 | nan ± nan | 4122.6 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.292 | 0.000 | 6.30 | 0.00 | 0.45 |
| stamper | 6937.1 ± 162.8 | -28413.6 ± 834.0 | 1041.8 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.021 | 1.000 | 13.75 | 179.65 | 1.00 |
| hand | 32145.9 ± 593.0 | -3204.8 ± 834.8 | 4447.5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.295 | 0.000 | 11.60 | 0.00 | 0.60 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 0.864 | 0.955 | 0.872 (655) | 0.960 (872) | 0.835 (474) | 0.661 (25090) | 0.311 (46518) | 45.450 | 240.100 | 1.585 | 4.903 |
| careful | — | 0.668 | 0.000 (27448) | 0.000 (5667) | 0.000 (4419) | 0.000 (1173) | 0.000 (43745) | 23.750 | 700.250 | 1.094 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (20836) | 71.000 | 192.700 | 1.923 | 2.530 |
| hand | — | 0.803 | 0.000 (113) | 0.000 (11603) | 0.000 (18496) | 0.000 (15352) | 0.000 (43386) | 33.850 | 344.800 | 1.254 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| greedy | 39.700 | 0.000 | 0.000 | 0.000 | 0.000 | 0.200 | 0.000 |
| careful | 39.600 | 0.000 | 0.000 | 0.000 | 0.000 | 0.450 | 0.000 |
| stamper | 39.900 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| hand | 39.850 | 0.000 | 0.000 | 0.000 | 0.000 | 0.600 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 16.250 / 39.700 | 86.100 ± 3.611 | +79.800 ± 3.629 | 144.900 | +135.900 ± 2.816 | 6.050 | 0.279 | 25.750 | +21.600 ± 1.208 | 1743.450 | 0.045 | +0.021 ± 0.003 | 0.000 / 0.000 (0.000 / 0.000) | 32930.979 ± 384.574 | +10319.141 ± 485.122 | 29950.4 ± 361.2 | -5400.3 ± 814.4 | 28.793 | -9.774 ± 0.323 | 23.506 ± 0.355 | +9.807 ± 0.518 | 21.704 | 0.045 | 2121.300 | 19.700 | 23.450 | +6.000 ± 0.543 | 70.156 | 135.800 |
| careful | 22.150 / 39.600 | 6.300 ± 0.649 | — | 9.000 | — | 2.600 | 0.044 | 4.150 | — | 1595.100 | 0.024 | — | 0.000 / 0.000 (0.000 / 0.000) | 22611.837 ± 296.550 | — | 35350.7 ± 821.3 | — | 38.567 | — | 13.699 ± 0.397 | — | 16.874 | 0.000 | 2654.200 | 19.600 | 17.450 | — | 1103.486 | 220.800 |
| stamper | 4.850 / 39.900 | 13.750 ± 0.903 | +7.450 ± 0.860 | 109.400 | +100.400 ± 2.226 | 0.000 | 1.000 | 51.100 | +46.950 ± 1.974 | 871.800 | 0.194 | +0.170 ± 0.003 | 0.000 / 0.000 (0.000 / 0.000) | 8716.679 ± 214.897 | -13895.158 ± 410.681 | 6937.1 ± 162.8 | -28413.6 ± 834.0 | 27.527 | -11.040 ± 0.305 | 32.286 ± 0.656 | +18.587 ± 0.746 | 22.196 | 0.174 | 752.000 | 19.900 | 35.050 | +17.600 ± 0.828 | 5935.040 | 135.200 |
| hand | 19.500 / 39.850 | 11.600 ± 0.666 | +5.300 ± 0.941 | 62.250 | +53.250 ± 2.040 | 6.900 | 0.047 | 14.000 | +9.850 ± 0.933 | 1678.600 | 0.060 | +0.036 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 29714.546 ± 438.122 | +7102.709 ± 376.361 | 32145.9 ± 593.0 | -3204.8 ± 834.8 | 32.740 | -5.828 ± 0.318 | 20.386 ± 0.371 | +6.687 ± 0.456 | 19.478 | 0.010 | 2486.700 | 19.850 | 20.350 | +2.900 ± 0.369 | 86.726 | 150.900 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **greedy**: p0 0.765/0.235/0.000 (593); p1 0.298/0.701/0.001 (456); p2 0.569/0.431/0.000 (272); p3 0.561/0.439/0.000 (259); p4 0.497/0.502/0.001 (262); p5 0.500/0.500/0.000 (254); p6 0.533/0.466/0.001 (242); p7 0.547/0.453/0.000 (245); p8 0.570/0.430/0.000 (235); p9 0.613/0.387/0.000 (231); p10 0.534/0.466/0.000 (222); p11 0.573/0.427/0.000 (200); p12 0.549/0.451/0.000 (158); p13 0.610/0.390/0.000 (47); p14 0.446/0.554/0.000 (4)
- **careful**: p0 1.000/0.000/0.000 (622); p1 1.000/0.000/0.000 (758); p2 1.000/0.000/0.000 (860); p3 1.000/0.000/0.000 (866); p4 1.000/0.000/0.000 (750); p5 1.000/0.000/0.000 (254); p6 1.000/0.000/0.000 (12)
- **stamper**: p0 0.000/1.000/0.000 (566); p1 0.000/1.000/0.000 (304); p2 0.000/1.000/0.000 (153); p3 0.000/1.000/0.000 (12); p4 0.000/1.000/0.000 (7); p5 0.000/1.000/0.000 (1)
- **hand**: p0 —/—/— (0); p1 —/—/— (0); p2 —/—/— (0); p3 —/—/— (0); p4 —/—/— (0); p5 —/—/— (0); p6 —/—/— (0); p7 —/—/— (0); p8 —/—/— (0); p9 —/—/— (0); p10 —/—/— (0); p11 —/—/— (0); p12 —/—/— (0); p13 —/—/— (0); p14 —/—/— (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling the requester's wallet refused to raise at least once (never a plant's: its raise is minted — §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 2209.4 / 636.4 | 1.63 / 2.00 | +0.37 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.08 / 0.08 | +0.00 ± 0.00 | 0.520 / 0.623 | +0.103 ± 0.007 | 0.310 / 0.000 | 0.044 / 0.079 | 0.195 / 0.226 | +0.031 ± 0.005 | 3.52 / 3.68 | +0.17 ± 0.06 |
| careful | 2649.1 / 267.9 | 0.14 / 0.07 | -0.07 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.07 / 0.07 | +0.00 ± 0.00 | 0.119 / 0.122 | +0.003 ± 0.003 | 0.038 / 0.000 | 0.000 / 0.000 | 0.060 / 0.059 | -0.001 ± 0.003 | 1.33 / 1.15 | -0.18 ± 0.05 |
| stamper | 871.8 / 148.0 | 0.84 / 0.44 | -0.40 ± 0.04 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.03 / 0.31 | +0.29 ± 0.06 | 0.173 / 0.156 | -0.016 ± 0.007 | 0.095 / 0.000 | 0.137 / 0.219 | 0.089 / 0.077 | -0.013 ± 0.006 | 2.97 / 1.47 | -1.50 ± 0.16 |
| hand | 2502.1 / 631.4 | 0.54 / 0.45 | -0.09 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.14 / 0.16 | +0.02 ± 0.00 | 0.310 / 0.325 | +0.015 ± 0.005 | 0.128 / 0.000 | 0.010 / 0.013 | 0.089 / 0.078 | -0.011 ± 0.003 | 2.22 / 2.11 | -0.11 ± 0.08 |

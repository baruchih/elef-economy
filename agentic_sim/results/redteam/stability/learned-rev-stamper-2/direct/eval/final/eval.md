# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule`, seeds 21-40, hide ``, model `None` (value off, horizon 8)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the plant-blind seats — a revised submission or a panel, where no plant is received — are read apart: their share of the review decisions and the stamp rate on them.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | blind-seat share | blind-seat stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 30076.5 ± 564.7 | -5274.1 ± 889.2 | 3831.4 | 0.503 | 0.472 | 0.025 | 0.316 | 0.378 | 0.243 | 0.918 | 94.30 | 251.10 | 0.30 |
| careful | 35350.7 ± 821.3 | nan ± nan | 4122.6 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.292 | 0.000 | 6.30 | 0.00 | 0.45 |
| stamper | 6937.1 ± 162.8 | -28413.6 ± 834.0 | 1041.8 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.021 | 1.000 | 13.75 | 179.65 | 1.00 |
| hand | 32145.9 ± 593.0 | -3204.8 ± 834.8 | 4447.5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.295 | 0.000 | 11.60 | 0.00 | 0.60 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 0.879 | 0.957 | 0.899 (563) | 0.905 (1155) | 0.833 (478) | 0.670 (23963) | 0.362 (50470) | 42.150 | 288.850 | 1.490 | 5.957 |
| careful | — | 0.668 | 0.000 (27448) | 0.000 (5667) | 0.000 (4419) | 0.000 (1173) | 0.000 (43745) | 23.750 | 700.250 | 1.094 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (20836) | 71.000 | 192.700 | 1.923 | 2.530 |
| hand | — | 0.803 | 0.000 (113) | 0.000 (11603) | 0.000 (18496) | 0.000 (15352) | 0.000 (43386) | 33.850 | 344.800 | 1.254 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| direct | 39.850 | 0.000 | 0.000 | 0.000 | 0.000 | 0.300 | 0.000 |
| careful | 39.600 | 0.000 | 0.000 | 0.000 | 0.000 | 0.450 | 0.000 |
| stamper | 39.900 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| hand | 39.850 | 0.000 | 0.000 | 0.000 | 0.000 | 0.600 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 16.600 / 39.850 | 94.300 ± 3.968 | +88.000 ± 3.882 | 149.950 | +140.950 ± 4.298 | 11.100 | 0.316 | 22.300 | +18.150 ± 0.856 | 1777.300 | 0.049 | +0.025 ± 0.003 | 0.000 / 0.000 (0.000 / 0.000) | 32479.037 ± 522.264 | +9867.200 ± 483.256 | 30076.5 ± 564.7 | -5274.1 ± 889.2 | 29.517 | -9.051 ± 0.392 | 23.290 ± 0.381 | +9.591 ± 0.440 | 21.417 | 0.038 | 2177.550 | 19.850 | 23.250 | +5.800 ± 0.468 | 79.977 | 80.800 |
| careful | 22.150 / 39.600 | 6.300 ± 0.649 | — | 9.000 | — | 2.600 | 0.044 | 4.150 | — | 1595.100 | 0.024 | — | 0.000 / 0.000 (0.000 / 0.000) | 22611.837 ± 296.550 | — | 35350.7 ± 821.3 | — | 38.567 | — | 13.699 ± 0.397 | — | 16.874 | 0.000 | 2654.200 | 19.600 | 17.450 | — | 1103.486 | 220.800 |
| stamper | 4.850 / 39.900 | 13.750 ± 0.903 | +7.450 ± 0.860 | 109.400 | +100.400 ± 2.226 | 0.000 | 1.000 | 51.100 | +46.950 ± 1.974 | 871.800 | 0.194 | +0.170 ± 0.003 | 0.000 / 0.000 (0.000 / 0.000) | 8716.679 ± 214.897 | -13895.158 ± 410.681 | 6937.1 ± 162.8 | -28413.6 ± 834.0 | 27.527 | -11.040 ± 0.305 | 32.286 ± 0.656 | +18.587 ± 0.746 | 22.196 | 0.174 | 752.000 | 19.900 | 35.050 | +17.600 ± 0.828 | 5935.040 | 135.200 |
| hand | 19.500 / 39.850 | 11.600 ± 0.666 | +5.300 ± 0.941 | 62.250 | +53.250 ± 2.040 | 6.900 | 0.047 | 14.000 | +9.850 ± 0.933 | 1678.600 | 0.060 | +0.036 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 29714.546 ± 438.122 | +7102.709 ± 376.361 | 32145.9 ± 593.0 | -3204.8 ± 834.8 | 32.740 | -5.828 ± 0.318 | 20.386 ± 0.371 | +6.687 ± 0.456 | 19.478 | 0.010 | 2486.700 | 19.850 | 20.350 | +2.900 ± 0.369 | 86.726 | 150.900 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **direct**: p0 0.733/0.266/0.001 (616); p1 0.372/0.609/0.019 (437); p2 0.476/0.495/0.029 (278); p3 0.520/0.450/0.031 (260); p4 0.433/0.528/0.039 (267); p5 0.448/0.517/0.034 (261); p6 0.434/0.529/0.037 (260); p7 0.463/0.507/0.030 (253); p8 0.496/0.481/0.023 (244); p9 0.473/0.504/0.023 (249); p10 0.503/0.470/0.027 (234); p11 0.457/0.518/0.025 (225); p12 0.463/0.485/0.052 (167); p13 0.507/0.457/0.036 (58); p14 0.477/0.443/0.080 (23)
- **careful**: p0 1.000/0.000/0.000 (622); p1 1.000/0.000/0.000 (758); p2 1.000/0.000/0.000 (860); p3 1.000/0.000/0.000 (866); p4 1.000/0.000/0.000 (750); p5 1.000/0.000/0.000 (254); p6 1.000/0.000/0.000 (12)
- **stamper**: p0 0.000/1.000/0.000 (566); p1 0.000/1.000/0.000 (304); p2 0.000/1.000/0.000 (153); p3 0.000/1.000/0.000 (12); p4 0.000/1.000/0.000 (7); p5 0.000/1.000/0.000 (1)
- **hand**: p0 —/—/— (0); p1 —/—/— (0); p2 —/—/— (0); p3 —/—/— (0); p4 —/—/— (0); p5 —/—/— (0); p6 —/—/— (0); p7 —/—/— (0); p8 —/—/— (0); p9 —/—/— (0); p10 —/—/— (0); p11 —/—/— (0); p12 —/—/— (0); p13 —/—/— (0); p14 —/—/— (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling the requester's wallet refused to raise at least once (never a plant's: its raise is minted — §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 2253.8 / 647.8 | 1.34 / 1.57 | +0.24 ± 0.05 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.08 / 0.09 | +0.01 ± 0.00 | 0.444 / 0.533 | +0.089 ± 0.012 | 0.260 / 0.000 | 0.038 / 0.064 | 0.165 / 0.190 | +0.025 ± 0.005 | 3.26 / 3.37 | +0.11 ± 0.06 |
| careful | 2649.1 / 267.9 | 0.14 / 0.07 | -0.07 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.07 / 0.07 | +0.00 ± 0.00 | 0.119 / 0.122 | +0.003 ± 0.003 | 0.038 / 0.000 | 0.000 / 0.000 | 0.060 / 0.059 | -0.001 ± 0.003 | 1.33 / 1.15 | -0.18 ± 0.05 |
| stamper | 871.8 / 148.0 | 0.84 / 0.44 | -0.40 ± 0.04 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.03 / 0.31 | +0.29 ± 0.06 | 0.173 / 0.156 | -0.016 ± 0.007 | 0.095 / 0.000 | 0.137 / 0.219 | 0.089 / 0.077 | -0.013 ± 0.006 | 2.97 / 1.47 | -1.50 ± 0.16 |
| hand | 2502.1 / 631.4 | 0.54 / 0.45 | -0.09 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.14 / 0.16 | +0.02 ± 0.00 | 0.310 / 0.325 | +0.015 ± 0.005 | 0.128 / 0.000 | 0.010 / 0.013 | 0.089 / 0.078 | -0.011 ± 0.003 | 2.22 / 2.11 | -0.11 ± 0.08 |

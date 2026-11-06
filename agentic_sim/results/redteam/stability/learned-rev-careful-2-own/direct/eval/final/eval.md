# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule`, seeds 21-40, hide ``, model `None` (value off, horizon 8)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the plant-blind seats — a revised submission or a panel, where no plant is received — are read apart: their share of the review decisions and the stamp rate on them.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | blind-seat share | blind-seat stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 38416.2 ± 1079.9 | 3065.5 ± 1390.5 | 4049.6 | 0.695 | 0.302 | 0.003 | 0.047 | 0.057 | 0.280 | 0.944 | 43.90 | 55.05 | 0.60 |
| careful | 35350.7 ± 821.3 | nan ± nan | 4122.6 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.292 | 0.000 | 6.30 | 0.00 | 0.45 |
| stamper | 6937.1 ± 162.8 | -28413.6 ± 834.0 | 1041.8 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.021 | 1.000 | 13.75 | 179.65 | 1.00 |
| hand | 32145.9 ± 593.0 | -3204.8 ± 834.8 | 4447.5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.295 | 0.000 | 11.60 | 0.00 | 0.60 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 0.378 | 0.827 | 0.676 (22576) | 0.407 (7722) | 0.482 (5739) | 0.288 (1394) | 0.067 (43560) | 25.400 | 697.500 | 1.148 | 2.167 |
| careful | — | 0.668 | 0.000 (27448) | 0.000 (5667) | 0.000 (4419) | 0.000 (1173) | 0.000 (43745) | 23.750 | 700.250 | 1.094 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (20836) | 71.000 | 192.700 | 1.923 | 2.530 |
| hand | — | 0.803 | 0.000 (113) | 0.000 (11603) | 0.000 (18496) | 0.000 (15352) | 0.000 (43386) | 33.850 | 344.800 | 1.254 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| direct | 39.800 | 0.000 | 0.000 | 0.000 | 0.000 | 0.600 | 0.000 |
| careful | 39.600 | 0.000 | 0.000 | 0.000 | 0.000 | 0.450 | 0.000 |
| stamper | 39.900 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| hand | 39.850 | 0.000 | 0.000 | 0.000 | 0.000 | 0.600 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 22.600 / 39.800 | 43.900 ± 2.641 | +37.600 ± 2.641 | 22.150 | +13.150 ± 1.666 | 3.700 | 0.153 | 5.600 | +1.450 ± 0.651 | 1643.850 | 0.014 | -0.010 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 25583.530 ± 368.260 | +2971.693 ± 422.879 | 38416.2 ± 1079.9 | +3065.5 ± 1390.5 | 37.857 | -0.711 ± 0.386 | 14.150 ± 0.525 | +0.451 ± 0.761 | 18.051 | 0.001 | 2612.900 | 19.800 | 17.200 | -0.250 ± 0.703 | 1099.536 | 186.650 |
| careful | 22.150 / 39.600 | 6.300 ± 0.649 | — | 9.000 | — | 2.600 | 0.044 | 4.150 | — | 1595.100 | 0.024 | — | 0.000 / 0.000 (0.000 / 0.000) | 22611.837 ± 296.550 | — | 35350.7 ± 821.3 | — | 38.567 | — | 13.699 ± 0.397 | — | 16.874 | 0.000 | 2654.200 | 19.600 | 17.450 | — | 1103.486 | 220.800 |
| stamper | 4.850 / 39.900 | 13.750 ± 0.903 | +7.450 ± 0.860 | 109.400 | +100.400 ± 2.226 | 0.000 | 1.000 | 51.100 | +46.950 ± 1.974 | 871.800 | 0.194 | +0.170 ± 0.003 | 0.000 / 0.000 (0.000 / 0.000) | 8716.679 ± 214.897 | -13895.158 ± 410.681 | 6937.1 ± 162.8 | -28413.6 ± 834.0 | 27.527 | -11.040 ± 0.305 | 32.286 ± 0.656 | +18.587 ± 0.746 | 22.196 | 0.174 | 752.000 | 19.900 | 35.050 | +17.600 ± 0.828 | 5935.040 | 135.200 |
| hand | 19.500 / 39.850 | 11.600 ± 0.666 | +5.300 ± 0.941 | 62.250 | +53.250 ± 2.040 | 6.900 | 0.047 | 14.000 | +9.850 ± 0.933 | 1678.600 | 0.060 | +0.036 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 29714.546 ± 438.122 | +7102.709 ± 376.361 | 32145.9 ± 593.0 | -3204.8 ± 834.8 | 32.740 | -5.828 ± 0.318 | 20.386 ± 0.371 | +6.687 ± 0.456 | 19.478 | 0.010 | 2486.700 | 19.850 | 20.350 | +2.900 ± 0.369 | 86.726 | 150.900 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **direct**: p0 0.932/0.067/0.001 (595); p1 0.732/0.258/0.010 (736); p2 0.644/0.353/0.003 (845); p3 0.599/0.400/0.000 (795); p4 0.604/0.396/0.001 (610); p5 0.697/0.302/0.001 (335); p6 0.724/0.275/0.001 (98); p7 0.751/0.249/0.000 (32); p8 0.704/0.296/0.000 (4)
- **careful**: p0 1.000/0.000/0.000 (622); p1 1.000/0.000/0.000 (758); p2 1.000/0.000/0.000 (860); p3 1.000/0.000/0.000 (866); p4 1.000/0.000/0.000 (750); p5 1.000/0.000/0.000 (254); p6 1.000/0.000/0.000 (12)
- **stamper**: p0 0.000/1.000/0.000 (566); p1 0.000/1.000/0.000 (304); p2 0.000/1.000/0.000 (153); p3 0.000/1.000/0.000 (12); p4 0.000/1.000/0.000 (7); p5 0.000/1.000/0.000 (1)
- **hand**: p0 —/—/— (0); p1 —/—/— (0); p2 —/—/— (0); p3 —/—/— (0); p4 —/—/— (0); p5 —/—/— (0); p6 —/—/— (0); p7 —/—/— (0); p8 —/—/— (0); p9 —/—/— (0); p10 —/—/— (0); p11 —/—/— (0); p12 —/—/— (0); p13 —/—/— (0); p14 —/—/— (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling the requester's wallet refused to raise at least once (never a plant's: its raise is minted — §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 2608.5 / 306.1 | 0.20 / 0.07 | -0.14 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.07 / 0.08 | +0.01 ± 0.00 | 0.139 / 0.123 | -0.017 ± 0.006 | 0.045 / 0.000 | 0.001 / 0.000 | 0.058 / 0.058 | +0.000 ± 0.004 | 1.52 / 1.28 | -0.25 ± 0.09 |
| careful | 2649.1 / 267.9 | 0.14 / 0.07 | -0.07 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.07 / 0.07 | +0.00 ± 0.00 | 0.119 / 0.122 | +0.003 ± 0.003 | 0.038 / 0.000 | 0.000 / 0.000 | 0.060 / 0.059 | -0.001 ± 0.003 | 1.33 / 1.15 | -0.18 ± 0.05 |
| stamper | 871.8 / 148.0 | 0.84 / 0.44 | -0.40 ± 0.04 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.03 / 0.31 | +0.29 ± 0.06 | 0.173 / 0.156 | -0.016 ± 0.007 | 0.095 / 0.000 | 0.137 / 0.219 | 0.089 / 0.077 | -0.013 ± 0.006 | 2.97 / 1.47 | -1.50 ± 0.16 |
| hand | 2502.1 / 631.4 | 0.54 / 0.45 | -0.09 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.14 / 0.16 | +0.02 ± 0.00 | 0.310 / 0.325 | +0.015 ± 0.005 | 0.128 / 0.000 | 0.010 / 0.013 | 0.089 / 0.078 | -0.011 ± 0.003 | 2.22 / 2.11 | -0.11 ± 0.08 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| direct | -0.11 ± 0.02 | +0.00 ± 0.00 | +0.00 ± 0.00 | +0.002 ± 0.003 | -0.039 ± 0.007 | -0.001 ± 0.003 |
| careful | -0.07 ± 0.02 | +0.00 ± 0.00 | +0.00 ± 0.00 | +0.001 ± 0.003 | -0.039 ± 0.007 | -0.001 ± 0.003 |
| stamper | -0.94 ± 0.05 | +0.00 ± 0.00 | +0.29 ± 0.06 | -0.155 ± 0.012 | -0.190 ± 0.015 | -0.024 ± 0.007 |
| hand | -0.16 ± 0.02 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.027 ± 0.003 | -0.149 ± 0.014 | -0.011 ± 0.003 |

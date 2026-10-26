# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule`, seeds 21-40, hide ``, model `results/redteam/stability/learned-rev-stamper-2/wm/models/wm-online-5.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the plant-blind seats — a revised submission or a panel, where no plant is received — are read apart: their share of the review decisions and the stamp rate on them.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | blind-seat share | blind-seat stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 28065.9 ± 446.3 | -7284.8 ± 837.3 | 3506.5 | 0.567 | 0.430 | 0.003 | 0.282 | 0.307 | 0.197 | 0.977 | 69.90 | 209.60 | 0.15 |
| careful | 35350.7 ± 821.3 | nan ± nan | 4122.6 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.292 | 0.000 | 6.30 | 0.00 | 0.45 |
| stamper | 6937.1 ± 162.8 | -28413.6 ± 834.0 | 1041.8 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.021 | 1.000 | 13.75 | 179.65 | 1.00 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 0.892 | 0.952 | 0.876 (137) | 0.866 (881) | 0.753 (494) | 0.591 (22081) | 0.343 (46537) | 45.950 | 244.200 | 1.833 | 4.561 |
| careful | — | 0.668 | 0.000 (27448) | 0.000 (5667) | 0.000 (4419) | 0.000 (1173) | 0.000 (43745) | 23.750 | 700.250 | 1.094 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (20836) | 71.000 | 192.700 | 1.923 | 2.530 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| greedy | 39.850 | 0.000 | 0.000 | 0.000 | 0.000 | 0.150 | 0.000 |
| careful | 39.600 | 0.000 | 0.000 | 0.000 | 0.000 | 0.450 | 0.000 |
| stamper | 39.900 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 15.700 / 39.850 | 69.900 ± 4.260 | +63.600 ± 4.352 | 146.550 | +137.550 ± 3.518 | 6.050 | 0.247 | 26.100 | +21.950 ± 0.769 | 1742.600 | 0.054 | +0.030 ± 0.005 | 31390.217 ± 597.471 | +8778.380 ± 647.497 | 28065.9 ± 446.3 | -7284.8 ± 837.3 | 28.746 | -9.821 ± 0.337 | 23.940 ± 0.170 | +10.241 ± 0.446 | 21.930 | 0.061 | 2075.900 | 19.850 | 24.150 | +6.700 ± 0.465 | 79.352 | 141.700 |
| careful | 22.150 / 39.600 | 6.300 ± 0.649 | — | 9.000 | — | 2.600 | 0.044 | 4.150 | — | 1595.100 | 0.024 | — | 22611.837 ± 296.550 | — | 35350.7 ± 821.3 | — | 38.567 | — | 13.699 ± 0.397 | — | 16.874 | 0.000 | 2654.200 | 19.600 | 17.450 | — | 1103.486 | 220.800 |
| stamper | 4.850 / 39.900 | 13.750 ± 0.903 | +7.450 ± 0.860 | 109.400 | +100.400 ± 2.226 | 0.000 | 1.000 | 51.100 | +46.950 ± 1.974 | 871.800 | 0.194 | +0.170 ± 0.003 | 8716.679 ± 214.897 | -13895.158 ± 410.681 | 6937.1 ± 162.8 | -28413.6 ± 834.0 | 27.527 | -11.040 ± 0.305 | 32.286 ± 0.656 | +18.587 ± 0.746 | 22.196 | 0.174 | 752.000 | 19.900 | 35.050 | +17.600 ± 0.828 | 5935.040 | 135.200 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **greedy**: p0 0.822/0.178/0.000 (587); p1 0.384/0.600/0.016 (450); p2 0.457/0.536/0.008 (284); p3 0.584/0.413/0.003 (244); p4 0.540/0.459/0.001 (250); p5 0.491/0.508/0.001 (250); p6 0.508/0.491/0.000 (238); p7 0.546/0.454/0.000 (235); p8 0.590/0.410/0.000 (226); p9 0.569/0.431/0.000 (223); p10 0.538/0.462/0.000 (220); p11 0.586/0.414/0.000 (174); p12 0.563/0.437/0.000 (111); p13 0.393/0.607/0.000 (15)
- **careful**: p0 1.000/0.000/0.000 (622); p1 1.000/0.000/0.000 (758); p2 1.000/0.000/0.000 (860); p3 1.000/0.000/0.000 (866); p4 1.000/0.000/0.000 (750); p5 1.000/0.000/0.000 (254); p6 1.000/0.000/0.000 (12)
- **stamper**: p0 0.000/1.000/0.000 (566); p1 0.000/1.000/0.000 (304); p2 0.000/1.000/0.000 (153); p3 0.000/1.000/0.000 (12); p4 0.000/1.000/0.000 (7); p5 0.000/1.000/0.000 (1)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 2200.7 / 614.5 | 1.66 / 2.00 | +0.34 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.07 / 0.08 | +0.01 ± 0.00 | 0.510 / 0.621 | +0.110 ± 0.007 | 0.060 / 0.112 | 0.195 / 0.228 | +0.033 ± 0.005 | 3.61 / 3.76 | +0.15 ± 0.05 |
| careful | 2649.1 / 267.9 | 0.14 / 0.07 | -0.07 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.07 / 0.07 | +0.00 ± 0.00 | 0.119 / 0.122 | +0.003 ± 0.003 | 0.000 / 0.000 | 0.060 / 0.059 | -0.001 ± 0.003 | 1.33 / 1.15 | -0.18 ± 0.05 |
| stamper | 871.8 / 148.0 | 0.84 / 0.44 | -0.40 ± 0.04 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.03 / 0.31 | +0.29 ± 0.06 | 0.173 / 0.156 | -0.016 ± 0.007 | 0.137 / 0.219 | 0.089 / 0.077 | -0.013 ± 0.006 | 2.97 / 1.47 | -1.50 ± 0.16 |

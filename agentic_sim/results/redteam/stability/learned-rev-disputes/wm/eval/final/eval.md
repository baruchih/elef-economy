# Evaluation — cell `--entry-pool 20 --stampers 0.6 --dispute-policy truthful --learner-pop all --learner-role reviewer --learner-exit rule`, seeds 21-40, hide ``, model `results/redteam/stability/learned-rev-disputes/wm/models/wm-online-10.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the plant-blind seats — a revised submission or a panel, where no plant is received — are read apart: their share of the review decisions and the stamp rate on them.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | blind-seat share | blind-seat stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 28191.7 ± 712.6 | -5252.8 ± 1248.3 | 3831.1 | 0.588 | 0.411 | 0.001 | 0.235 | 0.255 | 0.254 | 0.891 | 38.40 | 208.80 | 0.05 |
| careful | 33444.4 ± 894.0 | nan ± nan | 4101.7 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.285 | 0.000 | 0.40 | 0.00 | 0.25 |
| stamper | 7125.9 ± 112.8 | -26318.5 ± 968.0 | 1053.0 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.027 | 1.000 | 8.15 | 186.30 | 1.00 |
| hand | 32105.8 ± 614.4 | -1338.6 ± 964.9 | 4304.7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.284 | 0.000 | 3.55 | 0.00 | 0.45 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 0.864 | 0.944 | 0.905 (1267) | 0.848 (1538) | 0.700 (1202) | 0.518 (22011) | 0.334 (50604) | 45.450 | 319.800 | 1.572 | 4.594 |
| careful | — | 0.687 | 0.000 (24146) | 0.000 (6755) | 0.000 (4661) | 0.000 (1443) | 0.000 (45029) | 24.950 | 696.200 | 1.133 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (21060) | 72.100 | 199.700 | 1.874 | 2.584 |
| hand | — | 0.807 | 0.000 (75) | 0.000 (12084) | 0.000 (16204) | 0.000 (14686) | 0.000 (43045) | 35.850 | 354.500 | 1.322 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| greedy | 39.750 | 0.000 | 0.000 | 0.000 | 0.000 | 0.050 | 0.000 |
| careful | 39.700 | 0.000 | 0.000 | 0.000 | 0.000 | 0.250 | 0.000 |
| stamper | 39.900 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| hand | 39.850 | 0.000 | 0.000 | 0.000 | 0.000 | 0.450 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 16.200 / 39.750 | 38.400 ± 2.789 | +38.000 ± 2.781 | 122.200 | +111.550 ± 4.119 | 5.450 | 0.177 | 25.700 | +20.450 ± 1.055 | 1662.650 | 0.008 | -0.005 ± 0.001 | 126.100 / 91.800 (126.100 / 91.800) | 31332.624 ± 432.566 | +8907.164 ± 534.037 | 28191.7 ± 712.6 | -5252.8 ± 1248.3 | 29.793 | -8.288 ± 0.524 | 24.000 ± 0.472 | +9.640 ± 0.674 | 22.020 | 0.053 | 2162.650 | 19.750 | 23.550 | +6.650 ± 0.654 | 68.517 | 133.950 |
| careful | 22.800 / 39.700 | 0.400 ± 0.134 | — | 10.650 | — | 3.700 | 0.048 | 5.250 | — | 1598.100 | 0.013 | — | 26.700 / 26.200 (26.700 / 26.200) | 22425.460 ± 528.637 | — | 33444.4 ± 894.0 | — | 38.081 | — | 14.360 ± 0.339 | — | 17.273 | 0.001 | 2660.500 | 19.700 | 16.900 | — | 985.796 | 198.850 |
| stamper | 5.500 / 39.900 | 8.150 ± 0.612 | +7.750 ± 0.619 | 109.750 | +99.100 ± 2.159 | 0.000 | 1.000 | 52.200 | +46.950 ± 1.751 | 704.200 | 0.016 | +0.003 ± 0.001 | 172.850 / 164.950 (172.850 / 164.950) | 8280.104 ± 185.330 | -14145.356 ± 564.796 | 7125.9 ± 112.8 | -26318.5 ± 968.0 | 27.799 | -10.282 ± 0.500 | 29.430 ± 0.708 | +15.069 ± 0.889 | 22.363 | 0.202 | 730.600 | 19.900 | 34.400 | +17.500 ± 0.872 | 5961.570 | 192.700 |
| hand | 19.800 / 39.850 | 3.550 ± 0.359 | +3.150 ± 0.335 | 65.750 | +55.100 ± 1.231 | 7.650 | 0.051 | 16.000 | +10.750 ± 0.688 | 1566.750 | 0.013 | +0.000 ± 0.001 | 92.350 / 88.900 (92.350 / 88.900) | 29348.109 ± 401.843 | +6922.649 ± 466.210 | 32105.8 ± 614.4 | -1338.6 ± 964.9 | 32.443 | -5.638 ± 0.401 | 19.687 ± 0.403 | +5.327 ± 0.594 | 19.775 | 0.023 | 2419.950 | 19.850 | 20.050 | +3.150 ± 0.534 | 118.326 | 226.900 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **greedy**: p0 0.845/0.155/0.000 (597); p1 0.437/0.559/0.004 (606); p2 0.441/0.559/0.001 (374); p3 0.509/0.491/0.000 (266); p4 0.525/0.475/0.001 (267); p5 0.599/0.399/0.002 (264); p6 0.578/0.422/0.001 (259); p7 0.597/0.401/0.002 (248); p8 0.583/0.417/0.000 (252); p9 0.596/0.403/0.000 (254); p10 0.629/0.370/0.001 (198); p11 0.638/0.362/0.000 (118); p12 0.659/0.341/0.000 (88); p13 0.673/0.327/0.000 (40)
- **careful**: p0 1.000/0.000/0.000 (599); p1 1.000/0.000/0.000 (731); p2 1.000/0.000/0.000 (840); p3 1.000/0.000/0.000 (866); p4 1.000/0.000/0.000 (743); p5 1.000/0.000/0.000 (280); p6 1.000/0.000/0.000 (43)
- **stamper**: p0 0.000/1.000/0.000 (580); p1 0.000/1.000/0.000 (306); p2 0.000/1.000/0.000 (150); p3 0.000/1.000/0.000 (8); p4 0.000/1.000/0.000 (7); p5 0.000/1.000/0.000 (3)
- **hand**: p0 —/—/— (0); p1 —/—/— (0); p2 —/—/— (0); p3 —/—/— (0); p4 —/—/— (0); p5 —/—/— (0); p6 —/—/— (0); p7 —/—/— (0); p8 —/—/— (0); p9 —/—/— (0); p10 —/—/— (0); p11 —/—/— (0); p12 —/—/— (0); p13 —/—/— (0); p14 —/—/— (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling the requester's wallet refused to raise at least once (never a plant's: its raise is minted — §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 2270.2 / 589.1 | 1.43 / 1.71 | +0.28 ± 0.05 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.07 / 0.08 | +0.02 ± 0.00 | 0.474 / 0.587 | +0.113 ± 0.010 | 0.275 / 0.000 | 0.052 / 0.112 | 0.170 / 0.203 | +0.033 ± 0.005 | 3.40 / 3.44 | +0.04 ± 0.08 |
| careful | 2657.3 / 273.4 | 0.17 / 0.08 | -0.09 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.07 / 0.08 | +0.01 ± 0.00 | 0.130 / 0.126 | -0.004 ± 0.004 | 0.041 / 0.000 | 0.001 / 0.001 | 0.061 / 0.067 | +0.006 ± 0.003 | 1.41 / 1.25 | -0.16 ± 0.09 |
| stamper | 876.6 / 147.8 | 1.10 / 0.56 | -0.53 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.02 / 0.24 | +0.21 ± 0.03 | 0.255 / 0.236 | -0.019 ± 0.009 | 0.136 / 0.000 | 0.166 / 0.264 | 0.112 / 0.081 | -0.031 ± 0.006 | 3.35 / 1.94 | -1.40 ± 0.15 |
| hand | 2465.1 / 617.6 | 0.74 / 0.62 | -0.13 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.13 / 0.15 | +0.02 ± 0.00 | 0.353 / 0.380 | +0.026 ± 0.006 | 0.145 / 0.000 | 0.022 / 0.031 | 0.099 / 0.088 | -0.011 ± 0.002 | 2.55 / 2.34 | -0.21 ± 0.05 |

# Evaluation — cell `--entry-pool 20 --stampers 0.6 --dispute-policy truthful --learner-pop all --learner-role reviewer --learner-exit rule`, seeds 21-40, hide ``, model `results/redteam/stability/learned-rev-disputes-2/wm/models/wm-online-10.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the plant-blind seats — a revised submission or a panel, where no plant is received — are read apart: their share of the review decisions and the stamp rate on them.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | blind-seat share | blind-seat stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 30478.9 ± 701.2 | -2965.6 ± 963.2 | 4042.9 | 0.602 | 0.395 | 0.003 | 0.179 | 0.200 | 0.279 | 0.924 | 35.90 | 179.40 | 0.20 |
| careful | 33444.4 ± 894.0 | nan ± nan | 4101.7 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.285 | 0.000 | 0.40 | 0.00 | 0.25 |
| stamper | 7125.9 ± 112.8 | -26318.5 ± 968.0 | 1053.0 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.027 | 1.000 | 8.15 | 186.30 | 1.00 |
| hand | 32105.8 ± 614.4 | -1338.6 ± 964.9 | 4304.7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.284 | 0.000 | 3.55 | 0.00 | 0.45 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 0.856 | 0.931 | 0.874 (925) | 0.872 (971) | 0.738 (1022) | 0.504 (30217) | 0.301 (47724) | 42.000 | 303.650 | 1.391 | 4.271 |
| careful | — | 0.687 | 0.000 (24146) | 0.000 (6755) | 0.000 (4661) | 0.000 (1443) | 0.000 (45029) | 24.950 | 696.200 | 1.133 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (21060) | 72.100 | 199.700 | 1.874 | 2.584 |
| hand | — | 0.807 | 0.000 (75) | 0.000 (12084) | 0.000 (16204) | 0.000 (14686) | 0.000 (43045) | 35.850 | 354.500 | 1.322 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| greedy | 39.750 | 0.000 | 0.000 | 0.000 | 0.000 | 0.200 | 0.000 |
| careful | 39.700 | 0.000 | 0.000 | 0.000 | 0.000 | 0.250 | 0.000 |
| stamper | 39.900 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| hand | 39.850 | 0.000 | 0.000 | 0.000 | 0.000 | 0.450 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 17.350 / 39.750 | 35.900 ± 2.324 | +35.500 ± 2.314 | 103.450 | +92.800 ± 2.902 | 6.200 | 0.173 | 22.250 | +17.000 ± 0.729 | 1646.450 | 0.006 | -0.007 ± 0.001 | 105.350 / 72.850 (105.350 / 72.850) | 32765.026 ± 352.248 | +10339.566 ± 479.817 | 30478.9 ± 701.2 | -2965.6 ± 963.2 | 30.055 | -8.026 ± 0.402 | 23.095 ± 0.467 | +8.735 ± 0.566 | 21.826 | 0.026 | 2247.950 | 19.750 | 22.400 | +5.500 ± 0.626 | 70.359 | 173.400 |
| careful | 22.800 / 39.700 | 0.400 ± 0.134 | — | 10.650 | — | 3.700 | 0.048 | 5.250 | — | 1598.100 | 0.013 | — | 26.700 / 26.200 (26.700 / 26.200) | 22425.460 ± 528.637 | — | 33444.4 ± 894.0 | — | 38.081 | — | 14.360 ± 0.339 | — | 17.273 | 0.001 | 2660.500 | 19.700 | 16.900 | — | 985.796 | 198.850 |
| stamper | 5.500 / 39.900 | 8.150 ± 0.612 | +7.750 ± 0.619 | 109.750 | +99.100 ± 2.159 | 0.000 | 1.000 | 52.200 | +46.950 ± 1.751 | 704.200 | 0.016 | +0.003 ± 0.001 | 172.850 / 164.950 (172.850 / 164.950) | 8280.104 ± 185.330 | -14145.356 ± 564.796 | 7125.9 ± 112.8 | -26318.5 ± 968.0 | 27.799 | -10.282 ± 0.500 | 29.430 ± 0.708 | +15.069 ± 0.889 | 22.363 | 0.202 | 730.600 | 19.900 | 34.400 | +17.500 ± 0.872 | 5961.570 | 192.700 |
| hand | 19.800 / 39.850 | 3.550 ± 0.359 | +3.150 ± 0.335 | 65.750 | +55.100 ± 1.231 | 7.650 | 0.051 | 16.000 | +10.750 ± 0.688 | 1566.750 | 0.013 | +0.000 ± 0.001 | 92.350 / 88.900 (92.350 / 88.900) | 29348.109 ± 401.843 | +6922.649 ± 466.210 | 32105.8 ± 614.4 | -1338.6 ± 964.9 | 32.443 | -5.638 ± 0.401 | 19.687 ± 0.403 | +5.327 ± 0.594 | 19.775 | 0.023 | 2419.950 | 19.850 | 20.050 | +3.150 ± 0.534 | 118.326 | 226.900 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **greedy**: p0 0.873/0.127/0.000 (587); p1 0.510/0.486/0.003 (537); p2 0.522/0.477/0.001 (347); p3 0.570/0.429/0.001 (288); p4 0.568/0.427/0.005 (277); p5 0.567/0.428/0.005 (275); p6 0.565/0.431/0.004 (276); p7 0.550/0.447/0.003 (268); p8 0.560/0.436/0.004 (269); p9 0.581/0.412/0.007 (270); p10 0.594/0.401/0.006 (236); p11 0.556/0.442/0.002 (170); p12 0.600/0.399/0.001 (145); p13 0.543/0.456/0.001 (72); p14 0.551/0.449/0.000 (24); p15 0.558/0.442/0.000 (2)
- **careful**: p0 1.000/0.000/0.000 (599); p1 1.000/0.000/0.000 (731); p2 1.000/0.000/0.000 (840); p3 1.000/0.000/0.000 (866); p4 1.000/0.000/0.000 (743); p5 1.000/0.000/0.000 (280); p6 1.000/0.000/0.000 (43)
- **stamper**: p0 0.000/1.000/0.000 (580); p1 0.000/1.000/0.000 (306); p2 0.000/1.000/0.000 (150); p3 0.000/1.000/0.000 (8); p4 0.000/1.000/0.000 (7); p5 0.000/1.000/0.000 (3)
- **hand**: p0 —/—/— (0); p1 —/—/— (0); p2 —/—/— (0); p3 —/—/— (0); p4 —/—/— (0); p5 —/—/— (0); p6 —/—/— (0); p7 —/—/— (0); p8 —/—/— (0); p9 —/—/— (0); p10 —/—/— (0); p11 —/—/— (0); p12 —/—/— (0); p13 —/—/— (0); p14 —/—/— (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling the requester's wallet refused to raise at least once (never a plant's: its raise is minted — §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 2292.7 / 621.8 | 1.40 / 1.65 | +0.25 ± 0.04 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.09 / 0.12 | +0.03 ± 0.01 | 0.510 / 0.613 | +0.103 ± 0.008 | 0.285 / 0.000 | 0.025 / 0.048 | 0.172 / 0.204 | +0.032 ± 0.006 | 3.23 / 3.34 | +0.11 ± 0.05 |
| careful | 2657.3 / 273.4 | 0.17 / 0.08 | -0.09 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.07 / 0.08 | +0.01 ± 0.00 | 0.130 / 0.126 | -0.004 ± 0.004 | 0.041 / 0.000 | 0.001 / 0.001 | 0.061 / 0.067 | +0.006 ± 0.003 | 1.41 / 1.25 | -0.16 ± 0.09 |
| stamper | 876.6 / 147.8 | 1.10 / 0.56 | -0.53 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.02 / 0.24 | +0.21 ± 0.03 | 0.255 / 0.236 | -0.019 ± 0.009 | 0.136 / 0.000 | 0.166 / 0.264 | 0.112 / 0.081 | -0.031 ± 0.006 | 3.35 / 1.94 | -1.40 ± 0.15 |
| hand | 2465.1 / 617.6 | 0.74 / 0.62 | -0.13 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.13 / 0.15 | +0.02 ± 0.00 | 0.353 / 0.380 | +0.026 ± 0.006 | 0.145 / 0.000 | 0.022 / 0.031 | 0.099 / 0.088 | -0.011 ± 0.002 | 2.55 / 2.34 | -0.21 ± 0.05 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| greedy | -0.19 ± 0.03 | +0.00 ± 0.00 | -0.00 ± 0.01 | -0.046 ± 0.005 | -0.384 ± 0.015 | -0.007 ± 0.005 |
| careful | -0.08 ± 0.02 | +0.00 ± 0.00 | +0.01 ± 0.00 | -0.001 ± 0.003 | -0.040 ± 0.008 | +0.006 ± 0.003 |
| stamper | -1.08 ± 0.04 | +0.00 ± 0.00 | +0.20 ± 0.03 | -0.188 ± 0.012 | -0.256 ± 0.013 | -0.043 ± 0.007 |
| hand | -0.23 ± 0.02 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.030 ± 0.005 | -0.176 ± 0.012 | -0.010 ± 0.002 |

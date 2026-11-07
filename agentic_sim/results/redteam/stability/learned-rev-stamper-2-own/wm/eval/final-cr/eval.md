# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule`, seeds 21-40, hide ``, model `/Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/learned-rev-stamper-2-own/wm/models/wm-online-10.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the plant-blind seats — a revised submission or a panel, where no plant is received — are read apart: their share of the review decisions and the stamp rate on them.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | blind-seat share | blind-seat stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 35657.6 ± 1089.9 | 183.0 ± 1385.2 | 4091.8 | 0.707 | 0.293 | 0.000 | 0.052 | 0.054 | 0.278 | 0.915 | 39.90 | 54.35 | 0.25 |
| careful | 35474.6 ± 806.5 | nan ± nan | 4031.2 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.284 | 0.000 | 6.70 | 0.00 | 0.40 |
| stamper | 6762.2 ± 145.0 | -28712.4 ± 863.6 | 1033.5 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.021 | 1.000 | 14.75 | 179.60 | 1.00 |
| hand | 32177.3 ± 564.1 | -3297.3 ± 816.5 | 4393.3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.290 | 0.000 | 11.65 | 0.00 | 0.70 |

The rate of verdicts given without inspecting by seat kind, measured from the engine's reviews (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, whose decisions the action counters cannot see). The reject-blind part is in brackets where it is not zero; the decisions pooled over the seeds in parentheses; `underfunded careful reviews` is the run's count of careful reviews that could not afford a cent of their care (mean ± SE), an upper bound on the blind readings that were a careful review paying nothing. Under 2.7.0 a plant reaches the initial review alone.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews |
|---|---|---|---|---|---|
| greedy | 0.052 (7161) / 0.054 (51955) [rej. blind 0.000] | — / 0.971 (20314) | — / 0.448 (2405) | — / — | 2.0 ± 0.4 |
| careful | 0.000 (5268) [rej. blind 0.000] / 0.000 (52441) [rej. blind 0.000] | — / 0.000 (19188) | — / 0.000 (3727) | — / — | 3.2 ± 0.4 |
| stamper | 1.000 (2911) / 1.000 (17318) | — / 1.000 (440) | — / — | — / — | 0.0 ± 0.0 |
| hand | 0.091 (12485) [rej. blind 0.000] / 0.141 (49888) | — / 0.012 (21309) | — / 0.005 (4184) | — / — | 0.9 ± 0.2 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 0.464 | 0.837 | 0.703 (15412) | 0.409 (9930) | 0.449 (7428) | 0.336 (5345) | 0.090 (43720) | 30.200 | 653.500 | 1.201 | 1.800 |
| careful | — | 0.675 | 0.000 (26075) | 0.000 (5345) | 0.000 (4336) | 0.000 (1149) | 0.000 (43719) | 24.450 | 701.250 | 1.178 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (20669) | 69.050 | 190.350 | 1.989 | 2.601 |
| hand | — | 0.806 | 0.000 (61) | 0.000 (11453) | 0.000 (17508) | 0.000 (15016) | 0.000 (43828) | 33.900 | 355.300 | 1.264 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| greedy | 39.600 | 0.000 | 0.000 | 0.000 | 0.000 | 0.250 | 0.000 |
| careful | 39.600 | 0.000 | 0.000 | 0.000 | 0.000 | 0.400 | 0.000 |
| stamper | 40.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| hand | 39.800 | 0.000 | 0.000 | 0.000 | 0.000 | 0.700 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 21.250 / 39.600 | 39.900 ± 2.533 | +33.200 ± 2.808 | 27.600 | +18.500 ± 1.977 | 4.150 | 0.143 | 10.600 | +5.750 ± 1.083 | 1698.850 | 0.012 | -0.011 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 27194.390 ± 783.104 | +3748.972 ± 905.786 | 35657.6 ± 1089.9 | +183.0 ± 1385.2 | 36.825 | -1.040 ± 0.855 | 16.673 ± 0.934 | +2.543 ± 1.125 | 18.417 | 0.001 | 2601.850 | 19.600 | 18.350 | +0.800 ± 0.531 | 840.687 | 209.550 |
| careful | 22.050 / 39.600 | 6.700 ± 0.788 | — | 9.100 | — | 3.550 | 0.056 | 4.850 | — | 1589.550 | 0.023 | — | 0.000 / 0.000 (0.000 / 0.000) | 23445.418 ± 457.620 | — | 35474.6 ± 806.5 | — | 37.866 | — | 14.129 ± 0.457 | — | 17.437 | 0.002 | 2623.950 | 19.600 | 17.550 | — | 1018.837 | 230.750 |
| stamper | 5.450 / 40.000 | 14.750 ± 0.882 | +8.050 ± 0.944 | 107.350 | +98.250 ± 1.343 | 0.000 | 1.000 | 49.050 | +44.200 ± 1.182 | 865.850 | 0.195 | +0.172 ± 0.003 | 0.000 / 0.000 (0.000 / 0.000) | 8723.964 ± 133.975 | -14721.454 ± 468.500 | 6762.2 ± 145.0 | -28712.4 ± 863.6 | 27.350 | -10.516 ± 0.542 | 33.102 ± 0.772 | +18.973 ± 0.905 | 22.321 | 0.164 | 755.600 | 20.000 | 34.550 | +17.000 ± 0.903 | 5950.263 | 152.600 |
| hand | 19.950 / 39.800 | 11.650 ± 0.646 | +4.950 ± 1.077 | 63.450 | +54.350 ± 2.413 | 6.400 | 0.052 | 14.100 | +9.250 ± 0.757 | 1676.650 | 0.059 | +0.036 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 29461.105 ± 426.345 | +6015.686 ± 552.395 | 32177.3 ± 564.1 | -3297.3 ± 816.5 | 32.912 | -4.953 ± 0.529 | 19.971 ± 0.414 | +5.841 ± 0.617 | 19.367 | 0.011 | 2476.850 | 19.800 | 19.850 | +2.300 ± 0.442 | 136.208 | 162.500 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **greedy**: p0 0.957/0.043/0.000 (584); p1 0.756/0.244/0.000 (695); p2 0.658/0.342/0.000 (777); p3 0.604/0.396/0.000 (745); p4 0.603/0.397/0.000 (539); p5 0.689/0.311/0.000 (342); p6 0.714/0.286/0.000 (189); p7 0.673/0.327/0.000 (76); p8 0.705/0.295/0.000 (62); p9 0.700/0.300/0.000 (56); p10 0.693/0.307/0.000 (28)
- **careful**: p0 1.000/0.000/0.000 (617); p1 1.000/0.000/0.000 (712); p2 1.000/0.000/0.000 (845); p3 1.000/0.000/0.000 (886); p4 1.000/0.000/0.000 (747); p5 1.000/0.000/0.000 (213); p6 1.000/0.000/0.000 (11)
- **stamper**: p0 0.000/1.000/0.000 (565); p1 0.000/1.000/0.000 (304); p2 0.000/1.000/0.000 (154); p3 0.000/1.000/0.000 (7); p4 0.000/1.000/0.000 (3); p5 0.000/1.000/0.000 (1)
- **hand**: p0 —/—/— (0); p1 —/—/— (0); p2 —/—/— (0); p3 —/—/— (0); p4 —/—/— (0); p5 —/—/— (0); p6 —/—/— (0); p7 —/—/— (0); p8 —/—/— (0); p9 —/—/— (0); p10 —/—/— (0); p11 —/—/— (0); p12 —/—/— (0); p13 —/—/— (0); p14 —/—/— (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling the requester's wallet refused to raise at least once (never a plant's: its raise is minted — §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 2597.8 / 358.1 | 0.23 / 0.16 | -0.07 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.08 / 0.10 | +0.02 ± 0.00 | 0.149 / 0.138 | -0.011 ± 0.008 | 0.049 / 0.000 | 0.001 / 0.001 | 0.067 / 0.071 | +0.004 ± 0.004 | 1.62 / 1.43 | -0.19 ± 0.08 |
| careful | 2622.1 / 263.4 | 0.23 / 0.11 | -0.13 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.07 / 0.08 | +0.01 ± 0.00 | 0.155 / 0.154 | -0.000 ± 0.003 | 0.059 / 0.000 | 0.001 / 0.002 | 0.060 / 0.062 | +0.002 ± 0.004 | 1.57 / 1.33 | -0.24 ± 0.07 |
| stamper | 865.9 / 145.6 | 0.85 / 0.43 | -0.41 ± 0.04 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.03 / 0.28 | +0.26 ± 0.04 | 0.175 / 0.148 | -0.027 ± 0.006 | 0.098 / 0.000 | 0.127 / 0.207 | 0.092 / 0.076 | -0.017 ± 0.006 | 3.22 / 1.76 | -1.47 ± 0.25 |
| hand | 2494.4 / 624.2 | 0.55 / 0.46 | -0.10 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.14 / 0.16 | +0.02 ± 0.00 | 0.314 / 0.330 | +0.016 ± 0.007 | 0.129 / 0.000 | 0.011 / 0.015 | 0.086 / 0.078 | -0.007 ± 0.004 | 2.21 / 1.95 | -0.25 ± 0.07 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| greedy | -0.08 ± 0.02 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.006 ± 0.003 | -0.051 ± 0.013 | -0.001 ± 0.004 |
| careful | -0.13 ± 0.02 | +0.00 ± 0.00 | +0.01 ± 0.00 | -0.002 ± 0.003 | -0.060 ± 0.008 | +0.002 ± 0.004 |
| stamper | -0.98 ± 0.05 | +0.00 ± 0.00 | +0.25 ± 0.04 | -0.179 ± 0.012 | -0.203 ± 0.018 | -0.032 ± 0.008 |
| hand | -0.19 ± 0.02 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.029 ± 0.004 | -0.152 ± 0.011 | -0.008 ± 0.004 |

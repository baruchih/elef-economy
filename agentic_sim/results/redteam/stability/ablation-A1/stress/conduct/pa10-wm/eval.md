# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1 --pi-a0 0.10 --pi-a-max 0.10`, seeds 21-60, hide ``, model `/Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/ablation-A1/stress/learned/horizon/pa10-t1-b1-mc/wm-ret/models/wm-online-10.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:greedy:0.25 | 33867.3 ± 362.6 | -1827.2 ± 522.8 | 4970.4 | 0.956 | 0.013 | 0.002 | 0.062 | 0.072 | 0.397 | 0.005 | 4.33 | 34.52 | 0.35 |
| mix:greedy:0.75 | 32746.1 ± 408.4 | -2948.4 ± 641.8 | 4832.1 | 0.843 | 0.036 | 0.016 | 0.207 | 0.208 | 0.368 | 0.067 | 9.75 | 97.50 | 0.35 |
| careful | 35694.5 ± 562.1 | nan ± nan | 4595.5 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.381 | 0.000 | 2.55 | 0.00 | 0.20 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:greedy:0.25 | 0.062 (18997) [rej. blind 0.004] / 0.072 (100865) [rej. blind 0.004] | 0.003 (9254) / 0.006 (52242) [rej. blind 0.000] | 0.003 (8382) [rej. blind 0.000] / 0.004 (9076) [rej. blind 0.000] | — / — |
| mix:greedy:0.75 | 0.207 (27263) [rej. blind 0.023] / 0.208 (94937) [rej. blind 0.020] | 0.061 (11093) [rej. blind 0.006] / 0.074 (41490) [rej. blind 0.007] | 0.053 (9446) [rej. blind 0.009] / 0.059 (9055) [rej. blind 0.008] | — / — |
| careful | 0.000 (10503) / 0.000 (103317) | 0.000 (6289) / 0.000 (49205) | 0.000 (6363) / 0.000 (8143) | — / — |

The stressed world's fourth action by seat kind — the allowance claimed and the verdict F without inspecting (counted above among the blind verdicts; the ledger sees a careful review, so the measured reading below cannot see it):

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:greedy:0.25 | 0.041 (18997) / 0.047 (100865) | 0.003 (9254) / 0.003 (52242) | 0.002 (8382) / 0.002 (9076) | — / — |
| mix:greedy:0.75 | 0.137 (27263) / 0.141 (94937) | 0.046 (11093) / 0.050 (41490) | 0.036 (9446) / 0.038 (9055) | — / — |
| careful | 0.000 (10503) / 0.000 (103317) | 0.000 (6289) / 0.000 (49205) | 0.000 (6363) / 0.000 (8143) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| mix:greedy:0.25 | 0.021 (18997) [rej. blind 0.004] / 0.026 (100865) [rej. blind 0.004] | 0.000 (9254) / 0.003 (52242) [rej. blind 0.000] | 0.001 (8382) [rej. blind 0.000] / 0.002 (9076) [rej. blind 0.000] | — / — | 2.3 ± 0.2 | -5678 |
| mix:greedy:0.75 | 0.071 (27263) [rej. blind 0.023] / 0.067 (94937) [rej. blind 0.020] | 0.016 (11093) [rej. blind 0.006] / 0.024 (41490) [rej. blind 0.007] | 0.017 (9446) [rej. blind 0.009] / 0.020 (9055) [rej. blind 0.008] | — / — | 1.6 ± 0.2 | -20392 |
| careful | 0.000 (10503) [rej. blind 0.000] / 0.000 (103317) [rej. blind 0.000] | 0.000 (6289) / 0.000 (49205) | 0.000 (6363) / 0.000 (8143) | — / — | 2.6 ± 0.3 | +13 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:greedy:0.25 | 1.000 | 0.977 | — (0) | — (0) | 0.000 (6381) | 0.000 (9795) | 0.014 (182640) | 11.775 | 480.100 | 1.267 | 2.932 |
| mix:greedy:0.75 | 1.000 | 0.999 | — (0) | — (0) | 0.000 (456) | 0.000 (542) | 0.035 (192286) | 17.775 | 350.825 | 1.466 | 5.485 |
| careful | — | 0.911 | — (0) | — (0) | 0.000 (33138) | 0.000 (1109) | 0.000 (149573) | 4.725 | 678.650 | 1.183 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| mix:greedy:0.25 | 39.825 | 0.000 | 0.000 | 0.000 | 0.000 | 0.350 | 0.000 |
| mix:greedy:0.75 | 39.775 | 0.000 | 0.000 | 0.000 | 0.000 | 0.350 | 0.000 |
| careful | 39.675 | 0.000 | 0.000 | 0.000 | 0.000 | 0.200 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:greedy:0.25 | 20.900 / 39.825 | 4.325 ± 0.386 | +1.775 ± 0.442 | 37.025 | +26.700 ± 2.211 | 5.350 | 0.084 | 11.775 | +7.050 ± 0.508 | 1946.425 | 0.039 | +0.014 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 29068.683 ± 282.973 | +3878.039 ± 360.803 | 33867.3 ± 362.6 | -1827.2 ± 522.8 | 33.415 | -2.564 ± 0.328 | 18.981 ± 0.255 | +3.870 ± 0.352 | 18.941 | 0.002 | 2529.175 | 19.825 | 18.925 | +2.550 ± 0.336 | 138.970 | 197.425 |
| mix:greedy:0.75 | 18.500 / 39.775 | 9.750 ± 0.628 | +7.200 ± 0.723 | 115.825 | +105.500 ± 3.276 | 10.250 | 0.233 | 17.775 | +13.050 ± 0.718 | 1886.900 | 0.064 | +0.040 ± 0.002 | 0.000 / 0.000 (0.000 / 0.000) | 29964.460 ± 298.054 | +4773.816 ± 378.443 | 32746.1 ± 408.4 | -2948.4 ± 641.8 | 31.162 | -4.817 ± 0.319 | 20.972 ± 0.292 | +5.862 ± 0.431 | 19.491 | 0.019 | 2341.375 | 19.775 | 21.275 | +4.900 ± 0.402 | 63.053 | 211.075 |
| careful | 23.300 / 39.675 | 2.550 ± 0.277 | — | 10.325 | — | 3.150 | 0.057 | 4.725 | — | 1887.250 | 0.025 | — | 0.000 / 0.000 (0.000 / 0.000) | 25190.644 ± 294.399 | — | 35694.5 ± 562.1 | — | 35.979 | — | 15.111 ± 0.293 | — | 18.104 | 0.002 | 2585.700 | 19.675 | 16.375 | — | 660.690 | 211.575 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **mix:greedy:0.25**: p0 0.987/0.010/0.003 (574); p1 0.933/0.062/0.004 (617); p2 0.982/0.013/0.005 (568); p3 0.990/0.009/0.001 (536); p4 0.989/0.008/0.003 (518); p5 0.996/0.003/0.001 (476); p6 0.997/0.003/0.000 (452); p7 0.993/0.005/0.003 (324); p8 0.999/0.000/0.001 (252); p9 0.996/0.001/0.002 (210); p10 0.997/0.002/0.002 (160); p11 0.993/0.001/0.006 (107); p12 0.995/0.005/0.001 (32); p13 1.000/0.000/0.000 (3)
- **mix:greedy:0.75**: p0 0.949/0.039/0.012 (492); p1 0.851/0.136/0.012 (365); p2 0.924/0.045/0.031 (304); p3 0.967/0.024/0.009 (286); p4 0.956/0.031/0.013 (293); p5 0.941/0.042/0.017 (294); p6 0.959/0.026/0.015 (299); p7 0.950/0.027/0.024 (296); p8 0.942/0.036/0.022 (305); p9 0.955/0.024/0.022 (306); p10 0.953/0.023/0.024 (307); p11 0.968/0.018/0.014 (288); p12 0.967/0.022/0.011 (254); p13 0.960/0.026/0.014 (174); p14 0.932/0.041/0.027 (58); p15 0.923/0.000/0.077 (1)
- **careful**: p0 1.000/0.000/0.000 (605); p1 1.000/0.000/0.000 (731); p2 1.000/0.000/0.000 (903); p3 1.000/0.000/0.000 (1015); p4 1.000/0.000/0.000 (1021); p5 1.000/0.000/0.000 (293); p6 1.000/0.000/0.000 (27); p7 1.000/0.000/0.000 (1)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:greedy:0.25 | 2521.6 / 474.9 | 0.48 / 0.40 | -0.09 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.14 / 0.16 | +0.02 ± 0.00 | 0.286 / 0.253 | -0.033 ± 0.006 | 0.121 / 0.127 | 0.002 / 0.000 | 0.073 / 0.069 | -0.003 ± 0.002 | 2.14 / 1.93 | -0.21 ± 0.07 |
| mix:greedy:0.75 | 2373.4 / 681.6 | 1.06 / 1.15 | +0.09 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.10 / 0.10 | +0.00 ± 0.00 | 0.445 / 0.470 | +0.026 ± 0.005 | 0.227 / 0.261 | 0.019 / 0.000 | 0.125 / 0.134 | +0.009 ± 0.003 | 2.91 / 2.96 | +0.04 ± 0.06 |
| careful | 2582.9 / 262.6 | 0.33 / 0.23 | -0.10 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.13 / 0.12 | -0.01 ± 0.00 | 0.181 / 0.155 | -0.026 ± 0.004 | 0.075 / 0.086 | 0.002 / 0.000 | 0.058 / 0.052 | -0.005 ± 0.002 | 1.88 / 1.54 | -0.34 ± 0.06 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| mix:greedy:0.25 | -0.10 ± 0.01 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.054 ± 0.004 | -0.009 ± 0.003 | -0.003 ± 0.002 |
| mix:greedy:0.75 | -0.05 ± 0.01 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.056 ± 0.003 | -0.015 ± 0.003 | -0.002 ± 0.002 |
| careful | -0.09 ± 0.01 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.027 ± 0.004 | +0.010 ± 0.002 | -0.005 ± 0.002 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| mix:greedy:0.25 | 0.509 / 0.209 | 0.20 / 0.19 | 0.040 / 0.112 | 0.00 / 0.00 | 0.20 / 0.20 | 0.309 / 0.180 |
| mix:greedy:0.75 | 0.430 / 0.255 | 0.38 / 0.40 | 0.046 / 0.103 | 0.00 / 0.00 | 0.40 / 0.40 | 0.443 / 0.279 |
| careful | 0.470 / 0.139 | 0.30 / 0.31 | 0.040 / 0.164 | 0.00 / 0.00 | 0.29 / 0.32 | 0.309 / 0.259 |

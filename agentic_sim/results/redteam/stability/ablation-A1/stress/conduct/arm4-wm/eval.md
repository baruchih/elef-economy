# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1 --arm 4`, seeds 21-60, hide ``, model `/Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/ablation-A1/stress/learned/horizon/arm4-t1-b1-mc/wm-ret/models/wm-online-10.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:greedy:0.25 | 27964.7 ± 466.8 | -3078.3 ± 503.7 | 3070.8 | 0.934 | 0.023 | 0.001 | 0.062 | 0.066 | 0.000 | 0.000 | 2.73 | 33.08 | 0.55 |
| mix:greedy:0.75 | 30270.2 ± 608.7 | -772.7 ± 672.2 | 3199.2 | 0.825 | 0.044 | 0.002 | 0.186 | 0.172 | 0.001 | 0.106 | 5.35 | 84.97 | 0.47 |
| careful | 31042.9 ± 550.2 | nan ± nan | 2927.0 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 2.48 | 0.00 | 0.17 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:greedy:0.25 | 0.062 (18158) [rej. blind 0.000] / 0.066 (104656) [rej. blind 0.001] | — / 0.000 (17) | — / — | — / — |
| mix:greedy:0.75 | 0.186 (25914) [rej. blind 0.001] / 0.172 (101912) [rej. blind 0.002] | — / 0.107 (131) | — / 0.091 (11) | — / — |
| careful | 0.000 (10900) / 0.000 (106176) | — / 0.000 (5) | — / — | — / — |

The stressed world's fourth action by seat kind — the allowance claimed and the verdict F without inspecting (counted above among the blind verdicts; the ledger sees a careful review, so the measured reading below cannot see it):

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:greedy:0.25 | 0.044 (18158) / 0.042 (104656) | — / 0.000 (17) | — / — | — / — |
| mix:greedy:0.75 | 0.143 (25914) / 0.125 (101912) | — / 0.099 (131) | — / 0.000 (11) | — / — |
| careful | 0.000 (10900) / 0.000 (106176) | — / 0.000 (5) | — / — | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| mix:greedy:0.25 | 0.018 (18158) [rej. blind 0.001] / 0.025 (104656) [rej. blind 0.001] | — / 0.000 (17) | — / — | — / — | 5.1 ± 0.4 | -5114 |
| mix:greedy:0.75 | 0.043 (25914) [rej. blind 0.001] / 0.048 (101912) [rej. blind 0.002] | — / 0.008 (131) | — / 0.091 (11) | — / — | 5.3 ± 0.3 | -16391 |
| careful | 0.000 (10900) [rej. blind 0.000] / 0.000 (106176) [rej. blind 0.000] | — / 0.000 (5) | — / — | — / — | 5.3 ± 0.4 | +39 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:greedy:0.25 | 0.998 | 0.987 | — (0) | — (0) | 0.002 (2460) | 0.008 (2727) | 0.024 (117644) | 8.900 | 525.500 | 1.223 | 3.716 |
| mix:greedy:0.75 | 1.000 | 0.999 | — (0) | — (0) | 0.000 (131) | 0.000 (175) | 0.044 (127662) | 12.275 | 429.150 | 1.203 | 6.923 |
| careful | — | 0.952 | — (0) | — (0) | 0.000 (11080) | 0.000 (1162) | 0.000 (104839) | 5.150 | 645.000 | 1.212 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| mix:greedy:0.25 | 39.375 | 0.000 | 0.000 | 0.000 | 0.000 | 0.550 | 0.000 |
| mix:greedy:0.75 | 39.400 | 0.000 | 0.000 | 0.000 | 0.000 | 0.475 | 0.000 |
| careful | 39.500 | 0.000 | 0.000 | 0.000 | 0.000 | 0.175 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:greedy:0.25 | 17.875 / 39.375 | 2.725 ± 0.253 | +0.250 ± 0.332 | 35.475 | +25.525 ± 2.383 | 6.050 | 0.098 | 8.900 | +3.750 ± 0.500 | 2002.300 | 0.032 | +0.015 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 23037.999 ± 400.599 | +3048.980 ± 493.613 | 27964.7 ± 466.8 | -3078.3 ± 503.7 | 35.308 | -2.988 ± 0.448 | 19.795 ± 0.633 | +5.614 ± 0.643 | 17.690 | 0.000 | 2620.625 | 19.375 | 21.500 | +2.350 ± 0.311 | 369.592 | 273.425 |
| mix:greedy:0.75 | 17.100 / 39.400 | 5.350 ± 0.457 | +2.875 ± 0.464 | 105.575 | +95.625 ± 3.047 | 7.325 | 0.323 | 12.275 | +7.125 ± 0.556 | 2038.375 | 0.054 | +0.037 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 25353.500 ± 246.453 | +5364.481 ± 354.150 | 30270.2 ± 608.7 | -772.7 ± 672.2 | 33.307 | -4.989 ± 0.288 | 20.228 ± 0.592 | +6.047 ± 0.669 | 18.100 | 0.002 | 2548.125 | 19.400 | 22.300 | +3.150 ± 0.339 | 54.616 | 235.200 |
| careful | 20.350 / 39.500 | 2.475 ± 0.277 | — | 9.950 | — | 3.850 | 0.045 | 5.150 | — | 1929.600 | 0.017 | — | 0.000 / 0.000 (0.000 / 0.000) | 19989.020 ± 331.294 | — | 31042.9 ± 550.2 | — | 38.296 | — | 14.182 ± 0.367 | — | 16.518 | 0.000 | 2659.550 | 19.500 | 19.150 | — | 999.178 | 263.125 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **mix:greedy:0.25**: p0 0.983/0.015/0.002 (546); p1 0.934/0.065/0.001 (485); p2 0.973/0.027/0.000 (384); p3 0.976/0.024/0.000 (353); p4 0.978/0.021/0.001 (299); p5 0.992/0.008/0.000 (236); p6 0.999/0.001/0.000 (191); p7 0.999/0.001/0.000 (151); p8 0.995/0.005/0.000 (120); p9 0.989/0.011/0.000 (89); p10 0.995/0.005/0.000 (54); p11 0.972/0.028/0.000 (27); p12 0.972/0.028/0.000 (6)
- **mix:greedy:0.75**: p0 0.956/0.039/0.005 (530); p1 0.894/0.103/0.004 (388); p2 0.952/0.047/0.001 (272); p3 0.939/0.059/0.002 (227); p4 0.967/0.031/0.003 (184); p5 0.973/0.027/0.000 (169); p6 0.968/0.032/0.000 (165); p7 0.987/0.013/0.000 (159); p8 0.961/0.038/0.001 (153); p9 0.966/0.033/0.001 (145); p10 0.951/0.047/0.002 (130); p11 0.948/0.050/0.001 (116); p12 0.910/0.090/0.000 (83); p13 0.886/0.114/0.000 (47); p14 0.873/0.127/0.000 (19); p15 0.978/0.022/0.000 (2)
- **careful**: p0 1.000/0.000/0.000 (556); p1 1.000/0.000/0.000 (540); p2 1.000/0.000/0.000 (542); p3 1.000/0.000/0.000 (529); p4 1.000/0.000/0.000 (529); p5 1.000/0.000/0.000 (205); p6 1.000/0.000/0.000 (25); p7 1.000/0.000/0.000 (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:greedy:0.25 | 2616.4 / 453.9 | 0.21 / 0.18 | -0.03 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.08 / 0.08 | +0.00 ± 0.00 | 0.135 / 0.118 | -0.017 ± 0.005 | 0.057 / 0.063 | 0.000 / 0.000 | 0.070 / 0.087 | +0.017 ± 0.002 | 1.63 / 1.48 | -0.15 ± 0.05 |
| mix:greedy:0.75 | 2547.8 / 647.9 | 0.38 / 0.42 | +0.04 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.10 / 0.10 | -0.00 ± 0.00 | 0.216 / 0.226 | +0.010 ± 0.008 | 0.101 / 0.123 | 0.002 / 0.000 | 0.087 / 0.108 | +0.021 ± 0.003 | 2.12 / 2.12 | +0.00 ± 0.04 |
| careful | 2654.4 / 272.5 | 0.13 / 0.07 | -0.06 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.06 / 0.07 | +0.01 ± 0.00 | 0.101 / 0.081 | -0.020 ± 0.003 | 0.033 / 0.035 | 0.000 / 0.000 | 0.058 / 0.063 | +0.005 ± 0.003 | 1.38 / 1.29 | -0.09 ± 0.08 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| mix:greedy:0.25 | -0.05 ± 0.01 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.032 ± 0.005 | -0.007 ± 0.002 | +0.005 ± 0.002 |
| mix:greedy:0.75 | -0.05 ± 0.01 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.042 ± 0.003 | -0.010 ± 0.002 | -0.001 ± 0.002 |
| careful | -0.06 ± 0.01 | +0.00 ± 0.00 | +0.01 ± 0.00 | -0.018 ± 0.003 | +0.003 ± 0.002 | +0.004 ± 0.002 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| mix:greedy:0.25 | 0.000 / 0.000 | 0.36 / — | 0.038 / 0.000 | 0.00 / — | — / — | 0.937 / 0.000 |
| mix:greedy:0.75 | 0.001 / 0.000 | 0.27 / — | 0.034 / 0.000 | 0.00 / — | — / — | 0.985 / 0.000 |
| careful | 0.000 / 0.000 | 0.50 / — | 0.040 / 0.000 | 0.00 / — | — / — | 0.888 / 0.000 |

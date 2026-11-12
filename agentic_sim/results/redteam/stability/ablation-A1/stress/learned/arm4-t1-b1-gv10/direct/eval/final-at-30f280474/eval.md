# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --arm 4 --temptation 1 --gv 10 --bond-mult-later 1`, seeds 21-40, hide ``, model `None` (value off, horizon 8)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 29695.4 ± 688.6 | 10.8 ± 751.1 | 3161.0 | 0.884 | 0.017 | 0.001 | 0.091 | 0.120 | 0.002 | 0.982 | 4.35 | 62.95 | 0.20 |
| careful | 29684.6 ± 609.8 | nan ± nan | 2897.3 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 2.90 | 0.00 | 0.60 |
| stamper | 6557.9 ± 267.2 | -23126.7 ± 599.0 | 975.4 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.000 | — | 9.40 | 170.90 | 1.00 |
| claimer | 8689.6 ± 210.8 | -20995.0 ± 636.0 | 977.1 | 0.000 | 0.000 | 0.000 | 1.000 | 1.000 | 0.000 | — | 9.35 | 171.60 | 1.00 |
| hand | 28265.0 ± 567.5 | -1419.7 ± 623.3 | 3091.7 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.002 | 0.000 | 3.15 | 0.00 | 0.45 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| direct | 0.091 (12865) [rej. blind 0.001] / 0.120 (50242) [rej. blind 0.001] | — / 1.000 (106) [rej. blind 0.038] | — / 0.714 (7) [rej. blind 0.714] | — / — |
| careful | 0.000 (5277) / 0.000 (52668) | — / 0.000 (1) | — / — | — / — |
| stamper | 1.000 (2604) / 1.000 (16904) | — / — | — / — | — / — |
| claimer | 1.000 (2626) / 1.000 (16916) | — / — | — / — | — / — |
| hand | 0.000 (12129) / 0.000 (49555) | — / 0.000 (136) | — / 0.000 (13) | — / — |

The stressed world's fourth action by seat kind — the allowance claimed and the verdict F without inspecting (counted above among the blind verdicts; the ledger sees a careful review, so the measured reading below cannot see it):

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| direct | 0.074 (12865) / 0.103 (50242) | — / 0.896 (106) | — / 0.000 (7) | — / — |
| careful | 0.000 (5277) / 0.000 (52668) | — / 0.000 (1) | — / — | — / — |
| stamper | 0.000 (2604) / 0.000 (16904) | — / — | — / — | — / — |
| claimer | 1.000 (2626) / 1.000 (16916) | — / — | — / — | — / — |
| hand | 0.000 (12129) / 0.000 (49555) | — / 0.000 (136) | — / 0.000 (13) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| direct | 0.023 (12865) [rej. blind 0.006] / 0.032 (50242) [rej. blind 0.004] | — / 0.104 (106) [rej. blind 0.038] | — / 0.714 (7) [rej. blind 0.714] | — / — | 49.5 ± 1.5 | -5387 |
| careful | 0.011 (5277) [rej. blind 0.009] / 0.014 (52668) [rej. blind 0.003] | — / 0.000 (1) | — / — | — / — | 53.3 ± 1.5 | +787 |
| stamper | 1.000 (2604) / 1.000 (16904) | — / — | — / — | — / — | 0.0 ± 0.0 | +0 |
| claimer | 0.038 (2626) / 0.057 (16916) | — / — | — / — | — / — | 0.0 ± 0.0 | -18478 |
| hand | 0.067 (12129) [rej. blind 0.005] / 0.100 (49555) [rej. blind 0.004] | — / 0.000 (136) | — / 0.000 (13) | — / — | 46.8 ± 1.4 | +5776 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 0.998 | 0.999 | — (0) | — (0) | 0.015 (131) | 0.027 (37) | 0.017 (63052) | 12.500 | 384.900 | 1.279 | 5.036 |
| careful | — | 0.946 | — (0) | — (0) | 0.000 (6401) | — (0) | 0.000 (51545) | 4.800 | 653.600 | 1.191 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (19508) | 50.850 | 210.400 | 1.747 | 3.361 |
| claimer | — | 1.000 | — (0) | — (0) | — (0) | — (0) | 0.000 (19542) | 54.900 | 205.250 | 1.744 | 3.126 |
| hand | — | 0.998 | — (0) | — (0) | 0.000 (94) | 0.000 (1026) | 0.000 (60713) | 11.000 | 335.800 | 1.314 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| direct | 39.500 | 0.000 | 0.000 | 0.000 | 0.000 | 0.200 | 0.000 |
| careful | 39.650 | 0.000 | 0.000 | 0.000 | 0.000 | 0.600 | 0.000 |
| stamper | 39.950 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| claimer | 39.800 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| hand | 39.750 | 0.000 | 0.000 | 0.000 | 0.000 | 0.450 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 17.550 / 39.500 | 4.350 ± 0.582 | +1.450 ± 0.829 | 65.350 | +56.450 ± 1.776 | 7.450 | 0.120 | 12.500 | +7.700 ± 0.719 | 1979.600 | 0.045 | +0.028 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 24882.207 ± 260.669 | +5599.936 ± 504.815 | 29695.4 ± 688.6 | +10.8 ± 751.1 | 32.732 | -5.195 ± 0.551 | 19.504 ± 0.582 | +5.337 ± 0.670 | 18.566 | 0.006 | 2504.950 | 19.500 | 21.950 | +2.400 ± 0.483 | 54.752 | 843.050 |
| careful | 20.100 / 39.650 | 2.900 ± 0.390 | — | 8.900 | — | 3.350 | 0.046 | 4.800 | — | 1902.800 | 0.018 | — | 0.000 / 0.000 (0.000 / 0.000) | 19282.271 ± 424.603 | — | 29684.6 ± 609.8 | — | 37.927 | — | 14.167 ± 0.344 | — | 16.820 | 0.001 | 2638.000 | 19.650 | 19.550 | — | 1013.908 | 686.050 |
| stamper | 4.450 / 39.950 | 9.400 ± 0.559 | +6.500 ± 0.796 | 95.700 | +86.800 ± 2.057 | 0.000 | 1.000 | 50.850 | +46.050 ± 1.688 | 848.850 | 0.195 | +0.177 ± 0.003 | 0.000 / 0.000 (0.000 / 0.000) | 6792.219 ± 170.408 | -12490.052 ± 451.089 | 6557.9 ± 267.2 | -23126.7 ± 599.0 | 28.583 | -9.345 ± 0.524 | 28.163 ± 1.131 | +13.996 ± 1.073 | 21.432 | 0.212 | 703.450 | 19.950 | 35.500 | +15.950 ± 0.535 | 6187.613 | 1197.450 |
| claimer | 4.400 / 39.800 | 9.350 ± 0.519 | +6.450 ± 0.651 | 99.400 | +90.500 ± 2.083 | 0.000 | 1.000 | 54.900 | +50.100 ± 1.767 | 848.650 | 0.196 | +0.179 ± 0.003 | 0.000 / 0.000 (0.000 / 0.000) | 5910.063 ± 149.252 | -13372.208 ± 490.241 | 8689.6 ± 210.8 | -20995.0 ± 636.0 | 27.651 | -10.277 ± 0.511 | 25.541 ± 0.654 | +11.374 ± 0.677 | 20.106 | 0.246 | 670.650 | 19.800 | 35.400 | +15.850 ± 0.595 | 6067.455 | 1151.700 |
| hand | 17.600 / 39.750 | 3.150 ± 0.499 | +0.250 ± 0.644 | 50.000 | +41.100 ± 1.901 | 7.100 | 0.053 | 11.000 | +6.200 ± 0.826 | 1934.850 | 0.037 | +0.019 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 25486.408 ± 304.942 | +6204.137 ± 408.614 | 28265.0 ± 567.5 | -1419.7 ± 623.3 | 32.413 | -5.514 ± 0.470 | 20.219 ± 0.487 | +6.052 ± 0.456 | 19.098 | 0.010 | 2461.050 | 19.750 | 22.150 | +2.600 ± 0.351 | 70.576 | 1058.650 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **direct**: p0 0.984/0.016/0.000 (499); p1 0.969/0.029/0.002 (331); p2 0.951/0.047/0.002 (246); p3 0.963/0.035/0.002 (203); p4 0.977/0.022/0.001 (179); p5 0.987/0.013/0.000 (176); p6 0.990/0.008/0.001 (172); p7 0.984/0.014/0.001 (177); p8 0.992/0.007/0.001 (177); p9 0.987/0.012/0.001 (175); p10 0.992/0.007/0.001 (171); p11 0.992/0.007/0.001 (154); p12 0.994/0.006/0.000 (108); p13 0.994/0.006/0.000 (65); p14 0.990/0.010/0.000 (19)
- **careful**: p0 1.000/0.000/0.000 (557); p1 1.000/0.000/0.000 (534); p2 1.000/0.000/0.000 (542); p3 1.000/0.000/0.000 (541); p4 1.000/0.000/0.000 (547); p5 1.000/0.000/0.000 (175); p6 1.000/0.000/0.000 (2)
- **stamper**: p0 0.000/1.000/0.000 (538); p1 0.000/1.000/0.000 (306); p2 0.000/1.000/0.000 (123); p3 0.000/1.000/0.000 (7); p4 0.000/1.000/0.000 (0)
- **claimer**: p0 —/—/— (0); p1 —/—/— (0); p2 —/—/— (0); p3 —/—/— (0); p4 —/—/— (0)
- **hand**: p0 —/—/— (0); p1 —/—/— (0); p2 —/—/— (0); p3 —/—/— (0); p4 —/—/— (0); p5 —/—/— (0); p6 —/—/— (0); p7 —/—/— (0); p8 —/—/— (0); p9 —/—/— (0); p10 —/—/— (0); p11 —/—/— (0); p12 —/—/— (0); p13 —/—/— (0); p14 —/—/— (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 2512.1 / 643.2 | 0.51 / 0.48 | -0.04 ± 0.04 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.16 / 0.12 | -0.04 ± 0.00 | 0.265 / 0.258 | -0.007 ± 0.009 | 0.124 / 0.138 | 0.006 / 0.000 | 0.098 / 0.115 | +0.017 ± 0.005 | 2.28 / 2.18 | -0.10 ± 0.08 |
| careful | 2633.4 / 263.9 | 0.18 / 0.10 | -0.09 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.11 / 0.12 | +0.01 ± 0.00 | 0.111 / 0.090 | -0.021 ± 0.005 | 0.041 / 0.044 | 0.001 / 0.000 | 0.060 / 0.067 | +0.007 ± 0.003 | 1.56 / 1.34 | -0.23 ± 0.07 |
| stamper | 845.2 / 130.2 | 0.73 / 0.45 | -0.28 ± 0.05 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.38 / 0.30 | -0.08 ± 0.01 | 0.144 / 0.114 | -0.030 ± 0.012 | 0.074 / 0.061 | 0.176 / 0.000 | 0.088 / 0.070 | -0.018 ± 0.004 | 3.34 / 2.09 | -1.25 ± 0.20 |
| claimer | 845.8 / 131.3 | 1.01 / 0.68 | -0.33 ± 0.06 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.37 / 0.27 | -0.10 ± 0.01 | 0.253 / 0.221 | -0.032 ± 0.011 | 0.123 / 0.108 | 0.214 / 0.000 | 0.109 / 0.076 | -0.033 ± 0.006 | 4.05 / 2.70 | -1.35 ± 0.24 |
| hand | 2477.8 / 606.5 | 0.68 / 0.64 | -0.05 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.16 / 0.12 | -0.04 ± 0.00 | 0.337 / 0.320 | -0.017 ± 0.007 | 0.151 / 0.149 | 0.010 / 0.000 | 0.111 / 0.122 | +0.011 ± 0.003 | 2.51 / 2.38 | -0.12 ± 0.07 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| direct | -0.07 ± 0.02 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.045 ± 0.004 | -0.013 ± 0.004 | -0.003 ± 0.004 |
| careful | -0.09 ± 0.02 | +0.00 ± 0.00 | +0.01 ± 0.00 | -0.023 ± 0.005 | +0.003 ± 0.003 | +0.007 ± 0.003 |
| stamper | -0.65 ± 0.08 | +0.00 ± 0.00 | -0.02 ± 0.01 | -0.127 ± 0.022 | -0.072 ± 0.013 | -0.032 ± 0.006 |
| claimer | -0.74 ± 0.08 | +0.00 ± 0.00 | -0.03 ± 0.01 | -0.157 ± 0.014 | -0.093 ± 0.011 | -0.047 ± 0.007 |
| hand | -0.09 ± 0.02 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.055 ± 0.003 | -0.019 ± 0.003 | -0.001 ± 0.003 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| direct | 0.002 / 0.000 | 0.39 / — | 0.035 / 0.000 | 0.00 / — | — / — | 0.966 / 0.000 |
| careful | 0.000 / 0.000 | 0.00 / — | 0.038 / 0.000 | 0.00 / — | — / — | 0.883 / 0.000 |
| stamper | 0.000 / 0.000 | — / — | 0.000 / 0.000 | — / — | — / — | 1.267 / 0.000 |
| claimer | 0.000 / 0.000 | — / — | 0.000 / 0.000 | — / — | — / — | 1.270 / 0.000 |
| hand | 0.003 / 0.000 | 0.52 / — | 0.035 / 0.000 | 0.00 / — | — / — | 0.952 / 0.000 |

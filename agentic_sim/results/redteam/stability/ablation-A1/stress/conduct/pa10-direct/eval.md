# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1 --pi-a0 0.10 --pi-a-max 0.10`, seeds 21-60, hide ``, model `None` (value off, horizon 8)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:direct:0.25 | 33486.3 ± 362.3 | -2208.2 ± 636.7 | 5045.6 | 0.940 | 0.015 | 0.014 | 0.093 | 0.095 | 0.404 | 0.010 | 4.40 | 36.92 | 0.33 |
| mix:direct:0.75 | 31580.6 ± 399.2 | -4113.9 ± 600.5 | 4734.8 | 0.808 | 0.052 | 0.034 | 0.263 | 0.259 | 0.355 | 0.064 | 10.35 | 106.60 | 0.53 |
| careful | 35694.5 ± 562.1 | nan ± nan | 4595.5 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.381 | 0.000 | 2.55 | 0.00 | 0.20 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:direct:0.25 | 0.093 (18757) [rej. blind 0.023] / 0.095 (101494) [rej. blind 0.023] | 0.008 (9382) [rej. blind 0.002] / 0.010 (51776) [rej. blind 0.002] | 0.008 (9134) [rej. blind 0.003] / 0.008 (11279) [rej. blind 0.002] | — / — |
| mix:direct:0.75 | 0.263 (27250) [rej. blind 0.049] / 0.259 (94841) [rej. blind 0.045] | 0.058 (10433) [rej. blind 0.011] / 0.070 (37800) [rej. blind 0.013] | 0.052 (9306) [rej. blind 0.010] / 0.059 (9760) [rej. blind 0.014] | — / — |
| careful | 0.000 (10503) / 0.000 (103317) | 0.000 (6289) / 0.000 (49205) | 0.000 (6363) / 0.000 (8143) | — / — |

The stressed world's fourth action by seat kind — the allowance claimed and the verdict F without inspecting (counted above among the blind verdicts; the ledger sees a careful review, so the measured reading below cannot see it):

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:direct:0.25 | 0.047 (18757) / 0.048 (101494) | 0.003 (9382) / 0.006 (51776) | 0.002 (9134) / 0.003 (11279) | — / — |
| mix:direct:0.75 | 0.147 (27250) / 0.142 (94841) | 0.031 (10433) / 0.041 (37800) | 0.026 (9306) / 0.029 (9760) | — / — |
| careful | 0.000 (10503) / 0.000 (103317) | 0.000 (6289) / 0.000 (49205) | 0.000 (6363) / 0.000 (8143) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| mix:direct:0.25 | 0.046 (18757) [rej. blind 0.023] / 0.047 (101494) [rej. blind 0.023] | 0.005 (9382) [rej. blind 0.002] / 0.005 (51776) [rej. blind 0.002] | 0.006 (9134) [rej. blind 0.003] / 0.005 (11279) [rej. blind 0.002] | — / — | 3.1 ± 0.4 | -6121 |
| mix:direct:0.75 | 0.116 (27250) [rej. blind 0.049] / 0.117 (94841) [rej. blind 0.045] | 0.027 (10433) [rej. blind 0.011] / 0.029 (37800) [rej. blind 0.013] | 0.026 (9306) [rej. blind 0.010] / 0.030 (9760) [rej. blind 0.014] | — / — | 1.9 ± 0.2 | -19833 |
| careful | 0.000 (10503) [rej. blind 0.000] / 0.000 (103317) [rej. blind 0.000] | 0.000 (6289) / 0.000 (49205) | 0.000 (6363) / 0.000 (8143) | — / — | 2.6 ± 0.3 | +13 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:direct:0.25 | 1.000 | 0.971 | — (0) | — (0) | 0.000 (10751) | 0.000 (6929) | 0.017 (184142) | 10.450 | 499.125 | 1.252 | 3.533 |
| mix:direct:0.75 | 1.000 | 0.999 | — (0) | — (0) | 0.000 (220) | 0.005 (214) | 0.052 (188956) | 15.850 | 362.800 | 1.434 | 6.726 |
| careful | — | 0.911 | — (0) | — (0) | 0.000 (33138) | 0.000 (1109) | 0.000 (149573) | 4.725 | 678.650 | 1.183 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| mix:direct:0.25 | 39.725 | 0.000 | 0.000 | 0.000 | 0.000 | 0.325 | 0.000 |
| mix:direct:0.75 | 39.750 | 0.000 | 0.000 | 0.000 | 0.000 | 0.525 | 0.000 |
| careful | 39.675 | 0.000 | 0.000 | 0.000 | 0.000 | 0.200 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:direct:0.25 | 21.100 / 39.725 | 4.400 ± 0.370 | +1.850 ± 0.428 | 41.125 | +30.800 ± 3.660 | 8.775 | 0.107 | 10.450 | +5.725 ± 0.567 | 1911.400 | 0.042 | +0.017 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 28857.197 ± 323.213 | +3666.553 ± 359.710 | 33486.3 ± 362.3 | -2208.2 ± 636.7 | 33.435 | -2.544 ± 0.298 | 19.035 ± 0.294 | +3.925 ± 0.397 | 18.990 | 0.002 | 2543.300 | 19.725 | 18.625 | +2.250 ± 0.390 | 125.463 | 198.825 |
| mix:direct:0.75 | 17.675 / 39.750 | 10.350 ± 0.571 | +7.800 ± 0.654 | 127.775 | +117.450 ± 3.204 | 14.875 | 0.299 | 15.850 | +11.125 ± 0.609 | 1844.775 | 0.071 | +0.047 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 29363.389 ± 265.043 | +4172.745 ± 350.305 | 31580.6 ± 399.2 | -4113.9 ± 600.5 | 31.043 | -4.936 ± 0.278 | 21.677 ± 0.250 | +6.566 ± 0.349 | 19.694 | 0.025 | 2322.175 | 19.750 | 22.075 | +5.700 ± 0.302 | 70.361 | 195.325 |
| careful | 23.300 / 39.675 | 2.550 ± 0.277 | — | 10.325 | — | 3.150 | 0.057 | 4.725 | — | 1887.250 | 0.025 | — | 0.000 / 0.000 (0.000 / 0.000) | 25190.644 ± 294.399 | — | 35694.5 ± 562.1 | — | 35.979 | — | 15.111 ± 0.293 | — | 18.104 | 0.002 | 2585.700 | 19.675 | 16.375 | — | 660.690 | 211.575 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **mix:direct:0.25**: p0 0.962/0.029/0.010 (572); p1 0.950/0.032/0.018 (628); p2 0.973/0.007/0.020 (613); p3 0.962/0.013/0.025 (627); p4 0.967/0.010/0.023 (580); p5 0.977/0.010/0.012 (483); p6 0.977/0.013/0.010 (358); p7 0.980/0.014/0.006 (318); p8 0.984/0.013/0.003 (263); p9 0.986/0.010/0.004 (186); p10 0.984/0.013/0.003 (127); p11 0.993/0.007/0.000 (73); p12 0.984/0.010/0.006 (40); p13 0.960/0.034/0.006 (21); p14 1.000/0.000/0.000 (5)
- **mix:direct:0.75**: p0 0.870/0.101/0.028 (518); p1 0.860/0.070/0.070 (355); p2 0.887/0.046/0.067 (296); p3 0.899/0.052/0.049 (279); p4 0.899/0.055/0.046 (295); p5 0.900/0.044/0.055 (296); p6 0.863/0.074/0.063 (296); p7 0.902/0.059/0.040 (289); p8 0.936/0.041/0.023 (288); p9 0.943/0.045/0.012 (290); p10 0.953/0.039/0.008 (287); p11 0.937/0.047/0.015 (277); p12 0.937/0.047/0.017 (236); p13 0.929/0.042/0.028 (189); p14 0.918/0.050/0.032 (48)
- **careful**: p0 1.000/0.000/0.000 (605); p1 1.000/0.000/0.000 (731); p2 1.000/0.000/0.000 (903); p3 1.000/0.000/0.000 (1015); p4 1.000/0.000/0.000 (1021); p5 1.000/0.000/0.000 (293); p6 1.000/0.000/0.000 (27); p7 1.000/0.000/0.000 (1)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:direct:0.25 | 2537.3 / 468.9 | 0.46 / 0.39 | -0.07 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.13 / 0.15 | +0.02 ± 0.00 | 0.288 / 0.263 | -0.025 ± 0.005 | 0.119 / 0.127 | 0.002 / 0.000 | 0.071 / 0.067 | -0.003 ± 0.003 | 2.02 / 1.92 | -0.09 ± 0.06 |
| mix:direct:0.75 | 2371.0 / 681.2 | 1.08 / 1.21 | +0.14 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.08 / 0.08 | -0.00 ± 0.00 | 0.432 / 0.456 | +0.024 ± 0.004 | 0.232 / 0.266 | 0.025 / 0.000 | 0.125 / 0.138 | +0.013 ± 0.002 | 2.97 / 3.10 | +0.14 ± 0.04 |
| careful | 2582.9 / 262.6 | 0.33 / 0.23 | -0.10 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.13 / 0.12 | -0.01 ± 0.00 | 0.181 / 0.155 | -0.026 ± 0.004 | 0.075 / 0.086 | 0.002 / 0.000 | 0.058 / 0.052 | -0.005 ± 0.002 | 1.88 / 1.54 | -0.34 ± 0.06 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| mix:direct:0.25 | -0.08 ± 0.01 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.052 ± 0.004 | -0.009 ± 0.003 | -0.004 ± 0.003 |
| mix:direct:0.75 | -0.04 ± 0.01 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.051 ± 0.002 | -0.013 ± 0.002 | +0.002 ± 0.002 |
| careful | -0.09 ± 0.01 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.027 ± 0.004 | +0.010 ± 0.002 | -0.005 ± 0.002 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| mix:direct:0.25 | 0.502 / 0.216 | 0.24 / 0.22 | 0.054 / 0.144 | 0.00 / 0.00 | 0.28 / 0.26 | 0.309 / 0.201 |
| mix:direct:0.75 | 0.392 / 0.244 | 0.44 / 0.45 | 0.063 / 0.119 | 0.00 / 0.00 | 0.46 / 0.49 | 0.493 / 0.350 |
| careful | 0.470 / 0.139 | 0.30 / 0.31 | 0.040 / 0.164 | 0.00 / 0.00 | 0.29 / 0.32 | 0.309 / 0.259 |

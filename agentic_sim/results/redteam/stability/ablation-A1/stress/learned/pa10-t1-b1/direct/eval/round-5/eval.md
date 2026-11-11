# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --pi-a0 0.10 --pi-a-max 0.10 --temptation 1 --bond-mult-later 1`, seeds 21-40, hide ``, model `None` (value off, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 30315.2 ± 499.4 | -5187.1 ± 893.2 | 3426.8 | 0.651 | 0.009 | 0.013 | 0.206 | 0.285 | 0.138 | 0.867 | 27.65 | 151.85 | 0.10 |
| careful | 35502.3 ± 852.9 | nan ± nan | 4637.9 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.384 | 0.000 | 2.55 | 0.00 | 0.30 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| direct | 0.206 (13700) [rej. blind 0.001] / 0.285 (45345) [rej. blind 0.001] | 0.800 (1533) [rej. blind 0.039] / 0.939 (6325) [rej. blind 0.000] | 0.592 (637) [rej. blind 0.411] / 0.683 (995) [rej. blind 0.513] | — / — |
| careful | 0.000 (5284) / 0.000 (51900) | 0.000 (3178) / 0.000 (24974) | 0.000 (3248) / 0.000 (4174) | — / — |

The stressed world's fourth action by seat kind — the allowance claimed and the verdict F without inspecting (counted above among the blind verdicts; the ledger sees a careful review, so the measured reading below cannot see it):

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| direct | 0.197 (13700) / 0.275 (45345) | 0.752 (1533) / 0.924 (6325) | 0.176 (637) / 0.168 (995) | — / — |
| careful | 0.000 (5284) / 0.000 (51900) | 0.000 (3178) / 0.000 (24974) | 0.000 (3248) / 0.000 (4174) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| direct | 0.009 (13700) [rej. blind 0.001] / 0.010 (45345) [rej. blind 0.001] | 0.048 (1533) [rej. blind 0.039] / 0.015 (6325) [rej. blind 0.000] | 0.416 (637) [rej. blind 0.411] / 0.516 (995) [rej. blind 0.513] | — / — | 1.2 ± 0.3 | -22421 |
| careful | 0.000 (5284) [rej. blind 0.000] / 0.000 (51900) [rej. blind 0.000] | 0.000 (3178) / 0.000 (24974) | 0.000 (3248) / 0.000 (4174) | — / — | 2.2 ± 0.3 | +7 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 1.000 | 1.000 | — (0) | — (0) | 0.000 (16) | — (0) | 0.009 (68519) | 42.250 | 251.650 | 1.667 | 3.594 |
| careful | — | 0.910 | — (0) | — (0) | 0.000 (16686) | 0.000 (779) | 0.000 (75293) | 24.350 | 668.700 | 1.190 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| direct | 39.750 | 0.000 | 0.000 | 0.000 | 0.000 | 0.100 | 0.000 |
| careful | 39.750 | 0.000 | 0.000 | 0.000 | 0.000 | 0.300 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 18.700 / 39.750 | 27.650 ± 1.230 | +25.100 ± 1.287 | 126.200 | +116.100 ± 2.639 | 6.000 | 0.253 | 22.500 | +17.900 ± 0.739 | 1873.850 | 0.077 | +0.052 ± 0.002 | 0.000 / 0.000 (0.000 / 0.000) | 27037.607 ± 440.712 | +2102.958 ± 609.340 | 30315.2 ± 499.4 | -5187.1 ± 893.2 | 29.611 | -6.619 ± 0.504 | 21.275 ± 0.245 | +6.177 ± 0.600 | 20.019 | 0.033 | 2198.150 | 19.750 | 21.050 | +4.250 ± 0.532 | 67.996 | 77.050 |
| careful | 22.950 / 39.750 | 2.550 ± 0.438 | — | 10.100 | — | 3.250 | 0.053 | 4.600 | — | 1896.050 | 0.025 | — | 0.000 / 0.000 (0.000 / 0.000) | 24934.650 ± 445.425 | — | 35502.3 ± 852.9 | — | 36.230 | — | 15.098 ± 0.513 | — | 17.953 | 0.001 | 2599.400 | 19.750 | 16.800 | — | 689.070 | 188.600 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **direct**: p0 0.995/0.004/0.001 (327); p1 0.922/0.022/0.056 (187); p2 0.962/0.018/0.019 (179); p3 0.922/0.051/0.027 (170); p4 0.934/0.032/0.034 (149); p5 0.969/0.017/0.015 (148); p6 0.971/0.012/0.017 (156); p7 0.977/0.008/0.015 (150); p8 0.983/0.006/0.012 (154); p9 0.980/0.005/0.015 (152); p10 0.982/0.006/0.013 (150); p11 0.975/0.004/0.021 (147); p12 0.979/0.001/0.020 (144); p13 0.967/0.002/0.031 (87); p14 0.978/0.000/0.022 (4)
- **careful**: p0 1.000/0.000/0.000 (605); p1 1.000/0.000/0.000 (751); p2 1.000/0.000/0.000 (913); p3 1.000/0.000/0.000 (1021); p4 1.000/0.000/0.000 (1014); p5 1.000/0.000/0.000 (292); p6 1.000/0.000/0.000 (40); p7 1.000/0.000/0.000 (2)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 2267.2 / 685.0 | 1.43 / 1.84 | +0.41 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.04 / 0.02 | -0.01 ± 0.00 | 0.523 / 0.604 | +0.081 ± 0.005 | 0.306 / 0.370 | 0.033 / 0.000 | 0.175 / 0.214 | +0.038 ± 0.004 | 3.12 / 3.43 | +0.30 ± 0.04 |
| careful | 2595.0 / 264.2 | 0.28 / 0.20 | -0.08 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.13 / 0.12 | -0.01 ± 0.00 | 0.170 / 0.144 | -0.025 ± 0.006 | 0.068 / 0.078 | 0.001 / 0.000 | 0.056 / 0.051 | -0.005 ± 0.004 | 1.75 / 1.49 | -0.26 ± 0.06 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| direct | +0.07 ± 0.02 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.042 ± 0.004 | -0.016 ± 0.003 | +0.011 ± 0.004 |
| careful | -0.08 ± 0.02 | +0.00 ± 0.00 | -0.01 ± 0.01 | -0.024 ± 0.005 | +0.011 ± 0.004 | -0.004 ± 0.004 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| direct | 0.138 / 0.074 | 0.58 / 0.61 | 0.029 / 0.074 | 0.00 / 0.00 | 0.63 / 0.64 | 0.808 / 0.610 |
| careful | 0.474 / 0.137 | 0.30 / 0.31 | 0.040 / 0.162 | 0.00 / 0.00 | 0.28 / 0.31 | 0.302 / 0.280 |

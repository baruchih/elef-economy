# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --pi-a0 0.20 --pi-a-max 0.20`, seeds 21-40, hide ``, model `None` (value off, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 34110.1 ± 812.6 | -1093.6 ± 876.1 | 4790.6 | 0.939 | 0.038 | 0.023 | 0.017 | 0.020 | 0.398 | 0.123 | 6.45 | 11.90 | 0.25 |
| careful | 35203.7 ± 703.1 | nan ± nan | 4876.6 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.412 | 0.000 | 2.40 | 0.00 | 0.30 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| direct | 0.017 (5415) [rej. blind 0.001] / 0.020 (52274) [rej. blind 0.001] | 0.095 (5422) [rej. blind 0.040] / 0.090 (23848) [rej. blind 0.004] | 0.258 (4925) [rej. blind 0.223] / 0.192 (3928) [rej. blind 0.182] | — / — |
| careful | 0.000 (5235) / 0.000 (52115) | 0.000 (5650) / 0.000 (25027) | 0.000 (5371) / 0.000 (4134) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| direct | 0.018 (5415) [rej. blind 0.002] / 0.020 (52274) [rej. blind 0.001] | 0.095 (5422) [rej. blind 0.040] / 0.090 (23848) [rej. blind 0.004] | 0.258 (4925) [rej. blind 0.223] / 0.192 (3928) [rej. blind 0.182] | — / — | 2.2 ± 0.4 | +8 |
| careful | 0.000 (5235) [rej. blind 0.000] / 0.000 (52115) [rej. blind 0.000] | 0.000 (5650) / 0.000 (25027) | 0.000 (5371) / 0.000 (4134) | — / — | 2.6 ± 0.5 | +5 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 0.843 | 0.921 | — (0) | — (0) | 0.072 (16152) | 0.061 (683) | 0.031 (78977) | 25.050 | 689.450 | 1.190 | 0.475 |
| careful | — | 0.908 | — (0) | — (0) | 0.000 (18247) | 0.000 (249) | 0.000 (79036) | 24.900 | 675.700 | 1.182 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| direct | 39.750 | 0.000 | 0.000 | 0.000 | 0.000 | 0.250 | 0.000 |
| careful | 39.550 | 0.000 | 0.000 | 0.000 | 0.000 | 0.300 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 24.200 / 39.750 | 6.450 ± 0.663 | +4.050 ± 0.734 | 13.300 | +3.150 ± 0.993 | 3.700 | 0.083 | 5.300 | -0.050 ± 0.783 | 1923.700 | 0.035 | +0.011 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 26034.147 ± 337.097 | +431.348 ± 363.381 | 34110.1 ± 812.6 | -1093.6 ± 876.1 | 35.413 | -0.852 ± 0.383 | 16.508 ± 0.381 | +0.952 ± 0.519 | 18.724 | 0.001 | 2617.850 | 19.750 | 15.550 | +0.000 ± 0.553 | 466.154 | 270.500 |
| careful | 24.000 / 39.550 | 2.400 ± 0.294 | — | 10.150 | — | 3.150 | 0.043 | 5.350 | — | 1905.300 | 0.024 | — | 0.000 / 0.000 (0.000 / 0.000) | 25602.799 ± 389.383 | — | 35203.7 ± 703.1 | — | 36.265 | — | 15.556 ± 0.334 | — | 17.880 | 0.001 | 2612.750 | 19.550 | 15.550 | — | 650.960 | 198.600 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **direct**: p0 0.962/0.037/0.001 (590); p1 0.907/0.056/0.037 (722); p2 0.930/0.042/0.028 (900); p3 0.939/0.033/0.028 (1038); p4 0.958/0.027/0.015 (1061); p5 0.936/0.042/0.022 (448); p6 0.924/0.039/0.036 (30)
- **careful**: p0 1.000/0.000/0.000 (596); p1 1.000/0.000/0.000 (796); p2 1.000/0.000/0.000 (1019); p3 1.000/0.000/0.000 (1083); p4 1.000/0.000/0.000 (1070); p5 1.000/0.000/0.000 (313)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 2613.7 / 270.8 | 0.31 / 0.19 | -0.12 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.11 / 0.11 | -0.00 ± 0.00 | 0.208 / 0.175 | -0.033 ± 0.006 | 0.080 / 0.089 | 0.001 / 0.000 | 0.057 / 0.053 | -0.004 ± 0.002 | 1.73 / 1.47 | -0.26 ± 0.10 |
| careful | 2605.8 / 261.8 | 0.24 / 0.15 | -0.10 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.12 / 0.12 | -0.01 ± 0.01 | 0.178 / 0.149 | -0.029 ± 0.005 | 0.069 / 0.074 | 0.001 / 0.000 | 0.053 / 0.054 | +0.000 ± 0.003 | 1.61 / 1.23 | -0.37 ± 0.08 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| direct | -0.11 ± 0.02 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.033 ± 0.006 | +0.009 ± 0.003 | -0.003 ± 0.002 |
| careful | -0.10 ± 0.02 | +0.00 ± 0.00 | -0.01 ± 0.01 | -0.027 ± 0.004 | +0.006 ± 0.005 | +0.001 ± 0.003 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| direct | 0.449 / 0.139 | 0.36 / 0.38 | 0.039 / 0.158 | 0.00 / 0.00 | 0.35 / 0.33 | 0.337 / 0.340 |
| careful | 0.474 / 0.143 | 0.34 / 0.36 | 0.041 / 0.158 | 0.00 / 0.00 | 0.32 / 0.35 | 0.305 / 0.315 |

# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule`, seeds 21-40, hide ``, model `None` (value off, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 35046.6 ± 661.9 | -330.0 ± 957.4 | 4379.1 | 0.809 | 0.185 | 0.005 | 0.026 | 0.034 | 0.338 | 0.500 | 18.15 | 31.05 | 0.45 |
| careful | 35376.6 ± 1021.8 | nan ± nan | 4380.3 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.354 | 0.000 | 2.65 | 0.00 | 0.40 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| direct | 0.026 (5470) [rej. blind 0.001] / 0.034 (52551) [rej. blind 0.000] | 0.456 (1593) [rej. blind 0.001] / 0.567 (23531) [rej. blind 0.001] | 0.219 (1357) [rej. blind 0.077] / 0.139 (3081) [rej. blind 0.110] | — / — |
| careful | 0.000 (5215) / 0.000 (51338) | 0.000 (1198) / 0.000 (24402) | 0.000 (1502) / 0.000 (3951) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| direct | 0.027 (5470) [rej. blind 0.001] / 0.034 (52551) [rej. blind 0.000] | 0.456 (1593) [rej. blind 0.001] / 0.567 (23531) [rej. blind 0.001] | 0.219 (1357) [rej. blind 0.077] / 0.139 (3081) [rej. blind 0.110] | — / — | 3.4 ± 0.5 | +10 |
| careful | 0.000 (5215) [rej. blind 0.000] / 0.000 (51338) | 0.000 (1198) / 0.000 (24402) | 0.000 (1502) / 0.000 (3951) | — / — | 2.6 ± 0.4 | +8 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 0.804 | 0.932 | — (0) | — (0) | 0.402 (15890) | 0.171 (1537) | 0.136 (70156) | 4.650 | 704.250 | 1.150 | 6.677 |
| careful | — | 0.919 | — (0) | — (0) | 0.000 (14115) | 0.000 (862) | 0.000 (72629) | 5.450 | 714.900 | 1.186 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| direct | 39.750 | 0.000 | 0.000 | 0.000 | 0.000 | 0.450 | 0.000 |
| careful | 39.700 | 0.000 | 0.000 | 0.000 | 0.000 | 0.400 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 23.350 / 39.750 | 18.150 ± 1.182 | +15.500 ± 1.099 | 13.850 | +3.150 ± 1.190 | 3.400 | 0.111 | 4.650 | -0.800 ± 0.526 | 1948.550 | 0.024 | -0.002 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 25337.936 ± 483.588 | +256.173 ± 591.489 | 35046.6 ± 661.9 | -330.0 ± 957.4 | 36.557 | +1.076 ± 0.561 | 15.469 ± 0.363 | +0.200 ± 0.600 | 18.223 | 0.000 | 2633.350 | 19.750 | 16.400 | +0.100 ± 0.538 | 720.183 | 247.350 |
| careful | 23.400 / 39.700 | 2.650 ± 0.412 | — | 10.700 | — | 3.500 | 0.046 | 5.450 | — | 1882.600 | 0.026 | — | 0.000 / 0.000 (0.000 / 0.000) | 25081.763 ± 393.915 | — | 35376.6 ± 1021.8 | — | 35.481 | — | 15.269 ± 0.468 | — | 18.472 | 0.010 | 2551.650 | 19.700 | 16.300 | — | 610.512 | 256.100 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **direct**: p0 0.945/0.052/0.002 (602); p1 0.793/0.197/0.010 (728); p2 0.785/0.209/0.006 (826); p3 0.750/0.245/0.005 (904); p4 0.791/0.206/0.002 (924); p5 0.859/0.131/0.010 (362); p6 0.886/0.107/0.007 (34)
- **careful**: p0 1.000/0.000/0.000 (597); p1 1.000/0.000/0.000 (719); p2 1.000/0.000/0.000 (854); p3 1.000/0.000/0.000 (954); p4 1.000/0.000/0.000 (961); p5 1.000/0.000/0.000 (294); p6 1.000/0.000/0.000 (1)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 2627.6 / 273.5 | 0.22 / 0.14 | -0.09 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.08 / 0.08 | +0.00 ± 0.00 | 0.165 / 0.130 | -0.035 ± 0.005 | 0.059 / 0.063 | 0.000 / 0.000 | 0.057 / 0.056 | -0.001 ± 0.004 | 1.45 / 1.22 | -0.23 ± 0.06 |
| careful | 2566.9 / 260.8 | 0.43 / 0.30 | -0.13 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.11 / 0.11 | -0.00 ± 0.00 | 0.196 / 0.164 | -0.032 ± 0.006 | 0.082 / 0.085 | 0.010 / 0.000 | 0.058 / 0.060 | +0.002 ± 0.003 | 2.07 / 1.63 | -0.45 ± 0.16 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| direct | -0.08 ± 0.01 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.034 ± 0.004 | +0.005 ± 0.003 | -0.001 ± 0.004 |
| careful | -0.13 ± 0.02 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.032 ± 0.006 | +0.002 ± 0.003 | +0.002 ± 0.003 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| direct | 0.442 / 0.140 | 0.45 / 0.42 | 0.038 / 0.163 | 0.00 / 0.00 | 0.44 / 0.48 | 0.352 / 0.293 |
| careful | 0.468 / 0.130 | 0.31 / 0.33 | 0.039 / 0.164 | 0.00 / 0.00 | 0.29 / 0.31 | 0.313 / 0.261 |

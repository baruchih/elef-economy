# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --pi-max 0.10`, seeds 21-40, hide ``, model `None` (value off, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 34150.9 ± 799.9 | -476.7 ± 830.3 | 4283.9 | 0.837 | 0.157 | 0.006 | 0.021 | 0.022 | 0.328 | 0.451 | 13.65 | 21.45 | 0.55 |
| careful | 34627.6 ± 839.5 | nan ± nan | 4376.9 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.354 | 0.000 | 2.80 | 0.00 | 0.30 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| direct | 0.021 (5181) [rej. blind 0.003] / 0.022 (52410) [rej. blind 0.000] | 0.424 (1401) [rej. blind 0.004] / 0.506 (22453) [rej. blind 0.001] | 0.209 (1249) [rej. blind 0.078] / 0.152 (2983) [rej. blind 0.106] | — / — |
| careful | 0.000 (5097) / 0.000 (51495) | 0.000 (1163) / 0.000 (24391) | 0.000 (1465) / 0.000 (3927) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| direct | 0.021 (5181) [rej. blind 0.003] / 0.022 (52410) [rej. blind 0.000] | 0.424 (1401) [rej. blind 0.004] / 0.506 (22453) [rej. blind 0.001] | 0.209 (1249) [rej. blind 0.078] / 0.152 (2983) [rej. blind 0.106] | — / — | 2.1 ± 0.4 | +3 |
| careful | 0.000 (5097) [rej. blind 0.000] / 0.000 (51495) | 0.000 (1163) / 0.000 (24391) | 0.000 (1465) / 0.000 (3927) | — / — | 2.9 ± 0.3 | +8 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 0.807 | 0.943 | — (0) | — (0) | 0.384 (13247) | 0.319 (2255) | 0.109 (70175) | 26.200 | 734.300 | 1.223 | 0.819 |
| careful | — | 0.917 | — (0) | — (0) | 0.000 (14626) | 0.000 (730) | 0.000 (72182) | 24.850 | 709.950 | 1.174 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| direct | 39.550 | 0.000 | 0.000 | 0.000 | 0.000 | 0.550 | 0.000 |
| careful | 39.700 | 0.000 | 0.000 | 0.000 | 0.000 | 0.300 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 23.000 / 39.550 | 13.650 ± 0.998 | +10.850 ± 0.874 | 12.650 | +2.750 ± 0.986 | 3.500 | 0.063 | 6.650 | +1.500 ± 0.605 | 1962.700 | 0.025 | +0.000 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 25222.682 ± 416.577 | +73.624 ± 605.324 | 34150.9 ± 799.9 | -476.7 ± 830.3 | 36.291 | +0.799 ± 0.547 | 15.912 ± 0.403 | +0.233 ± 0.630 | 18.321 | 0.001 | 2624.950 | 19.550 | 16.550 | -0.600 ± 0.400 | 620.240 | 226.500 |
| careful | 22.550 / 39.700 | 2.800 ± 0.367 | — | 9.900 | — | 3.150 | 0.038 | 5.150 | — | 1881.650 | 0.025 | — | 0.000 / 0.000 (0.000 / 0.000) | 25149.058 ± 420.211 | — | 34627.6 ± 839.5 | — | 35.493 | — | 15.680 ± 0.563 | — | 18.444 | 0.008 | 2564.150 | 19.700 | 17.150 | — | 592.071 | 260.250 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **direct**: p0 0.955/0.043/0.002 (595); p1 0.835/0.159/0.006 (709); p2 0.766/0.228/0.006 (838); p3 0.780/0.214/0.006 (920); p4 0.872/0.125/0.004 (979); p5 0.880/0.103/0.017 (242)
- **careful**: p0 1.000/0.000/0.000 (597); p1 1.000/0.000/0.000 (727); p2 1.000/0.000/0.000 (872); p3 1.000/0.000/0.000 (981); p4 1.000/0.000/0.000 (995); p5 1.000/0.000/0.000 (205)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 2620.5 / 259.1 | 0.22 / 0.11 | -0.11 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.07 / 0.06 | -0.00 ± 0.00 | 0.156 / 0.125 | -0.030 ± 0.004 | 0.055 / 0.061 | 0.001 / 0.000 | 0.058 / 0.055 | -0.002 ± 0.003 | 1.62 / 1.13 | -0.49 ± 0.09 |
| careful | 2574.8 / 254.8 | 0.41 / 0.29 | -0.12 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.11 / 0.10 | -0.00 ± 0.00 | 0.191 / 0.161 | -0.030 ± 0.006 | 0.076 / 0.079 | 0.008 / 0.000 | 0.061 / 0.059 | -0.003 ± 0.003 | 2.04 / 1.50 | -0.54 ± 0.15 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| direct | -0.11 ± 0.02 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.030 ± 0.004 | +0.006 ± 0.004 | -0.002 ± 0.003 |
| careful | -0.12 ± 0.02 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.031 ± 0.006 | +0.002 ± 0.004 | -0.002 ± 0.003 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| direct | 0.423 / 0.131 | 0.47 / 0.48 | 0.038 / 0.171 | 0.00 / 0.00 | 0.45 / 0.48 | 0.383 / 0.343 |
| careful | 0.467 / 0.128 | 0.30 / 0.31 | 0.038 / 0.165 | 0.00 / 0.00 | 0.29 / 0.33 | 0.311 / 0.272 |

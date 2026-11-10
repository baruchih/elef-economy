# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --pi0 0.40`, seeds 21-40, hide ``, model `None` (value off, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 28435.7 ± 677.0 | -1391.6 ± 778.9 | 5806.8 | 0.917 | 0.076 | 0.007 | 0.006 | 0.007 | 0.406 | 0.194 | 9.55 | 8.70 | 0.40 |
| careful | 29827.2 ± 564.0 | nan ± nan | 5661.4 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.394 | 0.000 | 4.45 | 0.00 | 0.50 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| direct | 0.006 (19283) [rej. blind 0.001] / 0.007 (49684) [rej. blind 0.001] | 0.187 (6372) [rej. blind 0.001] / 0.227 (30533) [rej. blind 0.000] | 0.130 (5223) [rej. blind 0.077] / 0.072 (5041) [rej. blind 0.057] | — / — |
| careful | 0.000 (19185) / 0.000 (49430) | 0.000 (4675) / 0.000 (30455) | 0.000 (4059) / 0.000 (5423) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| direct | 0.006 (19283) [rej. blind 0.001] / 0.007 (49684) [rej. blind 0.001] | 0.187 (6372) [rej. blind 0.001] / 0.227 (30533) [rej. blind 0.000] | 0.130 (5223) [rej. blind 0.077] / 0.072 (5041) [rej. blind 0.057] | — / — | 4.5 ± 0.5 | +11 |
| careful | 0.000 (19185) [rej. blind 0.000] / 0.000 (49430) [rej. blind 0.000] | 0.000 (4675) / 0.000 (30455) | 0.000 (4059) / 0.000 (5423) | — / — | 4.3 ± 0.5 | +12 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 0.836 | 0.864 | — (0) | — (0) | 0.090 (31954) | 0.075 (2044) | 0.071 (82138) | 24.850 | 214.200 | 1.108 | 0.350 |
| careful | — | 0.859 | — (0) | — (0) | 0.000 (32333) | 0.000 (1537) | 0.000 (79357) | 24.950 | 201.750 | 1.098 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| direct | 39.950 | 0.000 | 0.000 | 0.000 | 0.000 | 0.400 | 0.000 |
| careful | 39.850 | 0.000 | 0.000 | 0.000 | 0.000 | 0.500 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 19.150 / 39.950 | 9.550 ± 0.671 | +5.100 ± 1.002 | 38.200 | +0.800 ± 1.796 | 11.600 | 0.049 | 4.900 | -0.200 ± 0.683 | 1679.350 | 0.023 | -0.001 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 34348.429 ± 370.438 | +1220.407 ± 573.781 | 28435.7 ± 677.0 | -1391.6 ± 778.9 | 32.714 | -0.085 ± 0.486 | 26.817 ± 0.817 | +2.651 ± 0.803 | 21.852 | 0.003 | 2497.950 | 19.950 | 20.800 | +0.500 ± 0.407 | 69.626 | 94.350 |
| careful | 19.550 / 39.850 | 4.450 ± 0.591 | — | 37.400 | — | 12.900 | 0.055 | 5.100 | — | 1658.700 | 0.024 | — | 0.000 / 0.000 (0.000 / 0.000) | 33128.022 ± 486.531 | — | 29827.2 ± 564.0 | — | 32.799 | — | 24.167 ± 0.431 | — | 21.255 | 0.003 | 2486.750 | 19.850 | 20.300 | — | 126.087 | 109.200 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **direct**: p0 0.952/0.043/0.005 (198); p1 0.865/0.123/0.012 (240); p2 0.863/0.135/0.003 (294); p3 0.787/0.212/0.002 (297); p4 0.851/0.146/0.003 (306); p5 0.846/0.151/0.003 (303); p6 0.877/0.117/0.005 (297); p7 0.886/0.111/0.002 (301); p8 0.914/0.082/0.003 (303); p9 0.911/0.084/0.005 (305); p10 0.935/0.062/0.003 (302); p11 0.947/0.051/0.003 (311); p12 0.951/0.045/0.004 (314); p13 0.955/0.035/0.009 (317); p14 0.963/0.031/0.006 (325); p15 0.966/0.020/0.014 (331); p16 0.972/0.016/0.012 (336); p17 0.968/0.017/0.014 (325); p18 0.972/0.017/0.010 (274); p19 0.966/0.014/0.020 (115); p20 0.957/0.014/0.028 (14)
- **careful**: p0 1.000/0.000/0.000 (198); p1 1.000/0.000/0.000 (255); p2 1.000/0.000/0.000 (299); p3 1.000/0.000/0.000 (307); p4 1.000/0.000/0.000 (309); p5 1.000/0.000/0.000 (304); p6 1.000/0.000/0.000 (307); p7 1.000/0.000/0.000 (299); p8 1.000/0.000/0.000 (300); p9 1.000/0.000/0.000 (306); p10 1.000/0.000/0.000 (306); p11 1.000/0.000/0.000 (302); p12 1.000/0.000/0.000 (299); p13 1.000/0.000/0.000 (310); p14 1.000/0.000/0.000 (302); p15 1.000/0.000/0.000 (304); p16 1.000/0.000/0.000 (313); p17 1.000/0.000/0.000 (308); p18 1.000/0.000/0.000 (228); p19 1.000/0.000/0.000 (92); p20 1.000/0.000/0.000 (13)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 2484.2 / 964.1 | 0.44 / 0.43 | -0.01 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.19 / 0.17 | -0.02 ± 0.00 | 0.214 / 0.191 | -0.023 ± 0.002 | 0.125 / 0.114 | 0.003 / 0.000 | 0.087 / 0.081 | -0.005 ± 0.002 | 2.27 / 2.23 | -0.03 ± 0.04 |
| careful | 2471.5 / 959.2 | 0.56 / 0.58 | +0.02 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.20 / 0.18 | -0.02 ± 0.00 | 0.309 / 0.281 | -0.028 ± 0.003 | 0.159 / 0.151 | 0.002 / 0.000 | 0.098 / 0.099 | +0.001 ± 0.002 | 2.38 / 2.39 | +0.01 ± 0.04 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| direct | -0.00 ± 0.01 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.020 ± 0.002 | -0.010 ± 0.002 | -0.005 ± 0.002 |
| careful | +0.02 ± 0.01 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.026 ± 0.003 | -0.007 ± 0.002 | +0.001 ± 0.002 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| direct | 0.607 / 0.212 | 0.09 / 0.09 | 0.040 / 0.080 | 0.00 / 0.00 | 0.09 / 0.09 | 0.079 / 0.048 |
| careful | 0.608 / 0.207 | 0.08 / 0.08 | 0.039 / 0.079 | 0.00 / 0.00 | 0.07 / 0.09 | 0.072 / 0.045 |

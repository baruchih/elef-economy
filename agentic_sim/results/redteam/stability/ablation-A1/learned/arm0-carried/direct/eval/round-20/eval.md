# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --dial-start 3.009180,13.600128,6.192114,1.037742`, seeds 21-40, hide ``, model `None` (value off, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 35599.0 ± 406.4 | -302.4 ± 802.8 | 6204.4 | 0.972 | 0.011 | 0.017 | 0.006 | 0.006 | 0.491 | 0.052 | 2.95 | 2.85 | 0.30 |
| careful | 35901.4 ± 668.0 | nan ± nan | 6188.3 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.492 | 0.000 | 1.90 | 0.00 | 0.30 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| direct | 0.006 (11690) [rej. blind 0.001] / 0.006 (51510) [rej. blind 0.001] | 0.020 (9583) [rej. blind 0.007] / 0.020 (34542) [rej. blind 0.001] | 0.152 (11082) [rej. blind 0.124] / 0.104 (5681) [rej. blind 0.101] | — / — |
| careful | 0.000 (11010) / 0.000 (51887) | 0.000 (9330) / 0.000 (34712) | 0.000 (11119) / 0.000 (5708) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| direct | 0.006 (11690) [rej. blind 0.001] / 0.006 (51510) [rej. blind 0.001] | 0.020 (9583) [rej. blind 0.007] / 0.020 (34542) [rej. blind 0.001] | 0.152 (11082) [rej. blind 0.124] / 0.104 (5681) [rej. blind 0.101] | — / — | 3.5 ± 0.4 | +13 |
| careful | 0.000 (11010) [rej. blind 0.000] / 0.000 (51887) [rej. blind 0.000] | 0.000 (9330) / 0.000 (34712) | 0.000 (11119) / 0.000 (5708) | — / — | 2.8 ± 0.4 | +4 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 0.933 | 0.976 | — (0) | — (0) | 0.057 (3044) | 0.020 (13281) | 0.009 (107763) | 25.750 | 275.200 | 1.162 | 0.111 |
| careful | — | 0.968 | — (0) | — (0) | 0.000 (3912) | 0.000 (15164) | 0.000 (104690) | 24.950 | 285.050 | 1.074 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| direct | 39.900 | 0.000 | 0.000 | 0.000 | 0.000 | 0.300 | 0.000 |
| careful | 39.750 | 0.000 | 0.000 | 0.000 | 0.000 | 0.300 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 21.650 / 39.900 | 2.950 ± 0.328 | +1.050 ± 0.456 | 26.100 | +4.350 ± 2.506 | 7.400 | 0.051 | 5.850 | +0.650 ± 0.689 | 1925.550 | 0.031 | +0.006 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 32319.186 ± 434.791 | +830.750 ± 670.853 | 35599.0 ± 406.4 | -302.4 ± 802.8 | 34.113 | -0.600 ± 0.460 | 19.623 ± 0.333 | +0.682 ± 0.547 | 18.502 | 0.002 | 2587.650 | 19.900 | 18.250 | +0.250 ± 0.289 | 162.344 | 119.100 |
| careful | 21.750 / 39.750 | 1.900 ± 0.324 | — | 21.750 | — | 7.200 | 0.045 | 5.200 | — | 1924.750 | 0.025 | — | 0.000 / 0.000 (0.000 / 0.000) | 31488.436 ± 586.441 | — | 35901.4 ± 668.0 | — | 34.713 | — | 18.941 ± 0.399 | — | 18.048 | 0.001 | 2608.200 | 19.750 | 18.000 | — | 269.634 | 84.300 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **direct**: p0 0.958/0.034/0.008 (243); p1 0.956/0.005/0.038 (379); p2 0.942/0.024/0.034 (482); p3 0.978/0.006/0.016 (518); p4 0.966/0.011/0.023 (565); p5 0.972/0.015/0.013 (583); p6 0.981/0.009/0.010 (612); p7 0.977/0.013/0.010 (629); p8 0.975/0.012/0.013 (649); p9 0.977/0.011/0.011 (521); p10 0.979/0.005/0.016 (354); p11 0.983/0.003/0.014 (277); p12 0.980/0.003/0.017 (206); p13 0.980/0.003/0.017 (135); p14 0.979/0.002/0.019 (31); p15 0.984/0.002/0.014 (21)
- **careful**: p0 1.000/0.000/0.000 (244); p1 1.000/0.000/0.000 (382); p2 1.000/0.000/0.000 (498); p3 1.000/0.000/0.000 (556); p4 1.000/0.000/0.000 (582); p5 1.000/0.000/0.000 (617); p6 1.000/0.000/0.000 (640); p7 1.000/0.000/0.000 (681); p8 1.000/0.000/0.000 (720); p9 1.000/0.000/0.000 (604); p10 1.000/0.000/0.000 (325); p11 1.000/0.000/0.000 (141); p12 1.000/0.000/0.000 (102); p13 1.000/0.000/0.000 (57); p14 1.000/0.000/0.000 (30); p15 1.000/0.000/0.000 (9)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 2575.5 / 584.5 | 0.31 / 0.28 | -0.04 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.20 / 0.18 | -0.02 ± 0.00 | 0.246 / 0.195 | -0.051 ± 0.009 | 0.106 / 0.097 | 0.002 / 0.000 | 0.064 / 0.057 | -0.007 ± 0.002 | 1.84 / 1.71 | -0.14 ± 0.06 |
| careful | 2594.3 / 550.5 | 0.22 / 0.19 | -0.04 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.20 / 0.18 | -0.02 ± 0.00 | 0.198 / 0.157 | -0.041 ± 0.009 | 0.084 / 0.080 | 0.001 / 0.000 | 0.057 / 0.054 | -0.004 ± 0.002 | 1.65 / 1.55 | -0.10 ± 0.06 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| direct | -0.03 ± 0.01 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.035 ± 0.005 | -0.002 ± 0.003 | -0.005 ± 0.002 |
| careful | -0.03 ± 0.01 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.030 ± 0.004 | +0.001 ± 0.002 | -0.002 ± 0.002 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| direct | 0.661 / 0.213 | 0.11 / 0.15 | 0.039 / 0.214 | 0.00 / 0.00 | 0.11 / 0.14 | 0.100 / 0.134 |
| careful | 0.660 / 0.207 | 0.12 / 0.15 | 0.039 / 0.227 | 0.00 / 0.00 | 0.12 / 0.12 | 0.094 / 0.134 |

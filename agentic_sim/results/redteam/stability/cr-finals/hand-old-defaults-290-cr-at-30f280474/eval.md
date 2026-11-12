# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --p-floor 0.2 --p-halve-every 5`, seeds 21-40, hide ``, model `None` (value off, horizon 8)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| careful | 36397.1 ± 897.4 | nan ± nan | 4029.4 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.296 | 0.000 | 6.45 | 0.00 | 0.15 |
| hand | 32112.8 ± 594.8 | -4284.3 ± 882.6 | 4554.9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.324 | 0.000 | 11.00 | 0.00 | 0.50 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| careful | 0.000 (5158) / 0.000 (51598) | 0.000 (910) / 0.000 (18178) | 0.000 (1264) / 0.000 (3480) | — / — |
| hand | 0.000 (12288) / 0.000 (49253) | 0.000 (2616) / 0.000 (20418) | 0.000 (2515) / 0.000 (4009) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| careful | 0.000 (5158) [rej. blind 0.000] / 0.000 (51598) [rej. blind 0.000] | 0.000 (910) / 0.000 (18178) | 0.000 (1264) / 0.000 (3480) | — / — | 3.2 ± 0.5 | +8 |
| hand | 0.098 (12288) [rej. blind 0.000] / 0.148 (49253) | 0.000 (2616) / 0.012 (20418) | 0.000 (2515) / 0.005 (4009) | — / — | 0.8 ± 0.3 | +8796 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| careful | — | 0.688 | 0.000 (24950) | 0.000 (5218) | 0.000 (4441) | 0.000 (1075) | 0.000 (44904) | 4.850 | 721.150 | 1.165 | 0.000 |
| hand | — | 0.800 | 0.000 (265) | 0.000 (12827) | 0.000 (18329) | 0.000 (15766) | 0.000 (43912) | 15.550 | 356.200 | 1.333 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| careful | 39.750 | 0.000 | 0.000 | 0.000 | 0.000 | 0.150 | 0.000 |
| hand | 39.850 | 0.000 | 0.000 | 0.000 | 0.000 | 0.500 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| careful | 23.600 / 39.750 | 6.450 ± 0.663 | — | 9.450 | — | 2.900 | 0.054 | 4.850 | — | 1606.700 | 0.025 | — | 0.000 / 0.000 (0.000 / 0.000) | 24172.431 ± 390.691 | — | 36397.1 ± 897.4 | — | 36.628 | — | 14.204 ± 0.461 | — | 18.197 | 0.007 | 2568.600 | 19.750 | 16.150 | — | 874.255 | 272.750 |
| hand | 20.150 / 39.850 | 11.000 ± 0.946 | +4.550 ± 1.120 | 65.550 | +56.100 ± 1.196 | 6.050 | 0.054 | 15.550 | +10.700 ± 0.692 | 1650.450 | 0.059 | +0.034 ± 0.002 | 0.000 / 0.000 (0.000 / 0.000) | 30189.999 ± 343.518 | +6017.568 ± 482.744 | 32112.8 ± 594.8 | -4284.3 ± 882.6 | 32.354 | -4.274 ± 0.580 | 20.467 ± 0.458 | +6.263 ± 0.579 | 19.796 | 0.022 | 2420.750 | 19.850 | 19.700 | +3.550 ± 0.510 | 104.591 | 151.100 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **careful**: p0 1.000/0.000/0.000 (597); p1 1.000/0.000/0.000 (701); p2 1.000/0.000/0.000 (826); p3 1.000/0.000/0.000 (907); p4 1.000/0.000/0.000 (808); p5 1.000/0.000/0.000 (191)
- **hand**: p0 —/—/— (0); p1 —/—/— (0); p2 —/—/— (0); p3 —/—/— (0); p4 —/—/— (0); p5 —/—/— (0); p6 —/—/— (0); p7 —/—/— (0); p8 —/—/— (0); p9 —/—/— (0); p10 —/—/— (0); p11 —/—/— (0); p12 —/—/— (0); p13 —/—/— (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| careful | 2579.9 / 257.9 | 0.42 / 0.31 | -0.11 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.07 / 0.07 | -0.00 ± 0.00 | 0.190 / 0.160 | -0.030 ± 0.005 | 0.072 / 0.081 | 0.007 / 0.000 | 0.067 / 0.061 | -0.006 ± 0.004 | 1.96 / 1.64 | -0.32 ± 0.12 |
| hand | 2462.7 / 614.4 | 0.70 / 0.69 | -0.01 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.14 / 0.15 | +0.00 ± 0.00 | 0.318 / 0.322 | +0.003 ± 0.006 | 0.132 / 0.147 | 0.022 / 0.000 | 0.095 / 0.089 | -0.006 ± 0.002 | 2.49 / 2.44 | -0.05 ± 0.08 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| careful | -0.11 ± 0.02 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.031 ± 0.005 | +0.007 ± 0.003 | -0.006 ± 0.004 |
| hand | -0.10 ± 0.02 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.045 ± 0.005 | -0.011 ± 0.003 | -0.006 ± 0.002 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| careful | 0.349 / 0.106 | 0.37 / 0.38 | 0.038 / 0.160 | 0.00 / 0.00 | 0.29 / 0.30 | 0.324 / 0.258 |
| hand | 0.410 / 0.178 | 0.12 / 0.14 | 0.033 / 0.084 | 0.00 / 0.00 | 0.07 / 0.09 | 0.308 / 0.203 |

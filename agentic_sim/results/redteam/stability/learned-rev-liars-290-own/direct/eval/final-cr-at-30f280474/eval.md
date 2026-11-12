# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --dispute-policy truthful --appeal-lie 0.1 --dispute-lie 0.1`, seeds 21-40, hide ``, model `None` (value off, horizon 8)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 36978.0 ± 869.9 | 1070.9 ± 848.6 | 4543.1 | 0.763 | 0.230 | 0.006 | 0.015 | 0.012 | 0.375 | 0.614 | 2.85 | 6.10 | 0.20 |
| careful | 35907.1 ± 773.7 | nan ± nan | 4458.9 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.376 | 0.000 | 1.50 | 0.00 | 0.25 |
| stamper | 7163.1 ± 138.2 | -28744.0 ± 770.4 | 1092.2 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.028 | 1.000 | 8.15 | 191.05 | 1.00 |
| hand | 32478.6 ± 593.7 | -3428.5 ± 756.9 | 4939.4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.398 | 0.000 | 3.70 | 0.00 | 0.45 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| direct | 0.015 (5526) [rej. blind 0.005] / 0.012 (51270) [rej. blind 0.003] | 0.949 (136) / 0.930 (21860) [rej. blind 0.001] | 0.025 (3161) [rej. blind 0.020] / 0.044 (8908) [rej. blind 0.037] | — / — |
| careful | 0.000 (5147) / 0.000 (50490) | 0.000 (122) / 0.000 (21520) | 0.000 (2814) / 0.000 (9085) | — / — |
| stamper | 1.000 (3128) / 1.000 (18101) | — / 1.000 (343) | — / 1.000 (273) | — / — |
| hand | 0.000 (11968) / 0.000 (47531) | 0.000 (1231) / 0.000 (22663) | 0.000 (5241) / 0.000 (10153) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| direct | 0.015 (5526) [rej. blind 0.005] / 0.012 (51270) [rej. blind 0.003] | 0.949 (136) / 0.930 (21860) [rej. blind 0.001] | 0.025 (3161) [rej. blind 0.020] / 0.044 (8908) [rej. blind 0.037] | — / — | 2.6 ± 0.4 | +7 |
| careful | 0.000 (5147) [rej. blind 0.000] / 0.000 (50490) [rej. blind 0.000] | 0.000 (122) / 0.000 (21520) | 0.000 (2814) / 0.000 (9085) | — / — | 2.5 ± 0.5 | +5 |
| stamper | 1.000 (3128) / 1.000 (18101) | — / 1.000 (343) | — / 1.000 (273) | — / — | 0.0 ± 0.0 | +0 |
| hand | 0.105 (11968) / 0.167 (47531) | 0.000 (1231) / 0.009 (22663) | 0.000 (5241) / 0.013 (10153) | — / — | 1.0 ± 0.3 | +9556 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 0.779 | 0.923 | — (0) | — (0) | 0.461 (19702) | 0.394 (2900) | 0.158 (68259) | 6.050 | 696.750 | 1.203 | 1.008 |
| careful | — | 0.925 | — (0) | — (0) | 0.000 (13499) | 0.000 (722) | 0.000 (74957) | 5.350 | 707.050 | 1.229 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (21845) | 58.400 | 177.550 | 2.206 | 3.271 |
| hand | — | 1.000 | — (0) | — (0) | 0.000 (44) | 0.000 (515) | 0.000 (98228) | 16.900 | 352.400 | 1.406 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| direct | 39.750 | 0.000 | 0.000 | 0.000 | 0.000 | 0.200 | 0.000 |
| careful | 39.600 | 0.000 | 0.000 | 0.000 | 0.000 | 0.250 | 0.000 |
| stamper | 39.950 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| hand | 39.900 | 0.000 | 0.000 | 0.000 | 0.000 | 0.450 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 23.300 / 39.750 | 2.850 ± 0.460 | +1.350 ± 0.509 | 14.850 | +5.600 ± 1.249 | 3.000 | 0.065 | 6.050 | +0.700 ± 0.616 | 1656.950 | 0.008 | -0.005 ± 0.001 | 221.750 / 33.100 (30.250 / 28.950) | 26447.683 ± 387.429 | +1909.000 ± 520.632 | 36978.0 ± 869.9 | +1070.9 ± 848.6 | 35.618 | +0.945 ± 0.689 | 15.291 ± 0.556 | +0.679 ± 0.607 | 18.859 | 0.003 | 2562.850 | 19.750 | 16.450 | +1.150 ± 0.514 | 685.456 | 250.950 |
| careful | 24.300 / 39.600 | 1.500 ± 0.235 | — | 9.250 | — | 2.800 | 0.054 | 5.350 | — | 1657.400 | 0.013 | — | 209.300 / 28.550 (25.600 / 25.050) | 24538.683 ± 434.133 | — | 35907.1 ± 773.7 | — | 34.672 | — | 14.612 ± 0.282 | — | 18.491 | 0.007 | 2513.700 | 19.600 | 15.300 | — | 545.685 | 275.150 |
| stamper | 3.650 / 39.950 | 8.150 ± 0.509 | +6.650 ± 0.477 | 116.550 | +107.300 ± 2.608 | 0.000 | 1.000 | 58.400 | +53.050 ± 2.196 | 662.950 | 0.018 | +0.005 ± 0.001 | 245.500 / 170.400 (177.350 / 169.350) | 8486.596 ± 161.740 | -16052.087 ± 411.091 | 7163.1 ± 138.2 | -28744.0 ± 770.4 | 26.656 | -8.016 ± 0.602 | 29.999 ± 0.654 | +15.387 ± 0.735 | 22.845 | 0.262 | 696.600 | 19.950 | 36.300 | +21.000 ± 0.692 | 5631.928 | 157.600 |
| hand | 20.550 / 39.900 | 3.700 ± 0.465 | +2.200 ± 0.551 | 65.450 | +56.200 ± 1.599 | 5.550 | 0.038 | 16.900 | +11.550 ± 0.578 | 1642.350 | 0.012 | -0.001 ± 0.001 | 268.750 / 93.650 (93.300 / 90.400) | 29199.122 ± 427.802 | +4660.439 ± 448.600 | 32478.6 ± 593.7 | -3428.5 ± 756.9 | 31.141 | -3.531 ± 0.508 | 19.135 ± 0.395 | +4.523 ± 0.435 | 19.683 | 0.045 | 2283.700 | 19.900 | 19.350 | +4.050 ± 0.432 | 55.222 | 172.250 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **direct**: p0 0.953/0.044/0.003 (595); p1 0.815/0.178/0.007 (712); p2 0.727/0.268/0.005 (859); p3 0.703/0.294/0.003 (957); p4 0.716/0.280/0.005 (930); p5 0.721/0.260/0.020 (405); p6 0.709/0.255/0.037 (75); p7 0.737/0.253/0.011 (10)
- **careful**: p0 1.000/0.000/0.000 (603); p1 1.000/0.000/0.000 (715); p2 1.000/0.000/0.000 (846); p3 1.000/0.000/0.000 (989); p4 1.000/0.000/0.000 (1014); p5 1.000/0.000/0.000 (262); p6 1.000/0.000/0.000 (31)
- **stamper**: p0 0.000/1.000/0.000 (576); p1 0.000/1.000/0.000 (304); p2 0.000/1.000/0.000 (175); p3 0.000/1.000/0.000 (24); p4 0.000/1.000/0.000 (10); p5 0.000/1.000/0.000 (2)
- **hand**: p0 —/—/— (0); p1 —/—/— (0); p2 —/—/— (0); p3 —/—/— (0); p4 —/—/— (0); p5 —/—/— (0); p6 —/—/— (0); p7 —/—/— (0); p8 —/—/— (0); p9 —/—/— (0); p10 —/—/— (0); p11 —/—/— (0); p12 —/—/— (0); p13 —/—/— (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 2563.5 / 276.3 | 0.44 / 0.32 | -0.12 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.08 / 0.08 | +0.00 ± 0.00 | 0.238 / 0.202 | -0.036 ± 0.006 | 0.093 / 0.101 | 0.003 / 0.000 | 0.067 / 0.067 | +0.000 ± 0.003 | 2.05 / 1.61 | -0.43 ± 0.09 |
| careful | 2524.5 / 257.4 | 0.57 / 0.39 | -0.18 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.08 / 0.08 | -0.00 ± 0.00 | 0.259 / 0.218 | -0.041 ± 0.005 | 0.114 / 0.124 | 0.007 / 0.000 | 0.070 / 0.063 | -0.008 ± 0.003 | 2.29 / 1.83 | -0.47 ± 0.13 |
| stamper | 905.0 / 156.4 | 1.34 / 0.90 | -0.44 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.03 / 0.02 | -0.01 ± 0.00 | 0.306 / 0.297 | -0.009 ± 0.008 | 0.178 / 0.183 | 0.230 / 0.000 | 0.110 / 0.071 | -0.039 ± 0.004 | 3.72 / 2.31 | -1.41 ± 0.22 |
| hand | 2376.6 / 598.4 | 1.08 / 1.14 | +0.06 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.12 / 0.11 | -0.01 ± 0.00 | 0.479 / 0.492 | +0.013 ± 0.005 | 0.222 / 0.249 | 0.045 / 0.000 | 0.114 / 0.110 | -0.004 ± 0.003 | 3.01 / 2.92 | -0.09 ± 0.09 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| direct | -0.10 ± 0.02 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.032 ± 0.005 | +0.009 ± 0.003 | +0.001 ± 0.003 |
| careful | -0.17 ± 0.03 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.041 ± 0.005 | +0.009 ± 0.004 | -0.007 ± 0.003 |
| stamper | -0.90 ± 0.04 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.172 ± 0.015 | -0.121 ± 0.014 | -0.042 ± 0.006 |
| hand | -0.06 ± 0.02 | +0.00 ± 0.00 | -0.03 ± 0.00 | -0.054 ± 0.004 | -0.012 ± 0.004 | -0.007 ± 0.004 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| direct | 0.420 / 0.022 | 0.33 / 0.24 | 0.144 / 0.402 | 0.00 / 0.00 | 0.30 / 0.28 | 0.358 / 0.369 |
| careful | 0.420 / 0.022 | 0.32 / 0.40 | 0.139 / 0.398 | 0.00 / 0.00 | 0.31 / 0.32 | 0.375 / 0.402 |
| stamper | 0.019 / 0.000 | 0.01 / — | 0.268 / 0.999 | 0.00 / 0.00 | 0.00 / — | 1.274 / 1.998 |
| hand | 0.468 / 0.101 | 0.11 / 0.09 | 0.159 / 0.321 | 0.00 / 0.00 | 0.12 / 0.15 | 0.363 / 0.285 |

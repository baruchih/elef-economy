# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop half --learner-role reviewer --learner-exit rule`, seeds 21-40, hide ``, model `/Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/learned-rev-half-290-own/wm/models/wm-online-5.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 19648.9 ± 648.2 | -731.0 ± 524.0 | 2883.3 | 0.909 | 0.091 | 0.000 | 0.002 | 0.004 | 0.398 | 0.224 | 8.30 | 6.30 | 0.35 |
| careful | 20379.9 ± 538.2 | nan ± nan | 2970.4 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.404 | 0.000 | 3.60 | 0.00 | 0.30 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| greedy | 0.002 (6713) / 0.004 (27982) | 0.254 (2227) / 0.278 (16282) | 0.026 (1868) / 0.000 (2594) | — / — |
| careful | 0.000 (6655) / 0.000 (28773) | 0.000 (1889) / 0.000 (17502) | 0.000 (1635) / 0.000 (2955) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| greedy | 0.002 (6713) [rej. blind 0.000] / 0.004 (27982) [rej. blind 0.000] | 0.254 (2227) / 0.278 (16282) | 0.026 (1868) / 0.000 (2594) | — / — | 1.6 ± 0.2 | +6 |
| careful | 0.000 (6655) / 0.000 (28773) | 0.000 (1889) / 0.000 (17502) | 0.001 (1635) [rej. blind 0.001] / 0.000 (2955) | — / — | 1.7 ± 0.3 | +1 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 0.994 | 0.996 | — (0) | — (0) | 0.409 (154) | 0.013 (1986) | 0.093 (55526) | 13.250 | 218.400 | 2.199 | 0.475 |
| careful | — | 0.990 | — (0) | — (0) | 0.000 (614) | 0.000 (2189) | 0.000 (56606) | 12.900 | 217.250 | 2.213 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| greedy | 20.350 | 0.000 | 0.000 | 0.000 | 0.000 | 0.350 | 0.000 |
| careful | 20.350 | 0.000 | 0.000 | 0.000 | 0.000 | 0.300 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 12.350 / 20.350 | 8.300 ± 0.837 | +4.700 ± 0.898 | 41.300 | +2.250 ± 2.414 | 6.700 | 0.048 | 9.550 | +0.100 ± 0.827 | 1947.850 | 0.035 | -0.005 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 17590.814 ± 598.141 | -80.883 ± 580.812 | 19648.9 ± 648.2 | -731.0 ± 524.0 | 33.041 | -0.414 ± 0.522 | 19.466 ± 0.404 | +0.813 ± 0.725 | 19.018 | 0.010 | 2505.650 | 19.800 | 18.800 | +0.000 ± 0.316 | 116.486 | 136.900 |
| careful | 12.900 / 20.350 | 3.600 ± 0.387 | — | 39.050 | — | 6.650 | 0.042 | 9.450 | — | 1952.950 | 0.040 | — | 0.000 / 0.000 (0.000 / 0.000) | 17671.697 ± 612.668 | — | 20379.9 ± 538.2 | — | 33.454 | — | 18.653 ± 0.502 | — | 18.673 | 0.002 | 2528.450 | 19.800 | 18.800 | — | 198.417 | 154.650 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **greedy**: p0 0.960/0.040/0.000 (303); p1 0.892/0.108/0.000 (228); p2 0.861/0.139/0.000 (200); p3 0.847/0.153/0.000 (193); p4 0.855/0.145/0.000 (200); p5 0.829/0.171/0.000 (214); p6 0.872/0.128/0.000 (236); p7 0.889/0.111/0.000 (254); p8 0.920/0.080/0.000 (264); p9 0.949/0.051/0.000 (271); p10 0.978/0.022/0.000 (277); p11 0.980/0.020/0.000 (185); p12 0.986/0.014/0.000 (52); p13 1.000/0.000/0.000 (7)
- **careful**: p0 1.000/0.000/0.000 (294); p1 1.000/0.000/0.000 (260); p2 1.000/0.000/0.000 (202); p3 1.000/0.000/0.000 (206); p4 1.000/0.000/0.000 (248); p5 1.000/0.000/0.000 (241); p6 1.000/0.000/0.000 (252); p7 1.000/0.000/0.000 (244); p8 1.000/0.000/0.000 (244); p9 1.000/0.000/0.000 (271); p10 1.000/0.000/0.000 (247); p11 1.000/0.000/0.000 (187); p12 1.000/0.000/0.000 (73); p13 1.000/0.000/0.000 (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 2515.8 / 585.4 | 0.50 / 0.43 | -0.07 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.15 / 0.16 | +0.01 ± 0.00 | 0.266 / 0.241 | -0.025 ± 0.007 | 0.120 / 0.130 | 0.009 / 0.000 | 0.041 / 0.042 | +0.001 ± 0.002 | 2.18 / 1.88 | -0.31 ± 0.11 |
| careful | 2519.6 / 564.8 | 0.50 / 0.44 | -0.06 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.15 / 0.15 | -0.00 ± 0.00 | 0.290 / 0.265 | -0.026 ± 0.005 | 0.128 / 0.137 | 0.002 / 0.000 | 0.045 / 0.040 | -0.004 ± 0.003 | 2.05 / 1.90 | -0.15 ± 0.09 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| greedy | -0.11 ± 0.02 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.052 ± 0.006 | -0.007 ± 0.003 | -0.000 ± 0.002 |
| careful | -0.08 ± 0.02 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.049 ± 0.004 | -0.006 ± 0.003 | -0.003 ± 0.002 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| greedy | 0.547 / 0.218 | 0.12 / 0.13 | 0.038 / 0.096 | 0.00 / 0.00 | 0.10 / 0.11 | 0.266 / 0.152 |
| careful | 0.544 / 0.210 | 0.11 / 0.12 | 0.038 / 0.095 | 0.00 / 0.00 | 0.11 / 0.11 | 0.273 / 0.160 |

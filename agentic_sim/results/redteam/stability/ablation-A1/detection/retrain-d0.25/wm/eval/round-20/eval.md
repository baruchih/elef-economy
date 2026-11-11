# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --dispute-policy truthful --dispute-rate 0.25`, seeds 21-40, hide ``, model `/Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/ablation-A1/detection/retrain-d0.25/wm/models/wm-online-20.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 36132.7 ± 898.9 | 1415.2 ± 1130.6 | 4351.4 | 0.818 | 0.182 | 0.000 | 0.001 | 0.002 | 0.337 | 0.537 | 9.90 | 9.95 | 0.30 |
| careful | 34717.5 ± 757.5 | nan ± nan | 4466.2 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.359 | 0.000 | 2.00 | 0.00 | 0.35 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| greedy | 0.001 (5345) / 0.002 (52370) | 0.612 (1125) / 0.628 (23707) | 0.028 (1433) / 0.035 (3047) | — / — |
| careful | 0.000 (5185) / 0.000 (52085) | 0.000 (1026) / 0.000 (25160) | 0.000 (1644) / 0.000 (4224) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| greedy | 0.001 (5345) [rej. blind 0.000] / 0.002 (52370) [rej. blind 0.000] | 0.612 (1125) / 0.628 (23707) | 0.028 (1433) / 0.035 (3047) | — / — | 2.7 ± 0.4 | +13 |
| careful | 0.000 (5185) / 0.000 (52085) [rej. blind 0.000] | 0.000 (1026) / 0.000 (25160) | 0.000 (1644) / 0.000 (4224) | — / — | 3.0 ± 0.6 | +10 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 0.770 | 0.930 | — (0) | — (0) | 0.429 (17499) | 0.158 (811) | 0.119 (68717) | 24.550 | 717.000 | 1.152 | 0.405 |
| careful | — | 0.912 | — (0) | — (0) | 0.000 (15848) | 0.000 (45) | 0.000 (73431) | 24.700 | 697.350 | 1.167 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| greedy | 39.550 | 0.000 | 0.000 | 0.000 | 0.000 | 0.300 | 0.000 |
| careful | 39.700 | 0.000 | 0.000 | 0.000 | 0.000 | 0.350 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 23.200 / 39.550 | 9.900 ± 0.833 | +7.900 ± 0.864 | 10.600 | +0.600 ± 1.022 | 2.850 | 0.053 | 5.000 | +0.000 ± 0.669 | 1904.450 | 0.012 | -0.009 ± 0.001 | 7.700 / 7.650 (7.700 / 7.650) | 25978.838 ± 279.628 | +1463.918 ± 478.638 | 36132.7 ± 898.9 | +1415.2 ± 1130.6 | 36.402 | +0.128 ± 0.547 | 15.384 ± 0.412 | +0.139 ± 0.613 | 18.376 | 0.001 | 2621.450 | 19.550 | 16.350 | -0.050 ± 0.450 | 694.152 | 191.350 |
| careful | 23.300 / 39.700 | 2.000 ± 0.363 | — | 10.000 | — | 3.150 | 0.061 | 5.000 | — | 1893.000 | 0.021 | — | 7.100 / 7.000 (7.100 / 7.000) | 24514.919 ± 297.281 | — | 34717.5 ± 757.5 | — | 36.274 | — | 15.245 ± 0.414 | — | 17.860 | 0.001 | 2608.650 | 19.700 | 16.400 | — | 667.600 | 184.800 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **greedy**: p0 0.941/0.059/0.000 (604); p1 0.837/0.163/0.000 (732); p2 0.771/0.229/0.000 (836); p3 0.759/0.241/0.000 (916); p4 0.806/0.194/0.000 (925); p5 0.855/0.145/0.000 (297); p6 0.951/0.049/0.000 (30); p7 0.932/0.068/0.000 (10)
- **careful**: p0 1.000/0.000/0.000 (597); p1 1.000/0.000/0.000 (751); p2 1.000/0.000/0.000 (901); p3 1.000/0.000/0.000 (981); p4 1.000/0.000/0.000 (987); p5 1.000/0.000/0.000 (248)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 2618.5 / 267.2 | 0.25 / 0.17 | -0.09 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.07 / 0.07 | +0.00 ± 0.00 | 0.173 / 0.133 | -0.040 ± 0.006 | 0.067 / 0.069 | 0.001 / 0.000 | 0.056 / 0.056 | +0.000 ± 0.004 | 1.62 / 1.35 | -0.27 ± 0.08 |
| careful | 2604.2 / 259.2 | 0.27 / 0.18 | -0.08 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.10 / 0.10 | -0.00 ± 0.00 | 0.184 / 0.155 | -0.029 ± 0.006 | 0.075 / 0.080 | 0.001 / 0.000 | 0.055 / 0.059 | +0.004 ± 0.004 | 1.65 / 1.37 | -0.28 ± 0.06 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| greedy | -0.08 ± 0.02 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.039 ± 0.006 | +0.003 ± 0.003 | +0.001 ± 0.004 |
| careful | -0.08 ± 0.02 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.030 ± 0.006 | +0.005 ± 0.003 | +0.004 ± 0.004 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| greedy | 0.446 / 0.124 | 0.39 / 0.43 | 0.043 / 0.214 | 0.00 / 0.00 | 0.40 / 0.41 | 0.335 / 0.310 |
| careful | 0.477 / 0.127 | 0.30 / 0.29 | 0.043 / 0.199 | 0.00 / 0.00 | 0.29 / 0.31 | 0.298 / 0.262 |

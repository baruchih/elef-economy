# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --arm 2 --dispute-policy truthful --dispute-rate 0.25`, seeds 21-40, hide ``, model `results/redteam/stability/ablation-A1/learned/arm2/wm/models/wm-online-10.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 31023.9 ± 716.6 | 983.9 ± 515.1 | 3084.7 | 0.996 | 0.004 | 0.000 | 0.005 | 0.003 | 0.050 | 0.015 | 2.20 | 1.80 | 0.40 |
| careful | 30040.1 ± 643.0 | nan ± nan | 3080.9 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.050 | 0.000 | 1.50 | 0.00 | 0.60 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| greedy | 0.005 (5464) / 0.003 (53166) | — / 0.000 (4) | 0.029 (893) / 0.010 (2167) | — / — |
| careful | 0.000 (5348) / 0.000 (53180) | — / 0.000 (4) | 0.000 (899) / 0.000 (2187) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| greedy | 0.005 (5464) [rej. blind 0.000] / 0.004 (53166) [rej. blind 0.000] | — / 0.000 (4) | 0.029 (893) / 0.010 (2167) | — / — | 3.2 ± 0.6 | +11 |
| careful | 0.000 (5348) [rej. blind 0.000] / 0.000 (53180) [rej. blind 0.000] | — / 0.000 (4) | 0.000 (899) / 0.000 (2187) | — / — | 3.2 ± 0.6 | +11 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 0.865 | 0.950 | — (0) | — (0) | 0.015 (6145) | 0.019 (692) | 0.003 (54857) | 5.150 | 661.250 | 1.134 | 0.350 |
| careful | — | 0.944 | — (0) | — (0) | 0.000 (7034) | — (0) | 0.000 (54584) | 5.450 | 667.550 | 1.184 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| greedy | 39.200 | 0.000 | 0.000 | 0.000 | 0.000 | 0.400 | 0.000 |
| careful | 39.350 | 0.000 | 0.000 | 0.000 | 0.000 | 0.600 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 20.850 / 39.200 | 2.200 ± 0.388 | +0.700 ± 0.465 | 10.250 | +1.200 ± 0.787 | 3.850 | 0.039 | 5.150 | -0.300 ± 0.459 | 1918.700 | 0.015 | +0.000 ± 0.000 | 7.950 / 7.950 (7.950 / 7.950) | 19539.351 ± 310.044 | -85.904 ± 252.542 | 31023.9 ± 716.6 | +983.9 ± 515.1 | 38.189 | +0.391 ± 0.323 | 13.753 ± 0.352 | -0.632 ± 0.422 | 16.388 | 0.000 | 2662.900 | 19.200 | 18.350 | -0.400 ± 0.472 | 1002.009 | 251.500 |
| careful | 20.600 / 39.350 | 1.500 ± 0.256 | — | 9.050 | — | 4.000 | 0.046 | 5.450 | — | 1909.650 | 0.014 | — | 8.200 / 8.100 (8.200 / 8.100) | 19625.255 ± 284.439 | — | 30040.1 ± 643.0 | — | 37.798 | — | 14.385 ± 0.260 | — | 16.632 | 0.000 | 2663.200 | 19.350 | 18.750 | — | 924.074 | 243.750 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **greedy**: p0 1.000/0.000/0.000 (559); p1 0.999/0.001/0.000 (549); p2 0.997/0.003/0.000 (565); p3 0.993/0.007/0.000 (564); p4 0.994/0.006/0.000 (583); p5 0.991/0.009/0.000 (238); p6 0.970/0.030/0.000 (27)
- **careful**: p0 1.000/0.000/0.000 (558); p1 1.000/0.000/0.000 (547); p2 1.000/0.000/0.000 (564); p3 1.000/0.000/0.000 (580); p4 1.000/0.000/0.000 (606); p5 1.000/0.000/0.000 (225)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 2658.3 / 273.2 | 0.13 / 0.06 | -0.07 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.06 / 0.07 | +0.01 ± 0.00 | 0.102 / 0.082 | -0.021 ± 0.004 | 0.034 / 0.037 | 0.000 / 0.000 | 0.059 / 0.065 | +0.007 ± 0.003 | 1.45 / 1.24 | -0.21 ± 0.11 |
| careful | 2659.0 / 267.4 | 0.13 / 0.06 | -0.07 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.07 / 0.07 | +0.00 ± 0.00 | 0.103 / 0.087 | -0.016 ± 0.003 | 0.035 / 0.037 | 0.000 / 0.000 | 0.058 / 0.067 | +0.009 ± 0.003 | 1.47 / 1.25 | -0.22 ± 0.10 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| greedy | -0.06 ± 0.02 | +0.00 ± 0.00 | +0.01 ± 0.00 | -0.018 ± 0.004 | +0.003 ± 0.003 | +0.007 ± 0.003 |
| careful | -0.07 ± 0.02 | +0.00 ± 0.00 | +0.00 ± 0.00 | -0.016 ± 0.003 | +0.003 ± 0.003 | +0.009 ± 0.004 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| greedy | 0.000 / 0.000 | 0.50 / — | 0.043 / 0.176 | 0.00 / 0.00 | 0.17 / 0.11 | 0.932 / 0.189 |
| careful | 0.000 / 0.000 | 0.50 / — | 0.042 / 0.180 | 0.00 / 0.00 | 0.15 / 0.12 | 0.926 / 0.193 |

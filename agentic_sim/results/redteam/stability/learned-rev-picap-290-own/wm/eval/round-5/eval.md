# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --pi0 0.40`, seeds 21-40, hide ``, model `/Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/learned-rev-picap-290-own/wm/models/wm-online-5.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 27854.1 ± 703.4 | -1973.1 ± 767.5 | 5733.2 | 0.948 | 0.052 | 0.000 | 0.002 | 0.002 | 0.394 | 0.129 | 7.30 | 4.90 | 0.50 |
| careful | 29827.2 ± 564.0 | nan ± nan | 5661.4 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.394 | 0.000 | 4.45 | 0.00 | 0.50 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| greedy | 0.002 (19437) / 0.002 (50065) | 0.146 (5265) / 0.163 (30214) | 0.024 (4405) [rej. blind 0.005] / 0.007 (5279) [rej. blind 0.004] | — / — |
| careful | 0.000 (19185) / 0.000 (49430) | 0.000 (4675) / 0.000 (30455) | 0.000 (4059) / 0.000 (5423) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| greedy | 0.002 (19437) / 0.002 (50065) | 0.146 (5265) / 0.163 (30214) | 0.024 (4405) [rej. blind 0.005] / 0.007 (5279) [rej. blind 0.004] | — / — | 4.0 ± 0.6 | +9 |
| careful | 0.000 (19185) [rej. blind 0.000] / 0.000 (49430) [rej. blind 0.000] | 0.000 (4675) / 0.000 (30455) | 0.000 (4059) / 0.000 (5423) | — / — | 4.3 ± 0.5 | +12 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 0.910 | 0.848 | — (0) | — (0) | 0.034 (34710) | 0.096 (844) | 0.059 (79111) | 25.150 | 208.950 | 1.047 | 0.195 |
| careful | — | 0.859 | — (0) | — (0) | 0.000 (32333) | 0.000 (1537) | 0.000 (79357) | 24.950 | 201.750 | 1.098 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| greedy | 39.950 | 0.000 | 0.000 | 0.000 | 0.000 | 0.500 | 0.000 |
| careful | 39.850 | 0.000 | 0.000 | 0.000 | 0.000 | 0.500 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 19.400 / 39.950 | 7.300 ± 0.871 | +2.850 ± 1.055 | 35.950 | -1.450 ± 1.633 | 12.100 | 0.041 | 5.200 | +0.100 ± 0.571 | 1658.700 | 0.022 | -0.001 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 33087.297 ± 347.635 | -40.726 ± 611.707 | 27854.1 ± 703.4 | -1973.1 ± 767.5 | 32.958 | +0.159 ± 0.555 | 26.720 ± 1.073 | +2.553 ± 1.096 | 21.534 | 0.002 | 2515.550 | 19.950 | 20.550 | +0.250 ± 0.376 | 106.808 | 118.250 |
| careful | 19.550 / 39.850 | 4.450 ± 0.591 | — | 37.400 | — | 12.900 | 0.055 | 5.100 | — | 1658.700 | 0.024 | — | 0.000 / 0.000 (0.000 / 0.000) | 33128.022 ± 486.531 | — | 29827.2 ± 564.0 | — | 32.799 | — | 24.167 ± 0.431 | — | 21.255 | 0.003 | 2486.750 | 19.850 | 20.300 | — | 126.087 | 109.200 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **greedy**: p0 0.954/0.046/0.000 (197); p1 0.839/0.161/0.000 (244); p2 0.875/0.125/0.000 (292); p3 0.879/0.121/0.000 (304); p4 0.901/0.099/0.000 (308); p5 0.887/0.112/0.000 (298); p6 0.904/0.095/0.001 (300); p7 0.916/0.083/0.001 (299); p8 0.921/0.076/0.002 (302); p9 0.945/0.055/0.000 (293); p10 0.978/0.021/0.001 (297); p11 0.986/0.014/0.000 (307); p12 0.987/0.012/0.000 (307); p13 0.994/0.006/0.000 (311); p14 0.996/0.004/0.000 (314); p15 0.999/0.001/0.000 (314); p16 1.000/0.000/0.000 (315); p17 0.999/0.001/0.000 (304); p18 1.000/0.000/0.000 (286); p19 0.997/0.003/0.000 (118); p20 1.000/0.000/0.000 (22)
- **careful**: p0 1.000/0.000/0.000 (198); p1 1.000/0.000/0.000 (255); p2 1.000/0.000/0.000 (299); p3 1.000/0.000/0.000 (307); p4 1.000/0.000/0.000 (309); p5 1.000/0.000/0.000 (304); p6 1.000/0.000/0.000 (307); p7 1.000/0.000/0.000 (299); p8 1.000/0.000/0.000 (300); p9 1.000/0.000/0.000 (306); p10 1.000/0.000/0.000 (306); p11 1.000/0.000/0.000 (302); p12 1.000/0.000/0.000 (299); p13 1.000/0.000/0.000 (310); p14 1.000/0.000/0.000 (302); p15 1.000/0.000/0.000 (304); p16 1.000/0.000/0.000 (313); p17 1.000/0.000/0.000 (308); p18 1.000/0.000/0.000 (228); p19 1.000/0.000/0.000 (92); p20 1.000/0.000/0.000 (13)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 2503.2 / 971.9 | 0.47 / 0.49 | +0.02 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.18 / 0.16 | -0.02 ± 0.00 | 0.248 / 0.227 | -0.021 ± 0.003 | 0.131 / 0.122 | 0.002 / 0.000 | 0.092 / 0.091 | -0.001 ± 0.003 | 2.18 / 2.17 | -0.01 ± 0.05 |
| careful | 2471.5 / 959.2 | 0.56 / 0.58 | +0.02 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.20 / 0.18 | -0.02 ± 0.00 | 0.309 / 0.281 | -0.028 ± 0.003 | 0.159 / 0.151 | 0.002 / 0.000 | 0.098 / 0.099 | +0.001 ± 0.002 | 2.38 / 2.39 | +0.01 ± 0.04 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| greedy | +0.02 ± 0.01 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.019 ± 0.003 | -0.007 ± 0.002 | -0.000 ± 0.003 |
| careful | +0.02 ± 0.01 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.026 ± 0.003 | -0.007 ± 0.002 | +0.001 ± 0.002 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| greedy | 0.597 / 0.206 | 0.09 / 0.10 | 0.040 / 0.079 | 0.00 / 0.00 | 0.08 / 0.10 | 0.076 / 0.048 |
| careful | 0.608 / 0.207 | 0.08 / 0.08 | 0.039 / 0.079 | 0.00 / 0.00 | 0.07 / 0.09 | 0.072 / 0.045 |

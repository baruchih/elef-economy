# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule`, seeds 21-40, hide ``, model `None` (value off, horizon 8)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 38591.7 ± 1212.3 | -12019.5 ± 1808.0 | 8900.8 | 0.727 | 0.110 | 0.163 | 0.230 | 0.210 | 0.377 | 0.373 | 23.70 | 49.35 | 0.95 |
| careful | 50611.1 ± 1386.1 | nan ± nan | 9509.0 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.395 | 0.000 | 8.55 | 0.00 | 0.50 |
| hand | 57050.4 ± 915.0 | 6439.3 ± 1917.2 | 9783.5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.412 | 0.000 | 11.85 | 0.00 | 0.55 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| direct | 0.230 (12939) [rej. blind 0.204] / 0.210 (97969) [rej. blind 0.180] | 0.306 (5264) [rej. blind 0.090] / 0.433 (36641) [rej. blind 0.058] | 0.294 (7231) [rej. blind 0.233] / 0.301 (17972) [rej. blind 0.252] | — / — |
| careful | 0.000 (10612) / 0.000 (104492) | 0.000 (3077) / 0.000 (57596) | 0.000 (4198) / 0.000 (10206) | — / — |
| hand | 0.000 (19800) / 0.000 (95200) | 0.000 (5812) / 0.000 (59145) | 0.000 (5813) / 0.000 (9899) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| direct | 0.230 (12939) [rej. blind 0.204] / 0.210 (97969) [rej. blind 0.180] | 0.306 (5264) [rej. blind 0.090] / 0.433 (36641) [rej. blind 0.058] | 0.294 (7231) [rej. blind 0.233] / 0.301 (17972) [rej. blind 0.252] | — / — | 3.2 ± 0.5 | +9 |
| careful | 0.000 (10612) [rej. blind 0.000] / 0.000 (104492) | 0.000 (3077) / 0.000 (57596) | 0.000 (4198) / 0.000 (10206) | — / — | 1.8 ± 0.4 | +4 |
| hand | 0.061 (19800) [rej. blind 0.000] / 0.077 (95200) | 0.000 (5812) / 0.004 (59145) | 0.000 (5813) / 0.002 (9899) | — / — | 0.8 ± 0.2 | +8786 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 0.874 | 0.950 | — (0) | — (0) | 0.260 (19229) | 0.103 (6545) | 0.091 (152242) | 30.000 | 716.650 | 2.037 | 1.645 |
| careful | — | 0.860 | — (0) | — (0) | 0.000 (54098) | 0.000 (848) | 0.000 (135235) | 24.600 | 688.150 | 1.185 | 0.000 |
| hand | — | 0.962 | — (0) | — (0) | 0.000 (12899) | 0.000 (17481) | 0.000 (165289) | 35.950 | 353.750 | 1.389 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| direct | 39.900 | 0.000 | 0.000 | 0.000 | 0.000 | 0.950 | 0.000 |
| careful | 39.700 | 0.000 | 0.000 | 0.000 | 0.000 | 0.500 | 0.000 |
| hand | 39.900 | 0.000 | 0.000 | 0.000 | 0.000 | 0.550 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 14.200 / 39.900 | 23.700 ± 1.531 | +15.150 ± 1.802 | 33.150 | +14.800 ± 2.423 | 39.550 | 0.048 | 10.100 | +5.200 ± 0.991 | 3013.250 | 0.045 | +0.021 ± 0.003 | 0.000 / 0.000 (0.000 / 0.000) | 53657.850 ± 794.340 | +648.785 ± 1511.487 | 38591.7 ± 1212.3 | -12019.5 ± 1808.0 | 33.098 | -2.599 ± 0.875 | 34.529 ± 0.979 | +10.433 ± 1.576 | 23.488 | 0.082 | 4503.800 | 19.900 | 25.700 | +6.350 ± 0.350 | 438.954 | 296.350 |
| careful | 20.350 / 39.700 | 8.550 ± 0.800 | — | 18.350 | — | 6.950 | 0.047 | 4.900 | — | 3539.650 | 0.024 | — | 0.000 / 0.000 (0.000 / 0.000) | 53009.065 ± 1284.094 | — | 50611.1 ± 1386.1 | — | 35.698 | — | 24.096 ± 1.211 | — | 19.116 | 0.002 | 5226.800 | 19.700 | 19.350 | — | 727.842 | 209.300 |
| hand | 19.250 / 39.900 | 11.850 ± 0.712 | +3.300 ± 1.152 | 82.500 | +64.150 ± 2.217 | 11.450 | 0.053 | 16.050 | +11.150 ± 0.822 | 3615.250 | 0.041 | +0.017 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 60436.927 ± 845.083 | +7427.862 ± 1266.830 | 57050.4 ± 915.0 | +6439.3 ± 1917.2 | 31.590 | -4.108 ± 0.524 | 22.328 ± 0.370 | -1.769 ± 1.369 | 20.663 | 0.013 | 4742.850 | 19.900 | 20.650 | +1.300 ± 0.349 | 58.013 | 162.850 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **direct**: p0 0.948/0.049/0.002 (595); p1 0.834/0.157/0.009 (666); p2 0.791/0.201/0.008 (752); p3 0.779/0.214/0.006 (834); p4 0.845/0.152/0.004 (809); p5 0.854/0.097/0.049 (824); p6 0.631/0.093/0.276 (962); p7 0.619/0.087/0.293 (741); p8 0.610/0.099/0.290 (613); p9 0.638/0.070/0.292 (529); p10 0.573/0.044/0.384 (453); p11 0.659/0.035/0.305 (327); p12 0.680/0.045/0.275 (209); p13 0.597/0.023/0.379 (145); p14 0.529/0.032/0.440 (95); p15 0.601/0.034/0.365 (77); p16 0.539/0.036/0.425 (84); p17 0.605/0.029/0.365 (77); p18 0.603/0.023/0.374 (73); p19 0.279/0.000/0.721 (16); p20 0.113/0.000/0.887 (13); p21 0.068/0.000/0.932 (7)
- **careful**: p0 1.000/0.000/0.000 (589); p1 1.000/0.000/0.000 (717); p2 1.000/0.000/0.000 (884); p3 1.000/0.000/0.000 (986); p4 1.000/0.000/0.000 (949); p5 1.000/0.000/0.000 (935); p6 1.000/0.000/0.000 (933); p7 1.000/0.000/0.000 (946); p8 1.000/0.000/0.000 (949); p9 1.000/0.000/0.000 (936); p10 1.000/0.000/0.000 (610); p11 1.000/0.000/0.000 (76)
- **hand**: p0 —/—/— (0); p1 —/—/— (0); p2 —/—/— (0); p3 —/—/— (0); p4 —/—/— (0); p5 —/—/— (0); p6 —/—/— (0); p7 —/—/— (0); p8 —/—/— (0); p9 —/—/— (0); p10 —/—/— (0); p11 —/—/— (0); p12 —/—/— (0); p13 —/—/— (0); p14 —/—/— (0); p15 —/—/— (0); p16 —/—/— (0); p17 —/—/— (0); p18 —/—/— (0); p19 —/—/— (0); p20 —/—/— (0); p21 —/—/— (0); p22 —/—/— (0); p23 —/—/— (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 4898.4 / 647.0 | 1.02 / 0.96 | -0.06 ± 0.04 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.10 / 0.10 | -0.00 ± 0.00 | 0.277 / 0.253 | -0.024 ± 0.008 | 0.146 / 0.153 | 0.081 / 0.000 | 0.121 / 0.116 | -0.006 ± 0.003 | 3.44 / 3.53 | +0.09 ± 0.14 |
| careful | 5224.6 / 530.6 | 0.21 / 0.13 | -0.07 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.14 / 0.14 | +0.00 ± 0.00 | 0.123 / 0.098 | -0.024 ± 0.005 | 0.051 / 0.046 | 0.001 / 0.000 | 0.067 / 0.062 | -0.005 ± 0.003 | 1.66 / 1.45 | -0.21 ± 0.06 |
| hand | 4760.0 / 990.0 | 1.03 / 1.07 | +0.04 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.17 / 0.15 | -0.02 ± 0.00 | 0.541 / 0.512 | -0.029 ± 0.006 | 0.249 / 0.253 | 0.013 / 0.000 | 0.122 / 0.118 | -0.004 ± 0.003 | 2.81 / 2.77 | -0.04 ± 0.06 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| direct | -0.17 ± 0.04 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.043 ± 0.005 | -0.012 ± 0.004 | -0.016 ± 0.003 |
| careful | -0.07 ± 0.02 | +0.00 ± 0.00 | +0.00 ± 0.00 | -0.026 ± 0.005 | -0.006 ± 0.002 | -0.005 ± 0.003 |
| hand | -0.03 ± 0.02 | +0.00 ± 0.00 | -0.03 ± 0.00 | -0.043 ± 0.004 | -0.007 ± 0.003 | -0.002 ± 0.003 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| direct | 0.373 / 0.120 | 0.37 / 0.37 | 0.137 / 0.399 | 0.00 / 0.00 | 0.40 / 0.39 | 0.387 / 0.592 |
| careful | 0.548 / 0.165 | 0.14 / 0.14 | 0.040 / 0.163 | 0.00 / 0.00 | 0.12 / 0.14 | 0.152 / 0.127 |
| hand | 0.613 / 0.224 | 0.07 / 0.09 | 0.036 / 0.105 | 0.00 / 0.00 | 0.06 / 0.07 | 0.169 / 0.140 |

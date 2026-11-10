# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop half --learner-role reviewer --learner-exit rule`, seeds 21-40, hide ``, model `None` (value off, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 20469.7 ± 491.3 | 89.8 ± 607.3 | 2889.7 | 0.867 | 0.127 | 0.006 | 0.014 | 0.012 | 0.383 | 0.325 | 10.65 | 9.80 | 0.10 |
| careful | 20379.9 ± 538.2 | nan ± nan | 2970.4 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.404 | 0.000 | 3.60 | 0.00 | 0.30 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| direct | 0.014 (7001) [rej. blind 0.003] / 0.012 (28666) [rej. blind 0.002] | 0.354 (2161) [rej. blind 0.000] / 0.377 (15768) [rej. blind 0.000] | 0.146 (1735) [rej. blind 0.055] / 0.092 (2463) [rej. blind 0.068] | — / — |
| careful | 0.000 (6655) / 0.000 (28773) | 0.000 (1889) / 0.000 (17502) | 0.000 (1635) / 0.000 (2955) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| direct | 0.014 (7001) [rej. blind 0.003] / 0.012 (28666) [rej. blind 0.002] | 0.354 (2161) [rej. blind 0.000] / 0.377 (15768) [rej. blind 0.000] | 0.146 (1735) [rej. blind 0.055] / 0.092 (2463) [rej. blind 0.068] | — / — | 1.8 ± 0.4 | +2 |
| careful | 0.000 (6655) / 0.000 (28773) | 0.000 (1889) / 0.000 (17502) | 0.001 (1635) [rej. blind 0.001] / 0.000 (2955) | — / — | 1.7 ± 0.3 | +1 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 0.995 | 0.997 | — (0) | — (0) | 0.338 (80) | 0.174 (1120) | 0.125 (56594) | 12.950 | 203.600 | 2.353 | 0.757 |
| careful | — | 0.990 | — (0) | — (0) | 0.000 (614) | 0.000 (2189) | 0.000 (56606) | 12.900 | 217.250 | 2.213 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| direct | 20.350 | 0.000 | 0.000 | 0.000 | 0.000 | 0.100 | 0.000 |
| careful | 20.350 | 0.000 | 0.000 | 0.000 | 0.000 | 0.300 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 12.650 / 20.350 | 10.650 ± 0.856 | +7.050 ± 1.009 | 44.100 | +5.050 ± 1.697 | 6.900 | 0.059 | 9.600 | +0.150 ± 0.563 | 1969.150 | 0.037 | -0.003 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 18074.396 ± 484.849 | +402.699 ± 640.643 | 20469.7 ± 491.3 | +89.8 ± 607.3 | 33.339 | -0.116 ± 0.469 | 19.118 ± 0.311 | +0.465 ± 0.667 | 18.797 | 0.005 | 2512.300 | 19.800 | 18.750 | -0.050 ± 0.359 | 146.828 | 176.450 |
| careful | 12.900 / 20.350 | 3.600 ± 0.387 | — | 39.050 | — | 6.650 | 0.042 | 9.450 | — | 1952.950 | 0.040 | — | 0.000 / 0.000 (0.000 / 0.000) | 17671.697 ± 612.668 | — | 20379.9 ± 538.2 | — | 33.454 | — | 18.653 ± 0.502 | — | 18.673 | 0.002 | 2528.450 | 19.800 | 18.800 | — | 198.417 | 154.650 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **direct**: p0 0.955/0.040/0.005 (293); p1 0.834/0.145/0.021 (221); p2 0.831/0.153/0.016 (178); p3 0.779/0.215/0.006 (190); p4 0.842/0.153/0.005 (210); p5 0.891/0.106/0.003 (215); p6 0.853/0.144/0.003 (221); p7 0.848/0.150/0.002 (250); p8 0.868/0.128/0.004 (269); p9 0.898/0.099/0.003 (263); p10 0.862/0.134/0.003 (255); p11 0.885/0.110/0.005 (198); p12 0.893/0.100/0.007 (111); p13 0.916/0.081/0.003 (17)
- **careful**: p0 1.000/0.000/0.000 (294); p1 1.000/0.000/0.000 (260); p2 1.000/0.000/0.000 (202); p3 1.000/0.000/0.000 (206); p4 1.000/0.000/0.000 (248); p5 1.000/0.000/0.000 (241); p6 1.000/0.000/0.000 (252); p7 1.000/0.000/0.000 (244); p8 1.000/0.000/0.000 (244); p9 1.000/0.000/0.000 (271); p10 1.000/0.000/0.000 (247); p11 1.000/0.000/0.000 (187); p12 1.000/0.000/0.000 (73); p13 1.000/0.000/0.000 (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 2508.7 / 601.6 | 0.49 / 0.42 | -0.06 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.15 / 0.15 | +0.01 ± 0.01 | 0.280 / 0.256 | -0.025 ± 0.008 | 0.120 / 0.128 | 0.005 / 0.000 | 0.043 / 0.043 | -0.000 ± 0.002 | 2.21 / 1.96 | -0.25 ± 0.10 |
| careful | 2519.6 / 564.8 | 0.50 / 0.44 | -0.06 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.15 / 0.15 | -0.00 ± 0.00 | 0.290 / 0.265 | -0.026 ± 0.005 | 0.128 / 0.137 | 0.002 / 0.000 | 0.045 / 0.040 | -0.004 ± 0.003 | 2.05 / 1.90 | -0.15 ± 0.09 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| direct | -0.09 ± 0.02 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.053 ± 0.006 | -0.009 ± 0.003 | -0.000 ± 0.002 |
| careful | -0.08 ± 0.02 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.049 ± 0.004 | -0.006 ± 0.003 | -0.003 ± 0.002 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| direct | 0.545 / 0.215 | 0.12 / 0.14 | 0.037 / 0.095 | 0.00 / 0.00 | 0.13 / 0.13 | 0.280 / 0.151 |
| careful | 0.544 / 0.210 | 0.11 / 0.12 | 0.038 / 0.095 | 0.00 / 0.00 | 0.11 / 0.11 | 0.273 / 0.160 |

# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop half --learner-role reviewer --learner-exit rule`, seeds 21-40, hide ``, model `/Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/learned-rev-half-290-own/wm/models/wm-online-10.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 20145.7 ± 753.4 | -234.2 ± 595.9 | 2933.3 | 0.924 | 0.076 | 0.000 | 0.000 | 0.000 | 0.386 | 0.196 | 7.90 | 4.10 | 0.35 |
| careful | 20379.9 ± 538.2 | nan ± nan | 2970.4 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.404 | 0.000 | 3.60 | 0.00 | 0.30 |
| stamper | 3732.8 ± 134.8 | -16647.1 ± 530.3 | 515.0 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.023 | 1.000 | 10.65 | 88.70 | 1.00 |
| hand | 15767.6 ± 653.4 | -4612.3 ± 505.9 | 2318.6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.360 | 0.000 | 7.20 | 0.00 | 0.60 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| greedy | 0.000 (6598) / 0.000 (29404) | 0.237 (2167) / 0.241 (16200) | 0.009 (1785) / 0.000 (2512) | — / — |
| careful | 0.000 (6655) / 0.000 (28773) | 0.000 (1889) / 0.000 (17502) | 0.000 (1635) / 0.000 (2955) | — / — |
| stamper | 1.000 (1406) / 1.000 (8658) | — / 1.000 (217) | — / 1.000 (18) | — / — |
| hand | 0.000 (5819) / 0.000 (23856) | 0.000 (1420) / 0.000 (11988) | 0.000 (1258) / 0.000 (2030) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| greedy | 0.000 (6598) / 0.000 (29404) [rej. blind 0.000] | 0.237 (2167) / 0.241 (16200) | 0.009 (1785) / 0.000 (2512) | — / — | 2.1 ± 0.5 | +3 |
| careful | 0.000 (6655) / 0.000 (28773) | 0.000 (1889) / 0.000 (17502) | 0.001 (1635) [rej. blind 0.001] / 0.000 (2955) | — / — | 1.7 ± 0.3 | +1 |
| stamper | 1.000 (1406) / 1.000 (8658) | — / 1.000 (217) | — / 1.000 (18) | — / — | 1.4 ± 0.5 | +0 |
| hand | 0.106 (5819) [rej. blind 0.000] / 0.156 (23856) | 0.000 (1420) / 0.012 (11988) | 0.000 (1258) / 0.007 (2030) | — / — | 1.1 ± 0.4 | +4493 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 0.996 | 0.990 | — (0) | — (0) | 0.032 (627) | 0.026 (2736) | 0.079 (55303) | 12.650 | 212.750 | 2.282 | 0.324 |
| careful | — | 0.990 | — (0) | — (0) | 0.000 (614) | 0.000 (2189) | 0.000 (56606) | 12.900 | 217.250 | 2.213 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (10299) | 34.100 | 96.400 | 4.386 | 2.601 |
| hand | — | 0.999 | — (0) | — (0) | 0.000 (93) | 0.000 (472) | 0.000 (45806) | 19.300 | 189.750 | 2.600 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| greedy | 20.350 | 0.000 | 0.000 | 0.000 | 0.000 | 0.350 | 0.000 |
| careful | 20.350 | 0.000 | 0.000 | 0.000 | 0.000 | 0.300 | 0.000 |
| stamper | 20.450 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| hand | 20.400 | 0.000 | 0.000 | 0.000 | 0.000 | 0.600 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 13.050 / 20.350 | 7.900 ± 0.750 | +4.300 ± 0.843 | 40.900 | +1.850 ± 2.089 | 6.600 | 0.057 | 9.400 | -0.050 ± 0.694 | 1969.050 | 0.039 | -0.001 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 17462.537 ± 538.840 | -209.159 ± 426.879 | 20145.7 ± 753.4 | -234.2 ± 595.9 | 33.611 | +0.157 ± 0.487 | 18.932 ± 0.522 | +0.279 ± 0.742 | 18.744 | 0.004 | 2534.600 | 19.800 | 18.550 | -0.250 ± 0.435 | 201.670 | 160.950 |
| careful | 12.900 / 20.350 | 3.600 ± 0.387 | — | 39.050 | — | 6.650 | 0.042 | 9.450 | — | 1952.950 | 0.040 | — | 0.000 / 0.000 (0.000 / 0.000) | 17671.697 ± 612.668 | — | 20379.9 ± 538.2 | — | 33.454 | — | 18.653 ± 0.502 | — | 18.673 | 0.002 | 2528.450 | 19.800 | 18.800 | — | 198.417 | 154.650 |
| stamper | 0.050 / 20.450 | 10.650 ± 0.494 | +7.050 ± 0.526 | 90.600 | +51.550 ± 2.020 | 5.900 | 0.035 | 32.450 | +23.000 ± 0.918 | 1751.500 | 0.084 | +0.044 ± 0.002 | 0.000 / 0.000 (0.000 / 0.000) | 3576.467 ± 120.623 | -14095.230 ± 587.569 | 3732.8 ± 134.8 | -16647.1 ± 530.3 | 27.547 | -5.907 ± 0.421 | 27.256 ± 0.309 | +8.604 ± 0.420 | 23.790 | 0.338 | 1397.550 | 20.000 | 29.000 | +10.200 ± 0.457 | 71.653 | 181.800 |
| hand | 10.100 / 20.400 | 7.200 ± 0.735 | +3.600 ± 0.828 | 62.400 | +23.350 ± 2.540 | 6.050 | 0.039 | 15.850 | +6.400 ± 0.799 | 1925.900 | 0.054 | +0.014 ± 0.002 | 0.000 / 0.000 (0.000 / 0.000) | 14312.525 ± 571.494 | -3359.172 ± 356.072 | 15767.6 ± 653.4 | -4612.3 ± 505.9 | 31.698 | -1.756 ± 0.432 | 19.417 ± 0.270 | +0.765 ± 0.444 | 19.674 | 0.027 | 2365.800 | 19.850 | 19.200 | +0.400 ± 0.358 | 59.930 | 165.350 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **greedy**: p0 0.985/0.015/0.000 (298); p1 0.879/0.121/0.000 (232); p2 0.907/0.093/0.000 (190); p3 0.865/0.135/0.000 (196); p4 0.874/0.126/0.000 (238); p5 0.909/0.091/0.000 (241); p6 0.920/0.080/0.000 (250); p7 0.899/0.101/0.000 (258); p8 0.913/0.087/0.000 (271); p9 0.956/0.044/0.000 (272); p10 0.972/0.028/0.000 (250); p11 0.979/0.021/0.000 (167); p12 0.969/0.031/0.000 (56); p13 1.000/0.000/0.000 (13); p14 1.000/0.000/0.000 (2)
- **careful**: p0 1.000/0.000/0.000 (294); p1 1.000/0.000/0.000 (260); p2 1.000/0.000/0.000 (202); p3 1.000/0.000/0.000 (206); p4 1.000/0.000/0.000 (248); p5 1.000/0.000/0.000 (241); p6 1.000/0.000/0.000 (252); p7 1.000/0.000/0.000 (244); p8 1.000/0.000/0.000 (244); p9 1.000/0.000/0.000 (271); p10 1.000/0.000/0.000 (247); p11 1.000/0.000/0.000 (187); p12 1.000/0.000/0.000 (73); p13 1.000/0.000/0.000 (0)
- **stamper**: p0 0.000/1.000/0.000 (290); p1 0.000/1.000/0.000 (141); p2 0.000/1.000/0.000 (61); p3 0.000/1.000/0.000 (17); p4 0.000/1.000/0.000 (5); p5 0.000/1.000/0.000 (0)
- **hand**: p0 —/—/— (0); p1 —/—/— (0); p2 —/—/— (0); p3 —/—/— (0); p4 —/—/— (0); p5 —/—/— (0); p6 —/—/— (0); p7 —/—/— (0); p8 —/—/— (0); p9 —/—/— (0); p10 —/—/— (0); p11 —/—/— (0); p12 —/—/— (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 2531.8 / 564.6 | 0.44 / 0.36 | -0.07 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.15 / 0.16 | +0.01 ± 0.00 | 0.246 / 0.224 | -0.023 ± 0.006 | 0.102 / 0.107 | 0.004 / 0.000 | 0.042 / 0.037 | -0.005 ± 0.002 | 2.03 / 1.89 | -0.14 ± 0.09 |
| careful | 2519.6 / 564.8 | 0.50 / 0.44 | -0.06 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.15 / 0.15 | -0.00 ± 0.00 | 0.290 / 0.265 | -0.026 ± 0.005 | 0.128 / 0.137 | 0.002 / 0.000 | 0.045 / 0.040 | -0.004 ± 0.003 | 2.05 / 1.90 | -0.15 ± 0.09 |
| stamper | 2056.5 / 517.5 | 1.99 / 2.15 | +0.16 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.12 / 0.14 | +0.02 ± 0.00 | 0.567 / 0.624 | +0.057 ± 0.005 | 0.372 / 0.414 | 0.331 / 0.000 | 0.024 / 0.015 | -0.010 ± 0.002 | 3.24 / 2.71 | -0.53 ± 0.30 |
| hand | 2411.3 / 593.3 | 0.86 / 0.91 | +0.05 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.15 / 0.15 | -0.01 ± 0.00 | 0.403 / 0.411 | +0.009 ± 0.004 | 0.176 / 0.199 | 0.027 / 0.000 | 0.048 / 0.045 | -0.003 ± 0.002 | 2.70 / 2.75 | +0.05 ± 0.13 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| greedy | -0.09 ± 0.01 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.045 ± 0.003 | -0.010 ± 0.002 | -0.003 ± 0.001 |
| careful | -0.08 ± 0.02 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.049 ± 0.004 | -0.006 ± 0.003 | -0.003 ± 0.002 |
| stamper | -0.20 ± 0.03 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.063 ± 0.005 | -0.044 ± 0.004 | -0.006 ± 0.002 |
| hand | -0.08 ± 0.02 | +0.00 ± 0.00 | -0.03 ± 0.00 | -0.052 ± 0.004 | -0.009 ± 0.003 | -0.004 ± 0.002 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| greedy | 0.537 / 0.207 | 0.11 / 0.13 | 0.036 / 0.095 | 0.00 / 0.00 | 0.11 / 0.11 | 0.283 / 0.168 |
| careful | 0.544 / 0.210 | 0.11 / 0.12 | 0.038 / 0.095 | 0.00 / 0.00 | 0.11 / 0.11 | 0.273 / 0.160 |
| stamper | 0.468 / 0.210 | 0.14 / 0.15 | 0.016 / 0.073 | 0.00 / 0.00 | 0.12 / 0.15 | 0.440 / 0.353 |
| hand | 0.525 / 0.214 | 0.11 / 0.14 | 0.035 / 0.085 | 0.00 / 0.00 | 0.09 / 0.11 | 0.321 / 0.216 |

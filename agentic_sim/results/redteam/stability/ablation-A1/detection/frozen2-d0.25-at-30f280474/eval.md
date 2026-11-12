# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --dispute-policy truthful --dispute-rate 0.25`, seeds 21-40, hide ``, model `None` (value off, horizon 8)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 33733.7 ± 804.4 | -983.8 ± 977.6 | 4235.9 | 0.826 | 0.168 | 0.006 | 0.025 | 0.027 | 0.314 | 0.496 | 15.40 | 32.95 | 0.35 |
| careful | 34717.5 ± 757.5 | nan ± nan | 4466.2 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.359 | 0.000 | 2.00 | 0.00 | 0.35 |
| hand | 32660.6 ± 670.2 | -2056.9 ± 1068.1 | 4880.3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.375 | 0.000 | 6.65 | 0.00 | 0.55 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| direct | 0.025 (5536) [rej. blind 0.001] / 0.027 (52557) [rej. blind 0.001] | 0.502 (1032) [rej. blind 0.006] / 0.543 (21303) [rej. blind 0.002] | 0.400 (1291) [rej. blind 0.064] / 0.205 (2999) [rej. blind 0.111] | — / — |
| careful | 0.000 (5185) / 0.000 (52085) | 0.000 (1026) / 0.000 (25160) | 0.000 (1644) / 0.000 (4224) | — / — |
| hand | 0.000 (12271) / 0.000 (48723) | 0.000 (2784) / 0.000 (26160) | 0.000 (3267) / 0.000 (4401) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| direct | 0.026 (5536) [rej. blind 0.001] / 0.028 (52557) [rej. blind 0.001] | 0.502 (1032) [rej. blind 0.006] / 0.543 (21303) [rej. blind 0.002] | 0.400 (1291) [rej. blind 0.064] / 0.206 (2999) [rej. blind 0.111] | — / — | 2.0 ± 0.4 | +11 |
| careful | 0.000 (5185) / 0.000 (52085) [rej. blind 0.000] | 0.000 (1026) / 0.000 (25160) | 0.000 (1644) / 0.000 (4224) | — / — | 3.0 ± 0.6 | +10 |
| hand | 0.100 (12271) / 0.150 (48723) | 0.000 (2784) / 0.009 (26160) | 0.000 (3267) / 0.009 (4401) | — / — | 0.7 ± 0.2 | +8789 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 0.833 | 0.943 | — (0) | — (0) | 0.379 (12953) | 0.207 (1061) | 0.130 (70704) | 4.800 | 682.750 | 1.185 | 6.865 |
| careful | — | 0.912 | — (0) | — (0) | 0.000 (15848) | 0.000 (45) | 0.000 (73431) | 5.000 | 697.350 | 1.167 | 0.000 |
| hand | — | 0.999 | — (0) | — (0) | 0.000 (27) | 0.000 (1272) | 0.000 (96307) | 15.450 | 350.950 | 1.360 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| direct | 39.750 | 0.000 | 0.000 | 0.000 | 0.000 | 0.350 | 0.000 |
| careful | 39.700 | 0.000 | 0.000 | 0.000 | 0.000 | 0.350 | 0.000 |
| hand | 39.800 | 0.000 | 0.000 | 0.000 | 0.000 | 0.550 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 22.600 / 39.750 | 15.400 ± 1.228 | +13.400 ± 1.234 | 14.950 | +4.950 ± 1.727 | 3.500 | 0.073 | 4.800 | -0.200 ± 0.546 | 1945.850 | 0.021 | -0.000 ± 0.001 | 11.000 / 7.700 (11.000 / 7.700) | 24494.083 ± 394.371 | -20.837 ± 450.363 | 33733.7 ± 804.4 | -983.8 ± 977.6 | 36.469 | +0.195 ± 0.461 | 15.648 ± 0.345 | +0.403 ± 0.506 | 18.157 | 0.001 | 2631.750 | 19.750 | 17.150 | +0.750 ± 0.517 | 693.925 | 192.500 |
| careful | 23.300 / 39.700 | 2.000 ± 0.363 | — | 10.000 | — | 3.150 | 0.061 | 5.000 | — | 1893.000 | 0.021 | — | 7.100 / 7.000 (7.100 / 7.000) | 24514.919 ± 297.281 | — | 34717.5 ± 757.5 | — | 36.274 | — | 15.245 ± 0.414 | — | 17.860 | 0.001 | 2608.650 | 19.700 | 16.400 | — | 667.600 | 184.800 |
| hand | 20.650 / 39.800 | 6.650 ± 0.621 | +4.650 ± 0.741 | 66.300 | +56.300 ± 1.560 | 6.950 | 0.065 | 15.450 | +10.450 ± 0.731 | 1923.650 | 0.044 | +0.023 ± 0.001 | 23.500 / 22.600 (23.500 / 22.600) | 29930.177 ± 326.184 | +5415.257 ± 384.587 | 32660.6 ± 670.2 | -2056.9 ± 1068.1 | 31.922 | -4.352 ± 0.403 | 19.890 ± 0.474 | +4.646 ± 0.661 | 19.564 | 0.021 | 2401.900 | 19.800 | 19.150 | +2.750 ± 0.469 | 67.413 | 186.050 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **direct**: p0 0.941/0.056/0.002 (604); p1 0.827/0.166/0.007 (668); p2 0.791/0.203/0.006 (808); p3 0.756/0.239/0.004 (840); p4 0.844/0.152/0.005 (865); p5 0.822/0.163/0.015 (411); p6 0.824/0.168/0.008 (40)
- **careful**: p0 1.000/0.000/0.000 (597); p1 1.000/0.000/0.000 (751); p2 1.000/0.000/0.000 (901); p3 1.000/0.000/0.000 (981); p4 1.000/0.000/0.000 (987); p5 1.000/0.000/0.000 (248)
- **hand**: p0 —/—/— (0); p1 —/—/— (0); p2 —/—/— (0); p3 —/—/— (0); p4 —/—/— (0); p5 —/—/— (0); p6 —/—/— (0); p7 —/—/— (0); p8 —/—/— (0); p9 —/—/— (0); p10 —/—/— (0); p11 —/—/— (0); p12 —/—/— (0); p13 —/—/— (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 2627.8 / 276.8 | 0.23 / 0.16 | -0.08 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.06 / 0.06 | -0.00 ± 0.00 | 0.157 / 0.130 | -0.027 ± 0.004 | 0.059 / 0.062 | 0.001 / 0.000 | 0.062 / 0.067 | +0.005 ± 0.002 | 1.55 / 1.39 | -0.16 ± 0.05 |
| careful | 2604.2 / 259.2 | 0.27 / 0.18 | -0.08 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.10 / 0.10 | -0.00 ± 0.00 | 0.184 / 0.155 | -0.029 ± 0.006 | 0.075 / 0.080 | 0.001 / 0.000 | 0.055 / 0.059 | +0.004 ± 0.004 | 1.65 / 1.37 | -0.28 ± 0.06 |
| hand | 2436.2 / 613.5 | 0.82 / 0.85 | +0.03 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.14 / 0.14 | +0.00 ± 0.00 | 0.383 / 0.377 | -0.006 ± 0.006 | 0.173 / 0.188 | 0.021 / 0.000 | 0.098 / 0.090 | -0.008 ± 0.004 | 2.63 / 2.76 | +0.12 ± 0.10 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| direct | -0.07 ± 0.01 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.024 ± 0.004 | +0.005 ± 0.004 | +0.006 ± 0.002 |
| careful | -0.08 ± 0.02 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.030 ± 0.006 | +0.005 ± 0.003 | +0.004 ± 0.004 |
| hand | -0.07 ± 0.02 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.059 ± 0.005 | -0.012 ± 0.003 | -0.008 ± 0.003 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| direct | 0.400 / 0.120 | 0.47 / 0.48 | 0.043 / 0.177 | 0.00 / 0.00 | 0.49 / 0.49 | 0.402 / 0.324 |
| careful | 0.477 / 0.127 | 0.30 / 0.29 | 0.043 / 0.173 | 0.00 / 0.00 | 0.29 / 0.32 | 0.298 / 0.245 |
| hand | 0.527 / 0.194 | 0.10 / 0.14 | 0.041 / 0.129 | 0.00 / 0.00 | 0.10 / 0.11 | 0.317 / 0.214 |

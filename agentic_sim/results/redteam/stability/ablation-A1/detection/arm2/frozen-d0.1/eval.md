# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --arm 2 --dispute-policy truthful --dispute-rate 0.1`, seeds 21-40, hide ``, model `None` (value off, horizon 8)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 30487.2 ± 693.0 | -91.3 ± 754.1 | 3064.2 | 0.975 | 0.024 | 0.000 | 0.018 | 0.019 | 0.043 | 0.160 | 4.80 | 12.15 | 0.60 |
| careful | 30578.5 ± 847.0 | nan ± nan | 3086.2 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.046 | 0.000 | 2.05 | 0.00 | 0.40 |
| hand | 30124.6 ± 380.4 | -453.9 ± 819.7 | 3401.0 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.074 | 0.000 | 3.55 | 0.00 | 0.65 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| direct | 0.018 (5409) [rej. blind 0.001] / 0.019 (53225) [rej. blind 0.000] | — / 0.500 (2) | 0.257 (759) / 0.120 (1890) [rej. blind 0.003] | — / — |
| careful | 0.000 (5493) / 0.000 (53368) | — / 0.000 (2) | 0.000 (845) / 0.000 (2017) | — / — |
| hand | 0.000 (12591) / 0.000 (50403) | — / 0.000 (72) | 0.000 (2128) / 0.000 (2826) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| direct | 0.019 (5409) [rej. blind 0.001] / 0.019 (53225) [rej. blind 0.000] | — / 0.500 (2) | 0.257 (759) / 0.120 (1890) [rej. blind 0.003] | — / — | 3.2 ± 0.5 | +19 |
| careful | 0.000 (5493) [rej. blind 0.000] / 0.000 (53368) [rej. blind 0.000] | — / 0.000 (2) | 0.000 (845) / 0.000 (2017) | — / — | 3.6 ± 0.7 | +15 |
| hand | 0.071 (12591) [rej. blind 0.000] / 0.107 (50403) | — / 0.000 (72) | 0.000 (2128) / 0.007 (2826) | — / — | 2.0 ± 0.3 | +6329 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 0.838 | 0.957 | — (0) | — (0) | 0.085 (5710) | 0.039 (155) | 0.018 (55420) | 24.850 | 657.450 | 1.183 | 0.489 |
| careful | — | 0.947 | — (0) | — (0) | 0.000 (6799) | 0.000 (245) | 0.000 (54681) | 24.400 | 641.000 | 1.161 | 0.000 |
| hand | — | 0.999 | — (0) | — (0) | 0.000 (4) | 0.000 (800) | 0.000 (67216) | 31.400 | 334.800 | 1.186 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| direct | 39.500 | 0.000 | 0.000 | 0.000 | 0.000 | 0.600 | 0.000 |
| careful | 39.300 | 0.000 | 0.000 | 0.000 | 0.000 | 0.400 | 0.000 |
| hand | 39.450 | 0.000 | 0.000 | 0.000 | 0.000 | 0.650 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 21.050 / 39.500 | 4.800 ± 0.479 | +2.750 ± 0.688 | 12.950 | +1.850 ± 1.091 | 3.550 | 0.072 | 5.350 | +0.250 ± 0.611 | 1950.650 | 0.020 | +0.004 ± 0.001 | 3.750 / 2.900 (3.750 / 2.900) | 19578.122 ± 363.456 | +185.144 ± 303.366 | 30487.2 ± 693.0 | -91.3 ± 754.1 | 38.285 | +0.145 ± 0.381 | 13.982 ± 0.286 | +0.141 ± 0.478 | 16.307 | 0.000 | 2665.800 | 19.500 | 18.450 | +0.000 ± 0.384 | 1003.643 | 192.950 |
| careful | 20.850 / 39.300 | 2.050 ± 0.328 | — | 11.100 | — | 3.250 | 0.063 | 5.100 | — | 1927.350 | 0.017 | — | 2.550 / 2.450 (2.550 / 2.450) | 19392.978 ± 274.913 | — | 30578.5 ± 847.0 | — | 38.140 | — | 13.842 ± 0.400 | — | 16.419 | 0.000 | 2673.650 | 19.300 | 18.450 | — | 986.511 | 229.100 |
| hand | 18.150 / 39.450 | 3.550 ± 0.420 | +1.500 ± 0.484 | 55.050 | +43.950 ± 1.953 | 7.750 | 0.050 | 11.950 | +6.850 ± 0.769 | 1965.750 | 0.038 | +0.022 ± 0.001 | 7.200 / 6.900 (7.200 / 6.900) | 26095.478 ± 333.400 | +6702.501 ± 353.826 | 30124.6 ± 380.4 | -453.9 ± 819.7 | 32.851 | -5.289 ± 0.406 | 19.170 ± 0.328 | +5.328 ± 0.574 | 18.475 | 0.003 | 2519.950 | 19.450 | 21.300 | +2.850 ± 0.365 | 78.830 | 353.600 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **direct**: p0 0.995/0.004/0.000 (558); p1 0.989/0.011/0.000 (550); p2 0.975/0.024/0.001 (563); p3 0.969/0.030/0.000 (575); p4 0.967/0.032/0.000 (577); p5 0.933/0.066/0.001 (234); p6 0.945/0.055/0.000 (7)
- **careful**: p0 1.000/0.000/0.000 (558); p1 1.000/0.000/0.000 (545); p2 1.000/0.000/0.000 (558); p3 1.000/0.000/0.000 (566); p4 1.000/0.000/0.000 (584); p5 1.000/0.000/0.000 (254); p6 1.000/0.000/0.000 (17); p7 1.000/0.000/0.000 (3)
- **hand**: p0 —/—/— (0); p1 —/—/— (0); p2 —/—/— (0); p3 —/—/— (0); p4 —/—/— (0); p5 —/—/— (0); p6 —/—/— (0); p7 —/—/— (0); p8 —/—/— (0); p9 —/—/— (0); p10 —/—/— (0); p11 —/—/— (0); p12 —/—/— (0); p13 —/—/— (0); p14 —/—/— (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 2661.2 / 270.4 | 0.10 / 0.05 | -0.05 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.06 / 0.07 | +0.02 ± 0.00 | 0.077 / 0.062 | -0.014 ± 0.005 | 0.022 / 0.031 | 0.000 / 0.000 | 0.059 / 0.066 | +0.006 ± 0.004 | 1.35 / 1.26 | -0.10 ± 0.06 |
| careful | 2668.4 / 274.6 | 0.11 / 0.06 | -0.05 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.07 / 0.07 | +0.01 ± 0.00 | 0.096 / 0.076 | -0.020 ± 0.005 | 0.029 / 0.030 | 0.000 / 0.000 | 0.060 / 0.070 | +0.010 ± 0.003 | 1.35 / 1.23 | -0.13 ± 0.05 |
| hand | 2520.2 / 629.5 | 0.55 / 0.58 | +0.03 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.12 / 0.11 | -0.01 ± 0.00 | 0.341 / 0.335 | -0.006 ± 0.005 | 0.149 / 0.158 | 0.003 / 0.000 | 0.114 / 0.123 | +0.010 ± 0.003 | 2.24 / 2.23 | -0.01 ± 0.04 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| direct | -0.05 ± 0.02 | +0.00 ± 0.00 | +0.02 ± 0.00 | -0.015 ± 0.005 | +0.008 ± 0.003 | +0.006 ± 0.004 |
| careful | -0.05 ± 0.01 | +0.00 ± 0.00 | +0.01 ± 0.00 | -0.018 ± 0.005 | +0.001 ± 0.002 | +0.009 ± 0.003 |
| hand | -0.02 ± 0.02 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.040 ± 0.005 | -0.008 ± 0.003 | -0.001 ± 0.003 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| direct | 0.000 / 0.000 | 0.00 / — | 0.040 / 0.164 | 0.00 / 0.00 | 0.14 / 0.11 | 0.947 / 0.190 |
| careful | 0.000 / 0.000 | 0.50 / — | 0.040 / 0.166 | 0.00 / 0.00 | 0.14 / 0.12 | 0.926 / 0.178 |
| hand | 0.001 / 0.000 | 0.15 / — | 0.039 / 0.113 | 0.00 / 0.00 | 0.07 / 0.08 | 0.983 / 0.059 |

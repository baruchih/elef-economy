# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1 --pi-a0 0.10 --pi-a-max 0.10`, seeds 21-40, hide ``, model `/Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/ablation-A1/stress/learned/pa10-t1-b1/wm/models/wm-online-10.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:greedy:0.75 | 31589.6 ± 491.5 | nan ± nan | 4695.1 | 0.817 | 0.000 | 0.000 | 0.188 | 0.241 | 0.370 | 0.104 | 15.05 | 119.60 | 0.45 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:greedy:0.75 | 0.188 (13444) / 0.241 (45673) | 0.113 (5662) / 0.133 (21271) | 0.018 (4248) [rej. blind 0.000] / 0.021 (3605) [rej. blind 0.000] | — / — |

The stressed world's fourth action by seat kind — the allowance claimed and the verdict F without inspecting (counted above among the blind verdicts; the ledger sees a careful review, so the measured reading below cannot see it):

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:greedy:0.75 | 0.188 (13444) / 0.241 (45673) | 0.113 (5662) / 0.133 (21271) | 0.018 (4248) / 0.021 (3605) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| mix:greedy:0.75 | 0.000 (13444) / 0.000 (45673) | 0.000 (5662) / 0.000 (21271) | 0.000 (4248) [rej. blind 0.000] / 0.000 (3605) [rej. blind 0.000] | — / — | 0.7 ± 0.1 | -17129 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:greedy:0.75 | — | 1.000 | — (0) | — (0) | 0.000 (25) | 0.000 (41) | 0.000 (93837) | 45.100 | 247.500 | 1.673 | 2.652 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| mix:greedy:0.75 | 39.700 | 0.000 | 0.000 | 0.000 | 0.000 | 0.450 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:greedy:0.75 | 16.600 / 39.700 | 15.050 ± 1.448 | — | 114.850 | — | 6.850 | 0.249 | 25.400 | — | 1879.300 | 0.071 | — | 0.000 / 0.000 (0.000 / 0.000) | 30082.880 ± 308.234 | — | 31589.6 ± 491.5 | — | 29.941 | — | 22.230 ± 0.255 | — | 20.025 | 0.048 | 2193.300 | 19.700 | 23.100 | — | 69.574 | 112.650 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **mix:greedy:0.75**: p0 1.000/0.000/0.000 (380); p1 1.000/0.000/0.000 (276); p2 1.000/0.000/0.000 (251); p3 1.000/0.000/0.000 (271); p4 1.000/0.000/0.000 (277); p5 1.000/0.000/0.000 (264); p6 1.000/0.000/0.000 (278); p7 1.000/0.000/0.000 (298); p8 1.000/0.000/0.000 (290); p9 1.000/0.000/0.000 (301); p10 1.000/0.000/0.000 (292); p11 1.000/0.000/0.000 (282); p12 1.000/0.000/0.000 (254); p13 1.000/0.000/0.000 (120); p14 1.000/0.000/0.000 (6)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:greedy:0.75 | 2283.7 / 672.2 | 1.37 / 1.71 | +0.34 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.10 / 0.10 | -0.01 ± 0.00 | 0.536 / 0.602 | +0.065 ± 0.005 | 0.303 / 0.351 | 0.047 / 0.000 | 0.159 / 0.183 | +0.023 ± 0.004 | 3.13 / 3.45 | +0.32 ± 0.05 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| mix:greedy:0.75 | +0.05 ± 0.02 | +0.00 ± 0.00 | -0.03 ± 0.00 | -0.048 ± 0.003 | -0.023 ± 0.003 | +0.003 ± 0.004 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| mix:greedy:0.75 | 0.456 / 0.264 | 0.35 / 0.37 | 0.027 / 0.075 | 0.00 / 0.00 | 0.33 / 0.33 | 0.424 / 0.248 |

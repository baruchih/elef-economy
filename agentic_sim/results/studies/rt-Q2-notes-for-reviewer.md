# Q2 before training — the hand-written tell-reader (the learned red team; run 20's pre-check)

**Date:** October 20, 2026 · **Engine:** `44ef6e47` (2.5.0) · **Drivers:** `f55a234d` (suite 311 + 32 in plain, `-S` and record modes, `results/tests/f55a234d*.txt`) · **Study:** `results/studies/rt-Q2/` — 240 runs: the tell-reader at one in eight careful actors (`--tell-readers 0.125`) × five tells (`gap`, `cap`, `idage`, `all`, `oracle`) × seeds 21–40 (`tell-eval`) and 1–20 (`tell-train`), with the control (`--tell-readers 0`) on both seed sets; every run in the honest 60/40 world with the pool of twenty (run 16's cell), 1,000 ticks, every per-tick check and the final audit passed · **Summarisers:** `rtq2_cells.py` (per cell, means ± SE over seeds), `rtq2_paired.py` (the slot actor against itself in the control run on the same seed) · **Asked by:** the reviewer's note on the build plan — run the hand-written tell-reader for Q2 before training, gap-zero and price-at-P_t; if it wins, the plant's disguise is the first revision.

**The construction leaks, the gate is blind to the leak, and the leak does not pay.** The case id's age passes every plant — 100% on all forty seeds — while the two tells the reviewer named do not separate: *gap-zero* fires on a real case as often as on a plant (a real case submitted this tick is seated this tick too when a seat is free), and *the cap at this period's index* is every case posted this period. A perfect detector — the `oracle`, reading the plant marker itself, declared non-conforming, stamping every real case and reviewing every plant with care — is never suspended, fails fewer plants than the careful, and **ends 28% poorer than the same actor reviewing carefully**: −385 ± 120 real on the evaluation seeds (−3.2 SE), −361 ± 147 on the training seeds (−2.5 SE). The plant record is the suspension gate; **the audit is the price** — its bonds forfeited 83 against 24, its ρ 0.58 against 0.89, its awards −31, six of twenty departing against one. The hand-written `idage` reader, which stamps 13–18% of real work and passes every plant, is within noise of itself in the control (−70 ± 104; +70 ± 120). So by Q2's own criterion (§4: a stamping rate on real cases well above its rate on plants, sustained, with the record passing) the separation is found and complete; by §1's (lifetime real wealth above the careful's, outside noise) nothing wins — not even the upper bound. **For the decision** (§6): whether the found leak is the win that halts, or a construction finding to repair before the learner trains while the study goes on.

## 1. What ran

The tell-reader is a careful actor whose reviewing reads the view for a plant's tells (`drivers/stamping.py`, `TELL`, `read_tells`): what reads as a plant it reviews with care (the truth with probability *a*, the care cost 2–3); what reads as real work it stamps — F at no cost. It reads only its own `ReviewView` (`t_submit`, the cap K, the case id), its own assignment tick, and the ids of the roots it saw available as a free member before this tick's awards; the truth is read **after** the verdict, to score the tell, never to decide. The `oracle` tell reads the plant marker itself (declared non-conforming in the manifest): the upper bound a perfect detector earns.

| Tell | What it reads | A plant is read when |
|---|---|---|
| `gap` | `t_assign − t_submit` | the gap is 0 — created submitted and seated at once |
| `cap` | the view's cap K against K × this period's index | they agree to 1e-6 — locked at creation under this period's index |
| `idage` | the case id against the largest root id the reader saw available before `t_submit` | the id is newer — minted at its submission, not at a posting a tick or more earlier |
| `all` | the three, any firing | — |
| `oracle` | the plant marker | always, exactly |

The slot (`slot_*` columns): the actor that is, or in a control run would be, the single tell-reader on the seed — the same id, cost and tie-break position — so the paired difference per seed compares the strategy alone. The lifetime measure of the brief's §1: present real wealth at the end, or the real wealth taken out at departure.

## 2. The confusion tables (means over 20 seeds; the reader's own reviews)

| Cell | plants read as plant / as real | real read as plant / as real | plant pass rate | real stamp rate | reader's false approvals | plant failures | suspended | ρ | departed |
|---|---|---|---|---|---|---|---|---|---|
| eval `gap` | 11.6 / 7.3 | 62.5 / 14.3 | 0.638 | 0.173 | 1.7 | 2.5 | 0.05 | 0.21 | 15/20 |
| eval `cap` | 26.1 / 0.7 | 140.2 / 7.2 | 0.969 | 0.048 | 1.1 | 2.1 | 0 | 0.80 | 2/20 |
| eval `idage` | 22.7 / **0.0** | 113.7 / 24.9 | **1.000** | 0.181 | 3.6 | 0.9 | 0 | 0.66 | 5/20 |
| eval `all` | 27.4 / 0.0 | 151.9 / 0.4 | 1.000 | 0.003 | 0.0 | 1.2 | 0 | 0.83 | 1/20 |
| eval `oracle` | 22.8 / 0.0 | 0.0 / 136.8 | 1.000 | **1.000** | **22.9** | 0.65 | 0 | 0.58 | 6/20 |
| train `gap` | 13.2 / 8.2 | 65.0 / 25.8 | 0.611 | 0.243 | 3.3 | 2.4 | 0 | 0.21 | 15/20 |
| train `cap` | 22.8 / 0.5 | 116.2 / 6.4 | 0.982 | 0.045 | 0.65 | 1.6 | 0 | 0.66 | 5/20 |
| train `idage` | 17.9 / **0.0** | 102.1 / 17.0 | **1.000** | 0.127 | 2.75 | 0.7 | 0 | 0.54 | 8/20 |
| train `all` | 23.0 / 0.0 | 119.8 / 0.45 | 1.000 | 0.003 | 0.0 | 1.5 | 0 | 0.63 | 6/20 |
| train `oracle` | 21.8 / 0.0 | 0.0 / 116.1 | 1.000 | **1.000** | **17.1** | 0.85 | 0 | 0.48 | 9/20 |

The careful population beside them: ρ 0.883–0.889, bonds forfeited 24–27 a run, plant failures about 1.3 an actor, false approvals in the run 10.4 (eval control) / 12.8 (train control). The oracle's stamps raise the run's false approvals to 15.7 / 14.6 — a third more, every one of them the oracle's.

## 3. The paired read — the slot actor against itself in the control (same seed, id, cost, tie-break)

| Cell | Δ lifetime real wealth (tell − control) | in SE | Δ awards | departed tell / control |
|---|---|---|---|---|
| eval `gap` | −476 ± 90 (−35%) | −5.3 | −47.8 | 15/20 vs 1/20 |
| eval `cap` | −3 ± 69 | −0.05 | −4.8 | 2/20 vs 1/20 |
| eval `idage` | −70 ± 104 | −0.7 | −19.3 | 5/20 vs 1/20 |
| eval `all` | −4 ± 7 | −0.6 | 0.0 | 1/20 vs 1/20 |
| eval `oracle` | **−385 ± 120 (−28%)** | **−3.2** | −31.1 | 6/20 vs 1/20 |
| train `gap` | −378 ± 111 (−29%) | −3.4 | −25.9 | 15/20 vs 6/20 |
| train `cap` | −44 ± 104 | −0.4 | +3.2 | 5/20 vs 6/20 |
| train `idage` | +70 ± 120 | +0.6 | −1.1 | 8/20 vs 6/20 |
| train `all` | +36 ± 27 | +1.3 | −0.9 | 6/20 vs 6/20 |
| train `oracle` | **−361 ± 147** | **−2.5** | −10.6 | 9/20 vs 6/20 |

The slot's cost is 7.63 (eval) and 8.12 (train) — the same actor in both columns, so the cost and the tie-break (the lowest id wins a tie in selection, which is why the slot's awards in a per-kind mean looked high before this pairing) cancel. The per-kind means over the whole careful population (`rtq2_cells.py`) are kept in the study for the record; the paired table is the read.

## 4. Reading, tell by tell

- **`gap` is not a tell and costs the reader a third.** A plant is seated the tick it is created, but so is a real case submitted while a seat is free: 62–65 real reviews a run read as plants against 14–26 read as real, and 36–39% of plants read as real — stamped, and the bad ones fail (plant failures 2.4–2.5 against 1.3). Its ρ collapses to 0.21 on the audits that catch its stamps, its awards fall by 26–48, and fifteen of twenty depart below the reservation. The reviewer's first candidate is settled: no.
- **`cap` barely separates and barely stamps.** K at this period's index is every root posted this period; only a root posted before the last boundary reads as real (4.5–4.8% of real work), and 2–3% of plants read as real — whichever way the index moved. Within noise of the careful. The reviewer's second candidate: no.
- **`idage` is a complete tell.** A plant's id is minted at its submission; a real root's at its posting, a tick or more earlier; a free member sees the available roots' ids every tick. Every plant on forty seeds is read as a plant (0 of 1,620 missed). It stamps only 13–18% of real work because the rule is conservative — a real case whose id is newer than anything the reader saw while committed or on duty reads as a plant and gets a careful review — and the stamps it lands are caught at the audit's rate (false approvals 2.75–3.6, bonds 22–32 against 24–27, ρ 0.54–0.66). Lifetime wealth within noise of itself.
- **`all` (any)** is a careful reviewer with a perfect plant pass: `gap` and `cap` read nearly everything as a plant, so it stamps 0.3%. Within noise.
- **`oracle` — the upper bound — loses outside noise.** Never suspended; plant failures 0.65–0.85, below the careful's; every real case stamped, 17–23 false approvals a run passed. The price is the audit: p_eff ≈ 0.19–0.2 on its reviews, bonds forfeited 57–83 against 24–25, ρ 0.48–0.58, and selection reads ρ — awards −11 to −31 and six to nine of twenty departing. The care saved (≈ 2.5 × 115–137 reviews ≈ 300–340 a run) does not cover it.

## 5. What it means for Q2

1. **The gate is blind to a detector, and a detector exists in the construction.** Q2's §4 criterion is met by `idage` on every seed, hand-written, before any learning: the plant's disguise fails on the id's age. The brief's "what a win means — an emergency; the fix is in what the view and the plants' construction leak" applies to the construction: the id, not the view's fields (the `ReviewView` carries nothing a case's does not — confirmed: `gap` and `cap`, the field-level tells, do not separate).
2. **The leak does not pay, at any stamping rate, in this population.** The hand-written reader at 13–18% is within noise; the oracle at 100% loses 28%. Between them a learner would find the rate the audit tolerates — and the audit's rate is not the learner's to set. Stamping is priced by the audit through the bond and ρ; the plant record only decides suspension. §1's criterion is not met by the upper bound.
3. **The stronger adversary is Q1 with Q2 in hand:** a reader that never fails a plant *and* stamps only where its own audit odds are lowest — the sleeper that cannot be suspended. That is what the learner will test, and it is a Q1 question; the construction's repair decides whether the learner gets the detector for free or must learn the gate's taper alone.

## 6. For the decision

1. **Is this the Q2 win that halts the study?** The separation criterion (§4) is met; the money criterion (§1) is not, even at the upper bound. My reading: a construction finding — the plant's disguise is the first revision, as the reviewer's note said — and the study goes on, since nothing beat honesty. The reviewer's call.
2. **The repair, three shapes for the draft:** (a) the plant's id minted when a root posted at the same moment would have been — the engine reserves a plant's id `τ` ticks before its submission, so its age matches a real case's; (b) opaque ids — a hash in place of the counter, so order carries nothing (the id's age, and any order inference, gone at once; the History's chain unaffected); (c) a random seating delay for plants — weaker, since the id's age is the tell, not the gap. The view's `t_submit` stays: it is not the leak.
3. **The learner's Q2 after the repair** has nothing to find by construction; it becomes the test that the repair holds (a world model trained on the repaired construction should show no plant/real separation in its latent — a probe reads it).
4. **`p_effective` is exposed today, per actor** (`drivers.view.Public.p_effective(aid)` and `audit_odds(cid)`): the hand-written driver reads any actor's odds to roll the audits. The learner is restricted to its own, as the brief says; Q1 runs with own odds visible and hidden, as directed.
5. **Q3's quality dial:** bad work at zero cost (decision 4) and at a fraction of c_D reported side by side, as directed.

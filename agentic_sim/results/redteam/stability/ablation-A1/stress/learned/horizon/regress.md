# The regression at a horizon of 1 (I5's first test) — the pin's chain of record at ffd23d851

**(a) The target at a horizon of 1 is the stored reward.** 270 files, 896223 decisions of the chain's data (the offline set and the ten rounds): the largest difference 0 — identical.

**(b) Stored episodes replayed by their recorded actions on the environment as built:** the attributed reward against the stored `reward` (float32), the export beside.

| episode | decisions replayed / stored | max |attributed − stored| | unclaimed (sum, real) | pre-boundary (real) | suspension charges (sum) | decisions charged |
|---|---|---|---|---|---|---|
| careful-seed1.npz | 4717 / 4717 | 4.76e-07 | 12153.5 | 12973.5 | 0.0 | 0 |
| eps4-seed2.npz | 4356 / 4356 | 9.19e-07 | 13444.8 | 14312.1 | -107.7 | 6 |
| online10-seed3.npz | 3245 / 3245 | 1.35e-06 | 14823.9 | 15699.1 | -52.3 | 3 |

The attribution is unchanged within float32 (every difference under 1e-3).

**(c) The direct policy refit at a horizon of 1, the code as built against the code of record (f9c0dbb3e), on the chain's data, torch seed 0, six epochs, on the CPU:** the weights identical, tensor for tensor (9 tensors; 51 s / 50 s).

**The world model's trainer the same** (seeds 1–3, two epochs, horizon 16, the value head, two heads, stride 8, on the CPU): the weights identical, tensor for tensor (67 tensors).

**Verdict:** passed — a horizon of 1 reproduces the chain of record: the same targets, the same attribution, the same fit.

# A seed's episode depends on the platform — where, and why one bit is enough (November 7, 2026)

*The record's reviewer 1 ran the plain driver from the `5186c18f6` archive on Linux x86-64 — seed 21, `--entry-pool 20 --stampers 0.6`, 1,000 ticks — and read 9 standing false approvals where the record's macOS arm64 machine reads 12, with the posted, vested and final counts differing too (the record's draft 12, S73). The question put to the economy's implementer: where in the engine does a seed's episode depend on the platform, and which platform were the recorded runs made on? Notes §76 carries the answer; this folder is its evidence.*

## The answer in one paragraph

Every recorded run was made on this machine: all 12,385 run manifests under `results/` record `macOS-26.5.1-arm64-arm-64bit-Mach-O`, and so were the suite's results files and the goldens. The site is the engine's one transcendental call, `Params.emission`: `E0 * 2.0 ** (-t / H)`, the C library's `pow`. Apple's libm returns a value more than half a unit in the last place from the true one at three of the thousand arguments a 1,000-tick run uses (t = 112, 181 and 338); glibc's at one (t = 338, the same value as Apple's). So the two platforms' emission differs by one unit in the last place at ticks 112 and 181 — about 10⁻¹⁶ of the ten credits a period's emission starts from. One bit is enough because the emission share is paid as a ledger event whose `amount` is hashed into the History, and the engine's seed-free draws are keyed on the History head: `_plant_draw` (a plant's ceiling ratio, its time to submission, a planted approval's public odds), the plant alias names, the plant nonces and the state's verdict coin on a plant. The first plant posted after the settlement batch of tick 181 draws a different ceiling, and the episode diverges from there. On seed 21 the three platforms' History heads are identical through tick 181 and part at tick 181's batch (`first-divergence.txt`: the head logged after `advance` at 182); the batch at 112, if any, paid no emission on that seed.

## What was run

- `summary-lines.txt` — the driver's summary line at `5186c18f6` on macOS arm64 (four Pythons, four hash seeds: identical), on Linux arm64 and Linux x86-64 (`python:3.12-slim` containers, glibc 2.41): the Linux lines are reviewer 1's to the digit (`posted=2372 vested=1849 final_N=496 false_approvals=9 false_rejections=31 …`); then macOS with the emission's power correctly rounded (a third episode: 11 false approvals, posted 2,361) and with it nudged one ulp up or down (17 and 8).
- `nudge_runner.py` — reviewer 1's test extended: `exp`, `log`, `cos`, `sin` (the `math` functions and `random`'s bound copies) nudged one ulp either way leave the macOS line unchanged, as reviewer 1 found on Linux; the emission's power nudged alone moves it. The driver's cost draw `c_d_median · exp(gauss)` is rounded to four decimals and the dial's gain is 1.0 (`x ** 1.0` is exact in every libm), so the power is the engine's only libm-dependent number.
- `pow_check.py`, `pow-mismatch.txt` — the platform's `2.0 ** (-t/1000)` against the correctly rounded double (decimal at 60 digits) over the thousand ticks, on each platform.
- `emission_runner.py`, `heads-*.txt` — the History head after every tick, native or with the power correctly rounded (decimal at 40 digits, then the double product `E0 · p` as the engine computes it); `first-divergence.txt` the first tick the heads differ, pairwise.
- `suite-linux-arm64-5186c18f6.txt` — the suite at `5186c18f6` inside the Linux container: 369 passed, **4 failed**, 32 expected failures. The four are the goldens (`test_perf_equivalence`'s two seeds and `test_record_mode`'s two): the 200-tick golden scenario pays emission at tick 112 or 181, so the History heads pinned on macOS do not hold on Linux. Everything else passes.
- `suite-macos-main-cr-emission.txt` — the suite at main (`c3746e0ff`) on macOS with the emission's power computed correctly rounded: the same four failures, nothing else — the blast radius of the fix below is the goldens alone.

## Classification and the proposed correction

An implementation effect (spec §18.2), the engine's: no rule is misapplied and no rule moves. The recorded runs and every figure on record are Apple's episodes at their commits and reproduce on macOS arm64; a reader re-running them on glibc gets the same code's neighbouring episode from the first emission-paying batch at tick 112 or 181 on — the same picture, not the same episode, which is how reviewer 1 reads its scripted figures.

Proposed, **not landed** (it re-pins the goldens once and changes every seed's episode from the fixing commit on, so it is the reviewer's and Baruchi's call): compute the emission's power correctly rounded —

```python
def emission(self, t: int) -> float:
    from decimal import Decimal, localcontext
    with localcontext() as ctx:
        ctx.prec = 40
        return self.E0 * float(Decimal(2) ** Decimal(-t / self.H))
```

— the spec's formula exactly rounded, identical on every platform and under `python3 -S` (`decimal` is the standard library's). After it a run reproduces anywhere; the runs before it reproduce on macOS arm64 at their commits, as they do now. Rounding the emission to a fixed number of decimals was considered and set aside (a value within an ulp of a rounding boundary would still differ); so was pinning Apple's three values (a platform's error written into the rule).

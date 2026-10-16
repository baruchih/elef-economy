# External reviews R01–R10

One review per version, by an external reviewer (GPT-6 Pro), each supplied as a report and — from R03 on —
a bundle of regression tests that were copied **verbatim** into `agentic_sim/tests/test_review*.py`.
The `_notes.md` files are the reviewer's shorter cover notes where they were shared separately.

| File | Of | Found | Closed in |
|---|---|---|---|
| R01_of_v0_2.md | v0.2 | funding gap; bond vs liability; stamping-deterrence overclaim | v0.3 |
| R02_of_v0_3.md | v0.3 | payout after shortfall; indexing | v0.4 |
| R03_of_v0_4.md | v0.4 + first engine | atomicity, occupancy, replacement, cost units, Ω claims; nested denomination; kill-fee basis; two-question ⊥ appeal — 20 tests (`test_review_regressions.py`) | v0.5 |
| R04_of_v0_5.md | v0.5 | 13 interaction defects (`test_review2_interactions.py`) | v0.6 |
| R05_of_v0_6.md | v0.6 | 10 boundary defects + 4 controls (`test_review3_boundaries.py`) | v0.7 |
| R06_of_v0_7.md | v0.7 | 7 follow-through defects + 6 controls (`test_review4_followthrough.py`) | v0.8 |
| R07_of_v0_8.md (+notes) | v0.8 | correction logic; identical views, different admissible answers — 7 + 10 (`test_review5_contracts.py`) | v0.9 |
| R08_of_v0_9.md (+notes) | v0.9 | 16 of 25 checks failed, all from audit reopening (`test_review6_reopening.py`) | v0.10 withdrew reopening |
| R09_of_v0_10.md (+notes) | v0.10 | no new execution defect; "blindness stands" overclaimed; freeze + consolidate | v1.0 |
| R10_of_v1_0.md | v1.0 | four wording errata | v1.0.1 Appendix E |

The reviewers' test bundles themselves are not in this repo — they arrived as separate archives and were copied
into `agentic_sim/tests/test_review*.py` at the time; the reports name the tests they shipped, so names and
counts can be compared, but byte-for-byte verbatimness cannot be re-verified from this repo alone.

R03's "case 12" is the one original expected failure (single-answer ⊥ appeal). R07's identical-views test
(four parameters) is superseded by the view contract. R08's nineteen reopening-dependent runs are expected
failures on a withdrawn path. All reasons are stated in `agentic_sim/run_tests.py`.

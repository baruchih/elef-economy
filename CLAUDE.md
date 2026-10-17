# Agentic-OS — the economic loop

A rulebook for a task → verification → dispute → settlement loop among autonomous actors, and a
reference implementation of it with no strategies. Ten external reviews. The rulebook is at **1.1.0**:
the frozen 1.0.1 baseline plus one design revision (the verification deposit is two pots, §4.3),
made under §19 after the first scoped run showed careful review paid for its own care. Read
`HANDOFF.md` first for where things stand and what is proposed next.

## Layout

```
spec/agentic_economics_loop_spec_v1_1_0.md   the text in force (standalone; Appendix A defaults, E errata, F design revision 1)
spec/design_revisions/                       accepted design revisions, verbatim (dr1: two pots, 1.1.0-rc.3)
spec/history/                                v0.1 … v1.0.1 — superseded, kept for provenance only
reviews/                                     R01–R10, one external review per version, with the reviewer's notes
agentic_sim/                                 the engine, 19 invariants, 18 test files, runner, drivers, results
docs/line_map_economic_loop_v1_0_1.txt       text export of the _line map of the loop (the live map is the source)
HANDOFF.md                                   status, history table, open questions, proposed next step
```

## Commands

```
cd agentic_sim
python3 run_tests.py        # expected: 181 passed, 0 failed, 25 expected failures
python3 -S run_tests.py     # same, with no site-packages
python3 -m pytest tests -q  # expected: 181 passed, 25 xfailed, 0 xpassed (conftest mirrors the runner)
python3 -m drivers.load_run --actors 200 --ticks 10000 --on-duty 40 --tasks 30 --record-dir /path  # throughput run
python3 -m drivers.stamping --actors 20 --ticks 1000 --stampers 0.5 --seed 1   # §18.1 q1, careful vs stamping
python3 -m drivers.stamping --on-duty 8 --fee 4 --seed 1                       # the 1.1.0 rerun's other cells
```

Drivers hold a `drivers.view.Public`, not the `World`: that class lists the operations a driver may
call. A driver that needs something not on it has found a conformance bug or a design question.

Results are kept (`drivers/results.py`): the runner writes what it printed to `results/tests/<commit>.txt`
(one file per commit, `-dirty` when the tree differs from it); every run writes
`results/runs/<run-id>/` with `manifest.json` (engine commit, params, declared operations, outcome),
`metrics.csv` and `fingerprint.json`. Commit the ones that matter. Results are written by the code and
read by people; the suite and the engine stay the authority — never edit a result to match.

Any other result is a regression — including an XPASS. The 25 expected failures each have a stated
reason in `run_tests.py` (`EXPECTED_FAIL`, with `EXPECTED_FAIL_PARAMS` naming the parameter runs inside a
mixed test): one original (a single-answer ⊥ appeal), four superseded by the reviewer-view contract,
nineteen on the withdrawn audit-reopening path, one superseded by design revision 1 (it pinned the
1.0.1 deposit through the human's budget; its principle is re-asserted in `test_v11`). They are strict in both entry points: an expected
failure that passes means a withdrawn path is admitted again, and the run fails.

## Change discipline — spec §19, and the one rule that matters most

Classify a finding before acting on it:

| Finding | What it warrants |
|---|---|
| The engine misapplies a rule, or a refused action has effects | Fix the engine, add a regression test. **The rules do not move.** |
| Two active rules demand contradictory outcomes | The smallest explicit rule decision, versioned and labelled as a design revision |
| A workflow that would be useful but is not offered | A proposal for a later design revision — not an obligation to support it now |
| A strategy performs badly, or an incentive looks wrong | An evaluation under the fixed rules — not a rule change |
| The consolidated wording says more or less than the decisions | Errata (as in v1.0.1 Appendix E) |

A conformance pass may change *how* a rule is applied; a change to *what participants may do* is a
design revision and is read on its own before it is implemented. v0.9 broke this once (an interface
finding answered with a state-machine expansion); the next review found sixteen consequences and the
change was withdrawn, not repaired. Do not repeat it.

While building strategy runs, the baseline stays frozen between revisions. Drivers live in
`agentic_sim/drivers/`, use only the public operations of `World`, and never reach into engine internals.
A design revision is a release candidate (`-rc.N`, not in force) until accepted; then the engine is
changed to it, the goldens are re-pinned once at the implementing commit, reviewer tests that pinned the
old figures become expected failures with that reason and their principle re-asserted, and the text is
consolidated into one standalone spec with the accepted revision kept verbatim in `spec/design_revisions/`.

## Conventions in `agentic_sim`

- Every action is validated whole before anything is recorded or moved. A refused action changes
  nothing — tests assert this against full world snapshots. Keep it that way for any new operation.
- Nineteen invariants run after every tick (`sim/invariants.py`). A failing invariant is an engine
  bug or a spec contradiction, never a property of a strategy. Two entry points, one set of
  predicates: `check_all` is the full audit from genesis (what tests call; scheduled in a run by
  `Params.full_check_every`); `check_tick` is what `advance` runs, the same predicates over the
  working set — cases and reviews that can still change, plus anything touched since the last tick.
  `tests/test_perf_equivalence.py` holds the proof that they agree and pins the engine's History head
  (re-pinned once for 1.1.0, since settlement changed). Keep new invariants in that shape: a predicate
  over an explicit scope.
  The per-tick check is not configurable: `advance` always runs it. `full_check_every` only adds
  the full audit on a cadence (0 = not scheduled; runs call `check_all` at the end), and
  `record_dir` only moves where the record is stored. `python3 run_tests.py --record` runs the
  whole suite in record mode as the storage layer's conformance check. The per-tick check is the
  incremental audit; the full audit is from genesis by definition, so scheduling it makes a run
  quadratic — strategy runs use the per-tick check plus one final `check_all`.
- The engine keeps every case and review ever created in `cases` and `reviews`, and a working set
  (`_live_cases`, `_live_reviews`) that the tick loop and `check_tick` read. A settled case leaves
  the working set and comes back through `_dirty_cases` when touched again. New engine code that
  mutates a case must do so through an operation that logs to the case or moves money on its
  account; that is what marks it dirty.
- With `Params.record_dir` set, the record lives on disk (`sim/record.py`): the History and the
  event copy are journals written through to files, and settled cases and reviews are paged out
  to archives, so RAM holds the working set. `w.cases[k]` makes an object resident (for code that
  may change it); `peek` and iteration give a read-only copy without pulling the archive in — the
  invariants use `_peek`, and new audit code must too. `check_all` streams the record in chunks.
  `tests/test_record_mode.py` proves the fingerprint is identical to the in-memory run and that
  the chain re-hashes from the file alone. Without `record_dir` nothing in `record.py` is used.
- Reviewer test files (`tests/test_review*.py`) are kept **verbatim**. Never edit one to make it
  pass; if a reviewer test must fail, add it to `EXPECTED_FAIL` with the reason, and mirror it in
  `tests/conftest.py`.
- No strategies in the engine. Every bid, verdict, appeal, audit roll, ruling and human action is
  injected by the caller; `sim/strategies.py` holds Protocols only.
- Defaults are in `sim/params.py` and spec Appendix A. Moving a default is not a design change;
  changing a rule is.
- The engine has no bid registry, no selection and no audit roll: `award` takes the chosen actor,
  and `p_audit` per reviewer is maintained but never rolled. Offers, S_θ with λ and the κ tie band,
  and the audit roll are the driver's — by design. A driver that skips the roll or reads `p_audit`
  dishonestly produces an implementation effect, not an economic one (spec §18.2).
- There is no enforced read-only facade on `World`; "public operations only" is a convention. Put a
  thin read-only view in `drivers/` so the rule is checkable.
- The `History` hash chain in `sim/ledger.py` is the authoritative record; wallet events and case
  logs are copies that invariant I16 checks for membership and order.
- The deposit is two pots (1.1.0 §4.3): the case pool's `deposit` field is the expense allowance φ^E
  (the 1.0.1 name is kept, reviewer tests read it) and `fee_pot` is φ^F. Expenses come from the
  allowance only; fixed fees `w_r · f_fee` from the pot; a nested case's reviews draw on its root's
  pool; the cross-pot step and the refund happen only at tree closure (`_maybe_close_tree`), and I10
  admits exactly those post-vesting movements by the event's note (`"nested …"`, `"tree closure…"`).
  I19 checks the pots per tick. A root with open pots stays in the working set until its tree closes.
- Money is checked by invariant I1 (conservation) — never silently create or lose credits.

## Vocabulary (spec Appendix C has the full notation)

F / N / P / ⊥ — fulfilled / not fulfilled / partially fulfilled / cannot assess. P and ⊥ are
responses to a submission, available only on the first review of an unrevised submission.
Pending — approved or appeal admitted, window open, actor's capacity released. Suspended — a challenge
or audit holds the case. Vested — financial finality. Ω — the orchestrator's operating account, a
revolving float. ρ reliability, κ duty credit. G guarantee, G^V reviewer bond, D court fee,
K reasonable-cost cap, φ = φ^E + φ^F verification deposit (expense allowance + fee pot), f the ordinary-review
fee (appeal and audit 1.5 f), β price ceiling, v_t credit value = Res_t / M_t.
"Ruling" has two senses: the orchestrator rules on splits inside the procedure; only a human
*overrides* it (spec §15.2).

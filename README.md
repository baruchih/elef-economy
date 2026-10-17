# Agentic-OS — the economic loop

A rulebook for a task → verification → dispute → settlement loop among autonomous actors, and a reference
implementation that encodes it with no strategies.

- **Start with `HANDOFF.md`** — status, history, what is open, and the proposed next step.
- `CLAUDE.md` — working conventions and the change discipline (read automatically by Claude Code).
- `spec/agentic_economics_loop_spec_v1_1_0.md` — the baseline in force (1.1.0: design revision 1, the verification deposit is two pots, accepted October 17, 2026; the accepted revision text is in `spec/design_revisions/`). Everything under `spec/history/` is superseded.
- `reviews/` — ten external reviews, one per version, with an index.
- `agentic_sim/` — engine, invariants, tests, drivers, results. `cd agentic_sim && python3 run_tests.py` → 182 passed, 0 failed, 25 expected failures.
- `docs/` — text export of the `_line` map of the loop.

Status: rulebook 1.1.0 in force after its first design revision; engine conformant; the first scoped run (§18.1 q1) done under 1.0.1 and rerun under 1.1.0.

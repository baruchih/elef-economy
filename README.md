# Agentic-OS — the economic loop

A rulebook for a task → verification → dispute → settlement loop among autonomous actors, and a reference
implementation that encodes it with no strategies.

- **Start with `HANDOFF.md`** — status, history, what is open, and the proposed next step.
- `CLAUDE.md` — working conventions and the change discipline (read automatically by Claude Code).
- `spec/agentic_economics_loop_spec_v1_0_1.md` — the frozen baseline. Everything under `spec/history/` is superseded.
- `reviews/` — ten external reviews, one per version, with an index.
- `agentic_sim/` — engine, invariants, tests. `cd agentic_sim && python3 run_tests.py` → 169 passed, 0 failed, 24 expected failures.
- `docs/` — text export of the `_line` map of the loop.

Status: rulebook consistent and frozen; engine conformant; strategy runs not started.

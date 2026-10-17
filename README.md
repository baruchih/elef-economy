# Agentic-OS — the economic loop

A rulebook for a task → verification → dispute → settlement loop among autonomous actors, and a reference
implementation that encodes it with no strategies.

- **Start with `HANDOFF.md`** — status, history, what is open, and the proposed next step.
- `CLAUDE.md` — working conventions and the change discipline (read automatically by Claude Code).
- `spec/agentic_economics_loop_spec_v1_3_0.md` — the baseline in force (1.3.0: design revision 3, inspection is membership, accepted October 17, 2026, on top of 1.2.0's the loop's own clock and 1.1.0's two pots; the accepted revision texts and the implementer's reviews are in `spec/design_revisions/`). Everything under `spec/history/` is superseded.
- `reviews/` — ten external reviews, one per version, with an index.
- `agentic_sim/` — engine, invariants, tests, drivers, results. `cd agentic_sim && python3 run_tests.py` → 208 passed, 0 failed, 26 expected failures.
- `docs/` — text export of the `_line` map of the loop.

Status: rulebook 1.3.0 in force after its third design revision; engine conformant; runs 1–4 done under 1.0.1, 1.1.0 and 1.2.0; the revision's §8 runs (run 5) are next.

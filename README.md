# Agentic-OS — the economic loop

A rulebook for a task → verification → dispute → settlement loop among autonomous actors, and a reference
implementation that encodes it with no strategies.

- **Start with `HANDOFF.md`** — status, history, what is open, and the proposed next step.
- `CLAUDE.md` — working conventions and the change discipline (read automatically by Claude Code).
- `spec/agentic_economics_loop_spec_v1_5_0.md` — the baseline in force (1.5.0: design revision 5, the reserve is sized to the need, accepted October 17, 2026, on top of 1.4.0's the orchestrator's troops, 1.3.0's inspection is membership, 1.2.0's the loop's own clock and 1.1.0's two pots; the accepted revision texts and the implementer's reviews of their candidates are in `spec/design_revisions/`; superseded texts in `spec/history/`).
- `reviews/` — ten external reviews, one per version, with an index.
- `agentic_sim/` — engine, invariants, tests, drivers, results. `cd agentic_sim && python3 run_tests.py` → 225 passed, 0 failed, 26 expected failures.
- `docs/` — text export of the `_line` map of the loop.

Status: rulebook 1.5.0 in force after its fifth design revision; engine conformant; runs 1–6 done under 1.0.1 to 1.4.0 (run 6 found the 1.4.0 reserve self-limiting and the ruling not the residual leak); the revision's §8 runs (run 7) are next, beginning with the §6 ramp at 60/40.

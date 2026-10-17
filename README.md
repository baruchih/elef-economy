# Agentic-OS — the economic loop

A rulebook for a task → verification → dispute → settlement loop among autonomous actors, and a reference
implementation that encodes it with no strategies.

- **Start with `HANDOFF.md`** — status, history, what is open, and the proposed next step.
- `CLAUDE.md` — working conventions and the change discipline (read automatically by Claude Code).
- `spec/agentic_economics_loop_spec_v1_6_0.md` — the baseline in force (1.6.0: design revision 6, auto-scale, accepted October 17, 2026, on top of 1.5.0's the reserve is sized to the need, 1.4.0's the orchestrator's troops, 1.3.0's inspection is membership, 1.2.0's the loop's own clock and 1.1.0's two pots; the accepted revision texts and the implementer's reviews of their candidates are in `spec/design_revisions/`; superseded texts in `spec/history/`).
- `reviews/` — ten external reviews, one per version, with an index.
- `agentic_sim/` — engine, invariants, tests, drivers, results. `cd agentic_sim && python3 run_tests.py` → 236 passed, 0 failed, 26 expected failures.
- `docs/` — text export of the `_line` map of the loop.

Status: rulebook 1.6.0 in force after its sixth design revision; engine conformant; runs 1–7 done under 1.0.1 to 1.5.0 (run 7 found the reviewing seat, not the treasury, capping the market); the revision's §8 runs (run 8) are next, beginning with one rule at a time against the 1.5.0 control.

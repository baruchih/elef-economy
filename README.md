# Agentic-OS — the economic loop

A rulebook for a task → verification → dispute → settlement loop among autonomous actors, and a reference
implementation that encodes it with no strategies.

- **Start with `HANDOFF.md`** — status, history, what is open, and the proposed next step.
- `CLAUDE.md` — working conventions and the change discipline (read automatically by Claude Code).
- `spec/agentic_economics_loop_spec_v1_7_1.md` — the baseline in force (1.7.1: 1.7.0 — design revision 7, the state's earnings, accepted October 18, 2026 — with the award summons read per request, a conformance correction ruled the same day; on top of 1.6.0's auto-scale, 1.5.0's the reserve is sized to the need, 1.4.0's the orchestrator's troops, 1.3.0's inspection is membership, 1.2.0's the loop's own clock and 1.1.0's two pots; the accepted revision texts and the implementer's reviews of their candidates are in `spec/design_revisions/`; superseded texts in `spec/history/`).
- `reviews/` — ten external reviews, one per version, with an index.
- `agentic_sim/` — engine, invariants, tests, drivers, results. `cd agentic_sim && python3 run_tests.py` → 248 passed, 0 failed, 26 expected failures.
- `docs/` — text export of the `_line` map of the loop.

Status: rulebook 1.7.0 in force after its seventh design revision; engine conformant; runs 1–8 done under 1.0.1 to 1.6.0 (run 8 found the panel rule the honesty gain and the troops' earnings paying the reviewers while Ω went broke on the clock's rebates — 1.7.0 moves the troops' surplus to Ω); run 7 found the reviewing seat, not the treasury, capping the market); the revision's §8 runs (run 9) are next, beginning with the three one-factor cells against the 1.6.0 control, plants unfunded read first.

"""The learned red team (the brief of October 20, 2026; the build plan `docs/red_team_build_plan.md`).

A separate package the engine, the drivers and the test runner never import. It needs the `elef-redteam` environment (Python 3.11,
torch, gymnasium, stable-worldmodel) — the project's own Python runs the suite without it. The learner is a driver: it reads the public
view and its own history, acts through the public operations, and is scored on its own lifetime real wealth.
"""

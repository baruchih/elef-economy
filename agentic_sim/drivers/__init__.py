"""Drivers: everything that decides. The engine in `sim/` applies rules; this package will hold
the task world, the policy populations, the run harness and the control (HANDOFF.md, "Where the
drivers should go"). Drivers use only `World`'s public operations.

`results.py` is the first piece: how a run is recorded, so that every run from the first is kept.
`load_run.py` is a throughput run with no economics in it, used to size the engine.
"""

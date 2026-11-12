# ELEF — the economic loop

ELEF (Agentic Economics) is a rulebook for a task → verification → dispute → settlement loop among autonomous
actors, and a reference implementation of it with no strategies in the engine. Work is posted, awarded, delivered,
reviewed, challenged and settled under rules that an orchestrator applies and a hash-chained ledger records; a
learned red team and hand-written populations then play the rules to find where they fail. The readable account
of the project — what it is, what was found, and what is still open — is at **https://elef.baruchih.com**.

## The rulebook in force

Rulebook **2.9.0** (design revision 17, *the plant takes the wrong step*, October 27, 2026) is the text in force:
`spec/agentic_economics_loop_spec_v2_9_0.md`, standalone, with its defaults in Appendix A, the errata in Appendix E
and the accepted design revisions and rulings in Appendices F–V. Every accepted revision is kept verbatim in
`spec/design_revisions/`, beside the implementer's review of each candidate; the superseded texts v0.1 … v2.8.0 are
in `spec/history/`, for provenance only. Rules move only by a design revision under the spec's §19; a conformance
correction changes how a rule is applied, never what participants may do.

## The results are not settled

The findings are evaluations under fixed rules, and the question that drove the last four revisions is still open:
a reviewer population learning in self-play against its own audits still approves blind at the audit seat about
half the time (the audit seat's remaining half-stamp), with 2.9.0's per-seat dial still moving. The runs, their
manifests and the notes written for the economy's reviewer are under `agentic_sim/results/`
(`results/studies/2.7.0-notes-for-reviewer.md` is the running record, §1–§108). Nothing here should be read as a
settled result; the website states what is settled and what is not, sentence by sentence against the record.

## Running the engine

```
cd agentic_sim
python3 run_tests.py        # 392 passed, 0 failed, 32 expected failures
python3 -S run_tests.py     # the same with no site-packages
python3 run_tests.py --record   # the same with every world in record mode (the storage layer's conformance check)
```

The engine needs Python 3.11 or later and nothing else. The 32 expected failures are reviewer tests pinned to
withdrawn or superseded figures, each with a stated reason in `run_tests.py`; an expected failure that passes is a
regression. The drivers (`agentic_sim/drivers/`) run the hand-written populations; `agentic_sim/README.md` documents
the engine and lists the command for every cell. The learned red team (`agentic_sim/redteam/`) needs a conda
environment with PyTorch, gymnasium and stable-worldmodel; the suite never imports it. Its trained policies are
PyTorch `.pt` files under `results/`, which load through pickle as PyTorch models do.

## The rest of the repository

- `reviews/` — ten external reviews of the rulebook, R01 of v0.2 to R10 of v1.0, one per version, with the
  reviewers' notes and an index. Later versions were reviewed by the economy's reviewer inside the record; those
  rulings are in the spec's appendices and in the notes.
- `docs/` — the reviewer's consolidated account of 2.0.0 → 2.5.0, the learned red team's brief and build plan, each
  with the implementer's review beside it, and a text export of the `_line` map of the loop.
- `CLAUDE.md` — the working conventions and the change discipline of the session that maintains the repository,
  published as they were used.
- `HANDOFF.md` — the handoff written on October 18, 2026 at rulebook 1.1.0 and extended through the 2.x work; kept
  as part of the record. The spec's own change log is the current status.

## Licence

MIT. The `LICENSE` file carries the text.

## Size, and how to clone

The repository tracks every result the record cites — about 78,000 files and 5.5 GB, nearly all of it under
`agentic_sim/results/` (`.npz`, `.csv`, `.pt` and `.json`). The history is not rewritten: the website and the
record cite commits by hash, so the results stay where they are. To read and run the text without the results:

```
git clone --filter=blob:none --sparse https://github.com/baruchih/elef-economy.git
cd elef-economy
git sparse-checkout set spec reviews docs agentic_sim/sim agentic_sim/drivers agentic_sim/tests agentic_sim/redteam
```

That checks out the spec, the reviews, the docs and the engine with its tests and drivers, and leaves
`agentic_sim/results/` on the server; the test suite runs from it. Or read the files on GitHub. Result files
record the paths of the machine they were made on, as the manifests always have.

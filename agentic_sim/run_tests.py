#!/usr/bin/env python3
"""Run every suite with plain Python: `python3 run_tests.py`.
With pytest installed, `python3 -m pytest -q` discovers the same files and reports the one
deliberate API-compatibility failure as XFAIL (see tests/conftest.py).

Suites:
  tests/test_spec.py                  §16 worked example and variants; exceptional paths from R1/R2
  tests/test_review_regressions.py    the third review's 20 regressions, verbatim
  tests/test_v05.py                   the v0.5 rules in explicit form
  tests/test_review2_interactions.py  the fourth review's 13 interaction tests, verbatim
  tests/test_v06.py                   the v0.6 repairs in explicit form
  tests/test_review3_boundaries.py    the fifth review's 10 boundary tests and 4 controls, verbatim
  tests/test_v07.py                   the v0.7 rules and repairs in explicit form
  tests/test_review4_followthrough.py the sixth review's 7 follow-through checks and 6 controls, verbatim
  tests/test_v08.py                   the v0.8 rules and repairs in explicit form
  tests/test_review5_contracts.py     the seventh review's 7 checks and 10 controls, verbatim
  tests/test_v09.py                   the v0.9 rules and repairs in explicit form (reopening withdrawn)
  tests/test_review6_reopening.py     the eighth review's 25 checks, verbatim; the reopening-dependent ones are
                                      expected failures (the rule was withdrawn), its controls pass
  tests/test_v10.py                   the withdrawal of reopening, asserted directly
  tests/test_v101.py                  withdrawing an unawarded request, the one permitted operation no suite had exercised
  tests/test_perf_equivalence.py      the per-tick check equals the full audit, and the working-set engine reproduces
                                      the v1.0.1 engine's History head on a seeded random scenario
  tests/test_record_mode.py           the record on disk (Params.record_dir): same fingerprint as in memory, the
                                      chain verifiable from the file alone, paged-out cases return when touched;
                                      `--record` runs every suite in record mode

Expected failure, by design: the third review's case 12 appeals a ⊥ without stating whether
the objection stood; §8.1 requires that disposition explicitly and refuses to infer it from
the fulfillment verdict.
"""
import importlib
import os
import sys
import traceback

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "tests"))

# `--record`: run the whole suite in record mode (Params.record_dir set on every World the tests
# build), as a conformance check of the storage layer. Reviewer tests that edit the in-memory
# event list by list surgery (slice assignment, swapping) cannot be expressed on a journal and are
# reported as what they are; everything else must pass identically. Results go to
# results/tests/<commit>-record.txt.
RECORD = "--record" in sys.argv
if RECORD:
    import shutil
    import tempfile
    from sim.engine import World
    _orig_world_init = World.__init__
    _record_root = tempfile.mkdtemp(prefix="agentic_record_suite_")
    _worlds: list = []

    def _record_init(self, params, *a, **k):
        if params.record_dir is None:
            params.record_dir = os.path.join(_record_root, f"w{len(_worlds) + 1}")
        _worlds.append(self)
        _orig_world_init(self, params, *a, **k)
    World.__init__ = _record_init

    def _close_worlds():
        for w in _worlds:
            try:
                w.close()
            except Exception:  # noqa: BLE001
                pass
        _worlds.clear()
        shutil.rmtree(_record_root, ignore_errors=True)
        os.makedirs(_record_root, exist_ok=True)
else:
    def _close_worlds():
        pass

try:
    import pytest  # noqa: F401
    HAVE_PYTEST = True
except ImportError:
    import _mini_pytest
    sys.modules["pytest"] = _mini_pytest.pytest
    HAVE_PYTEST = False

WITHDRAWN = ("exercises the v0.9 audit-reopening rule, withdrawn in v0.10 (§8.3): an audit is answered "
             "F or N, and P/⊥ on an audit is refused — see test_v10 for the assertion of that refusal")
EXPECTED_FAIL = {
    "test_review_12_appeal_can_uphold_a_cannot_assess_claim":
        "appeals of ⊥ must state the objection disposition explicitly (§8.1); see test_v05 for the explicit form",
    # the fifth review's unfunded-dispute test pins the v1.0.1 deposit through the human's budget
    "test_r5_a_unfunded_dispute_keeps_vacated_audit_obligation": 'superseded by design revision 1 (1.1.0, §4.3): the root pay-in is B + φ^E + φ^F + ω, so a human budget of exactly B + 10 no longer funds the award; the principle — a refused filing waives nothing — is re-asserted in test_v11 at the 1.1.0 pay-in',
    # the third review's test 18 pins Ω's cold-start float at 20 (Appendix A, 1.1.0)
    "test_review_18_unused_deposit_returned_when_no_review_entitled": "superseded by design revision 2 (1.2.0, Appendix A): Ω's cold-start float is 300, one period of plants at m = 1, not 20; the principle — an explicit acceptance with no paid review returns the whole deposit — holds at the new float (the test's other assertions pass)",
    # the seventh review's identical-views test: superseded, not refuted
    "test_identical_fulfillment_views_have_same_response_admissibility": "superseded in v0.10: an initial review's view and an audit's view are no longer identical — the view states `responses_available`, so the admissibility it complained of is now visible; see test_v09/test_v10 for the contract as it stands",
    # the eighth review's cases that depend on reopening; its controls still pass
    "test_later_audit_answer_preserves_its_prior_authorization": WITHDRAWN,     # only the P/⊥ runs fail — see EXPECTED_FAIL_PARAMS
    "test_later_resumed_audit_preserves_its_prior_authorization": WITHDRAWN,
    "test_later_child_audit_does_not_erase_the_parents_valid_milestone": WITHDRAWN,
    "test_reopened_audit_timeout_has_a_replacement_path": WITHDRAWN,
    "test_waiver_after_reopened_audit_timeout_cannot_make_obligation_count_negative": WITHDRAWN,
    "test_upheld_reopening_audit_appeal_stays_within_the_path_bound": WITHDRAWN,
    "test_nested_audit_appeal_charges_the_auditor_not_the_requester": WITHDRAWN,
    "test_nested_abandoned_audit_records_the_premature_requester_approval": WITHDRAWN,
    "test_control_root_reopening_audit_rejected_appeal_settles": WITHDRAWN,
    "test_reopening_cannot_create_a_second_untracked_execution": WITHDRAWN,
    "test_reopening_while_actor_reviews_preserves_one_active_assignment": WITHDRAWN,
    "test_control_idle_actor_can_resume_a_reopened_audit": WITHDRAWN,
    "test_merged_audit_reopening_keeps_the_dispute_answerable": WITHDRAWN,
}


def param_runs(fn):
    """Expand parametrization from either the fallback helper (_params) or real pytest marks.
    A comma-separated names string means each value is a tuple of positional arguments;
    stacked marks form a cross product, as pytest does. Arguments are passed by keyword."""
    import inspect
    import itertools

    def names_of(names):
        if isinstance(names, str):
            return [n.strip() for n in names.split(",")]
        return list(names)

    def expand(names, values):
        ns = names_of(names)
        return [(dict(zip(ns, (tuple(v) if len(ns) > 1 else (v,)))), f"{v!r}") for v in values]

    layers = []
    params = getattr(fn, "_params", None)
    if params is not None:
        layers.append(expand(params[0], params[1]))
    for mark in getattr(fn, "pytestmark", []):
        if getattr(mark, "name", "") == "parametrize":
            layers.append(expand(mark.args[0], mark.args[1]))
    if not layers:
        return [({}, "")]
    runs = []
    for combo in itertools.product(*layers):
        kwargs = {}
        for d, _ in combo:
            kwargs.update(d)
        runs.append((kwargs, "[" + "-".join(lbl for _, lbl in combo) + "]"))
    return runs


SUITES = ["test_spec", "test_review_regressions", "test_v05", "test_review2_interactions", "test_v06",
          "test_review3_boundaries", "test_v07", "test_review4_followthrough", "test_v08",
          "test_review5_contracts", "test_v09", "test_review6_reopening", "test_v10", "test_v101", "test_v11", "test_v12", "test_v13", "test_v14",
          "test_perf_equivalence", "test_record_mode"]
# For a parametrized test with both withdrawn-path runs and controls, only the named parameter
# labels are expected to fail; every other run of it must pass.
EXPECTED_FAIL_PARAMS = {
    "test_later_audit_answer_preserves_its_prior_authorization": {"['P']", "['⊥']"},
}


def expected_to_fail(name: str, label: str) -> bool:
    if name not in EXPECTED_FAIL:
        return False
    only = EXPECTED_FAIL_PARAMS.get(name)
    return True if only is None else label in only


passed = failed = xfailed = 0
lines: list[str] = []


def say(msg: str):
    """Print, and keep for results/tests/<commit>.txt."""
    print(msg)
    lines.append(msg)


for suite in SUITES:
    mod = importlib.import_module(suite)
    say(f"== {suite}")
    for name, fn in list(vars(mod).items()):
        if not (name.startswith("test_") and callable(fn)):
            continue
        for kwargs, label in param_runs(fn):
            xf = expected_to_fail(name, label)
            try:
                fn(**kwargs)
            except Exception:  # noqa: BLE001
                _close_worlds()
                if xf:
                    xfailed += 1
                    say(f"XFAIL {name}{label} — {EXPECTED_FAIL[name][:60]}…")
                else:
                    failed += 1
                    say(f"FAIL  {name}{label}")
                    traceback.print_exc()
            else:
                _close_worlds()
                if xf:
                    # strict: an expected failure that passes means a withdrawn or superseded path
                    # is admitted again, and that is a regression, not a bonus
                    failed += 1
                    say(f"XPASS {name}{label} — expected to fail ({EXPECTED_FAIL[name][:60]}…) but passed")
                else:
                    passed += 1
                    say(f"PASS  {name}{label}")
say(f"\n{passed} passed, {failed} failed, {xfailed} expected failures")

# keep the result: one file per commit under results/tests/, overwritten by a rerun on the same commit
try:
    from drivers.results import git_commit, now, RESULTS
    import platform
    commit = git_commit()
    os.makedirs(os.path.join(RESULTS, "tests"), exist_ok=True)
    path = os.path.join(RESULTS, "tests", f"{commit}{'-record' if RECORD else ''}.txt")
    with open(path, "w") as f:
        f.write(f"# run_tests.py — {now()} — engine {commit} — Python {platform.python_version()}"
                f" — {'pytest' if HAVE_PYTEST else '_mini_pytest'}{' -S' if sys.flags.no_site else ''}"
                f"{' — record mode (--record)' if RECORD else ''}\n")
        f.write("\n".join(lines) + "\n")
    print(f"written to {os.path.relpath(path)}")
except Exception as e:  # noqa: BLE001  — keeping the result never changes it
    print(f"(result not written: {e})")
sys.exit(1 if failed else 0)

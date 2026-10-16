import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# One verbatim regression is an expected failure by design: it appeals a ⊥ without stating
# whether the objection stood, which spec §8.1 requires explicitly. Under raw pytest it is
# reported as XFAIL (strict: it must keep failing for the reason stated), so both entry points
# agree on the result.
EXPECTED_FAIL = {
    "test_review_12_appeal_can_uphold_a_cannot_assess_claim":
        "appeals of ⊥ must state the objection disposition explicitly (§8.1); see test_v05 for the explicit form",
}
EXPECTED_FAIL["test_identical_fulfillment_views_have_same_response_admissibility"] = "superseded in v0.10: an initial review's view and an audit's view are no longer identical — the view states `responses_available`, so the admissibility it complained of is now visible; see test_v09/test_v10 for the contract as it stands"
WITHDRAWN = ("exercises the v0.9 audit-reopening rule, withdrawn in v0.10 (§8.3); see test_v10")
for _n in ("test_later_audit_answer_preserves_its_prior_authorization",
           "test_later_resumed_audit_preserves_its_prior_authorization",
           "test_later_child_audit_does_not_erase_the_parents_valid_milestone",
           "test_reopened_audit_timeout_has_a_replacement_path",
           "test_waiver_after_reopened_audit_timeout_cannot_make_obligation_count_negative",
           "test_upheld_reopening_audit_appeal_stays_within_the_path_bound",
           "test_nested_audit_appeal_charges_the_auditor_not_the_requester",
           "test_nested_abandoned_audit_records_the_premature_requester_approval",
           "test_control_root_reopening_audit_rejected_appeal_settles",
           "test_reopening_cannot_create_a_second_untracked_execution",
           "test_reopening_while_actor_reviews_preserves_one_active_assignment",
           "test_control_idle_actor_can_resume_a_reopened_audit",
           "test_merged_audit_reopening_keeps_the_dispute_answerable"):
    EXPECTED_FAIL[_n] = WITHDRAWN
# For a parametrized test with both withdrawn-path runs and controls, only the named parameter
# ids are expected to fail; the controls must pass. Every expected failure is strict: an
# unexpected pass means a withdrawn or superseded path is admitted again — a regression.
EXPECTED_FAIL_PARAMS = {
    # pytest escapes non-ASCII ids by default, so the ⊥ run is "\\u22a5" unless escaping is disabled
    "test_later_audit_answer_preserves_its_prior_authorization": {"P", "\u22a5", "\\u22a5"},
}


def pytest_collection_modifyitems(config, items):
    import pytest
    for item in items:
        name, _, rest = item.name.partition("[")
        if name not in EXPECTED_FAIL:
            continue
        only = EXPECTED_FAIL_PARAMS.get(name)
        if only is not None and rest.rstrip("]") not in only:
            continue
        item.add_marker(pytest.mark.xfail(reason=EXPECTED_FAIL[name], strict=True))

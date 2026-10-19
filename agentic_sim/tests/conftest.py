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
EXPECTED_FAIL["test_r5_a_unfunded_dispute_keeps_vacated_audit_obligation"] = 'superseded by design revision 1 (1.1.0, §4.3): the root pay-in is B + φ^E + φ^F + ω, so a human budget of exactly B + 10 no longer funds the award; the principle — a refused filing waives nothing — is re-asserted in test_v11 at the 1.1.0 pay-in'
EXPECTED_FAIL["test_review_06_future_service_fee_pays_fifo_reimbursement_claim"] = "superseded by design revision 10 (2.2.0, §10.4): Ω's fee income is pooled for the period's rebate claims until the close, so a service fee no longer advances a reviewer's reimbursement mid-period and does not pay an outstanding claim at once — the claim is paid from Ω's unlocked balance (the returns of capital, the pool's remainder at the close); the principle — Ω's claims are paid first in, first out as it can — holds at the close (test_v22, test_v11)"
EXPECTED_FAIL["test_r4_08_fifo_repayment_updates_the_correct_review"] = "superseded by design revision 10 (2.2.0, §10.4): the second root's service fee is pooled until the period's close instead of advancing the first review's reimbursement, so the deferred amounts the test pins at 1.x's advance differ; the principle — FIFO repayment updates the review that was deferred — holds when the pool's remainder is released (test_v22)"
EXPECTED_FAIL["test_review_14_failed_award_has_no_partial_financial_effects"] = 'superseded by design revision 8 (2.0.0, §2.1, I29): a root request locks its all-in maximum at posting, so a human with 42 cannot post at β = 40 (the all-in is 55) — the refusal moves from the award to the posting and is whole there; the principle — a refused action has no partial financial effect — is re-asserted in test_v20 at the posting lock'
EXPECTED_FAIL["test_review_04_reimbursement_uses_spent_credits_not_real_cost"] = "superseded by design revision 8 (2.0.0, §2.4): there is no backing — v_t = Res_t/M_t is retired and the credit's value is P_0/P_t, which emission does not move; the principle — reimbursement in the credits spent, within the indexed cap — is re-asserted in test_v20 with P_t in the index's place"
EXPECTED_FAIL["test_review_18_unused_deposit_returned_when_no_review_entitled"] = "superseded by design revision 2 (1.2.0, Appendix A): Ω's cold-start float is 300, one period of plants at m = 1, not 20; the principle — an explicit acceptance with no paid review returns the whole deposit — holds at the new float (the test's other assertions pass)"
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

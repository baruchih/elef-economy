"""Addendum 23's AC2 (November 17, 2026; notes §120): the road of an appeal under arm 1, counted from the record of world 3's all-careful
cell — the hundred seeds of a19/rerun/cw3-* (run again whole at 906fc5ac4 for §118, 0 differences against the record). Nothing is run:
the reader sums run_q's rows (the driver's counters and the seats-by-kind tally at a vested real root's closure, addendum 15's P3.4).

Usage: a21_read.py OUT.md [CW3_DIR ...]
"""
import json, math, statistics as st, sys

out = sys.argv[1]
dirs = sys.argv[2:] or ["results/redteam/stability/ablation-A1/stress/a19/rerun/cw3-s21-70",
                        "results/redteam/stability/ablation-A1/stress/a19/rerun/cw3-s71-120"]
rows = []
for d in dirs:
    e = json.load(open(f"{d}/eval.json"))
    rows += e["episodes"]["careful"]
n = len(rows)
f = lambda r, k: float(r.get(k, 0) or 0)
S = lambda k: sum(f(r, k) for r in rows)
se = lambda xs: st.stdev(xs) / math.sqrt(len(xs))
aw = S("awarded")
sk = {}
for r in rows:
    for k, v in json.loads(r.get("seats_by_kind_json") or "{}").items():
        sk[k] = sk.get(k, 0) + v
g = lambda k: sk.get(k, 0)

L = ["# Addendum 23's AC2 — the road of an appeal under arm 1, from the record of world 3's all-careful cell",
     f"\nThe hundred seeds (21–120) of `a19/rerun/cw3-*` ({n} rows; the all-careful of world 3's cell at 906fc5ac4, 0 differences against the record). "
     "The denominator is the real roots awarded a run, as notes §114's P3.4 took it (nearly every awarded root vests). Per-seed errors are the SE over the seeds.\n",
     "## The count, for each real root awarded\n",
     "| quantity | a run | for each real root awarded | note |", "|---|---|---|---|"]
def line(label, k, note="", per_root=True):
    xs = [f(r, k) / f(r, "awarded") for r in rows] if per_root else [f(r, k) for r in rows]
    L.append(f"| {label} | {S(k) / n:.2f} | {S(k) / aw:.4f} ± {se(xs):.4f} | {note} |")
L.append(f"| real roots awarded | {aw / n:.0f} | 1 | |")
line("appeals filed", "appeals_filed", "every one by an actor whose work the truth says is fulfilled (`--appeal-policy truthful`, the default; `--appeal-lie` 0)")
line("… of good work rejected", "false_rejections_appealed", "`false_rejections_appealed`")
line("… of bad work rejected", "true_rejections_appealed", "`true_rejections_appealed`: none in a hundred runs; the planted lies apart (`plant_lies_filed_appeal`)")
line("deciding verdicts opened on an appeal (the panel escalated)", "deciding_panel", "`deciding_panel`; disputes are off in this cell (`disputes_filed` 0), so every one is an appeal's")
L.append(f"| deciding verdicts on an appeal in the roots that vested | {g('dec_panel_appeal') / n:.2f} | {g('dec_panel_appeal') / aw:.4f} | `dec_panel_appeal` at closure — notes §114's 0.039 |")
line("appeals won (the rejection overturned)", "false_rejections_overturned", "`false_rejections_overturned` = `appeals_won`")
A, D, W = S("appeals_filed"), S("deciding_panel"), S("false_rejections_overturned")
L += [f"| appeals that ended at the panel, both confirming (at most) | {(A - D) / n:.2f} | {(A - D) / aw:.5f} | filed less escalated: {100 * (A - D) / A:.2f} in 100 of the appeals, the panels still open at the run's end inside it |",
      f"| appeals not overturned (at most) | {(A - W) / n:.2f} | {(A - W) / aw:.5f} | filed less won: the panel's confirmations, the deciding verdict's, and the appeals open or in their window at the run's end |",
      f"| … of them the deciding verdict's confirmations of N on an appeal (at most) | {(D - g('dec_panel_appeal')) / n:.2f} | {(D - g('dec_panel_appeal')) / aw:.5f} | opened less vested; the cases still in their window at the end inside it (a vesting takes {S('vest_ticks_mean') / n:.1f} ticks from the submission) |",
      f"| deciding verdicts unresolved at the run's end, every reason | {(S('deciding_opened') - S('deciding_confirmed') - S('deciding_overturned')) / n:.2f} | | opened less confirmed less overturned |",
      f"| false penalties at the appeal seat | {S('false_penalty_appeal') / n:.2f} | {S('false_penalty_appeal') / aw:.5f} | a member panelist overturned against the deciding verdict on a verdict the truth agrees with |",
      f"| rulings | {S('rulings') / n:.2f} | {S('rulings') / aw:.5f} | {S('rulings_wrong') / n:.2f} wrong; on the orchestrator's own deliveries, which arm 1 does not reach (A1.3) |",
      f"| good work's rejections that stood as final N | {S('false_rejections') / n:.2f} | {S('false_rejections') / aw:.5f} | `false_rejections`: the appeals not overturned above and the rejections never appealed (an appellant that cannot fund the court fee) |",
      "", "## The seats, for each real root awarded (the tally at a vested real root's closure)\n",
      "| seat | members | the state |", "|---|---|---|",
      f"| the appeal panel's seats | {g('panelseat_member_appeal') / aw:.4f} | {g('panelseat_troop_appeal') / aw:.4f} |",
      f"| the audit that differed, attached to the challenge record (notes §114's 'third' column) | {g('panelseat_member_audit') / aw:.4f} | {g('panelseat_troop_audit') / aw:.4f} |",
      f"| the deciding verdict opened after a member's audit differed (`dec_audit_audit`) | {g('dec_audit_audit') / aw:.4f} ({g('dec_audit_audit')} cases against {g('panelseat_member_audit')} member audit seats attached) | |",
      f"| … after the state's audit differed (`dec_state_audit_audit`) | | {g('dec_state_audit_audit') / aw:.4f} ({g('dec_state_audit_audit')} cases against {g('panelseat_troop_audit')} troop audit seats attached) |",
      f"| the deciding verdict's own seats | | {sum(v for k, v in sk.items() if k.startswith('decseats_')) / aw:.4f} |",
      f"\nThe deciding verdicts a run by reason: after a member's audit differed {S('deciding_audit') / n:.1f}, after the state's audit differed {S('deciding_state_audit') / n:.1f}, "
      f"on an appeal {S('deciding_panel') / n:.1f} — {S('deciding_opened') / n:.1f} in all, {S('deciding_splits') / n:.1f} of them split to a third seat ({100 * S('deciding_splits') / S('deciding_opened'):.1f} in 100), "
      f"{S('deciding_seats') / n:.1f} seats. The state's share of the appeal panel's seats {100 * g('panelseat_troop_appeal') / (g('panelseat_troop_appeal') + g('panelseat_member_appeal')):.0f} in 100 "
      f"(a seat unfilled for w_R = 2 seating steps with no free panel-eligible member goes to a troop); the panel seats' waiting ticks {S('appeals_unassignable_ticks') / n:.0f} a run.",
      "", "## By the rates (the reviewer's arithmetic, R)\n",
      f"Appeals: 0.8 of the real tasks good × 0.05 rejected = 0.040 a root; read {A / aw:.4f}. A panel of two careful seats both wrong on good work: 0.05² = 0.0025 of the appeals, {0.0025 * A / n:.2f} a run; "
      f"read at most {(A - D) / n:.2f}. The deciding verdict wrong on good work: both seats wrong 0.0025 plus a split (0.095) with the third wrong (0.05) = 0.00725 of the appeals, {0.00725 * D / n:.2f} a run; read at most {(D - g('dec_panel_appeal')) / n:.2f}, "
      "the cases still in their window at the run's end inside it."]
open(out, "w").write("\n".join(L) + "\n")
print("\n".join(L))

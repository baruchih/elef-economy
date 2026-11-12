"""The provenance listing of the plant kind's state-seat stage (addendum 8 H1; November 13, 2026): every place on record that quotes the column —
the evaluations' stage tables (eval.md / eval.json, `life_plant_state_seats` and the period rows' state seats), the pairings' "state seats per plant"
rows and period-matched Δ, the notes — with the figure before (the evaluation of record) and after (the re-read on the corrected stage table,
`<eval>-at-30f280474/`; the pairing produced again over the re-reads). Where the evaluation of record was made before the corrected emission
(the macOS episode, §77) it is not re-run: the figure is listed with its bound — the planted approvals closed a run × 3 (a planted approval's
state seats are at most its third seat and a panel of two) over the plants seated at a member's first seat. Every other column of a re-read is
checked against the record: `other keys moved` counts the summary figures that differ by more than 1e-9.
Usage: restage_read.py OUT.md"""
import json, os, sys, glob, numpy as np
sys.path.insert(0, os.path.dirname(__file__)); from restage import affected, root, SUF, SUFS
def val(x):
    if isinstance(x, dict): x = x.get("mean", x.get("m"))
    if isinstance(x, (list, tuple)): x = x[0] if x else None          # the summary's [mean, se]
    try: return float(x)
    except (TypeError, ValueError): return float("nan")
def fmt(x): return "—" if x != x else f"{x:.3f}"
L = ["# The plant kind's state-seat stage on record — before and after the driver's correction (30f280474)\n",
     "Produced by `2.9.0-s82/restage_read.py` over the evaluations of record and their re-reads (`restage.py`, `restage.sh`) and the pairings produced again (`restage_pair.sh`). "
     "The column: the plant kind's `state seats` in a stage table (`life_plant_state_seats`: the state's verdicts on a plant after a member's first seat, per plant so seated; "
     "the period-matched table's plant row `state_seats`). Before the correction a planted approval's state seats were filed under it with no seated count; after, a planted "
     "approval is skipped (its stages are the `pa_*` readings'). The real kind's `state seats per real root` never carried one and is unchanged.\n"]
L.append("\n## 1. The notes\n\nOne place quotes the column: §108's seam paragraph (`results/studies/2.7.0-notes-for-reviewer.md`), which states the correction with the figures before and after for the G3 cell and seed 21's hand run. No other section quotes the plant kind's state-seat stage; the `state seats per real root` rows in §83, §84 and §88's tables are the real kind's.\n")
L.append("\n## 2. The evaluations' stage tables (`eval.md`, `eval.json`)\n\n| evaluation | policy | before | after | other keys moved | note |\n|---|---|---|---|---|---|")
n_run = n_old = n_moved = 0
for rel, j, old in affected():
    d = os.path.join(root, rel); ja = None
    for x in SUFS:
        pa = os.path.join(d + x, "eval.json")
        if os.path.exists(pa): ja = json.load(open(pa)); break
    for pol, s in j["summary"].items():
        b = val(s.get("life_plant_state_seats"))
        if ja is not None and pol in ja["summary"]:
            a = val(ja["summary"][pol].get("life_plant_state_seats"))
            moved = [k for k in s if k not in ("life_plant_state_seats", "life_by_period", "seconds") and isinstance(s[k], (int, float, dict, list)) and abs(val(s[k]) - val(ja["summary"][pol].get(k))) > 1e-9 and not (val(s[k]) != val(s[k]))]
            n_run += 1; n_moved += bool(moved)
            L.append(f"| {rel} | {pol} | {fmt(b)} | {fmt(a)} | {len(moved)}{(' (' + ', '.join(moved[:4]) + ')') if moved else ''} | re-read |")
        else:
            eps = j["episodes"].get(pol, [])
            bound = np.nanmean([3 * float(e.get("pa_closed") or 0) / float(e.get("life_plant_n") or np.nan) for e in eps]) if eps else float("nan")
            n_old += 1
            L.append(f"| {rel} | {pol} | {fmt(b)} | ≥ {fmt(b - bound)} (bound) | — | {'the macOS episode, not re-run' if old else 're-read pending'} |")
L.append(f"\n{n_run} policy columns re-read ({n_moved} with another key moved), {n_old} bounded.\n")
L.append("\n## 3. The pairings (`finals-paired.py`'s \"state seats per plant\" rows and the period-matched table's state seats)\n")
for md in sorted(glob.glob(root + "/**/*.md", recursive=True)):
    if md.endswith(SUF + ".md") or "state seats per plant" not in open(md).read(): continue
    rel = os.path.relpath(md, root); mda = md[:-3] + SUF + ".md"
    rows_b = [l for l in open(md) if l.startswith("| state seats per plant") or l.startswith("| state seats |") or ("state_seats" in l)]
    if os.path.exists(mda):
        A = open(mda).read().splitlines(); B = open(md).read().splitlines()
        diff = [(b, a) for b, a in zip(B, A) if b != a and not b.startswith("#") and not b.startswith("Produced")]
        L.append(f"\n### {rel} — re-paired as `{os.path.basename(mda)}`; {len(diff)} rows differ\n")
        for b, a in diff[:40]:
            L.append(f"- before: `{b.strip()}`\n  after:  `{a.strip()}`")
        if len(A) != len(B): L.append(f"- (the files differ in length: {len(B)} against {len(A)} lines)")
    else:
        L.append(f"\n### {rel} — not re-paired (a side made before the corrected emission, or the reader's); the rows of record:\n")
        for r in rows_b[:6]: L.append(f"- `{r.strip()}`")
open(sys.argv[1], "w").write("\n".join(L) + "\n"); print("\n".join(L[:12]))

"""The provenance listing of the plant kind's state-seat stage (addendum 8 H1; November 13, 2026): every place on record that quotes the column —
the evaluations' stage tables (eval.md / eval.json, `life_plant_state_seats` and the period rows' state seats), the pairings' "state seats per plant"
rows and period-matched Δ, the notes — with the figure before (the evaluation of record) and after (the re-read on the corrected stage table,
`<eval>-at-30f280474/`; the pairing produced again over the re-reads). Where the evaluation of record was made before the corrected emission
(the macOS episode, §77) it is not re-run: the figure is listed with its bound — the planted approvals closed a run × 3 (a planted approval's
state seats are at most its third seat and a panel of two) over the plants seated at a member's first seat. Every other column of a re-read is
checked against the record: `other keys moved` counts the summary figures that differ by more than 1e-9 — the four suspension-count keys of the
driver's log (`half_care_suspensions`, `half_claim_suspensions`, `slot_suspensions`, `false_approvals_per_suspension`) are left out of the count, since every
re-read runs on the driver at 4df18f1bc, whose log no longer counts an arrival as a suspension (notes §109), and in a population cell with arrivals they move
by that correction alone.
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
     "approval is skipped (its stages are the `pa_*` readings'). The real kind's `state seats per real root` never carried one and is unchanged. The re-read found two further columns of the plant kind that the planted approvals had joined, in the cells where disputes are on alone: a planted approval there is disputed first (§68), and its dispute was filed under the plant kind's `filed share` (`life_plant_filing_share`) and its panel's wait under `panel wait` (`life_plant_panel_wait`); section 2b lists them. No other summary figure of any re-read differs from the record but the four suspension-count keys of the driver's log, corrected at 4df18f1bc (notes §109) and counted apart.\n"]
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
            moved = [k for k in s if k not in ("life_plant_state_seats", "life_by_period", "seconds", "half_care_suspensions", "half_claim_suspensions", "slot_suspensions", "false_approvals_per_suspension") and isinstance(s[k], (int, float, dict, list)) and abs(val(s[k]) - val(ja["summary"][pol].get(k))) > 1e-9 and not (val(s[k]) != val(s[k]))]
            n_run += 1; n_moved += bool(moved)
            L.append(f"| {rel} | {pol} | {fmt(b)} | {fmt(a)} | {len(moved)}{(' (' + ', '.join(moved[:4]) + ')') if moved else ''} | re-read |")
        else:
            eps = j["episodes"].get(pol, [])
            bound = np.nanmean([3 * float(e.get("pa_closed") or 0) / float(e.get("life_plant_n") or np.nan) for e in eps]) if eps else float("nan")
            n_old += 1
            L.append(f"| {rel} | {pol} | {fmt(b)} | ≥ {fmt(max(0.0, b - bound))} (bound) | — | {'the macOS episode, not re-run' if old else 're-read pending'} |")
L.append(f"\n{n_run} policy columns re-read ({n_moved} with another key moved), {n_old} bounded.\n")
L.append("\n### 2b. The plant kind's filed share and panel wait where they moved (the cells with disputes on)\n\n| evaluation | policy | filed share before | after | panel wait before | after |\n|---|---|---|---|---|---|")
n2b = 0
for rel, j, old in affected():
    d = os.path.join(root, rel); ja = None
    for x in SUFS:
        pa = os.path.join(d + x, "eval.json")
        if os.path.exists(pa): ja = json.load(open(pa)); break
    if ja is None: continue
    for pol, s in j["summary"].items():
        if pol not in ja["summary"]: continue
        t = ja["summary"][pol]
        fb, fa = val(s.get("life_plant_filing_share")), val(t.get("life_plant_filing_share")); pb, pa_ = val(s.get("life_plant_panel_wait")), val(t.get("life_plant_panel_wait"))
        if (fb == fb and abs(fb - fa) > 1e-9) or (pb == pb and abs(pb - pa_) > 1e-9):
            n2b += 1; L.append(f"| {rel} | {pol} | {fmt(fb)} | {fmt(fa)} | {fmt(pb)} | {fmt(pa_)} |")
L.append(f"\n{n2b} policy columns; in every other re-read both are the record's to the decimal. The bounded finals of the liar chains of §68–§70 (`learned-rev-liars-290/`, `-290b/`, `-B-290/`) carried the planted approvals' disputes in the same way; their filed share is bounded as the state seats are, by the planted approvals closed a run over the plants seated.\n")
L.append("\n## 3. The pairings (every row of a pairing of record against the pairing produced again over the re-reads)\n\nA pairing's rows are aligned by their label; a cell is *changed* where the record carried a figure and the re-pairing carries a different one, and *newly read* where the record carried none (`nan`, `—`) — the re-reads were made with today's `run_q`, whose evaluation writes readings (the leak, the overhead, the false penalties) the evaluations of record predate, so a base side re-read carries figures its record lacked; those are not the correction's and are counted apart.\n")
import re
NUM = re.compile(r"[-+]?(?:\d+\.\d+|\d+|nan|inf)")
def cells(line): return [c.strip() for c in line.strip().strip("|").split("|")]
def nums(c):
    out = []
    for t in NUM.findall(c):
        try: out.append(float(t))
        except ValueError: pass
    return out
def finite(xs): return [x for x in xs if x == x and abs(x) != float("inf")]
def sections(path):
    """the file's tables by section ('## ' headings); within a section a row is keyed by its label and its occurrence — robust to tables re-ordered between the script of record and today's"""
    out = {}; cur = ""; out[cur] = []
    for l in open(path):
        if l.startswith("## "): cur = l.strip(); out.setdefault(cur, [])
        elif l.startswith("| ") and not l.startswith("|---"): out[cur].append((cells(l)[0], l.rstrip()))
    return out
n_pair = n_changed_rows = n_new_rows = 0
for md in sorted(glob.glob(root + "/**/*.md", recursive=True)):
    if md.endswith(SUF + ".md") or "state seats per plant" not in open(md).read(): continue
    if not any(ch.isdigit() for l in open(md) if l.startswith("| state seats per plant") for ch in l): continue   # a table with no plant figure (the 2.7.0 side)
    rel = os.path.relpath(md, root); mda = md[:-3] + SUF + ".md"
    rows_b = [l for l in open(md) if l.startswith("| state seats per plant") or l.startswith("| state seats |") or ("state_seats" in l)]
    if os.path.exists(mda):
        SB = sections(md); SA = sections(mda); changed = []; newly = []; lost = []
        for sec, B in SB.items():
            A = SA.get(sec, []); byl = {}
            for lab, a in A: byl.setdefault(lab, []).append(a)
            seen = {}
            for lab, b in B:
                k = seen.get(lab, 0); seen[lab] = k + 1
                if k >= len(byl.get(lab, [])): lost.append(b); continue
                a = byl[lab][k]
                cb, ca = cells(b), cells(a)
                if len(cb) != len(ca): changed.append((b, a)); continue
                ch = nw = False
                for x, y in zip(cb, ca):
                    nx, ny = nums(x), nums(y)
                    if finite(nx):
                        if len(nx) != len(ny) or any(abs(u - v) > 1e-9 for u, v in zip(nx, ny)): ch = True
                    elif not nx and not ny:
                        if x != y: ch = True
                    elif finite(ny): nw = True
                if ch: changed.append((b, a))
                elif nw: newly.append(lab)
        n_pair += 1; n_changed_rows += len(changed); n_new_rows += len(newly)
        L.append(f"\n### {rel} — re-paired as `{os.path.basename(mda)}`; {len(changed)} rows changed, {len(newly)} rows newly read where the record had none{', ' + str(len(lost)) + ' rows of record with no counterpart' if lost else ''}\n")
        for b, a in changed[:60]:
            L.append(f"- before: `{b.strip()}`\n  after:  `{a.strip()}`")
        if len(changed) > 60: L.append(f"- … and {len(changed) - 60} more rows changed")
        for b in lost[:5]: L.append(f"- no counterpart: `{b.strip()}`")
    else:
        L.append(f"\n### {rel} — not re-paired (a side made before the corrected emission, or the reader's); the rows of record:\n")
        for r in rows_b[:6]: L.append(f"- `{r.strip()}`")
L.append(f"\n{n_pair} pairings re-paired: {n_changed_rows} rows changed, {n_new_rows} rows newly read where the record had none.\n")
open(sys.argv[1], "w").write("\n".join(L) + "\n"); print("\n".join(L[:12]))

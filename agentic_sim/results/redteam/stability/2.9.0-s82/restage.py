"""The provenance re-read of the plant kind's state-seat stage (the reviewer's ask after §108, addendum 8 H1; November 13, 2026): every evaluation of record
on the corrected engine (ce29d2b14 and after) whose stage table carried the planted approvals' state seats under the plant kind — the finals of record, the
frozen and retrained detection cells, the stressed finals and the mixed worlds, the honest side's cells, the cr-finals' hand cells — run again whole by
the command its eval.json records, on the driver's corrected stage table (30f280474), into `<eval>-at-30f280474/` beside it. The evaluation of record is
untouched; every column but the plant kind's stage reproduces to the decimal (checked by restage_read.py). The rounds' evaluations (round-N) and the
finals made before the corrected emission (the macOS episode, §77) are not re-run: their figure is listed with its bound.
Usage: restage.py list|emit [> cmds.txt]"""
import glob, json, os, sys
PY = "/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python"
root = os.path.abspath("results/redteam/stability")
SUF = "-at-30f280474"
def affected():
    out = []
    for f in sorted(glob.glob(root + "/**/eval.json", recursive=True)):
        d = os.path.dirname(f); rel = os.path.relpath(d, root)
        if rel.endswith(SUF) or "-at-7394be48b" in rel: continue
        md = os.path.join(d, "eval.md")
        if not os.path.exists(md) or "| state seats |" not in open(md).read(): continue
        j = json.load(open(f)); cell = " ".join(j.get("cell", []))
        if "--rules 2.8.0" in cell or "--rules 2.7.0" in cell or "--planted-approval off" in cell: continue
        if "/2.7.0" in rel or "-280/" in rel or "-2/" in rel.split("/")[0] + "/": continue   # the 2.8.0 and 2.7.0 chains: no planted approval existed, the stage never carried one
        base = os.path.basename(d)
        if base.startswith("round-") and "probe-seats" not in rel: continue          # the chains' own progress reads
        old = (rel.split("/")[0] in ("learned-rev-careful-290", "learned-rev-liars-290", "learned-rev-stamper-290", "learned-rev-careful-290b", "learned-rev-liars-290b", "learned-rev-careful-A-290", "learned-rev-half-290"))
        old = old or (rel.split("/")[0] in ("learned-rev-careful-290-own", "learned-rev-liars-290-own", "learned-rev-stamper-290-own") and base == "final")   # the macOS episode's finals (§77); final-cr is the corrected engine's
        out.append((rel, j, old))
    return out
def cmd(rel, j):
    d = os.path.join(root, rel); out = d + SUF
    pol = ",".join(j["summary"].keys())
    c = [PY, "-m", "redteam.run_q", "--out", out, "--seeds", j["seeds"], "--policies", pol, "--horizon", str(j["horizon"]), "--samples", str(j["samples"]), "--iters", str(j["iters"]),
         "--boundary-read", j.get("boundary_read", "auto"), "--attrib", "own", "--role", j.get("role", "reviewer")]
    if j.get("model"): c += ["--model", j["model"]]
    if j.get("direct_model"): c += ["--direct-model", j["direct_model"]]
    if j.get("hide"): c += ["--hide", j["hide"]]
    if rel.endswith("final-2000"): c += ["--ticks", "2000"]
    c += ["--"] + j["cell"]
    return " ".join(c) + f" > {out}.log 2>&1"
if __name__ == "__main__":
    rows = affected()
    if sys.argv[1] == "list":
        for rel, j, old in rows: print(("OLD  " if old else "RUN  ") + rel + "  " + ",".join(j["summary"].keys()) + f"  {j.get('seconds', 0):.0f}s")
        print(len([r for r in rows if not r[2]]), "to run;", len([r for r in rows if r[2]]), "old-engine (bounded)")
    else:
        for rel, j, old in rows:
            if old: continue
            if os.path.exists(os.path.join(root, rel + SUF, "eval.json")): continue
            for k in ("model", "direct_model"):
                if j.get(k) and not os.path.exists(j[k]): print("# missing", k, rel, file=sys.stderr)
            print(cmd(rel, j))

"""The dispute panel's own actions by the dispute's truth and owner (the reviewer's note of November 10, after read (3)): on a collection of
run 42's final policy (ε 0.1) in a detection cell, the dispute-panel decisions (the observation's question one-hot) split by the case's
truth (fulfilled: a lie; unfulfilled: a truthful dispute) and its owner (a plant: the plant requester's — a truthful dispute of a bad plant
or a planted lie; a real case: the customer's), the action mix at each — inspect, blind confirmation (approve: the standing F stands),
blind rejection (siding with the disputer). The appeal panel beside. Usage: panel_by_truth.py <data dir> [policy tag, default online11]"""
import glob, os, sys
import numpy as np
sys.path.insert(0, os.getcwd())
from redteam.obs import IDX
root = sys.argv[1]; tag = sys.argv[2] if len(sys.argv) > 2 else "online11"
files = sorted(glob.glob(os.path.join(root, f"{tag}-seed*.npz")))
def ms(v):
    v = np.array([x for x in v if not np.isnan(x)], float); return f"{v.mean():.3f} ± {v.std(ddof=1)/np.sqrt(len(v)):.3f}" if len(v) > 1 else "—"
print(f"{root} ({tag}, {len(files)} seeds)")
for q in ("dispute", "appeal"):
    print(f"\n{q} panel | kind | decisions | inspect | blind confirmation | blind rejection")
    for kind, test in (("truthful, the customer's (real, unfulfilled)", lambda P, F: (~P) & (~F)), ("truthful, the plant's (bad plant)", lambda P, F: P & (~F)),
                       ("a lie, the customer's (real, fulfilled)", lambda P, F: (~P) & F), ("a lie, the plant's (good plant)", lambda P, F: P & F), ("all", lambda P, F: np.ones_like(P, bool))):
        n = 0; insp = []; conf = []; rej = []
        for f in files:
            z = np.load(f, allow_pickle=True); O = z["obs"]; A = z["action"]; P = z["is_plant"].astype(bool); F = z["fulfilled"].astype(bool)
            m = (O[:, IDX["rv_q_" + q]] > 0.5) & test(P, F)
            if m.sum() == 0: continue
            n += int(m.sum()); a = A[m]
            confirm = 1 if q == "dispute" else 2          # the standing verdict: F at a dispute panel, N at an appeal panel
            insp.append(float((a == 0).mean())); conf.append(float((a == confirm).mean())); rej.append(float((a == (3 - confirm)).mean()))
        if n: print(f"  {kind:46s} | {n:6d} | {ms(insp)} | {ms(conf)} | {ms(rej)}")

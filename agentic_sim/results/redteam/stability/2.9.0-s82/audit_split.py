"""Who takes the audit seat, by case kind, in one episode: a member or the state (a troop / the state's verdict), and the wait from the
obligation to the seat — the real roots' pending Fs, the planted approvals, the other plants' pending Fs."""
import sys, numpy as np
sys.path.insert(0, ".")
from redteam.env import ElefReviewerEnv
from redteam.direct import load_direct, DirectPolicy
from redteam.run_q import boundary_read_for, policy_of
from redteam.model import device
cell = ["--entry-pool", "20", "--stampers", "0.6", "--learner-pop", "all", "--learner-role", "reviewer", "--learner-exit", "rule"]
model = sys.argv[1]; seeds = [int(x) for x in sys.argv[2].split(",")]; which = sys.argv[3].split(",") if len(sys.argv) > 3 else ["direct", "hand"]
br = boundary_read_for(cell, "auto")
env = ElefReviewerEnv(cell, ticks=1000, role="reviewer")
dm, _ = load_direct(model); dm.to(device())
pols = {"direct": DirectPolicy(dm, boundary_read=br), "hand": policy_of("hand", "reviewer")}
rng = np.random.default_rng(0)
for name in which:
    pol = pols[name]
    for s in seeds:
        obs, info = env.reset(seed=s); done = info.get("terminal", False)
        while not done:
            a = pol(obs, rng); obs, r, done, _, info = env.step(a)
        W = env.run._world
        tally = {}
        for cid, c in W.cases.items():
            if not getattr(c, "is_root", True): continue
            is_plant = getattr(c, "plant_truth", None) is not None or getattr(c, "plant_created", None) is not None or cid in getattr(W, "plants", {}) if hasattr(W, "plants") else getattr(c, "plant_truth", None) is not None
            pa = bool(getattr(c, "planted_approval", False))
            kind = "planted approval" if pa else ("plant" if is_plant else "real")
            rolled = getattr(c, "audit_rolled_at", None)
            if rolled is None: continue
            t = tally.setdefault(kind, {"obligations": 0, "member": 0, "state": 0, "discharged": 0, "open": 0, "wait_member": [], "wait_state": []})
            t["obligations"] += 1
            member = [W.reviews[r] for r in c.reviews if W.reviews[r].role == "audit" and W.reviews[r].status != "withdrawn"]
            pss = getattr(c, "plant_state_seats", None) or []
            if pa and pss and t["obligations"] == 1: print("   example plant_state_seats:", pss)
            state = [x for x in pss if ("audit" in str(x))]
            if member:
                rv = member[0]
                if W.is_troop(rv.reviewer) if hasattr(W, "is_troop") else str(rv.reviewer).startswith("T"):
                    t["state"] += 1; t["wait_state"].append(rv.t_assign - rolled)
                else:
                    t["member"] += 1; t["wait_member"].append(rv.t_assign - rolled)
            elif state:
                x = state[0]; tt = (x.get("t") or x.get("tick")) if isinstance(x, dict) else (x[1] if isinstance(x, (tuple, list)) and len(x) > 1 and isinstance(x[1], int) else getattr(x, "t", None))
                t["state"] += 1
                if tt is not None: t["wait_state"].append(tt - rolled)
            elif getattr(c, "audit_obligation", False): t["open"] += 1
            else: t["discharged"] += 1
        print(f"\n== {name} seed {s}")
        for k, t in tally.items():
            wm = np.mean(t["wait_member"]) if t["wait_member"] else float("nan"); ws = np.mean(t["wait_state"]) if t["wait_state"] else float("nan")
            print(f"  {k:18s} obligations {t['obligations']:5d}  member {t['member']:5d}  state {t['state']:5d}  open {t['open']:3d}  neither {t['discharged']:3d}  wait member {wm:.2f}  wait state {ws:.2f}")
        # a sample planted approval and a sample real root with a state audit: the fields
        sys.stdout.flush()

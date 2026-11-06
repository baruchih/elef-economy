"""The reviewer's reading after run 38 (fact ii): the standing false approvals of a run split by channel — audited and confirmed by a member,
audited and confirmed by the state (a troop at the audit seat), audited and rejected yet vested (the third seat / a ruling), never audited
(the roll never sent the review to audit). Run 38's finals: the careful basin's direct and head-alone models on seeds 21–40, the hand beside;
paired by seed. Usage: fa_channels.py "<cell>" seeds direct-model wm-model OUT.md"""
import sys, numpy as np
sys.path.insert(0, ".")
from redteam.env import ElefReviewerEnv, policy_of
from redteam.train import load_model
from redteam.plan import GreedyPolicy, boundary_read_for
from redteam.direct import load_direct, DirectPolicy
from redteam.model import device
from sim.invariants import public_id
cell = sys.argv[1].split(); seeds = [int(x) for x in sys.argv[2].split(",")]; dmp, wmp, out = sys.argv[3], sys.argv[4], sys.argv[5]
br = boundary_read_for(cell, "auto")
dm, _ = load_direct(dmp); dm.to(device()); wm, ck = load_model(wmp); wm.to(device())
pols = {"direct": DirectPolicy(dm, boundary_read=br), "head alone": GreedyPolicy(wm, boundary_read=br), "hand": policy_of("hand", "reviewer")}
CH = ["member confirmed", "state confirmed", "audited, rejected, vested", "disputed, panel confirmed (a member sat)", "disputed, panel confirmed (the state's alone)",
      "appealed, panel sided with the appellant (a member sat)", "appealed, panel sided with the appellant (the state's alone)", "never audited"]
# the fifth and sixth channels (run 40): where disputes are on, a false approval the requester disputed and the panel confirmed has no audit
# review — §4 discharges the obligation at the dispute's settlement — so it is split out of "never audited" by the panel's composition.
# Corrected November 6, 2026 (the economy reviewer's ruling on the record's second finding; re-run, not relabelled): the engine creates every
# panel review — a dispute's or an appeal's — with the role "appeal", so the first reader's test for a "dispute" role was always empty and its
# "a member sat" column always zero for that reason alone. The panel is now read from the case's challenge record (`c.challenge["reviews"]`,
# the reviews that sat it; a vacated seat is removed by the engine) with its kind (`c.challenge["kind"]`), and a paid appeal — the actor's
# appeal of its bad work's N that the panel overturned to F (the liar cell's lying appeal paid) — is its own channel, split by the panel's
# composition as the disputes are. The tables of October 28 are superseded by the ones this reader writes.
res = {n: {} for n in pols}
for seed in seeds:
    for name, pol in pols.items():
        env = ElefReviewerEnv(cell, ticks=1000, role="reviewer")
        obs, info = env.reset(seed=seed); rng = np.random.default_rng(seed); done = info.get("terminal", False)
        while not done:
            obs, r, done, _, info = env.step(int(pol(obs, rng)))
        run = env.run; W = run.w._w
        cnt = dict.fromkeys(CH, 0); rolled_never = 0; odds = []; other_kinds = 0
        for cid, c in W.cases.items():
            t = run.tasks.get(public_id(cid))                      # the driver keys its tasks by the public id
            if t is None or t.plant or not c.is_root or c.state != "VESTED" or t.fulfilled or W.is_troop(c.actor): continue
            audits = [W.reviews[x] for x in c.reviews if W.reviews[x].role == "audit"]
            if not audits:
                ch = c.challenge
                if ch is not None:
                    panel = [W.reviews[x] for x in ch["reviews"]]
                    member_sat = any(not W.is_troop(p_.reviewer) for p_ in panel)
                    who = "a member sat" if member_sat else "the state's alone"
                    if ch["kind"] == "dispute":
                        cnt[f"disputed, panel confirmed ({who})"] += 1
                    elif ch["kind"] == "appeal":
                        cnt[f"appealed, panel sided with the appellant ({who})"] += 1
                    else:
                        other_kinds += 1                               # an audit-opened challenge has an audit review; should be 0 here
                    continue
                cnt["never audited"] += 1
                if c.audit_rolled_at is not None: rolled_never += 1
                if c.audit_odds_at_verdict is not None: odds.append(c.audit_odds_at_verdict)
                continue
            conf = [a for a in audits if a.verdict == "F" and a.status in ("done", "vested")]
            if conf: cnt["state confirmed" if W.is_troop(conf[-1].reviewer) else "member confirmed"] += 1
            else: cnt["audited, rejected, vested"] += 1
        cnt["rolled but never seated"] = rolled_never; cnt["odds at verdict, never audited (mean)"] = float(np.mean(odds)) if odds else float("nan"); cnt["other challenge kinds"] = other_kinds
        res[name][seed] = cnt
        print(f"seed {seed} {name}: {sum(cnt[k] for k in CH)} standing false approvals — " + ", ".join(f"{k} {cnt[k]}" for k in CH) + f"; rolled-never {rolled_never}; other kinds {other_kinds}; odds {cnt['odds at verdict, never audited (mean)']:.3f}", flush=True)
L = []
L.append(f"# The standing false approvals by channel (the reviewer's reading after run 38; the reader corrected November 6, 2026 — the panel read from the case's challenge record with its kind, a paid appeal its own channel): the chain's finals on seeds {sys.argv[2].split(',')[0]}–{sys.argv[2].split(',')[-1]}, the direct ({dmp}) and head alone ({wmp}), the hand beside. A standing false approval: a real root (not a plant, not the state's delivery) vested with its work unfulfilled. Channels: its audit seat confirmed it (a member's or the state's — a troop at the audit seat), it was audited and rejected yet vested (the third seat or a ruling), it was disputed by its requester and the panel confirmed it (no audit review: §4 discharges the obligation at the dispute's settlement; split by whether a member sat on the panel or the state's reviewers alone did), its actor appealed its N and the panel sided with the appellant — a paid appeal (the same split), or it was never audited (no audit review, no challenge: the roll never sent it). `rolled but never seated` counts never-audited cases with an obligation recorded (should be 0: a vested case has no standing obligation).\n")
L.append("| policy | standing false approvals | " + " | ".join(CH) + " | never-audited share | odds at verdict of the never-audited (mean) |"); L.append("|---|---|" + "---|" * (len(CH) + 2))
def ms(v): v = np.asarray(v, float); return f"{v.mean():.1f} ± {v.std(ddof=1)/np.sqrt(len(v)):.1f}"
for name in pols:
    R = res[name]; tot = np.array([sum(R[s][k] for k in CH) for s in seeds])
    cols = [ms(tot)] + [ms([R[s][k] for s in seeds]) for k in CH]
    never = np.array([R[s]["never audited"] for s in seeds]); share = never.sum() / max(1, tot.sum())
    od = np.array([R[s]["odds at verdict, never audited (mean)"] for s in seeds]); od = od[~np.isnan(od)]
    L.append(f"| {name} | " + " | ".join(cols) + f" | {share:.3f} | {od.mean():.3f} |")
L.append("\nPaired against the hand on the same seeds (policy − hand):\n")
L.append("| policy | total | " + " | ".join(CH) + " |"); L.append("|---|---|" + "---|" * len(CH))
for name in ("direct", "head alone"):
    d = [ms([sum(res[name][s][k] for k in CH) - sum(res["hand"][s][k] for k in CH) for s in seeds])] + [ms([res[name][s][k] - res["hand"][s][k] for s in seeds]) for k in CH]
    L.append(f"| {name} − hand | " + " | ".join(d) + " |")
L.append("\nPer seed (" + " / ".join(CH) + "):\n")
for s in seeds:
    L.append(f"- seed {s}: " + "; ".join(f"{n} " + " / ".join(str(res[n][s][k]) for k in CH) for n in pols))
open(out, "w").write("\n".join(L) + "\n"); print("\n".join(L))

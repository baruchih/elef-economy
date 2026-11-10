"""The reviewer's reads 1 and 2 of November 10: the customers' truthful disputes won by the panel's make-up — two members, one of each, two of
the state's — and the state's share of the panel seats by its cause (members off the panel tier by their record, or none free within w_R).
Run 42's final policy (the direct's round-10 model) in a detection cell, seeds 21–40, read from the engine's cases at the end (fa_channels'
pattern); the careful beside as the hand reference. Usage: disputes_by_panel.py <rate> <direct-model> OUT.md [seeds]"""
import sys, numpy as np
sys.path.insert(0, ".")
from redteam.env import ElefReviewerEnv, policy_of
from redteam.plan import boundary_read_for
from redteam.direct import load_direct, DirectPolicy
from redteam.model import device
from sim.invariants import public_id
rate, dmp, out = sys.argv[1], sys.argv[2], sys.argv[3]
seeds = [int(x) for x in (sys.argv[4] if len(sys.argv) > 4 else "21-40").replace("-", ",").split(",")]
seeds = list(range(seeds[0], seeds[-1] + 1)) if len(seeds) == 2 else seeds
cell = ["--entry-pool", "20", "--stampers", "0.6", "--learner-pop", "all", "--learner-role", "reviewer", "--learner-exit", "rule", "--dispute-policy", "truthful", "--dispute-rate", rate]
br = boundary_read_for(cell, "auto"); dm, _ = load_direct(dmp); dm.to(device())
pols = {"direct": DirectPolicy(dm, boundary_read=br), "careful": policy_of("careful", "reviewer")}
MK = ["two members", "one member, one of the state's", "two of the state's"]
res = {}; JOINT = {}; SEATF = {}
for name, pol in pols.items():
    per = {k: [] for k in MK}; counters = []
    for seed in seeds:
        env = ElefReviewerEnv(cell, ticks=1000, role="reviewer"); obs, info = env.reset(seed=seed); rng = np.random.default_rng(seed); done = info.get("terminal", False)
        while not done:
            obs, r, done, _, info = env.step(int(pol(obs, rng)))
        run = env.run; W = run.w._w; cnt = {k: [0, 0] for k in MK}
        joint = JOINT.setdefault(name, {}); seatF = SEATF.setdefault(name, {})
        for cid, c in W.cases.items():
            t = run.tasks.get(public_id(cid))
            if t is None or t.plant or not c.is_root or W.is_troop(c.actor) or t.fulfilled: continue
            ch = c.challenge
            if ch is None or ch.get("kind") != "dispute" or ch.get("challenger") != c.requester or not ch.get("resolved"): continue
            panel = [W.reviews[x] for x in ch["reviews"]]
            members = sum(1 for p_ in panel if not W.is_troop(p_.reviewer))
            k = MK[2 - members] if len(panel) >= 2 else None
            if k is None: continue
            cnt[k][0] += 1; cnt[k][1] += int(ch.get("outcome") == "N")
            # the joint of the two verdicts on the panel (the reviewer's read of November 10, the two-member panels the question): both confirm
            # the standing F, split, both reject — against the product of the single-seat confirmation rates
            vs = tuple(sorted(p_.verdict for p_ in panel[:2]))
            jk = "both confirm" if vs == ("F", "F") else ("both reject" if vs == ("N", "N") else "split")
            joint.setdefault(k, {"both confirm": 0, "split": 0, "both reject": 0})[jk] += 1
            seatF.setdefault(k, [0, 0]); seatF[k][0] += sum(1 for p_ in panel[:2] if p_.verdict == "F"); seatF[k][1] += 2
        for k in MK: per[k].append(cnt[k])
        cc = run.c
        counters.append({x: cc.get(x, 0) for x in ("appeals_unassignable_ticks", "panel_short_tier_ticks", "panel_short_free_ticks", "seated_appeal_member", "troop_panel_seats", "troop_audits", "panel_ineligible_member_periods", "disputes_filed", "disputes_won")})
        print(f"seed {seed} {name}: " + ", ".join(f"{k} {cnt[k][1]}/{cnt[k][0]}" for k in MK) + f"; short tier {cc.get('panel_short_tier_ticks',0)} free {cc.get('panel_short_free_ticks',0)}", flush=True)
    res[name] = (per, counters)
def ms(v): v = np.asarray(v, float); return f"{v.mean():.2f} ± {v.std(ddof=1)/np.sqrt(len(v)):.2f}"
L = [f"# The customers' truthful disputes by the panel's make-up, and the state's panel seats by cause — detection {rate}, run 42's final policy ({dmp}) and the careful, seeds {seeds[0]}–{seeds[-1]}\n",
     "| policy | make-up | disputes a run | won a run | **won share (pooled)** |", "|---|---|---|---|---|"]
for name, (per, counters) in res.items():
    for k in MK:
        a = np.array(per[k]); L.append(f"| {name} | {k} | {ms(a[:, 0])} | {ms(a[:, 1])} | {a[:, 1].sum() / max(1, a[:, 0].sum()):.3f} ({int(a[:, 0].sum())}) |")
L.append("\n| policy | member panel seats | state panel seats (audit + appeal) | state audits | panel seats unfilled at the driver's seating (ticks) | … a free member kept off the tier | … no member free | member-periods panel-ineligible |"); L.append("|---|---|---|---|---|---|---|---|")
for name, (per, counters) in res.items():
    g = lambda x: ms([c[x] for c in counters])
    L.append(f"| {name} | {g('seated_appeal_member')} | {g('troop_panel_seats')} | {g('troop_audits')} | {g('appeals_unassignable_ticks')} | {g('panel_short_tier_ticks')} | {g('panel_short_free_ticks')} | {g('panel_ineligible_member_periods')} |")
L.append("\nThe joint of the two verdicts on the customers' truthful disputes, by make-up (pooled): both confirm the standing F / split / both reject, against the product of the single-seat F rate p on the same panels (p², 2p(1−p), (1−p)²):\n")
L.append("| policy | make-up | panels | single-seat F rate p | both confirm (observed / p²) | split (observed / 2p(1−p)) | both reject (observed / (1−p)²) |"); L.append("|---|---|---|---|---|---|---|")
for name in res:
    for k in MK:
        j = JOINT.get(name, {}).get(k); sf = SEATF.get(name, {}).get(k)
        if not j or not sf or not sf[1]: continue
        n = sum(j.values()); p = sf[0] / sf[1]
        L.append(f"| {name} | {k} | {n} | {p:.3f} | {j['both confirm'] / n:.3f} / {p * p:.3f} | {j['split'] / n:.3f} / {2 * p * (1 - p):.3f} | {j['both reject'] / n:.3f} / {(1 - p) ** 2:.3f} |")
open(out, "w").write("\n".join(L) + "\n"); print("\n".join(L))

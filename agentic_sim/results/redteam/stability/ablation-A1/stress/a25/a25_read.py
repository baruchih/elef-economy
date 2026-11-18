"""Addendum 29 (November 18, 2026, later that morning; notes §124): how often one pair meets where care is scarce (AI3) — world 3's all-careful and read 29 run again whole at 8e30eac40
for the pair tally (checked to the digit against a23/rerun and a23/r29), read 32 from a24 — the mean over the pairs that meet, the share meeting more than three times, the largest, apart by
whether the audit seat is a careful slot's or the conduct's; the reviewer's even-spread arithmetic recomputed from the record; and the two counts of a careful slot's failed tests (AI4) from
the record. a24_read.py's helpers copied. Usage: a25_read.py OUT.md"""
import json, os, sys, hashlib, math, numpy as np
R = "results/redteam/stability/ablation-A1/stress"; D25, D24, D23 = f"{R}/a25", f"{R}/a24", f"{R}/a23"
def f(e, k): v = e.get(k); return float(v) if v not in (None, "") else np.nan
def mse(x): x = np.array(x, float); x = x[~np.isnan(x)]; return (x.mean(), x.std(ddof=1) / np.sqrt(len(x))) if len(x) > 1 else ((x.mean() if len(x) else np.nan), np.nan)
def slots(e): return list(json.loads(e["learner_slots_json"]).values())
def load(dirs, pol):
    E, C = [], {}
    for d in dirs:
        p = f"{d}/eval.json"
        if not os.path.exists(p): continue
        j = json.load(open(p))
        if pol in j["episodes"]: E += j["episodes"][pol]
        if "careful" in j["episodes"]: C.update({int(e["seed"]): e for e in j["episodes"]["careful"]})
    return E, C
def col(rows, k): return np.array([r[k] for r in rows], float)
def careful_of(e):
    """The slots' side of the mix: a name is the careful's where its hash falls at or above the share (as redteam.scripted.MixPolicy draws it)."""
    share = float(e.get("half_share") or 0.5); seed = int(e["seed"])
    return lambda x: int.from_bytes(hashlib.md5(f"{seed}:{x}".encode()).digest()[:2], "big") >= share * 65536
def pairs_of(e, side=None):
    """The pairs of a first reviewer and the member at its audit seat (the first seat a slot's; the alias pairs of d28f75da5's collections dropped), the audit seat's holder on `side` (None: every member; 'careful' / 'conduct' by the mix's hash)."""
    pmj = {k: v for k, v in json.loads(e.get("pair_meet_json") or "{}").items() if not k.startswith("plant_rev")}
    if side is not None:
        c = careful_of(e); pmj = {k: v for k, v in pmj.items() if c(k.split("|")[1]) == (side == "careful")}
    if not pmj: return None
    ns = [len(v) for v in pmj.values()]; firsts = {}
    for k, v in pmj.items(): firsts.setdefault(k.split("|")[0], set()).add(k.split("|")[1])
    S = json.loads(e["learner_slots_json"]); n = len(S); n_side = (sum(1 for x in S if careful_of(e)(x) == (side == "careful")) if side else n)
    return dict(pairs=len(ns), meetings=sum(ns), mean=np.mean(ns), gt3=sum(1 for x in ns if x > 3) / len(ns), mx=max(ns), partners=np.mean([len(s) for s in firsts.values()]), n=n, n_side=n_side,
                lam=sum(ns) / (n - 1) / n_side if n_side else np.nan)   # the audit seats on this side's slots spread evenly over the first reviewers (the reviewer's λ)
def pois(lam):
    """By chance alone (a Poisson count at λ a pair): the mean over the pairs that meet, and the share of them meeting more than three times."""
    p = [math.exp(-lam) * lam ** k / math.factorial(k) for k in range(4)]; return lam / (1 - p[0]), (1 - sum(p)) / (1 - p[0])
def repro(new_eps, old_eps, label):
    old = {int(e["seed"]): e for e in old_eps}; n_rows = n_keys = n_slots = n_seeds = 0; diffs = []; bm_d = []
    for e in new_eps:
        s_ = int(e["seed"])
        if s_ not in old: continue
        o = old[s_]; n_seeds += 1
        for k in o:
            if k in ("learner_slots_json", "bad_met_first_json"): continue
            n_rows += 1
            if o[k] != e.get(k): diffs.append((s_, k))
        So, Sn = json.loads(o["learner_slots_json"]), json.loads(e["learner_slots_json"])
        for x, v in So.items():
            n_slots += 1
            for k, val in v.items():
                n_keys += 1
                if Sn.get(x, {}).get(k) != val: diffs.append((s_, x, k))
        bo, bn = json.loads(o["bad_met_first_json"]), json.loads(e["bad_met_first_json"])
        for k, val in bo.items():
            if bn.get(k) != val: bm_d.append((s_, k))
    return f"- **{label}**: {n_seeds} seeds, {n_rows} row columns and {n_keys} per-slot keys over {n_slots} slots compared with the record's — **{len(diffs)} differences**" + (f" ({diffs[:5]})" if diffs else "") + f"; the `bad_met_first_json` tally **{len(bm_d)} differences**" + (f" ({bm_d[:4]})" if bm_d else "") + "."
CW3_23 = load([f"{D23}/rerun/cw3-s21-70", f"{D23}/rerun/cw3-s71-120"], "careful")[1]; CW3 = load([f"{D25}/rerun/cw3-s21-70", f"{D25}/rerun/cw3-s71-120"], "careful")[1]
R29_23 = load([f"{D23}/r29/s21-70", f"{D23}/r29/s71-120"], "mix:caseM0.2:0.75")[0]; R29 = load([f"{D25}/rerun/r29-s21-70", f"{D25}/rerun/r29-s71-120"], "mix:caseM0.2:0.75")[0]
R32 = load([f"{D24}/r32/s21-70", f"{D24}/r32/s71-120"], "mix:caseM0.1:0.75")[0]; R25 = load([f"{D24}/rerun/r25-s21-70", f"{D24}/rerun/r25-s71-120"], "mix:caseM0.1:1.0")[0]
R33 = load([f"{D24}/r33/s21-70", f"{D24}/r33/s71-120"], "mix:caseG0.1:1.0")[0]; R34 = load([f"{D24}/r34/s21-70", f"{D24}/r34/s71-120"], "mix:caseG0.1:1.0")[0]
L = ["# Addendum 29 — how often one pair meets where care is scarce, and two counts of a careful slot's failed tests (November 18, 2026; notes §124)\n"]
if CW3 and CW3_23: L.append(repro(list(CW3.values()), list(CW3_23.values()), "world 3's all-careful run again whole at 8e30eac40 (a23/rerun, itself 0 differences against a22/rerun)"))
if R29 and R29_23: L.append(repro(R29, R29_23, "read 29 run again whole at 8e30eac40 (a23/r29)"))
L.append(f"\nLoaded: cw3 {len(CW3)} (record {len(CW3_23)}), r29 {len(R29)} (record {len(R29_23)}), r32 {len(R32)}, r25 {len(R25)}, r33 {len(R33)}, r34 {len(R34)} episodes.\n")
# ---------------------------------------------------------------- AI3
L += ["## 1. How often one pair meets — a first reviewer and the member at its audit seat (AI3)\n",
      "Over a run, every member audit seat whose first seat was a slot's (the state's and the orchestrator's first seats apart): the pairs that meet, the mean over them, the share of them meeting more than three times, the largest; by the holder of the audit seat where the world has two conducts. The reviewer's even spread (R) is the side's audit seats over the first reviewers, λ = the side's member audit seats a run / (slots − 1) / the side's slots; by chance alone a Poisson count at λ gives the mean over the pairs that meet and the share over three.\n",
      "| population | audit seat's holder | member audit seats a run (a slot's first seat) | pairs that meet | **meetings a pair that meets** | **more than three times (share)** | the largest | members a first reviewer meets | λ, the even spread (R: his) | by chance alone: mean / share > 3 | the reviewer's range |", "|---|---|---|---|---|---|---|---|---|---|---|"]
EXP = {("cw3", None): ("0.93", "1.5–2.4 / 0.02–0.12"), ("r29", "careful"): ("2.56", "2.8–4.5 / 0.28–0.55"), ("r29", "conduct"): ("0.39", "1.2–1.8 / —"), ("r32", "careful"): ("1.26", "1.8–3.0 / 0.06–0.25"), ("r32", "conduct"): ("0.78", "1.4–2.2 / —")}
OUT = {}
for key, nm, E, sides in (("cw3", "world 3's all-careful", list(CW3.values()), (None,)), ("r29", "read 29: case-keyed M at 0.2 on 3 in 4", R29, (None, "careful", "conduct")), ("r32", "read 32: case-keyed M at 0.1 on 3 in 4", R32, (None, "careful", "conduct")),
                          ("r25", "read 25: M at 0.1 on every slot", R25, (None,)), ("r33", "read 33: two groups, today's picks", R33, (None,)), ("r34", "read 34: the seating by group", R34, (None,))):
    for side in sides:
        PR = [p for p in (pairs_of(e, side) for e in E) if p]
        if not PR: continue
        lam = np.mean(col(PR, "lam")); ch = pois(lam); OUT[(key, side)] = dict(mean=np.mean(col(PR, "mean")), gt3=np.mean(col(PR, "gt3")), mx=np.mean(col(PR, "mx")), lam=lam, ch=ch); ex = EXP.get((key, side), ("—", "—"))
        L.append(f"| {nm} | {side or 'any member'} | {np.mean(col(PR, 'meetings')):.0f} | {np.mean(col(PR, 'pairs')):.0f} | **{np.mean(col(PR, 'mean')):.2f}** | **{np.mean(col(PR, 'gt3')):.2f}** | {np.mean(col(PR, 'mx')):.1f} | {np.mean(col(PR, 'partners')):.1f} | {lam:.2f} ({ex[0]}) | {ch[0]:.1f} / {ch[1]:.2f} | {ex[1]} |")
L.append("\nThe pairs are the round-robin's: the audit seat goes to the next free panel-eligible member in id order after the last pick, so a first reviewer's audits fall to the few members free at its cases' turns and the same two meet many times where an even draw would give one or two.\n")
# ---------------------------------------------------------------- AI4
L += ["## 2. Two counts of a careful slot's failed tests (AI4) — world 3's all-careful, from the record\n"]
V = [v for e in (CW3 or CW3_23).values() for v in slots(e)]; n = len(V); S_ = ("initial", "resumed", "audit", "third", "appeal", "dispute"); mf = lambda v: sum(v.get(f"pw_member_{s}", 0) for s in S_); lostt = lambda v: v.get("ticks_member_noseat", 0) - v.get("ticks_member_noseat_undet", 0)
anyf = [v for v in V if v.get("pf_phase", "before") != "before"]; memf = [v for v in V if "pf_first_member_n" in v]; pro = [v for v in V if v.get("pw_probation_initial", 0) > 0]; lost = [v for v in V if lostt(v) > 0]
le3 = [v for v in memf if v["pf_first_member_n"] <= 3]; m47 = [v for v in memf if 4 <= v["pf_first_member_n"] <= 7]; ge8 = [v for v in memf if v["pf_first_member_n"] >= 8]
adm = [v for v in pro if "adm_t" in v]; carried = [v for v in adm if lostt(v) > 0 and mf(v) == 0]; ge8_lost = [v for v in ge8 if lostt(v) > 0]; ge8_two = [v for v in ge8_lost if mf(v) >= 2]; ge8_one = [v for v in ge8_lost if mf(v) == 1]; ge8_one_pro = [v for v in ge8_one if v.get("pw_probation_initial", 0) > 0]
nof = [v for v in lost if mf(v) == 0 and v.get("pw_probation_initial", 0) == 0]
L += [f"Of {n} slots on 100 seeds, **{len(anyf) / n:.3f} carry a wrong planted verdict in the run at any standing** — this is §118's '52 in 100 reach the first loss of their earned seats': the driver's phase from the first wrong verdict on (`pf_phase` 'lost' begins at `pfail_ticks[0]`, whatever the standing and whether or not the seats go, and ends at the next tick as a member with the seats, of zero length where the first failure takes nothing) — of which **{len(memf) / n:.3f} as a member** (§122's 0.41) and {len(pro) / n:.3f} on probation (an arrival's, or the way back's; the two overlap). "
      f"The seats are lost by the record — a member's ticks with a determined record and no earned seats — for **{len(lost) / n:.3f} of the slots**, {np.mean([lostt(v) for v in lost]):.0f} ticks each on the mean. By the road, in 100 of all slots:\n",
      "| how the earned seats come to be lost | slots (in 100 of all) | of the slots that lose them |", "|---|---|---|",
      f"| the first wrong verdict as a member with the bad window at 4 to 7 — the seats held and taken at once | {100 * sum(1 for v in m47 if lostt(v) > 0) / n:.1f} | {sum(1 for v in m47 if lostt(v) > 0) / len(lost):.2f} |",
      f"| the first wrong verdict as a member with the bad window at 3 or under — the record undetermined, the seats never yet held, withheld when it is determined until the window holds eight | {100 * sum(1 for v in le3 if lostt(v) > 0) / n:.1f} | {sum(1 for v in le3 if lostt(v) > 0) / len(lost):.2f} |",
      f"| a later wrong verdict as a member: the first with the window at eight or more took nothing, a second within it did | {100 * len(ge8_two) / n:.1f} | {len(ge8_two) / len(lost):.2f} |",
      f"| a wrong verdict carried from probation alone (an arrival admitted with it in the window, no wrong verdict as a member) | {100 * len(carried) / n:.1f} | {len(carried) / len(lost):.2f} |",
      f"| one wrong verdict as a member with the window at eight or more, and a wrong one on probation before it | {100 * len(ge8_one_pro) / n:.1f} | {len(ge8_one_pro) / len(lost):.2f} |",
      f"| otherwise — one wrong verdict as a member with the bad window at eight or more and nothing on probation: by the rule the only road left is a rejected *good* plant with the good record determined (four to seven good plants met; the tally carries the verdict, not the kind) | {100 * (len(ge8_one) - len(ge8_one_pro)) / n:.1f} | {(len(ge8_one) - len(ge8_one_pro)) / len(lost):.2f} |",
      f"| no wrong verdict recorded (a tick or so at the record's determination) | {100 * len(nof) / n:.1f} | {len(nof) / len(lost):.2f} |",
      f"\nThe first wrong verdict as a member by its window: at 3 or under {len(le3) / len(memf):.2f} of them (the seats not yet held; {sum(1 for v in le3 if lostt(v) > 0)} of {len(le3)} later carry lost ticks), at 4 to 7 {len(m47) / len(memf):.2f} ({sum(1 for v in m47 if lostt(v) > 0)} of {len(m47)} lose the seats), at 8 or more {len(ge8) / len(memf):.2f} ({len(ge8_lost)} of {len(ge8)} ever lose them in the run, {len(ge8) - len(ge8_lost)} never) — §122's 0.47 'take the seats at once' is the first two together, and {len(m47) / len(memf):.2f} of the first failures take seats a member held. Of the {len(pro)} slots with a wrong verdict on probation {len(adm)} are admitted within the run and {sum(1 for v in adm if lostt(v) > 0)} of those are members without the seats on a determined record, {len(carried)} with no wrong verdict of their own as a member. The rule as the engine has it: `record_passes(θ)` fails a kind whose window holds n_min or more with (wrong + 1) / (n + 2) above θ — one wrong bad plant fails θ_panel 0.20 at n ≤ 7, two at n ≤ 12; one rejected good plant at 4 ≤ n_good ≤ 7 (a careful slot meets 2.3 good plants as a member in a run, so that record is seldom determined).\n"]
open(sys.argv[1], "w").write("\n".join(L) + "\n"); print("wrote", sys.argv[1], len(L), "lines")

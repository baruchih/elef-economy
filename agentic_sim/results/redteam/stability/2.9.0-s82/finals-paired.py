"""§67: the 2.9.0 chains' finals (learned-rev-<cell>-290/) against the 2.8.0 chains' (-280/), seeds 21–40, paired by seed —
the shape of 2.8.0-s82/finals-paired.py with the 2.9.0 readings added (the planted approvals' life, the dial per seat, the planted
lies, the bad plants met by seat, the state's seats, the panel-ineligible member-periods, the mints by kind).
Usage: python3 finals-paired.py OUT.md [cell ...]
Env: SUF290 (default -290) the 2.9.0 side's directory suffix (e.g. -290b, the re-runs on the corrected engine after the rulings of §69);
BASESUF (default -280) the base side's; TAG290 / TAGBASE their column labels (default 2.9.0 / 2.8.0)."""
import json, sys, math, os
SUF290=os.environ.get("SUF290","-290"); BASESUF=os.environ.get("BASESUF","-280"); TAG290=os.environ.get("TAG290","2.9.0"); TAGBASE=os.environ.get("TAGBASE","2.8.0")
FINAL=os.environ.get("FINAL","final"); BASEFINAL=os.environ.get("BASEFINAL",FINAL)   # November 7, 2026: the finals' directory on each side (final-cr: the re-evaluation on the corrected engine, notes §77)
import numpy as np
R="results/redteam/stability"
CELLS=sys.argv[2:] or ["careful","liars","stamper","disputes","half","careful-A","liars-B"]
BASE={"careful-A":"careful","liars-B":"liars"}   # the ablations' 2.8.0 side is the cell they ablate from
BASECELL=dict(x.split(":") for x in os.environ.get("BASECELL","").split(",") if x)   # November 10, 2026: the base cell by name (e.g. pifloor:careful — the owed pinned cells against run 42)
def load(cell, suf, learner, side="290"):
    if side=="base": cell=BASECELL.get(cell, BASE.get(cell,cell) if BASESUF=="-280" else cell)
    p=f"{R}/learned-rev-{cell}{suf}/{learner}/eval/{FINAL if side=='290' else BASEFINAL}/eval.json" if "/" not in cell else \
      f"{R}/{cell}/{learner}/eval/{FINAL if side=='290' else BASEFINAL}/eval.json"   # November 10, 2026: a cell given as a path under results/redteam/stability (the ablation chains, ablation-A1/learned/<arm>)
    try: return json.load(open(p))
    except FileNotFoundError: return None
def eps(d,pol): return {e["seed"]:e for e in d["episodes"][pol]}
def arr(E,key,seeds):
    out=[]
    for s in seeds:
        v=E[s].get(key)
        try: out.append(float(v) if v not in (None,"") else np.nan)
        except (TypeError, ValueError): out.append(np.nan)
    return np.array(out)
def mse(x):
    x=x[~np.isnan(x)]; return (x.mean(), x.std(ddof=1)/math.sqrt(len(x))) if len(x)>1 else (np.nan,np.nan)
def fmt(m,s=None,d=1):
    if m is None or np.isnan(m): return "—"
    return f"{m:.{d}f}" if s is None else f"{m:+.{d}f} ± {s:.{d}f}"
def pooled_rate(E,seeds,seat,kind):
    st=sum(E[s].get(f"seat_{seat}_{kind}_stamped",0) for s in seeds); n=sum(E[s].get(f"seat_{seat}_{kind}_seen",0) for s in seeds)
    return (st/n if n else np.nan), n
def pooled_ratio(E,seeds,num,den):
    a=sum(float(E[s].get(num) or 0) for s in seeds); b=sum(float(E[s].get(den) or 0) for s in seeds)
    return (a/b if b else np.nan), b
KEYS=[("false_approvals_run","false approvals (run)",1),("bad_plants_approved","bad plants approved",1),("good_plants_rejected","good plants rejected",1),
      ("suspensions_run","suspensions",1),("audit_overturn_rate","audit overturn rate",3),("audits_held","audits held",0),("disputes_filed","disputes filed",1),("disputes_won","disputes won",1),
      ("appeals_filed","appeals filed",1),("appeals_won","appeals won",1),("true_rejections_appealed","lying appeals (real)",1),("true_rejections_overturned","lying appeals paid",1),
      ("true_approvals_disputed","lying disputes (real)",1),("true_approvals_overturned","lying disputes paid",1),
      ("learner_pop_n","slots alive",1),("pop_surplus_nominal","nominal surplus",0),("lifetime_real_wealth","real lifetime",0),("pop_tasks_per_1000","tasks per 1,000",1),
      ("P_t","P_t",1),("member_price_mean","members' price",1),("requester_wallet_mean","requesters' wallet",0),("state_share","state share",3),("awarded","awarded",0),("idle_for_bond_ticks","idle for bond",0),
      ("cost_of_truth","cost of truth",0),("life_real_state_seats","state seats per real root",3),("life_plant_state_seats","state seats per plant",3),("F_hat","F̂",3)]
KEYS+=[("leak_paid","leak: false approvals per vested task",4),("leak_bad","leak: false approvals per bad delivery",3),("sys_overhead_per_vested","system overhead a vested task",3),("cust_overhead_per_vested","customers' overhead a vested task",3),
       ("vest_ticks_p50","ticks to vest p50",1),("vest_ticks_p90","ticks to vest p90",1),("rulings","rulings sought",1),("rulings_wrong","rulings wrong",1),
       ("false_penalty_initial","false penalties: initial seat",2),("false_penalty_audit","false penalties: audit seat",2),("false_penalty_appeal","false penalties: panel seat",2)]   # November 10, 2026: the two leak figures and the overhead views (notes §78's plan), the owed cells read with them
ERR={"false_approvals_run","pop_surplus_nominal","lifetime_real_wealth","P_t","pop_tasks_per_1000","cost_of_truth"}
NEW=[("pa_posted","planted approvals posted",1),("pa_verdicts","their verdicts",1),("pa_audited","audited by a member",1),("pa_confirmed","confirmed at the audit seat",1),
     ("pa_rejected","rejected at the audit seat",1),("pa_third","third seats",1),("pa_state_audit","audited by the state (past w_R)",1),("pa_state_would_seat","the pass would have seated (read)",1),
     ("pa_disputed","disputed first",1),("pa_pass_would_audit","the pass would have taken the audit seat (read)",1),("pa_unseated","unseated at the window's end (closed by truth)",1),("obligations_discharged","obligations discharged at a dispute",1),("pa_closed","closed",1),
     ("m_A","m^A at the end",2),("pi_A","π^A at the end",3),("F_hat_A","F̂^A (last period)",3),
     ("plant_lies_coin","planted lies by the coin",1),("plant_lies_floor","planted lies by the floor",1),("life_real_filing_pos","filing position in the period: real",3),("life_plant_filing_pos","truthful plant",3),("life_lie_filing_pos","planted lie",3),
     ("plant_lies_filed_appeal","planted appeals filed",1),("lie_adj_appeal","their seats answered by members",1),("lie_sided_appeal","members siding with the lie",1),("m_La","m^La at the end",2),("pi_La","π^La at the end",3),("F_hat_La","F̂^La (last period)",3),
     ("plant_lies_filed_dispute","planted disputes filed",1),("lie_adj_dispute","their seats answered by members",1),("lie_sided_dispute","members siding with the lie",1),("m_Ld","m^Ld at the end",2),("pi_Ld","π^Ld at the end",3),("F_hat_Ld","F̂^Ld (last period)",3),
     ("bad_met_initial","bad plants met at the initial seat",1),("bad_met_audit","at the audit seat",1),("bad_met_third","at the third seat",1),("bad_met_appeal","at an appeal panel",1),("bad_met_dispute","at a dispute panel",1),
     ("member_periods","member-periods",1),("panel_ineligible_member_periods","of them panel-ineligible",1),
     ("plant_mint_dial","minted: the dial's plants",0),("plant_mint_approval","minted: the planted approvals",0),("plant_mint_lie","minted: the planted lies",0),("plant_mint_rev","minted: the alias reviewer's bonds",0)]
out=[]
def P(*a): out.append(" ".join(str(x) for x in a))
P(f"# §8.2: the {TAG290} chains' finals (learned-rev-<cell>{SUF290}/{{direct,wm}}/eval/{FINAL}/, seeds 21–40) beside the {TAGBASE} chains' ({BASESUF}/, eval/{BASEFINAL}/), the same seeds and references; paired {TAG290} − {TAGBASE} by seed; within 2.9.0 paired against the hand; the 2.9.0 readings; the rounds' mix; the stages after the first verdict. Produced by finals-paired.py over the eval.json files.")
for cell in CELLS:
    W={}
    for suf,tag,side in ((SUF290,TAG290,"290"),(BASESUF,TAGBASE,"base")):
        for L in ("direct","wm"):
            d=load(cell,suf,L,side)
            if d is not None: W[(tag,L)]=d
    if not any(k[0]==TAG290 for k in W): continue
    P(f"\n## {cell}\n")
    for k in ((TAG290,"direct"),(TAG290,"wm"),(TAGBASE,"direct"),(TAGBASE,"wm")):
        if k not in W: P(f"missing {cell} {k[0]} {k[1]}")
    seeds=list(range(21,41))
    cols=[]
    for tag in (TAG290,TAGBASE):
        for pol,L in (("direct","direct"),("greedy","wm"),("hand","direct"),("careful","direct")):
            d=W.get((tag,L))
            name={"direct":"direct","greedy":"head alone","hand":"hand","careful":"careful"}[pol]
            if d is None or pol not in d["episodes"]: cols.append((f"{tag} {name}",None)); continue
            cols.append((f"{tag} {name}", eps(d,pol)))
    P("| reading | "+" | ".join(c[0] for c in cols)+" |"); P("|---|"+"---|"*len(cols))
    r=[]
    for n,E in cols:
        if E is None: r.append("—"); continue
        c=arr(E,"care_share",seeds).mean(); a=arr(E,"approve_blind_share",seeds).mean(); j=arr(E,"reject_blind_share",seeds).mean()
        r.append(f"{c:.3f} / {a:.3f} / {j:.3f}")
    P("| mix care / approve / reject | "+" | ".join(r)+" |")
    for seat in ("initial","audit","panel"):
        r=[]
        for n,E in cols:
            if E is None: r.append("—"); continue
            pr,pn=pooled_rate(E,seeds,seat,"plant"); rr,rn=pooled_rate(E,seeds,seat,"real")
            r.append(f"{fmt(pr,d=3)} ({pn}) / {fmt(rr,d=3)} ({rn})")
        P(f"| {seat} seats stamped plant / real | "+" | ".join(r)+" |")
    for seat in ("initial","audit","panel"):                               # the same rates measured from the engine's reviews (November 7, 2026; carries the hand's)
        r=[]; anyv=False
        for n,E in cols:
            if E is None: r.append("—"); continue
            def mrate(kind):
                n_=sum(E[s].get(f"measured_{seat}_{kind}_seen",0) for s in seeds); b=sum(E[s].get(f"measured_{seat}_{kind}_approve_blind",0)+E[s].get(f"measured_{seat}_{kind}_reject_blind",0) for s in seeds)
                return (b/n_ if n_ else np.nan), n_
            if not any(f"measured_{seat}_real_seen" in E[s] for s in seeds): r.append("—"); continue
            anyv=True; pr,pn=mrate("plant"); rr,rn=mrate("real"); r.append(f"{fmt(pr,d=3)} ({pn}) / {fmt(rr,d=3)} ({rn})")
        if anyv: P(f"| {seat} seats blind, measured from the reviews, plant / real | "+" | ".join(r)+" |")
    r=[]
    for n,E in cols:
        if E is None: r.append("—"); continue
        pr,pn=pooled_ratio(E,seeds,"pa_confirmed","pa_audited")
        r.append(f"{fmt(pr,d=3)} ({int(pn)})" if n.startswith(TAG290) and "pa_audited" in next(iter(E.values())) else "—")
    P("| planted approvals confirmed at the members' audit seat (pooled F̂^A) | "+" | ".join(r)+" |")
    r=[]
    for n,E in cols:
        if E is None: r.append("—"); continue
        st=sum(E[s]["blind_seat_stamps"] for s in seeds); nn=sum(E[s]["blind_seats"] for s in seeds); dec=sum(E[s]["decisions"] for s in seeds)
        r.append(f"{st/nn if nn else float('nan'):.3f} ({nn/dec:.3f})")
    P("| non-initial seats stamped (share of decisions) | "+" | ".join(r)+" |")
    for key,label,dd in KEYS:
        r=[]
        for n,E in cols:
            if E is None: r.append("—"); continue
            m,s=mse(arr(E,key,seeds)); r.append(f"{m:.{dd}f} ± {s:.{dd}f}" if key in ERR else f"{m:.{dd}f}")
        P(f"| {label} | "+" | ".join(r)+" |")
    P(f"\nThe {TAG290} readings (means over the seeds):\n")
    P("| reading | "+" | ".join(c[0] for c in cols[:4])+" |"); P("|---|---|---|---|---|")
    for key,label,dd in NEW:
        r=[]
        for n,E in cols[:4]:
            if E is None: r.append("—"); continue
            m,s=mse(arr(E,key,seeds)); r.append(f"{m:.{dd}f}")
        P(f"| {label} | "+" | ".join(r)+" |")
    r=[]
    for n,E in cols[:4]:
        if E is None: r.append("—"); continue
        m,_=pooled_ratio(E,seeds,"pa_state_audit","pa_verdicts"); r.append(fmt(m,d=3))
    P("| share of planted approvals audited by the state | "+" | ".join(r)+" |")
    r=[]
    for n,E in cols[:4]:
        if E is None: r.append("—"); continue
        m,_=pooled_ratio(E,seeds,"panel_ineligible_member_periods","member_periods"); r.append(fmt(m,d=3))
    P("| share of member-periods panel-ineligible | "+" | ".join(r)+" |")
    r=[]
    for n,E in cols[:4]:
        if E is None: r.append("—"); continue
        m,_=pooled_ratio(E,seeds,"bad_met_audit","bad_met_initial"); r.append(fmt(m,d=3))
    P("| bad plants met at the audit seat per one met at the initial seat | "+" | ".join(r)+" |")
    r=[]
    for n,E in cols[:4]:
        if E is None: r.append("—"); continue
        a,_=pooled_ratio(E,seeds,"lie_sided_appeal","lie_adj_appeal"); b,_=pooled_ratio(E,seeds,"lie_sided_dispute","lie_adj_dispute"); r.append(f"{fmt(a,d=3)} / {fmt(b,d=3)}")
    P("| members siding with the planted lie, appeal / dispute (pooled F̂^La / F̂^Ld) | "+" | ".join(r)+" |")
    P(f"\nPaired {TAG290} − {TAGBASE} by seed (same seeds, the same policy class; for the learners the two chains' own policies):\n")
    P("| reading | direct | head alone | hand | careful |"); P("|---|---|---|---|---|")
    for key,label,dd in KEYS+[("care_share","care share",3),("approve_blind_share","approve blind",3),("reject_blind_share","reject blind",3)]:
        r=[]
        for i in range(4):
            A=cols[i][1]; B=cols[i+4][1]
            if A is None or B is None: r.append("—"); continue
            m,s=mse(arr(A,key,seeds)-arr(B,key,seeds)); r.append(fmt(m,s,dd))
        P(f"| {label} | "+" | ".join(r)+" |")
    for seat in ("initial","audit","panel"):
        for kind in ("plant","real"):
            r=[]
            for i in range(4):
                A=cols[i][1]; B=cols[i+4][1]
                if A is None or B is None: r.append("—"); continue
                def rate(E,s):
                    n=E[s].get(f"seat_{seat}_{kind}_seen",0); return E[s].get(f"seat_{seat}_{kind}_stamped",0)/n if n else np.nan
                x=np.array([rate(A,s)-rate(B,s) for s in seeds]); m,s_=mse(x); r.append(fmt(m,s_,3))
            P(f"| {seat} {kind} stamp rate (per seed) | "+" | ".join(r)+" |")
    P(f"\nWithin {TAG290}, paired against the hand on the same seeds:\n")
    P("| reading | direct − hand | head alone − hand | careful − hand |"); P("|---|---|---|---|")
    H=cols[2][1]
    for key,label,dd in KEYS:
        r=[]
        for i in (0,1,3):
            A=cols[i][1]
            if A is None or H is None: r.append("—"); continue
            m,s=mse(arr(A,key,seeds)-arr(H,key,seeds)); r.append(fmt(m,s,dd))
        P(f"| {label} | "+" | ".join(r)+" |")
    for i in (0,1):
        A=cols[i][1]
        if A and H:
            fa=arr(A,"false_approvals_run",seeds); fh=arr(H,"false_approvals_run",seeds)
            P(f"- {cols[i][0]}: false approvals / hand's = {fa.mean()/fh.mean():.2f}; seeds above the hand: {(fa>fh).sum()}/20")
    H2=cols[6][1]
    for i in (4,5):
        A=cols[i][1]
        if A and H2:
            fa=arr(A,"false_approvals_run",seeds); fh=arr(H2,"false_approvals_run",seeds)
            P(f"- {cols[i][0]}: false approvals / hand's = {fa.mean()/fh.mean():.2f}; seeds above the hand: {(fa>fh).sum()}/20")
    P(f"\nMix by period ({TAG290} finals, pooled over seeds):")
    for i in (0,1):
        n,E=cols[i]
        if E is None: continue
        agg={}
        for s in seeds:
            m=json.loads(E[s]["learner_mix_by_period"])
            for p,row in enumerate(m):
                a=agg.setdefault(p,[0,0,0])
                for k in range(3): a[k]+=row[k]
        P(f"- **{n}**: "+"; ".join(f"p{p} {a[0]/sum(a):.3f}/{a[1]/sum(a):.3f}/{a[2]/sum(a):.3f} ({sum(a)//20})" for p,a in sorted(agg.items()) if sum(a)))
    P(f"\nStages after the first verdict ({TAG290} finals), real / plant, pooled; then plant − real period-matched (real rates reweighted by the plants' count per period), paired by seed:")
    P("| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats | Δ audited (matched) | Δ state seats (matched) | Δ filed (matched) |"); P("|---|---|---|---|---|---|---|---|---|---|")
    for i in (0,1,2,3):
        n,E=cols[i]
        if E is None: continue
        def g(k):
            m,_=mse(arr(E,k,seeds)); return m
        da=[];ds=[];df=[]
        for s in seeds:
            if "life_by_period" not in E[s]: continue             # the stage table by period is 8b26ebf6's; a 2.7.0 chain of record read before it has none
            lb=json.loads(E[s]["life_by_period"])
            na=0;ns=0;nf=0;npl=0
            for p,kk in lb.items():
                pl=kk.get("plant",{}); re=kk.get("real",{})
                if not pl.get("n") or not re.get("n"): continue
                npl+=pl["n"]
                na+=pl.get("audit_n",0)-re.get("audit_n",0)/re["n"]*pl["n"]
                ns+=pl.get("state_seats",0)-re.get("state_seats",0)/re["n"]*pl["n"]
                nf+=pl.get("filing_n",0)-re.get("filing_n",0)/re["n"]*pl["n"]
            if npl: da.append(na/npl); ds.append(ns/npl); df.append(nf/npl)
        da=np.array(da); ds=np.array(ds); df=np.array(df)
        P(f"| {n} | {g('life_real_audit_share'):.3f} / {g('life_plant_audit_share'):.3f} | {g('life_real_audit_wait'):.2f} / {g('life_plant_audit_wait'):.2f} | {g('life_real_filing_share'):.3f} / {g('life_plant_filing_share'):.3f} | {g('life_real_filing_delay'):.2f} / {g('life_plant_filing_delay'):.2f} | {g('life_real_panel_wait'):.2f} / {g('life_plant_panel_wait'):.2f} | {g('life_real_state_seats'):.3f} / {g('life_plant_state_seats'):.3f} | {fmt(*mse(da),3)} | {fmt(*mse(ds),3)} | {fmt(*mse(df),3)} |")
open(sys.argv[1],"w").write("\n".join(out)+"\n"); print("\n".join(out))

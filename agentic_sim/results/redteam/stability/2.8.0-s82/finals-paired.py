"""§54: the four 2.8.0 chains' finals against the 2.7.0 (-2) chains', seeds 21–40, paired by seed."""
import json, sys, math
import numpy as np
R="results/redteam/stability"
CELLS=["careful","stamper","disputes","half"]
def load(cell, suf, learner):
    p=f"{R}/learned-rev-{cell}{suf}/{learner}/eval/final/eval.json"
    try: return json.load(open(p))
    except FileNotFoundError: return None
def eps(d,pol): return {e["seed"]:e for e in d["episodes"][pol]}
def arr(E,key,seeds):
    out=[]
    for s in seeds:
        v=E[s].get(key)
        out.append(float(v) if v not in (None,"") else np.nan)
    return np.array(out)
def mse(x):
    x=x[~np.isnan(x)]; return (x.mean(), x.std(ddof=1)/math.sqrt(len(x))) if len(x)>1 else (np.nan,np.nan)
def fmt(m,s=None,d=1):
    if np.isnan(m): return "—"
    return f"{m:.{d}f}" if s is None else f"{m:+.{d}f} ± {s:.{d}f}"
def pooled_rate(E,seeds,seat,kind):
    st=sum(E[s].get(f"seat_{seat}_{kind}_stamped",0) for s in seeds); n=sum(E[s].get(f"seat_{seat}_{kind}_seen",0) for s in seeds)
    return (st/n if n else np.nan), n
KEYS=[("false_approvals_run","false approvals (run)",1),("bad_plants_approved","bad plants approved",1),("good_plants_rejected","good plants rejected",1),
      ("suspensions_run","suspensions",1),("audit_overturn_rate","audit overturn rate",3),("disputes_filed","disputes filed",1),("disputes_won","disputes won",1),
      ("learner_pop_n","slots alive",1),("pop_surplus_nominal","nominal surplus",0),("lifetime_real_wealth","real lifetime",0),("pop_tasks_per_1000","tasks per 1,000",1),
      ("P_t","P_t",1),("requester_wallet_mean","requesters' wallet",0),("state_share","state share",3),("awarded","awarded",0),("idle_for_bond_ticks","idle for bond",0),
      ("F_hat","F̂",3)]
out=[]
def P(*a): out.append(" ".join(str(x) for x in a))
for cell in CELLS:
    P(f"\n## {cell}\n")
    W={}
    for suf,tag in (("-280","2.8.0"),("-2","2.7.0")):
        for L in ("direct","wm"):
            d=load(cell,suf,L)
            if d is None: P(f"missing {cell}{suf}/{L}"); continue
            W[(tag,L)]=d
    seeds=list(range(21,41))
    # columns: 2.8.0 direct, 2.8.0 wm, 2.8.0 hand, 2.8.0 careful, 2.7.0 direct, 2.7.0 wm, 2.7.0 hand, 2.7.0 careful
    cols=[]
    for tag in ("2.8.0","2.7.0"):
        for pol,L in (("direct","direct"),("greedy","wm"),("hand","direct"),("careful","direct")):
            d=W.get((tag,L))
            if d is None: cols.append((f"{tag} {pol if L=='direct' else 'head alone'}",None)); continue
            name = {"direct":"direct","greedy":"head alone","hand":"hand","careful":"careful"}[pol]
            cols.append((f"{tag} {name}", eps(d,pol)))
    P("| reading | "+" | ".join(c[0] for c in cols)+" |"); P("|---|"+"---|"*len(cols))
    def mixrow():
        r=[]
        for n,E in cols:
            if E is None: r.append("—"); continue
            c=arr(E,"care_share",seeds).mean(); a=arr(E,"approve_blind_share",seeds).mean(); j=arr(E,"reject_blind_share",seeds).mean()
            r.append(f"{c:.3f} / {a:.3f} / {j:.3f}")
        return r
    P("| mix care / approve / reject | "+" | ".join(mixrow())+" |")
    for seat in ("initial","audit","panel"):
        r=[]
        for n,E in cols:
            if E is None: r.append("—"); continue
            pr,pn=pooled_rate(E,seeds,seat,"plant"); rr,rn=pooled_rate(E,seeds,seat,"real")
            r.append(f"{fmt(pr,d=3)} ({pn}) / {fmt(rr,d=3)} ({rn})")
        P(f"| {seat} seats stamped plant / real | "+" | ".join(r)+" |")
    r=[]
    for n,E in cols:
        if E is None: r.append("—"); continue
        st=sum(E[s]["blind_seat_stamps"] for s in seeds); nn=sum(E[s]["blind_seats"] for s in seeds)
        dec=sum(E[s]["decisions"] for s in seeds)
        r.append(f"{st/nn if nn else float('nan'):.3f} ({nn/dec:.3f})")
    P("| non-initial seats stamped (share of decisions) | "+" | ".join(r)+" |")
    for key,label,dd in KEYS:
        r=[]
        for n,E in cols:
            if E is None: r.append("—"); continue
            m,s=mse(arr(E,key,seeds)); r.append(f"{m:.{dd}f} ± {s:.{dd}f}" if key in ("false_approvals_run","pop_surplus_nominal","lifetime_real_wealth","P_t","pop_tasks_per_1000") else f"{m:.{dd}f}")
        P(f"| {label} | "+" | ".join(r)+" |")
    # paired: 2.8.0 − 2.7.0 by seed, per policy
    P("\nPaired 2.8.0 − 2.7.0 by seed (same seeds, the same policy class; for the learners the two chains' own policies):\n")
    P("| reading | direct | head alone | hand | careful |"); P("|---|---|---|---|---|")
    for key,label,dd in KEYS+[("care_share","care share",3),("approve_blind_share","approve blind",3)]:
        r=[]
        for i in range(4):
            A=cols[i][1]; B=cols[i+4][1]
            if A is None or B is None: r.append("—"); continue
            m,s=mse(arr(A,key,seeds)-arr(B,key,seeds)); r.append(fmt(m,s,dd))
        P(f"| {label} | "+" | ".join(r)+" |")
    # paired against hand within 2.8.0
    P("\nWithin 2.8.0, paired against the hand on the same seeds:\n")
    P("| reading | direct − hand | head alone − hand | careful − hand |"); P("|---|---|---|---|")
    H=cols[2][1]
    for key,label,dd in KEYS:
        r=[]
        for i in (0,1,3):
            A=cols[i][1]
            if A is None or H is None: r.append("—"); continue
            m,s=mse(arr(A,key,seeds)-arr(H,key,seeds)); r.append(fmt(m,s,dd))
        P(f"| {label} | "+" | ".join(r)+" |")
    # ratio of false approvals to hand
    for i in (0,1):
        A=cols[i][1]
        if A and H:
            fa=arr(A,"false_approvals_run",seeds); fh=arr(H,"false_approvals_run",seeds)
            P(f"- {cols[i][0]}: false approvals / hand's = {fa.mean()/fh.mean():.2f}; seeds above the hand: {(fa>fh).sum()}/20")
    for i in (4,5):
        A=cols[i][1]; H2=cols[6][1]
        if A and H2:
            fa=arr(A,"false_approvals_run",seeds); fh=arr(H2,"false_approvals_run",seeds)
            P(f"- {cols[i][0]}: false approvals / hand's = {fa.mean()/fh.mean():.2f}; seeds above the hand: {(fa>fh).sum()}/20")
    # mix by period (2.8.0 learners)
    P("\nMix by period (2.8.0 finals, pooled over seeds):")
    for i in (0,1):
        n,E=cols[i]
        if E is None: continue
        agg={}
        for s in seeds:
            m=json.loads(E[s]["learner_mix_by_period"])
            for p,row in enumerate(m):
                a=agg.setdefault(p,[0,0,0]); 
                for k in range(3): a[k]+=row[k]
        P(f"- **{n}**: "+"; ".join(f"p{p} {a[0]/sum(a):.3f}/{a[1]/sum(a):.3f}/{a[2]/sum(a):.3f} ({sum(a)//20})" for p,a in sorted(agg.items()) if sum(a)))
    # post-verdict stages, pooled and period-matched (2.8.0 finals)
    P("\nStages after the first verdict (2.8.0 finals), real / plant, pooled; then plant − real period-matched (real rates reweighted by the plants' count per period), paired by seed:")
    P("| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats | Δ audited (matched) | Δ state seats (matched) | Δ filed (matched) |"); P("|---|---|---|---|---|---|---|---|---|---|")
    for i in (0,1,2,3):
        n,E=cols[i]
        if E is None: continue
        def g(k): 
            m,_=mse(arr(E,k,seeds)); return m
        da=[];ds=[];df=[]
        for s in seeds:
            lb=json.loads(E[s]["life_by_period"])
            na=0;ns=0;nf=0;npl=0
            for p,kk in lb.items():
                pl=kk.get("plant",{}); re=kk.get("real",{})
                if not pl.get("n") or not re.get("n"): continue
                npl+=pl["n"]
                na+=pl.get("audit_n",0)-re.get("audit_n",0)/re["n"]*pl["n"]
                ns+=pl.get("state_seats",0)-re.get("state_seats",0)/re["n"]*pl["n"]
                nf+=pl.get("filing_n",0)-re.get("filing_n",0)/re["n"]*pl["n"]
            da.append(na/npl); ds.append(ns/npl); df.append(nf/npl)
        da=np.array(da); ds=np.array(ds); df=np.array(df)
        P(f"| {n} | {g('life_real_audit_share'):.3f} / {g('life_plant_audit_share'):.3f} | {g('life_real_audit_wait'):.2f} / {g('life_plant_audit_wait'):.2f} | {g('life_real_filing_share'):.3f} / {g('life_plant_filing_share'):.3f} | {g('life_real_filing_delay'):.2f} / {g('life_plant_filing_delay'):.2f} | {g('life_real_panel_wait'):.2f} / {g('life_plant_panel_wait'):.2f} | {g('life_real_state_seats'):.3f} / {g('life_plant_state_seats'):.3f} | {fmt(*mse(da),3)} | {fmt(*mse(ds),3)} | {fmt(*mse(df),3)} |")
open(sys.argv[1],"w").write("\n".join(out)); print("\n".join(out))

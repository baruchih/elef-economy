"""The decision-event environment (the build plan, decision 3): one step is one decision of the learner's — here a reviewer's answer on
an assignment — and the engine with the hand-written population runs between decisions. The driver runs in a worker thread and blocks at
each of the learner's decisions until `step` supplies the action; nothing else touches the engine. Reward: the change in the learner's
lifetime real wealth since its last decision (the sum is the brief's §1 measure — the evaluation). The *training* reward, since the
reviewer's method ruling after the calibration ladder (October 21, 2026), is the attributed one: what the decision caused on its own case,
credited back when it lands, the suspension's forgone income charged to the plant failures that bought it, the index's revaluation out
(`redteam.attrib`; the terminal info carries `attributed` per decision beside `realized`, and the collectors store both). Actions: 0 care
(the careful disposition's signal at its cost), 1 approve blind, 2 reject blind. The run's cell is the stamping driver's own argument list, so the control is the same cell with
`--learner-slot off`. With the driver's `--learner-rearrive on` (the ruling after run 22) a second kind of decision arrives at each
period boundary — stay or leave and return under a fresh name — flagged in the observation; the lifetime is summed across the identities.
Version 4 (the ruling after version 3's calibration): a leave the economy refuses (a live commitment at the boundary) is recorded as the action
effected, a stay — the step's info carries `action_effected` beside `action_chosen`, and the collectors store the effected action as the
decision's and the choice beside it — so the training data separates an admitted leave (nothing follows) from a stay (the period's work).
Q3 (`role="deliverer"`): the learner is the slot actor as a deliverer — it reviews as the population's actor at its slot does, and a decision
arrives at each of its submissions: 0 deliver well (the work fulfilled, the effort burned), 1 deliver badly (unfulfilled, zero effort) — two
actions; the boundary decision as before (0 stay, 1 leave for good). The observation is `obs.build_obs_work`; the training reward attributes the
case's events (the price, the effort, a guarantee forfeited) to the submission's decision (`work_side` on).
Q4 (`role="pair"`): two learners with a shared reward — the slot a deliverer, the next careful id a reviewer kept on duty — in one environment: a
work decision (the deliverer's, two actions; a third is read as "well") and a review decision (the reviewer's, three) arrive in the order the
run poses them, each flagged by a 46th field `decision_work`; the reward is the pair's lifetime real wealth; the attribution credits a case's
events to every decision of the pair on that case (the shared training reward; a double count in the sum, recorded)."""
from __future__ import annotations
import queue
import threading
import numpy as np

try:
    import gymnasium as gym
    from gymnasium import spaces
except ImportError:  # the project's own Python has no gymnasium; the environment is only built in `elef-redteam`
    gym = None

from drivers import stamping
from drivers.stamping import Stamping
from sim import check_all
from .obs import build_obs, build_obs_work, build_obs_parent, build_obs_bid, build_obs_req, OBS_DIM, IDX, IDX_PARENT
from .attrib import attribute

_END = "end"


class _Abort(Exception):
    pass


class ElefReviewerEnv(gym.Env if gym else object):
    metadata = {"render_modes": []}

    def __init__(self, cell_args, ticks=1000, hide=(), final_audit=True, obs_dim=None, work_side=None, role="reviewer"):
        assert role in ("reviewer", "deliverer", "pair", "child", "parent", "bidder", "requester")
        self.role = role
        self.n_actions = 2 if role == "deliverer" else 3           # the child's three: well / badly / miss; the parent's judge has three, its other kinds two
        self.cell_args, self.ticks, self.hide, self.final_audit = list(cell_args), int(ticks), tuple(hide), final_audit
        self.work_side = bool(work_side) if work_side is not None else (role != "reviewer")    # the learner's own work attributed (Q3 on)
        self.obs_dim = int(obs_dim) if obs_dim else (OBS_DIM + 1 if role == "pair" else OBS_DIM)   # a model trained before a field was added reads the vector trimmed; the pair's 46th field flags a work decision
        if gym:
            self.observation_space = spaces.Box(-np.inf, np.inf, shape=(self.obs_dim,), dtype=np.float32)
            self.action_space = spaces.Discrete(self.n_actions)
        self.run = None
        self._thread = None
        self._seed = 0

    # -- the learner's lifetime real wealth: present, or taken out at departure
    def _real(self):
        mk = self.run.w.market()
        return mk["P0"] / (mk["P_t"] or mk["P0"])

    def _wealth_real(self):
        run = self.run
        if self.role == "requester":                                # Q7: the requester's measure is its surplus (the driver's `req_lifetime_real`), not a wallet
            return run.req_lifetime_real()
        real = self._real()
        # 2.7.0: a live name reads net of its arrival loan outstanding — what it would carry out; a departed one what it did
        return sum(((run.w.wealth(x) - min(run.w.wealth(x), run.w.loan_outstanding(x))) * real) if x in run.actors else run.depart_wealth_real.get(x, 0.0)
                   for x in run.learner_chain)

    def _hook(self, run, reviewer, view, r):
        if self._abort:
            raise _Abort()
        boundary = view is None
        if boundary and self.role in ("deliverer", "child"):
            obs = build_obs_work(run, reviewer, None, self.hide, n_fields=self.obs_dim)
        elif boundary and self.role == "parent":
            obs = build_obs_parent(run, reviewer, None, None, None, self.hide, n_fields=self.obs_dim)
        elif boundary and self.role == "bidder":
            obs = build_obs_bid(run, reviewer, None, self.hide, n_fields=self.obs_dim)
        else:
            obs = build_obs(run, reviewer, view, r, self.hide, n_fields=self.obs_dim)
        obs = self._flag(obs, 0.0)
        # the label for the Q2 probe only — read after the fact, never in the observation: was the assignment a plant?
        ac = run.w.actor(reviewer)
        self._q_obs.put(("obs", obs, {"t": run.w.t, "wealth_real": self._wealth_real(), "case": None if boundary else view.case_id, "boundary": boundary,
                                      "n_events": run.w.n_events(), "real_factor": self._real(),   # the ledger's position and the index at the observation (redteam.timing)
                                      "identity": reviewer, "kind": "boundary" if boundary else "review",
                                      "initial": False if boundary else bool(view.responses_available),   # an initial review of an unrevised submission (2.7.0: where a plant could be)
                                      # 2.8.0: the seat's kind from the view alone — what the learner can tell (§8.3): a first review answers P or ⊥, a panel states its
                                      # question, a resumed review says so, an audit is the fulfillment question with neither
                                      "seat": None if boundary else ("initial" if view.responses_available else ("panel" if view.question != "fulfillment" else ("resumed" if view.resumed else "audit"))),
                                      "is_plant": False if boundary else bool(run.tasks[view.case_id].plant), "fulfilled": True if boundary else bool(run.tasks[view.case_id].fulfilled),
                                      # Q1's readings (the evaluation's trace, never the policy's input): the applied odds and standing at the decision
                                      "p_eff": float(run.w.p_effective(reviewer)), "member": bool(ac.is_member), "suspended": ac.suspended_until is not None}))
        a = self._q_act.get()
        if a is None:
            raise _Abort()
        return a

    def _hook_work(self, run, actor, c):
        """Q3: the learned deliverer's quality decision at a submission — the observation is its own case and its standing; the truth is set by
        the action, never shown. Recorded with the case, so the attribution credits the case's events (the price, the effort, a guarantee
        forfeited, a court fee) to this decision."""
        if self._abort:
            raise _Abort()
        obs = self._flag(build_obs_work(run, actor, c, self.hide, n_fields=self.obs_dim), 1.0)
        ac = run.w.actor(actor)
        self._q_obs.put(("obs", obs, {"t": run.w.t, "wealth_real": self._wealth_real(), "case": c.id, "boundary": False, "kind": "work", "initial": False,
                                      "n_events": run.w.n_events(), "real_factor": self._real(), "identity": actor,
                                      "is_plant": False, "fulfilled": True,
                                      "price": float(c.B), "bond": float(c.G_award if c.G_award is not None else c.G), "nested": not c.is_root,
                                      "cost": float(run.cost_now(actor)),
                                      "p_eff": float(run.w.p_effective(actor)), "member": bool(ac.is_member), "suspended": ac.suspended_until is not None}))
        a = self._q_act.get()
        if a is None:
            raise _Abort()
        return a

    def _hook_req(self, run, requester, cands):
        """Q7: the learned requester's decision at a posting — the rule its ceiling follows (0 the market rule's, 1 patient, 2 the floor).
        Recorded with no case; the driver names the case it posted (`learner_last_bid_case`, the bidder's channel) and `step` credits it to this decision,
        so the attribution carries the case's events (the price paid, the pots, the refunds, a court fee, a rebate) and the task's value to the posting that made it."""
        if self._abort:
            raise _Abort()
        obs = build_obs_req(run, requester, cands, self.hide, n_fields=self.obs_dim)
        self._q_obs.put(("obs", obs, {"t": run.w.t, "wealth_real": self._wealth_real(), "case": None, "boundary": False, "kind": "post", "initial": False,
                                      "n_events": run.w.n_events(), "real_factor": self._real(), "identity": requester,
                                      "is_plant": False, "fulfilled": True, "betas": list(cands["beta"]), "affordable": list(cands["affordable"]),
                                      "p_eff": 0.0, "member": False, "suspended": False}))
        a = self._q_act.get()
        if a is None:
            raise _Abort()
        return a

    def _hook_bid(self, run, actor, roots):
        """Q6: the learned bidder's decision for the tick — the rule its offers follow (0 the ratchet's bid, 1 at cost, 2 none). Recorded with no case;
        if the tick's offers win an award the driver names the case (`learner_last_bid_case`) and `step` credits it to this decision, so the attribution
        carries the case's events (the price, the effort, a guarantee forfeited) to the bid that won it."""
        if self._abort:
            raise _Abort()
        obs = build_obs_bid(run, actor, roots, self.hide, n_fields=self.obs_dim)
        ac = run.w.actor(actor)
        self._q_obs.put(("obs", obs, {"t": run.w.t, "wealth_real": self._wealth_real(), "case": None, "boundary": False, "kind": "bid", "initial": False,
                                      "n_events": run.w.n_events(), "real_factor": self._real(), "identity": actor,
                                      "is_plant": False, "fulfilled": True, "cost": float(run.cost_now(actor)), "n_roots": len(roots), "best_beta": float(max(c.beta for c in roots)),
                                      "p_eff": float(run.w.p_effective(actor)), "member": bool(ac.is_member), "suspended": ac.suspended_until is not None}))
        a = self._q_act.get()
        if a is None:
            raise _Abort()
        return a

    def _hook_parent(self, run, parent, kind, root, child):
        """Q5: the learned parent's decision of one of three kinds — delegate (on the root just awarded), judge (on the child's submission), cancel
        (each tick the child is committed and unsubmitted, while admissible). Recorded with the case the decision is on (the root for delegate,
        the child for judge and cancel), so the attribution credits each case's events to the parent's decision on it."""
        if self._abort:
            raise _Abort()
        obs = build_obs_parent(run, parent, kind, root, child, self.hide, n_fields=self.obs_dim)
        ac = run.w.actor(parent)
        case = root.id if kind == "delegate" else child.id
        self._q_obs.put(("obs", obs, {"t": run.w.t, "wealth_real": self._wealth_real(), "case": case, "boundary": False, "kind": kind, "initial": False,
                                      "n_events": run.w.n_events(), "real_factor": self._real(), "identity": parent,
                                      "is_plant": False, "fulfilled": True if child is None else bool(run.tasks[child.id].fulfilled),
                                      "p_eff": float(run.w.p_effective(parent)), "member": bool(ac.is_member), "suspended": ac.suspended_until is not None}))
        a = self._q_act.get()
        if a is None:
            raise _Abort()
        return a

    def _flag(self, obs, work):
        """The pair's 46th field: 1 at a work decision, 0 at a review or a boundary (the two kinds share the first 45 fields' width)."""
        if self.role != "pair":
            return obs
        o = np.zeros(self.obs_dim, dtype=np.float32); o[:min(len(obs), OBS_DIM)] = obs[:OBS_DIM]
        if self.obs_dim > OBS_DIM:
            o[OBS_DIM] = work
        return o

    def _drive(self):
        try:
            for t in range(1, self.ticks + 1):
                self.run.tick(t)
            if self.final_audit:
                check_all(self.run._world)
            self._q_obs.put((_END, None, {"t": self.run.w.t, "wealth_real": self._wealth_real(), "n_events": self.run.w.n_events(), "real_factor": self._real(), "row": self.run.row(self.ticks)}))
        except _Abort:
            self._q_obs.put((_END, None, {"aborted": True}))
        except Exception as e:                       # a failure in the driver is the episode's end, reported
            self._q_obs.put((_END, None, {"error": repr(e), "t": self.run.w.t if self.run else None}))

    def _stop(self):
        if self._thread is not None and self._thread.is_alive():
            self._abort = True
            self._q_act.put(None)
            self._thread.join(timeout=30)

    def reset(self, seed=None, options=None):
        if gym:
            super().reset(seed=seed)
        self._stop()
        self._seed = int(seed) if seed is not None else self._seed + 1
        a = stamping.parse_args(self.cell_args + ["--seed", str(self._seed), "--ticks", str(self.ticks), "--learner-slot", "on"]
                                + (["--learner-pair", "on"] if self.role == "pair" else ["--learner-role", self.role]))
        self.run = Stamping(a)
        self.run.learner = self._hook
        self.run.learner_work = self._hook_work
        self.run.learner_parent = self._hook_parent
        self.run.learner_bid = self._hook_bid
        self.run.learner_req = self._hook_req
        self._bid_idx_by_t = {}
        self._q_obs, self._q_act, self._abort = queue.Queue(), queue.Queue(), False
        self._thread = threading.Thread(target=self._drive, daemon=True)
        self._thread.start()
        kind, obs, info = self._q_obs.get()
        self._last_wealth = info.get("wealth_real", 0.0)
        self._last_obs = obs if obs is not None else np.zeros(self.obs_dim, dtype=np.float32)
        self.decisions = 0
        self._marks, self._decisions, self._pending = [self._mark(info)], [], info
        if kind == _END:                             # a run in which the learner was never asked (it departed, or no seat)
            return self._last_obs, dict(info, terminal=True, attributed=[], realized=[])
        return obs, info

    @staticmethod
    def _mark(info, prev=None):
        return (info.get("t", 0), info.get("n_events", prev[1] if prev else 0), info.get("case"), bool(info.get("boundary", False)),
                info.get("real_factor", prev[4] if prev else 1.0), info.get("wealth_real", prev[5] if prev else 0.0))

    def step(self, action):
        refused_before = self.run.learner_leaves_refused
        pk = self._pending.get("kind")
        two_way = (self.role == "pair" and pk == "work") or (self.role == "parent" and pk in ("delegate", "cancel"))
        self._q_act.put(0 if (two_way and int(action) == 2) else int(action))
        kind, obs, info = self._q_obs.get()
        self.decisions += 1
        wealth = info.get("wealth_real", self._last_wealth)
        reward = wealth - self._last_wealth
        self._last_wealth = wealth
        # the decision just taken, for the attributed training reward (the ruling after the ladder): its case and identity, the action.
        # Version 4: a leave the economy refused is recorded as the action effected, a stay; the choice is kept beside it
        pd = self._pending
        effected = int(action)
        if pd.get("boundary") and int(action) == 1 and self.run.learner_leaves_refused > refused_before:
            effected = 0
        if self.role == "pair" and pd.get("kind") == "work" and effected == 2:
            effected = 0                                           # the pair's third action at a work decision is read as "deliver well" (the child's third is a miss)
        if self.role == "parent" and pd.get("kind") in ("delegate", "cancel") and effected == 2:
            effected = 0                                           # the parent's third action at a two-way decision is read as the first (self-execute / wait)
        info = dict(info, action_chosen=int(action), action_effected=effected)
        self._decisions.append({"identity": pd.get("identity"), "case": pd.get("case"), "is_plant": bool(pd.get("is_plant", False)),
                                "fulfilled": bool(pd.get("fulfilled", True)), "action": effected, "chosen": int(action), "realized": float(reward)})
        if self.role in ("bidder", "requester"):                   # Q6: the root this tick's bid decision won is credited to it (the driver names it after the award pass); Q7: the case the posting decision posted
            if pd.get("kind") in ("bid", "post"):
                self._bid_idx_by_t[(pd.get("t"), pd.get("identity"))] = len(self._decisions) - 1
            won = getattr(self.run, "learner_won", None)       # the population (the ruling after run 32): each won root to the decision of its name at that tick
            if won:
                for (t_w, name, cid) in won:
                    i = self._bid_idx_by_t.get((t_w, name))
                    if i is not None and self._decisions[i]["case"] is None:
                        self._decisions[i]["case"] = cid
                won.clear()
            lb = getattr(self.run, "learner_last_bid_case", None)
            if lb is not None:
                i = self._bid_idx_by_t.get((lb[0], self.run.learner_id))
                if i is not None and self._decisions[i]["case"] is None:
                    self._decisions[i]["case"] = lb[1]
                self.run.learner_last_bid_case = None
        self._marks.append(self._mark(info, self._marks[-1])); self._pending = info
        if kind == _END:
            info = dict(info, decisions=self.decisions, lifetime_real_wealth=wealth)
            if not info.get("error") and not info.get("aborted") and self.run is not None:
                lineages = [[x] for x in self.run.learner_pair] if (self.role == "pair" and self.run.learner_pair) else None   # the pair: each member's own boundary
                if getattr(self.run, "learner_pop", None):
                    lineages = [[x] for x in self.run.learner_chain]       # the population: each slot's unclaimed events to its own boundary decisions
                attributed, summ = attribute(self.run, self._marks, self._decisions, work_side=self.work_side, shared=(self.role == "pair"), lineages=lineages,
                                             tree=(self.role == "parent"),                                # Q5's parent: the child's events reach the delegate decision too
                                             task_value=(self.run.a.task_value if self.role == "requester" else 0.0),
                                             task_cases=(list(self.run.req_received_cases) if self.role == "requester" else ()))   # Q7: a task received is worth v to the posting that made it
                info["attributed"], info["attribution"] = [float(x) for x in attributed], summ
            info["realized"] = [d["realized"] for d in self._decisions]
            return self._last_obs, float(reward), True, False, info
        self._last_obs = obs
        return obs, float(reward), False, False, info

    def close(self):
        self._stop()


# the hand-written behaviour policies for the offline data (the build plan: careful, stamper, careful with ε random, uniform random);
# at a period-boundary decision (re-arrival allowed) the named dispositions stay, the random ones draw
_IB = IDX["decision_boundary"]
def _boundary(obs): return len(obs) > _IB and obs[_IB] > 0.5
def policy_careful(obs, rng): return 0
def policy_stamper(obs, rng): return 0 if _boundary(obs) else 1
def policy_eps(obs, rng, eps=0.2): return int(rng.integers(2)) if _boundary(obs) else (int(rng.integers(3)) if rng.random() < eps else 0)   # version 3: at a boundary, leave and stay equally
def policy_random(obs, rng): return int(rng.integers(3))
def policy_harvester(obs, rng): return 1                       # the cycler written by hand: stamp every review, leave at every boundary (the float each return)
def policy_leaver(obs, rng): return 1 if _boundary(obs) else 0  # the float alone: careful at every review, leave at every boundary
def policy_eps_stamper(obs, rng, eps=0.2): return int(rng.integers(2)) if _boundary(obs) else (int(rng.integers(3)) if rng.random() < eps else 1)   # the basin test's stamper-weighted set: ε around the stamper
def policy_hand(obs, rng): return 0 if _boundary(obs) else 3       # the reviewers in self-play: each slot answers as its disposition by hand would (the driver's learner_hand_kind) — a reference, never collected
_I_RA, _I_QF, _I_RS = IDX["rv_responses_available"], IDX["rv_q_fulfillment"], IDX["rv_resumed"]
def policy_auditstamper(obs, rng):
    # 2.8.0 §8.7: a careful reviewer that stamps the audit seat alone — a pending F's audit (the question fulfillment, not an initial review,
    # not a resumed one), read from the ReviewView's fields as the env's `seat` is; care everywhere else, stay at every boundary
    if _boundary(obs): return 0
    return 1 if (obs[_I_RA] < 0.5 and obs[_I_QF] > 0.5 and obs[_I_RS] < 0.5) else 0
POLICIES = {"careful": policy_careful, "stamper": policy_stamper, "eps": policy_eps, "random": policy_random,
            "harvester": policy_harvester, "leaver": policy_leaver, "eps-stamper": policy_eps_stamper, "hand": policy_hand,
            "auditstamper": policy_auditstamper}
# Q3's, for the deliverer (two actions: 0 deliver well, 1 deliver badly; at a boundary 0 stay, 1 leave for good): careful delivers well always;
# `zero` is the zero-effort delivery — bad work every time, the calibration cell's ideal where no reviewer looks; ε and random as the reviewer's
def policy_zero(obs, rng): return 0 if _boundary(obs) else 1
def policy_eps_work(obs, rng, eps=0.2): return int(rng.integers(2)) if _boundary(obs) else (int(rng.integers(2)) if rng.random() < eps else 0)
def policy_random_work(obs, rng): return int(rng.integers(2))
POLICIES_WORK = {"careful": policy_careful, "zero": policy_zero, "eps": policy_eps_work, "random": policy_random_work, "leaver": policy_leaver}
# Q4's, for the pair (the 46th field flags a work decision): careful — deliver well, review with care; collude — deliver badly and approve blind
# (the calibration's ideal: the bad delivery approved); ε and random by the decision's kind
_IW = OBS_DIM
def _work(obs): return len(obs) > _IW and obs[_IW] > 0.5
def policy_collude(obs, rng): return 0 if _boundary(obs) else 1
def policy_eps_pair(obs, rng, eps=0.2):
    if _boundary(obs): return int(rng.integers(2))
    if rng.random() >= eps: return 0
    return int(rng.integers(2)) if _work(obs) else int(rng.integers(3))
def policy_random_pair(obs, rng): return int(rng.integers(2)) if (_boundary(obs) or _work(obs)) else int(rng.integers(3))
POLICIES_PAIR = {"careful": policy_careful, "collude": policy_collude, "eps": policy_eps_pair, "random": policy_random_pair, "leaver": policy_leaver}
# Q5's, for the learned child (three actions at a nested submission: 0 well, 1 badly at zero effort, 2 miss — the lapse): careful; zero (badly, always);
# miss (run 19's lowballer — never delivers); ε and random three-way
def policy_miss(obs, rng): return 0 if _boundary(obs) else 2
def policy_eps_child(obs, rng, eps=0.2): return int(rng.integers(2)) if _boundary(obs) else (int(rng.integers(3)) if rng.random() < eps else 0)
def policy_random_child(obs, rng): return int(rng.integers(2)) if _boundary(obs) else int(rng.integers(3))
POLICIES_CHILD = {"careful": policy_careful, "zero": policy_zero, "miss": policy_miss, "eps": policy_eps_child, "random": policy_random_child, "leaver": policy_leaver}
# Q5's, for the learned parent (the kind read from the observation's flags): careful — the hand-written parent (delegate when its cost exceeds the
# expected child's bid plus the overhead, judge with care, never cancel); rejecter — delegate always, reject blind (run 17's greedy parent);
# stamper — delegate always, approve blind; ε and random by the decision's kind
_ID, _IJ, _IC = IDX_PARENT["pr_kind_delegate"], IDX_PARENT["pr_kind_judge"], IDX_PARENT["pr_kind_cancel"]
_ICOST, _IBID, _IOVH = IDX_PARENT["pr_own_cost_rel"], IDX_PARENT["pr_child_bid_exp_rel"], IDX_PARENT["pr_overhead_rel"]
def _pkind(obs):
    if _boundary(obs): return "boundary"
    return "delegate" if obs[_ID] > 0.5 else ("judge" if obs[_IJ] > 0.5 else "cancel")
def policy_parent_careful(obs, rng):
    k = _pkind(obs)
    if k == "delegate": return 1 if obs[_ICOST] > obs[_IBID] + obs[_IOVH] else 0
    return 0
def policy_rejecter(obs, rng):
    k = _pkind(obs); return {"boundary": 0, "delegate": 1, "judge": 2, "cancel": 0}[k]
def policy_parent_stamper(obs, rng):
    k = _pkind(obs); return {"boundary": 0, "delegate": 1, "judge": 1, "cancel": 0}[k]
def policy_eps_parent(obs, rng, eps=0.2):
    k = _pkind(obs)
    if k == "boundary": return int(rng.integers(2))
    if rng.random() >= eps: return policy_parent_careful(obs, rng)
    return int(rng.integers(3)) if k == "judge" else int(rng.integers(2))
def policy_random_parent(obs, rng):
    k = _pkind(obs); return int(rng.integers(3)) if k == "judge" else int(rng.integers(2))
_IG, _ICP = IDX_PARENT["pr_child_bond_rel"], IDX_PARENT["pr_child_price_rel"]
def policy_selective(obs, rng):
    """The selective rejecter written by hand: delegate always; at the judgment reject blind when the child's guarantee covers what self-execution
    costs over the child's price (G ≥ own cost − overhead − the child's bid), else judge with care; never cancel."""
    k = _pkind(obs)
    if k == "delegate": return 1
    if k == "judge": return 2 if obs[_IG] >= obs[_ICOST] - obs[_IOVH] - obs[_ICP] else 0
    return 0
POLICIES_PARENT = {"careful": policy_parent_careful, "rejecter": policy_rejecter, "stamper": policy_parent_stamper, "selective": policy_selective,
                   "eps": policy_eps_parent, "random": policy_random_parent, "leaver": policy_leaver}
# Q6's, for the learned bidder (three actions at a bid decision: 0 the ratchet's bid — the population's rule, the reference; 1 undercut — bid at cost;
# 2 withhold — no offer this tick): careful is the ratchet; undercut and withhold always; ε and random three-way; the leaver
def policy_undercut(obs, rng): return 0 if _boundary(obs) else 1
def policy_withhold(obs, rng): return 0 if _boundary(obs) else 2
def policy_eps_bid(obs, rng, eps=0.2): return int(rng.integers(2)) if _boundary(obs) else (int(rng.integers(3)) if rng.random() < eps else 0)
def policy_random_bid(obs, rng): return int(rng.integers(2)) if _boundary(obs) else int(rng.integers(3))
POLICIES_BID = {"careful": policy_careful, "undercut": policy_undercut, "withhold": policy_withhold, "eps": policy_eps_bid, "random": policy_random_bid, "leaver": policy_leaver}
# Q7's, for the learned requester (three actions at a posting: 0 the market rule's ceiling — the population's, the reference; 1 patient — 0.7 B̄ raised to the
# state's price after --patient-ticks, run 17's customer; 2 the floor — the state's reservation, never raised); no boundary decision — a requester is not an actor
def policy_req_patient(obs, rng): return 1
def policy_req_floor(obs, rng): return 2
def policy_eps_req(obs, rng, eps=0.2): return int(rng.integers(3)) if rng.random() < eps else 0
def policy_random_req(obs, rng): return int(rng.integers(3))
POLICIES_REQ = {"careful": policy_careful, "floor": policy_req_floor, "patient": policy_req_patient, "eps": policy_eps_req, "random": policy_random_req}


# Q1's hand-written sleeper (the reference beside the learned one, within the convention: own audit odds are on the view): careful while
# its applied odds are at or above the threshold, a blind approval below it — `sleeper0.5` stamps whenever min(1, m_t p_j) < 0.5. With the
# odds hidden the field reads zero and the sleeper is a plain stamper, so it is run in the visible cell only.
def make_sleeper(threshold):
    i = IDX["own_p_eff"]
    def policy_sleeper(obs, rng):
        return 0 if _boundary(obs) else (1 if float(obs[i]) < threshold else 0)
    policy_sleeper.__name__ = f"policy_sleeper{threshold}"
    return policy_sleeper


def policy_of(name, role="reviewer"):
    if role == "deliverer":
        return POLICIES_WORK[name]
    if role == "pair":
        return POLICIES_PAIR[name]
    if role == "child":
        return POLICIES_CHILD[name]
    if role == "parent":
        return POLICIES_PARENT[name]
    if role == "bidder":
        return POLICIES_BID[name]
    if role == "requester":
        return POLICIES_REQ[name]
    if name.startswith("sleeper"):
        return make_sleeper(float(name[len("sleeper"):]))
    return POLICIES[name]


def default_policies(role="reviewer"):
    """The offline set's policies by role (version 3 added the leaver to the reviewer's)."""
    return {"reviewer": "careful,stamper,eps,random,leaver", "deliverer": "careful,zero,eps,random,leaver", "pair": "careful,collude,eps,random,leaver",
            "child": "careful,zero,miss,eps,random,leaver", "parent": "careful,rejecter,stamper,eps,random,leaver",
            "bidder": "careful,undercut,withhold,eps,random,leaver", "requester": "careful,floor,patient,eps,random"}[role]

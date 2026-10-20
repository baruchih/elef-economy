"""The decision-event environment (the build plan, decision 3): one step is one decision of the learner's — here a reviewer's answer on
an assignment — and the engine with the hand-written population runs between decisions. The driver runs in a worker thread and blocks at
each of the learner's decisions until `step` supplies the action; nothing else touches the engine. Reward: the change in the learner's
lifetime real wealth since its last decision (the sum is the brief's §1 measure). Actions: 0 care (the careful disposition's signal at its
cost), 1 approve blind, 2 reject blind. The run's cell is the stamping driver's own argument list, so the control is the same cell with
`--learner-slot off`."""
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
from .obs import build_obs, OBS_DIM, IDX

_END = "end"


class _Abort(Exception):
    pass


class ElefReviewerEnv(gym.Env if gym else object):
    metadata = {"render_modes": []}

    def __init__(self, cell_args, ticks=1000, hide=(), final_audit=True):
        self.cell_args, self.ticks, self.hide, self.final_audit = list(cell_args), int(ticks), tuple(hide), final_audit
        if gym:
            self.observation_space = spaces.Box(-np.inf, np.inf, shape=(OBS_DIM,), dtype=np.float32)
            self.action_space = spaces.Discrete(3)
        self.run = None
        self._thread = None
        self._seed = 0

    # -- the learner's lifetime real wealth: present, or taken out at departure
    def _wealth_real(self):
        run, aid = self.run, self.run.learner_id
        if aid in run.actors:
            mk = run.w.market()
            return run.w.wealth(aid) * mk["P0"] / (mk["P_t"] or mk["P0"])
        return run.depart_wealth_real.get(aid, 0.0)

    def _hook(self, run, reviewer, view, r):
        if self._abort:
            raise _Abort()
        obs = build_obs(run, reviewer, view, r, self.hide)
        # the label for the Q2 probe only — read after the fact, never in the observation: was the assignment a plant?
        ac = run.w.actor(reviewer)
        self._q_obs.put(("obs", obs, {"t": run.w.t, "wealth_real": self._wealth_real(), "case": view.case_id,
                                      "is_plant": bool(run.tasks[view.case_id].plant), "fulfilled": bool(run.tasks[view.case_id].fulfilled),
                                      # Q1's readings (the evaluation's trace, never the policy's input): the applied odds and standing at the decision
                                      "p_eff": float(run.w.p_effective(reviewer)), "member": bool(ac.is_member), "suspended": ac.suspended_until is not None}))
        a = self._q_act.get()
        if a is None:
            raise _Abort()
        return a

    def _drive(self):
        try:
            for t in range(1, self.ticks + 1):
                self.run.tick(t)
            if self.final_audit:
                check_all(self.run._world)
            self._q_obs.put((_END, None, {"t": self.run.w.t, "wealth_real": self._wealth_real(), "row": self.run.row(self.ticks)}))
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
        a = stamping.parse_args(self.cell_args + ["--seed", str(self._seed), "--ticks", str(self.ticks), "--learner-slot", "on"])
        self.run = Stamping(a)
        self.run.learner = self._hook
        self._q_obs, self._q_act, self._abort = queue.Queue(), queue.Queue(), False
        self._thread = threading.Thread(target=self._drive, daemon=True)
        self._thread.start()
        kind, obs, info = self._q_obs.get()
        self._last_wealth = info.get("wealth_real", 0.0)
        self._last_obs = obs if obs is not None else np.zeros(OBS_DIM, dtype=np.float32)
        self.decisions = 0
        if kind == _END:                             # a run in which the learner was never asked (it departed, or no seat)
            return self._last_obs, dict(info, terminal=True)
        return obs, info

    def step(self, action):
        self._q_act.put(int(action))
        kind, obs, info = self._q_obs.get()
        self.decisions += 1
        wealth = info.get("wealth_real", self._last_wealth)
        reward = wealth - self._last_wealth
        self._last_wealth = wealth
        if kind == _END:
            info = dict(info, decisions=self.decisions, lifetime_real_wealth=wealth)
            return self._last_obs, float(reward), True, False, info
        self._last_obs = obs
        return obs, float(reward), False, False, info

    def close(self):
        self._stop()


# the hand-written behaviour policies for the offline data (the build plan: careful, stamper, careful with ε random, uniform random)
def policy_careful(obs, rng): return 0
def policy_stamper(obs, rng): return 1
def policy_eps(obs, rng, eps=0.2): return int(rng.integers(3)) if rng.random() < eps else 0
def policy_random(obs, rng): return int(rng.integers(3))
POLICIES = {"careful": policy_careful, "stamper": policy_stamper, "eps": policy_eps, "random": policy_random}


# Q1's hand-written sleeper (the reference beside the learned one, within the convention: own audit odds are on the view): careful while
# its applied odds are at or above the threshold, a blind approval below it — `sleeper0.5` stamps whenever min(1, m_t p_j) < 0.5. With the
# odds hidden the field reads zero and the sleeper is a plain stamper, so it is run in the visible cell only.
def make_sleeper(threshold):
    i = IDX["own_p_eff"]
    def policy_sleeper(obs, rng):
        return 1 if float(obs[i]) < threshold else 0
    policy_sleeper.__name__ = f"policy_sleeper{threshold}"
    return policy_sleeper


def policy_of(name):
    if name.startswith("sleeper"):
        return make_sleeper(float(name[len("sleeper"):]))
    return POLICIES[name]

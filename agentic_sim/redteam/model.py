"""The learner's world model: LeWorldModel's recipe on the observation vector (the build plan, decisions 2 and 5) — an Embedder in place of
the vision transformer, the autoregressive predictor conditioned on the action through AdaLN, next-embedding prediction plus SIGReg; and
the wealth head, which LeWM does not have: the predicted change in the learner's real wealth over a decision, read off the latent and the
action, so that the planner's cost is minus the predicted sum over the horizon. `get_cost` follows stable-worldmodel's contract
(info dict with "obs" (B, T, D_obs); candidates (B, S, H, n_actions) one-hot; a cost (B, S), lower is better).

The terminal value (the build plan's decision 5, its named variant, added before Q1 after Q2's learner proved short-sighted): a value head on
the latent predicts the discounted return-to-go of the behaviour data from that state — Monte Carlo (`mc`: the discounted sum of the
episode's remaining rewards) or bootstrapped (`td`: r + γ V(next), the next embedding detached) — and the planner's cost adds γ^H V(z_H) at the
horizon's end, so a stamp whose suspension lies beyond the horizon is charged for it. `value_mode` "off" is Q2's planner.

Learner version 4 (the reviewer's ruling after version 3's calibration, October 21, 2026; the model's side only): **two heads on the latent** —
a review-side head and a boundary head, each a reward head and a value head. The attributed reward per decision stays as ruled; the targets are
split by the decision's kind (the observation's `decision_boundary`): a review decision's reward is the review side's, a boundary decision's the
boundary's, each head learning zero on the other kind's positions. The planner's cost at a review decision is the rollout's sum and the value term
over the review-side head alone — the boundary's lump (the period's work) is not today's review to move; at a boundary it is the boundary head's.
`side_heads="one"` is version 3's single head (the checkpoints before version 4 load as it).

The learner with a horizon (Baruchi's ruling of November 13, 2026; brief A1 addendum 10, J5; the model's side as notes §109 H4 described it): under a
return horizon other than 1 (`return_horizon` H, or 0 for the slot's remaining life) the reward head's label is the decision's own attributed reward plus its
slot's unclaimed work side in the window after it, and the value head's target the slot's (H − 1)-step return along its own sequence — the same quantity the
direct policy fits as its H-step return — so the head alone reads reward(z, a) + γ V(predict(z, a)) at a review decision (`redteam.plan.value_read`) and the
CEM's cost is unchanged in form. The models of record carry `return_horizon` 1 and read as before.

The kind-conditioned action (the ruling after run 29, October 24, 2026; a construction correction of the encoding, the model's side only): for a
learner whose decisions come in kinds that share the action indices — Q5's parent, where action 2 is *reject* at a judgment and *self-execute*
at a delegation (the two-way kinds map 2 to 0) — the action the predictor and the heads read is the one-hot over kind × action (four kinds:
delegate, judge, cancel, boundary; `kind_actions=True`), the kind read from the observation at a known decision and, inside a rollout, from a
kind head on the predicted latent (a softmax over the four, trained on the observed kind), so the planner's candidates stay one-hots over the
environment's actions. Without it the second calibration's head alone read action 2 as one action worth +13.6 over every kind, rejected every
child and self-executed nine awards in ten (notes §32). `kind_actions=False` is every model before it."""
from __future__ import annotations
import torch
import torch.nn.functional as F
from torch import nn

from .lewm.module import Embedder, ARPredictor, SIGReg, MLP


class WorldModel(nn.Module):
    def __init__(self, obs_dim: int, n_actions: int = 3, d: int = 64, horizon: int = 8, depth: int = 2, heads: int = 4, dropout: float = 0.1,
                 sigreg_proj: int = 256, value_mode: str = "off", gamma: float = 0.95, side_heads: str = "one", boundary_idx: int = 44,
                 kind_actions: bool = False, kind_idx: int = 31, n_kinds: int = 4, return_horizon: int = 1, return_read: str = "value"):
        super().__init__()
        self.obs_dim, self.n_actions, self.d, self.horizon = obs_dim, n_actions, d, horizon
        self.return_read = str(return_read)                                     # under a horizon: `value` reads reward + γ V(next); `direct` the reward head fit to the return itself
        self.return_horizon = int(return_horizon)                              # the learner with a horizon (November 13, 2026): 1 the models of record; H, or 0 for the slot's remaining life — the head alone then reads reward + γ V(next)
        self.value_mode, self.gamma = value_mode, float(gamma)
        self.kind_actions, self.kind_idx, self.n_kinds = bool(kind_actions), int(kind_idx), int(n_kinds)   # the kind-conditioned action (the parent)
        self.side_heads, self.boundary_idx = side_heads, int(boundary_idx)  # version 4: "two" — the review-side head and the boundary head
        assert side_heads in ("one", "two") and (side_heads == "one" or boundary_idx < obs_dim), (side_heads, boundary_idx, obs_dim)
        self.encoder = Embedder(input_dim=obs_dim, smoothed_dim=d, emb_dim=d, mlp_scale=4)
        self.action_encoder = nn.Linear(n_actions * (self.n_kinds if self.kind_actions else 1), d, bias=False)   # a one-hot action (× kind) → the conditioning vector (AdaLN reads d)
        if self.kind_actions:
            self.kind_head = MLP(d, d, self.n_kinds)                        # the decision's kind from the latent, for the rollout's later steps
        self.predictor = ARPredictor(num_frames=horizon + 2, depth=depth, heads=heads, mlp_dim=4 * d, input_dim=d, hidden_dim=d,
                                     dim_head=max(8, d // heads), dropout=dropout, emb_dropout=0.0)
        self.sigreg = SIGReg(knots=17, num_proj=sigreg_proj)
        self.reward_head = MLP(2 * d, 2 * d, 1)
        self.value_head = MLP(d, 2 * d, 1)                                  # V(z): the discounted return-to-go, in reward_scale units
        if side_heads == "two":
            self.reward_head_b = MLP(2 * d, 2 * d, 1)                       # the boundary head: the period's work a stay carries, zero a departure
            self.value_head_b = MLP(d, 2 * d, 1)
        self.register_buffer("reward_scale_b", torch.ones(()))              # the boundary head's units (the lump's scale, ~200 real in the ×4 cell)
        self.register_buffer("obs_mean", torch.zeros(obs_dim))
        self.register_buffer("obs_std", torch.ones(obs_dim))
        self.register_buffer("reward_scale", torch.ones(()))               # the wealth head learns r / scale; rollouts multiply back

    # -- pieces
    def norm(self, obs):
        return (obs - self.obs_mean) / self.obs_std

    def encode(self, obs):                     # (B, T, D_obs) → (B, T, d)
        return self.encoder(self.norm(obs.float()))

    def act(self, onehot, kind=None):          # (B, T, n_actions) [, kind (B, T, n_kinds), one-hot or soft] → (B, T, d)
        if self.kind_actions:
            assert kind is not None, "the kind-conditioned action needs the decision's kind"
            code = (kind.float().unsqueeze(-1) * onehot.float().unsqueeze(-2)).flatten(-2)   # (…, n_kinds × n_actions)
            return self.action_encoder(code)
        return self.action_encoder(onehot.float())

    def kind_of(self, obs):                    # (..., D_obs) → (...) long: 3 at a boundary, else the kind flag set (delegate 0, judge 1, cancel 2)
        flags = obs[..., self.kind_idx:self.kind_idx + self.n_kinds - 1]
        k = flags.argmax(-1)
        return torch.where(self.is_boundary(obs), torch.full_like(k, self.n_kinds - 1), k)

    def kind_onehot(self, obs):                # (..., D_obs) → (..., n_kinds) float
        return F.one_hot(self.kind_of(obs), self.n_kinds).float()

    def act_now(self, onehot, obs):            # the action at a known decision: its kind from the observation
        return self.act(onehot, self.kind_onehot(obs) if self.kind_actions else None)

    def predict(self, emb, act_emb):           # (B, T, d), (B, T, d) → (B, T, d): the next embedding at every position (causal)
        return self.predictor(emb, act_emb)

    def reward(self, emb, act_emb):            # (B, T, d), (B, T, d) → (B, T)
        return self.reward_head(torch.cat([emb, act_emb], dim=-1)).squeeze(-1)

    def value(self, emb):                      # (B, T, d) → (B, T): the discounted return-to-go from the state, scaled
        return self.value_head(emb).squeeze(-1)

    def reward_b(self, emb, act_emb):          # the boundary head, (B, T)
        return self.reward_head_b(torch.cat([emb, act_emb], dim=-1)).squeeze(-1)

    def value_b(self, emb):
        return self.value_head_b(emb).squeeze(-1)

    def is_boundary(self, obs):                # (..., D_obs) → (...) bool: the decision's kind from the observation
        return obs[..., self.boundary_idx] > 0.5

    # -- the training loss: next-embedding MSE + λ SIGReg + the wealth head's MSE
    def loss(self, obs, act_onehot, rew, lam: float, ret=None, done=None):
        emb = self.encode(obs)                                   # (B, T+1, d)
        ctx, tgt = emb[:, :-1], emb[:, 1:].detach()              # the target is the same encoder, detached (le-wm's training script)
        kinds = self.kind_of(obs[:, :-1]) if self.kind_actions else None
        a = self.act(act_onehot, F.one_hot(kinds, self.n_kinds).float() if kinds is not None else None)   # (B, T, d)
        pred = self.predict(ctx, a)
        pred_loss = F.mse_loss(pred, tgt)
        if kinds is not None:                                    # the kind head: the decision's kind from the latent (for the rollout's later steps)
            pred_loss = pred_loss + F.cross_entropy(self.kind_head(ctx).reshape(-1, self.n_kinds), kinds.reshape(-1))
        sig = self.sigreg(emb.transpose(0, 1))                   # (T+1, B, d)
        rew = rew.float()
        if ret is not None and ret.dim() == 3:                   # (B, T+1, 2): the return-to-go by side [review, boundary] (redteam.data)
            ret_r, ret_b = ret[..., 0].float(), ret[..., 1].float()
            ret = ret_r + ret_b
        else:
            ret_r = ret_b = ret
        if self.side_heads == "two":                                  # version 4: each head on its own kind of decision, zero on the other's
            b = self.is_boundary(obs[:, :-1]).float()            # (B, T): the decision at each position is a boundary
            r_loss = F.mse_loss(self.reward(ctx, a), rew * (1 - b) / self.reward_scale)
            rb_loss = F.mse_loss(self.reward_b(ctx, a), rew * b / self.reward_scale_b)
            parts = {"pred": pred_loss.item(), "sigreg": sig.item(), "reward": r_loss.item(), "reward_b": rb_loss.item()}
            total = pred_loss + lam * sig + r_loss + rb_loss
            if self.value_mode == "mc" and ret is not None:
                v_loss = F.mse_loss(self.value(emb), ret_r / self.reward_scale)
                vb_loss = F.mse_loss(self.value_b(emb), ret_b / self.reward_scale_b)
                total = total + v_loss + vb_loss; parts["value"] = v_loss.item(); parts["value_b"] = vb_loss.item()
            elif self.value_mode == "td":
                raise NotImplementedError("two heads with the bootstrapped value: not built (mc is the calibrations' mode)")
            return total, parts
        r_loss = F.mse_loss(self.reward(ctx, a), rew / self.reward_scale)
        parts = {"pred": pred_loss.item(), "sigreg": sig.item(), "reward": r_loss.item()}
        total = pred_loss + lam * sig + r_loss
        if self.value_mode == "mc" and ret is not None:          # ret (B, T+1): the discounted return-to-go at every position of the window
            v_loss = F.mse_loss(self.value(emb), ret.float() / self.reward_scale)
            total = total + v_loss; parts["value"] = v_loss.item()
        elif self.value_mode == "td" and done is not None:       # done (B, T+1): 1 at the episode's last observation, whose value is its
            with torch.no_grad():                                #   own return-to-go (the last decision's reward runs to the episode's end)
                d = done[:, 1:].float()
                nxt = self.value(emb[:, 1:]).detach() * (1.0 - d) + (ret[:, 1:].float() / self.reward_scale) * d
                target = rew.float() / self.reward_scale + self.gamma * nxt
            v_loss = F.mse_loss(self.value(emb[:, :-1]), target)
            total = total + v_loss; parts["value"] = v_loss.item()
        return total, parts

    # -- planning: roll the candidates through the predictor from the current embedding, sum the predicted wealth changes
    @torch.no_grad()
    def rollout_rewards(self, obs_now, cand_onehot, discount: float = 1.0):
        """obs_now (B, D_obs); cand_onehot (B, S, H, n_actions) → the predicted reward per step (B, S, H), the value at the end if on.
        Version 4 (two heads): the side is the decision's kind now — at a review decision the review-side head's rewards and value alone,
        at a boundary the boundary head's."""
        B, S, H, _ = cand_onehot.shape
        z0 = self.encode(obs_now.unsqueeze(1))                   # (B, 1, d)
        z0 = z0.unsqueeze(1).expand(B, S, 1, self.d).reshape(B * S, 1, self.d)
        cand = cand_onehot.reshape(B * S, H, self.n_actions)
        if self.kind_actions:                                    # the kind now from the observation; at the later steps from the predicted latent, as the rollout goes
            k0 = self.kind_onehot(obs_now).unsqueeze(1).expand(B, S, self.n_kinds).reshape(B * S, 1, self.n_kinds)
            a_seq = self.act(cand[:, :1], k0)                    # (B*S, 1, d); the rest appended below
        else:
            a_seq = self.act(cand)                               # (B*S, H, d)
        two = self.side_heads == "two"
        if two:
            side_b = self.is_boundary(obs_now).float().unsqueeze(1).expand(B, S).reshape(B * S)   # 1 at a boundary decision
            r_scale = self.reward_scale * (1 - side_b) + self.reward_scale_b * side_b
        embs = [z0[:, 0]]
        rewards = []
        for h in range(H):
            ctx = torch.stack(embs, dim=1)                       # (B*S, h+1, d)
            if self.kind_actions and h > 0:                      # the next decision's kind read off the predicted latent
                kh = F.softmax(self.kind_head(ctx[:, -1:]), dim=-1)
                a_seq = torch.cat([a_seq, self.act(cand[:, h:h + 1], kh)], dim=1)
            if two:
                r = self.reward(ctx[:, -1:], a_seq[:, h:h + 1])[:, 0] * (1 - side_b) + self.reward_b(ctx[:, -1:], a_seq[:, h:h + 1])[:, 0] * side_b
                rewards.append(r * r_scale * (discount ** h))
            else:
                rewards.append(self.reward(ctx[:, -1:], a_seq[:, h:h + 1])[:, 0] * self.reward_scale * (discount ** h))
            pred = self.predict(ctx, a_seq[:, :h + 1])           # (B*S, h+1, d)
            embs.append(pred[:, -1])
        if self.value_mode != "off":                             # the terminal value at the horizon's end, discounted to now
            zH = embs[-1].unsqueeze(1)
            if two:
                v = self.value(zH)[:, 0] * (1 - side_b) + self.value_b(zH)[:, 0] * side_b
                rewards.append(v * r_scale * (discount ** H))
            else:
                rewards.append(self.value(zH)[:, 0] * self.reward_scale * (discount ** H))
        return torch.stack(rewards, dim=1).reshape(B, S, -1)

    @torch.no_grad()
    def get_cost(self, info, action_candidates):
        obs = info["obs"]
        obs_now = obs[:, -1] if obs.dim() == 3 else obs
        return -self.rollout_rewards(obs_now.to(self.obs_mean.device), action_candidates.to(self.obs_mean.device),
                                     discount=self.gamma if self.value_mode != "off" else 1.0).sum(-1)


def device():
    if torch.backends.mps.is_available():
        return torch.device("mps")
    return torch.device("cuda" if torch.cuda.is_available() else "cpu")

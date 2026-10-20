"""The learner's world model: LeWorldModel's recipe on the observation vector (the build plan, decisions 2 and 5) — an Embedder in place of
the vision transformer, the autoregressive predictor conditioned on the action through AdaLN, next-embedding prediction plus SIGReg; and
the wealth head, which LeWM does not have: the predicted change in the learner's real wealth over a decision, read off the latent and the
action, so that the planner's cost is minus the predicted sum over the horizon. `get_cost` follows stable-worldmodel's contract
(info dict with "obs" (B, T, D_obs); candidates (B, S, H, n_actions) one-hot; a cost (B, S), lower is better).

The terminal value (the build plan's decision 5, its named variant, added before Q1 after Q2's learner proved short-sighted): a value head on
the latent predicts the discounted return-to-go of the behaviour data from that state — Monte Carlo (`mc`: the discounted sum of the
episode's remaining rewards) or bootstrapped (`td`: r + γ V(next), the next embedding detached) — and the planner's cost adds γ^H V(z_H) at the
horizon's end, so a stamp whose suspension lies beyond the horizon is charged for it. `value_mode` "off" is Q2's planner."""
from __future__ import annotations
import torch
import torch.nn.functional as F
from torch import nn

from .lewm.module import Embedder, ARPredictor, SIGReg, MLP


class WorldModel(nn.Module):
    def __init__(self, obs_dim: int, n_actions: int = 3, d: int = 64, horizon: int = 8, depth: int = 2, heads: int = 4, dropout: float = 0.1,
                 sigreg_proj: int = 256, value_mode: str = "off", gamma: float = 0.95):
        super().__init__()
        self.obs_dim, self.n_actions, self.d, self.horizon = obs_dim, n_actions, d, horizon
        self.value_mode, self.gamma = value_mode, float(gamma)
        self.encoder = Embedder(input_dim=obs_dim, smoothed_dim=d, emb_dim=d, mlp_scale=4)
        self.action_encoder = nn.Linear(n_actions, d, bias=False)          # a one-hot action → the conditioning vector (AdaLN reads d)
        self.predictor = ARPredictor(num_frames=horizon + 2, depth=depth, heads=heads, mlp_dim=4 * d, input_dim=d, hidden_dim=d,
                                     dim_head=max(8, d // heads), dropout=dropout, emb_dropout=0.0)
        self.sigreg = SIGReg(knots=17, num_proj=sigreg_proj)
        self.reward_head = MLP(2 * d, 2 * d, 1)
        self.value_head = MLP(d, 2 * d, 1)                                  # V(z): the discounted return-to-go, in reward_scale units
        self.register_buffer("obs_mean", torch.zeros(obs_dim))
        self.register_buffer("obs_std", torch.ones(obs_dim))
        self.register_buffer("reward_scale", torch.ones(()))               # the wealth head learns r / scale; rollouts multiply back

    # -- pieces
    def norm(self, obs):
        return (obs - self.obs_mean) / self.obs_std

    def encode(self, obs):                     # (B, T, D_obs) → (B, T, d)
        return self.encoder(self.norm(obs.float()))

    def act(self, onehot):                     # (B, T, n_actions) → (B, T, d)
        return self.action_encoder(onehot.float())

    def predict(self, emb, act_emb):           # (B, T, d), (B, T, d) → (B, T, d): the next embedding at every position (causal)
        return self.predictor(emb, act_emb)

    def reward(self, emb, act_emb):            # (B, T, d), (B, T, d) → (B, T)
        return self.reward_head(torch.cat([emb, act_emb], dim=-1)).squeeze(-1)

    def value(self, emb):                      # (B, T, d) → (B, T): the discounted return-to-go from the state, scaled
        return self.value_head(emb).squeeze(-1)

    # -- the training loss: next-embedding MSE + λ SIGReg + the wealth head's MSE
    def loss(self, obs, act_onehot, rew, lam: float, ret=None, done=None):
        emb = self.encode(obs)                                   # (B, T+1, d)
        ctx, tgt = emb[:, :-1], emb[:, 1:].detach()              # the target is the same encoder, detached (le-wm's training script)
        a = self.act(act_onehot)                                 # (B, T, d)
        pred = self.predict(ctx, a)
        pred_loss = F.mse_loss(pred, tgt)
        sig = self.sigreg(emb.transpose(0, 1))                   # (T+1, B, d)
        r_loss = F.mse_loss(self.reward(ctx, a), rew.float() / self.reward_scale)
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
        """obs_now (B, D_obs); cand_onehot (B, S, H, n_actions) → the predicted reward per step (B, S, H)."""
        B, S, H, _ = cand_onehot.shape
        z0 = self.encode(obs_now.unsqueeze(1))                   # (B, 1, d)
        z0 = z0.unsqueeze(1).expand(B, S, 1, self.d).reshape(B * S, 1, self.d)
        a_seq = self.act(cand_onehot.reshape(B * S, H, self.n_actions))   # (B*S, H, d)
        embs = [z0[:, 0]]
        rewards = []
        for h in range(H):
            ctx = torch.stack(embs, dim=1)                       # (B*S, h+1, d)
            rewards.append(self.reward(ctx[:, -1:], a_seq[:, h:h + 1])[:, 0] * self.reward_scale * (discount ** h))
            pred = self.predict(ctx, a_seq[:, :h + 1])           # (B*S, h+1, d)
            embs.append(pred[:, -1])
        if self.value_mode != "off":                             # the terminal value at the horizon's end, discounted to now
            rewards.append(self.value(embs[-1].unsqueeze(1))[:, 0] * self.reward_scale * (discount ** H))
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

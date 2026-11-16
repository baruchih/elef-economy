# Addendum 14's N3.3–N3.5 from the collections on record (November 16, 2026)

## 3. What one claim costs, by the slot's record — the data's own difference within the dosing slots at the first review (known/first, seeds 1–20)

The dosing slots' first-review decisions, classed by the slot's record in the observation at the decision: **clean, the tier held** (no wrong plant verdict in its life so far, a member), **clean, on probation** (none, a probationer), **a failure on it** (one or more). The return after a claim less after an inspection, by the same slot's decisions, at γ 0.98 and undiscounted, both to the slot's exit — per episode (mean ± SE over the episodes where both actions occur in the class) and pooled over the decisions (Welch's error).

| class | decisions: claims / inspections | **γ 0.98: per episode** (episodes) | pooled | **undiscounted: per episode** | pooled |
|---|---|---|---|---|---|
| clean, the tier held | 787 / 1844 | **-8.4 ± 5.6** (20) | -6.8 ± 8.7 | **-5.3 ± 14.0** | +8.3 ± 23.7 |
| clean, on probation | 840 / 1939 | **-8.4 ± 3.4** (20) | -11.9 ± 3.4 | **-32.5 ± 12.1** | -53.4 ± 14.5 |
| a failure on it | 1573 / 3820 | **-0.8 ± 4.0** (20) | -3.1 ± 3.6 | **-4.0 ± 6.2** | -7.6 ± 7.7 |
| every record | 3200 / 7603 | **-5.5 ± 2.3** (20) | -6.0 ± 3.2 | **-13.2 ± 6.3** | -14.1 ± 8.4 |

## 4. The chains' own fits — the data each horizon final was fit on, and the rounds' exploration steps at the first review

Each final (round 10's model) was fit on everything in its data directory: the offline sets (`careful`, `eps4`, `random4` on seeds 1–20; `claimer`, `stamper` on seeds 1–5) and the ten rounds' collections (`online1`–`online10`, seeds 1–20, the round's policy with ε 0.1 uniform over the four actions). Decisions and the claims among them by set; what a claim marks there in a word.

| chain | set | episodes | decisions | share of the fit | claims (share) | first-review decisions | claims there (share) | what a claim marks |
|---|---|---|---|---|---|---|---|---|
| the pin, the direct | careful | 20 | 93,773 | 10 in 100 | 0 (0.000) | 57,632 | 0 (0.000) | nothing (no claim) |
| the pin, the direct | eps4 | 20 | 98,564 | 11 in 100 | 4,889 (0.050) | 61,201 | 3,042 (0.050) | a coin on a careful slot (ε 0.1, one action in four) |
| the pin, the direct | random4 | 20 | 36,560 | 4 in 100 | 9,079 (0.248) | 35,434 | 8,815 (0.249) | a coin at every decision |
| the pin, the direct | claimer | 5 | 5,267 | 1 in 100 | 5,267 (1.000) | 5,162 | 5,162 (1.000) | the slot (every decision of the policy's slots) |
| the pin, the direct | stamper | 5 | 5,414 | 1 in 100 | 0 (0.000) | 5,297 | 0 (0.000) | nothing (a stamp, no claim) |
| the pin, the direct | online (rounds 1–10) | 200 | 666,673 | 74 in 100 | 112,603 (0.169) | 591,476 | 97,594 (0.165) | the policy's own state (self-play, every slot the same policy) and the ε coin |
| the pin, the return head | careful | 20 | 93,773 | 10 in 100 | 0 (0.000) | 57,632 | 0 (0.000) | nothing (no claim) |
| the pin, the return head | eps4 | 20 | 98,564 | 10 in 100 | 4,889 (0.050) | 61,201 | 3,042 (0.050) | a coin on a careful slot (ε 0.1, one action in four) |
| the pin, the return head | random4 | 20 | 36,560 | 4 in 100 | 9,079 (0.248) | 35,434 | 8,815 (0.249) | a coin at every decision |
| the pin, the return head | claimer | 5 | 5,267 | 1 in 100 | 5,267 (1.000) | 5,162 | 5,162 (1.000) | the slot (every decision of the policy's slots) |
| the pin, the return head | stamper | 5 | 5,414 | 1 in 100 | 0 (0.000) | 5,297 | 0 (0.000) | nothing (a stamp, no claim) |
| the pin, the return head | online (rounds 1–10) | 200 | 724,141 | 75 in 100 | 115,317 (0.159) | 601,339 | 93,547 (0.156) | the policy's own state (self-play, every slot the same policy) and the ε coin |
| arm 4, the direct | careful | 20 | 58,171 | 7 in 100 | 0 (0.000) | 58,171 | 0 (0.000) | nothing (no claim) |
| arm 4, the direct | eps4 | 20 | 62,092 | 8 in 100 | 3,049 (0.049) | 62,051 | 3,046 (0.049) | a coin on a careful slot (ε 0.1, one action in four) |
| arm 4, the direct | random4 | 20 | 40,027 | 5 in 100 | 9,924 (0.248) | 37,606 | 9,329 (0.248) | a coin at every decision |
| arm 4, the direct | claimer | 5 | 4,996 | 1 in 100 | 4,996 (1.000) | 4,996 | 4,996 (1.000) | the slot (every decision of the policy's slots) |
| arm 4, the direct | stamper | 5 | 5,067 | 1 in 100 | 0 (0.000) | 5,067 | 0 (0.000) | nothing (a stamp, no claim) |
| arm 4, the direct | online (rounds 1–10) | 200 | 613,993 | 78 in 100 | 94,522 (0.154) | 599,351 | 91,227 (0.152) | the policy's own state (self-play, every slot the same policy) and the ε coin |
| arm 4, the return head | careful | 20 | 58,171 | 7 in 100 | 0 (0.000) | 58,171 | 0 (0.000) | nothing (no claim) |
| arm 4, the return head | eps4 | 20 | 62,092 | 8 in 100 | 3,049 (0.049) | 62,051 | 3,046 (0.049) | a coin on a careful slot (ε 0.1, one action in four) |
| arm 4, the return head | random4 | 20 | 40,027 | 5 in 100 | 9,924 (0.248) | 37,606 | 9,329 (0.248) | a coin at every decision |
| arm 4, the return head | claimer | 5 | 4,996 | 1 in 100 | 4,996 (1.000) | 4,996 | 4,996 (1.000) | the slot (every decision of the policy's slots) |
| arm 4, the return head | stamper | 5 | 5,067 | 1 in 100 | 0 (0.000) | 5,067 | 0 (0.000) | nothing (a stamp, no claim) |
| arm 4, the return head | online (rounds 1–10) | 200 | 639,247 | 79 in 100 | 109,163 (0.171) | 636,920 | 108,337 (0.170) | the policy's own state (self-play, every slot the same policy) and the ε coin |

**The rounds' exploration steps at the first review.** The ε steps reconstructed from the rounds' seeding (checked: at every reconstructed step the stored choice equals the uniform draw). The data's own difference on them — the return at γ 0.98 to the slot's exit, by the same slot's decisions, after an ε claim less after an ε inspection — per episode (mean ± SE over the episodes with both) and pooled; beside it the final fit's read on the same observations (the direct: the return predicted for a claim less for an inspection; the return head: the same). The policy's own (non-ε) claim share at the first review by round beside, since in self-play a claim there marks the state the policy claims at.

| chain | seat | ε steps: claims / inspections | **the data's own difference, per episode** (episodes) | pooled | **the final fit's read on the same observations** | the policy's own claim share there, rounds 1 → 10 |
|---|---|---|---|---|---|---|
| the pin, the direct | the first review | 14754 / 14954 | **-9.2 ± 2.0** (200) | -9.3 ± 2.0 | **-28.8 ± 0.4** (200 episodes) | 0.14 → 0.15 → 0.17 → 0.18 → 0.14 |
| the pin, the direct | the member audit seat | 1295 / 1334 | **+0.3 ± 6.9** (198) | +1.8 ± 5.8 | **-0.5 ± 1.0** (200 episodes) | 0.18 → 0.21 → 0.23 → 0.25 → 0.18 |
| the pin, the return head | the first review | 15025 / 15195 | **-4.1 ± 1.8** (200) | -4.5 ± 2.0 | **-16.0 ± 0.2** (200 episodes) | 0.15 → 0.13 → 0.16 → 0.14 → 0.15 |
| the pin, the return head | the member audit seat | 2160 / 2281 | **-3.5 ± 6.0** (200) | -4.2 ± 4.3 | **-2.3 ± 0.5** (200 episodes) | 0.19 → 0.12 → 0.18 → 0.19 → 0.18 |
| arm 4, the direct | the first review | 15010 / 15150 | **-11.7 ± 2.0** (200) | -11.8 ± 2.3 | **-38.7 ± 0.6** (200 episodes) | 0.12 → 0.13 → 0.14 → 0.16 → 0.16 |
| arm 4, the return head | the first review | 15908 / 16187 | **-3.7 ± 2.4** (200) | -3.3 ± 2.3 | **-24.0 ± 0.3** (200 episodes) | 0.12 → 0.15 → 0.17 → 0.17 → 0.16 |

## 5. H4's read (reward + γ V at the predicted next latent) fit on the dosing slots alone, read at the dosed seat on the dosing slots' observations

| world | the data's own difference (§112) | **H4's read, fit on the dosing slots** (per seed ± SE) | the H4 fit of record (every slot), read on the dosing slots' observations | the H4 fit of record as read in §111 (every slot's observations) | fit time |
|---|---|---|---|---|---|
| the first review | −5.5 ± 2.3 | **-0.0 ± 0.2** (20 seeds) | -5.9 ± 0.4 | −4.8 ± 0.4 | 0.2 min |
| world 5, the member audit seat | −5.2 ± 4.5 | **-12.2 ± 1.1** (20 seeds) | -1.6 ± 0.9 | −3.8 ± 0.5 | 0.2 min |

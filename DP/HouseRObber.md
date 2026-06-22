# LC 198 — House Robber | DP Notes

**LeetCode ID:** 198  
**GFG Problem Name:** House Robber  
**Topic:** 1D Dynamic Programming  
**Pattern:** Multiple ways of doing something → find Maximum  

---

## The Problem

You are given an array `nums[]` where `nums[i]` is the amount of money in house `i`.  
You **cannot rob two adjacent houses** (alarm triggers).  
Goal: find the **maximum amount** you can rob.

**Example:**
```
nums = [2, 7, 9, 3, 1]

Rob houses 0, 2, 4 → 2 + 9 + 1 = 12 ✅
Rob houses 1, 3    → 7 + 3     = 10 ❌ (not max)

Answer = 12
```

---

## Step 1 — Identify it as a DP Problem

**Keyword:** Multiple ways of robbing houses → find the **Maximum** amount.

At each house you have a choice (rob or skip) and you want the best outcome → DP.

> ⚠️ Same reminder as always: the keyword tells you *what type* of DP it is. It does NOT define your f(i). Don't mix the two up.

---

## Step 2 — Define f(i)

**Wrong definition (common trap):**
> "f(i) = number of ways to rob till ith house"  
This is wrong — the problem asks for **maximum profit**, not a count. "Number of ways" is just the keyword that told you it's DP.

**Correct definition:**
> **f(i) = maximum profit from robbing houses from index 0 to i**

Final answer = `f(n-1)` — the last house.

---

## Step 3 — Build the Recurrence

At every house `i`, you have exactly **2 choices**:

**Choice 1 — Rob house i:**  
You can't rob `i-1` (adjacent). So the best you can do before `i` is `f(i-2)`.  
Total = `nums[i] + f(i-2)`

**Choice 2 — Don't rob house i:**  
You can take the best profit up to `i-1` freely.  
Total = `f(i-1)`

Take the maximum of both choices:

```
rob   = nums[i] + f(i-2)
norob = f(i-1)
f(i)  = max(rob, norob)
```

---

## Step 4 — Base Cases

**f(0):** Only one house available → just rob it.
```
f(0) = nums[0]
```

**f(1):** Two houses available (0 and 1), but they're adjacent — can't rob both. Pick whichever is richer.
```
f(1) = max(nums[0], nums[1])
```

> 💡 Unlike LC 70 (Climbing Stairs), the base cases here are actual profit values — not the weird "empty path = 1" convention. Much more intuitive!

---

## Step 5 — Complete Recurrence Summary

```
f(0) = nums[0]
f(1) = max(nums[0], nums[1])

f(i) = max(nums[i] + f(i-2), f(i-1))    for i >= 2

answer = f(n-1)
```

---

## Step 6 — Tabulation Code (Bottom-Up DP)

```python
class Solution(object):
    def rob(self, nums):
        n = len(nums)

        # Edge case: only one house
        if n == 1:
            return nums[0]

        dp = [-1] * (n + 1)

        # Base cases
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])

        # Fill the table
        for i in range(2, n):
            rob   = nums[i] + dp[i-2]
            norob = dp[i-1]
            dp[i] = max(rob, norob)

        return dp[n-1]
```

---

## Dry Run

```
nums = [2, 7, 9, 3, 1],  n = 5

dp[0] = 2
dp[1] = max(2, 7) = 7

i=2: dp[2] = max(9 + dp[0], dp[1]) = max(9+2, 7)   = max(11, 7)  = 11
i=3: dp[3] = max(3 + dp[1], dp[2]) = max(3+7, 11)  = max(10, 11) = 11
i=4: dp[4] = max(1 + dp[2], dp[3]) = max(1+11, 11) = max(12, 11) = 12

return dp[4] = dp[n-1] = 12 ✅
```

---

## Bugs to Watch Out For

### Bug 1 — Wrong loop range
```python
# WRONG
for i in range(2, n+1):   # goes out of bounds — nums[n] doesn't exist

# CORRECT
for i in range(2, n):
```

### Bug 2 — Returning loop variable instead of dp[n-1]
```python
# WRONG
return dp[i]   # i is the loop variable — unreliable after loop ends
               # crashes with UnboundLocalError when loop never runs (e.g. n=2)

# CORRECT
return dp[n-1]
```

> 💡 Golden rule: **never return `dp[i]` after a loop.** Always return the specific index your definition points to. Your definition says "f(n-1) = max profit across all houses" → return `dp[n-1]`.

### Bug 3 — Missing n=1 edge case
When `n = 1`, `dp[1]` doesn't exist yet. Handle it separately:
```python
if n == 1: return nums[0]
```

---

## Key Mental Notes

### On the recurrence choice
The "rob or don't rob" pattern appears everywhere in DP. Whenever a problem says "you can't take two adjacent/consecutive elements," immediately think:
- **Take it** → skip one back → `nums[i] + f(i-2)`
- **Skip it** → `f(i-1)`

### On base cases
Here the base cases are clean and intuitive — actual profit values, no weird conventions like LC 70's `dp[0] = 1`.  
`f(0)` = just rob the only available house.  
`f(1)` = pick the richer of the first two houses.

### On what to return
Your f(i) definition is "max profit from 0 to i" → answer lives at `dp[n-1]`. Always tie your return statement back to your definition.

---

## Comparison with Previous Problems

| Problem | Keyword | Recurrence | Key difference |
|---|---|---|---|
| LC 746 Min Cost Climbing Stairs | Multiple ways → Min | `min(f(i-1)+cost[i-1], f(i-2)+cost[i-2])` | Backward — came from i-1 or i-2 |
| LC 70 Climbing Stairs | Count total ways | `f(i-1) + f(i-2)` | Count → add instead of min/max |
| LC 198 House Robber | Multiple ways → Max | `max(nums[i]+f(i-2), f(i-1))` | Choice: rob (skip adjacent) or skip |
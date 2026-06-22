# LC 746 — Min Cost Climbing Stairs | DP Notes

**LeetCode ID:** 746  
**GFG Problem Name:** Min Cost Climbing Stairs  
**Topic:** 1D Dynamic Programming  
**Pattern:** Multiple ways of doing something → find Minimum  

---

## The Problem

You are given an array `cost[]` where `cost[i]` is the cost of stepping on stair `i`.  
Once you pay the cost, you can jump **1 step** or **2 steps** forward.  
You can start from index `0` or index `1` for **free**.  
Goal: reach the **top of the floor** (index `n`, just beyond the last stair) with **minimum cost**.

**Example:**
```
cost = [10, 15, 20]

Possible paths:
- Start at 0 → pay 10 → jump 2 → reach top  → total = 10
- Start at 1 → pay 15 → jump 2 → reach top  → total = 15
- Start at 0 → pay 10 → jump 1 → pay 15 → jump 1 → reach top → total = 25

Answer = 15
```

---

## Step 1 — Identify it as a DP Problem

Your tutor's framework says: first identify the keyword.

> **Keyword here:** "Multiple ways of reaching the top → find the Minimum cost"

This means DP. At every stair, you have **choices** (1-step or 2-step) and you want the **best** outcome across all those choices.

> ⚠️ Important distinction: The keyword tells you *what type* of DP it is. It does NOT define your `f(i)`. Don't mix these two up.

---

## Step 2 — Define f(i) Clearly

This is the most important step. Your `f(i)` definition controls everything that follows.

**Wrong definition (common mistake):**
> "f(i) = number of ways to reach the top"  
This is wrong because the problem asks for **minimum cost**, not a count. You can't `min()` a count — that doesn't mean anything.

**Correct definition:**
> **f(i) = minimum cost to reach index i**

And the final answer is:
> **f(n)** — because the top floor is at index `n` (one beyond the last stair at index `n-1`)

> 💡 If cost[] has n elements (indices 0 to n-1), the "top" is index n. Not n-1. Think of it like floors — to climb ALL stairs, you must land beyond the last one.

---

## Step 3 — Thinking Direction (Backward vs Forward)

Once you define `f(i) = cost to reach i`, your thinking direction naturally becomes **backward**:

> "I'm at stair `i`. How did I get here?"

You came from either:
- `i-1` (took a 1-step jump from i-1), or
- `i-2` (took a 2-step jump from i-2)

**Why backward?**  
Because f(i) is defined as cost to *reach* i — so it's natural to ask "where did I come from to get here?"

**Alternative — forward thinking:**  
You could define `f(i) = minimum cost to reach the top FROM index i`. Then you'd ask "where do I go from here?" Both are valid. They just produce different (but equally correct) recurrences. Your tutor used backward — so we stick with that.

---

## Step 4 — Build the Recurrence Relation

Apply the 1D DP framework:

**1. Represent in terms of index** → done: `f(i)`

**2. Do all possible stuff at that index:**

If I arrived at `i` from `i-1`:
- It cost me `f(i-1)` to reach `i-1`
- Then I paid `cost[i-1]` to step off stair `i-1` and jump to `i`
- Total = `f(i-1) + cost[i-1]`

If I arrived at `i` from `i-2`:
- It cost me `f(i-2)` to reach `i-2`
- Then I paid `cost[i-2]` to step off stair `i-2` and jump to `i`
- Total = `f(i-2) + cost[i-2]`

**3. Find the minimum:**

```
f(i) = min(f(i-1) + cost[i-1], f(i-2) + cost[i-2])
```

---

## Step 5 — Base Cases

The recursion must stop somewhere. Without base cases, `f(0)` would try to call `f(-1)` and `f(-2)` — which don't exist.

**Think about it physically:**
- To *be* at stair 0, you started there → free → `f(0) = 0`
- To *be* at stair 1, you started there → free → `f(1) = 0`

```
f(0) = 0
f(1) = 0
```

---

## Step 6 — Complete Recurrence Summary

```
f(0) = 0
f(1) = 0
f(i) = min(f(i-1) + cost[i-1], f(i-2) + cost[i-2])   for i >= 2

Answer = f(n)
```

---

## Step 7 — Plain Recursion Code (Python)

```python
def func(idx, cost):
    if idx == 0 or idx == 1:
        return 0
    onestep = func(idx - 1, cost) + cost[idx - 1]
    twostep = func(idx - 2, cost) + cost[idx - 2]
    return min(onestep, twostep)
```

**Call it as:**
```python
n = len(cost)
print(func(n, cost))
```

**⚠️ Problem with this:** Time complexity is **O(2^n)**.

Why? Trace `f(5)`:
```
f(5)
├── f(4)
│   ├── f(3)
│   │   ├── f(2)   ← computed here
│   │   └── f(1)
│   └── f(2)       ← computed AGAIN
└── f(3)           ← computed AGAIN
    ├── f(2)       ← computed AGAIN
    └── f(1)
```

`f(2)` is computed 3 times, `f(3)` twice. This is called **overlapping subproblems** — the core problem that DP solves.

---

## Step 8 — Memoization (Top-Down DP)

**The fix:** Before computing `f(i)`, check if we already computed it. If yes, reuse it directly.

**How:**
1. Create a `dp[]` array of size `n+1`, initialized to `-1` (meaning "not yet computed")
2. Before computing `f(i)`, check if `dp[i] != -1` — if so, return `dp[i]`
3. After computing, store the result in `dp[i]` before returning

```python
def func(idx, dp):
    # Base case
    if idx == 0 or idx == 1:
        return 0
    
    # Already computed? Return directly (the "dejavu" check)
    if dp[idx] != -1:
        return dp[idx]
    
    # Compute
    onestep = func(idx - 1, dp) + cost[idx - 1]
    twostep = func(idx - 2, dp) + cost[idx - 2]
    
    # Store before returning
    dp[idx] = min(onestep, twostep)
    return dp[idx]


# Driver
n = len(cost)
dp = [-1] * (n + 1)
print(func(n, dp))
```

**Time complexity: O(n)** — every subproblem is solved exactly once.  
**Space complexity: O(n)** — for the dp array + recursion call stack.

---

## Key Mental Notes (Don't Forget These)

### On defining f(i)
Your f(i) definition is the foundation. Get it wrong and everything else crumbles.  
Always ask: *"What does my function return in plain English?"* and make sure it matches what the problem is asking.

### On the top of the stairs
If cost[] has n elements → top is index **n** (not n-1).  
Always figure out where the answer lives before writing the call.

### On backward vs forward thinking
- `f(i)` = cost to *reach* i → ask "where did I come from?" (backward)
- `f(i)` = cost to *go* from i to top → ask "where do I go?" (forward)  
Neither is wrong. Pick one and stay consistent.

### On memoization
Memoization = "recognize we've been here before and skip the work."  
Three moves: init dp with -1, check before computing, store after computing.

### On overlapping subproblems
When you see the same `f(i)` being called multiple times in a recursion tree — that's the signal. Plain recursion is exponential. Memoization brings it to linear.

---

## What's Next — Tabulation (Bottom-Up DP)

Memoization is **top-down** — start from `f(n)` and recurse down to base cases.  
Tabulation is **bottom-up** — start from base cases and build up to `f(n)` using a loop. No recursion at all.

Same recurrence, different implementation direction.
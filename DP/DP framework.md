# Master DP Frameworks & Patterns

---

## Framework 1 — How to Identify a DP Problem

### Step 1: Is it a recursive problem?
Ask yourself — does the problem involve **making choices** at each step?
If yes → it's recursive → it might be DP.

### Step 2: Which keyword applies?

| Keyword | Example | Operator |
|---|---|---|
| **Count total number of ways** | "How many ways to climb n stairs?" | `+` |
| **Multiple ways → find Min/Max** | "Minimum cost to climb stairs" | `min()` or `max()` |
| **Can it be done?** | "Can we partition into equal subsets?" | `or` / `True` / `False` |

> ⚠️ The keyword tells you what TYPE of DP it is. It does NOT define f(i). Don't mix them up.

---

## Framework 2 — How to Build the Recurrence (1D DP)

Your tutor's 3 steps:

```
1) Represent the problem in terms of INDEX
2) Do ALL possible stuff at that index (your choices)
3) Combine results using min / max / sum / or
```

### Step 1 — Define f(i) clearly
f(i) must match exactly what the problem asks you to return.

| Problem | f(i) definition |
|---|---|
| Min Cost Climbing Stairs | f(i) = minimum cost to REACH index i |
| Climbing Stairs | f(i) = number of ways to REACH index i |
| House Robber | f(i) = maximum profit from houses 0 to i |

> 💡 Your f(i) definition decides your thinking direction:
> - "cost to REACH i" → think BACKWARD (where did I come from?)
> - "cost to go FROM i to end" → think FORWARD (where do I go?)

### Step 2 — Do all possible stuff at index i
List every choice you have at index i.

Example — Min Cost Climbing Stairs:
- Came from i-1 → cost = f(i-1) + cost[i-1]
- Came from i-2 → cost = f(i-2) + cost[i-2]

Example — House Robber:
- Rob house i → nums[i] + f(i-2)
- Skip house i → f(i-1)

### Step 3 — Combine using the right operator

```python
# Count total ways → ADD
f(i) = f(i-1) + f(i-2)

# Find minimum → MIN
f(i) = min(f(i-1) + cost[i-1], f(i-2) + cost[i-2])

# Find maximum → MAX
f(i) = max(nums[i] + f(i-2), f(i-1))

# Can it be done → OR
f(i, target) = f(i+1, target-nums[i]) or f(i+1, target)
```

---

## Framework 3 — Base Cases

Base cases = the stopping point of recursion.

**Rule:** Ask "what is the simplest version of this problem that I can answer directly?"

| Problem | Base Case | Why |
|---|---|---|
| Min Cost Climbing Stairs | f(0)=0, f(1)=0 | Start there for free |
| Climbing Stairs | f(0)=1, f(1)=1 | 1 way to be at start (empty path counts!) |
| House Robber | f(0)=nums[0], f(1)=max(nums[0],nums[1]) | Only 1 or 2 houses available |
| Partition Subset Sum | target==0 → True, i==n → False | Found answer / ran out of elements |

> ⚠️ The `f(0) = 1` trap: "0 ways" feels right but the correct answer is "1 way — the empty path."
> In combinatorics, doing nothing = 1 valid way.

---

## Framework 4 — The Count Total Ways Skeleton

Your tutor's golden framework for ANY "count total ways" problem:

```python
def f(params):
    # Base case — found a valid answer
    if condition_true:
        return 1
    # Base case — invalid / ran out of options
    if condition_false:
        return 0

    # Make choices
    option1 = f(smaller_problem_1)
    option2 = f(smaller_problem_2)

    # Combine — ADD for counting
    return option1 + option2
```

### Example — LC #70 Climbing Stairs
```python
def f(i):
    if i == 0: return 1   # 1 way to be at start
    if i < 0:  return 0   # invalid

    return f(i-1) + f(i-2)
```

---

## Framework 5 — All 3 Problem Types Side by Side

```python
# TYPE 1: Count total ways → return int (count)
def f(i):
    if base_true:  return 1
    if base_false: return 0
    return f(i-1) + f(i-2)   # ADD

# TYPE 2: Find Min/Max → return int (value)
def f(i):
    if base_case: return actual_value
    option1 = f(i-1) + cost
    option2 = f(i-2) + cost
    return min(option1, option2)   # or max()

# TYPE 3: Can it be done → return bool
def f(i, target):
    if target == 0: return True
    if i == n:      return False
    include = f(i+1, target - nums[i])
    exclude = f(i+1, target)
    return include or exclude   # OR
```

| Type | Keyword | Base case returns | Combine with |
|---|---|---|---|
| Count ways | "total number of ways" | 1 or 0 | `+` |
| Min/Max | "minimum/maximum of ways" | actual value | `min()` / `max()` |
| Existence | "can it be done" | True or False | `or` |

---

## Framework 6 — Converting Recursion → Memoization

**3 moves. Always the same 3 moves.**

```
1. Initialize dp array with -1
2. CHECK: if dp[...] != -1 → return dp[...] (before computing)
3. STORE: dp[...] = result (after computing, before returning)
```

### 1D Memoization Template
```python
dp = [-1] * (n + 1)

def f(i):
    if i == 0 or i == 1:      # base case
        return base_value

    if dp[i] != -1:            # CHECK
        return dp[i]

    result = f(i-1) + f(i-2)  # compute

    dp[i] = result             # STORE
    return dp[i]
```

### 2D Memoization Template
```python
dp = [[-1] * cols for _ in range(rows)]

def f(i, j):
    if base_case:              # base case
        return base_value

    if dp[i][j] != -1:         # CHECK
        return dp[i][j]

    result = f(i-1, j) + ...   # compute

    dp[i][j] = result          # STORE
    return dp[i][j]
```

### When to use 2D dp?
Your function has **2 changing parameters** → 2D dp.
Example: `f(day, last)` in Geek's Training → `dp[day][last]`

> 💡 Rule: number of dimensions in dp = number of changing parameters in your function.

---

## Framework 7 — Converting Memoization → Tabulation

**Key difference:**
- Memoization = top-down (start from answer, recurse to base)
- Tabulation = bottom-up (start from base, build to answer)

```
Memoization → Tabulation conversion steps:
1. Remove the recursive function entirely
2. Fill base cases manually before the loop
3. Loop from base → answer (opposite direction of recursion)
4. Return dp[answer_index] explicitly
```

### 1D Tabulation Template
```python
dp = [-1] * (n + 1)

# Base cases
dp[0] = base_value_0
dp[1] = base_value_1

# Fill bottom-up
for i in range(2, n + 1):
    dp[i] = dp[i-1] + dp[i-2]   # same recurrence, just with array

return dp[n]   # explicit — tied to your f(i) definition
```

### 2D Tabulation Template
```python
dp = [[-1] * cols for _ in range(rows)]

# Base cases — fill row 0 manually
dp[0][0] = ...
dp[0][1] = ...

# Fill remaining rows
for i in range(1, rows):
    for j in range(cols):
        dp[i][j] = dp[i-1][...] + ...   # recurrence

return dp[rows-1][answer_col]   # explicit
```

---

## Framework 8 — Common Bugs Checklist

### Loop range bugs
```python
for i in range(2, n):    # goes up to n-1
for i in range(2, n+1):  # goes up to n
```
Which one depends on your dp array size and f(i) definition.

### Return statement bugs
```python
return dp[i]      # ❌ loop variable — unreliable, crashes if loop never runs
return dp[n-1]    # ✅ explicit — tied to your definition
return dp[n]      # ✅ if top is index n
```
**Golden rule: never return `dp[loop_variable]`. Always return `dp[specific_index]`.**

### Wrong base case values
```python
# Climbing Stairs
dp[0] = 0   # ❌ feels right but breaks recurrence
dp[0] = 1   # ✅ "1 way to stand at start — the empty path"
```

### Indexing bugs
```python
dp[day-1, task]    # ❌ wrong Python syntax for 2D list
dp[day-1][task]    # ✅ correct
```

---

## Full Journey Template (Any DP Problem)

```
Step 1: Identify keyword → Count / Min-Max / Existence
Step 2: Define f(i) in plain English — match what problem asks
Step 3: Decide direction — forward or backward
Step 4: List choices at index i
Step 5: Write recurrence using right operator (+, min, max, or)
Step 6: Write base cases
Step 7: Code plain recursion
Step 8: Add memoization (3 moves)
Step 9: Convert to tabulation (fill table bottom-up)
```

---

## Problems Solved & Patterns Used

| Problem | LC ID | Type | Operator | Dimensions |
|---|---|---|---|---|
| Min Cost Climbing Stairs | 746 | Min/Max | `min()` | 1D |
| Climbing Stairs | 70 | Count ways | `+` | 1D |
| House Robber | 198 | Min/Max | `max()` | 1D |
| House Robber II | 213 | Min/Max | `max()` | 1D (run twice) |
| Partition Equal Subset Sum | 416 | Existence | `or` | 2D |
| Geek's Training | GFG | Min/Max | `max()` | 2D |
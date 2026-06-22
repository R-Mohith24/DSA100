# Geek's Training | DP Notes (Recursion)

**GFG Problem Name:** Geek's Training  
**Topic:** 2D Dynamic Programming  
**Pattern:** Multiple ways of doing something → find Maximum  

---

## The Problem

Geek has `n` days of training. Each day he can do one of 3 activities:
- `0` = Running
- `1` = Fighting  
- `2` = Learning

`mat[i][j]` = merit points for activity `j` on day `i`.

**Constraint:** Cannot do the same activity on two consecutive days.  
**Goal:** Maximize total merit points across all `n` days.

**Example:**
```
mat = [[1, 2, 5],   ← day 0
       [3, 1, 1],   ← day 1
       [3, 3, 3]]   ← day 2

Best path: Learning(day 0) + Running(day 1) + Fighting(day 2)
         = 5 + 3 + 3 = 11 ✅
```

---

## Step 1 — Identify it as DP

**Keyword:** Multiple ways of picking activities across days → find **Maximum** points.

At each day you have choices (3 activities, minus restriction) and want the best outcome → DP.

---

## Step 2 — Define f(i)

**First attempt (1 parameter):**
> f(i) = maximum merit points from day 0 to day i

This feels right — but there's a problem. The problem has a **constraint**: you can't repeat the same activity on consecutive days.

So f(i) alone is not enough — you also need to know **what activity was done on day i**, so that day i+1 knows what to avoid.

**Correct definition (2 parameters):**
> **f(day, last) = maximum merit points from day 0 to `day`, given that `last` was the activity performed on `day`**

Final answer = `f(n-1, 3)` — start from last day, `last=3` means no restriction (3 is an invalid activity index).

---

## Step 3 — Understanding the `last` Parameter

This is the trickiest part. Let's be very clear:

> `last` does NOT mean "restriction on THIS day."  
> `last` means "what I did on the PREVIOUS day — so don't repeat it today."

So when you call `f(2, last=3)`:
- You're on day 2
- `last=3` → no restriction (no previous day from the initial call's perspective)

When recursion goes deeper:
- Day 2 picks activity `j` → calls `f(1, last=j)`
- Day 1 now knows "don't pick `j` today"
- Day 1 picks activity `k` → calls `f(0, last=k)`
- Day 0 now knows "don't pick `k` today"

So the flow is:
```
f(2, last=3)      ← day 2, unrestricted
  → f(1, last=j)  ← day 1, restricted by day 2's choice
    → f(0, last=k) ← day 0, restricted by day 1's choice
```

> ⚠️ Common mistake: thinking day 0 is always unrestricted because "it's the starting day."  
> Day 0 IS restricted — by whatever day 1 picked. Only the initial call (day n-1) is unrestricted.

---

## Step 4 — Build the Recurrence

At each day, loop through all 3 activities. Skip whichever equals `last`. For each valid activity `j`:

- Earn `mat[day][j]` points today
- Plus the best points from all previous days: `f(day-1, j)`
- Pass `j` as the new `last` so the previous day knows what to avoid

```
for j in [0, 1, 2]:
    if j != last:
        points = f(day-1, j) + mat[day][j]

f(day, last) = max(points across all valid j)
```

---

## Step 5 — Base Case

When `day == 0` — the very first day. No previous days exist to recurse into.

Just pick the best activity that isn't `last`:

```
if day == 0:
    return max(mat[0][j] for j in [0,1,2] if j != last)
```

> 💡 Note: day 0 can still be restricted! If day 1 picked activity 2, then day 0 can't pick activity 2 either. The `last` parameter handles this automatically.

---

## Step 6 — Complete Recursive Solution

```python
def training(days, last, mat):
    activities = [0, 1, 2]
    maxi = 0

    # Base case — first day, pick best available activity
    if days == 0:
        for task in activities:
            if task != last:
                maxi = max(maxi, mat[0][task])
        return maxi

    # Recursive case — try all valid activities
    for task in activities:
        if task != last:
            points = training(days - 1, task, mat) + mat[days][task]
            maxi = max(maxi, points)

    return maxi


# Initial call — start from last day, no restriction (last=3)
n = len(mat)
print(training(n - 1, 3, mat))
```

---

## Dry Run

```
mat = [[1, 2, 5],
       [3, 1, 1],
       [3, 3, 3]]
```

**`training(2, last=3)`** — day 2, no restriction:
- j=0: mat[2][0] + training(1, 0) = 3 + training(1, 0)
- j=1: mat[2][1] + training(1, 1) = 3 + training(1, 1)
- j=2: mat[2][2] + training(1, 2) = 3 + training(1, 2)

**`training(1, last=0)`** — day 1, can't do activity 0:
- j=1: mat[1][1] + training(0, 1) = 1 + training(0, 1)
- j=2: mat[1][2] + training(0, 2) = 1 + training(0, 2)

**`training(0, last=1)`** — day 0, can't do activity 1:
- j=0: mat[0][0] = 1
- j=2: mat[0][2] = 5
- returns max(1, 5) = **5**

**`training(0, last=2)`** — day 0, can't do activity 2:
- j=0: mat[0][0] = 1
- j=1: mat[0][1] = 2
- returns max(1, 2) = **2**

Back to `training(1, last=0)`:
- j=1: 1 + 5 = 6
- j=2: 1 + 2 = 3
- returns **6**

**`training(1, last=1)`** — day 1, can't do activity 1:
- j=0: mat[1][0] + training(0, 0) = 3 + max(2,5) = 3 + 5 = 8
- j=2: mat[1][2] + training(0, 2) = 1 + max(1,2) = 1 + 2 = 3
- returns **8**

**`training(1, last=2)`** — day 1, can't do activity 2:
- j=0: mat[1][0] + training(0, 0) = 3 + 5 = 8
- j=1: mat[1][1] + training(0, 1) = 1 + max(1,5) = 1 + 5 = 6
- returns **8**

Back to `training(2, last=3)`:
- j=0: 3 + 6  = 9
- j=1: 3 + 8  = 11
- j=2: 3 + 8  = 11
- returns **max(9, 11, 11) = 11 ✅**

---

## Key Mental Notes

### On needing 2 parameters
Whenever a problem has a **constraint between consecutive choices** (can't repeat, can't go adjacent, etc.), your f(i) likely needs a second parameter to carry that constraint forward.

### On the initial call
Always pass an **invalid/sentinel value** for `last` in the initial call to mean "no restriction."  
Convention: use `3` (or `-1`) since valid activities are only 0, 1, 2.

### On forward vs backward
- Definition: `f(day, last)` = max points from day 0 **to** day (forward definition)
- Implementation: recurse to `day-1` (backward recursion)
- Both are consistent — the definition tells you what f means, recursion tells you how to compute it.

### On the base case
Base case is NOT always "no restriction." Day 0 gets restricted by whatever day 1 chose.  
The `last` parameter handles this automatically — trust it.

---

## What's Next

This recursive solution has **overlapping subproblems** — same `(day, last)` pairs get recomputed multiple times.

Next step: **Memoization** — add a 2D dp array of size `n × 4` (4 because last can be 0,1,2,3) initialized to -1, and cache results at `dp[day][last]`.



# Geek's Training | DP Notes (Memoization)

**Continuing from:** Recursion notes  
**This section covers:** Converting recursion → memoization  

---

## The Problem with Plain Recursion

The recursive solution works correctly but is **exponentially slow**.

Why? Because the same `(days, last)` pairs get recomputed multiple times.

For example, `training(1, last=0)` might be called from multiple different branches of the recursion tree — and each time, it repeats all the work from scratch.

This is the **overlapping subproblems** problem — same thing that killed plain recursion in LC 746 and House Robber.

**Time complexity of plain recursion: O(3^n)**  
(At each day, up to 3 choices, repeated n times)

---

## The Fix — Memoization

The idea is simple:

> "If we already computed `training(days, last)` before — just reuse that answer. Don't compute it again."

**3 moves to add memoization (always the same 3 moves):**
1. Initialize a dp array with `-1` (meaning "not yet computed")
2. Before computing — **check** if `dp[days][last] != -1` → return it directly
3. After computing — **store** `maxi` in `dp[days][last]` before returning

---

## Why is dp 2D here?

In 1D problems like LC 746, the function had **one parameter** (`idx`) → 1D dp array.

Here, `training(days, last)` has **two parameters** → 2D dp array.

`dp[days][last]` stores the answer to: "max points from day 0 to `days`, given last activity was `last`."

---

## Size of the dp Array

- `days` ranges from `0` to `n-1` → **n rows**
- `last` ranges from `0` to `3` → **4 columns**
  - 0, 1, 2 = actual activities
  - 3 = sentinel value meaning "no restriction" (used in initial call)

```python
dp = [[-1] * 4 for _ in range(n)]
```

---

## The Memoization Pattern (Always the Same)

```
function(params):
    BASE CASE → return directly (no storing needed)
    
    CHECK → if dp[...] != -1: return dp[...]
    
    COMPUTE → do the work (same as plain recursion)
    
    STORE → dp[...] = result
    RETURN → dp[...]
```

> ⚠️ Common mistake: storing inside the base case.  
> You don't need to — base cases are trivially fast and always return the same value anyway.

---

## The Confusing Part — What to Check and Return

This confused us during the session. Here's the clear answer:

Your function returns `maxi` at the end.  
So `maxi` is exactly what you store in dp.

```python
dp[days][last] = maxi      # store what you computed
return dp[days][last]      # return the stored value
```

And the check before computing:
```python
if dp[days][last] != -1:   # already computed before?
    return dp[days][last]  # yes → skip all work, return directly
```

Simple rule: **whatever you return, you store. Whatever you store, you check.**

---

## The `last=3` Sentinel — Why It Works

A natural question: "Where does the program know `last=3` means no restriction?"

Answer: **It doesn't need to explicitly know.** It's just math.

The check inside the loop is:
```python
if task != last:   # last = 3
```

When `last=3`:
- task=0: 0 != 3 ✅ allowed
- task=1: 1 != 3 ✅ allowed  
- task=2: 2 != 3 ✅ allowed

All 3 activities pass through naturally. No special case needed. `3` is just an out-of-range value that never matches any valid activity.

---

## Dry Run (Small Example)

```
mat = [[2, 3, 1],   ← day 0
       [4, 1, 5]]   ← day 1

n = 2
dp = [[-1,-1,-1,-1],   ← day 0
      [-1,-1,-1,-1]]   ← day 1
```

**Initial call: `training(1, last=3)`**

`dp[1][3] == -1` → not cached, proceed.

Try all tasks:
- j=0: 4 + `training(0, 0)`
- j=1: 1 + `training(0, 1)`
- j=2: 5 + `training(0, 2)`

---

**`training(0, last=0)`** → base case (day=0)
- j=1: mat[0][1] = 3
- j=2: mat[0][2] = 1
- returns **3** → `dp[0][0] = 3`

**`training(0, last=1)`** → base case
- j=0: mat[0][0] = 2
- j=2: mat[0][2] = 1
- returns **2** → `dp[0][1] = 2`

**`training(0, last=2)`** → base case
- j=0: mat[0][0] = 2
- j=1: mat[0][1] = 3
- returns **3** → `dp[0][2] = 3`

---

Back to **`training(1, last=3)`**:
- j=0: 4 + 3 = 7
- j=1: 1 + 2 = 3
- j=2: 5 + 3 = **8** ← winner
- `dp[1][3] = 8`
- returns **8** ✅

**Final dp table:**
```
         last=0  last=1  last=2  last=3
day 0  [   3,     2,      3,     -1   ]
day 1  [  -1,    -1,     -1,      8   ]
```

Notice: if `training(1, 3)` is ever called again → immediately returns `dp[1][3] = 8`. No recomputation.

---

## Complete Memoized Solution

```python
def solve(mat):
    n = len(mat)
    activities = [0, 1, 2]

    # Initialize dp with -1
    dp = [[-1] * 4 for _ in range(n)]

    def training(days, last):
        maxi = 0

        # Base case — first day
        if days == 0:
            for task in activities:
                if task != last:
                    maxi = max(maxi, mat[0][task])
            return maxi

        # Check — already computed?
        if dp[days][last] != -1:
            return dp[days][last]

        # Compute
        for task in activities:
            if task != last:
                points = training(days - 1, task) + mat[days][task]
                maxi = max(maxi, points)

        # Store and return
        dp[days][last] = maxi
        return dp[days][last]

    # Initial call — last day, no restriction
    return training(n - 1, 3)


mat = [[1, 2, 5],
       [3, 1, 1],
       [3, 3, 3]]
print(solve(mat))  # Output: 11
```

---

## Time and Space Complexity

| | Plain Recursion | Memoization |
|---|---|---|
| Time | O(3^n) | O(n × 4) = **O(n)** |
| Space | O(n) call stack | O(n × 4) dp + O(n) stack = **O(n)** |

Every unique `(days, last)` pair is computed exactly once. There are `n × 4` such pairs → O(n) time.

---

## Key Mental Notes

### The 3 memoization moves are always the same
Check → Compute → Store. This never changes across any DP problem. Only the dp indexing changes (1D vs 2D vs 3D).

### 2D dp = 2 changing parameters
Whenever your recursive function has 2 parameters that change across calls → 2D dp. 3 parameters → 3D dp. And so on.

### Store what you return
Whatever value your function returns (`maxi` here) — that's what goes into dp. Never store intermediate values.

### Base case doesn't need storing
Base cases are O(1) to compute and always return the same value. No need to cache them.

---

## What's Next — Tabulation (Bottom-Up)

Memoization is top-down — starts at `training(n-1, 3)` and recurses down to day 0.

Tabulation is bottom-up — starts at day 0 and builds up to day n-1 using a loop. No recursion at all.

Same recurrence, same dp array, just filled in the opposite direction.

```ruby
class Solution:
    def maximumPoints(self, mat):
        activities = [0,1,2]
        dp = []
        n = len(mat)
        for _ in range(n):
            dp.append([-1]*4)
            
        def training(days,last,dp):
            maxi = 0
            if days == 0:
                for tasks in activities:
                    if tasks != last:
                        maxi = max(maxi , mat[0][tasks])
                        
                return maxi
            if dp[days][last] != -1:
                return dp[days][last]
                
            for tasks in activities:
                if tasks != last:
                    points = training(days-1 , tasks ,dp) + mat[days][tasks]
                    maxi = max(points,maxi)
                    
            dp[days][last] = maxi
            return dp[days][last]
            
        ans = training(n-1 , 3 , dp)
        return ans
```


# Geek's Training | DP Notes (Tabulation)

**Continuing from:** Memoization notes  
**This section covers:** Converting memoization → tabulation  

---

## Memoization vs Tabulation — Key Difference

| | Memoization (Top-Down) | Tabulation (Bottom-Up) |
|---|---|---|
| Direction | Starts at `f(n-1, 3)`, recurses down to day 0 | Starts at day 0, builds up to day n-1 |
| Implementation | Recursive function + dp check | Just loops, no recursion |
| Base cases | Inside the function as `if` conditions | Filled manually before the loop |
| Return | From the recursive call | From `dp[n-1][3]` directly |

Same recurrence. Same dp array. Just opposite direction.

---

## Step 1 — Fill Base Cases (day 0)

In memoization, base cases were handled inside the recursive function as `if days == 0`.

In tabulation, you fill them **manually before the loop starts**.

For day 0, `dp[0][last]` = best activity on day 0 excluding `last`:

```python
dp[0][0] = max(mat[0][1], mat[0][2])        # can't do task 0
dp[0][1] = max(mat[0][0], mat[0][2])        # can't do task 1
dp[0][2] = max(mat[0][0], mat[0][1])        # can't do task 2
dp[0][3] = max(mat[0][0], mat[0][1], mat[0][2])  # no restriction
```

---

## Step 2 — Fill Remaining Days (loop)

For each `(day, last)` cell, try all valid tasks and pick the best:

```python
for day in range(1, n):
    for last in range(4):
        maxi = 0
        for task in activities:
            if task != last:
                points = dp[day-1][task] + mat[day][task]
                maxi = max(maxi, points)
        dp[day][last] = maxi
```

**Why 3 loops?**
- Loop 1 (`day`) → fills one row at a time
- Loop 2 (`last`) → fills one cell in that row
- Loop 3 (`task`) → tries all valid activities for that cell

---

## Step 3 — Return Answer

```python
return dp[n-1][3]
```

`dp[n-1][3]` = max points up to last day, no restriction on last activity = the final answer.

---

## Dry Run

```
mat = [[1, 2, 5],   ← day 0
       [3, 1, 1],   ← day 1
       [3, 3, 3]]   ← day 2
n = 3
```

### Base Cases (day 0):
```
dp[0][0] = max(2, 5) = 5   (skip task 0)
dp[0][1] = max(1, 5) = 5   (skip task 1)
dp[0][2] = max(1, 2) = 2   (skip task 2)
dp[0][3] = max(1, 2, 5) = 5 (no restriction)
```

```
         last=0  last=1  last=2  last=3
day 0  [   5,     5,      2,      5   ]
day 1  [  -1,    -1,     -1,     -1   ]
day 2  [  -1,    -1,     -1,     -1   ]
```

---

### day=1:

**last=0** (skip task 0):
```
task=0: SKIP
task=1: dp[0][1] + mat[1][1] = 5 + 1 = 6
task=2: dp[0][2] + mat[1][2] = 2 + 1 = 3
dp[1][0] = max(6, 3) = 6
```

**last=1** (skip task 1):
```
task=0: dp[0][0] + mat[1][0] = 5 + 3 = 8
task=1: SKIP
task=2: dp[0][2] + mat[1][2] = 2 + 1 = 3
dp[1][1] = max(8, 3) = 8
```

**last=2** (skip task 2):
```
task=0: dp[0][0] + mat[1][0] = 5 + 3 = 8
task=1: dp[0][1] + mat[1][1] = 5 + 1 = 6
task=2: SKIP
dp[1][2] = max(8, 6) = 8
```

**last=3** (no restriction):
```
task=0: dp[0][0] + mat[1][0] = 5 + 3 = 8
task=1: dp[0][1] + mat[1][1] = 5 + 1 = 6
task=2: dp[0][2] + mat[1][2] = 2 + 1 = 3
dp[1][3] = max(8, 6, 3) = 8
```

```
         last=0  last=1  last=2  last=3
day 0  [   5,     5,      2,      5   ]
day 1  [   6,     8,      8,      8   ]
day 2  [  -1,    -1,     -1,     -1   ]
```

---

### day=2:

**last=0** (skip task 0):
```
task=0: SKIP
task=1: dp[1][1] + mat[2][1] = 8 + 3 = 11
task=2: dp[1][2] + mat[2][2] = 8 + 3 = 11
dp[2][0] = 11
```

**last=1** (skip task 1):
```
task=0: dp[1][0] + mat[2][0] = 6 + 3 = 9
task=1: SKIP
task=2: dp[1][2] + mat[2][2] = 8 + 3 = 11
dp[2][1] = 11
```

**last=2** (skip task 2):
```
task=0: dp[1][0] + mat[2][0] = 6 + 3 = 9
task=1: dp[1][1] + mat[2][1] = 8 + 3 = 11
task=2: SKIP
dp[2][2] = 11
```

**last=3** (no restriction):
```
task=0: dp[1][0] + mat[2][0] = 6 + 3 = 9
task=1: dp[1][1] + mat[2][1] = 8 + 3 = 11
task=2: dp[1][2] + mat[2][2] = 8 + 3 = 11
dp[2][3] = 11
```

### Final dp table:
```
         last=0  last=1  last=2  last=3
day 0  [   5,     5,      2,      5   ]
day 1  [   6,     8,      8,      8   ]
day 2  [  11,    11,     11,     11   ]
```

**Return `dp[2][3]` = `dp[n-1][3]` = 11 ✅**

---

## Complete Tabulation Solution

```python
class Solution:
    def maximumPoints(self, mat):
        activities = [0, 1, 2]
        n = len(mat)
        dp = [[-1] * 4 for _ in range(n)]

        # Base cases — day 0
        dp[0][0] = max(mat[0][1], mat[0][2])
        dp[0][1] = max(mat[0][0], mat[0][2])
        dp[0][2] = max(mat[0][0], mat[0][1])
        dp[0][3] = max(mat[0][0], mat[0][1], mat[0][2])

        # Fill remaining days
        for day in range(1, n):
            for last in range(4):
                maxi = 0
                for task in activities:
                    if task != last:
                        points = dp[day-1][task] + mat[day][task]
                        maxi = max(maxi, points)
                dp[day][last] = maxi

        return dp[n-1][3]
```

---

## Time and Space Complexity

| | Memoization | Tabulation |
|---|---|---|
| Time | O(n × 4 × 3) = **O(n)** | O(n × 4 × 3) = **O(n)** |
| Space | O(n×4) dp + O(n) stack = **O(n)** | O(n×4) dp only = **O(n)** |

Tabulation is slightly better on space — no recursion call stack overhead.

---

## Key Mental Notes

### Tabulation = no recursion
If you find yourself writing a recursive function inside tabulation — stop. Tabulation is purely iterative.

### Fill order matters
You must fill day 0 before day 1, day 1 before day 2, and so on — because `dp[day]` depends on `dp[day-1]`. Always fill bottom-up.

### Why loop over `last` too?
In memoization, `last` came as a function parameter — it varied naturally via recursion.
In tabulation, no recursion exists — so you must explicitly loop over all possible values of `last` (0, 1, 2, 3) to fill every cell.

### Return is always explicit
Always return `dp[n-1][3]` — not `dp[day][last]` (loop variable), not `dp[n][3]` (out of bounds). Tie your return to your definition: "answer = max points up to last day, no restriction."

---

## Full Journey Summary

```
Problem → identify DP keyword
       → define f(day, last)
       → build recurrence
       → base cases
       → plain recursion   O(3^n)
       → memoization       O(n) time, O(n) space (with stack)
       → tabulation        O(n) time, O(n) space (no stack)
```
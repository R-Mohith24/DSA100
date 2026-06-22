# Minimum Path Sum | DP Notes

**LeetCode ID:** 64
**GFG Problem Name:** Minimum Path Sum in a Grid
**Codeforces:** #1499C (similar spirit, harder)
**Topic:** 2D Dynamic Programming
**Pattern:** Multiple ways → find **Minimum** → operator: `min()`

---

## The Problem

Given an `n×m` grid filled with non-negative numbers, find a path from `grid[0][0]` (top-left) to `grid[n-1][m-1]` (bottom-right) that **minimizes the sum** of all numbers along the path.

**Allowed moves:** Only **right** or **down**.

**Example:**
```
grid = [[1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]]

Best path: 1 → 3 → 1 → 1 → 1 = 7 ✅
```

---

## How is this different from LC #62 and LC #63?

| Problem | What to return | Operator |
|---|---|---|
| LC #62 Unique Paths | Count of paths | `+` |
| LC #63 Unique Paths II | Count of paths (with obstacles) | `+` |
| LC #64 Minimum Path Sum | Minimum cost path | `min()` |

Everything else — grid structure, moves, recurrence skeleton — is **identical**.

---

## Step 1 — Identify it as DP

**Is it recursive?** Yes — at each cell you make a choice (came from above or from left).

**Keyword:** Multiple ways of reaching destination → find **Minimum** cost → `min()` → DP!

---

## Step 2 — Define f(i, j)

> **f(i, j) = minimum path sum to reach cell (i, j) from (0, 0)**

Final answer = `f(n-1, m-1)`

**Thinking direction:** Backward — at `(i, j)`, ask "where did I come from?"

---

## Step 3 — Build the Recurrence

At cell `(i, j)`, you came from either:
- **Above** → `(i-1, j)` → cost = `grid[i][j] + f(i-1, j)`
- **Left** → `(i, j-1)` → cost = `grid[i][j] + f(i, j-1)`

Take the **minimum** of both:

```
f(i, j) = grid[i][j] + min(f(i-1, j), f(i, j-1))
```

---

## Step 4 — Base Cases

```python
if i == 0 and j == 0:
    return grid[0][0]    # start cell — just return its value

if i < 0 or j < 0:
    return float('inf')  # out of bounds — return infinity
```

**Why `grid[0][0]` and not `1`?**
Because unlike counting problems where base = 1, here the base is the **actual cost** of the starting cell.

**Why `float('inf')` for out of bounds?**
Because we're using `min()`. If an invalid path returns `0`, `min()` would always pick it — wrong!
`float('inf')` is always larger than any valid path → `min()` will never pick it. ✅

> 💡 Rule: For **counting** problems → out of bounds returns `0`. For **min/max** problems → out of bounds returns `float('inf')` or `float('-inf')`.

---

## Step 5 — Complete Recurrence Summary

```
f(0, 0) = grid[0][0]
f(i, j) = float('inf')                              if i < 0 or j < 0
f(i, j) = grid[i][j] + min(f(i-1, j), f(i, j-1))  for all other cells

answer = f(n-1, m-1)
```

---

## Step 6 — Recursive Solution

```python
def MinPath(i, j, grid):
    # Base case — start cell
    if i == 0 and j == 0:
        return grid[0][0]
    # Base case — out of bounds
    if i < 0 or j < 0:
        return float('inf')

    up   = grid[i][j] + MinPath(i-1, j, grid)   # came from above
    left = grid[i][j] + MinPath(i, j-1, grid)   # came from left

    return min(up, left)

# Call
n, m = len(grid), len(grid[0])
print(MinPath(n-1, m-1, grid))
```

**Problem:** Overlapping subproblems — same cells recomputed multiple times → O(2^(n+m))

---

## Step 7 — Memoization (Top-Down)

**3 moves as always:**
1. Initialize `dp[n][m]` with `-1`
2. Check `dp[i][j] != -1` → return it
3. Store result before returning

```python
def MinPath(i, j, grid, dp):
    # Base cases
    if i == 0 and j == 0:
        return grid[0][0]
    if i < 0 or j < 0:
        return float('inf')

    # Check
    if dp[i][j] != -1:
        return dp[i][j]

    # Compute
    up   = grid[i][j] + MinPath(i-1, j, grid, dp)
    left = grid[i][j] + MinPath(i, j-1, grid, dp)

    # Store and return
    dp[i][j] = min(up, left)
    return dp[i][j]

# Setup and call
n, m = len(grid), len(grid[0])
dp = [[-1] * m for _ in range(n)]
print(MinPath(n-1, m-1, grid, dp))
```

**Time: O(n×m)** — every cell computed exactly once.
**Space: O(n×m)** — dp array + recursion stack.

---

## Step 8 — Tabulation (Bottom-Up)

**Key insight for tabulation:**
Default `up = left = float('inf')` — NOT `0`!

Why? Because `min(something, 0) = 0` always — which is wrong for cells in the first row/column where one direction is invalid.

```python
class Solution:
    def minPathSum(self, grid):
        n = len(grid)
        m = len(grid[0])
        dp = [[-1] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    dp[i][j] = grid[0][0]        # start cell
                else:
                    up   = float('inf')           # default invalid
                    left = float('inf')           # default invalid
                    if i > 0: up   = grid[i][j] + dp[i-1][j]
                    if j > 0: left = grid[i][j] + dp[i][j-1]
                    dp[i][j] = min(up, left)

        return dp[n-1][m-1]
```

---

## Dry Run

```
grid = [[1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]]
n=3, m=3
```

**Fill order (row by row, left to right):**

```
i=0, j=0: dp[0][0] = grid[0][0] = 1

i=0, j=1: up=inf, left = 1 + dp[0][0] = 1+1 = 4  → dp[0][1] = 4
i=0, j=2: up=inf, left = 1 + dp[0][1] = 1+4 = 5  → dp[0][2] = 5  (wrong wait...)
```

Wait — `grid[0][2] = 1`, so:
```
i=0, j=2: left = grid[0][2] + dp[0][1] = 1 + 4 = 5  → dp[0][2] = 5
```

```
i=1, j=0: left=inf, up = grid[1][0] + dp[0][0] = 1+1 = 2   → dp[1][0] = 2
i=1, j=1: up = grid[1][1] + dp[0][1] = 5+4 = 9
           left = grid[1][1] + dp[1][0] = 5+2 = 7
           dp[1][1] = min(9, 7) = 7

i=1, j=2: up = grid[1][2] + dp[0][2] = 1+5 = 6
           left = grid[1][2] + dp[1][1] = 1+7 = 8
           dp[1][2] = min(6, 8) = 6

i=2, j=0: left=inf, up = grid[2][0] + dp[1][0] = 4+2 = 6   → dp[2][0] = 6
i=2, j=1: up = grid[2][1] + dp[1][1] = 2+7 = 9
           left = grid[2][1] + dp[2][0] = 2+6 = 8
           dp[2][1] = min(9, 8) = 8

i=2, j=2: up = grid[2][2] + dp[1][2] = 1+6 = 7
           left = grid[2][2] + dp[2][1] = 1+8 = 9
           dp[2][2] = min(7, 9) = 7
```

**Final dp table:**
```
      j=0  j=1  j=2
i=0 [  1,   4,   5 ]
i=1 [  2,   7,   6 ]
i=2 [  6,   8,   7 ]
```

**Return `dp[2][2]` = 7 ✅**

Path taken: 1 → 3 → 1 → 1 → 1 = 7

---

## The `float('inf')` Trick — When to Use It

This is a pattern that appears in ALL min/max grid problems:

| Problem type | Default for invalid path |
|---|---|
| Count total ways | `0` |
| Find minimum | `float('inf')` |
| Find maximum | `float('-inf')` |

> 💡 Think about it logically — invalid paths should NEVER be picked by min/max. So give them a value that loses every comparison.

---

## Memoization vs Tabulation — How to NOT Mix Them Up

This was a real confusion during the session. Here's the trigger:

> **Ask yourself: am I writing a FUNCTION or a LOOP?**

| | Memoization | Tabulation |
|---|---|---|
| Structure | `def f(i, j):` | `for i in range(n):` |
| Base cases | `if i==0: return value` | `dp[0][0] = value` |
| Invalid paths | `return float('inf')` | `up = left = float('inf')` |
| dp check | `if dp[i][j] != -1: return dp[i][j]` | not needed |
| Store | `dp[i][j] = result` | `dp[i][j] = result` |
| Return | `return dp[i][j]` | `return dp[n-1][m-1]` |

Pick ONE before writing a single line. Never mix.

---

## Key Mental Notes

### On base cases for min problems
- Start cell → return `grid[0][0]` (actual value, not 1)
- Out of bounds → return `float('inf')` (not 0!)

### On tabulation default values
Initialize `up = left = float('inf')` — NOT `0`. Using `0` causes `min()` to always pick the invalid direction.

### On the recurrence
```
f(i, j) = grid[i][j] + min(f(i-1, j), f(i, j-1))
```
You ADD `grid[i][j]` because you're collecting the cost AT each cell as you pass through it.

---

## All 3 Grid DP Problems Compared

| | LC #62 | LC #63 | LC #64 |
|---|---|---|---|
| Problem | Unique Paths | Unique Paths II | Min Path Sum |
| Extra constraint | None | Obstacles | None |
| Keyword | Count ways | Count ways | Find minimum |
| Operator | `+` | `+` | `min()` |
| Base (start) | `1` | `1` (if no obstacle) | `grid[0][0]` |
| Base (invalid) | `0` | `0` | `float('inf')` |
| Default (tabulation) | `up=left=0` | `up=left=0` | `up=left=float('inf')` |
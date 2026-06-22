# Unique Paths in N×M Grid | DP Notes

**LeetCode ID:** 62  
**GFG Problem Name:** Count Unique Paths in a Grid  
**CSES:** Grid Paths #1638  
**Topic:** 2D Dynamic Programming  
**Pattern:** Count total number of ways → operator: `+`  

---

## The Problem

Given an `n×m` grid, find the total number of unique paths from `mat[0][0]` (top-left) to `mat[n-1][m-1]` (bottom-right).

**Allowed moves:** Only **right** or **down** at any point.

**Example:**
```
3×3 grid:

S  →  →
↓  ↓  ↓
→  →  E

S = start (0,0)
E = end (2,2)

Answer = 6 unique paths
```

---

## Understanding Rows and Columns (Never Forget This)

This was confusing so let's be very clear:

```
        j=0  j=1  j=2   ← j increases going RIGHT
       ┌────┬────┬────┐
i=0   │    │    │    │  ← ROW 0 (horizontal line)
       ├────┼────┼────┤
i=1   │    │    │    │  ← ROW 1
       ├────┼────┼────┤
i=2   │    │    │    │  ← ROW 2
       └────┴────┴────┘
  ↑
COL 0 (vertical line)
i increases going DOWN
```

- `i` = **row number** → increases going **DOWN**
- `j` = **column number** → increases going **RIGHT**
- `n` = total number of rows
- `m` = total number of columns
- `mat[i][j]` → first index = row, second index = column (always!)

**Movements:**
- `i+1` = move to next row = go **DOWN**
- `j+1` = move to next column = go **RIGHT**
- `i-1` = came from **above**
- `j-1` = came from **left**

---

## Step 1 — Identify it as DP

**Is it recursive?** Yes — at each cell, you make a choice (came from above or from left).

**Keyword:** Count total number of **unique paths** → **`+`** operator → DP!

---

## Step 2 — Define f(i, j)

> **f(i, j) = number of ways to reach cell (i, j) from (0, 0)**

Final answer = `f(n-1, m-1)`

**Thinking direction:** Backward — at cell `(i, j)`, ask "where did I come from?"

---

## Step 3 — Build the Recurrence

At cell `(i, j)`, you could have arrived from:
- **Above** → `(i-1, j)` — number of ways = `f(i-1, j)`
- **Left** → `(i, j-1)` — number of ways = `f(i, j-1)`

Since keyword is **count total ways** → ADD both:

```
f(i, j) = f(i-1, j) + f(i, j-1)
```

---

## Step 4 — Base Cases

```python
if i == 0 and j == 0:
    return 1    # reached start — 1 valid path found

if i < 0 or j < 0:
    return 0    # out of bounds — invalid path
```

**Why `f(0,0) = 1`?**  
You're AT the starting cell — there's exactly 1 way to be here (the empty path). Same "empty path = 1" convention as LC #70 Climbing Stairs.

**Why out of bounds = 0?**  
You fell off the grid — not a valid path.

---

## Step 5 — Complete Recurrence Summary

```
f(0, 0) = 1
f(i, j) = 0          if i < 0 or j < 0
f(i, j) = f(i-1, j) + f(i, j-1)    for all other cells

answer = f(n-1, m-1)
```

---

## Step 6 — Recursive Solution

```python
def UniquePaths(i, j):
    # Base case — reached start
    if i == 0 and j == 0:
        return 1
    # Base case — out of bounds
    if i < 0 or j < 0:
        return 0

    left = UniquePaths(i, j - 1)   # came from left
    up   = UniquePaths(i - 1, j)   # came from above

    return left + up

# Call
print(UniquePaths(n - 1, m - 1))
```

**Problem:** Overlapping subproblems — same `(i, j)` cells get recomputed multiple times → O(2^(n*m))

---

## Step 7 — Memoization (Top-Down)

**"Top-down"** means: start from the big problem `f(n-1, m-1)` and recurse down to the base case `f(0,0)`.

> ⚠️ "Top-down" refers to problem size — NOT grid direction. `(n-1, m-1)` is the bottom-right of the grid but it's the "top" of the problem (the answer we want).

**3 moves as always:**
1. Initialize `dp[n][m]` with `-1`
2. Check `dp[i][j] != -1` → return it
3. Store result in `dp[i][j]` before returning

```python
def UniquePaths(i, j, dp):
    # Base cases
    if i == 0 and j == 0:
        return 1
    if i < 0 or j < 0:
        return 0

    # Check
    if dp[i][j] != -1:
        return dp[i][j]

    # Compute
    left = UniquePaths(i, j - 1, dp)
    up   = UniquePaths(i - 1, j, dp)

    # Store and return
    dp[i][j] = left + up
    return dp[i][j]

# Setup and call
n, m = 3, 3
dp = [[-1] * m for _ in range(n)]
print(UniquePaths(n - 1, m - 1, dp))
```

**Time complexity: O(n × m)** — every cell computed exactly once.  
**Space complexity: O(n × m)** — dp array + recursion stack.

---

## Step 8 — Tabulation (Bottom-Up)

**"Bottom-up"** means: start from the base case `(0,0)` and build up to `(n-1, m-1)` using loops. No recursion at all.

### Base cases in tabulation:
- First row: only 1 way to reach any cell → `dp[0][j] = 1`
- First column: only 1 way to reach any cell → `dp[i][0] = 1`

**Why?** In the first row, you can only come from the left (can't come from above — no row above). So there's exactly 1 path to every cell in row 0. Same logic for first column.

### Elegant single-loop approach:
Instead of separately filling first row and column, handle everything in one loop:

```python
dp = [[-1] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            dp[0][0] = 1          # start cell
        else:
            left = up = 0
            if j > 0: left = dp[i][j - 1]   # came from left
            if i > 0: up   = dp[i - 1][j]   # came from above
            dp[i][j] = left + up

return dp[n - 1][m - 1]
```

**Why check `if j > 0` and `if i > 0`?**  
Because cells in the first row have no cell above them (`i-1` would be -1).  
Cells in the first column have no cell to their left (`j-1` would be -1).  
The checks prevent out-of-bounds access.

---

## Dry Run (3×3 Grid)

```
n=3, m=3
```

**Fill order (row by row, left to right):**

```
i=0, j=0: dp[0][0] = 1   (start)
i=0, j=1: left=dp[0][0]=1, up=0  → dp[0][1] = 1
i=0, j=2: left=dp[0][1]=1, up=0  → dp[0][2] = 1

i=1, j=0: left=0, up=dp[0][0]=1  → dp[1][0] = 1
i=1, j=1: left=dp[1][0]=1, up=dp[0][1]=1 → dp[1][1] = 2
i=1, j=2: left=dp[1][1]=2, up=dp[0][2]=1 → dp[1][2] = 3

i=2, j=0: left=0, up=dp[1][0]=1  → dp[2][0] = 1
i=2, j=1: left=dp[2][0]=1, up=dp[1][1]=2 → dp[2][1] = 3
i=2, j=2: left=dp[2][1]=3, up=dp[1][2]=3 → dp[2][2] = 6
```

**Final dp table:**
```
      j=0  j=1  j=2
i=0 [  1,   1,   1 ]
i=1 [  1,   2,   3 ]
i=2 [  1,   3,   6 ]
```

**Return `dp[2][2]` = 6 ✅**

Notice the pattern — each cell is just the sum of the cell above and the cell to its left. Beautiful!

---

## Complete Solution

```python
class Solution:
    def uniquePaths(self, n: int, m: int) -> int:
        dp = [[-1] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    dp[0][0] = 1
                else:
                    left = up = 0
                    if j > 0: left = dp[i][j - 1]
                    if i > 0: up   = dp[i - 1][j]
                    dp[i][j] = left + up

        return dp[n - 1][m - 1]
```

---

## Time and Space Complexity

| | Recursion | Memoization | Tabulation |
|---|---|---|---|
| Time | O(2^(n×m)) | O(n×m) | O(n×m) |
| Space | O(n+m) stack | O(n×m) + stack | O(n×m) |

---

## Key Mental Notes

### On rows and columns
- Rows = horizontal, indexed by `i`, increase going DOWN
- Columns = vertical, indexed by `j`, increase going RIGHT
- `mat[i][j]` → always row first, column second

### On the recurrence
At every cell, you could have come from above or from left → add both.  
This is the standard 2D grid DP recurrence — you'll see it in almost every grid problem.

### On base cases
- `(0,0)` = 1 (start — empty path counts as 1 way)
- Out of bounds = 0 (invalid)
- First row = all 1s (only one way — keep going right)
- First column = all 1s (only one way — keep going down)

### On top-down vs bottom-up
These terms refer to **problem size**, not grid direction:
- Top-down = start from answer, recurse to base case
- Bottom-up = start from base case, build to answer

### The elegant single-loop trick
Instead of separately initializing first row and column, use `if j > 0` and `if i > 0` guards inside the main loop. Cleaner code, same result.

---
# Unique Paths II — Maze with Obstacles | Addendum Notes

**LeetCode ID:** 63  
**GFG Problem Name:** Unique Paths in a Grid with Obstacles  
**Base problem:** LC #62 Unique Paths (99% identical — read those notes first)

---

## What's Different from LC #62?

Only **one extra condition** — if a cell has an obstacle (`mat[i][j] == 1`), return `0` (can't pass through).

Everything else — recurrence, dp size, logic — is identical.

---

## Changes in Each Phase

### Recursive Solution
Add one extra base case:
```python
if mat[i][j] == 1:
    return 0
```

⚠️ Order matters — check out of bounds BEFORE accessing `mat[i][j]`:
```python
def UniquePaths(i, j, mat):
    if (i == 0 and j == 0) and mat[i][j] != 1:
        return 1
    if (i < 0 or j < 0) or mat[i][j] == 1:   # out of bounds first, then obstacle
        return 0
    left = UniquePaths(i, j-1, mat)
    up   = UniquePaths(i-1, j, mat)
    return left + up
```

> 💡 Python short-circuits `or` left to right — so `i < 0 or j < 0` is checked before `mat[i][j]`. No crash.

### Memoization
Identical to LC #62 — just add `mat` as parameter and the obstacle check in base cases.

```python
def UniquePaths(i, j, dp, mat):
    if (i == 0 and j == 0) and mat[i][j] != 1:
        return 1
    if (i < 0 or j < 0) or mat[i][j] == 1:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    left = UniquePaths(i, j-1, dp, mat)
    up   = UniquePaths(i-1, j, dp, mat)
    dp[i][j] = left + up
    return dp[i][j]

dp = [[-1] * m for _ in range(n)]
print(UniquePaths(n-1, m-1, dp, mat))
```

### Tabulation
Use `if/elif/else` — critical to avoid overwriting obstacle cells:

```python
dp = [[-1] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if mat[i][j] == 1:        # obstacle → always 0
            dp[i][j] = 0
        elif i == 0 and j == 0:   # start cell
            dp[i][j] = 1
        else:                      # normal cell
            left = up = 0
            if j > 0: left = dp[i][j-1]
            if i > 0: up   = dp[i-1][j]
            dp[i][j] = left + up

return dp[n-1][m-1]
```

> ⚠️ Common bug: using separate `if` instead of `elif` — the obstacle sets `dp[i][j] = 0` but then the `else` block overwrites it with `left + up`. Always use `if/elif/else` here.





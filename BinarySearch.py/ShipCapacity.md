```
def func(weights: list[int] , capacity : int) -> int:
    load = 0
    days = 1
    for i in range(len(weights)):
        if load + weights[i] > capacity:
            days += 1
            load = weights[i]
        else:
            load += weights[i]
    return days
def shipWithinDays(weights: List[int], days: int) -> int:
    low = max(weights)
    high = sum(weights)
    ans = sum(weights)

    while low <= high:
        mid = (low+high) // 2
        if func(weights , mid) > days:
            low = mid + 1
        else:
            ans = mid
            high = mid -1
    return ans
```
# Capacity To Ship Packages Within D Days 
---

## PART 1 — Understanding the Problem

You have packages with weights. A ship has a fixed capacity. Every day you load packages **in order** (no skipping, no reordering). Find the **minimum capacity** to ship everything within `days` days.

```
weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
days = 5
```

```
capacity=15:
Day 1: 1+2+3+4+5 = 15 ✅ (adding 6 would make 21 > 15, so stop)
Day 2: 6+7       = 13 ✅ (adding 8 would make 21 > 15, so stop)
Day 3: 8         = 8  ✅
Day 4: 9         = 9  ✅
Day 5: 10        = 10 ✅
→ Done in 5 days ✅

Answer = 15
```

---

## PART 2 — Why Binary Search? 🧠

As capacity increases → days needed decreases. Always monotonic:

```
capacity:     10   11  ...  14   15   16  ...  55
days needed:  ❌   ❌   ❌   ❌   ✅   ✅   ✅
```

**Always ❌❌❌✅✅✅** → Binary Search on Answer! 🎯

We are NOT searching the `weights` array. We are searching the **capacity range:**
- `low = max(weights)` → ship must carry at least the heaviest package
- `high = sum(weights)` → worst case, ship everything in 1 day

---

## PART 3 — The Code (Line by Line) 💻

### Helper Function: `func`

```python
def func(weights: list[int], capacity: int) -> int:
```
> Helper function. Given a capacity, simulate the loading process and return how many days it takes.

---

```python
    load = 0
    days = 1
```
> `load` → current day's total weight loaded so far
> `days` → number of days used so far (start at 1, not 0!)
> We start at day 1 because we always have at least one day of loading.

---

```python
    for i in range(len(weights)):
```
> Go through every package one by one in order (order must be maintained!).

---

```python
        if load + weights[i] > capacity:
```
> If adding this package to today's load **exceeds** capacity...
> Note: `>` not `>=` — if it equals capacity exactly, it still fits! ✅

---

```python
            days += 1
            load = weights[i]
```
> ...start a new day!
> Increment days counter.
> Reset load to just this package (it goes on the new day).

---

```python
        else:
            load += weights[i]
```
> Package fits → just add it to today's load. No new day needed.

---

```python
    return days
```
> Return total days needed for this capacity.

---

### Main Function: `shipWithinDays`

```python
def shipWithinDays(weights: List[int], days: int) -> int:
```
> Main function. Returns minimum capacity to ship within `days` days.

---

```python
    low = max(weights)
    high = sum(weights)
```
> Binary search range for capacity.
> `low = max(weights)` → ship MUST be able to carry the heaviest single package. If capacity < max(weights), we can never ship that package at all!
> `high = sum(weights)` → if capacity = total weight, everything ships in 1 day. No need to go higher.

---

```python
    ans = sum(weights)
```
> Default answer = worst case capacity (sum of all weights).
> We'll keep updating this as we find smaller valid capacities.

---

```python
    while low <= high:
```
> Keep searching while window is valid.

---

```python
        mid = (low + high) // 2
```
> Pick the middle capacity of current search window.
> We're testing: "can we ship everything in `days` days with capacity = `mid`?"

---

```python
        if func(weights, mid) > days:
            low = mid + 1
```
> If days needed with capacity `mid` is MORE than allowed days...
> → capacity is too small → need bigger capacity → go RIGHT.

---

```python
        else:
            ans = mid
            high = mid - 1
```
> If days needed is WITHIN allowed days...
> → this capacity works! Save it as current best answer.
> → try even smaller capacity → go LEFT.

---

```python
    return ans
```
> Return the minimum valid capacity found.

---

## PART 4 — Detailed Dry Run 🔍

```
weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
days = 5
```

### Setup:
```python
low  = max(weights) = 10
high = sum(weights) = 55
ans  = 55
```

```
Capacity range: [10, 11, 12, ... , 55]
                  ↑                 ↑
                 low               high
```

---

### Iteration 1:

```python
mid = (10 + 55) // 2 = 32
```

**func(weights, 32):**
```
load=0, days=1

i=0: load+1=1   <= 32 → load=1
i=1: load+2=3   <= 32 → load=3
i=2: load+3=6   <= 32 → load=6
i=3: load+4=10  <= 32 → load=10
i=4: load+5=15  <= 32 → load=15
i=5: load+6=21  <= 32 → load=21
i=6: load+7=28  <= 32 → load=28
i=7: load+8=36  > 32  → days=2, load=8
i=8: load+9=17  <= 32 → load=17
i=9: load+10=27 <= 32 → load=27

return days = 2
```

```python
func returns 2
2 > 5? → FALSE
→ ans = 32, high = 31
```

```
low=10, high=31, ans=32
```

---

### Iteration 2:

```python
mid = (10 + 31) // 2 = 20
```

**func(weights, 20):**
```
load=0, days=1

i=0:  1  → load=1
i=1:  3  → load=3
i=2:  6  → load=6
i=3:  10 → load=10
i=4:  15 → load=15
i=5:  21 > 20 → days=2, load=6
i=6:  13 → load=13
i=7:  21 > 20 → days=3, load=8
i=8:  17 → load=17
i=9:  27 > 20 → days=4, load=10

return days = 4
```

```python
4 > 5? → FALSE
→ ans = 20, high = 19
```

```
low=10, high=19, ans=20
```

---

### Iteration 3:

```python
mid = (10 + 19) // 2 = 14
```

**func(weights, 14):**
```
load=0, days=1

i=0:  1  → load=1
i=1:  3  → load=3
i=2:  6  → load=6
i=3:  10 → load=10
i=4:  15 > 14 → days=2, load=5
i=5:  11 → load=11
i=6:  18 > 14 → days=3, load=7
i=7:  15 > 14 → days=4, load=8
i=8:  17 > 14 → days=5, load=9
i=9:  19 > 14 → days=6, load=10

return days = 6
```

```python
6 > 5? → TRUE
→ low = 14 + 1 = 15
```

```
low=15, high=19, ans=20
```

---

### Iteration 4:

```python
mid = (15 + 19) // 2 = 17
```

**func(weights, 17):**
```
load=0, days=1

i=0:  1  → load=1
i=1:  3  → load=3
i=2:  6  → load=6
i=3:  10 → load=10
i=4:  15 → load=15
i=5:  21 > 17 → days=2, load=6
i=6:  13 → load=13
i=7:  21 > 17 → days=3, load=8
i=8:  17 → load=17
i=9:  27 > 17 → days=4, load=10

return days = 4
```

```python
4 > 5? → FALSE
→ ans = 17, high = 16
```

```
low=15, high=16, ans=17
```

---

### Iteration 5:

```python
mid = (15 + 16) // 2 = 15
```

**func(weights, 15):**
```
load=0, days=1

i=0:  1  → load=1
i=1:  3  → load=3
i=2:  6  → load=6
i=3:  10 → load=10
i=4:  15 → load=15
i=5:  21 > 15 → days=2, load=6
i=6:  13 → load=13
i=7:  20 > 15 → days=3, load=8
i=8:  17 > 15 → days=4, load=9
i=9:  19 > 15 → days=5, load=10

return days = 5
```

```python
5 > 5? → FALSE
→ ans = 15, high = 14
```

```
low=15, high=14 → low > high → STOP ❌
```

---

### Final Answer:
```python
return ans = 15 ✅
```

---

## PART 5 — Summary Table

| Iteration | low | high | mid | days needed | Valid? | Action |
|---|---|---|---|---|---|---|
| 1 | 10 | 55 | 32 | 2 | ✅ | ans=32, high=31 |
| 2 | 10 | 31 | 20 | 4 | ✅ | ans=20, high=19 |
| 3 | 10 | 19 | 14 | 6 | ❌ | low=15 |
| 4 | 15 | 19 | 17 | 4 | ✅ | ans=17, high=16 |
| 5 | 15 | 16 | 15 | 5 | ✅ | ans=15, high=14 |
| - | 15 | 14 | - | - | STOP | return 15 |

---

## PART 6 — The Universal Binary Search on Answer Template 🧠

```python
low  = minimum possible answer
high = maximum possible answer
ans  = high   # default worst case

while low <= high:
    mid = (low + high) // 2
    if helper(mid) satisfies condition:
        ans = mid          # save it
        high = mid - 1     # try smaller
    else:
        low = mid + 1      # try larger

return ans
```


---

## PART 7 — Complexity

| | Complexity |
|---|---|
| **Time** | O(n × log(sum(weights))) |
| **Space** | O(1) |



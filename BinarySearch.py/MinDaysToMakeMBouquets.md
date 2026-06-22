### Brute Force
```
def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
    if m*k > len(bloomDay): return -1
    n = len(bloomDay)
    for day in range(min(bloomDay) , max(bloomDay)+1):
        count = 0
        Bouquets = 0
        for i in range(n):
            if bloomDay[i] <= day:
                count += 1
                if count == k:
                    Bouquets += 1
                    count = 0
        if Bouquets >= m:
            return day
    return -1
```
### Binary Search ###
```
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay): return -1
        def canMake(bloomDay , mid , m , k):
            count = 0
            bouquet = 0
            for i in range(len(bloomDay)):
                if bloomDay[i] <= mid:
                    count +=1
                    if count == k:
                        bouquet += 1
                        count = 0
                else:
                    count = 0
            if bouquet >= m:
                return True
            return False

            
        ans = max(bloomDay)
        low = min(bloomDay)
        high = max(bloomDay)
        while low <= high:
            mid = (low + high) // 2
            if canMake(bloomDay , mid , m , k) == True:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans  
```

# Minimum Number of Days to Make M Bouquets 📝

**LeetCode #1482** | **GFG: Minimum Days to Make M Bouquets**

---

## PART 1 — Understanding the Problem

You have `n` flowers. Each flower blooms on a certain day.
You need `m` bouquets, each bouquet needs `k` **adjacent** bloomed flowers.

```
bloomDay = [7, 7, 7, 7, 12, 7, 7]
m = 2   → need 2 bouquets
k = 3   → each bouquet needs 3 adjacent flowers
```

```
Day 7:  [x, x, x, x, _, x, x]
         -------        ----
         3 adjacent   only 2 → can't make bouquet
         = 1 bouquet ❌

Day 12: [x, x, x, x, x, x, x]
         -------  -------
         bouquet1  bouquet2
         = 2 bouquets ✅
```

Answer = **12**

---

## PART 2 — Why Binary Search? 🧠

The key observation is:

> If day `X` is enough to make m bouquets,
> then day `X+1` is ALSO enough (more flowers bloom = easier)

So the pattern of days looks like:

```
Day:  1   2  ... 7   8  ... 12  13  14
      ❌  ❌   ❌  ❌    ✅   ✅   ✅
```

**All ❌ first, then all ✅ — this is monotonic!**

This means we can Binary Search on the **day numbers** themselves (not the bloomDay array!) from `min(bloomDay)` to `max(bloomDay)`.

We ask: **"Is day `mid` enough?"**
- If YES → save it, try smaller days (go left)
- If NO → try bigger days (go right)

---

## PART 3 — The Two Functions Explained

### Function 1: `canMake(bloomDay, mid, m, k)`

**Purpose:** Given that `mid` days have passed, can we make `m` bouquets of `k` adjacent flowers?

```python
def canMake(bloomDay, mid, m, k):
```
> Define helper function. Takes the bloom schedule, the day we're checking, and m, k.

---

```python
    count = 0
    bouqets = 0
```
> `count` → tracks current streak of adjacent bloomed flowers
> `bouqets` → tracks how many bouquets we've completed so far

---

```python
    for i in range(len(bloomDay)):
```
> Go through every flower one by one from left to right.

---

```python
        if bloomDay[i] <= mid:
            count += 1
```
> If this flower has bloomed by day `mid` → add it to current streak.
> If NOT bloomed → we do nothing (streak breaks implicitly below via reset).

---

```python
            if count == k:
                bouqets += 1
                count = 0
```
> If we've collected `k` adjacent bloomed flowers → we have a bouquet!
> Increment bouquet count and **reset streak to 0** to start counting the next bouquet.

---

```python
        else:
            count = 0
```

Wait — this is actually **missing from your code!** 😮

If a flower hasn't bloomed, the streak **must break**. Without this, you'd count non-adjacent flowers as adjacent!

Add this:
```python
        if bloomDay[i] <= mid:
            count += 1
            if count == k:
                bouqets += 1
                count = 0
        else:
            count = 0   # ← streak breaks!
```

---

```python
    if bouqets >= m:
        return True
    return False
```
> After checking all flowers — did we make enough bouquets?
> If yes → return True. If no → return False.

---

### Function 2: `minDays(bloomDay, m, k)`

```python
def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
```
> Main function. Returns the minimum day, or -1 if impossible.

---

```python
    if m * k > len(bloomDay):
        return -1
```
> **Impossible check.** We need `m × k` flowers total minimum.
> If the array doesn't even have that many flowers → impossible → return -1 immediately.

---

```python
    low = min(bloomDay)
    high = max(bloomDay)
```
> Set up binary search range.
> `low` = earliest possible day (smallest bloom day)
> `high` = latest possible day (largest bloom day)
> We're searching on THIS range of days, NOT on the bloomDay array!

---

```python
    ans = max(bloomDay)
```
> Default answer = last possible day.
> We'll keep updating this as we find smaller valid days.

---

```python
    while low <= high:
```
> Keep searching while window is valid.

---

```python
        mid = (low + high) // 2
```
> Pick middle day of current search window.

---

```python
        if canMake(bloomDay, mid, m, k):
            ans = mid        # save this day as potential answer
            high = mid - 1   # try to find an even smaller day
```
> If `mid` days is enough → save it as current best answer.
> Then search LEFT (smaller days) — maybe we can do it in fewer days!

---

```python
        else:
            low = mid + 1   # need more days → search RIGHT
```
> If `mid` days is NOT enough → we need more days → go right.

---

```python
    return ans
```
> Return the minimum day we found.

---

## PART 4 — Detailed Dry Run 🔍

```
bloomDay = [7, 7, 7, 7, 12, 7, 7]
m = 2, k = 3
n = 7
```

### Impossible check:
```python
m * k = 2 * 3 = 6
len(bloomDay) = 7
6 > 7? → NO → continue ✅
```

### Setup:
```python
low = min(bloomDay) = 7
high = max(bloomDay) = 12
ans = 12
```

```
Day range: [7, 8, 9, 10, 11, 12]
            ↑                 ↑
           low               high
```

---

### Binary Search Iteration 1:

```python
mid = (7 + 12) // 2 = 9
```

**canMake(bloomDay, 9, 2, 3):**
```
bloomDay = [7,  7,  7,  7,  12,  7,  7]
day 9?     [✅, ✅, ✅, ✅,  ❌, ✅, ✅]

i=0: bloomDay[0]=7 <= 9 → count=1
i=1: bloomDay[1]=7 <= 9 → count=2
i=2: bloomDay[2]=7 <= 9 → count=3 → count==k! → bouquets=1, count=0
i=3: bloomDay[3]=7 <= 9 → count=1
i=4: bloomDay[4]=12 <= 9? NO → count=0 (streak breaks!)
i=5: bloomDay[5]=7 <= 9 → count=1
i=6: bloomDay[6]=7 <= 9 → count=2

bouquets=1 >= m=2? → FALSE → return False
```

```python
canMake = False → low = mid + 1 = 10
```

```
low=10, high=12, ans=12
```

---

### Binary Search Iteration 2:

```python
mid = (10 + 12) // 2 = 11
```

**canMake(bloomDay, 11, 2, 3):**
```
bloomDay = [7,  7,  7,  7,  12,  7,  7]
day 11?    [✅, ✅, ✅, ✅,  ❌, ✅, ✅]

i=0: count=1
i=1: count=2
i=2: count=3 → bouquets=1, count=0
i=3: count=1
i=4: 12 <= 11? NO → count=0
i=5: count=1
i=6: count=2

bouquets=1 >= 2? → FALSE → return False
```

```python
canMake = False → low = mid + 1 = 12
```

```
low=12, high=12, ans=12
```

---

### Binary Search Iteration 3:

```python
mid = (12 + 12) // 2 = 12
```

**canMake(bloomDay, 12, 2, 3):**
```
bloomDay = [7,  7,  7,  7,  12,  7,  7]
day 12?    [✅, ✅, ✅, ✅,  ✅, ✅, ✅]

i=0: count=1
i=1: count=2
i=2: count=3 → bouquets=1, count=0
i=3: count=1
i=4: 12<=12 ✅ → count=2
i=5: count=3 → bouquets=2, count=0
i=6: count=1

bouquets=2 >= 2? → TRUE → return True ✅
```

```python
canMake = True → ans = 12, high = mid - 1 = 11
```

```
low=12, high=11 → low > high → STOP
```

---

### Final Answer:
```python
return ans = 12 ✅
```

---

## PART 5 — Summary Table

| Iteration | low | high | mid | canMake? | Action |
|---|---|---|---|---|---|
| 1 | 7 | 12 | 9 | ❌ | low = 10 |
| 2 | 10 | 12 | 11 | ❌ | low = 12 |
| 3 | 12 | 12 | 12 | ✅ | ans=12, high=11 |

---

## PART 6 — The Bug to Remember ⚠️

Always reset `count = 0` when a flower hasn't bloomed:

```python
if bloomDay[i] <= mid:
    count += 1
    if count == k:
        bouquets += 1
        count = 0
else:
    count = 0   # ← DON'T forget this!
```

Without this, non-adjacent flowers get counted as adjacent!

---

## PART 7 — Complexity

| | Brute Force | Binary Search |
|---|---|---|
| Time | O(n × maxDay) | O(n × log(maxDay)) |
| Space | O(1) | O(1) |

If `maxDay = 10^9`:
- Brute force → **10^14** operations 😱
- Binary search → **30 × n** operations ✅

---

## PART 8 — The Core Pattern to Remember

> **Binary Search on Answer** — when the answer has a ❌❌❌✅✅✅ monotonic pattern, don't search the array — search the **answer space** itself!

🚀
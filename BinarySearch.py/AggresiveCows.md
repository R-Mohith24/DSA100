```
Given an array nums of size n, which denotes the positions of stalls,
and an integer k,which denotes the number of aggressive cows,
assign stalls to k cows such that the minimum distance between
any two cows is the maximum possible.Find the maximum possible minimum distance.

```

```
def canPlace(arr,dist,cows):
    n = len(arr)
    count = 1
    last_placed_cow = arr[0]
    for i in range(1,n):
        if arr[i] - last_placed_cow >= dist:
            count += 1
            last_placed_cow = arr[i]

    if count >= cows:
        return True
    return False

```
```
def aggressiveCows(self, stalls, k):
    stalls.sort()
    n = len(stalls)
    low = 1
    high = stalls[n-1] - stalls[0] 
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if canPlace(stalls , mid , k) == True:
            ans = mid
            low = mid + 1

        else:
            high = mid -1
    return ans
```

```

The pattern is:
- **Minimize** the answer → when valid, go **LEFT**
- **Maximize** the answer → when valid, go **RIGHT**

Lock this in your brain forever! 🔐

---

Now dry run time! 😄

```
stalls = [1, 2, 4, 8, 9]
k = 3
```

### Setup:
```python
stalls.sort() → [1, 2, 4, 8, 9]
low = 1
high = 9 - 1 = 8
ans = -1
```

```
Distance range: [1, 2, 3, 4, 5, 6, 7, 8]
                 ↑                    ↑
                low                  high
```

---

### Iteration 1:
```python
mid = (1 + 8) // 2 = 4
```

**canPlace(stalls, 4, 3):**
```
arr = [1, 2, 4, 8, 9]
last = 1, count = 1

i=1: arr[1]=2,  2-1=1  >= 4? ❌
i=2: arr[2]=4,  4-1=3  >= 4? ❌
i=3: arr[3]=8,  8-1=7  >= 4? ✅ → count=2, last=8
i=4: arr[4]=9,  9-8=1  >= 4? ❌

count=2 >= 3? ❌ → return False
```

```python
high = mid - 1 = 3
```
```
low=1, high=3, ans=-1
```

---

### Iteration 2:
```python
mid = (1 + 3) // 2 = 2
```

**canPlace(stalls, 2, 3):**
```
arr = [1, 2, 4, 8, 9]
last = 1, count = 1

i=1: 2-1=1  >= 2? ❌
i=2: 4-1=3  >= 2? ✅ → count=2, last=4
i=3: 8-4=4  >= 2? ✅ → count=3, last=8
i=4: 9-8=1  >= 2? ❌

count=3 >= 3? ✅ → return True
```

```python
ans = 2
low = mid + 1 = 3
```
```
low=3, high=3, ans=2
```

---

### Iteration 3:
```python
mid = (3 + 3) // 2 = 3
```

**canPlace(stalls, 3, 3):**
```
arr = [1, 2, 4, 8, 9]
last = 1, count = 1

i=1: 2-1=1  >= 3? ❌
i=2: 4-1=3  >= 3? ✅ → count=2, last=4
i=3: 8-4=4  >= 3? ✅ → count=3, last=8
i=4: 9-8=1  >= 3? ❌

count=3 >= 3? ✅ → return True
```

```python
ans = 3
low = mid + 1 = 4
```
```
low=4, high=3 → low > high → STOP ❌
```

---

### Final Answer:
```python
return ans = 3 ✅
```

---

## Summary Table

| Iteration | low | high | mid | canPlace? | Action |
|---|---|---|---|---|---|
| 1 | 1 | 8 | 4 | ❌ | high=3 |
| 2 | 1 | 3 | 2 | ✅ | ans=2, low=3 |
| 3 | 3 | 3 | 3 | ✅ | ans=3, low=4 |
| - | 4 | 3 | - | STOP | return 3 |

---

## The Golden Rule 🔐

```
MINIMIZE answer → valid means try SMALLER → high = mid - 1
MAXIMIZE answer → valid means try LARGER  → low  = mid + 1
```

| Problem | Goal | When Valid |
|---|---|---|
| Bouquets | Minimize days | high = mid - 1 |
| Smallest Divisor | Minimize divisor | high = mid - 1 |
| Ship Packages | Minimize capacity | high = mid - 1 |
| Aggressive Cows | **Maximize** distance | **low = mid + 1** |

🚀
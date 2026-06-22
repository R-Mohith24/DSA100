```
class Solution:
    def find(self, arr, x):
        n = len(arr)
        
        def lower_bound(arr, x):
            low, high = 0, len(arr) - 1
            ans = len(arr)   # default if not found
        
            while low <= high:
                mid = (low + high) // 2
        
                if arr[mid] >= x:
                    ans = mid
                    high = mid - 1   # go left
                else:
                    low = mid + 1    # go right
        
            return ans


        def upper_bound(arr, x):
            low, high = 0, len(arr) - 1
            ans = len(arr)   # default if not found
        
            while low <= high:
                mid = (low + high) // 2
        
                if arr[mid] > x:
                    ans = mid
                    high = mid - 1   # go left
                else:
                    low = mid + 1    # go right
        
            return ans
        lowBound = lower_bound(arr,x)
        if lowBound == n or arr[lowBound] != x:
            return [-1,-1]
        return [lowBound , upper_bound(arr,x) - 1]
```

Let's do it! Full detailed dry run. 🔥

---

## Setup

```python
arr = [1, 3, 5, 5, 5, 5, 8, 10]
x = 5
n = 8
```

```
Index:  0  1  2  3  4  5  6   7
arr  : [1, 3, 5, 5, 5, 5, 8, 10]
```

---

## PART 1 — `lower_bound(arr, 5)`

**Goal:** Find first index where `arr[mid] >= 5`

```python
low, high = 0, len(arr) - 1
ans = len(arr)
```
```
low = 0, high = 7, ans = 8
```

---

### Iteration 1

```python
mid = (low + high) // 2
```
```
mid = (0 + 7) // 2 = 3
```

```
Index:  0  1  2  [3]  4  5  6   7
arr  : [1, 3, 5,  5,  5, 5, 8, 10]
                  ^
                 mid
```

```python
if arr[mid] >= target:   # arr[3] = 5 >= 5 → TRUE
    ans = mid            # ans = 3
    high = mid - 1       # high = 2   → go LEFT
```
```
low=0, high=2, ans=3
```

---

### Iteration 2

```python
mid = (0 + 2) // 2 = 1
```

```
Index:  0  [1]  2  3  4  5  6   7
arr  : [1,  3,  5, 5, 5, 5, 8, 10]
            ^
           mid
```

```python
if arr[mid] >= target:   # arr[1] = 3 >= 5 → FALSE
    ...
else:
    low = mid + 1        # low = 2   → go RIGHT
```
```
low=2, high=2, ans=3
```

---

### Iteration 3

```python
mid = (2 + 2) // 2 = 2
```

```
Index:  0  1  [2]  3  4  5  6   7
arr  : [1, 3,  5,  5, 5, 5, 8, 10]
               ^
              mid
```

```python
if arr[mid] >= target:   # arr[2] = 5 >= 5 → TRUE
    ans = mid            # ans = 2  ← updated!
    high = mid - 1       # high = 1 → go LEFT
```
```
low=2, high=1, ans=2
```

---

### Loop Check
```
low=2 > high=1 → STOP
```

```python
return ans   # returns 2
```

✅ `lower_bound` returns **2** → first occurrence of 5 is at index 2

---

## PART 2 — `upper_bound(arr, 5)`

**Goal:** Find first index where `arr[mid] > 5`

```python
low, high = 0, 7
ans = 8
```

---

### Iteration 1

```python
mid = (0 + 7) // 2 = 3
```

```
Index:  0  1  2  [3]  4  5  6   7
arr  : [1, 3, 5,  5,  5, 5, 8, 10]
                  ^
                 mid
```

```python
if arr[mid] > target:   # arr[3] = 5 > 5 → FALSE
    ...
else:
    low = mid + 1       # low = 4   → go RIGHT
```
```
low=4, high=7, ans=8
```

---

### Iteration 2

```python
mid = (4 + 7) // 2 = 5
```

```
Index:  0  1  2  3  4  [5]  6   7
arr  : [1, 3, 5, 5, 5,  5,  8, 10]
                        ^
                       mid
```

```python
if arr[mid] > target:   # arr[5] = 5 > 5 → FALSE
    ...
else:
    low = mid + 1       # low = 6   → go RIGHT
```
```
low=6, high=7, ans=8
```

---

### Iteration 3

```python
mid = (6 + 7) // 2 = 6
```

```
Index:  0  1  2  3  4  5  [6]   7
arr  : [1, 3, 5, 5, 5, 5,  8,  10]
                            ^
                           mid
```

```python
if arr[mid] > target:   # arr[6] = 8 > 5 → TRUE
    ans = mid           # ans = 6
    high = mid - 1      # high = 5  → go LEFT
```
```
low=6, high=5, ans=6
```

---

### Loop Check
```
low=6 > high=5 → STOP
```

```python
return ans   # returns 6
```

✅ `upper_bound` returns **6** → first index where element > 5

---

## PART 3 — Back in `find()`

```python
lowBound = lower_bound(arr, x)   # lowBound = 2
```

```python
if lowBound == n or arr[lowBound] != x:
# 2 == 8?  → FALSE
# arr[2] != 5? → FALSE
# Overall → FALSE → skip this block
```

```python
return [lowBound, upper_bound(arr, x) - 1]
# return [2, 6 - 1]
# return [2, 5]
```

---

## Final Answer

```
[2, 5]
```

```
Index:  0  1  [2]  3  4  [5]  6   7
arr  : [1, 3,  5,  5, 5,  5,  8, 10]
               ^            ^
             first         last
```

✅ **Correct!**

---

The beauty of this approach — **two clean binary searches, O(log n) each.** 🚀
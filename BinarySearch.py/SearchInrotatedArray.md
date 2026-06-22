```
class Solution:
    def search(self, arr: List[int], target: int) -> int:
        n = len(arr)
        low , high = 0 , n-1
        while low <= high:
            mid = (low+high) // 2
            if arr[mid] == target:
                return mid
            if arr[low] <= arr[mid]: #left half is sorted 
                if arr[low] <= target and target <= arr[mid]:
                    #the target element is present in the left half only
                    high = mid - 1
                else:
                    low = mid + 1
            else: #right half is sorted
                if arr[mid] <= target and target <= arr[high]:
                    # the target is present in the right half only
                    low = mid + 1
                else:
                    high = mid - 1
        return -1

```

---

## Setup

```python
arr = [4, 5, 6, 7, 1, 2, 3]
target = 1
n = 7
```

```
Index:  0  1  2  3  4  5  6
arr  : [4, 5, 6, 7, 1, 2, 3]
```

---

## Iteration 1

```python
low, high = 0, 6
```

```python
mid = (0 + 6) // 2
```
```
mid = 3
```

```
Index:  0  1  2  [3]  4  5  6
arr  : [4, 5, 6,  7,  1, 2, 3]
                  ^
                 mid
low=0                    high=6
```

```python
if arr[mid] == target:   # arr[3] = 7 == 1? → FALSE
```

```python
if arr[low] <= arr[mid]:   # arr[0]=4 <= arr[3]=7? → TRUE
```
✅ **Left half is sorted** → `[4, 5, 6, 7]`

```python
if arr[low] <= target and target <= arr[mid]:
# arr[0]=4 <= 1?  → FALSE
# condition fails immediately
```
❌ Target 1 is **NOT** in the left half range `[4...7]`

```python
else:
    low = mid + 1   # low = 4  → search RIGHT half
```

```
low=4, high=6, ans=?
```

---

## Iteration 2

```python
mid = (4 + 6) // 2
```
```
mid = 5
```

```
Index:  0  1  2  3  4  [5]  6
arr  : [4, 5, 6, 7, 1,  2,  3]
                        ^
                       mid
              low=4         high=6
```

```python
if arr[mid] == target:   # arr[5] = 2 == 1? → FALSE
```

```python
if arr[low] <= arr[mid]:   # arr[4]=1 <= arr[5]=2? → TRUE
```
✅ **Left half is sorted** → `[1, 2]`

```python
if arr[low] <= target and target <= arr[mid]:
# arr[4]=1 <= 1? → TRUE
# 1 <= arr[5]=2? → TRUE
# Overall → TRUE ✅
```
✅ Target **IS** in this range!

```python
high = mid - 1   # high = 4  → search LEFT
```

```
low=4, high=4
```

---

## Iteration 3

```python
mid = (4 + 4) // 2
```
```
mid = 4
```

```
Index:  0  1  2  3  [4]  5  6
arr  : [4, 5, 6, 7,  1,  2, 3]
                     ^
                    mid
             low=4 high=4
```

```python
if arr[mid] == target:   # arr[4] = 1 == 1? → TRUE ✅
    return mid           # return 4
```

---

## Final Answer

```
return 4
```

```
Index:  0  1  2  3  [4]  5  6
arr  : [4, 5, 6, 7,  1,  2, 3]
                     ^
                  FOUND! ✅
```

---

## Summary Table

| Iteration | low | high | mid | arr[mid] | Decision |
|---|---|---|---|---|---|
| 1 | 0 | 6 | 3 | 7 | Left sorted, target not in left → go RIGHT |
| 2 | 4 | 6 | 5 | 2 | Left sorted, target in left → go LEFT |
| 3 | 4 | 4 | 4 | 1 | **FOUND at index 4** ✅ |

---

## Why It Works 💡

The whole trick is — even though the full array isn't sorted, **one half is always sorted**. And a sorted half lets you do a simple range check `arr[low] <= target <= arr[mid]` to decide where to go.

Normal binary search: *"Is target left or right of mid?"*
This problem: *"Which half is sorted? Is target in that sorted half?"*

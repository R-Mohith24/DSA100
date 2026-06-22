```
def findPeakElement(nums: List[int]) -> int:
    n = len(nums)
    if n == 1:
        return 0
    if nums[0] > nums[1]:
        return  0
    if nums[n-1] > nums[n-2]:
        return n-1

    low , high = 1 , n - 2
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
            return mid
        elif nums[mid] > nums[mid-1]:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```
# Find Peak Element — Complete Notes 📝

**LeetCode #162** | **GFG: Peak Element in Array**

---

## PART 1 — What is a Peak Element?

A peak element is an element that is **strictly greater than both its neighbors**.

```
arr = [1, 2, 4, 5, 7, 8, 3]
idx =  0  1  2  3  4  5  6
```
```
arr[5] = 8 → left neighbor = 7, right neighbor = 3
8 > 7 ✅ and 8 > 3 ✅ → 8 is a PEAK
```

### Special boundary rule the problem gives us:
```
nums[-1] = -∞  (imaginary element before index 0)
nums[n]  = -∞  (imaginary element after last index)
```

This means:
- If `arr[0] > arr[1]` → first element is a peak (its left is -∞)
- If `arr[n-1] > arr[n-2]` → last element is a peak (its right is -∞)

---

## PART 2 — Why does Binary Search work here? 🧠

The array is NOT sorted. So how can we use Binary Search?

Because of this one golden rule:

> **If you are on an upward slope, a peak MUST exist in that direction.**

Think about it like a hill:

```
If values are going UP to the right:
1, 3, 5, ...
         → keep going right, you WILL hit a peak
           (because the array is finite, it must come down eventually)

If values are going DOWN to the right:
..., 5, 3, 1
 ↑
you're already on a downward slope
→ peak must be to the LEFT (or at current position)
```

So at every `mid`, we just ask:
> **"Which direction is uphill?"**

Then we go that way. We're guaranteed to find a peak. ✅

---

## PART 3 — The Code (Line by Line) 💻

```python
def findPeakElement(nums: List[int]) -> int:
```
> Define the function. Takes a list of integers, returns the **index** of a peak.

---

```python
    n = len(nums)
```
> Store length of array. Used for edge case checks below.

---

```python
    if n == 1:
        return 0
```
> Only one element in array. No neighbors exist.
> By the -∞ boundary rule, this single element is always a peak.
> Return index 0.

---

```python
    if nums[0] > nums[1]:
        return 0
```
> Check if the FIRST element is a peak.
> Its left neighbor is -∞ (always smaller).
> So we only need to check: is it greater than its RIGHT neighbor?
> If yes → it's a peak → return index 0.

---

```python
    if nums[n-1] > nums[n-2]:
        return n-1
```
> Check if the LAST element is a peak.
> Its right neighbor is -∞ (always smaller).
> So we only need to check: is it greater than its LEFT neighbor?
> If yes → it's a peak → return index n-1.

---

```python
    low, high = 1, n - 2
```
> We already handled index 0 and index n-1 above.
> So now we safely search between index 1 and n-2.
> Every element in this range has both a left AND right neighbor.

---

```python
    while low <= high:
```
> Keep searching while the window is valid (low hasn't crossed high).

---

```python
        mid = (low + high) // 2
```
> Find the middle index of current search window.

---

```python
        if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
            return mid
```
> Check if mid is a peak:
> Is it greater than RIGHT neighbor? → `nums[mid] > nums[mid+1]`
> Is it greater than LEFT neighbor? → `nums[mid] > nums[mid-1]`
> Both true? → `mid` is a peak → return its index immediately.

---

```python
        elif nums[mid] > nums[mid-1]:
            low = mid + 1
```
> `mid` is NOT a peak (didn't return above).
> But `arr[mid] > arr[mid-1]` means we are on an **upward slope going RIGHT**.
> This means: a peak MUST exist to the right.
> So eliminate the left half → move `low` to `mid + 1`.

---

```python
        else:
            high = mid - 1
```
> We're on a downward slope (or `arr[mid] < arr[mid-1]`).
> This means: a peak MUST exist to the left.
> So eliminate the right half → move `high` to `mid - 1`.

---

```python
    return -1
```
> Technically unreachable if input is valid.
> A peak always exists by the problem's guarantee.
> Just here as a safety return.

---

## PART 4 — Detailed Dry Run 🔍

```
arr = [1, 2, 4, 5, 7, 8, 3]
idx =  0  1  2  3  4  5  6
n = 7
```

### Edge Case Checks:

```python
n == 1?          # 7 == 1? → NO
nums[0] > nums[1]?  # 1 > 2? → NO
nums[6] > nums[5]?  # 3 > 8? → NO
```
> None of the edge cases trigger. Move to binary search.

```python
low, high = 1, 5
```
```
Index:  0  1  2  3  4  5  6
arr  : [1, 2, 4, 5, 7, 8, 3]
          ↑              ↑
         low            high
```

---

### Iteration 1:

```python
mid = (1 + 5) // 2 = 3
```

```
Index:  0  1  2  [3]  4  5  6
arr  : [1, 2, 4,  5,  7, 8, 3]
                  ^
                 mid
         low=1            high=5
```

```python
nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]?
# arr[3]=5 > arr[4]=7? → FALSE ❌
# Not a peak
```

```python
elif nums[mid] > nums[mid-1]?
# arr[3]=5 > arr[2]=4? → TRUE ✅
# We are on UPWARD slope going right
low = mid + 1 = 4
```

```
State: low=4, high=5
```

---

### Iteration 2:

```python
mid = (4 + 5) // 2 = 4
```

```
Index:  0  1  2  3  [4]  5  6
arr  : [1, 2, 4,  5,  7, 8, 3]
                     ^
                    mid
                  low=4  high=5
```

```python
nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]?
# arr[4]=7 > arr[5]=8? → FALSE ❌
# Not a peak
```

```python
elif nums[mid] > nums[mid-1]?
# arr[4]=7 > arr[3]=5? → TRUE ✅
# Still on UPWARD slope going right
low = mid + 1 = 5
```

```
State: low=5, high=5
```

---

### Iteration 3:

```python
mid = (5 + 5) // 2 = 5
```

```
Index:  0  1  2  3  4  [5]  6
arr  : [1, 2, 4, 5, 7,  8,  3]
                        ^
                       mid
                     low=5 high=5
```

```python
nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]?
# arr[5]=8 > arr[6]=3? → TRUE ✅
# arr[5]=8 > arr[4]=7? → TRUE ✅
# BOTH TRUE → arr[5] is a PEAK! 🎉
return 5
```

---

### Final Answer:
```
return 5
```
```
Index:  0  1  2  3  4  [5]  6
arr  : [1, 2, 4, 5, 7,  8,  3]
                        ^
                     PEAK ✅
```

---

## PART 5 — Summary Table

| Iteration | low | high | mid | arr[mid] | Decision |
|---|---|---|---|---|---|
| 1 | 1 | 5 | 3 | 5 | Upward slope → go RIGHT |
| 2 | 4 | 5 | 4 | 7 | Upward slope → go RIGHT |
| 3 | 5 | 5 | 5 | 8 | Peak found! ✅ |

---

## PART 6 — The Core Idea in One Line

> **Always move towards the uphill side — you WILL hit a peak because the array is finite and the boundaries are -∞.**

---

## Time & Space Complexity

| | Complexity |
|---|---|
| **Time** | O(log n) — binary search halves the search space each time |
| **Space** | O(1) — no extra data structures used |
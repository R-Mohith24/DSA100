Alright — now we’re doing the **real DSA upgrade** 🔥
I’ll make this so clear that you’ll **never forget it again**.

---

# 🧠 First — Intuition (don’t skip this)

We are given a **sorted + rotated array**:

```
[4,5,6,7,0,1,2]
```

👉 Key observation:

* Left half → sorted
* Right half → sorted
* BUT one side contains the **minimum (pivot)**

---

### 💡 Golden Rule

👉 Compare `nums[mid]` with `nums[high]`

* If `nums[mid] > nums[high]`
  → minimum is in **right half**

* Else
  → minimum is in **left half (including mid)**

---

# ✅ Code (SUPER SIMPLE + COMMENTED)

```python
class Solution:
    def findMin(self, nums):
        low = 0                      # start of array
        high = len(nums) - 1         # end of array

        while low < high:            # loop until they meet
            mid = (low + high) // 2  # find middle index

            # Case 1: mid element is greater than last element
            # → minimum must be on the RIGHT side
            if nums[mid] > nums[high]:
                low = mid + 1        # ignore left part

            # Case 2: mid element is smaller or equal
            # → minimum is on LEFT side (including mid)
            else:
                high = mid           # keep mid in search

        # when loop ends, low == high → minimum index
        return nums[low]
```

---

# 🔥 Dry Run (STEP BY STEP — VERY DETAILED)

### Input:

```
nums = [4,5,6,7,0,1,2]
```

---

## 🟢 Step 1

```
low = 0
high = 6
mid = (0+6)//2 = 3
nums[mid] = 7
nums[high] = 2
```

👉 Compare:

```
7 > 2  → TRUE
```

👉 Means:
➡ Minimum is in RIGHT half

```
low = mid + 1 = 4
```

---

## 🟢 Step 2

```
low = 4
high = 6
mid = (4+6)//2 = 5
nums[mid] = 1
nums[high] = 2
```

👉 Compare:

```
1 > 2 → FALSE
```

👉 Means:
➡ Minimum is in LEFT (including mid)

```
high = mid = 5
```

---

## 🟢 Step 3

```
low = 4
high = 5
mid = (4+5)//2 = 4
nums[mid] = 0
nums[high] = 1
```

👉 Compare:

```
0 > 1 → FALSE
```

👉 Means:
➡ Minimum is in LEFT

```
high = mid = 4
```

---

## 🟢 Step 4

```
low = 4
high = 4
```

👉 Loop stops (low == high)

---

# 🎯 Final Answer

```
nums[low] = nums[4] = 0
```

---

# 🧠 Why this works (lock this in)

Instead of searching the minimum directly, we:

👉 **eliminate sorted halves smartly**

* If mid > high → left part is useless ❌
* If mid <= high → right part is useless ❌

---

# ⚠️ Common Mistakes (you WOULD have made these)

* Using `while low <= high` ❌ (wrong here)
* Doing `high = mid - 1` ❌ (loses answer)
* Comparing with `nums[low]` ❌ (breaks logic)

---


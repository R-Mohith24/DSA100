
## 5.1 Maximum Sum Subarray of Size K

**LeetCode:** No direct equivalent
**GFG:** Maximum Sum Subarray of Size K

### Problem Statement

Given an integer array `arr` and an integer `k`, find the **maximum sum** of any **contiguous subarray** of size exactly `k`.

---

#### Example 1

**Input:**

```text
arr = [100, 200, 300, 400]
k = 2
```

**Output:**

```text
700
```

**Explanation:**

Subarrays of size `2`:

```text
[100,200] = 300
[200,300] = 500
[300,400] = 700
```

Maximum sum = **700**

---

#### Example 2

**Input:**

```text
arr = [1,4,2,10,23,3,1,0,20]
k = 4
```

**Output:**

```text
39
```

**Explanation:**

The subarray:

```text
[4,2,10,23]
```

has the maximum sum = **39**.

---

#### Constraints

```text
1 <= arr.length <= 10^5
-10^4 <= arr[i] <= 10^4
1 <= k <= arr.length
```

---

```python
class Solution:
    def maxSumSubarray(self, nums: List[int], k: int) -> int:
        res = float('-inf')
        curr_sum = 0

        left = 0
        for right in range(len(nums)):
            curr_sum += nums[right]

            if right - left + 1 > k:
                curr_sum -= nums[left]
                left += 1

            if right - left + 1 == k:
                res = max(res , curr_sum)

        return res
```




The way to remember Sliding Window forever is this:

> **"Grow → Shrink → Process."**

Your code does exactly that.

### 1. Grow the window

```python
curr_sum += nums[right]
```

Every iteration, the window expands to the right by one element.

---

### 2. Shrink the window

```python
if right - left + 1 > k:
    curr_sum -= nums[left]
    left += 1
```

If the window becomes **too big**, remove the leftmost element and move `left`.

Now the window is back to size `k`.

---

### 3. Process the window

```python
if right - left + 1 == k:
    res = max(res, curr_sum)
```

Only when the window is **exactly** size `k` do we use it to update the answer.

---

## The pattern to memorize

```text
Add new element
        ↓
Window too big?
        ↓
Remove old element
        ↓
Window exactly right?
        ↓
Update answer
```


Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of nums except `nums[i]`.

The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in `O(n)` time and without using the division operation.



```
Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]


Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
```

--

```python

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        #buld a prefix product array
        prefix = [0]*n
        prefix[0] = nums[0]
        for i in range(1,n):
            prefix[i] = prefix[i-1] * nums[i]
        #build a suffix Product Array

        suffix = [0] * n
        suffix[n - 1] = nums[n - 1]

        for j in range(n - 2 , -1 , -1):
            suffix[j] = suffix[j+1] * nums[j]
        
        ans = []

        for i in range(n):
            left = prefix[i-1] if i > 0 else 1
            right = suffix[i + 1] if i < n - 1 else 1
            ans.append(left * right)

        return ans
```
---
---
---

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n

        left = 1
        for i in range(n):
            ans[i] = left
            left *= nums[i]

        right = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= right
            right *= nums[i]

        return ans
```


Let's dry run with:

```text
nums = [1,2,3,4]
```

Initially:

```text
ans = [1,1,1,1]
left = 1
```

### Pass 1 (Left → Right)

| i | ans[i] = left | left *= nums[i] | ans       |
| - | ------------- | --------------- | --------- |
| 0 | 1             | 1×1 = 1         | [1,1,1,1] |
| 1 | 1             | 1×2 = 2         | [1,1,1,1] |
| 2 | 2             | 2×3 = 6         | [1,1,2,1] |
| 3 | 6             | 6×4 = 24        | [1,1,2,6] |

Now:

```text
ans = [1,1,2,6]
```

👉 Every index contains the **left product**.

---

Now start the second pass.

```text
right = 1
```

### Pass 2 (Right → Left)

| i | ans[i] *= right | right *= nums[i] | ans         |
| - | --------------- | ---------------- | ----------- |
| 3 | 6×1 = 6         | 1×4 = 4          | [1,1,2,6]   |
| 2 | 2×4 = 8         | 4×3 = 12         | [1,1,8,6]   |
| 1 | 1×12 = 12       | 12×2 = 24        | [1,12,8,6]  |
| 0 | 1×24 = 24       | 24×1 = 24        | [24,12,8,6] |

Done! ✅

---

## The mental model (this is the part to remember)

Imagine every index has **two friends**:

```text
Left Product  ×  Right Product
```

### First pass

Tell every index:

> "I'm giving you everything on your left."

### Second pass

Tell every index:

> "Now multiply by everything on your right."

That's it.

You never build prefix/suffix arrays separately—the answer array **becomes the left-product array**, and then you enrich it with the right product.

---

### 🧠 One-line memory trick

```text
Pass 1 → Store LEFT product in ans.
Pass 2 → Multiply RIGHT product into ans.
```

If you remember just those two sentences, you can reconstruct the entire algorithm during an interview. I actually think this version is easier to derive under pressure than the separate prefix/suffix arrays. 🚀

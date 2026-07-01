# Next Greater Element I

The next greater element of some element `x` in an array is the first greater element that is to the right of `x` in the same array.

You are given two distinct 0-indexed integer arrays `nums1` and `nums2`, where `nums1` is a subset of `nums2`.

For each `0 <= i < nums1.length`, find the index j such that `nums1[i] == nums2[j]` and determine the next greater element of `nums2[j]` in `nums2`. If there is no next greater element, then the answer for this query is `-1`.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

 
```
Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.

Example 2:

Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
- 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.
```


## brute force

```CPP
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {n : i for i, n in enumerate(nums1)}
        res = [-1] * len(nums1)

        for i in range(len(nums2)):
            if nums2[i] in hashmap:
                for j in range(i + 1, len(nums2)):
                    if nums2[j] > nums2[i]:
                        idx = hashmap[nums2[i]]
                        res[idx] = nums2[j]
                        break
        return res
```

## Optimal (using monotonic stack)
```python
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {n : i for i, n in enumerate(nums1)}
        res = [-1] * len(nums1)
        stack = []
        for i in range(len(nums2)):
            curr = nums2[i]
            while stack and curr > stack[-1]:
                val = stack.pop()
                idx = hashmap[val]
                res[idx] = curr

            if curr in hashmap:
                stack.append(curr)

        return res

```



✅ Time: O(n + m) (effectively linear)
✅ Space: O(n)



### Next Greater Element I (Monotonic Stack)

**Idea:**

* `hashmap` stores the index of each element in `nums1` so we can directly place the answer in `res`.
* `stack` stores only those elements from `nums1` whose next greater element has **not yet been found**.

**Algorithm:**

1. Traverse `nums2` from left to right.
2. Let `curr` be the current element.
3. While `curr` is greater than the top of the stack:

   * We have found the next greater element for the stack top.
   * Pop `val`.
   * Store `curr` as the answer for `val`.
4. If `curr` belongs to `nums1`, push it into the stack.
5. Any elements left in the stack have no greater element to their right, so they remain `-1`.

**Important Invariant:**

* Every element in the stack is guaranteed to exist in `hashmap`.
* Why? Because the **only** way an element enters the stack is:

  ```python
  if curr in hashmap:
      stack.append(curr)
  ```
* Therefore:

  ```python
  idx = hashmap[val]
  ```

  can never throw a `KeyError`.

**Pattern to remember:**

* Push elements whose answer is still unknown.
* When a larger element arrives, resolve as many pending elements as possible by popping them.

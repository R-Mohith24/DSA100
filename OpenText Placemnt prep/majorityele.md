169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 
```
Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
```

Constraints:
```
n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
```
The input is generated such that a majority element will exist in the array.


```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        n = len(nums)

        for i in range(n):
            if count == 0:
                candidate = nums[i]
                count = 1
            elif nums[i] == candidate:
                count += 1
            else:
                count -= 1

        return candidate
```
### if the question says that the array Might NOT contain a majority element and we have to return -1 if the array doesnt have any majority element then -

```python
class Solution:
    def majorityElement(self, arr):
        candidate = None
        count = 0

        for i in arr:
            if count == 0:
                candidate = i
                count = 1
            elif i == candidate:
                count += 1
            else:
                count -= 1
        count = 0
        for i in arr:
            if candidate == i:
                count += 1
        if count > len(arr) // 2:
            return candidate
        return -1
```
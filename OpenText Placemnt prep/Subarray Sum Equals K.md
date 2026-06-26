## Subarray Sum Equals K

Given an array of integers `nums` and an integer `k`, return the total number of subarrays whose sum equals to `k`.
A subarray is a contiguous non-empty sequence of elements within an array.

 
```
Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2
```
```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        Prefix_Sum = 0
        hashmap = {0 : 1}
        for n in nums:
            Prefix_Sum += n
            diff = Prefix_Sum - k
            res += hashmap.get(diff , 0)

            hashmap[Prefix_Sum] = hashmap.get(Prefix_Sum , 0) + 1

        return res
```

**https://www.youtube.com/watch?v=fFVZt-6sgyo**


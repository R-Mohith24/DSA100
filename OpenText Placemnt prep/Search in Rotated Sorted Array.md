## Search in Rotated Sorted Array

There is an integer array `nums` sorted in ascending order (with distinct values).

Prior to being passed to your function, `nums` is possibly left rotated at an unknown index `k` `(1 <= k < nums.length)` such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0]`, `nums[1], ..., nums[k-1]]` (0-indexed). For example, `[0,1,2,4,5,6,7]` might be left rotated by 3 indices and become `[4,5,6,7,0,1,2]`.

Given the array `nums` after the possible rotation and an integer target, return the index of target if it is in `nums`, or -1 if it is not in `nums`.

You must write an algorithm with `O(log n)` runtime complexity.


```
Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1
```


```
Rotated Binary Search

Every iteration asks ONLY 2 questions.

1. Which half is sorted?
2. Does the target belong to that sorted half?

"Belong" means:
start <= target <= end

If yes → search there.
If no → search the other half.
```
---
---
---

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n - 1
        while low <= high:

            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            
            # check whether the left half is sorted or not
            if nums[low] <= nums[mid]:
                if nums[low] <= target and target <= nums[mid]:
                    # our target is in left half
                    high = mid - 1
                else:
                    # our target is NOT In left half
                    low = mid + 1
                    
            # check whether the right half is sorted or not
            else:
                #to check whether the target is in right half or not
                if nums[high] >= target and target >= nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1
```
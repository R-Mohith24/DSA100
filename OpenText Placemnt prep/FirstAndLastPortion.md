##  Find First and Last Position of Element in Sorted Array

Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.

If `target` is not found in the array, return `[-1, -1]`.

You must write an algorithm with `O(log n)` runtime complexity.


```
Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
```

```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def BinarySearch(nums , target , LeftBias):
            n = len(nums)
            low , high = 0 , n - 1
            idx = -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] > target:
                    high = mid - 1

                elif nums[mid] < target:
                    low = mid + 1

                else:
                    idx = mid
                    if LeftBias == True: #Meaning we have to search for the left most element
                        high = mid - 1
                    else:
                        low = mid + 1
            return idx
        
        left = BinarySearch(nums , target , True)
        right = BinarySearch(nums , target , False)
        return [left , right]
```

```
Binary Search - First/Last Occurrence

When target is found:

DON'T return immediately.

Save it:
    idx = mid

Reason:
This is a VALID answer,
but there might be a BETTER answer.

First occurrence:
    Better = More LEFT

Last occurrence:
    Better = More RIGHT

idx always stores the BEST answer found so far.
```
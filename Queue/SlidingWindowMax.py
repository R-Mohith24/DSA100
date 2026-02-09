'''
Given an array arr[] of positive integers and an integer k. You have to find the maximum value for each contiguous subarray of size k.
Return an array of maximum values corresponding to each contiguous subarray

'''
'''
Input: arr[] = [1, 2, 3, 1, 4, 5, 2, 3, 6], k = 3
Output: [3, 3, 4, 5, 5, 5, 6]
Explanation: 
1st contiguous subarray [1, 2, 3], max = 3
2nd contiguous subarray [2, 3, 1], max = 3
3rd contiguous subarray [3, 1, 4], max = 4
4th contiguous subarray [1, 4, 5], max = 5
5th contiguous subarray [4, 5, 2], max = 5
6th contiguous subarray [5, 2, 3], max = 5
7th contiguous subarray [2, 3, 6], max = 6
'''

from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        dq = deque()      # stores indices
        result = []

        for i in range(len(nums)):

            # 1. remove expired indices (front)
            if dq and dq[0] < i - k + 1:
                dq.popleft()

            # 2. remove smaller elements (rear)
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            # 3. add current index
            dq.append(i)

            # 4. record max
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result

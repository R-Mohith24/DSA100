
#nextGreaterElement from leetcode 496

"""
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2.
If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.
"""
'''
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
'''

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):

        n = len(nums2)
        res = [-1]*n
        stack = []

        for i in range(n-1,-1,-1):
            while stack and nums2[i] >= nums2[stack[-1]]:
                stack.pop()

            if stack: #not empty
                res[i] = nums2[stack[-1]]

            stack.append(i)
        
        nge_map = {}
        for i in range(n):
            nge_map[nums2[i]] = res[i]

        ans = []

        for val in nums1:
            ans.append(nge_map[val])

        return ans
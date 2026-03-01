"""
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped
"""
# watch tutorial from NEETCODE
class Solution(object):
    def trap(self, height):

        if not height:
            return False


        n = len(height)
        l , r = 0 , n-1
        leftmax = height[l]
        rightmax = height[r]
        res = 0

        while l<r:
            if leftmax < rightmax:
                l += 1
                leftmax = max(leftmax,height[l])
                res += leftmax - height[l]

            else:
                r -= 1
                rightmax = max(rightmax,height[r])
                res += rightmax - height[r]

        return res

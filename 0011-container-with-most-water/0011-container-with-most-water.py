class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        l , r = 0 , len(height) - 1
        while l < r:
            area = (r-l) * min(height[l] , height[r])
            res = max(res , area)

            if height[l] < height[r]:
                l += 1
            elif height[r] < height[l]:
                r -= 1
            else: #both are equal (doesnt matter whicever you move)
                r -= 1

        return res

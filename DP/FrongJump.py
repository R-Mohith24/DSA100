class Solution:
    def minCost(self, height):
        def f(idx , height , dp):
            if (idx==0):
                return 0
            if (dp[idx] != -1):
                return dp[idx]
            left = f(idx-1,height,dp) + abs(height[idx] - height[idx-1])
            # we initialise Right because when idx == 1 , we never execute right inside IF block
            # so durinng dp[idx] = min(left,right) --> we get an error , Hence we initialise it with MAX
            right = float('inf')
            if idx > 1:
                right = f(idx-2,height,dp) + abs(height[idx] - height[idx-2])
            dp[idx] = min(left,right)
            return dp[idx]
        
        n = len(height)
        dp = [-1]*(n+1)
        return f(n-1,height,dp)


# TABULATION
n = len(height)
dp = [-1] * n
dp[0] = 0
for idx in range(1,n):
    left = dp[idx - 1] + abs(height[idx] - height[idx-1])
    right = float('inf')
    if idx > 1:
        right = dp[idx-2] + abs(height[idx] - height[idx-2])
    dp[idx] = min(left,right)
return dp[n-1] #or dp[idx] too cuz after the loop completes idx == n-1
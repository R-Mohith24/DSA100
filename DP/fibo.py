# #fibonachi recursion
# def fibonachi(n):
#     if n <= 1:
#         return n

#     return fibonachi(n-1) + fibonachi(n-2)

print(fibonachi(5))

# memorisation
def fibonachi(n,dp):
    if n <= 1:
        return n 
    if dp[n] != -1:
        return dp[n]

        dp[n] = fibonachi(n-1 , dp[i]) + fibonachi(n-2 , dp[i])
        return dp[n]

dp = [-1] * (n+1)

# tabulation

n = int(input())
dp = [-1] * (n+1)
dp[0] = 0
dp[1] = 1
for i in range(2,n+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n])
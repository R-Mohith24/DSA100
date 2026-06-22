def func(idx , dp):
    if idx == 0 or idx == 1:
        return 0
    if dp[idx] != -1:
        return dp[idx]
    onestep = func(idx-1 , dp) + cost[idx-1]
    twostep = func(idx-2 , dp) + cost[idx-2]
    dp[idx] = min(onestep , twostep)
    return dp[idx]

n = len(cost)
dp = [-1]*(n+1)
print(func(n,dp))


#tabulation
n = len(cost)
dp = [-1]*(n+1)
dp[0] = 0
dp[1] = 0
for idx in range(2,n+1):
    onestep = dp[idx-1] + cost[idx-1]
    twostep = dp[idx-2] + cost[idx-2]

    dp[idx] = min(onestep,twostep)
return dp[idx]
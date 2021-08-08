N = int(input())
res = 0

dp = [0 for _ in range(N+1)]

for i in range(N+1):
    if i == 0:
        dp[i] = 0
    
    elif i == 1:
        dp[i] = 1

    elif i == 2:
        dp[i] = 2

    else:
        dp[i] = dp[i-1] + dp[i-2]

print(dp[N] % 10007)


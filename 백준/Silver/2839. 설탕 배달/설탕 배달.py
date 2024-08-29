n = int(input())

if n == 3: print(1)
elif n == 4: print(-1)
else:
    dp = [float('inf') for _ in range(n+1)]
    dp[3], dp[5] = 1, 1

    for i in range(3,n+1):
        if i+3 <= n: dp[i+3] = min(dp[i+3], dp[i]+1)
        if i+5 <= n: dp[i+5] = min(dp[i+5], dp[i]+1)

    print(-1 if dp[-1] == float('inf') else dp[-1])
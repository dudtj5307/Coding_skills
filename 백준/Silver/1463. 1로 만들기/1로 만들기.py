N = int(input())

dp = [float('inf') for _ in range(N+1)]
dp[1] = 0

for i in range(1,N):
    for new in [i*2, i*3, i+1]:     # [2배, 3배, +1] 총 3가지 연산묶음
        if new <= N: dp[new] = min(dp[new], dp[i]+1)  # DP

print(dp[-1])
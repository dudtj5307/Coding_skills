MAX_NUM = 12

T = int(input())
dp = [0 for _ in range(MAX_NUM)]
dp[1], dp[2], dp[3] = 1, 2, 4

for i in range(4, MAX_NUM):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for _ in range(T):
    print(dp[int(input())])
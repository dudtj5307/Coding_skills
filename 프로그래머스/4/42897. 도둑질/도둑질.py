def solution(money):
    L = len(money)
    dp1, dp2 = [0] * L, [0] * L
    dp1[0] = money[0]
    for i in range(0, L-1):
        dp1[i] = max(dp1[i-1], dp1[i-2] + money[i])
    for i in range(1, L):
        dp2[i] = max(dp2[i-1], dp2[i-2] + money[i])
    return max(dp1[-2], dp2[-1])
        
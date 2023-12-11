def solution(left, right):
    dp = [0] * (right + 1)
    for i in range(1, right+1):
        for p in range(i, right+1, i):
            dp[p] += 1
    answer = 0
    for i in range(left, right+1):
        if dp[i] % 2: answer -= i
        else: answer += i
    return answer
from collections import deque

def solution(prices):
    answer = [0] * len(prices)
    q = deque()
    for i, p in enumerate(prices):
        while q and p < prices[q[-1]]:
            j = q.pop()
            answer[j] = i - j
        q.append(i)
    while q:
        j = q.pop()
        answer[j] = len(prices) - j - 1
    return answer
            
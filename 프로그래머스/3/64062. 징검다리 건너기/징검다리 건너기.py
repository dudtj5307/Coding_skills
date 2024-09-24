from heapq import heappush, heappop

def solution(stones, k):
    q = []
    answer = float('inf')
    for i, stone in enumerate(stones):
        heappush(q, [-stone, i])
        while i - q[0][1] >= k:
            heappop(q)
        if i >= k - 1:
            answer = min(answer, -q[0][0])
    return answer
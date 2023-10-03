from heapq import heappop, heappush

def solution(scoville, K):
    h = []
    for s in scoville:
        heappush(h, s)
    answer = 0
    while h[0] < K and len(h) >= 2:
        a = heappop(h)
        b = heappop(h)
        heappush(h, a + 2 * b)
        answer += 1
    if h[0] < K: return -1
    return answer
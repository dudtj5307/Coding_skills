from heapq import heappop, heappush

def solution(k, score):
    answer = []
    hq = []
    for s in score:
        heappush(hq, s)
        if len(hq) == k + 1:
            heappop(hq)
        answer.append(hq[0])
    return answer
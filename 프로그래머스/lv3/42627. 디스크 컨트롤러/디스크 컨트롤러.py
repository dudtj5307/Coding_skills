from heapq import heapify, heappush, heappop

def solution(jobs):
    last, now = -1, 0
    answer, hq = [], []
    while len(answer) < len(jobs):
        for js, dur in jobs:
            if last < js <= now:
                heappush(hq, [dur, js])
        if hq:
            w = heappop(hq)
            last = now
            now += w[0]
            answer.append(now - w[1])
        else:
            now += 1
    return sum(answer)//len(jobs)
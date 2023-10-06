from heapq import heappush, heappop, nlargest, heapify

def solution(operations):
    hq = []
    for o in operations:
        order, n = o.split(" ")
        if order == "I":
            heappush(hq, int(n))
        elif hq and order == "D":
            if int(n) == 1:
                largnum = nlargest(1, hq)[0]
                hq.remove(largnum)
                # hq = heapify(hq)
            else: heappop(hq)
    if hq:
        return [max(hq), min(hq)]
    else:
        return [0, 0]
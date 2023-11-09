from collections import defaultdict

def solution(strArr):
    d = defaultdict(int)
    for s in strArr:
        d[len(s)] += 1
    return max(d.values())
from itertools import combinations

def solution(d, budget):
    i, _sum = 0, 0
    for n in sorted(d):
        _sum += n
        if _sum > budget:
            return i
        i += 1
    return i
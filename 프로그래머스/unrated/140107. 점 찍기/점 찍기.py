from math import floor

def solution(k, d):
    dk = floor(d/k)
    answer = 0
    for x in range(dk+1):
        answer += min(dk, floor(((d/k)**2 - x**2)**0.5)) + 1
    return answer
def solution(a, d, included):
    return sum([included[i] * (a + d*i) for i in range(len(included))])
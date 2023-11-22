from collections import defaultdict

def solution(weights):
    d = defaultdict(int)
    answer = 0
    for w in weights:
        answer += d[w] + d[w/3*2] + d[w/2] + d[w/2*3] + d[w/4*3] + d[w*2] + d[w/3*4]
        d[w] += 1
    return answer
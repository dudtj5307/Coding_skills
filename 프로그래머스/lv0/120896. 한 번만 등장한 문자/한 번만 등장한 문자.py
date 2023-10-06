from collections import defaultdict

def solution(s):
    answer = []
    d = defaultdict(int)
    for i in s:
        d[i] += 1
    for k, v in d.items():
        if v == 1:
            answer.append(k)
    return "".join(sorted(answer))
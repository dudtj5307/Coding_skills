def solution(clothes):
    d = {}
    for c, t in clothes:
        if t not in d.keys():
            d[t] = 2
        else: d[t] += 1
    answer = 1
    for v in d.values():
        answer *= v
    return answer - 1
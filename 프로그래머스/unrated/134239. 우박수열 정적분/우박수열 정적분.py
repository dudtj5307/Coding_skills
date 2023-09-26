def solution(k, ranges):
    y = []
    while k != 1:
        if k % 2: y.append(2 * k + 0.5); k = 3 * k + 1
        else:     y.append(3 / 4 * k);   k = k // 2
    answer = []
    for s, e in ranges:
        e = len(y) + e
        if s==0 and e==len(y): answer.append(sum(y))
        elif s <= e: answer.append(sum(y[s:e]))
        else: answer.append(-1)
    return answer
    
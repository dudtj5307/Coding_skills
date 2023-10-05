def solution(score):
    ls, li = -1, -1
    answer = [0] * len(score)
    score = sorted([[i, sum(s)] for i, s in enumerate(score)], key=lambda x: -x[1])
    for i, (idx, s) in enumerate(score):
        if ls == s:
            answer[idx] = li + 1
        else:
            answer[idx] = i + 1
            ls, li = s, i
    return answer
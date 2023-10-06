def solution(emergency):
    answer = [0] * len(emergency)
    temp = []
    for i, e in enumerate(emergency):
        temp.append([i, e])
    for i, (ti, te) in enumerate(sorted(temp, key=lambda x: -x[1])):
        answer[ti] = i + 1
    return answer
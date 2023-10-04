def solution(rank, attendance):
    s, i, answer = 0, 1, []
    while s != 3:
        idx = rank.index(i)
        if attendance[idx]:
            answer.append(idx)
            s += 1
        i += 1
    return 10000 * answer[0] + 100 * answer[1] + answer[2]
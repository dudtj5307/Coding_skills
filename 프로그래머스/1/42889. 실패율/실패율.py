def solution(N, stages):
    answer = [[i,0,0] for i in range(N+1)]    # [idx, 멈춘수, 총수]
    for s in stages:
        if s != N+1:
            answer[s][1] += 1
        else:
            s = N
        for i in range(1, s+1):
            answer[i][2] += 1
    for i in range(1, len(answer)):
        if answer[i][2] == 0:
            answer[i][1] = 0
        else:
            answer[i][1] = answer[i][1] / answer[i][2]
    return [idx for idx, _, _ in sorted(answer[1:], key=lambda x:-x[1])]
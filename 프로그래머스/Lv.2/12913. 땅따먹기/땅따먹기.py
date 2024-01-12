def solution(land):
    answer = [[l for l in la] for la in land]
    for i in range(len(land)-1):
        for j in range(4):
            for k in range(4):
                if j != k:
                    answer[i+1][k] = max(answer[i+1][k], land[i+1][k] + answer[i][j])
    return max(map(max, answer))
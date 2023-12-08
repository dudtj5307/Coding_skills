from collections import defaultdict

def solution(X, Y):
    answer = ""
    dX, dY = defaultdict(int), defaultdict(int)
    for x in X: dX[x] += 1
    for y in Y: dY[y] += 1
    for i in range(9, -1, -1):
        si = str(i)
        answer += si * min(dX[si], dY[si])
    if answer == "":
        return "-1"
    if answer[0] == "0":
        return "0"
    return answer
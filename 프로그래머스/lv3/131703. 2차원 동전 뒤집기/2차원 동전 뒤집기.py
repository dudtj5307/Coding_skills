def solution(beginning, target):
    h, w = len(beginning), len(beginning[0])
    t = [[beginning[i][j] ^ target[i][j] for j in range(w)] for i in range(h)]
    
    cnt = 0
    for i in range(1,h):
        if t[i] != t[0]:
            cnt += 1
            if list(map(lambda x: x ^ 1, t[i])) != t[0]:
                return -1
    return min(sum(t[0]) + cnt, h + w - sum(t[0]) - cnt)


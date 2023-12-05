from collections import deque

def solution(land):
    m, n = len(land), len(land[0])
    oil = []
    answer = [0] * n
    for i in range(m):
        for j in range(n):
            if land[i][j]:
                land[i][j] = 0
                x = [j]
                q = deque([[i,j]])
                while q:
                    si, sj = q.popleft()
                    for di, dj in [(-1,0), (1,0), (0,1), (0,-1)]:
                        ni, nj = si + di, sj + dj
                        if 0 <= ni < m and 0 <= nj < n and land[ni][nj]:
                            land[ni][nj] = 0
                            x.append(nj)
                            q.append([ni,nj])
                oil.append([min(x), max(x), len(x)])
                for o in range(min(x), max(x)+1):
                    answer[o] += len(x)
    return max(answer)
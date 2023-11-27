from collections import deque
way = [(-1,0), (1,0), (0,1), (0,-1)]

def solution(maps):
    m, n = len(maps), len(maps[0])
    q = deque([[0, 0]])
    while q:
        y, x = q.popleft()
        for dy, dx in way:
            if 0 <= x + dx < n and 0 <= y + dy < m and maps[y+dy][x+dx] == 1:
                maps[y+dy][x+dx] = maps[y][x] + 1
                q.append([y+dy,x+dx])
    return maps[m-1][n-1] if maps[m-1][n-1] != 1 else -1
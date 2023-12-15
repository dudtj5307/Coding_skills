from collections import deque

def partToShape(part):
    imin, imax = min(part, key=lambda x:x[0])[0], max(part, key=lambda x:x[0])[0]
    jmin, jmax = min(part, key=lambda x:x[1])[1], max(part, key=lambda x:x[1])[1]
    shape = [[0 for _ in range(jmax-jmin+1)] for _ in range(imax-imin+1)]
    for pi, pj in part:
        shape[pi-imin][pj-jmin] = 1
    return shape

def findPart(board, value):
    shapes = []
    for i in range(m):
        for j in range(n):
            if board[i][j] == value:
                board[i][j] = 1 - value
                part = [[i,j]]
                q = deque(part)
                while q:
                    si, sj = q.popleft()
                    for di, dj in [(-1,0),(1,0),(0,1),(0,-1)]:
                        ni, nj = si + di, sj + dj
                        if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == value:
                            board[ni][nj] = 1 - value
                            part.append([ni, nj])
                            q.append([ni, nj])
                shapes.append(partToShape(part))
    # print(shapes)
    return shapes

def rotate(shape):
    return [list(l) for l in zip(*shape[::-1])]
                
def solution(game_board, table):
    global m, n
    m, n = len(game_board), len(game_board[0])
    shapes1, shapes2 = findPart(game_board, 0), findPart(table, 1)
    answer = 0
    for s2 in shapes2:
        r = 0
        while r < 4:
            if r > 0:
                s2 = rotate(s2)
            r += 1
            if s2 in shapes1:
                answer += sum(list(map(sum, s2)))
                shapes1.remove(s2)
                break
    return answer


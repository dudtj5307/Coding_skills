direction = [(-1,0), (0,1), (1,0), (0,-1)] # UP, RIGHT, DOWN, LEFT

def rotate(d, node):
    if node == "R":
        d = (d + 1) % 4
    elif node == "L":
        d = (d - 1) % 4
    return d

def solution(grid):
    m, n = len(grid), len(grid[0])
    visited = [[[0 for _ in range(4)] for _ in range(n)] for _ in range(m)]
    answer = []
    for i in range(m):
        for j in range(n):
            for d in range(4):
                ni, nj, nd = i, j, d
                cnt = 0
                while visited[ni][nj][nd] == 0:
                    visited[ni][nj][nd] = 1
                    ni, nj = (ni + direction[nd][0]) % m, (nj + direction[nd][1]) % n
                    nd = rotate(nd, grid[ni][nj])
                    cnt += 1
                if cnt:
                    answer.append(cnt)
    return sorted(answer)
                    
        
from collections import deque
direction = [[(-1,0), (1,0), (0,1), (0,-1)], [[0,0]]]

def solution(maze):
    m, n = len(maze), len(maze[0])
    R_visited, B_visited = [[0] * n for _ in range(m)], [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            value = maze[i][j]
            if value == 1: start_r = [i, j]; R_visited[i][j] = 1
            elif value == 2: start_b = [i, j]; B_visited[i][j] = 1
            elif value == 3: end_r = [i, j]
            elif value == 4: end_b = [i, j]
            elif value == 5: R_visited[i][j], B_visited[i][j] = 5, 5
            
    q = deque([[start_r, start_b, R_visited, B_visited]])
    while q:
        (ri, rj), (bi, bj), RV, BV = q.popleft()
        k = 0
        if [ri, rj] == end_r: k = 1
        for di1, dj1 in direction[k]:
            n_ri, n_rj = ri+di1, rj+dj1
            if 0 <= n_ri < m and 0 <= n_rj < n and (RV[n_ri][n_rj] == 0 or maze[n_ri][n_rj] == 3):
                k = 0
                if [bi, bj] == end_b: k = 1
                for di2, dj2 in direction[k]:
                    n_bi, n_bj = bi+di2, bj+dj2
                    if 0 <= n_bi < m and 0 <= n_bj < n and (BV[n_bi][n_bj] == 0 or maze[n_bi][n_bj] == 4):
                        if [n_ri,n_rj] != [n_bi,n_bj] and [n_ri,n_rj, n_bi,n_bj] != [bi,bj, ri,rj]:
                            RVtemp, BVtemp = [], []
                            for R in RV:
                                temp = [r for r in R]
                                RVtemp.append(temp)
                            for B in BV:
                                temp = [b for b in B]
                                BVtemp.append(temp)
                            RVtemp[n_ri][n_rj] = RVtemp[ri][rj] + 1
                            BVtemp[n_bi][n_bj] = BVtemp[bi][bj] + 1
                            q.append([[n_ri,n_rj], [n_bi, n_bj], RVtemp, BVtemp])
                            if end_r == [n_ri, n_rj] and end_b == [n_bi, n_bj]:
                                return RVtemp[n_ri][n_rj] - 1
    return 0
            
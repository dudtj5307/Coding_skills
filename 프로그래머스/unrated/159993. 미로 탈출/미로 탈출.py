import numpy as np
from collections import deque

def solution(maps):
    h, w = len(maps), len(maps[0])
    v = [[-1,0],[1,0],[0,-1],[0,1]]
    
    for i, row in enumerate(maps):
        if "S" in row: Si, Sj = i, row.index("S")
        if "L" in row: Li, Lj = i, row.index("L")
        if "E" in row: Ei, Ej = i, row.index("E")
    # <BFS> S -> L, L -> E
    def escape(ai,aj,bi,bj):
        q = deque()
        q.append([ai,aj])
        vis = [[0]*w for i in range(h)]
        vis[ai][aj] = 1
        while q:
            Ni, Nj = q.popleft()
            if [Ni, Nj] == [bi, bj]: return vis[bi][bj]
            
            for i in range(4):
                ni, nj = Ni+v[i][0], Nj+v[i][1]
                if 0 <= ni < h and 0 <= nj < w:
                    if vis[ni][nj]==0 and maps[ni][nj]!="X":
                        q.append([ni,nj])
                        vis[ni][nj] = vis[Ni][Nj] + 1
        return 0
    # main                
    S_L = escape(Si, Sj, Li, Lj)
    if S_L: 
        L_E = escape(Li, Lj, Ei, Ej)
        if L_E: return S_L+L_E - 2
        else: return -1
    else: return -1
    
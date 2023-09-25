from collections import deque
import numpy as np


def solution(board):
    
    def slide(Ri,Rj,v):
        while (0<=Ri+m[v][0]<h)&(0<=Rj+m[v][1]<w):
            if board[Ri+m[v][0]][Rj+m[v][1]]=="D":break
            else: Ri += m[v][0]; Rj += m[v][1]
        return Ri, Rj

    h, w = len(board), len(board[0])
    visit = [[0]*w for i in range(h)]
    m = [[-1,0], [1,0], [0,-1], [0,1]]
    
    for i, b in enumerate(board):
        if "R" in b: Ri, Rj = i, list(b).index("R")
    visit[Ri][Rj] = 1
    q = deque(); q.append([Ri,Rj])
    while q:
        Ri, Rj = q.popleft()
        if board[Ri][Rj] == "G": return visit[Ri][Rj] - 1
        for v in range(4):
            Ni, Nj = Ri, Rj
            Ni, Nj = slide(Ni, Nj, v)
            if [Ni,Nj] != [Ri,Rj] and visit[Ni][Nj] == 0:
                q.append([Ni,Nj])
                visit[Ni][Nj] = visit[Ri][Rj] + 1
    return -1
    

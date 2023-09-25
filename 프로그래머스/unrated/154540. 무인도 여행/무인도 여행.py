from collections import deque

def solution(maps):
    h, w = len(maps), len(maps[0])
    v = [[-1,0], [1,0], [0,-1], [0,1]]
    visit, answer = [], []
    for i in range(h):
        for j in range(w):
            if maps[i][j] != "X" and [i,j] not in visit:
                visit.append([i,j])
                q = deque()
                q.append([i,j])
                food = 0
                while q:
                    Ni, Nj = q.popleft()
                    food += int(maps[Ni][Nj])
                    for n in range(4):
                        di, dj = v[n]
                        if 0<=Ni+di<h and 0<=Nj+dj<w and maps[Ni+di][Nj+dj]!="X":
                            if [Ni+di, Nj+dj] not in visit:
                                q.append([Ni+di, Nj+dj])
                                visit.append([Ni+di, Nj+dj])
                answer += [food]
    if answer == []: return [-1]
    return sorted(answer)
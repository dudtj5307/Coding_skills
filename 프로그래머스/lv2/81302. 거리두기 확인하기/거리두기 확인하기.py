from collections import deque
from copy import deepcopy

m = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def search(vmap, pos_P):
    for si, sj in pos_P:
        vmap1 = deepcopy(vmap)
        vmap1[si][sj] = 0
        q2 = deque()
        q2.append([si, sj])
        while q2:
            pi, pj = q2.popleft()
            for di, dj in m:
                if 0 <= pi+di <= 4 and 0 <= pj+dj <= 4:
                    if vmap1[pi+di][pj+dj] == 'P' and vmap1[pi][pj] <= 1:
                        return 0;
                    if vmap1[pi+di][pj+dj] == 0:
                        vmap1[pi+di][pj+dj] = vmap1[pi][pj] + 1
                        q2.append([pi+di, pj+dj])
    return 1;

def solution(places):
    result = []
    for place in places:
        flag = 0
        pos_P = deque([(i,j) for i, pl in enumerate(place) for j,  p in enumerate(pl) if p=='P'])
        vmap = [[0 if p=='O' else p for p in pl] for pl in place]
        if not search(vmap, pos_P): result.append(0); continue
        result.append(1)
    return result
                            
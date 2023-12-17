from itertools import product

def rotate(i, j, r):
    if r == 0: return
    r_clock[i][j] = (r_clock[i][j] + r) % 4
    for di, dj in [(-1,0),(1,0),(0,1),(0,-1)]:
        ni, nj = i + di, j + dj
        if 0 <= ni < m and 0 <= nj < n:
            r_clock[ni][nj] = (r_clock[ni][nj] + r) % 4

def solution(clock):
    global m, n, r_clock
    m, n = len(clock), len(clock[0])
    answer_list = []
    for first in list(product([0,1,2,3], repeat=n)):
        r_clock = [c[:] for c in clock]
        answer = sum(first)
        for j in range(n):
            rotate(0, j, first[j])
        for i in range(1, m):
            for j in range(n):
                r = (4 - r_clock[i-1][j]) % 4
                rotate(i, j, r)
                answer += r
        if sum(list(map(sum, r_clock))) == 0:
            answer_list.append(answer)
    return min(answer_list)
    

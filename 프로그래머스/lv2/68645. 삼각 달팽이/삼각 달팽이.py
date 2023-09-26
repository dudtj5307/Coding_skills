def solution(n):
    answer = [[0] * i for i in range(1, n+1)]
    DIR = {0: (1, 0), 1: (0, 1), 2: (-1, -1)}
    
    r, c, num, v = -1, 0, 1, 0
    for i in range(0, n):
        for _ in range(i, n):
            dr, dc = DIR[v]
            r += dr; c += dc
            answer[r][c] = num
            num += 1
        v = (v + 1) % 3
    return sum(answer, [])
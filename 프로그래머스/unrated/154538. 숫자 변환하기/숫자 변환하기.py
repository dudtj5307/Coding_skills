from collections import deque

def solution(x, y, n):
    visit = [0] * 1000001
    q = deque()
    q.append(x)
    while q:
        num = q.popleft()
        if num == y: return visit[y]
        for new_num in (num+n, num*2, num*3):
            if 0 <= new_num <= 1000000 and visit[new_num]==0:
                q.append(new_num)
                visit[new_num] = visit[num] + 1
    return visit[y] or -1

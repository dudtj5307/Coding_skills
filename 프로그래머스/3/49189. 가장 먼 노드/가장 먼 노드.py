from collections import deque

def solution(n, edge):
    node = [[] for _ in range(n+1)]
    visit = [0 for i in range(n+1)]
    for a, b in edge:
        node[a].append(b)
        node[b].append(a)
    
    visit[1] = 1
    q = deque([1])
    while q:
        k = q.popleft()
        for n in node[k]:
            if not visit[n]:
                visit[n] = visit[k] + 1
                q.append(n)

    return visit.count(max(visit))
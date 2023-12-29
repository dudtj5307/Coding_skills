from collections import deque

def solution(cacheSize, cities):
    answer = 0
    q = deque()
    for c in cities:
        c = c.lower()
        if c not in q:
            q.append(c)
            if len(q) > cacheSize:
                q.popleft()
            answer += 5
        else:
            q.remove(c)
            q.append(c)
            answer += 1
    return answer
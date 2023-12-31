from collections import deque

def solution(people, limit):
    q = deque(sorted(people))
    answer = 0
    while q:
        if len(q) == 1:
            answer += 1; return answer
        if q[0] + q[-1] <= limit:
            q.pop()
            q.popleft()
            answer += 1
        else:
            q.pop()
            answer += 1
    return answer

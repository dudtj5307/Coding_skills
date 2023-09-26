from collections import deque

def solution(priorities, location):
    q = deque(priorities)
    answer = 0
    while True:
        if q[0] >= max(q):
            q.popleft()
            answer += 1
            if location == 0: return answer
        else:
            q.rotate(-1)
        location = (location - 1) % len(q)
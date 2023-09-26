from collections import deque

def solution(order):
    c = deque()
    c.extend([i for i in range(1,len(order)+1)])
    q = deque()
    answer = 0
    while c or (q and q[-1] == order[answer]):
        if q and q[-1] == order[answer]:
            q.pop()
            answer += 1
        elif c[0] == order[answer]:
            c.popleft()
            answer += 1
        else:
            q.append(c[0])
            c.popleft()
    return answer
from collections import deque

def solution(string):
    q = deque()
    for s in string:
        q.append(s)
        while len(q) >= 2 and q[-2] == q[-1]:
            q.pop(); q.pop();
    return int(q == deque([]))
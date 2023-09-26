from collections import deque

def solution(progresses, speeds):
    answer = []
    q_pro, q_spd = deque(progresses), deque(speeds)
    i = 0
    while q_pro:
        i += 1
        a = 0
        while q_pro and q_pro[0] + q_spd[0] * i >= 100:
            q_pro.popleft()
            q_spd.popleft()
            a += 1
        if a: answer.append(a)
    return answer
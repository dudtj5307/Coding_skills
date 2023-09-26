from collections import deque

def solution(bridge_length, weight, truck_weights):
    s_q, e_q, m_q = deque(truck_weights), deque(), deque([0 for _ in range(bridge_length)])
    m = 0
    answer = 0
    while len(e_q) != len(truck_weights):
        tempm = m_q.popleft()
        if tempm: 
            e_q.append(tempm)
            m -= tempm
        if s_q and m + s_q[0] <= weight:
            temps = s_q.popleft()
            m_q.append(temps)
            m += temps
        else:
            m_q.append(0)
        answer += 1
    return answer
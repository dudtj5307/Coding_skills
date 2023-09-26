from collections import deque

def solution(weights):
    u_cnt = {}
    for i in range(len(weights)):
        if weights[i] not in u_cnt.keys():
            u_cnt[weights[i]] = 1
        else: u_cnt[weights[i]] += 1

    answer = 0
    q = deque()
    q.extend(sorted(u_cnt.keys()))
    while q:
        pos = []
        wl = q.popleft()
        for a in [3/2, 2/3, 2, 1/2, 3/4, 4/3]:
            if wl * a == int(wl * a): pos += [int(wl * a)]
        for wr in q:
            if wr in pos: answer += 1 * u_cnt[wl] * u_cnt[wr]

    for s in list(u_cnt.values()):
        while s > 1:
            s -= 1
            answer += s

    return answer
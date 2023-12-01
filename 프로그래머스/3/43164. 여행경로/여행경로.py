from collections import defaultdict, deque

def solution(tickets):
    place = defaultdict(list)
    for s, e in tickets:
        place[s].append(e)
    for k in place.keys():
        place[k] = sorted(place[k], reverse=True)
    answer = []
    q = deque(['ICN'])
    while q:
        current = q[-1]
        if current in place and len(place[current]) != 0:
            q.append(place[current].pop())
        else:
            answer.append(q.pop())
    return answer[::-1]
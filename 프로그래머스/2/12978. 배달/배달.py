from collections import defaultdict, deque
from heapq import heappop, heappush

def solution(N, road, K):
    distance = [float('inf')] * (N+1)
    distance[1] = 0
    graph = defaultdict(lambda:defaultdict(list))
    for s, e, k in road:
        graph[s][e].append(k)
        graph[e][s].append(k)
    q = [[0, 1]]    # distance : 0 / startNode = 1
    while q:
        dist_now, node_now = heappop(q)
        for node_next, dist in graph[node_now].items():
            dist_next = dist_now + min(dist)
            if dist_next < distance[node_next]:
                distance[node_next] = dist_next
                heappush(q, [dist_next, node_next])              
    return len(list(filter(lambda x: x <= K, distance[1:])))

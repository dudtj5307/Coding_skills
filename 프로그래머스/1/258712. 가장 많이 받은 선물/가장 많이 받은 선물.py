from collections import defaultdict
from itertools import combinations

def solution(friends, gifts):
    give, take = defaultdict(int), defaultdict(int)
    g_dic = defaultdict(lambda: defaultdict(int))
    for g, t in map(lambda x:x.split(" "), gifts):
        give[g] += 1
        take[t] += 1
        g_dic[g][t] += 1
    answer = defaultdict(int)
    for a, b in combinations(friends, 2):
        if g_dic[a][b] > g_dic[b][a]: answer[a] += 1
        elif g_dic[a][b] < g_dic[b][a]: answer[b] += 1
        else:
            if give[a] - take[a] > give[b] - take[b]: answer[a] += 1
            elif give[a] - take[a] < give[b] - take[b]: answer[b] += 1
            else: answer[a] += 0
    return max(answer.values())
    
    
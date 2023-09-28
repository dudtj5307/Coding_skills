from collections import Counter

def solution(genres, plays):
    sump, d = {}, {}
    for i, g in enumerate(genres):
        if g in d:
            d[g].append([plays[i],i])
            sump[g] += plays[i]
        else:
            d[g] = [[plays[i],i]]
            sump[g] = plays[i]
    s_sump = sorted(sump.items(), key = lambda item: item[1], reverse=True)
    answer = []
    for gen, _ in s_sump:
        t = sorted(d[gen], key=lambda x: x[0], reverse=True)
        for i in range(min(2, len(t))):
            answer += [t[i][1]]
    return answer
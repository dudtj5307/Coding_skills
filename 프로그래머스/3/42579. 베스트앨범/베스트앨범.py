from collections import Counter, defaultdict

def solution(genres, plays):
    d, sump = defaultdict(list), defaultdict(int)
    for i, gen in enumerate(genres):
        d[gen].append([plays[i],i])
        sump[gen] += plays[i]

    s_sump = sorted(sump.items(), key = lambda item: item[1], reverse=True)
    answer = []
    for gen, _ in s_sump:
        t = sorted(d[gen], key=lambda x: -x[0])
        for i in range(min(2, len(t))):
            answer += [t[i][1]]
    return answer
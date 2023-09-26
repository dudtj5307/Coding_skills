import bisect, itertools, collections

def solution(info, query):
    info_map = collections.defaultdict(list)
    binarys = list(itertools.product((True, False), repeat=4))
    for inf in info:
        inf = inf.split()
        for b in binarys:
            key = ''.join(inf[i] if b[i] else '-' for i in range(4))
            info_map[key].append(int(inf[4]))

    for k in info_map.keys():
        info_map[k].sort()
    
    answer = []
    for q in query:
        q1, _, q2, _, q3, _, q4, scores = q.split()
        key = ''.join([q1,q2,q3,q4])
        bi = bisect.bisect_left(info_map[key], int(scores))
        answer.append(len(info_map[key]) - bi)
    return answer
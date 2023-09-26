def solution(k, tangerine):
    d = {}
    for t in tangerine:
        if t in d.keys(): d[t] += 1
        else: d[t] = 1

    for i, n in enumerate(sorted(d.values(), reverse=True)):
        k -= n
        if k <= 0: return i+1
            
    
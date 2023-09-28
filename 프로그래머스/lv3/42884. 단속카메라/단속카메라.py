def solution(routes):
    routes = sorted(routes, key=lambda x: (x[0], x[1]))
    si, ei = routes[0]
    answer = 1
    for s, e in routes:
        if ei < s:
            si, ei = s, e
            answer += 1
        elif ei < e:
            si = s
        else:
            si, ei = s, e
    return answer
            
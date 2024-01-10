T = "0123456789ABCDEF"

def transform(n, formation):
    q, r = divmod(n, formation)
    if q == 0: return str(T[r])
    else: return transform(q, formation) + str(T[r])

def solution(n, t, m, p):
    answer, i = "", 0
    while len(answer) < t * m:
        answer += transform(i, n)
        i += 1
        
    return answer[p-1:m*t:m].upper()
def solution(string, skip, index):
    a = list('abcdefghijklmnopqrstuvwxyz')
    for sk in skip: del a[a.index(sk)]
    print(a)
    answer = ""
    for st in string: answer += a[(a.index(st)+index)%len(a)]
    return answer
def solution(s):
    rev = list(reversed(s.split(" ")))
    i, answer = 0, 0
    while i < len(rev):
        if rev[i] == 'Z': i += 1
        else: answer += int(rev[i])
        i += 1
    return answer
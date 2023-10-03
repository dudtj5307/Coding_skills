def solution(n):
    cnt, i = 0, 0
    while cnt != n:
        i += 1
        if i % 3 != 0 and '3' not in str(i): cnt += 1
    return i
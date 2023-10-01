def solution(sizes):
    a, b = 0, 0
    for s in sizes:
        a = max(a, min(s))
        b = max(b, max(s))
    return a * b
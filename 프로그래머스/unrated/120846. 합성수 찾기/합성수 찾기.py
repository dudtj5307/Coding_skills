def solution(n):
    s = set({1})
    prime = 1
    for i in range(2, n+1):
        if i not in s:
            prime += 1
            for j in range(i, n+1, i):
                s.add(j)
    return n - prime
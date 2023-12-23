def solution(n):
    root_n = n ** (1/2)
    if root_n == int(root_n): return (root_n + 1) ** 2
    else:
        return -1
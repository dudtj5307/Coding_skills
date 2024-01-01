def solution(n, s):
    div, mod = divmod(s, n)
    if div == 0: return [-1]
    return [div] * (n - mod) + [div+1] * mod
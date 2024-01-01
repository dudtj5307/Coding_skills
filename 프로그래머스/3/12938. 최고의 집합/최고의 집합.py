def solution(n, s):
    if s < 3 * n:
        return [-1]
    big = ((s // n) + 1 * bool(s % n)) * n
    diff = big - s
    each = big // n
    answer = [each for _ in range(n)]
    for i in range(diff):
        answer[i] -= 1
    return answer
def solution(n):
    max_twos = n // 2
    answer = 0
    for twos in range(0, max_twos+1):
        ones = n - 2 * twos
        answer += fac(ones+twos) // (fac(ones) * fac(twos))
    return answer % 1000000007
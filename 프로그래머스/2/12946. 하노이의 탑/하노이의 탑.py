def solution(n):
    def hanoi(start, temp, end, n):
        if n == 1:
            return [[start, end]]
        return hanoi(start, end, temp, n-1) + [[start, end]] + hanoi(temp, start, end, n-1)
    return hanoi(1,2,3,n)

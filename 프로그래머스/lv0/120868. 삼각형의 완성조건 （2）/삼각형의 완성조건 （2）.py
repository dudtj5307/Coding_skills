def solution(sides):
    answer = 0
    a, b = sides
    for c in range(1, 3000):
        l = max([a, b, c])
        if l < a + b + c - l:
            answer += 1
        if c >= a + b:
            return answer
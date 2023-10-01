def solution(brown, yellow):
    area = brown + yellow
    a = 3
    while True:
        if area % a == 0:
            b = area // a
            if (a + b) * 2 - 4 == brown:
                return [b, a]
        a += 1
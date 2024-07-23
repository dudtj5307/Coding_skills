def solution(n, stations, w):
    answer = 0
    W = 2 * w + 1
    last = 1
    for s in stations:
        space = (s - w - last)
        answer += space // W + bool(space % W)
        last = s + w + 1
    return answer + (n - s + w) // W
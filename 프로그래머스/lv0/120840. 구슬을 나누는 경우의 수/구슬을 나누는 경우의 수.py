def solution(balls, share):
    answer = 1
    for _ in range(share):
        answer *= balls
        balls -= 1
    for _ in range(share):
        answer //= share
        share -= 1
    return answer
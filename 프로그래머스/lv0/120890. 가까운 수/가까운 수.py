def solution(array, n):
    answer = [float('inf'), float('inf')]
    for a in array:
        if abs(n-a) < answer[0]:
            answer = [abs(n-a), a]
        elif abs(n-a) == answer[0]:
            answer[1] = min(answer[1], a)
    return answer[1]
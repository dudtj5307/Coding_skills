def solution(array):
    answer = 0
    for arr in array:
        for a in str(arr):
            if a == '7': answer += 1
    return answer
def solution(arr, k):
    answer = []
    for a in arr:
        if a not in answer:
            answer.append(a)
    for _ in range(k-len(answer)):
        answer.append(-1)
    return answer[:k]
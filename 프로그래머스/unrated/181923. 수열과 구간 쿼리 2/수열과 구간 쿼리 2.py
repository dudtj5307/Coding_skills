def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        a = list(filter(lambda x: x > k, arr[s:e+1]))
        if a: answer.append(min(a))
        else: answer.append(-1)
    return answer
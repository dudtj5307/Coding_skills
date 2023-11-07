def solution(arr, flag):
    answer = []
    for i in range(len(arr)):
        if flag[i]:
            answer.extend([arr[i] for _ in range(arr[i] * 2)])
        else:
            for i in range(arr[i]):
                if answer:
                    answer.pop()
    return answer
            
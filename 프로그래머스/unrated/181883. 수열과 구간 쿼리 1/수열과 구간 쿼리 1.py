def solution(arr, queries):
    for si, ei in queries:
        for i in range(si, ei+1):
            arr[i] += 1
    return arr
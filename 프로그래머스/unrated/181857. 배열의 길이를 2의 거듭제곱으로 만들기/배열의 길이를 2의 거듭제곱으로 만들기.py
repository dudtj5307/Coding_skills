def div(n):
    i = 0
    while True:
        if n / 2 <= 1:
            return i
        n /= 2
        i += 1

def solution(arr):
    if len(arr) == 1:
        return arr
    for _ in range(2**(div(len(arr))+1) - len(arr)):
        arr.append(0)
    return arr
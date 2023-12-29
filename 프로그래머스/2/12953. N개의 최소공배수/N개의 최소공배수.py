def GCD(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def solution(arr):
    a = arr[0]
    for i in range(1, len(arr)):
        gcd = GCD(a, arr[i])
        a = a * arr[i] // gcd
    return a
def solution(A, B):
    for i in range(len(A)):
        A = A[-1] + A[:-1]
        if A == B: return (i + 1) % len(A)
    return -1
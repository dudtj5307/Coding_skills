from collections import deque

def solution(A, B):
    A, B = sorted(A), deque(sorted(B))
    answer = 0
    for i in range(len(A)):
        while A[i] >= B[0]:
            B.popleft()
            if len(B) == 0: return answer
        B.popleft()
        answer += 1
        if len(B) == 0: return answer
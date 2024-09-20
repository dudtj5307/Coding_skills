import sys
input = sys.stdin.readline
N, S = map(int, input().split())
array = list(map(int, input().split()))

end, total = 0, 0
answer = float('inf')

for start in range(N):
    while total < S and end < N:
        total += array[end]
        end += 1
    if total >= S:
        answer = min(answer, end-start)
    total -= array[start]
if answer == float('inf'): answer = 0
print(answer)
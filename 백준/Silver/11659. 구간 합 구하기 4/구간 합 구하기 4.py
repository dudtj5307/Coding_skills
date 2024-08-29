import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = [0] + list(map(int, input().split()))
for i in range(1,N):
    nums[i+1] += nums[i]

for _ in range(M):
    si, ei = map(int, input().split())
    print(nums[ei]-nums[si-1])
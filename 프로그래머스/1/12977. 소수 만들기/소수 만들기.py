from itertools import combinations
from collections import defaultdict

prime = defaultdict(int)
for i in range(1, 3001):
    for j in range(i, 3001, i):
        prime[j] += 1
        
def solution(nums):
    s_sum = [sum(n) for n in combinations(nums, 3)]
    return sum([1 for s in s_sum if prime[s] == 2])
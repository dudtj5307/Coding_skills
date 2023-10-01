from itertools import permutations

def is_prime(num):
    if num <= 1: return False
    for n in range(2, num):
        if num % n == 0: return False
    return True

def solution(numbers):
    num_list = []
    for i in range(1, len(numbers)+1):
        num_list.extend(list(permutations(numbers, i)))
    num_set = set(map(lambda x: int(''.join(x)), num_list))
    answer = 0
    for num in num_set:
        if is_prime(num):
            answer += 1
    return answer
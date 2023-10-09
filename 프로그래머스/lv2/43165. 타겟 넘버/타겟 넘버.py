from itertools import product

def solution(numbers, target):
    return list(map(sum, (product(*[(-x, x) for x in numbers])))).count(target)
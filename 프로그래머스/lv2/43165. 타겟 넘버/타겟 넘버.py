from itertools import permutations

def solution(numbers, target):
    case = [[1], [-1]]
    for i in range(1, len(numbers)):
        temp = []
        for c in case:
            temp.extend([c + [1], c + [-1]])
        case = temp
    answer = 0
    for c in case:
        if sum([numbers[i] * c[i] for i in range(len(numbers))]) == target:
            answer += 1
    return answer
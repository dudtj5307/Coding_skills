def solution(numbers):
    s = set()
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                s.add(numbers[i]+numbers[j])
    return sorted(list(s))
def solution(citations):
    answer = 0
    print(sorted(citations, reverse=True))
    for i, c in enumerate(sorted(citations, reverse=True)):
        if c >= i + 1: answer += 1
    return answer
def solution(n, m, section):
    answer = 1
    for i in range(len(section)):
        if i == 0: r = section[i] + m
        else:
            if section[i] >= r:
                answer += 1
                r = section[i] + m
    return answer
            
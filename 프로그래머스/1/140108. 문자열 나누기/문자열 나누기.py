def solution(s):
    x = "0"
    a, b = 0, 0
    answer = 0
    for i in range(len(s)):
        if x == "0":
            x = s[i]
        if s[i] == x: a += 1
        else: b += 1
        if a == b:
            answer += 1
            a, b, x = 0, 0, "0"
    if x != "0":
        answer += 1
    return answer
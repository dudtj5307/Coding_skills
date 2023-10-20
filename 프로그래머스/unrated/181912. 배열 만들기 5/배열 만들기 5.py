def solution(intStrs, k, s, l):
    answer = []
    for intS in intStrs:
        snum = intS[s:s+l]
        if snum and int(snum) > k:
            answer.append(int(snum))
    return answer
def counter(s, si, ei):
    cnt = 0
    while 0 <= si < len(s) and 0 <= ei < len(s):
        if s[si] == s[ei]: cnt += 1
        else: break
        si, ei = si - 1, ei + 1
    return cnt

def solution(s):
    answer = 0
    for i in range(0, len(s)):
        answer = max(answer, counter(s, i-1, i+1)*2 + 1)
        answer = max(answer, counter(s, i, i+1)*2)
    return answer
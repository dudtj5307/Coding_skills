def decide(word):
    q = []
    for w in word:
        if not q:
            if w in ["(", "[", "{"]: q.append(w)
            else: return 0
        else:
            if w in ["(", "[", "{"]: q.append(w)
            elif w == ")" and q[-1] == "(": del q[-1]
            elif w == "}" and q[-1] == "{": del q[-1]
            elif w == "]" and q[-1] == "[": del q[-1]
            else: return 0
    if q: return 0
    else: return 1

def solution(s):
    answer = 0
    for i in range(len(s)):
        answer += decide(s)
        s = s[1:] + s[0]
    return answer
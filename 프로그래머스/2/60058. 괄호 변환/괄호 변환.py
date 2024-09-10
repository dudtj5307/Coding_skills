def balanceString(s):
    left, right = 0, 0
    for i in range(len(s)):
        if s[i] == "(": left += 1
        else: right += 1
        if left == right:
            return s[:i+1], s[i+1:]

def isCorrect(s):
    left, right = 0, 0
    for i in range(len(s)):
        if s[i] == "(": left += 1
        else: right += 1
        if left < right:
            return False
    return True

def solution(p):
    if p == "": return ""
    u, v = balanceString(p) # 균형잡힌 괄호 문자열
    if isCorrect(u):        # 올바른 괄호 문자열
        return u + solution(v)
    else:
        return "(" + solution(v) + ")" + ''.join('(' if char==')' else ')' for char in u[1:-1])
        
    
    
        
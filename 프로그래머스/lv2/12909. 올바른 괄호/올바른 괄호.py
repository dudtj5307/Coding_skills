def solution(string):
    if string[0] == ')': return False
    if string[-1] == '(': return False
    l, r = 1, 0
    for s in string[1:]:
        if s == '(': l += 1
        else: r += 1
        if l < r: return False
    if l != r: return False
    return True
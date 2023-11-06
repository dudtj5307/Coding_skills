def solution(myString, pat):
    return 1 if pat in ''.join(['A' if s == 'B' else 'B' for s in myString]) else 0
    
def solution(s):
    if len(s) == 4 or len(s) == 6:
        for s_ in s:
            if s_.isalpha():
                return False
        return True
    else:
        return False
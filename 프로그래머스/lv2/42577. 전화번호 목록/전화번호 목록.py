def solution(phone_book):
    s = sorted(phone_book)
    for i in range(len(s)-1):
        l = min(len(s[i]), len(s[i+1]))
        if s[i][:l] == s[i+1][:l]:
            return False
    return True
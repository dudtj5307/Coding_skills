def solution(s, n):
    answer = ""
    for s_ in s:
        if s_.isalpha():
            o = ord(s_)
            new_o = o + n
            if o <= 90: answer += chr(new_o - 26 * (new_o//91))
            else: answer += chr(new_o - 26 * (new_o//123))
        else:
            answer += s_
    return answer
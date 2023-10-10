def solution(my_string):
    answer = []
    for s in my_string:
        if ord(s) < 97:
            answer.append(chr(ord(s) + 32))
        else:
            answer.append(s)
    return ''.join(sorted(answer))
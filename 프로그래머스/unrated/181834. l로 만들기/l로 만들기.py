def solution(myString):
    return ''.join([s if ord(s) > ord("l") else "l" for s in myString ])
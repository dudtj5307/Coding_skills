def solution(myString, pat):
    return sum([1 if myString[i:i+len(pat)] == pat else 0 for i in range(len(myString)-len(pat)+1)])
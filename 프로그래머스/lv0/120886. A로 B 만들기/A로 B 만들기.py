from collections import Counter

def solution(before, after):
    if Counter(before) == Counter(after):
        return 1
    return 0
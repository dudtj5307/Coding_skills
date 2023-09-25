from collections import Counter as cnt

def solution(participant, completion):
    return list((cnt(participant) - cnt(completion)).keys())[0]
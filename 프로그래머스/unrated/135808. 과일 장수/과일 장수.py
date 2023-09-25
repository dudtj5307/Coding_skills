import numpy as np

def solution(k, m, score):
    
    sum = 0
    score.sort(reverse=True)
    for i in range(len(score)):
        if (i+1) % m == 0:
            sum += score[i] * m
    
    return sum
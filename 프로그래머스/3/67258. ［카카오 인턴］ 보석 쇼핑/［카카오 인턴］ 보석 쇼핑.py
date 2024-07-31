from collections import defaultdict

def solution(gems):
    N = len(set(gems))
    ei = 0
    length = float('inf')
    d = defaultdict(int)
    for si, gem in enumerate(gems):
        while len(d) < N and ei < len(gems):
            d[gems[ei]] += 1
            ei += 1
        if len(d) == N and ei - si < length:
            answer = [si+1, ei]
            length = ei - si
        d[gem] -= 1
        if d[gem] == 0:
            del d[gem]
    return answer
        
                
                
            
        
        
    
            
            
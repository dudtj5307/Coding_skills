def solution(seq, k):
    
    L = len(seq)
    start, end = 0, 0
    p_sum = seq[0]
    result = []
    
    for start in range(L):
        while end + 1 < L and p_sum < k:
            end += 1
            p_sum += seq[end]
            
        if p_sum == k:
            if not result: result = [start, end]
            else: 
                if result[1] - result[0] > end - start: result = [start, end]
                
        p_sum -= seq[start]
    
    return result

            
                
                
                

            
    


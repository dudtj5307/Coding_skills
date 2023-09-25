def solution(food):
    half = ""
    for i, num in enumerate(food):
        half += str(i) * (num//2)
        
    return half+"0"+half[::-1]
    

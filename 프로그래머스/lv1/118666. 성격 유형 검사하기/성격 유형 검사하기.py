def solution(survey, choices):
    
    result = {"R":0, "T":0, "C":0, "F":0,
              "J":0, "M":0, "A":0, "N":0}
    
    for i, sur in enumerate(survey):
        
        choice = choices[i]
        
        if choice <=3:
            result[sur[0]] += 4 - choice
        elif choice >= 5:
            result[sur[1]] += choice - 4
    
    answer = ''
    if result["R"] >= result["T"]: answer += "R"
    else: answer += "T"
        
    if result["C"] >= result["F"]: answer += "C"
    else: answer += "F"
        
    if result["J"] >= result["M"]: answer += "J"
    else: answer += "M"
        
    if result["A"] >= result["N"]: answer += "A"
    else: answer += "N"
    
    return answer
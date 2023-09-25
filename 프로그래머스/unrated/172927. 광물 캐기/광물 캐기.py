def solution(picks, minerals):
    
    if sum(picks) * 5 < len(minerals): minerals = minerals[:sum(picks) * 5]
    ml, sl = [], []
    for m in minerals: ml += [1] if m=="stone" else [5] if m=="iron" else [25]
    for i in range(len(ml)//5): sl += [sum(ml[i*5:i*5+5])]
    sl += [sum(ml[5*i+5:])]

    answer = 0
    while ml and sl and picks != [0,0,0]:
        if picks[0]: picks[0] -= 1; p = 25
        elif picks[1]: picks[1] -= 1; p = 5
        else: picks[2] -= 1; p = 1
        
        idx = sl.index(max(sl)); del sl[idx]
        if idx == len(ml)//5:
            for mi in ml[idx*5:]: answer += mi // p or 1
            
            del ml[idx*5:]; continue
        
        for mi in ml[idx*5:idx*5+5]: answer += mi // p or 1
        print(mi, p, answer)
        del ml[idx*5:idx*5+5]
        
    return answer
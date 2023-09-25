def solution(keymap, targets):
    
    k_dict = {}
    for key in keymap:
        for i, k in enumerate(list(key)):
            k_dict[k] = min(i + 1, k_dict[k]) if k in k_dict.keys() else i+1
            
            
            
            # if k not in k_dict.keys():
            #     k_dict[k] = i + 1
            # else: k_dict[k] = min(i + 1, k_dict[k])
    
    answer = []
    for target in targets:
        sum = 0
        for t in target:
            if t not in k_dict.keys():
                sum = -1
                break
            sum += k_dict[t]
        answer.append(sum)
    
    return answer
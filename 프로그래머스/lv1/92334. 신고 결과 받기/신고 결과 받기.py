def solution(id_list, report, k):
    
    r_dict = {id_:[] for id_ in id_list}
    
    for rep in report:
        rep_from, rep_to = rep.split(" ")
        if rep_from not in r_dict[rep_to]:
            r_dict[rep_to] += [rep_from]
    
    
    id_dict = {id_:0 for id_ in id_list}
    
    for i, count in enumerate(r_dict.values()):
        if len(count) >= k:
            for c in count:
                id_dict[c] += 1
    
    return list(id_dict.values())
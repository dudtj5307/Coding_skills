def delay(pcs, t_dict, delay_time):
    if pcs:
        for p in pcs:
            t_dict[p] += delay_time
    return t_dict
        

def solution(plans):
    
    s_list, n_dict, t_dict = [], {}, {}
    for name, start, time in plans:
        start = int(start.split(":")[0])*60 + int(start.split(":")[1])
        s_list.append(start)
        n_dict[start] = name
        t_dict[start] = int(time)
        
    pcs, done = [], []
    for s in sorted(s_list):
        time = t_dict[s]
        
        if not pcs: pcs.append(s);
        else:
            if s < pcs[-1] + t_dict[pcs[-1]]: 
                t_dict = delay(pcs, t_dict, t_dict[s])
                pcs.append(s);
                
            else:
                while(pcs):
                    if pcs[-1] + t_dict[pcs[-1]] <= s:
                        done.append(pcs[-1]); del pcs[-1]
                    else: break
                    
                t_dict = delay(pcs, t_dict, t_dict[s])
                pcs.append(s); print("case3",pcs,done)
                        
    return [n_dict[d] for d in done] + [n_dict[p] for p in reversed(pcs)]
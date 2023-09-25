def solution(park, routes):
    
    # Find Starting position
    one_line = ""    
    for col in park: one_line += col
    s_i, s_j = one_line.index("S") // len(col), one_line.index("S") % len(col)
    
    park_sep = [list(col) for col in park]
    
    w_dict = {"E":[0,1], "W":[0,-1], "S":[1,0], "N":[-1,0]}
    
    for r in routes:
        w, n = r.split(" ")
        n = int(n)
        wi, wj = w_dict[w]
        if not (0<=s_i+wi*n<len(park_sep)) & (0<=s_j+wj*n<len(park_sep[0])): continue
        
        print(s_i, s_j)
        for i in range(n):
            if park_sep[s_i+wi*(i+1)][s_j+wj*(i+1)] == "X" :                
                n = 0
                break
        
        s_i, s_j = s_i+wi*n, s_j+wj*n
    
    return [s_i, s_j]
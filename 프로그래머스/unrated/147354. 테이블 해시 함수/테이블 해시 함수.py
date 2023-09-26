def solution(data, col, row_begin, row_end):
    data = sorted(data, key = lambda x:x[col-1])
    x, s, e = 0, 0, 0
    for i, d in enumerate(data):
        if d[col-1] != x:
            if s < e: data[s:e+1] = sorted(data[s:e+1], reverse=True)
            s = i
            x = d[col-1]
        else: e = i
    
    xor = 0
    for i in range(row_begin, row_end+1):
        xor2 = 0
        for d in data[i-1]: 
            xor2 += d % i
        xor = xor ^ xor2
    return xor
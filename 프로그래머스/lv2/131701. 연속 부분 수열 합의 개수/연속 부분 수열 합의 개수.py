def solution(elements):
    l = len(elements)
    elist = []
    for i in range(0, l):
        a = 0
        for j in range(i, i+l):
            a += elements[j%l]
            elist.append(a)
    return len(list(set(elist)))
        
        

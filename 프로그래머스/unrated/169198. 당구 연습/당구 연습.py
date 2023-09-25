def solution(m, n, sX, sY, balls):
    
    answer = []
    for b in balls:
        dist = []
        if sX != b[0]:
            dist += [(sX-b[0])**2 + (2*n-sY-b[1])**2]
            dist += [(sX-b[0])**2 + (sY+b[1])**2]
        elif sY > b[1]: dist += [(2*n-sY-b[1])**2]
        elif sY < b[1]: dist += [(sY+b[1])**2]
        
        if sY != b[1]:
            dist += [(sX+b[0])**2 + (sY-b[1])**2]
            dist += [(2*m-sX-b[0])**2 + (sY-b[1])**2]
        elif sX < b[0]: dist += [(sX+b[0])**2]
        elif sX > b[0]: dist += [(2*m-sX-b[0])**2]
        
        # for cx, cy in [[0,0],[m,0],[n,0],[m,n]]:
        #     if (cy-sY)/(cx-sX) == (cy-b[1])/(cx-b[0]):
        #         if [cx,cy]==[0,0] and sX<b[0]:
        #             wall += (sX+b[0])**2 + (2*m-
                

        answer += [min(dist)]
    return answer
def solution(arr):
    def sqz(i1,i2,j1,j2):
        if i2 - i1 == 1 or all(arr[i][j] == arr[i1][j1] for i in range(i1,i2) for j in range(j1,j2)):
            answer[arr[i1][j1]] += 1
            pass
        else:
            im, jm = (i1+i2) // 2, (j1+j2) // 2
            sqz(i1,im,j1,jm); sqz(i1,im,jm,j2); sqz(im,i2,j1,jm); sqz(im,i2,jm,j2); 
            
    answer = {0:0, 1:0}
    sqz(0,len(arr),0,len(arr))
    return [answer[0], answer[1]]
    
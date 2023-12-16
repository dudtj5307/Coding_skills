from collections import defaultdict
vector = {'U': (0,1), 'D': (0,-1), 'R': (1,0), 'L': (-1,0)}

def solution(dirs):
    dic = defaultdict(int)
    x, y = 0, 0
    for d in dirs:
        dx, dy = vector[d]
        nx, ny = x + dx, y + dy
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            dic[(x,y,nx,ny)] = 1
            dic[(nx,ny,x,y)] = 1
            x, y = nx, ny
            
    return sum(dic.values()) / 2
            
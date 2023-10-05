def solution(dots):
    minx, miny, maxx, maxy = float('inf'), float('inf'), -float('inf'), -float('inf')
    for x, y in dots:
        print(x, y)
        if x >= maxx: maxx = x
        if x <= minx: minx = x
        if y >= maxy: maxy = y
        if y <= miny: miny = y
    return (maxx - minx) * (maxy - miny)
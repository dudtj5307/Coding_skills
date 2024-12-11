def possible(result):
    COL, BOW = 0, 1
    for x, y, a in result:
        if a == COL and y != 0 and (x,y-1,COL) not in result \
        and (x-1,y,BOW) not in result and (x,y,BOW) not in result:
            return False
        if a == BOW and (x,y-1,COL) not in result and (x+1,y-1,COL) not in result \
        and not ((x-1,y,BOW) in result and (x+1,y,BOW) in result):
            return False
    return True

def solution(n, build_frame):
    result = set()
    for x, y, a, install in build_frame:
        item = (x, y, a)
        if install:
            result.add(item)
            if not possible(result):
                result.remove(item)
        else:
            result.remove(item)
            if not possible(result):
                result.add(item)

    return sorted(map(list, result), key=lambda x:(x[0],x[1],x[2]))
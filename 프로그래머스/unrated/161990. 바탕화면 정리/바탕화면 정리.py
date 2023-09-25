def solution(wallpaper):
    h, w = len(wallpaper), len(wallpaper[0])
    l = "NS"
    for i, wp in enumerate(wallpaper):
        for j, w in enumerate(list(wp)):
            if w == "#":
                if l=="NS": l, r, u, d = i, i, j,j
                else: l, r, u, d = min(i,l), max(i,r), min(j,u), max(j,d)
    return [l,u,r+1,d+1]
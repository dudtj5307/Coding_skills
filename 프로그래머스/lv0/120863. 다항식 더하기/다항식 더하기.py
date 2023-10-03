def solution(polynomial):
    
    p_list = polynomial.split(" + ")
    cnt_x, cnt_n = 0, 0
    for p in p_list:
        if p == "x": cnt_x += 1
        elif "x" in p: cnt_x += int(p[:-1])
        else: cnt_n += int(p)
    if cnt_x == 0:
        return f"{cnt_n}"
    elif cnt_x == 1 and cnt_n != 0:
        return f"x + {cnt_n}"
    elif cnt_x == 1 and cnt_n == 0:
        return f"x"
    elif cnt_n == 0:
        return f"{cnt_x}x"
    return f"{cnt_x}x + {cnt_n}"
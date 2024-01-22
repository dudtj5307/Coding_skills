_D = {0:"4", 1:"1", 2:"2"}
def tf(num):
    q, r = divmod(num, 3)
    if q == 0 and r != 0: return _D[r]        
    elif q == 0 and r == 0: return ""

    if q and num % 3 == 0:
        return tf(q-1) + _D[r]
    else:
        return tf(q) + _D[r]

def solution(n):
    return tf(n)
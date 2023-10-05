def solution(id_pw, db):
    for d in db:
        if d == id_pw: return "login"
        elif d[0] == id_pw[0]: return "wrong pw"
    return "fail"
    
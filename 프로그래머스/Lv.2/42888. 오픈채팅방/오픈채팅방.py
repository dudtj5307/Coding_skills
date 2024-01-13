from collections import defaultdict
d_act = {"Enter": "들어왔습니다.", "Leave": "나갔습니다."}

def solution(record):
    db = []
    dic = defaultdict(str)
    for r in record:
        act, uid = r.split()[:2]
        if act == "Enter":
            name = r.split()[-1]
            dic[uid] = name
            db.append([uid, act])
        elif act == "Leave":
            db.append([uid, act])
        else:
            rename = r.split()[-1]
            dic[uid] = rename
    answer = []
    for uid, act in db:
        if act != "Change":
            answer.append(f"{dic[uid]}님이 {d_act[act]}")
    return answer
        
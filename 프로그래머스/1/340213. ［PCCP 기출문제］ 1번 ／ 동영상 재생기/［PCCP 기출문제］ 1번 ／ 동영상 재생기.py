TO_SEC = lambda x: int(x[:2])*60 + int(x[3:])

def solution(video_len, pos, op_start, op_end, commands):
    video_len, pos, op_start, op_end = map(TO_SEC, [video_len, pos, op_start, op_end])
    if op_start <= pos <= op_end: pos = op_end
    for command in commands:
        if command == "prev":
            pos = max(pos-10, 0)
        else:
            pos = min(pos+10, video_len)
        if op_start <= pos <= op_end:
            pos = op_end
    pos_min, pos_sec = map(str, divmod(pos, 60))
    return pos_min.zfill(2)+":"+pos_sec.zfill(2)
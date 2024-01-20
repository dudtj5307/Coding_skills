def _T(M):
    return M.replace("A#","H").replace("C#","I").replace("D#","J").replace("F#","K").replace("G#","L")

def solution(m, musicinfos):
    m = _T(m)
    answer = []
    for s, e, title, sound in map(lambda x:x.split(","), musicinfos):
        sound = _T(sound)
        time = (int(e[:2])-int(s[:2])) * 60 + int(e[3:]) - int(s[3:])
        if m in sound * (time//len(sound)) + sound[:time%len(sound)]:
            answer.append([title, time])
    return "(None)" if answer==[] else sorted(answer, key=lambda x:(-x[1], answer.index(x)))[0][0]
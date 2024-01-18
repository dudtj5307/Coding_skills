def S(string, flag):
    for i in range(len(string)):
        if string[i].isnumeric():
            for j in range(i, len(string)):
                if not string[j].isnumeric():
                    break
            else: j += 1
            break
    return string[:i] if flag == 0 else string[i:j]  # flag: (0)Head/(1)Num

def solution(files):
    return sorted(files,key=lambda x:(S(x,0).lower(), int(S(x,1)[:5])))
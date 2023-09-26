def solution(name):
    if set(name) == {'A'}: return 0;
    answer = float('inf')
    for i in range(len(name)//2 + 1):
        r_l = name[i::-1] + name[i+1:][::-1]
        l_r = name[-i:] + name[:-i]
        for n in [r_l, l_r]:
            while n and n[-1] == 'A':
                n = n[:-1]
            cnt = [min(ord(c)-ord('A'), ord('Z')-ord(c)+1) for c in n]
            answer = min(answer, sum(cnt) + i  + len(n) - 1)
    return answer
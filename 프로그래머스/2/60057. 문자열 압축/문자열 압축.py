def solution(s):
    answer = len(s)
    for n in range(1, len(s)//2+1):  # 자르는 단위
        temp = s[:n]
        count, total = 0, len(s)
        for i in range(1, len(s)//n +1):
            next_s = s[i*n : (i+1)*n]
            if next_s == temp:
                count += 1
                total -= n
            else:
                if count > 0: total += len(str(count+1)) 
                temp = next_s
                count = 0
        answer = min(answer, total)
    return answer
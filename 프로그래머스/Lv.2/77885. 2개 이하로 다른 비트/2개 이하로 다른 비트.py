def solution(numbers):
    answer = []
    for num in numbers:
        b_num = bin(num)
        for i in range(len(b_num)-1,1,-1):
            if b_num[i] == "0":
                if i == len(b_num)-1: b_num = b_num[:i] + "1"
                else: b_num = b_num[:i] + "10" + b_num[i+2:]
                answer.append(int(b_num, 2))
                break
        else:
            b_num = b_num[:2] + "10" + b_num[3:]
            answer.append(int(b_num, 2))
    return answer
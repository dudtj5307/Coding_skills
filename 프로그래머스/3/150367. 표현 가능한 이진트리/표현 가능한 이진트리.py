def solution(numbers):
    def inspect(i, b_num):
        if numbers[i] and (m_idx := (len(b_num)//2)):
            if b_num[m_idx] == '0' and ('1' in b_num):
                numbers[i] = 0
            else:
                inspect(i, b_num[:m_idx]), inspect(i, b_num[m_idx+1:])
        
    for i, num in enumerate(numbers):
        b_num, numbers[i] = bin(num)[2:], 1
        j, tree = 1, 1
        while len(b_num) > tree:
            tree += 2 ** j
            j += 1
        b_num = b_num.rjust(tree, '0')
        inspect(i, b_num)
    return numbers
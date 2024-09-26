from itertools import permutations
OPERATOR = {'+': lambda x, y: x + y, '-': lambda x, y: x - y,'*': lambda x, y: x * y}

def solution(expression):
    num_list, op_list = [], []
    si = 0
    for i, e in enumerate(expression):
        if e in OPERATOR.keys():
            num_list.append(int(expression[si:i]))
            op_list.append(e)
            si = i + 1
    num_list.append(int(expression[si:]))

    answer = 0
    operations = [op for op in ['+', '-', '*'] if op in expression]
    for sequence in permutations(operations):
        nums, ops = [n for n in num_list], [o for o in op_list]
        for oper in sequence:
            while oper in ops:
                idx = ops.index(oper)
                nums[idx] = OPERATOR[oper](nums[idx], nums[idx+1])
                del nums[idx+1], ops[idx]
        answer = max(answer, abs(nums[0]))
    return answer
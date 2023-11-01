def to_one(num):
    i = 0
    while num != 1:
        if num % 2: num = (num - 1)//2
        else: num //= 2
        i += 1
    return i

def solution(num_list):
    return sum([to_one(n) for n in num_list])
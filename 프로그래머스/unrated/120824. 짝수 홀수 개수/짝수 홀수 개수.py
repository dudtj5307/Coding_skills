def solution(num_list):
    num_list = [n % 2 for n in num_list]
    return [num_list.count(0), num_list.count(1)]
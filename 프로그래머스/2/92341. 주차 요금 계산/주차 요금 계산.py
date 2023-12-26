from collections import defaultdict

def solution(fees, records):
    def_time, def_fee, u_time, u_fee = fees
    dic = {}
    answer = defaultdict(int)
    for record in records:
        t, car, status = record.split()
        h, m = map(int, t.split(':'))
        time = 60 * h + m
        if status == 'IN':
            dic[car] = time
        else:
            in_time = dic[car]
            del dic[car]
            if time - in_time <= def_time:
                answer[car] += def_fee
            else:
                answer[car] += def_fee + -(-(time - in_time - def_time) // u_time) * u_fee
                print(answer)
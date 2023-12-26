from collections import defaultdict

def solution(fees, records):
    def_time, def_fee, u_time, u_fee = fees
    dic = {}
    usage = defaultdict(int)
    for record in records:
        t, car, status = record.split()
        h, m = map(int, t.split(':'))
        time = 60 * h + m
        if status == 'IN':
            dic[car] = time
        else:
            in_time = dic[car]
            del dic[car]
            usage[car] += time - in_time
    end_time = 23 * 60 + 59
    for car, in_time in dic.items():
        usage[car] += end_time - in_time
    answer = []
    for car, use_time in sorted(usage.items(), key=lambda x:x[0]):
        if use_time <= def_time:
            answer.append(def_fee)
        else:
            answer.append(def_fee + -(-(use_time - def_time) // u_time) * u_fee)
    return answer
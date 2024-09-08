def solution(wallet, bill):
    answer = 0
    while (bill[0] > wallet[0] or bill[1] > wallet[1]) and (bill[1] > wallet[0] or bill[0] > wallet[1]):
        bill_max, bill_min = max(bill), min(bill)
        bill = [bill_max//2, bill_min]
        answer += 1
    return answer
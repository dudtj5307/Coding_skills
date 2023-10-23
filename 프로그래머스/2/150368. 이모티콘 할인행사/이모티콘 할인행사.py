from itertools import product

def solution(users, emoticons):
    def plus_sale(rates):
        plus, sales = 0, 0
        for u_rate, u_price in users:
            us = 0
            for rate, price in zip(rates, emoticons):
                if rate >= u_rate:
                    us += price / 100 * (100 - rate)
            if us >= u_price: plus += 1
            else: sales += us
        return [plus, sales]

    answer = []
    for rates in list(product([10, 20, 30, 40], repeat=len(emoticons))):
        answer.append(plus_sale(rates))
    return sorted(answer, key=lambda x:(-x[0],-x[1]))[0]
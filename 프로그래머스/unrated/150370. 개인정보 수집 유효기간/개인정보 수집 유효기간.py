    
# m_list = [i for i in range(1,13)]
# d_list = [j for j in range(1,29)]

def solution(today, terms, privacies):
    
    term_dict = {t[0]:int(t[2:]) for t in terms}
    
    answer = []
    for i, privacy in enumerate(privacies):
        date, topic = privacy.split(' ')
        y, m, d = map(int, date.split('.'))
        
        expire = y*12*28 + m*28 + d + term_dict[topic] * 28
                
        t_y, t_m, t_d = map(int, today.split('.'))
        if t_y * 12 * 28 + t_m * 28 + t_d >= expire:
            answer.append(i+1)

    return answer
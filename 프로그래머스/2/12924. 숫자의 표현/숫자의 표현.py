def solution(n):
    answer = 0
    for i in range(1, n+1):
        if (n - i*(i-1)//2) % i == 0:
            if i*(i-1)//2 >= n:
                break
            answer += 1
    return answer
            
        
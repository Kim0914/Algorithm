def solution(n):
    fibo = [0] * 100001
    fibo[1] = 1
    
    
    for i in range(2, 100001):
        fibo[i] = fibo[i-1] + fibo[i-2]
    
    
    answer = fibo[n] % 1234567
    return answer
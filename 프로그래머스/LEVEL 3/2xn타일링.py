def solution(n):
    answer = 0
    
    res = [0]
    for i in range(1, n+1):
        if i == 1:
            res.append(1)
        
        elif i == 2:
            res.append(2)
        
        else:
            res.append((res[i-1] + res[i-2]) % 1000000007)
    
    answer = res[-1]
    return answer
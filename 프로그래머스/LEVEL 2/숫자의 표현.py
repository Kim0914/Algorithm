def solution(n):
    answer = 0
    for i in range(1,n+1):
        res = []
        for j in range(i,n+1):
            res.append(j)
            
            if sum(res) == n:
                answer += 1
                break

            if sum(res) > n:
                break
    
    return answer

print(solution(15))
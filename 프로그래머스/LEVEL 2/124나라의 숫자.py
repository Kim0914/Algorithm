def solution(n):
    nums = ['4', '1', '2']
    s = ''
    answer = 0
    while True:
        q = n // 3
        r = n % 3
        
        if r == 0:
            q = q - 1
            
        s = s + nums[r]
        
        n = q
        if q == 0:
            break
    
    answer = s[::-1]
    return answer
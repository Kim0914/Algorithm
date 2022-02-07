def solution(numbers):
    answer = []
    
    for num in numbers:
        bin_num = list(bin(num)[2:])
        
        bin_num.insert(0,'0')
        
        ind = 0
        N = len(bin_num)
        for i in range(N):
            if  bin_num[i] == '0':
                ind = i
        
        if ind == N-1: # 가장 마지막 원소가 1인 경우
            bin_num[ind] = '1'
            
        else:
            bin_num[ind] = '1'
            bin_num[ind+1] = '0'
        
        
        # 제곱근 계산
        j = 0
        res = 0
        for i in range(N-1, -1, -1):
            if bin_num[i] == '1':
                res += 2**j
            j+=1
        answer.append(res)
        
    return answer
                

# def solution(numbers):
#     answer = []
    
#     for num in numbers:
#         if num % 2 == 0:
#             answer.append(num+1)
#             continue

#         bin_num = list(bin(num)[2:])
    
#         while True:
#             num += 1
#             cmp_num = list(bin(num)[2:])

#             N = len(cmp_num)

#             if len(bin_num) != N:       # 자리 수 맞추기
#                 diff = N - len(bin_num)
#                 for _ in range(diff):
#                     bin_num.insert(0, '0')

#             cnt = 0
#             for i in range(N-1, -1, -1):
#                 if bin_num[i] != cmp_num[i]:
#                     cnt += 1

#             if cnt <= 2 and cnt != 0:
#                 answer.append(num)
#                 break
            
#     return answer
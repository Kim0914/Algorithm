def solution(s):
    result = []
    N = len(s)
    if N == 1:
        return 1

    for i in range(1, (N//2) + 1):
        cmp = s[:i]
        res = ''
        cnt = 1

        for j in range(i, N, i):
            if cmp == s[j: j+i]: # 패턴이 같은 경우
                cnt += 1


            else: # 다른 패턴을 찾은 경우
                if cnt == 1:
                    res = res + cmp
                
                else:
                    res = res + str(cnt) + cmp
                
                cmp = s[j: j+i]
                cnt = 1
        

        if cnt == 1:
            res = res + cmp
        
        else:
            res = res + str(cnt) + cmp
            
        result.append(res)
    

    len_list = []
    for data in result:
        len_list.append(len(data))
        
    answer = min(len_list)
    return answer

print(solution('aabbaccc'))


'''
"aabbaccc"	7
"ababcdcdababcdcd"	9
"abcabcdede"	8
"abcabcabcabcdededededede"	14
"xababcdcdababcdcd"	17

'''
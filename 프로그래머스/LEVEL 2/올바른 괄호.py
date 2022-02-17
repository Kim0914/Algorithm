def check(li):
    stack = []

    for data in li:
        if data == '(': # 여는 괄호인 경우
            stack.append(data)

        else: # 닫는 괄호인 경우
            if len(stack) == 0:
                return False
            stack.pop()
            
    
    if len(stack) == 0:
        return True
    
    else:
        return False
            
        

def solution(s):
    answer = check(s)
    return answer


print(solution("(()("))
    

def check(li):
    stack = []

    for c in li:
        if c == '(' or c == '{' or c == '[': # 여는 괄호인 경우 스택에 넣음
            stack.append(c)
             
        else:
            if len(stack) == 0:
                return False

            compare_c = stack.pop()

            if c == ']' and compare_c != '[':
                return False

            elif c == ')' and compare_c != '(':
                return False

            elif c == '}' and compare_c != '{':
                return False
                
    return True

def solution(s):
    answer = 0
    if len(s) % 2 == 1:
        return answer
    
    li = s
    
    li = list(li)
    
    if check(li):
        answer += 1
    
    for _ in range(len(li) - 1):
        word = li.pop(0)
        li.append(word)
        
        if check(li):
            answer += 1
    return answer

print(solution(s))
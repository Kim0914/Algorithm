def check(st):
    stack = []
    N = len(st)
    for i in range(N):
        if st[i] == '(':
            stack.append(st[i])
        else:
            if len(stack) == 0:
                return False
            stack.pop(0)
            
    if len(stack) == 0:
        return True
    else:
        return False

def solution(p):
    answer = ''
    
    if check(p):
        answer = p
        return answer
    
    return answer
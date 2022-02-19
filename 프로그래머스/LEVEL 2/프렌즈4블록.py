def check(i,j, board):
    c = board[i][j]
    
    if  c == board[i][j+1] and c == board[i+1][j] and c == board[i+1][j+1]:
        return True
    else:
        return False    

def solution(m, n, board):
    answer = 0
    flag = True
        
    checked = [['X'] * n for _ in range(m)]
    
    # 전처리
    for i in range(len(board)):
        board[i] = list(board[i])

    # 같은 캐릭터 체크
    for i in range(m-1):
        for j in range(n-1):
            if check(i,j,board):
                checked[i][j] = 'O'
                checked[i+1][j] = 'O' 
                checked[i][j+1] = 'O' 
                checked[i+1][j+1] = 'O'
                  
    # 같은 캐릭터 제거
    tmp = []
    for j in range(n):
        c_str = ''
        for i in range(m):
            if checked[i][j] == 'X':
                c_str += board[i][j]
                
        while len(c_str) < n:
            c_str += 'X'
        tmp.append(c_str)
    
    
    print(tmp)
    return answer
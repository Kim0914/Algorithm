import sys

def find_number(n,m):
    nums = [1,2,3,4,5,6,7,8,9]
    for i in range(9): # 가로 행 먼저 검사
        if sdoku[n][i] in nums:
            nums.remove(sdoku[n][i])
    
    for j in range(9): # 세로 열 검사
        if sdoku[j][m] in nums:
            nums.remove(sdoku[j][m])

    # 0이 있는 좌표의 행, 열을 순회하며 이미 사용된 숫자를 제거 후 3x3 검사
    # 예를 들어 (5,2)가 0인 경우, (5,2)가 속한 3x3 그룹의 시작점인 (3.0) 부터 시작해야 한다
    # x 좌표가 0~2 => 0, 3~5 => 3, 6~8 => 6
    # y 좌표가 0~2 => 0, 3~5 => 3, 6~8 => 6
    x_cor = (n // 3) * 3
    y_cor = (m // 3) * 3
    

    for i in range(x_cor, x_cor+3):
        for j in range(y_cor, y_cor+3):
            if sdoku[i][j] in nums:
                nums.remove(sdoku[i][j])
    # 행, 열, 3x3 까지 검사하여 0 자리에 가능한 숫자 list인 nums 반환
    return nums

def dfs(index):
    global answer_flag
    if answer_flag == True:
        return
    
    if index == len(zero_point):
        for line in sdoku: # zero_point를 모두 체크한 경우 출력
            print(*line)
        answer_flag = True
        return
    
    print('index : ', end ='')
    print(index)
    i, j = zero_point[index] # 스도쿠에서 0인 좌표를 하나씩 가져온다
    able_nums = find_number(i,j) # 행, 열, 3x3을 검사해서 가능한 숫자 후보 리스트
    for num in able_nums: 
        sdoku[i][j] = num # 일단 가능한 숫자 중에 하나를 넣음
        dfs(index + 1) # 다음 빈칸(0) 체크
        sdoku[i][j] = 0 # 원래 상태로 돌려놓기

sdoku = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
zero_point = [(i,j) for i in range(9) for j in range(9) if sdoku[i][j] == 0]
answer_flag = False
print('-----------------------------')
dfs(0)
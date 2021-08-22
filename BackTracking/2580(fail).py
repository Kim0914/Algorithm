def check(row, col):
    check_line = []
    zero_flag = 0
    for i in range(row, row+3):
        for j in range(col, col+3):
            check_line.append(sdoku[i][j])
            if sdoku[i][j] == 0:
                zero_flag += 1
                if zero_flag == 1:
                    row_ind, col_ind = i, j
    if zero_flag == 1:
        elem = list(set(nums) - set(check_line))
        sdoku[row_ind][col_ind] = elem.pop()
    else:
        return
            

sdoku = []
nums = [1,2,3,4,5,6,7,8,9]

for _ in range(9): # 스도쿠 입력 받기 & 가로 한줄 검사
    one_line = list(map(int, input().split()))
    zero_flag = 0
    for i in range(len(one_line)):
        if one_line[i] == 0:
            zero_flag += 1
    if zero_flag == 1: # 입력받은 스토쿠 한줄에서 0이 하나만 있는 경우
        zero_index = one_line.index(0) # 0이 있는 자리의 인덱스를 찾고
        elem = list(set(nums) - set(one_line)) # 필요한 한개의 수를 elem에 가져온 뒤
        one_line[zero_index] = elem.pop() # 0을 elem으로 바꾼다
        sdoku.append(one_line)
    
    else:
        sdoku.append(one_line)

for i in range(9): # 세로로 검사
    zero_flag = 0
    col_line = []
    for j in range(9):
        if sdoku[j][i] == 0:
            zero_flag += 1
            if zero_flag == 1:
                row_ind, col_ind = j, i
        col_line.append(sdoku[j][i]) # 세로로 한줄을 담는 col_line

    if zero_flag == 1:
        elem = list(set(nums) - set(col_line))
        sdoku[row_ind][col_ind] = elem.pop()

for i in range(0,9,3): # 3 x 3 검사
    for j in range(0,9,3):
        check(i,j)

print('-------------------------------------------------')
for i in range(9):
    for j in range(9):
        print(sdoku[i][j], end = ' ')
    print()

'''
모든 경우의 수를 만족시키지 못함
주어진 testcase만을 통과하는 코드
가로 -> 세로 -> 3x3 검사하는 로직은 맞지만, 생각해야할 부분이 훨씬 많음
'''
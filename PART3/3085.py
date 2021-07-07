def count(mat):
    n = len(mat)
    ret = 0

    for i in range(n): # 행 기준 연속된 문자 검사
        cnt = 1
        for j in range(n-1):
            if mat[i][j] == mat[i][j+1]:
                cnt += 1
            else:
                cnt = 1

            if cnt > ret:
                ret = cnt

    for i in range(n): # 열 기준 연속된 문자 검사
        cnt = 1
        for j in range(n-1):
            if mat[j][i] == mat[j+1][i]:
                cnt += 1
            else:
                cnt = 1

            if cnt > ret:
                ret = cnt

    return ret


n = int(input())
mat = []
result = 1

for i in range(n):
    candy = input()
    list_candy = list(candy)
    mat.append(list_candy)

for i in range(n):
    for j in range(n-1):
        # 행 기준으로 인접한 두 값 변경
        mat[i][j], mat[i][j+1] = mat[i][j+1], mat[i][j]
        tmp = count(mat)
        # 다시 행렬 원상 복귀
        mat[i][j], mat[i][j+1] = mat[i][j+1], mat[i][j]

        if(tmp > result):
            result = tmp

        # 열 기준으로 인접한 두 값 변경
        mat[j][i], mat[j+1][i] = mat[j+1][i], mat[i][j]
        tmp = count(mat)
        # 다시 행렬 원상 복귀
        mat[j][i], mat[j+1][i] = mat[j+1][i], mat[i][j]
        
        if(tmp > result):
            result = tmp

print(result)
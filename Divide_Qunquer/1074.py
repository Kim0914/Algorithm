def search(mat, row, col):
    global num, n
    for i in range(row,row+2):
        for j in range(col, col+2):
            mat[i][j] = num
            num += 1
    



n, r, c = map(int, input().split())
n = 2 << n

mat = [[0] * n for _ in range(n)]
num = 0

print(mat[r][c])
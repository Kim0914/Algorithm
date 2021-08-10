def check(row, col, N):
    global minus_cnt, zero_cnt, one_cnt
    val = paper[row][col]
    # 현재 종이의 색(val)과 다르면 9개로 분할하기
    for i in range(row, row+N):
        for j in range(col, col+N):
            if paper[i][j] != val:
                N = N // 3
                check(row, col, N) # 9개로 쪼개었을때 (첫번째)
                check(row, col + N , N) # 9개로 쪼개었을때 (두번째)
                check(row, col + (2 * N), N) # 9개로 쪼개었을때 (세번째)
                check(row + N , col, N) # 9개로 쪼개었을때 (네번째)
                check(row + N , col + N, N) # 9개로 쪼개었을때 (다섯번째)
                check(row + N , col + (2 * N), N) # 9개로 쪼개었을때 (여섯번째)
                check(row + (2 * N), col, N) # 9개로 쪼개었을때 (일곱번째)
                check(row + (2 * N), col + N, N) # 9개로 쪼개었을때 (여덟번째)
                check(row + (2 * N), col + (2 * N), N) # 9개로 쪼개었을때 (아홉번째)
                return
    # 현재 종이 색상에 따라 갯수 카운트
    if val == -1:
        minus_cnt += 1
    elif val == 0:
        zero_cnt += 1
    else:
        one_cnt += 1

N = int(input())

paper = [list(map(int, input().split())) for _ in range(N)]
minus_cnt, zero_cnt, one_cnt = 0, 0, 0

check(0,0,N)

print(minus_cnt)
print(zero_cnt)
print(one_cnt)          